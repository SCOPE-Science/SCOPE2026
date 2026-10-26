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
# Reproducibility and proof checks

The proof in `RESULT.md` is independent of computational experiments. For \(u\perp_B v\), \(\|u\|=\|v\|=1\), setting \(D=tu-t^{-1}v\) gives \(\|D\|\geq t\) and \(\|D\|\geq |t-t^{-1}|\). The two exact decompositions of \(u-v\) imply the three scalar upper envelopes \(2t\), \(t^{-1}\), and \(2t^{-1}-t^{-3}\); their only global equality scale is \(t=2^{-1/2}\). At that scale, the bound is attained exactly when \(\|u-2v\|=1\). Both planar witnesses are provided with explicit norm-one support functionals.

The standalone `verify.py` uses only the Python standard library. Execute `python3 verify.py` to check two exact endpoint examples, a total of 11,340 finite tests on smooth \(\ell_p^2\) Birkhoff profiles, and 4,999 scalar envelope checks. At original execution it printed `PASS: 2 exact extremal norms; 11340 smooth Birkhoff profile checks; 4,999 envelope checks; max smooth ratio 1.260784823312`.

These finite checks cannot prove the universal theorem. The infinite-dimensional result and the global maximization are justified by the analytic inequalities, not by enumeration. Historical publication priority remains subject to independent literature review; no independent mathematical audit has been performed.
