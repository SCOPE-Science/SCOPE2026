---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For nonnegative geometric samples, P(M_m=k)=(1-q^(k+1))^m-(1-q^k)^m and p0=(1-q)^m>0. For m=1, log PGF positive jump masses q^k/k. For m=2, exact PGF (1-q)^2(1+qz)/((1-qz)(1-q²z)) gives positive summable log coefficients [q^(2k)+(1+(-1)^(k+1))q^k]/k. For m>=3, log z² coefficient is v^m-(u^(2m)+1)/2; u=1+q, v=1+q+q², identity u^6+1-2v³=q²(3+6q+3q²-q⁴)>0, Jensen exponent m/3>=1, yield strict negativity for 0<q<1. Compound-Poisson ID criterion then proves exact iff. Independently checked polynomial and rational parameter grid; finite checks only corroborate unrestricted inequality.

## originality

PASS

Best-of-knowledge original ADDITIVE infinite-divisibility iff m<=2 cutoff for the discrete generalized exponential distribution DGEII at integer shape parameter m. Important alias correction: the maximum of m iid zero-based geometric inputs is exactly the long-established DGEII(α=m,p=q) / exponentiated-geometric family; its PMF, sample-maximum closure and general PGF are PRIOR mathematics in Nekoukhou–Kundu (2017) and earlier authors. The new comparison is exclusively the positivity of the logarithmic PGF coefficients for m=1,2 versus the all-q negative z² coefficient for m>=3. The highly relevant 2013 DGEII and 2015 EGD papers could not be retrieved in full through available OA/institutional routes; priority risk is material but, absent decisive known implication, does not automatically defeat the original cutoff.

## value

PASS

Ordinary additive infinite divisibility is a fundamental classification question for a natural non-Poisson count family (already known as DGEII), and the transition exactly at integer shape two with explicit Levy intensities is a self-contained structural result. The probability law itself and its generic PGF are not new; the additive ID cutoff is the motivated contribution. Prior-paper access risks are recorded.

The dated certificate retains the supplied scientific assessment, sources and limitations.
