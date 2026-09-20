# Sharp paired-total domination gap in trees

Let \(T\) be a finite tree of order \(n\ge 2\). Write \(\gamma_t(T)\) for its
total domination number and \(\gamma_{\mathrm{pr}}(T)\) for its paired-domination
number. A paired-dominating set is a dominating set whose induced subgraph
contains a perfect matching.

## Theorem

For every \(n\ge2\),
\[
\boxed{
\max_{|V(T)|=n}\bigl(\gamma_{\mathrm{pr}}(T)-\gamma_t(T)\bigr)
=
\max\left\{0,\left\lfloor\frac{n-3}{2}\right\rfloor\right\}.
}
\]
Moreover, all extremal trees are determined up to isomorphism.

- For \(n=2\) and \(n=3\), the unique tree is extremal.
- For \(n=4\), both \(P_4\) and \(K_{1,3}\) are extremal.
- If \(n=2m+1\ge5\), the unique extremal tree is the subdivided star
  \(S(K_{1,m})\), obtained by subdividing every edge of \(K_{1,m}\) once.
- If \(n=2m\ge6\), there are exactly two extremal trees:
  \[
  A_m=K_{1,m-1}\circ K_1,
  \]
  the corona obtained by attaching one new leaf to every vertex of
  \(K_{1,m-1}\), and
  \[
  B_m,
  \]
  obtained from \(S(K_{1,m-1})\) by attaching one additional leaf to any
  support vertex.

For the odd extremal tree,
\[
\gamma_t\bigl(S(K_{1,m})\bigr)=m+1,
\qquad
\gamma_{\mathrm{pr}}\bigl(S(K_{1,m})\bigr)=2m.
\]
For each even extremal tree \(A_m,B_m\),
\[
\gamma_t=m,
\qquad
\gamma_{\mathrm{pr}}=2m-2.
\]

**Same-model review: passed. Independent audit: not yet performed.**

## Proof

A support vertex is a vertex adjacent to a leaf. Let \(s=s(T)\) be the
number of support vertices of \(T\). Chellali and Haynes proved for every
tree of order at least three that
\[
\gamma_{\mathrm{pr}}(T)\le \gamma_t(T)+s-1.
\tag{1}
\]
Hence, if
\[
q(T):=\gamma_{\mathrm{pr}}(T)-\gamma_t(T),
\]
then
\[
q(T)\le s-1.
\tag{2}
\]
For \(n\ge3\), choose one leaf adjacent to each support vertex. These chosen
leaves are distinct and disjoint from the support vertices, so
\[
s\le \left\lfloor\frac n2\right\rfloor.
\tag{3}
\]
The odd-order upper bound follows immediately. The even case requires one
additional parity-and-structure argument.

### Odd order

Let \(n=2m+1\ge5\). From (2)--(3),
\[
q(T)\le m-1.
\]
The subdivided star \(S(K_{1,m})\) attains this bound. Its \(m\) support
vertices are independent and belong to every total dominating set, because
each is the unique neighbor of a leaf. The supports together with the
center form a total dominating set, so \(\gamma_t=m+1\). Every
paired-dominating set also contains all supports. Since those supports are
independent, each needs a distinct partner; pairing every support with its
leaf gives a paired-dominating set of size \(2m\). Thus
\[
\gamma_{\mathrm{pr}}=2m,
\qquad q=m-1.
\]

We now characterize equality. Suppose \(q(T)=m-1\). Equations (2)--(3)
force \(s=m\). Choose one leaf adjacent to each support, and call the sets of
supports and chosen leaves \(S\) and \(L\), respectively. Exactly one vertex
\(x\) remains outside \(S\cup L\).

If \(x\) were an additional leaf, then all nonleaves would be supports and
\(T[S]\) would be a connected tree. Thus \(S\) itself would be a total
dominating set, so \(\gamma_t=m\). Equality \(q=m-1\) would then force
\(\gamma_{\mathrm{pr}}=2m-1\), impossible because every paired-dominating
set has even cardinality. Hence \(x\) is neither a leaf nor a support, and
\(L\) is exactly the set of leaves.

