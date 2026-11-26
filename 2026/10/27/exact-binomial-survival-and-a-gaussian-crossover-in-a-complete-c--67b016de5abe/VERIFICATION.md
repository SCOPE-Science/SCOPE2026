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

For initial two-count k, every two falls to one, and the sign at a one is the sign of T_n−k. If the ones die, the k survivors at one are already on the uniform two-cycle for k≥2; a singleton fixes at two on the next update. If the ones rise, the roles switch and the remaining extinction test at update two compares n−k to T_n. The second update either restores the initial state or leaves the retained sites uniformly at one. Endpoints k=0,n give full survival. At ties k=T_n or n−k=T_n, the full state becomes uniform at one by the corresponding update if no earlier extinction occurred. For all other initial counts the strict formula is unchanged, even if T_n is integral. The at-most-two binomial atoms have total mass O(n^{-1/2}). Complete survival away from these atoms and endpoints is the strict interval |(2k−n)/sqrt(n)|<2s for s>0, empty for s≤0. The CLT then gives the asserted atom at one, while on the complementary event the distance to 1/2 is bounded by |k/n−1/2| except on the negligible ties. Bounded convergence of the expectations follows from weak convergence on [0,1]. At fixed alpha=2/3 the threshold equals (n−1)/2, giving the critical limit; on either strict side the LLN gives the stated jump. Independent integer arithmetic verified two-step entry, occupancies and binomial multiplicities in 1,200 exchangeability classes at n=3..11, sampling every threshold chamber and boundary. The frozen replay path is verify.py, a rational finite test excluding ties; it was inspected, not executed. No finite test is evidence for the CLT by itself.

## originality

PASS

Pass for the exact finite complete-graph survival law and its critical-window mixture. The map, asymptotic vacancy threshold, atypical full occupancy beyond that threshold, and maximum eventual period have antecedents; they are not claimed new. The prior-work paragraph would be more complete if it mentioned the same paper's analysis of full-occupancy entropy and alpha_atyp. That overlap does not give the finite census or the crossover.

## value

PASS

The finite law quantifies how a canonical complete-mixing limit approaches a known discontinuity, and gives exact probabilities even for atypical full occupancy. The natural threshold window produces a one-sided Gaussian probability weight for a non-Gaussian limiting mixture, a more precise answer than either the bulk threshold or an eventual-period theorem. The elementary case split and CLT are methods; the exact finite count and window are the result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
