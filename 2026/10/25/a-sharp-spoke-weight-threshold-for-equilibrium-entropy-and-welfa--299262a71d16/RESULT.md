# A sharp spoke-weight threshold for equilibrium entropy and welfare in wheel anti-coordination games

## Finding

Consider a binary anti-coordination game on the labeled wheel \(K_1*C_m\), where \(m\ge3\), the \(m\) rim edges have weight \(1\), the \(m\) spokes have weight \(\lambda>0\), and each player's payoff equals the total weight of incident edges joining opposite actions. A pure Nash equilibrium (PNE) allows indifferent deviations; a strict PNE requires every unilateral switch to decrease the deviator's payoff.

Let \(P_0=3\), \(P_1=0\), \(P_2=2\), \(P_m=P_{m-2}+P_{m-3}\) be the Perrin numbers, and \(L_0=2\), \(L_1=1\), \(L_m=L_{m-1}+L_{m-2}\) be the Lucas numbers. The number \(N_m(\lambda)\) of labeled binary-action PNE, counting both global action inversions, is exactly

\[
\boxed{N_m(\lambda)=\begin{cases}
2P_m,&0<\lambda<2,\\
2L_m,&\lambda=2,\\
2,&\lambda>2.
\end{cases}}
\]

The corresponding strict PNE count is \(2P_m-4\mathbf1_{2\mid m}\) for \(0<\lambda<2\), zero for \(\lambda=2\), and two for \(\lambda>2\). Thus the equilibrium growth exponent jumps from \(\log\alpha\) to \(\log\varphi\) and then to zero at the exact spoke-weight threshold \(2\), where \(\alpha\) is the positive root of \(t^3-t-1=0\) and \(\varphi=(1+\sqrt5)/2\). The exponent here is precisely \(\lim_{m\to\infty}m^{-1}\log N_m(\lambda)\), evaluated at fixed \(\lambda\).

For \(0<\lambda<2\), put \(z\) for the number of rim players using the hub's action. The feasible values are precisely \(\lceil m/3\rceil\le z\le\lfloor m/2\rfloor\), and the number of PNE for each \(z\) is

\[
\boxed{N_{m,z}(\lambda)=\frac{2m}{z}\binom{z}{m-2z}.}
\]

At \(\lambda=2\), the feasible values are \(0\le z\le\lfloor m/2\rfloor\), with

\[
\boxed{N_{m,z}(2)=\frac{2m}{m-z}\binom{m-z}{z}.}
\]

For \(\lambda>2\), both equilibria have \(z=0\). Every PNE in the first regime has social welfare \(2[\lambda m+(2-\lambda)z]\); every PNE at the threshold has welfare \(4m\), and every PNE in the final regime has welfare \(2\lambda m\).

The maximum social welfare is twice the maximum weighted cut, with

\[
C_m^*(\lambda)=\lambda m+(2-\lambda)_+\lfloor m/2\rfloor.
\]

Here \(t\)_+=\max\{t,0\}. All welfare maximizers are PNE, so the price of stability is \(1\) for every positive \(\lambda\). The exact welfare price of anarchy is

\[
\boxed{\mathrm{PoA}_m(\lambda)=\begin{cases}
\dfrac{\lambda m+(2-\lambda)\lfloor m/2\rfloor}
{\lambda m+(2-\lambda)\lceil m/3\rceil},&0<\lambda<2,\\[5pt]
1,&\lambda\ge2.
\end{cases}}
\]

For each fixed \(0<\lambda<2\), its limit as \(m\to\infty\) is \(3(\lambda+2)/[4(\lambda+1)]\); in particular the unweighted wheel limit is \(9/8\).

## Assumptions and scope

The graph has one distinguished hub \(h\) and the rim vertices \(v_0,\dots,v_{m-1}\), with rim indices modulo \(m\). There is one edge between consecutive rim vertices and one edge from \(h\) to each rim vertex; there are no other edges. All vertices have exactly two available actions, \(0\) and \(1\). On each edge of weight \(w>0\), both endpoints receive payoff \(w\) if their actions differ and zero if their actions agree. Players can only change their own action. A PNE means that no single player has a *strictly profitable* change; indifferent changes do not exclude an equilibrium. The strict notion requires a *strictly positive* payoff advantage for retaining the current action for every player. Welfare is the sum of vertex utilities, so it is exactly twice the weight of the associated action cut. Counting concerns all labeled profiles: no rotation, reflection, or global color-inversion quotient is taken.

## Proof

