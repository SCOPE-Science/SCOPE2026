---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For every n>=3 with prime P=2^(n-1)+3, s_j=(2+√3)^(2^j)+(2-√3)^(2^j). Put E=2^(n-2)=(P-3)/2, take u²=3,v²=2 in F_(P²), y=(1+u)/v so y²=2+u. For odd n>=5, Legendre(2/P)=Legendre(3/P)=-1 and y^P=y^-1; hence α^E=α^-2 giving s_(n-2)=14 mod P. For even n>=4, (2/P)=-1,(3/P)=1 and y^P=-y; thus α^E=-α^-1 giving s_(n-2)=-4. Handle n=3,P=7 directly. Dividing by 2 proves residues 7 and -2. Independent 14 prime-modulus exact recurrence checks support, not establish, the all-n theorem. The result has NO converse and is not a primality test.

## originality

PASS

The specific prime-case parity congruence was posed openly as Conjecture 112 on 2026-07-23; its truth is proved here by a classical finite-field trace argument. The technique is not new, and an earlier implicit generalized Lucas theorem could supersede priority; not identified in inspected sources.

## value

PASS

Proving a publicly stated exact prime-case congruence resolves the necessary direction of a named arithmetic conjecture, replacing an experimental pattern with an all-n theorem; it does not establish a new practical primality test or composite obstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
