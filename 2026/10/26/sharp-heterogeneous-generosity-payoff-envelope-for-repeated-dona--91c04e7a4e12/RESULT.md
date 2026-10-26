# Sharp heterogeneous-generosity payoff envelope for repeated donation games

## Finding

A population's mean generosity is not in general enough to compute its repeated-game payoff. In the donation-game version of generous tit-for-tat (GTFT) described below, replacing independently drawn individual generosity values by their common mean **always overestimates** expected GTFT-versus-GTFT payoff, except when generosity is constant. This difference does not vanish simply by increasing the population size while its generosity law stays nondegenerate. At a given mean and known interval of admissible generosity, the largest overestimate is attained by a unique two-point law supported on the interval endpoints.

More precisely, fix a benefit \(b>c>0\), a continuation probability \(0<\delta<1\), and a maximum generosity \(0<G\leq1\). Let \(U,V\) be independent identically distributed generosity parameters with law \(\nu\) on \([0,G]\). In each repeated donation game the players cooperate initially with probability \(1/2\), independently, and subsequently cooperate with probability \(1\) after the other player cooperated or with probability equal to their own generosity after the other player defected. Each round has payoffs \((b-c,-c,b,0)\) for states \((CC,CD,DC,DD)\), and another round occurs independently with probability \(\delta\). Let \(f(u,v)\) be the expected total payoff to the first player, and \(\bar u=\mathbb E U\).

Define the **homogenization overestimate**
\[
\Delta(\nu)=f(\bar u,\bar u)-\mathbb E f(U,V).
\]
Put \(X=1-U\), \(\mu=\mathbb E X\), \(\sigma^2=\operatorname{Var}(X)\), \(L=1-G\), \(H=1\), and \(\vartheta=(\mu-L)/(H-L)\). Then
\[
\boxed{\quad \frac{(b-c)\delta^3}{2}\,\mu\sigma^2\ \leq\ \Delta(\nu)\ \leq\ \frac{b-c}{2}\left[\mathcal E_{L,H}(\vartheta)-\frac{1}{1-\delta\mu}\right],\quad}
\]
where
\[
\mathcal E_{L,H}(\vartheta)=
\frac{(1-\vartheta)^2}{1-\delta L}
+\frac{\vartheta^2}{1-\delta H}
+\frac{2\vartheta(1-\vartheta)\bigl(1+\delta(L+H)/2\bigr)}{1-\delta^2 LH}.
\]
For \(0<\vartheta<1\), the exact minimum of \(\Delta\) over all such laws with fixed \(\mu\) is \(0\), attained only by the constant law; the exact maximum is the displayed upper endpoint, attained only by the law giving probability \(1-\vartheta\) to \(U=G\) and probability \(\vartheta\) to \(U=0\). For a nonconstant law, \(\Delta>0\). The stated variance lower bound is asymptotically sharp as \(\delta\downarrow0\):
\[
\Delta(\nu)=\frac{b-c}{2}\,\mu\sigma^2\delta^3+O(\delta^4).
\]
Furthermore, \(\Delta\) increases under convex-order spreading of the law of \(X=1-U\) at fixed mean.

In the incremental-generosity-tuning protocol of Alistarh, Chatterjee, Karrabi and Lazarsfeld (2023), the stationary generosity law assigns strictly positive weights proportional to \(((1-\beta)/\beta)^j\) to \(jG/(k-1)\), for \(j=0,\ldots,k-1\), whenever \(0<\beta<1\), \(k\geq2\), and \(G>0\). Consequently its stationary GTFT-pair homogenization gap is strictly positive for every such choice. For the unbiased two-level law with \(k=2\), \(\beta=1/2\), \(G=1\), \(b=3\), \(c=2\), \(\delta=1/2\), its exact value is \(1/48\): the homogeneous calculation gives \(4/3\) while the heterogeneous pair payoff is \(21/16\).

## Assumptions and scope

