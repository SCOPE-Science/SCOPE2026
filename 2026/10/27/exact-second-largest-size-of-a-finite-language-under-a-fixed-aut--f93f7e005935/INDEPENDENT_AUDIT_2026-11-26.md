# Independent mathematical audit

## correctness

PASS

In the minimal complete DFA for a finite nonempty language, remove the unique empty-right-language sink; a directed cycle among remaining states would give arbitrarily long accepted words. They are all reachable and coaccessible, so the initial state can be placed first and the last state is accepting. For fixed acceptance bits e_i, backward induction gives suffix count at v_i at most B_i=Σ_{j≥i}e_j q^(j−i), since these chain counts strictly decrease and every live transition goes forward. Maximizing B_0 gives the last-f pattern. A different admissible pattern costs at least q^(n−f)−q^(n−f−1), and is possible only for 2≤f<n. If the pattern is extremal, the first skipping letter from v_i is reached by q^i distinct prefixes and costs at least q^i(B_{i+1}−B_{i+2}), using B_n=0 at the final eligible transition. The loss equals at least q^(n−2) when v_{i+1} is in the accepting block, and at least q^(n−f−2)(q^f−1) otherwise (that branch is used only when i+1<n−f). For f≥2 the latter exceeds (q−1)q^(n−f−1) since q^f−1>q(q−1). For f=1 and n≥3 it is exactly (q−1)q^(n−3), whereas n=2 allows only deletion of one terminal transition for the smallest gap. For f=n only the q^(n−2) case applies. Each specified modification preserves at least one letter to every successive state, so all live states are accessible and their maximum accepted suffix lengths n−1−i distinguish them and the sink. This proves both attainability and the strict second-largest bound. Independently enumerated forward complete transition tables for (q,n)=(2,2),(2,3),(2,4),(3,2),(3,3),(4,2),(4,3), computing literal accepted-word sets of lengths 0 through n−1 for reachability/minimality-filtered states and every accepting-state stratum; the top two agree (e.g. at q=4,n=3: (16,13),(20,17),(21,17)). Read VERIFICATION.md and verify_small_cases.py; the source's finite census is separate recorded evidence.

## originality

PASS

Credit the exact first loss conditional on both state budgets and the corresponding witnesses, not the familiar unrestricted maximum from bounding longest accepted word length. Inspected finite-automata enumeration and structural sources do not give the conditional gap or a stronger result that implies it mechanically.

## value

PASS

The conditional first gap tells how much cardinality is sacrificed by any departure from extremality when two natural automaton resources are held fixed. It distinguishes acceptance placement from transition shortcuts and separates the single-final, mixed, and all-final cases, where the controlling scale changes. The independent constructive sharpness matters for language-size feasibility; the claim is not a census of all intermediate sizes or just the depth-based maximum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
