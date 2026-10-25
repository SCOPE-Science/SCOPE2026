# Scientific review: support–gcd conjugacy classification

## Correctness

**PASS.** The finding proves the full algebra automorphism group for a pure evolution chain, computes its affine/scaling action on the annihilator-valued operator coefficients, determines stabilizers by the identity \(\gcd(2^r-1,2^s-1)=2^{\gcd(r,s)}-1\), and applies orbit–stabilizer and Burnside to the exact support census. These steps establish all \(e\ge1\), \(n\ge2\). The included `verify.py` exhausts automorphism matrices for two small cases and orbit partitions for ten field/dimension pairs; it returns `VERIFY_OK`. Testing is finite corroboration, not an infinite proof.

## Originality

**PASS, with priority qualification.** The new content is the complete characteristic-two automorphism-conjugacy orbit-size, support and stabilizer classification, not the existing characterization of the operator space or the previously described chain automorphism group. The closest articles are Qaralleh–Mukhamedov–Khakimov (arXiv:2606.22623v1 and 2601.08669v1) on characteristic-zero operators and Mukhamedov–Khakimov–Omirov–Qaralleh (arXiv:1805.10285v2) on automorphisms. A prior characteristic-two operator-space calculation supplies the prerequisite but not the orbit count. Earlier odd-field chain-orbit work has incompatible field hypotheses and a larger operator family. An indexed exterior-algebra Rota–Baxter orbit census concerns a different algebra. No equivalent all-even-field orbit census was located. Older/unindexed conjugacy-enumeration literature may still overlap.

## Mathematical value

**PASS.** This is a complete inequivalent-operator classification for an infinite algebraic family, not merely a count of labeled operators. The support-dependent stabilizers show explicitly how field extension degree interacts with chain length; the exact arithmetic divisor sum and boundary formulas support further classification and comparison of operator structures.

## Limits and audit status

Only finite characteristic-two fields and pure maximal-nilindex chains are covered. The algebra automorphism and operator-parametrization ingredients are not asserted as novel. Small computations do not justify arbitrary parameters without the displayed proof. Literature priority may change with full inspection of unindexed sources. No independent expert or formal audit has been performed.

Self-review: passed. Independent audit: not yet performed.
