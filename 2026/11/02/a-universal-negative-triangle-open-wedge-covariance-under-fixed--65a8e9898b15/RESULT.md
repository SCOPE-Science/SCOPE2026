# A universal negative triangle–open-wedge covariance under fixed-edge conditioning

## Finding

Let \(n\ge4\), \(N=\binom n2\), and let \(G_{n,m}\) be uniform among simple graphs with vertex set \(\{1,\ldots,n\}\) and exactly \(m\) edges, for any integer \(0\le m\le N\). Let \(T\) count unordered three-vertex sets inducing three edges (triangles), and let \(S\) count unordered three-vertex sets inducing exactly two edges (open wedges, or induced paths of length two). Define

\[
Q_{n,m}=m(n^2-3n-8)+(n-1)(n^2-n-4).
\]

Then the **exact, all-density finite-size covariance** is

\[
\boxed{\operatorname{Cov}_{G_{n,m}}(T,S)
=-\frac{4m(m-1)(m-2)(N-m)(N-m-1)Q_{n,m}}
{(n+1)^2(n+2)(N-5)(N-4)(N-2)^2}.}
\tag{1}
\]

In particular,

\[
\boxed{\operatorname{Cov}_{G_{n,m}}(T,S)<0
\quad\Longleftrightarrow\quad 3\le m\le N-2.}
\tag{2}
\]

At all remaining allowable edge counts the covariance is exactly zero. The sign does not change with density, in contrast to independent-edge random graphs.

Specifically, under \(G(n,p)\), where each edge is independently present with probability \(p\in[0,1]\),

\[
\boxed{\operatorname{Cov}_{G(n,p)}(T,S)
=3\binom n3p^4(1-p)\bigl[2(n-3)-(3n-8)p\bigr].}
\tag{3}
\]

For \(0<p<1\), the latter covariance is positive below the sharp threshold \(p_c=2(n-3)/(3n-8)\), zero at the threshold, and negative above it. Hence conditioning on an exact edge count forces negative triangle–open-wedge covariance, although the corresponding independent-edge model has positive covariance at many edge densities. For example, at five vertices, \(\operatorname{Cov}_{G(5,5)}(T,S)=-185/252\), whereas \(\operatorname{Cov}_{G(5,1/2)}(T,S)=15/32\).

For any fixed \(0<p<1\), if \(m=m_n\) satisfies \(m_n/N\to p\), then

\[
\boxed{n^{-3}\operatorname{Cov}_{G_{n,m_n}}(T,S)
\longrightarrow -p^4(1-p)^2.}
\tag{4}
\]

The corresponding independent-edge covariance is of order \(n^4\) away from its threshold. Thus the sign reversal is accompanied by a change in fluctuation scale.

## Assumptions and scope

All graphs are simple, undirected, and labelled. The random variables \(T,S\) count **induced types on unordered vertex triples**; no rooted, oriented, or non-induced multiplicities are attached. In contrast, define the non-induced two-edge wedge count \(W=\sum_v\binom{\deg(v)}2\). Every induced open wedge contributes one to \(W\), and every triangle contributes three, so \(W=S+3T\). This distinction is essential: the assertion concerns \(\operatorname{Cov}(T,S)\), not \(\operatorname{Cov}(T,W)\).

All finite formulas require \(n\ge4\) and \(m\) integral in \([0,N]\). The independent-edge comparison holds for \(n\ge4\) and \(p\in[0,1]\). The asymptotic statement holds for deterministic sequences \(m_n\) with limiting edge fraction strictly between zero and one.

## Proof

Put \(A=\binom n3\), \(B=3A\), and for \(0\le j\le6\) define the hypergeometric edge-inclusion probability

\[
f_j=\frac{(m)_{\underline j}}{(N)_{\underline j}},
\qquad (z)_{\underline j}=z(z-1)\cdots(z-j+1).
\]

The numerator is taken to be zero when \(j>m\). Since \(n\ge4\), \(N\ge6\), so all denominators appearing here are nonzero. For any set of \(j\) distinct potential edges, the chance that every edge in that set occurs in \(G_{n,m}\) equals \(f_j\).

**Step 1: enumerate triangle–wedge overlaps.** Fix an unordered three-vertex set \(U\). Its triangle indicator is a product of three edge indicators. Among all \(B=3\binom n3\) potential non-induced two-edge wedges, exactly three lie on \(U\) and share two of the triangle's three edges; exactly \(6(n-3)\) have one edge in common with the triangle; and the remaining \(B-3-6(n-3)\) share no edge with it. Their respective joint inclusion probabilities with the triangle are \(f_3,f_4,f_5\). Every single wedge has mean \(f_2\). Summing over \(U\) gives

\[
\operatorname{Cov}(T,W)=A\Bigl[
3(f_3-f_3f_2)+6(n-3)(f_4-f_3f_2)
+\bigl(B-3-6(n-3)\bigr)(f_5-f_3f_2)\Bigr].
\tag{5}
\]

**Step 2: enumerate pairs of triangles.** For each \(U\), one triangle is the same triangle, and exactly \(3(n-3)\) different triangle triples share an edge with \(U\). Other triangle triples use six distinct edge coordinates in their joint indicator product. The respective joint inclusion probabilities are \(f_3,f_5,f_6\). Therefore

