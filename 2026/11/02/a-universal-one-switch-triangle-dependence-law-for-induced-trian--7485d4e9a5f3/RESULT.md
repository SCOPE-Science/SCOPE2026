# A universal one-switch triangle dependence law for induced triangle-free motifs in fixed-edge random graphs

## Finding

Let \(G\) be uniform among all simple graphs with vertex set \([n]\) and exactly \(m\) edges. Let \(T\) be its triangle count and \(X_H\) the number of \(h\)-vertex subsets inducing a fixed connected triangle-free graph \(H\), up to isomorphism. Put \(e=|E(H)|\) and
\[
 d=n-h,\qquad N=\binom n2,\qquad B=N-\binom h2,\qquad A=\binom d3+h\binom d2.
\]
For \(h\ge3\), \(n\ge h+3\), and every integer \(e+2\le m\le B+e\), let \(\mathcal A\) denote the event that a specified set of \(h\) vertices induces a graph isomorphic to \(H\). Then
\[
\mathbb E[T\mid\mathcal A]
=A\frac{(m-e)_{\underline3}}{B_{\underline3}}
+ed\frac{(m-e)_{\underline2}}{B_{\underline2}},
\qquad
\mathbb E[T]=\binom n3\frac{m_{\underline3}}{N_{\underline3}}.
\]
The quotient \(R(m)=\mathbb E[T\mid\mathcal A]/\mathbb E[T]\) is **strictly increasing in \(m\)**. Therefore the covariance \(\operatorname{Cov}(T,X_H)\) has at most one sign transition in the stated range, and any transition is from negative to positive. The covariance sign is identical for all connected triangle-free graphs having the same numbers of vertices and edges.

For \(n=7,h=4,e=3\), the path and claw have \(R(15)=15884/15925<1\) but \(R(16)=247/245>1\), giving a genuine crossing for two nonisomorphic induced motifs.

## Assumptions and scope

Graphs are finite, simple and labeled at the ambient level. Isomorphism in the event \(\mathcal A\) or in \(X_H\) means induced isomorphism, not merely containment. The graph \(H\) is connected and triangle-free, so \(e\ge h-1\ge2\); additionally \(e\le\binom h2\). The integer range ensures positive probability of \(\mathcal A\), at least two outside edges, and a strictly positive unconditioned triangle expectation. Falling factorials have the definition \((z)_{\underline k}=\prod_{i=0}^{k-1}(z-i)\). The theorem does not assert that every motif has a sign crossing; it establishes at most one crossing, and gives examples that have one.

## Proof

**Conditional triangle enumeration.** Given the complete induced graph on the distinguished \(h\)-set, the remaining \(B\) eligible edges form a uniformly chosen \((m-e)\)-set. A triangle can meet the distinguished set in zero, one, two, or three vertices. Respectively, the number of candidate triangles with all three edges unrestricted is \(\binom d3\), \(h\binom d2\), zero in the two-vertex case, and zero in the three-vertex case. There are instead exactly \(ed\) candidates with two distinguished vertices: their internal edge must be one of the \(e\) edges of \(H\), and the other two edges are unrestricted. Since \(H\) is triangle-free there are no internal triangles. This gives the conditional formula by elementary uniform-subset inclusion probabilities \((m-e)_{\underline k}/B_{\underline k}\). The unconditional formula follows by summing over \(\binom n3\) potential triangles.

