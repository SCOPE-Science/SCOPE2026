# Sharp finite Cesàro self-commutator endpoint norm and boundary doubling

## Finding
For each integer \(n\ge2\), form the finite Cesàro averaging matrix \(H_n\) and its Hilbert-space self-commutator \(K_n=H_n^{\mathsf T}H_n-H_nH_n^{\mathsf T}\). The induced coordinatewise supremum norm of \(K_n\), on real or complex \(\ell^\infty_n\), is given **exactly at every size** by
\[
\boxed{\|K_n\|_{\infty\to\infty}=2m_n\sum_{k=m_n+1}^{n}\frac1{k^2},\quad m_n=\max\left\{1\le j<n:\frac1j<\sum_{k=j}^{n}\frac1{k^2}\right\}.}
\]
The maximum absolute row sum is achieved in the first row; for \(n\ge3\) this maximizing row is unique. A two-valued sign-step input changing sign after coordinate \(m_n\) attains the sharp bound. For \(n=2\), both rows maximize.

The switching index obeys \(m_n=\sqrt{n/2}+O(1)\), and the norm has a two-term sharp finite-size expansion
\[
\boxed{\|K_n\|_{\infty\to\infty}=2-2\sqrt{\frac2n}+\frac{2}{3n}+O(n^{-3/2})\qquad(n\to\infty).}
\]
In contrast, the self-commutator \(J=H^*H-HH^*\) of the ordinary **infinite** Cesàro operator on \(\ell^2\) has a canonical bounded kernel extension to \(\ell^\infty\) with \(\|J\|_{\infty\to\infty}=1\). The factor-two limiting discrepancy is caused by an explicit rank-one boundary correction in finite sections. In particular, a finite section of the infinite self-commutator is not the self-commutator of the finite Cesàro section.

## Assumptions and scope
For \(n\ge2\), use row and column indices \(i,j\in\{1,\ldots,n\}\) and define
\[
(H_n)_{ij}=\begin{cases}1/i,&j\le i,\\0,&j>i.\end{cases}
\]
The matrix \(K_n=H_n^{\mathsf T}H_n-H_nH_n^{\mathsf T}\) is symmetric, and \(\|K_n\|_{\infty\to\infty}\) means the induced \(\ell^\infty_n\) norm, equivalently the maximum absolute row sum; it is **not** the spectral norm. Define
\[
a_j=\frac1j-\sum_{k=j}^{n}\frac1{k^2},\qquad 1\le j\le n.\]
The integer \(m_n\) in the theorem is the largest index with \(a_j<0\). Such an index exists and is less than \(n\). All sharpness claims hold over both real and complex scalars.

For the infinite operator, define \((Hx)_i=i^{-1}\sum_{j=1}^i x_j\) initially on \(\ell^2(\mathbb N)\); Hardy's inequality makes it bounded there. The infinite self-commutator \(J=H^*H-HH^*\) is understood on \(\ell^2\), and the \(\ell^\infty\) norm refers to its separately defined, absolutely row-summable matrix kernel. No boundedness of \(H^*\) on \(\ell^\infty\) is assumed.

## Proof
**1. The finite kernel and unique sign change.** Direct matrix multiplication gives
\[
(H_n^{\mathsf T}H_n)_{ij}=\sum_{k=\max(i,j)}^n\frac1{k^2},\quad
(H_nH_n^{\mathsf T})_{ij}=\frac1{\max(i,j)},\quad
(K_n)_{ij}=-a_{\max(i,j)}.
\]
Moreover
\[
a_{j+1}-a_j=\frac1{j^2(j+1)}>0,\quad a_1=-\sum_{k=2}^n\frac1{k^2}<0,\quad a_n=\frac{n-1}{n^2}>0.
\]
Consequently the signs switch exactly once, allowing a possible zero value at the boundary. Exchanging finite sums also gives
\[
\sum_{j=1}^n a_j=\sum_{j=1}^n\frac1j-\sum_{k=1}^n\frac{k}{k^2}=0.
\]

