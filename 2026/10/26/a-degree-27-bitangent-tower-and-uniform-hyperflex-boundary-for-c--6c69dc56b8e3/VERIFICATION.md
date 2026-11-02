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

Fx=-z^3 eliminates affine singularities, and Fz at the unique infinity point is nonzero. Any line y=t z meets infinity with multiplicity one; only x=a y+b z can be another bitangent. Squaring Q=y^2+u yz+v z^2 in F3 and comparing all coefficients yields A(a)=a^9-d a^3+a+e+dc-c^3 and B(a,b)=b^3-b-f+[(a^3-c)^2-d]^2. Independent sparse-polynomial F3 verification reproduced the unconditional identity, while A_a=1, B_b=-1 give etale covers of degrees 9 and 3. Q=(y-u z)^2-dz^2 supplies contact roots r^2=d; unique tangent line at a smooth point prevents double-counting between bitangents. For d!=0 54 finite points plus infinity; for d=0 each of 28 lines is hyperflex. No assertion on Frobenius orbit counts.

## originality

PASS

The classical 28-bitangent theorem for odd-characteristic smooth quartics and special all-hyperflex examples are prior. Duque-Rosero et al. cover Artin–Schreier genus-three stratification and normal forms, not the located relative degree-27 etale tower and contact cover. Oyono–Ritzenthaler studies quartic intersection-point rationality and bitangent context without the evaluated all-parameter contact divisor in inspected material. A specialized classical theta-characteristic formula could be equivalent; risk retained.

## value

PASS

The universal finite-etale bitangent parameterization and a simple exact coefficient-space hyperflex wall give a family-wide geometric incidence invariant, including distinct contact-count jump, beyond repeating the classical total 28.

The dated certificate retains the supplied scientific assessment, sources and limitations.