The set \(S\cup L\) is paired dominating, using the \(m\) support-leaf
edges as a perfect matching, so \(\gamma_{\mathrm{pr}}\le2m\). Every total
dominating set contains all \(m\) supports. Since
\(\gamma_{\mathrm{pr}}-\gamma_t=m-1\) and \(\gamma_{\mathrm{pr}}\) is even,
we obtain
\[
\gamma_t=m+1,
\qquad
\gamma_{\mathrm{pr}}=2m.
\tag{4}
\]
If two supports \(u,v\in S\) were adjacent, then
\[
S\cup\bigl(L\setminus\{\ell_u,\ell_v\}\bigr)
\]
would be paired dominating: pair \(u\) with \(v\), and pair every other
support with its chosen leaf. This set has size \(2m-2\), contradicting
(4). Therefore \(S\) is independent. Since deleting the leaves leaves the
connected tree induced by \(S\cup\{x\}\), every support must be adjacent to
\(x\). Hence \(T\cong S(K_{1,m})\), proving uniqueness.

### Even order

Let \(n=2m\ge6\). If \(s\le m-1\), (2) gives
\[
q(T)\le m-2.
\tag{5}
\]
It remains to consider \(s=m\). In this case the chosen \(m\) leaves and the
\(m\) supports exhaust the vertex set. Hence
\[
T=H\circ K_1
\]
for a connected tree \(H\) on the support vertices. Every total dominating
set contains all support vertices, while the support set itself is total
dominating, so
\[
\gamma_t(T)=m.
\tag{6}
\]
Let \(\nu(H)\) be the matching number of \(H\). Then
\[
\boxed{\gamma_{\mathrm{pr}}(H\circ K_1)=2m-2\nu(H).}
\tag{7}
\]
Indeed, all \(m\) supports belong to every paired-dominating set. At most
\(2\nu(H)\) of them can be paired to other supports, so at least
\(m-2\nu(H)\) of their private leaves must be selected as partners.
Conversely, a maximum matching of \(H\), together with the private leaf of
each unmatched support, realizes a perfect matching on a paired-dominating
set of exactly that size. Since \(H\) is connected and \(m\ge2\),
\(\nu(H)\ge1\), and (6)--(7) yield
\[
q(T)=m-2\nu(H)\le m-2.
\tag{8}
\]
Together with (5), this proves the even-order upper bound.

Both claimed families attain it. For
\(A_m=K_{1,m-1}\circ K_1\), equation (7) and
\(\nu(K_{1,m-1})=1\) give
\[
\gamma_t(A_m)=m,
\qquad
\gamma_{\mathrm{pr}}(A_m)=2m-2.
\]
For \(B_m\), let \(S\) be its \(m-1\) support vertices. They are independent
and forced into every total or paired dominating set. Adding the subdivided
star center gives a total dominating set of size \(m\), while pairing each
support with one of its leaf neighbors gives a paired-dominating set of size
\(2m-2\). The matching requirement and independence of \(S\) show these are
minimum, so again \(q=m-2\).

We finish by classifying equality for even order. Suppose \(q(T)=m-2\).
Then (2) implies \(s\ge m-1\), so there are two cases.

If \(s=m\), the corona representation above applies, and equality in (8)
forces \(\nu(H)=1\). A connected tree with matching number one is a star;
therefore \(T\cong A_m\).

Now suppose \(s=m-1\). Choose one leaf adjacent to each support, with sets
\(S\) and \(L\), and let \(U=V(T)\setminus(S\cup L)\). Then \(|U|=2\).
Every vertex of \(U\) is adjacent to a support: an element of \(U\) that is
a leaf has a support as its unique neighbor, while a nonleaf with no support
neighbor could only be adjacent to the other vertex of \(U\), contradicting
that it is a nonleaf. Hence \(S\cup L\) is a paired-dominating set of size
\(2m-2\), so
\[
\gamma_{\mathrm{pr}}\le2m-2.
\]
All \(m-1\) supports belong to every total dominating set. If
\(\gamma_t=m-1\), then equality \(q=m-2\) would make
\(\gamma_{\mathrm{pr}}=2m-3\), which is odd. Consequently
\[
\gamma_t=m,
\qquad
\gamma_{\mathrm{pr}}=2m-2.
\tag{9}
\]

