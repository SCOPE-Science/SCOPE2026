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

The standalone `verify.py` artifact was read from its actual packaged path before replay.

It constructs the seven exponent-pair vertices, derives adjacency solely from the two exponent-sum inequalities, and exhausts all
\[
2^7=128
\]
vertex subsets under the standard zero forcing color-change rule.

It verifies the coefficient dictionary
\[
\{2:4,\ 3:24,\ 4:33,\ 5:21,\ 6:7,\ 7:1\},
\]
checks that the four stated two-vertex sets are exactly the minimum zero forcing sets, and replays a five-force chronological sequence for each.

The same artifact checks every edge and running-intersection condition of the width-two path decomposition, verifies the induced four-cycle used for the treewidth lower bound, and directly reconstructs representative ideal-product graphs from divisor arithmetic for four choices of distinct primes.

Exact replay output:

```text
zero forcing polynomial: {2: 4, 3: 24, 4: 33, 5: 21, 6: 7, 7: 1}
minimum zero forcing sets: [((0, 1), (0, 2)), ((0, 1), (1, 1)), ((1, 0), (1, 1)), ((1, 0), (2, 0))]
forcing sequence ((0, 1), (0, 2)) : [((0, 1), (2, 1)), ((0, 2), (2, 0)), ((2, 0), (1, 2)), ((2, 1), (1, 1)), ((1, 2), (1, 0))]
forcing sequence ((0, 1), (1, 1)) : [((0, 1), (2, 1)), ((1, 1), (1, 2)), ((2, 1), (0, 2)), ((0, 2), (2, 0)), ((1, 2), (1, 0))]
forcing sequence ((1, 0), (1, 1)) : [((1, 0), (1, 2)), ((1, 1), (2, 1)), ((1, 2), (2, 0)), ((2, 0), (0, 2)), ((2, 1), (0, 1))]
forcing sequence ((1, 0), (2, 0)) : [((1, 0), (1, 2)), ((2, 0), (0, 2)), ((0, 2), (2, 1)), ((1, 2), (1, 1)), ((2, 1), (0, 1))]
width-2 path decomposition OK; induced C4 OK
Z/36Z direct ideal-product graph OK: 7 vertices
Z/100Z direct ideal-product graph OK: 7 vertices
Z/225Z direct ideal-product graph OK: 7 vertices
Z/1225Z direct ideal-product graph OK: 7 vertices
all 128 subsets classified; 90 are zero forcing
VERIFY_OK
```

The exhaustive subset census proves the finite polynomial after the symbolic ring-to-graph reduction. The scalar zero forcing number and both widths also have explicit structural certificates independent of exhaustive search.
