# Independent audit — 2026-09-30

Record: `2026/09/19/rational-robust-bezout-witnesses-for-simplices--80f476e5c442`  
Assigned and audited source tree: `8c6911b425f406b780aef0815451a3fb26793699`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `936c3fe3db19f4fd65f256b3e99c58bd8f5bcf90`  
Disposition: **passed**

## Correctness

**independently_supported**. The continuity and certification argument is correct. If A_j→A and B_j→B in Hausdorff distance and A,B have a common interior point, contracting A∩B toward a common interior ball gives a uniform support-function margin; uniform convergence of support functions then places the contracted points in A_j∩B_j, while compactness gives the reverse outer limit. For x in int(K-K), int K intersects int(K-x), so this lemma proves joint Hausdorff continuity of K∩(K-x). The segment map, volume, and mixed volume are continuous, hence the displayed defect is jointly continuous on the incidence domain. Langharst–Wang's special-pair characterization supplies at least one strict positive defect for every non-simplex; openness then gives a nonempty open witness set, a rational point in it, and a positive margin stable under small Hausdorff perturbations. The countable Q^n test-bank equivalence follows immediately. The unit-square check independently gives defect s^2/4>0 with the stated sign.

## Originality

**qualified_short_consequence_of_recent_characterization**. Langharst–Wang's September 2026 theorem is the substantive simplex characterization and is fully prior. Targeted searches did not locate the rational/countable test-bank formulation, open strict-witness set, or one-shift Hausdorff robustness statement in the current public source or neighboring literature. These conclusions are, however, short topological consequences of the new special-test theorem plus standard Hausdorff/mixed-volume continuity, so the originality claim is accepted only at that refinement level.

## Scientific value

**useful_robust_countable_certification**. The result converts a continuum universal test into a fixed countable certification system and shows that failure is open and perturbation-stable rather than exceptional. That is useful for discretized or sampled testing, while correctly making no uniform margin or detection-probability claim near the simplex locus.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/19/rational-robust-bezout-witnesses-for-simplices--80f476e5c442
- https://arxiv.org/abs/2609.20380
- https://doi.org/10.1093/imrn/rnv390
- https://arxiv.org/abs/1801.02675
## Limitations

- The result depends on Langharst–Wang's characterization and is not an alternative proof of the Bézout simplex theorem.
- No dimension-only lower bound is obtained for witness-set measure, violation margin, sampling probability, or stability radius.
- The intersection-continuity argument uses interior difference-body shifts; no boundary-shift extension is claimed.
- The motivating preprint is very recent and the refinement is short, so parallel observations may be unindexed.