**2. The first row is sharp.** The absolute row sum at row \(i\) equals
\[
R_i=i|a_i|+\sum_{j=i+1}^n|a_j|.
\]
The consecutive difference is
\[
R_{i+1}-R_i=i\bigl(|a_{i+1}|-|a_i|\bigr).
\]
Because the sequence \((a_i)\) increases strictly, its absolute values first decrease and then increase, possibly with a single flat link. Thus \((R_i)\) first decreases and then increases, so its maximum lies at one of the endpoint rows. The final row has \(R_n=n|a_n|=(n-1)/n\), whereas the zero sum of the \(a_j\) gives
\[
R_1=\sum_{j=1}^n|a_j|\ge 2|a_1|=2\sum_{k=2}^n k^{-2}\ge\sum_{k=2}^n\frac1{k(k-1)}=\frac{n-1}{n}.
\]
The last inequality uses \(2/k^2\ge1/[k(k-1)]\), with strict inequality for \(k\ge3\). Hence \(R_1\ge R_n\), strictly if \(n\ge3\); the first link also decreases strictly when \(n\ge3\), and the one-valley structure makes row one the unique maximizer then. The case \(n=2\) has tied endpoint rows. Since the \(a_j\) have zero sum,
\[
R_1=-2\sum_{j=1}^{m_n}a_j=2m_n\sum_{k=m_n+1}^n k^{-2},
\]
where the final equality follows from interchanging the finite double sum. This proves the exact norm formula. Taking the input equal to \(-1\) before and including \(m_n\), and \(+1\) afterward, makes every nonzero entry in the first output coordinate have the same sign, and hence attains the norm. A global unimodular factor is harmless.

**3. Location and asymptotics.** Put
\[
\tau_n=\sum_{k=n+1}^\infty\frac1{k^2},\qquad
b_j=\sum_{k=j}^\infty\frac1{k^2}-\frac1j;
\]
then \(a_j=\tau_n-b_j\). Euler--Maclaurin summation with the conventional integral remainder gives, as positive indices diverge,
\[
\tau_n=\frac1n-\frac1{2n^2}+O(n^{-3}),\qquad
b_j=\frac1{2j^2}+\frac1{6j^3}+O(j^{-5}).
\]
The sequence \((b_j)\) decreases strictly. Inserting the two expansions into the inequalities \(b_{m_n}>\tau_n\ge b_{m_n+1}\) and testing the integers within fixed distance of \(\sqrt{n/2}\) shows that
\[
m_n=\sqrt{n/2}+O(1).
\]
The same expansions give, uniformly for this sequence of indices,
\[
\begin{aligned}
2m_n\sum_{k=m_n+1}^n\frac1{k^2}
&=2-\frac1{m_n}-\frac{2m_n}{n}+\frac1{3m_n^2}
 +O(m_n^{-4}+m_n n^{-2}).
\end{aligned}
\]
Writing \(m_n=\sqrt{n/2}+O(1)\), the first derivative of \(m\mapsto1/m+2m/n\) vanishes at \(m=\sqrt{n/2}\). Taylor's formula therefore yields
\[
\frac1{m_n}+\frac{2m_n}{n}=2\sqrt{\frac2n}+O(n^{-3/2}),\qquad
\frac1{3m_n^2}=\frac{2}{3n}+O(n^{-3/2}),
\]
which proves the expansion. No finite-size computation is used in place of these all-size estimates.

**4. Infinite endpoint and rank-one boundary defect.** For the infinite \(\ell^2\) Cesàro operator, direct multiplication gives
\[
J_{ij}=b_{\max(i,j)},\qquad b_j>0,\quad b_j-b_{j+1}=\frac1{j^2(j+1)}>0.
\]
For \(N\ge1\), an exchange of sums shows
\[
\sum_{j=1}^N b_j=N\sum_{k=N+1}^\infty\frac1{k^2}=N\tau_N\longrightarrow1.
\]
Every kernel row has a finite absolute sum. The row-sum difference between consecutive rows equals \(i(b_{i+1}-b_i)<0\), so the maximum row sum occurs at row one and equals \(\sum_{j=1}^\infty b_j=1\). Positivity and the constant test vector show that the induced \(\ell^\infty\) kernel norm is exactly \(1\). Finally, because \(a_j=\tau_n-b_j\), for the coordinate projection \(P_n\) onto the first \(n\) basis vectors,
\[
K_n=P_nJP_n-\tau_n\boldsymbol1_n\boldsymbol1_n^{\mathsf T},\qquad n\tau_n\to1.
\]
Thus finite-section formation creates a rank-one term of nonvanishing endpoint norm, explaining why the finite commutator norm tends to \(2\), not the infinite kernel norm \(1\).

