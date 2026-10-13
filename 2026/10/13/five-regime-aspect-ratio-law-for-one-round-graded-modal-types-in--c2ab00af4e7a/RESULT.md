# Five-regime aspect-ratio law for one-round graded modal types in random epistemic grids

## Finding

Let \(0<p<1\) and \(a>0\) be fixed, and set \(m=\lfloor n^a\rfloor\). Independently color every cell of the \(m\times n\) grid with a single propositional atom, true with probability \(p\). The two named \(\mathsf{S5}\) accessibility relations connect all cells in the same row and all cells in the same column, including each cell itself. Graded diamonds can count an arbitrary finite number of successors of a specified color. Let \(K_1(n,a)\) be the number of cells' equivalence classes under all Boolean graded modal formulas of nesting depth at most one. Write \(v=p(1-p)\) and

\[
\phi_v(x)=\frac{e^{-x^2/(2v)}}{\sqrt{2\pi v}},\qquad
L_v=\int_{-\infty}^{\infty}\bigl(1-e^{-\phi_v(x)}\bigr)\,dx.
\]

**Theorem (complete polynomial-aspect spectrum at depth one).** As \(n\to\infty\), for every fixed \(a>0\),

\[
\frac{K_1(n,a)}{F_a(n)}\ \xrightarrow{\mathbb P}\ 1,
\]

where all logarithms are natural and

\[
F_a(n)=\begin{cases}
4\sqrt{2v(1-a/2)}\,n^{3a/2}\sqrt{\log n},&0<a<1/2,\\[2pt]
4L_v\sqrt{3v/2}\,n^{3/4}\sqrt{\log n},&a=1/2,\\[2pt]
16v\sqrt{(a-1/2)(1-a/2)}\,n^{(a+1)/2}\log n,&1/2<a<2,\\[2pt]
4L_v\sqrt{3v}\,n^{3/2}\sqrt{\log n},&a=2,\\[2pt]
4\sqrt{2v(a-1/2)}\,n^{3/2}\sqrt{\log n},&a>2.
\end{cases}
\]

In particular, on a square grid \(a=1\),

\[
K_1(n,1)\sim_{\mathbb P}8p(1-p)n\log n.
\]

The two transitions at \(a=1/2\) and \(a=2\) have genuinely different, Gaussian-occupancy constants; inserting either critical exponent into an adjacent noncritical formula is invalid. If \(\mathcal D_1\) denotes the Boolean algebra of all depth-at-most-one graded-modal definable subsets, then \(|\mathcal D_1|=2^{K_1(n,a)}\). Thus the theorem also gives the exact leading asymptotic of its base-two logarithm.

**Structural strengthening.** Let \(R\) be the number of distinct observed row sums and \(C\) the number of distinct observed column sums. In *all five regimes*,

\[
\frac{K_1(n,a)}{2RC}\ \xrightarrow{\mathbb P}\ 1.
\]

Thus nearly every possible marked/unmarked degree-pair signature actually occurs, even though row and column sums are dependent across the matrix.

## Assumptions and scope

The probability \(p\in(0,1)\) and exponent \(a>0\) are constants independent of \(n\); the entries are independent Bernoulli random variables. Each relation is reflexive and comprises a complete row or column equivalence class. There is one atomic proposition and unlimited finite counting thresholds; both modalities are named, so rows and columns are not interchangeable in the language. Equivalence is *within one marked model*, not across two random models. All asymptotic assertions are convergence in probability. The five regimes cover every fixed positive polynomial aspect exponent, including the boundary exponents. No assertion is made for \(p=p_n\), \(a=a_n\), or unbounded modal depth.

## Proof

**Step 1: an exact logical signature.** Let \(X_{ij}\in\{0,1\}\) denote the marking, \(D_i=\sum_jX_{ij}\), and \(E_j=\sum_iX_{ij}\). In the row modality the number of \(p\)-successors of \((i,j)\) is \(D_i\); in the column modality it is \(E_j\). Counts for \(\neg p\) are \(n-D_i\) and \(m-E_j\). Every depth-one graded formula is a Boolean combination of \(p\) and counting formulas whose depth-zero interiors are Boolean combinations of \(p\). Conversely, finite thresholds and negation test the exact values of both counts. Therefore two cells have identical depth-one theories if and only if their triples

\[
(X_{ij},D_i,E_j)
\]

