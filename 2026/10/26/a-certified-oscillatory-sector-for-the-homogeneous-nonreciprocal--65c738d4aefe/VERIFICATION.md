---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Reconstructed all-domain, all-initial-condition ODE proof from the exact 9319-byte RESULT.md: (-1-x)<=dx/dt<=(1-x) and analogous y bound yield boundedness and inward physical square; linearization eigenvalues J-1 +/- iK make the unique origin a hyperbolic repeller. At any nonzero equilibrium set F_J(u)=atanh(u)/u-J, derive F_J(x)F_J(y)=-K^2; one negative factor has modulus <J-1 and forces both coordinate magnitudes below the unique m_J root, a contradiction even at K=J-1. The outward transverse circle excludes the origin from all other omega limits; Poincare-Bendixson then proves the entire omega-limit is a periodic orbit. For K>J the exact polar-angle derivative and |a tanh(b)-b tanh(a)|<a tanh(a)+b tanh(b) imply strict clockwise speed; tanh(s)/s monotonicity and Cauchy-Schwarz give the strict T bounds. Independently checked 5 pairs (J,K), including equality and strong K>J, with 36 test points/inequalities per pair; these finite values do not prove global behavior. Limitation: no uniqueness of cycles, no sharp coupling boundary, no finite noisy lattice claim.

## originality

PASS

Best-of-knowledge PASS after comparing actual global dynamical quantifiers and explicit sector/period inequalities to the foundational nonreciprocal Ising primary article and a broader inhibitory-network theorem. Existing studies obtain the model, simulations, phase boundaries and sufficient fixed-point stability, but the inspected statements do not imply the asserted universal repeller/periodic omega-limit sector. A previously unrecognized two-neuron planar theorem may imply the special case; priority remains qualified.

## value

PASS

A concrete nonperturbative open parameter wedge J>1,K>=J-1 with an explicit inclusive boundary is a substantive dynamical statement: it rules out every nonzero static omega-attractor for every initial state, not just local Hopf existence. Strong-coupling rotation monotonicity and quantitative period bounds are independently useful for the two-species nonreciprocal model. This is not a trivial renaming of local linear stability, and it does not promise noise-robustness or uniqueness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
