# Arithmetic sixth-root resonance for three-line Fourier sampling

## Finding

Let \(q\ge2\) be any prime power, let \(\mathbb F_q\) be the field of order \(q\), let \(t\in\mathbb F_q^\times\), and let \(\psi:\mathbb F_q\to\mathbb C^\times\) be any nontrivial additive character. Define the three-line set
\[
E_t=\{(0,0)\}\cup\{(s,0),(0,s),(s,ts):s\in\mathbb F_q^\times\},
\qquad |E_t|=3q-2,
\]
and its principal Fourier sampling matrix
\[
M_t=\bigl(\psi(x_1y_1+x_2y_2)\bigr)_{x,y\in E_t}.
\]
Write \(N=q-1\), \(z=t^2\), and \(w=1+t^2\), using field operations in these last two definitions. Then its complex nullity is exactly as follows.

**Isotropic third direction.** If \(w=0\), then
\[
\dim_{\mathbb C}\ker M_t=\begin{cases}N/2,&\operatorname{char}\mathbb F_q\ne2,\\0,&\operatorname{char}\mathbb F_q=2.\end{cases}
\]

**Nonisotropic third direction.** If \(w\ne0\), let \(H=\langle z,w\rangle\le\mathbb F_q^\times\) and \(h=|H|\). Put \(\omega=e^{2\pi i/3}\) and \(\xi=e^{\pi i/3}\). Say that the parameter is *resonant* when there is a multiplicative character \(\vartheta:H\to\mathbb C^\times\) satisfying
\[
\vartheta(z)=\omega,\qquad\vartheta(w)=\xi.
\]
Then
\[
\dim_{\mathbb C}\ker M_t=
\begin{cases}2N/h,&\text{if resonant},\\0,&\text{otherwise}.\end{cases}
\]
Consequently \(\operatorname{rank}_{\mathbb C}M_t=3q-2-\dim_{\mathbb C}\ker M_t\) in every case. The result is independent of the chosen nontrivial additive character.

The resonance test is purely arithmetic. If \(w\ne0\), choose any generator \(g\) of \(\mathbb F_q^\times\) and write \(z=g^a\), \(w=g^b\). Resonance is possible only if \(6\mid N\). When this holds, it is equivalent to the simultaneous solvability in an integer \(k\) of
\[
ak\equiv N/3\pmod N,\qquad bk\equiv N/6\pmod N.
\]
Thus the theorem requires at most two finite-field discrete logarithms and two linear congruences. In particular **every field of characteristic two yields an invertible matrix for every nonzero \(t\)**.

For examples: at \(q=7,t=2\), the nullity is \(2\) and the rank is \(17\); at \(q=13,t=3\), they are \(4\) and \(33\); at \(q=13,t=5\), the third direction is isotropic and the nullity is \(6\) (rank \(31\)). These cases show that different arithmetic mechanisms and nonzero nullities occur in natural three-line configurations.

## Assumptions and scope

The three directions \((1,0)\), \((0,1)\), and \((1,t)\) are distinct because \(t\ne0\). The origin is included exactly once. The bilinear pairing is the standard symmetric dot product on \(\mathbb F_q^2\), and matrix rank and nullity are over \(\mathbb C\), not over \(\mathbb F_q\). The field may have any characteristic and any extension degree. No assumptions on the additive character beyond nontriviality are made. The theorem concerns an exponential *basis*, not orthogonality of the exponentials or the spectral-set property.

## Proof

Put \(u_1=(1,0)\), \(u_2=(0,1)\), \(u_3=(1,t)\). Their bilinear pairing matrix is
\[
A=(u_i\cdot u_j)_{1\le i,j\le3}=\begin{pmatrix}1&0&1\\0&1&t\\1&t&w\end{pmatrix}.
\]
Every function on \(E_t\) has one value at the origin and three functions on the punctured multiplicative arms. Expand each arm in the multiplicative characters of \(\mathbb F_q^\times\). This decomposes the function space into the four-dimensional constant-on-arms block \(V_1\) and the three-dimensional blocks
\[
V_\chi=\{f:f(0)=0,\ f(su_j)=c_j\chi(s)\ (s\ne0),\ 1\le j\le3\},
\]
one for each nontrivial multiplicative character \(\chi\). The dimensions add to \(4+3(N-1)=3q-2\).

**The constant block is nonsingular.** Write its coefficients as \((c_0,c_1,c_2,c_3)\). Since \(\sum_{s\ne0}\psi(as)\) equals \(N\) for \(a=0\) and \(-1\) otherwise, the sampled equations at the origin and on each arm are
\[
\begin{split}
&c_0+N(c_1+c_2+c_3)=0,\\
&c_0-c_1+Nc_2-c_3=0,\\
&c_0+Nc_1-c_2-c_3=0,\\
&c_0-c_1-c_2+\delta c_3=0,
\end{split}
\]
where \(\delta=-1\) if \(w\ne0\) and \(\delta=N\) if \(w=0\). When \(w\ne0\), subtracting the last equation from the middle two gives \(qc_1=qc_2=0\), then \(c_0=c_3=0\). When \(w=0\), the same subtraction gives \(c_1=c_2=c_3\), and the first and last equations then give \(2qc_3=0\). All scalar coefficients are complex; hence the constant block is injective in either case.

