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

For Cauchy(mu,sigma), sigma>0, f(x)=sigma/[pi((x-mu)^2+sigma^2)] asymptotically sigma/(pi x^2); hence |x|^r f(x) is comparable to |x|^(r-2) and E|X|^r diverges for every integer r>=1. Odd power positive and negative parts both diverge. The claimed density inverse has an unacknowledged sign: (pi sigma f(x))^{-1}-1=(x-mu)^2/sigma^2, so the displayed plus-root gives mu+|x-mu|, not x on x<mu. On the principal upper boundary complex power, the integrability strip is exactly -1<Re z<1; the upper-half-plane residue at mu+i sigma yields E[X^z]=(mu+i sigma)^z on that strip, with both endpoints divergent. The analytic continuation outside it is not an ordinary expectation. Direct tail, inversion and residue checks independently reconstruct the package proof.

## originality

PASS

Best-of-knowledge original as a documented source-specific correction of the September 2026 LOTUS Theorem 3.1 and its erroneous inversion step; NOT original for the known nonexistence of Cauchy integer moments or the Okamura–Otobe fractional complex identity. The identical misleading positive-integer formula is in the primary article; identifying precisely the mathematical error and separating maximal valid integrability from analytic continuation is the narrow surviving new claim. No prior published correction to this exact 2026 theorem was identified.

## value

PASS

Correcting a newly published false positive-integer expectation theorem prevents misuse of nonexistent Cauchy moments, its dependent central-moment statements and higher statistical interpretations; precise failure of a noninjective density inverse and sharp legitimate replacement domain is substantive despite elementary tail algebra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
