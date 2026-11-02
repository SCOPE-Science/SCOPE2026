---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Independently reconstructed δ_C(t)=E[F_t²] for F_t=P(Y≤t|X), ordered in t with E F_t=t. δ(a)=a forces F_a=1_A, P(A)=a, and F_b=F_c=1 on A; δ(b)=a+(b-a)²/(1-a) makes F_b=(b-a)/(1-a)=α constant on A^c. With E[T|A^c]=γ=(c-a)/(1-a) and α≤T=F_c≤1, Jensen and (T−α)(1−T)≥0 yield exactly L=a+(c-a)²/(1-a) and U=c−(b-a)(1-c)/(1-a). Conditional-row probabilities for both endpoints have nonnegative masses summing to 1; splitting latent row intervals constructs a valid checkerboard input copula and arbitrary convex interpolation. Pairwise targets (1/4,1/2,3/4) give d=1/3, L=7/12, U=2/3, excluding 3/4, although (a,b),(a,c),(b,c) pairs have separate witnesses. Four distinct exact rational triples were independently checked, not mistaken for a universal proof. Strict a<b<c<1 protects all divisions and yields positive interval width.

## originality

PASS

Independently compared the exact final mathematical statement, not just title or matching parameter, with the primary material identified below and a new semantic research-index search. No inspected stronger statement implies the precise final claim; foundational results and methods are credited. This is a qualified best-of-knowledge judgment with explicitly retained gaps, not a certification of priority.

## value

PASS

The exact three-anchor range on the first saturated/second minimal-variance boundary answers a natural constrained conditional-moment compatibility problem explicitly highlighted as unresolved by the originating paper. Sharp interval realization and a continuum of pairwise-feasible but jointly impossible specifications give structural content beyond a one-point numerical example. It is not a classification of all multithreshold moment data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
