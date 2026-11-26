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

RESULT.md lines 29–52: write α(i,j)=(a_i(j),b_i(j)). The map xα(x) is bijective exactly if b_0=p and b_1=q are permutations. For α itself to be bijective, each target second coordinate has two preimages with complementary output first coordinates, independently giving two choices at each target, hence L_r=2^r(r!)². The map α(x)x additionally requires complementary output first coordinates at each source column, so write them ε_j and 1−ε_j. The target condition now reads ε_j=ε_(q^(−1)p(j)), proving the fixed-(p,q) count including common matching edges (fixed points). Summing over ρ=q^(−1)p gives r! times its cycle enumerator at 2; inserting a singleton or using one of r−1 insertion positions multiplies by r+1, yielding B_r=r!(r+1)! and the stated fraction. Opposite-band symmetry exchanges the two products, and inversion exchanges the two one-sided sets, so the counts also hold for two columns. Minor scope wording: the displayed premise min(|I|,|J|)=2 forces r≥2, even though the proof and assumptions discuss r=1. The r=1 extension indeed holds for 2×1 and 1×2 (both maps are complete); the displayed implication for its stated premise remains true.

## originality

PASS

The supported distinction is the same-permutation intersection and its relative-permutation fiber theorem on the first nontrivial rectangular bands. One-sided existence and the cycle polynomial are standard; the closed count follows from the polynomial once the band-specific fiber characterization has been proved. Bounded comparisons did not identify this characterization or the joint count in prior work.

## value

PASS

Requiring a single transversal permutation to work in both the table and its opposite is a natural symmetric restriction unnoticed by separate-existence statements. The two-row family is the first nondegenerate family, the exact fraction quantifies failure of simultaneous compatibility, and the fiber count identifies when prescribed row maps admit many choices. The value is in the structural enumeration, not in re-evaluating the standard cycle polynomial or a finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
