# Cubic Gauss-sum equality census below characteristic 50
## Finding
Let \(p\) be an odd prime with \(p<50\), put \(q=p^3\) and \(n=q-1\), and fix a Teichmüller character \(\omega:\mathbb F_q^\times\to\mu_n\). For \(c\in\mathbb Z/n\mathbb Z\), write \(\chi_c=\omega^{-c}\), and identify characters under Frobenius conjugacy \(c\sim pc\pmod n\).

The complete equality census is: non-Frobenius equalities \(G(\chi_c)=G(\chi_{c'})\) occur exactly for \(p\in\{11,23,37\}\). At \(p=11\) and \(p=23\), the only nontrivial class is the familiar order-\(14\)/quadratic class. At \(p=37\), there are exactly five nontrivial classes.

Writing \(n=37^3-1=50652\) and \(\psi_m=\omega^{-n/m}\), representatives of the five \(p=37\) classes are
\[
G(\psi_{14})=G(\psi_{14}^3)=G(\psi_2),
\]
\[
G(\psi_{42})=G(\psi_{42}^{13}),\qquad G(\psi_{42}^5)=G(\psi_{42}^{11}),
\]
\[
G(\psi_{28})=G(\psi_{28}^5),\qquad G(\psi_{28}^3)=G(\psi_{28}^{11}),
\]
where each character is understood together with its Frobenius orbit. The order-\(28\) representatives have digit sums \(45,45,63,63\), whereas the midpoint is \(3(37-1)/2=54\). Thus those two equality pairs are outside the midpoint pure-sum situation isolated in Proposition 2.13 of the source paper, and order \(28\) is also outside its quoted Evans Theorem 5.1, which concerns order \(2m\) with \(m\) odd.

## Assumptions and scope
Gauss sums use the additive character and Teichmüller normalization of Adrian, Diamond, Kramer and Tam. The classification is finite: it covers every odd prime \(p<50\) and every multiplicative character on \(\mathbb F_{p^3}^\times\). It does not assert a pattern for larger \(p\) or other extension degrees.

## Proof
For \(0\le c<n\), write the base-\(p\) expansion \(c=c_0+c_1p+c_2p^2\), and define
\[
s_q(c)=c_0+c_1+c_2,\qquad \nu_q(c)=c_0!c_1!c_2!\pmod p.
\]
Proposition 2.9 of Adrian--Diamond--Kramer--Tam gives a necessary and sufficient criterion for odd \(p\):
\[
G(\chi_c)=G(\chi_{c'})
\]
if and only if \(\nu_q(c)=\nu_q(c')\pmod p\) and
\[
s_q(uc)=s_q(uc')
\]
for every unit \(u\in(\mathbb Z/n\mathbb Z)^\times\). Frobenius conjugacy is exactly multiplication of \(c\) by \(p\) modulo \(n\).

The verifier applies this criterion exhaustively. For each prime it first partitions all \(n=p^3-1\) exponents by \(\nu_q\) and by digit sums for a deterministic separating subset of units. Any true equality must remain in one such cell. Every cell already contained in one Frobenius orbit is therefore permanently eliminated. Only cells containing more than one Frobenius orbit are retained; for those cells the verifier evaluates \(s_q(uc)\) for every unit \(u\), so the surviving classes are exactly the Gauss-sum equality classes supplied by Proposition 2.9.

For \(p=37\), the surviving exponent orbits are exactly
\[
(3618,32562,39798)=(10854,18090,47034)=(25326),
\]
\[
(1206,30150,44622)=(15678,22914,37386),
\]
\[
(5427,34371,48843)=(19899,27135,41607),
\]
\[
(6030,20502,49446)=(13266,27738,34974),
\]
and
\[
(1809,16281,45225)=(9045,23517,30753),
\]
where equality signs mean equal Gauss sums between the indicated Frobenius orbits. Their character orders are respectively \(14,14,2\), \(42,42\), \(28,28\), \(42,42\), and \(28,28\). Direct base-\(37\) expansion gives digit sums \(45,45,63,63\) for the four order-\(28\) representatives \(1809,9045,5427,19899\).

For \(p=11,23,37\), \(2\in\langle p\rangle\pmod 7\), so Evans's pure-sum result, quoted as Theorem 5.1 in the source paper, explains the order-\(14\)/quadratic class. The four additional \(p=37\) classes are distinct from that class; in particular the order-\(28\) pairs do not satisfy the midpoint digit-sum condition.

## Verification
Run `python3 verify.py`. The supplied standard-library verifier enumerates all \(385032\) character exponents across the fourteen odd primes below \(50\), performs the rigorous separating-subset reduction, checks every unit on every unresolved multi-orbit cell, compares the resulting classes with the stated census, verifies character orders, and checks the order-\(28\) digit sums. Its recorded output is:

`VERIFY_OK primes=14 total_characters=385032 exceptional_primes=[11, 23, 37] p37_classes=5 p37_orders=[[14, 14, 2], [42, 42], [28, 28], [42, 42], [28, 28]] order28_digits=[45,45,63,63]`

## Relationship to prior work
Adrian, Diamond, Kramer and Tam give the exact digit criterion used here and report a sample for extension degree \(3\): all equalities are Frobenius-trivial for \(p=2,3,5,7,13,17\), while \(p=11\) has a nontrivial order-\(14\) equality. Their paper does not give the odd-prime census through \(50\), and its text contains none of the \(p=37\) exponents above. Their Theorem 5.1, quoting Evans, accounts for the order-\(14\)/quadratic equality at \(p=11,23,37\). It does not apply to order \(28\), and for order \(42\) its hypothesis \(2\in\langle37\rangle\pmod{21}\) fails. Targeted semantic-index and public-literature searches found no prior table or theorem containing the \(p=37\) order-\(28\) and order-\(42\) equality classes.

## Limitations
This is an exact finite classification, not a theorem for all characteristics. Its correctness depends on Proposition 2.9 as stated in the source paper and on exhaustive integer evaluation of that criterion. The literature comparison cannot exclude an unindexed older computational table; that is the principal residual originality risk. No numerical approximation of Gauss sums is used.

## References
1. Moshe Adrian, Jack Diamond, Kenneth Kramer, and Geo Kam-Fai Tam, “Distinguishing Gauss sums,” arXiv:2609.28211v1, 2026. In particular Proposition 2.9, Example 2.12, Proposition 2.13, and Theorem 5.1.
2. Ronald J. Evans, “Pure Gauss sums over finite fields,” *Mathematika* 28 (1981), 239–248, DOI 10.1112/S0025579300010299; see Corollary 8.
