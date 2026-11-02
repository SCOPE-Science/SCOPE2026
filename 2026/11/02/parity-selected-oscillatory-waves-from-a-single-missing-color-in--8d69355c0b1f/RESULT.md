# Parity-selected oscillatory waves from a single missing color in cyclic graph dynamics

## Finding
Consider the synchronous successor-contact cyclic cellular automaton on a labelled loopless complete bipartite graph \(K_{a,b}\), with \(q\ge 3\) colors \(\mathbb Z/q\mathbb Z\). At each update a vertex of color \(c\) changes to \(c+1\pmod q\) exactly if some opposite-shore vertex has that successor color.

**Single-defect theorem.** Suppose the colors present on one shore are precisely \(\mathbb Z/q\mathbb Z\setminus\{d\}\), while the other shore contains all \(q\) colors. The first periodic-entry time and eventual least period are, exactly,
\[
(T_q,p_q)=\begin{cases}(q-1,q),&q\text{ even},\\(q-2,q+1),&q\text{ odd}.\end{cases}
\]
These values are independent of the shore sizes and of the nonzero color multiplicities. In particular, for odd \(q\), a single missing initial color produces a period strictly exceeding the number of colors.

**Alternating-wave orbit census.** Put \(m=\lceil q/2\rceil\), and define the surjection polynomial evaluated at integers
\[
U_m(n)=\sum_{j=0}^{m}(-1)^j\binom mj(m-j)^n.
\]
Define the alternating-wave family by the following occupied-color support pairs and all labelled colorings realizing them: for even \(q\), the two pairs consisting of even versus odd colors in opposite shores; for odd \(q\), the \(2q\) pairs obtained by uniformly rotating and shore-swapping \((\{0,2,\ldots,q-1\},\{1,3,\ldots,q-2,q-1\})\). Every state in this family is periodic of least period \(p_q\). Its number of distinct primitive orbits is exactly
\[
\boxed{\mathcal N_q(a,b)=\begin{cases}
\dfrac{2U_m(a)U_m(b)}q,&q\text{ even},\\[4pt]
\dfrac{2qU_m(a)U_m(b)}{q+1},&q\text{ odd}.
\end{cases}}
\]
Here \(U_m(n)=0\) for \(n<m\). This is a count of the *specified alternating-wave family*, not a claim to classify every periodic orbit for all \(q\).

**Conditional rare-event law.** Let \(a=b=n\) and let the \(2n\) initial colors be independent uniform draws from \(\mathbb Z/q\mathbb Z\). Let \(E_n\) be the event that at least one shore initially omits a color. For each fixed \(q\ge3\),
\[
\Pr(E_n)=2q\left(\frac{q-1}{q}\right)^n\left[1+O_q\!\left(\left(\frac{q-1}{q}\right)^n\right)\right]
\]
and
\[
\Pr\bigl((T,p)=(T_q,p_q)\mid E_n\bigr)=1-O_q\!\left(\left(\frac{q-1}{q}\right)^n\right).
\]
More precisely, for every \(n\) for which the conditioning event has positive probability, the latter conditional probability is at least
\[
\boxed{\frac{2qU_{q-1}(n)U_q(n)}{q^{2n}-U_q(n)^2}.}
\]
The lower bound is the exact conditional probability that precisely one shore omits precisely one color and the other is color-complete.

## Assumptions and scope
The graph is simple and undirected, every vertex belongs to one of two nonempty labelled shores, and every cross-shore edge is present. Colors are labelled residues, not anonymous species. Updates are synchronous, with contact threshold exactly one. The first-entry time \(T\) is the smallest nonnegative integer for which the entire labelled configuration lies on a periodic orbit; \(p\) is that orbit's least period. The deterministic theorem requires every retained color to be represented by at least one vertex, so the shore with one omitted color has at least \(q-1\) vertices and the other at least \(q\). The orbit census holds for all positive shore sizes, with zero counts when its support is impossible. Asymptotics fix \(q\) first and send \(n\to\infty\).

## Proof
**Step 1: exact support evolution.** Rotate colors and exchange shores if necessary so that the initial support pair is \((A_0,B_0)=(\{1,\ldots,q-1\},\{0,\ldots,q-1\})\). Because every vertex in a shore with the same color has the same opposite-shore neighbors, the support map is exact:
\[
\mathcal F(A,B)=(f_B(A),f_A(B)),\quad
f_D(S)=\{\phi_D(c):c\in S\},\quad
\phi_D(c)=\begin{cases}c+1\pmod q,&c+1\pmod q\in D,\\c,&\text{otherwise.}\end{cases}
\]
A direct residue check gives, for all applicable time indices before the first two-cycle,
\[
\begin{aligned}
A_{2k}&=\{1,3,\ldots,2k+1\}\cup\{2k+2,\ldots,q-1\},\\
B_{2k}&=\{0,2,\ldots,2k-2\}\cup\{2k,\ldots,q-1\},\\
A_{2k+1}&=\{0,2,\ldots,2k\}\cup\{2k+2,\ldots,q-1\},\\
B_{2k+1}&=\{1,3,\ldots,2k+1\}\cup\{2k+2,\ldots,q-1\}.
\end{aligned}
\]
Empty initial arithmetic progressions and terminal intervals are interpreted as empty sets. Substitution into \(\mathcal F\) verifies the even-to-odd and odd-to-even steps by splitting colors below and at/above the displayed boundary; the only wraparound transition is from \(q-1\) to \(0\). These formulas also establish strict loss of one occupied color in one shore at every preperiodic update after the first or second initial step.

**Step 2: exact temporal onset and period.** If \(q=2m\), at time \(T=2m-1\) the supports are the even and odd residues, respectively. They swap every update, and every vertex advances once per update. Hence the configuration is already periodic with least period \(q\). Earlier support pairs cannot recur because their successive shore-size pairs strictly decrease toward \((m,m)\).

