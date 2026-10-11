---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The symmetric geometric variance \(\sigma_q^2=2q/(1-q)^2\) is correct. On each lattice band, the closed central mass equals \(1-2q^{m+1}/(1+q)\) and decreases with \(q\). Solving the threshold \(c\sqrt{2q}/(1-q)=s\) gives \(q_s=\exp(-2\operatorname{arsinh}(c/(\sqrt2\,s)))\). The complementary band extrema \(T_s\) have strictly negative logarithmic derivative because \(t>\tanh t\), so the first band is globally extremal. At \(s=1\), the mass is \(c/\sqrt{c^2+2}\); the closed event has an unattained infimum while the open event attains its unique minimum at \(q_1=1+c^2-c\sqrt{c^2+2}\). The endpoint jump and uniqueness are handled correctly.

## originality

PASS

Zhang, Hu and Sun inspect the same symmetric-geometric family and prove the one-standard-deviation value \(1/\sqrt3\), which is exactly the \(c=1\) specialization. Their complete primary text does not state the all-\(c>0\) standardized profile, the unique open-event optimizer, or the first-band monotonicity theorem. Bobkov, Marsiglietti and Melbourne give broader discrete log-concave concentration inequalities, but those optimize fixed integer windows rather than a centered window whose radius scales with each law's own standard deviation. No Resultary search returned a stronger all-radius statement.

## value

PASS

The result upgrades a published sharp one-standard-deviation fact to the complete standardized concentration profile for the same canonical extremal family, including attainment and unique optimizer. The first-threshold principle is a clean structural statement that can serve as a benchmark for broader discrete concentration problems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
