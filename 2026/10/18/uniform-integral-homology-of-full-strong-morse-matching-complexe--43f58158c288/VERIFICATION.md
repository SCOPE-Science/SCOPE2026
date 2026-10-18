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

The standalone `verify_strong_cycle_homology.py` needs only Python 3. Run it in the same directory as this file. Its observed final line is `VERIFY_OK`.

Checks performed: all vertex-order-induced matching faces against the independent cyclic-word criterion for \(3\le n\le8\); the precise forbidden monochromatic vertex-cover condition; mod-two boundary-rank homology in every degree for \(6\le n\le9\); complete acyclic element-matching critical-cell counts for \(\operatorname{Ind}_2(C_n)\), \(6\le n\le22\), and \(\operatorname{Ind}_1(C_n)\), \(6\le n\le16\); and evaluation of the 22-cycle formula. In addition, the computed group formula agrees with the tabulated homology in Knudson–Owens-White [1, Table 1] for all \(6\le n\le21\).

No direct exhaustive boundary-matrix reduction of the 22-cycle's strong matching complex was attempted; its number of faces is too large for that to be a reasonable prerequisite. Its integral groups instead follow from the symbolic relative-chain decomposition, simplicial nerve lemma, integral Alexander duality, and the published all-cycle higher-independence homotopy theorems as detailed in `RESULT.md`. Finite-field homology or a finite acyclic matching is not, by itself, a proof of an infinite parameter theorem or absence of torsion. No independent external review has occurred.
