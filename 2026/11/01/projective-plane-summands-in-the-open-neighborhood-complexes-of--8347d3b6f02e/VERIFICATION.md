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

Run `python3 verify_neighborhood.py` using the Python 3 standard library. The program builds the exact adjacency sets, checks the explicit two-permutation incidence isomorphism, independently enumerates all \(2^{16}\) possible vertex subsets, constructs all matchings, tests the orientation of every Hasse incidence for acyclicity, and recursively computes integral signed Morse boundaries. It cross-checks the resulting homology by separately constructing the full simplicial boundary matrices over \(\mathbb F_2\) and \(\mathbb F_3\).

The two nonempty complexes each contain \(808\) faces with dimension vector \((16,120,320,240,96,16)\), and each has \(375\) acyclic matching pairs. The unique critical one-cell supports an integral boundary coefficient set \(\{0,-2,+2\}\) from the critical two-cells with gcd exactly two. The Shrikhande counts are \((-2:4,0:39,+2:13)\), and rook counts \((-2:9,0:38,+2:9)\). Both direct field computations give Betti vectors \((1,1,56,0,0,0)\) over \(\mathbb F_2\) and \((1,0,55,0,0,0)\) over \(\mathbb F_3\).

The executable proof is finite and complete for these two labeled graphs. It is not a certificate of novelty, of similar behavior for larger graphs, or of an equivariant homotopy decomposition. The exact integer Morse coefficients are necessary: mod-prime ranks alone would not establish the \(\mathbb{RP}^2\) attaching map.
