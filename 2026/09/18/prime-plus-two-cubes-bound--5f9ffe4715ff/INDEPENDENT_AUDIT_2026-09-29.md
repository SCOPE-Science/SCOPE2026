# Independent Audit — Prime plus two positive cubes below 333334^3

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `52c822dd62b2bec0dc7146a620adc992375247af`  
**Audited current source tree:** `52c822dd62b2bec0dc7146a620adc992375247af`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree exactly matches the assigned source-tree SHA. GitHub was used read-only as evidence; no repository change was made during the audit.

## Correctness — PASS

PASS. The first-two-cube branch is exhaustively reduced by b^3-a^3=3t^2-3t+1, equivalently 12(b^3-a^3)-3=(6t-3)^2. For t≤333333 and the floor condition, a≤6933 and b≤8735, so the finite (a,b) search is complete. An independently compiled integer implementation reproduced exactly 36,531,779 pairs, 7,683 integral-t equalities, 579 floor-admissible first-pair solutions, and zero triple-cube obstructions. Applegate–Pratt Theorems 3.1–3.2 and Corollary 3.5 then give the extension: below 10^16 the source result applies; above it, the unresolved two-cube branch has third residual alpha2=n-(t-2)^3 between the largest E3 exception and 10^12, and the new computation makes alpha2 a noncube, so Theorem 3.1 supplies alpha2=p+x^3. The resulting endpoint is 333334^3=37037259259703704.

## Originality — PASS

PASS. The full open Applegate–Pratt paper was inspected. It proves the two-cube representation only through 10^16, explicitly isolates the two-adjacent-cube branch, and states the stronger three-consecutive shifted-cube assertion as Conjecture 5.1; its reported brute force toward the stronger equality conjecture reaches only t<10^4. Searches did not locate the endpoint 333334^3 or an equivalent t≤333333 exclusion. The submitted finite reduction therefore supplies a new certified extension rather than restating the source computation.

## Scientific value — PASS

PASS. The record raises a concrete verified prime-plus-two-cubes range by a factor of about 3.7 and simultaneously pushes the exact triple-cube obstruction relevant to the source bootstrap from a reported 10^4 search scale to 333333. The discriminant reduction makes the finite verification compact and independently reproducible, and the deduction reuses the source’s published 10^12 prime-plus-one-cube computation efficiently.

## Independent checks

- Read and visually checked the open source PDF pages for Theorems 3.1–3.2, Corollary 3.5, and Conjectures 5.1–5.2.
- Re-derived the discriminant square identity and global a,b bounds from the floor condition.
- Ran an independent compiled exhaustive search and reproduced the 36,531,779 / 7,683 / 579 / 0 counts exactly.
- Recomputed the third-residual upper and lower bounds needed to invoke Applegate–Pratt Theorem 3.1.
- Checked the endpoint cube 333334^3 and the positivity of the reused cube t-2.
- Verified the current main directory tree SHA exactly equals the assigned source tree SHA.

## Limitations

- The result is a finite verification and does not prove the source’s Conjecture 5.1 for all n.
- The large 10^12 prime-plus-one-cube computation and the source interval through 10^16 are used as published inputs rather than rerun independently.
- The motivating preprint is extremely recent, so unindexed simultaneous work remains a residual originality risk.

## Evidence and references

- https://arxiv.org/abs/2609.20505
- https://github.com/kapplegate2020/Sums-of-a-Prime-with-Squares-or-Cubes
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/18/prime-plus-two-cubes-bound--5f9ffe4715ff

This change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
