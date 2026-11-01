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

For q fixed, the fraction of matrices with a zero row or a proportional row pair is O_q(n^2 q^{-n}). On 2LI matrices, rank-one left multiplication by any natural-basis vector forces a singleton support relative to the original basis, hence every natural basis change is monomial. The group ((F_q^*)^n)⋊S_n has order (q-1)^n n!; summing nonidentity fixed-point fractions gives O_q(n^2(1-1/q)^n) from support-s permutation orbit and diagonal-scaling bounds. The sandwich between genuine algebra-isomorphism classes and monomial orbits on the full and 2LI subsets gives a uniform absolute error across coranks. Standard rank-k matrix count gives exact principal probability q^{-r^2}product_{j>r}(1-q^{-j})^2/P_{n-r}(q). Sum over all ranks needs the joint sandwich, not n times the individual bound. Fixed r yields q^{-r^2}P∞/P_r²; the perfect limiting fraction P∞. Independent finite-field F2 rank distributions for n=1..3 independently match principal exact matrix-count formula, NOT the unrestricted class-count asymptotics. The explicit proof, not small experiments, establishes the result.

## originality

PASS

Wei–Zou enumerates perfect/invertible evolution algebras, and 2LI basis rigidity is classical, but the full singular-corank orbit squeeze, positive nonperfect density and uniform absolute error do not follow merely from perfect classes. A 2026 survey identifies full enumeration as a problem; inaccessible complete survey passage is not asserted to have been read here.

## value

PASS

Asymptotically counts true nonperfect as well as perfect algebra isomorphism types and gives every fixed corank probability. Resolving monomial-vs-unrestricted isomorphism at the orbit-count scale is substantive beyond standard matrix-rank probability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
