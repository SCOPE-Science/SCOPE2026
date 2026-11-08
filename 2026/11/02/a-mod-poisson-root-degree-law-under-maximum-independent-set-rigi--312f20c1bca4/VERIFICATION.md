---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Root essentiality iff all root branches nonessential follows by exact dynamic-programming comparison of root-included/excluded maximum independent sets. Uniform recursive tree exponential specifications T(z)=−log(1−z), E’=exp(T−E) solve e^E=1+T, so marking the number of nonessential root branches yields [z^{n−1}]exp(u[T−log(1+T)]) for the exact joint pgf. Algebraic-logarithmic singularity transfer uniformly for u near 1 gives n^{u−1}/(Gamma(u)(log n)^u)(1+O(1/logn)); division yields mod-Poisson λ=logn−loglogn. Differentiating complex-uniform errors gives mean λ+γ and variance λ+γ−π²/6 up to O(1/logn); CLT follows. At n=1 event certain; n=2 event impossible; n>=3 positive. Independent exhaustive global maximum independent-set enumeration and rational marked coefficient comparison matched all n<=7; finite enumeration does not prove asymptotics.

## originality

PASS

Fuchs et al. already establish the unmarked root-essential probability, and Janson establishes essentiality recursion/Yule-time formulas; total independence-number CLTs and known unconditioned degree are likewise prior. The additional joint root-degree/essentiality marked PGF and complex-uniform conditional mod-Poisson law with diverging loglog deficit were not in materially inspected primary earlier sections. Novelty qualified because generic recursive-tree marking methods and unindexed deterministic essential-vertex work may contain an implicit equivalence.

## value

PASS

The natural rare root membership in every maximum independent set interacts with a fundamental local statistic. A diverging loglog correction to both conditional mean and variance, and an inverse-Gamma correction governing all cumulants, is an interpretable structural result beyond scalar root-rigidity probabilities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
