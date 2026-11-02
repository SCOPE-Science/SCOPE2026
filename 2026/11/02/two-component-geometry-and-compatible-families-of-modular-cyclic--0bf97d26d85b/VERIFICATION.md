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

# Verification of the finite-field checks

The reproducible, standard-library-only command is `python3 verify.py`. `verification_output.txt` records its exact output.

The checker represents the algebra using the original multiplication table of \(k[t]/(t^4)\) and tests the original Rota–Baxter identity on all sixteen ordered pairs of basis elements. In \(\mathbb F_2\), it exhausts every one of the \(2^{16}=65536\) linear endomorphisms without presupposing the normal form, accepting 24; the rank distribution is \((1,13,10)\), and four operators have index three. It tests all 576 ordered pairs of accepted operators, finding 448 compatible ones, and all 13824 ordered triples, finding 7680 compatible ones.

For \(\mathbb F_4\), the checker independently implements extension-field multiplication using the irreducible polynomial \(z^2+z+1\). It exhaustively tests all \(4^8=65536\) linear maps whose images belong to the proven forced square-zero ideal; 448 satisfy the defining identity, with rank distribution \((1,123,324)\) and 144 index-three operators. The rank and compatibility comparisons use the explicit theoretical formulas. Finite checks do not replace the proof over all characteristic-two fields and all tuple lengths.

The source and recorded output are complete files contained in the same package. No external certification, independent mathematical audit or formal proof assistant validation was performed.
