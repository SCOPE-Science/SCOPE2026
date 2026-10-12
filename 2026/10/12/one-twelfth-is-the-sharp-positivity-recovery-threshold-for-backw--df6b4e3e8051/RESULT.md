# One twelfth is the sharp positivity-recovery threshold for backward Euler on the classical fourth-order compact heat operator

## Finding
Let \(S\) denote the unit shift on the infinite one-dimensional lattice and define
\[
W=\frac1{12}(S^{-1}+10I+S),
\qquad
D=S^{-1}-2I+S.
\]
The classical fourth-order compact second-derivative relation is
\[
W u_{xx}=h^{-2}D u.
\]
Applying backward Euler to the heat equation gives
\[
(W-\sigma D)u^{n+1}=Wu^n,
\qquad
\sigma=\frac{\Delta t}{h^2},
\]
so the one-step map is
\[
B_\sigma=(W-\sigma D)^{-1}W.
\]

The exact positivity set is
\[
\boxed{\ B_\sigma\ge0
\quad\Longleftrightarrow\quad
\sigma=0\ \text{or}\ \sigma\ge\frac1{12}\ }.
\]
Here \(B_\sigma\ge0\) means that every nonnegative lattice datum is sent to a nonnegative datum.

Thus backward Euler has a re-entrant positivity law for this compact spatial discretization. The zero step is the identity, every strictly positive step below \(1/12\) produces a negative response to a point mass, and positivity is recovered exactly at \(1/12\). Whenever it is positive, the step also preserves constants and therefore preserves the full data range.

The phenomenon is already visible on a four-point periodic grid. At
\[
\sigma=\frac1{100},
\]
the point-mass input \(e_0\) gives
\[
B_{1/100}e_0
=
\left(
\frac{13217}{13568},
\frac3{212},
-\frac{33}{13568},
\frac3{212}
\right)^{\mathsf T}.
\]
The negative third component is an exact counterexample to an unqualified pointwise maximum-principle assertion for this backward-Euler compact heat step.

## Assumptions and scope
The sharp if-and-only-if theorem is for the translation-invariant infinite lattice with the standard fourth-order compact relation
\[
\frac1{10}u''_{j-1}+u''_j+\frac1{10}u''_{j+1}
=
\frac65\frac{u_{j-1}-2u_j+u_{j+1}}{h^2}.
\]
Multiplying by \(5/6\) gives the equivalent \(W,D\) normalization used above.

The finite periodic example uses the same \(W\) and \(D\) matrices with wrap-around. It is included only as a direct finite counterexample; this finding does not classify the exact positivity threshold for every finite periodic grid size or for boundary closures.

The result concerns pointwise positivity of one backward-Euler step. Unconditional spectral stability, convergence order, weak monotonicity of weighted averages, and positivity after an added limiter are distinct properties.

## Proof
Put
\[
A_\sigma=W-\sigma D.
\]
Since
\[
D=S^{-1}-2I+S,
\]
one has
\[
A_\sigma
=
aI+b(S+S^{-1}),
\qquad
a=\frac56+2\sigma,
\qquad
b=\frac1{12}-\sigma.
\]

At \(\sigma=0\),
\[
B_0=W^{-1}W=I,
\]
so positivity is immediate.

Assume first
\[
\sigma\ge\frac1{12}.
\]
Then \(b\le0\). Moreover,
\[
a-2|b|
=
\frac56+2\sigma-2\left(\sigma-\frac1{12}\right)
=
1.
\]
Thus \(A_\sigma\) is a strictly diagonally dominant tridiagonal \(M\)-matrix on the lattice. Equivalently, for \(\sigma>1/12\) its Green kernel is a positive geometric sequence, while at \(\sigma=1/12\) one simply has \(A_\sigma=I\). Therefore
\[
A_\sigma^{-1}\ge0.
\]
Since \(W\ge0\) entrywise,
\[
B_\sigma=A_\sigma^{-1}W\ge0.
\]
Also
\[
W\mathbf1=\mathbf1,\qquad D\mathbf1=0,
\]
so
\[
B_\sigma\mathbf1=\mathbf1.
\]
Hence a positive step is also a Markov convolution and preserves the minimum and maximum of bounded data.

Now suppose
\[
0<\sigma<\frac1{12}.
\]
Then \(b>0\). The inverse of \(A_\sigma\) has the translation-invariant Green kernel
\[
g_j=C r^{|j|},
\]
where
\[
C=\frac1{\sqrt{a^2-4b^2}}>0,
\qquad
r=\frac{-a+\sqrt{a^2-4b^2}}{2b}.
\]
Since \(a>2b>0\), one has
\[
-1<r<0.
\]
For \(j\ge1\),
\[
(B_\sigma e_0)_j
=
\frac{g_{j-1}+10g_j+g_{j+1}}{12}
=
\frac{C r^{j-1}}{12}(1+10r+r^2).
\]
The characteristic equation is
\[
b(r^2+1)+ar=0.
\]
Therefore
\[
1+10r+r^2
=
r\left(10-\frac ab\right).
\]
Using the displayed \(a,b\),
\[
10-\frac ab
=
-\frac{144\sigma}{1-12\sigma},
\]
and hence
\[
1+10r+r^2
=
-\frac{144\sigma}{1-12\sigma}\,r>0.
\]
It follows that the sign of \((B_\sigma e_0)_j\) is the sign of \(r^{j-1}\). In particular,
\[
(B_\sigma e_0)_2
=
-\frac{12C\sigma r^2}{1-12\sigma}<0.
\]
So no strictly positive timestep below \(1/12\) is positivity preserving.

