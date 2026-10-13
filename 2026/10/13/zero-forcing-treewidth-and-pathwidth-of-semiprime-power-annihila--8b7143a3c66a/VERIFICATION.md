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

The standalone `verify.py` artifact was read from its actual packaged path before replay. It verifies the claimed chronological forcing sequence and complete-minor branch-set certificate for every \(2\le a\le30\). It exhaustively enumerates zero forcing sets through \(a=8\) and obtains \(Z=a-1\) throughout.

As an independent check of the algebra-to-graph reduction, the verifier constructs nonzero proper divisor ideals directly in four integer residue rings and tests zero ideal products by divisibility. Every edge agrees with the abstract adjacency rules.

Exact replay output:

```text
symbolic forcing and K_a-minor certificates: a=2..30 OK
a=2: exact Z=1, minimum_sets=2
a=3: exact Z=2, minimum_sets=6
a=4: exact Z=3, minimum_sets=23
a=5: exact Z=4, minimum_sets=63
a=6: exact Z=5, minimum_sets=207
a=7: exact Z=6, minimum_sets=559
a=8: exact Z=7, minimum_sets=1774
Z/12Z: direct ideal-product graph has 4 vertices and matches the abstract graph
Z/80Z: direct ideal-product graph has 8 vertices and matches the abstract graph
Z/1215Z: direct ideal-product graph has 10 vertices and matches the abstract graph
Z/875Z: direct ideal-product graph has 6 vertices and matches the abstract graph
a=1 boundary: K2 with Z=1
VERIFY_OK
```

The computations are finite corroboration. The arbitrary-exponent theorem is established by the symbolic forcing sequence, the \(K_a\)-minor certificate, and standard graph-parameter inequalities.
