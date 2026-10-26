# Sharp two-point stability of sorting in finite-star Sobolev norms

## Finding

Let \(n\ge1\) be an integer and \(\gamma>0\). Regard the coordinate set \(\{0,1,\ldots,n\}\) as the vertices of the star with hub \(0\). Equip \(\mathbb R^{n+1}\) with the graph-Sobolev norm
\[
 \|x\|_{n,\gamma}^2=\sum_{i=0}^n x_i^2+\gamma\sum_{j=1}^n(x_0-x_j)^2.
\]
Let \(S(x)\) be the vector of the \(n+1\) coordinates of \(x\) sorted in nondecreasing order, so the smallest coordinate is assigned to vertex \(0\). Its *global two-point* Lipschitz modulus is exactly
\[
 \boxed{\operatorname{Lip}_{n,\gamma}(S)=
 \frac{\sqrt{4+\delta_{n,\gamma}}+\sqrt{\delta_{n,\gamma}}}{2},\qquad
 \delta_{n,\gamma}=\frac{\gamma^2(n^2-1)}{(1+\gamma)(1+(n+1)\gamma)}.}
\]
The value is \(1\) at \(n=1\), and strictly exceeds \(1\) for \(n\ge2\). This maximum is attained by an actual pair of different vectors in the interior of a single sorting chamber. Every chamber for which the sorting permutation fixes the star hub has local modulus \(1\); every chamber that moves the hub has local modulus equal to the displayed sharp global constant.

For each fixed \(\gamma>0\), as \(n\to\infty\),
\[
 \operatorname{Lip}_{n,\gamma}(S)\sim\sqrt{\frac{\gamma n}{1+\gamma}}.
\]
At coupling \(\gamma=\lambda/n\) with fixed \(\lambda>0\), the exact limit is
\[
 \frac{\sqrt{4+\lambda^2/(1+\lambda)}+\lambda/\sqrt{1+\lambda}}{2}.
\]
The same sorting map, acting on vectors modulo constants with the homogeneous Dirichlet norm \(\|x\|_{\dot H^1}^2=\sum_{j=1}^n(x_0-x_j)^2\), has the exact global Lipschitz constant
\[
 \frac{\sqrt{n+3}+\sqrt{n-1}}2;
\]
for \(n=1\) this is \(1\), and for \(n=2\) it is the golden ratio.

## Assumptions and scope

The graph is the unweighted finite star with one hub, \(n\) leaves, unit vertex masses, and a single positive edge-energy weight \(\gamma\). Inputs are arbitrary real vectors (ties are allowed). The map assigns the sorted values to the fixed vertex ordering \(0,1,\ldots,n\). Since all coordinate permutations occur as sorting-chamber derivatives, the sharp modulus does not depend on which fixed vertex receives which rank. The Lipschitz modulus uses **two arbitrary inputs**; it is not the ratio of graph energies of an input and its own rearrangement. The homogeneous norm is a norm on the quotient by additive constants, and sorting respects that quotient.

## Proof

**Step 1: Reduce the nonlinear modulus to finitely many linear norms.** Set \(A=I+\gamma L\), where \(L\) is the graph Laplacian of the star with hub \(0\). Every strict sorting chamber is an open convex set on which \(S\) acts as one coordinate permutation matrix \(P\). The segment between any two inputs crosses only finitely many sorting walls, so the triangle inequality along the segment gives
\[
 \|S(x)-S(y)\|_A\le\bigl(\max_P\|P\|_{A\to A}\bigr)\|x-y\|_A.
\]
If a segment lies along a wall, the same inequality follows by approximation and continuity. Conversely, every strict chamber has nonempty interior: take any interior vector and a sufficiently small displacement along a maximizing vector of \(P^TAP\) relative to \(A\). This gives equality in the global Lipschitz supremum with a *finite, nonidentical pair in one chamber*. Thus the sharp modulus equals the largest induced norm among coordinate permutations.

**Step 2: Only moving the hub matters.** A permutation fixing vertex \(0\) merely permutes leaves, hence \(P^TAP=A\) and its induced norm is \(1\). If a permutation moves the hub, its conjugated form is \(B=I+\gamma L_1\), the quadratic form of the star whose hub is vertex \(1\), up to relabeling leaves. All such permutations have the same generalized eigenvalues as the transposition \(T=(0\,1)\), by symmetry of the original and new stars. Write \(D=1+(n+1)\gamma\). The inverse of the positive definite matrix \(A\) has entries
\[
 (A^{-1})_{00}=\frac{1+\gamma}{D},\qquad
 (A^{-1})_{0j}=\frac{\gamma}{D},\qquad
 (A^{-1})_{ij}=\frac{\mathbf1_{\{i=j\}}}{1+\gamma}
 +\frac{\gamma^2}{(1+\gamma)D}\quad(i,j\ge1).
\]
These identities can be verified directly by multiplication with the hub/leaf block matrix of \(A\).

