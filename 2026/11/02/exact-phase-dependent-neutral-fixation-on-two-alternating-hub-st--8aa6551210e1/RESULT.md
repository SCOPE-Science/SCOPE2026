# Exact phase-dependent neutral fixation on two alternating hub stars

## Finding

In the neutral birth–death process on \(n\ge3\) vertices, alternate \(\tau\ge1\) steps on a star centered at \(A\) with \(\tau\) steps on a star centered at a different vertex \(B\), repeating indefinitely. Start exactly at the beginning of an \(A\)-star block. The neutral fixation probabilities of a single mutant placed at \(A\), at \(B\), or at any of the \(n-2\) other vertices are respectively
\[
\boxed{p_A=U/Z,\quad p_B=V/Z,\quad p_L=W/Z},
\]
where, setting
\[
x=\left(1-\frac{1}{n(n-1)}\right)^\tau,\qquad
 y=\left(\frac{n-2}{n(n-1)}\right)^\tau,
\]
we have
\[
\begin{aligned}
U&=(n-1)-x+(n^2-3n+3)y-(n-1)^2xy,\\
V&=(n-1)^2-(n^2-3n+3)x-(n-1)xy+y,\\
W&=(n-1)^2(1-xy)-x+y,\\
Z&=U+V+(n-2)W.
\end{aligned}
\]
For every finite \(n\ge3\) and \(\tau\ge1\), the probabilities are strictly ordered:
\[
\boxed{p_A<p_B<p_L},\qquad
p_B-p_A=\frac{(n-1)(n-2)(1-x)(1-y)}Z,
\qquad p_L-p_B=\frac{(n-1)(n-2)x(1-y)}Z.
\]
In particular, the two vertices that alternately serve as hubs have different neutral fixation probabilities, although each is a hub for exactly half the steps.

There is a sharp macroscopic switching-duration scale. For any sequence of integers \(\tau=\tau(n)\ge1\) such that \(\tau(n)/n^2\to\theta\in[0,\infty]\),
\[
\boxed{n^2p_A\to1,\qquad np_B\to1-e^{-\theta},\qquad np_L\to1,}
\]
with \(e^{-\infty}=0\). Thus the second-season hub changes from smaller-than-order-\(1/n\) fixation for \(\tau=o(n^2)\) to order-\(1/n\) fixation for \(\tau\) comparable to \(n^2\), while the first-season hub remains asymptotically of order \(1/n^2\).

For the shortest blocks, \(\tau=1\), the formulas simplify exactly to
\[
D=n^4-4n^3+6n^2-2n-2,\qquad
(p_A,p_B,p_L)=\frac1D\bigl((n-1)^2,\ n^2-n-1,\ (n-1)(n^2-n-1)\bigr).
\]
For fixed \(n\), as \(\tau\to\infty\), these tend to the reproductive values of the initially active star:
\[
p_A\to \frac1{(n-1)^2+1},\qquad
p_B,p_L\to\frac{n-1}{(n-1)^2+1}.
\]

## Assumptions and scope

The temporal graph has \(n\) labeled vertices. Its first active graph is the unweighted undirected star with center \(A\), followed after exactly \(\tau\) updates by the star with distinct center \(B\); the process repeats with period \(2\tau\). At every update the reproducing vertex is selected uniformly among all \(n\) vertices (neutral fitness), and one of its neighbors in the current graph is selected uniformly to have its type replaced. No self-replacement or mutations occur. All probabilities refer to eventual fixation from one mutant introduced at time zero, before the first \(A\)-star update. They are not probabilities for a uniformly random phase of introduction. \(\tau\) is a positive integer and the star switch is deterministic. The other \(n-2\) vertices are interchangeable.

The corresponding weighted aggregate static graph has edge \(AB\) of weight two and each other edge incident to \(A\) or \(B\) of weight one. Its static birth–death neutral values are
\[
\widetilde p_A=\widetilde p_B=\frac{2}{n^2-2n+4},\qquad
\widetilde p_L=\frac{n}{n^2-2n+4}.
\]
Thus aggregation erases a strict time-order effect at every finite switching interval; it does not reproduce the two distinct hub probabilities.

