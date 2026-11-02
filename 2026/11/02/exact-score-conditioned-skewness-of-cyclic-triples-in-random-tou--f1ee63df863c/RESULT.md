# Exact score-conditioned skewness of cyclic triples in random tournaments

## Finding
Let \(T\) be the uniformly oriented complete graph on \(n\ge4\) labeled vertices, let \(v\) be one fixed vertex, let \(D\) be its outdegree, and let \(C\) be the number of **unordered three-vertex sets** whose induced orientation is a directed cycle. Put \(m=n-1\), \(N=\binom m3\), and \(q=d(m-d)\). Conditional on \(D=d\), for every integer \(0\le d\le m\), the first three cumulants of \(C\) are exactly

\[
\begin{aligned}
\mathbb E[C\mid D=d]&=\frac N4+\frac q2,\\
\operatorname{Var}(C\mid D=d)&=\frac{3N}{16}+\frac q4,\\
\mathbb E[(C-\mathbb E[C\mid D=d])^3\mid D=d]
 &=\frac{3(4-m)N}{32}-\frac{3(m-2)q}{16}.
\end{aligned}
\]

For \(n\ge6\), **every** conditional third centered moment is strictly negative. For \(n=5\), it vanishes at the extreme degrees \(d=0,4\) and is strictly negative at \(d=1,2,3\). For \(n=4\), it is positive at \(d=0,3\) and negative at \(d=1,2\). For every \(n\ge5\), the magnitude of the *standardized* conditional skewness increases strictly as \(q=d(m-d)\) increases, hence is largest for the most balanced possible marked-vertex score(s). The comparisons across degree classes refer to standardized third moments, not to a stochastic ordering of the entire count distribution.

## Assumptions and scope
Each of the \(\binom n2\) edge orientations is an independent fair coin. The marked vertex is predetermined, not chosen by its score. A cyclic triple is counted once, with neither its three rotations nor its direction as separate objects. Since the model is invariant under relabeling, conditioning on \(D=d\) is equivalent, for the distribution of \(C\), to fixing an outneighborhood \(A\) of size \(d\) and its complementary inneighborhood \(B\) of size \(m-d\). Edges in the other \(m\) vertices remain independent fair orientations. Variance is positive for every \(n\ge4\), including the extreme degrees.

## Proof
Write \(U=V(T)\setminus\{v\}\), \(A=\{u:v\to u\}\), and \(B=\{w:w\to v\}\). For distinct \(x,y\in U\), define \(\epsilon_{xy}=1\) if \(x\to y\), and \(-1\) otherwise, so \(\epsilon_{yx}=-\epsilon_{xy}\). The independent edge variables are symmetric Rademacher signs.

For each unordered triple \(\{x,y,z\}\subset U\), its directed-cycle indicator is

\[
\frac14\bigl(1-\epsilon_{xy}\epsilon_{xz}-\epsilon_{yx}\epsilon_{yz}-\epsilon_{zx}\epsilon_{zy}\bigr).
\]

Therefore the centered count of cyclic triples entirely inside \(U\) is

\[
Q=-\frac14\sum_{x\in U}\ \sum_{\{y,z\}\subset U\setminus\{x\}}
 \epsilon_{xy}\epsilon_{xz}.
\]

Exactly the \(q=|A||B|\) unordered pairs crossing from \(A\) to \(B\) can form cyclic triples with \(v\). Their centered contribution is

\[
L=\frac12\sum_{a\in A,b\in B}\epsilon_{ab}.
\]

Thus \(C=N/4+q/2+Q+L\). Every monomial in \(Q\) consists of a distinct two-edge wedge in the complete graph on \(U\). Orthogonality of distinct Rademacher monomials gives

\[
\mathbb E Q=\mathbb E L=\mathbb E[QL]=0,\qquad
\mathbb E Q^2=\frac{3N}{16},\quad \mathbb E L^2=\frac q4.
\]

For the third moment, \(\mathbb E[Q^2L]=\mathbb E[L^3]=0\) by parity. A nonzero product of three distinct wedge monomials in \(Q^3\) corresponds to three edges that either share one common vertex (a three-star) or form a triangle. Their signed coefficient products are respectively \(-1/64\) and \(+1/64\). There are \(m\binom{m-1}{3}\) stars and \(\binom m3\) triangles, and every triple is ordered in six ways. Hence

