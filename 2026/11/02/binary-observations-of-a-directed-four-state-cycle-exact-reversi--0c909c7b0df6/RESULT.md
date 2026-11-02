# Binary observations of a directed four-state cycle: exact reversibility boundary and cubic four-frame information

## Finding
Consider a stationary clockwise continuous-time Markov cycle with four microscopic states \(0,1,2,3\), positive departure rates \((a,b,c,d)\), and the binary observable \(Y_t=X_t\bmod 2\). All equally spaced observation records of length at most three have time-reversal-invariant laws. In contrast, the **entire observed process**, with arbitrary finite observation times, is reversible **if and only if** \(a=c\) or \(b=d\).

Write \(J=(a^{-1}+b^{-1}+c^{-1}+d^{-1})^{-1}\), \(U=bc+ad\), \(V=cd+ab\), and \(p_h(w)=\Pr\{(Y_0,Y_h,Y_{2h},Y_{3h})=w\}\) for a binary word \(w\) of length four. Then, as \(h\downarrow0\),
\[
p_h(0101)=JUh^3+O(h^4),\quad p_h(1010)=JVh^3+O(h^4),\quad
p_h(0101)-p_h(1010)=-J(a-c)(b-d)h^3+O(h^4).
\]
The four-frame forward-versus-reverse block relative entropy, in natural-log units,
\[
\mathcal D_4(h)=\sum_{w\in\{0,1\}^4}p_h(w)\log\frac{p_h(w)}{p_h(w^{\mathrm{rev}})},
\]
satisfies the exact leading law
\[
\boxed{\mathcal D_4(h)=J(U-V)\log(U/V)\,h^3+O(h^4).}
\]
Its cubic coefficient is strictly positive exactly when both opposite-rate contrasts are nonzero. Thus four *uniformly spaced* readouts are the shortest record capable of detecting time reversal of this binary stationary signal, and they detect it at all sufficiently fine positive sampling intervals in the generic region.

## Assumptions and scope
The state space is \(\mathbb Z/4\mathbb Z\). The only positive off-diagonal generator elements are \(Q_{i,i+1}=r_i\) (indices modulo four), with \((r_0,r_1,r_2,r_3)=(a,b,c,d)\) and all rates strictly positive; the diagonal elements are \(Q_{ii}=-r_i\). The chain is initialized in its unique stationary distribution \(\pi_i=J/r_i\). The observed binary alphabet consists of the even and odd states. The observation step \(h\) is positive. Reversibility of the complete observed process means invariance of every finite-dimensional law under reflection of its observation times; reversibility of a finite block refers only to the equally spaced times \(0,h,2h,3h\). The Landau bounds hold for fixed positive rates as \(h\to0^+\), and are not asserted uniformly when rates approach zero or infinity.

## Proof
**Stationarity and three-frame obstruction.** Every edge carries the same stationary clockwise flow \(\pi_i r_i=J\). For an arbitrary stationary binary process, \(\Pr(01)=\Pr(10)\). The stationary three-letter word identities therefore give \(\Pr(001)=\Pr(100)\) and \(\Pr(011)=\Pr(110)\); the four remaining three-letter words are palindromes. Consequently every equally spaced two- and three-frame distribution is reversible, with no Markov assumption needed.

**Symmetry-protected reversible families.** The time-reversed microscopic generator jumps counterclockwise from state \(i\) at rate \(r_i\), since \(\pi_{i-1}r_{i-1}/\pi_i=r_i\). When \(b=d\), reflection \(R(i)=-i\pmod4\) preserves parity and the departure rate: \(r_{R(i)}=r_i\). When \(a=c\), reflection \(R(i)=2-i\pmod4\) has the same two properties. Either reflection conjugates the reversed microscopic generator to the original clockwise generator and preserves \(\pi\) and the parity observable. Thus the complete observed process is reversible in either family.

**Four-frame witness and necessity.** A change of observed parity in one time interval requires at least one microscopic clockwise jump. The words \(0101\) and \(1010\) have three changes, hence their order-\(h^3\) terms come only from exactly one jump in each of the three intervals. The two microscopic paths underlying \(0101\) are \(0\to1\to2\to3\) and \(2\to3\to0\to1\), contributing respectively \(\pi_0abc=Jbc\) and \(\pi_2cda=Jad\). For \(1010\), the paths are \(1\to2\to3\to0\) and \(3\to0\to1\to2\), contributing \(Jcd\) and \(Jab\). Analyticity of the finite-state semigroup yields the stated expansions. Since \(U-V=-(a-c)(b-d)\), both contrasts nonzero imply different forward and reversed four-frame probabilities for every sufficiently small positive \(h\). Hence the full observed process cannot be reversible. Together with the reflections, this proves the exact if-and-only-if criterion.

