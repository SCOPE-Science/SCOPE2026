# The index-eleven characteristic spectrum of permutation binomials over all finite fields

## Finding
For a prime \(p\), let \(\mathcal P_{11}\) mean that there exist positive integers \(m,r,s\), a nonzero \(a\in\mathbb F_{p^m}\), and a permutation of \(\mathbb F_{p^m}\) induced by \(f(X)=X^r(X^s+a)\) such that \(\gcd(s,p^m-1)=11\). Then
\[
\mathcal P_{11}\quad\Longleftrightarrow\quad p=23.
\]
Thus the only possible prime characteristic is \(23\), even when arbitrary extension degrees and exponents are permitted. The example \(f(X)=X^{12}+2X\) over \(\mathbb F_{23}\) realizes it.

## Assumptions and scope
Every finite field is of order \(Q=p^m\), with \(p\) prime and \(m\ge1\). All exponents are positive integers and \(a\ne0\). The assertion classifies possible prime characteristics, **not** all parameters \((m,r,s,a)\) in characteristic \(23\). The proof below eliminates the other Wendt-determinant primes by exact finite-field certificates, valid uniformly over all extension degrees.

## Proof
Put \(g=\gcd(s,Q-1)=11\), \(t=(Q-1)/11\), \(u=s/11\). Since \(\gcd(u,t)=1\), choose \(b\in\{0,\ldots,t-1\}\) with \(bu\equiv r\pmod t\). If \(f\) is a permutation, then \(\gcd(r,11)=1\) and the quotient map
\[
\psi(y)=y^b(y+a)^{11},\qquad y\in\mu_t=\{y\in\mathbb F_Q^\times:y^t=1\},
\]
permutes \(\mu_t\). Indeed, the map \(x\mapsto x^{11}\) identifies the nonzero \(11\)-torsion fibers with \(\mu_t\), and \(f(x)^{11}=\psi((x^{11})^u)\). Let \(\zeta=(-a)^t\). Nonzero-root exclusion gives \(\zeta\ne1\) and \(\zeta^{11}=1\). Multiplying \(f(x)/x^r\) over all \(x\ne0\) yields
\[
(\zeta-1)^{11}=(-1)^{r-1}.
\]
According to the parity of \(r\), either \(\eta=\zeta\) or \(\eta=\zeta^{-1}\) satisfies \(\eta^{11}=(\eta-1)^{11}=1\). Hence the polynomials \(X^{11}-1\) and \((X+1)^{11}-1\) have a common zero modulo \(p\). Their exact integer resultant is
\[
W_{11}=101832157445630503=23^5\,67^2\,89\,199^2.
\]
Therefore \(p\in\{23,67,89,199\}\). The resultant identity is independently reconstructed by the supplied integer Sylvester/Bareiss calculation.

It remains to eliminate \(p=67,89,199\) over **all** extension fields. For each such prime, \(11\mid p-1\), so all roots of \(Z^{11}=1\) in every extension already lie in \(\mathbb F_p\); hence \(\zeta\in\mathbb F_p\). Also \(t\ge(p-1)/11\ge6\), and \(22<p\).

Define the polynomials \(P_k(T,U,Z)\) over \(\mathbb Z\) by
\[
P_1=1,\qquad P_{k+1}=\big[(U-k)(Z-1)-kTZ\big]P_k+TZ(Z-1)\,\partial_Z P_k.
\]
For every \(1\le U\le t\), partial fractions give
\[
\sum_{y^t=1}\frac{y^U}{w-y}=\frac{tw^{U-1}}{w^t-1}.
\]
Differentiating \(k-1\) times, and using the displayed recurrence, gives
\[
\frac{d^{k-1}}{dw^{k-1}}\frac{tw^{U-1}}{w^t-1}
=\frac{tw^{U-k}}{(w^t-1)^k}P_k(t,U,w^t).
\]
As \(\psi\) permutes \(\mu_t\), both reciprocal power sums \(\sum_{y\in\mu_t}\psi(y)^{-j}\) vanish for \(j=1,2\). Since \(11j<p\), the factorials introduced by differentiation are invertible. With \(U_j=t-(jb\bmod t)\) and \(\tau=-11^{-1}\in\mathbb F_p\), this proves
\[
P_{11}(\tau,U_1,\zeta)=0,\qquad P_{22}(\tau,U_2,\zeta)=0.
\]
Moreover, if \(c=\lfloor2b/t\rfloor\in\{0,1\}\), then \(U_2=2U_1+(c-1)t\), and because \(11t=Q-1\equiv-1\pmod p\),
\[
U_2\equiv2U_1+(1-c)11^{-1}\pmod p.
\]

