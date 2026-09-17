# Exact forced 3-colouring polynomials at maximum degree two

## Statement

Let \(FC_3(G;p)=FC(G;p,3)\) be the forced 3-colouring polynomial of Farr, and put
\[
r=1-3p.
\]

For the path \(P_n\), \(n\ge 1\),
\[
\boxed{
FC_3(P_n;p)=
\sum_{j=0}^{\lfloor (n-1)/2\rfloor}
3\,2^{\,n-j-1}
\binom{n-1-j}{j}
p^{\,n-j}r^j .
}
\tag{1}
\]
Equivalently, if \(A_n=FC_3(P_n;p)\), then
\[
A_1=3p,\qquad A_2=6p^2,\qquad
A_n=2pA_{n-1}+2prA_{n-2}\quad(n\ge3).
\tag{2}
\]

For the cycle \(C_n\), \(n\ge3\),
\[
\boxed{
FC_3(C_n;p)=
\sum_{j=0}^{\lfloor n/2\rfloor}
\frac{n}{n-j}\binom{n-j}{j}
\bigl(2^{\,n-j}+2(-1)^{\,n-j}\bigr)
p^{\,n-j}r^j .
}
\tag{3}
\]

Consequently, \(FC_3(G;p)\) has an explicit closed form for every graph
\(\Delta(G)\le2\): decompose \(G\) into path and cycle components and multiply
the corresponding factors, using multiplicativity over disjoint unions.

At the coefficient level, the number \(fcol(G,i;3)\) of forcing partial
3-assignments with domain size \(i\) is therefore explicit. In particular,
\[
fcol(P_n,n-j;3)=
3\,2^{\,n-j-1}\binom{n-1-j}{j},
\tag{4}
\]
and
\[
fcol(C_n,n-j;3)=
\frac{n}{n-j}\binom{n-j}{j}
\bigl(2^{\,n-j}+2(-1)^{\,n-j}\bigr).
\tag{5}
\]

These formulas give linear-time arithmetic evaluation on maximum-degree-two
graphs after their components are identified, in contrast with the general
fixed-\(\lambda\ge3\) evaluation problem, which Farr proves is #P-hard.

## Proof

A partial 3-assignment can force an uncoloured vertex only when that vertex has
two coloured neighbours carrying two distinct colours. Hence on a graph of
maximum degree two, any vertex that is not initially coloured and is eventually
forced must have degree exactly two.

### Paths

Let \(U\) be the set of initially uncoloured vertices of \(P_n\).

First, neither endpoint can lie in \(U\). Moreover, \(U\) cannot contain two
adjacent vertices. Indeed, in a nonempty run of at least two initially
uncoloured vertices, no vertex can be the first one forced: each endpoint of
the run has at most one coloured neighbour until another vertex of the same
run is coloured, and each internal vertex has none or one. Thus such a run
remains permanently uncoloured.

Conversely, suppose that \(U\) is an independent subset of the \(n-2\) internal
vertices. Every \(u\in U\) then has both neighbours initially coloured. The
partial assignment forces the whole path exactly when:

1. adjacent initially coloured vertices receive different colours; and
2. for every \(u\in U\), its two neighbours receive different colours.

Suppressing every vertex of \(U\) turns these constraints into the usual
proper-colouring constraints on a path with \(n-|U|\) vertices. Thus for a
fixed \(U\) of size \(j\), there are exactly
\[
3\cdot 2^{n-j-1}
\]
forcing partial assignments.

The number of independent \(j\)-subsets of the internal path on \(n-2\)
vertices is
\[
\binom{n-1-j}{j}.
\]
Each such assignment contributes \(p^{n-j}r^j\) to \(FC_3(P_n;p)\), proving
(1) and (4). Splitting the independent subsets according to whether the last
eligible internal vertex is selected gives the weighted Fibonacci recurrence
(2).

### Cycles

