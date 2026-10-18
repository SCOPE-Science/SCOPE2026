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

# Reproduction and limits

The proof is an infinite-family argument based on the exact star cover and a graph-of-spaces homotopy equivalence; the finite tests below are checks of implementation, signs and boundary conventions, not a substitute for the proof.

From the directory containing the packaged files, run:

```bash
python3 verify_biclique.py
```

The program requires only the Python standard library. It independently enumerates all strict vertex orders for the seven bipartition sizes \((2,2),(2,3),(3,3),(3,4),(3,5),(4,4),(4,5)\), constructs strong matchings using the one-earlier-neighbor criterion, and checks that the downward closure equals the stated facet model. It separately computes all mod-two boundary ranks and compares with the predicted first Betti number \(2mn-m-n+1\). For \((2,2),(3,3),(3,4)\), it computes signed simplicial Lefschetz numbers under all indicated group elements, including balanced-side interchanges, then compares them with the complete integral-cycle-module character.

The delivered `verify_output.txt` records each face count, finite f-vector, homology rank and automorphism check total; the program ends with `ALL INDEPENDENT FINITE CHECKS PASSED` on success. Computational homology is over \(\mathbb F_2\); the integral homology and the integral symmetry representation are proved by the graph cycle-complex isomorphism, not inferred from the characteristic-two check.

The finite enumeration checks were replayed from the actual embedded program and matched the embedded recorded output. No independent external audit or third-party mathematical certification was performed.
