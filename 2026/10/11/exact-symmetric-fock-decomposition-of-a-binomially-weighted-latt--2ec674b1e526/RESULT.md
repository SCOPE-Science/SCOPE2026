# Exact symmetric-Fock decomposition of a binomially weighted lattice backward shift

## Finding

Let \((\omega_k)_{k\ge0}\) be nonzero complex numbers and define \(\mu_{i,j}=\omega_{i+j}\sqrt{\binom{i+j}{i}}\) on \(\mathbb N_0^2\). On \(X_\omega=\ell^2(\mathbb N_0^2,\mu)\), initially set \((Bf)(i,j)=f(i+1,j)+f(i,j+1)\) on finitely supported functions. Then \(B\) extends boundedly if and only if \(\sup_{k\ge0}|\omega_k/\omega_{k+1}|<\infty\), and then \(\|B\|=\sqrt2\sup_{k\ge0}|\omega_k/\omega_{k+1}|\). After the degreewise unitary Hadamard rotation \(u=(z_1+z_2)/\sqrt2\), \(v=(z_1-z_2)/\sqrt2\), \(B\) is the orthogonal direct sum over transverse degrees \(r\ge0\) of unilateral weighted backward shifts with weights \(\beta^{(r)}_{m+1}=\sqrt2\,(\omega_{m+r}/\omega_{m+r+1})\sqrt{(m+1)/(m+r+1)}\). Equivalently, for every \(q\ge0\) and \(n\ge1\), if \(X_k\) denotes the diagonal \(i+j=k\), the nonzero singular values of \(B^n:X_{q+n}\to X_q\) are exactly \(\sigma_s(q,n)=|\omega_q/\omega_{q+n}|2^{n/2}\sqrt{q!(n+s)!/((q+n)!s!)}\), \(s=0,\ldots,q\). Hence \(s_{\min}(B^n|_{X_{q+n}})=|\omega_q/\omega_{q+n}|2^{n/2}\sqrt{q!n!/(q+n)!}\) and \(\|B^n|_{X_{q+n}}\|=|\omega_q/\omega_{q+n}|2^{n/2}\). This is a genuinely non-radial family because the within-diagonal factor \(\sqrt{\binom{k}{i}}\) is unbounded across growing diagonals.

## Assumptions and scope

The vertex set is \(\mathbb N_0^2\), every \(\omega_k\neq0\), and
\[
\|f\|_{X_\omega}^2=\sum_{i,j\ge0}|\omega_{i+j}|^2\binom{i+j}{i}|f(i,j)|^2.
\]
For each \(k\ge0\), \(X_k\) is the finite-dimensional subspace supported on \(i+j=k\). The theorem concerns bounded extension of \(B\), its unitary decomposition when bounded, and the exact singular spectrum of every transfer \(B^n:X_{q+n}\to X_q\).

## Proof

Use the orthonormal weighted-coordinate basis on each \(X_k\). For the one-step transfer \(T_k:X_{k+1}\to X_k\), the two coefficients entering output coordinate \(i\) are
\[
\frac{\omega_k}{\omega_{k+1}}\sqrt{\frac{i+1}{k+1}}
\quad\text{and}\quad
\frac{\omega_k}{\omega_{k+1}}\sqrt{\frac{k+1-i}{k+1}}.
\]
Thus, under the standard identification with degree-\(k\) symmetric tensors in two variables,
\[
T_k=\frac{\omega_k}{\omega_{k+1}}\frac{a_1+a_2}{\sqrt{k+1}},
\]
where \(a_1,a_2\) are the annihilation operators.

The unitary Hadamard rotation \(u=(z_1+z_2)/\sqrt2\), \(v=(z_1-z_2)/\sqrt2\) sends \(a_1+a_2\) to \(\sqrt2\,a_u\). Hence \(v\)-degree \(r\) is preserved. On the normalized vector with \(u\)-degree \(m+1\) and \(v\)-degree \(r\), the coefficient is
\[
\sqrt2\frac{\omega_{m+r}}{\omega_{m+r+1}}\sqrt{\frac{m+1}{m+r+1}},
\]
which proves the orthogonal direct-sum description.

Iterating from total degree \(q+n\) to \(q\) gives
\[
T_q\cdots T_{q+n-1}=\frac{\omega_q}{\omega_{q+n}}2^{n/2}\sqrt{\frac{q!}{(q+n)!}}\,a_u^n.
\]
For output \(u\)-degree \(s\), the input has \(u\)-degree \(n+s\), and \(a_u^n\) contributes \(\sqrt{(n+s)!/s!}\). These channels are mutually orthogonal, so the coefficients are exactly all nonzero singular values. They increase with \(s\), giving the stated minimum and maximum. For \(n=1\), the largest singular value of \(T_k\) is \(\sqrt2|\omega_k/\omega_{k+1}|\). Since the degree spaces are orthogonal and \(B\) maps \(X_{k+1}\) into \(X_k\), boundedness is equivalent to uniform boundedness of these level norms, and the global norm is their supremum.

## Verification

Every step uses exact binomial ratios and a unitary change of basis. The endpoint \(q=0\) gives the single singular value \(|\omega_0/\omega_n|2^{n/2}\); the case \(n=1\) recovers the level norm used for boundedness. No finite experiment or asymptotic estimate is used to prove the infinite statement.

## Relationship to prior work

Chen, Wang, and Zhou analyze the same quadrant backward shift in arXiv:2609.34308v1. Their sharp Hilbert-space theorem assumes radial weights \(\mu_{i,j}=\omega_{i+j}\), uses Pascal transfer matrices, and derives an asymptotic smallest-singular-value law; their further-questions section explicitly asks about non-radial weights. The present binomial factor is non-radial and converts the transfer into a symmetric-Fock annihilation operator, yielding every singular value exactly.

Baranov, Lishanskii, and Papathanasiou give broad sufficient and necessary growth criteria for hypercyclic lattice shifts on the infinite quadrant, but not this unitary decomposition or exact finite-level spectrum.

## Limitations

The theorem treats this canonical binomially weighted family, not arbitrary non-radial weights. It does not claim a complete \(\mathcal F\)-transitivity classification. An equivalent annihilation-operator identity may occur in classical symmetric-Fock, Drury--Arveson, or multishift literature under terminology not recovered by the searches.

## References

1. Xiang Chen, Cui Wang, and Ze-hua Zhou, “\(\mathcal F\)-Transitivity of Backward Shifts on Lattice Graphs,” arXiv:2609.34308v1, first posted 2026-09-28.
2. Anton Baranov, Andrei Lishanskii, and Dimitris Papathanasiou, “Hypercyclic shifts on lattice graphs,” arXiv:2312.13934; *Revista de la Real Academia de Ciencias Exactas, Físicas y Naturales. Serie A. Matemáticas* 120 (2026), Article 78, DOI:10.1007/s13398-026-01868-8.
