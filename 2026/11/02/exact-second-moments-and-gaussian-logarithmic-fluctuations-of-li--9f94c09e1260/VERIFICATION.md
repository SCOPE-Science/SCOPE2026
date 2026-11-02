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

# Reproducibility and scientific limitations

Execute the supplied `verify.py` using Python 3.9 or later, with no third-party dependencies: `python3 verify.py`. Compare its standard output byte-for-byte against `verify-output.txt`.

The checker enumerates every direct ball from all pairwise disjoint adjacent-swap masks and compares each volume to a separate path-matching dynamic program. It enumerates all 35,778 words for alphabet size two through length eleven, alphabet size three through length eight, and alphabet size four through length seven. Every exact mean and second moment is also compared with (i) an independent Bernoulli-boundary enumeration and (ii) rational-moment recurrences. Additional paired-matching matrix checks cover alphabet sizes two, three, four, seven and one hundred through length 79. The checker evaluates illustrative logarithmic constants; these floating-point computations do not certify the convergence theorem or the algebraic separation for infinitely many alphabet sizes.

The mathematical proof in `RESULT.md`, not finite enumeration or recorded logs, establishes all-length correctness, matrix asymptotics and renewal limit laws. No independent scientific validation has been performed. The full expanded 2017 journal treatment remains a publication-priority uncertainty.
