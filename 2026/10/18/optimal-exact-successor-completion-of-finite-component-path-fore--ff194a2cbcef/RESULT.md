# Optimal exact-successor completion of finite-component path forests

## Finding
Let \(R\) be a functional, inverse-functional, acyclic directed relation on a nonempty set \(X\). A *successor completion* is a strict linear order \(<\) of \(X\) for which every \(R\)-edge is an immediate-successor pair. Its defect is the number of immediate-successor pairs of \(<\) not already in \(R\).

Every undirected component of \(R\) is a directed finite nonempty path, a one-way ray of type \(\omega\), a reverse ray of type \(\omega^*\), or a two-way infinite path of type \(\mathbb Z\). Let \(f\) and \(z\) denote the respective numbers of finite-path and two-way-infinite components.

**Theorem (sharp completion defect).** If \(R\) has finitely many components, then the minimum defect over all successor completions is
\[
\boxed{\delta(R)=\max\{0,f-z-1\}.}
\]
In particular, the prescribed relation is *exactly* the successor relation of some linear order if and only if \(f\le z+1\). The counts of one-way and reverse rays play no role in the minimum.

If \(R\) has infinitely many components, then \(\delta(R)=0\), also for uncountably many components (assuming the usual choice principles). Thus these two cases give a complete existence test and the optimal number of forced additional successor pairs for every functional, inverse-functional, acyclic graph.

## Assumptions and scope
A graph is functional if its outdegree is at most one, and inverse-functional if its indegree is at most one. Acyclic excludes all finite directed cycles. An isolated vertex is a finite path with one vertex. All components refer to connectivity after forgetting edge directions. Infinite components are necessarily countable, even if the entire vertex set is uncountable.

For a strict linear order \(<\), define
\[
\operatorname{Succ}(<)=\{(x,y):x<y\text{ and there is no }w\text{ with }x<w<y\}.
\]
The optimization domain consists of all \(<\) satisfying \(R\subseteq\operatorname{Succ}(<)\). Its defect is \(|\operatorname{Succ}(<)\setminus R|\), and the theorem provides an order with a finite defect in every case. For a finite-component graph this is a finite combinatorial minimization regardless of the sizes of its components.

## Proof
**1. Path components and convexity.** Outdegree and indegree at most one imply that every connected component is a finite directed path, a ray in one of two directions, or a double ray, unless it is a directed cycle; cycles are excluded. Orient each path by its directed edges. An order respecting all prescribed successor edges must order each component internally in this direction. Moreover, that component must be convex: an element of a different component lying between two of its vertices would lie between two consecutive vertices along their finite connecting path, contradicting that their connecting edge is an immediate-successor pair. Therefore every possible completion is an ordered sum of the given components, with their internal orders fixed.

**2. The endpoint transition rule.** Write \(F\), \(A\), \(B\), and \(Z\) for components of types finite, \(\omega\), \(\omega^*\), and \(\mathbb Z\), respectively. An immediate successor pair crossing the boundary of two adjacent component blocks appears if and only if the left block has a greatest element and the right block has a least element. Hence a boundary creates exactly one new edge precisely for
\[
\text{left type in }\{F,B\}\quad\text{and}\quad
\text{right type in }\{F,A\}.
\]
No new edges appear inside a component, and a boundary never creates more than one new edge. For a finite component list, the defect is therefore exactly the count of transitions obeying this rule.

**3. The finite-component lower bound.** Suppose there are \(f\ge2\) finite components, in their order of appearance. These form \(f-1\) distinct gaps. Consider a gap containing no \(Z\) component. If there is no intermediate block, the transition \(F\to F\) creates an edge. Otherwise the intermediate word contains only \(A\) and \(B\). If its first letter is \(A\), the left \(F\to A\) transition creates an edge. If its last letter is \(B\), the right \(B\to F\) transition creates an edge. In the remaining case the word begins with \(B\) and ends with \(A\), hence contains a \(B\to A\) transition, which also creates an edge. Thus each finite-to-finite gap containing no \(Z\) forces at least one additional edge. Each \(Z\) component can occupy at most one such gap, and the gaps do not overlap, so the defect is at least \(f-1-z\). The trivial nonnegative lower bound covers \(f\le1\).