## Proof

Write the current type indicator at the two hubs and one representative ordinary leaf as \((X_A,X_B,X_L)\). All ordinary leaves have the same expected type when initialized symmetrically; to compute the probability for one mutant at an ordinary leaf, linearity instead lets us use the entire \(n\)-vertex expectation operator and extract any ordinary-leaf coordinate from the symmetric stationary row below.

A birth–death step on the \(A\)-centered star transforms the vector of expected indicators by
\[
M_A=\begin{pmatrix}
1/n&1/n&(n-2)/n\\
1/[n(n-1)]&1-1/[n(n-1)]&0\\
1/[n(n-1)]&0&1-1/[n(n-1)]
\end{pmatrix}.
\]
On the \(B\)-centered star it transforms it by
\[
M_B=\begin{pmatrix}
1-1/[n(n-1)]&1/[n(n-1)]&0\\
1/n&1/n&(n-2)/n\\
0&1/[n(n-1)]&1-1/[n(n-1)]
\end{pmatrix}.
\]
These formulas follow by conditioning on the uniformly chosen reproducer: a leaf is replaced with probability \(1/[n(n-1)]\) by its center, and the center is replaced with probability \(1/n\) by each leaf. Both matrices are row-stochastic and irreducible with positive diagonal. Each has three distinct eigenvalues
\[
1,\qquad \lambda=1-\frac1{n(n-1)},\qquad \mu=\frac{n-2}{n(n-1)}.
\]
For either matrix \(M\), write its spectral projectors as
\[
E_\lambda(M)=\frac{(M-I)(M-\mu I)}{(\lambda-1)(\lambda-\mu)},\quad
E_\mu(M)=\frac{(M-I)(M-\lambda I)}{(\mu-1)(\mu-\lambda)},\quad
E_1(M)=I-E_\lambda(M)-E_\mu(M).
\]
Consequently, for every integer \(\tau\ge1\),
\[
M^\tau=E_1(M)+xE_\lambda(M)+yE_\mu(M).
\]
The expected-indicator dynamics sampled at the starts of successive \(A\)-blocks have one-period matrix
\[
T=M_B^\tau M_A^\tau.
\]
This is a primitive row-stochastic three-state matrix; the full \(n\)-vertex mean dynamics have the same unique constant limit on a connected periodic network. Let \(q=(q_A,q_B,q_O)\) be the normalized positive stationary row of \(T\). The three-state directed-tree formula gives, up to a common factor,
\[
\begin{aligned}
q_A&\propto T_{BA}T_{OA}+T_{BA}T_{OB}+T_{BO}T_{OA},\\
q_B&\propto T_{AB}T_{OB}+T_{AB}T_{OA}+T_{AO}T_{OB},\\
q_O&\propto T_{AO}T_{BO}+T_{AO}T_{BA}+T_{AB}T_{BO}.
\end{aligned}
\]
Substituting the displayed spectral-projector identity into these three tree sums yields exactly the common positive factor
\[
F=\frac{(n-1)(1-xy)+x-y}{(n-1)^2(n^2-2n+2)}>0
\]
times the respective weights \(U,V,(n-2)W\). Hence
\[
(q_A,q_B,q_O)=\frac1Z(U,V,(n-2)W).
\]
This computation can alternatively be checked without the tree formula by substituting the same expressions into \(qT=q\); the standalone checker independently computes finite powers over rational numbers. Since \(T\) is primitive, its unique stationary row is positive. The full neutral process on a finite connected periodically switching graph almost surely reaches one of its two homogeneous absorbing states (the graphical dual has coalescing backward lineages, and there is a uniformly positive finite-block probability of coalescence). Therefore \(T^k\to\boldsymbol1 q\) for the expectation evolution, and its limiting coordinate under a single initial mutant is its fixation probability. As the ordinary-leaf group represents \(n-2\) identical vertices, the probability for one such vertex is \(q_O/(n-2)\), proving the exact formula.

