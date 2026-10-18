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

# Reproduction and verification

All files are ordinary UTF-8 text. With Python 3's standard library, run:

```sh
python3 verify_morse.py
python3 verify_independent.py
```

The first program enumerates all \(2^{14}=16{,}384\) subsets, all \(8{,}850\) nonempty faces and all \(52{,}304\) nonempty Hasse covering relations. It constructs seven rounds of toggle pairs, verifies the critical cells and full acyclicity by Kahn topological sorting, independently enumerates all \(5{,}040\) point permutations to identify the Fano graph collineations, verifies four graph symmetry generators, and computes their signed simplicial Lefschetz numbers. No numerical approximation, solver timeout, or undocumented external software is used.

The second program builds the graph from a separately labeled Fano triple system, implements the complement-dominating definition directly, builds every simplicial mod-two boundary and reduces all its columns using integer bit operations. Its ranks and resulting reduced mod-two Betti vector independently agree with the integral Morse conclusion. The scripts intentionally use different labels and different face conditions.

Expected exact output transcripts are supplied as `verify_morse_output.txt` and `verify_independent_output.txt`. Do not substitute transcripts for running the included code. The proof of the group action uses the ordinary Lefschetz formula on signed oriented simplices, and the full graph-automorphism generation is explicitly exhausted. This is a finite-combinatorial complete certificate for one graph, not a proof of a family classification or an integral description of the quotient-space homotopy type.

Self-review: passed. Independent audit: not yet performed.
