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

Run `python3 verify_q4_ind2.py certificate.json` using Python 3.9+ from the directory containing these exact two files. The program needs only Python's standard library. Both files are embedded complete in this package.

The checker builds the four-cube adjacency from bit flips, inspects every vertex mask, independently generates all admissible faces, and checks the face vector \((16,120,464,964,960,440,80,10)\). It recomputes the pivot-sequence matching rather than reading pairs from the certificate, checks that the \(1517\) pairs are legal and disjoint, verifies the twenty critical masks, and topologically sorts the complete directed Hasse graph of \(3054\) faces and \(13{,}568\) incidences. It then computes the signed integral Morse boundaries of the two critical four-cells by exact gradient elimination; their columns are negatives, each with three entries of absolute value one. These exact signed entries are compared to the certificate.

Finally, separate mod-two simplicial boundary elimination computes the full boundary-rank vector \((15,105,359,589,370,70,10)\) and reduced Betti vector \((0,0,0,16,1,0,0,0)\). Successful execution prints `VERIFY_OK` with face, matching and signed-boundary counts.

**Logical scope.** The complete finite matching certifies the integral Morse CW model. The homotopy wedge follows because its sole nonzero signed attaching map is a primitive vector in the free \(\mathbb Z^{17}\) third-homotopy group: one four-cell cancels one three-sphere; the other attaches trivially and yields one four-sphere. The independent mod-two check is a consistency test and is not itself a proof of integral homotopy. No statement about larger hypercubes, all higher-independence parameters or an equivariant decomposition is tested or claimed. An independent scientific audit has not been performed.
