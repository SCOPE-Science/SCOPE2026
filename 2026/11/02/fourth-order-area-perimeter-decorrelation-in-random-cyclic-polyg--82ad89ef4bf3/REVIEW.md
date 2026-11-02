# Self-review

## Correctness — PASS

The claim follows from exact \(\operatorname{Dirichlet}(1,\ldots,1)\) power-sum moments, a bivariate exponential central limit theorem, and controlled sine remainder terms. The critical constants \(360,28800,3254400\) yield the orthogonal variance \(9504\pi^{10}\); the least-squares identity gives \(297\pi^4/10\). The embedded `VERIFIER.py` completed 76 checks, including independent numerical simplex integration. Finite checks are corroborative and do not certify asymptotics.

## Originality — PASS, with priority uncertainty

Bélisle (2011) concerns marginal area/perimeter laws. Xu–Meng–Li (2019) and Wang–Xu–Liu (2021) study fixed linear extrapolation and its variance; 2021 Lemma 2.2 gives variance \(3616\pi^{10}\) for centered \((4S_n-A_n)/3\), whereas the present optimal centered area residual has variance \(9504\pi^{10}\). Koroleva–Nikitin (2013) treats subset maxima. Dedicated published-finding corpus searches also found no equivalent statement. The uninspected portions of relevant 2011 and 2019 sources are an explicit priority risk; these comparisons are not historical uniqueness certification.

## Mathematical value — PASS

The optimal area-on-semiperimeter coefficient carries a genuinely second-order correction \(-48\pi^2/n^2\). Its residual variance is just \(33/113\) of the classical fixed-slope residual, quantifying additional joint information that separate marginal limit laws miss. The sharp decorrelation constant gives a natural quantitative measure of asymptotic redundancy in circular-polygon statistics.

## Boundaries

The result is for iid arclength-uniform samples on the unit circle, and for linear least-squares prediction only. The proof does not establish results for arbitrary sampling laws, noncircular boundaries, conditional expectations, or historical priority.

Self-review: passed. Independent audit: not yet performed.
