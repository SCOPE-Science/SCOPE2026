---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The affine group \(\operatorname{AGL}(2,3)\) has exactly two orbits on the 126 five-subsets, of sizes 54 and 72. For each representative, Fourier zeros correspond to rows of the 9-by-5 evaluation matrix annihilating the coefficient vector. A feasible exact zero set is the row-span closure of a rank-deficient row set whose kernel is not trapped in any coordinate hyperplane; rows outside the closure impose additional proper hyperplanes, so a vector avoiding their finite union has exactly that zero set. I independently replayed the exact \(\mathbb Q(\omega)\) rank/closure enumeration over all 512 row subsets for each representative and obtained zero-set sizes exactly \(\{0,1,2,3,4\}\); an independent affine-orbit enumeration again gave sizes 54 and 72. Thus the Fourier supports are exactly 9 down to 5.

## originality

PASS

Bonami--Ghobber determine the Meshulam minimum and equality cases for \(\mathbb Z_p^2\). For \(p=3,k=5\), their formula gives the global at-most-five minimum \(\theta(5)=3\), but Theorem 23 says there is no exact-support-five equality case because 5 is not divisible by 3. This does not determine the next attainable support, its dependence on the fixed five-set, or the entire spectrum. Delvaux--Van Barel study rank-deficient Kronecker Fourier submatrices and global uncertainty bounds, likewise not this per-support complete spectrum. The audited finite classification therefore supplies a genuine exact-support refinement.

## value

PASS

This is the complete exact-support uncertainty layer at the middle support size of the smallest noncyclic odd-prime plane. It resolves both the minimum and all higher attainable Fourier-support sizes uniformly over the two geometric support orbits, a natural finite invariant for Fourier uncertainty.

The dated certificate retains the supplied scientific assessment, sources and limitations.
