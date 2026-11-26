# Independent mathematical audit

## correctness

PASS

The two prescribed windows each give a total order on positions and agree on the increasing chain of m shared positions. Private elements in different shared-position gaps are ordered by the separating shared positions. Within a gap any shuffle of the two private chains satisfies both window orders, and the full shuffle assigns ranks 1 through 3m uniquely. The alternating pattern has m−1 paired gaps of size (1,1). Moving rank 5 from the odd prefix to the suffix and rank 4 in the opposite direction gives paired nonunit gaps (2,1) and (1,2) and m−4 gaps of size (1,1). This yields 9·2^(m−4) versus 2^(m−1), including 9 versus 8 at m=4. Independently enumerating the first window's values and ranking the uniquely completed second window reproduces the two counts for m=4,…,7 (python3 /workspace/branches/independent_finite_checks.py 3). Definition 2.6 and Remark 2.7 of the cited v1 use prescribed starts and permit extra occurrences. Conjecture 7.1's stated odd/even ranks exhaust all ranks at K=2m, so the strict inequality refutes its maximizing assertion for j=2. The result does not establish minimality across all conjecture parameters or identify the true maximizers.

## originality

PASS

The primary source provides the counting framework and explicitly conjectures the contrary extremal assertion, but the inspected passages do not give the strict counterexample or the infinite 9/8 family. The family is a new supported comparison on examined evidence, not a new linear-extension technique or a priority certification.

## value

PASS

The counterexample excludes a natural published maximizing rule in the simplest nontrivial prescribed-occurrence regime, for infinitely many admissible overlaps. It isolates the obstruction: a local redistribution replaces three factors of two by two factors of three. That structural explanation is a useful constraint on any replacement conjecture even without a maximizer theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
