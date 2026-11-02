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

# Reproduction and evidence

Run `python verify.py` in the directory containing the bundled script. Only the Python standard library is used. The script independently constructs the two Jordan-block shift, builds all normalized complement generators for eight \((d,r,q)\) cases, and computes exact ranks of their \(2d\) Krylov columns.

The normalized tests compare expected values \(q^{4d-4}\) for \(r=0\) and \((q-1)q^{4d-5}\) otherwise for \((d,r,q)\) equal to \((3,0,2),(3,1,2),(3,2,2),(3,2,3),(4,0,2),(4,1,2),(4,2,2),(4,3,2)\). It also enumerates every Hankel coefficient tuple for \(r=1,2,3,4\) over \(\mathbb F_2\) and \(\mathbb F_3\), and separately exhausts all \(651\) two-dimensional subspaces of \(\mathbb F_2^6\) in each of the three dimension-six Jordan cases. The expected splitting counts in those Grassmannian tests are \(256,128,128\). Successful output concludes with `VERIFY_OK`.

The nonstandard infinite-size ingredient is Dwivedi--Grinberg, arXiv:2109.05415, Theorem 1.1: for each \(r\ge1\) there are precisely \(q^{2r-2}\) singular \(r\)-by-\(r\) finite-field Hankel matrices. The remaining algebraic reduction is proved in RESULT.md. Exhaustive finite tests do not independently establish that reduction for unbounded \(d\), nor do they prove novelty or publication priority.