\[
\operatorname{Var}(T)=A\Bigl[
(f_3-f_3^2)+3(n-3)(f_5-f_3^2)
+\bigl(A-1-3(n-3)\bigr)(f_6-f_3^2)
\Bigr].
\tag{6}
\]

**Step 3: subtract and factor.** The identity \(S=W-3T\) yields

\[
\operatorname{Cov}(T,S)=\operatorname{Cov}(T,W)-3\operatorname{Var}(T).
\tag{7}
\]

Substitute (5) and (6) and the falling-factorial expressions for \(f_2,\ldots,f_6\). Cancelling the common denominator and factoring the numerator gives exactly (1), with \(Q_{n,m}\) as stated. This is an identity in the integer parameters, not an approximation or a numerical extrapolation; equations (5)–(7) also furnish an independent rational expression suitable for direct verification of the factorization.

**Step 4: certify the sign at every boundary.** The denominator of (1) is strictly positive for \(n\ge4\). When \(n\ge5\), \(n^2-3n-8>0\) and \((n-1)(n^2-n-4)>0\), so \(Q_{n,m}>0\) throughout \(0\le m\le N\). When \(n=4\), \(Q_{4,m}=4(6-m)\), which is positive throughout the only potentially strictly negative range \(3\le m\le4=N-2\). The product of the five remaining edge-count factors is positive precisely for \(3\le m\le N-2\), and zero otherwise. This proves (2), including both degenerate extremes.

**Step 5: compare the independent-edge ensemble.** In \(G(n,p)\), a set of \(j\) required edges is present with probability \(p^j\). Replace each \(f_j\) in (5) and (6) by \(p^j\). The same intersection counts and (7) simplify to (3). For \(0<p<1\), the leading factors in (3) are positive; the remaining affine factor changes sign at \(p_c=2(n-3)/(3n-8)\in(0,1)\). At \(p=0\) and \(p=1\), both motif counts are deterministic and the covariance is zero.

**Step 6: dense asymptotics.** Substitute \(N=n(n-1)/2\) and \(m_n/N\to p\) into the exact factorization (1). The leading terms \(m_n\sim pn^2/2\), \(N-m_n\sim(1-p)n^2/2\), and \(Q_{n,m_n}\sim pn^4/2\) give (4). No rate assumption beyond convergence of the edge fraction is required.

## Verification

The separate `check.py` uses only the Python standard library. It exhaustively enumerates all labelled simple graphs on four, five, and six vertices; computes \(T\), \(S\), and their covariance exactly as rational numbers; and independently compares those values to (5)–(7) and (1). For each such order it also enumerates the entire independent-edge probability distribution at five rational values of \(p\), verifying (3). A separate rational-arithmetic sweep checks (1) against (5)–(7) and its strict sign for every edge count on orders four through thirty. All 9,187 exact comparisons passed. Independently, symbolic cancellation of the rational functions in (5)–(7) and (1), and of their independent-edge analogues, returned identically zero. These calculations corroborate the algebra but do not replace Steps 1–6 as the all-parameter proof.

To reproduce the embedded finite checks: `python check.py`.

## Relationship to prior work

Goldschmidt, Griffiths and Scott (2019 preprint; 2020 journal version) study subgraph-count deviations in \(G(n,m)\) and \(G(n,p)\), using non-induced two-path and triangle counts, and provide general martingale expressions and asymptotic results. Their inclusion-exclusion treatment of induced counts and the common overlap-count method are relevant precursors. The present result isolates the **exact finite-parameter covariance of triangles against induced open wedges**, supplies its complete strict-sign classification for all edge counts, and contrasts that classification with the opposite sign possible in \(G(n,p)\). Those assertions do not follow merely from the cited asymptotic deviation estimates; the finite overlap calculation and factor-sign analysis are supplied here.

Neeman, Radin and Sadun (2021 preprint) analyze cycle-count moderate deviations in \(G(n,m)\). Their results concern triangle and longer cycle tails rather than the joint induced-wedge covariance. Classical random-graph subgraph counting and triad-census methods provide further background, but a general counting method or marginal deviation theorem should not be mistaken for an existing statement of the exact sign classification proved above.

## Limitations

The result treats the uniform fixed-edge and homogeneous independent-edge ensembles. It establishes covariance and its sign, not stochastic negative association, negative quadrant dependence, conditional monotonicity, causal effects of suppressing triangles, or analogous behavior for arbitrary random graph models. The independent-edge threshold concerns a joint covariance, not the mean clustering coefficient. The only asymptotic assertion is for a fixed limiting density in \((0,1)\). General subgraph moment-counting literature may contain equivalent specializations not identified here; independent historical-priority assessment remains outstanding.

## References

1. C. Goldschmidt, S. Griffiths and A. Scott, *Moderate deviations of subgraph counts in the Erdős–Rényi random graphs \(G(n,m)\) and \(G(n,p)\)*, arXiv:1902.06830, first posted 18 February 2019, https://arxiv.org/abs/1902.06830; Transactions of the American Mathematical Society 373 (2020), 5517–5585.
2. J. Neeman, C. Radin and L. Sadun, *Moderate Deviations in Cycle Count*, arXiv:2101.08249, first posted 20 January 2021, https://arxiv.org/abs/2101.08249.
