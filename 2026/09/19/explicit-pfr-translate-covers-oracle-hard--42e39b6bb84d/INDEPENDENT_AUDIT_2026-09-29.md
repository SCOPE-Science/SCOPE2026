# Independent Audit — Explicit PFR translate covers are oracle-hard even below doubling two

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `b13ea2c77960aeeb1373dbe78d06b6d0257c5d16`  
**Audited current source tree:** `b13ea2c77960aeeb1373dbe78d06b6d0257c5d16`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree exactly matches the assigned source-tree SHA. GitHub was used read-only as evidence, and the dated independent-audit files were absent when this guarded plan was prepared.

## Correctness — PASS

PASS. For A_z=H∪{z}, A_z+A_z=H∪(z+H), so K<2 and H,z+H give an admissible two-coset cover; one coset with |V|≤|A_z| is impossible. If L cosets of V cover H and h=dim(V∩H), then 2^{m-h}≤L, while dim pi(V)≤m-h; hence the projected union contains at most L·2^{dim pi(V)}≤L^2 quotient classes and any fixed successful output covers at most L^2 possible hidden outliers. Until a sample or membership query identifies z, the transcript only excludes tested z-values, leaving z uniform over at least M-q candidates. The stated success bound and M/6 lower bound follow. Independent small-m checks reproduce the doubling identity and quotient-dimension constraint.

## Originality — PASS

PASS, narrowly scoped. The September 2026 algorithmic PFR theorem explicitly assumes uniform-sample plus membership-oracle access and outputs a subspace of size at most |A| whose K^{O(1)} translates cover A; its public theorem/abstract does not require materializing those translate representatives. Earlier 2025--2026 algorithmic and robust PFR formulations similarly construct subspaces and bound covering numbers. Targeted searches for explicit translate-list recovery/query lower bounds did not locate this hidden-outlier barrier. Folklore risk is real because the instance and information argument are short, so the novelty claim is limited to the explicit oracle-output separation.

## Scientific value — PASS

PASS. The theorem explains an otherwise subtle output convention in algorithmic PFR: even below doubling two, and even with the correct structured subspace supplied for free, explicitly recovering a constant-size translate cover can require exponentially many sample/query interactions. This cleanly separates structural subspace recovery from witness materialization.

## Independent checks

- Recomputed |A_z|, |A_z+A_z|, the exact doubling constant, and the optimal two-coset cover.
- Reproved the structural L^2 bound through V∩H and the quotient G/H, allowing arbitrary admissible V and noncanonical/overlapping translate representatives.
- Checked adaptive membership queries: before the first positive answer all informative responses merely exclude candidate z values, so conditioning preserves uniformity on the untested set.
- Checked the constants in the 2/3 lower bound: s+q≤M/6 contributes at most 1/6 and L^2/(M-q)≤1/10.
- Independently checked small m doubling cases and compared with the repository's finite subspace verification only as supplementary evidence.
- Compared the output convention against the current algorithmic PFR theorem and robust-PFR formulations; targeted searches found no explicit-cover lower bound.
- Verified the assigned record tree is unchanged from the dispatcher source-check commit to current main and that the dated audit markers are absent.

## Limitations

- The lower bound is specific to explicit lists of translate representatives under uniform-sample plus point-membership access; stronger access or compressed symbolic witnesses may evade it.
- The proof is intentionally elementary, so an unrecorded folklore observation cannot be excluded absolutely.
- No lower bound is asserted for the subspace-only output task solved by algorithmic PFR.

## Evidence and references

- https://arxiv.org/abs/2609.20771
- https://eccc.weizmann.ac.il/report/2026/189/
- https://arxiv.org/abs/2604.04547
- https://arxiv.org/abs/2608.00451
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/19/explicit-pfr-translate-covers-oracle-hard--42e39b6bb84d

This change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
