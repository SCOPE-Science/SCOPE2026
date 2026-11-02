---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For h>=3,d>=1,gcd(a,d)=1, B=h²-h+1, T=(h-1)², a=qB+s with q>=h−1, every element has residue indexed M=v+Bu and minimal cost W(M)=h² floor(M/B)+h(M mod B). Replacing M by M+a increases W because W(M+a)-W(M)=h(a-T*K), K<=q+1, and a−T(q+1)>=q*h+s−T>0 in stated range. Thus Apéry_{dr mod a}=aW(r)+dr, r=0..a−1. Summing complete B-blocks gives the stated genus; max Apéry lies at full-block terminal qB−1 or residual terminal a−1, giving R,U, U−R=ds−ah(T−s). The two terminal elements are maximal and incomparable in semigroup preorder by explicit residue-minimum inequalities; the PF set is {R}, s=0, or {R,U}, s>0, giving type and symmetry. Equality U=R is excluded since gcd(a,d)=1, s in (0,B), and a> s. Independent priority-queue residue shortest paths for 215 actual h,a,d parameter triples recomputed all Apéry values, genus and pseudo-Frobenius sets without using greedy construction; finite checks support the unlimited proof.

## originality

PASS

Qualified PASS: Liu–Xin–Ye–Yin first identify this nonmonotone family as an open-ended target in arXiv:2306.03459; their later general GCNS theorem requires a fixed common coefficient u and cannot yield the three displayed generators for h>=3. We independently compared the coefficient equation, not merely title/parameters. The full explicit Apéry, PF, genus and sharp symmetry criterion is not in inspected theorem statements. General graph/Apéry algorithms compute instances but do not trivially imply this closed uniform classification.

## value

PASS

Complete natural numerical semigroup classification with an explicit Apéry set, symmetry/type transition at B|a, d-dependent competing pseudo-Frobenius extrema, genus, and F for a substantial infinite three-generator family singled out in prior literature as nonmonotone. Unlike a routine two-generator formula, a nontrivial no-wrap lemma is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
