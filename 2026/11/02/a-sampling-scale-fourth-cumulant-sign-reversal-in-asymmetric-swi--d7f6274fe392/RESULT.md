# A sampling-scale fourth-cumulant sign reversal in asymmetric switching movement

## Finding

Five regularly timed position observations can distinguish a stationary two-behavior velocity model from an exactly covariance-matched Gaussian velocity model using the fourth joint cumulant of four consecutive observed displacements. The distinction is unchanged by arbitrary independent, non-Gaussian position-localization errors having finite fourth moments. In the asymmetric regime the cumulant has a unique *blind sampling interval* at which it crosses from negative to positive.

Define \(b=\pi(1-\pi)\) and \(H(x)=(1-e^{-x})/x\). For observation spacing \(\Delta>0\) and total switch rate \(a>0\), the exact expression is

\[\kappa_4=\delta^4b\Delta^4e^{-2a\Delta}H(a\Delta)^2\left[(1-2\pi)^2-2bH(a\Delta)^2\right].\]

The complete strict sign classification is:

1. If \(\pi=1/2\), \(\kappa_4<0\) for all \(\Delta>0\).
2. If \(0<|1-2\pi|<1/\sqrt3\), there is exactly one \(\Delta_*>0\) with \(\kappa_4=0\); the cumulant is negative before and positive after it, with \(H(a\Delta_*)=|1-2\pi|/\sqrt{2b}\).
3. If \(|1-2\pi|\ge1/\sqrt3\), \(\kappa_4>0\) for all \(\Delta>0\).

The strict boundary \(|1-2\pi|=1/\sqrt3\) has positive cumulant at every positive spacing, although its short-spacing limit after dividing out \(\Delta^4\) is zero.

## Assumptions and scope

Let \(Z(t)\in\{0,1\}\) be a stationary irreducible continuous-time Markov chain with transition rates \(q_{01}>0\) and \(q_{10}>0\). Set \(a=q_{01}+q_{10}\), \(\pi=q_{01}/a\), and \(S(t)=Z(t)-\pi\). The physical velocity is \(v(t)=c+\delta S(t)\), with arbitrary drift \(c\in\mathbb R\) and \(\delta\ne0\). The latent position is

\[X(t)=\int_0^t v(u)\,du+\sqrt{2D}\,B(t),\qquad D\ge0,\]

where \(B\) is standard Brownian motion independent of \(Z\). For a fixed \(\Delta>0\), observe \(Y_j=X(j\Delta)+\varepsilon_j\) for \(j=0,1,2,3,4\), and define \(I_j=Y_j-Y_{j-1}\). The five errors \(\varepsilon_j\) are mutually independent and independent of \((Z,B)\), have finite fourth moments and arbitrary means, distributions and variances. No Gaussian-error assumption is used.

The comparator replaces \(\delta S\) by a centered stationary Gaussian Ornstein–Uhlenbeck velocity \(G\) with covariance \(\operatorname{Cov}(G(t),G(s))=\delta^2b\exp(-a|t-s|)\), keeping the same drift, diffusion and localization-error laws. The statement concerns population moments and cumulants, not inference from a finite dataset.

## Proof

**1. Exact ordered-time cumulant.** Stationarity and the two-state transition semigroup give \(\mathbb E[S(t+h)\mid S(t)]=e^{-ah}S(t)\). Since \(S\) takes the values \(-\pi\) and \(1-\pi\),

\[S(t)^2=b+(1-2\pi)S(t).\]

For ordered instants \(t_1<t_2<t_3<t_4\), the centered second moment is \(\mathbb E[S(t_i)S(t_j)]=b e^{-a(t_j-t_i)}\). Recursively conditioning the four-point product and subtracting its three pairwise products yields

\[\operatorname{cum}(S(t_1),S(t_2),S(t_3),S(t_4))=b e^{-a(t_4-t_1)}\left[(1-2\pi)^2-2b e^{-a(t_3-t_2)}\right].\]

For additional explicit verification, with \(r=e^{-a(t_2-t_1)}\), \(z=e^{-a(t_3-t_2)}\), \(t=e^{-a(t_4-t_3)}\), the right-hand side equals \(brzt[(1-2\pi)^2-2bz]\). The accompanying symbolic checker derives exactly this polynomial from four products of the transition matrices \(P_u=\mathbf1\pi^\top+(I-\mathbf1\pi^\top)u\), without using the claimed cumulant as an input.

**2. Integrate over disjoint observation intervals.** Multilinearity of cumulants permits integration of the preceding continuous kernel over \([0,\Delta]\), \([\Delta,2\Delta]\), \([2\Delta,3\Delta]\), \([3\Delta,4\Delta]\). Writing \(x=a\Delta\), the first-to-fourth exponential contribution factors into

\[\left(\int_0^\Delta e^{at}\,dt\right)\left(\int_{3\Delta}^{4\Delta}e^{-at}\,dt\right)=\Delta^2e^{-2x}H(x)^2.\]

