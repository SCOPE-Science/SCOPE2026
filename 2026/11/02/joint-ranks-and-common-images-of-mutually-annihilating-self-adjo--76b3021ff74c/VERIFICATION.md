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

# Reproduction and scientific limits

Execute `python checker.py` (Python 3, standard library) and compare its complete standard output to `checker_output.txt`.

The program constructs every self-adjoint matrix directly from a symmetric matrix and the chosen Gram form, evaluates \(T^2=0\) and \(T_iT_j=0\) by original field matrix multiplication, determines each rank and combined image span by Gaussian elimination, and compares every nonzero stratum coefficient to the theorem. It exhausts seven ambient configurations: \(n=2,q=3\) both forms, \(n=3,q=3,5\), \(n=4,q=3\) both forms, and \(n=2,q=9\) split. The extension field is represented by irreducible \(X^2+1\) over \(\mathbb F_3\). These are checks for \(m=1,2\); the proof covers every \(m\ge1\).

The finite results do not establish historical originality, do not constitute an independent audit, and do not replace the general symbolic argument. No nonreduced scheme computation is claimed.
