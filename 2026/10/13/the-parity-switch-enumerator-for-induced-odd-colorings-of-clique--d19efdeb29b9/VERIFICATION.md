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

# Direct verification and reproducibility

Extract `verify_induced_odd_clique_corona.py` and `verify_induced_odd_clique_corona_output.txt` beside this document and execute `python3 verify_induced_odd_clique_corona.py` using a standard Python 3 installation. No third-party modules or datasets are required. The script terminates only after all assertions succeed and prints `VERIFY_OK`.

The code directly enumerates \(4,467,792\) assignments of named colors on \(99\) small clique-corona instances; it checks every vertex's number of same-color neighbors rather than using the claimed factorization in the direct count. It independently computes the local hyperbolic-series factors from multinomial coefficients and directly enumerates local leaf-color assignments for \(1\le r\le5\), \(1\le q\le4\). On all \(1,099\) labeled graphs of orders \(1\) through \(5\), the one-color boundary and binary equations match direct enumeration; the six-cycle is checked as a graph with no induced-odd two-coloring but with three colors available.

The complete infinite proof is in `RESULT.md`. Finite tests do not establish the theorem for all graph sizes, all palettes, or all clique sizes, and they do not demonstrate historical novelty. The independent audit status in the front matter intentionally remains `not_performed`.