The middle correction factors into

\[\left(\int_\Delta^{2\Delta} e^{at}\,dt\right)\left(\int_{2\Delta}^{3\Delta}e^{-at}\,dt\right)=\Delta^2H(x)^2.\]

Multiplying the integrals by the velocity contrast \(\delta^4\) proves the boxed formula. Since every cumulant term is bounded and each time interval is compact, interchange of expectation, integrals and cumulant expansion is justified.

**3. Eliminate diffusion and measurement-error contributions.** Brownian increments in disjoint observation intervals are independent Gaussian and independent of the switching velocity. Each localization error \(\varepsilon_j\) enters at most two of the four observed increments, while every mixed fourth cumulant involving mutually independent source groups is zero unless all four arguments share a common source. Therefore neither Brownian noise nor independent localization errors contribute to \(\operatorname{cum}(I_1,I_2,I_3,I_4)\), irrespective of the latter's marginal kurtoses. Adding deterministic drift also changes no cumulant of order four.

**4. Sharp sign transition.** The positive prefactor leaves the sign of \((1-2\pi)^2-2bH(x)^2\). As \(H(x)=\int_0^1e^{-xt}\,dt\), \(H\) is strictly decreasing from 1 to 0 on \(x>0\). At \(x\downarrow0\), the bracket equals \((1-2\pi)^2-2b=1-6b\). For \(0<|1-2\pi|<1/\sqrt3\), the bracket starts negative and ends positive, so it has exactly one positive zero. At \(\pi=1/2\) it is strictly negative. At \(|1-2\pi|\ge1/\sqrt3\), it is strictly positive for \(x>0\), including equality, because \(H(x)<1\). This exhausts \(0<\pi<1\).

**5. Gaussian covariance-matched comparator.** Both centered velocities have covariance \(\delta^2b e^{-a|t-s|}\), so integration and independent addition give the same means and every pairwise covariance for all positions and displacements. The comparator's four integrated Gaussian velocities have zero fourth cumulant, and Step 3 removes the other sources. This proves the claimed second-order indistinguishability and fourth-order separation, except at the unique zero of this particular statistic.

## Verification

The included `verify.py` reconstructs the ordered-time four-point cumulant symbolically using stationary transition matrices, checks both interval-integral simplifications symbolically, and stress-tests the strict phase sign prediction for a grid of positive sampling intervals and stationary probabilities. This executable exercise supports the identities but is not a substitute for the preceding analytic arguments. Run `python verify.py` with Python 3 and SymPy available.

## Relationship to prior work

The 2007 public preprint by Cywiński and coauthors derives time-ordered four-point correlations and fourth cumulants for **symmetric** random telegraph noise in qubit dephasing (Appendix A); this establishes that general four-point cumulants of telegraph processes are not new here. López and Ratanov analyze asymmetric telegraph processes, and Kolesnik treats single-time moments and semi-invariants. The specific novel-candidate content assessed here is the *sharp stationary-asymmetry sampling-interval sign phase diagram for the mixed cumulant of four successive displacements*, together with its cancellation of arbitrary independent position errors and exact second-order equivalence to an Ornstein–Uhlenbeck comparator.

Fleming and collaborators analyze autocorrelated animal trajectories using Gaussian movement likelihoods and first two moments; Blackwell and collaborators study switching behavioral states in continuous-time movement. Neither directly supplies the present sampling-interval threshold in the inspected material. Broader multi-time cumulant literature could still subsume this mathematical specialization; historical priority is provisional.

## Limitations

The chain is stationary and two-state, switch rates and cadence are constant, and measurement errors are independent across distinct fix times and of the latent process. Temporally correlated localization errors, state-dependent localization errors, or non-Gaussian latent diffusion invalidate the error-cancellation claim without further assumptions. The special cadence \(\Delta_*\) is a blind spot only for this selected fourth cumulant; it does not imply equal full distributions. No finite-sample estimator, error-rate guarantee, or empirical field validation is established. Related full-text sources that could not be inspected leave an explicit priority risk.

## References

- Ł. Cywiński et al. (public preprint December 13, 2007), *How to Enhance Dephasing Time in Superconducting Qubits*, Appendix A, https://arxiv.org/abs/0712.2225.
- Kolesnik (2012), *Moment analysis of the telegraph random process*, bibliographic record and abstract, https://www.math.md/en/publications/basm/issues/y2012-n1/11070/.
- J. M. López and N. Ratanov (2014), *On the asymmetric telegraph processes*, DOI:10.1239/jap/1402578644.
- C. H. Fleming et al. (public online March 9, 2014), *Non-Markovian maximum likelihood estimation of autocorrelated movement processes*, DOI:10.1111/2041-210X.12176.
- P. G. Blackwell et al. (2015), *Exact Bayesian inference for animal movement in continuous time*, DOI:10.1111/2041-210X.12460.
