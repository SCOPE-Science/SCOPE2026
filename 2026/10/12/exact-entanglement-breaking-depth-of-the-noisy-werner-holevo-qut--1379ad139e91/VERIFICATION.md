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

For Phi_x=(1-x)id+(x/2)(Tr(.)I-T), 0<=x<=1, scalar/symmetric-traceless/skew-transpose eigenvalues are 1,s=1-3x/2,a=1-x/2. The normalized Choi partial transpose has ranks 3,1,5 eigenvalues (2-5s^k-3a^k)/18, (1+5s^k-3a^k)/9, (2+s^k+3a^k)/18. The third stays positive. Orthogonally invariant Choi states are determined by f=Tr(rho F),g=Tr(rho P), with PPT rectangle 0<=f<=1,0<=g<=1/3; all four corners are orthogonal twirls of explicit product states, so PPT iff separable within this family. Thus exact two EB inequalities hold for every k. Rational x=1/2 checks k1..4 give first EB at k=4, k=2 interval is [(4+sqrt2)/7,1], x=0 never, x>0 eventually. Monotone small-x exponential limit gives x*nEB -> -2 log y, 5y^3+3y=2. Independently reconstructed 30 direct 9x9 Choi matrices/eigenvalues and exact rational critical cases; this finite test is supplementary.

## originality

PASS

Earlier noisy Werner–Holevo papers characterize one-step channels/capacities and Lami–Giovannetti determine depth two for the unmixed Werner endpoint. Zhu–Wang 2026 show x=1/2 has zero quantum/private capacities but is not PPT after one use. None of the material read supplies the full-family necessary-sufficient two-inequality EB phase diagram, first-four iteration threshold or small-noise constant; these calculations are additional. Residual priority risk remains for implicit computations in orthogonally invariant channel literature.

## value

PASS

EB depth of a physically motivated noisy qutrit channel determines when repeated unfiltered noise irrevocably destroys reference entanglement. The exact phase boundary, surprising depth four at zero-capacity x=1/2, and weak-noise 1/x law give concrete distinctions between capacity, PPT status and entanglement-breaking iteration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
