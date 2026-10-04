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

Run `python3 verify.py` in the same directory.

The verifier uses only exact integer arithmetic and the Python standard library. It reduces feasible strict ternary length-two rankings to \(420\) length-relevant shape classes. For each shape and each integer gap \(1\le t\le28\), it substitutes \(H_i=L_i+t\) and solves the induced lower-bound difference constraints by exact longest-path closure. If no positive cycle exists, the closure is the componentwise least nonnegative solution and therefore minimizes the total profile sum for that fixed \(t\).

The script verifies that every one of the \(420\) shapes has a realization of length at most \(86\). Since any \(t\ge29\) contributes at least \(3t\ge87\) to the profile sum, no omitted gap can improve an optimum. The unique worst shape has minimum \(86\), corresponding to exactly \(72\) labeled rankings after restoring the two orientations, the six edge-pair orders, and the six loop-label orders.

For the canonical extremizer the script checks the exact profile matrix \(\begin{pmatrix}12&5&6\\0&13&15\\11&10&14\end{pmatrix}\), verifies its row sums equal its column sums, constructs an Eulerian circuit, and confirms a circular realization of length \(86\). It also checks the direct lower-bound anchors for that ranking. Expected terminal lines include `MAX_MIN_LENGTH 86`, `EXTREMAL_RANKINGS 72`, `EULER_LENGTH 86`, and `VERIFY_OK`.
