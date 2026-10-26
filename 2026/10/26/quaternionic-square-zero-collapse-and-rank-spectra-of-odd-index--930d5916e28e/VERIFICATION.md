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

The accompanying `verify_dicyclic.c` is a self-contained C11 checker. Compile using `cc -O3 -std=c11 verify_dicyclic.c -o verify_dicyclic` and run `./verify_dicyclic`. It independently multiplies group elements from the defining presentation, tests the square-zero equation on every element in three complete group-algebra instances, and calculates left multiplication ranks by row reduction. It also enumerates all \(2\times2\) matrices over \(\mathbb F_2[t]/(t^4)\) and checks image lengths without applying the decomposition theorem.

Observed successful checks:

- \(\mathbb F_2[Q_8]\): all \(256\) algebra elements tested; square-zero rank counts \((1,1,6,8)\) at ranks \((0,1,2,4)\).
- \(\mathbb F_4[Q_8]\): all \(65{,}536\) elements tested; counts \((1,3,60,192)\) at ranks \((0,1,2,4)\).
- \(M_2(\mathbb F_2[t]/(t^4))\): all \(65{,}536\) matrices tested; image-length histogram \((1,9,78,168,384)\) at lengths \((0,1,2,3,4)\).
- \(\mathbb F_2[G_3]\), where \(|G_3|=24\): all \(16{,}777{,}216\) group-algebra elements tested; square-zero rank polynomial has coefficients \((1,1,15,9,140,78,708,168,2016,384,3648,3072)\) at ranks \((0,1,2,3,4,5,6,7,8,9,10,12)\), for a total of \(10{,}240\) elements.

Final checker line: `QUATERNION_DICYCLIC_CHECK_OK`.

These exhaustive computations verify only the displayed finite instances. The unrestricted theorem depends on the proofs of quadratic étale block splitting, quaternionic square-zero collapse, and the length-four matrix valuation partition; the checker cannot establish all those statements for arbitrary finite-field orders or arbitrary odd \(m\). No independent audit has been performed.
