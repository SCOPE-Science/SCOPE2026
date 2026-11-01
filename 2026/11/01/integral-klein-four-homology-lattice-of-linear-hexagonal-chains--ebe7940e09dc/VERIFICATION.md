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

# Reproducibility and boundaries

Run `python3 verify_hex_lattice.py` with Python 3 and no third-party packages. The program exactly enumerates faces of the linear hexagonal chains for \(1\le n\le5\), forms the simplicial boundary maps over \(\mathbb F_2\), constructs quotient homology bases, and checks the ranks of \(h-I\) and \(v-I\). Its separate recursion and brute-force quotient-graph tests verify the end-reversal fixed-point counts. It checks that the alternating-rung simplex is maximal through \(n=14\).

Observed output ends with:

`VERIFY_OK: 40 transfer checks; 7 independent orbit enumerations; 14 primitive facets; 5 exact mod-2 homology action checks`

The argument for every \(n\) is the five-part proof in `RESULT.md`, notably its finite-dimensional free-relative-cell hyper-Tor calculation and integral rank-two involution classification. Experiments alone do not imply the infinite claim. The published nonequivariant homotopy type is a separately attributed prerequisite; this package does not independently reprove that external theorem. Independent mathematical audit is not performed.
