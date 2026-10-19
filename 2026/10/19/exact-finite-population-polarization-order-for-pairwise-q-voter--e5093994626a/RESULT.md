# Exact finite-population polarization order for pairwise q-voter influence and its three-voter reversal

## Finding

Consider the noisy binary unanimity-voter process on a complete graph. At stationarity, let \(K_R\) and \(K_D\) be the numbers of positive opinions when the influence group is sampled respectively **with replacement** (\(R\)) or **without replacement** (\(D\)). If the group has size \(q=2\), then for every population size \(N\geq3\) and independence probability \(0<p<1\),

\[
K_R\preceq_{\mathrm{cx}}K_D.
\]

Here convex order means that \(\mathbb E\varphi(K_R)\leq\mathbb E\varphi(K_D)\) for *every* convex real function \(\varphi\) on \([0,N]\). More precisely, \(\lvert K_R-N/2\rvert\) is below \(\lvert K_D-N/2\rvert\) in **likelihood-ratio order**: the stationary mass ratio between the two models is nonincreasing as distance from the balanced state increases. For \(N=3\), both stationary laws coincide. For every \(N\geq4\), their variances satisfy the strict inequality

\[
\operatorname{Var}(K_R)<\operatorname{Var}(K_D).
\]

The group size matters decisively. At \(q=3\) and \(N=4\), the convex order **reverses** for *every* \(0<p<1\):
\[
K_D\preceq_{\mathrm{cx}}K_R,\qquad
\operatorname{Var}(K_D)<\operatorname{Var}(K_R).
\]

Thus allowing repeated influence agents reduces stationary polarization under pairwise unanimity, but increases it in the smallest admissible three-person influence example. These assertions hold for every positive noise level, not merely in a thermodynamic approximation.

## Assumptions and scope

Fix an integer \(N\geq3\) and \(0<p<1\). Each of the \(N\) agents has a binary opinion. In each elementary update, choose one focal agent uniformly. With probability \(p\), independently flip that agent's opinion with probability \(1/2\). Otherwise choose \(q\) of the other \(N-1\) agents uniformly, either as independent draws with replacement or as distinct draws without replacement. Only a unanimous influence group causes the focal opinion to conform. For the distinct-draw model require \(1\leq q\leq N-1\). There are no zealots, external fields, network weights, or asymmetric spontaneous choices.

Let \(K\in\{0,1,\ldots,N\}\) count positive opinions, and use superscripts \(R\) and \(D\) to distinguish replacement and distinct draws. Write \(M=N-1\), \(a=p/2\), and \(b=1-p\). For \(q=2\), define
\[
f_R(j)=\frac{j^2}{M^2},\qquad
f_D(j)=\frac{j(j-1)}{M(M-1)},\qquad 0\leq j\leq M.
\]
The second formula includes \(f_D(0)=f_D(1)=0\). The step probabilities of the count chain are
\[
u_k^X=\frac{N-k}{N}[a+b f_X(k)],\qquad
v_k^X=\frac{k}{N}[a+b f_X(N-k)],\quad X\in\{R,D\}.
\]
The residual probability is a self-loop. Since \(a>0\), each count chain is irreducible and aperiodic and has a unique stationary law \(\pi^X\).

## Proof

**1. Exact finite-state reversibility and spin symmetry.** The complete graph makes the count process Markov. Every birth–death chain is reversible on its line of states, hence
\[
\frac{\pi_{k+1}^X}{\pi_k^X}=\frac{u_k^X}{v_{k+1}^X},\qquad 0\leq k<N.
\]
The rates obey \(u_{N-k}^X=v_k^X\), so uniqueness gives \(\pi_k^X=\pi_{N-k}^X\). In particular both laws have mean \(N/2\).

**2. A comparison of the stationary density ratios.** Put
\[
T(j)=\frac{a+bj^2/M^2}{a+bj(j-1)/[M(M-1)]},\qquad 0\leq j\leq M.
\]
The exact identity
\[
T(j)=1+\frac{bj(M-j)}{M^2(M-1)[a+bj(j-1)/(M(M-1))]}
\]
shows that \(T(0)=T(M)=1\). For integers \(0<j<M/2\), the numerator \(j(M-j)\) of the correction is invariant under \(j\mapsto M-j\), whereas the denominator strictly increases under this replacement: \(j(j-1)<(M-j)(M-j-1)\). Thus
\[
T(j)>T(M-j)\qquad (0<j<M/2).
\]
Define \(R_k=\pi_k^R/\pi_k^D\). Cancelling identical focal-selection factors in the detailed-balance ratios yields
\[
\frac{R_{k+1}}{R_k}=\frac{T(k)}{T(M-k)}.
\]
It follows that \(R_0=R_1\); \(R_k\) increases strictly across available interior steps toward the center and decreases symmetrically thereafter. If \(N=3\), there are no strict interior steps and all \(R_k\) are equal, hence the laws coincide. If \(N\geq4\), at least \(k=1\) gives a strict increase, so they differ.

