---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Shell edge counts give first squared bond 2n and remaining b_r^2=(r+1)(n-r); positive bonds make the shell Jacobi matrix cyclic at the hub by induction on the tridiagonal recurrence. Its even–odd decomposition gives a positive squared block of dimension ceil(n/2). Only the first odd-shell diagonal is changed relative to a single cube, by +n. The normalized single-cube radial eigenvector at least positive frequency ell has corner squared amplitude binom(n,(n-ell)/2)/2^n by the Walsh projection; its shell-1 amplitude is ell/sqrt(n) times the corner amplitude. Its even and odd parts have equal norm by the bipartite eigenvector equations for ell>0. Thus the Rayleigh upper increment for the squared block is 2 ell^2 binom(n,(n-ell)/2)/2^n, and the lower bound is strict because the simple minimum eigenspace has nonzero shell-1 component. For odd n>=3 the two central binomial coefficients are equal and other terms contribute, giving 1<y_min<2. For n=2m the ratio of successive binom(2m,m-1)/4^m is (m+1)(2m+1)/(2m(m+2)), equal to one for m=1 and below one thereafter. At n=4 the Rayleigh bound is strict because its trial vector is not parallel to e_1 (nonzero off-diagonal) and is not an eigenvector after the perturbation. Thus 4<y_min<6 for even n>=4. Phase agreement for both signs of each supported frequency makes the squared frequencies commensurate; their positive integer trace forces rationality, and the monic integer squared polynomial forces integrality. In even n all squared bonds are even, so the determinant recurrence reduces to y^(n/2) mod 2 and excludes 5. At n=1 the two phases need only agree with each other; at n=2 the zero mode fixes their phase to 1, yielding the stated least times. Reviewed, not executed, the source script. Own exact finite corroboration (/tmp/opencode/frozen-review-replay.py, section 5) gives squared-block polynomials y-2, y-6, y^2-13y+18, y^2-24y+104 for n=1–4 and parity evaluations for even n through 30. The analytic argument is not inferred from those values.

## originality

PASS

The distinct supported finding is the exact shared-vertex periodicity cutoff, not the glued graph, its tridiagonal reduction, or the general ratio condition. The same graph is established prior art. No examined stronger result supplies the dimension-uniform spectral obstruction for the hub.

## value

PASS

The hub is the distinguished junction in a studied quantum-walk model. Exact recurrence there is a natural contrast with perfect recurrence of the single cube and with high but imperfect peaks from remote corners. The all-dimension obstruction and genuinely attained low-dimensional exceptions resolve that distinction sharply; they do not claim bounds on approximate recurrence, remote-corner periodicity, or a Laplacian result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
