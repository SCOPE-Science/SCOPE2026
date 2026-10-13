# The primary-pseudoperfect strong-uniqueness conjectures fail at \(47058\)

## Finding
The integer \(47058\) is a counterexample to two conjectures of McCormack and Zelinsky. It is primary pseudoperfect and strongly pseudoperfect. Consequently, their Conjecture 46 and the formally stronger Conjecture 47 are both false.

Explicitly,
\[
47058=2\cdot3\cdot11\cdot23\cdot31.
\]
For primary pseudoperfectness,
\[
1+23529+15686+4278+2046+1518=47058,
\]
so after division by \(47058\),
\[
\frac1{47058}+\frac12+\frac13+\frac1{11}+\frac1{23}+\frac1{31}=1.
\]

For strong pseudoperfectness, take
\[
S=\{1,47058,2,23529,3,15686,22,2139,23,2046,31,1518,33,1426,93,506\}.
\]
The elements of \(S\) form exactly the eight complementary divisor pairs
\[
(1,47058),(2,23529),(3,15686),(22,2139),(23,2046),(31,1518),(33,1426),(93,506),
\]
and
\[
\sum_{d\in S}d=94116=2\cdot47058.
\]
Thus \(d\in S\) if and only if \(47058/d\in S\), and \(S\) is a strongly pseudoperfect representation.

## Assumptions and scope
A positive integer \(n\) is primary pseudoperfect when
\[
\frac1n+\sum_{p\mid n}\frac1p=1,
\]
where the sum is over prime divisors. A positive integer \(n\) is strongly pseudoperfect when there is a set \(S\) of positive divisors such that \(d\in S\) if and only if \(n/d\in S\), and \(\sum_{d\in S}d=2n\).

No unproved classification is used. The claim is only that the displayed integer is a counterexample; existence of one valid witness settles both conjectures negatively.

## Proof
The displayed factorization has five prime factors. Multiplying the reciprocal identity by \(47058\) reduces it to the exact integer equality
\[
1+23529+15686+4278+2046+1518=47058,
\]
which proves primary pseudoperfectness.

For the strong condition, each displayed pair has product \(47058\), so the set \(S\) is closed under complementary divisors in both directions. Summing the eight pair-sums gives
\[
(1+47058)+(2+23529)+(3+15686)+(22+2139)+(23+2046)+(31+1518)+(33+1426)+(93+506)=94116.
\]
Since \(94116=2\cdot47058\), the definition of strongly pseudoperfect is met.

McCormack and Zelinsky state Conjecture 46 as the assertion that \(6\) is the only primary pseudoperfect number that is strongly pseudoperfect. The example \(47058\ne6\) refutes it. Their weak-primary condition only requires the reciprocal expression to be an integer; here it equals \(1\), so the same example also refutes Conjecture 47.

## Verification
The accompanying `verify.py` independently checks primality of the five displayed factors by trial division, their product, the exact primary-pseudoperfect integer identity, divisor membership of every element of \(S\), complement closure, distinctness, and the exact sum \(2n\). The accompanying `certificate.json` records the factorization and complement pairs. These checks replay the finite arithmetic; no search bound or probabilistic test is involved.

## Relationship to prior work
McCormack and Zelinsky, arXiv:2312.11661, define the relevant notions and in their current full text state Conjectures 46 and 47 explicitly. Their first public arXiv version is dated 2023-12-18. OEIS A054377 already records \(47058\) as a primary pseudoperfect number, but does not supply the strongly pseudoperfect witness above. OEIS A334405 is the canonical strongly pseudoperfect sequence; its currently published b-file does not contain \(47058\).

A directly relevant later paper by Wang and Zelinsky, arXiv:2609.36068v1, develops strongly pseudoperfect numbers and new restrictions. Full-text checks found no occurrence of `47058`, `primary pseudoperfect`, or the conjecture terminology. A current MathDB entry still records the primary-pseudoperfect/strongly-pseudoperfect uniqueness statement as open. Targeted published-findings-index searches for the exact integer, the two notions, the conjecture number, and low-support variants returned no covering result.

## Limitations
This finding gives a counterexample, not a classification of all integers that are simultaneously primary pseudoperfect and strongly pseudoperfect. It does not determine whether there are infinitely many such intersections. The literature comparison cannot exclude an unindexed or unpublished independent observation, but it includes the conjecturing paper, the canonical OEIS entries, a 2026 paper devoted to strongly pseudoperfect numbers, a current conjecture database, and targeted semantic searches.

## References
1. Tim McCormack and Joshua Zelinsky, *Weighted Versions of the Arithmetic-Mean-Geometric Mean Inequality and Zaremba's Function*, arXiv:2312.11661v1 (first public 2023-12-18); current full text states Conjectures 46 and 47.
2. Audrey Wang and Joshua Zelinsky, *Strongly Pseudoperfect Numbers*, arXiv:2609.36068v1 (2026-09-28).
3. OEIS A054377, *Primary pseudoperfect numbers*.
4. OEIS A334405, *Strongly pseudoperfect numbers*.
5. MathDB problem 361204, *Primary pseudoperfect strongly pseudoperfect uniqueness conjecture*.