**1. Local best responses.** Fix a hub action, and encode each rim vertex by \(x_i=1\) if it opposes the hub and \(x_i=0\) if it agrees. Let \(z\) count zeros. The hub obtains \(\lambda(m-z)\), whereas changing its action yields \(\lambda z\); the hub is stable exactly when \(z\le m/2\), strictly stable when \(z<m/2\).

For a rim vertex with \(x_i=0\), write \(k\in\{0,1,2\}\) for its number of rim neighbors with \(x=1\). Retaining the action pays \(k\); switching pays \(\lambda+2-k\). Its best-response condition is \(2k\ge\lambda+2\). Consequently a zero requires *two neighboring ones* when \(0<\lambda\le2\), and is impossible when \(\lambda>2\). For a rim vertex with \(x_i=1\), let \(\ell\in\{0,1,2\}\) count neighboring ones. Retaining the action pays \(\lambda+2-\ell\); switching pays \(\ell\), so its condition is \(\lambda+2\ge2\ell\). When \(0<\lambda<2\), this prohibits exactly the case \(\ell=2\), namely a cyclic occurrence of \(111\). At \(\lambda\ge2\), every one is stable.

**2. Complete configuration classification.** For \(0<\lambda<2\), zeros are isolated and no three consecutive rim symbols can be ones. The all-one rim is excluded. Therefore successive zeros, read cyclically, are separated by either one or two ones; equivalently the cyclic zero-to-zero gap lengths are \(2\) and \(3\). This forces \(\lceil m/3\rceil\le z\le\lfloor m/2\rfloor\), automatically satisfying the hub constraint. Conversely, every cyclic sequence of gaps of length \(2\) or \(3\) satisfies all players' best responses. At \(\lambda=2\), only isolated zeros are required, with no upper limit on runs of ones; the empty zero set is allowed. The hub constraint again follows automatically. At \(\lambda>2\), all rim players must oppose the hub. There are precisely two global inversions, and each is a strict PNE.

**3. Exact multiplicity and entropy.** In the first regime, exactly \(m-2z\) of the \(z\) successive zero-to-zero gaps have length \(3\); the others have length \(2\). Choose their locations in \(\binom{z}{m-2z}\) ways, choose a starting zero among the \(m\) labeled vertices, and divide by \(z\) for the choices of which zero was designated first. There are \(m\binom{z}{m-2z}/z\) rim profiles per hub, giving the first refined formula after multiplying by two. These cyclic gap words are closed walks of length \(m\) in the three-state directed graph with arrows \(A\to B\), \(B\to A,C\), \(C\to A\). Its adjacency matrix has characteristic polynomial \(t^3-t-1\), and its traces in powers \(0,1,2\) are \(3,0,2\); hence the trace at exponent \(m\) is \(P_m\). This establishes \(2P_m\) exactly, not merely asymptotically.

At \(\lambda=2\), choose \(z\) nonadjacent zero sites on the labeled cycle. For \(z\ge1\), their number is \(m\binom{m-z-1}{z-1}/z=m\binom{m-z}{z}/(m-z)\). The same final expression yields one profile at \(z=0\). The number of all cycle independent sets is \(L_m\), as follows from the trace of the independent-set transfer matrix \(\left(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\right)\), whose trace powers start \(2,1\) and satisfy the Fibonacci recurrence. Multiplying by two counts the hub action. The dominant roots yield the entropy exponents stated above.

**4. Strict equilibria.** For \(0<\lambda<2\), all rim-player equilibrium inequalities are strict. The hub is indifferent only when \(m\) is even and \(z=m/2\), in which case the zero sites alternate around the rim. There are exactly two alternating rim profiles for each of the two hub choices, hence exactly four non-strict PNE. At \(\lambda=2\), any equilibrium containing a zero has an indifferent zero, while an all-one rim has indifferent ones; therefore no PNE is strict. For \(\lambda>2\), both all-one-rim equilibria are strict, including at the hub.

**5. Welfare and extrema.** If the zero sites are isolated, every zero creates exactly two disagreeing rim edges, while the \(m-z\) ones create the disagreeing spokes. Thus the weighted cut has value \(\lambda(m-z)+2z=\lambda m+(2-\lambda)z\). This gives all equilibrium welfare levels and shows that the worst PNE at \(0<\lambda<2\) has \(z=\lceil m/3\rceil\); all those values occur by the gap construction.

