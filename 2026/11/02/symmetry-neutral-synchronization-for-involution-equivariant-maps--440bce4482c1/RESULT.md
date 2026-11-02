# Symmetry-neutral synchronization for involution-equivariant maps and magma monoids

## Finding

Let \(Y\) be a finite set of size \(N\geq 1\), and let \(\tau:Y\to Y\) be an involution with \(f\) fixed points and \(m\) two-element orbits, so \(N=f+2m\). Let
\[
\mathcal C(\tau)=\{T:Y\to Y:T\tau=\tau T\}.
\]
Call \(T\) **synchronizing** if \(T^k\) is a constant map for some integer \(k\geq1\). If \(f\geq1\), then
\[
|\mathcal C(\tau)|=f^f N^m,\qquad
|\{T\in\mathcal C(\tau):T^k\text{ is constant for some }k\geq1\}|=
\begin{cases}f^{f-1},&m=0,\\ f^fN^{m-1},&m\geq1.\end{cases}
\]
In particular, for a **uniformly chosen** commuting transformation, the exact synchronizing probability is \(1/N\), independently of the number of transposition orbits. More precisely, the number eventually constant at any **specified** fixed point is \(f^{f-2}\) for \(m=0\), and \(f^{f-1}N^{m-1}\) for \(m\geq1\), with the convention that a one-vertex rooted tree contributes one. If \(f=0\), there are no synchronizing commuting transformations.

**Magma-monoid specialization.** Let \(X\) have \(n\geq2\) elements. On the set \(\mathcal M(X)\) of all binary operations on \(X\), use the Kim–Neggers monoid product
\[
(b\triangleleft c)(x,y)=c(b(x,y),b(y,x)).
\]
The exact number of operations \(b\) for which some positive \(\triangleleft\)-power \(b^{\triangleleft k}\) is a constant binary operation is
\[
\boxed{n^{n^2-2}}.
\]
There are \(n^{n^2}\) operations in total; hence the exact proportion is \(\boxed{1/n^2}\). For each specified constant output, exactly \(n^{n^2-3}\) operations have some power equal to that constant operation. For \(n=1\), the unique operation is itself constant and the proportion equals one.

## Assumptions and scope

The carrier \(Y\), the involution \(\tau\), and all transformations are labeled. The multiplication on \(\mathcal M(X)\) is the displayed binary-operation composition, not pointwise function composition or repeated multiplication within an individual magma. A positive power means a positive integer power in this *monoid*. Uniform sampling means uniform sampling of the labeled functions or operation tables, never isomorphism classes. The formulas hold for every positive integer \(N\) and involution with at least one fixed point, with explicit treatment of \(m=0\), and for all \(n\geq1\) in the specialization.

## Proof

**1. Fixed points of a constant power.** Suppose \(T^k\) is the constant map with value \(c\). Commutativity of \(T\) with \(T^k\) implies \(T(c)=c\): indeed, \(T\circ T^k\) has constant value \(T(c)\) whereas \(T^k\circ T\) has constant value \(c\). If also \(T\tau=\tau T\), then \(T^k\tau=\tau T^k\) and thus \(\tau(c)=c\). Conversely, if the functional digraph of \(T\) is an in-arborescence converging to a single fixed vertex \(c\), with its root self-loop, then \(T^N\) is constant at \(c\). Therefore synchronization is equivalent to eventual arrival at one \(\tau\)-fixed root, with no other directed cycle.

**2. Count all commuting maps.** The \(f\) singleton orbits must map to singleton orbits; their images may be selected independently in \(f^f\) ways. For each of the \(m\) two-element orbits, pick one representative. Its image may be any of the \(N\) vertices, and the other representative's image is forced by equivariance. Thus
\[
|\mathcal C(\tau)|=f^f N^m.
\]
If \(f=0\), an equivariant constant map cannot exist, by Step 1.

