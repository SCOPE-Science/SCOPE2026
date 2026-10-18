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

Dias--Koenig Theorems 5.4 and 5.6 give Gaussian-unitary normal form sqrt(f)|0000>+sqrt(1-f)|1111>, f=F_G in [1/2,1]. Majorana bridge on the total-occupation-four cross sector gauges to 2 times four-cube adjacency. Six zero-eigenvalue Walsh characters have overlap 1/2 with the endpoint sum, so kernel norm=3/2, reject norm=1/2. The diagonal two-copy terms are in the kernel and orthogonal to this cross sector, yielding r=f(1-f)/2. Independently constructed the 8-Majorana 256x256 Jordan--Wigner bridge matrix and spectral projector: zero eigenvalue multiplicity 70 and r values 0, .045, .09375, .125 at f=1,.9,.75,.5; all agree to 1e-15. Since x=1-f<=1/2, x(1-x)/2 is monotone and threshold sharp; independent rounds multiply acceptance probabilities. No mixed-state or higher-mode claim.

## originality

PASS

Earlier West--Larocca provides a mode-independent lower bound r>=F_G(1-F_G)/2 and r>=epsilon^2/8 for pure states; an inequality in arbitrary n does not imply equality for n=4. Dias--Koenig provides the four-mode canonical family but does not evaluate this bridge test. The exact attained law and finite-R count synthesize these structures; best-of-knowledge not located as a prior theorem.

## value

PASS

The exact finite-mode false-acceptance curve is a motivated sharp quantification of an operational Gaussianity tester: general bounds prove only a floor. The first nontrivial four-mode case determines optimal constants for the specified test and is useful for finite-sample calibration, not merely a numerical example or a renamed inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