An exact calculation in each prime field now finishes the proof. The certificate enumerates every \(\zeta\in\mathbb F_p\) satisfying \(\zeta\ne1\), \(\zeta^{11}=1\), and \((\zeta-1)^{11}\in\{1,-1\}\); then every root \(U\in\mathbb F_p\) of \(P_{11}(\tau,U,\zeta)\); then both possible \(P_{22}\) residues. Entries in the last column are the ordered residues for \(c=0,1\), respectively:

| \(p\) | \(\zeta\) | \(U\) roots of \(P_{11}\) | Corresponding \(P_{22}\) residue pairs |
|---|---|---|---|
| 67 | 9 | 27, 34 | (11,34); (52,47) |
| 67 | 15 | 50, 57 | (21,66); (38,32) |
| 67 | 25 | 19 | (31,38) |
| 67 | 59 | 65 | (12,38) |
| 89 | 2 | 43 | (51,14) |
| 89 | 45 | 65 | (28,13) |
| 199 | 61 | 69, 180 | (127,3); (129,23) |
| 199 | 62 | 48, 159 | (10,108); (183,185) |
| 199 | 63, 139 | none | not applicable |

None of the displayed residues is zero, excluding each candidate in every extension degree. Finally, over \(\mathbb F_{23}\), \(f(x)=x^{12}+2x\) maps the nonzero squares to \(3x\) and fixes the nonsquares. The element \(3=7^2\) is a square modulo \(23\), so this map and \(f(0)=0\) are bijective. This exhibits the required characteristic \(23\), completing the proof.

## Verification
Run `python3 verify.py`. The standalone script computes \(W_{11}\) using an exact \(22\times22\) Sylvester determinant with fraction-free Bareiss elimination, verifies the proposed prime factorization and primality, constructs \(P_{11}\) and \(P_{22}\) by the stated polynomial recurrence over each finite prime field, exhaustively enumerates all admissible \((\zeta,U,c)\), and checks the \(23\)-element witness permutation. It prints `CERTIFICATE_OK`. No network access, external dependencies, numerical approximations, or precomputed tables are required. The script checks finite algebraic certificates; the analytic reduction from arbitrary extensions to these certificates is proved above.

## Relationship to prior work
Ni–Pang–Yu–Yuan (2026, arXiv:2609.28595v1) completely characterize the structured binomials \(X^r(X^{q-1}+a)\) over \(\mathbb F_{q^e}\). In that family, the fixed gcd of the exponent difference with \(q^e-1\) is \(q-1\), which cannot be \(11\) because \(q=12\) is not a prime power. The unrestricted exponent-index characteristic question is therefore not implied by their classification. Fan (2026, arXiv:2609.20354v1) treats the related coprime-index family, which likewise does not contain fixed index \(11\).

Tang–Fan (2026, arXiv:2610.18584v1) subsequently establish Wendt-determinant restrictions and the prime-field \(g=11\) classification \(p=23\). Their Corollary 5.2 only concerns prime fields, and the general finiteness theorem does not eliminate \(67\), \(89\), or \(199\) over arbitrary extension fields. The extra reciprocal-moment certificate above eliminates exactly those remaining characteristics. Ayad–Belghaba–Kihel (2014) give bounds in prime fields but do not establish this extension-field spectrum. The necessary quotient and power-sum identities have been derived explicitly above for reproducibility.

## Limitations
The theorem establishes possible characteristics, not all permutation binomials in characteristic \(23\). The argument does not provide a classification at other fixed indices. The finite certificate exhausts small *prime-field parameter residues* of necessary conditions, not all polynomials in unbounded extension fields; the reduction justifying this is essential. An earlier implicit derivation of the characteristic spectrum from broader permutation-binomial theory remains an originality risk pending independent assessment.

## References
- J. Ni, X. Pang, J. Yu, and P. Yuan, *Permutation binomials of the form \(X^r(X^{q-1}+a)\) over finite fields*, arXiv:2609.28595v1 (2026-09-23), https://arxiv.org/abs/2609.28595.
- X. Fan, *A complete classification of permutation binomials of the form \(X^r(X^{q-1}+a)\) over finite fields*, arXiv:2609.20354v1 (2026-09-17), https://arxiv.org/abs/2609.20354.
- Z. Tang and X. Fan, *Wendt's determinant and finiteness of prime characteristics for permutation binomials*, arXiv:2610.18584v1 (2026-10-13), https://arxiv.org/abs/2610.18584.
- M. Ayad, K. Belghaba, and O. Kihel, *On permutation binomials over finite fields*, Bull. Aust. Math. Soc. 89 (2014), 112–124, DOI:10.1017/S0004972713000208.
