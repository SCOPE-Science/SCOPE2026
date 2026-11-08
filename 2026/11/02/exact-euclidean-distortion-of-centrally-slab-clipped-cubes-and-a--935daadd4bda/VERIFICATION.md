---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Every real ellipsoid sandwich can be averaged over coordinate permutations because the clipped norm is invariant and the quadratic inequalities are linear, reducing the global infimum to Q_beta=||x||_2^2+beta(sum x_i)^2. The dual norm calculation gives U=max{(1+(n−1)beta)/(1+n beta), nt^2/(1+n beta)}, crossing at beta0=(nt^2−1)/(n−1). Full vertex enumeration of the convex clipped cube gives V=v0+beta/t^2 for beta>=beta0, including even-dimension balanced cube vertices; for beta<=beta0 Cauchy–Schwarz makes the product nonincreasing and for beta>=beta0 its derivative strictly positive. Thus beta0 is the unique permutation-invariant optimum and direct algebra gives the parity-dependent rational formulas, t=1 endpoints and asymptotic limits. Independent exact-rational enumeration checked 15 (n,t) cases and both sides of beta0, plus symbolic derivative factorizations. Finite tests supplement the all-n,t argument.

## originality

PASS

Qualified original all-dimensional exact Banach–Mazur formula for a central TWO-SIDED signed-sum clipped cube. Full Deza–Hiriart-Urruty–Pournin primary PDF describes polytopal balls interpolating cube/crosspolytope and computes their face structures and volumes, not this signed-diagonal slab nor its optimal ellipsoid sandwich. Other exact small-dimensional, unconditional and one-sided cap families differ either in norm/geometry or the optimization objective. A general ellipsoid-averaging technique is an ingredient but not the evaluated parity-reversal theorem.

## value

PASS

The body is the cube under a single canonical diagonal measurement constraint, so its Euclidean distortion is a natural Banach–Mazur invariant rather than an arbitrary norm. A full n,t evaluation and the surprising even/odd reversal identify exact geometric behavior inaccessible from standard cube/crosspolytope endpoints, with a constructive invariant optimal form.

The dated certificate retains the supplied scientific assessment, sources and limitations.
