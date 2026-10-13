# Finite-resolution orbit growth of the ultrametric random graph is a partition-lattice zeta polynomial

## Finding

Let \(\mathcal R=(\omega^\omega,d,E)\) be the universal homogeneous closed graph on Baire space constructed by Kubiś, Pech, and Pech. Its nonzero metric values are \(2^{-j}\), \(j\ge0\). For integers \(n\ge1\) and \(h\ge0\), define \(O_{n,h}\) to be the number of metric-automorphism orbits on injective ordered tuples
\[
(x_1,\ldots,x_n)
\]
with
\[
d(x_i,x_j)\ge 2^{-h}\qquad(i\ne j).
\]

Let \(H_h(n)\) be the number of chains of set partitions
\[
\pi_0\preceq\pi_1\preceq\cdots\preceq\pi_{h+1}
\]
where \(\preceq\) means refinement,
\[
\pi_0=\{[n]\},\qquad
\pi_{h+1}=\{\{1\},\ldots,\{n\}\}.
\]
Then
\[
\boxed{O_{n,h}=2^{\binom n2}H_h(n)}.
\]

The hierarchy count satisfies
\[
H_0(n)=1,
\qquad
H_{h+1}(n)=\sum_{\pi\in\Pi_n}\prod_{B\in\pi}H_h(|B|),
\]
so it is the usual higher-order Bell-number iteration, with the order parameter interpreted here as metric resolution depth.

More strongly, for each fixed \(n\), \(H_h(n)\) is a polynomial in \(h\) of degree \(n-1\). Its leading coefficient is
\[
\boxed{[h^{n-1}]H_h(n)=\frac{n!}{2^{n-1}}}.
\]
Consequently
\[
\boxed{O_{n,h}
=n!\,2^{(n-1)(n-2)/2}h^{n-1}+O(h^{n-2})}.
\]

Thus the full action, which has infinitely many distance scales and is not oligomorphic, admits an exact finite-resolution orbit profile whose growth in the number of visible scales is polynomial of degree \(n-1\).

## Assumptions and scope

A metric automorphism preserves both the graph relation and the ultrametric. Only injective ordered tuples are counted. The cutoff \(d(x_i,x_j)\ge2^{-h}\) exposes exactly the distance values
\[
1,2^{-1},\ldots,2^{-h}.
\]
The graph convention in the source adds loops at every vertex; on an injective tuple the only free graph data are the \(\binom n2\) off-diagonal unordered pairs.

The principal source proves existence, universality, and strict metric homogeneity of the ultrametric graph. It does not enumerate finite-resolution tuple orbits. Higher-order Bell numbers and nested partitions are classical combinatorics; the contribution here is the exact orbit/zeta-polynomial identification for this single Polish metric structure and the resulting fixed-arity resolution asymptotic.

## Proof

For a tuple \(\bar x=(x_1,\ldots,x_n)\) satisfying the cutoff, define \(\pi_j\) for \(0\le j\le h+1\) by declaring two indices equivalent when the corresponding Baire-space branches agree through the first \(j\) coordinates. At level \(0\) every index is equivalent, while injectivity together with the cutoff makes level \(h+1\) discrete. Agreement can only split as the level increases, so
\[
\pi_0\preceq\pi_1\preceq\cdots\preceq\pi_{h+1}.
\]
Conversely, any such refinement chain determines a labeled ultrametric on \([n]\): for distinct \(i,j\), let \(s\) be the first level at which they lie in different blocks and put
\[
d(i,j)=2^{-(s-1)}.
\]
The chain condition is exactly what makes this an ultrametric, and every distance belongs to \(\{1,\ldots,2^{-h}\}\). Hence there are exactly \(H_h(n)\) labeled metric patterns at resolution \(h\).

Kubiś--Pech--Pech prove strict homogeneity: every metric isomorphism between the relevant small substructures extends to a global metric automorphism. In the graph example, their extension property realizes arbitrary finite graph extensions while preserving the ultrametric. Therefore two injective ordered tuples lie in the same metric-automorphism orbit exactly when their labeled finite metric graphs agree.

For each fixed metric hierarchy, the graph relation on the \(\binom n2\) unordered pairs is unrestricted. There are therefore
\[
2^{\binom n2}
\]
graph patterns, independent of the metric chain. Multiplying gives
\[
O_{n,h}=2^{\binom n2}H_h(n).
\]

