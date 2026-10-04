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

Let
\[
P=\{x:|x_i\pm x_j|\le1\text{ for all }i<j\}.
\]
The embedded exact-rational checker enumerates every intersection of four defining root hyperplanes and proves that the feasible vertex set is exactly
\[
\{\pm e_i\}\cup\{(\pm1/2,\pm1/2,\pm1/2,\pm1/2)\}.
\]
Hence the finite polyhedral identity used in the proof is independently reconstructed.

It then takes these \(24\) points as the normals of the halfspace system
\[
m\cdot x\le1/2
\]
and again enumerates every fourfold active intersection. The resulting vertices are exactly
\[
\frac12\{\pm e_i\pm e_j:i<j\}.
\]
This verifies the polar halfspace description of \(V_{D_4^*}\) exactly.

For additional consistency, the checker evaluates the support inequalities for all tested \(D_4\) points with integer coordinates in \([-4,4]\) and all tested \(D_4^*\) points with half-integer coordinates in \([-7/2,7/2]\). It also confirms that each root direction uniquely selects its corresponding root vertex in \(C\).

The replay output is:

`VERIFY_OK D4 24-cell reduced-complete identity`

The finite lattice sweeps are not used to prove the infinite statements. The all-lattice Voronoi inequalities are proved symbolically in `RESULT.md` by elementary estimates on integral and half-integral coordinates.