**3. Likelihood-ratio and convex order.** Since each law is reflection symmetric, the probability ratio for the radial coordinate \(D=\lvert K-N/2\rvert\) equals \(R_k\) at either reflected state. The preceding monotonicity makes the ratio \(\Pr(D_R=d)/\Pr(D_D=d)\) nonincreasing in \(d\). Normalization therefore gives likelihood-ratio order and consequently first-order stochastic dominance \(D_R\preceq_{\mathrm{st}}D_D\). To deduce convex order of \(K\), for every convex \(\varphi\) consider the symmetrization
\[
h(d)=\frac{\varphi(N/2+d)+\varphi(N/2-d)}2.
\]
Convexity makes \(h\) nondecreasing for \(d\geq0\). Because the \(K\)-laws are symmetric, \(\mathbb E\varphi(K_X)=\mathbb E h(D_X)\). Thus the desired convex order follows. Choosing \(\varphi(x)=(x-N/2)^2\), which is strictly increasing in radial distance away from zero, gives strict variance ordering when \(N\geq4\).

**4. Sharp failure of a group-size-uniform direction.** For \(q=3,N=4\), we have \(M=3\), and distinct sampling of three neighbors reaches unanimous positive opinion only when all three are positive. At \(j=1,2\), its unanimity probability is zero, whereas repetition gives respectively \(1/27\) and \(8/27\). With the analogous ratio \(T_3(j)=[a+b(j/3)^3]/[a+b\binom j3/\binom33]\),
\[
T_3(0)=T_3(3)=1,\qquad
\frac{T_3(1)}{T_3(2)}=\frac{a+b/27}{a+8b/27}<1.
\]
Therefore \(R_0=R_1=R_3=R_4>R_2\), after normalization. The repeated-draw stationary law places strictly greater relative mass at all noncentral levels than at \(K=2\). Its radial distribution is larger in likelihood-ratio order. This yields the reversed convex order and strict variance comparison for every \(0<p<1\), completing the proof.

## Verification

Run `python3 verify.py`, using only the Python standard library. The program reconstructs exact stationary birth–death probabilities and checks all stated detailed-balance and radial-tail comparisons using rational arithmetic for \(3\leq N\leq21\) and four independent noise fractions. It also enumerates all ordered influence tuples from the microscopic update rules for \(3\leq N\leq7\) to independently check the count-chain rates. Finally it verifies the opposite \(q=3,N=4\) variance ordering and microscopic transitions. The packaged checker completed 6,492 exact rational assertions. The general proof above, not these finite checks, establishes the assertions for unbounded \(N\) and all real \(0<p<1\).

## Relationship to prior work

Weron, Nyczka and Szwabiński (2024) compare repetition and nonrepetition in noisy \(q\)-voter influence groups through simulations, mean-field and pair approximations. Their model's microscopic rules coincide with the present setting on a complete graph, but the exact all-finite-population stationary likelihood-ratio and convex-order conclusions are distinct from their approximations and simulated concentration curves. Vieira et al. (2020) analyze a more general noisy threshold \(q\)-voter mechanism, including repetition choices; their inspected preprint focuses on mean-field and pair approximations, critical phase diagrams and simulation scaling rather than the exact stationary finite-count law compared here. The ordinary birth–death detailed-balance identity and likelihood-ratio stochastic-order implication are standard and are not presented as new. The contribution is the explicit finite-population comparison and its sharp change of direction as the influence-group size changes.

## Limitations

The results do not assert stochastic ordering at every time from arbitrary initial states, nor do they cover sparse graphs, \(q\geq4\), agent heterogeneity, or other noise mechanisms. The stationary ordering depends on the precisely specified exclusion of the focal voter from influence sampling. At \(p=0\), the chain is not irreducible and the unique-stationary-law argument fails; at \(p=1\), the two chains coincide, so strictness fails. The statement addresses stationary laws, not temporal trajectories or transition rates. A broader unlocated finite-state comparison theorem could imply parts of this result, so publication priority requires additional independent literature assessment.

## References

1. T. Weron, P. Nyczka and J. Szwabiński, "Composition of the Influence Group in the q-Voter Model and Its Impact on the Dynamics of Opinions," *Entropy* 26 (2024), 132, published January 31, 2024. DOI: 10.3390/e26020132.
2. A. R. Vieira, A. F. Peralta, R. Toral, M. San Miguel and C. Anteneodo, "Pair approximation for the noisy threshold q-voter model," *Physical Review E* 101 (2020), 052131. DOI: 10.1103/PhysRevE.101.052131; preprint arXiv:2002.04715.
3. A. Jędrzejewski, "Pair approximation for the q-voter model with independence on complex networks," *Physical Review E* 95 (2017), 012307. DOI: 10.1103/PhysRevE.95.012307.
