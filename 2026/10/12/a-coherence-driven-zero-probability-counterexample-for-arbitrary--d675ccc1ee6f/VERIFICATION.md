---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

PASS: The displayed real 4×4 matrix was checked symbolically to be orthogonal. The two input Fock components are normalized and mutually orthogonal. For each output with exactly one q=1 photon at i∈{1,2,3}, independent symbolic expansion gives amplitude (1+e^{iφ})/12; three orthogonal internal-resolved outcomes yield (1+cosφ)/24. The incoherent mixture gives 1/24 and φ=π gives zero. Relevant two-photon amplitudes √2/4 and 1/(2√3), and fully indistinguishable three-photon amplitude √6/8, are nonzero. This verifies suppression produced by coherence in the arbitrary internally correlated state, not independent-product sources.

## originality

PASS

The exact three-photon internally entangled zero supplies a counterexample to the unrestricted arbitrary-fixed-occupation zero-probability conjecture in Shchesnovich 2015. It does not refute independent-product versions, and the original 2023 same-author source explicitly restricts its illustrative calculation to independent single-photon sources.

## value

PASS

PASS: A small exact counterexample isolates a missing hypothesis in a published arbitrary-input mathematical conjecture. Its phase-only change switches an exact 3-photon output from 1/12 to zero while every fully indistinguishable subset transition remains nonzero. It clarifies a rigorous boundary between correlated and independent preparations; no broad theorem about arbitrary products is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
