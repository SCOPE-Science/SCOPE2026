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

Run `python3 verify.py`.

The checker enumerates ternary squarefree words recursively by proper borders. Alphabet relabeling fixes the first symbol to \(0\). If a squarefree word has \(r\) proper borders, its longest border has at least \(r-1\) proper borders and length less than half the whole word; hence every candidate is generated as two equal border copies separated by a squarefree-compatible middle.

The replay recomputes the exact minima
\[
1,\ 3,\ 7,\ 23,\ 59,\ 142
\]
for zero through five nontrivial periods, checks that there are four normalized minimizers at length \(142\), and verifies the displayed witness and its exact borders and periods.

No sampling, timeout inference, or finite-to-infinite extrapolation is used. Independent audit has not been performed.
