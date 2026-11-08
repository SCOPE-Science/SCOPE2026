---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Ghrist's radial-tree graph homotopy theorem makes F3(S_m) connected with no H>=2 and known beta1=1+m(m+1)(2m−5). Finite group equivariant Euler gives 1−tr H1=χ(F3(S_m)^{(σ,τ)}). For τ=id a fixed configuration consists of three points on the fixed-arm star S_f; its three-edge-per-arm cubical Euler coefficient is 6[z³]((1+z)(1+z+z²+z³)^f−fz(1+z+z²)(1+z+z²+z³)^(f−1))=−f(f+1)(2f−5), including f=0,1,2. For a transposition of labels one point lies in fixed S_f and an exchanged pair occupies each length-two arm cycle at the same positive radius, producing 2c2 contractible components; a 3-cycle similarly produces 3c3 intervals. Hence the three full trace formulas follow. Exact falling-factorial moments E[(f)_j]=1 for j≤m give vanishing full-arm invariants, while signed moments E_sgn[(f)_j]=1 iff m−j∈{0,1} yield exceptional alternating-arm ranks 5,2,0. Independently expanded the cubical Euler polynomial for f=0..8, finding exact agreement. The source checker constructs cell support products and checks 45 conjugacy representatives for m=3..5. This is a symbolic all-m argument, not an extrapolation from these tests.

## originality

PASS

Ghrist's general star-graph homotopy formula and Farley--Sabalka's graph braid methods provide ranks and topology, not simultaneous arm/particle-label traces. Wawrykow's complete ordered-star presentation and representation stability may encode the answer implicitly, but no same joint closed character was identified in the accessed primary full text. Earlier unlabeled-star symmetry determines only the trivial label-isotypic projection, expressly excluded from novelty.

## value

PASS

Label and arm permutations are intrinsic, commuting symmetries of ordered graph configurations. The exact nontrivial label-sign and standard sectors and the disappearing alternating-arm quotient homology beyond four arms provide reusable representation data not inferred from the previously known wedge count. A complete uniform answer for exactly three particles can be valuable without solving the general particle-count problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
