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
# Reproduction and limitations

Execute `python3 artifacts/verify_petersen.py` from the directory containing these files. It reconstructs the Petersen graph, enumerates all 314,928 faces, checks the deterministic acyclic toggle matching (157,259 augmented pairs), topologically sorts the full 2,099,520-incidence directed Hasse diagram, constructs the signed 77-by-333 critical attaching-degree matrix (235 nonzero entries, maximal absolute value one), and verifies 39 integer unit pivots and a zero residual submatrix. The terminal output includes `PETERSEN_HOMOTOPY_PASS S7_x_38 S8_x_294`.

Execute `python3 artifacts/verify_petersen_counts.py`, a separate standard-library verifier that constructs the graph Laplacian and evaluates its exact characteristic determinant at ten integers using fraction-free elimination. Polynomial uniqueness and the matrix–forest theorem produce the same ten face counts, terminating with `INDEPENDENT_ROOTED_FOREST_COUNT_OK`.

The program uses mathematical identities and exact integer computations. It is not a universal formal proof checker, does not establish a family-wide result, and has not undergone independent external validation. Reproduction is possible using the embedded source alone; no other files or downloaded code are needed.
