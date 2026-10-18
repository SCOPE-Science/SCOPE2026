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

The standalone `verify_prism_morse.py` uses only Python's standard library and has no external files or environment dependencies. Execute `python3 verify_prism_morse.py`.

The program independently generates all simplex masks through rooted-forest recursion and exhaustive edge-state assignments, checks the accepted sets agree, and verifies the exact face vector. For the fixed incidence-bit order in the result, it constructs and checks \(832\) disjoint matching pairs and identifies exactly \(64\) critical degree-four masks. It enumerates all \(6624\) cover incidences, reverses matched covers, and proves acyclicity by processing every directed-graph vertex in Kahn's algorithm. Since all loops range over finite, explicitly bounded sets, passing these assertions is an exhaustive check, not a sample. These verified facts imply the wedge-of-spheres homotopy type using the standard discrete Morse theorem.

A second exact computation in the same program performs Gaussian elimination over \(\mathbb F_2\) on the simplicial boundary matrices and obtains ranks \((17,109,319,386)\). This check is independent of the matching logic but is not a substitute for the acyclicity assertion.

The result depends on the established identification \(\mathcal M(\partial\Delta^2)\cong C_3\square K_2\) and on the standard discrete-Morse CW theorem. Nothing here certifies other graphs, higher iterates, independent reproducibility, or originality against unindexed literature.