are equal. In particular, \(K_1\le 2RC\), exactly for every finite matrix.

**Step 2: a reusable binomial occupancy lemma.** Suppose \(Y_1,\ldots,Y_t\) are independent \(\operatorname{Bin}(L,p)\) variables with \(L\to\infty\) a fixed positive power of \(n\), and let \(U\) be the number of distinct values observed. Let \(q_k=\Pr(Y_1=k)\). Stirling's formula gives, uniformly when \(|k-Lp|=O(\sqrt{L\log n})\),

\[
q_k=\frac{1+o(1)}{\sqrt{2\pi Lv}}
\exp\left(-\frac{(k-Lp)^2}{2Lv}\right).
\]

All following statements are convergence in probability.

(a) If \(t/\sqrt L\to0\) while \(t\to\infty\), then \(U/t\to1\). Indeed, \(t-U\) is bounded by the number of equal sampled pairs, whose expectation is at most \(\binom t2\max_kq_k=O(t^2/\sqrt L)=o(t)\).

(b) If \(t/\sqrt L\to1\), then \(U/\sqrt L\to L_v\). The exact expected occupancy is

\[
\mathbb EU=\sum_k\bigl[1-(1-q_k)^t\bigr].
\]

Put \(x=(k-Lp)/\sqrt L\), apply the displayed local approximation on bounded \(x\), and bound the remaining tails by the expected number of observations there. The sum becomes a Riemann integral with limit \(L_v\). For different \(k\ne l\), the occupied-bin indicators have nonpositive covariance, because

\[
(1-q_k-q_l)^t\le(1-q_k)^t(1-q_l)^t.
\]

Hence \(\operatorname{Var}(U)\le\mathbb EU=O(\sqrt L)\), and Chebyshev's inequality completes the concentration proof.

(c) If \(t/\sqrt L=n^{\beta+o(1)}\) with fixed \(\beta>0\), then

\[
U\sim2\sqrt{2Lv\beta\log n}.
\]

For every \(\varepsilon\in(0,1)\), every integer within \((1-\varepsilon)\sqrt{2Lv\beta\log n}\) of \(Lp\) has occupancy expectation at least \(n^{\beta(2\varepsilon-\varepsilon^2)+o(1)}\). A union bound makes all those values present. Outside the larger radius \((1+\varepsilon)\sqrt{2Lv\beta\log n}\), the number of distinct observed values is at most the number of observations there. A Bernstein tail bound shows that its expectation is \(o(\sqrt{L\log n})\). Markov's inequality, followed by \(\varepsilon\downarrow0\), proves the claim. This step uses no independence between row and column degrees; it is applied separately to two independent samples.

**Step 3: asymptotics of the two degree alphabets.** Row sums form an independent sample of size \(m\) from \(\operatorname{Bin}(n,p)\), and column sums independently form a sample of size \(n\) from \(\operatorname{Bin}(m,p)\). The ratios governing their occupancy phases are

\[
\frac{m}{\sqrt n}=n^{a-1/2}(1+o(1)),\qquad
\frac{n}{\sqrt m}=n^{1-a/2}(1+o(1)).
\]

Apply parts (a), (b), (c) of Step 2 as appropriate to get

\[
R\sim_{\mathbb P}\begin{cases}
n^a,&0<a<1/2,\\
L_vn^{1/2},&a=1/2,\\
2\sqrt{2nv(a-1/2)\log n},&a>1/2,
\end{cases}
\]

and

\[
C\sim_{\mathbb P}\begin{cases}
2\sqrt{2n^av(1-a/2)\log n},&0<a<2,\\
L_vn,&a=2,\\
n,&a>2.
\end{cases}
\]

Each limit holds jointly with the other by elementary union bounds, even though row and column sums themselves are correlated.

**Step 4: almost all candidate triples occur.** For \(a<2\), put \(\beta=1-a/2>0\). Fix \(\varepsilon\in(0,1)\) and let \(I\) be the integer column-degree interval centered at \(mp\) with radius \((1-\varepsilon)\sqrt{2mv\beta\log n}\). For each row \(i\), color \(x\in\{0,1\}\), and degree \(k\in I\), independence across columns gives the exact one-column probability

\[
\Pr(X_{ij}=x, E_j=k)
=p^x(1-p)^{1-x}\Pr\bigl(\operatorname{Bin}(m-1,p)=k-x\bigr).
\]

