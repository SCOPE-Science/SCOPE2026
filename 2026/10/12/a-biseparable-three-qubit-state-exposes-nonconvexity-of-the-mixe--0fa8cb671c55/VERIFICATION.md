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

The exact witness is
\[
\rho_\star=\frac13\left(
|\psi_{AB}\rangle\langle\psi_{AB}|+
|\psi_{AC}\rangle\langle\psi_{AC}|+
|\psi_{BC}\rangle\langle\psi_{BC}|
\right),
\]
with the three pure states given in `RESULT.md`. Direct expansion yields a normalized positive semidefinite density matrix because it is an explicit convex combination of rank-one projectors.

For the \(A|BC\) cut, the partial transpose contains the invariant block
\[
\frac16\begin{pmatrix}0&0&1\\0&0&1\\1&1&0\end{pmatrix}
\]
on \(\operatorname{span}\{|001\rangle,|010\rangle,|100\rangle\}\). The vector proportional to \((1,1,-\sqrt2)\) is an exact eigenvector with eigenvalue \(-\sqrt2/6\). Permutation symmetry gives the identical NPT witness on the other two cuts.

The standard-library script `verify_r2_nonconvex.py` checks the exact rational matrix entries, normalization, permutation symmetry, the three product factorizations, all three partial transposes, and the negative-eigenvector identity in the quadratic field \(\mathbb Q(\sqrt2)\). It prints `VERIFY_OK` when all checks pass.

The computation does not evaluate the convex roofs. Their strict positivity follows analytically: the fixed-cut pure seed is continuous, nonnegative, and zero exactly on cut-product pure states; finite-dimensional convex-roof minima are attained, so the mixed convex roof is zero exactly on the corresponding cut-separable set. NPT excludes that set for every cut of \(\rho_\star\).

No claim is made about the exact positive value of \(R_2(\rho_\star)\), average LOCC failure, or multipartite systems beyond the displayed three-qubit witness.
