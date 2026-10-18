---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

The normalization for λ=2,μ=3 is 2 N(2x+3y) N(3x−2y)/[13(N(x)^2+N(y)^2)]. Each norm is max over eight signed support functionals. Choose active supports c,d; every 64 ordered pair of normals reduces under dihedral symmetries to five angular relative classes k=0..4. For each class the package specifies positive convex combinations G_x,G_y of rank-one normal projections, hence x^TG_x x≤N(x)^2 and similarly y. The proposed 4×4 symmetric matrix C0 diag(G_x,G_y)−(ell m^T+m ell^T)/2, C0=3+149√2/48, is PSD for all five classes. I independently reconstructed these matrices and all 75 nonempty principal minors: 26 identically zero, 49 strictly positive using exact rational comparisons in Q(√2), so PSD is mathematically certified independent of numerical scanning. Independently recomputed the witness x=(1−√2,−1), y=(−z,−w), z=6/(9+4√2), w=(9−4√2−6z)/12; direct active-support evaluation gives N(x)=1, N(y)=z, exactly the claimed quotient (144+149√2)/312. A finite set of certificates is exhaustive because every possible active support pair reduces to one of the five proven classes; no assumption about sampled vectors is used.

## originality

PASS

The original 2021 generalized constant and its Example 4.3 treat (2,3) but only the C_NJ=2 endpoint; the regular octagon is uniformly non-square with C_NJ<2. The 2025 skew p-family primary full text pp.1–12 extends the definition and gives square endpoint and other examples, not the regular octagon exact product. The highly relevant 2024 Yang–Li–Yang octagon paper computes Euler–Lagrange sums of squares, a distinct objective whose bound need not attain equal transformed norms at the optimizer. Its full paper remained inaccessible and is a material but not alone decisive risk.

## value

PASS

The exact generalized Zbăganu product invariant for the regular octagon at the defining paper’s natural λ,μ=(2,3) is a motivated benchmark bridging Hilbert (value 1) and square-type extremal endpoints. A complete global exact certificate across 64 active-support pairs and a sharp algebraic witness are nontrivial, independently reusable tools for related polyhedral Banach-space constants. The fixed parameter pair is not arbitrary: it is explicitly singled out by the initiating 2021 Example 4.3.

The dated certificate retains the supplied scientific assessment, sources and limitations.