If two supports \(u,v\in S\) were adjacent, then
\[
S\cup\bigl(L\setminus\{\ell_u,\ell_v\}\bigr)
\]
would be a paired-dominating set of size \(2m-4\), contradicting (9).
Thus \(S\) is independent. A minimum total dominating set has the form
\(S\cup\{x\}\). Because \(S\) is independent and \(|S|\ge2\), the vertex
\(x\) must belong to \(U\) and be adjacent to every support. The graph
induced by \(\{x\}\cup S\cup L\) is already a tree. Therefore the remaining
vertex of \(U\) attaches to it by exactly one edge and is a leaf; as observed
above, its neighbor is a support. Hence \(T\cong B_m\).

The cases \(n=2,3,4\) are direct: the gap is zero, with the extremal trees
listed in the theorem.

## Context and originality

Paired domination was introduced by Haynes and Slater in 1998. Chellali and
Haynes subsequently studied total and paired domination together in trees;
among their sharp support-sensitive inequalities is (1). Henning later gave
a constructive characterization of trees satisfying
\(\gamma_t=\gamma_{\mathrm{pr}}\). A 2020 survey chapter by Desormeaux,
Haynes and Henning reviews the major bounds on paired domination. More
recent work has treated paired domination in trees through structural bounds,
algorithms and probabilistic asymptotics.

The checked sources and exact/synonymous searches did not locate the
fixed-order extremum of \(\gamma_{\mathrm{pr}}-\gamma_t\), the parity-sensitive
formula above, the corona matching identity (7) in this role, or the complete
odd/even equality classification. The numerical upper bound is a short
consequence of the 2004 support-vertex inequality except for the even-order
parity refinement; the principal addition is the exact sharpness and complete
classification of all extremal trees. Originality is claimed only to the best
of our knowledge.

The 2020 survey chapter was identified and its bibliographic/abstract material
was inspected, but its complete chapter text was not available in the checked
sources. It is therefore the most relevant inaccessible source that could
contain an equivalent short corollary. The relevant support-sensitive theorem
from the 2004 paper is stated in accessible abstract/indexed material, while
the article was not read end-to-end. These leave a residual originality risk,
especially for differently phrased results not indexed under “difference” or
“gap”.

## Verification

`artifacts/verify_paired_total_gap.py` independently computes
\(\gamma_t\) and \(\gamma_{\mathrm{pr}}\) by exhaustive subset search and
checks the classification against every nonisomorphic tree of orders
\(2\) through \(12\). With NetworkX 3.6.1, the number of extremal isomorphism
classes is \(1,1,2,1,2,1,2,1,2,1,2\) for orders \(2,\ldots,12\), exactly as
predicted. The recorded output is in `artifacts/expected_output.txt`.

## Limitations

- The theorem concerns finite simple trees only; no corresponding extremum
  over all connected graphs is claimed.
- The fixed-order upper bound builds on an established support-sensitive
  inequality. The new claim is the exact order-only extremum together with
  the full extremal-tree classification.
- The 2020 paired-domination survey chapter was not inspected in full, and
  the 2004 paper was not read end-to-end. An equivalent corollary in older or
  differently indexed domination literature remains possible.
- Exhaustive verification is finite and supports, but does not replace, the
  proof.

## References

1. T. W. Haynes, P. J. Slater, *Paired-domination in graphs*, Networks 32
   (1998), 199--206.
   https://doi.org/10.1002/(SICI)1097-0037(199810)32:3<199::AID-NET4>3.0.CO;2-F
2. M. Chellali, T. W. Haynes, *Total and paired-domination numbers of a tree*,
   AKCE International Journal of Graphs and Combinatorics 1(2) (2004),
   69--75. https://doi.org/10.1080/09728600.2004.12088782
3. M. A. Henning, *Trees with equal total domination and paired-domination
   numbers*, Utilitas Mathematica 69 (2006).
   https://utilitasmathematica.com/index.php/Index/article/view/452
4. W. J. Desormeaux, T. W. Haynes, M. A. Henning, *Paired Domination in
   Graphs*, in *Topics in Domination in Graphs*, Developments in Mathematics
   64 (2020), 31--77. https://doi.org/10.1007/978-3-030-51117-3_3
5. A. Gorzkowska, M. A. Henning, M. Kleszcz, M. Pilśniak, *Paired Domination
   in Trees*, Graphs and Combinatorics 38 (2022), 129.
   https://doi.org/10.1007/s00373-022-02542-7
6. D. Ralaivaosaona, M. A. Henning, *Paired domination in trees: A linear
   algorithm and asymptotic normality*, posted 4 August 2026.
   https://doi.org/10.2139/ssrn.7228193
