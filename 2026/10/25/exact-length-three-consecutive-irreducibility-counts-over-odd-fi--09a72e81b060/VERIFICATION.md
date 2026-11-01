---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Scalar and variable substitutions normalize u0,u1 to one, with exactly (q-1)^2 originals per eligible (a,t); reversing gives Q_a=X^2+X+a and G=X^3+X^2+aX+t. Q irreducibility has (q-1)/2 allowable nonzero a. A cubic is irreducible exactly when rootless. For fixed a, using N0=N2+2N3 and counting the ordered triples with x+y+z=-1, xy+yz+zx=a gives 3N0 points on x^2+xy+y^2+x+y+a=0 away from the triple-root exceptional case. The shifted conic has q-1 (split) or q+1 (nonsplit) solutions for q mod3 1 or 2. At a=1/3 in q mod3=2, every cubic is a translated cube and reducible; in char 3 the conic has q solutions and triple roots cannot occur. Summation yields the displayed three formulas. Independently recomputed every normalized cubic root-image fiber and I3 in 13 finite fields, including q=9,25; all matched. Universal field-size conclusion is proved algebraically, not by these finite tests.

## originality

PASS

Best-of-knowledge PASS. Gómez-Pérez–Ostafe–Sha (2018), Theorem 5.5 in the actual 2018 arXiv PDF, proves exact I2=(q-1)^3/2 and only I3 >= (q-1)^2(q-9)(q-2sqrt(q)-6)/6 for q>13, not exact I3. Their normalization of initial coefficients is prior, but the triple-root conic and split/nonsplit/char3 fiber evaluation supply new exact information. Chou–Cohen (1999) constructs sequences and more general polynomial-distribution estimates, not the checked exact coefficient-restricted I3. Resultary searches returned related finite-field cubic problems but no matching count; this is best-of-knowledge, not proof of priority.

## value

PASS

PASS: closes a concrete exact-count gap explicitly left at the first nontrivial length beyond exact I2 in an active finite-field arithmetic problem. The nonuniform q mod3 and exceptional a=1/3 fiber are structural and motivate the full formula; an exact base case can be useful for bounding longer chains without claiming to solve them.

The dated certificate retains the supplied scientific assessment, sources and limitations.
