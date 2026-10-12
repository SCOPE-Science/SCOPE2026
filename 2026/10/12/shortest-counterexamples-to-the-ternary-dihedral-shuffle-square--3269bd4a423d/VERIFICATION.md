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

Run `python3 verify.py` in the same directory as `certificate.json`.

The checker enumerates every even ternary word at lengths \(2,4,6,8\). For each word of length \(2n\), it tests every \(n\)-position subset and compares the two induced subwords against all rotations and reflected rotations. It verifies the total even-word counts
\[
3,\ 21,\ 183,\ 1641
\]
and the corresponding failure counts
\[
0,\ 0,\ 0,\ 48.
\]

At length \(8\), it recomputes the symmetry classes under alphabet permutations and reversal and verifies four classes of size \(12\), with representatives `00011022`, `00110220`, `00111221`, and `01112210`.

For `00011022`, it also verifies all \(\binom84=70\) position splits, finds \(24\) oriented balanced splits, confirms that they all yield the same unordered pair `0012`/`0102`, and checks the complete \(D_4\)-orbit of `0012`.

The verifier is exhaustive only over these finite lengths. The claim makes no assertion about counts at larger lengths. Independent audit has not been performed.
