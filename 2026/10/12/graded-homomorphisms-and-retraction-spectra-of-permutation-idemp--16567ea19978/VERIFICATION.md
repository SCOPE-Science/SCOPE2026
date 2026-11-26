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

This verdict is for the repaired RESULT.md. In the frozen image proof (line 55), yᵢ has augmentation zero for i>1, so yᵢyⱼ=0 rather than y₁yⱼ. The theorem survives: with W=im F and c=1, choose y₁ of augmentation one, take a basis zᵢ of W∩Hₙ, and replace zᵢ by y₁+zᵢ. The resulting basis has augmentation one on every vector, so the Aᵣ relations hold, and the images of its PBW words form a basis in each positive degree, including r=1. Re-audit: the PBW product ε(u)v forces all column sums equal as soon as any column is nonzero, and includes the zero map with c=0. In degree d the map is c^(d−1)F. The block square gives c²=c, B²=B, Bu=(1−c)u; c=0 kills all higher images and leaves a square-zero degree-one part. Shears remove u in both cases, and idempotent B is conjugate to a projection with fixed rank; c and r distinguish precisely 2n classes. For finite fields, a rank-s B is counted by choosing its image and one of q^(s(n−1−s)) complements; the extra u fiber has dimension s at c=0 or n−1−s at c=1. Substituting s=r−c gives both exponents r(n−r), and exchanging image with kernel (or Gaussian symmetry) gives the palindromic profile. In the hand check n=q=2, the multiplicities in (c,r) order (0,0),(0,1),(1,1),(1,2) were 1,2,2,1. The stated n=4,q=2 polynomial follows by substituting the Gaussian values 1,7,7,1.

## originality

PASS

The supported contribution is the complete classification of maps and retractions of the published canonical algebras, not their presentation or the generic finite-field count of complements. The strongest matching published passages establish the canonical presentation and study specific Veronese/Segre maps or the underlying solutions. The closest indexed rank-spectrum result concerns a different finite-dimensional algebra, not a theorem covering this algebra. Repairing the basis argument does not alter the claim, and the same comparisons apply to the corrected result.

## value

PASS

The canonical Yang–Baxter algebras are a published natural family and graded splittings are intrinsic to that family. The joint result shows which retracts die above degree one and which remain in the canonical family, and when two labeled splittings are equivalent under graded symmetries. At the same positive degree-one rank these grading behaviors can differ, so the scalar type is structural, not just an extra counted parameter. The uniform exact frequencies refine that classification rather than reporting a small prime-field computation. The repair preserves the statement and supplies the missing argument for the persistent image type.

The dated certificate retains the supplied scientific assessment, sources and limitations.
