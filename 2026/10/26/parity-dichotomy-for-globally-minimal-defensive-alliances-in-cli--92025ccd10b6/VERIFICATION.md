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
# Reproducibility and evidence

The theorem is established by the symbolic proof in `RESULT.md`. For independent finite corroboration, run `python3 verify.py` with Python 3.9 or later. `verification_output.txt` is the recorded exact output.

The verifier forms the original adjacency relation for a clique bouquet and directly checks the condition \(2\deg_S(v)+1\ge\deg(v)\) for selected vertices. It enumerates all nonempty subsets of each test graph. A defensive set is globally minimal exactly when it does not contain any earlier defensive set, because every nonempty proper subset has a smaller bit-mask integer value. The implementation constructs such a reference family and separately constructs the predicted two families; it tests equality of the resulting vertex sets and coefficients.

Checks cover 21 selected parameter tuples, all two or more cliques of orders at least two, representing 18,891 nonempty subsets. The tests include both one-or-fewer-odd and multiple-odd cases, unequal blade sizes, and four-blade instances. This exhaustively verifies the tested *finite* graphs only; no such finite test proves the arbitrary-parameter theorem.

The proof's only arithmetic steps are the exact peripheral threshold, the center requirement \(K\ge \lfloor R/2\rfloor=T+\lfloor o/2\rfloor\), and the global-minimal suballiance exclusion; these are reproduced in `RESULT.md`. There is no unresolved computational dependency.
