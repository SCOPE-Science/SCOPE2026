---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The proof is infinite and does not depend on computation.

For even \(k\), \(y^k\equiv1\pmod8\), while \(n2^{an}-1\equiv7\pmod8\) when \(an\ge3\). The three low-\(an\) values are \(1,3,7\).

For odd \(k\ge3\),
\[
T=(y^k+1)/(y+1)
\]
is odd and divides \(n\), hence \(T\le n\). Since \(T>3y^{k-1}/4\), one obtains \(y^k<(4n/3)^{3/2}\). For \(n\ge3\), \(n2^{an}-1>(4n/3)^{3/2}\); for \(n=1,2\), \(T\mid n\) and \(T>1\) is already impossible.

The packaged checker independently tests a finite grid and the boundary inequalities. Its output is corroborative only.