Now let \(U\) be the initially uncoloured set in \(C_n\). Exactly the same
"no first forced vertex" argument shows that \(U\) must be independent.
Conversely, if \(U\) is independent, every member of \(U\) has two initially
coloured neighbours and all of \(U\) is forced precisely when consecutive
surviving coloured vertices around the cycle receive different colours.

For \(|U|=j\), write \(m=n-j\). The cyclic sequence of the \(m\) surviving
vertices has
\[
Q_m=2^m+2(-1)^m
\]
valid 3-colourings. For \(m\ge3\) this is the standard chromatic polynomial
of a cycle evaluated at \(3\); when \(m=2\), which occurs only in the small
alternating cases, the same expression is \(6\), the required number of
different-colour assignments to the two surviving vertices.

The number of independent \(j\)-subsets of \(C_n\) is
\[
\frac{n}{n-j}\binom{n-j}{j}.
\]
Multiplying these two counts and the probability weight
\(p^{n-j}r^j\), then summing over \(j\), proves (3) and (5).

Finally, every graph of maximum degree at most two is a disjoint union of
paths and cycles, and \(FC_3\) is multiplicative over disjoint unions. This
proves the general maximum-degree-two statement.

## A correction to a displayed small example

Farr's arXiv:2609.17108v1, Proposition 6, equation (10), prints
\[
FC_3(K_{1,2};p)=6p^2(1-2p).
\]
Specialising (1) to \(P_3=K_{1,2}\) instead gives
\[
\boxed{FC_3(K_{1,2};p)=6p^2(1-p).}
\tag{6}
\]
This can also be checked directly: there are six forcing assignments with only
the two endpoints initially coloured (they must have distinct colours) and
twelve proper total 3-colourings, giving
\[
6p^2(1-3p)+12p^3=6p^2(1-p).
\]
The printed expression also fails the paper's Proposition 4(c) at \(p=1/3\):
it gives \(2/9\), whereas
\[
3^{-3}P(P_3;3)=12/27=4/9.
\]
Thus the \(\lambda=3\) line of equation (10) appears to be a typographical
error. Formula (1) agrees with the paper's displayed \(P_4\) value
\(24p^3(1-2p)\), and formula (3) agrees with its displayed \(C_4\) value
\(6p^2(2-8p+9p^2)\).

## Context and relation to prior work

Farr and Morgan introduced the forced-colouring function in their work on graph
polynomials. Farr's 2026 paper develops its fundamental properties, proves
multiplicativity, gives formulas for empty and complete graphs and all connected
graphs on at most four vertices, and proves a closed formula for \(FC_2\) on
bipartite graphs. It also proves that evaluating \(FC_\lambda(G;p)\) is #P-hard
for fixed \(\lambda\ge3\) and the stated range of \(p\).

For maximum-degree-two graphs, Farr's Proposition 5 already makes
\(\lambda\ge4\) immediate from the chromatic polynomial, and Theorem 7 handles
\(\lambda=2\) on the bipartite cases. The missing nontrivial case is therefore
\(\lambda=3\), which (1)--(5) settle exactly for every path, cycle, and hence
every graph of maximum degree at most two.

## Verification

Direct exhaustive enumeration of all partial 3-assignments was performed for
\(P_n\) with \(1\le n\le7\) and \(C_n\) with \(3\le n\le7\). The resulting
coefficient counts agree with (4)--(5). The proof above is independent of this
finite check.

## Limitations

The result is specific to maximum degree at most two and to the nontrivial
three-colour case. It does not give analogous closed forms for degree-three
families, where forcing can branch in substantially more complicated ways.
The source paper is extremely recent, so unindexed parallel work remains a
residual originality risk.

## References

1. G. E. Farr, *The forced colouring function of a graph*,
   arXiv:2609.17108v1 (2026).
   https://arxiv.org/abs/2609.17108v1
2. G. Farr and K. Morgan, *Graph polynomials: some questions on the edge*,
   arXiv:2406.15746v1 (2024); later published in *Model Theory, Computer
   Science, and Graph Polynomials* (Springer, 2025), pp. 265--301.
   https://arxiv.org/abs/2406.15746v1
