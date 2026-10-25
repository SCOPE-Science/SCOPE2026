# Polynomial lower growth of leaf-neighbour counts in a mixed friend-tree model

## Finding

Fix a parameter \(p\in(0,1/2)\). In the mixed friend-tree process defined below, for every fixed vertex label \(v\), the number \(L_n(v)\) of its leaf neighbours satisfies

\[
\liminf_{n\to\infty} n^{-(1-2p)}\,\mathbb E\big[(L_n(v)-1)_+\big]
\;\ge\; C_{v,p}\;>0,
\]

where \((x)_+=\max\{x,0\}\). One explicit admissible constant is

\[
C_{v,p}=b_{v,p}\frac{\Gamma(m_v)}{\Gamma(m_v+1-2p)},\qquad
(m_v,b_{v,p})=
\begin{cases}
(3,p/2),&v\in\{1,2\},\\
(v+2,p^2/[v(v+1)]),&v\ge3.
\end{cases}
\]

This is an expectation lower bound; it does not assert almost-sure polynomial growth or a matching upper bound.

## Assumptions and scope

Start from the single edge \(T_2\) on vertices \(1,2\). At each step with current tree \(T_n\), choose \(V_n\) uniformly from its \(n\) vertices. Independently, with probability \(p\) attach the new vertex \(n+1\) to \(V_n\); with probability \(1-p\), attach it to a uniformly chosen neighbour \(W_n\) of \(V_n\). Choices at different steps are independent conditional on the current tree. Fix \(v\) and let \(D_n(v)\) be its degree and \(L_n(v)\) the number of neighbours of degree one in \(T_n\), for \(n\ge\max\{2,v\}\). The result is only for \(0<p<1/2\).

## Proof

Write \(\mathcal F_n\) for the tree history through time \(n\), put \(L=L_n(v)\), \(D=D_n(v)\), and define

\[
S=\sum_{\substack{u\sim v\\D_n(u)\ge2}}\frac1{D_n(u)}\ge0.
\]

The count \(L_n(v)\) increases by one if the new vertex attaches to \(v\), and decreases by one if a current leaf-neighbour of \(v\) receives the new edge. Therefore

\[
\Pr(\Delta L=1\mid\mathcal F_n)=\frac{p+(1-p)(L+S)}n,
\qquad
\Pr(\Delta L=-1\mid\mathcal F_n)=\frac{pL+(1-p)L/D}n.
\]

The first formula separates the direct attachment to \(v\), of probability \(p/n\), from redirection through each neighbour \(u\), of probability \((1-p)/(nD_n(u))\). In the second formula, each of the \(L\) leaf-neighbours ceases to be a leaf either when it is chosen directly (probability \(p/n\)) or when \(V_n=v\) and redirection selects that leaf (probability \((1-p)/(nD)\)). These are the only ways to change \(L_n(v)\), and its increment lies in \(\{-1,0,1\}\).

Subtracting the two probabilities gives the exact drift identity

\[
\mathbb E[\Delta L\mid\mathcal F_n]
=\frac{(1-2p)(L-1)+(1-p)(1-L/D+S)}n.
\]

Since \(L\le D\) and \(S\ge0\), the second term in the numerator is nonnegative. Let \(c=1-2p>0\) and \(Y_n=(L_n(v)-1)_+\). If \(L_n(v)\ge2\), then \(\Delta Y_n=\Delta L_n(v)\), so the drift identity yields

\[
\mathbb E[Y_{n+1}\mid\mathcal F_n]\ge(1+c/n)Y_n.
\]

If \(L_n(v)\le1\), then \(Y_n=0\) and \(Y_{n+1}\ge0\), so the same inequality holds. Taking expectations and iterating, for any \(m\) with \(a_m=\mathbb E Y_m>0\),

\[
\mathbb E Y_n\ge a_m\prod_{k=m}^{n-1}\left(1+\frac ck\right)
=a_m\frac{\Gamma(n+c)\Gamma(m)}{\Gamma(n)\Gamma(m+c)},\qquad n\ge m.
\]

It remains to give a positive starting value. If \(v=1\) or \(v=2\), the initial neighbour is a leaf at time two; a direct attachment to \(v\) at that step, of probability \(p/2\), leaves both that neighbour and the new vertex as leaf-neighbours of \(v\). Thus \(m_v=3\) and \(\mathbb E Y_{m_v}\ge p/2\). If \(v\ge3\), the event that the next two arrivals attach directly to \(v\) has probability \(p^2/[v(v+1)]\); at time \(v+2\), these two new vertices are leaf-neighbours of \(v\). Thus \(m_v=v+2\) and \(\mathbb E Y_{m_v}\ge p^2/[v(v+1)]\). Substituting these bounds for \(a_m\), dividing by \(n^c\), and using \(\Gamma(n+c)/(\Gamma(n)n^c)\to1\) proves the stated lower bound and constant.

## Verification

The transition probabilities enumerate all possible changes of the fixed vertex's leaf-neighbour count. The exact drift identity follows by direct algebra; its remainder over \(c(L-1)/n\) is \((1-p)(1-L/D+S)/n\ge0\). The multiplicative product is evaluated exactly by the gamma recurrence \(\Gamma(x+1)=x\Gamma(x)\), and the limiting constant uses the standard gamma-ratio asymptotic. No finite experiment is used as proof. The claim concerns an expectation only; no almost-sure lower bound, exact exponent, upper bound, or phase transition is asserted.

## Relationship to prior work

Addario-Berry, Briend, Devroye, Donderwinkel, Kerriou, and Lugosi introduce the random friend tree and discuss a mixture that attaches directly to the sampled vertex with probability \(p\) and to a uniformly sampled neighbour with probability \(1-p\). Their paper gives a qualitative degree-divergence observation for this variant, but the inspected statement does not give a polynomial lower bound for the expected number of leaf-neighbours of a fixed vertex. Cannings and Jordan study the same zero-step/one-step random-walk mixture through the global proportion of leaves and obtain bounds on its limiting lower and upper values; those global bounds do not imply the fixed-vertex estimate proved here. The present result supplies a local expectation bound for the mixed model; it does not determine the exact growth exponent or establish a phase transition.

## Limitations

The exponent \(1-2p\) is a proven lower-bound exponent, not a claimed exact growth exponent or a demonstrated phase transition. The proof does not establish almost-sure growth of \(L_n(v)\), nor any upper bound. The constant depends on the fixed label and on \(p\). Unindexed literature on local statistics in mixed random-walk attachment trees may contain related estimates.

## References

1. L. Addario-Berry, S. Briend, L. Devroye, S. Donderwinkel, C. Kerriou, and G. Lugosi, “Random friend trees,” arXiv:2403.20185v1, first posted 29 March 2024; later published in *Random Structures & Algorithms*. The arXiv source gives the model, the primary MSC 60C05, and the mixed-attachment variant.
2. C. Cannings and J. Jordan, “Random walk attachment graphs,” *Electronic Communications in Probability* 18 (2013), no. 77, 1–5; arXiv:1303.1052v2. This treats random-walk lengths zero and one and bounds the global leaf proportion.
