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

# Mathematical and reproducibility verification

The unrestricted assertion is proved symbolically in `RESULT.md`. Its essential equivalence is
\[
x\notin D_{\omega}(A)\quad\Longleftrightarrow\quad X\setminus A\in\mathcal F_x
\]
for every point \(x\) with all neighbourhoods infinite, followed by the ultrafilter complement law. Neither finite enumeration nor any external computer certificate proves the unrestricted theorem.

Execute `python3 verify.py` with Python 3 and no third-party packages. The script enumerates all proper filters on finite labelled carrier sets of sizes one through five; on a finite carrier every such filter has a unique nonempty generating kernel. For each filter it tests all ordered pairs of subsets for additivity of the positive-set predicate and the equivalence between meet preservation and singleton generation. Expected aggregate: 57 filters, 36,084 ordered-pair tests, PASS. These finite filters are *abstract analogues*, not finite models with nonempty \(\omega\)-accumulation (there are none).

The first-countability failure is checked by a purely mathematical selection of two disjoint sequences through a nested neighbourhood base; the countable Hausdorff example depends on a free ultrafilter, whose existence is assumed in ZFC. Verify the Hausdorff and clopen-neighbourhood conditions directly as displayed in the proof. There is no claim of independent certification or of a finite computational proof of the free ultrafilter's existence.
