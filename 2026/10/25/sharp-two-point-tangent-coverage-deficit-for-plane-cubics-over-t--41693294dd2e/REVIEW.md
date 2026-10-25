# Review of sharp two-point tangent-coverage deficit

## Correctness — PASS

The finite domain is all \((5^{10}-1)/4=2441406\) scalar-normalized ternary cubics. Two different exact enumerators, one using projective gradients and the other first-order coefficients of restrictions to rational flags, agree throughout the full \(32\)-entry histogram and on the \(186000\) maximizers at \(29\) covered points. A complete five-generator projective-group orbit computation decomposes all maximizers into two \(93000\)-element orbits. Algebraic gradient contradictions prove geometric smoothness of both representatives; the chart Gröbner calculations independently reproduce it. Thus the upper bound, sharpness and equality classification are verified on the entire asserted domain. The C executables and calculations can be reproduced from the included sources.

## Originality — PASS, with a specific residual risk

Asgarli–Ghioca (2023, arXiv:2302.13420) defines tangent-filling curves and provides general non-filling conditions whose size hypotheses exclude this cubic setting. A previous exact no-filling exclusion over the five-element field provides only coverage at most \(30\), not the new sharp \(29\) or the complete two-orbit equality classification. Published arc classifications have related point-incidence objects but their accessible abstracts do not establish this rational algebraic tangent-incidence theorem. Possible previously unindexed equivalent computations or consequences of uninspected arc tables are a documented publication-priority risk; no claim of global novelty is made from negative searches alone.

## Value — PASS

The natural target is the sharp coverage boundary below tangent-filling for the first small prime plane where cubics cannot cover all rational points. The exact two-point deficit and two entire projective equality classes distinguish two forms of extremal elliptic cubic with different rational point counts, rather than simply recomputing non-filling. The classification is a reusable arithmetic benchmark for the dual Gauss-image blocking problem. No claim is made for other finite fields.

## Limitations and sources

The theorem is restricted to the field with five elements and exact finite arithmetic; an independently audited external proof has not been supplied. The most relevant detailed primary source is Asgarli–Ghioca, *Tangent-filling plane curves over finite fields* (arXiv:2302.13420, 2023). Coolsaet's 2012 complete 3-arc classification is a priority-risk comparison: only its abstract was inspected.

Self-review: passed. Independent audit: not yet performed.
