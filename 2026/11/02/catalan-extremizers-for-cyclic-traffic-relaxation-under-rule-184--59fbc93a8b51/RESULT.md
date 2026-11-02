# Catalan extremizers for cyclic traffic relaxation under Rule 184

## Finding

Let \(x\) range over indexed binary cyclic words of length \(n\) with exactly \(k\) ones, where \(n\ge2\) and \(1\le k<n\). Apply elementary cellular automaton Rule 184 synchronously. Define \(m=\min\{k,n-k\}\), and let \(T(x)\) be the first time at which no two cyclically adjacent minority symbols remain. Here the minority is \(1\) when \(k\le n/2\), and \(0\) when \(k>n/2\). At equal density, either choice gives the same alternating configurations.

**Theorem.** For every such \((n,k)\),

\[
\max_{x:\,\#1(x)=k}T(x)=m-1,
\qquad
\#\{x:\#1(x)=k,\ T(x)=m-1\}
=n\operatorname{Cat}_{m-1}
=\frac{n}{m}\binom{2m-2}{m-1}.
\]

The count is of **indexed states**, not binary necklaces. Each extremal low-density state determines exactly one marked car and a plane rooted ordered tree on \(m\) vertices. For uniformly sampled fixed-density states, the exact extremal probability is

\[
\Pr(T=m-1)=\frac{n\operatorname{Cat}_{m-1}}{\binom{n}{k}}.
\]

In the critical window \(n=2m+h\) with each fixed nonnegative integer \(h\),

\[
\lim_{m\to\infty}\Pr(T=m-1)=2^{-h-1}.
\]

In particular, exactly half of uniformly sampled balanced states are asymptotically maximally slow under this finite-ring definition.

## Assumptions and scope

Rule 184 has the following exact parallel traffic interpretation. Every occupied site moves one position clockwise at an update if that destination was vacant immediately **before** the update; otherwise it remains. Cars cannot overtake each other. The ring has labeled sites \(0,\ldots,n-1\), and its density is fixed throughout. For \(k\le n/2\), absence of cyclic \(11\) means that every car subsequently travels one site per update; this is the low-density free-flow regime. For \(k>n/2\), we measure disappearance of cyclic \(00\), equivalently the free-flow regime of vacancies in the opposite direction. This definition excludes the two constant states, for which there is no minority species.

Write \(\operatorname{Cat}_r=\frac{1}{r+1}\binom{2r}{r}\) for the \(r\)-th Catalan number, including \(\operatorname{Cat}_0=1\). All maxima and counts quantify over **all** \(\binom nk\) indexed states, without randomness, a special ordering, or assumptions on the initial gaps.

## Proof

**1. Exact cyclic min-plus representation.** Initially assume \(1\le k\le n/2\). Label the cars in their clockwise cyclic order and lift their positions to integers \(p_i(t)\) with \(p_{i+k}(t)=p_i(t)+n\). The elementary Rule-184 update is

\[
p_i(t+1)=\min\{p_i(t)+1,p_{i+1}(t)-1\}.
\]

Let \(g_i=p_{i+1}(0)-p_i(0)-1\) be the nonnegative number of vacancies following car \(i\), and set \(\delta_i=g_i-1\ge-1\). These numbers are periodic with period \(k\), and their sum is \(h=n-2k\ge0\). Define

\[
S_i(j)=\sum_{r=0}^{j-1}\delta_{i+r},\qquad S_i(0)=0.
\]

Subtracting uniform translation \(t\) from the car positions and inducting in the displayed update gives the *exact* identity

\[
p_i(t)-t=p_i(0)+\min_{0\le j\le t}S_i(j).
\]

Indeed, the two alternatives at time \(t+1\) are the previous minimum at \(j\le t\) and, using \(p_{i+1}(0)-p_i(0)-2=\delta_i\), the minimum of \(S_i(j)\) at \(1\le j\le t+1\). This proves the formula for every \(t\ge0\).

Since \(S_i(j+k)=S_i(j)+h\) and \(h\ge0\), the global minimum occurs within \(0\le j<k\). Define \(\tau_i\) to be the **first** index in \(\{0,\ldots,k-1\}\) at which this global minimum is attained. By the min-plus identity, car \(i\) experiences no further stopped update after time \(\tau_i\). All cars are moving freely from time \(\max_i\tau_i\) onwards, whereas earlier at least one car must still stop. Consequently

\[
T(x)=\max_i\tau_i\le k-1.
\]

**2. Characterize equality by strict negative suffixes.** We have \(T(x)=k-1\) exactly when there exists a car \(i\) such that the first global minimum of \(S_i\) occurs at \(j=k-1\). This is equivalent to

\[
\sum_{r=a}^{k-2}\delta_{i+r}<0
\quad\text{for every}\quad0\le a\le k-2.
\]

In words, each nonempty suffix of the \(k-1\) increments preceding the omitted closing gap must have strictly negative sum. Put the increments in reverse order \(d_j=\delta_{i+k-1-j}\) for \(1\le j\le k-1\). Then \(d_j\ge-1\) and all nonempty prefix sums \(\sum_{j=1}^{s}d_j\) are strictly negative.

**3. Prove the distinguished car is unique.** Suppose two different car roots satisfy the strict-suffix condition. Reindex the first as \(i=0\) and the second as \(i=s\), where \(1\le s\le k-1\). For the first root, the suffix from increment \(s-1\) through \(k-2\) has strictly negative sum. For the second root, the suffix from increment \(k-1\), then through increment \(s-2\) cyclically, also has strictly negative sum. These two disjoint arcs partition the entire cyclic list of \(k\) increments. Their sum is \(h=n-2k\), which is nonnegative, a contradiction. Therefore the maximizing root is unique.

**4. Catalan bijection, including the unconstrained closing gap.** Fix a car root \(i\). For a strict-negative-prefix sequence \(d_1,\ldots,d_{k-1}\), put

\[
a_0=-\sum_{j=1}^{k-1}d_j,\qquad
 a_j=1+d_{k-j}\quad(1\le j\le k-1).
\]

Every \(a_j\) is a nonnegative integer, \(\sum_{j=0}^{k-1}a_j=k-1\), and for \(1\le \ell<k\),

\[
\sum_{j=0}^{\ell-1}(a_j-1)
=-1-\sum_{r=1}^{k-\ell}d_r\ge0.
\]

The full sum \(\sum_{j=0}^{k-1}(a_j-1)\) equals \(-1\). These are exactly the preorder outdegree sequences of rooted plane trees with \(k\) vertices. Conversely, each such tree yields the unique strict-negative-prefix sequence. There are exactly \(\operatorname{Cat}_{k-1}\) choices, including one when \(k=1\).

Given this sequence, the final, omitted cyclic gap is uniquely forced by the sum of increments:

\[
\delta_{i+k-1}=h-\sum_{j=1}^{k-1}d_j\ge1.
\]

Thus there is no dependence of the Catalan count on the number \(h\) of excess vacancies. Once the root car's indexed position is specified (\(n\) choices), the gaps determine all other car positions and hence the entire state. The uniqueness in step 3 eliminates double counting, proving exactly \(n\operatorname{Cat}_{k-1}\) extremizers and attainability of the upper bound.

**5. Particle–vacancy symmetry.** Define \((Jx)_j=1-x_{-j\bmod n}\), a complement followed by cyclic reflection. An immediate check of the local Rule-184 update shows \(JF=FJ\), and \(J\) bijects \(k\)-car states with \((n-k)\)-car states. It interchanges absence of adjacent cars and absence of adjacent vacancies, preserving \(T\). Apply steps 1–4 to \(Jx\) when \(k>n/2\). This replaces \(k\) by \(m=\min\{k,n-k\}\) and establishes the two formulas for all admissible densities.

**6. Exact probability and critical-window limit.** Uniform sampling from \(\binom nk\) indexed states yields the displayed quotient. For \(n=2m\) it simplifies exactly to

\[
\Pr(T=m-1)=\frac{m}{2m-1}.
\]

For \(n=2m+h\), compare the quotient against the \(h=0\) case:

\[
\frac{\Pr_{m,h}(T=m-1)}{\Pr_{m,0}(T=m-1)}
=\frac{2m+h}{2m}\,
\frac{\binom{2m}{m}}{\binom{2m+h}{m}}
\longrightarrow 2^{-h}.
\]

Since \(\Pr_{m,0}\to\tfrac12\), the fixed-\(h\) limit is \(2^{-h-1}\). This concludes the proof.

## Verification

The accompanying `verify.py` implements Rule 184 directly as synchronous bitwise particle moves, independently computes the gap minima, tests the terminal-cut criterion, and counts exact extremizers. It exhaustively checks all \(131{,}038\) nonconstant indexed states for ring lengths from \(2\) through \(16\), and compares both descriptions on \(5{,}600\) further seeded random configurations at larger lengths up to \(101\). It separately enumerates strict-negative-prefix sequences at small lengths and checks the Catalan counts. The expected successful output begins `VERIFY_OK`.

These experiments provide independent finite checks but are **not** substituted for the all-length proof above. The program uses only the Python 3 standard library and can be run using `python3 verify.py`.

## Relationship to prior work

Fukś (1997) proves finite-time density classification using Rule 184 and gives a uniform convergence bound in terms of total ring length; it does not state the sharp number-of-cars bound together with the exact count of extremal indexed configurations. Fukś (1999) studies deterministic traffic flow and preimage probabilities. Belitsky and Ferrari (1998 preprint) study invariant measures and convergence. Jha and collaborators (2025, 2026) analyze system relaxation time and traffic-delay observables, particularly numerical or continuum-limit distributions, but do not give the sharp finite-size extremal multiplicity here. Biham and collaborators (2026) derive last-stopping distributions for individual cars under random initial conditions, not this fixed-density cyclic global maximum count. The present statement concerns a **joint** maximization and exact enumeration over the entire finite-density ensemble.

The cyclic Rule-184 total-delay distribution is a different invariant: a sum of all stopped-car updates is not the largest individual stopping time. Neither this scalar sum nor the known finite convergence bound yields the Catalan multiplicity without further analysis. Priority remains subject to possible unindexed earlier queueing or traffic combinatorics sources.

## Limitations

The theorem is for deterministic synchronous binary Rule 184, periodic rings, and indexed configurations. It measures the **first time with no adjacent minority particles**, not a mixing time, stochastic traffic delay, or the time until a cellular automaton reaches a fixed configuration. The critical-window limit fixes \(h\) and lets \(m\to\infty\); it does not describe arbitrary density scalings. The known absence of a fully indexed historical literature makes unindexed equivalences a residual priority risk.

## References

- H. Fukś, *Solution of the Density Classification Problem with Two Cellular Automata Rules* (first posted March 7, 1997), https://arxiv.org/abs/comp-gas/9703001.
- H. Fukś, *Exact results for deterministic cellular automata traffic models* (1999), https://arxiv.org/abs/math/9904182.
- V. Belitsky and P. Ferrari, *Invariant Measures and Convergence for Cellular Automaton 184 and Related Processes* (preprint 1998), https://arxiv.org/abs/math/9811103.
- A. Jha et al., *Evidence of Non-Equilibrium Critical Phenomena in a Simple Model of Traffic* (first posted January 14, 2025), https://arxiv.org/abs/2501.08417.
- A. Jha et al., *Equilibrium-like statistical mechanics in space-time for a deterministic traffic model far from equilibrium* (2026), https://arxiv.org/abs/2602.08991.
- O. Biham et al., *First-passage processes in a deterministic one-dimensional cellular automaton model of traffic flow* (2026), https://arxiv.org/abs/2605.19023.
