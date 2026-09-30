# Independent audit — 2026-09-30

Record: `2026/09/19/three-consecutive-derivative-threshold-inner-diameter--48c31c20d4bf`  
Assigned and audited source tree: `22a263f26822bc665c13ba9a0b48b85152f657f6`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `55b9dcb3c1b020c260d2e550d304213a2842e730`  
Disposition: **passed**

## Correctness

**independently_supported**. The positive direction is immediate once MacMahon's finite-inner-diameter Rubel_0(2) theorem is applied to h=f^(a): bounded f^(a) would integrate downward along uniformly short interior paths and force f bounded, so h is unbounded and h,h',h'' diverge along one sequence. The negative construction works for every gap m=b-a>=3: the quadratic interior pieces have zero m-th derivative, while the cutoff strips have uniformly small function value. After a-fold integration the function remains unbounded because each interval contributes a positive constant order to the limiting weighted integral. Whitney analytic approximation preserves derivatives through order b, and a sufficiently thin variable-width complex neighborhood preserves the two-derivative separation while remaining simply connected with uniformly bounded interior path diameter. Thus any index set of span at least three is obstructed and every set contained in three consecutive orders is forced.

## Originality

**qualified_with_inaccessible_legacy_source**. MacMahon's September 2026 paper proves the first two Rubel levels coincide for the relevant geometry and constructs the {0,3} separation, but its public summary does not state the arbitrary derivative-set threshold or all-gap pairwise construction. Targeted searches found no equivalent exact selected-derivative theorem. Rubel's 1984 paper is the most relevant legacy source; lawful open-access searches did not expose its full text, and an authorized Oxford retrieval attempt returned no verified paper, so it is not claimed to have been read. The originality assessment is therefore qualified and limited to the exact universal derivative-set threshold.

## Scientific value

**meaningful_exact_threshold**. The theorem turns the source's first separation at derivative order three into a complete universal classification of which finite or infinite derivative index sets are forced by finite interior path diameter. It identifies a sharp span-two boundary and shows the obstruction is not special to {0,3}.

## Literature and evidence checked

- https://arxiv.org/abs/2609.20607
- https://doi.org/10.2307/1989708
- https://doi.org/10.1112/S002557930001490X
- https://doi.org/10.1090/S0002-9939-1994-1204374-0
- Rubel, Unbounded analytic functions and their derivatives on plane domains, Bull. Inst. Math. Acad. Sinica 12 (1984), 363–377 (full text not located)
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/19/three-consecutive-derivative-threshold-inner-diameter--48c31c20d4bf
## Literature access note

Rubel (1984), Bull. Inst. Math. Acad. Sinica 12, 363–377: No lawful readable full text located by exact-title and bibliographic searches. Authorized Oxford retrieval was attempted after OA failure but returned an unavailable/invalid worker response; no verified PDF was obtained. The source is **not** claimed to have been read in full.

## Limitations

- The theorem classifies only the universal statement over simply connected domains of finite interior-path diameter, not an arbitrary fixed domain.
- The counterexample domain depends on the obstructed derivative pair; no single domain is shown to realize all gaps.
- No quantitative divergence rates are obtained.
- Rubel (1984) could not be inspected in full after open-access and authorized institutional attempts and remains an explicit attribution risk.
