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

The proof is symbolic and applies to every finite commutative local ring. The computational check in `verify.py` is deliberately finite and independent of the orbit-count formula: it tests group invertibility from the three defining equations by exhaustive search for the inverse candidate.

For each of \(\mathbb Z/4\mathbb Z\) and \(\mathbb F_2[\varepsilon]/(\varepsilon^2)\), the checker enumerates all \(256\) matrices in \(M_2\), searches all \(256\) candidate group inverses for each matrix, and obtains residue-rank counts \((1,48,96)\), total \(145\). It also checks every residue fiber over \(M_2(\mathbb F_2)\): a group-invertible residue matrix of nullity \(k\) has exactly \(2^{4-k^2}\) group-invertible lifts, while a non-group-invertible residue matrix has none.

The finite computation does not establish the general theorem. The all-ring conclusion depends on the image/kernel decomposition, freeness of finite projective modules over a local ring, orbit-stabilizer counting, and the exact kernel size of reduction \(\operatorname{GL}_s(R)\to\operatorname{GL}_s(\mathbb F_q)\).
