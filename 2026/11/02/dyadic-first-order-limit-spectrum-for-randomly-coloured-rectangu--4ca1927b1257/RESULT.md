# Dyadic first-order limit spectrum for randomly coloured rectangular grids

## Finding

Let \(G_{m,n}=P_m\mathbin\square P_n\) be the undirected Cartesian product of two path graphs, regarded as a structure with its undirected adjacency relation \(E\) and one independently sampled unary predicate \(P\). Each vertex satisfies \(P\) independently with a fixed probability \(p\), where \(0<p<1\). Assume \(m,n\geq3\) and \(\min(m,n)\to\infty\), with no restriction on the aspect ratio.

**Theorem.** For every first-order sentence \(\varphi\) in \(\{E,P\}\), there is a finite integer \(L=L(\varphi)\) and a Boolean function \(F_\varphi\) of the colours in four \(L\times L\) inward-oriented corner patches such that
\[
\Pr\bigl(G_{m,n}\models\varphi\ \mathbin\triangle\ F_\varphi\bigr)\longrightarrow0.
\]
Here \(\triangle\) means exclusive-or of the two events. The function can be chosen invariant under all permutations of its four patch arguments. Consequently, the limiting probability \(\ell_\varphi(p)\) exists for every fixed \(0<p<1\) and is a polynomial in \(p\) with integer coefficients.

For fair colours \(p=1/2\), the set of all possible first-order limiting probabilities is **exactly**
\[
\boxed{\bigl\{k/2^d: d\in\mathbb N_0,\ 0\leq k\leq 2^d\bigr\}.}
\]
More strongly, every such dyadic rational is attained by a first-order sentence whose probability equals that rational for *all sufficiently large* \(m,n\), not merely in the limit.

## Assumptions and scope

The language has equality, the symmetric irreflexive edge relation \(E\), and the unary colour predicate \(P\); it has no coordinate orders, edge directions, named corners, arithmetic, counting quantifiers, or transitive closure. The graph \(G_{m,n}\) is the cover graph (undirected Hasse graph) of the finite distributive lattice \(C_m\times C_n\), not that lattice in its full order language. A vertex is a *corner* precisely when its graph degree is two, once \(m,n\geq3\). For a fixed sentence, the probability is over the independent vertex colours only.

A rooted coloured radius-\(R\) ball is the induced \(\{E,P\}\)-structure on vertices at graph distance at most \(R\), together with its root. We use the bounded-degree form of Hanf locality: for each sentence \(\varphi\), there exist \(R,T\geq1\) such that two degree-at-most-four structures satisfying, for every rooted radius-\(R\) type, equal multiplicities below \(T\) or multiplicities both at least \(T\), agree on \(\varphi\).

## Proof

**1. Abundance away from the corners.** Fix \(\varphi\) and choose the locality parameters \(R,T\). Call a rooted coloured radius-\(R\) type *repeatable* if its uncoloured rooted geometry occurs in the infinite square grid \(\mathbb Z^2\) or in an infinite grid half-plane \(\mathbb Z\times\mathbb N_0\). There are only finitely many possible rooted types because the graph degrees are bounded and there is one unary predicate.