**The nontrivial blocks.** For nontrivial \(\chi\), put \(G(\chi)=\sum_{s\ne0}\chi(s)\psi(s)\). Elementary additive orthogonality gives \(|G(\chi)|^2=q\), so this number is nonzero. For \(r\ne0\),
\[
\sum_{s\ne0}\chi(s)\psi(rs a)=
\begin{cases}
0,&a=0,\\G(\chi)\chi((ra)^{-1}),&a\ne0.
\end{cases}
\]
Thus \(M_t\) maps \(V_\chi\) to \(V_{\chi^{-1}}\), and, after removal of the nonzero common Gauss factor, the corresponding three-by-three coefficient matrix is
\[
B_\chi=\begin{pmatrix}
1&0&1\\0&1&\chi(t^{-1})\\1&\chi(t^{-1})&b_\chi
\end{pmatrix},\qquad
b_\chi=\begin{cases}\chi(w^{-1}),&w\ne0,\\0,&w=0.\end{cases}
\]
The top-left two-by-two identity block implies that every singular \(B_\chi\) has nullity exactly one. When \(w\ne0\), its determinant vanishes exactly when
\[
\chi(w^{-1})=1+\chi(t^{-2}),
\quad\text{equivalently}\quad
\chi(w)=1+\chi(z),
\]
where the equivalence follows by complex conjugation because character values lie on the unit circle. When \(w=0\), the determinant vanishes exactly when \(\chi(-1)=-1\). The latter condition has exactly \(N/2\) solutions in odd characteristic and none in characteristic two.

For \(w\ne0\), both \(\chi(z)\) and \(\chi(w)\) are unit complex numbers. If \(y=1+x\) with \(|x|=|y|=1\), then \(2+2\operatorname{Re}x=1\), so \(x\) is \(\omega\) or \(\overline\omega\), while \(y\) is respectively \(\xi\) or \(\overline\xi\). Thus every singularity is one of precisely two conjugate sixth-root prescriptions on \(H=\langle z,w\rangle\). Every character of \(H\) extends to exactly \(N/h\) characters of the cyclic group \(\mathbb F_q^\times\). If one prescription extends, its conjugate does too, and the two sets are disjoint; otherwise neither contributes. This yields nullity \(2N/h\) or zero.

Finally, characters of \(\mathbb F_q^\times\) have the form \(\chi_k(g)=e^{2\pi ik/N}\). Imposing the prescribed values on \(g^a\) and \(g^b\) gives exactly the two stated congruences, and completes the proof.

## Verification

The accompanying standalone script `three_line_rank_checker.py` independently constructs the additive-character matrix and compares numerical singular-value nullities with the exact finite-field congruence prediction. It checks every nonzero slope across seventeen field models, comprising prime fields and extensions of degrees two, three, and four, for a total of **232 comparisons** and **36 singular parameter configurations**. All comparisons passed in the recorded execution. The script uses explicit polynomial-basis field arithmetic and canonical trace characters. These are finite corroborations only: the preceding Gauss-sum decomposition and character-extension count prove the theorem for every prime power.

## Relationship to prior work

Finite-field exponential bases, spectral sets, and Fourier zeros are studied in Iosevich–Mayeli–Pakianathan (2015) and Aten et al. (2015). Those papers' spectral/tiling criteria require orthogonality and do not give the rank of the specific principal matrix on a three-line union. In fact, for odd prime \(q>3\), \(|E_t|=3q-2\) need not be a permissible cardinality of an *orthogonally spectral set*, but invertibility of the nonorthogonal principal sampling matrix can still hold. Caragea–Lee (2024) analyze two-by-two and three-by-three principal Fourier minors of cyclic character tables; this is a different group and a different matrix size. The present arithmetic sixth-root criterion classifies a growing three-line family across all prime powers.

## Limitations

The classification is for the coordinate-normalized triple of lines with the standard dot pairing; it is not asserted for arbitrary triples of directions or arbitrary bilinear forms. It establishes exact rank, not singular values, conditioning, or orthogonal spectrality. The proof is self-contained modulo standard finite-field character orthogonality, which is also explicitly used in the proof. The originality comparison is bounded by the inspected references and indexed mathematical records; an older equivalent result expressed through multiplicative-character blocks remains possible. No independent mathematical validation has been carried out.

## References

1. A. Iosevich, A. Mayeli, J. Pakianathan, *The Fuglede Conjecture holds in \(\mathbb Z_p\times\mathbb Z_p\)*, arXiv:1505.00883v1, publicly submitted 5 May 2015. https://arxiv.org/html/1505.00883v1
2. C. Aten et al., *Tiling sets and spectral sets over finite fields*, arXiv:1509.01090v1, publicly submitted 3 September 2015. https://arxiv.org/html/1509.01090v1
3. A. Caragea and D. G. Lee, *On the principal minors of Fourier matrices*, arXiv:2409.09793, first submitted September 2024. https://arxiv.org/html/2409.09793v3
