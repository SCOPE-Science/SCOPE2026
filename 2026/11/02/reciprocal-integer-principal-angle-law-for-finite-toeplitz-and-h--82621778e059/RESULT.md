# Reciprocal-integer principal-angle law for finite Toeplitz and Hankel matrix spaces

## Finding

Let \(\mathcal T_n\) and \(\mathcal H_n\) be the complex Toeplitz and Hankel subspaces of \(M_n(\mathbb C)\), respectively, with the Frobenius inner product. Write \(G_n\) for the cross-Gram matrix between their normalized diagonal and antidiagonal indicator bases, and enumerate its singular values in nonincreasing order, padding by zeros. For each fixed integer \(k\ge1\),

\[
\lim_{n\to\infty}s_{2k-1}(G_n)=\lim_{n\to\infty}s_{2k}(G_n)=\frac1k.
\]

Indeed the entire singular-value sequence converges in \(\ell^2\) to \((1,1,1/2,1/2,1/3,1/3,\ldots)\). In particular,

\[
\lim_{n\to\infty}\|G_n\|_{\mathcal S_2}^2=\frac{\pi^2}{3}.
\]

For \(n\ge3\), the intersection \(\mathcal I_n=\mathcal T_n\cap\mathcal H_n\) has dimension exactly two. The sharp constant in the intersection-normalized decomposition inequality

\[
\|A+B\|_F^2\ge c_n\bigl(\|A\|_F^2+\|B\|_F^2\bigr),
\quad A\in\mathcal T_n\ominus\mathcal I_n,\ B\in\mathcal H_n\ominus\mathcal I_n,
\]

is \(c_n=1-s_3(G_n)\), and hence \(\lim_{n\to\infty}c_n=1/2\). Thus after fixing the canonical common component, the Toeplitz-plus-Hankel decomposition remains asymptotically uniformly conditioned; its sharp limiting squared-norm stability constant is one half.

## Assumptions and scope

Indices \(i,j\) range from \(0\) to \(n-1\). Toeplitz means constant on diagonals \(i-j=d\); Hankel means constant on antidiagonals \(i+j=s\). All spaces are over \(\mathbb C\). The matrix Hilbert norm is \(\|X\|_F=(\sum_{i,j}|X_{ij}|^2)^{1/2}\), and \(\mathcal S_2\) denotes the Hilbert–Schmidt ideal on Hilbert spaces. The singular values \(s_j\) are those of the finite real nonnegative cross-Gram matrix; its zeros are included. The theorem is about **principal angles of two matrix subspaces**, not singular values of individual Toeplitz or Hankel matrices. There is no arbitrary rescaling of the Frobenius norm.

## Proof

**1. Exact discrete cross-Gram matrix and common directions.** Let \(D_d\) be the indicator of diagonal \(i-j=d\), and \(E_s\) the indicator of antidiagonal \(i+j=s\). The normalized families \(D_d/\sqrt{n-|d|}\) and \(E_s/\sqrt{n-|s-(n-1)|}\) are orthonormal bases of \(\mathcal T_n\) and \(\mathcal H_n\). Their cross-Gram entries are

\[
G_n(d,s)=\frac{\mathbf1_{\{d\equiv s\pmod2,\ |d|\le s\le2n-2-|d|\}}}{\sqrt{(n-|d|)(n-|s-(n-1)|)}},
\quad -(n-1)\le d\le n-1,\quad0\le s\le2n-2.
\]

This follows by solving \(i-j=d\), \(i+j=s\) for the unique possible cell. Intersection matrices that are simultaneously Toeplitz and Hankel must satisfy \(X_{i,j}=X_{i+1,j+1}=X_{i+1,j-1}\) whenever indices permit, so the entries depend only on the parity of \(i+j\); for \(n\ge3\), this gives precisely the constant and checkerboard matrices. Their dimension is two. General principal-angle theory, or the equality condition for orthogonal projections, implies that precisely two singular values of \(G_n\) equal one.

