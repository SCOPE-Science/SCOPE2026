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

Run `python3 verify.py`. The script uses exact integer arithmetic for the intersection matrices and NetworkX only to exhaustively enumerate automorphisms of the finite weighted graph. It reconstructs all nineteen vertices and twenty graph edges, including the two multiplicity-two edges, and verifies that the weighted graph has exactly four automorphisms. Exactly one automorphism both swaps \(a_1\) with \(b_4\) and preserves the two \(I_2\) component pairs individually; the script checks that this map is the permutation stated in the finding and that its only fixed vertex is \(a_7\).

The script then forms the nineteen-by-nineteen curve-intersection matrix, checks rank \(16\), forms the nine difference vectors, verifies their primitive relation with coefficient vector \((4,6,8,6,4,2,4,1,1)\), and checks that deleting \(d_9\) gives an eight-by-eight Gram determinant \(1024=2^{10}\). Comparing with the standard determinant \(256=2^8\) of \(E_8(-2)\) gives index \(2\).

The finite computation does not prove the source's geometric premises or the general Nikulin theorem; those are cited separately. It certifies the exact consequences of those premises used here.