The repeated-game payoff is the *sum* of payoffs over a geometrically stopped sequence of rounds (not the undiscounted stationary per-round payoff). The two GTFT parameters are sampled independently from the same distribution; the claim does not cover assortative pairing, negatively correlated generosity or opponent distributions different from the focal population. The donation payoff condition \(b>c>0\), common first-round cooperation probability \(1/2\), GTFT reactive rule and \(0<\delta<1\) are essential to the proof. The sharp-envelope comparison fixes both the generosity support interval and the mean; no finite-support assumption is made. The number of individuals does not enter the iid-pair comparison. The IGT specialization concerns pairs sampled from its product-form stationary generosity law, not transient strategic distributions.

## Proof

**1. Exact pair payoff.** Index joint actions by \((CC,CD,DC,DD)\). If the first player has generosity \(u\) and the second \(v\), the conditional next-round transition matrix is
\[
M=\begin{pmatrix}
1&0&0&0\\
u&0&1-u&0\\
v&1-v&0&0\\
uv&u(1-v)&v(1-u)&(1-u)(1-v)
\end{pmatrix}.
\]
The initial state distribution is \(q=(1/4,1/4,1/4,1/4)\), and the row-player donation reward vector is \(r=(b-c,-c,b,0)^{\mathsf T}\). Since \(\delta<1\), the inverse \((I-\delta M)^{-1}\) exists. Direct multiplication of \(q(I-\delta M)^{-1}r\) gives
\[
f(u,v)=\frac{b-c}{1-\delta}+\frac{c\delta(1-u)-b\delta(1-v)+c-b}{2\bigl(1-\delta^2(1-u)(1-v)\bigr)}.
\tag{1}
\]
This is the pairwise formula established in the motivating paper; it is independently checked by exact rational matrix inversion in the included verification script. It is *not* claimed as new.

**2. Symmetric independent pairing.** Write \(Y=1-V\), an independent copy of \(X\). Averaging (1), and exchanging \(X\) and \(Y\) in one of the two symmetric terms, yields
\[
\mathbb E f(U,V)=\frac{b-c}{1-\delta}-\frac{b-c}{2}\,\mathbb E\Psi(X,Y),
\quad \Psi(x,y)=\frac{1+\delta(x+y)/2}{1-\delta^2xy}.
\]
For the constant law at \(\mu\), \(\Psi(\mu,\mu)=1/(1-\delta\mu)\). Thus
\[
\Delta(\nu)=\frac{b-c}{2}\left(\mathbb E\Psi(X,Y)-\frac1{1-\delta\mu}\right).
\tag{2}
\]

**3. Nonnegative moment expansion.** Put \(m_j=\mathbb E X^j\) with \(m_0=1\). Since \(0\leq X,Y\leq1\) and \(\delta<1\), the geometric expansion converges absolutely and uniformly, so independence and bounded convergence give
\[
\mathbb E\Psi(X,Y)
=\sum_{j=0}^{\infty}\delta^{2j}\bigl(m_j^2+\delta m_jm_{j+1}\bigr).
\tag{3}
\]
Jensen's inequality implies \(m_j\geq\mu^j\) for every integer \(j\geq1\); all summands in the difference between (3) and its constant-law version are nonnegative. The first strictly positive possible summand is the \(\delta^3\) contribution \(\mu(m_2-\mu^2)=\mu\sigma^2\). This proves the variance bound and strict positivity for any nonconstant law: a nonconstant \(X\geq0\) necessarily has \(\mu>0\). Boundedness of the moments gives a uniform \(O(\delta^4)\) remainder for \(\delta\) in a fixed interval below \(1\), proving sharp leading order. If two laws have the same mean and are ordered by convex order, all their moments of integer order at least one are similarly ordered, proving monotonicity of (2).

**4. Sharp endpoint extremizers.** For \(x\in[L,H]\), each convex monomial \(x^j\), \(j\geq1\), lies below its chord between the endpoints:
\[
x^j\leq\frac{H-x}{H-L}L^j+\frac{x-L}{H-L}H^j.
\]
Taking expectations, each moment \(m_j\) is bounded by the corresponding moment of the two-point endpoint law of mean \(\mu\). Every term in (3) is coordinatewise increasing in the nonnegative moments. Hence the endpoint law maximizes \(\mathbb E\Psi\), whereas the constant law minimizes it. Substituting the endpoint law into the two-variable kernel gives exactly \(\mathcal E_{L,H}(\vartheta)\). Equality at the upper bound for non-endpoint means requires equality in the chord bound for \(x^2\), forcing support on \(\{L,H\}\); equality at the lower bound forces zero variance and thus a constant law. Both extremizers have the prescribed mean, proving sharpness.