**Strict ratio monotonicity.** Set \(x=m-e\) and
\[
 c=\frac{ed(B-2)}{A},\qquad
 K=\frac{A(N)_{\underline3}}{\binom n3(B)_{\underline3}}>0.
\]
Since \(d\ge3\), \(A>0\). Combining the conditional two-edge and three-edge contributions yields
\[
 R(m)=K\frac{x(x-1)(x-2+c)}{(x+e)(x+e-1)(x+e-2)}.
\]
Furthermore direct expansion shows
\[
3A-d(B-2)=\frac{d(d-3)(h-2)}2\ge0,
\quad\text{hence}\quad 0<c\le3e.
\]
Write \(P_c(x)=x(x-1)(x-2+c)\), \(Q(x)=(x+e)(x+e-1)(x+e-2)\), and \(J_c(x)=P'_c(x)Q(x)-P_c(x)Q'(x)\). For fixed \(x,e\), this derivative numerator is affine in \(c\). When \(c=0\), \(P_0/Q=\prod_{j=0}^2(x-j)/(x+e-j)\), a product of strictly increasing nonnegative functions of \(x\ge2\); the derivative is strictly positive, including at \(x=2\). At the other endpoint, symbolic expansion gives
\[
J_{3e}(x)=e(e-1)\{6y^3+(12e+21)y^2
 +(6e^2+30e+24)y+9e^2+20e+8\},\qquad y=x-2\ge0.
\]
This is positive for \(e\ge2\). Positivity of the affine function \(c\mapsto J_c(x)\) at both endpoints forces positivity for every \(0\le c\le3e\). Because \(Q(x)>0\), \(R(m)\) is strictly increasing (indeed on the real interval \(x\ge2\)).

**Covariance and sign.** Each fixed \(h\)-set has the same conditional triangle expectation, so linearity gives
\[
\operatorname{Cov}(T,X_H)
=\mathbb E[X_H]\bigl(\mathbb E[T\mid\mathcal A]-\mathbb E[T]\bigr).
\]
Both factors \(\mathbb E[X_H]\) and \(\mathbb E[T]\) are strictly positive in the stated range. The sign is therefore the sign of \(R(m)-1\), which can switch at most once and only from negative to positive. The conditional formula contains no structure of \(H\) beyond \(h,e\), proving the graph-shape invariance.

## Verification

The accompanying `verify.py` requires Python 3 and SymPy. It checks the analytic derivative identity exactly, the endpoint positivity polynomial, explicit enumeration of small labeled ambient graphs for induced paths, claws and cycles, and more than forty thousand rational finite-parameter instances. Run `python verify.py` after extracting the standalone file. These computations test, but do not replace, the preceding proof for arbitrary \(n,h,e,m\).

## Relationship to prior work

Classical random-graph subgraph-count results, including Ellis and Ferry's overlay-polynomial variance calculations, organize overlap effects for noninduced subgraph counts in \(G(n,p)\). Warnke studies random-graph concentration and an \(H\)-free process rather than these fixed-edge conditional triangle means. Their broader tools motivate comparing graph statistics but neither inspected statement supplies the all-\(H\) fixed-edge monotonic ratio or its positivity certificate. Ordinary overlap enumeration alone would not establish the sign of the ratio's derivative on the full admissible interval.

## Limitations

The theorem concerns fixed-edge \(G(n,m)\), not independent-edge \(G(n,p)\), and requires triangle-free \(H\), at least three outside vertices and \(m\ge e+2\). It does not classify whether a crossing exists for each parameter triple, nor claim a multi-scale stochastic ordering. Literature coverage is not exhaustive: closely related general overlap formulas could implicitly yield aspects of this result, and historical priority should not be inferred from search results alone. No independent audit has been performed.

## References

- L. Warnke, *On the method of typical bounded differences*, arXiv:1212.5796, first public 23 December 2012, https://arxiv.org/abs/1212.5796. The preprint records primary MSC 60C05.
- R. B. Ellis and J. P. Ferry, *Variance of the subgraph count for sparse Erdős–Rényi graphs*, Discrete Applied Mathematics **158** (2010), 649–658, https://doi.org/10.1016/j.dam.2009.11.012.
- C. Goldschmidt, S. Griffiths and A. Scott, *Moderate deviations of subgraph counts in the Erdős–Rényi random graphs \(G(n,m)\) and \(G(n,p)\)*, Oxford repository, https://ora.ox.ac.uk/objects/uuid:82787811-deea-46a4-9595-8a4f42d6cb43.
