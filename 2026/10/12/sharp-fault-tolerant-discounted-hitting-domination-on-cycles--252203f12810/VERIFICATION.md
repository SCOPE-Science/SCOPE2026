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

# Reproducible checks and limits

The all-parameter conclusion follows from the analytic proof in `RESULT.md`. The two standalone scripts below use only the Python standard library and independently test demanding finite boundaries; none certifies a theorem by finite enumeration.

Run `python3 verify_faults.py` to reconstruct the discounted hitting potential for every nonempty source set on labeled cycles of orders \(3\) through \(9\), for fidelities \(1/2\), \(2/3\), and \(4/5\). The script solves the original pinned linear system over exact rational numbers. It evaluates every allowed removal of \(f\) sources for \(f=1,2,3\) (where admissible) and the extreme \(f=n-1\). It checks the proposed cyclic-window characterization for every source set at each strict and equality threshold, verifies the exact minimum, and checks the number of optimum labeled source sets against an independently generated cyclic-composition count. The recorded result is in `faults_verification_output.txt`: **PASS**, with 3,027 pinned solves, 57,345 removal cases, 948 threshold profiles, 194,796 source-set classifications, and 10,464 optimum-set comparisons.

Run `python3 verify_transfer.py` for a separate finite matrix-enumerator test. It constructs the state transitions and takes literal matrix-power traces as polynomials, comparing the resulting coefficient with an independently enumerated set of cyclic compositions. The recorded result is in `transfer_verification_output.txt`: **PASS** across 374 parameter profiles, including 229 nonzero coefficients.

The programs are fully reproducible from the files in this package. The linear solver is exact over \(\mathbb Q\); the universal theorem also applies to irrational \(\lambda\) and \(\tau\) by the algebraic proof. Neither program is an independently commissioned audit, a formal external certification, or evidence for any untested graph family.
