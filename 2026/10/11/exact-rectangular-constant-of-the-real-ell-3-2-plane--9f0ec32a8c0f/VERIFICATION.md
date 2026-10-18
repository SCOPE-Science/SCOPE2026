---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Every nonzero real Birkhoff-orthogonal pair in l_3^2 reduces by signed-coordinate interchange to x=(1,t), y=±s(t²,-1), 0<=t<=1, s>=0. The noncompetitive branches are bounded by 2^(2/3) and explicit t=1/3,s=4/3 exceeds this bound. Interior stationarity yields E1(t,s)=0 and G(t,s)=0; exact resultant factors with degree-14 P(t³), Sturm gives precisely two roots in (0,1) and only the first admits s>t. Exact isolated t≈0.30927767737,s≈1.23472445472 yield μ≈1.72853813848209; independent numerical optimization corroborated not proved the global bound. Script was read and symbolic certificate structure checked against proof.

## originality

PASS

The full Baronti–Casini–Papini primary rectangular-constant paper explicitly reports the p=3 value only numerically (1.7285) rather than the root-isolated exact algebraic characterization. The Paul–Ghosh–Sain arXiv full text proves attainment and polygonal reductions but no exact l3 parameter. Published Resultary comparisons returned distinct cubic generalized and l4 constants, not the same l3 Joly constant; uniqueness beyond searched sources not guaranteed.

## value

PASS

The exact sharp classical rectangular constant of the non-Hilbert l3^2 benchmark replaces an established only-approximate numerical value with a rigorous isolated algebraic root and unique optimizer. It is a natural invariant whose exact value is useful for testing geometric inequalities and precise extremal comparisons, rather than an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
