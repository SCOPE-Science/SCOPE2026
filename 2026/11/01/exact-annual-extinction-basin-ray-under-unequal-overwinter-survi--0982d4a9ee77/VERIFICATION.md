---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

Under ξ1=ξ2, q=y/x obeys (log q)'=A−β1/(1+αq) independently of total magnitude; w=αq obeys w'=w(Aw−C)/(1+w), A=g2+μ1, C=g1−g2. The annual map Q(q)=(δ2/δ1)φτ(q) has Q(q)/q strictly increasing since f'(q)>0 and order preservation. Endpoint multipliers Q/q→Λ2/Λ1<1 as q↓0 and →(δ2/δ1)exp(Aτ)>1 as q→∞ from 1<Λ2<Λ1 and δ_i≤1; hence a unique repelling q*>0, below it q_n→0 and above it q_n→∞. Integration at φτ(q*)=s q*, s=δ1/δ2, yields q*=(C/A)(H−1)/(α(H−s)), H=(s exp(Cτ))^(A/β1), for C≠0, and (1−1/s)/(α(Aτ−log s)) if C=0. The potentially singular denominator H=s is ruled out by the multipliers; nonzero H−1 under strict inequalities; C=0 branch valid with s>1. On invariant q* ray, y follows Beverton–Holt map Λ2 y/(1+ξJy), J>0, attracting all positive points to unique annual saddle E with eigenvalues Q'(q*)>1 and 1/Λ2<1. Off ray, reciprocal population recurrence has asymptotically contracting coefficients and converges to axial R1 or R2. Thus exact annual basin partition, not necessarily a fixed separator within the favorable season; finite numerical verifier's three samples are corroborative only.

## originality

PASS

Best-of-knowledge: the exact new assertion was compared to its natural aliases, stronger/general results and selected primary literature, as well as the Resultary search. Known foundations are not claimed as new. Sources read and unresolved priority limitations are recorded explicitly. extinction.

## value

PASS

In a biologically motivated bistable seasonal competition model, the explicit annual initial-ratio threshold is a globally valid separatrix and predicts extinction outcome from initial population ratio, including unequal overwinter survival and equal-growth degeneracy. The closed formula independent of common crowding ξ and inverse in mating-competition α is useful quantitative information beyond general existence of a separating curve.

The dated certificate retains the supplied scientific assessment, sources and limitations.
