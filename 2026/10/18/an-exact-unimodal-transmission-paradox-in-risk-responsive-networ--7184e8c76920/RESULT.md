# An exact unimodal transmission paradox in risk-responsive network SIR

## Finding

Consider synchronous susceptible-infectious-recovered (SIR) transmission with one-step infectious periods and instantaneous threshold-based preventive behaviour. There is a connected eight-vertex contact network, with one initial infectious vertex and all other vertices initially susceptible, on which the expected eventual number of cases is **strictly unimodal** in the per-edge transmission probability \(\beta\in[0,1]\). In particular, raising \(\beta\) from \(4/5\) to \(1\) **reduces** the mean final case count from \(7267213/1953125\) to exactly \(3\). The law holds unchanged throughout a nonempty open range of genuinely mixed social/infection awareness responses, with **any** undirected social graph of positive degrees. An explicit family of connected networks of unbounded size has the same nonmonotonicity mechanism.

For the eight-vertex graph and all parameters in the open region specified below,
\[
F(\beta)=\mathbb E[Z_\infty]
=1+2\beta+2\beta^2(1-\beta)
 \left(1+4\beta+6\beta^2(1-\beta)^2+6\beta^3(1-\beta)^3\right).
\]
Its unique interior maximizer \(\beta_*\approx0.794710107785494\) is the only root in \((0,1)\) of \(F'(\beta)=0\); the maximum is \(F(\beta_*)\approx3.721192164484\).

## Assumptions and scope

At the start of each discrete step, a susceptible vertex \(i\) becomes protected precisely when
\[
(1-\alpha)\frac{a_i}{d_i^{\mathrm{soc}}}
+\alpha\frac{k_i}{d_i^{\mathrm{con}}}>\Theta,
\]
where \(a_i\) is the number of aware social neighbours and \(k_i\) is the number of infectious contact neighbours. Social and contact degrees are positive. All awareness states are simultaneously recomputed each step, before infection transitions. Protected susceptibles are fully immune for that step. Unprotected susceptibles with \(k_i\) infectious contact neighbours are infected, independently conditional on the current configuration, with probability \(1-(1-\beta)^{k_i}\). Every currently infectious person then recovers with certainty; newly infected persons become infectious at the next step, and recovered persons never return to susceptibility. The output \(Z_\infty\) counts the initial case and all subsequent infections. This is an exact finite-population stochastic process, not a mean-field approximation.

For the canonical eight-vertex *contact* graph, name vertices \(o,a,b,d,h,v_1,v_2,v_3\). Its edges are
\[
\{oa,ob,ad,bd,ah,bh,hv_1,hv_2,hv_3,v_1v_2,v_1v_3,v_2v_3\}.
\]
Thus \(o,d\) have contact degree two, \(a,b,v_1,v_2,v_3\) degree three, and the gate \(h\) degree five. Initially only \(o\) is infectious; every other person is susceptible. Initial awareness states may be arbitrary. The social graph can be any fixed loop-free graph on these eight vertices with no isolated vertices (including the contact graph).

The stated law holds whenever
\[
\frac13<\Theta<\frac25,
\qquad
\max\!\left\{\frac32(1-\Theta),\frac52\Theta\right\}<\alpha\le1.
\]
At \(\Theta=3/8\), the second condition is exactly \(15/16<\alpha\le1\). In particular, it includes genuine social-awareness mixing \(\alpha<1\), not only the pure local-risk limit \(\alpha=1\). Ties at the awareness threshold and parameter-boundary cases are excluded.

## Proof

**1. The awareness-margin lemma.** All possible infectious-neighbour fractions in the contact graph belong to
\[
\{0,1/5,1/3,2/5,1/2,3/5,2/3,4/5,1\}.
\]
There are no such fractions strictly between \(1/3\) and \(2/5\). For any possible social aware-neighbour fraction \(s\in[0,1]\), if \(k_i/d_i^{\mathrm{con}}\le1/3\), then the mixed score is at most \(1-2\alpha/3<\Theta\). If \(k_i/d_i^{\mathrm{con}}\ge2/5\), the score is at least \(2\alpha/5>\Theta\). Hence the protection indicator is exactly the same as under pure local-risk awareness, regardless of previous awareness states or social-network topology. It suffices to analyze \(\alpha=1\).

**2. Gate and immediate transmission.** At the first step, the seed \(o\) independently infects \(a\) and \(b\) with probability \(\beta\) each: their infectious-neighbour fraction is \(1/3<\Theta\). The sentinel \(d\) has no infectious neighbour initially. At the next step, if both \(a,b\) are infectious, the gate \(h\) sees \(2/5>\Theta\) and is protected; if neither is infectious, nothing passes. When exactly one of \(a,b\) is infectious, the gate sees \(1/5<\Theta\), so it is infected with probability \(\beta\). The sentinel \(d\), seeing one or two infectious neighbours out of two, becomes protected and cannot be infected. Thus the probability that the gate is ever infected is exactly
\[
P_h=2\beta^2(1-\beta).
\]
If the gate is infected, at its infectious step the other bridge has one infectious neighbour out of three and becomes infected with probability \(\beta\). Independently, each of the three clique vertices has one infectious neighbour out of three and becomes infected with probability \(\beta\).

**3. Three-vertex downstream epidemic.** Conditional on gate infection, the number \(K\) of initially infected vertices in \(\{v_1,v_2,v_3\}\) is \(\operatorname{Bin}(3,\beta)\). Those three initial trials contribute mean \(3\beta\). If \(K=2\), the remaining susceptible has two infectious neighbours out of three, so it protects itself, and the clique outbreak stops. If \(K=1\), each of two remaining vertices sees one infectious neighbour out of three and is infected with probability \(\beta\), giving an extra mean \(6\beta^2(1-\beta)^2\), after averaging over \(K\). If exactly one of those two becomes infected, the last susceptible again receives one unprotected exposure in the following step, giving a further mean \(6\beta^3(1-\beta)^3\). There are no later infections. Adding the gate itself and the remaining bridge gives conditional expected further cases
\[
1+4\beta+6\beta^2(1-\beta)^2+6\beta^3(1-\beta)^3.
\]
Multiplying by \(P_h\) and adding the seed and first-step mean \(2\beta\) proves the displayed formula for \(F\). In particular,
\[
F(4/5)=\frac{7267213}{1953125}>3=F(1).
\]

**4. Unique turning point.** Let \(t=\beta/(1-\beta)\) for \(0<\beta<1\). Exact differentiation and expansion yield
\[
\frac{(1+t)^8}{2}
F'\!\left(\frac{t}{1+t}\right)
=1+10t+51t^2+160t^3+255t^4+110t^5+27t^6-4t^7-4t^8.
\]
The right-hand polynomial has exactly one sign change when coefficients are read in descending degree. By Descartes' rule it has at most one positive root; its value is positive at zero and negative for sufficiently large \(t\), so it has exactly one. Since \(F'(0)=2\) and \(F'(1)=-8\), the unique root is a strict global maximizer. The numerical values are for illustration only; the exact root characterization proves uniqueness.

**5. Connected families of unbounded size.** For each integer \(m\ge3\), take vertices \(o,a,b,h\), \(m-2\) sentinels \(d_1,\ldots,d_{m-2}\), and \(m\) clique vertices \(v_1,\ldots,v_m\). Join each of \(o,h,d_j\) to both \(a,b\), join \(h\) to all clique vertices, and complete the clique. This graph has \(2m+2\) vertices and is connected. Bridge and clique degrees equal \(m\), gate degree equals \(m+2\), and seed and sentinels have degree two. Choose any
\[
\frac1m<\Theta<\frac2{m+2};
\]
this interval exists exactly for \(m>2\). At \(\alpha=1\), the bridges remain unprotected after the seed exposure; a lone infected bridge transmits to the unprotected gate; two infected bridges instead protect it. The sentinels always protect themselves against exposed bridges, and the clique vertices are unprotected against their first gate exposure. Therefore
\[
\mathbb E Z_\infty(1)=3,
\qquad
\mathbb E Z_\infty(4/5)
\ge\frac{1785+128m}{625}>3.
\]
The inequality counts only the seed, initially infected bridges, gate, and gate-to-clique first exposures; any later cases can only increase the expectation. Consequently, nonmonotone final size occurs for connected contact networks of arbitrarily large size. For each fixed \(m,\Theta\) the finite set of possible infectious-neighbour ratios is separated strictly from \(\Theta\); hence the same construction persists for all \(\alpha<1\) sufficiently close to one, with any social graph of positive degrees.

## Verification

The self-contained `verify.py` computes the **entire exact symbolic absorption distribution** directly from synchronous infection transitions on the actual eight-vertex graph; no part of the displayed formula is used in the enumerator. It checks the resulting exact degree-nine polynomial, its rational values, the transformed derivative polynomial, the interval of mixed-awareness parameters, and the elementary inequalities underlying the scalable construction. In the enumeration, all infection states are absorbed after at most six updates. Run with Python and SymPy using `python verify.py`.

## Relationship to prior work

Van Wesemael, Rocha, and Baetens [1] define the coupled threshold-awareness/SIR mechanism, with deterministic awareness updates followed by infection, and report nonmonotone infection reach as transmission increases in **simulated multiplex random networks**, principally where mixed awareness causes social cascades. Their paper does not give a finite contact motif with a closed expected-case polynomial, a unique turning point, or the social-topology-independent open parameter wedge here. This theorem does not claim discovery of qualitative nonmonotonicity. Silva, Anteneodo, and Ferreira [2] study local and global adaptive prevention using a distinct continuous-rate behaviour-switching mechanism, and do not imply the present exact synchronous result. Earlier risk-perception work [3] already establishes the importance of fractions of infectious neighbours, but not the exact statement assessed here.

## Limitations

This theorem concerns a stylized finite graph construction under deterministic one-step recovery, complete protection on awareness, synchronous updates, homogeneous thresholds, and independent per-neighbour transmission trials. The eight-vertex graph is minimal **within the indicated two-bridge, guarded-gate, clique construction**, not asserted globally minimal among all graphs. The broad family proves nonmonotonicity but does not give closed full outbreak distributions for every family member. The results describe model dynamics, not an empirically measured human behavioural response; an independent scientific and publication-priority review remains outstanding.

## References

[1] T. Van Wesemael, L. E. C. Rocha, and J. M. Baetens, *Epidemic risk perception and social interactions lead to awareness cascades on multiplex networks*, arXiv:2404.16466 (first posted 2024-04-25), especially §§2.2 and 3.2.2. https://arxiv.org/html/2404.16466v2

[2] D. H. Silva, C. Anteneodo, and S. C. Ferreira, *Epidemic outbreaks with adaptive prevention on complex networks*, arXiv:2203.15024 (first posted 2022-03-28), especially §§II and IV. https://arxiv.org/abs/2203.15024

[3] F. Bagnoli, P. Lio, and L. Sguanci, *Risk perception in epidemic modeling*, arXiv:0705.1974 (2007). https://arxiv.org/abs/0705.1974
