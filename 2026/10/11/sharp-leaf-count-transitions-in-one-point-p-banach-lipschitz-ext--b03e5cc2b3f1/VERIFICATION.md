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
# Verification of the finite-star \(p\)-trace theorem

The analytic argument gives the universal target upper bounds by choosing a leaf or arithmetic mean. It gives the lower bound in a fixed finite-dimensional real free \(p\)-space by comparing negative barycentric coordinates with the classical transportation norm, then evaluating positive barycentric coordinates with the exact finite spanning-tree formula of Cúth–Raunig (arXiv:2311.02920v1, Theorem 2.2). For each possible spanning tree rooted at a selected leaf, the subtree flow along the edge from any other vertex dominates that vertex's nonnegative coefficient. This proves the lower bound for every tree without enumerating particular trees.

The remaining optimization is concave on the ordered probability simplex and is therefore reduced *analytically* to its \(n\) extreme points, for every integer \(n\ge4\). The values of those points are \(k^{1-p}\) for \(k<n\) and \((n-1)n^{-p}\) for \(k=n\). The \(p=1\) case is treated separately for minimizer uniqueness. This proves the exact trace and center classification for every real \(0<p\le1\).

The standalone file `CHECK.py` independently enumerates \(n^{n-2}\) labeled spanning trees by Prüfer sequences in the finite dimensions \(n=4,5,6\), checks the formula for four exponents, and tests random simplex centers. Run with `python CHECK.py`. On replay the script printed `FINITE_STRESS_PASS (not exhaustive over centers, not a proof)`. The finite tests cannot establish any larger-dimensional or continuous-parameter result; those quantifiers are established solely by the preceding analytic proof.

The first-public-source date \(2024\text{-}02\text{-}05\) and its early primary \(46\mathrm{A}16\) classification were checked against the arXiv v1 first page, which lists both \(54\mathrm{C}20\) and \(46\mathrm{A}16\) as primary. The later journal record makes a different primary/secondary choice; classification of the new theorem rests on the quasi-Banach geometry and the explicitly primary code in the original source.

No formal proof assistant or independent audit was performed. The bibliography comparison is limited to inspected material and indexed records; hidden equivalent literature remains possible.
