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

Run `python3 verify.py` with a standard Python 3 interpreter. No third-party packages are required.

The verifier performs the following exact checks:

- constructs all \(81\) words in \(\{0,1,2\}^4\);
- computes every one-deletion shadow by two independent definitions and requires equality;
- builds the compatibility graph and checks its \(2370\) edges;
- enumerates maximal cliques by Bron--Kerbosch and independently counts fixed-cardinality cliques in increasing vertex order;
- requires six \(11\)-cliques and zero \(12\)-cliques;
- reconstructs the nine-word core and six outside words;
- verifies that admissible outside pairs form a connected two-regular graph on six vertices, hence a six-cycle;
- checks that symbol permutations and reversal form the stated order-\(12\) action, with one orbit on the six maxima and stabilizer order \(2\);
- checks the common deletion-shadow profile and exact coverage of \(23\) of \(27\) received words.

The finite proof establishes only the stated ternary length-four result. It does not infer behavior at other lengths or alphabet sizes.
