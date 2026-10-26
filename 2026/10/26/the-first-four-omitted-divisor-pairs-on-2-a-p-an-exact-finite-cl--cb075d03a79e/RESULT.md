# The first four omitted divisor pairs on \(2^a p\): an exact finite classification

## Finding

For an integer \(a\geq1\) and an odd prime \(p\), let \(n=2^a p\). An *omission of order \(k\)* means a collection of exactly \(k\) distinct complementary divisor pairs \(\{d,n/d\}\) whose total sum equals \(\sigma(n)-2n\). Removing those pairs from the complete divisor set therefore gives a strongly pseudoperfect representation of \(n\).

**Theorem.** Among all integers \(n=2^a p\), with \(a\geq1\) and \(p\) an odd prime, the smallest integer admitting an omission of order four is
\[
\boxed{630194176=2^{20}\cdot601.}
\]
Its order-four omission is unique, with four complementary pairs
\[
(512,1230848),\quad(65536,9616),\quad
(262144,2404),\quad(524288,1202).
\]
This integer has no omission of order one, two, or three. Moreover, **no** integer \(2^a p\) with \(1\leq a\leq27\) and odd prime \(p\) has an omission of order three. In the same complete exponent range, the integers with an omission of order four are exactly
\[
\boxed{2^{20}\cdot601,\quad 2^{20}\cdot2311,\quad 2^{24}\cdot49123,}
\]
with a unique omission of order four for each.

The final assertion is a finite classification with a complete, reproducible integer-arithmetic certificate, not an assertion about unbounded exponents. The order-four occurrence before any order-three occurrence in the bounded range illustrates that the realization hierarchy need not appear in order of omission size.

## Assumptions and scope

The divisor sum is \(\sigma(n)=\sum_{d\mid n}d\). Strong pseudoperfectness means that some set of positive divisors is invariant under \(d\mapsto n/d\) and sums to \(2n\). Here \(p\) is always an odd *prime*, not a general odd cofactor. The integer \(2^a p\) is never a square, so every complementary pair contains exactly two distinct divisors. The order is the number of omitted **pairs** (not the number of omitted individual divisors). A number may admit representations of different orders; the theorem does not assert that an omission of order four is the first representation of every member of the three-integer list.

## Proof

**1. Exhaustive parametrization.** Since \(p\) is an odd prime, all divisors of \(n=2^a p\) occur in the disjoint complementary pairs
\[
P_i=\bigl(2^i,\,p2^{a-i}\bigr),\qquad 0\leq i\leq a,
\]
and
\[
\sigma(n)=(2^{a+1}-1)(p+1),\qquad
\sigma(n)-2n=2^{a+1}-1-p.
\]
An omission indexed by \(I\subseteq\{0,\ldots,a\}\) therefore exists if and only if
\[
\sum_{i\in I}\bigl(2^i+p2^{a-i}\bigr)=2^{a+1}-1-p.
\tag{1}
\]
The pair \(P_0\) cannot be omitted: its sum \(1+p2^a\) exceeds the right side, because \(p\geq3\). If \(0\notin I\) but \(a\in I\), the numerator \(2^{a+1}-1-\sum_{i\in I}2^i\) is odd and the denominator \(1+\sum_{i\in I}2^{a-i}\) is even, hence no integer \(p\) can satisfy (1). Thus every nonempty omission has \(I\subseteq\{1,\ldots,a-1\}\). Solving (1) for \(p\) gives the exact sieve
\[
\boxed{
 p=\frac{2^{a+1}-1-\sum_{i\in I}2^i}
 {1+\sum_{i\in I}2^{a-i}}
}.\tag{2}
\]
Conversely, any choice of \(a,I\) for which (2) is an odd prime gives a genuine symmetric omission; no other cases exist.

**2. Finite upper bound.** If \(2^a p\leq630194176\), then \(3\cdot2^a\leq630194176<3\cdot2^{28}\), so \(a\leq27\). Therefore proving the first occurrence requires only the bounded exponents \(1\leq a\leq27\). In each exponent the order-four possibilities are all four-subsets of \(\{1,\ldots,a-1\}\). There are exactly
\[
\sum_{a=5}^{27}\binom{a-1}{4}=80730
\]
sets. For order three there are exactly
\[
\sum_{a=4}^{27}\binom{a-1}{3}=17550
\]
sets.

**3. Complete exact classification.** Apply (2) to each of the \(17550\) three-subsets, requiring an integer odd quotient at least three. Exactly three triples \((a,p,I)\) pass this integrality test:
\[
(16,3531,\{12,13,14\}),\quad
(19,4595,\{12,13,17\}),\quad
(26,76083,\{16,17,24\}).
\]
Each quotient is composite: respectively divisible by \(3\), \(5\), and \(3\). Hence there are no order-three omissions with \(a\leq27\).

