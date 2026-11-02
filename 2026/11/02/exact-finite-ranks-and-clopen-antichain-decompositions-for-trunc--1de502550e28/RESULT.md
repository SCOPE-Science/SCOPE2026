# Exact finite ranks and clopen antichain decompositions for truncated eventual domination

## Finding

For the strict numerical order on \(\omega\), consider the finite-stage relations used to approximate eventual strict domination. For every integer \(m,k\ge1\), their exact chain height and the exact ordinal rank of their strict transitive closures are

\[
\operatorname{ht}(\prec_{m,k})=\operatorname{rk}(\overline{\prec_{m,k}})=m(k-1)+1.
\]

There is a **continuous**, finite-prefix-determined strict order homomorphism from the closure to the chain of precisely this size. Its fibers form exactly \(m(k-1)+1\) clopen antichains, and no partition into fewer (even arbitrary) antichains exists. In particular the canonical diagonal truncation \(\prec_m=\prec_{m,m}\) has exact rank \(m(m-1)+1\).

## Assumptions and scope

Work in Baire space \(\omega^\omega\) with the product of the discrete topologies. All comparisons \(<\) on natural numbers are the ordinary numerical strict order. For \(x,y\in\omega^\omega\) satisfying \(x(i)<y(i)\) for all sufficiently large \(i\), let \(n(x,y)\) be the **least** index \(n\) with \(x(i)<y(i)\) for every \(i\ge n\). Write

\[
x\prec_{m,k}y \quad\Longleftrightarrow\quad
\bigl[x(i)<y(i)\text{ eventually}\bigr]\ \wedge\ n(x,y)<m\ \wedge\ x(n(x,y))<k\ \wedge\ y(n(x,y))<k.
\]

These relations need not be transitive. Denote their strict transitive closures by \(\overline{\prec_{m,k}}\). The rank of a strict well-founded partial order is the least ordinal admitting a strict order homomorphism into it, as in the motivating reference. We allow all \(m,k\ge1\), including \(k=1\), when the relation is empty.

## Proof

**1. The strict finite-prefix rank map.** Put \(N=m(k-1)+1\). For \(x\in\omega^\omega\), let

\[
J(x)=\{i<m:x(i)<k-1\}.
\]

If \(J(x)\) is empty, put \(r(x)=1\). Otherwise let \(j(x)=\max J(x)\), and put

\[
r(x)=1+j(x)(k-1)+(k-1-x(j(x))).
\]

This takes values in \(\{1,2,\dots,N\}\), and depends only on \(x(0),\dots,x(m-1)\); hence it is continuous into a discrete finite set. (For \(k=1\), always \(J(x)=\varnothing\) and \(r(x)=1\).)

Suppose \(x\prec_{m,k}y\), and write \(n=n(x,y)\). Numerical strictness at the pivot implies \(x(n)\le k-2\), so \(j(x)\) exists and \(j(x)\ge n\). For every \(i>j(x)\) with \(i<m\), we have \(x(i)\ge k-1\). Since \(i\ge n\), we have \(y(i)>x(i)\), so \(y(i)\ge k\). Thus either \(J(y)\) is empty or \(j(y)\le j(x)\). If \(J(y)\) is empty, \(r(y)=1<r(x)\), unless \(r(x)=1\); the latter is impossible since \(x(n)\le k-2\). If \(j(y)<j(x)\), the strict inequality \(r(y)<r(x)\) follows from the disjoint consecutive blocks of possible ranks attached to successive values of \(j\). If \(j(y)=j(x)\), then \(y(j(x))>x(j(x))\), so the final summand in \(r\) strictly decreases. Thus in every case,

\[
x\prec_{m,k}y\quad\Longrightarrow\quad r(x)>r(y).
\]

The same is true along every nonempty finite path and therefore in \(\overline{\prec_{m,k}}\). The increasing rank map \(h(x)=N-r(x)\) takes values in \(\{0,\dots,N-1\}\), proving \(\operatorname{rk}(\overline{\prec_{m,k}})\le N\) and forbidding chains with more than \(N\) vertices.

