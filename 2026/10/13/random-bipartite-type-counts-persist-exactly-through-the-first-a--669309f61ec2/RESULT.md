# Random-bipartite type counts persist exactly through the first algebraic-closure threshold
## Finding
Let \(T_{m,n}\) be the complete theory of existentially closed \(K_{m,n}\)-free incidence structures, with \(m,n\ge2\), and put \(k=\min(m,n)\). Define
\[
a_r=\sum_{p=0}^r\binom rp2^{p(r-p)}.
\]
Then the complete \(k\)-type count is still exactly the random-bipartite count
\[
|S_k(T_{m,n})|=\sum_{j=0}^k {{k\brace j}}a_j.
\]
This extends the previously established closure-free formula from \(r<\min(m,n)\) to the boundary arity \(r=\min(m,n)\), where algebraic closure is already nontrivial.

More precisely, among injective \(k\)-types, every mixed-sort type has algebraic-closure size \(k\). If \(m<n\), exactly the all-point type has larger closure, of size \(m+n-1\); if \(n<m\), exactly the all-line type does; and if \(m=n=k\), exactly those two same-sort types have closure size \(2k-1\). Hence the number of injective boundary types with trivial closure is \(a_k-1\) when \(m\ne n\), and \(a_k-2\) when \(m=n\).

## Assumptions and scope
The language is Conant--Kruckman's two-sorted incidence language with point predicate \(P\), line predicate \(L\), and incidence relation \(I\). Their theory \(T_{m,n}\) is the model companion of the universal theory of \(K_{m,n}\)-free incidence structures. Their algebraic-closure theorem identifies \(\operatorname{acl}(A)\) with incidence closure: whenever \(m\) points are present, one adjoins all \(n-1\) common lines, and dually whenever \(n\) lines are present, one adjoins all \(m-1\) common points.

## Proof
First consider an injective \(k\)-tuple. If it contains both points and lines, then it has fewer than \(m\) points and fewer than \(n\) lines, because \(k=\min(m,n)\). Therefore no algebraic-closure rule fires, so its algebraic closure is exactly its support.

Suppose the tuple consists entirely of points. This can meet the point threshold only when \(m=k\). In that case the \(m\) marked points have exactly \(n-1\) common lines, all algebraic over the tuple. After adjoining them there are only \(n-1<n\) lines, so the dual closure rule cannot fire, while there is no new \(m\)-set of points. Thus closure stops after one step and has size
\[
m+(n-1)=m+n-1.
\]
If \(m>k\), the all-point tuple is already closed. The all-line case is dual.

Although these one or two boundary types acquire algebraic elements, they do not split into additional complete types: the newly adjoined common lines or points are uniquely determined up to marked incidence isomorphism. Every injective boundary type is therefore still determined solely by its side assignment and the incidences among marked coordinates. Choosing \(p\) point coordinates gives \(\binom kp\) choices of sides and \(2^{p(k-p)}\) independent cross-incidence patterns, so there are exactly \(a_k\) injective \(k\)-types.

For arbitrary tuples, quotient by equality. An equality partition with \(j\) blocks yields an injective \(j\)-tuple. For \(j<k\), the previously established closure-free argument applies; for \(j=k\), the boundary argument above applies. Hence
\[
|S_k(T_{m,n})|=\sum_{j=0}^k {{k\brace j}}a_j.
\]

## Verification
The proof is finite and structural. A standalone exact-arithmetic replay recomputes the injective sequence
\[
1,2,6,26,162,1442,18306,330626
\]
and its Stirling transform
\[
1,2,8,46,362,3804,52994,981838
\]
through arity seven, and checks the boundary-exception census for every \(2\le m,n\le8\). It returns `VERIFY_OK 149 exact assertions`.

## Relationship to prior work
Conant and Kruckman prove the model-companion theorem, characterize algebraic closure by incidence closure, and show that complete types are determined by marked algebraic closures. They do not state the boundary counting formula or the exact boundary closure-size census above.

A previous calculation for this same family established the random-bipartite type formula only for \(r<\min(m,n)\), precisely where closure is trivial. The present result is not an immediate restatement of that claim: at \(r=\min(m,n)\), algebraic closure can add \(m+n-1-k\) elements. The new point is that this first nontrivial closure does not yet change the complete-type count, and the proof identifies exactly which injective types acquire algebraic elements.

Targeted semantic-index searches for the boundary formula, for “generic incidence” plus “random bipartite” and \(\min(m,n)\), and for the closure size \(m+n-1\) returned no equivalent finding. Exact web searches likewise returned the primary generic-incidence paper and unrelated uses of \(T_{m,n}\), but no published boundary census.

## Limitations
No formula is claimed above the boundary arity \(\min(m,n)\). Already at the next arity, several threshold subsets can interact and marked algebraic closure need not be determined by the raw incidence pattern alone. The originality assessment is search-based, and this short boundary observation could exist as uncatalogued folklore.

## References
1. Gabriel Conant and Alex Kruckman, *Independence in generic incidence structures*, Journal of Symbolic Logic 84 (2019), 750--780. arXiv:1709.09626. DOI: 10.1017/jsl.2019.8. First public version: 27 September 2017.
