# Independent mathematical audit

## correctness

PASS

For the repaired claim, the known instantaneous step mean is sinh(cx)/(2 sinh x) with x=(L/2)√(r/D), so the physical speed at fixed L is rL times this mean. Its logarithmic derivative in x is H=2/x+c coth(cx)−coth x. Strict convexity gives sinh(cx)<c sinh x, hence H_x<0. Its endpoint limits are +∞ and c−1<0; its unique zero is a global maximum in both x and r. H_c=(sinh(cx)cosh(cx)−cx)/sinh²(cx)>0 for cx>0, so the maximizer increases strictly with c. As c→1, monotonicity and H(x,1)=2/x exclude a finite root limit. The mean-value theorem applied to u coth(ux_*) then gives 2/x_*=(1−c)(1+o(1)), including the stated squared divergence in r. c=0 is a zero-current model, not a distinguished optimum. Independent bounded replay: python3 /workspace/repairs/4/check.py, output /workspace/branches/repaired-4-check.txt; eight sampled critical points satisfy derivative signs and ordering and three scaled near-endpoint roots pass. The analytic sign and limit arguments, not the numerical samples, prove the theorem. The original dispersion formula is not removed for incorrectness: from the Laplace excursion endpoints one obtains E[N], E[N²] and E[NT]=E[N]/r−∂r E[N]; the centered cycle variance per mean cycle time yields the stated coefficient. To justify variance convergence rather than only a CLT, stop the martingale of centered iid rewards at the first cycle crossing the observation time. Its second moment is the single-cycle variance times rt+1. The crossing duration is bounded in second moment by the sum of an exponentially dominated age and an exponential residual; conditioning on alarm times bounds the crossing reward and the unfinished displacement in L² uniformly, so their omission changes variance by o(t). Independent tilted-kernel derivative checks of the original formula at four parameters are in /workspace/branches/independent-4.txt (python3 /workspace/branches/independent_checks.py 4). The frozen checker was inspected but not executed.

## originality

PASS

The frozen submission's main dispersion, covariance and enhancement package has exact equivalent coverage in a distinct indexed record, so it is not accepted as a distinct contribution. The matched path is dated later; this comparison establishes equivalent coverage, not earlier publication, priority or any relationship between authors. The repaired submission drops that package and retains only the explicit physical drift optimum: uniqueness for every interior asymmetry, strict dependence on asymmetry, and the singular endpoint scale. The old drift formula is credited as input. On the checked evidence the retained theorem is distinct; neither dimensional drift nonmonotonicity at variable system length nor a diffusivity maximum implies it.

## value

PASS

The retained claim settles a natural physical design question not answered by a qualitative peak versus dimensionless length. It supplies exactly one usable optimum at every interior asymmetry, rules out competing peaks, and quantifies how rapidly the optimal clock must speed up as the capture well approaches the forward boundary. The strict comparison across asymmetries and the singular rate scale make this an exact all-parameter result rather than routine numerical maximization of a known formula. No credit is assigned to the removed dispersion package. The corrected scientific files and checker are in /workspace/repairs/4; the frozen evidence is unchanged.

The dated certificate retains the supplied scientific assessment, sources and limitations.
