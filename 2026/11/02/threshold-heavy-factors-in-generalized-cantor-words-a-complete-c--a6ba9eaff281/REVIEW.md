# Independent mathematical audit

## correctness

PASS

Weighting each binary addition column by (b-1)b^r gives the carry excess (b-1)(b-2) sum_r c_r b^r. It is nonnegative and vanishes iff there is no common set bit. The span of the first k ones in any qualifying interval is therefore at least E_b(k-1); equality forces both endpoints to be ones and the starting one-index i to satisfy i & (k-1)=0. The prefix attains the bound, and strict increase of E_b excludes an extra one. Writing i=a+2^h t, disjoint bits imply a+k-1<2^h, so all k offsets depend only on a; letting t vary gives infinite occurrences. For two different allowed residues, let q be the least differing bit. The common increment r=2^q-(a mod 2^q) is between 1 and k-1 since k-1>=2^{h-1}. Exactly one of a+r and a'+r then has valuation q, and their consecutive-one gaps differ by the formula gap(s)=(b-2)b^{nu_2(s)}+1. Thus the words are distinct and the count is the number of free bits. The k=1 case is the single word 1. The threshold computation makes each prefix maximum-weight at its length, the gaps at powers of two are unbounded, and sliding to a zero run realizes every intervening weight. The jump formulas follow by binary digit sums. Independent direct digit membership and finite window scans agreed for b=4,5,6, k=1–8, and lengths 1–30 for the Abelian checks. The supplied verify.py and recorded 102-case run were inspected, not executed. The infinite result rests on RESULT.md lines 42–72, not the finite checks.

## originality

PASS

Credit the classification of distinct ordinary words and their allowed starts at the least length attaining k ones, not the already known classical Cantor maximum-weight and Abelian recurrences. The strongest checked same-family catalogue result determines palindromes, not these general extremizers. The closest generalized-Cantor paper was not accessible in full text; its scope remains a real risk, not evidence against the exact classification. This is a best-of-knowledge judgment, not a priority certificate.

## value

PASS

The first-attainment factors refine a natural maximum-weight statistic to an exact language classification at every threshold. The count of distinct words can jump from one to 2^m at successive one-count thresholds, while Abelian complexity identifies all the words at any one threshold. The admissible starts and recurring representative words supply precisely the information that the prefix profile does not contain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
