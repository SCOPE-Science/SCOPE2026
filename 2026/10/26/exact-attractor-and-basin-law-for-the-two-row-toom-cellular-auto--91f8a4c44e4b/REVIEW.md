# Independent mathematical audit

## correctness

PASS

The frozen Finding says every fixed configuration has identical rows, but the constant column words (01)^n and (10)^n are fixed too. The repaired Finding limits the boundary-count formula to column-uniform targets and explicitly gives both discordant fixed points singleton basins. Re-derivation: agreement freezes a column; disagreement lets the east vote decide both rows. Agreement persists, eroding each discordant run by one per step; without agreement the whole word shifts. Fixing a word under k shifts constrains gcd(n,k) independent bits, and inversion over divisors followed by division by period counts orbits. For a uniform target exactly its outbound changes are compulsory initial anchors; all other sites have three choices, subtracting the 2^n anchorless states only for a constant target. A marked zero in a mask gives k gaps bounded by t and counts each labelled mask k times, proving E_n(t), including its two recurrent constant masks at t=0. Disjoint Bernoulli blocks and the union bound give the logarithmic typical time; one anchor gives the sharp n-1. Independent exact enumeration checked 21,840 states for 2<=n<=7, including both exceptional singleton basins and all cumulative depth counts; replay with python3 /workspace/reproductions/independent_finite_checks.py. The frozen verifier and recorded output were inspected, not run; its `cycles` field is a histogram of points, not of orbit counts, now clarified in the repaired RESULT.md. Enumeration does not prove the all-n statements.

## originality

PASS

Best-of-knowledge decision for the full labelled two-row census. Credit the material catalogue overlap: the 2026/11/17 entry gives the very same pointwise basins, anchor/copy reduction, discordant shift and depth mechanism for n>=3. It adds Ising output statistics; it does not give the joint finite-size census of primitive orbits and cumulative depths in this record. The dates on the records are documentary context, not priority certification. No inspected earlier theorem covers the full census; neither the familiar shift-word counts nor runs-of-ones counting as standalone combinatorics is a novelty claim. The repair changes only the description of the already-classified period-one discordant orbits.

## value

PASS

The thin periodic quotient is a natural minimum width for distinct north and center votes. The joint census resolves, rather than just estimates, three natural questions: which patterns recur, how many initial states feed each attractor and how rapidly recurrence begins. In particular it separates the exponentially small nonfixed travelling subsystem with no outside predecessors from the basin-rich frozen patterns, and quantifies logarithmic typical versus linear worst-case depth. The repaired statement gives the proper period-one boundary case rather than a new claim based on an arbitrary small example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
