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

# Reproducing the finite collapse and relative homology calculations

The file `verification/check.py` is a self-contained Python 3 program. Run it with

```sh
python3 verification/check.py
```

Expected output is recorded in `verification/output.txt`. The final line must be `ALL_CHECKS_PASS`. There are no external libraries, network queries, downloaded tables, random seeds, or input files.

The program creates the graph \(\mu(C_n)\) directly from the edge formulas for each \(n\in\{3,4,5,6\}\). It enumerates all masks in the range \(0\le m<2^{2n+1}\), comparing two independently coded membership tests—maximum induced degree and connected-component traversal—for both ordinary and two-independence. The resulting face counts are exact.

For \(n=3,4,5\), the code makes the sequential toggle matching and checks a *literal order of free-face elementary collapses*. It removes only the two faces of each free pair and finally asserts that the remaining faces are exactly those of the original ordinary independence complex. It also checks Hasse-digraph acyclicity. The counts of elementary collapses are \(12,28,105\), respectively.

For \(n=6\), it constructs the relative simplicial boundary operator over the integers, with coefficients determined by the parity of lower-positioned vertex bits. A separately checked acyclic matching has \(301\) matched pairs and leaves seven critical three-faces, two critical four-faces, and one critical five-face. All \(301\) integer algebraic-Morse elimination pivots are verified to have absolute value one. The reduced differential \(\partial_4\) has two identical primitive columns \((0,0,1,1,0,-1,0)^T\), and \(\partial_5=(1,-1)^T\). The full chain identities are checked before and after cancellation. This establishes the integral relative group without relying on rational or mod-two rank alone.

An additional implementation computes mod-two ranks directly from the **original unreduced relative chain complex** and checks all degree-by-degree Betti numbers. Its agreement with the integral reduction is a cross-check, not an independent proof of the integral torsion claim.

The conclusion is finite and exact for the stated values of \(n\); code execution cannot establish a pattern for larger graphs. No externally independent audit has been performed.