## Verification
The supplementary standalone standard-library script `cesaro_finite_commutator_check.py` builds the finite matrices with exact rational entries and checks their commutator kernels, all absolute row sums, uniqueness of the first maximizing row for each \(3\le n\le24\), and the sign-step maximizing vectors. It also numerically checks the asymptotic formula for selected dimensions through \(n=50000\). Running `python cesaro_finite_commutator_check.py` completes with its `PASS` line. The proof above, rather than the finite experiments, establishes the formula and asymptotic law for every admissible size.

## Relationship to prior work
Brown--Halmos--Shields [1] studies the classical infinite Cesàro operator and its hyponormality; it does not state the finite-matrix \(\ell^\infty\) self-commutator norm. Lacruz--León-Saavedra--Petrovic--Zabeti [2] investigate extended eigenvalues of continuous and discrete Cesàro operators and do not study the present finite sections. Gül [3] develops essential normality of the infinite operator, not sharp finite \(\ell^\infty\) matrix norms.

The published *Cubic spectral decay of the classical Cesàro self-commutator* [4] proves infinite-operator eigenvalue and Schatten results using an infinite kernel; that work does not evaluate the noncommuting finite-section correction or the sharp finite \(\ell^\infty\) endpoint. *Finite Gram reduction of sharp Cesàro self-commutator bounds at every order* [5] establishes weighted infinite-dimensional \(\ell^2\) quadratic-form constants, rather than the present finite row-sum norm. Their conclusions do not imply the signed-row maximizer and the explicit boundary-doubling coefficient shown here. A direct row-kernel calculation is elementary once these finite truncations are considered; historical equivalent calculations outside indexed literature remain possible.

## Limitations
The result concerns the classical *unweighted* first-order Cesàro matrices, their Hilbert-adjoint commutators, and the induced coordinatewise maximum norm, not general Cesàro weights, \(\ell^2\) spectral norms, or commutators of operators originally defined on \(\ell^\infty\). The asymptotic error is a bound of order \(n^{-3/2}\), not a claim of a further universal coefficient. Relevant literature may contain an unindexed equivalent finite-section row-sum calculation; the scope of the primary-source search cannot eliminate this residual risk. No independent scientific validation was performed.

## References
1. A. Brown, P. R. Halmos, and A. L. Shields, *Cesàro Operators*, Acta Sci. Math. (Szeged) **26** (1965), 125–137. Full text: https://acta.bibl.u-szeged.hu/14062/1/math_026_fasc_001_002_125-137.pdf
2. M. Lacruz, F. León-Saavedra, J. Petrovic, and O. Zabeti, *Extended eigenvalues for Cesàro operators*, arXiv:1403.4844v1, first public 2014-03-19. https://arxiv.org/abs/1403.4844
3. U. Gül, *The Cesaro Operator in \(\ell^2\) is Essentially Normal*, arXiv:2311.15245v1 (2023), full text: https://arxiv.org/pdf/2311.15245
4. *Cubic spectral decay of the classical Cesàro self-commutator* (2026), published mathematical result: https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-cubic-spectral-decay-of-the-classical-ces-ro-self-commutator--1d9ae52b1d38
5. *Finite Gram reduction of sharp Cesàro self-commutator bounds at every order* (2026), published mathematical result: https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-finite-gram-reduction-of-sharp-ces-ro-self-commutator-bounds-at--2747cc29070a