The local approximation in Step 2 bounds \(n\) times this probability below by \(n^{\delta}\), for a fixed \(\delta>0\) depending on \(a,p,\varepsilon\) and all sufficiently large \(n\). Therefore the probability that *any* row misses *either* color at *any* degree in \(I\) is bounded by a polynomial factor times \(e^{-n^\delta}\), which tends to zero. Select one representative row for each of the \(R\) different row sums; every selected row contains both colors at every column degree in \(I\). Hence, with high probability,

\[
2R|I|\le K_1\le2RC,
\quad\frac{|I|}{C}\xrightarrow{\mathbb P}1-\varepsilon.
\]

Let \(\varepsilon\downarrow0\). For \(a\ge2\), interchange rows and columns: the row-degree sample is in the large-occupancy regime, and each column contains both colors at every row degree in its central interval, giving the symmetric inequality. This proves \(K_1/(2RC)\to1\) for every \(a>0\).

**Step 5: the five constants.** Multiply the corresponding expressions for \(R\) and \(C\) from Step 3 and use Step 4. The listed \(F_a\) follow directly. For example, at \(a=1\) the two degree alphabets each have \((2\sqrt{v n\log n})(1+o_{\mathbb P}(1))\) elements, so twice their product is \((8vn\log n)(1+o_{\mathbb P}(1))\). At \(a=1/2\) or \(a=2\), the critical occupancy integral replaces the logarithmic-width law on exactly one side, producing the two displayed exceptional constants. This proves every part of the theorem.

## Verification

The companion standard-library script `verify.py` exhaustively compares the triple signature against a direct evaluation of all primitive graded depth-one formula truth vectors on 9,418 binary matrices (every rectangular shape with sides at most four and at most twelve cells). It independently evaluates the exact binomial occupancy expectation and the Gaussian critical integral at three probabilities and three lengths, and runs 32 finite random-rectangle checks at eight exponent/size combinations. A successful local run ended with:

```text
VERIFY_OK exhaustive_matrices 9418 critical_PMF_cases 9 random_rectangular_cases 32
```

Exhaustive finite checks validate the semantics and implementation, not convergence for arbitrarily large matrices. The analytic limits rely on the Stirling/Bernstein estimates, occupancy calculation, and uniform one-sided color-coverage argument in the proof.

## Relationship to prior work

Otto's graded modal bisimulation work supplies the modal-depth/graded back-and-forth semantics. Ahvonen, Heiman and Kuusisto identify the corresponding graded multimodal types and counting message-passing refinement. Neither inspected full text studies random row-column equivalence grids or quantitative first-round type capacity. Liebenau and Wormald analyze asymptotic enumeration of random bipartite graphs by their degree sequences, providing important context for degree distributions; their theorems neither define graded modal types on cells nor assert the joint marked/unmarked degree-pair occupancy that produces \(K_1\).

A qualitative statement that depth one fails to separate all worlds on a large square frame does not determine its precise number of distinguishable types. The contribution here is the **sharp first-round count**, the degree-pair saturation property, the five polynomial-aspect regimes, and the two critical constants. General binomial occupancy and moderate deviations are used as standard tools, not claimed as original. Independent originality review could still find antecedents under graph-refinement or incidence-matrix terminology.

## Limitations

All five limits hold at fixed \(p\) and fixed exponent \(a\); varying-density or near-critical moving aspect exponents may require crossover scaling not addressed here. The theorem concerns a single graded-modal round, not ordinary modalities, bounded counting thresholds, or later refinement rounds. No claim is made about a limiting distribution of centered fluctuations. The proof is analytic, with independent finite checks as supporting reproducibility; an independent mathematical or literature audit has not yet been performed.

## References

1. M. Otto, *Graded modal logic and counting bisimulation*, arXiv:1910.00039, version 1 publicly submitted 2019-09-30. https://arxiv.org/abs/1910.00039
2. V. Ahvonen, D. Heiman and A. Kuusisto, *Graded modal logic and counting message passing automata*, arXiv:2401.06519, version 1 publicly submitted 2024-01-12. https://arxiv.org/abs/2401.06519
3. A. Liebenau and N. Wormald, *Asymptotic enumeration of digraphs and bipartite graphs by degree sequence*, arXiv:2006.15797, version 1 publicly submitted 2020-06-29; *Random Structures & Algorithms* (2023), DOI:10.1002/rsa.21105. https://arxiv.org/abs/2006.15797