**All four-frame antisymmetries.** Write \(p(w)\) for an arbitrary stationary binary four-letter law. Stationarity equates the total incoming and outgoing probability of every three-letter word: \(\sum_z p(zuvw)=\sum_z p(uvwz)\). For \(uvw=000,111,010,101,001,100\), respectively, these equations imply, with \(\Delta=p(0101)-p(1010)\),
\[
\begin{aligned}
p(0001)-p(1000)&=0,\\
p(0111)-p(1110)&=0,\\
p(0010)-p(0100)&=\Delta,\\
p(0011)-p(1100)&=-\Delta,\\
p(1011)-p(1101)&=\Delta.
\end{aligned}
\]
These are the five other nonpalindromic reversal pairs. In particular all reversal differences are \(O(h^3)\) for the present model.

**Relative-entropy asymptotics.** The sum in \(\mathcal D_4\) groups reversal pairs as \((p-q)\log(p/q)\), which are nonnegative. The alternating pair has \(p=JUh^3+O(h^4)\), \(q=JVh^3+O(h^4)\), giving \(J(U-V)\log(U/V)h^3+O(h^4)\). Each nonalternating, nonpalindromic four-letter word has at most two changes of parity, so its positive probability is \(\Theta(h^m)\) for some \(m\le2\) (or is bounded away from zero if \(m=0\)); its reversed counterpart has the same leading order because the difference is \(O(h^3)\). Hence its paired KL term is \(O(h^{6-m})=O(h^4)\). Palindromes contribute zero. This proves the displayed KL expansion. Since \((U-V)\log(U/V)>0\) for \(U\ne V\), the strictness and the absence of any shorter equally spaced witness follow.

## Verification
The self-contained Python standard-library program `verify.py` computes exact rational order-three coefficients of all sixteen four-letter words from \(\pi E_{w_0}e^{hQ}E_{w_1}e^{hQ}E_{w_2}e^{hQ}E_{w_3}\mathbf1\). It separately evaluates the finite-time probabilities by stochastic uniformization. It checks both alternating-word coefficients, the complete set of six reversal pairs, the stationary relations, normalizations, and the small-step KL coefficient. Run `python3 verify.py`; a successful run reports 1036 deterministic exact-rational and numerical assertions. The code does not prove global asymptotics by finite sampling; the proof above does.

## Relationship to prior work
Singh and Aghion (2026) show that coarse-graining a driven bistable run-and-tumble model to a dichotomous Markov description can erase its stationary entropy production. The present question concerns whether *multitime* binary records can recover directional information, using an analytically transparent four-microstate kinetic cycle rather than their underlying particle model. Chen (2011) proves reversibility of deterministic binary observations of irreducible three-state continuous-time hidden Markov chains, supplying the known lower-state comparison; it is **not** claimed here as a new theorem. Barato, Hartich, and Seifert (2013) treat information rates in four-state bipartite networks, rather than the exact opposite-rate reversible surfaces and four-frame KL coefficient. Blom and collaborators (2023) study how coarse-grained temporal memory affects thermodynamic inference; their milestoning framework does not give this four-cycle classification. Ellison and collaborators (2011) develop general information-theoretic time-reversal concepts; their general framework is acknowledged rather than rederived.

## Limitations
The microscopic chain is purely clockwise, so ordinary thermodynamic entropy production relative to the microscopic backward path measure is not finite; the finite quantity proved here is **observed four-frame KL information**, not microscopic heat dissipation. The four-frame detection guarantee is for sufficiently small step sizes, not necessarily every positive step size. This is a complete classification only for the specified deterministic parity observation and directed four-state ring, not arbitrary HMMs. Existing general hidden-process methods might imply some parts of the result indirectly. No independent mathematical or publication-priority audit has been performed.

## References
1. R. K. Singh and E. Aghion, *Spatial density, first passage times, and entropy of run and tumble particles in a bistable potential* (2026), arXiv:2610.08029v1, first public 2026-10-06, https://arxiv.org/html/2610.08029v1.
2. Y. Chen, *On the reversibility of the observed process of three-state hidden Markov model* (2011), arXiv:1101.5482v1, https://arxiv.org/pdf/1101.5482.
3. A. C. Barato, D. Hartich, and U. Seifert, *Rate of mutual information between coarse-grained non-Markovian variables* (2013), arXiv:1306.1698, https://arxiv.org/abs/1306.1698.
4. K. Blom, K. Song, E. Vouga, A. Godec, and D. E. Makarov, *Milestoning estimators of dissipation in systems observed at a coarse resolution: When ignorance is truly bliss* (2023), arXiv:2310.06833v2, https://arxiv.org/html/2310.06833v2.
5. C. J. Ellison, J. R. Mahoney, R. G. James, J. P. Crutchfield, and J. Reichardt, *Information Symmetries in Irreversible Processes* (2011), arXiv:1107.2168, https://arxiv.org/pdf/1107.2168.
