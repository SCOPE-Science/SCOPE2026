# One third is the sharp positivity-recovery threshold for backward Euler on the classical fourth-order heat stencil
## Finding
On the infinite uniform one-dimensional lattice, let the classical fourth-order centered approximation of the second derivative be
\[
(L_4u)_j=\frac{-u_{j-2}+16u_{j-1}-30u_j+16u_{j+1}-u_{j+2}}{12h^2},
\qquad j\in\mathbb Z.
\]
For one backward Euler step for the heat equation, write
\[
u^{n+1}=(I-\Delta t L_4)^{-1}u^n,
\qquad r=\frac{\Delta t}{h^2}>0.
\]
Then the update is positivity preserving on bounded nonnegative lattice data if and only if
\[
\boxed{r\ge \frac13}.
\]
In fact, for \(r\ge1/3\) its convolution kernel is strictly positive at every lattice offset and has total mass one. Consequently every bounded datum satisfies the range principle
\[
\inf_j u^n_j\le u^{n+1}_j\le \sup_j u^n_j
\qquad\text{for every }j\in\mathbb Z.
\]
For every \(0<r<1/3\), the Green kernel has a negative coefficient. Hence a single nonnegative point mass produces a negative value after one backward Euler step.

The threshold is therefore a positivity-recovery threshold rather than the usual upper CFL restriction: making the implicit time step too small destroys positivity for this spatial stencil, while every sufficiently large backward Euler step restores it.

For example, at \(r=1/10\), the exact Green kernel is exponentially decaying but oscillatory; its coefficient at distance three is
\[
g_3=-1.78311524445\ldots\times10^{-4}<0.
\]
This numerical value is only a reproducible witness. The if-and-only-if threshold is proved analytically for every \(r>0\).

## Assumptions and scope
The lattice is \(\mathbb Z\), with no physical boundary. The claim concerns the standard five-point, fourth-order centered long stencil for the one-dimensional second derivative and one backward Euler time step. It is not a claim about compact fourth-order formulas, finite-element-derived fourth-order schemes, or boundary closures.

The inverse is understood as the bounded translation-invariant resolvent, equivalently convolution with the absolutely summable Green kernel. Positivity preservation means that nonnegative bounded input data give nonnegative output data coordinatewise.

No assertion is made here for finite Dirichlet intervals or for every periodic lattice size. Boundary modifications and periodization can change inverse signs.

## Proof
Let \(T\) be the bilateral shift and put
\[
X=T+T^{-1}.
\]
Since
\[
T^2+T^{-2}=X^2-2I,
\]
the dimensionless fourth-order Laplacian satisfies
\[
h^2L_4=\frac{-X^2+16X-28I}{12}.
\]
Thus the backward Euler matrix is
\[
A_r=I-rh^2L_4
=\frac r{12}\left(X^2-16X+28I+\frac{12}{r}I\right).
\]
Define
\[
s_\pm=8\pm\sqrt{36-\frac{12}{r}}.
\]
Then
\[
A_r=\frac r{12}(s_+I-X)(s_-I-X).
\]

Assume first that \(r\ge1/3\). Both \(s_+\) and \(s_-\) are real and at least \(2\); for finite \(r\), in fact \(s_->2\), except that at \(r=1/3\) the two factors coincide at \(s_+=s_-=8\). For every real \(s>2\), the inverse of \(sI-X\) has the strictly positive Green kernel
\[
K_s(k)=\frac{q_s^{|k|}}{\sqrt{s^2-4}},
\qquad
q_s=\frac{s-\sqrt{s^2-4}}2\in(0,1).
\]
Therefore, for \(r>1/3\),
\[
A_r^{-1}=\frac{12}{r}(s_+I-X)^{-1}(s_-I-X)^{-1}
\]
has kernel \((12/r)(K_{s_+}*K_{s_-})\), which is strictly positive. At \(r=1/3\), the kernel is \(36(K_8*K_8)\), again strictly positive. Since \(L_4\mathbf 1=0\), one has \(A_r\mathbf 1=\mathbf 1\); hence the positive kernel has mass one. Positivity and the range principle follow.

