# Endogenous majority amplification in a three-agent bi-layer voter process

## Finding

In the asynchronous two-channel, no-bot specialization of the bi-layer tolerant/intolerant voter process on a complete graph of three agents, suppose initially two agents are in state \(A^-\) and one is in state \(B^-\). For each parameter \(0<\gamma\leq 1\), the probability \(F(\gamma)\) that all agents ultimately hold opinion \(A\) is exactly

\[
F(\gamma)=\frac{10\gamma^4+168\gamma^3+903\gamma^2+1995\gamma+1574}{3(6\gamma^4+94\gamma^3+473\gamma^2+998\gamma+754)}.
\]

In particular,

\[
F(\gamma)-\frac23=\frac{(1-\gamma)(2\gamma^3+22\gamma^2+65\gamma+66)}{3(6\gamma^4+94\gamma^3+473\gamma^2+998\gamma+754)}>0\qquad(0<\gamma<1).
\]

Moreover \(F\) is strictly decreasing throughout \((0,1]\), with \(F(1)=2/3\) and \(\lim_{\gamma\downarrow0}F(\gamma)=787/1131=2/3+11/377\). Thus uniform initial intolerance can favor the initial opinion majority despite assigning identical microscopic rules to all agents: a finite, exactly quantified endogenous majority amplification.

## Assumptions and scope

There are three agents joined by every undirected edge, two opinions \(A,B\), and two tolerance states \(+,-\). An agent state is one of \(A^+,A^-,B^+,B^-\). Time is continuous. Each ordered pair of distinct agents (focal, speaker) has two independent rate-one clocks, called the tolerance and opinion channels. At a tolerance-clock ring, the focal agent adopts the speaker's tolerance sign while retaining its opinion. At an opinion-clock ring with distinct opinions, a tolerant focal agent changes to the speaker's opinion at rate one and remains tolerant, while an intolerant focal agent changes to the speaker's opinion at relative rate \(\gamma\) and becomes tolerant. When the opinions agree the opinion clock does nothing. Equivalently, opposite-opinion copying occurs at rate \(1\) or \(\gamma\) according to the focal tolerance. All channels are independent. Their common rate scale does not affect absorption probabilities. This fixes an asynchronous continuous-time realization of the two layers of the rules in Vega-Oliveros and collaborators (2022), not every conceivable simultaneously coupled update scheme.

Consensus is the first time the three opinions all agree, irrespective of their possibly differing tolerance signs. The claimed probability concerns exactly the initial count vector \((n_{A^+},n_{A^-},n_{B^+},n_{B^-})=(0,2,0,1)\), up to permutation of labeled agents. The parameter range is \(0<\gamma\leq1\); the endpoint \(\gamma=0\) is excluded from the absorption statement.

## Proof

Let \(s=(a_+,a_-,b_+,b_-)\) be the count vector, with entries summing to three. Its transitions depend only on counts. Index the four types by \(u=0,1,2,3\) in that order. The number of ordered distinct focal/speaker pairs of types \(u,v\) is \(s_u(s_v-\mathbf 1_{u=v})\). For each such pair, the tolerance-copy destination type is \(2\lfloor u/2\rfloor+(v\bmod 2)\) at unit rate when it differs from \(u\). If the opinions differ, the opinion-copy destination is \(2\lfloor v/2\rfloor\), at rate one for an even \(u\) (tolerant), and rate \(\gamma\) for an odd \(u\) (intolerant). These rules specify all off-diagonal generator entries; the diagonal is minus the row sum.

All eight consensus-opinion count states have prescribed hitting probability one (for \(b_++b_-=0\)) or zero (for \(a_++a_-=0\)). There are exactly twelve nonconsensus count states. Set

\[
D(\gamma)=754+998\gamma+473\gamma^2+94\gamma^3+6\gamma^4,
\]

and define a polynomial \(N_s(\gamma)\) by the following coefficient table. Each five-tuple gives coefficients of \(1,\gamma,\gamma^2,\gamma^3,\gamma^4\) in increasing degree. The order of components in \(s\) is \((a_+,a_-,b_+,b_-)\).

