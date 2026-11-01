# Exact mean rendezvous times and a cube-root laziness transition on complete bipartite graphs

## Finding

**Theorem.** Let \(a,b\) be arbitrary positive integers and let \(K_{a,b}\) be the complete bipartite graph with parts \(A,B\). Two independent walkers start at prescribed vertices in opposite parts. At every integer time both simultaneously either hold their current positions with probability \(s\in(0,1)\), or independently move to a uniformly sampled neighbor with probability \(1-s\). Denote their first meeting time (in steps after time zero) by \(T_{a,b}(s)\), and put \(t=a+b\). Then

\[
M_{a,b}(s):=\mathbb E T_{a,b}(s)
=\frac{1}{2s(1-s)}+
\frac{4ab-3t+2+s(t-2)}{(1-s^2)(t+s-1)}.
\]

For every \(a,b\ge1\), \(M_{a,b}\) has exactly one global minimizer \(s_{a,b}\in(0,1)\). It satisfies \(s_{a,b}\le\tfrac12\), with equality if and only if \(a=b=1\). Let \(H=ab/(a+b)\). Along every sequence with \(\min(a,b)\to\infty\), including arbitrarily unbalanced parts,

\[
s_{a,b}\sim(16H)^{-1/3},\qquad
\min_{0<s<1}M_{a,b}(s)
=4H+3(H/4)^{1/3}+O(1).
\]

In the balanced case \(a=b=n\), this reads

\[
s_{n,n}\sim\frac{1}{2n^{1/3}},\qquad
\min_s M_{n,n}(s)=2n+\frac32n^{1/3}+O(1).
\]

In the opposite, star-like limit \(a=1\), \(b\to\infty\), the optimal holding probability and minimum mean converge to

\[
s_{1,b}\longrightarrow\frac{\sqrt3-1}{2},\qquad
\min_sM_{1,b}(s)\longrightarrow2+\sqrt3.
\]

Thus the optimal holding probability vanishes at a cube-root rate only when *both* sides become large. For \(a=b=n\), choosing the conventional constant \(s=\tfrac12\) has leading mean \(8n/3\), whereas optimized holding has leading mean \(2n\), a \(25\%\) first-order reduction. Setting \(s=0\) instead makes the meeting time infinite, because synchronous walks that start on opposite sides retain opposite parity.

## Assumptions and scope

All graphs are finite, undirected, simple, and complete bipartite, with both part sizes strictly positive. The two walkers use independent transition randomness, including independent holding decisions. Their moves occur synchronously in discrete time. A meeting means occupying **the same vertex at the same integer time**; crossing the same edge in opposite directions is not a meeting. The starting vertices are in opposite parts; symmetry makes their identities irrelevant. Expectations count steps starting with the first joint transition. The asymptotic assertions require both \(a\to\infty\) and \(b\to\infty\), without a restriction on their ratio. The star limit fixes one part at size one. For every \(s\in(0,1)\), the product chain has almost-sure finite absorption time and finite expectation.

## Proof

**1. Exact first-step system.** Write \(u=1-s\) and \(v=s(1-s)\). Until the walkers meet, symmetry distinguishes an opposite-part state \(O\), a pair of distinct vertices within \(A\), denoted \(A_d\), and a pair of distinct vertices within \(B\), denoted \(B_d\). Ignoring transitions that cause a meeting, the transient probability matrix, in that order, is

\[
Q=\begin{pmatrix}
s^2+u^2 &v(a-1)/a&v(b-1)/b\\
2v&s^2&u^2(b-1)/b\\
2v&u^2(a-1)/a&s^2
\end{pmatrix}.
\]

For instance, from \(O\) exactly one walker changes sides with probability \(2v\); conditional on its direction, it avoids the waiting walker with probability \((a-1)/a\) or \((b-1)/b\). When \(a=1\) or \(b=1\), the corresponding distinct-pair state is unreachable; its formal row is an algebraic convenience and is multiplied by zero in the reachable first-step equation. Equivalently one may delete it before solving.

The vector \(E=(E_O,E_A,E_B)^\top\) satisfies \((I-Q)E=\boldsymbol1\). Solving the latter two equations gives