Now let \(0<r<1/3\). Write
\[
\eta=\sqrt{\frac{12}{r}-36}>0,
\qquad
s_+=8+i\eta,
\qquad
s_-=8-i\eta.
\]
For a complex \(s\notin[-2,2]\), let \(q(s)\) denote the root of
\[
q+q^{-1}=s
\]
that lies strictly inside the unit disk. The Green kernel of \((sI-X)^{-1}\) is a nonzero constant multiple of \(q(s)^{|k|}\). Because \(s_-\) is the conjugate of \(s_+\), the decaying characteristic roots are \(q\) and \(\overline q\), where \(q=\rho e^{i\theta}\) with \(0<\rho<1\) and \(\theta\notin\{0,\pi\}\).

Partial fractions in the two factors show that, for \(k\ge0\), the real Green kernel of \(A_r^{-1}\) has the form
\[
g_k=Cq^k+\overline C\,\overline q^{\,k}
=2|C|\rho^k\cos(k\theta+\phi),
\]
with \(C\ne0\). The coefficient cannot vanish because the relevant pole of the resolvent is simple.

It remains only to note that a nonconstant rotation cannot keep the cosine nonnegative forever. If \(\theta/(2\pi)\) is irrational, the phases are dense modulo \(2\pi\), so some cosine is negative. If \(\theta/(2\pi)\) is rational, the phases form a finite nontrivial orbit whose cosine values sum to zero over a full period; they cannot all be nonnegative unless they all vanish, which is impossible for a nontrivial orbit with \(\theta\notin\{0,\pi\}\). Hence some \(g_k<0\). Taking the input to be a unit point mass at the origin proves failure of positivity for every \(0<r<1/3\).

This proves the sharp threshold.

## Verification
The accompanying `verify.py` checks the shift-polynomial factorization exactly with rational arithmetic. It also evaluates the closed Green-kernel formula from the factorization and confirms a robust negative coefficient at \(r=1/10\), namely
\[
g_3=-1.78311524445\ldots\times10^{-4}.
\]
The computation is not used to infer the all-\(r\) result. The all-\(r\) necessity follows from the complex-root oscillation argument in the proof, and sufficiency follows from convolution of two strictly positive second-order resolvent kernels.

## Relationship to prior work
The five-point fourth-order centered derivative formula is classical. Fornberg gives systematic finite-difference weight generation and equispaced high-order formulas; the stencil itself is not claimed as new.

Inverse positivity and discrete maximum principles are also classical. Modern high-order maximum-principle work explicitly notes that ordinary higher-order schemes generally cease to be \(M\)-matrices and develops special fourth-order discretizations whose monotonicity follows from different factorizations. In particular, Shen and Zhang analyze a fourth-order finite-difference representation derived from \(Q^2\) spectral elements and obtain discrete maximum principles under mesh and time-step constraints; their inspected full text emphasizes that its time-step condition is a lower bound on \(\Delta t/\Delta x^2\). That operator is not the classical translation-invariant five-point stencil considered here.

Wang, Li, and Zhao derive explicit inverses for general pentadiagonal Toeplitz matrices by a tridiagonal factorization and Sherman--Morrison--Woodbury corrections. Their accessible abstract establishes prior art for such factorizations; it does not state the infinite-lattice positivity classification or the threshold \(r=1/3\). Full-text comparison was not available, so this remains an explicit originality risk.

The closest checked published-index result on lattice positivity concerns backward-Euler-filtered Crank--Nicolson for the standard heat lattice. It studies a different time-composition and spatial operator and does not imply the present threshold.

## Limitations
The theorem is deliberately confined to the infinite one-dimensional lattice. Finite interval boundary closures and finite periodic grids require separate analysis.

The result concerns one-step positivity and the range principle, not accuracy optimization. The regime \(r\ge1/3\) can be strongly diffusive, and positivity alone does not make it the preferred accuracy regime.

The main originality risk is that the same threshold could be implicit in older pentadiagonal Toeplitz inverse formulas or maximum-principle literature under different terminology. The checked sources did not state an implication-equivalent result.

## References
1. Bengt Fornberg, *Generation of finite difference formulas on arbitrarily spaced grids*, Mathematics of Computation 51 (1988), 699--706, DOI: 10.1090/S0025-5718-1988-0935077-0.
2. Chaojie Wang, Hongyi Li, and Di Zhao, *An explicit formula for the inverse of a pentadiagonal Toeplitz matrix*, Journal of Computational and Applied Mathematics 278 (2015), 12--18, DOI: 10.1016/j.cam.2014.08.010.
3. Jie Shen and Xiangxiong Zhang, *Discrete Maximum Principle of a High Order Finite Difference Scheme for a Generalized Allen--Cahn Equation*, arXiv:2104.11813.
