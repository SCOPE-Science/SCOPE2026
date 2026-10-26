# Strict positive transient three-site Palm dependence in nearest-neighbor adsorption

## Finding

For each nonterminal observation time \(0<t<1\), consider the first *permitted* neighboring occupied-site indicators on the two sides of an occupied origin, \(J_-(t)=\omega_{-2}(t)\) and \(J_+(t)=\omega_2(t)\). Their full time-resolved conditional joint law is a nontrivial, strictly positively dependent Bernoulli mixture. In particular,
\[
\Pr(J_-(t)=0\mid\omega_0(t)=1)=\Pr(J_+(t)=0\mid\omega_0(t)=1)=\frac{2t}{e^{2t}-1},
\]
\[
\Pr(J_-(t)=0,J_+(t)=0\mid\omega_0(t)=1)
=\frac{2(t-t^2+t^3/3)}{e^{2t}-1},
\]
and consequently the strictly positive three-site conditional covariance is
\[
\boxed{\operatorname{Cov}(J_-(t),J_+(t)\mid\omega_0(t)=1)
=\frac{2(t-t^2+t^3/3)}{e^{2t}-1}-\frac{4t^2}{(e^{2t}-1)^2}>0.}
\]
All other entries of the conditional binary pair distribution follow by subtraction. The positivity holds at every \(0<t<1\), not just at saturation, and exhibits transient conditioning-induced dependence not specified by the previously established two-point correlation function. The formula extends continuously to \(t=1\). At that endpoint it gives the jammed adjacent-gap joint matrix
\[
\begin{array}{c|cc}
 & R=2 & R=3\\ \hline
L=2 & 1-\dfrac{10}{3(e^2-1)} & \dfrac{4}{3(e^2-1)}\\[5pt]
L=3 & \dfrac{4}{3(e^2-1)} & \dfrac{2}{3(e^2-1)}
\end{array}.
\]
**The saturated gap matrix is a corollary already determined by the published all-distance pair-correlation function and is not asserted as a separately original contribution.** Its agreement is an exact check on the transient three-site law.

## Assumptions and scope

Let \((T_j)_{j\in\mathbb Z}\) be independent uniform random variables on \((0,1)\). Initially all sites of \(\mathbb Z\) are empty. At its only attempt time \(T_j\), site \(j\) is permanently occupied if and only if both immediate neighbors are still empty; otherwise it remains permanently empty. Let \(\omega_j(t)\) be the occupied-site indicator at time \(t\), for \(0\le t\le1\). The process is well defined on the full infinite lattice: the probability of a decreasing-priority nearest-neighbor path of length \(n\) from a fixed site is at most \(2^n/(n+1)!\), which tends to zero. Consequently local acceptance decisions depend almost surely on a finite priority neighborhood.

Probabilities conditional on \(\omega_0(t)=1\) refer to an occupied-site Palm conditioning, not to a randomly selected spatial location without conditioning. At \(t=1\), every unoccupied site has an occupied neighbor almost surely (its own attempt was rejected), and adjacent occupied sites are impossible. Thus \(L,R\in\{2,3\}\). At intermediate times define \(J_-(t)=\omega_{-2}(t)\) and \(J_+(t)=\omega_2(t)\); these indicators do not themselves necessarily determine the nearest occupied neighbor before saturation.

## Proof

