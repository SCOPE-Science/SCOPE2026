# Direction-invariant norms of finite-particle mixed free-Fock operators

## Finding

Let \(H\) be a nonzero complex Hilbert space and \(P_N\) the projection onto its full tensor Fock space's particle grades from zero through \(N\). For any vectors \(u,v\in H\), the compression \(T_N=P_N(\ell(u)+\ell(v)^*)P_N\) has an exact operator norm determined only by their separate lengths. Write \(a=\|u\|\), \(b=\|v\|\), and define the nonnegative \((N+1)\)-square matrix \(B_N(a,b)\) by

\[
(B_N(a,b))_{j+1,j}=a,\qquad(B_N(a,b))_{j,j+1}=b\quad(0\leq j<N),
\]

with all other entries zero. For every \(N\geq1\),

\[
\boxed{\|P_N(\ell(u)+\ell(v)^*)P_N\|=\|B_N(\|u\|,\|v\|)\|.}
\]

The norm is independent of the angle or phase between \(u\) and \(v\), and independent of the one-particle space's dimension. For \(a,b>0\), the proof constructs norm-attaining alternating pure-tensor vectors supported on one parity of particle degrees. The finite scalar norm is explicitly the square root of the largest eigenvalue of the nonnegative matrix \(B_N^*B_N\). Its diagonal at index \(j\) equals \(a^2\mathbf 1_{j<N}+b^2\mathbf 1_{j>0}\), and its only nonzero off-diagonals join indices two steps apart, with value \(ab\). Thus the large tensor-space norm is an exact calculation from two finite Jacobi matrices.

When \(a=b=s\), the path matrix is symmetric and yields the closed form

\[
\boxed{\|T_N\|=2s\cos\!\left(\frac{\pi}{N+2}\right)}.
\]

Consequently the sharp cutoff loss is

\[
2s-\|T_N\|=\frac{s\pi^2}{(N+2)^2}+O\!\left(\frac{s}{(N+2)^4}\right)
\]

as \(N\to\infty\) for fixed \(s\geq0\).

## Assumptions and scope

The full tensor (not bosonic/symmetric) Fock space is \(\mathcal F(H)=\bigoplus_{j=0}^{\infty}H^{\otimes j}\), with \(H^{\otimes0}=\mathbb C\Omega\) and pairwise orthogonal homogeneous summands. Left creation is \(\ell(u)\xi=u\otimes\xi\); annihilation is its Hilbert adjoint. There is no hypothesis that \(u\) and \(v\) are linearly independent, orthogonal, real, or normalized. The one-particle space may be infinite dimensional. The operator acts on the full Fock space but vanishes on the orthogonal complement of grades at most \(N\).

For \(N=0\), the compression is zero. For \(N\geq1\), if \(a=0\) or \(b=0\), the compressed nonzero left shift or its adjoint has norm \(\max(a,b)\). The construction below treats \(a,b>0\); these degenerate cases are immediate.

## Proof

**Upper bound.** For \(x=\sum_{j=0}^{N}x_j\) with \(x_j\in H^{\otimes j}\), put \(z_j=\|x_j\|\). Its grade-\(k\) output is the sum of \(\ell(u)x_{k-1}\), if \(k\geq1\), and \(\ell(v)^*x_{k+1}\), if \(k<N\). Their norms are at most \(a z_{k-1}\) and \(b z_{k+1}\). Hence

\[
\|T_Nx\|^2\leq\sum_{k=0}^{N}(a z_{k-1}+b z_{k+1})^2
=\|B_N(a,b)z\|_2^2\leq\|B_N(a,b)\|^2\|x\|^2,
\]

with missing grades interpreted as zero.

**Attainment in both parity sectors.** The scalar matrix \(B_N\) maps even-indexed coordinates into odd-indexed coordinates and vice versa, so its norm is the greater of the two rectangular parity-block norms. All its entries are nonnegative; replacing a scalar vector by its entrywise absolute value cannot decrease its output norm. Therefore each parity-block norm has a nonnegative unit maximizing vector.

Set \(\widehat u=u/a\) and \(\widehat v=v/b\). For parity \(p=0\), let \(\theta_k^{(0)}=\widehat u\) when \(k\) is odd and \(\widehat v\) when \(k\) is even. For parity \(p=1\), interchange \(\widehat u\) and \(\widehat v\). Define

\[
\xi_0^{(p)}=\Omega,\qquad
\xi_j^{(p)}=\theta_j^{(p)}\otimes\theta_{j-1}^{(p)}\otimes\cdots\otimes\theta_1^{(p)}\quad(j\geq1).
\]

