# Attracting cycles of unbounded period in a public-goods opinion–action game

## Finding

In the simultaneous best-response version of the public-goods opinion–action model of Davidson, Zino, Cao, and Ye [1], there are **exponentially attracting, non-equilibrium periodic trajectories of every arbitrarily large prescribed prime period**. The trajectories exist even on strongly connected, fully off-diagonal-positive directed opinion networks. Thus convergence to an equilibrium is **not universal** over all revision sequences covered by the model's stated Assumption 1. The result does not contradict that paper's proved sufficient condition for all-defection convergence.

More precisely, for every integer \(n\ge2\), fix homogeneous parameters
\[
\alpha=\frac1{20},\quad \beta=\lambda=\frac{19}{40},\quad r=\frac{3n}{4},\quad \gamma_i=0,
\]
and activate every player at every integer time. With \(P\) the cyclic permutation on \(n\) vertices, the network \(W=P\) possesses exactly one exponentially attracting orbit for every binary necklace of length \(n\), and no other recurrent trajectories. The number of prime-period-\(m\) orbits, for each positive divisor \(m\mid n\), is
\[
L_m=\frac1m\sum_{d\mid m}\mu(d)\,2^{m/d},
\]
where \(\mu\) is the number-theoretic Möbius function. In particular, the word with exactly one cooperating player has prime period \(n\). For every initial opinion in \([0,1]^n\) and every initial action, the trajectory is exponentially attracted to its uniquely determined necklace orbit.

The cycles persist for every nonnegative row-stochastic **zero-diagonal** \(W\) with
\[
\|W-P\|_\infty<\frac{17}{76},
\]
where the norm is the maximum absolute row sum. Each necklace retains a distinct exponentially locally attracting periodic orbit of its original prime period. An explicit **positive-off-diagonal** example for every \(n\ge3\) is
\[
W=\frac{19}{20}P+\frac1{20}\frac{J-I}{n-1}.
\]
It has zero diagonal and every off-diagonal entry strictly positive; its distance from \(P\) is at most \(1/10<17/76\).

## Assumptions and scope

Players have binary actions \(x_i(t)\in\{0,1\}\) and opinions \(y_i(t)\in[0,1]\); the public-good multiplier satisfies \(1<r<n\). Homogeneous payoff weights \(\alpha,\beta,\lambda>0\) sum to one, the prejudice parameters are zero, and \(W\) is row-stochastic and nonnegative with zero diagonal. At every time all players simultaneously select the best response based on the preceding opinion profile, resolving a tie in favor of defection. These choices are directly permitted by [1], Eqs. (5)–(12) and Assumptions 1–2. Define
\[
a=\frac{\beta}{\beta+\lambda},\qquad b=\frac{\lambda}{\beta+\lambda}=1-a,\qquad
\theta=\frac12+\frac{\alpha(1-r/n)(\beta+\lambda)}{\beta\lambda}.
\]
Assume \(0<a<1\) and \(1/2<\theta<1\). Write \(s(u)=0\) for \(u\le\theta\), and \(s(u)=1\) for \(u>\theta\), applying it componentwise. The original best-response rule is exactly
\[
x(t+1)=s(Wy(t)),\qquad y(t+1)=aWy(t)+b\,s(Wy(t)). \tag{1}
\]
Indeed, the action discriminant in [1] is \(\alpha(r/n-1)+[\beta\lambda/(\beta+\lambda)]((Wy)_i-1/2)\), hence (1). Our displayed parameters give \(a=b=1/2\) and \(\theta=21/38\). The condition \(1<r<n\) holds at every \(n\ge2\).

The permutation \(P\) is defined by \((Pv)_i=v_{i-1}\) with indices cyclic modulo \(n\). A binary necklace is an equivalence class of binary words under cyclic rotation; its primitive length is its least positive rotation period. Exponential attraction means that in a neighborhood of each orbit, distance to the orbit at the corresponding temporal phase converges to zero exponentially; for \(P\) the conclusion is global with phase selected by the initial threshold word.

