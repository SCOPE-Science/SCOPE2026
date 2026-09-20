# Sharp b-chromatic extremum at fixed order and cycle rank

**Same-model review: passed. Independent audit: not yet performed.**

## Definitions

Let \(G\) be a finite simple connected graph with order \(n\ge 2\), size \(m\), and cyclomatic number
\[
\mu(G)=m-n+1.
\]
A proper coloring is a **b-coloring** if every color class contains a vertex adjacent to at least one vertex in every other color class. The largest number of colors in a b-coloring is the **b-chromatic number** \(b(G)\).

For fixed feasible integers
\[
n\ge2,\qquad 0\le r\le \binom{n-1}{2},
\]
write
\[
B(n,r)=\max\{b(G): |V(G)|=n,\ G\text{ connected},\ \mu(G)=r\}.
\]

## Main theorem

For every feasible pair \((n,r)\),
\[
\boxed{B(n,r)=\min\left\{n,\ 1+\left\lfloor\sqrt{n+2r-1}\right\rfloor\right\}.}
\]
Equivalently, every connected \(n\)-vertex graph of cyclomatic number \(r\) satisfies
\[
\boxed{b(G)\le 1+\left\lfloor\sqrt{n+2r-1}\right\rfloor,}
\]
and this bound is sharp whenever it is below the trivial bound \(b(G)\le n\).

### Upper bound

Put \(q=b(G)\). A b-coloring with \(q\) colors has at least \(q\) b-vertices, one from each color class, and each such vertex has degree at least \(q-1\). Since \(G\) is connected and \(n\ge2\), every remaining vertex has degree at least \(1\). Hence
\[
2m\ge q(q-1)+(n-q)=q^2-2q+n.
\]
Using \(m=n-1+r\),
\[
(q-1)^2\le n+2r-1.
\]
Thus
\[
q\le 1+\left\lfloor\sqrt{n+2r-1}\right\rfloor,
\]
and of course \(q\le n\).

### Sharp construction

Set
\[
k=\min\left\{n,\ 1+\left\lfloor\sqrt{n+2r-1}\right\rfloor\right\},
\qquad
R_k=\frac{(k-1)(k-2)}2.
\]

**Case 1: \(r\le R_k\).** Choose any connected simple graph \(H\) on \(k\) vertices with exactly \(k-1+r\) edges. For each \(v\in V(H)\), attach
\[
k-1-d_H(v)
\]
new leaves to \(v\). The resulting graph has
\[
k+\sum_v(k-1-d_H(v))
=k^2-2k+2-2r
\]
vertices. The definition of \(k\) gives
\[
n\ge k^2-2k+2-2r,
\]
so attach any remaining vertices as additional leaves to one fixed core vertex.

Color the \(k\) vertices of \(H\) with distinct colors. At a core vertex \(v\), assign its first \(k-1-d_H(v)\) leaves bijectively the colors of the core vertices not adjacent to \(v\). Any additional leaves may receive any color different from the color of their neighbor. Every core vertex then sees all other \(k-1\) colors, so the coloring is a b-coloring with \(k\) colors.

**Case 2: \(r>R_k\).** Start with a copy of \(K_k\), attach each of the remaining \(n-k\) vertices as a leaf to one clique vertex, and then add \(r-R_k\) arbitrary missing edges. The starting graph has cyclomatic number \(R_k\), while an \(n\)-vertex simple graph has maximum cyclomatic number \(\binom{n-1}{2}\); hence there are enough missing edges because \(r\le\binom{n-1}{2}\). The final graph contains \(K_k\), so \(\chi(G)\ge k\). Since every chromatic coloring is a b-coloring, \(b(G)\ge\chi(G)\ge k\).

Together with the upper bound, these constructions prove the theorem.

## Minimum-order threshold for a prescribed b-chromatic number

For \(k\ge2\) and \(r\ge0\), let \(N_k(r)\) be the minimum order of a connected simple graph \(G\) with \(\mu(G)=r\) and \(b(G)\ge k\). Then
\[
\boxed{
N_k(r)=\max\left\{
 k,
 k^2-2k+2-2r,
 \left\lceil\frac{3+\sqrt{1+8r}}2\right\rceil
\right\}.}
\]
Writing \(R_k=(k-1)(k-2)/2\), this becomes
\[
\boxed{
N_k(r)=
\begin{cases}
 k^2-2k+2-2r,&0\le r\le R_k,\\[1mm]
 \left\lceil\dfrac{3+\sqrt{1+8r}}2\right\rceil,&r>R_k.
\end{cases}}
\]
The third term is exactly the simple-graph feasibility condition \(r\le\binom{n-1}{2}\), and the formula follows by inverting the main theorem.

