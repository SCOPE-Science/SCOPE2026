# Same-model review

## Correctness

PASS. Conditioning on a common exponential breakthrough-infection clock gives the exact immunization-before-infection probability \(\mathbb E[e^{-hT}]\). Strict Jensen convexity proves the deterministic fixed-time lower bound for every nonnegative waiting law with mean \(T_*\), with equality only for deterministic waiting. The exponential and fixed-time formulas, the steady exit fluxes, and the waiting-stock formulas follow exactly. The bundled script checks the explicit formulas and representative nondegenerate distributions, but the infinite-family claim rests on the analytic Jensen proof rather than finite experiments.

## Originality

PASS. The 2022 source explicitly juxtaposes the ODE and transport mechanisms and says their direct comparison is highly arbitrary because \(\vartheta_V\) and \(T_*\) lack counterparts. It does not use the natural mean calibration \(\vartheta_V=1/T_*\), derive the fixed-versus-exponential ordering, or state the stronger deterministic extremum over all mean-matched waiting laws. The 2008 antecedent and 2017 vaccination-age model are closely related but their inspected records do not imply this calibrated result. General phase-type literature makes exponential waiting in Markov stages standard, so that general fact is not claimed as new.

## Value

PASS. The theorem addresses a modeling ambiguity highlighted by the primary source. It quantifies a systematic direction of bias after the most natural calibration and shows the fixed-time model is an extremal benchmark, with an unbounded relative gap in successful-immunization throughput as \(hT_*\) grows. This can affect how ODE vaccination compartments are calibrated against known biological immunization times.

## Closest literature and limitations

The primary comparison is Colombo, Marcellini, and Rossi (2022), DOI 10.3934/nhm.2022012. The ODE antecedent is Liu, Takeuchi, and Iwami (2008), DOI 10.1016/j.jtbi.2007.10.014. Vaccination-age structured SVIR dynamics are treated by Wang, Guo, and Liu (2017), DOI 10.1093/imamat/hxx020. The latter two were not available as complete open full text in the inspected sources, so a residual literature risk remains. The mathematical statement itself is restricted to constant infection hazard and, for stock/flux formulas, constant inflow; it does not order fully coupled epidemic trajectories.

Same-model review: passed. Independent audit: not yet performed.
