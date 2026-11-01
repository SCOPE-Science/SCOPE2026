# Frequency-resolved Hausdorff ambiguity of full logistic directional itineraries

## Finding

Let \(F:[0,1]\to[0,1]\) be \(F(x)=4x(1-x)\). For \(x\) whose forward orbit never satisfies \(F^{n+1}(x)=F^n(x)\), record the **complete directional word** \(w(x)\in\{+,-\}^{\mathbb N_0}\), writing a plus when \(F^{n+1}(x)>F^n(x)\) and a minus when the inequality is reversed. For each prescribed word \(w\), let
\[
 E_w=\{x\in[0,1]:\operatorname{sgn}(F^{n+1}(x)-F^n(x))=w_n\text{ for every }n\ge0\}.
\]

**Theorem.** Suppose a binary word \(w\) contains infinitely many minus symbols, contains no consecutive minus symbols, and has a limiting minus frequency
\[
 p=\lim_{N\to\infty}\frac1N\#\{0\le n<N:w_n=-\}.
\]
Then \(E_w\) is uncountable and
\[
 \boxed{\dim_{\mathrm H}E_w=p,\qquad 0\le p\le\tfrac12.}
\]
For almost every \(x\) under the invariant arcsine measure \(d\mu(x)=dx/(\pi\sqrt{x(1-x)})\), the directional word satisfies \(p=1/3\). In particular the complete infinite directional observation of a typical point is consistent with a fractal set of initial points of **Hausdorff dimension \(1/3\)**.

The induced stationary two-symbol process is a Markov chain with transitions \(P(+\mid+)=P(-\mid+)=1/2\) and \(P(+\mid-)=1\). Its stationary minus fraction is \(1/3\) and its entropy rate is \((2/3)\log2\), below the underlying system's \(\log2\). These elementary symbolic statistics support the typical-fiber assertion and are **not** claimed as newly discovered formulas.

## Assumptions and scope

The logistic parameter is exactly \(4\). All directional comparisons are strict; the countable set of initial points whose forward orbit meets one of the fixed points \(0\) or \(3/4\) is omitted. Only words with infinitely many minus signs and with a limiting frequency are quantified. Such words are precisely the no-double-minus symbolic words in this regime, with the stated additional frequency condition. Geometric dimensions refer to the standard Euclidean metric on the initial-value interval, not to the symbolic metric. Hausdorff dimension is understood as the dimension of the entire observation fiber, not the dimension of a finite-time cylinder.

## Proof

**1. Exact tent conjugacy and the sign threshold.** Define \(T(t)=1-|1-2t|\) and \(h(t)=\sin^2(\pi t/2)\). The increasing homeomorphism \(h:[0,1]\to[0,1]\) satisfies \(F\circ h=h\circ T\). Directly on the two monotonicity intervals of \(T\), \(T(t)>t\) exactly when \(0<t<2/3\), and \(T(t)<t\) exactly when \(2/3<t\le1\); equality occurs at \(0\) and \(2/3\). Thus the directional itinerary is the two-cell observation at the threshold \(2/3\) of the tent map. Preimages of the equality points form a countable set.

**2. A three-cell Markov refinement.** Split the tent interval into
\[
 A=[0,1/2],\qquad B=[1/2,2/3],\qquad C=[2/3,1].
\]
Their possible transitions (ignoring endpoint duplications) are \(A\to A,B,C\), \(B\to C\), and \(C\to A,B\). The observed plus cell is \(A\cup B\) and the minus cell is \(C\). Hence no strict word contains \(--\). A word whose minus times are \(m_1<m_2<\cdots\) has gaps \(k_j=m_{j+1}-m_j\ge2\).

**3. Exactly two independent inverse branches for each return gap.** For any fixed gap \(k\ge2\), there are exactly two Markov itineraries from \(C\) back to \(C\), without an intermediate visit to \(C\):
\[
 C\,A^{k-1}\,C\quad\text{and}\quad C\,A^{k-2}B\,C.
\]
Every branch is affine with inverse slope magnitude \(2^{-k}\); each maps the whole return target \(C\) into an interval inside \(C\), and these two inverse intervals have disjoint interiors. For prescribed successive gaps \(k_1,\ldots,k_j\), concatenate either of the two possibilities at every return. This produces exactly \(2^j\) disjoint-interior inverse intervals, each of length \(|C|2^{-n_j}\), where \(n_j=k_1+\cdots+k_j\). No hidden itinerary is omitted, because \(B\) must be immediately followed by \(C\), and all prior intermediate cells must be \(A\). A finite prefix preceding the first minus imposes only a finite union of affine preimages and does not alter Hausdorff dimension. Removing countably many boundary-orbit points likewise does not change the dimensions; the unrestricted choices of two branches at every return also show that the strict fiber is uncountable.

**4. Upper dimension bound.** Among the first \(n_j\) observations following the first minus there are \(j+O(1)\) minus symbols. Hence the assumed frequency limit gives \(j/n_j\to p\). The stage-\(j\) cover consists of \(2^j\) intervals of diameter \((1/3)2^{-n_j}\). For every \(s>p\), the sum of the \(s\)-th powers of their diameters tends to zero, so \(\dim_{\mathrm H}E_w\le p\). This includes \(p=0\).

