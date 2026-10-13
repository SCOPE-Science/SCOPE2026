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
The finite phase certificate is replayable with `python3 artifacts/verify.py`. The script uses exact integers and `fractions.Fraction`; it checks strict positivity and normalization of all \(64\) weights, all \(28\) target cosine moments, exact affine rank \(16\), and the count of \(16\) distinct restricted cosine characters. The replay result for the packaged file is `VERIFY_OK`.

The analytic steps checked separately are: \(\theta_1=\theta_2+\theta_4\); \(\theta_2=\theta_1^2-2\); irreducibility of \(x^3-3x-1\) by the rational-root test; the resulting three-dimensional Kronecker torus; the path identities converting target coherences into \(J/8\); and the finite-dimensional convex fact \(\operatorname{relint}(C)=\operatorname{relint}(\overline C)\) for nonempty convex \(C\).

The verifier does not numerically approximate readout times. Exact time atoms are asserted existentially from dense phase flow plus relative-interior membership and Carathéodory. The result is limited to \(q=9\).
