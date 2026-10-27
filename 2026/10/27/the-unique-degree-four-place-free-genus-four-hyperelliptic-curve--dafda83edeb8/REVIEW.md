# Scientific review

**Correctness — PASS.** The symbolic argument proves that \(y^2=x^{q^2}-x\) is smooth of genus \((q^2-1)/2\) and has no degree-four points for every odd prime power \(q\). The exact upper bound is attributed to Aubry–Herbaut–Monaldi and yields equality for \(\rho\). The complete genus-four hyperelliptic enumeration over \(\mathbb F_3\) checks all 13,122 squarefree degree-nine and 39,366 squarefree degree-ten monic forms, and verifies that precisely one has \(B_4=0\). The twist argument reduces both nonsquare and square leading coefficients; the two possibilities for the exceptional polynomial are ground-field isomorphic.

**Originality — PASS, with residual risk.** Aubry–Herbaut–Monaldi's 2023 paper provides upper bounds and exact values only in genera at most three; Lario's accessible tables do not classify degree-four-point-free genus-four hyperelliptic curves over \(\mathbb F_3\). A 2025-2026 paper of the same authors concerns different maximality conditions. Targeted research-record and literature searches, including aliases, closed points, Frobenius orbits, Diophantine stability and extension-field equality, did not disclose equivalent coverage. The displayed equation itself is not claimed new. Possible unindexed arithmetic tables or a stronger indirect result remain a source of novelty uncertainty.

**Mathematical value — PASS.** The new invariant is the existence of a degree-four closed point, naturally tied to an explicit unsolved higher-genus range of \(\rho(q,g)\). A complete classification of all hyperelliptic genus-four counterexamples over \(\mathbb F_3\), followed by an infinite sharp threshold family, is substantial finite arithmetic geometry rather than a routine isolated example. The nonhyperelliptic genus-four locus is deliberately excluded from the uniqueness assertion.

**Independent validation:** not performed. The exact C++ enumeration and separate Python witness checker accompany the proof. Self-review checked the hypotheses, finite-field arithmetic, proof of nonsquareness, quantifiers, comparison to stronger literature, and residual limits.

Self-review: passed. Independent audit: not yet performed.
