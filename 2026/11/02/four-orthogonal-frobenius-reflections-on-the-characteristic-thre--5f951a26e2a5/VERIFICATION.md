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

The quartic is Hermitian over F9 with 28 rational hyperflexes and tangent inverse images splitting into 56 (-1)-curves by the explicit quartic identity; geometric completeness uses the standard 56-curve theorem for smooth degree-two del Pezzo surfaces. The inspected verify.py constructs exact GF9 curve parameters, all 56x56 intersection entries, seven disjoint exceptional curves, an integral blow-up basis and Frobenius permutation. Independently reconstructed four listed root vectors in J=diag(1,-1^7), checked pairwise perpendicularity, square -2 and -K orthogonality, formed M as reflection product, confirmed M^2=I, characteristic polynomial and Smith invariant with SymPy, plus directly enumerated all 13 F3 projective points to obtain 10 surface points and separately all 91 F9 projective points, 28 Hermitian branch points and 154 surface points. The 154 F9 points follow from 28 branch points and square values; zeta and cohomology follow from the established integral lattice action. Independent finite checks of roots do not independently certify every GF9 curve incidence, which remains separately sourced by inspected exact script and proof.

## originality

PASS

Closest statement/implication comparisons and bounded primary reading support best-of-knowledge originality with explicitly named residual priority risks; no claim of exhaustive historical uniqueness.

## value

PASS

Identifying the named F3 model’s integral Galois/Picard module, primitive (-1) lattice and H1 is a natural arithmetic-geometric invariant not determined by previously known F9 point counts. Four-root decomposition is a substantive explicit descent certificate with a computable zeta function. Scope carefully excludes novelty of geometric bitangents and F9 counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
