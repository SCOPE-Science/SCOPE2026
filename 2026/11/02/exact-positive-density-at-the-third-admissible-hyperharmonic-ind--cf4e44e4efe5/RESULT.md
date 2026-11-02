# Exact positive density at the third admissible hyperharmonic index, \(45\)

## Finding
For integers \(n,r\ge1\), let \(h_n^{(r)}\) be the hyperharmonic number of index \(n\) and order \(r\). Its standard identity is
\[
h_n^{(r)}=\binom{n+r-1}{n}\sum_{j=0}^{n-1}\frac1{r+j}.
\]
For \(n=45\), the set \(\mathcal I_{45}=\{r\in\mathbb Z_{>0}:h_{45}^{(r)}\in\mathbb Z\}\) is periodic with the explicit (not necessarily minimal) period
\[
M=1096405020816651129231648000.
\]
Exactly \(9588267818680320000\) of the \(M\) residue classes are admissible, giving the exact natural density
\[
\boxed{\delta_{45}=\frac{15810560}{1807915433082759}=0.00000000874518780618\ldots.}
\]
In particular \(r=692567016770669472150374656\) belongs to \(\mathcal I_{45}\). Among indices \(n>1\), the first three that admit integral hyperharmonic numbers are \(33,39,45\); the known positive cases for \(33,39\) are not new contributions.

