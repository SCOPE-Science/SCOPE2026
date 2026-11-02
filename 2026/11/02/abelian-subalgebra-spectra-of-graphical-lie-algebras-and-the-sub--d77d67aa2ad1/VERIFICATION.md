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

# Verification details

Run `python3 checks/check_abelian_graph_lie.py` from the directory containing the extracted files. Only the Python standard library is required. `checks/OUTPUT.txt` records the executed result. The script independently lists every reduced-row-echelon subspace over selected finite fields; checking its edge-bracket minors does not rely on the polynomial formula it tests. For small graphs it also enumerates all abelian Lie subalgebras in the full vertex-plus-edge algebra, testing the graph-lift formula.

The finite-field arithmetic includes the genuine four-element extension field with irreducible relation \(u^2+u+1=0\). It tests all labeled simple graphs with at most four vertices over \(\mathbb F_2\), additional paths and triangles over \(\mathbb F_3\) and \(\mathbb F_4\), and one isolated-vertex example over \(\mathbb F_5\), for 84 graph-field configurations. It also verifies the polynomial-evaluation triangular inverse and the recurrence for path component polynomials over several integer parameter choices. The scripted test prints `GRAPH_LIE_ABELIAN_SUBALGEBRA_CENSUS_OK 84`.

Mathematical validation does not rely on finite enumeration: the edge minors, projective component lines, lattice Möbius inversion, free ordered-basis quotient, central lift count, and polynomial interpolation are proved in `RESULT.md`. There is no computer algebra package, undisclosed input or downloaded full-paper dependency. The checks do not establish an independent audit or exhaustive novelty.
