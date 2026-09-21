# Sharp certified-domination gap for connected graphs

## Result

Let \(G\) be a finite simple connected graph of order \(n\ge 2\). Write
\(\gamma(G)\) for the domination number and \(\gamma_{\rm cer}(G)\) for the
certified domination number, and define
\[
\Delta_{\rm cer}(G)=\gamma_{\rm cer}(G)-\gamma(G).
\]

Then
\[
\max_{|V(G)|=n,\;G\ {\rm connected}}\Delta_{\rm cer}(G)=
\begin{cases}
n/2,& n\ \text{even},\\[2mm]
(n-3)/2,& n\ \text{odd}.
\end{cases}
\]

The equality cases are exact:

1. If \(n\) is even, equality holds if and only if \(G\) is a corona
   \(H\circ K_1\) of a connected graph \(H\).
2. If \(n\ge5\) is odd, equality holds if and only if \(G\) is a diadem
   of a connected graph: start with \(H\circ K_1\), add one new vertex,
   and join it to one support vertex of the corona.
3. For \(n=3\), the maximum is \(0\), attained by both connected graphs
   \(P_3\) and \(K_3\).

A useful equality theorem underlying the odd-order characterization is:

> **Factor-two equality theorem.** For every connected graph \(G\) of
> order at least \(2\),
> \[
> \gamma_{\rm cer}(G)=2\gamma(G)
> \quad\Longleftrightarrow\quad
> G=H\circ K_1
> \]
> for some connected graph \(H\).

Thus the usual factor-two upper bound for certified domination has no
other connected equality cases.

## Definitions

A dominating set \(D\subseteq V(G)\) is **certified** when every vertex
of \(D\) has either zero or at least two neighbors in \(V(G)\setminus D\).
A support vertex is **weak** if it has exactly one leaf neighbor. A vertex
of a dominating set is **half-shadowed** when it has exactly one neighbor
outside the dominating set.

A **corona** \(H\circ K_1\) is obtained by attaching one new leaf to each
vertex of \(H\). A **diadem** is obtained from a corona by adding one more
leaf adjacent to one support vertex.

## Proof of the factor-two equality theorem

The case \(K_2\) is immediate, since \(K_2=K_1\circ K_1\),
\(\gamma(K_2)=1\), and \(\gamma_{\rm cer}(K_2)=2\).

Assume now that \(G\) is connected and has at least three vertices.
The proof of the standard bound
\[
\gamma_{\rm cer}(G)\le \gamma(G)+|S_1(G)|\le 2\gamma(G)
\]
can be sharpened as follows. Choose a minimum dominating set \(D\) that
contains no leaf and, among such sets, minimizes the number of
half-shadowed vertices. Let \(D_{\rm hs}\) be its half-shadowed vertices.
The standard exchange argument shows
\[
D_{\rm hs}\subseteq S_1(G),
\]
where \(S_1(G)\) is the set of weak supports. Adding to \(D\) the unique
leaf adjacent to every vertex of \(D_{\rm hs}\) gives a certified
dominating set. Hence
\[
\gamma_{\rm cer}(G)
 \le \gamma(G)+|D_{\rm hs}|
 \le \gamma(G)+|S_1(G)|
 \le 2\gamma(G).
\]
(The last inequality follows because every dominating set must meet each
of the pairwise disjoint weak-support/leaf pairs.)

Suppose \(\gamma_{\rm cer}(G)=2\gamma(G)\). Every inequality in the
display is then an equality, so
\[
|D_{\rm hs}|=|D|=\gamma(G).
\]
Thus \(D_{\rm hs}=D\). Every \(s\in D\) is therefore a weak support and
is half-shadowed with respect to \(D\). Since \(D\) contains no leaves,
the unique neighbor of \(s\) outside \(D\) is precisely its unique leaf.
Consequently every other neighbor of \(s\) lies in \(D\).

Because \(D\) dominates \(G\), every vertex outside \(D\) is adjacent to
some vertex of \(D\). The preceding paragraph forces every such vertex
to be the unique leaf of that support. Therefore \(V(G)\setminus D\)
consists of exactly one private leaf for every vertex of \(D\), and
\(G=G[D]\circ K_1\). Connectivity of \(G\) implies connectivity of
\(G[D]\).

Conversely, if \(G=H\circ K_1\) with \(H\) connected, every dominating
set must meet each support/leaf pair, so \(\gamma(G)=|V(H)|\). The known
corona characterization gives
\(\gamma_{\rm cer}(G)=|V(G)|=2|V(H)|=2\gamma(G)\).
This proves the factor-two equality theorem.

## Proof of the sharp order bound

For every connected graph of order \(n\ge2\), the classical domination
bound gives
\[
\gamma(G)\le \frac n2,
\]
and certified domination satisfies
\[
\gamma_{\rm cer}(G)\le 2\gamma(G).
\]
Therefore
\[
\Delta_{\rm cer}(G)\le \gamma(G)\le \left\lfloor\frac n2\right\rfloor.
\]

### Even order

Let \(n=2m\). Then \(\Delta_{\rm cer}(G)\le m\).
If equality holds, necessarily
\[
\gamma(G)=m,\qquad \gamma_{\rm cer}(G)=2m=n.
\]
For connected graphs, the known characterization of
\(\gamma_{\rm cer}(G)=n\) says exactly that \(G\) is a corona.
Conversely every connected corona of order \(2m\) has
\(\gamma=m\) and \(\gamma_{\rm cer}=2m\). Thus the maximum is \(m=n/2\),
with precisely the connected coronas as extremal graphs.

