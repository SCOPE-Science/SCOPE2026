# Research assessment

## Correctness

**PASS.** The original graph-specific mean-field fixed-point equations are explicitly stated. Stationarity forces susceptible fractions positive at every vertex and connectivity propagates any nonzero strain to every vertex. The leaf-symmetry lemma requires no symmetry hypothesis: the same strictly increasing one-variable equation must hold at each leaf. The star/clique equations yield exact susceptible fractions; a nonsingular \(2\times2\) system yields the unique candidate infection fractions. The signs of two explicit rational expressions give the necessary inequalities, and strict positivity of the susceptible and infected fractions is independently verified to be sufficient. The boundary equalities are excluded without inferring anything unsupported about non-coexistence equilibria. Symbolic identities and \(25,872\) exact-rational instances reproduce the original equations; finite checks are not used to prove the infinite statement.

## Originality

**PASS, subject to literature-access risk.** The 2014 general multilayer survival-threshold analysis, the 2021 general coexistence/global convergence work, and the 2022 general quantitative bounding results concern the same model. The 2022 paper explicitly suggests analysis of star topologies as future work. Those general theorems already encompass the qualitative possibility of coexistence, which is *not* presented as new. The distinct resolved question here is the non-implicit, all-vertex closed form and complete sharp region for star-vs-clique overlays of every size, including a proof ruling out nonsymmetric coexistence. The closest 2022/2023 general equilibrium-count paper addresses different questions and does not print this explicit solution. An equivalent unindexed specialization remains possible; bibliographic exclusion is not mathematically absolute.

## Mathematical value

**PASS.** The explicit center/leaf endemic levels and the sharp interval \(\sqrt m<a/b<[m-1+\sqrt{(m-1)^2+4}]/2\) quantify an epidemiologically motivated contact-topology asymmetry. This is an infinite family, not an arbitrary tiny numerical slice; it answers a topology singled out by quantitative bi-SIS literature. The complementary strength cutoff specifies the full region in which both infections can be jointly positive, rather than a spectral bound or numerical plot. Does not establish global convergence or stability.

## Closest sources and limitations

Sources: Sahneh–Scoglio (2014), DOI 10.1103/PhysRevE.89.062817; Doshi–Mallick–Eun (2021), arXiv:2104.10872; Doshi–Hu–Eun (2022), arXiv:2209.07304; Liu et al. (2019), arXiv:1901.00765; Anderson–Ye (2022), arXiv:2210.11044. The analysis excludes arbitrary irregular/directed layers, rate heterogeneity, boundary equilibrium classification, basins and finite stochastic epidemic behavior. Additional unindexed equivalents cannot be excluded.

Self-review: passed. Independent audit: not yet performed.
