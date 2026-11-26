# Independent mathematical audit

## correctness

PASS

For the repaired statement, θy∼v(y) at zero; using the exact density (rather than differentiating an asymptotic equivalence) gives g∼γ(((1+α)θ)/α)^γ y^(γ−1), and 1−G→1. In the tail, with a=α/(1+α) and ε=e^(−θy), the inner CDF factor is (1−ε)/(1−(1−a)ε)=1−aε+O(ε²). Thus 1−G∼γaε and g∼γaθε; all parameters are positive, so division is valid and the limit is θ. The three origin cases follow. Nondecrease cannot start above the finite tail limit, nonincrease cannot start below it, and a positive function with initial limit 0 cannot initially decline; a finite-valued hazard with initial limit +∞ cannot initially rise. This excludes the four prose assignments in α,γ,θ order, including the directions required for standard bathtub and upside-down bathtub shapes. The frozen attribution to Figure 1 labels as if all four prose triples were actually plotted in the hazard panel is inaccurate: p. 6 lists (1.5,1.2,1.5) and (0.5,1.1,1.5) in that panel, and the prose's bathtub triple (1.5,2.8,1.5) belongs to the density-panel legend. The repaired RESULT.md, VERIFICATION.md and slogan distinguish the sources, do not assign an undocumented label to a curve, and prove that both extra hazard-panel triples also exclude an initial decline. An independent bounded mpmath check used u=a/expm1(θy) and I=expm1(γ log1p(u))/(γu), evaluating h/θ=(a+u)/(a(1+u)I) on the four prose triples; at θy=10^−90 and 80 the relative errors against the two laws were below 10^−8 and 10^−30 respectively. The original checker was inspected only. No claim is made about all interior turning points or the original plotting code.

## originality

PASS

Credit the repaired, model- and paper-specific correction of four explicit hazard claims, not novelty of the distribution family, power transform, or elementary endpoint method. The original paper supplies the formulas that prove the limits but assigns the opposite global behaviors to the four examples; distinguishing the prose assignments from the plotted legend is part of the verified comparison. No inspected source already makes the four-way correction.

## value

PASS

The repaired result gives a concrete reliability correction: all four explicit illustrative assignments violate analytic endpoint behavior, with the figure/prose discrepancy kept separate instead of silently treating the labels as matching. It also provides a parameter-wide necessary test for future shape claims and identifies the universal tail rate. Its value is the falsification of these advertised global behaviors, not the routine asymptotic calculation in isolation or a claim to a full shape diagram.

The dated certificate retains the supplied scientific assessment, sources and limitations.
