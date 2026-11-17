---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The deterministic greedy simultaneous embeddings of X=P^k and Y=rev(P)^ell have a shared next letter exactly at i+j congruent q-1 mod q. At most k+ell-1 shared steps occur before either input finishes, proving the lower bound (q-1)(k+ell)+1 together with qk and qell. When A,B>=0, the skeleton has q-1 solo steps before first shared step, q-2 between consecutive shared steps, and q-1 after last shared step. Any A X-solo and B Y-solo schedule is feasible; greedy transitions recover solo types uniquely from the resulting word, so distinct output words are in bijection with binomial(A+B,A) schedules. When A or B<0, the shorter input embeds entirely in the longer reverse-period input, giving a unique optimum. Independent set-valued exact SCS dynamic programming computed all distinct shortest words for 27 (q,k,ell) triples (q=2..4; k,ell=1..3), checking both length and count, including q=2 and threshold cases; all agreed. Finite testing supports rather than replaces the all-parameter greedy-skeleton proof.

## originality

PASS

Best-of-knowledge: published general SCS algorithms treat arbitrary inputs and compute optimum length or enumerate all inclusion-minimal words; they do not give this all-q, unequal-exponent, distinct shortest-output binomial formula. A nearby complete ternary binomial law counts maximal common SUBSEQUENCES, not shortest common SUPERSEQUENCES, and its source provides no bijection between these distinct output families. Arbitrary-power reversal is a structurally distinct claim.

## value

PASS

Counting different optimal merged strings is a natural, separate and nontrivial invariant beyond merely computing a shortest possible length or number of alignments. The exact sharp phase transition and all-q, unequal-exponent binomial law solve a complete structured infinite family with a reproducible bijection, useful for string enumeration and merge ambiguity; this is not a renamed textbook LCS formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
