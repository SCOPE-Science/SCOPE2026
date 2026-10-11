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

Using the source model's density-band characterization, admissible observed densities satisfy \(a_n\phi\le m\le\phi\). For target density \(m_2=b\phi(\cdot-r)\), total variation on the observed space plus missing atom equals the maximum of the positive and negative observed-density discrepancy masses. The monotone Gaussian likelihood ratio crosses the lower and upper admissible ratios once, forcing exactly the two tail discrepancies \(B_{n,b}(r)\) and \(A_b(r)\); pointwise clipping attains both bounds simultaneously. For the critical asymptotic, independent symbolic substitution of \(r=L/\sqrt{2S}\) into the derived upper-tail asymptotic confirms the prefactor \(C_b=\sqrt b L/(4\sqrt\pi)\), and the stated \(-3/2\log\log n\) normalization gives \(nA_b\to e^{-x}\). The lower crossing is much farther into the Gaussian tail, making \(nB_{n,b}\to0\).

## originality

PASS

The motivating 2026 paper is the exact missing-data confidence-interval problem and its accessible primary statement advertises minimax rates and finite-sample adaptive intervals, not the audited exact one-sample TV projection or the log-log critical window. Earlier realisable-missingness and Huber-contamination papers provide related estimation/testing frameworks but no located statement with the exact clipping modulus or \(-3/2\log\log n\) normalization. Resultary searches found no equivalent finding. Complete text of the 2026 paper could not be obtained: the open route did not expose the needed full material and the permitted Oxford retrieval attempt was safety-blocked, so priority remains best-of-knowledge with an explicit residual risk.

## value

PASS

The total-variation projection is the natural testing modulus driving the adaptive confidence lower bound. Its exact clipping form, nontrivial \(-3/2\log\log n\) critical window and improved fixed-MCAR leading lower coefficient materially sharpen a logarithmically slow information boundary while making appropriately limited claims about product TV and minimax sharpness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