**5. Stationary protocol specialization.** The 2023 IGT multinomial stationary law has one-agent probability \(p_j\propto((1-\beta)/\beta)^j\) at generosity \(jG/(k-1)\), \(j=0,\ldots,k-1\). With \(0<\beta<1\), \(k\geq2\), \(G>0\), the law is nonconstant, so step 3 gives strict payoff overestimation for independent stationary draws. For the stated two-point numerical parameters, direct evaluation of (1) at all four ordered pairs gives \(\mathbb E f(U,V)=21/16\), while \(f(1/2,1/2)=4/3\), hence \(\Delta=1/48\).

## Verification

Run `python3 verify.py` with Python 3 and no third-party dependencies. Its independent four-state rational linear-system solver checks the pair payoff against (1) at \(108\) parameter pairs; it checks the sharp-envelope and variance bounds for rational three-point laws at three continuation probabilities, tests the strict stationary IGT specialization, and checks the displayed \(1/48\) example. The test run returned `VERIFIED 346 exact-rational assertions; illustration gap = 1/48`. The uncountable-distribution and infinite-series assertions rest on steps 2–4, not finite tests.

## Relationship to prior work

Alistarh, Chatterjee, Karrabi and Lazarsfeld (arXiv:2307.07297, first posted July 14, 2023) introduced the IGT population dynamics, proved the multinomial stationary law and explicitly derived the pair payoff (1), including their donation-game equation (44). They compared the full heterogeneous-pair payoff and a homogeneous average-generosity payoff numerically in their Section 6.3.3. These results and the source's proposed payoff calculation are prior art. The additional claim here is the universal *sign*, its positive variance certificate, convex-order monotonicity, and a sharp distribution-free envelope with unique extremal laws, none of which is stated in those inspected sections.

Núñez Rodríguez and Neves (arXiv:1509.01225, 2015) analytically classified replicator regimes for three reactive strategies in an infinitely repeated game; this is a different population process and payoff objective. Nowak and Sigmund (Nature 355, 250–253, 1992) studied heterogeneous reciprocity and the emergence of generosity, but the accessible abstract does not establish the stated sharp envelope. The exact Markov formula plus classical moment convexity are substantial acknowledged ingredients; this is not a claim of new Markov-chain inversion or new Jensen theory.

## Limitations

The result concerns the particular donation-game GTFT kernel and independent identically distributed generosity at a fixed time. It does not show that heterogeneity harms cooperation in *every* repeated game, or that an intervention increasing homogeneity improves evolutionary fitness, nor does it characterize dynamic equilibrium selection. Homogeneous-pair mean-field substitution is being assessed, not the exact multinomial distribution itself. The earliest motivating source is verifiably from 2023; broader priority under alternative terminology, especially other heterogeneous-strategy repeated-game work, is not independently certified.

## References

1. Dan Alistarh, Krishnendu Chatterjee, Mehrdad Karrabi and John Lazarsfeld, *Game Dynamics and Equilibrium Computation in the Population Protocol Model*, arXiv:2307.07297 (2023), https://arxiv.org/abs/2307.07297. See Sections 1.3, 2.2, 6.1 and 6.3.3.
2. Irene Núñez Rodríguez and Armando G. M. Neves, *Evolution of cooperation in a particular case of the infinitely repeated Prisoner's Dilemma with three strategies*, arXiv:1509.01225 (2015), https://arxiv.org/abs/1509.01225.
3. Martin A. Nowak and Karl Sigmund, *Tit for tat in heterogeneous populations*, Nature 355 (1992), 250–253, https://doi.org/10.1038/355250a0.
4. Per Molander, *The Optimal Level of Generosity in a Selfish, Uncertain Environment*, Journal of Conflict Resolution 29 (1985), 611–618, https://doi.org/10.1177/0022002785029004004.
