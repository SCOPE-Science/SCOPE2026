# Scientific review: dyadic consensus atoms and a uniform weak limit

## Correctness — PASS

The two independent Bernoulli directional choices produce, at any fixed opinion gap, no selection, one-sided selection, or two-sided selection with the probabilities explicitly calculated in RESULT.md. Eliminating idle rounds yields a geometric waiting time and a stopped binary subdivision of the initial interval. Independent fair branch choices give each distinct midpoint at depth \(k\) mass \(S_k s_k/2^k\). The stopping depth is almost surely finite because its conditional stopping probability is bounded below by the positive initial one. Conditional midpoint-grid moments yield the exact variance, and stagewise holding times give the exact expected consensus time. At fixed finite levels the stopping chance tends to zero as confidence width vanishes; coupling each dyadic midpoint to uniform mass on its interval proves weak uniform convergence. Fixed-confidence atomicity gives total variation one. The first-stage geometric waiting time supplies the exact Arrhenius prefactor, since the sum of later-stage expected waiting times is exponentially smaller. All hypotheses and limits appear explicitly in the result; numerical checks are supportive, not substitutes for these arguments.

## Originality — PASS, subject to historical priority

The October 2026 motivating work provides the logistic inclusion rule and simulation outcomes, but not the state-dependent two-agent exact distribution, its purely atomic law, its singular continuous weak limit or the sharp time prefactor. Mäs, Flache and Helbing (2016) already describe positive-probability cross-group contact and eventual consensus in related simulations, so eventual consensus is not claimed to be the novel ingredient. Elboim, Peres and Peretz (2024) study consensus times and variance for fixed-kernel asynchronous DeGroot averaging; their exact dynamics, population assumptions and time asymptotics are different. Shi, Johansson and Johansson (2012) analyze unreliable randomized gossip but do not give the logistic state-dependent stopped-dyadic law in the accessible material. Targeted mathematical-record searches and checked accessible historical claims did not expose an implication-equivalent prior theorem. General stopped-dyadic-process mathematics and specialized stochastic gossip literature remain residual coverage risks. The comparative claim is priority-provisional, not certification of unique novelty.

## Mathematical value — PASS

The paired properties are not a routine statement of eventual consensus. The exact law shows that at any strictly positive confidence width the random consensus outcome lives on a countable dense atomic set, while at vanishing width it becomes almost indistinguishable from uniform by weak observables even though total variation never approaches zero. The sharp \(e^{\beta d/\varepsilon}\) waiting-time prefactor quantitatively reconciles nearly frozen simulated polarization with eventual exact agreement. Both the output law and the time law are natural quantities for validating inference and stopping criteria for this specific stochastic social-influence rule. The result is restricted to two agents, independent directional sampling and unweighted midpoint influence; it makes no general-population convergence claim.

## Closest sources and limits

Relevant sources: Giaquinta–Hernández–Chavalarias (arXiv:2610.07971v1, 2026), Mäs–Flache–Helbing (JASSS 19(4), 2016), Elboim–Peres–Peretz (Random Structures & Algorithms 65, 2024), and Shi–Johansson–Johansson (arXiv:1203.6028). The mathematical proof is self-contained; historical priority outside inspected sources is not independently established.

Self-review: passed. Independent audit: not yet performed.
