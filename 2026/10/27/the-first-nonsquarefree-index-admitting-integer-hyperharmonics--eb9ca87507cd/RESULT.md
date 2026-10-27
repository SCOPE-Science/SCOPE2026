# The first nonsquarefree index admitting integer hyperharmonics

## Finding
For positive integers \(n,r\), let \(h_n^{(r)}\) denote the usual hyperharmonic number, recursively given by
\[
h_n^{(1)}=\sum_{j=1}^n\frac1j,\qquad h_n^{(r)}=\sum_{j=1}^n h_j^{(r-1)}\quad (r\ge2).
\]
The least nonsquarefree index \(n>1\) at which a hyperharmonic integer occurs is \(45\). More precisely, set
\[
M=45!=119622220865480194561963161495657715064383733760000000000,\qquad R=68700053771933018729983527085685223542008840099658203156.
\]
**Theorem.** For every integer \(k\ge0\),
\[
h_{45}^{(R+kM)}\in\mathbb Z.
\]
For every nonsquarefree integer \(n\) with \(2\le n<45\), and every positive integer \(r\), one has \(h_n^{(r)}\notin\mathbb Z\). In particular, the admissible orders at index \(45\) have natural density at least \(1/45!\). This does not determine their exact density.

## Assumptions and scope
All indices and orders are positive integers. An integer is nonsquarefree if some prime square divides it. Standard congruences and factorials are in \(\mathbb Z\). This theorem concerns the *least nonsquarefree index*, not the least index of any nontrivial integer hyperharmonic; known integer hyperharmonics occur at the squarefree index \(33\).

## Proof
For each positive integer \(n\), define the monic integer polynomial
\[
F_n(x)=\prod_{j=0}^{n-1}(x+j),\qquad P_n(x)=F_n'(x)=\sum_{j=0}^{n-1}\prod_{\substack{0\le i<n\\ i\ne j}}(x+i).
\]
The standard binomial--harmonic identity gives
\[
h_n^{(r)}=\binom{n+r-1}{n}\sum_{j=0}^{n-1}\frac1{r+j}=\frac{P_n(r)}{n!}.
\]
This equality is an identity of rationals for every positive \(n,r\); the polynomial expression includes no division by the individual factors.

We exhibit one complete congruence certificate for \(P_{45}(R)\equiv0\pmod{45!}\). For every prime \(p\le45\), the following table gives \(e=\nu_p(45!)\) and a positive integer \(t_p\) satisfying \(P_{45}(t_p)\equiv0\pmod{p^e}\):

| \(p\) | \(e\) | \(t_p\) | \(p\) | \(e\) | \(t_p\) |
|---:|---:|---:|---:|---:|---:|
| 2 | 41 | 20 | 3 | 21 | 19 |
| 5 | 10 | 31 | 7 | 6 | 1 |
| 11 | 4 | 11 | 13 | 3 | 8 |
| 17 | 2 | 7 | 19 | 2 | 13 |
| 23 | 1 | 2 | 29 | 1 | 14 |
| 31 | 1 | 18 | 37 | 1 | 30 |
| 41 | 1 | 38 | 43 | 1 | 42 |

All \(14\) displayed modular polynomial evaluations vanish exactly; `verify.py` recomputes each one using only integer multiplication. The same checker verifies that \(R\equiv t_p\pmod{p^e}\) for every row. Since the moduli are pairwise coprime and their product equals \(45!\), the Chinese remainder theorem implies
\[
P_{45}(R)\equiv0\pmod{45!}.
\]
Because \(P_{45}\in\mathbb Z[x]\), substituting congruent integers preserves the value modulo \(45!\):
\[
P_{45}(R+k45!)\equiv P_{45}(R)\equiv0\pmod{45!}\quad(k\ge0).
\]
The binomial--harmonic identity therefore proves the asserted integrality for every \(k\ge0\), not just those orders checked numerically. This supplies an actual infinite progression with density \(1/45!\).

To prove minimality, suppose \(n\) is nonsquarefree and \(1<n<45\). If \(n\) is odd and not a prime power, then it has at least two distinct odd prime factors and one squared prime factor. The smallest such possibility is \(3^2\cdot5=45\), a contradiction. Consequently every nonsquarefree \(n<45\) is either even or an odd prime power. The established nonintegrality theorem of Göral and Sertbaş rules out \(h_n^{(r)}\in\mathbb Z\) for every positive \(r\) when \(n\) is even or a prime power. This completes the proof.

## Verification
`verify.py` is a standalone Python 3 standard-library checker. It independently reconstructs all fourteen \(45!\) prime-power factors, recomputes all modular derivative zeros, checks the Chinese-remainder certificate, and directly evaluates the hyperharmonic identity as an exact reduced rational at orders \(R\), \(R+45!\) and \(R+2\cdot45!\). All three values have denominator one. It also checks the elementary index classification below \(45\).

The infinite progression follows *symbolically* from polynomial congruence invariance; the three sample evaluations are additional cross-checks. The minimality argument invokes the previously published nonintegrality theorem and does not rely on finite enumeration.

## Relationship to prior work
Mező posed the integrality question in 2008. Göral and Sertbaş proved that even and prime-power indices cannot support integer hyperharmonics. Sertbaş subsequently exhibited integer hyperharmonics at the squarefree index \(33\), while his later density paper gives exact densities at indices \(33\) and \(39\). Those known results establish neither the minimal nonsquarefree index nor the explicit \(45\)-index congruence certificate.

The 2025 density paper is particularly relevant, but only its abstract was accessible in the present literature inspection; its full body was not read. Its abstract identifies \(33\) and \(39\) as the exact-density examples and does not mention \(45\). A previously reported congruence progression or a general theorem implying this case may exist in that uninspected body or elsewhere, so originality remains subject to human literature verification.

## Limitations
This result identifies the first nonsquarefree admissible index and one explicit positive-density progression of orders; it does not classify all integer hyperharmonic indices or give the exact order-density at \(45\). The modular table and executable checker are finite certificates of explicit congruences; the infinitely many orders are proved by the polynomial argument. No independent mathematical audit has been performed.

## References
1. I. Mező, *About the Non-Integer Property of Hyperharmonic Numbers*, arXiv:0811.0043 (first posted 31 October 2008), https://arxiv.org/abs/0811.0043.
2. H. Göral and D. C. Sertbaş, *Almost all hyperharmonic numbers are not integers*, Journal of Number Theory **171** (2017), 495–526, https://doi.org/10.1016/j.jnt.2016.07.023.
3. D. C. Sertbaş, *Hyperharmonic integers exist*, Comptes Rendus Mathématique **358** (2020), 1179–1185, https://doi.org/10.5802/crmath.137.
4. D. C. Sertbaş, *Density results on hyperharmonic integers*, Journal of the Mathematical Society of Japan **77** (2025), 189–219, https://doi.org/10.2969/jmsj/91179117 (abstract inspected; full text inaccessible).
5. E. Alkan, H. Göral and D. C. Sertbaş, *Hyperharmonic numbers can rarely be integers*, INTEGERS **18** (2018), A43, https://math.colgate.edu/~integers/s43/s43.pdf.