**3. Count the singleton-orbit restriction.** For a synchronizing map, the restriction to the \(f\) fixed vertices must be a rooted labeled tree oriented toward a chosen root \(c\), with the root self-loop. For a specified \(c\), the number is \(f^{f-2}\) if \(f\geq2\), by Cayley's tree formula; for \(f=1\), it is one. Summing over root choices gives \(f^{f-1}\), valid also at \(f=1\). This establishes the entire theorem when \(m=0\).

**4. Count the two-element-orbit choices.** For each of the \(m\) two-element orbits, choose the image of its representative. Its target may be (i) any of the \(f\) fixed vertices, or (ii) either orientation of any of the other \(m-1\) two-element orbits. Its image may also lie within its own orbit, but either choice would create a directed cycle, contrary to synchronization; hence those choices are excluded. Collapse each two-element orbit to one vertex and collapse the fixed-point set to one absorbing sink. The necessary and sufficient condition is that these \(m\) orbit vertices form a directed forest oriented toward the sink; acyclicity on these orbits makes every trajectory enter the already synchronizing fixed-point sector. Each edge to the sink has weight \(f\), accounting for the choice of target fixed point, and each edge to another free orbit has weight \(2\), accounting for the orientation of the target pair. Consequently, the number of valid choices on the free orbits is the total weight of spanning trees on \(m+1\) labeled vertices, where one distinguished vertex is the sink and edge weights are \(f\) for sink edges and \(2\) for edges between other vertices. The orientations toward the sink are unique.

**5. Evaluate the weighted tree sum without an unproved counting assumption.** For \(m\geq1\), put vertex weights \(w_0=f\) at the sink and \(w_1=\cdots=w_m=2\). The weight of any undirected edge \(ij\) is \(w_iw_j/2\), exactly the weight specified in Step 4. Every tree has \(m\) edges; hence its edge-weight product is
\[
2^{-m}\prod_{i=0}^{m}w_i^{\deg(i)}.
\]
The Prüfer-word bijection for labeled trees on \(m+1\) vertices has word length \(m-1\), and vertex \(i\) appears exactly \(\deg(i)-1\) times in the word. Summing over all words gives the exact identity
\[
\sum_{\text{trees}}\prod_{i=0}^{m}w_i^{\deg(i)}
=(\prod_{i=0}^{m}w_i)(\sum_{i=0}^{m}w_i)^{m-1}.
\]
Therefore the desired forest weight is
\[
2^{-m}(f2^m)(f+2m)^{m-1}=fN^{m-1}.
\]
No infinite limiting argument or probabilistic independence approximation is used.

**6. Complete the first count.** Multiply the \(f^{f-1}\) valid fixed-vertex restrictions from Step 3 by the \(fN^{m-1}\) free-orbit choices from Step 5. This yields \(f^fN^{m-1}\) for \(m\geq1\). Divide by the total \(f^fN^m\) from Step 2 to obtain exactly \(1/N\). Dividing the successful count by the \(f\) symmetric possible terminal roots gives the per-root count. The elementary boundary cases \(m=0\) and \(f=0\) were handled separately.

**7. Identify magma powers.** On \(Y=X\times X\), define \(\tau(x,y)=(y,x)\). This involution has \(f=n\) fixed points and \(m=\binom n2\) free orbits, so \(N=n^2\). Every binary operation \(b\) determines
\[
T_b(x,y)=(b(x,y),b(y,x)),
\]
which commutes with \(\tau\). Conversely, given a commuting \(T\), define \(b(x,y)\) as its first coordinate; equivariance forces its second coordinate to be \(b(y,x)\), so \(T=T_b\). Thus the correspondence is bijective. The monoid product satisfies \(T_{b\triangleleft c}=T_c\circ T_b\) in the usual right-to-left convention of function composition, by direct substitution. Therefore \(T_{b^{\triangleleft k}}=T_b^k\). A constant operation corresponds exactly to a constant transformation into a diagonal point \((c,c)\). Apply the first theorem with \(f=n\), \(m=\binom n2\), \(N=n^2\): for \(n\geq2\), the successful count is \(n^n(n^2)^{\binom n2-1}=n^{n^2-2}\). Its ratio to the \(n^{n^2}\) operation tables is \(1/n^2\). When \(n=1\), there is one operation and its first power is constant. This completes the proof.

