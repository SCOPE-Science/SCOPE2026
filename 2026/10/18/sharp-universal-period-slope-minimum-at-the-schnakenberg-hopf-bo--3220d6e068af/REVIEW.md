# Self-review: fixed-determinant Schnakenberg period slope

**Correctness — PASS.** At fixed \(0<s<1\) the trace is exactly \(\mu\) and the determinant exactly \(s^2\). Exact resonant Fourier projections yield \(m=1/(4s^2)\), \(\omega_2=-(9s^4-5s^2+1)/(24s^4)\); a separate complex cubic normal-form calculation verifies \(\Re c_{21}=-1/(8s^3)<0\). Standard nondegenerate Hopf theory supplies local existence, uniqueness, stability, and the asymptotic remainder. The symbolic checker confirms all critical identities; physical-time numerical shooting corroborates three different parameter values but is not a proof.

**Originality — PASS, with residual risk.** Liu–Shi–Wang–Feng (2013) treats exactly the same system and establishes Hopf location and supercriticality, but its stated period law stops at the linear leading term. The present exact period derivative and sharp universal minimizing feed balance are not implied by that statement. The 2021 same-model limit-cycle chapter and full 1979 founding paper were unavailable, and their unknown details are a genuine priority risk. Prior analyses of cycle uniqueness and of other reaction-network cycles do not give the present phase coefficient.

**Value — PASS.** Fixing the linearized determinant removes the first-order change of the linear frequency and isolates nonlinear slowing; the sharp lower bound \(1/6\) and unique optimizer \(s=1/\sqrt3\) characterize meaningful parameter-wide near-onset frequency sensitivity. This is a natural exact invariant, not a generic Hopf exercise or a small parameter-specific numerical improvement.

**Limits.** The conclusion is local to the small attracting Hopf cycle along the stated path. There is no global period monotonicity, no statement for larger cycles, and no uniformity at the ends of \(s\in(0,1)\). Historical text-access gaps remain.

Self-review: passed. Independent audit: not yet performed.