To optimize over *all* action profiles, first consider \(0<\lambda<2\). If a zero has a zero rim neighbor, changing that zero to one increases the cut weight by at least \(\lambda>0\); hence any global maximizer has isolated zeros. Among such profiles \(\lambda m+(2-\lambda)z\) increases with \(z\), and the largest possible \(z\) is \(\lfloor m/2\rfloor\). These optimal configurations belong to the PNE classification because their cyclic gaps are lengths \(2\) or \(3\). When \(\lambda=2\), changing any zero to one never reduces the cut weight, and the all-one rim has cut weight \(2m\), attained by every independent zero set. For \(\lambda>2\), changing any zero to one strictly improves the cut weight, so the all-one rim is the unique optimum for either hub action. The maximum-cut and price formulas follow, with welfare being twice cut weight. Since every global cut maximum is a PNE, the price of stability is one. Finally \(\lfloor m/2\rfloor/m\to1/2\) and \(\lceil m/3\rceil/m\to1/3\), giving the claimed price-of-anarchy limit.

## Verification

Run `python3 verify.py` using Python's standard library only. The included checker enumerates both hub choices and every binary rim profile for each \(m=3,\ldots,14\) and the six rational spoke weights \(\lambda\in\{1/2,1,199/100,2,201/100,5\}\). It evaluates player payoffs directly, both weak and strict deviation tests, the weighted cut for all configurations, the full equilibrium histogram by \(z\), and the exact welfare extrema. The comparison uses exact `Fraction` arithmetic and integer binomial coefficients, rather than floating-point thresholds. All 72 size/weight cases, totaling 393,120 profiles, passed. Independent arithmetic recurrence checks for the Perrin/Lucas count identities passed for every \(3\le m\le299\). The unbounded-size assertions are proved above; finitely many computations alone could not certify them.

## Relationship to prior work

Sánchez Muñoz and Mc Gettrick (2021) explicitly enumerate Nash equilibria in two-choice anti-coordination games on ladder and circular-ladder graphs; those graphs have no universal hub, and their formula does not imply the weighted-wheel counts, strict-equilibrium thresholds, or welfare price of anarchy here. The paper explicitly classifies its game-theoretic results under MSC \(91A43\).

Qiu and collaborators (2023) analyze existence and convergence for networked anti-coordination games using threshold-driven graphical dynamics; their general existence and potential arguments do not provide the exact weighted-wheel multiplicities or efficiency spectrum. Deligkas and collaborators (2023) formalize binary-action polymatrix anti-coordination games and compare computational difficulty of welfare and equilibrium optimization on general networks. Their general hardness and potential-game observations motivate, but do not supply, the complete exact phase diagram for this family. In particular the implication that the largest cut is a PNE is standard for symmetric cut games and is *not* presented as an original result by itself.

Equivalently, the equilibria here are the one-vertex-flip local maxima of the weighted cut on the wheel, or the zero-temperature single-spin-flip stable configurations of an antiferromagnetic Ising model with rim and spoke couplings. The Perrin and Lucas recurrences are classical integer sequences. Their independent existence is not the novelty claim: the new claim is the exact joint wheel-game classification including the spoke-weight phase transition, refined state counts, strictness, and the complete welfare efficiency law.

## Limitations

Only two actions, identical payoff interests along each undirected edge, uniform positive spoke weight, uniform unit rim weight, and labeled wheels with at least three rim vertices are covered. Weak-equilibrium counts at the exact tie parameter \(\lambda=2\) depend on permitting indifference; a rule that excludes ties would change the result. No conclusions are claimed for weighted rims, directed influences, mixed equilibria, noisy revisions, or non-wheel graphs. Exact claims are proved, but novelty relative to all unindexed literature, especially older zero-temperature spin-system enumerations, is not independently certified.

## References

1. V. Sánchez Muñoz and M. Mc Gettrick, *Nash Equilibria in certain two-choice multi-player games played on the ladder graph*, arXiv:2101.09103, first publicly submitted 2021-01-22. https://arxiv.org/abs/2101.09103
2. Z. Qiu, C. Chen, M. V. Marathe, S. S. Ravi, D. J. Rosenkrantz, R. E. Stearns and A. Vullikanti, *Networked Anti-Coordination Games Meet Graphical Dynamical Systems: Equilibria and Convergence*, arXiv:2301.02889, first publicly submitted 2023-01-07. https://arxiv.org/abs/2301.02889
3. A. Deligkas, E. Eiben, G. Gutin, P. R. Neary and A. Yeo, *Some coordination problems are harder than others*, arXiv:2311.03195, first publicly submitted 2023-11-06. https://arxiv.org/abs/2311.03195
