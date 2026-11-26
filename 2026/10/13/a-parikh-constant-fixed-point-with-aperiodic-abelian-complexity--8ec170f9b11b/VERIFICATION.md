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

All images have Parikh vector U=(1,1,1); the substitution is prolongable on 0 and primitive. Writing the letter at 3i+s as s−x_i mod 3 gives, for shifts 3m+t with t=1,2, the difference sets (t−D_m)∪(t−D_(m+1)) via no carry and carry, both realized over starting offsets. For t=0 the set is −D_m. At shift 1 the successive difference is 1 off the boundary and becomes 1 minus a smaller-index successive difference at a boundary; values 0 and 1 occur by index 2. At shift 2 the union with D_0={0} gives {1,2}. The only consecutive positive pairs in the exceptional family of powers and twice-powers of 3 are (1,2),(2,3); both unions of the corresponding D sets are full. Induction yields the asserted complete classification, including alternation at powers. Every factor occurs in some τ^j(0), and τ^j(a+c)=τ^j(a)+(−1)^jc. Since all letters appear in the fixed point, the entire translated factor language is realized. At length 3q, the two off-boundary offsets use opposite signed unit-vector differences for any one nonzero letter difference; cyclic translation gives both three-element orbits, while alignment gives qU. At length 3q+1 the baseline qU+e_j acquires a second three-element orbit exactly when 2∈D_q (q≥1); at 3q+2 the baseline qU+U−e_j acquires the orbit of qU+2e_j exactly when 1∈D_(q+1) (including q=0). These absence tests give the two sparse exceptional families and n=1 is direct. The exact value-3 lengths have unbounded gaps and occur infinitely often, ruling out ultimate periodicity. The formula is for positive lengths (the empty factor, if included, has complexity 1). I inspected verify.py and certificate.json without executing them; independent coordinate generation to length 19683 and window counts at 132 lengths (1–120 and triples around 244,728,2188,6560) agreed, but the infinite claim follows from the proof, not this prefix.

## originality

PASS

The word is known; credit the exact abelian-complexity formula and the counterexample to ultimate periodicity for a Parikh-constant fixed point. The closest inspected primary literature asks this question and does not answer it affirmatively or negatively for this substitution.

## value

PASS

This answers the explicit Parikh-constant periodicity question negatively with a primitive, transparent ternary example. The complete profile supplies exact exceptional lengths and isolates their arithmetic mechanism, rather than relying on a graph or a long finite prefix. It has a clear role as a boundary example for automaticity versus ultimate periodicity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