### Odd order

Let \(n=2m+1\). For connected graphs,
\(\gamma(G)\le m\). If
\(\Delta_{\rm cer}(G)=m\), then the inequalities
\(\Delta_{\rm cer}(G)\le\gamma(G)\le m\) force
\[
\gamma(G)=m,\qquad \gamma_{\rm cer}(G)=2m=n-1,
\]
but a certified domination number can never equal \(n-1\).
Hence
\[
\Delta_{\rm cer}(G)\le m-1=(n-3)/2.
\]

For \(m\ge2\), a diadem built from a connected graph \(H\) on \(m\)
vertices has order \(2m+1\). Its \(m\) original support vertices dominate
the graph, while the \(m\) original pendant leaves force every dominating
set to contain at least one vertex from each support/leaf pair. Hence
\(\gamma(G)=m\). The established diadem formula gives
\(\gamma_{\rm cer}(G)=n-2=2m-1\), and therefore
\(\Delta_{\rm cer}(G)=m-1\). The bound is sharp.

It remains to identify all odd extremal graphs. Suppose \(n=2m+1\ge5\)
and \(\Delta_{\rm cer}(G)=m-1\). Since
\[
m-1\le\gamma(G)\le m,
\]
there are two possibilities. If \(\gamma(G)=m-1\), then
\(\gamma_{\rm cer}(G)=2m-2=2\gamma(G)\), and the factor-two equality
theorem would make \(G\) a corona, which is impossible because coronas
have even order. Thus \(\gamma(G)=m\), and consequently
\[
\gamma_{\rm cer}(G)=2m-1=n-2.
\]
The known connected characterization of
\(\gamma_{\rm cer}(G)=n-2\) then says that \(G\) is a diadem.
The converse was proved above.

For \(n=3\), direct use of the definitions gives
\(\gamma_{\rm cer}=\gamma=1\) for both \(P_3\) and \(K_3\).

## Independent finite verification

The accompanying script exhaustively checks every connected graph in
NetworkX's Graph Atlas through order \(7\). It computes
\(\gamma\) and \(\gamma_{\rm cer}\) directly from their definitions,
checks the sharp bound, and checks that the extremal isomorphism classes
are exactly the corona/diadem families stated above (with the \(n=3\)
exception).

The output is recorded in `artifacts/expected_output.txt`.

## Literature context and originality

Dettlaff, Lemańska, Topp, Ziemann and Żyliński introduced certified
domination and proved the two ingredients
\[
\gamma_{\rm cer}(G)\le 2\gamma(G)
\]
and the characterizations of connected graphs with
\(\gamma_{\rm cer}=n\) and \(\gamma_{\rm cer}=n-2\). Their discussion
states that coronas establish sharpness of the factor-two bound, but the
inspected full text does not state the converse equality
characterization \(\gamma_{\rm cer}=2\gamma\Rightarrow\) corona, nor the
fixed-order maximum of \(\gamma_{\rm cer}-\gamma\).

The 2019 paper on equal domination and certified domination numbers was
also inspected in full. It develops the equality
\(\gamma_{\rm cer}=\gamma\), upper certified domination, and related
corona structure, but no factor-two equality theorem or fixed-order gap
extremum was located.

Later work includes a linear algorithm for minimum certified domination
in trees and a 2025 constructive characterization of trees satisfying
\(\gamma_{\rm cer}=\gamma\). These are closely related to the same
parameters but address different questions. The full text of the 2025
tree-equality paper was not available in the inspected sources, so a
differently phrased overlap there cannot be completely excluded.

Accordingly, originality is claimed only **to the best of our
knowledge**. Residual risk remains from unindexed literature or results
phrased purely in terms of corona/diadem structure without using the
language of a certified-domination gap.

## References

1. M. Dettlaff, M. Lemańska, J. Topp, R. Ziemann, P. Żyliński,
   “Certified domination,” *AKCE International Journal of Graphs and
   Combinatorics* 17 (2020), 86–97.
   DOI: https://doi.org/10.1016/j.akcej.2018.09.004
   Preprint: https://arxiv.org/abs/1606.03257
2. M. Dettlaff, M. Lemańska, M. Miotk, J. Topp, R. Ziemann,
   P. Żyliński, “Graphs with equal domination and certified domination
   numbers,” *Opuscula Mathematica* 39 (2019), 815–827.
   DOI: https://doi.org/10.7494/OpMath.2019.39.6.815
3. M. Lemańska et al., “Theoretical modelling of efficient fire safety
   water networks by certified domination,” *Scientific Reports* (2024).
   DOI: https://doi.org/10.1038/s41598-024-72285-3
4. A. Cabrera Martínez, “Trees with equal domination and certified
   domination numbers,” *Indian Journal of Pure and Applied Mathematics*
   (2025).
   DOI: https://doi.org/10.1007/s13226-025-00907-1

## Limitations

The theorem is for finite simple connected graphs. Originality is to the
best of our knowledge; unindexed or differently phrased equivalent
results remain possible. The 2025 tree-equality article was identified
from its bibliographic record and abstract, but its full theorem text
was not inspected.
