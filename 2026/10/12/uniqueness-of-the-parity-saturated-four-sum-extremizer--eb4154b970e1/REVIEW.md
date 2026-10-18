# Independent mathematical audit

## correctness

PASS

For each n>=6 the proposed middle-even witness tuples were checked symbolically: if a in [6,2n-4] is even, (1,2,a-2,a-1) for a<=n+1 or (a-n,n,a-n+1,n-1) for a>=n+2 is positive, strictly distinct and has precisely the required six allowed sums. Without middle evens E is one of four triples in {2,4,2n-2,2n}; the two explicit boundary tuples eliminate three triples. The surviving {2,2n-2,2n} admits no witness: three same-parity summands force three distinct even sums among only the two even values >=4, while a two/two split forces two opposite-parity larger summands at least n, whose sum exceeds 2n. An independently written brute-force enumerator reproduced exactly the surviving triple for each n=6,...,12, corroborative rather than an infinite proof.

## originality

PASS

The exact statement is equality-case uniqueness inside the class containing every odd integer with exactly three even additions. The closest source constructs the single surviving set and gives a mechanism eliminating middle evens but does not resolve all boundary triples or state the iff classification. The distinct earlier van Doorn narrow extremality theorem is about five input integers. Best-of-knowledge originality passes, qualified by the real possibility of an unindexed boundary-case observation; the generic sharp h4 result is not itself a uniqueness classification.

## value

PASS

The all-odd plus three-even family is canonically singled out by the published extremal construction at sharp h4(n)=4 and cardinality n+3. Its exact unique equality profile for every n>=6 resolves a natural structural rigidity question that the existence extremizer does not answer. This is deliberately narrower than a classification of all size-n+3 witness-free sets and does not assert that broader result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
