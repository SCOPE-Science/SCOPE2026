# Scientific review

## Correctness — PASS

The complete claim is structural identification on \(a>0\), \(\beta>0\), \(0\le\eta\le1\). The two- and three-person outbreak probabilities follow from independent infectious durations, conditional Poisson contact processes, and a disjoint enumeration of zero and one additional infections. The inverse first determines the two needed Laplace transform values, then uses a strictly decreasing ratio of logarithms to obtain \(\lambda_2/a\), shape, intensity, base rate, and mixing exponent uniquely. Strict convexity of \((1+t)\log(1+t)\) proves the only nontrivial uniqueness step. A nonzero mean-map Jacobian and the implicit-function theorem give an actual local family of confounded medium-resolution parameters at every interior mixing exponent. The strict Gamma variance signal has the claimed Taylor coefficient. Exact rational graph enumeration from an independently constructed directed-edge model corroborates the forward law, and round-trip inversion tests succeed.

## Originality — PASS, qualified by bibliographic risk

The 2026 motivating work supplies the household transmission model, the forward likelihood, and a *qualitative suggestion* that freeing infectious-period shape may make medium-resolution final-size data unidentifiable while high-resolution data could remedy it. That suggestion does not prove a global inverse nor determine the minimum observed household sizes or the dimension of the medium-summary ambiguity. The new claim establishes an explicit inversion and a sharp information-resolution distinction in a specified smallest mixed-size design. Earlier general finite-household final-size formulas (Ball 1986; Miller 2019), and the generalized framework in Ball–Britton–Neal 2025, provide forward distributions and inference context; they do not, in the inspected material, assert the three-parameter global identification result. Search results are not exhaustive evidence of priority. A more general inverse theorem elsewhere could imply this special case, and independent bibliographic verification remains outstanding.

## Mathematical value — PASS

The exact sufficiency/insufficiency threshold addresses a concrete data-reporting decision posed by the motivating household-epidemiology work: when the infectious-period distribution's variability is unknown, is a size-specific secondary attack fraction enough, and what additional outcome statistic must be retained? This theorem answers the question for the first two nontrivial household sizes with exact formulas, explains the obstruction by a positive-dimensional fiber, and distinguishes structural uniqueness from weak-transmission practical ill-conditioning. It does not claim a general theory for all household sizes or non-Gamma distributions. Recovered results are mathematically motivated rather than arbitrary numerical slices.

## Closest sources and risks

- Brooks et al., arXiv:2603.25235, Methods and Discussion including the explicit hypothesis about free Gamma shape: nearest direct source, but not equivalent to the proved global inverse.
- Miller, arXiv:1907.05138, main probability formulas and Section 6 inference: broader forward probability machinery, not the same inverse theorem in the inspected text.
- Ball, Britton and Neal, arXiv:2505.17890, main model and asymptotic theorems: general household framework with distinct objectives.
- Remaining risk: specialized inverse-problem literature or algebraic consequences of older general finite-outbreak theorems may contain the conclusion; mathematical priority is not independently certified.

Self-review: passed. Independent audit: not yet performed.
