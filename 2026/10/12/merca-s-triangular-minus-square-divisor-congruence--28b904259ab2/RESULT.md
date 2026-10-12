# Merca's triangular-minus-square divisor congruence
## Finding
Let \(\tau(N)=\sigma_0(N)\) denote the number of positive divisors of \(N\), and let \(T_m=m(m+1)/2\). For every integer \(n\ge 0\),
\[
4\nmid \tau(8n+1)\quad\Longrightarrow\quad n=T_m-r^2
\]
for some integers \(m,r\ge 0\). Equivalently, if \(n\) is not the difference between a triangular number and a square, then
\[
\tau(8n+1)\equiv 0\pmod 4.
\]
Thus Conjecture 5 of Merca (2022) holds.

More precisely, put \(N=8n+1\). If \(4\nmid\tau(N)\), then either \(N\) is a square, or there is a unique prime \(p\) occurring to an odd exponent and
\[
N=p^{4a+1}v^2,\qquad p\equiv 1\pmod 8,\qquad p\nmid v.
\]
In the second case a representation \(p=A^2-8B^2\) yields the explicit witness
\[
N=(Ap^{2a}v)^2-8(Bp^{2a}v)^2,
\]
and hence \(n=T_m-r^2\) with \(2m+1=Ap^{2a}v\) and \(r=Bp^{2a}v\).

## Assumptions and scope
All variables are ordinary integers. The statement covers every \(n\ge 0\); it is not an asymptotic or finite-range assertion. The only standard inputs are unique factorization of integers, quadratic reciprocity for \(2\), and the norm-Euclidean property of \(\mathbb Z[\sqrt2]\), for which a short proof of the needed consequence is included below.

The phrase “difference between a triangular number and a square” is used in the orientation \(T_m-r^2\), which is already sufficient for Merca's implication. A later OEIS entry uses the broader convention allowing either orientation; that broader convention is not needed here.

## Proof
Set \(N=8n+1\) and write
\[
N=\prod_i p_i^{e_i}.
\]
Then
\[
\tau(N)=\prod_i(e_i+1).
\]
Suppose \(4\nmid\tau(N)\).

If every \(e_i\) is even, then \(N=X^2\) for an odd integer \(X\). Write \(X=2m+1\). Since \(8n+1=(2m+1)^2\), division by \(8\) gives \(n=T_m\), so the desired representation holds with \(r=0\).

Assume now that some \(e_i\) is odd. Since the product \(\prod_i(e_i+1)\) has \(2\)-adic valuation exactly \(1\), exactly one exponent is odd. Call the corresponding prime \(p\). Moreover \(e_p+1\) has \(2\)-adic valuation exactly \(1\), so
\[
e_p\equiv 1\pmod 4.
\]
Thus
\[
N=p^{4a+1}v^2
\]
with \(p\nmid v\). Because \(N\equiv1\pmod8\), because \(v\) is odd, and because \(4a+1\) is odd, it follows that \(p\equiv1\pmod8\).

It remains to use the following standard norm lemma.

**Lemma.** Every prime \(p\equiv1\pmod8\) has integers \(A,B\) with
\[
p=A^2-8B^2.
\]

**Proof of the lemma.** The ring \(R=\mathbb Z[\sqrt2]\) is norm-Euclidean for the absolute norm \(|x^2-2y^2|\). Indeed, after dividing in \(\mathbb Q(\sqrt2)\), approximate each coefficient by a nearest integer. If the two coefficient errors are \(u,v\) with \(|u|,|v|\le1/2\), then
\[
|u^2-2v^2|\le u^2+2v^2\le 3/4<1.
\]
Hence \(R\) is a unique factorization domain.

Quadratic reciprocity gives \((2/p)=1\) for \(p\equiv1\pmod8\). Choose an integer \(s\) with \(s^2\equiv2\pmod p\). In \(R\), the rational prime \(p\) divides
\[
(s+\sqrt2)(s-\sqrt2),
\]
but divides neither factor. Therefore \(p\) is not irreducible in the unique factorization domain \(R\). A nontrivial factor of \(p\) must have absolute norm \(p\); multiplying by the unit \(1+\sqrt2\), whose norm is \(-1\), if necessary changes the sign. Thus
\[
p=A^2-2C^2
\]
for some integers \(A,C\). Reducing modulo \(8\), the congruence \(p\equiv1\pmod8\) forces \(A\) odd and \(C\) even. Write \(C=2B\). Then \(p=A^2-8B^2\), proving the lemma.

Return to \(N=p^{4a+1}v^2\). From the lemma,
\[
N=(Ap^{2a}v)^2-8(Bp^{2a}v)^2.
\]
The first coordinate is odd, because its square is congruent to \(N\equiv1\pmod8\). Write \(Ap^{2a}v=2m+1\) after changing its sign if needed, and put \(r=|B|p^{2a}v\). Then
\[
8n+1=(2m+1)^2-8r^2,
\]
so \(n=T_m-r^2\). This proves the claim.

## Verification
The proof is symbolic and covers all integers \(n\ge0\). As a regression check, `artifacts/verify.py` independently factors every \(8n+1\) for \(0\le n\le100000\). Whenever \(4\nmid\tau(8n+1)\), it checks the forced exponent pattern and constructs a triangular-minus-square witness. The captured output in `artifacts/verification_output.txt` is `VERIFY_OK`; it reports \(21447\) exceptional inputs, split into \(447\) square cases and \(21000\) unique-odd-exponent cases.

The finite computation is not used to infer the universal theorem. Its role is only to detect algebraic or normalization mistakes in the symbolic argument.

## Relationship to prior work
Merca's 2022 paper introduces Conjecture 5 exactly in this setting: if \(n\) is not the difference between a triangular number and a square, then \(\sigma_0(8n+1)\) should vanish modulo \(4\). The paper gives numerical evidence but no proof. Its primary MSC classification is 11A25 and its publication date is 18 July 2022.

Craig and Merca's broader classification theorem for Ramanujan-type congruences of multiplicative functions proves a different progression-level conjecture and does not state the triangular-minus-square implication above. Merca's 2024 paper on divisor sums and partition congruences concerns different divisor-sum identities and does not state this criterion.

OEIS A391309, created in 2025, records integers not representable as a difference of a triangular number and a square and formulates the representation problem through Pell-type norm equations. It does not connect that representation set to the divisibility of \(\tau(8n+1)\). OEIS A035251 records the classical representability criterion for \(x^2-2y^2\), consistent with the norm lemma used in the proof.

## Limitations
No claim is made about analogous congruences modulo higher powers of \(2\), about the other residue classes \(8n+r\), or about a converse to the displayed implication. The literature search cannot rule out an unindexed or unpublished prior proof; the closest inspected sources did not contain this result. The self-review reported here is not an independent audit.

## References
1. Mircea Merca, “Families of Ramanujan-Type Congruences Modulo 4 for the Number of Divisors,” *Axioms* 11 (2022), 342. DOI: 10.3390/axioms11070342.
2. William Craig and Mircea Merca, “On Ramanujan-Type Congruences for Multiplicative Functions,” arXiv:2112.05649 (2021).
3. Mircea Merca, “From sums of divisors to partition congruences,” *RACSAM* 118 (2024), 115. DOI: 10.1007/s13398-024-01617-9.
4. OEIS A391309, positive integers not representable as a difference of a triangular number and a square number.
5. OEIS A035251, positive integers representable as \(x^2-2y^2\).