For four-subsets, exactly eight triples pass the same integral-odd-quotient test:
\[
\begin{aligned}
 &(20,601,\{9,16,18,19\}),\\
 &(20,2311,\{11,12,14,17\}),\\
 &(21,30363,\{15,16,18,19\}),\\
 &(23,9615,\{13,14,16,19\}),\\
 &(23,13815,\{13,18,19,20\}),\\
 &(24,23631,\{14,16,18,20\}),\\
 &(24,49123,\{15,19,20,22\}),\\
 &(27,3369195,\{22,23,24,25\}).
\end{aligned}
\]
The five quotients \(30363,9615,13815,23631,3369195\) are divisible by \(3\). Trial division through the integer square root confirms that \(601,2311,49123\) are prime. Thus the three integers stated in the theorem are the entire order-four list for \(a\leq27\). Their sizes are strictly increasing in the displayed order, and only the first is at most \(630194176\).

The two finite tables are not inferred from a partial search. The accompanying standalone `verify.py` executes exactly the index ranges above, checks divisibility using integers, certifies primality by complete trial division, and asserts the full lists rather than stopping at the first hit. The exhaustion is valid because equation (2) is necessary and sufficient for every admissible pair set. The executable code and this bijection together give a finite proof of the tables.

**4. Witness and exact omission complexity.** For \(a=20,p=601,I=\{9,16,18,19\}\), direct evaluation gives
\[
\sigma(630194176)=1262484902,
\quad2n=1260388352,
\quad\sigma(n)-2n=2096550.
\]
The four displayed pair sums are \(1231360,75152,264548,525490\), totaling \(2096550\). They are disjoint complementary divisor pairs, so the unomitted divisors sum to \(2n\). Exhausting one- and two-element subsets of \(\{0,\ldots,20\}\), as in the verifier, yields no omission of either order for this same \(n\); order three was already ruled out in step 3. The unique quadruple follows from the complete order-four table. \(\square\)

## Verification

Run `python3 verify.py` with standard Python 3. Its expected final line is

`VERIFY_OK triple_tuples=17550 quadruple_tuples=80730 integer_triples=3 integer_quadruples=8 prime_quads=3 first_four_pair=630194176 no_smaller_three_pairs=PASS direct_divisor_sums=PASS`.

The verifier uses standard-library combinations, exact integer divisibility, independent complete trial-division primality, and direct recomputation of all divisors and omitted divisor sums for each of the three prime candidates. It explicitly checks the bound on \(a\), both tuple totals and complete raw quotient tables, and lack of shorter omissions for the least four-pair witness. No randomization, outside database, precomputed certificate, or time-limited search is required. Exhaustive verification proves these finite claims only; it does not decide whether three-pair omissions exist at some exponent greater than \(27\).

## Relationship to prior work

Wang and Zelinsky (2026, arXiv:2609.36068, primary MSC \(11\mathrm{A}25\)) define and study strongly pseudoperfect numbers and study restrictions on few omitted divisor pairs; their results include families omitting two pairs of divisors in other prime-support families. Their paper does not state this bounded \(2^a p\) three-/four-pair classification or its least four-pair witness. The published research note *The first multi-pair strongly pseudoperfect number of the form \(2^a p\)* (2026) already gives the exact general bit-mask/quotient parametrization used in equation (2) and the first genuine two-pair omission at \(11776\). Neither the reduction (2) nor the two-pair result is claimed as new here. The new finding is the exhaustive next finite structure: no three-pair omissions for all exponents through \(27\), the complete four-pair list in this range, and the first order-four witness.

## Limitations

The classification is limited to the family \(2^a p\) with \(p\) an odd prime, and the complete three-/four-pair table is limited to \(a\leq27\). The omission order is existential; the theorem does not classify all strongly pseudoperfect integers or all minimal representation orders globally. It does not determine the first three-pair example if any exists beyond this range, or prove an infinite family of four-pair solutions. The published research note giving the exact general quotient was recoverable through its public summary but the full repository text was not accessible for direct comparison; independent priority review should revisit it. A broader unpublished or unindexed enumeration could cover the finite table.

## References

1. Audrey Wang and Joshua Zelinsky, *Strongly Pseudoperfect Numbers*, arXiv:2609.36068v3 (2026). https://arxiv.org/html/2609.36068v3 (first public version: 28 September 2026).
2. *The first multi-pair strongly pseudoperfect number of the form* \(2^a p\), public research record (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-the-first-multi-pair-strongly-pseudoperfect-number-of-the-form-2--067a5b7cff02 . Accessible abstract/summary used for comparison; complete text not inspected.
3. Vedant Aryan, Dev Madhavani, Savan Parikh, Ingrid Slattery, and Joshua Zelinsky, *On 2-Near Perfect Numbers*, *Integers* **24** (2024), A61. https://math.colgate.edu/~integers/y61/y61.pdf . This source treats two omitted individual divisors, not eight omitted divisors.