Subtracting the displayed polynomials gives
\[
V-U=(n-1)(n-2)(1-x)(1-y),\quad
W-V=(n-1)(n-2)x(1-y).
\]
As \(0<x,y<1\), strict ordering follows. Substituting \(\tau=1\) yields the rational shortest-block formulas; setting \(x=y=0\) gives the long-block limit. The weighted aggregate graph formula follows from the standard undirected neutral birth–death reproductive value proportional to reciprocal weighted degree: the two hub degrees are \(n\), and each remaining vertex has degree \(2\).

For the growing-network limit, uniformly over all integer \(\tau\ge1\), \(0<y\le1/n\) and \(1-x\le\tau/[n(n-1)]\). These give \(ny(1-x)\to0\) uniformly because \(y\le n^{-\tau}\) and \(\tau/n^\tau\le1/n\). It follows directly from the displayed polynomials that
\[
U=n(1+o(1)),\qquad V=n^2(1-x)+O(n),\qquad W=n^2(1+o(1)),\qquad Z=n^3(1+o(1)),
\]
where the little-oh terms are uniform in \(\tau\). If \(\tau/n^2\to\theta\), the standard logarithmic expansion of \(x\) gives \(x\to e^{-\theta}\), including the endpoint \(\theta=\infty\). The three asserted limits follow.

## Verification

Run the supplied `verify.py` with Python 3 and SymPy. It independently computes exact \(2^n\)-state birth–death chains at period boundaries for small networks and compares their absorption probabilities against all three closed forms. It additionally checks the three-state matrix fixed-point identities, strict inequalities, special \(\tau=1\) rational formulas, and large-network scaling for specified samples. The completed run produced 48 exact matrix stationarity checks, 48 exact strict-order checks, 31 independent full-state fixation comparisons, 15 numerical scaling checks, and 98 rational special-case checks. These are reproducible finite checks; the infinite-family result is established by the preceding argument, not by enumeration.

## Relationship to prior work

Bhaumik and Masuda (2023) formulate the same neutral birth–death process on periodically switching networks; their Theorem 1 establishes fixation probability \(1/n\) after averaging uniformly over all starting vertices, and their general fixation method is a finite absorbing-state recurrence. They discuss switching star–complete and star–complete-bipartite networks, switching-order effects under selection, and static aggregation. Their paper does not state the site-resolved closed formulas, strict two-hub ordering, or \(n^2\) duration crossover for two stars with different centers. The present result does not claim the general recurrence or uniform-initialization theorem as new; indeed \((p_A+p_B+(n-2)p_L)/n=1/n\), exactly as required by that theorem.

Su, McAvoy, and Plotkin (2023) derive neutral reproductive-value formalisms for dynamic networks, but their focal-first update selects the receiver before its donor (death–birth), whereas the present process selects the reproducer first (birth–death). The general idea of a time-dependent reproductive-value vector is prior art. The explicit alternating-star expressions and threshold are the narrower finding evaluated here.

## Limitations

The theorem is neutral, requires unweighted stars with exactly two distinct centers and equal integer block lengths, and assumes introduction at the beginning of the first block. It makes no claim for positive or negative selection, random switching, arbitrary temporal graphs, or random initialization phases. The published general fixation recurrences necessarily entail special-case probabilities in principle, so priority concerns whether an equivalent closed formula and limit law have appeared elsewhere. An unidentified specialized calculation cannot be excluded by the searched literature. Neither independent external audit nor empirical biological applicability is established.

## References

- J. Bhaumik and N. Masuda, *Fixation probability in evolutionary dynamics on switching temporal networks*, arXiv:2304.00170 (first public 2023-03-31); *Journal of Mathematical Biology* 87, 64 (2023), https://doi.org/10.1007/s00285-023-01987-5. Source: https://arxiv.org/abs/2304.00170
- Q. Su, A. McAvoy, and J. B. Plotkin, *Strategy evolution on dynamic networks*, arXiv:2301.11982 (2023), https://arxiv.org/abs/2301.11982.
