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

The proof was checked symbolically from the explicit free model. The critical count is
\[
|\operatorname{Fix}_{D_{r,k}}(\sigma^d)|=2^{k-1}F_d(\sigma)^k,
\]
because the \(k-1\) letters from \(\{a,b\}\) are untouched by generator permutations and each of the \(k\) generator letters must lie in \(\operatorname{Fix}_X(\sigma^d)\).

For every source-generator \(d\)-cycle, equivariance determines all images from one representative; consistency after one circuit imposes exactly the displayed fixed-point condition. Burnside averaging and cycle-type grouping then give the theorem.

`verify.py` separately represents a length-\(k\) element as a pair consisting of an \(X\)-word and a binary word, enumerates all homogeneous generator maps, computes their relabeling orbits directly, and compares those orbit counts with the partition formula. The run recorded in `verification.log` checks
\[
(r,k)\in\{(1,1),(1,2),(2,1),(2,2),(3,1),(3,2)\}
\]
and terminates with `VERIFY_OK`.

The computation is finite and is not used to infer the theorem for arbitrary rank or length. The asymptotic follows separately from the symbolic bound that every nonidentity permutation has at most \(r-1\) cycles.