**5. Lower bound when \(p>0\).** Assign each of the two branch choices probability \(1/2\) independently at every prescribed return. The resulting Borel probability on the nested Cantor fiber gives each stage-\(j\) interval mass \(2^{-j}\). Because all such intervals are disjoint and have the same length \(L_j=(1/3)2^{-n_j}\), a ball of radius at most \(L_j\) meets at most four stage-\(j\) intervals. For \(L_{j+1}<r\le L_j\), its measure is at most \(4\,2^{-j}\). Since \(p>0\) and \(j/n_j\to p\), also \(j/n_{j+1}\to p\). Thus for any \(s<p\), eventually \(4\,2^{-j}\le C_s L_{j+1}^{s}\le C_s r^s\). The mass-distribution principle gives \(\dim_{\mathrm H}E_w\ge s\), and letting \(s\uparrow p\) proves equality. If \(p=0\), the already proved upper bound and nonemptiness give dimension zero.

**6. Transfer back to the logistic coordinate.** The conjugacy \(h\) is a smooth diffeomorphism with derivative bounded above and away from zero on every compact subinterval of \((0,1)\). Exhausting \((0,1)\) by countably many such compacts preserves Hausdorff dimensions. The endpoints contribute at most two points. Therefore the tent-coordinate fiber dimension agrees with \(\dim_{\mathrm H}E_w\).

**7. Typical frequency.** Under the invariant arcsine logistic measure, \(h^{-1}(x)\) is Lebesgue-uniform. The tent map is Lebesgue-ergodic. Since \(|C|=1/3\), the Birkhoff ergodic theorem gives minus frequency \(1/3\) almost everywhere. Equivalently, refining by \(A,B,C\) and elementary interval proportions yields the stated stationary two-symbol Markov chain. This completes the proof.

## Verification

Run `python3 verify_direction_fiber.py` with Python's standard library. It checks exactly (using rational arithmetic) all observed words of lengths 1 through 10 against the Markov probabilities, both return paths for every gap from 2 to 16, and selected multiple-gap families including exact interval lengths and separation. The checker also verifies the stationary sign distribution. The combinatorial and measure-theoretic proof above, not finite tests, establishes the infinite-word assertions. Finite computation is not substituted for the infinite-dimensional proof.

## Relationship to prior work

Dixit, Chauhan and Shrimali (2026) motivate direction-sign observations and phase ordering of the logistic map, but study predicted phase statistics and coupled lattices rather than dimensions of the full infinite-observation inverse fibers. Bollt, Stanford, Lai and Życzkowski (2001) rigorously analyze arbitrary tent-map threshold coding and loss of uniqueness; notably Section 8 constructs uncountably many indistinguishable initial states. Their result establishes nonuniqueness as prior art, but the inspected full text does not state the exact word-by-word Hausdorff-dimension formula \(\dim_{\mathrm H}E_w=p\) at the fixed \(2/3\) sign threshold. Pfante, Olbrich, Bertschinger, Ay and Jost (2013/2014) analyze information-theoretic coarse-graining and Markovian tent symbols, explicitly emphasizing the \(2/3\) threshold; their symbolic/statistical framework is prior art rather than a new claim here. The complete text of the last paper was not accessible at review, so whether a specialized geometric statement is present remains a priority risk. The present contribution is restricted to the **complete-fiber Hausdorff law** and its almost-sure \(1/3\) consequence.

## Limitations

The formula does not assert uniqueness or stability of recovering an initial condition; indeed typical complete sign observations leave a positive-dimensional ambiguity. It assumes the exact fully chaotic map and no observation noise. Frequency-nonconvergent words are outside the theorem. Dimension zero for sparse minus symbols does **not** imply a countable fiber. Historical priority is provisional, particularly because the complete 2013 tent coarse-graining text was inaccessible.

## References

1. S. Dixit, S. Chauhan, and M. D. Shrimali, *Predicting Phase Ordering in Chaotic Maps and Coupled Map Lattices*, arXiv:2609.00983v1 (first publicly submitted September 1, 2026), https://arxiv.org/abs/2609.00983.
2. E. M. Bollt, T. Stanford, Y.-C. Lai, and K. Życzkowski, *What symbolic dynamics do we get with a misplaced partition? On the validity of threshold crossings analysis of chaotic time-series*, Physica D **154** (2001), 259–286, https://doi.org/10.1016/S0167-2789(01)00242-1.
3. O. Pfante, E. Olbrich, N. Bertschinger, N. Ay, and J. Jost, *Closure measures for coarse-graining of the tent map*, MPI MIS Preprint 108 (2013), Chaos **24** (2014), 013136, https://doi.org/10.1063/1.4869075.
4. P. Walters, *An Introduction to Ergodic Theory*, Springer (1982), basic entropy and ergodic-theorem background.
