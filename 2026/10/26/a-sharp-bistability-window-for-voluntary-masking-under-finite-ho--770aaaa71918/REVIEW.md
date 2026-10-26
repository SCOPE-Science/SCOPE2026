# Self-review

## Correctness — PASS

The population game uses a Poisson probability of one or more events, \(1-e^{-\lambda a m(p)}\), not the bilinear approximation. The utility difference is exactly \(\ell[e^{-\lambda q m(p)}-e^{-\lambda m(p)}]-c\). Differentiation gives the unique peak \(m_*=\log(1/q)/[\lambda(1-q)]\). Restricting that peak to the feasible interval \((q,1)\) and comparing the strict endpoint and peak levels proves necessity and sufficiency of the entire cost/exposure window. The orientation of the two interior crossings verifies the stated replicator stability. The rational witness is independently factored into \((y-7/16)(y-9/16)\); its roots lie inside the real exposure interval. The attached code ran successfully. The universal claim does not rely on the finite parameter sample.

## Originality — PASS, with limitations

The 2022 Altman–Datar–de Pellegrini–Perlaza–Menasché paper provides a bilinear infection-rate game, while its Appendix A.6 mentions Poisson daily contact counts and expressly leaves nonlinear game analysis open. Its spatiotemporal alternative in Appendix A.5 is a different kernel from the event-count model solved here. Kabir–Risa–Tanimoto (2021) uses coupled epidemiological dynamics and social-conformity effects; Yang et al. (2022) models institutionally and socially driven tipping; Qiu et al. (2022) uses peer-pressure and fear-threshold contagions. Their reported tipping mechanisms do not imply the sharp cost window for the frozen-prevalence, homogeneous, no-conformity Poisson game. Published semantic-record searches also did not retrieve a covering statement. The 2025 Pei–Xu–Zhang networked mask-game abstract was inspected, but its complete article remained inaccessible; its precise relationship is an unresolved bibliographic risk rather than an assertion of noncoverage.

## Mathematical value — PASS

The result is a complete structural bifurcation classification for a motivated, minimally nonlinear infection-risk replacement of a published bilinear mask game. It shows that probability saturation alone can create bistability, with no risk-type asymmetry, norm conformity, or endogenous epidemiological feedback, and identifies the exact nonempty region where two interior Nash fractions occur. The explicit rational-exponential witness distinguishes the saturation mechanism from the linearized game's strictly decreasing advantage. This is a general parameter-family statement rather than an arbitrary numerical instance.

## Closest literature and limitations

See Altman et al. (2022), Appendix A.5–A.6; Kabir et al. (2021), behavioral and infection model; Yang et al. (2022), norm-driven game; Qiu et al. (2022), multilayer behavioral contagion; and Pei et al. (2025), network-mask abstract only. Strictly fixed Poisson thinning, nonatomic symmetric adoption, risk-neutral payoffs, and the specified replicator dynamic are essential scope restrictions. A specialist check of related full-text work is still needed.

Self-review: passed. Independent audit: not yet performed.
