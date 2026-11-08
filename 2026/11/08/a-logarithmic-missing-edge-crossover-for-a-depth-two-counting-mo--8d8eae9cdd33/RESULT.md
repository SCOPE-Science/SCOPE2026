# A logarithmic missing-edge crossover for a depth-two counting-modal formula

## Finding

Let \(\varepsilon_n\in[0,1]\) satisfy \(\varepsilon_n\to0\). On \(n\) labelled worlds, fix a root \(o\), independently assign one proposition \(p\) to each world with probability \(1/2\), and put each directed edge, including each loop, independently with probability \(1-\varepsilon_n\). In the counting modal language, \(\#\theta\) denotes the number of successors satisfying \(\theta\), and \(\top\) denotes truth. Define

\[
 E := (\#\top=2\#p),\qquad
 O := (\#\top=2\#p-1),\qquad
 \Psi := (\#E\ge\#O).
\]

Let \(\Phi\) denote the standard normal distribution function, with \(\Phi(+\infty)=1\). Then, with natural logarithms,

\[
 \boxed{\Pr(\Psi\text{ holds at }o)
   =\frac32-\Phi\!\left(\sqrt{\varepsilon_n\log n}\right)+o(1).}
\]

In particular, when \(\varepsilon_n\log n\to a\in[0,+\infty]\), the limiting probability is \(3/2-\Phi(\sqrt a)\). Thus the critical scale is missing-edge probability \(a/\log n\): the limit changes continuously from \(1\) at \(a=0\) to \(1/2\) at \(a=+\infty\). This is one theorem about the same fixed depth-two formula across the whole near-complete regime, not an assertion about every formula in the counting-modal language.

## Assumptions and scope

Models are finite, directed, labelled, and loop-allowing. Ordered edges and atomic valuations are mutually independent, and the unary predicate has fixed fair probability \(1/2\). The root is one predetermined label. In \(E\), equality means the outdegree equals twice the number of outgoing \(p\)-successors; in \(O\), it equals twice that number minus one. Successors are counted as distinct vertices, so a loop contributes one successor. Only the regime \(\varepsilon_n\to0\) is covered. All limits are along positive integers \(n\to\infty\), with \(\log\) the natural logarithm.

The formula \(\Psi\) was introduced as a nonconvergent example for full regular rooted trees with deterministic branching degree in Ghosh--Schwarzentruber (2026, Section 6.1); the present result concerns the distinct random directed-graph ensemble and a logarithmic near-complete edge-thinning window.

## Proof

**1. Conditional reduction.** Set \(r_n=1-\varepsilon_n\). Encode the colors by \(s_w=+1\) when \(p\) is false at \(w\) and \(s_w=-1\) when it is true, and put \(B=\sum_w s_w\). Then \(B/\sqrt n\Rightarrow Z\), where \(Z\) is standard normal. At a vertex \(v\), define \(D_v=\sum_w s_w R(v,w)\). The events \(E\) and \(O\) are respectively \(D_v=0\) and \(D_v=-1\).

Conditional on all colors, write \(K=(n-B)/2\) and \(L=(n+B)/2\). The variables \(D_v\) are independent across distinct rows, each distributed as \(Y-X\) for independent \(Y\sim\operatorname{Bin}(L,r_n)\) and \(X\sim\operatorname{Bin}(K,r_n)\). Put \(q_j(B)=\Pr(D_v=j\mid (s_w)_w)\), for \(j=0,-1\).

For \(v\ne o\), the root edge \(R(o,v)\) is independent of row \(v\). Therefore the difference between the two root successor counts, excluding the possible root self-successor, is a sum \(T_n\) of \(n-1\) independent, identically distributed terms, conditional on the colors, with

\[
\Pr(U_v=+1)=r_nq_0(B),\quad
\Pr(U_v=-1)=r_nq_{-1}(B),\quad
\Pr(U_v=0)=1-r_n(q_0(B)+q_{-1}(B)).
\]

The omitted self-successor contributes an integer of absolute value at most \(1\), and is nonzero only if \(D_o\in\{0,-1\}\). Unconditionally \(D_o\) is the sum of \(n\) independent terms that are \(\pm1\) with probabilities \(r_n/2\) each and \(0\) with probability \(\varepsilon_n\). Conditioning on the number of nonzero terms (which is \(\operatorname{Bin}(n,r_n)\)) and applying the elementary maximum-binomial-atom bound shows \(\Pr(D_o\in\{0,-1\})=O(n^{-1/2})\). It consequently suffices to analyze \(\Pr(T_n\ge0)\).

**2. Local probabilities when there are sufficiently many missing edges.** Fix \(C>0\) and \(c>0\). Uniformly for \(|B|\le C\sqrt n\) and \(\varepsilon_n\ge c/\log n\), provided \(\varepsilon_n\to0\), the two lattice point probabilities obey

\[
q_j(B)=\frac{\exp\left(-\frac{(r_nB-j)^2}{2n r_n\varepsilon_n}\right)}
 {\sqrt{2\pi n r_n\varepsilon_n}}
 \left(1+O_{C,c}\left(\frac{(\log n)^2}{\sqrt n}\right)\right),
 \qquad j\in\{0,-1\}.
\]

Here is a derivation sufficient for the moderate-deviation range used. Let \(V\sim\operatorname{Bin}(K,\varepsilon_n)\) and \(U\sim\operatorname{Bin}(L,\varepsilon_n)\) be independent missing-edge counts. Then \(D_v=B-(U-V)\). The cumulant generating function of \(U-V\) is

\[
 H(t)=L\log(1-\varepsilon_n+\varepsilon_n e^t)
       +K\log(1-\varepsilon_n+\varepsilon_n e^{-t}).
\]

Its first two derivatives at zero are \(H'(0)=\varepsilon_n B\) and \(H''(0)=n\varepsilon_n r_n\). On a fixed neighborhood of zero, its third and higher fixed derivatives are \(O(n\varepsilon_n)\). The exponential tilt solving \(H'(t)=B-j\) therefore has \(t=O_{C,c}(1/(\varepsilon_n\sqrt n))=O(\log n/\sqrt n)\). Taylor's theorem gives the tilted rate

\[
 t(B-j)-H(t)=\frac{(r_nB-j)^2}{2n r_n\varepsilon_n}
           +O_{C,c}\left(\frac{(\log n)^2}{\sqrt n}\right).
\]

Under this tilt, summands remain independent lattice Bernoulli variables with individual nonzero probabilities comparable to \(\varepsilon_n\), and total variance \(n r_n\varepsilon_n(1+o(1))\). For each such Bernoulli factor with success probability \(u\), the characteristic-function modulus is at most \(\exp[-2u(1-u)\sin^2(t/2)]\); the product is consequently bounded by \(\exp[-c n\varepsilon_n\sin^2(t/2)]\) uniformly outside the central Fourier region. Expanding the centered log-characteristic function there as \(-\tfrac12 n r_n\varepsilon_n t^2+O(n\varepsilon_n(|t|^3+|t|^2\log n/\sqrt n))\), then integrating on the Gaussian scale \(t=O((n\varepsilon_n)^{-1/2})\), gives the centered local central limit estimate \((2\pi n r_n\varepsilon_n)^{-1/2}(1+O((n\varepsilon_n)^{-1/2}+O(\log n/\sqrt n)))\): outside a shrinking neighborhood of frequency zero the characteristic function is exponentially suppressed in \(n\varepsilon_n\), while near zero a cubic Taylor remainder has order \(O((n\varepsilon_n)^{-1/2})\). This yields the displayed relative estimate. It is a local approximation in a moderate-deviation regime, not an inference from a central limit theorem without local control.

In particular, uniformly on the same domain,

\[
 q_0(B)+q_{-1}(B)=O_{C,c}\!\left(\sqrt{\frac{\log n}{n}}\right),
\qquad
 \frac{q_{-1}(B)}{q_0(B)}=1+O_{C,c}\!\left(\frac{(\log n)^2}{\sqrt n}\right).
\]

Define \(M_n=(n-1)r_n(q_0(B)+q_{-1}(B))\). If \(M_n\to\infty\) for a sequence of color profiles with \(|B|\le C\sqrt n\), the conditional variance of \(T_n\) is asymptotic to \(M_n\) and the conditional mean divided by its standard deviation is at most

\[
 O_{C,c}\!\left(\sqrt{M_n}\frac{(\log n)^2}{\sqrt n}\right)
 =O_{C,c}\!\left(n^{-1/4}(\log n)^{9/4}\right)=o(1).
\]

The bounded independent summands satisfy Lindeberg's condition, so \(\Pr(T_n\ge0\mid (s_w)_w)\to1/2\). If instead \(M_n\to0\), a union bound gives \(\Pr(T_n=0\mid (s_w)_w)\to1\), so \(\Pr(T_n\ge0\mid (s_w)_w)\to1\). These statements hold uniformly wherever \(M_n\) diverges to infinity or tends to zero uniformly.

**3. The critical logarithmic window.** Suppose \(\varepsilon_n\log n\to a\in(0,\infty)\). For \(|B|\le C\sqrt n\), the local estimate gives

\[
 \frac{\log M_n}{\log n}
 =\frac12-\frac{(B/\sqrt n)^2}{2a}+o(1)
\]

uniformly when \(B/\sqrt n\) ranges over a fixed compact set. Thus \(M_n\to\infty\) if \(|B|/\sqrt n<\sqrt a\) stays a fixed distance below \(\sqrt a\), and \(M_n\to0\) if it stays a fixed distance above \(\sqrt a\). Since the standard normal has no atom at either boundary, conditioning on \(B\) and letting the boundary neighborhood shrink yields

\[
 \lim\Pr(\Psi)=\frac12\Pr(|Z|<\sqrt a)+\Pr(|Z|>\sqrt a)
 =\frac32-\Phi(\sqrt a).
\]

**4. Both end regimes.** If \(\varepsilon_n\log n\to+\infty\), then on every \(|B|\le C\sqrt n\), the local estimate implies \(\log M_n=(1/2+o(1))\log n\); the conditional sign tends to \(1/2\). Tightness of \(B/\sqrt n\) gives overall limit \(1/2\).

If \(\varepsilon_n\log n\to0\), fix \(0<\delta<C\) and restrict to \(\delta\sqrt n\le|B|\le C\sqrt n\). Writing \(D_v=B-(U-V)\), the target values \(0,-1\) require a deviation of order at least \(\delta\sqrt n\) of \(U-V\) from its mean \(\varepsilon_nB\). Bernstein's inequality for the independent bounded missing-edge contributions gives, for some \(c_{\delta,C}>0\),

\[
 q_0(B)+q_{-1}(B)\le
 4\exp\!\left[-\frac{c_{\delta,C}}{\varepsilon_n+n^{-1/2}}\right].
\]

Because \(\varepsilon_n+n^{-1/2}=o(1/\log n)\), it follows that \(M_n\to0\) uniformly. The normal limit for \(B/\sqrt n\) makes the excluded event \(|B|/\sqrt n<\delta\) arbitrarily rare by taking \(\delta\downarrow0\), while \(|B|>C\sqrt n\) is arbitrarily rare for large \(C\). Hence the probability of \(\Psi\) tends to \(1\).

Finally, for arbitrary \(\varepsilon_n\to0\), every subsequence of \(a_n=\varepsilon_n\log n\) has a further subsequence converging in the compact extended interval \([0,+\infty]\). The three cases above and continuity of \(a\mapsto3/2-\Phi(\sqrt a)\) force the claimed moving-parameter approximation by a subsequence contradiction.

## Verification

The included standalone `checker.py` uses only Python's standard library. It separately computes the conditional binomial-convolution probabilities for every color split through size eleven, and exhaustively evaluates all labeled directed graphs with loops and all unary valuations through four worlds. It checks that the conditional difference excluding the root self-edge has exactly the trinomial law used in the proof, and that the only possible discrepancy is the self-edge term. Run `python3 checker.py`; a successful run ends with `NEAR_COMPLETE_MODAL_BALANCE_EXACT_CHECKS_OK`.

These finite checks test the reduction, not the large-deviation estimate or the infinite limiting theorem. The asymptotic argument is given in the proof above.

## Relationship to prior work

Ghosh and Schwarzentruber, *On Counting Graphs for Modal Logic with Counting* (arXiv:2610.26187v1, first submitted October 19, 2026), Section 6.1, identify exactly this formula as a nonconvergence witness for complete rooted trees with a prescribed branching factor. Their Section 7 explicitly poses convergence questions for random graphs. The present graph result concerns independent random edges and the previously untreated near-complete missing-edge scale; it does not contradict the tree nonconvergence theorem.

Neighborhood-balance papers including Almeida (arXiv:2512.24293) and Collins--Hook--McBee--Trenk (arXiv:2603.05705) study the existence and structure of balanced colorings of undirected graphs. They do not imply the probability of this fixed randomly assigned unary predicate and directed counting-modal root formula. Benedikt and Zhukovskii (arXiv:2602.17752) study aggregate concentration on undirected Erdős--Rényi graphs at fixed dense or polynomial sparse probabilities. Their inspected full-text main results do not cover directed near-complete edge probabilities tending to one at a logarithmic rate, nor the stated exact threshold profile.

## Limitations

The statement applies to the specific depth-two formula displayed, a fixed root, independent fair vertex labels, independent ordered edges, and the near-complete regime. It does not establish decidability of convergence for arbitrary counting-modal formulas, does not establish analogous results for undirected edges or non-fair colors, and supplies no uniform quantitative error bound in the moving-parameter approximation. Earlier specialist probability or logical-limit-law literature could express an equivalent result under different terminology. The finite checker does not constitute independent validation of the asymptotic proof.

## References

1. Avijeet Ghosh and François Schwarzentruber, *On Counting Graphs for Modal Logic with Counting*, arXiv:2610.26187v1 (October 19, 2026), Sections 3, 4, 6.1, 7. https://arxiv.org/abs/2610.26187
2. Maurice Geneveiva Almeida, *Quasi Neighborhood Balanced Coloring of Graphs*, arXiv:2512.24293v1 (December 30, 2025). https://arxiv.org/abs/2512.24293
3. Karen L. Collins, Jonelle Hook, Cayla McBee and Ann N. Trenk, *Color 2-switches and neighborhood λ-balanced graphs with k colors*, arXiv:2603.05705v1 (March 5, 2026). https://arxiv.org/abs/2603.05705
4. Michael Benedikt and Maksim Zhukovskii, *A logical approach to concentration*, arXiv:2602.17752v1 (February 19, 2026). https://arxiv.org/abs/2602.17752
