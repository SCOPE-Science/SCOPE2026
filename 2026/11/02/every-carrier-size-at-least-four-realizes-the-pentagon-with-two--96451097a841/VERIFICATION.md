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

# Reproducibility and verification

The standalone `verify.py` is a pure Python 3 program. Run `python3 verify.py` in the directory containing the script; it requires no external packages, network, or user input. The exact program was run in the packaged build, and its observed standard output was saved in `verification_output.txt`.

For every carrier size \(n\in\{4,5,6,7,8\}\), the program independently enumerates all set partitions (equivalence relations) on \(n\) labeled points, constructs precisely the proposed unary maps on \(n\) points, and checks directly whether each partition is preserved by all operations. It independently checks that every operation has image cardinality two and that the operation count is \(\binom{n-2}{2}(2^{n-2}-2)+2\). The surviving partitions are precisely the five specified relations. The outputs report `verification=PASS` for each size and conclude with `VERIFY_OK`.

The experiment is exhaustive only for the listed five finite sizes. The unbounded assertion \(\operatorname{spec}_2(N_5)=\{4,5,\ldots\}\) is justified by the structural two-case congruence proof and the partition-lattice height bound in `RESULT.md`, not by finite enumeration. The program does not perform an independent scientific audit or certify historical novelty.