**2. Both parity blocks have the same Hilbert–Schmidt continuum limit.** Partition rows according to \(d\pmod2\) and columns according to \(s\pmod2\). The cross-Gram matrix is the direct sum of two blocks. For a given parity, set \(x=d/n\), \(y=(s+1)/n\), and \(h=2/n\). Identify each coordinate vector with its value times \(h^{-1/2}\) on its associated half-open interval of length \(h\), and extend by zero on unused boundary intervals. These embeddings are isometries into \(L^2(-1,1)\) for the row space and \(L^2(0,2)\) for the column space; their step-function kernel is \(G_n(d,s)/h\).

Away from the null boundary curves, the entries converge pointwise to the kernel

\[
g(x,y)=\frac{\mathbf1_{\{|x|<\min(y,2-y)\}}}{2\sqrt{(1-|x|)\min(y,2-y)}},\qquad -1<x<1,\ 0<y<2.
\]

Here is the boundary estimate needed to upgrade local convergence to \(L^2\)-convergence. Put \(\ell_d=n-|d|\) and \(\ell_s=n-|s-(n-1)|\). For any fixed row with \(\ell_d=\ell\), there are exactly \(\ell\) nonzero entries, and each has \(\ell_s\ge n-\ell+1\). Consequently its squared sum is at most \(1/(n-\ell+1)\). There are at most two rows for each \(\ell\). Similarly, any fixed column with \(\ell_s=\ell\) has exactly \(\ell\) nonzero entries, each with \(\ell_d\ge n-\ell+1\), and at most two such columns occur for each \(\ell\). Thus, for any \(0<\delta<1/2\), the total squared entries with either \(\ell_d<\delta n\) or \(\ell_s<\delta n\) are bounded uniformly by \(4\delta/(1-\delta)+O(1/n)\), even before restricting to one parity. The integral kernel has the same vanishing boundary tails by direct integration, or by its squared formula and the analogous one-dimensional bounds. On the complement, all step kernels are uniformly bounded and converge almost everywhere, so dominated convergence applies. Sending first \(n\to\infty\), then \(\delta\downarrow0\), proves convergence in Hilbert–Schmidt norm of **each** parity block to the same compact operator \(\mathcal G\) with kernel \(g\).

**3. Reduction to a weighted Volterra operator.** Fold the two branches \(x=\pm u\) and the two branches \(y=t,2-t\) using symmetric and antisymmetric normalized combinations. The kernel \(g\) is symmetric under each reflection, so it acts only from the symmetric column functions to symmetric row functions. On these symmetric components its kernel is exactly

\[
(Kf)(u)=\frac1{\sqrt{1-u}}\int_u^1\frac{f(t)}{\sqrt t}\,dt,\qquad0<u<1.
\]

On antisymmetric components \(\mathcal G\) vanishes. Consequently its positive singular values are exactly those of \(K\). The integral kernel of \(K\) is square integrable: \(\int_0^1\int_u^1((1-u)t)^{-1}\,dt\,du=\pi^2/6\), as also follows from the eigenvalue computation below.

**4. Exact singular spectrum of the limiting Volterra operator.** For each \(k\ge1\), define the polynomial

\[
F_k(t)=t\,{}_2F_1(1-k,k+1;2;t)
=t\sum_{j=0}^{k-1}\frac{(1-k)_j(k+1)_j}{(2)_j\,j!}t^j.
\]

The hypergeometric series terminates, \(F_k(0)=0\), and its coefficients directly verify the differential equation \(t(1-t)F_k''(t)-tF_k'(t)+k^2F_k(t)=0\). Set \(f_k(t)=\sqrt{1-t}\,F_k'(t)\). Its leading polynomial coefficient is nonzero, so the \(f_k\) span a dense subspace of \(L^2(0,1)\): polynomials are dense and multiplication by \(\sqrt{1-t}\) has dense range.

