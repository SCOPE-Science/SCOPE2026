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

# Verification notes

The proof of the theorem appears in `RESULT.md`; the following reproducible checks are finite, supplementary tests only.

Execute `python verify.py` using Python 3 and no third-party dependencies. The program enumerates every binary word of lengths one through eleven (4094 inputs) and independently constructs its entire minimal absent scattered-subsequence set via all-subsequence generation and one-symbol extensions. It verifies the sharp binomial inequality, reconstructs each absent pattern from its greedily embedded source one-indices and terminal bit, and rejects any duplicate encoding.

For each \(1\le k\le9\), a separate explicit-construction routine forms all patterns indexed by a subset of \(\{1,\ldots,k\}\) and a terminal bit, tests that none embeds in \((010)^k\), tests every single-letter deletion for a successful embedding, tests distinctness, and checks each exact count \(\binom{k+1}{r}\). For \(1\le k\le3\), it additionally compares the explicit construction with brute-force enumeration of every MAS.

Observed output:

```text
VERIFY_OK binary_words=4094 witness_k=1..9 canonical_injection=checked
```

No computer search is claimed to prove the assertion for unbounded \(k\). The mathematical proof covers every \(k\ge1\) and every number of zeros; no independent scientific audit has been performed.
