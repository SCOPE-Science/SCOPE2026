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

# Verification and reproducibility

The proof in `RESULT.md` is valid for arbitrary finite fields and all \(d\ge3\). Its nonstandard step is the intersection identity \(\operatorname{im}\phi\cap\bigwedge^2V=\bigwedge^2\operatorname{im}A+B(\ker A)\), proved there by projection onto \(V\). Counting linear-map ranks using Gaussian binomials then yields the exact polynomial and its support; the limiting distribution is deduced from a tight matrix-corank law and injection probability into a growing quotient space.

Run the standalone program with `python verify.py` using Python 3 and no packages. This program explicitly evaluates the bracket map on the free Lie generators and computes the rank of the resulting \((d+\binom d2)\)-dimensional linear matrix. It compares independent exhaustive histograms with the claimed closed formula for \((d,q)=(2,2),(3,2),(2,3)\), totaling \(64+262144+729=262937\) individually examined endomorphisms. The boundary case \(d=2\) is used only as an implementation diagnostic, not as an extension of the theorem's stated gap claims. An additional check compares predicted rank supports and gap sizes for \(3\le d\le15\).

Expected final console marker: `VERIFY_OK`. Direct finite enumeration is not an infinite-field or infinite-dimension certificate; the general result depends on the mathematical proof. The fixed-field asymptotic concerns weak convergence of the normalized integer corank, not total-variation convergence to a nonlattice continuous measure.
