# Independent mathematical audit

## correctness

PASS

The Brownian hitting-time transform E_x[e^{-s tau0}]=e^{-x sqrt(s)} yields M_N(u^2)=W(1-e^{-u})/[u^2 sum_j a_j e^{-a_j u}], and differentiation gives uM'/M=h(u)-2+u mu_N(u). At u=c/a_j, c=0.5 or 2, normalize by a_j: lower-index terms total <=1/999 and higher terms <=2*10^6 e^{-500}, hence |mu_N/a_j-1|<=e^2(1/999+2*10^6e^{-500})<0.01 uniformly for every N,j. The derivative is < -0.495 at c=0.5 and >2/7-2+1.98>0 at c=2. Each window has an interior strict local minimum since the positive real-analytic function is nonconstant; signs on successive windows imply intervening strict maxima. r=u^2 is order-preserving. Independent recalculation verifies the analytic bound and 231 endpoint windows up to N=21; finite tests do not establish all N.

## originality

PASS

The N-site MFPT formula and two-site metastability were established by Julián-Salgado, Dagdug and Boyer, arXiv:2311.11897, Eq.(4)/Sections III–VI. The new claim is a uniform explicit construction producing arbitrarily many disjoint strictly minimizing reset-rate windows, requiring derivative-sign and scale-dominance estimates not present in that two-site result. Besga et al. (arXiv:2004.11311) treat a Gaussian site law and a single metastable optimum. Mendez et al. (arXiv:2401.01125) study distributed reset locations and equivalent first-passage laws, not a uniform all-N multiple-well theorem. Searches are bounded, so absolute priority is not established.

## value

PASS

Unbounded numbers of local extrema in the mean search time are a structural multiscale optimization phenomenon for a natural stochastic-reset process. A uniform N-independent lower-bound construction rules out a universal finite cap and explains the competing timescales; not a routine two-site parameter substitution. It is useful without claiming any global-minimum coexistence or upper extrema count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
