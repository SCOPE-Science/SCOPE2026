# Conditional \(10^{4000}\) verification of the \(\sigma_{2,2}\)-pair squarefreeness conjecture

## Finding
A \(\sigma_{2,2}\) pair is a pair of distinct odd primes \(p,q\) such that
\[
q\mid p^2+p+1,\qquad p\mid q^2+q+1.
\]
Bibby, Vyncke, and Zelinsky formulate the conjecture that for every such pair, both
\[
p^2+p+1\quad\text{and}\quad q^2+q+1
\]
are squarefree.

Assume their reported exhaustive-search statement: after the pair
\[
(22419767768701,107419560853453),
\]
there is no further \(\sigma_{2,2}\) pair with both primes below \(10^{4000}\). Under that published search input, their squarefreeness conjecture holds for every \(\sigma_{2,2}\) pair with both primes below \(10^{4000}\).

The three pairs in that range are
\[
(3,13),\qquad (13,61),\qquad
(22419767768701,107419560853453).
\]
For their components the complete factorizations are
\[
3^2+3+1=13,
\]
\[
13^2+13+1=3\cdot61,
\]
\[
61^2+61+1=3\cdot13\cdot97,
\]
\[
22419767768701^2+22419767768701+1
=3\cdot7\cdot199\cdot1119712369\cdot107419560853453,
\]
and
\[
107419560853453^2+107419560853453+1
=3\cdot7\cdot24508477928503\cdot22419767768701.
\]
Every displayed prime factor occurs to exponent one.

## Assumptions and scope
The finite range statement is conditional on the correctness and intended scope of the primary paper's explicit computational report that, after its displayed large pair, there are no further \(\sigma_{2,2}\) pairs below \(10^{4000}\). This package does not claim an independent replay of that enormous pair search.

The squarefreeness part is independently checkable here: all factors in the five distinct displayed values are below \(2^{64}\), so the supplied verifier checks their primality deterministically and checks the products exactly.

The primary paper first appeared publicly as arXiv:1908.09420v1 on 26 August 2019 and has primary MSC 11A25.

## Proof
The primary paper proves that every quasisolution of the divisibility system is a consecutive pair in the integer sequence \(t_1=t_2=1\) defined by
\[
t_{n+2}=\frac{t_{n+1}^2+t_{n+1}+1}{t_n}.
\]
It identifies the three prime pairs displayed above and reports that a computer search found no further \(\sigma_{2,2}\) pair below \(10^{4000}\) after the large pair.

Under that report, it remains only to check the squarefreeness conjecture on those three pairs. The complete factorizations displayed in the Finding section do so immediately: each value is a product of distinct primes. The repeated value \(13^2+13+1=183\) occurs in both of the first two pairs and needs only one factorization.

For completeness, the verifier also reconstructs the recurrence through the large pair and confirms
\[
(t_3,t_4)=(3,13),\qquad (t_4,t_5)=(13,61),
\]
and
\[
(t_{22},t_{23})=(22419767768701,107419560853453).
\]
It then verifies the defining cross-divisibilities for all three pairs.

Therefore, conditional on the published exhaustive-search statement, every \(\sigma_{2,2}\) pair with both primes below \(10^{4000}\) satisfies Conjecture 9.

## Verification
The accompanying `verify.py` performs only exact integer checks. It reconstructs the recurrence through \(t_{23}\), checks the three pair locations and cross-divisibilities, multiplies the complete displayed factorizations, verifies that no factor repeats, and certifies every listed factor as prime with the standard deterministic Miller--Rabin base set valid below \(2^{64}\). It prints `VERIFY_OK` on success.

The script deliberately does not claim to reproduce the source's search to \(10^{4000}\). That search is an explicit scientific input to the conditional finite theorem.

## Relationship to prior work
Bibby, Vyncke, and Zelinsky state the squarefreeness assertion as Conjecture 9. In the same paper they classify quasisolutions by the recurrence above, identify the large prime pair, and report that no later \(\sigma_{2,2}\) pair occurs below \(10^{4000}\). They do not state the resulting finite squarefreeness verification.

OEIS A264611 and A264612 currently list exactly the three known prime pairs. Targeted searches for the conjecture label, the term \(\sigma_{2,2}\), the large pair, the \(10^{4000}\) cutoff, and the squarefreeness conclusion did not locate a publication stating this finite implication.

## Limitations
The result is conditional on a published computational search whose certificate is not supplied in the source and is not reconstructed here. It therefore does not convert Conjecture 9 into an unconditional theorem over the stated range independently of that search.

It also says nothing about a possible \(\sigma_{2,2}\) pair beyond the reported cutoff. Failed literature searches do not prove that an unindexed observation of the same finite implication does not exist.

## References
1. Sean Bibby, Pieter Vyncke, and Joshua Zelinsky, “On the third largest prime divisor of an odd perfect number,” arXiv:1908.09420v1, first posted 26 August 2019; later published in *Integers* 21 (2021), A115.
2. OEIS A264611, smaller primes in known \(\sigma_{2,2}\) pairs.
3. OEIS A264612, larger primes in known \(\sigma_{2,2}\) pairs.
