---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For fixed α>−1 and standard L_n^(α)(0)=binom(n+α,n), the primitive F= x^(α+1)e^(−x)L_(n−1)^(α+1)/n satisfies F′=x^α e^(−x)L_n^(α) and F″+(1−α/x)F′+(n/x)F=0. Stieltjes integration by parts gives the exact BV norm sup|F|, attained by a single Heaviside jump. The exact Sonin derivative d/dx(F²+x F′²/n)=(2α+1−2x)F′²/n puts the global maximum at first zero for −1<α≤−1/2, otherwise at nearest zeros bracketing x*=α+1/2. Mehler–Heine scaling of first root gives n M→(j_(α,1)/2)^(α+1)|J_(α+1)(j_(α,1))| in edge regime; compact-uniform Plancherel–Rotach oscillations with local zero spacing O(n^(−1/2)) give bulk M~n^(α/2−3/4)e^(−x*/2)(x*)^(α/2+1/4)/√π. α=−1/2 matches 1/√π. Independently recomputed root extremizers at n=9 for α=−.8,−.5,0,1; these bounded checks do not establish classical asymptotic uniformity.

## originality

PASS

Sluchak’s 2026-11-02 paper covers the generic variation-by-primitive principle and ordinary Laguerre primitive but its inspected Section 8 does not provide the parameter-uniform sharp generalized-Laguerre global maximizer or both asymptotic constants. Another Resultary 2026-11-08 record explicitly establishes only α=0 (a proper bulk specialization); it does not cover −1<α≤−1/2 or arbitrary α>−1, and the assigned full-parameter transition has independent substantive mathematical scope. Classical DLMF special-function formulas supply proof ingredients, not the sharp global classification. Residual risk from uninspected older generalized Sonin/orthogonal polynomial extremum literature and 2023 Laguerre jump-coefficient source.

## value

PASS

Sharp BV-to-Laguerre coefficient operator norms and locations of maximizing jumps are natural approximation-theoretic invariants. The parameter α=−1/2 changes the optimal localization from the hard edge x~1/n to positive bulk x*=α+1/2, with genuinely different decay exponents; the all-α classification is motivated, not an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
