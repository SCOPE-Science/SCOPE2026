---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

On the reference triangle with area 1/2, translate the integer nodes by the same integer without phase change. For a repeated pair r,r and singleton s, integrating over the singleton barycentric coordinate v gives the integral of (1−v)exp(−2πi(s−r)v) over [0,1], namely 1/(2πi(s−r)); the minus-imaginary sign is consistent with the convention. For three distinct nodes the two edge exponentials after the inner integration have nonzero integer frequencies and both integrals vanish. Three equal nodes give 1/2. Each physical facet carries the same Jacobian 2A_f, so summing over the omitted node leaves zero for all-distinct nodes and cancels opposite pair contributions for 2+2. For 2+1+1 the sum can vanish only when the two nonzero reciprocal gaps 1/(s−r), 1/(t−r) add to zero, equivalently s+t=2r. Type 3+1 has positive real part from its constant face, and type 4 has Fourier value 4A_f, the total area. This exhausts all integer phases. Independently the stated cube count 396 splits as 336 all-distinct, 24 two-pair, 24 symmetric with repeated zero, and 12 symmetric with zero a singleton (then the other singleton is 2r). This and the rational finite check corroborate the claim; the analytical calculation proves it on all of L*. The supplied check.py was read, not executed.

## originality

PASS

Standard simplex exponential integrals and divided differences already provide the facet-evaluation machinery. The supported distinct claim is the explicit necessary-and-sufficient rule for cancellation of the equal-area tetrahedron's scalar surface sum at reciprocal edge lattice frequencies, including the single repeated-pair midpoint condition. The closest verified lattice-zero classifications use simplex volume in other dimensions. Potential overlap with inaccessible polyhedral form-factor literature remains qualified.

## value

PASS

A uniform regular tetrahedral shell is a natural scattering object, and its exact extinctions at reciprocal edge frequencies are a concrete invariant distinct from the volume form factor. The rule resolves cases where individual facet contributions are nonzero but all cancel; in particular it distinguishes symmetric from nonsymmetric gaps in the same 2+1+1 multiplicity type. The result gives an all-frequency-lattice test without evaluating form factors afresh; it is not a check at a few frequencies or the renormalization of a known volume zero set.

The dated certificate retains the supplied scientific assessment, sources and limitations.
