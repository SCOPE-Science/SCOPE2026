---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For every prime p<=2339 the exact recurrence w_j=r w_(j-1), b_j=j b_(j-1)+w_j (mod p), b_0=w_0=1, computes a_r for all r in [1,p-1]; Eratosthenes covers every p. An independently implemented factorial/inverse-factorial modular computation over the same finite domain verified exactly 345 smaller primes, complete histogram (121,140,65,14,4,1), earliest five-root p=593, and the six and only six residues 156,470,520,589,1092,2170 at p=2339. This proves a sharp finite least-prime cutoff, not unboundedness of lambda(p) or higher prime-power claims.

## originality

PASS

Miska explicitly tabulated smaller Schenker root multiplicities and asked Question 4 about arbitrary m; that literature supplies the residue reduction but does not list the exhaustive first six-root cutoff. The new finite census resolves a motivated next threshold rather than asserting an infinite prime theorem. A search not finding another census is qualified evidence only.

## value

PASS

The least prime where multiplicity reaches the first previously unlisted level six is a natural exact threshold in the original root-class question, with an exhaustive and independently implementable certificate. Exact earliest witnesses and their root residue set can be useful in later Schenker arithmetic or experimental conjectures; no unboundedness claim is implied.

The dated certificate retains the supplied scientific assessment, sources and limitations.
