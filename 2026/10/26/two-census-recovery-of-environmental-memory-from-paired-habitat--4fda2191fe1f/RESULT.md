# Two-census recovery of environmental memory from paired habitat occupancy

## Finding

**Theorem (two-patch, two-census moment identification).** Consider two identical binary habitat patches evolving under a shared stationary two-state Markov environment as defined below. For all parameters
\[
0<p<1,\qquad 0<a<\min\{p,1-p\},\qquad 0\le \lambda<1,\qquad -1<\rho<1,
\]
the four parameters \((p,a,\lambda,\rho)\) are uniquely determined by the joint law of patch occupancies at **two consecutive census dates**, and in fact by one mean and three second-order moments. Write
\[
\begin{aligned}
 m&=\mathbb E X_{1,t},\\
 C_0&=\operatorname{Cov}(X_{1,t},X_{2,t}),\\
 C_1&=\operatorname{Cov}(X_{1,t},X_{2,t+1}),\\
 A_1&=\operatorname{Cov}(X_{1,t},X_{1,t+1}).
\end{aligned}
\]
All denominators in the following reconstruction are nonzero:
\[
\boxed{\lambda=\frac{A_1-C_1}{m(1-m)-C_0},\qquad
 q=\frac{C_1}{C_0},\qquad
 \rho=\frac{q-\lambda}{1-\lambda q},\qquad
 a=\sqrt{C_0\frac{(1+\lambda)(1-\lambda\rho)}{(1-\lambda)(1+\lambda\rho)}},\qquad p=m.}
\]
The sign convention \(a>0\) chooses which latent environmental state is called favorable; without this convention the sign of \(a\) is unidentifiable by environmental-state relabeling.

Two dates are sharp for a **two-patch panel**: there exist two different admissible parameter quadruples with precisely the same complete one-date two-bit occupancy distribution.

## Assumptions and scope

The environmental state \(S_t\in\{-1,+1\}\) is a stationary, symmetric, irreducible Markov chain with
\[
\Pr(S_{t+1}=v\mid S_t=u)=\frac{1+\rho uv}{2},\qquad u,v\in\{-1,+1\}.
\]
Consequently \(\mathbb E S_t=0\) and \(\mathbb E(S_tS_{t+h})=\rho^{|h|}\). Each patch has occupancy \(X_{i,t}\in\{0,1\}\), for \(i=1,2\). At each date and independently for each patch, a fresh Bernoulli switch with success probability \(\lambda\) decides whether to copy that patch's previous occupancy; otherwise a fresh independent Bernoulli draw has probability \(p+aS_t\) of being occupied. Formally,
\[
X_{i,t}=H_{i,t}X_{i,t-1}+(1-H_{i,t})Z_{i,t},
\]
where the switches \(H_{i,t}\) are Bernoulli with parameter \(\lambda\), and conditional on the entire environmental sequence the refresh variables \(Z_{i,t}\) are independent Bernoulli variables with parameter \(p+aS_t\). All random switches and refresh noises are mutually independent across patches and dates, conditional on the environment. The finite-state chain has a unique stationary distribution under the displayed strict bounds. The theorem concerns this stationary distribution and exact population moments, not noisy estimates from a single observation per date. Occupancy is observed without classification error and there is no dispersal or direct interaction between patches.

## Proof

**1. Conditional patch means and spatial covariance.** Conditional on the entire two-sided environmental history, the patch processes use separate noises and are independent. Their common conditional mean equals \(p+M_t\), with the unique bounded stationary solution
\[
M_t=\lambda M_{t-1}+(1-\lambda)aS_t
=(1-\lambda)a\sum_{j=0}^{\infty}\lambda^j S_{t-j}.
\]
The series converges absolutely for \(0\le\lambda<1\). Since \(\mathbb E M_t=0\), \(m=p\) and \(C_0=\mathbb E M_t^2\). Using the Markov covariance of the environment,
\[
d:=\mathbb E(M_tS_t)
=\lambda\rho d+(1-\lambda)a
=\frac{(1-\lambda)a}{1-\lambda\rho}.
\]
Square the recursion for \(M_t\), note \(\mathbb E(M_{t-1}S_t)=\rho d\), and solve
\[
(1-\lambda^2)C_0=(1-\lambda)^2a^2+2\lambda(1-\lambda)a\rho d.
\]
This gives the exact positive expression
\[
\boxed{C_0=a^2\frac{(1-\lambda)(1+\lambda\rho)}{(1+\lambda)(1-\lambda\rho)}>0.}
\]

**2. Lagged cross covariance and local persistence.** Again using conditional independence of patches given the environmental history,
\[
\begin{aligned}
C_1&=\mathbb E(M_tM_{t+1})\\
&=\lambda C_0+(1-\lambda)a\mathbb E(M_tS_{t+1})\\
&=\lambda C_0+(1-\lambda)a\rho d.
\end{aligned}
\]
Thus the ratio simplifies exactly to
\[
\boxed{\frac{C_1}{C_0}=\frac{\lambda+\rho}{1+\lambda\rho}.}
\]
For one patch, conditioning on the full environmental history leaves a stationary conditional variance \(V_t=(p+M_t)(1-p-M_t)\). In the one-step update, only the copying event carries covariance from \(X_{i,t}\) to \(X_{i,t+1}\), giving
\[
\operatorname{Cov}(X_{i,t},X_{i,t+1}\mid (S_s)_{s\in\mathbb Z})=\lambda V_t.
\]
By total covariance and the marginal Bernoulli variance,
\[
\boxed{A_1=C_1+\lambda\,[p(1-p)-C_0].}
\]
The bracket is \(\mathbb EV_t>0\), because the conditional occupation probability belongs to the compact interior interval \([p-a,p+a]\subset(0,1)\).

