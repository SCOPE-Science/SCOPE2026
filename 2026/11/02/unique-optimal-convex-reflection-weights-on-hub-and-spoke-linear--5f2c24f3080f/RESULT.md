# Unique optimal convex reflection weights on hub-and-spoke linear systems

## Finding

For every integer \(n\ge 2\) and every \(0<c<1\), put \(s=\sqrt{1-c^2}\), and consider the \(n\) unit vectors
\[
u_1=e_1,\qquad u_j=c e_1+s e_j\quad(2\le j\le n).
\]
For positive probabilities \(p_j\) summing to one, let
\[
M(p)=I-2\sum_{j=1}^n p_j u_j u_j^{\mathsf T},\qquad
\rho(p)=\|M(p)\|_2.
\]
Define \(D=n+(n-2)c\). **The unique minimizer** of \(\rho(p)\) over all such probabilities is
\[
\boxed{p_1^*=\frac{1+(n-2)c}{D},\qquad p_j^*=\frac1D\quad(2\le j\le n).}
\]
The sharp factor and spectral gap are
\[
\boxed{\rho_*=\frac{n-2+nc}{n+(n-2)c},\qquad 1-\rho_*=\frac{2(1-c)}{n+(n-2)c}.}
\]
For uniform probabilities \(p_j=1/n\), the exact gap instead equals
\[
1-\rho_{\mathrm{unif}}=
\frac{2+(n-2)c^2-c\sqrt{(n-2)^2c^2+4(n-1)}}n.
\]
For fixed \(c\in(0,1)\), as \(n\to\infty\),
\[
1-\rho_{\mathrm{unif}}\sim \frac{2(1-c^2)}{c^2 n^2},\qquad
1-\rho_*\sim\frac{2(1-c)}{(1+c)n},\qquad
\frac{1-\rho_*}{1-\rho_{\mathrm{unif}}}\sim\frac{c^2}{(1+c)^2}n.
\]
Thus the optimal positive reflection masses change a quadratic-in-dimension spectral-gap loss into a linear-in-dimension loss. For \(n=2\) the optimal masses are equal; for every \(n\ge3\) and \(c>0\), uniform masses are strictly suboptimal.

## Assumptions and scope

Work in real Euclidean space \(\mathbb R^n\). The \(u_j\) are the outward normals to affine hyperplanes \(H_j=\{x:\langle u_j,x\rangle=b_j\}\), with arbitrary real \(b_j\). Because their row matrix is nonsingular for \(s>0\), these hyperplanes have a unique intersection \(x_*\). The reflection in \(H_j\) is
\[
R_j(x)=x+2(b_j-\langle u_j,x\rangle)u_j.
\]
The method takes their simultaneous *convex centroid*, \(x^+=\sum_{j=1}^n p_jR_j(x)\), for fixed strictly positive \(p_j\) with \(\sum p_j=1\). Its exact error recursion is \(x^+-x_*=M(p)(x-x_*)\). The result optimizes the Euclidean worst-case single-step and asymptotic norm factor within this fixed convex-centroid family; weights or relaxation parameters not representing such probabilities are outside its optimization domain.

## Proof

**Step 1: Reduce the factor to the smallest positive eigenvalue.** Write
\[
B(p)=2\sum_{j=1}^n p_j u_j u_j^{\mathsf T}.
\]
The independent normals and positive masses make \(B(p)\) positive definite. Each normal has unit length, so \(\operatorname{tr}B(p)=2\). Let its extremal eigenvalues be \(0<\mu_{\min}\le\mu_{\max}<2\); for \(n=2\), the second inequality is still strict because the smaller eigenvalue is positive. The eigenvalues of \(M=I-B\) lie between \(1-\mu_{\max}\) and \(1-\mu_{\min}\). Since \(\mu_{\max}+\mu_{\min}\le\operatorname{tr} B=2\),
\[
\rho(p)=\max\{\mu_{\max}-1,1-\mu_{\min}\}=1-\mu_{\min}(B(p)).
\]
The equality for \(n=2\) is allowed. Therefore minimizing the step factor is precisely maximizing the least eigenvalue of \(B(p)\).

**Step 2: A common Rayleigh upper bound for every mass vector.** Let \(D=n+(n-2)c\) and take a unit vector \(q\) with
\[
q_1=\sqrt{\frac{1-c}{D}},\qquad q_j=-\frac{1+c}{s}q_1\quad(2\le j\le n).
\]
Indeed, \(\|q\|^2=q_1^2[1+(n-1)(1+c)^2/s^2]=q_1^2D/(1-c)=1\). The hub normal satisfies \(u_1^{\mathsf T}q=q_1\), while **each** spoke satisfies \(u_j^{\mathsf T}q=cq_1+sq_j=-q_1\). Consequently, for every admissible probability vector,
\[
q^{\mathsf T}B(p)q=2\sum_{j=1}^n p_j(u_j^{\mathsf T}q)^2
=2q_1^2=\frac{2(1-c)}D=:\mu_*.
\]
The min-max principle proves \(\mu_{\min}(B(p))\le\mu_*\) for **all** admissible masses, without any assumption of symmetry or stationarity of a candidate optimum.