These are unit vectors, and their different particle grades are orthogonal. If \(j\equiv p\pmod2\), then \(\theta_j^{(p)}=\widehat v\) for \(j\geq1\) and \(\theta_{j+1}^{(p)}=\widehat u\) for \(j<N\). Therefore the **exact**, not merely norm-bounded, action is

\[
T_N\xi_j^{(p)}=a\xi_{j+1}^{(p)}\mathbf1_{j<N}
+b\xi_{j-1}^{(p)}\mathbf1_{j>0},\qquad j\equiv p\pmod2.
\]

Let \(c\) be a nonnegative norm-maximizing coefficient vector supported on that parity and put \(x=\sum_{j\equiv p(2)}c_j\xi_j^{(p)}\). The grade components on the right-hand side coincide at each target grade, so \(\|T_Nx\|=\|B_Nc\|=\|B_N\|\) for whichever parity achieves the scalar norm. This matches the upper bound for arbitrary dimension and arbitrary relative direction.

**Exact finite matrix and balanced specialization.** Direct multiplication gives \((B_N^*B_N)_{jj}=a^2\mathbf1_{j<N}+b^2\mathbf1_{j>0}\), \((B_N^*B_N)_{j,j+2}=ab\), and zeros in all other off-diagonal positions. The even and odd index subspaces are invariant and provide the asserted two Jacobi matrices. If \(a=b=s\), \(B_N\) itself is the symmetric path adjacency matrix. Its normalized sine eigenvectors have components proportional to \(\sin((j+1)k\pi/(N+2))\) with eigenvalues \(2s\cos(k\pi/(N+2))\), for \(k=1,\ldots,N+1\). The spectral norm is therefore \(2s\cos(\pi/(N+2))\). Expanding \(\cos t=1-t^2/2+O(t^4)\) establishes the sharp cutoff deficit and its coefficient.

## Verification

The proof above covers all integers \(N\geq0\), every nonzero complex one-particle Hilbert space, arbitrary complex \(u,v\), and both the balanced and unbalanced cases. The accompanying `verify_mixed_fock.py` independently builds finite-grade tensor matrices from the definitions, compares their singular norms with the scalar path matrix, checks alternating-parity extremizers, checks the exact scalar Jacobi entries, and tests the balanced cosine formula and deficit. Run `python verify_mixed_fock.py` with NumPy installed. Tests are finite corroboration; they do not replace the dimension-independent proof.

## Relationship to prior work

Bandeira, Kunisky, Nizić-Nikolac, Pesenti, and Wang (arXiv:2610.01982v1) explicitly use low-particle projections of Fock creation/annihilation operators in matrix-concentration bounds. Their Sections 3.1 and 4 establish the operator model and norm **inequalities** for self-adjoint matrix pencils, not this exact finite-cutoff norm for a possibly nonselfadjoint creator in one direction plus annihilator in another. Kargin's *Lecture Notes on Free Probability* (arXiv:1305.2611) give the standard full Fock representation and the one-dimensional semicircular example; that covers background and the classical path mechanism, not the two-vector direction-independence of finite compressed mixed operators.

The nonnegative path reduction and the two distinct alternating saturating families are the quantitative and structural assertions here. Earlier Jacobi path eigenvalues themselves are not claimed as novel. A relevant published indexed finding on binomially weighted symmetric-Fock lattice shifts treats a different Hilbert space and a different operator. No mathematical-index search proves uniqueness, and equivalent finite-section calculations elsewhere in the free-probability literature remain a genuine priority risk.

## Limitations

The theorem determines the largest singular value, not the complete singular-value distribution. It is specific to the full tensor Fock norm and to one creation term plus one annihilation term. Symmetric/bosonic or deformed Fock spaces, multiple creation directions, and weighted particle projections are outside its scope. For unequal lengths, the result is an exact finite Jacobi eigenvalue computation rather than a uniform closed radical formula. Publication priority has not been independently established.

## References

1. A. S. Bandeira, D. Kunisky, P. Nizić-Nikolac, L. Pesenti, and R. Wang, *Matrix Concentration and Equivalent Operators on Fock Spaces*, arXiv:2610.01982v1, October 1, 2026; especially Sections 3.1 and 4. https://arxiv.org/html/2610.01982v1
2. V. Kargin, *Lecture Notes on Free Probability*, arXiv:1305.2611, examples on full Fock creation/annihilation and semicircular elements. https://arxiv.org/html/1305.2611v2
