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

# Verification evidence and limits

`verify.py` uses only the Python standard library. Running `python3 verify.py` enumerates all 52 equality types of five-letter words (restricted-growth representatives). The 52-type cover is *exhaustive*, not a sample: any five-letter word over any alphabet induces a set partition of five positions, and each partition has a unique restricted-growth representative. Both the descendant sets and their weights are invariant under injective relabeling. For each type, the code checks the integer inequality \(\sum_{v\in D_2(w)}5h(v)\ge5\).

The same program checks every length-five word over alphabets of sizes two through six and independently lists each of the six ternary codewords' exact three-symbol deletion shadows. The shadows are pairwise disjoint and their union has twenty words. The checker output is embedded verbatim as `verification_output.txt`.

The universal inequality is proved in `RESULT.md` by complete multiplicity case analysis; passing finite checks cannot substitute for that proof. The six-code construction and upper bound prove the exact ternary capacity, but the work does not certify originality exhaustively or comprise an independent mathematical audit.