\[
E_A=\frac{2a(2b+s-1)}{(1-s^2)(a+b+s-1)},\qquad
E_B=\frac{2b(2a+s-1)}{(1-s^2)(a+b+s-1)}.
\]

The first equation simplifies to

\[
E_O=\frac{1}{2s(1-s)}
+\frac{a-1}{2a}E_A+\frac{b-1}{2b}E_B.
\]

Substituting yields the stated exact formula. As \(s\downarrow0\) or \(s\uparrow1\), its first term diverges to infinity, so a global minimizer lies in the open interval.

**2. Unique minimum.** Set \(z=s/(1-s)>0\), \(x=a-1\ge0\), \(y=b-1\ge0\), \(t=a+b\), and \(p=ab\). Direct differentiation of the exact rational expression gives

\[
\frac{d}{dz}M_{a,b}\!\left(\frac{z}{1+z}\right)
=\frac{P(z)}{2z^2(2z+1)^2(tz+t-1)^2},
\qquad P(z)=\sum_{j=0}^{6}c_jz^j,
\]

where

\[
\begin{aligned}
c_0&=-(t-1)^2,\\
c_1&=-2(t-1)(3t-2),\\
c_2&=-(10x^2+28xy+34x+10y^2+34y+23),\\
c_3&=16x^2y+6x^2+16xy^2-4xy-22x+6y^2-22y-24,\\
c_4&=48x^2y+35x^2+48xy^2+94xy+40x+35y^2+40y+8,\\
c_5&=4(3t-2)(4p-t),\\
c_6&=4t(4p-t).
\end{aligned}
\]

For all positive integer part sizes, \(4p-t>0\). Consequently \(c_0,c_1,c_2<0\), while \(c_4,c_5,c_6>0\), with no restriction on \(c_3\). In descending order the coefficient sequence has exactly one sign change. Descartes' rule of signs therefore gives exactly one positive zero of \(P\), counted with multiplicity. Since \(P(0)<0\) and the leading coefficient is positive, this zero exists and is the unique point at which the derivative switches from negative to positive. The minimum is therefore unique.

Moreover, at \(z=1\) one computes

\[
P(1)=128x^2y+72x^2+128xy^2+240xy+72x+72y^2+72y\ge0,
\]

with equality exactly when \(x=y=0\). As the derivative changes sign only once, this establishes \(s_{a,b}\le1/2\), with equality precisely for \(K_{1,1}\).

**3. Two-large-part asymptotics.** Let \(H=ab/(a+b)\). Uniformly for positive integer \(a,b\) and \(0<s\le1/2\), elementary division of the exact expression gives

\[
M_{a,b}(s)=\frac{1}{2s(1-s)}+\frac{4H}{1-s^2}+O(1),
\]

where the \(O(1)\) constant is absolute. In fact, subtracting the two fractions gives exactly

\[
\frac{-3t+2+s(t-2)+4H(1-s)}{(1-s^2)(t+s-1)},
\]

whose absolute value is at most \(16\) on this parameter domain, since \(H\le t/4\), \(t\ge2\) and \(0<s\le1/2\). In particular,

\[
M_{a,b}(s)\ge4H+\frac{1}{2s}+4Hs^2-O(1).
\]

The elementary function \(1/(2s)+4Hs^2\) has its unique minimum at \(s_0=(16H)^{-1/3}\), with minimum \(3(H/4)^{1/3}\). For \(H\to\infty\), \(s_0<1/2\) eventually, and evaluation at \(s_0\) provides the matching upper bound

\[
M_{a,b}(s_0)=4H+3(H/4)^{1/3}+O(1),
\]

because \(Hs_0^4=O(H^{-1/3})\) and \(s_0\to0\). These bounds yield the optimal-value asymptotic. To locate the minimizer, write \(s=cH^{-1/3}\): uniformly on compact \(c\)-subintervals of \((0,\infty)\),

\[
H^{-1/3}\bigl(M_{a,b}(cH^{-1/3})-4H\bigr)
\longrightarrow\frac{1}{2c}+4c^2.
\]

