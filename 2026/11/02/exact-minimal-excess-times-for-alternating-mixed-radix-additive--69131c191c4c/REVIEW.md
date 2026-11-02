# Self-review

**Correctness — PASS.** Each mixed-radix integer decomposes uniquely into its even- and odd-position components. At the highest occupied position \(k\), the excess reduces exactly to a truncated finite-pair count \(\beta_k A_k(u)-(u+1)\) or its swapped analogue. For every proper lower block, the explicit additional pair in the proof forces strict inequality; at the completed block the excess is exactly one. This argument covers the boundary \(n=0\), every radix \(r_i\ge2\), and every integer \(n\ge0\). Nine bounded independent enumerations corroborate the stated classification and count.

**Originality — PASS with residual priority risk.** The original construction and existence of infinitely many minimal-excess points are already in Ma (2022), Lemma 3.1 and (3.1), and in the earlier digit-separated literature. Zhang (2026), Section 6, lists equality at \(4^k-1\) for the base-four model. Neither inspected result gives the exact if-and-only-if return set nor the arbitrary-radix counting law. Three semantically targeted research-record queries and targeted exact-phrase literature searches revealed no equivalent or stronger statement. This is not a claim of an independently certified literature survey; earlier Chen–Fang material and unindexed digital decompositions remain priority risks.

**Mathematical value — PASS.** At the critical sharpness construction for additive-complement excess, the distinction between occasional equality and a complete description of equality times is mathematically natural. The theorem classifies the full equality locus for all mixed radices and quantifies its scarcity, identifying previously unmentioned intervening binary-scale returns for the base-four extremal example. It is a structural exact theorem, not an arbitrary finite search or an improvement of the known sharp global threshold.

The result concerns the established digit-separated family, not all additive complements. The Python enumeration does not prove infinite validity. Primary overlap was compared by statements and implication, with a residual risk of unindexed equivalent proofs.

Self-review: passed. Independent audit: not yet performed.
