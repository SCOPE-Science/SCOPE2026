# First minimum-rank failure in the PrimePowers backtracking routine
## Finding
For the public PrimePowers backtracking routine associated with arXiv:2508.01686, the first input in the conjecture range \(n\ge 24\) where the returned decomposition length is not the true minimum is \(n=50\): the routine returns \(50=32+9+9\) (three terms), while the minimum is two because \(50=25+25\). Hence the repository's generated `Length` field is not a minimum-rank certificate. Consistently, the paper's displayed five-term representation of \(512550\) is not minimal, since \(512550=659^2+5^7+2^7+2^4\) uses four prime powers.

## Assumptions and scope
A prime power means \(p^k\) with prime \(p\) and integer \(k\ge 2\), exactly as in the source paper. The statement concerns the public repository routine at blob `2a1a0f4485e60b783542da37e5f2aa7ca4ea6079` and the minimum number of summands among decompositions allowed by that definition, with two to five summands. The cutoff claim "first" is restricted to the paper's conjecture range \(n\ge 24\).

## Proof
The repository routine recursively chooses candidate prime powers in descending numerical order. At each node it immediately returns the first recursive success. It does not run separate searches for two terms, then three terms, and so on. Therefore its traversal order is not an optimization by number of summands.

For \(n=50\), the routine first reaches
\[
50=32+9+9=2^5+3^2+3^2,
\]
and returns this three-term decomposition. But
\[
50=25+25=5^2+5^2,
\]
so the true minimum is at most two. One-term decompositions are excluded by the source definition of the search and, in any case, \(50\) is not a prime power. Thus the true minimum is exactly two.

To establish that \(50\) is the first failure in the conjecture range, `verify_minimality.py` independently enumerates exact \(k\)-term nonincreasing decompositions for \(k=2,3,4,5\), increasing \(k\) from two. For every \(24\le n<50\), the source-order routine's returned length equals this independently computed minimum. At \(n=50\), the lengths first differ, as above.

The source paper also prints
\[
512550=502681+7921+1331+361+256
\]
as a five-term example. A shorter valid representation is
\[
512550=434281+78125+128+16=659^2+5^7+2^7+2^4.
\]
Each base \(659,5,2,2\) is prime, so all four summands satisfy the paper's prime-power definition.

## Verification
Running `python3 verify_minimality.py` prints
`VERIFY_OK first_mismatch=50 source=(32,9,9) minimum=(25,25) alt_512550=(434281,78125,128,16)`.
The checker uses a separate exact minimum-length search and also verifies the four-term identity for \(512550\).

## Relationship to prior work
Stricker's 2025 paper proposes that every integer \(n>23\) is a sum of two to five prime powers and reports computational evidence. The accompanying repository states that its backtracking algorithm aims for the minimum number of terms and records a `Length` column, while the actual routine returns the first success in a descending depth-first traversal. The present result does not challenge the existence claim "at most five"; it isolates the earliest failure of a minimum-length interpretation of the released routine and gives a shorter decomposition for a displayed five-term example.

Targeted searches of published-finding corpus and the public web found no checked source documenting this exact minimum-rank failure or the \(n=50\) cutoff. Those searches are evidence of comparison, not proof of absolute novelty.

## Limitations
This finding does not disprove the main five-summand conjecture and does not determine whether five summands are ever genuinely necessary. It concerns the inspected public repository blobs and can be affected by future repository revisions. The exhaustive "first failure" certificate covers only \(24\le n\le 50\), which is sufficient for the stated first-mismatch claim. No independent audit has been performed.

## References
1. Julius Stricker, *On the Representation of Integers as Sums of Limited Prime Powers*, arXiv:2508.01686v1, 2025.
2. PrimePowers/PrimePowers, `backtrack_decomposition`, blob `2a1a0f4485e60b783542da37e5f2aa7ca4ea6079`.
3. PrimePowers/PrimePowers, `README.md`, blob `6adf409a056f3fbf8f413b869abf0ef24aaa82ed`.
