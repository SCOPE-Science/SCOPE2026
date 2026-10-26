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

The boundary root condition \(z^{n-k}=\varepsilon\) follows from pairing two unit complex numbers with nonzero real sum. This gives all positive crossing levels, including endpoint \(s=2\).

At any crossing the Jacobian equals the exact positive integer \(n^2-k^2\). Reconstruct the first derivative from \(nu w+kv\bar w=-\delta\), then substitute \(w=-\delta v/(n+k)\), \(uv=1\) into its derivative to obtain \(w'=[nk-(n^2+nk+k^2)v^2]/(n+k)^3\). The exact identity \(\operatorname{Re}v^2=s^2/2-1\) yields the radial second derivative.

An exact example check: at \(n=9\), \(k=1\), \(s=\sqrt2\), the second radial logarithmic derivative is \(9/1000\); at \(s=2\) it equals \(-41/500\). The thresholds are \(\sqrt2\) and \(2\), with winding steps of sizes two and one, respectively. The full proof establishes every exponent without exhaustive computation.

Limits: The winding is signed, not the unsigned zero count. The real-analytic branch exists locally only. No independent mathematical audit has been undertaken.