\[
\mathbb E Q^3=\frac6{64}\left(\binom m3-m\binom{m-1}{3}\right)
=\frac{3(4-m)N}{32}.
\]

Only two cross edges sharing a common endpoint can contribute to \(\mathbb E[QL^2]\). Each unordered pair contributes \(-1/8\), including the factor two from the square. The number of such pairs is

\[
|A|\binom{|B|}{2}+|B|\binom{|A|}{2}=\frac{q(m-2)}2.
\]

Consequently \(\mathbb E[QL^2]=-q(m-2)/16\) and \(\mathbb E[(Q+L)^3]=\mathbb E Q^3+3\mathbb E[QL^2]\), proving all three formulas. Their signs follow directly from \(m\ge3\), \(N\ge1\), and \(q\ge0\).

For the standardized assertion assume \(m\ge4\), put \(a=3(m-4)N/32\), \(b=3(m-2)/16\), and \(v_0=3N/16\). The absolute conditional skewness equals

\[
s(q)=\frac{a+bq}{(v_0+q/4)^{3/2}},
\qquad 0\le q\le\frac{m^2}{4}.
\]

Its derivative has the sign of

\[
b(v_0+q/4)-\frac38(a+bq)
=\frac b8\left(\frac{m(m-1)}2-q\right)>0,
\]

because \(m(m-1)/2>m^2/4\) for \(m>2\). Thus \(s\) increases strictly with the degree-balance statistic \(q\). This does not assert strict change between scores \(d\) and \(m-d\), which give the same \(q\) and hence the same conditional law by reversal symmetry.

## Verification
The accompanying standalone `verify.py` enumerates every remaining-edge orientation after fixing the marked vertex's outneighborhood and counts cycles directly from each triple's three edge directions. For all \(3\le n\le7\) and every admissible \(d\), its exact rational mean, variance, and third centered moment agree with the formulas. It also checks the sign classifications and the derivative algebra on a wide finite parameter range. The proof above, not the finite computation, establishes the identities for all \(n\).

To reproduce: run `python3 verify.py` with a standard Python 3 interpreter in the same directory. No network or external package is required.

## Relationship to prior work
The classical score-sequence identity for the number of cyclic triples in a *deterministic* tournament is established background. Komarov and Mackey (arXiv:1410.6828, first submitted 2014-10-24) treat exact cycle-count identities and extremal bounds, mainly for directed five-cycles, and recount the older cyclic-triple extremal theory. Coregliano and Razborov (arXiv:1501.04074, first submitted 2015-01-16) investigate transitive-subtournament densities and quasirandomness. Andersson (1998) studies asymptotic distributions of tournament subgraph counts. The present finite score-conditioned third cumulant and standardized skewness ordering are different questions; a third-moment formula is not obtained from an unconditional variance or fourth-cumulant formula alone. Earlier implicit derivations in general random-tournament moment machinery remain possible.

## Limitations
The conclusions require independent fair orientations. They do not extend without proof to correlated or biased match outcomes, to a randomly selected maximum-score vertex, or to arbitrary subgraph counts. The score-conditioned laws are not claimed to be likelihood-ratio ordered or stochastically ordered. Only cumulants through order three are evaluated here; no central limit theorem or numerical error bound is asserted. Historical priority, especially possible implicit coverage in earlier general subgraph-count methods, has not been fully excluded.

## References
- N. Komarov and J. Mackey, *On the number of 5-cycles in a tournament*, arXiv:1410.6828 (first public version 2014-10-24), https://arxiv.org/abs/1410.6828 .
- L. N. Coregliano and A. A. Razborov, *On the Density of Transitive Tournaments*, arXiv:1501.04074 (first public version 2015-01-16), https://arxiv.org/abs/1501.04074 .
- P. Andersson, *On the asymptotic distributions of subgraph counts in a random tournament*, Random Structures & Algorithms 13 (1998), 249–260, https://doi.org/10.1002/(SICI)1098-2418(199810/12)13:3/4%3C249::AID-RSA4%3E3.0.CO;2-V .
