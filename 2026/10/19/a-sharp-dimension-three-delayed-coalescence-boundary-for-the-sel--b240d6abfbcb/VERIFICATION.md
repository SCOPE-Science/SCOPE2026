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

The statements are established by the five-step analytical proof in `RESULT.md`. The central calculations are the global scalar bounds on \(x\log x\), an exact normalization/injectivity argument on the strict decreasing scalar branch, the invariant symmetric-line identity \(T_3(P(s))=P(F(s))\), and a unique interior fold certified by opposite derivative signs.

The inequality \(e^{1+1/e}<4\) is proved using elementary rational bounds for \(e\) and the positive series for \(\log2\). The nearly tangent dimension-three endpoint sign is proved without numerical assumptions using \(e^3>89641/4480>20\) and \(10-7\sqrt2>1/10\). Consequently no finite computation is being treated as a proof of a continuum result.

An executable, standalone Python 3 standard-library check is embedded as `VERIFY.py`. It evaluates the scalar map, solves the fold and inverse equations by bisection, checks distinct one-step outputs, and confirms coincidence after two steps. Its numerical examples are diagnostics only; they do not constitute exhaustive tests over the simplex or prove priority.

No separate expert or independent scientific audit has been performed. A same-model correctness, originality and value review was completed on the specified claim. Possible equivalent statements outside directly checked literature remain a bibliographic risk.
