---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

From the exact odd-index telescoping sum u(2m+1)=1+2 sum_{k=1}^m u(k), parity of oddpart mod4 yields a finite A(m) recurrence. Binary induction establishes u(2^v(2m+1))=1+2 eps0+4Q(m) mod8 for all m,v. Two-state transfer T=[[1,1],[-1,1]] satisfies T^T T=2I and T^4=-4I, deriving both rational generating functions and exact dyadic counts. Aligned dyadic blocks yield O(sqrt N), and N=2^(4a+1) yields matching lower-size fluctuations separately for each residue. Independent exact recurrence/mod8 test checked 65,535 terms and all 16 dyadic prefix censuses to 2^16; infinite claim is analytic.

## originality

PASS

Modulo-four semi-Pell behavior and Rudin–Shapiro square-root mechanisms are acknowledged old; what survives is an explicit next 2-adic digit law, exact four-class dyadic census, all-N distribution with individually sharp error. A highly relevant primary 2023 theorem was checked and covers only the previous mod-four layer. Best-of-knowledge priority remains qualified by older automatic-sequence literature.

## value

PASS

The next congruence layer of a natural self-similar counting sequence and the exact frequency/optimal discrepancy of each odd residue are motivated intrinsic arithmetic properties. The classification joins a novel digital form to sharp global distribution, not merely a short mod-eight table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
