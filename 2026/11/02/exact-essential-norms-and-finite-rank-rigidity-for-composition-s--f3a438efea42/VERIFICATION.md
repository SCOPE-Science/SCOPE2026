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
# Verification of mathematical package

The included `verify.py` uses Python's standard library only. Running `python verify.py` yielded 3494 passing finite assertions. The checks include the exact sphere-count relation, direct two-point \(\ell_p\)-norm maximizers, the finite-rank tail profile for several branching degrees and exponents, and independent primal-versus-dual finite-block optimizations at \(p=1\) and \(p=\infty\).

These computations cover illustrative finite cases. The infinite essential-norm equality is established by the finite-coordinate support reduction and the weak-null compact-operator lower bound in `RESULT.md`. The endpoint finite-rank result follows from a finite partition palette for any fixed finite coefficient list, not from an experiment. The source example is credited to Liu and Ma; its new exact quantitative and endpoint analysis is shown in the proof.

Mathematical limits: no explicit universal rate of tail convergence is claimed for general maps, and the endpoint stabilization index is map-dependent. Independent correctness and definitive literature priority remain unverified.
