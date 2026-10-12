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
# Verification

The packaged `verify_absorption.py` was executed from its actual path before assembly. It implements Kihara's hierarchy recursion and the proved finite absorption normal form.

The exhaustive counts are
\[
\begin{array}{c|rrrrrrrr}
\text{length}&1&2&3&4&5&6&7&8\\
\hline
\text{level at most }4&4&14&38&56&40&14&2&0\\
\Sigma_4&0&1&10&23&19&7&1&0\\
\Pi_4&0&1&10&23&19&7&1&0.
\end{array}
\]
Hence there are \(61\) normalized fourth-level patterns on each side.

The checker then computes the full absorption relation using optional expansion of each infinite quantifier, ordinary duplicate contraction, and subsequence containment. Its symmetric quotient has \(37\) classes for \(\Sigma_4\) and \(37\) for \(\Pi_4\). It also reproduces the source's \(17\) normalized \(\Sigma_3\) patterns.

The exact replay is bundled as `verification_output.txt` and ends with `VERIFY_OK`.

## Limits

The executable check certifies the finite syntactic quotient after the mathematical cutoff and normal-form proofs. It does not prove semantic inequivalence between distinct absorption classes. Therefore \(37\) is an upper bound, not an asserted exact many-one or di-many-one count.
