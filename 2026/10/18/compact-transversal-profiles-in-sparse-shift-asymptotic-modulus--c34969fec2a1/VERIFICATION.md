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

# Mathematical verification and boundaries
The core identity is the exact diagonal coefficient formula
\[
|W^n|^{1/n}e_k=\exp\left(-\frac1n\sum_{i:\,k\le p_i\le k+n-1}\alpha_i(p_i-1)\right)e_k.
\]
Comparing the \(k\)-th and first coordinates removes a fixed initial finite sum and adds only spike positions in the length-\((k-1)\) window immediately after \(n\). This produces precisely the two asymptotic cases in RESULT.md: a scalar limit when the next spike is more than every fixed distance away, or a step limit when it occurs at a fixed positive distance. The lacunarity estimates and the explicit subsequences establish both necessity and realization. Uniform operator boundedness upgrades coordinatewise convergence to strong convergence. The proof does not extrapolate from a finite computation.

Source comparison read the primary 2026 paper's full relevant Introduction/Question 3 and Section 4, including Proposition 4.1, its proof, and Example 4.3 with proof. Its bounded-below classification and disconnectedness witness do not determine the full non-bounded-below cluster set or arbitrary compact transversal realizations. The full spectrum of alternative terminology in older literature cannot be ruled out by database searches alone.

Independent audit and external proof certification were not performed.