## Assumptions and scope
Set \(F_n(X)=\prod_{j=0}^{n-1}(X+j)\in\mathbb Z[X]\), and \(P_n(X)=F_n'(X)\). The defining identity gives
\[
h_n^{(r)}=\frac{P_n(r)}{n!},\qquad
h_n^{(r)}\in\mathbb Z\quad\Longleftrightarrow\quad P_n(r)\equiv0\pmod{n!}.
\]
The prime factors of \(45!\) are exactly \(2,3,5,7,11,13,17,19,23,29,31,37,41,43\). Write \(e_p=\nu_p(45!)\), \(q_p=p^{e_p}\), and define \(m_p,\rho_p\) by the following **exact local table**, with \(\rho_p\) the number of roots of \(P_{45}\) modulo \(q_p\) among residues modulo \(m_p\):

| \(p\) | \(e_p\) | certified shift \(m_p\) | admissible residues \(\rho_p\) | first admissible residue |
|---:|---:|---:|---:|---:|
| 2 | 41 | 256 | 32 | 0 |
| 3 | 21 | 243 | 18 | 19 |
| 5 | 10 | 125 | 20 | 31 |
| 7 | 6 | 49 | 25 | 0 |
| 11 | 4 | 121 | 41 | 0 |
| 13 | 3 | 169 | 92 | 0 |
| 17 | 2 | 289 | 193 | 0 |
| 19 | 2 | 361 | 145 | 0 |
| 23 | 1 | 23 | 22 | 0 |
| 29 | 1 | 29 | 16 | 0 |
| 31 | 1 | 31 | 14 | 0 |
| 37 | 1 | 37 | 8 | 0 |
| 41 | 1 | 41 | 4 | 0 |
| 43 | 1 | 43 | 2 | 0 |

The scope is all positive integral orders \(r\); no unproved condition on primes, or statistical independence assumption, is used.

## Proof
**Polynomial congruence reduction.** Differentiating \(F_n\) gives \(P_n(X)=\sum_{j=0}^{n-1}\prod_{0\le i<n,\,i\ne j}(X+i)\), and the stated hyperharmonic identity follows after division by \(n!\). Thus the condition is a finite system of prime-power polynomial congruences.

**Global validity of finite shift certificates.** Let \(Q(X)\in\mathbb Z[X]\) have degree at most \(d\). If \(Q(0),\ldots,Q(d)\) all vanish modulo an integer \(q\), all its initial forward differences \(\Delta^jQ(0)\) vanish modulo \(q\). Newton's formula \(Q(X)=\sum_{j=0}^d\Delta^jQ(0)\binom Xj\) then proves \(q\mid Q(X)\) for **every** integer \(X\), because \(\binom Xj\in\mathbb Z\) at integral \(X\). Since \(P_{45}\) has degree \(44\), its shift difference \(P_{45}(X+m_p)-P_{45}(X)\) has degree at most \(43\). For each row of the table, the supplied verifier checks the **44** exact congruences
\[
P_{45}(x+m_p)\equiv P_{45}(x)\pmod{q_p},\qquad 0\le x\le43.
\]
The preceding lemma extends them to all integral \(x\), with no extrapolation from a finite experiment. The verifier also enumerates every \(0\le x<m_p\) and checks exactly \(\rho_p\) roots, using two algebraically distinct polynomial evaluators. This finite enumeration is exhaustive because of the proven shift property.

**Chinese remaindering and density.** Distinct \(m_p\) are powers of distinct primes, so are pairwise coprime. Consequently the Chinese remainder theorem gives exactly \(\prod_p\rho_p=9588267818680320000\) admissible residues modulo \(M=\prod_p m_p=1096405020816651129231648000\). Every positive order belongs to precisely one such residue class, so the exact natural density is their ratio, reducing to \(15810560/1807915433082759\). Applying CRT to the first-root column gives the displayed admissible order, which is also checked directly modulo \(45!\). This proves the complete claim about \(\mathcal I_{45}\).

**Why \(45\) is the third admissible index.** The published non-integrality theorem excludes all indices \(2\le n\le32\), all even indices, and prime-power indices. Published examples provide admissible orders at \(n=33,39\). In the interval \(34\le n\le44\), the only odd composite non-prime-power index other than \(39\) is \(35\). At \(n=35\), \(\nu_7(35!)=5\). The same finite-difference argument certifies \(P_{35}(X+49)\equiv P_{35}(X)\pmod{7^5}\) from the 34 values \(0\le X\le33\); exhaustive evaluation of the 49 residue classes \(X\pmod{49}\) finds **no** root. Hence \(h_{35}^{(r)}\notin\mathbb Z\) for all positive \(r\). Therefore \(33,39,45\) are the first three qualifying indices greater than one.

## Verification
Run \(`python3 verify.py`\) with any standard Python 3 interpreter. It performs exact modular product-derivative calculations for 14 prime powers, 616 global shift-certificate evaluations, 1,817 local residues, an independent prefix/suffix polynomial evaluation, CRT, an exact big-integer check of the displayed order, and the 35th-index 7-adic obstruction. The expected terminal marker is \(`VERIFY_OK`\). The shift lemma in the proof is what converts the finite certificates into statements for all integers. No claim is made that this verifier formalizes the external classification theorems used in establishing the ordinal position of \(45\).

## Relationship to prior work
Mező introduced the non-integrality question and expressed hyperharmonic numbers using binomial and harmonic quantities. Göral and Sertbaş proved extensive non-integrality criteria, including the low-index and even/prime-power obstructions. Sertbaş later constructed infinitely many integers at index \(33\). His 2025 density paper publicly identifies exact density computations at \(33\) and \(39\); the accessible abstract does not state the index-\(45\) exact density, the fourteen-row local spectrum, or the 35th-index obstruction. The 2025 paper's **full text was not available for inspection** through public routes or the available institutional-access action, so an unnoticed implication or appendix covering the present calculation is a specific unresolved literature risk. The present result does not reassert a general existence/density theorem as novel: it determines the next arithmetically motivated index and its exact rational constant.

## Limitations
The certified \(M\) is a period, not asserted minimal, and the explicit admissible \(r\) is not asserted least. The theorem concerns index \(45\), not all indices \(n\). The exact density is tiny and does not supply a uniform positive-density bound. The originality judgment is provisional and subject to an independent literature review, especially of the inaccessible 2025 full text. Finite modular computations are made exhaustive by the proved shift lemma, not by assuming that tested large samples reflect unbounded behavior.

## References
1. I. Mező, “About the Non-Integer Property of Hyperharmonic Numbers,” arXiv:0811.0043v1, public 2008-10-31. https://arxiv.org/abs/0811.0043
2. H. Göral and D. C. Sertbaş, “Almost all hyperharmonic numbers are not integers,” *Journal of Number Theory* 171 (2017), 495–526, DOI:10.1016/j.jnt.2016.07.023. https://doi.org/10.1016/j.jnt.2016.07.023
3. D. C. Sertbaş, “Hyperharmonic integers exist,” *Comptes Rendus Mathématique* 358 (2020), 1179–1185, DOI:10.5802/crmath.137. https://www.numdam.org/item/10.5802/crmath.137.pdf
4. D. C. Sertbaş, “Density results on hyperharmonic integers,” *Journal of the Mathematical Society of Japan* 77 (2025), 189–219, DOI:10.2969/jmsj/91179117. https://www.jstage.jst.go.jp/article/jmath/77/1/77_189/_article/-char/en
