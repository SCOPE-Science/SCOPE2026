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

# Checks

- Run `python3 verify.py` with a standard Python 3 interpreter in the directory containing the included script. The script uses only `itertools`, `fractions`, and `math` from the standard library.
- For each integer \(1\le n\le9\), it enumerates all \(n!\) permutations, counts their original functional cycles and left-to-right upper records, and checks \(\mathbb E[C_n]\), \(\mathbb E[R_n]\), all positional cycle/record covariances, and the summed covariance with exact fractions.
- For all \(1\le k\le n\le200\), it compares the two exact harmonic/binomial expressions for the expected number of fully closed prefix cycles.
- Successful execution ends with the literal line `PASS exact enumeration n<=9, all n<=200 binomial-harmonic identities`.

# Independent audit limitation

These finite checks support the exact symbolic derivation but do not prove the theorem for unbounded \(n\); the all-\(n\) proof appears in RESULT.md. The distribution-free convergence of partial permutation completions, the record compatibility cases, and the binomial asymptotic tail have been established analytically, not via finite experiments. No separate independent scientific validation has been performed.
