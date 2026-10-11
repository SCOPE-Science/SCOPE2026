# Half-cycle spectral rigidity and gap products for arbitrary cyclic Fourier masks

## Finding

Let \(N\geq1\), \(G=\mathbb Z/(2N)\mathbb Z\), and \(H=\{0,\ldots,N-1\}\). For any nonempty set of frequency indices \(F\subseteq\{0,\ldots,2N-1\}\), write \(E=\{k\in F:k\equiv0\pmod2\}\), \(O=\{k\in F:k\equiv1\pmod2\}\), \(e=|E|\), \(o=|O|\), and \(r=\min(e,o)\). Let \(P_F\) be orthogonal projection onto the span of the corresponding Fourier characters, and let \(C_F=P_FM_{1_H}P_F\) act on that Fourier subspace.

**Exact transition multiplicity and pairing.** The multiplicity of the half-energy concentration eigenvalue is
\[
\operatorname{mult}_{C_F}(1/2)=|e-o|.
\]
The remaining \(2r\) eigenvalues lie in symmetric pairs \(\lambda,1-\lambda\), none equal to \(1/2\).

**Exact noncentral gap product.** Put \(z_k=\exp(\pi i k/N)\). With the empty-product and empty-index-sum conventions, set
\[
\mathcal G(F)=\prod_{\lambda\in\sigma(C_F),\,\lambda\ne1/2}|2\lambda-1|,
\]
where algebraic multiplicity is included. Then \(\mathcal G(F)>0\) and
\[
\mathcal G(F)=\left(\frac2N\right)^{2r}
\sum_{\substack{I\subseteq E,\ |I|=r\\J\subseteq O,\ |J|=r}}
\frac{\prod_{\{a,b\}\subseteq I}|z_a-z_b|^2
      \prod_{\{c,d\}\subseteq J}|z_c-z_d|^2}
     {\prod_{a\in I,\ c\in J}|z_a-z_c|^2}.
\]
All two-element subsets in the numerator are unordered. In the balanced case \(e=o=r\), only one summand occurs and
\[
\det(2C_F-I)=(-1)^r\mathcal G(F),\qquad
\mathcal G(F)=\left(\frac2N\right)^{2r}
\frac{\prod_{\{a,b\}\subseteq E}|z_a-z_b|^2
      \prod_{\{c,d\}\subseteq O}|z_c-z_d|^2}
     {\prod_{a\in E,\ c\in O}|z_a-z_c|^2}.
\]
If \(e\ne o\), then \(\det(2C_F-I)=0\), and the first formula gives the signed nonzero-eigenvalue product after multiplication by \((-1)^r\).

## Assumptions and scope

The Hilbert space \(L^2(G)\) has normalized counting measure. The Fourier characters \(\chi_k(t)=\exp(\pi i kt/N)\) are an orthonormal basis. The time window is exactly one contiguous half of an even cycle; no contiguity or symmetry is assumed of \(F\). The formula applies to all \(N\ge1\), including the cases \(r=0\) (all eigenvalues equal \(1/2\), with \(\mathcal G(F)=1\)) and \(F=G\) (eigenvalues \(0\) and \(1\), each with multiplicity \(N\)). A cyclic translate of \(H\) gives a unitarily conjugate concentration operator and hence the same results.

## Proof

1. In the orthonormal frequency basis, matrix entries are
\[
(C_F)_{k\ell}=\frac{1}{2N}\sum_{t=0}^{N-1}\exp\!\left(\frac{\pi i(\ell-k)t}{N}\right).
\]
For \(k=\ell\) the entry is \(1/2\). For distinct indices of the same parity, the geometric sum is zero: the ratio is a nontrivial \(N\)-th root of unity. For opposite parity, the geometric numerator equals \(2\).

2. Order the even frequencies before the odd ones and set \(U=2C_F-I\). Then
\[
U=\begin{pmatrix}0&B\\B^*&0\end{pmatrix},\qquad
B_{ac}=\frac2N\frac{z_a}{z_a-z_c}\quad(a\in E,\ c\in O).
\]
The denominators cannot vanish: all \(z_k\) for \(0\le k<2N\) are distinct. The square minors of \(B\) are nonzero by the Cauchy determinant identity
\[
\left|\det\left(\frac1{z_a-z_c}\right)_{a\in I,c\in J}\right|
=\frac{\prod_{\{a,b\}\subseteq I}|z_a-z_b|\prod_{\{c,d\}\subseteq J}|z_c-z_d|}
{\prod_{a\in I,c\in J}|z_a-z_c|}.
\]
The factors \(z_a\) have modulus one. Thus \(\operatorname{rank}B=r\) for every mask, not merely generic masks.

