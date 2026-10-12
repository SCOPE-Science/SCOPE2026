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

The proof is analytic. The accompanying `verify.py` checks the exact rational consequences
\[
p_{\mathrm{MAP}}=\frac34,\qquad
\mathbb E_{\mathrm{Haar}}\!\left[\lvert\langle\tau\rvert P\lvert\tau\rangle\rvert^2\right]=\frac13,\qquad
\bar F_{\max}=\frac56.
\]

The key structural check is not delegated to code: for every polarization-preserving beamsplitter in the stated model, \(\lvert\phi^+\rangle\) and \(\lvert\phi^-\rangle\) have identical photon-count likelihoods because their only difference is a phase between orthogonal all-horizontal and all-vertical sectors. Therefore their combined prior mass contributes at most \(1/4\) to any maximum-posterior label decision, while the two remaining Bell labels contribute at most \(1/2\), proving \(p_{\mathrm{MAP}}\le3/4\).

At 50:50 the standard analyzer distinguishes the two \(\psi\)-states and leaves only the \(\phi\)-pair unresolved, so the bound is attained. A wrong Bell label leaves a nonidentity Pauli on the teleported qubit; Haar rotational symmetry gives average fidelity \(1/3\) for every such wrong correction.

The checker also records \(7/8\) for a uniform polar-angle diagnostic. That value is not part of the claim and is not evidence for the source's numerical implementation.

Unproved limits: no claim is made for analyzers with additional nonvacuum ancillas, active or nonlinear optical elements, or for non-Haar input ensembles.