This proves the infinite-lattice classification.

For the four-point periodic witness, take the circulant matrices
\[
W=\frac1{12}
\begin{pmatrix}
10&1&0&1\\
1&10&1&0\\
0&1&10&1\\
1&0&1&10
\end{pmatrix},
\qquad
D=
\begin{pmatrix}
-2&1&0&1\\
1&-2&1&0\\
0&1&-2&1\\
1&0&1&-2
\end{pmatrix}.
\]
Exact rational inversion at \(\sigma=1/100\) yields the vector stated above, whose third entry is negative.

## Verification
The embedded `verify.py` uses exact rational arithmetic for the four-point periodic counterexample. It reconstructs \(W\), \(D\), \(A_\sigma=W-\sigma D\), inverts \(A_\sigma\) by fraction-preserving Gauss--Jordan elimination, and verifies
\[
B_{1/100}e_0
=
\left(
\frac{13217}{13568},
\frac3{212},
-\frac{33}{13568},
\frac3{212}
\right)^{\mathsf T}.
\]
It also verifies that these four entries sum to \(1\).

For several rational \(\sigma\) below \(1/12\), the verifier checks the algebraic identity
\[
10-\frac ab
=
-\frac{144\sigma}{1-12\sigma}
\]
and numerically evaluates the decaying characteristic root to confirm the predicted negative distance-two kernel coefficient. At and above \(1/12\), it checks the \(M\)-matrix sign pattern and the exact diagonal-dominance margin.

The universal theorem is the analytic Green-kernel argument in the proof; finite numerical checks are not used as an infinite-lattice proof.

## Relationship to prior work
Zhao, Dai, and Niu develop fourth-order compact schemes for the heat equation. Their interior relation is exactly the classical three-point compact second-derivative formula used here, and they prove solvability and unconditional stability for a Crank--Nicolson construction with Neumann boundary treatment. Stability does not imply pointwise positivity, and their paper does not give the backward-Euler positivity classification proved here.

Li, Xie, and Zhang study bound preservation for classical compact finite differences. In their periodic notation they define
\[
W_2=\frac1{12}(S^{-1}+10I+S)
\]
and the standard centered second-difference operator \(D_{xx}\), exactly matching the spatial operators used here. Their introduction states, without a timestep qualification or proof there, that backward Euler or Crank--Nicolson with the fourth-order compact method satisfies a maximum principle for the heat equation. The exact four-point periodic computation above shows that the pointwise backward-Euler statement cannot hold for all positive timesteps: at \(\sigma=1/100\) the same displayed operators produce a negative component. Their main explicit weak-monotonicity and limiter results are different statements and are not challenged by this calculation.

More generally, work on positivity-preserving implicit high-order methods has observed that a lower, rather than upper, timestep restriction can arise. The present result identifies the exact lower threshold for this classical compact heat operator and explains the mechanism through the sign change of the tridiagonal resolvent kernel.

The closest related positivity result located for a different heat discretization concerns backward-Euler filtering of Crank--Nicolson. Its operator and conclusion are different and do not imply the \(1/12\) compact-scheme threshold.

## Limitations
The sharp classification is for the infinite one-dimensional lattice. Finite periodic grids, Dirichlet or Neumann boundary closures, multidimensional tensor-product compact schemes, variable coefficients, nonlinear diffusion, and Crank--Nicolson are not classified here.

The finite four-point calculation proves that an unconditional pointwise maximum principle fails for the periodic version, but it does not identify every finite-size threshold.

The argument is exact-arithmetic analysis. Floating-point roundoff can perturb tiny negative coefficients close to \(\sigma=0\) or \(1/12\), although it does not change the mathematical sign law.

Residual originality risk remains that older compact-scheme or monotonicity literature may contain the same \(1/12\) threshold under an \(M\)-matrix, inverse-positivity, or lower-CFL formulation. Targeted searches using those aliases did not locate such a result.

## References
1. J. Zhao, W. Dai, and T. Niu, “Fourth-order compact schemes of a heat conduction problem with Neumann boundary conditions,” Numerical Methods for Partial Differential Equations 23 (2007), 949–959, DOI 10.1002/num.20200. First published online 2007-05-18; AMS classifications 65M06, 65M12.
2. H. Li, S. Xie, and X. Zhang, “A high order accurate bound-preserving compact finite difference scheme for scalar convection diffusion equations,” SIAM Journal on Numerical Analysis 56 (2018), 3308–3345, DOI 10.1137/18M1208551; public arXiv version 2310.16170.
3. T. Qin and C.-W. Shu, “Implicit Positivity-Preserving High-Order Discontinuous Galerkin Methods for Conservation Laws,” SIAM Journal on Scientific Computing, DOI 10.1137/17M112436X.
