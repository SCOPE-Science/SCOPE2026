---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For coprime integers p,q>1 and s>1 coprime with pq, map a to x^q and b to y*x^p*y^{-1} from <a,b|a^p=b^q> to <x,y|x^{pq}=y^s>. The relation is respected because both pth and qth images equal k=x^{pq}, which is central. Quotient by central powers gives C_p*C_q to C_{pq}*C_s. Images x^q and y*x^p*y^{-1} have exact orders p,q and lie in distinct conjugates of the C_{pq} factor; alternating nonidentity syllables remain reduced when y words are inserted, so the quotient map is injective. Any kernel is therefore contained in the central <a^p>; its generator maps to k, which has infinite order under homomorphism x→s,y→pq to Z. Hence injective. Both full centers are these infinite cyclic powers, because quotient free products have trivial centers; a finite-order element of C_p*C_q has order dividing p or q, so cannot have order pq, while C_{pq}*C_s does have one. Thus groups are nonisomorphic. Example (p,q,s)=(2,3,5) gives G_{2,3}↪G_{6,5}. This proves sufficiency, not classification of all embeddings.

## originality

PASS

The cited Myers prime-parameter lemma concerns embeddings when each exponent is prime; the current explicit composite target pq and conjugation construction is outside it. The normal-form argument is elementary, but the infinite three-parameter counterfamily to naïve extension of prime rigidity is not printed or implied by the inspected prime-only lemma. General torus-knot subgroup classification remains an important priority risk.

## value

PASS

Testing whether Myers-style prime-exponent embedding rigidity extends to arbitrary torus-knot groups is a motivated group-theoretic boundary question. An infinite concrete coprime composite-target family with explicit injective maps and nonisomorphism witnesses resolves a genuine necessary-hypothesis boundary, not a randomly chosen finite example. The proof is elementary and makes no claim to a general embedding classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
