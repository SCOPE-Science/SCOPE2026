# Scientific review

## Correctness — PASS

The proof derives the exact two-selected-party inversion count and mean directly from fixed marginals; the variance becomes a squared pair-label-sum deviation. Mirror pairs attain zero for even populations, and zero cost permits no other support. For odd populations the central party's fixed inclusion probability yields the pointwise dual bound \(2/n\); equality pins the support to outer mirror pairs and the central triangle, whose weights are forced. The all-population anonymity benchmark follows from exact covariance of two draws without replacement. Finite tests (exact rational, \(3\le n\le100\), plus independent numerical linear programs for \(3\le n\le18\)) corroborate rather than substitute for the proof.

## Originality — PASS, qualified

The closest primary work is La Commare, Tucker-Foltz, and Verdugo, *Envy-Free Randomized Apportionment*, arXiv:2610.24217v1, Sections 2–4. It already proves the fixed mean and polynomial-time variance optimization. The present contribution is a uniform closed-form parity value, **unique** optimizing distribution and exact anonymous benchmark in the two-residual-seat equal-entitlement case; neither these statements nor an implication establishing them directly was identified in the inspected material. Other known multi-floor apportionment results address different feasibility and expectation objectives. General balanced-sampling sources are closely related, but full access was incomplete and an unindexed equivalent classification remains a priority risk. These are scientific priority qualifications, not claims of exhaustive novelty verification.

## Mathematical value — PASS

This is an exact risk classification for the smallest nontrivial correlated two-seat apportionment problem, motivated by the variance objective explicitly proposed in the source. The parity obstruction is structural, not an arbitrary finite census. The all-population uniqueness and the enormous difference between anonymous and unrestricted variance quantify a genuine cost of requiring party-symmetric tie-breaking under an otherwise arbitrary fixed order.

## Scope and limitations

The theorem is about a fixed arbitrary index-based convention for equal-residue ties. The risk-optimal mechanism is not anonymous for \(n\ge4\). Different definitions of envy at exact ties, nonuniform residues, additional residual seats and inter-house-size consistency are outside the claim. Numerical LP checks use floating point but the algebraic lower bound and support argument are exact; no external independent validation is asserted.

Self-review: passed. Independent audit: not yet performed.