**2. An extremal chain.** Begin with the identically zero sequence. For each \(j=m-1,m-2,\dots,0\) in that order, perform exactly \(k-1\) moves, each increasing by one **every** coordinate of index at least \(j\), and keeping every coordinate below \(j\) fixed. At the start of phase \(j\), its pivot coordinate has value zero, since earlier phases used only larger pivots. During the \(k-1\) moves at pivot \(j\), that coordinate takes successive values \(0,1,\dots,k-1\). Every coordinate at least \(j\) strictly increases, while for \(j>0\) the preceding coordinate \(j-1\) is unchanged. Therefore each move has least eventual-onset index exactly \(j<m\), with both pivot values below \(k\), and is an edge of \(\prec_{m,k}\). This constructs precisely \(m(k-1)\) edges, hence \(N\) distinct vertices. For \(k=1\) there are zero moves, giving the one-vertex extremum. This proves the reverse bound and the exact rank.

**3. Optimal clopen decomposition.** Each fiber of \(r\) is clopen, since membership depends on finitely many discrete coordinates, and is an antichain for the strict transitive closure, since \(r\) strictly decreases on comparable pairs. The extremal chain meets all \(N\) fibers and forces any antichain partition (Borel or otherwise) to have at least \(N\) classes. Hence the ordinary and clopen antichain-chromatic numbers both equal \(N\). Substituting \(k=m\) yields \(m(m-1)+1\) for the canonical truncations.

## Verification

The accompanying standalone `checker.py` constructs all sharp chains for \(1\le m,k\le4\), checks every edge and verifies that the explicit rank descends by exactly one at successive vertices. It additionally exhausts 4,816 finite-prefix edge instances for \(1\le m\le3\), \(1\le k\le4\), with a fixed strictly increasing infinite tail after the prefix, checking strict rank decrease. Run using `python3 checker.py` from the extracted package. The mathematical proof above, not finite enumeration, establishes all parameters and infinite tails.

## Relationship to prior work

Cull and Weilacher, *Hyperwellfoundedness and Eventual Domination* (arXiv:2610.27477v1, October 20, 2026), Proposition 1.6 and Section 2.2, introduce the relations \(\prec_{m,k}\) for arbitrary **countable partially ordered** coefficient sets and derive the upper bound \((k+1)^m\) for chain height. Their general construction demonstrates hyper-(finite rank) and Borelness of the strict transitive closures; these conclusions are not claimed as new here. Restricting to the particular strict numerical order is essential for the threshold argument \(x(n)\le k-2\). The present result determines the **exact** rank and optimal clopen antichain decomposition, which do not follow from the stated general upper bound alone.

The Borel antichain-coloring problem is also discussed in Bosek, Grytczuk and Lonc, *Dilworth's Theorem for Borel Posets* (arXiv:2004.02162v1, 2020). Abstract finite-rank antichain decomposition principles are not presented here as new; what is determined is the sharp explicit rank and a continuous finite-prefix witness for this specific family.

## Limitations

The exact formula applies only to the usual natural-number strict order, **not** to an arbitrary partial order on a numerically labeled countable set. It concerns these prescribed truncation relations and their strict transitive closures, not every possible finite-rank approximation to eventual domination. The sharp chain bound is not an optimality statement about the entire countable decomposition in the motivating theorem. Although the inspected primary source does not state this exact formula, historical priority relative to all unpublished or unlocated treatments is not established. 
## References

1. A. Cull and F. Weilacher, *Hyperwellfoundedness and Eventual Domination*, arXiv:2610.27477v1 (2026), Proposition 1.6, Section 2.2. https://arxiv.org/html/2610.27477v1
2. B. Bosek, J. Grytczuk and Z. Lonc, *Dilworth's Theorem for Borel Posets*, arXiv:2004.02162v1 (2020). https://arxiv.org/abs/2004.02162
