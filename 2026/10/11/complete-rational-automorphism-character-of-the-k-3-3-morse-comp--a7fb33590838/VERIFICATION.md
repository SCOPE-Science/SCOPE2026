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

The self-contained `verify.py` uses Python 3 standard libraries only. It performs two exhaustive face enumerations of the ordinary Morse complex of \(K_{3,3}\), one by the six vertex options and one by nine edge states. Each checks unique used vertices, unique used edges and absence of directed cycles. Both produce \(1791\) nonempty simplices with face vector \((18,126,432,729,486)\). It constructs every augmented boundary matrix over \(\mathbb F_2\) and obtains rank vector \((1,17,109,323,406)\). The proof in `RESULT.md` explains why the same rational ranks follow from chain-complex upper bounds, rather than assuming they equal finite-field ranks.

The verifier enumerates every \(72\) graph automorphism, computes each signed simplex trace, independently checks the same traces by counting cycles of the induced permutations on fixed faces, and checks that the resulting character is constant on every conjugacy class. It tests all nine candidate rational irreducible characters for orthonormality, checks that their squared dimensions total the group order, and calculates their exact multiplicities. The diagnostic output ends with `VERIFY_OK`.

The result is a complete finite exact calculation; it neither supplies a general formula for larger bipartite graphs nor establishes publication novelty with certainty. No independent audit has been performed.
