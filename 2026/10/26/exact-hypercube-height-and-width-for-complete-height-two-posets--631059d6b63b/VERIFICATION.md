---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Let U be union of a incomparable lower Boolean sets; Sperner bounds a≤binom(|U|,floor(|U|/2)), hence |U|≥mu(a). With b>=2 incomparable upper sets, no upper is U, so rank ≥mu(a)+1. Minimal mu(a) forces any a selected central-layer subsets of [mu(a)] to cover all mu(a) coordinates, since otherwise Sperner on mu(a)-1 coordinates would contradict minimality. Adding b distinct new coordinates to that union gives b incomparable upper sets of size mu(a)+1. At minimum rank the lower union has size exactly mu(a) and each upper must be union plus a distinct new coordinate; w*=mu(a)+b follows, as does w*=a+b iff a=2,3,4. Checked mu(a) for a=2..15; the Sperner/union argument proves all a,b≥2.

## originality

PASS

Qualified PASS for exact two-parameter evaluation in the natural complete height-two family, with elementary proof and genuine folklore risk. Flídr–Ivan–Jaffe (arXiv:2509.26630) introduce h*,w*, prove the general upper bound w*(P)≤|P| and ask which posets achieve equality (Question 8). The inspected paper text does not state both formulas or the full equality criterion. This is not novelty for Sperner or isolated equality witnesses; it is a precise full-family invariant.

## value

PASS

Complete height-two posets are a canonical first family testing a published structural equality question for optimized Boolean embeddings. The result determines both hypercube invariants for all two-level sizes and the exact equality region; an exact natural classification can be independently valuable despite its short Sperner proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
