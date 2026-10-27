# Review summary

**Correctness (C): PASS.** The error recurrence is \(e_{k+n}=\sigma(I-2A/(L+\mu))e_k\), whose worst-case norm factor per block is \((L-\mu)/(L+\mu)\). For any admissible numerator, the endpoint constant-term identity \(L p_\mu(0)-\mu p_L(0)=-\sigma(L-\mu)\) forces the same lower bound on the largest root modulus. The proposed numerator attains it.

**Originality (O): PASS, subject to the stated literature limits.** The closest direct source proves the general lower bound but gives explicit optimal constructions only for degrees \(1,2,3\). The polynomial-variation result uses \((z-1)^n\) and a different algorithm class; the inspected internal-model papers address tracking conditions rather than this minimax rate. Searches of the findings index returned adjacent but non-equivalent records, not this claim. Classical repetitive-control literature remains a residual risk.

**Value (V): PASS.** This supplies a closed-form optimal controller for a natural infinite family of periodic and antiperiodic models at every degree \(n\ge4\), converting a general lower bound into an exact constructive benchmark. The statement is deliberately not generalized to arbitrary unit-circle pole sets.

Closest literature: Van Scoy–Bianchin, arXiv:2510.12512v1; Wu–Petersen–Shames, arXiv:2508.21335v2; Bianchin–Van Scoy, arXiv:2407.08037v3 and the 2025 CDC paper identified in the references.

Self-review: passed. Independent audit: not yet performed.
