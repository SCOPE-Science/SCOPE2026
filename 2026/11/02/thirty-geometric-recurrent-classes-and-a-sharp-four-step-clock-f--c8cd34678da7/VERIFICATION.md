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

# Reproducible verification

## Exact scope

Synchronous two-opinion neighbor-majority dynamics with persistent opinion on ties, on Boolean hypercubes of dimensions one through four. The graph vertices are indexed by their binary words, and state masks have exactly \(2^n\) bits in dimension \(n\). There are exactly 65,536 configurations in dimension four.

## Reproduction

```sh
g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_hypercube.cpp -o verify_hypercube
./verify_hypercube > cert_full.txt
python3 verify_independent.py > independent_output.txt
```

The C++ program directly implements the update at each vertex from its four (or fewer) neighbors, iterates all states, and reports actual counts of fixed points, primitive two-cycle states, entrance-time layers and basin classes. Its complete list of 885 primitive two-cycle pairs on the four-cube is printed in `cert_full.txt`. It checks all expected finite counts by assertions.

The Python 3.10+ program uses distinct bit-mask neighbor arithmetic, constructs all transitions, performs indegree-zero pruning of the functional digraph, checks all components of the joint first-entry/period distribution, and constructs the complete graph-automorphism action of 384 affine coordinate permutations. It then checks that the resulting 14 fixed and 16 two-cycle symmetry classes partition **every** recurrent configuration exactly once. It generates the supplied `orbit_classes.csv`. The actual printed output is supplied as `independent_output.txt`.

## Critical finite checks and limitations

- \(Q_4\): 702 fixed states, 1,770 distinct two-periodic states, hence 885 temporal two-cycles; no longer cycles.
- All 65,536 initial configurations partition into 46,166 fixed-point basins and 19,370 two-cycle basins.
- The complete entry layers at times \(0,1,2,3,4\) have populations 2,472; 17,336; 34,944; 8,864; 1,920.
- Direct stepwise witness \(1972\to1377\to276\to1\to0\) first enters a fixed point at time four; no state has larger entrance time.
- The spatial quotient has 14 classes of fixed states and 16 classes of temporal two-cycles. This is a finite exhaustive classification, not an inference about higher dimensions.

No independent external audit or validation has been performed. Checking the supplied outputs without executing their programs is insufficient for replay. The source programs and exact finite domains, not log lines by themselves, constitute the reproducible enumeration certificate.
