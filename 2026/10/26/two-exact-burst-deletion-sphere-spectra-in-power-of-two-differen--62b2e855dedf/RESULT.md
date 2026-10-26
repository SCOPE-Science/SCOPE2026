# Two exact burst-deletion sphere spectra in power-of-two differential VT codes

## Finding

For every power of two \(n=2^r\), \(r\ge2\), and every residue \(a\pmod{2n}\), consider the binary differential Varshamov–Tenengolts code
\[
\mathcal C_a(n)=\left\{x\in\{0,1\}^n:\sum_{i=1}^n i\delta_i(x)\equiv a\pmod{2n}\right\},
\qquad
\delta_i(x)=x_i\oplus x_{i+1}\ (i<n),\quad \delta_n(x)=x_n.
\]
Write \(\mathcal B_2(x)\) for the **set of distinct length-\(n-2\) words** obtained by deleting precisely two adjacent positions of \(x\), and set
\[
W_a(z)=\sum_{x\in\mathcal C_a(n)} z^{|\mathcal B_2(x)|},\qquad
G_n(z)=z(1+z)^{n-2},\qquad
K_n(z)=z(1-z)^{n/2}(1+z)^{n/2-2}.
\]
Then the **complete deletion-sphere-size enumerator**, coefficient by coefficient, is
\[
\boxed{W_a(z)=\begin{cases}
\dfrac{2G_n(z)+(n-2)K_n(z)}{n},&a\equiv 0\text{ or }n/2\pmod n,\\[2mm]
\dfrac{2G_n(z)-2K_n(z)}{n},&\text{otherwise}.
\end{cases}}
\]
Consequently exactly four of the \(2n\) syndrome classes have the first polynomial, while all other classes have the second. These polynomials are different for every \(n\ge4\), since the coefficient of \(z\) is one in the first and zero in the second. Thus the first classes each contain precisely one word with a single distinct two-burst-deletion descendant, whereas the others contain none.

For example, at \(n=8\), the two polynomials are \(z+3z^3+8z^4+3z^5+z^7\) and \(2z^2+4z^3+4z^4+4z^5+2z^6\). Evaluating at \(z=1\) recovers the common cardinality \(|\mathcal C_a(n)|=2^{n-1}/n\). Differentiating at \(z=1\) yields \(\sum_{x\in\mathcal C_a(n)}|\mathcal B_2(x)|=2^{n-2}\), consistently with the established perfect two-burst-deletion correction/covering property.

## Assumptions and scope

The alphabet is binary. Two deleted positions must be **consecutive**, and outputs are counted without multiplicity. All \(2n\) differential-VT syndrome classes are included; \(n\) is restricted to powers of two at least four. The code need not be linear. The enumerator records each codeword's number of distinct channel outputs, not the number of possible deletion locations and not the number of received words in a Hamming metric ball.

## Proof

**1. Distinct two-burst descendants.** Index possible two-position deletion windows by \(i=1,\ldots,n-1\), and let \(y_i\) be the resulting word. Direct comparison shows \(y_i=y_{i+1}\) if and only if \(x_i=x_{i+2}\). More generally, for \(i<j\), equality \(y_i=y_j\) forces the subword on positions \(i,\ldots,j+1\) to have period two: comparing the shifted pieces gives \(x_t=x_{t+2}\) for every \(i\le t<j\). Hence the sequence of outputs \(y_1,\ldots,y_{n-1}\) has contiguous equality blocks and distinct values in different blocks. Therefore
\[
|\mathcal B_2(x)|=1+\sum_{i=1}^{n-2}{\bf1}_{x_i\ne x_{i+2}}
=1+\sum_{i=1}^{n-2}{\bf1}_{\delta_i(x)\ne\delta_{i+1}(x)}.
\]
(The second equality follows from cancellation in the binary differences.)

**2. Remove the final difference.** The map from a binary word to its differential vector \((\delta_1,\ldots,\delta_n)\) is bijective. For each first \(n-1\) difference bits and each residue \(a\pmod {2n}\) consistent with their weighted sum modulo \(n\), there is exactly one choice of \(\delta_n\in\{0,1\}\) satisfying the syndrome modulo \(2n\), because its coefficient is \(n\). Thus \(W_a\) depends only on \(v=a\bmod n\) and equals the transition enumerator for difference bits \(e_1,\ldots,e_{n-1}\) subject to \(\sum_{i=1}^{n-1}i e_i\equiv v\pmod n\).

**3. Finite Fourier transform.** For an \(n\)-th root of unity \(q\), define
\[
F_n(q,z)=\sum_{e\in\{0,1\}^{n-1}} z^{1+\sum_{i=1}^{n-2}{\bf1}_{e_i\ne e_{i+1}}}\,q^{\sum_{i=1}^{n-1}i e_i}.
\]
Let \(J=\begin{pmatrix}1&z\\z&1\end{pmatrix}\), \(D_i(q)=\operatorname{diag}(1,q^i)\), \(P_n(q,z)=\prod_{i=1}^{n}JD_i(q)\), with increasing index order, and \({\bf1}=(1,1)^\top\). Since \(D_n=I\) and \(J{\bf1}=(1+z){\bf1}\), expanding the matrix product gives the polynomial identity
\[
(1+z)^2F_n(q,z)=z\, {\bf1}^\top P_n(q,z){\bf1}.
\]
When \(q=1\), choosing the initial bit and independently each transition gives \(F_n(1,z)=2z(1+z)^{n-2}=2G_n(z)\).