If \(q=2m+1\), at time \(T=2m-1\) the supports are
\[
A_T=\{0,2,\ldots,2m\},\qquad B_T=\{1,3,\ldots,2m-1,2m\}.
\]
They swap every update. Over two updates, the occupied classes in the first shore undergo the cycle \(0\mapsto2\mapsto\cdots\mapsto2m\mapsto0\), and the second shore undergoes \(1\mapsto3\mapsto\cdots\mapsto2m-1\mapsto2m\mapsto1\). Every class is nonempty, so each two-step return has least order \(m+1\). Since the shore supports have least period two, the labelled configuration has least period \(2(m+1)=q+1\). Before \(T\), the shore support sizes decrease, ruling out earlier periodic entry. This proves the first assertion, including both parities, by an all-\(q\) induction rather than finite extrapolation.

**Step 3: orbit census.** A coloring of \(n\) labelled vertices using each of \(m\) prescribed colors at least once has \(U_m(n)\) possibilities by inclusion-exclusion. For even \(q\) there are two alternating support pairs. For odd \(q\), the specified basic pair has \(q\) distinct joint rotations and two shore orientations, yielding \(2q\) distinct ordered pairs. At every one of these supports the update maps each occupied shore color injectively to the next corresponding shore color, so no two labelled color classes merge. Every such state is therefore periodic with least period \(p_q\), as established in Step 2. Dividing the resulting \(2U_m(a)U_m(b)\), respectively \(2qU_m(a)U_m(b)\), periodic states by their orbit lengths gives the formulas. No other periodic-state families are being counted.

**Step 4: conditional distribution.** There are \(U_q(n)\) color-complete assignments to one shore and \(qU_{q-1}(n)\) assignments omitting exactly one color. Consequently
\[
\Pr(E_n)=1-\frac{U_q(n)^2}{q^{2n}},\qquad
\Pr(H_n)=\frac{2qU_{q-1}(n)U_q(n)}{q^{2n}},
\]
where \(H_n\subseteq E_n\) is the single-defect event in Step 1. The first theorem gives \(H_n\subseteq\{(T,p)=(T_q,p_q)\}\). Inclusion-exclusion yields
\[
\frac{U_q(n)}{q^n}=1-q\alpha^n+O_q(\beta^n),\qquad
\frac{U_{q-1}(n)}{q^n}=\alpha^n+O_q(\beta^n),
\]
where \(\alpha=(q-1)/q\), \(\beta=(q-2)/q\), and \(\beta<\alpha^2\) for \(q\ge3\). Substitution proves the probability asymptotics and the exact lower bound. Because the conditional probability is bounded above by one, the lower bound tending to one supplies the asserted convergence and exponential error rate.

## Verification
The self-contained standard-library file `cyclic_defect_verify.py` verifies the support formulas for every integer \(3\le q\le64\) at all times through the predicted first periodic entry (2,046 support-time comparisons). It independently simulates the labelled vertex rule in 4,692 single-defect experiments across \(3\le q\le48\), color rotations, shore swaps, permutations, and redundant labeled vertices. It also exhaustively enumerates 145,231 labelled initial configurations across five small parameter cases, checks every alternating-supported configuration is already periodic with the claimed least period, and matches its count against the surjection formula. Reproduce using `python3 cyclic_defect_verify.py`; the expected output is in `cyclic_defect_verification_output.txt`. The all-\(q\) proof is symbolic; finite checks are corroboration, not a substitute for it.

## Relationship to prior work
Matamala and Goles studied cyclic automata on finite graphs in the published 1995 LATIN proceedings, including transient and period bounds in terms of graph structure. The available abstract does not specify an all-\(q\), one-color-defect bipartite formula; the inaccessible chapter's full contents remain a substantive coverage risk. Gravner, Lyu, and Sivakoff analyze three-color excitation on general graphs by a comparison process, cycle forms, and a synchronization criterion, not the arbitrary-color, precise rare-defect wave law and exact alternating-family orbit count here. Earlier special-case bipartite cyclic-automaton censuses at three and four colors, and an all-color Greenberg–Hastings family, cover related mechanisms but do not imply the claimed cyclic-contact first-entry formula across every number of colors or its conditional occupancy asymptotics. The Greenberg–Hastings rule differs because refractory colors increment automatically.

## Limitations
No classification of every possible recurrent orbit of the arbitrary-\(q\) cyclic automaton is asserted. The conditional limit fixes the color alphabet before growing the shore sizes; it does not describe simultaneous growth of \(q\) and \(n\), nonuniform color probabilities, missing multiple colors, or graphs without every cross-shore edge. Independent external review has not occurred. The historical 1995 chapter and related 1997 article were not available in full text; consequently, exact historical uniqueness has not been established.

## References
1. M. Matamala and E. Goles, *Cyclic Automata Networks on Finite Graphs*, LATIN '95, Lecture Notes in Computer Science 911, pp. 398–410, Springer (printed proceedings published 1995-03-20), DOI: `10.1007/3-540-59175-3_105`.
2. M. Matamala and E. Goles, *Dynamic Behavior of Cyclic Automata Networks*, Discrete Applied Mathematics 77 (1997), 161–184, DOI: `10.1016/S0166-218X(97)84104-2`.
3. J. Gravner, H. Lyu, and D. Sivakoff, *Limiting Behavior of 3-Color Excitable Media on Arbitrary Graphs*, arXiv:1610.07320v1 (2016-10-24), later published in Annals of Applied Probability.
4. R. Fisch, J. Gravner, and D. Griffeath, *Cyclic Cellular Automata in Two Dimensions*, in Spatial Stochastic Processes (1991), pp. 171–185.
