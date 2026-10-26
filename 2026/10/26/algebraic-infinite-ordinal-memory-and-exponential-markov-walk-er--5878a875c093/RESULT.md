# Algebraic infinite ordinal memory and exponential Markov-walk error for the tripling map

## Finding

Let \(T(x)=3x\bmod1\) act on \([0,1)\) with normalized Lebesgue measure and, for every \(j\ge0\), define the order-two, lag-one ordinal symbol \(Y_j=+\) when \(T^{j+1}x>T^jx\) and \(Y_j=-\) otherwise. The probability of a tie is zero. For every integer \(n\ge1\),

\[
R_n:=\Pr(Y_0=\cdots=Y_{n-1}=+)=\frac{n+2}{2\,3^n},\qquad
\Pr(Y_n=+\mid Y_0=\cdots=Y_{n-1}=+)=\frac{n+3}{3(n+2)}.
\]

The observed process has **no finite Markov order**. The stationary first-order Markov surrogate calibrated to the same one-step ordinal transitions instead predicts

\[
\widetilde R_n=\frac12\left(\frac49\right)^{n-1},\qquad
\frac{\widetilde R_n}{R_n}=\frac{3(4/3)^{n-1}}{n+2}\longrightarrow\infty.
\]

Thus an ordinal-transition Markov walk with a strictly positive spectral gap can exponentially overestimate the probability of long monotone runs in the very process used to estimate its edges. The result is an exact counterexample to transferring the finite-walk fading-memory interpretation directly to the original dynamical observation.

## Assumptions and scope

The state space is the real interval \([0,1)\), the invariant initial distribution is normalized Lebesgue measure, and the map is the slope-three expanding transformation \(T\). The observation is **only** the sign of a strict comparison of two consecutive iterates; the surrogate is defined solely by stationary one-step joint frequencies of these two ordinal symbols. Boundary and equality cases have measure zero, so symbols there do not affect the statements. Statements about Markov order refer to the stationary stochastic process \((Y_j)_{j\ge0}\) under this measure. No estimate is asserted for arbitrary signals, arbitrary ordinal embedding dimensions, or trained reservoirs.

## Proof

**1. A four-cell Markov refinement.** For \(x\in[k/3,(k+1)/3)\), \(T(x)=3x-k\). Comparing it with \(x\) shows that rises occur exactly on \((0,1/3)\cup(1/2,2/3)\) modulo endpoints, and falls on the remaining two subintervals. Denote the four ordered cells by

\[
I_0=(0,1/3),\quad I_1=(1/3,1/2),\quad
I_2=(1/2,2/3),\quad I_3=(2/3,1).
\]

The endpoints of this partition map to endpoints, and each restriction of \(T\) is affine of slope three; its image is a union of entire partition cells. Under Lebesgue measure, conditional distributions on itinerary cylinders are uniform in their terminal cells. Therefore the itinerary process of these four cells is a stationary Markov chain with stationary row and transition matrix

\[
\pi=\left(\frac13,\frac16,\frac16,\frac13\right),\qquad
P=\begin{pmatrix}
\frac13&\frac16&\frac16&\frac13\\
\frac23&\frac13&0&0\\
0&0&\frac13&\frac23\\
\frac13&\frac16&\frac16&\frac13
\end{pmatrix}.
\]

Each entry is simply the fraction of its source-cell length mapped into its destination cell. The two rise cells are \(I_0\) and \(I_2\).

**2. Exact all-rise cylinders.** Restricting the four-state chain to the ordered rise states gives

\[
Q=\begin{pmatrix}\frac13&\frac16\\0&\frac13\end{pmatrix}
=\frac13\begin{pmatrix}1&\frac12\\0&1\end{pmatrix},\qquad
Q^{n-1}=3^{-(n-1)}\begin{pmatrix}1&(n-1)/2\\0&1\end{pmatrix}.
\]

Starting with the unnormalized stationary rise row \((1/3,1/6)\), the probability of remaining in the rise states for \(n\) observations is

\[
R_n=\left(\frac13,\frac16\right)Q^{n-1}\begin{pmatrix}1\\1\end{pmatrix}
=\frac{n+2}{2\,3^n}.
\]

