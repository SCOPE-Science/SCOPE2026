# A three-regime equilibrium and exact convergence law for balanced single-peaked Schelling swaps

## Finding

**Theorem.** Let \(n\ge2\), and put exactly \(n\) red and \(n\) blue agents on the vertices of \(K_{n,n}\). All agents use the same single-peaked closed-neighborhood utility of Bilò, Bilò, Lenzner and Molitor, with peak \(0<\Lambda<1\). A swap is permitted only when **both** exchanged agents strictly improve. Let \(x\in\{0,\ldots,n\}\) be the number of red agents on the first side, and let \(E_n(\Lambda)\) count equilibrium *vertex colorings*, not permutations of individually labeled agents.

There are exactly three regimes:

\[
\begin{array}{c|c|c}
\text{peak}&\text{equilibrium values of }x&E_n(\Lambda)\\\hline
0<\Lambda<1/2&\{0,n\}&2\\
\Lambda=1/2&\{0,1,\ldots,n\}&\binom{2n}{n}\\
1/2<\Lambda<1&\{\lfloor n/2\rfloor,\lceil n/2\rceil\}&\displaystyle\sum_{j=\lfloor n/2\rfloor}^{\lceil n/2\rceil}\binom nj^2.
\end{array}
\]

Moreover, **every maximal sequence of strict mutually beneficial swaps from the same coloring has the same exact number of swaps**:

\[
T_{n,\Lambda}(x)=\begin{cases}
\min\{x,n-x\},&\Lambda<1/2,\\
0,&\Lambda=1/2,\\
\max\{0,\lfloor n/2\rfloor-x,x-\lceil n/2\rceil\},&\Lambda>1/2.
\end{cases}
\]

This counts strict swaps, not attempts or updates that leave the coloring unchanged. For individually labeled red and blue agents, every coloring corresponds to \((n!)^2\) labeled assignments and the equilibrium assignment count is \((n!)^2E_n(\Lambda)\).

For a uniformly random initial vertex coloring with \(n\) agents of each color, let \(X\) denote its initial red count on the first side. Define

\[
D_n=\begin{cases}
\displaystyle \frac n4\frac{\binom{n}{n/2}^2}{\binom{2n}{n}},&n\text{ even},\\
\displaystyle \frac{(n+1)^2}{4n}\frac{\binom{n}{(n-1)/2}^2}{\binom{2n}{n}},&n\text{ odd}.
\end{cases}
\]

The exact expected strict-swap counts are \(n/2-D_n\) below one half, \(0\) at one half, and \(D_n-\tfrac12\mathbf1_{\{n\text{ odd}\}}\) above one half. In particular, as \(n\to\infty\), these are respectively

\[
\frac n2-\sqrt{\frac{n}{4\pi}}+o(\sqrt n),\quad 0,\quad \sqrt{\frac{n}{4\pi}}+o(\sqrt n).
\]

## Assumptions and scope

Each vertex is occupied; the two parts of the undirected simple graph each have size \(n\). Each agent evaluates **the closed neighborhood**, including herself. At any occupied vertex \(v\), if the number of agents of the same color in the opposite part is \(s\), the agent's same-color fraction is \((s+1)/(n+1)\).

The utility \(p:[0,1]\to[0,1]\) satisfies \(p(0)=p(1)=0\), \(p(\Lambda)=1\), is strictly increasing on \([0,\Lambda]\), and obeys
\[
p(t)=p\left(\frac{\Lambda(1-t)}{1-\Lambda}\right)\quad(\Lambda\le t\le1).
\]
No continuity, linearity, differentiability, or particular shape beyond these axioms is assumed. Ties are not strictly beneficial. The result concerns complete balanced bicliques with **balanced total color composition**; it does not characterize unbalanced bicliques, additional colors, vacancies or heterogeneous utility functions.

## Proof

**Step 1 (ordinal reduction).** Define
\[
q_\Lambda(t)=\min\left\{\frac{t}{\Lambda},\frac{1-t}{1-\Lambda}\right\}.
\]
The axioms imply \(p(t)=g(q_\Lambda(t))\) for a strictly increasing \(g:[0,1]\to[0,1]\): take \(g(s)=p(\Lambda s)\). Consequently \(p(t)>p(1-t)\), for \(0<t<1\), exactly when \((1/2-\Lambda)(1/2-t)>0\); equality holds for \(t=1/2\) or \(\Lambda=1/2\). This comparison follows by applying the two linear branches of \(q_\Lambda\) to \(t\) and \(1-t\); the boundary values \(t=0,1\) are not used in an available cross-color swap.

**Step 2 (the only possible improvements).** Swapping two agents of the same color exchanges their old utilities, so both cannot strictly gain. Exchanging two agents of different colors within the same part changes neither agent's same-color fraction. Thus any mutually beneficial swap exchanges opposite colors across the parts, changing \(x\) by exactly one.

If a red agent in the first part swaps with a blue agent in the second, then \(x\mapsto x-1\). **Both** agents have fraction \((n-x+1)/(n+1)\) before, and \(x/(n+1)\) after. The swap is available for \(1\le x\le n\). With \(t=x/(n+1)\), the two fractions are \(1-t\) and \(t\). The gain criterion is \(p(t)>p(1-t)\).

If instead a blue agent in the first part swaps with a red agent in the second, then \(x\mapsto x+1\). Both have fraction \((x+1)/(n+1)\) before and \((n-x)/(n+1)\) after. This swap is available for \(0\le x\le n-1\). With \(t=(x+1)/(n+1)\), the gain criterion is \(p(1-t)>p(t)\).

