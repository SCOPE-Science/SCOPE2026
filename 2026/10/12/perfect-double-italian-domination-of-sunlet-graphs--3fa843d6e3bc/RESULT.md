# Perfect double Italian domination of sunlet graphs
## Finding
For every integer \(n\ge3\), let
\[
S_n=C_n\circ K_1
\]
be the sunlet graph obtained by attaching one pendant leaf to each cycle vertex of \(C_n\). Then
\[
\gamma_{dI}^{p}(S_n)=2n+\left\lceil\frac n3\right\rceil.
\]

Thus the perfect double Italian domination number of this canonical one-leaf corona is exactly a baseline cost of two per cycle-leaf pair plus one additional unit for every three cycle positions, rounded upward.

## Assumptions and scope
Write the cycle vertices as
\[
x_1,x_2,\ldots,x_n
\]
with indices modulo \(n\), and let \(y_i\) be the leaf adjacent only to \(x_i\).

A perfect double Italian dominating function is a map
\[
f:V(G)\to\{0,1,2,3\}
\]
such that whenever \(f(v)\in\{0,1\}\),
\[
3\le \sum_{u\in N[v]}f(u)\le4.
\]
Its weight is
\[
\omega(f)=\sum_{v\in V(G)}f(v),
\]
and \(\gamma_{dI}^{p}(G)\) is the minimum possible weight.

This is the perfect double Italian definition introduced in 2023. A later paper uses the name “perfect Roman \(\{3\}\)-domination” for a different exact open-neighborhood condition; that later invariant is not used here.

## Proof
Fix a perfect double Italian dominating function \(f\). For each \(i\), consider the pendant pair
\[
\{x_i,y_i\}.
\]
If \(f(x_i)=0\), then the leaf \(y_i\) cannot have label \(0\) or \(1\), because its closed-neighborhood weight would be at most \(1\). Hence \(f(y_i)\ge2\). If \(f(x_i)=1\), again \(f(y_i)\ge2\). If \(f(x_i)=2\), the pair has weight at least \(3\), since \(y_i=0\) would give the leaf closed-neighborhood weight \(2\). If \(f(x_i)=3\), the pair has weight at least \(3\). Therefore
\[
f(x_i)+f(y_i)\ge2
\]
for every \(i\), and equality occurs only at
\[
(f(x_i),f(y_i))=(0,2).
\tag{1}
\]

Call index \(i\) exceptional when its pair is not the state in (1), and let \(E\) be the set of exceptional indices. Every exceptional pair contributes at least one unit beyond the baseline \(2\), so
\[
\omega(f)\ge2n+|E|.
\tag{2}
\]

No three consecutive indices can all be nonexceptional. Indeed, if \(i-1,i,i+1\notin E\), then
\[
f(x_{i-1})=f(x_i)=f(x_{i+1})=0,
\qquad
f(y_i)=2.
\]
The cycle vertex \(x_i\) is labeled \(0\), but its closed-neighborhood weight is then only
\[
0+0+0+2=2,
\]
contrary to the required interval \([3,4]\).

The \(n\) cyclic blocks of three consecutive indices must therefore all meet \(E\). Each exceptional index belongs to exactly three such blocks, hence
\[
n\le3|E|.
\]
Thus
\[
|E|\ge\left\lceil\frac n3\right\rceil.
\]
Together with (2),
\[
\omega(f)\ge2n+\left\lceil\frac n3\right\rceil.
\tag{3}
\]

It remains to attain the bound. Label every leaf \(y_i\) by \(2\). On the cycle use only labels \(0\) and \(1\), with exactly \(\lceil n/3\rceil\) ones and no cyclic run of three zeros. Explicitly, writing \(n=3q+r\):

- if \(r=0\), repeat the block \((1,0,0)\) exactly \(q\) times;
- if \(r=1\), use \((1,0,0)^q(1)\);
- if \(r=2\), use \((1,0,0)^q(1,0)\).

These cyclic words have no run of three zeros and no run of three ones. If \(f(x_i)=0\), then at least one of its two cycle neighbors has label \(1\), so
\[
3\le f(N[x_i])=2+f(x_{i-1})+f(x_{i+1})\le4.
\]
If \(f(x_i)=1\), at most one cycle neighbor has label \(1\), so
\[
3\le f(N[x_i])=3+f(x_{i-1})+f(x_{i+1})\le4.
\]
The leaves all have label \(2\), so no condition is imposed on them. Hence this is a valid perfect double Italian dominating function of weight
\[
2n+\left\lceil\frac n3\right\rceil.
\]
Combined with (3), this proves the formula.

## Verification
The included checker tests the defining closed-neighborhood condition directly.

It exhausts all
\[
4^6+4^8+4^{10}=1{,}118{,}208
\]
labelings for \(S_3,S_4,S_5\), obtaining minimum weights \(7,10,12\), exactly as the formula predicts.

An independent cycle-state search minimizes over all cycle labels for every \(3\le n\le10\), choosing the pendant label locally from the original definition, and again obtains
\[
2n+\left\lceil\frac n3\right\rceil.
\]
The explicit construction is also checked directly for every \(3\le n\le50\).

## Relationship to prior work
Hao, Jalilolghadr, and Mojdeh introduced perfect double Italian domination in 2023. Their paper defines precisely the closed-neighborhood interval used above, establishes NP-completeness even on bipartite graphs, determines the parameter on several standard graphs, compares it with perfect double Roman domination, and characterizes several extreme values. The full accessible article contains no occurrence of “sunlet” or “corona”, and targeted searches did not locate a sunlet specialization.

The sunlet family is the corona \(C_n\circ K_1\), a canonical unicyclic graph family. The formula here does not follow from the initiating paper’s extremal-value characterizations: its value grows as
\[
2n+\left\lceil\frac n3\right\rceil
\]
on a graph of order \(2n\), and the proof depends on a local three-position obstruction specific to the pendant-cycle geometry.

A 2024 paper uses the name “perfect Roman \(\{3\}\)-domination” for a different invariant requiring exact open-neighborhood sums \(3\) and \(2\) at labels \(0\) and \(1\), respectively. That terminology overlap does not cover the present claim.

## Limitations
The theorem concerns the uniform one-leaf corona of a cycle. It does not determine perfect double Italian domination for arbitrary coronas \(G\circ K_1\), for cycles with nonuniform pendant multiplicities, or for the distinct later invariant also called perfect Roman \(\{3\}\)-domination.

The computation is corroborative only. The arbitrary-order result follows from the pair-weight lower bound and the cyclic three-block covering argument.

Search coverage cannot exclude a differently phrased or non-indexed treatment of the same sunlet family.

## References
1. G. Hao, P. Jalilolghadr, D. A. Mojdeh, “Perfect double Italian domination of a graph,” AKCE International Journal of Graphs and Combinatorics 20(3) (2023), 247–257, DOI 10.1080/09728600.2023.2218457; published online 21 June 2023.
2. A. Almulhim, “Perfect Roman \(\{3\}\)-Domination in Graphs: Complexity and Bound of Perfect Roman \(\{3\}\)-Domination Number of Trees,” Journal of Mathematics (2024), DOI 10.1155/jom/1900923; first published 24 December 2024. This source uses a different definition and is cited only to disambiguate terminology.
