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
# Finite verification and mathematical scope

Run `python3 verify.py` in a directory containing this document and `verify.py`, using Python 3.8 or later and no third-party packages. The program exhaustively examines every nonempty labeled graph on one through six vertices, a total of 33,861 edge-subset cases. It independently constructs 2,996 explicit edge-girth-four witnesses, for four edges and then every edge count from six through three thousand, and checks each edge in each witness for a simple quadrilateral. It also checks connectedness, absence of triangles, vertex and edge counts, and the bound on missing matching edges. Its checked output is included in `VERIFY_OUTPUT.txt`.

The mathematical proof is finite in description but universal in parameters; it does not rely on the finite computation to establish the formula for arbitrarily large edge counts. The excluded five-edge count is ruled out by the impossibility of two different four-cycles sharing three edges, not by computer enumeration. No external independent validation has been performed.