The lower bound above excludes \(c\to0\) and \(c\to\infty\) for minimizing sequences, so uniqueness of the limiting minimum at \(c=16^{-1/3}\) gives \(s_{a,b}\sim(16H)^{-1/3}\). This argument remains valid when \(a/b\to0\) or infinity, as long as \(\min(a,b)\to\infty\), which is equivalent to \(H\to\infty\).

**4. Star limit.** With \(a=1\) and \(b\to\infty\), the exact expression converges locally uniformly on \((0,1)\) to

\[
M_\star(s)=\frac{1+2s}{2s(1-s)}.
\]

Its unique stationary point is \((\sqrt3-1)/2\), with value \(2+\sqrt3\). The divergence of the first term at both endpoints provides uniform exclusion of minimizers near the endpoints; hence the finite-size minimizers and minima converge to these values. This completes the theorem.

## Verification

The accompanying standalone \(\texttt{meeting\_checker.py}\) uses only Python's standard library. It independently constructs the full ordered-pair absorbing Markov chain on small complete bipartite graphs and solves its hitting-time linear system in exact rational arithmetic. It also independently solves the three-type first-step system, checks the required derivative sign properties over a finite parameter grid, and performs numerical large-size asymptotic diagnostics. Executing \(\texttt{python3 meeting\_checker.py}\) passed **793 exact or algebraic assertions** and **3 numerical asymptotic diagnostics**. The theorem's claims for all sizes and the scaling limit follow from the analytic proof above, not from finite enumeration.

## Relationship to prior work

Ohwa, *Exact computation for meeting times and infection times of random walks on graphs* (2015), develops general joint-chain recurrences and explicit continuous-time star and other graph laws. Its discrete-time general recurrence is compatible with the first-step method here; the particular complete-bipartite optimized-laziness law and cube-root theorem are not given in its inspected graph-specific sections. Kanade, Mallmann-Trenn and Sauerwald, *On coalescence time in graphs: When is coalescing as fast as meeting?* (first posted 2016-11-08), analyze meeting/coalescence bounds and the order of star meeting times, not the optimum holding probability for opposite-part synchronous starts. Van Belle and Klimovsky, *Meeting Times of Markov Chains via Singular Value Decomposition* (first posted 2024-06-07), supply general spectral meeting-time representations, but their inspected results do not state or optimize the present rational law. The result is an exact graph-family specialization and optimization, not an assertion that the general product-chain first-step principle is new. A potentially related 2023 thesis on rendezvous and network agents was not fully accessible; its indexed description concerns different graph families. These comparisons limit rather than certify historical priority.

## Limitations

The optimality theorem is for two **independent** walkers using the **same fixed holding probability**, beginning in opposite parts, and observing synchronized integer-time vertex meetings. It does not optimize unequal holding rates, adaptive controls, continuous-time clocks, edge-crossing meetings, or arbitrary bipartite graphs. The stated value estimate has absolute additive \(O(1)\) precision; no finer constant term or finite-parameter closed form for the unique polynomial root is asserted. Historical priority has not been independently audited; the inaccessible 2023 thesis remains a bounded comparison risk.

## References

1. T. Ohwa, *Exact computation for meeting times and infection times of random walks on graphs*, Pacific Journal of Mathematics for Industry **7**, article 5 (2015), https://doi.org/10.1186/s40736-015-0016-2.
2. V. Kanade, F. Mallmann-Trenn and T. Sauerwald, *On coalescence time in graphs: When is coalescing as fast as meeting?*, arXiv:1611.02460, first posted 2016-11-08, https://arxiv.org/abs/1611.02460.
3. T. van Belle and A. Klimovsky, *Meeting Times of Markov Chains via Singular Value Decomposition*, arXiv:2406.04958, first posted 2024-06-07, https://arxiv.org/abs/2406.04958.
4. *Mobile agents on simple networks: social distancing, gathering, dispersion and search games* (2023 doctoral thesis), Warwick Research Archive, https://wrap.warwick.ac.uk/id/eprint/184058/ (full PDF not inspected).
