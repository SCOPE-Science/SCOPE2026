---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The consecutive nonpositive X-coordinates force x_{j+2}=B and y_{j+2}=B; D>1+T+T² gives the displayed four-cycle, with its two negative consecutive X values. At T=0 the parity-coordinate subsequences evolve by the scalar g; the positive branch maps onto the whole interval with slope −D, so survival cylinders have relative lengths D^(−k). Scalar first hits of B from the two independent coordinates are geometric; their nonpositive scalar indices are h−1,h+1,… and k−1,k+1,…. Aligning the even and odd subsequences gives the three stated times (same parity: 2 max; h>k with different parity: 2h−1; k>h: 2k+1). The ±1 corrections cancel by exchangeability and summing max tails yields the exact mean. Scaling the two independent geometric variables and dropping the bounded integer correction gives the claimed critical limit. The frozen continuity proof is correct by strict signs and almost-sure finite boundary reset; the repaired quantitative claim is stronger and was separately checked: normalize B=1, set a=√D and M=max(1,D−1). The orbit errors obey e₀=0, e₁≤T, e_{j+2}≤D e_j+T e_{j+1}+TM. Adding cT with c=M/(D−1) absorbs the forcing; (a+T)²≥D+T(a+T), so e_j≤(1+c)T(a+T)^j. At the boundary each marginal consists of a uniform component of weight D^(−floor(j/2)) and atoms at 1 and 1−D, because the active branch takes the continuing uniform component onto the whole interval. For N=floor(log_a(1/T))−K_D, pick K_D so errors through N are strictly below the smallest absolute endpoint. The signed-threshold disagreement then has probability O_D(T) per iterate: the continuous density attenuation cancels the error growth up to bounded (1+T/a)^N and parity factors. The geometric law bounds the exceptional event R₀>N by O_D(T). Union over N+1 switches and the total-variation coupling prove O_D(T log(1/T)), even on the extended countable state space. The packaged rational checker was inspected, not executed, and does not prove the rate.

## originality

PASS

Pass the quantitative small-coupling stability of the complete-reset law at fixed D, with the correct finite-D clock. Credit the shared geometric mechanism and the critical law explicitly, rather than treating a shift of initial square or a bounded change of cycle phase as a new critical scaling result. The exact first-capture distribution for positive-square draws differs from the complete-reset distribution at fixed D; the ingredients of its proof do supply the boundary geometric law by a simple shift and substantial overlap. None of the inspected direct comparisons gives the repaired total-variation rate. It requires quantitative cancellation between branch expansion and attenuation of the uniform part, not just finite orbit continuity or cycle stability.

## value

PASS

The quantitative complete-reset law answers a natural perturbation question for a coupled map with a moving switch and an expanding active branch. It controls all stopping events, rather than just continuity at fixed observation time or the distribution of reaching any cycle phase for the boundary map. Its explicit rate makes the overlap in the geometric critical calculation supporting material, not the reason for acceptance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
