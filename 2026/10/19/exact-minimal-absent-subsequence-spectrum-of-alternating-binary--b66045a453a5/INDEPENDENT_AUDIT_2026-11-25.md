# Independent mathematical audit

## correctness

PASS

Greedy embedding in the infinite alternating word ends at L: cost 1 or 2 for the initial letter and 1 or 2 per step according as the letter changes or stays. This position is minimal. It suffices to check one-letter deletions by transitivity of subsequence. The front deletion loses 0 exactly for ab and 2 otherwise; an interior deletion loses 0 exactly for an isolated opposite letter, and 2 otherwise. The final deletion loses 1 or 2 according as the final letters differ or agree. This forces exactly the two endpoint costs 2m+1 and 2m+2 and the stated restrictions; length-one words are present. For an allowed word every internal run has length ≥2, and a first a-run must have length ≥2 when there is a second run. For S=uz/(1−uz²) and T=u²z³/(1−uz²), this gives a-start S/(1−T) and b-start zS+zS²/(1−T). Doubling the final letter multiplies the weight by uz² and bijects allowed nonempty words with allowed words ending in an equal pair, so both coefficient extractions follow. Taking u=1, the coefficient recurrence for indices n≥4 has distinct characteristic roots r with r³=r+1; their squares solve y³−2y²+y−1=0, giving the paired parity recurrence and the stated generating function from 3,5,9. The supplied checker and saved output were inspected, not executed; their finite tests are not the all-m proof.

## originality

PASS

The distinct claim at the October 19 frozen record is the explicit minimal-absent family characterization and full length enumerator, not a new general characterization or an enumeration algorithm. There is demonstrably equivalent catalogue coverage in separately dated later records; it is explicitly credited as overlap, not treated as evidence of an earlier source. No inspected pre-existing theorem supplies this spectrum or total recurrence as a direct specialization.

## value

PASS

Even-length alternating hosts are a canonical periodic binary test family. The result determines which words are the minimal failures of scattered containment and how many occur at each length, without running an enumerator on each input. This provides an exact workload benchmark and a structural explanation of the growth via a short recurrence; the result is not inferred from samples and does not purport to cover arbitrary periodic hosts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
