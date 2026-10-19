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
# Verification record

The file `check_maw_palindromes.py` was executed directly. It constructs the finite factor language and checks minimal absence by two distinct present boundary factors, independent of the symbolic five-family derivation. All 1728 triples \(1\le a,b,c\le12\) satisfied the exact predicted set, cardinality \(b+\max(a,c)+1+\mathbf1_{a>c}\), and universal palindromicity of the minimal absent factors. Another 342 one- and three-run palindrome cases passed, including the ambient-alphabet missing-letter boundary. The seven-run palindrome `0010110100` was verified to have precisely two nonpalindromic minimal absent factors, `0011` and `1100`.

Passing program output:

`PASS_PALINDROMIC_FIVE_RUN_MAW parameter_triples=1728 one_three_run_cases=342 all_sets_exact=true nonuniversal_palindrome_counterexample=0010110100`

The infinite family and the sharp bound are established by the proof in `RESULT.md`, not inferred from the finite verification. No independent audit has been performed.
