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

The complete exact finite-state certificate and independent small-order check are in `verify.cpp`. With a standard C++17 compiler, run:

```sh
c++ -std=c++17 -O2 verify.cpp -o verify
./verify
```

The observed successful output was:

```text
VERIFY_OK core=16 cycles=1,1,4,5,5; full-graph n=7..12; colorings_examined=11182080; checked n through 100
```

The checker constructs every permissible transition from the explicitly defined nine-bit condition (256 input states, two candidate appended bits apiece), verifies that precisely 90 directed arcs exist, and obtains the exact retained-set sizes \(42,20,16\) in three rounds of incoming/outgoing pruning. It then compares the induced graph with the 16-state, 16-arc cycle certificate displayed in `RESULT.md`. The complete recurrent graph is sufficient for an all-\(n\) proof because any cyclic outer coloring must trace a closed directed walk.

As a separate check, the program considers all \(2^{2n-1}\) possible assignments of shore colors to the original \(2n\) vertices with the first outer color fixed, for every \(7\le n\le12\). It tests every original outer, spoke, and inner edge condition directly, without using the reduced state graph, and compares the cut counts and crossing-spoke spectra with the theorem. This totals 11,182,080 assignments. It also tests direct periodic representatives for every allowed multiple through order 100 and checks finite closed-walk counts for \(7\le n\le100\).

These full-coloring tests do not by themselves prove an infinite assertion; that assertion follows from the reduction and the exhaustive finite transition core. The verification does not establish external peer review, publication priority, or results for other jump parameters.
