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

Haar averaging over the two lifts of a residue changes the sign of the next cosine, giving consistent positive cylinder masses 2^(-N)R_N. Squaring each factor gives digit weights h_0=1+a²/2, h_±1=a, h_±2=a²/4. In the Fourier sum, the congruence is modulo 2^N, so all three terminal carries, not just zero, count. The even digit-plus-carry transition yields states -1,0,1, with the two signed states having equal weight, and gives the stated matrix, trace and determinant. The characteristic polynomial is positive at 0, negative at 1 and positive at 2; S_0=1 and S_1=1+a² fix the two-root formula and the positive leading weight. The level-N collision probability is 2^(-N)S_N and tends to zero. Telescoping the kernel between adjacent scales gives a nonnegative energy sum with multiplier 1-2^(-s), also valid truncated at N by capping the valuation. The generating function, convergence threshold, pole and linear critical truncation all follow from the two roots; the smaller root contributes boundedly at criticality. An independent finite computation at a=1/2, N=4 gave S_4=4633/2048 via all 625 digit tuples and agreed with the direct residue average and the transfer. Source: /workspace/branches/c70fc0f0-dc2e-4174-ac8c-981994cb03fb/independent_carry_check.py. The frozen checker was inspected, not executed; no finite check establishes the all-level theorem.

## originality

PASS

The supported distinction is the exact L² transfer and evaluated energy of the constant real-amplitude consecutive dyadic measure. Generic energy/Fourier identities and a Fourier-dimension theorem for the same object are antecedents, not this evaluation. The most plausible historical same-object full-text comparison remains unresolved; there is no verified prior equivalent in the material inspected.

## value

PASS

The first dependent conductor regime changes the scale of pair collisions on a natural compact group. An exact transfer determines both the energy threshold and its sharp coefficient, quantifying behavior that Fourier dimension zero does not describe. This is more useful than a finite numerical norm or a general unevaluated energy identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
