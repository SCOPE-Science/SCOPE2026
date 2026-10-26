# Scientific review

## Correctness — PASS

The proof uses a complete equitable quotient on coordinate-distance profiles. For every strongly regular factor with parameters \((v,k,\lambda,\mu)\), the five explicit profile-transition counts determine the entire refinement trace. Shells propagate outward from the single marked root. When \(\mu\ne2\), the number of edges into the previous distance shell separates coordinate profiles at the distance's arrival round. When \(\mu=2\) but \(k\ne2\lambda+2\), the same-shell edge count separates them one round later. Exactly when \(\mu=2\) and \(k=2\lambda+2\), the distance partition is equitable and remains unsplit. Sharpness follows since shells at distances \(2d-1\) and \(2d\) remain indistinguishable through round \(2d-2\). The final size formulas use multinomial counting and the standard strongly regular parameter identity.

The standalone tester constructs genuine strongly regular graphs and applies vertex-level 1-WL directly to Cartesian products. All 20 test cases passed. Finite tests do not prove the quantified theorem.

## Originality — PASS, qualified

The nearest verified archive-period literature defines colour refinement and Cartesian/Hamming graphs. Papers on Doob graph distance arrays, extremal general iteration counts and higher-dimensional coherent configurations do not in their inspected material state the precise singly rooted, all-common-parameter strongly regular dichotomy or exact round bound. The old Hamming/Doob distance-regularity facts are acknowledged, and earlier individual Hamming or odd-cycle cases are subsumed rather than reasserted as new. More comprehensive expert literature review may identify earlier equivalent coverage.

## Mathematical value — PASS

The result is a natural classification applying across *all* finite strongly regular factors with matching parameters, including nonisomorphic factors. It gives a sharp global stopping round, an exceptional exact parameter equation and a phase change from linear to quadratic numbers of cells, with all class sizes. Its proof identifies two different local mechanisms through which one-dimensional counting detects coordinate information.

## Limits and nearest literature

Kersting–Mladenov–Garnett–Grohe (2014), Kiefer–McKay (2020), Bespalov–Krotov (2015) and Cai–Guo–Gavrilyuk–Ponomarenko (2024) are compared in the accompanying structured audit and mathematical result. Only partial material from some sources was available or read; exact novelty beyond the inspected sources is not certified. No automorphism-orbit or graph-isomorphism classification is asserted.

Self-review: passed. Independent audit: not yet performed.