**Step 3: Compute the entire nontrivial generalized spectrum.** If \(n=1\), both centered stars are the same edge and the sharp modulus is \(1\). Assume \(n\ge2\). The difference \(B-A=\gamma(L_1-L_0)\) has rank at most two: explicitly,
\[
 L_1-L_0=(n-1)(e_1e_1^T-e_0e_0^T)
 -(e_1-e_0)\sum_{j=2}^n e_j^T
 -\left(\sum_{j=2}^n e_j\right)(e_1-e_0)^T.
\]
Thus at least \(n-1\) of the \(n+1\) generalized eigenvalues of \((B,A)\) equal \(1\). Since a vertex permutation conjugates \(A\) to \(B\), \(\det B=\det A\), so the remaining positive generalized eigenvalues \(\rho_+,\rho_-\) have product \(1\). The inverse matrix above gives, for distinct leaves \(j\ne k\),
\[
 (e_j-e_k)^TA^{-1}(e_j-e_k)=\frac2{1+\gamma},\qquad
 (e_0-e_j)^TA^{-1}(e_0-e_j)=\frac{2+(n+1)\gamma}{(1+\gamma)D}.
\]
Using the decomposition \(L_h=\sum_{j\ne h}(e_h-e_j)(e_h-e_j)^T\), we consequently obtain
\[
 \operatorname{tr}(A^{-1}B)-(n+1)
 =\gamma(n-1)\left[\frac2{1+\gamma}
 -\frac{2+(n+1)\gamma}{(1+\gamma)D}\right]
 =\delta_{n,\gamma}.
\]
Hence \(\rho_++\rho_-=2+\delta_{n,\gamma}\). As their product is \(1\),
\[
 \sqrt{\rho_+}=\frac{\sqrt{4+\delta_{n,\gamma}}+\sqrt{\delta_{n,\gamma}}}{2}.
\]
The largest generalized eigenvalue is \(\rho_+>1\). The induced norm of \(T\) is its square root, proving the sharp formula and the chamber classification.

**Step 4: Limits and homogeneous quotient.** Elementary asymptotics yield the two coupling regimes stated above. For the homogeneous norm, restrict to the mean-zero subspace. Every permutation preserves constants and this subspace. Both \(A\) and \(B\) act identically on constants, and the generalized Rayleigh quotient \(x^TBx/x^TAx\) on the complement converges uniformly on its Euclidean unit sphere to the quotient \(x^TL_1x/x^TL_0x\) as \(\gamma\to\infty\). Consequently, the sharp homogeneous quotient norm is the limit of the displayed positive-definite norm, with \(\delta_{n,\gamma}\to n-1\), giving \((\sqrt{n+3}+\sqrt{n-1})/2\). The same chamber and segment argument is valid modulo constants.

## Verification

Run `python sorting_star_checker.py` with Python 3.10 or later and NumPy installed. The standalone checker recomputes the inverse and trace identities using exact fractions, enumerates every sorting permutation for small stars, compares independent generalized-eigenvalue calculations, and constructs real pairs achieving the predicted modulus inside individual sorting chambers. It reports **2704 independent exact-rational, chamber and attaining-pair checks** on successful execution. These finite computations are reproducibility tests, not substitutes for the all-dimensional analytic proof.

## Relationship to prior work

The classical decreasing-rearrangement contraction and its use for monotone-function estimation are developed by Chernozhukov, Fernández-Val, and Galichon (arXiv:0704.3686, first public 2007-04-27); those \(L^p\) statements do not control a graph-gradient term in a two-input difference. Steinerberger's work on discrete rearrangements and Pólya–Szegő inequalities on graphs (arXiv:2209.06765) studies how rearrangement changes the gradient energy of *one input*, not the perturbation modulus \(\|S(x)-S(y)\|_{n,\gamma}/\|x-y\|_{n,\gamma}\). The GroupSort treatment by Anil, Lucas, and Grosse (arXiv:1811.05381) establishes norm-preserving/Lipschitz behavior in permutation-symmetric coordinate norms; the present energy form is not permutation-invariant. The spectral computation is elementary linear algebra, but these inspected sources do not state the sharp finite-star Sobolev two-point profile or its extremizing-chamber rigidity.

## Limitations

The exact formula assumes a finite unweighted star and a common coupling. It does not cover arbitrary weighted stars, arbitrary graph topologies, other smoothness exponents, or infinite stars. The phrase 'sharp' refers to a global **two-input** Lipschitz modulus, not single-input energy comparison. Existing unindexed rearrangement or numerical linear-algebra literature could contain an equivalent special case. No claim of an independent audit is made.

## References

1. V. Chernozhukov, I. Fernández-Val, A. Galichon, *Improving Estimates of Monotone Functions by Rearrangement*, arXiv:0704.3686 (first public 2007-04-27), https://arxiv.org/abs/0704.3686.
2. S. Steinerberger, *Discrete Rearrangements and the Pólya–Szegő Inequality on Graphs*, arXiv:2209.06765, https://arxiv.org/abs/2209.06765.
3. C. Anil, J. Lucas, R. Grosse, *Sorting Out Lipschitz Function Approximation*, arXiv:1811.05381; ICML 2019, https://arxiv.org/abs/1811.05381.
