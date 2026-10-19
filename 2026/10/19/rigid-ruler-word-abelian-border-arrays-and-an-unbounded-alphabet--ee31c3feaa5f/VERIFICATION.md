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
# Reproduction and evidence

Run `python3 verify.py` with the Python 3 standard library. The script independently constructs the longest Abelian-border arrays by comparing prefix and suffix multisets at each prefix length. For the ruler prefixes it verifies the displayed formula at lengths \(1,2,3,4,5,6,7,8,16,32,64,128,256,512\). It additionally enumerates all normalized restricted-growth words that satisfy the target array prefix constraints at every length \(1\) through \(16\); in each case it finds exactly the ruler prefix. The checker exits nonzero on disagreement and prints `RULER_ABELIAN_BORDER_CHECKS_PASS` on success.

## Proof dependencies

The unrestricted result depends on two exact Parikh-vector cancellation identities and induction on the prefix length, detailed in RESULT.md. The valuation identity for a multiple of a power of two plus a smaller positive integer is elementary. The computation is a finite regression check, not an infinite certificate. No external datasets, third-party code, or downloaded articles are needed to reproduce the computation.

## Scope of verification

Only the ruler-family inverse theorem and its alphabet-size corollaries are claimed. No global optimality for general length-\(n\) arrays, higher-alphabet counting formula, or complete algorithm for arbitrary Abelian-border arrays is claimed. Literature overlap was reviewed separately; no independent scientific audit has been performed.
