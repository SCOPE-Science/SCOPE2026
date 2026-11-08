---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Read frozen RESULT.md with explicit tent shear f_eta, H_eta coordinates and Haar initial measure. The area-preserving triangular-shear change of variables makes (Y0,Y1)=(y,v) independent Haar, with X0=v-y-f_eta(y), X2=v-y+f_eta(v). Character expectations factor exactly into J_eta(k-l,k)J_eta(l-k,l), J_eta(m,r)=(1-eta)E(r+m(1-eta))+eta E(r-m eta), E(t)=∫e^{2πitz}dz. This representation handles removable denominator singularities. The tent map pushes Haar onto Haar, hence all C(k,k)=0 for k nonzero and X2-X0 is Haar; C(1,-1)=sin²(2πη)/[π²(3-2η)²(1-2η)²]>0, so observations not independent. C(1,2) negative formula gives d_TV≥|C|/2~eta/6; at eta=0 the cat linear map X2=2X0+3Y0 makes independent pair. Independent 100 direct-original-coordinate Fourier grid quadratures agreed within stated grid tolerances. Analytic factorization, not quadratures, covers all frequencies and parameters.

## originality

PASS

Best-knowledge: distinct precise final statement not implied by inspected prior work; exact comparisons and known subclaims separated. Inaccessibility of some sources alone not a scientific failure; residual risks stated. Prior exact map definitions match, but prior theorem conclusions address mixing/Bernoulli on parameter windows, not all-parameter explicit lag-two Fourier coefficients. The broader dynamics framework and cat-map mixing do not by logical implication yield the exact Fourier factorization for every interior parameter.

## value

PASS

The map exhibits a subtle but exact separation of uniform displacement from genuine two-time independence in a named nonmonotone mixing family, complete with all Fourier coefficients and a quantitative approach to the linear cat limit; the example can serve as a rigorous finite-time correlation benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
