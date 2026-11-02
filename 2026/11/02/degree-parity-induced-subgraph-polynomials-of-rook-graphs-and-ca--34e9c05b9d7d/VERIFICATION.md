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

# Verification record

The ordinary standard-library script `verify.py` can be run with `python3 verify.py` in a folder containing the script. It constructs adjacency for each rook graph independently of the incidence-matrix formula, enumerates all vertex subsets, and determines whether every selected vertex has odd or even degree in the induced graph. This includes the vacuously admissible empty set in both counters.

It compares exact coefficient dictionaries with an independently written parity-constrained binary-matrix enumerator on 19 general rook graphs having up to 12 vertices, and with a two-row combinatorial counter on prisms with up to 20 vertices. Altogether it directly checks 1,412,734 vertex subsets. The Fourier projection is separately expanded coefficientwise and compared against 64 tiny binary-matrix cases, and the two closed supports are checked through 60 columns.

Observed output:

`VERIFY_OK general_graphs=19 prism_graphs=10 direct_vertex_subsets=1412734 fourier_blocks=64 symbolic_support_orders=60`

Proof dependencies are the degree equality \(\deg_{R[S]}(i,j)=d_i+e_j-2\), the unique parity partition of rows and columns, the roots-of-unity parity projection, and the two-row full-pair/disjoint-row dichotomy. Each is derived in `RESULT.md`. These finite checks are corroboration and do not certify the infinite theorem or publication priority. No independent audit has been performed.
