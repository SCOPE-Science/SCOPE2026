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

# Reproducibility and limits

Run `python3 verification/check_bundled.py` from the directory containing `RESULT.md`. It uses the standard library only. An exhaustive generator enumerates the set partitions of worlds of size \(1\) through \(6\), evaluates the bundled Boolean operation on **all** subsets for each ordered pair, and groups pairs by equal complete truth tables. It tests every fiber involving a transverse pair against the claimed cardinality \(2^c\), verifies that no nontransverse pair shares such a fiber, and checks equality of join-component counts within the fiber.

Observed labelled-pair totals are \(1,4,25,225,2704,41209\), and observed transverse-pair totals are \(0,0,0,6,60,630\). For sizes \(4,5,6\), the transverse fibers number \(3,30,315\), all of size \(2\). A second construction checks each size from \(4\) through \(12\), with the predicted maximum ordered fibers \(2,2,2,2,4,4,4,4,8\), and explicitly distinguishes the local-only swap at size eight from global reversal.

No computation tests infinitely many cardinalities or every finite size. The general conclusion rests on the direct minimal-neighborhood, proper-two-colouring, and component-size proofs in `RESULT.md`. These finite tests are reproducible self-review; they are neither a formal proof assistant certification nor an independent audit.