| \(s\) | coefficients of \(N_s\) |
|---|---|
| \((0,1,0,2)\) | \((688,999,516,114,8)\) |
| \((0,1,1,1)\) | \((886,996,387,54,2)\) |
| \((0,1,2,0)\) | \((1112,965,234,14,0)\) |
| \((0,2,0,1)\) | \((1574,1995,903,168,10)\) |
| \((0,2,1,0)\) | \((1844,2090,668,48,0)\) |
| \((1,0,0,2)\) | \((418,904,751,234,18)\) |
| \((1,0,1,1)\) | \((566,981,612,154,12)\) |
| \((1,0,2,0)\) | \((754,998,473,94,6)\) |
| \((1,1,0,1)\) | \((1376,1998,1032,228,16)\) |
| \((1,1,1,0)\) | \((1696,2013,807,128,6)\) |
| \((2,0,0,1)\) | \((1150,2029,1185,268,18)\) |
| \((2,0,1,0)\) | \((1508,1996,946,188,12)\) |

Let \(H(s)=N_s(\gamma)/(3D(\gamma))\) on these twelve transient states; at consensus boundaries use the numerators \(3D\) or zero. Direct multiplication of the generator by this candidate shows that for **every** transient state \(s\),

\[
\sum_{t\neq s}q_{st}(\gamma)\bigl(N_t(\gamma)-N_s(\gamma)\bigr)=0
\]

as a polynomial identity, with coefficients of degrees zero through five all zero. The accompanying `verify.py` computes all twelve equations by exact integer-polynomial arithmetic from the specified rules, independently of any matrix inversion. Because \(\gamma>0\), from every nonconsensus state there exists a positive-rate path of finitely many opinion-copy events leading to some consensus. A finite continuous-time Markov chain with this reachability has no closed nonconsensus communicating class and hits a consensus class almost surely. Hence the Dirichlet hitting-probability problem has a unique solution: the displayed \(H\) is the actual probability of consensus on \(A\).

For \(s=(0,2,0,1)\) this yields the stated formula. Subtracting \(2/3\) and factoring gives the strictly positive expression in the Finding section. Differentiating yields

\[
F'(\gamma)=-\frac{68\gamma^6+1376\gamma^5+11388\gamma^4+47348\gamma^3+106293\gamma^2+127280\gamma+66622}{3D(\gamma)^2}<0.
\]

All coefficients in the numerator and denominator are positive for \(\gamma>0\). Substitution and a one-sided limit give the two endpoint values. At \(\gamma=1\) every focal agent copies the opposed opinion at the same unit rate regardless of tolerance, and the initial opinion frequency \(2/3\) is a martingale, providing a separate classical voter-model check.

## Verification

Run `python3 verify.py` in the directory containing this result and the script. Only the Python standard library is needed. The checker enumerates every ordered distinct-type interaction for all twelve transient states and verifies exact zero generator residuals coefficient by coefficient, confirms the majority-gain factorization, and checks the values at \(\gamma=1\) and \(\gamma\downarrow0\). This is an algebraic certificate for every parameter in the stated interval, not an inference from a finite sampling of parameter values. The unique-solvability argument above is the noncomputational step linking the identities to absorption probabilities.

## Relationship to prior work

Vega-Oliveros, Grande, Iannelli, and Vazquez introduce a bi-layer model separating tolerance and opinion copying and study its mean-field equations and simulated opinion dynamics. The present finding focuses on a finite, three-agent no-bot realization of those two channels and supplies exact absorption probabilities not inferred from mean-field equilibria or simulation trajectories. The older confident-voting model of Volovik and Redner is a different stochastic rule in which additional opposite contacts are required to overturn confidence, rather than copying a second tolerance layer independently; its results do not directly determine this rational function.

## Limitations

The formula applies to exactly three agents with the specified asynchronous channel rates and initial all-intolerant two-versus-one opinion state; no formula is claimed for arbitrary networks, concurrent coupled-layer updates, or heterogeneous contact rates. The endpoint \(\gamma=0\) is singular because a fully intolerant mixed configuration may remain frozen; \(787/1131\) is the limit from strictly positive \(\gamma\), not the unconditional absorption probability at zero. Literature overlap may remain in specialized finite-state voter-model work not indexed by the searches performed. An independent audit has not been performed.

## References

1. L. Vega-Oliveros, S. Grande, F. Iannelli, and F. Vazquez, *Bi-layer voter model: Modeling intolerant/tolerant positions and bots in opinion dynamics*, arXiv:2201.02218 (first submitted 2022-01-06), especially the microscopic copying rules, mean-field equations, and Appendix A. https://arxiv.org/abs/2201.02218
2. D. Volovik and S. Redner, *Dynamics of Confident Voting*, arXiv:1111.3883 (2011). https://arxiv.org/abs/1111.3883
