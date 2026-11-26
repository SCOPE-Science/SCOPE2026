---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Expanded the tandem FCFS recursions and independently proved all three statements via the backward maximum for total waiting; details in /workspace/audit-01-derivation.md. For a Palm customer 0 with a_0=0, the terms are a_i+(j−i)c+Σ_{ℓ=j}^{−1}S_ℓ for i≤j≤0. The diagonal gives the c=0 waiting time. If S≥c each term is bounded by its i-diagonal, establishing the finite transfer and the stationary extension by the monotone limit of the finite backward maxima. In the sharpness example the frozen line 34 has a local arithmetic typo: Y_2(0)=s+s_2, not 2s+s_2. With the arrivals given there, Y_2(c)=2c+s_2, so the stated violation by c−s is correct (for s=0 the excess is c−ε). The waiting times exclude both services. Subtracting the independent-of-downstream M/D/1 mean first wait from the M/G/1 mean total wait gives the floor formula. For small c without a floor, write m=j−i≥1, h=−j, U_m for the pre-j sum of m external gaps, R_m for their m downstream marks, and V_h for the subsequent downstream-mark-minus-gap sum. To improve on the diagonal maximum a term must have U_m<mc, R_m<mc and V_h>−mc, by comparing with both endpoint diagonals and the zero term. Its gain is bounded by mc. These three variables are independent. Use the gamma bound P(U_m<mc)≤(eλc)^m and P(V_h>−mc)≤e^(αmc)r^h with r=E exp(α(S−A))<1 by the exponential moment and strict load bound. Summing the gains over m,h gives O(c²P(S<c)+c³)=o(c²) for positive S, with m=1 producing the P(S<c) factor. This also bounds the backward supremum and its mean. Thus the change of total waiting is o(c²), whereas the added mean first-station wait is λc²/(2(1−λc)), proving (F(0)−F(c))/c²→λ/2. The direct check avoids relying on derivative interchange or on a verbatim general-service reading of Cao–Hu–Wang Eq. (14). The frozen script was inspected but not run; its finite checks do not prove either stationary theorem.

## originality

PASS

The supported distinct claims are exact delay transfer under a service floor and, especially, the no-floor small-duration coefficient for positive independent downstream marks under the stated regularity and load hypotheses. Classical FCFS recursions, mean-delay identities, and stationary IPA/group methods are prior, as is monotonicity. The unavailable full Niu text leaves a specified risk for the floor formula; no exhaustive priority or novelty of the component tools is asserted.

## value

PASS

The pathwise transfer explains when an upstream deterministic operation moves waiting between stations without changing its total. The universal near-zero coefficient gives a quantitative prediction where monotonicity gives only a sign, and where a floor argument fails for every positive c. It isolates the small-duration sensitivity at fixed arrival rate, not a light-traffic approximation obtained by changing that rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