The nontrivial Jordan block in \(Q\) produces the linear prefactor \(n+2\); it is a structural origin of the observed algebraic dependence.

**3. Infinite memory.** The exact conditional probability is \(R_{n+1}/R_n=(n+3)/(3(n+2))\), which strictly decreases with \(n\) because \((n+4)/(n+3)<(n+3)/(n+2)\) for all positive integers. If the stationary binary process had finite Markov order \(k\), all events consisting of \(n\ge\max\{1,k\}\) consecutive rises would have the same length-\(k\) trailing history and hence the same next-rise conditional probability. Every such event has strictly positive probability, contradicting the displayed strictly changing ratios. Thus no finite \(k\) works.

**4. The calibrated one-step Markov surrogate.** Since \(R_1=1/2\), \(R_2=2/9\), its plus-to-plus transition probability is \(R_2/R_1=4/9\). Reflection \(x\mapsto1-x\) conjugates \(T\) to itself up to null endpoints and exchanges the comparison signs; equivalently, stationarity and the computed matrix give minus-to-minus probability \(4/9\). The surrogate transition matrix in the \((+,-)\) order is

\[
\widetilde P=\begin{pmatrix}4/9&5/9\\5/9&4/9\end{pmatrix}.
\]

Its eigenvalues are \(1\) and \(-1/9\), hence its absolute spectral gap is \(1-1/9=8/9\). Starting in its stationary distribution \((1/2,1/2)\), the surrogate predicts \(\widetilde R_n=(1/2)(4/9)^{n-1}\). Dividing by the exact expression gives \(3(4/3)^{n-1}/(n+2)\), which diverges exponentially. This proves every claimed assertion.

## Verification

The accompanying standalone rational-arithmetic checker constructs the full transition matrix by intersecting source and target cells, independently enumerates inverse-image intervals of the rise event through nine observations, and checks the matrix-power identity through twenty observations. It also checks the surrogate's transition spectrum and the conditional-probability identities. The analytic Jordan-block calculation and Markov-order contradiction—not these finite checks—establish the statements for every positive integer \(n\).

## Relationship to prior work

Potratzki, de Jong, Small and Bröhl (2026) define ordinal-pattern transition networks and study Markov walks on the networks, including their spectral-gap-based fading-memory and reservoir-computing behavior. Their finite-state walk is a constructed surrogate, not a proof that the original observed ordinal process has the same higher-order word law. The present calculation isolates and quantifies that difference for a canonical uniformly expanding interval map. Sakellariou, Stemler and Small (2019) likewise advocate Markov modeling via ordinal partitions; the exact all-rise distribution of this slope-three map is not part of the inspected statements. Work on possible and forbidden ordinal patterns concerns a related but different combinatorial question. The originality assessment compares **mathematical implications**, not only terminology.

## Limitations

The result applies to the tripling map with Lebesgue initial distribution and order-two, lag-one rise/fall symbols. It does not rule out higher-memory or hidden-state models, since the four-cell refinement itself is Markov; it establishes that the **binary factor** has infinite memory. It does not quantify actual reservoir-computing performance or mixing of arbitrary observables. An earlier specialized exact ordinal-run computation may exist outside the inspected references. Independent validation and independent historical-priority audit have not been performed.

## References

1. Potratzki, de Jong, Small and Bröhl, *Ordinal Pattern Transition Networks as a Symbolic Substrate for Reservoir Computing* (first public version 15 October 2026), arXiv:2610.21973v1, https://arxiv.org/html/2610.21973v1 .
2. Sakellariou, Stemler and Small, *Markov modeling via ordinal partitions: An alternative paradigm for network-based time-series analysis*, Physical Review E 100 (2019), 062307, DOI:10.1103/PhysRevE.100.062307; author-posted full text: https://www.researchgate.net/publication/338031445_Markov_modeling_via_ordinal_partitions_An_alternative_paradigm_for_network-based_time-series_analysis .
3. Amigó and Kennel, *Forbidden ordinal patterns in higher dimensional dynamics* (2007), related work on admissible and forbidden ordinal patterns; not a source for the exact run law here.
