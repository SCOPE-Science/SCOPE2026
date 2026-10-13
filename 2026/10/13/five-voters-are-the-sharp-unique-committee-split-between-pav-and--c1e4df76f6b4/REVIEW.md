# Self-review

## Correctness
**PASS.** The lower bound does not rely only on enumeration. After normalizing a putative conflict to PAV winner \(\{A,B\}\) and CC winner \(\{A,C\}\), unique CC forces singleton counts \(b<a,c\), while the strict PAV comparison \(P_{AB}>P_{AC}\) forces \(x-y>2(c-b)\), hence at least three \(\{A,B\}\) ballots. Therefore \(n\ge a+c+x\ge5\). Equality forces exactly the canonical \(3\times\{A,B\}+\{A\}+\{C\}\) profile. A separate exact verifier independently exhausts labeled and anonymous profiles and reproduces the orbit and incidence counts.

Risk: the classification is intentionally restricted to three candidates and two seats.

## Originality
**PASS.** The inspected primary literature defines PAV, defines approval CC as coverage/maximum coverage, and explicitly identifies approval CC as weighted PAV with vector \((1,0,\ldots)\). Later literature compares approval-based committee objectives quantitatively, and a recent source uses the same three-candidate, two-seat CC geometry. None of the inspected material states the five-voter unique-winner boundary, the canonical \(3,1,1\) obstruction, or the exact \(120\)-profile census. Exact-count, alias, weighted-Thiele, and canonical-pattern searches also did not locate a covering statement.

Risk: a small unpublished or poorly indexed example table could contain the same profile; failed search is not a proof of bibliographic uniqueness.

## Value
**PASS.** PAV and approval CC are canonical but materially different approval-committee objectives: harmonic diminishing returns versus one-hit voter coverage. The first electorate where they make different unambiguous choices is therefore a natural structural boundary. The boundary is especially informative because its entire first layer collapses to one transparent orbit, showing exactly how repeated representation of a cohesive bloc first defeats maximum coverage.

Self-review: passed. Independent audit: not yet performed.
