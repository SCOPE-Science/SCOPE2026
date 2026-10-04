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

The standalone `verify.py` artifact was inspected at its packaged path before replay.

For each integer
\[
3\le n\le20,
\]
the checker explicitly constructs every proper nontrivial cyclic and dihedral subgroup of \(D_{2n}\) as a set of group elements, builds adjacency from literal nontrivial intersections, and exhaustively searches for total and paired dominating sets up to the claimed minima.

It also checks the symbolic witnesses \(H_{p,r}\), \(\langle aangle\), \(\langle a^pangle\), and \(\langle a^2angle\) in the appropriate divisibility cases.

Exact output:

```text
n=3 prime p=3 vertices=4 total=none paired=none
n=4 composite p=2 vertices=8 gamma_t=2 gamma_pr=2 total_witness=['H_2,0', 'H_2,1'] paired_witness=['H_2,0', 'H_2,1']
n=5 prime p=5 vertices=6 total=none paired=none
n=6 composite p=2 vertices=14 gamma_t=3 gamma_pr=4 total_witness=['H_2,0', 'H_2,1', 'A_1'] paired_witness=['H_2,0', 'H_2,1', 'A_1', 'A_2']
n=7 prime p=7 vertices=8 total=none paired=none
n=8 composite p=2 vertices=17 gamma_t=2 gamma_pr=2 total_witness=['H_2,0', 'H_2,1'] paired_witness=['H_2,0', 'H_2,1']
n=9 composite p=3 vertices=14 gamma_t=3 gamma_pr=4 total_witness=['H_3,0', 'H_3,1', 'H_3,2'] paired_witness=['H_3,0', 'H_3,1', 'H_3,2', 'A_3']
n=10 composite p=2 vertices=20 gamma_t=3 gamma_pr=4 total_witness=['H_2,0', 'H_2,1', 'A_1'] paired_witness=['H_2,0', 'H_2,1', 'A_1', 'A_2']
n=11 prime p=11 vertices=12 total=none paired=none
n=12 composite p=2 vertices=32 gamma_t=2 gamma_pr=2 total_witness=['H_2,0', 'H_2,1'] paired_witness=['H_2,0', 'H_2,1']
n=13 prime p=13 vertices=14 total=none paired=none
n=14 composite p=2 vertices=26 gamma_t=3 gamma_pr=4 total_witness=['H_2,0', 'H_2,1', 'A_1'] paired_witness=['H_2,0', 'H_2,1', 'A_1', 'A_2']
n=15 composite p=3 vertices=26 gamma_t=4 gamma_pr=4 total_witness=['H_3,0', 'H_3,1', 'H_3,2', 'A_1'] paired_witness=['H_3,0', 'H_3,1', 'H_3,2', 'A_1']
n=16 composite p=2 vertices=34 gamma_t=2 gamma_pr=2 total_witness=['H_2,0', 'H_2,1'] paired_witness=['H_2,0', 'H_2,1']
n=17 prime p=17 vertices=18 total=none paired=none
n=18 composite p=2 vertices=43 gamma_t=3 gamma_pr=4 total_witness=['H_2,0', 'H_2,1', 'A_1'] paired_witness=['H_2,0', 'H_2,1', 'A_1', 'A_2']
n=19 prime p=19 vertices=20 total=none paired=none
n=20 composite p=2 vertices=46 gamma_t=2 gamma_pr=2 total_witness=['H_2,0', 'H_2,1'] paired_witness=['H_2,0', 'H_2,1']
VERIFY_OK
```

The finite checks establish only the displayed calibration range. The general result rests on the proof in `RESULT.md`: the reflection-cover lower bound, the \(p^2\)-divisibility test for prime-order rotations, and the explicit clique matchings.