**Step 3: Construct an optimizer and verify every eigenvalue.** Put \(r=1/D\), \(t=[1+(n-2)c]/D\) and take \(p^*=(t,r,\ldots,r)\). Direct substitution gives \(B(p^*)q=\mu_*q\). The subspace of vectors with first coordinate zero and remaining coordinates summing to zero is invariant with eigenvalue
\[
\mu_{\mathrm{spoke}}=2rs^2=\frac{2(1-c^2)}D
\]
of multiplicity \(n-2\), when \(n\ge3\). In the remaining two-dimensional invariant subspace, the other eigenvalue is, by the trace,
\[
\mu_{\mathrm{top}}=\frac{2(1+c)[1+(n-2)c]}D.
\]
For \(0<c<1\), \(\mu_*<\mu_{\mathrm{spoke}}\) and \(\mu_*<\mu_{\mathrm{top}}\); for \(n=2\), only the latter comparison is needed. Thus \(\mu_*\) is the least eigenvalue. The Rayleigh upper bound is attained, proving the sharp rate and gap.

**Step 4: Strict uniqueness without an implicit symmetry assumption.** Suppose another positive vector \(p\) achieves \(\mu_{\min}=\mu_*\). Equality in the Rayleigh bound from Step 2 forces the fixed vector \(q\) to lie in the least-eigenvalue eigenspace, so \(B(p)q=\mu_*q\). Looking at coordinates \(j\ge2\),
\[
-2s p_jq_1=-\mu_*\frac{1+c}{s}q_1.
\]
Since \(q_1,s>0\), this yields \(p_j=\mu_*(1+c)/(2s^2)=1/D\) for every spoke. The probability constraint then gives \(p_1=t\). Thus the global minimizer is unique.

**Step 5: Uniform weights and the asymptotic gap.** Let \(U\) be the square matrix whose rows are the normals. The nonzero spectra of \(U^{\mathsf T}U\) and \(UU^{\mathsf T}\) coincide. The row Gram matrix has a spoke-difference eigenspace with eigenvalue \(1-c^2\) and a two-dimensional block
\[
\begin{pmatrix}1&c\sqrt{n-1}\\c\sqrt{n-1}&1+(n-2)c^2\end{pmatrix}.
\]
The smaller block eigenvalue is
\[
\lambda_-=\frac{2+(n-2)c^2-c\sqrt{(n-2)^2c^2+4(n-1)}}2,
\]
strictly smaller than \(1-c^2\). Hence the uniform least eigenvalue is \(2\lambda_-/n\), giving the displayed uniform gap. The block determinant is \(1-c^2\), while its larger eigenvalue is asymptotic to \(nc^2\) for fixed \(c>0\). Therefore \(\lambda_-\sim(1-c^2)/(nc^2)\). Division by the explicit optimal gap proves the dimension-linear improvement.

## Verification

The accompanying standalone `check.py` reproduces exact symbolic matrix and eigenvector identities for \(n=2,\ldots,8\) and three rational trigonometric pairs, together with numerical spectral checks on additional dimensions and positive weights. Executing `python check.py` in an environment containing Python 3, SymPy and NumPy prints `VERIFY_OK 3159`. These checks establish reproducibility on their specified finite inputs; the quantified assertions for all integers and all \(0<c<1\) follow from the preceding proof, not the tests.

## Relationship to prior work

Cimmino's simultaneous reflection centroid is classical. Guida and Sbordone (2023) study its geometric error contraction and mention weighted centroids without solving the present hub-and-spoke probability optimization. Sharma (2026, arXiv:2605.24692v1) obtains sharp spectral criteria, two-row global unit-weight optimality, and a general fixed-weight scaling formula. Its Theorems 1 and 5 supply a broad spectral framework, but neither the general scaling identity nor its two-row analysis states the unique positive **shape** of the optimal \(n\)-row hub-and-spoke probability vector or the linear-versus-quadratic dimension-dependent spectral gaps. The result here uses those standard spectral principles and proves a new geometry-specific minimax inequality using a common dual Rayleigh direction; it does not claim discovery of the general principle of spectral weight optimization. General optimal-design and frame-scaling formulations are related but are not asserted to be new.

## Limitations

The result concerns fixed, exact-arithmetic, convex combinations of reflections from the specified nonsingular real hub-and-spoke family. It is not a theorem for arbitrary unit-normal frames, signed weights, nonlinear constraints, changing weights, stochastic sampling, floating-point stability, or optimal work per iteration. A numerical spectral gap is not itself a wall-clock speedup. Existing general E-optimal design theory may contain an equivalent specialization; priority of the exact explicit family and its asymptotic comparison remains subject to external scholarly checking.

## References

1. H. Sharma, *Sharp Convergence Rates and Optimal Weights for Cimmino's Reflection Algorithm*, arXiv:2605.24692v1 (2026-05-23), https://arxiv.org/abs/2605.24692.
2. M. Guida and C. Sbordone, *The Reflection Method for the Numerical Solution of Linear Systems*, SIAM Review **65** (2023), 1137–1151, https://doi.org/10.1137/22M1470463.
3. W. L. Martinez and E. J. Wegman, *An alternative criterion useful for finding exact E-optimal designs*, Statistics & Probability Letters **47** (2000), 325–328, https://doi.org/10.1016/S0167-7152(99)00173-X.