### Equality structure in the sparse threshold regime

If \(0\le r\le R_k\), every graph of order \(N_k(r)\) with cyclomatic number \(r\) and b-chromatic number at least \(k\) is obtained as follows: take a connected \(k\)-vertex graph \(H\) of cyclomatic number \(r\), and attach exactly \(k-1-d_H(v)\) leaves to each \(v\in V(H)\).

Indeed, equality in the degree-sum bound forces exactly \(k\) vertices to have degree \(k-1\) and every other vertex to have degree \(1\). The degree-one vertices cannot lie internally on paths joining the high-degree vertices, so those \(k\) vertices induce a connected core \(H\); deleting leaves preserves the cyclomatic number. Conversely, every such leaf completion has the b-coloring described above. At \(r=R_k\), this reduces to \(K_k\).

## Consequences

For trees,
\[
\max_{|V(T)|=n} b(T)=1+\left\lfloor\sqrt{n-1}\right\rfloor.
\]
For connected unicyclic graphs,
\[
\max_{|V(G)|=n,\ \mu(G)=1} b(G)=1+\left\lfloor\sqrt{n+1}\right\rfloor.
\]
These are specializations of the fixed-\((n,r)\) theorem and are not asserted here as separately new results.

## Relation to prior work

Irving and Manlove introduced the b-chromatic number and proved the fundamental degree-sequence bound \(b(G)\le m(G)\): a b-coloring with \(k\) colors requires at least \(k\) vertices of degree at least \(k-1\). Kouider and Mahéo later gave, among other bounds, the size-only inequality
\[
b(G)\le \frac12+\sqrt{2m+\frac14},
\]
which follows from \(2m\ge b(G)(b(G)-1)\). The 2018 survey of Jakovac and Peterin records these bounds and the main subsequent directions.

The present connected-graph estimate uses the positive degree forced on every non-b-vertex and is therefore a simultaneous order-size refinement:
\[
b(G)\le 1+\left\lfloor\sqrt{2m-n+1}\right\rfloor.
\]
More importantly, the construction above proves exact sharpness for every feasible pair \((n,m)\) with \(m\ge n-1\), or equivalently every feasible \((n,r)\), and yields the minimum-order threshold and its sparse equality structure.

A 2026 preprint of Zaker gives improved b-chromatic bounds in terms of independence and chromatic numbers; its abstract does not state an order-cycle-rank extremum. Searches under b-chromatic/b-coloring, cyclomatic number/cycle rank/excess, and joint order-size formulations did not locate the exact theorem above. Originality is therefore claimed only to the best of our knowledge.

## Verification

`artifacts/verify.py` computes the b-chromatic number exactly for every connected graph in the NetworkX Graph Atlas through order 7. It checks all 996 such graphs and all 42 feasible \((n,r)\) parameter pairs, confirming that their observed maxima equal the theorem. It also constructs a theorem witness for every feasible pair through order 30 (4089 pairs), checking connectivity, cycle rank, and the relevant b-coloring or clique certificate.

Expected output is in `artifacts/expected_output.txt`. The computation used NetworkX 3.6.1. These finite checks support but do not replace the proof.

## Limitations

- The equality classification above is only for minimum-order realizations in the sparse regime \(r\le R_k\); minimum-order extremal graphs in the dense regime are not classified.
- The full text of Kouider--Mahéo (2002) was not inspected. Its size and order bounds were checked through the 2018 survey; an unadvertised equivalent connected refinement in that paper remains a residual originality risk.
- The 2026 Zaker preprint was checked at abstract level only. Its stated scope concerns independence- and chromatic-number bounds rather than cyclomatic extremality.
- Originality is to the best of our knowledge; differently indexed papers, theses, or proceedings using terms such as excess, circuit rank, or m-degree may contain an equivalent statement.

## References

1. R. W. Irving and D. F. Manlove, *The b-chromatic number of a graph*, Discrete Applied Mathematics 91 (1999), 127--141. DOI: 10.1016/S0166-218X(98)00146-2.
2. M. Kouider and M. Mahéo, *Some bounds for the b-chromatic number of a graph*, Discrete Mathematics 256 (2002), 267--277. DOI: 10.1016/S0012-365X(01)00469-1.
3. M. Jakovac and I. Peterin, *The b-chromatic number and related topics---A survey*, Discrete Applied Mathematics 235 (2018), 184--201. DOI: 10.1016/j.dam.2017.08.008.
4. M. Zaker, *Improved bounds on the b-chromatic number using the independence and chromatic numbers*, arXiv:2606.07461 (2026).
