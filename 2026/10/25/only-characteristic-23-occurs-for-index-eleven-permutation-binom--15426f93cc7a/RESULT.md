# Only characteristic 23 occurs for index-eleven permutation binomials

## Finding
For a prime \(p\), a positive integer \(m\), and \(q=p^m\), consider all polynomials
\[
f(X)=X^r(X^s+a)\in\mathbb F_q[X],\qquad r,s\ge1,\quad a\in\mathbb F_q^\times.
\]
Set \(g=\gcd(s,q-1)\) and let \(\mathcal P_g\) consist of the prime characteristics for which *some* such polynomial permutes *some* finite field \(\mathbb F_{p^m}\) of that characteristic. Then
\[
\boxed{\mathcal P_{11}=\{23\}.}
\]
The conclusion covers every extension degree, coefficient, and positive exponent satisfying the index condition. In particular, characteristics \(67\), \(89\), and \(199\), although divisors of the relevant Wendt determinant, never occur in any extension.

## Assumptions and scope
All fields are finite, \(p\) is prime, \(m,r,s\ge1\), \(a\ne0\), and the index is exactly \(\gcd(s,p^m-1)=11\). The assertion concerns admissible **prime characteristics**, not a classification of the individual permutation polynomials within characteristic \(23\). The proof uses the necessary product and inverse-power-sum identities established in [1]; their hypotheses include \(t=(q-1)/11>2\) for application at indices \(j=1,2\).

## Proof
**Step 1: Reduce to four primes.** The Wendt obstruction [1, Proposition 2.2] shows that if a polynomial of index \(11\) permutes \(\mathbb F_q\), then \(p\) divides
\[
W_{11}=\operatorname{Res}_X\bigl(X^{11}-1,(X+1)^{11}-1\bigr).
\]
An exact Sylvester-determinant evaluation gives
\[
W_{11}=101832157445630503=23^5\cdot67^2\cdot89\cdot199^2.
\]
The standalone exact-arithmetic verifier computes the integer determinant and checks this factorization directly. Thus only \(p\in\{23,67,89,199\}\) can occur.

**Step 2: Set up the two necessary inverse-power sums.** Suppose \(p\in\{67,89,199\}\) and an index-eleven binomial permutes \(\mathbb F_q\). Put \(t=(q-1)/11\), so \(t\ge6\), and choose \(b\in\{0,\ldots,t-1\}\) as in quotient normalization [1, Lemma 2.5]. Let
\[
\zeta=(-a)^t,\qquad U_1=t-b,\qquad U_2=t-(2b\bmod t).
\]
The product obstruction [1, Lemma 2.1] yields
\[
\zeta^{11}=1,\quad\zeta\ne1,\quad(\zeta-1)^{11}\in\{1,-1\}.
\]
Each candidate satisfies \(p\equiv1\pmod{11}\), so all roots of \(Z^{11}-1\) belong to \(\mathbb F_p\); in particular, \(\zeta\in\mathbb F_p\). Also
\[
U_2\equiv2U_1\ \text{or}\ 2U_1-t\pmod p,
\qquad t\equiv-11^{-1}\pmod p.
\]
Let \(P_k(T,X,Y)\) be the integer polynomial from [1, Lemma 3.2], defined by
\[
P_1=1,\qquad P_{k+1}=\bigl((X-k)(Y-1)-kTY\bigr)P_k+TY(Y-1)\frac{\partial P_k}{\partial Y}.
\]
The two inverse-power-sum necessities [1, Lemma 3.3] are
\[
P_{11}(-11^{-1},U_1,\zeta)=0,
\qquad P_{22}(-11^{-1},U_2,\zeta)=0\quad\text{in }\mathbb F_p.
\]
Here \(11,22<p\), so no factorial-zero degeneration is involved.

**Step 3: An exhaustive small finite certificate.** For each of the three primes, enumerate precisely the \(\zeta\in\mathbb F_p\) satisfying the product constraints, then the \(x\in\mathbb F_p\) satisfying the first inverse-power-sum equation. The complete output is below. In the last column, the pair consists of the two values
\(P_{22}(-11^{-1},2x,\zeta)\) and \(P_{22}(-11^{-1},2x-t,\zeta)\), reduced modulo \(p\).

