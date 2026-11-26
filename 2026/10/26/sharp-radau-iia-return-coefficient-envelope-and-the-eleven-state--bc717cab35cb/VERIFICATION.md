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

The stability factor obtained from the two-stage Radau IIA tableau at z=−x is (6−2x)/(x²+4x+6). With x*=3+3√3 and m=(5−3√3)/2, subtracting m gives exactly −m(x−x*)²/(x²+4x+6); its unique minimum is at x*. In the reversible row convention, the diagonal coefficient is the spectral average for the unit vector eᵢ/√πᵢ in ℓ²(π). The zero-mode mass is πᵢ and the remaining positive masses sum to 1−πᵢ, proving the bound. Equality at h>0 is equivalent to eᵢ−πᵢ1 having eigenvalue −x*/h. Its off-i coordinates prescribe qⱼᵢ=(x*/h)πᵢ, which detailed balance converts to the claimed outgoing rates; the diagonal coordinate then follows by the row sums. The reset generator realizes this for all states and the bound is strict at h=0 for n≥2. Solving the sign of the affine envelope gives the claimed stationary-mass threshold, including sharp zero at the boundary. For all unweighted connected graphs the stationary mass is 1/n, giving strict diagonal positivity through eleven. At a universal vertex the centered indicator is a Laplacian eigenvector of eigenvalue n, including with arbitrary edges between other vertices. Substitution at h=3/4 gives (56−5n)/(3n²+16n+32), which is negative for n≥12 and equals −1/164 at 12. The positive roots of the general hub numerator give the asserted open interval of negativity. No conclusion is implied for full entrywise or internal-stage positivity.

## originality

PASS

There is verified material overlap in the scalar minimum, the two-state mass boundary, multipartite order cutoff and star witness. The supported distinct claim is the optimal statewise envelope over all finite reversible generators with an arbitrary prescribed stationary law, its local outgoing-rate characterization, and the resulting universal graph statement. The strongest matched original statements use a single nonzero mode in two states or a family-specific multipartite spectral decomposition. Neither covers the full quantifier scope and equality condition.

## value

PASS

Universal return positivity is a distinct, motivated numerical question even when a method is contractive or loses positivity elsewhere. The result isolates exactly which stationary masses guarantee it under arbitrary reversible rates, and gives a test for saturation involving only rates incident to the state. For unweighted graphs it converts family-specific phenomena into a sharp topology-independent size guarantee and a robust obstruction from one universal vertex. This is not an assertion about the full transition matrix.

The dated certificate retains the supplied scientific assessment, sources and limitations.