## Proof

**Step 1: exact global solution on a cyclic network.** For \(W=P\), write \(\sigma=s(y(0))\). Because \(0<a<1\), \(b=1-a\), and \(0<\theta<1\), the scalar function \(f(u)=au+b s(u)\) satisfies \(f([0,\theta])\subseteq[0,\theta)\) and \(f((\theta,1])\subseteq(\theta,1]\). In particular \(s(f(u))=s(u)\), even at the tie \(u=\theta\). The permutation commutes with coordinatewise \(s\). Thus the threshold word evolves exactly by rotation:
\[
s(y(t))=P^t\sigma,\qquad x(t)=P^t\sigma\quad(t\ge1).
\]
Substitution in (1), followed by induction, yields the exact formula for every \(t\ge0\):
\[
y(t)=P^t\bigl[\sigma+a^t(y(0)-\sigma)\bigr]. \tag{2}
\]
Consequently \(\|y(t)-P^t\sigma\|_\infty\le a^t\). Every initial condition converges exponentially to the binary rotating orbit labeled by \(\sigma\); the actions synchronize with the rotating word after one update. The binary words themselves are exact orbits, and distinct rotation classes give distinct orbits. Any recurrent point must lie on a binary orbit: otherwise (2), together with the finite periodicity of \(P^t\sigma\), precludes recurrence to the original nonbinary state. All binary orbits are locally exponentially attracting because each coordinate is a positive distance from \(\theta\). This proves the complete recurrent classification for \(P\).

**Step 2: exact period census.** A word of primitive period \(m\mid n\) is exactly an \(m\)-letter aperiodic binary word repeated \(n/m\) times. By Möbius inversion the number of such labeled words is \(\sum_{d\mid m}\mu(d)2^{m/d}\). Every orbit has exactly \(m\) distinct time phases, proving the formula for \(L_m\). Summation over divisors gives \(n^{-1}\sum_{d\mid n}\varphi(d)2^{n/d}\) orbits in total. The word containing exactly one \(1\) has primitive period \(n\), producing attracting cycles of arbitrarily large prime period.

**Step 3: persistence with genuinely distributed influence.** Fix any binary word \(\sigma\) of primitive period \(m\mid n\), and let \(\sigma_t=P^t\sigma\). Consider the affine, periodically forced system
\[
y_{t+1}=aWy_t+b\sigma_{t+1}. \tag{3}
\]
Its \(m\)-step linear part is \((aW)^m\). Because \(W\) is row-stochastic, \(\|aW\|_\infty=a<1\), so its \(m\)-step map is a contraction and possesses one \(m\)-periodic solution \(y_t^*\), given explicitly by
\[
y_0^*=[I-(aW)^m]^{-1}\;b\sum_{k=1}^m(aW)^{m-k}\sigma_k,
\quad y_t^*=aWy_{t-1}^*+b\sigma_t. \tag{4}
\]
In this formula indices of \(\sigma\) are taken modulo \(m\). Since \(\sigma_{t+1}=P\sigma_t\) and \(a+b=1\), the error \(e_t=y_t^*-\sigma_t\) obeys
\[
e_{t+1}=aWe_t+a(W-P)\sigma_t.
\]
Writing \(\varepsilon=\|W-P\|_\infty\), periodicity and the contraction inequality give
\[
\max_t\|e_t\|_\infty\le\frac{a\varepsilon}{1-a},\qquad
\max_t\|Wy_t^*-P\sigma_t\|_\infty\le\frac{\varepsilon}{1-a}. \tag{5}
\]
If \(\varepsilon<(1-a)\min\{\theta,1-\theta\}\), then (5) implies, *strictly in every coordinate and phase*,
\[
s(Wy_t^*)=P\sigma_t=\sigma_{t+1}.
\]
Thus (3) is the actual discontinuous best-response dynamics (1) on this orbit, not merely a forced surrogate. The strict margins persist under a sufficiently small perturbation of initial opinions. Within that local itinerary cylinder, every \(m\)-step error contracts by \((aW)^m\), proving exponential local attraction. The observed actions have primitive period \(m\), so the full orbit cannot have a smaller period. Two different necklaces cannot label the same orbit, since their action itineraries would then coincide up to a rotation. This proves preservation of all necklace cycles for every qualifying \(W\).

