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

The symbolic verification has four steps.

1. For a finite local nonfield, \(Z(R)=M\), and the published total-graph structure gives \(qK_s\) in residue characteristic \(2\), and \(K_s\sqcup((q-1)/2)K_{s,s}\) in odd residue characteristic.
2. A paired dominating set on a disconnected graph restricts to a paired dominating set on every component. In \(K_s\), these are exactly the positive even subsets. In \(K_{s,s}\), these are exactly the subsets selecting the same positive number of vertices from both parts.
3. Lowest nonzero degree gives \(2q\) or \(q+1\). The leading coefficient is \(1\) in residue characteristic \(2\), and \(s\) in odd residue characteristic, so the polynomial reconstructs \(q\), \(s\), and parity.
4. The standalone checker constructs the actual total graphs of \(\mathbb Z_4\), \(\mathbb Z_8\), and \(\mathbb Z_9\), exhaustively enumerates all subsets, tests domination and perfect matching, and compares the coefficient vectors with the formulas. It also replays the reconstruction rule on additional structural profiles.

Exact output:

```text
VERIFY_OK
actual_rings=Z4,Z8,Z9
bruteforce_subsets=16,256,512
additional_profiles=(4,4,char2),(8,8,char2),(3,9,odd),(5,5,odd),(7,7,odd)
reconstruction_from_lowest_degree_and_leading_coefficient=passed
```

The finite checks are corroborative only; the arbitrary-ring theorem is proved by the residue-coset decomposition and exact matching argument.