In the low-peak regime, the first swap is profitable exactly when \(x<(n+1)/2\), and the second exactly when \(x>(n-1)/2\). In the high-peak regime these strict inequalities reverse. At \(\Lambda=1/2\), neither is profitable.

**Step 3 (classification and clocks).** Below one half, every interior state has a strictly profitable move away from the midpoint: for \(x<n/2\), only decrement is profitable; for \(x>n/2\), only increment is profitable; for even \(n\) at \(x=n/2\), both directions are profitable and lead to the same remaining distance. Hence the only sinks are \(x=0,n\), and all maximal strict-swap paths have length \(\min(x,n-x)\).

Above one half, every state strictly outside \([\lfloor n/2\rfloor,\lceil n/2\rceil]\) has exactly one direction of profitable motion, toward that interval. Every state in the interval has no strictly beneficial swap. This gives the claimed sink set and distance formula. At the midpoint peak every placement is a sink. These arguments cover boundary availability at \(x=0,n\), and odd/even midpoint ties explicitly.

**Step 4 (enumeration and random initialization).** At a fixed red count \(x\) in the first part, the second part has \(n-x\) red agents, giving \(\binom nx\binom n{n-x}=\binom nx^2\) vertex colorings. The middle-regime sum is Vandermonde's identity \(\sum_x\binom nx^2=\binom{2n}{n}\). Under uniform initialization,
\[
\Pr(X=x)=\frac{\binom nx^2}{\binom{2n}{n}}.
\]
The low and high clocks are respectively \(n/2-|X-n/2|\), and \(|X-n/2|-\tfrac12\mathbf1_{\{n\text{ odd}\}}\). Write \(w_x=\binom nx^2\), and \(F_x=x^2w_x\). The binomial recurrence gives
\[
F_x-F_{x+1}=2n(x-n/2)w_x.
\]
Summing this telescoping identity over the positive half of the distribution and using symmetry proves \(\mathbb E|X-n/2|=D_n\), hence the expected-time formulas. Stirling's central-binomial estimate \(\binom n{\lfloor n/2\rfloor}\sim2^n\sqrt{2/(\pi n)}\) and \(\binom{2n}n\sim4^n/\sqrt{\pi n}\) show \(D_n\sim\sqrt{n/(4\pi)}\).

## Verification

The standalone \(\texttt{verify.py}\) checks the direct closed-neighborhood utility for the canonical piecewise-linear representative \(p=q_\Lambda\), which is ordinally equivalent to every admissible \(p\). For \(2\le n\le7\), all \(\binom{2n}n\) vertex colorings and every unlike-color swap were checked at each of seven rational peaks \(\Lambda\in\{1/8,1/4,2/5,1/2,3/5,3/4,7/8\}\). It verified the state-by-state equilibrium criterion, decrement by one of the claimed path clock at every profitable swap, and equilibrium counts: **32,928** coloring/peak cases and **215,664** profitable swaps. Separately, the exact \(D_n\) formula was checked via rational arithmetic for \(2\le n\le12\). These finite checks do not replace the proof for all \(n\) and all admissible utilities.

## Relationship to prior work

Bilò, Bilò, Lenzner and Molitor (arXiv:2204.12599, 2022) introduce this exact closed-neighborhood, single-peaked bilateral swap model. Their Theorem 1 proves finite improvement on almost regular graphs for \(\Lambda\le1/2\); Theorem 4 gives an independent-set sufficient condition for stability; and Corollary 1 gives equilibrium existence on bipartite graphs at \(\Lambda=1/2\). These results do not state the exact equilibrium spectrum, the all-colorings critical degeneracy, or the choice-independent path length and random-initialization distribution on balanced complete bipartite graphs. This result uses their utility normalization and does not claim that general existence or potential-method ideas are new.

Agarwal and collaborators (2021) study the different, monotone preference swap Schelling game. Friedrich and collaborators (2023) study single-peaked **jump** games with vacant locations. Neither directly implies the present full-occupation, two-agent-strict-swap statement. A search for alternative formulations and stronger characterizations in the accessible literature and indexed mathematical findings found no equivalent claim; this is evidence of noncoverage, not a guarantee of absolute publication priority.

## Limitations

This is a self-review, not independent verification or a claim of publication priority. Its threshold at one half uses equal part sizes, equal numbers of both agent colors, common ordinal utilities, self-including neighborhoods, and a bilateral strict-gain rule. Different swap or tie protocols may change the result. The time formulas count **profitable exchanges**, not asynchronous selection attempts. Undiscovered specialist literature could contain equivalent statements.

## References

1. D. Bilò, V. Bilò, P. Lenzner, and L. Molitor. *Tolerance is Necessary for Stability: Single-Peaked Swap Schelling Games*. arXiv:2204.12599, first public version 2022-04-26. https://arxiv.org/abs/2204.12599 ; IJCAI 2022, https://doi.org/10.24963/ijcai.2022/12 .
2. A. Agarwal, E. Elkind, J. Gan, A. Igarashi, W. Suksompong, and A. A. Voudouris. *Schelling Games on Graphs*. Artificial Intelligence 301 (2021), 103576. https://doi.org/10.1016/j.artint.2021.103576 .
3. T. Friedrich, P. Lenzner, L. Molitor, and L. Seifert. *Single-Peaked Jump Schelling Games*. arXiv:2302.12107, 2023. https://arxiv.org/abs/2302.12107 .