| \(p\) | \(\zeta\) | permitted first-sum root \(x\) | second-sum residues |
|---:|---:|---:|:---|
|67|9|27|(34, 11)|
|67|9|34|(47, 52)|
|67|15|50|(66, 21)|
|67|15|57|(32, 38)|
|67|25|19|(38, 31)|
|67|59|65|(38, 12)|
|89|2|43|(14, 51)|
|89|45|65|(13, 28)|
|199|61|69|(3, 127)|
|199|61|180|(23, 129)|
|199|62|48|(108, 10)|
|199|62|159|(185, 183)|
|199|63|none|—|
|199|139|none|—|

These are all possibilities: the \(\zeta\) values are exactly \(\{9,15,25,59\}\), \(\{2,45\}\), and \(\{61,62,63,139\}\) for the three primes, respectively. Every displayed second-sum residue is nonzero, and the final two cases already fail the first equation. Since \(U_1\) reduces to some \(x\in\mathbb F_p\) and \(U_2\) must reduce to one of the two tested choices, the two necessary equations cannot hold simultaneously. Thus none of these three characteristics occurs, in *any* extension degree.

**Step 4: Realize \(23\).** Over \(\mathbb F_{23}\), the polynomial
\[
f(X)=X^{12}+2X=X(X^{11}+2)
\]
has \(\gcd(11,22)=11\). Euler's criterion gives \(X^{11}=1\) for nonzero squares and \(-1\) for nonsquares, so \(f\) is multiplication by \(3\) on the nonzero squares and the identity on nonsquares. Since \(3=7^2\pmod{23}\), both pieces are permuted separately; \(0\) is fixed. Hence \(23\in\mathcal P_{11}\), proving the classification.

## Verification
Run `python3 verify.py` using Python 3 with no third-party packages. It computes the full integer Sylvester determinant by exact Bareiss elimination, verifies its stated complete prime factorization, exhaustively enumerates each relevant \(\zeta\) and first-sum residue, and checks that both possible second-sum values are nonzero. A separate polynomial-recurrence evaluation independently checks all candidate vanishing and nonvanishing tests against the generating-coefficient method. The script also directly evaluates the \(23\)-element permutation witness. The complete run prints `CERTIFICATE_OK 24 nonzero second-sum residues` and `WITNESS_OK`.

The proof for all field sizes is the reduction to this finite certificate, **not** extrapolation from finite samples of extension degrees. Reproducing the result requires exact integer and prime-field arithmetic, not floating-point computation.

## Relationship to prior work
Tang and Fan [1] proved characteristic finiteness via Wendt's determinant and classified all index values through \(10\) over arbitrary finite extensions. Their Corollary 5.2 classifies **only prime fields** at index \(11\), identifying characteristic \(23\); they do not eliminate the other determinant primes for arbitrary extensions. The present theorem closes that extension-field gap by simultaneously enforcing their first two inverse-power-sum conditions. The determinant factorization is listed independently in [4], but it supplies only candidate primes, not admissibility. Earlier work [2] gives a prime-field characteristic bound and a conditional descent argument for some extension degrees; it does not cover all possible extension degrees here. The broad family classified in [3] has index \(q_0-1\) for a prime-power base \(q_0\), which cannot equal \(11\). Search comparisons found no published implication covering the unrestricted index-eleven classification.

## Limitations
This theorem does not enumerate the individual binomials in characteristic \(23\), nor does it classify index \(12\) or higher. It depends on the published necessary identities [1], whose hypotheses were checked for each excluded prime; the additional finite exclusions are supplied and independently replayed here. Discovery of a previously unlocated covering theorem remains possible. There has been no independent mathematical audit.

## References
[1] Zhichao Tang and Xiang Fan, *Wendt's Determinant and Finiteness of Prime Characteristics for Permutation Binomials*, arXiv:2610.18584v1, first publicly submitted 2026-10-13. https://arxiv.org/html/2610.18584v1

[2] Mohamed Ayad, Kacem Belghaba, Omar Kihel, *On Permutation Binomials over Finite Fields*, arXiv:1210.1252 (2012); Bulletin of the Australian Mathematical Society 89 (2014), 112–124. https://arxiv.org/abs/1210.1252

[3] Xiang Fan, *A Complete Classification of Permutation Binomials of the Form \(X^r(X^{q-1}+a)\) over Finite Fields*, arXiv:2609.20354v1 (2026). https://arxiv.org/abs/2609.20354

[4] Gérard P. Michon, *Factorization of Wendt's Determinant*, Numericana. https://www.numericana.com/data/wendt.htm
