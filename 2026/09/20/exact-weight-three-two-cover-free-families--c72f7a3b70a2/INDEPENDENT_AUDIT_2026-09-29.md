# Independent Audit — 2026/09/20/exact-weight-three-two-cover-free-families--c72f7a3b70a2

- Audit date: 2026-09-29 (UTC) (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `d0f02030a2a9540b36b34e1daa1e743780ad1357`
- Disposition: **PASSED**

## Correctness

**PASS** — The repeated-pair reduction is correct. If a pair xy lies in s>=2 triples xyz_i, then each z_i has degree one: if a second block C contains z_i, the block xyz_i is contained in C union xyz_j for any j!=i, contradicting 2-cover-freeness. Deleting the s private vertices z_i leaves a 2-cover-free 3-uniform family on v-s points, so |F|<=s+F_3(v-s). A linear triple system is automatically 2-cover-free, because a third triple contained in the union of two others would have to share two points with one of them. Thus the classical maximum 2-(v,3,1) packing number D(v,3,2) gives the lower bound. The stated packing formula has D(m+2)>=D(m)+3 and D(m+1)>=D(m)+1 for m>=6; induction therefore makes every repeated-pair family strictly smaller than D(v,3,2) for v>=7. The direct small cases give F_3(3),F_3(4),F_3(5),F_3(6)=1,2,3,4, with the submitted v=6 four-block fan showing that maximum families need not be linear at the boundary. Independent exhaustive enumeration reproduced the values for v=3,4,5,6.

## Originality

**PASS** — The directly relevant 2006 Li-van Rees-Wei paper was retrieved through authorized access after open-access attempts failed. Its review of the Erdős-Frankl-Füredi uniform results states only T_3(2,v)=T_4(2,v)=v^2/6+O(v), while its exact Section 6 work concerns unrestricted 2-cover-free families on small point sets; it does not give the submitted exact weight-three all-v classification or the v>=7 linearity theorem. Yu-Wang-Ji (2025) optimize sparse disjunct matrices under row-weight constraints and give only asymptotic column-weight bounds in the relevant range. Targeted searches found no prior exact theorem matching the submitted formulas. The classical packing numbers themselves are, of course, prior design theory.

## Scientific value

**PASS** — The theorem turns the asymptotic weight-three cover-free problem into a complete exact classification and shows that, from v=7 onward, extremality is exactly the classical partial-Steiner-triple packing problem. The exceptional nonlinear v=6 optimum also identifies the sharp structural threshold. This is a useful bridge between cover-free families/group testing and exact packing theory.

## Sources

- **Families of finite sets in which no set is covered by the union of two others** — Paul Erdős; Peter Frankl; Zoltán Füredi. https://doi.org/10.1016/0097-3165(82)90004-8 — Classical 2-cover-free-family source; its uniform weight-three result is asymptotic rather than the audited exact all-v classification.
- **Constructions of 2-cover-free families and related separating hash families** — P. C. Li; G. H. J. van Rees; R. Wei. https://doi.org/10.1002/jcd.20109 — Authorized full text checked (Oxford job 99434e805fec87c8be37013d4caff92b), especially pages 2-3 and the small-family discussion.
- **Constructions of Optimal Sparse r-Disjunct Matrices via Packings** — Liying Yu; Xin Wang; Lijun Ji. https://doi.org/10.1002/jcd.21986 — 2025 sparse-disjunct-matrix comparison; exact results use row-weight restrictions, while limited-column-weight results are asymptotic.

## Limitations

- Only 3-uniform 2-cover-free families are classified; higher uniform weights and r-cover-free families are not addressed.
- The exact packing-number formula is classical prior art; novelty is the reduction and extremal-structure classification for cover-free families.
- The proof is elementary once the repeated-pair lemma is seen, so folklore or an equivalent design-theoretic formulation remains a residual priority risk.

## Independent checks

```json
{
  "repeated_pair_lemma_reconstructed": true,
  "packing_formula_and_induction_increments_checked": true,
  "small_v_exhaustive_values": {
    "3": 1,
    "4": 2,
    "5": 3,
    "6": 4
  },
  "li_van_rees_wei_full_text_checked": true,
  "oxford_job_id": "99434e805fec87c8be37013d4caff92b",
  "oxford_pages_checked": "1-12 of 18, with the relevant prior-results discussion on pages 2-3",
  "open_access_first": true,
  "oxford_used": true
}
```

The assigned source tree was unchanged between the inventory commit and the source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation or separate dispatcher report was performed. Open-access/preprint sources were checked before institutional retrieval, and inaccessible material is explicitly identified rather than inferred.