The adjoint formula yields \((K^*f_k)(t)=F_k(t)/\sqrt t\). Rewriting the displayed differential equation as \(\bigl((1-t)F_k'(t)\bigr)'=-k^2F_k(t)/t\) and integrating from \(u\) to \(1\) gives \((K K^* f_k)(u)=k^{-2}f_k(u)\). Hence \(K K^*\) is a compact positive self-adjoint operator with a complete eigenbasis of nonzero eigenvectors, indexed by all \(k\ge1\), having eigenvalues \(k^{-2}\). In particular \(s_k(K)=1/k\), and \(\|K\|_{\mathcal S_2}^2=\sum_{k\ge1}k^{-2}=\pi^2/6\).

**5. Back to finite sections and decomposition stability.** Hilbert–Schmidt convergence implies operator-norm convergence. Singular values of compact operators are 1-Lipschitz with respect to operator norm, so each parity block has \(k\)-th singular value tending to \(1/k\). Merging the two blocks proves the twofold reciprocal-integer law. Moreover the Hilbert–Schmidt convergence of the blocks gives convergence of their squared singular-value sums to \(2\|K\|_{\mathcal S_2}^2=\pi^2/3\); together with pointwise singular-value convergence, this implies convergence of the full ordered spectra in \(\ell^2\).

Finally, restrict the two subspaces to the Frobenius-orthogonal complements of their two-dimensional intersection. The maximal absolute cross inner product of unit vectors in these complements equals \(s_3(G_n)\). Thus \(2\operatorname{Re}\langle A,B\rangle_F\ge-2s_3(G_n)\|A\|_F\|B\|_F\ge-s_3(G_n)(\|A\|_F^2+\|B\|_F^2)\), and equality is achieved by opposite principal vectors of equal norm. The best constant is therefore \(1-s_3(G_n)\), which tends to \(1-1/2=1/2\).

## Verification

The standalone `checker.py` constructs the exact finite diagonal/antidiagonal incidence matrix, verifies its normalized entries for many dimensions and every admissible index, checks the two unit singular values and strict spectral gap at the next value, checks rational differential-equation coefficients for the polynomial eigenfunctions, and compares numerical singular values against the limiting reciprocal-integer values at a large cutoff. It produces 43,864 successful finite assertions. The proof of the limiting spectrum, \(\ell^2\)-convergence and sharp stability coefficient is analytical; finite experiments alone would not justify these assertions.

## Relationship to prior work

Babbar, Majee and Maji characterize the Toeplitz–Hankel intersection and the ambiguity of decomposing a sum (arXiv:2610.35897v1, particularly Theorems 5.5 and 6.1). Bhuia and Majee's earlier account recovers the two-dimensional checkerboard ambiguity for the special model space \(z^n\) (arXiv:2606.09370v1, Section 5). Those algebraic results provide the natural normalization, but do not give the principal-angle asymptotics or the sharp stability coefficient proved here. Classical theory of angles between subspaces/projection products supplies the identification of the cross-Gram singular values with principal-angle cosines, not the reciprocal-integer formula.

## Limitations

The theorem concerns square full complex matrix Toeplitz and Hankel subspaces with the unweighted Frobenius norm and the limit of increasing dimension. It does not assert finite-\(n\) closed forms for every singular value, operator-spectral-norm stability, non-square matrices, or generic finite Blaschke products. The sharp constant is for decompositions whose two summands are individually perpendicular to the common intersection. No general publication-priority or independent verification claim is made.

## References

1. K. Babbar, S. Majee and A. Maji, *Algebraic properties of Truncated Toeplitz + Truncated Hankel operators*, arXiv:2610.35897v1 (first publicly submitted 2026-09-24), https://arxiv.org/html/2610.35897v1.
2. S. R. Bhuia and S. Majee, *Algebraic characterizations of paired operators on model spaces*, arXiv:2606.09370v1 (2026), https://arxiv.org/abs/2606.09370.
3. E. Andruchow and G. Corach, *Schmidt decomposable products of projections*, Integral Equations and Operator Theory (2017), DOI 10.1007/s00020-017-2402-x (general projection-angle background).