**3. Global inversion and boundary checks.** The preceding formulas identify \(\lambda\) from \(A_1-C_1\), then the ratio \(q=C_1/C_0\). Since \(1+\lambda\rho>0\), \(|q|<1\) and \(1-\lambda q>0\), solving \(q=(\lambda+\rho)/(1+\lambda\rho)\) uniquely identifies \(\rho\). The positive value of \(a\) follows from the strictly positive formula for \(C_0\). All inversions remain valid if \(\rho=0\), \(\rho=\lambda\), \(\rho<0\), or \(\lambda=0\). This proves global uniqueness throughout the claimed parameter domain.

**4. Sharp one-date ambiguity.** Set \(p=1/2\). The distinct admissible parameter triples
\[
(a,\lambda,\rho)=(1/5,1/2,-2/7),\qquad (a,\lambda,\rho)=(1/10,0,0)
\]
both give \(C_0=1/100\). At one stationary census date the two exchangeable binary patch occupancies have the same exact joint law:
\[
\Pr(0,0)=\Pr(1,1)=13/50,\qquad
\Pr(0,1)=\Pr(1,0)=6/25.
\]
Indeed the entire two-bit law of an exchangeable Bernoulli pair is determined by its common marginal mean \(p\) and covariance \(C_0\). The differing parameters cannot therefore be distinguished by a single date; the two-date reconstruction is sharp for two patches.

## Verification

Run `python verify.py` (Python 3.10 or later, standard library only). This independently builds each 8-state joint environment/patch Markov transition matrix, solves the exact stationary equations over rational numbers, evaluates all four moments directly from transitions, and checks the formulas and inversions. The 12 parameter cases include both signs of environmental persistence, zero persistence, zero local copying, and the collision \(\lambda=\rho\). There are 768 independently constructed transition probabilities and 48 exact moment/formula comparisons, followed by 12 inverse checks. It also confirms the full one-date aliasing probability table. `verification_output.json` is the recorded output. Finite checks are illustrative and cannot establish the unrestricted theorem, which follows from the proof above.

## Relationship to prior work

The Moran-effect literature studies synchronized patch fluctuations driven by shared environmental stochasticity. Kendall et al. (2000) analyze population synchrony arising from dispersal and spatial environmental correlation in linearized population models; their detailed covariance calculations concern a different state model and do not provide the stated two-date inverse for Bernoulli patches with temporally Markov environmental forcing. Ripa (2000) studies linearized population synchrony and dispersal. MacKenzie et al. (2003) establish a separate multi-survey occupancy/detection framework, emphasizing confounding by imperfect detection; here occupancy is perfectly observed, and the unknown quantities are local state retention and persistence of the common environment. Massie et al. (2015) study temporally autocorrelated environmental forcing in population synchrony, but no equivalent two-site Bernoulli renewal moment identification was established from the material accessible for comparison. Heaton and Solo (2004) give broader structural-identification conditions for stationary dynamic factor models; only the abstract was accessible, so whether a specialization already yields some of the present covariance formulas remains a material priority risk. These connections motivate the problem and provide theoretical context; they are not claims of absolute priority.

## Limitations

The model assumes two homogeneous patches, conditional independence of their update noises, a symmetric binary exogenous environment, stationarity, and exact joint occupancy moments at adjacent dates. If environmental contrast vanishes (\(a=0\)), environmental memory is not identifiable. In the excluded nonrenewing limit \(\lambda=1\), local memory can prevent unique stationary occupancy. Unobserved detection error, patch-specific renewal probabilities, spatial dispersal, continuous-time irregular sampling, and finite-sample statistical efficiency are not addressed. Results about conditional environmental mechanisms must not be applied to data without model-fit checks. Related colored-noise synchrony models may imply special-case formulas; the present exact inversion and minimal two-date panel claim have not undergone independent audit.

## References

1. Kendall, B. E., Bjørnstad, O. N., Bascompte, J., Keitt, T. H., and Fagan, W. F. (2000). *Dispersal, Environmental Correlation, and Spatial Synchrony in Population Dynamics*. American Naturalist 155, 628–636. DOI: 10.1086/303350.
2. Ripa, J. (2000). *Analysing the Moran effect and dispersal: their significance and interaction in synchronous population dynamics*. Oikos 89, 175–187. DOI: 10.1034/j.1600-0706.2000.890119.x.
3. MacKenzie, D. I., Nichols, J. D., Hines, J. E., Knutson, M. G., and Franklin, A. B. (2003). *Estimating Site Occupancy, Colonization, and Local Extinction When a Species Is Detected Imperfectly*. Ecology 84, 2200–2207. DOI: 10.1890/02-3090; first published 1 August 2003.
4. Massie, T. M., Weithoff, G., Kuckländer, N., Gaedke, U., and Blasius, B. (2015). *Enhanced Moran effect by spatial variation in environmental autocorrelation*. Nature Communications 6, 5993. DOI: 10.1038/ncomms6993; published 9 January 2015.
5. Heaton, C., and Solo, V. (2004). *Identification of causal factor models of stationary time series*. The Econometrics Journal 7, 618–627. DOI: 10.1111/j.1368-423X.2004.00146.x.