For any repeatable type \(\tau\), fix a compatible placement in an infinite full grid or half-plane. Its local geometry appears in \(G_{m,n}\) at a number of mutually radius-\(R\)-disjoint placements tending to infinity as \(\min(m,n)\to\infty\): choose interior placements in the first case, or a long side with the same fixed distance from the boundary in the second. The event that a placement has precisely the prescribed colouring has the same strictly positive probability \(p^{a}(1-p)^{b}\), where \(a,b\) are fixed nonnegative integers. Events at disjoint placements are independent. A binomial tail bound therefore gives
\[
\Pr\bigl(\#\tau<T\bigr)\longrightarrow0.
\]
A union bound over finitely many repeatable types shows that, with probability tending to one, *every* repeatable type has multiplicity at least \(T\).

**2. Everything else is a corner event.** If an \(R\)-ball centre is not within distance \(R\) of two perpendicular sides, its uncoloured \(R\)-ball has exactly the geometry of a ball in the full plane or a half-plane (for all sufficiently large \(m,n\)). Thus every *nonrepeatable* coloured type has all its occurrences among the four corner squares of side \(R+1\). Each of those balls lies inside an inward-oriented corner square of side \(L=2R+1\). For sufficiently large sides, the four \(L\times L\) patches are disjoint. Every multiplicity of every nonrepeatable type is therefore an exact deterministic function of these four patches.

On the high-probability abundance event in Step 1, Hanf's criterion says that the truth of \(\varphi\) is completely determined by the truncated type-count profile. All repeatable coordinates of that profile are saturated, while all other coordinates are computed from the four corner patches. Any two sufficiently large coloured rectangles with the same four patches have the same truth value of \(\varphi\) whenever the abundance event holds. Hence a single Boolean function \(F_\varphi\), independent of \(m,n\), exists. Each exceptional count is the sum of the separate contributions of four isomorphic corner quadrants; consequently \(F_\varphi\) can be taken symmetric under permutation of its four patch arguments.

The colours in the four patches are independent Bernoulli-\(p\) variables. For some finite integer \(N=4L^2\), the limiting probability is consequently
\[
\ell_\varphi(p)=\sum_{\mathbf c:F_\varphi(\mathbf c)=1}
 p^{\#1(\mathbf c)}(1-p)^{N-\#1(\mathbf c)}.
\]
This is an integer-coefficient polynomial in \(p\). At \(p=1/2\) it is a dyadic rational, proving the upper inclusion.

**3. First-order recovery of arbitrarily many independent corner bits.** For each fixed \(j\geq0\) and corner \(c\), let \(v_j(c)\) be the vertex at coordinate distances \(j,j\) inward from \(c\). The point \(v_0(c)=c\) is definable. To define \(v_j(c)\) for \(j\geq1\), first say that the graph distance from \(c\) to \(v\) equals \(2j\), then require at least \(\binom{2j}{j}\) pairwise distinct shortest paths of length \(2j\) from \(c\) to \(v\). All these conditions are first-order for fixed \(j\): a shortest path of fixed length and a finite collection of pairwise different paths are expressible by finitely many existentially quantified vertices.

Indeed, for a vertex at inward coordinate distances \(a,b\) with \(a+b=2j\), the number of shortest paths from the corner is exactly \(\binom{2j}{a}\). This is strictly maximized at \(a=b=j\). Thus the formula defines precisely \(v_j(c)\), provided both grid sides exceed \(2j\).

Fix \(t\geq2\). For every corner \(c\), read the \(t\) bits \(P(v_0(c)),\ldots,P(v_{t-1}(c))\) as a corner code. For sufficiently large grid sides, these \(4t\) vertices are distinct, so the four corner codes are independent uniform members of an alphabet of size \(a=2^t\) when \(p=1/2\). Each specified corner code and each assertion about the multiset of four corner codes is first-order expressible. No orientation of the corners is needed.

**4. Exact realization of every dyadic rational.** The action of the full symmetric group on four positions partitions the \(a^4\) ordered quadruples of corner codes into orbits. Their sizes and numbers are
\[
\begin{array}{c|ccccc}
\text{orbit size}&1&4&6&12&24\\
\hline
\text{orbit count}&a&a(a-1)&\binom a2&a\binom{a-1}2&\binom a4.
\end{array}
\]
These correspond, respectively, to multiplicity patterns \((4),(3,1),(2,2),(2,1,1),(1,1,1,1)\) among the four symbols.

For \(a\geq4\), every integer between zero and \(a^4\) is a sum of a subcollection of these orbit sizes. To see this, list all orbit sizes nondecreasingly. The initial \(a\) ones attain every integer from zero to \(a\). The first four is no larger than \(a+1\); after all fours the current attainable maximum is \(a+4a(a-1)\geq52\), so the first six is at most that maximum plus one. The same induction applies to the twelves and twenty-fours. The elementary interval-extension rule is that adding a summand no larger than one more than the current full interval's endpoint preserves an initial interval of subset sums. The final maximum is the sum of all orbit sizes, namely \(a^4\).

Choose any desired \(K\in\{0,\ldots,a^4\}\), select a union of orbits with exactly \(K\) ordered code quadruples, and assert that the multiset of four corner codes belongs to this union. This is a first-order sentence, and its probability is *exactly* \(K/a^4\) for all sufficiently large rectangles. Every dyadic \(k/2^d\) can be written in this form by taking \(t\geq\max\{2,\lceil d/4\rceil\}\) and \(K=k2^{4t-d}\). This proves the reverse inclusion and the eventual-exactness assertion. \(\square\)

## Verification

The self-contained `checker.py` verifies the orbit-size totals, the gap-free subset-sum criterion for code alphabet sizes \(4,8,16\), and the uniqueness of diagonal-geodesic maximizers at four corners of several finite grids. It independently enumerates the \(4^4=256\) code quadruples and compares their multiplicity-pattern counts with the displayed orbit formula. Run `python3 checker.py` with a standard Python 3 interpreter. The expected terminal line is `ALL_CHECKS_OK`. The finite checker is a consistency test; Hanf locality, asymptotic abundance, and all-size subset-sum induction are proved above, not inferred from finite testing.

## Relationship to prior work

Kurilić's 2026 work on products of chains studies elementary equivalence, elementary substructures, finite axiomatizability, and definability for products in the *lattice order* language. The present result instead concerns stochastic unary expansions of their **undirected cover graphs** and determines the complete first-order probability spectrum as both path lengths grow. Neither claim follows by literal specialization of the other's statement.

Coupier, Desolneux, and Ycart study random images with periodic torus boundaries and directional image relations and prove a zero-one law for constant nondegenerate pixel bias. They expressly observe that *without* periodic boundaries the four corners yield a nontrivial limiting probability. That observation supplies a boundary obstruction but does not give the full converse construction realizing *every* dyadic probability in the unoriented graph language, nor the complete corner-control statement for arbitrary first-order sentences. The present argument uses the classical Hanf locality theorem rather than claiming it as new.

## Limitations

This is a limit classification for independently coloured, degree-bounded *undirected cover graphs*. It does not apply as stated to the full product-order relation, directed coordinate successor predicates, extra global relations, unbounded quantifier extensions, or coloured grids with one bounded side. The bias parameter is fixed strictly between zero and one; the theorem does not address regimes where the colour probability approaches zero or one with grid size. The degree and finite-pattern hypotheses are essential to the abundance argument. The priority comparison covers the cited sources and targeted searches, not every historical treatment of boundary-sensitive random image logic.

## References

1. M. S. Kurilić, *Model Theory of Products of Chains*, arXiv:2610.24683v1 (first submitted 2026-10-17), especially Theorem 1.1 and Sections 4–7. https://arxiv.org/abs/2610.24683
2. D. Coupier, A. Desolneux and B. Ycart, *A zero-one law for first-order logic on random images*, arXiv:math/0603333 (2006), especially the boundary discussion on page 4 and Proposition 2.4. https://arxiv.org/pdf/math/0603333
3. Hanf locality, as presented in *Finite and Algorithmic Model Theory*, Lecture 6, section “Hanf locality,” available at https://iccl.inf.tu-dresden.de/w/images/1/12/FMT-Lecture6.pdf .