**Step 4: a fully interconnected directed example.** For the displayed homogeneous parameters, \((1-a)\min\{\theta,1-\theta\}=17/76\). Put \(Q=(J-I)/(n-1)\) and \(W=(19/20)P+(1/20)Q\). For \(n\ge3\), this matrix is nonnegative, row-stochastic, has zero diagonal, and has all off-diagonal weights strictly positive, making the directed network strongly connected. The triangle inequality for stochastic rows gives \(\|W-P\|_\infty\le 1/10<17/76\), so Step 3 applies. For \(n=2\), \(Q=P\), and Step 1 applies. All parameters are strictly admissible.

## Verification

Run `python verify_cycles.py` with Python 3 and SymPy. The supplied standalone script uses exact rational arithmetic to check the source-model threshold, all binary words for cyclic networks of sizes \(2\) through \(8\), the exact global solution including threshold ties, the primitive-period divisor condition, and \(12\) distinct rational periodic-orbit constructions for strictly positive off-diagonal matrices of sizes \(3\) through \(6\). These checks are consistency tests, **not** a substitute for the all-size arguments above. The convergence estimate (2), period census, perturbation bounds (5), and contraction are proven analytically.

## Relationship to prior work

Davidson, Zino, Cao, and Ye [1] derive the precise best-response rule used here. Their Assumption 1 explicitly includes simultaneous updates; their published Theorem 2 concerns a *different parameter regime* in which the all-defection action is forced. Their conclusion mentions the prospect of proving universal equilibrium convergence, motivated by simulations. The constructed cycles show that a statement of universal convergence over their full permitted synchronous regime is false; they do **not** refute the restricted theorem, and they do **not** address exclusively single-agent asynchronous revision. Related opinion–action models [2,3] prove convergence under network-potential and activation hypotheses using coordination/anti-coordination payoffs rather than this public-goods payoff; these theorems do not imply equilibrium convergence in (1). Quantized opinion systems and switching maps are well-established broader mathematics, so the novelty asserted here is the exact public-goods-model realization, global symbolic classification for a cyclic network, and robust arbitrary-period cycles on densely connected directed networks, not the general idea that switching systems can cycle.

## Limitations

The claim assumes homogeneous zero-prejudice weights, synchronous updates, and directed nonnegative row-stochastic influence near a cyclic permutation. Global convergence to a periodic orbit is established for the exact permutation, whereas only local attraction of the specified cycles is established for perturbed networks. No claim is made about exclusively single-agent asynchronous revision, symmetric dense networks, every admissible network, stochastic asynchronous activation, or whether additional attractors appear after perturbation. The recurrence-count formula applies to the exact cyclic network, and gives a **lower bound** for nearby networks. Independent validation has not been performed. Wider literature on threshold-coupled maps may contain general results implying pieces of the argument.

## References

[1] E. C. Davidson, L. Zino, M. Cao, M. Ye, *Modelling the coevolution of opinion dynamics and decision making in social dilemmas*, arXiv:2604.08840v1 (first posted 2026-04-10), https://arxiv.org/html/2604.08840v1 .

[2] H. Dehghani Aghbolagh, M. Ye, L. Zino, Z. Chen, M. Cao, *Coevolutionary Dynamics of Actions and Opinions in Social Networks*, arXiv:2206.07242v2, https://arxiv.org/html/2206.07242v2 .

[3] H. Liang, M. Ye, L. Zino, W. Xia, *Coevolution of Actions and Opinions in Networks of Coordinating and Anti-Coordinating Agents*, arXiv:2505.03078v1, https://arxiv.org/html/2505.03078v1 .
