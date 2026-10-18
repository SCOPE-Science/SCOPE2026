---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Source Lemma4.1 modal matrix [[-f*l²-beta*q²,gamma*q],[beta*q²,-g*l²-gamma*q]] with q=1-1/R0>0 gives characteristic lambda²+A_l lambda+B_l with A_l>0 and B_l=f*g*l^4+(f*gamma*q+g*beta*q²)*l². Therefore B_0=0, eigs at l=0 are 0 and -gamma(R0-1), neutral eigenvector (1,R0-1). Differentiating exact nonlinear constant endemic family E_M=(M/(R0|Omega|),q*M/|Omega|) yields same tangent vector. Nearby E_M with M!=N stay distinct forever and cannot converge to E_N, refuting ambient asymptotic stability. On fixed-mass leaf the neutral direction excluded and for l>0 both A_l,B_l positive (connected domain). Independent exact rational eigenvalue and mass-identity checks confirmed key algebra; no claim of full nonlinear global/orbital stability.

## originality

PASS

The primary 2026 Liu–Wang–Zhang text explicitly states mass conservation and E_N while its Lemma4.1 proof asserts both modal characteristic coefficients strictly positive for all Neumann l>=0. Taking l=0 in its printed formula directly contradicts that assertion. Allen et al 2008 and Li–Peng–Xiang 2020 address fixed-mass SIS context and do not constitute a source-specific published correction to this lemma. A full fixed-mass stability interpretation may already be valid in the original invariant state space; the contribution is the exact missing zero mode and ambient-domain clarification, not a claim that all threshold dynamics fail.

## value

PASS

The neutral mass-changing mode is a structural conservation-law feature of epidemic diffusion. Correcting a central published stability lemma and distinguishing ambient from fixed-mass asymptotic stability prevents a real spectrum/phase-space error. This is mathematically motivated beyond a routine sign check because it supplies the exact equilibrium manifold and eigenvectors and the appropriate mass-leaf restriction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