## Verification

Run `python checker.py` using only the Python standard library. It exhaustively enumerates all \(n^{n^2}\) binary operation tables for \(n\in\{1,2,3\}\) and independently tests actual transformation iterates for eventual constant behavior. It additionally enumerates **all** equivariant maps for \(1\leq f\leq3\), \(0\leq m\leq2\), and computes the weighted orbit-forest sum directly for \(1\leq f\leq4\), \(1\leq m\leq5\). All tested counts agree with the theorem. In particular, the magma counts are \(1/1\), \(4/16\), and \(2187/19683\); for \((f,m)=(3,2)\), they are \(189/1323\). The program prints `VERIFY_OK`. These finite tests are corroboration, not a proof for arbitrary \(f,m,n\), which is supplied above.

## Relationship to prior work

Baiduk and Kozerenko (arXiv:2607.13746, first public July 15, 2026) identify the pairmorph model of the magma monoid in their §2 and derive Green-relation, ideal, idempotent, and regular-element counts in §§3–8. Their Theorem 3 supplies the underlying transformation correspondence, but their theorems do not state the distribution of elements whose **positive powers become constant**, nor an equivariant forest enumeration. The proof here makes the correspondence explicit and adds the genuinely different global-power count.

López-Permouth's open-access 2026 article determines idempotent magma elements and their counts (especially Theorems 2.9 and 3.6). Owusu-Mensah's January 2026 article treats almost-constant operations, low-order powers, and generators, including examples whose squares are constant; it does not give the all-cardinality enumeration or the involution-neutrality law. Konieczny's 1999 full-text paper describes an induced mapping on permutation cycles and characterizes Green relations and regularity for centralizers of permutations, rather than enumerating transformations whose powers converge to a constant. The exact rooted-tree mechanism has classical Cayley/Prüfer ancestry; what is not covered by those bare formulas is the invariant identification of arbitrary involution centralizers and the magma-monoid power count.

## Limitations

This is an exact **labeled** enumeration, not an isomorphism-class count. It requires an involution; a general permutation of larger order has different equivariance constraints and is not covered. Involutions without fixed points admit no synchronized maps, and the \(1/N\) law does not apply in that case. The conclusion concerns eventual **constant** powers, not all eventually idempotent elements (which are more numerous), not powers with other periodic images, and not arbitrary semigroup nilpotence. Although comparisons with closely related sources found no identical result, an earlier theorem on transformation centralizers, weighted rooted forests, or power classes might imply the formula under a different formulation; exhaustive historical coverage is not claimed.

## References

1. Y. Baiduk and S. Kozerenko, *Transformation semigroup perspective on the magma monoid*, arXiv:2607.13746 (first posted 2026-07-15); later *Semigroup Forum*, DOI: 10.1007/s00233-026-10659-x. Sections 2–8 and Theorem 3 are especially relevant.
2. S. R. López-Permouth, *Idempotent elements in binary and s-ary magma monoids*, *São Paulo Journal of Mathematical Sciences* 20, article 14 (2026), DOI: 10.1007/s40863-025-00519-x, published 2026-04-27.
3. I. Owusu-Mensah, *Generator Sets for the Magma Monoid*, *Advances in Pure Mathematics* 16 (2026), 1–18, DOI: 10.4236/apm.2026.161001, published 2026-01-08.
4. J. Konieczny, *Green's relations and regularity in centralizers of permutations*, *Glasgow Mathematical Journal* 41 (1999), 45–57, DOI: 10.1017/S0017089599970301.
5. Classical Cayley tree enumeration and Prüfer coding, used with all details of the necessary weighted identity given in Step 5.
