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

The mathematical certificate is the proof of the universal potential inequality in `RESULT.md`: the exact function \(F\) is at least one on nonsingletons, decreases by no more than one per transformation, and is realized by the displayed word. All quantifiers include \(n=2\); singleton subsets have time zero. The only rank-dropping transition to a singleton is \(\{0,1\}\overset b\longrightarrow\{1\}\), and the potential there equals one.

Run `python3 verify.py` using only the Python standard library. It independently constructs the full directed subset graph, computes distances to all singleton vertices by reverse breadth-first search, compares the closed formula for every nonempty subset for each \(n=2,3,\ldots,15\), and checks the full-set threshold. Expected output: `CERNY_SUBSET_GAP_PASS n=2..15 subsets=65518`. These finite checks are corroboration only, not a substitute for the proof.

No independent mathematical audit has been performed. This statement does not certify originality: a complete source comparison with the Cardoso dissertation remains outstanding, and equivalent formulae in other literature could exist.
