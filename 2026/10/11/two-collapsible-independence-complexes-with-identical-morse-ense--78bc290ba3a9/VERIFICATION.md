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

Run `python3 verify.py` from the directory containing the file (Python 3, standard library only). The successful final line is `VERIFY_OK`. The script independently: (i) checks each displayed edge set is a tree; (ii) constructs each combinatorial Laplacian and computes its entire characteristic polynomial by integer Newton trace identities; (iii) enumerates all 1,024 edge subsets for matching numbers, rejecting vertex collisions; (iv) computes weighted rooted-forest coefficients by a separate 1,024-subset union-find census; and (v) directly backtracks all proper six-label-color assignments on each complementary graph.

Expected exact characteristic coefficient vector in descending order: `(1,-20,169,-788,2223,-3916,4295,-2838,1051,-188,11,0)` for both trees. Expected matching counts in sizes zero to five: `(1,10,34,46,23,2)` and `(1,10,34,46,23,3)`. Expected proper six-colorings: `1440` and `2160`.

The paper's rooted-forest expansion and the elementary clique-partition argument supply the full symbolic proof. The finite computations concern only the two explicit eleven-vertex witnesses and do not establish minimality or a classification of all graph pairs. No independent audit has been performed.
