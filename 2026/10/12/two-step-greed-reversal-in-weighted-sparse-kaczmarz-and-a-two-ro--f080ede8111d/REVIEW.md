# Scientific review

## Correctness — PASS

The claimed algorithm is the inexact branch of Algorithm 1 of Zhang–Yuan–Wang–Zhang (arXiv 2306.06813v1, Sections 3.1–3.3). The normalized unit rows correspond to integer rows with squared norms \(2,5,2\), and the row matrix is nonsingular. Direct Fraction enumeration proves the exact \(p=0\) one- and two-step expectations; the specific row sequence \((2,1)\) has exactly \(971/200\) squared error. For every real \(p\ge24\), elementary rational inequalities give a lower bound \(994304/206949\) for the two-step expected error, strictly larger than \(4193/900\). The two-row no-reversal identity is a sum of nonnegative terms and covers all real input errors. `verify.py` reproduces all critical rational computations. Risk: finite test grids are not proofs of the universal two-row statement; the displayed identity is that proof.

## Originality — PASS, with residual priority risk

The defining WRaSK article proves Bregman-distance and Euclidean-norm convergence upper bounds, not exact comparative two-step squared risk; Tondji–Winkler–Lorenz (2021 Online ICCHA) independently give the same residual-weighted sparse algorithm and a global expected squared-error convergence-rate bound, not exact fixed-horizon domination; Steinerberger (arXiv 2007.02910) proves a residual-weighted projection rate upper bound, not finite-horizon domination. Nutini et al. (arXiv 1612.07838), Haddock–Ma (arXiv 1912.03544), and the task-ordering comparison of Tsipory et al. (arXiv 2510.19941) do not imply this two-step counterexample and two-row identity under their distinct objects/criteria. Searches for matching residual-power WRaSK reversals, Kaczmarz–Motzkin two-step comparisons, and two-row obstructions yielded no inspected dominating result. Risk: unindexed specialization or inaccessible further literature may establish an equivalent result; search absence is not proof of priority.

## Value — PASS

Residual-dependent sampling is deliberately designed to increase immediate progress and improve theoretical rate constants. The theorem isolates a mathematically motivated finite-budget limitation: improving first-step squared error can **increase the exact two-step expectation**, even on a uniquely solvable consistent system and even with the method's genuine positive regularizer. The nonnegative two-row projection defect identifies the minimum row-count obstruction in the zero-regularization subcase rather than merely supplying an arbitrary example. Risk: the example does not quantify typical-instance behavior or establish a universal adverse long-term rate.

Self-review: passed. Independent audit: not yet performed.
