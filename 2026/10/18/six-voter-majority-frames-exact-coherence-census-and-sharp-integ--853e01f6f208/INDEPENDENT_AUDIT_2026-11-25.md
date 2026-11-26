# Independent mathematical audit

## correctness

PASS

The ten complementary triple pairs give independent bits; all larger and smaller coalition decisions are fixed. An independent exact walk under adjacent transpositions (python3 /workspace/branches/independent_checks.py 2) verifies that minima 0,1,3,7,15,19,20,21,28,29,58,126,220 have respective orbit sizes 6,60,180,60,6,20,90,180,180,90,120,20,12. It tests the six printed integer tuples on all 64 subsets, and checks the seven printed four-triple witnesses for distinctness, selection and incidence two at each voter. Four strict half-total inequalities cannot sum to twice total weight, so the latter certificates rule out even real additive weights; relabeling transfers both types of certificate to the whole orbit. The resulting totals are 332 and 692. For mask 3, winning 123 and 124 and losing 134,125,126 force w2>w3,w4 and both w3,w4>w5,w6. If all weights are ≤3 these coordinates must be 3,2,2,1,1 respectively; then the losing 125 must be strictly lighter than its winning complement 346, requiring w1<1. The printed maximum-4 tuple realizes the mask, so the common bound is sharp. Independently enumerating sorted positive tuples and relabeling gives 152 realizable masks with maximum ≤3 and 332 with maximum ≤4. The supplied checker constructs its own rows and witnesses rather than parsing the printed table; the independent replay verifies the literal table. The theorem is restricted to the designated six-voter majority frames.

## originality

PASS

Best-of-knowledge pass for the frozen result. The exact census including the obstruction equivalence is also stated in a distinct later-listed catalogue record; the overlap is material, but independent discovery and priority are not established by the displayed dates alone. That record's quantitative invariant is a bound on integral deviations about a fixed total, not the unrestricted sharp minimum uniform cap on positive integer singleton weights. The earlier Moss–Pedersen primary paper supplies the definitions and four-coherence criterion, not sufficiency of that criterion for measurability in this family. The apparent published six-voter counterexample to sufficiency is invalid as printed, by explicit inspection below. Possible extraction of the weighted portion from early general catalogues remains a named risk.

## value

PASS

Six voters give a natural small carrier where nonmeasurability actually occurs. The exact classification resolves which local four-coalition certificates suffice, exposes the conflict in a printed six-voter example, and gives an optimal integer implementation bound. The certificates are useful beyond the two aggregate counts: they decide each relabeling class and avoid solving a general feasibility problem. No all-electorate sufficiency is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