**1. One-sided occupancy.** Consider the ray \(\{2,3,\ldots\}\), with site \(1\) permanently held vacant, and let \(b(s)\) be the probability that site \(2\) is occupied by time \(s\). Conditional on its attempt at time \(s\), its neighbor \(3\) has experienced the same ray problem while site \(2\) remains unattempted. Therefore \(b'(s)=1-b(s)\), with \(b(0)=0\). Hence
\[
b(s)=1-e^{-s}.
\]

**2. Law of a successful central attempt.** Fix \(T_0=u\), with \(0<u<t\). On either side, let \(A_u\) denote the event that the neighboring site \(1\) has not become occupied before \(u\), treating the origin as vacant until that time. The alternatives \(T_1>u\) and \(T_1=s\le u\) with site \(2\) already occupied at \(s\) give
\[
\Pr(A_u)=(1-u)+\int_0^u b(s)\,ds=e^{-u}.
\]
The two rays are independent. Thus the joint density of the event that the origin is successfully occupied at time \(u\) is \(e^{-2u}\,du\). In particular,
\[
\Pr(\omega_0(t)=1)=\int_0^t e^{-2u}\,du
=\frac{1-e^{-2t}}2,
\]
and the conditional success-time density is
\[
h_t(u)=\frac{2e^{-2u}}{1-e^{-2t}},\qquad 0<u<t.
\]

**3. Conditional Bernoulli law on each side.** Given \(T_0=u\) and successful occupation of the origin, site \(1\) remains empty forever. Within the event \(A_u\), the evolution at site \(2\) coincides with that of the one-sided ray having site \(1\) held empty. Let \(B_t\) be its occupation by \(t\). Splitting according to \(T_1>u\) and \(T_1=s\le u\), now demanding \(B_t\), yields
\[
\begin{aligned}
\Pr(B_t\cap A_u)
&=(1-u)b(t)+\int_0^u b(s)\,ds\\
&=e^{-u}-(1-u)e^{-t}.
\end{aligned}
\]
Dividing by \(\Pr(A_u)=e^{-u}\) gives
\[
q_t(u):=\Pr(\omega_2(t)=1\mid T_0=u,\omega_0(t)=1)
=1-(1-u)e^{u-t}.
\]
The identical formula holds for site \(-2\). Conditional on the successful central time \(u\), the two side events are independent. Their common Bernoulli success parameter \(q_t(u)\) depends strictly increasingly on \(u\), since \(q_t'(u)=u e^{u-t}>0\) for \(u>0\).

**4. Time-resolved positive dependence.** Put \(z_t(u)=1-q_t(u)=(1-u)e^{u-t}\). Under density \(h_t\), direct integration gives
\[
\mathbb E[z_t(U)]=\frac{2t}{e^{2t}-1},\qquad
\mathbb E[z_t(U)^2]=\frac{2(t-t^2+t^3/3)}{e^{2t}-1}.
\]
Conditional independence on the two sides implies
\[
\operatorname{Cov}(J_-(t),J_+(t)\mid\omega_0(t)=1)
=\operatorname{Var}(q_t(U))
=\operatorname{Var}(z_t(U))=C(t).
\]
Because \(U\) has positive density on \((0,t)\), and \(q_t\) is strictly increasing there, this variance is strictly positive for every \(t>0\). This proves the asserted analytic formula and strict sign without reliance on numerical data.

**5. Saturation boundary check and known pair-correlation implication.** At \(t=1\), the event \(L=3\) is precisely the event that site \(-2\) is empty, and similarly \(R=3\) iff site \(2\) is empty. Set \(a=e^2-1\). The preceding integrals yield
\[
\Pr(L=3\mid\omega_0(1)=1)=\frac2a,\qquad
\Pr(L=3,R=3\mid\omega_0(1)=1)=\frac{2}{3a}.
\]
Subtraction gives the other three entries of the displayed joint matrix. As \(L=2+\mathbf 1_{\{L=3\}}\) and similarly for \(R\), their covariance equals
\[
\frac{2}{3a}-\frac4{a^2}
=\frac{2(e^2-7)}{3(e^2-1)^2}.
\]
It is strictly positive: from \(e>1+1+1/2+1/6=8/3\), we get \(e^2>64/9>7\). At saturation this also demonstrates nonrenewal; this endpoint implication is recoverable from earlier pair correlations and is not the novelty claim. Indeed, because an occupied pair at distance four forces occupation of the intermediate site at jamming, the published pair probability at separation four directly gives the \(L=R=2\) entry, and the separation-two pair probability gives the marginal \(\Pr(L=2)\).

## Verification

The companion standalone `checker.py` uses only Python's standard library. It evaluates the success-time mixture via independent composite Simpson quadrature at twenty observation times, checks all exact matrix and covariance identities, and compares the full jamming matrix against a separately simulated random-priority greedy process on long periodic chains. Its saved execution output is in `checker_results.txt`. These finite and floating-point tests are diagnostic only; all infinite-volume and strict-sign assertions are proved above.

## Relationship to prior work

The model's one-site and two-site time-dependent probabilities, as well as the spatial shielding mechanism, were established in earlier random sequential adsorption work. Amaral and dos Santos (2022, arXiv:2210.05627) derive density and pair correlations in the exact one-attempt nearest-neighbor exclusion model; the success probability above reproduces their one-site law. The current result evaluates a **transient occupied-site-conditioned three-location event**, whose two-sided dependence for \(0<t<1\) is not determined by the marginal nearest-neighbor statistics or pair correlations alone. At saturation, however, hard-core and maximality make the resulting gap matrix deducible from published two-point formulas; we explicitly exclude that corollary from the novelty claim.

Gerin (2015) analyzes the dual Page–Rényi discrete parking construction, including density and correlation bounds; the present evaluated transient three-site conditional covariance is not stated in that work. Krivelevich et al. (2023/2024) treat expected random-greedy independent-set densities by local limits rather than this exact Palm gap dependence. Early spatial-correlation frameworks, notably Evans, Burgess, and Hoffman (1984), provide powerful general hierarchies and remain an important priority comparison; full text of that paper was not available for this assessment, so an equivalent derived three-site specialization elsewhere cannot be excluded. Work on continuum car parking and one-gap distributions does not directly determine this discrete two-gap joint law.

## Limitations

The calculation is for the infinite line, spatially homogeneous iid continuous first-attempt priorities, nearest-neighbor hard exclusion, no detachment or diffusion, and conditioning on an occupied central site. It does not assert a renewal theorem for any differently defined blocking process, does not describe three or more successive gaps, and does not quantify finite-system corrections. The original contribution asserted here is the transient (\(0<t<1\)) conditional triple law; the jammed two-gap specialization is implied by prior pair statistics and serves only as a check. The finite-time covariance concerns occupancies at distance two, not variable nearest occupied-site distances before saturation. Independent scholarly priority assessment has not been performed; general early hierarchy methods could imply the result after a nontrivial specialization.

## References

1. C. S. do Amaral and D. C. dos Santos, *Density and correlation in a random sequential adsorption model*, 2022, arXiv:2210.05627, https://arxiv.org/abs/2210.05627.
2. L. Gerin, *The Page–Rényi Parking Process*, Electronic Journal of Combinatorics 22 (2015), P4.4, doi:10.37236/5150, https://www.combinatorics.org/ojs/index.php/eljc/article/view/v22i4p4.
3. M. Krivelevich, T. Mészáros, P. Michaeli, C. Shikhelman, *Greedy maximal independent sets via local limits*, Random Structures & Algorithms 64 (2024), 986–1015, doi:10.1002/rsa.21200.
4. J. W. Evans, D. R. Burgess, D. K. Hoffman, *Irreversible random and cooperative processes on lattices: Spatial correlations*, J. Math. Phys. 25 (1984), 3051–3063, doi:10.1063/1.526021.
5. M. D. Rintoul, S. Torquato, G. Tarjus, *Nearest-neighbor statistics in a one-dimensional random sequential adsorption process*, Phys. Rev. E 53 (1996), 450–457, doi:10.1103/PhysRevE.53.450 (continuum hard-object model).