**4. Every proper nontrivial Fourier mode.** Suppose \(q\) has order \(d\), where \(2\le d\mid n/2\). Since \(n\) is a power of two, \(d\) is even and \(n/d\) is even. Periodicity of the diagonal factors gives \(P_n=P_d^{n/d}\). We prove \(\operatorname{tr}P_d=0\). Its trace is a sum over cyclic binary words \((e_1,\ldots,e_d)\), with summand
\[
z^{\sum_{i=1}^d{\bf1}_{e_i\ne e_{i+1}}}
q^{\sum_{i=1}^d i e_i},\qquad e_{d+1}=e_1.
\]
The all-zero cyclic word contributes \(1\); the all-one word contributes \(q^{d(d+1)/2}=-1\). Every other cyclic word has least rotational period \(p\mid d\) and \(0<w<p\) ones per primitive period. Rotating it one position multiplies its phase by \(q^{\pm(d/p)w}\), a nontrivial \(p\)-th root of unity; consequently the sum over its \(p\) rotations vanishes. This cancels every nonconstant orbit, proving the trace identity. Furthermore
\[
\det P_d=(1-z^2)^d q^{d(d+1)/2}=-(1-z^2)^d.
\]
The \(2\times2\) Cayley–Hamilton identity therefore gives \(P_d^2=(1-z^2)^d I\), and hence \(P_n=(1-z^2)^{n/2}I\). Substituting in the matrix identity yields
\[
F_n(q,z)=\frac{2z(1-z^2)^{n/2}}{(1+z)^2}=2K_n(z),
\]
where the displayed quotient is a polynomial because \(n/2\ge2\).

**5. Primitive Fourier modes.** If \(q\) has order \(n\), the involution \(e'_i=1-e_{n-i}\) on \(\{0,1\}^{n-1}\) preserves the number of transitions. Its weighted syndrome changes by \(\sum_{i=1}^{n-1}i=n(n-1)/2\equiv n/2\pmod n\). Because \(q^{n/2}=-1\), paired summands cancel and \(F_n(q,z)=0\).

**6. Fourier inversion.** Let \(\zeta\) be a primitive \(n\)-th root of unity. The required enumerator is
\[
W_a(z)=\frac1n\sum_{j=0}^{n-1}\zeta^{-jv}F_n(\zeta^j,z),\qquad v=a\bmod n.
\]
By steps 3–5 the transform is \(2G_n\) at \(j=0\), is zero at odd \(j\), and equals \(2K_n\) at nonzero even \(j\). Finally,
\[
\sum_{\substack{1\le j<n\\2\mid j}}\zeta^{-jv}
=\begin{cases}n/2-1,&v\equiv0\pmod{n/2},\\-1,&\text{otherwise}.
\end{cases}
\]
This yields the two stated polynomials and completes the proof. All equalities are polynomial identities over integers after Fourier inversion; no numerical approximation enters.

## Verification

The accompanying `verify.py` independently enumerates all binary words of lengths \(4,8,16\), directly builds all consecutive-two-deletion outputs as **sets of words**, independently computes syndromes, and compares the exact histograms to the formulas. It also checks the local burst-ball identity and confirms that every syndrome covers \(2^{n-2}\) outputs counting each distinct codeword ball. A separate exact-integer dynamic program over difference-vector prefixes checks every residue and all coefficients at lengths \(4,8,16,32,64\). The archived output records `DVT_BURST_SPECTRA_VERIFY_OK`. The proof, not these finite checks, establishes the claim for every power of two.

To reproduce: run `python3 verify.py` with Python 3.8 or newer; it requires only the standard library.

## Relationship to prior work

Xie, Sun and Ge (2026) establish that binary differential-VT classes are perfect for correction and covering of two consecutive deletions, but their stated coverage result does not enumerate the number of codewords with each distinct-burst-output count. Babu, Krishnamoorthy, Roth and Siegel (2025) study cardinalities of differential-VT classes and their generating functions, not this sphere-size distribution. Nguyen, Cai and Siegel (2024) establish the general differential-VT coding constructions and synchronization correction framework. The current theorem refines the two global equalities \(W_a(1)=|\mathcal C_a|\) and \(W'_a(1)=2^{n-2}\) to every individual coefficient for powers of two; the previous equalities alone do not determine these coefficients.

## Limitations

The two-class phenomenon is proved for powers of two; no claim is made for arbitrary even lengths or nonbinary alphabets, and no decoding-complexity improvement is implied. The code-syndrome convention is explicit above, and changing conventions may permute exceptional residue labels. An equivalent formula might be implicit in prior cyclic-transfer-matrix or insertion/deletion-enumerator literature; no independent priority audit has been performed. Exact computation verifies finite examples only.

## References

1. C. Xie, Y. Sun, and G. Ge, *New bounds for covering codes under insertions or deletions*, arXiv:2606.15379v1, 13 June 2026, https://arxiv.org/abs/2606.15379.
2. S. Babu, M. Krishnamoorthy, R. Roth, and P. Siegel, *On Differential Varshamov–Tenengolts Codes*, 2025, https://cmrr-star.ucsd.edu/static/pubs/On_Differential_VT_Codes.pdf.
3. T. T. Nguyen, K. Cai, and P. H. Siegel, *A New Version of q-Ary Varshamov–Tenengolts Codes With More Efficient Encoders: The Differential VT Codes and The Differential Shifted VT Codes*, IEEE Transactions on Information Theory 70 (2024), https://doi.org/10.1109/TIT.2024.3417894.
