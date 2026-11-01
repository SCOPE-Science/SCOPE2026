---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Reconstructed the exact channel: n>=4 over a labeled ternary alphabet, one nonwrapping four-position window rotated by 1, 2 or 3, identity included, duplicate outputs collapsed. Each window contributes <=3, giving 3n-8; the six-periodic prefix 000121 achieves all three increments for every appended window. A nontrivial cyclic rotation changes at least two coordinates, so the new terminal window cannot duplicate an output from any old window overlapping it in at most one position. This proves six-letter locality for every n, not just checked n. Independent complete 3-ary balls for n=4..8 give 72,126,246,474,930 maximum centers; the 21 canonical five-letter states and 41 edges were independently rebuilt from exact balls. Exact left-vector annihilation by Q(A) (order 10), plus the first ten values 126..47850, proves the displayed rational generating function for all n. Connectivity of the listed finite graph and its 01201 self-loop give primitivity and the Perron growth rate. Finite enumerations are graph/identity checks, not an extrapolated infinite proof.

## originality

PASS

Best-of-knowledge PASS for the complete ternary equality-case automaton, rational count and entropy; no inspected stronger source directly implies the statement. The source 2026 Chen–Milenkovic treats permutation/cyclic burst error-correcting codes and primarily binary redundancy rather than ternary four-window maximizing-center census; complete primary full text could not be retrieved this run, explicitly retained as a priority risk.

## value

PASS

PASS: It determines the exact infinite language of largest ambiguous centers of a motivated four-symbol cyclic read-error channel, not merely an isolated finite example or redundancy slogan. The all-length maximum, exact rational census and primitive-state entropy establish the rarity rate of worst-case centers; this natural language invariant is reusable in combinatorial channel analysis. No unsupported coding-rate or decoding gain is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
