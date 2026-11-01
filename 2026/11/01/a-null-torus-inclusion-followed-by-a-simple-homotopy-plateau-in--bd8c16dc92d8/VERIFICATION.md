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
# Verification of Paley-13 higher-independence filtration

Run `python3 check_paley13.py CERTIFICATE.json` using Python 3 standard library only. This directly checks that the certificate's quadratic residues construct the intended six-regular Paley graph on 13 vertices, then compares graph-search and union-find membership tests for all 8,192 subsets at each cutoff.

It finds 79, 313 and 677 faces including the empty face at cutoffs 1, 2 and 3. It checks all orientable-surface link conditions and a nonzero oriented 26-triangle fundamental 2-cycle for the first stage; it confirms the exact integral boundary identity between that cycle and a 26-tetrahedron chain of the second stage.

The 313-face second stage has an explicit acyclic ordinary discrete-Morse matching of 154 pairs, with critical cells in dimensions 0, 2, 3, 3. The checker topologically sorts all 312 nonempty faces and 897 directed Hasse incidences and obtains exact signed 3-to-2 Morse boundary coefficients \((0,0)\). The 677-face third stage undergoes 182 verified free-face collapses to precisely the second stage. Independent simplicial ranks over \(\mathbb F_2,\mathbb F_3,\mathbb F_5\) match the stated integral homotopy types.

The checker is an executable finite certificate, not an external certification service or substitute for the mathematical arguments linking zero attaching degrees to wedge decompositions and the explicit 2-cycle filling to nullhomotopy. The findings apply only to the specified fixed graph and cutoffs. No independent audit has been performed.
