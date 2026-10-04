# Same-model review

## Correctness
PASS. The kernel calculation is exact: Fourier inversion on the two lines turns vanishing into zero left- and right-incidence sums, while the extra point is one additional cyclotomic functional. The bipartite incidence rank gives the nullity formula, and invertibility forces a spanning connected unicyclic graph. On that graph the incidence kernel is the alternating cycle vector. The prime cyclotomic minimal polynomial gives the label-multiset criterion, and a reduced-incidence cofactor expansion after two inverse Fourier transforms gives \(|\det T(E_p,B)|=p^p|S_C|\). The bundled verifier supplies exact modular replay checks, including an exhaustive \(p=3\) census.

## Originality
PASS. The primary source asks about the same family in Question 1.10 and provides the Fourier-matrix framework, but the inspected full text does not give a bipartite graph, unicyclic classification, alternating label obstruction, or determinant formula. Targeted published-finding corpus and web searches found no equivalent statement. The closest later Fourier-minor paper concerns principal minors, which do not imply this fixed-row/arbitrary-column criterion.

## Value
PASS. This is a structural reduction of a specifically motivated open quantitative-spectrality family: all viable basis partners are compressed to one-cycle spanning graphs, and their determinant is controlled by a single explicit cycle sum. It does not settle the asymptotic Riesz ratio, but it removes most of the combinatorial search space and identifies the exact algebraic obstruction that any future optimization must respect.

## Closest literature and limitations
The closest source is Ferguson--Mayeli--Sothanaphan, arXiv:1904.04487v6, especially Question 1.10 and the basis-pair/Fourier-matrix propositions. Zhou, arXiv:2505.01189v1, is relevant broader Fourier-minor literature but is restricted to principal minors. The remaining scientific limitation is that no bound sharp enough to determine \(\rho(E_p)\) is proved; an unindexed equivalent formulation is also a residual novelty risk.

Same-model review: passed. Independent audit: not yet performed.
