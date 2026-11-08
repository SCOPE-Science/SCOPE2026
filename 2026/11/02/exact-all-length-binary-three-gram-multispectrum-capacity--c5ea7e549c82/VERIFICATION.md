---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Every binary word of n≥3 determines an Euler trail in the binary order-two de Bruijn digraph, and conversely every nonnegative 8-vector of edge counts with nonempty weakly connected support and admissible zero or +1/−1 vertex imbalance admits a word trail. Source proof parametrizes edge flows by three free multiplicities and two loop variables. The actual verify_threegram.py was read: it enumerates each of 255 nonempty support masks, all 13 allowed imbalance patterns, applies exact connectivity and positivity constraints, and sums geometric tails as an integer polynomial identity; algebraically reduced numerator and denominator agree with displayed GF, not merely interpolation of finite coefficients. Pole structure gives order five at z=1 and uncancelled primitive 3rd, 4th and −1 roots, proving degree4 period12. The displayed numerator evaluates to 13 at z=1, so leading coefficient 13/288. Independently generated all 2^n words n=3..16, finding exactly the expected 14 profile counts (T_15=1880,T_16=2449). The finite checks alone do not prove all lengths.

## originality

PASS

Best-of-knowledge originality of the precise final claim after Resultary and primary-paper statement/implication comparisons, with named inaccessible sources and residual risks explicitly retained: Exact all-length binary three-gram multispectrum capacity. No failed search is represented as a proof of novelty.

## value

PASS

The exact number of possible observation vectors is the optimal cardinality of a k-mer multiplicity-reconstruction code, an intrinsic information-capacity problem. Completing all lengths, quasipolynomial period and leading constant for the first nontrivial k=3 case adds a natural enumeration beyond k=2.

The dated certificate retains the supplied scientific assessment, sources and limitations.
