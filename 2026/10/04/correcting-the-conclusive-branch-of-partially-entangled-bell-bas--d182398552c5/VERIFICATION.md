---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Invert the four partially entangled measurement-basis vectors explicitly: the four Bob unnormalized maps are unitarily equivalent to diag(x,y)/√2 or diag(y,x)/√2, with 1/√2≤x≤1, y=√(1−x²). For y>0, any branchwise success Kraus K reversing an unknown qubit to cU requires KD=cU and K†K≤I, hence |c|²≤y²/2 by the inverse operator norm. The filters Ks=diag(y/x,1) and Kf=diag(√(1−y²/x²),0) attain the bound and satisfy exact completeness. Four exclusive branches give 2y², including x=1/√2 probability 1 and x=1 probability 0 (in the latter case the inverse formula replaced by limiting/impossibility rank argument). Eq (9) printed second filter diag(1−y/x,0) does not satisfy Kraus completeness unless endpoint; correcting its matrix and decomposition is necessary. This is an analytic operator inequality, not an inference from numerical replay.

## originality

PASS

General Mor–Horodecki and later Roa/Lee–Im–Kim–Nha–Kim theory covers optimal conclusive teleportation and least-singular-value branch reversal; the package explicitly does not claim that general optimization law as novel. Its specific new claim is identifying the inconsistent Eq. (8) and non-complete Eq. (9) of Trump–Bruß–Lewenstein arXiv v1 and giving the valid replacement instrument. No sourced v1 erratum was located in tested DOI/title/equation searches.

## value

PASS

An explicit valid quantum instrument and input-independent optimal heralded success probability are necessary to implement or evaluate this classical conclusive teleportation example. The product-basis endpoint exposes the old printed prediction as unphysical, and the corrected filter is operationally meaningful independent of a new general teleportation theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