The recurrence follows by conditioning on the first nontrivial partition. If \(\pi\) is the partition after exposing one additional level, then each block \(B\) carries an independent residual hierarchy of depth \(h\). Thus
\[
H_{h+1}(n)=\sum_{\pi\in\Pi_n}\prod_{B\in\pi}H_h(|B|).
\]
Equivalently, if
\[
F_h(z)=\sum_{n\ge0}H_h(n)\frac{z^n}{n!},
\]
then
\[
F_0(z)=e^z,
\qquad
F_{h+1}(z)=\exp(F_h(z)-1).
\]

For the polynomial statement, let \(c_{n,k}\) be the number of strict chains from the one-block partition to the discrete partition having exactly \(k\) strict refinement steps. Every weak chain of resolution \(h\) is obtained uniquely by choosing the \(k\) transition positions among the \(h+1\) available positions. Hence
\[
H_h(n)=\sum_{k=0}^{n-1}c_{n,k}\binom{h+1}k.
\]
This is a polynomial in \(h\) of degree at most \(n-1\). Maximal chains have exactly \(n-1\) strict steps. Reversing such a chain, when there are \(k\) current blocks there are \(\binom k2\) choices of blocks to merge, so
\[
c_{n,n-1}=\prod_{k=2}^n\binom k2
=\frac{n!(n-1)!}{2^{n-1}}.
\]
Since \(\binom{h+1}{n-1}\) has leading coefficient \(1/(n-1)!\),
\[
[h^{n-1}]H_h(n)
=\frac{c_{n,n-1}}{(n-1)!}
=\frac{n!}{2^{n-1}}.
\]
Multiplication by \(2^{\binom n2}\) yields the stated orbit asymptotic.

## Verification

A standalone exact replay independently generates set partitions, directly enumerates refinement multichains for \(n\le5\) and \(h\le3\), checks the higher-order-Bell recurrence, derives the strict-chain binomial-basis expansion, verifies the maximal-chain coefficient through \(n=7\), interpolates the leading coefficient through \(n=8\), and checks the graph factor and the binary special case. It reports

`VERIFY_OK 180 exact assertions`

and reproduces
\[
\begin{array}{c|rrrrrrr}
h & H_h(1)&H_h(2)&H_h(3)&H_h(4)&H_h(5)&H_h(6)&H_h(7)\\
0&1&1&1&1&1&1&1\\
1&1&2&5&15&52&203&877\\
2&1&3&12&60&358&2471&19302\\
3&1&4&22&154&1304&12915&146115
\end{array}
\]
The computation is a finite replay only; the theorem for all \(n,h\) is proved symbolically above.

## Relationship to prior work

Kubiś, Pech, and Pech construct the universal homogeneous ultrametric graph as an inverse limit built from a universal homogeneous endomorphism of the Rado graph. They describe it as a fractal-like graph on Baire space and prove strict metric homogeneity and universality. Their paper's graph example does not state finite tuple-orbit counts or a resolution-growth law.

Skau and Kristensen give a set-theoretic interpretation of higher-order Bell numbers by iterated/nested partitions. That supplies established terminology for the recurrence above, but their work does not concern ultrametric automorphism groups or finite-resolution orbit profiles.

There are two especially close neighboring observations. First, a fixed finite tower of nested equivalence relations naturally has higher-order-Bell orbit counts. Second, at arity two this ultrametric random graph has two graph choices on every positive metric sphere. The present statement links all arities and all finite metric resolutions inside one fixed Polish structure and adds the partition-lattice multichain polynomial and its exact leading coefficient. Targeted semantic, exact-phrase, and broader ultrametric/orbit searches found these ingredients but no equivalent finite-resolution theorem.

## Limitations

The theorem uses the canonical dyadic distance set from the inverse-limit presentation. It counts labeled ordered-tuple orbits, not orbits of unordered finite subsets. It also exploits the complete freedom of the graph relation; adding metric-dependent forbidden graph configurations would destroy the simple factor \(2^{\binom n2}\).

The polynomiality of finite-poset multichain counts and the maximal-chain formula for the partition lattice are classical combinatorial facts. The originality claim is therefore about their exact realization as the resolution profile of this ultrametric random graph, not about those combinatorial facts in isolation. A residual risk is that this bridge is known informally but uncatalogued.

## References

1. Wiesław Kubiś, Christian Pech, and Maja Pech, *Homogeneous ultrametric structures*, arXiv:2301.10953, first submitted 26 January 2023. Primary MSC 03C30.
2. Ivar Henning Skau and Kai Forsberg Kristensen, *Sets of iterated Partitions and the Bell iterated Exponential Integers*, arXiv:1903.08379, first submitted 20 March 2019.
3. Eric Temple Bell, *The iterated exponential integers*, *Annals of Mathematics* 39 (1938), 539--557.