3. The nonzero eigenvalues of the Hermitian block-off-diagonal matrix \(U\) are exactly \(s_1,-s_1,\ldots,s_r,-s_r\), where \(s_j>0\) are the positive singular values of \(B\). Its nullity is \(e+o-2r=|e-o|\). Since \(C_F=(I+U)/2\) is a compression of a positive contraction, its eigenvalues belong to \([0,1]\), and the asserted pairing follows.

4. The product of magnitudes of all nonzero eigenvalues of \(U\) is \(\prod_{j=1}^{r}s_j^2\). By Cauchy--Binet this equals
\[
\sum_{\substack{I\subseteq E,\ |I|=r\\J\subseteq O,\ |J|=r}}|\det B_{I,J}|^2.
\]
One of the two chosen index sets is necessarily the entire smaller parity class. Substituting the Cauchy determinant identity gives the displayed gap-product formula. The signed product is \((-1)^r\mathcal G(F)\); when \(e=o\) there are no zero eigenvalues and it is the determinant. The formula remains true for \(r=0\) under the specified conventions. This completes the proof for every finite \(N\) without extrapolating from numerical data.

## Verification

The standalone script `verification.py` reconstructs the Fourier compression directly from the geometric sum, diagonalizes the Hermitian centered matrix numerically, checks the predicted nullity and eigenvalue pairing, and evaluates the explicit chord-product formula. It exhaustively checks all nonempty masks for \(1\le N\le4\) and checks deterministic pseudorandom masks for \(5\le N\le7\). The verified output is `VERIFY_OK exhaustive_n=1..4 random_n=5..7 checks=696`. These numerical checks are corroborative, not an infinite proof; the proof above uses exact geometric and Cauchy identities.

## Relationship to prior work

Jaming (first public preprint 16 December 2009, primary MSC 42A38 in the journal metadata) studies structural characterizations of Fourier transformations on cyclic groups, rather than eigenvalues of frequency/time-window compressions. The periodic discrete prolate spheroidal framework originates in the works of Xu and Chamzas and its successors. Matthysen and Huybrechs, in their section on periodic discrete prolate spheroidal sequences, work with contiguous frequency bands and spatial intervals and analyze the resulting eigenfunctions and computations, not arbitrary frequency-mask half-window transition multiplicities or the chord-product invariant. Zhu and coauthors analyze the distribution of eigenvalues for contiguous symmetric DFT bands and time intervals by nonasymptotic estimates rather than the exact parity-count nullity. Existing related concentration results on other geometries do not imply a formula for the discrete cyclic Fourier matrix without a new kernel identification.

## Limitations

The result is specific to exact half-cycle windows in groups of even cardinality; it does not classify transition eigenvalues for general time sets or unequal interval lengths, nor determine each noncentral eigenvalue individually. The proof uses classical Cauchy matrix identities; a prior equivalent statement under a different periodic-prolate, Toeplitz, or Cauchy-matrix terminology cannot be categorically excluded. The 1984 Xu--Chamzas paper is a material access limitation: its bibliographic record and abstract are accessible, but its complete primary text was not available for direct comparison. No independent audit has been performed.

## References

1. P. Jaming, *A characterization of Fourier transforms*, arXiv:0912.3129v1 (16 December 2009); *Colloquium Mathematicum* 118 (2010), 569--580, DOI 10.4064/cm118-2-12. First listed MSC: 42A38.
2. W. Y. Xu and C. Chamzas, *On the Periodic Discrete Prolate Spheroidal Sequences*, *SIAM Journal on Applied Mathematics* 44 (1984), 1210--1217, DOI 10.1137/0144086. Full text access limited for the present comparison.
3. R. Matthysen and D. Huybrechs, *Fast Algorithms for the Computation of Fourier Extensions of Arbitrary Length*, arXiv:1509.00206v1 (1 September 2015), §3.3; *SIAM Journal on Scientific Computing* 38 (2016), A899--A922.
4. Z. Zhu, S. Karnik, M. A. Davenport, J. Romberg, and M. B. Wakin, *The Eigenvalue Distribution of Discrete Periodic Time-Frequency Limiting Operators*, arXiv:1707.05344v1 (17 July 2017), §II and Theorem 1.