**4. Attaining the bound.** Put all \(A\) components first and all \(B\) components last. When \(f=0\), place the \(Z\) components between these groups, giving no new edges. When \(f\ge1\), arrange the \(F\) components in a row, interposing one \(Z\) component between each successive pair for as long as \(Z\) components remain. Put any remaining \(Z\) components immediately after the final \(F\). By the endpoint transition rule the only new edges are between adjacent \(F\) components left unseparated. Their number is exactly \(\max\{0,f-z-1\}\). This completes the finite-component formula.

**5. Infinitely many components.** Let \(\kappa\) be the infinite cardinal number of components. Choose a dense linear order without endpoints of size \(\kappa\), for example the lexicographic order on \(\kappa\times\mathbb Q\). Index the components by this order and form their ordered sum. Distinct component blocks are never immediately adjacent in the sum, because a third block lies strictly between them. The only immediate-successor pairs are therefore the prescribed edges inside the components, and the defect is zero. For countably many components this is the dense-completion construction already used in the motivating literature.

**Consequences and boundaries.** A finite collection of path components admits an exact successor representation on the same vertex set precisely when \(f\le z+1\). One \(\mathbb Z\)-component can eliminate at most one compulsory finite-to-finite join; no collection of \(\omega\)- or \(\omega^*\)-components can replace that bridging role. If a graph has three isolated vertices and one double ray, exactly one extra edge is forced. With two isolated vertices and one double ray, none is forced. All witnessing orders with finitely many components are finite ordered sums of finite paths, rays, and double rays and hence are scattered.

## Verification
The independent executable file `verify_successor_completion.py` checks the symbolic endpoint transition rule by exhaustive component-order enumeration and by a separate dynamic-programming recurrence. For every nonempty multiset of the four component types with at most nine components, it verifies that the minimum defect equals the formula and that the explicit canonical arrangement attains it. This covers 714 multisets and 349,524 distinct component-type orders. Run `python3 verify_successor_completion.py`; the final success marker is `SUCCESSOR_COMPLETION_VERIFY_OK`.

The enumeration verifies the finite endpoint optimization through nine components; it is not an exhaustive proof for arbitrary component counts or arbitrary cardinals. Those conclusions follow from the argument above.

## Relationship to prior work
Michaliszyn and Witkowski, *Two-Variable Logic with Arbitrarily Many Successor Relations*, arXiv:2610.09758v1 (October 7, 2026), Lemma 2.2, prove exact successor realizability for a countable acyclic functional, inverse-functional graph with infinitely many components by a dense index order. They also distinguish such infinite completions from finite spanning paths, and use the lemma in their model construction. The present contribution is the sharp missing finite-component condition and, more strongly, the exact minimum number of unavoidable additional successor edges. The infinite-component case above records and straightforwardly extends their dense construction rather than claiming it as new.

Zeume and Harwath, *Order-Invariance of Two-Variable Logic is Decidable*, arXiv:1604.05843 (2016), investigate finite structures with linear orders and induced successor relations. For a finite vertex set the present formula specializes to the elementary fact that separate directed path components require exactly one joining edge per extra component. The genuinely different part concerns finitely many components that may be infinite rays or double rays, and how these change exact representability and the optimal defect.

## Limitations
The result concerns a *single* successor relation, with no requirement that the chosen order be a well-order or satisfy additional first-order constraints. It does not solve simultaneous completion for several interacting successor relations or the complexity questions of the motivating paper. A directed cycle is a genuine obstruction to any successor completion, rather than a case assigned a finite defect. The endpoint rule is elementary; the contribution is its sharp global minimization and structural zero-defect boundary for finite-component path forests. Historical priority under an older order-theoretic formulation remains possible and has not been independently certified.

## References
1. J. Michaliszyn and P. Witkowski, *Two-Variable Logic with Arbitrarily Many Successor Relations*, arXiv:2610.09758v1, first public version October 7, 2026. https://arxiv.org/abs/2610.09758.
2. T. Zeume and F. Harwath, *Order-Invariance of Two-Variable Logic is Decidable*, arXiv:1604.05843, 2016. https://arxiv.org/abs/1604.05843.
