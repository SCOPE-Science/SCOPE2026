---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

Checked displayed H=q(x)y²/2+V(x), q=1+2ax+kx², V=x²/2-a x³/3+kx⁴/4: independently expanding H_x xdot+H_y ydot gave exactly zero. k>a² makes q>0 and V single-well/coercive, so two turning points and one periodic oval for each E>0. Original-time period T=sqrt(2/E)J follows from both traversals, without hidden time reparameterization. Splitting J into asinh primitive J0 and turn-point correction J1, the latter tends log(2)/sqrt(k) by integrable moving-endpoint dominated convergence; together yield stated log(8k²/(k-a²)). On |x|≤s_E^u with 0<u<1, (1-V/E)^-1/2→1 uniformly and integral per sign is u log(s_E)/sqrt(k)+o(log s_E), yielding each probability u/2 and joint weak limit. Fixed-parameter, nondegenerate boundaries respected; finite checker not proof.

## originality

PASS

Llibre–Rondón Theorem 2(c), equation (23) already classifies this exact cubic family under k>a² as global center. Ghose-Choudhury–Guha supply the broad variable-mass period quadrature, a methodological antecedent; neither reviewed statement fixes the two-term discriminant constant or signed log-scale occupation. Other published Resultary cubic-center records concern different vector fields/invariants. No verified stronger coverage of both quantified asymptotics was found; source classification and generic quadrature remain explicitly credited.

## value

PASS

For a naturally classified global-center polynomial family, qualitative periodicity does not determine speed along large orbits. The logarithmic physical-time period with a parameter-dependent additive constant and log-uniform signed occupation give two exact global-dynamical invariants not implied by local linear center or generic period existence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
