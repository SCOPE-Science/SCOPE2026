# Exact forbidden-target sum-product threshold over prime fields

## Finding

For every prime \(p\ge5\) and every nonzero \(a\in\mathbb F_p\), define
\[
M_p(a)=\max\{|A|: A\subseteq\mathbb F_p,\ a\notin (A+A)\cup(AA)\}.
\]
Let \(m_p(a)\) be the order in \(\operatorname{PGL}_2(\mathbb F_p)\) of
\[
T_a=\begin{pmatrix}a&-a\\1&0\end{pmatrix},
\]
which acts by \(x\mapsto a-a/x\) on the projective line. Then the exact extremum is
\[
\boxed{M_p(a)=\frac{p-1}{2}-\mathbf1\!\left\{a\text{ is a square in }\mathbb F_p^\times\text{ and }2\mid m_p(a)\right\}.}
\]
In particular, the sharp half-density construction for the forbidden value \(1\) does **not** persist uniformly for other nonzero target values. For example, \(M_7(1)=3\) whereas \(M_7(2)=2\), and \(M_{11}(3)=4\).

## Assumptions and scope

The prime \(p\) is at least \(5\); all sums, products, inverses, and matrices are over \(\mathbb F_p\). Both variables in a sum or product may be equal. The target \(a\) is nonzero. The projective order \(m_p(a)\) is the least positive integer \(m\) for which \(T_a^m\) is a nonzero scalar matrix. The claim concerns exact maximal cardinality, not a count or classification of all maximizing subsets. The excluded target \(a=0\) is not covered.

## Proof

**1. The two-involution graph and the universal upper bound.** Form a colored graph on \(\mathbb F_p\) with a sum edge between \(x\) and \(s(x)=a-x\), and, for \(x\ne0\), a product edge between \(x\) and \(i(x)=a/x\). Fixed points of either operation carry loops; a looped vertex is forbidden in an independent set. The independent sets are precisely the subsets whose pairwise sums and products omit \(a\). The involution \(s\) has the single fixed point \(w=a/2\) and partitions the remaining \(p-1\) vertices into \((p-1)/2\) two-element edges. Consequently, every independent set has size at most \((p-1)/2\).

**2. Structure and the only possible one-unit loss.** Each vertex has at most one neighbor of each color. If \(s(x)=i(x)\ne x\), the two colors join the same pair \(\{x,s(x)\}\), forming a separate two-vertex component (the equality also holds at its partner). Such a component permits one selected vertex. A vertex with a sum loop is \(w\); vertices with product loops are the square roots of \(a\), if any. The vertex \(0\) has no product edge. Outside the collapsed two-vertex components and loop vertices, all connected components are alternating even cycles or alternating paths; the endpoints of a nontrivial path are among \(0\), \(w\), and the product-loop roots. Indeed all other vertices have exactly two distinct neighbors, one of each color. The special case \(a=4\) has \(w=2\), which is looped in both colors and isolated.

Call an independent set *sum-saturating* on a component if it chooses one vertex from each of that component's nonloop sum pairs and omits \(w\), if present. An even alternating cycle admits two sum-saturating alternating choices. The isolated double-colored edge admits one vertex. On an alternating path with endpoints other than two **distinct product-loop vertices**, alternating selection also saturates every sum pair while avoiding any looped endpoint. This can be checked from the edge colors at the ends: a path starting at \(0\) starts with a sum edge, one starting at \(w\) starts with a product edge, and one starting at a product-loop root starts with a sum edge; the alternating parity fixes a compatible choice unless both endpoints are product-loop roots. An isolated vertex with two loops is omitted.

If two distinct product-loop roots lie on the same path, the path starts and ends with sum edges and has \(2h\) vertices for some \(h\ge2\). Its two endpoints are forbidden. The remaining \(2h-2\) vertices form a path, with maximal independent-set size \(h-1\), whereas it contains \(h\) nonloop sum pairs. Thus precisely one sum pair must be left unrepresented. There are at most two product-loop roots globally, so this defect can occur in at most one component. Hence
\[
M_p(a)=\frac{p-1}{2}-\mathbf1\{\text{the two distinct product-loop roots lie in one component}\}.
\]
When \(a\) is a nonsquare, there are no product-loop roots and the indicator is zero. When \(a=4\), one root equals \(w\) and is an isolated looped vertex, so the indicator is again zero.

**3. Projective-order criterion for the exceptional path.** Suppose \(a=u^2\) and \(a\ne4\), with roots \(u\) and \(-u\). Put \(f=s\circ i\), the projective transformation represented by \(T_a\). Since \(i^2=s^2=1\), one has \(i f i=f^{-1}\). Because \(i(u)=u\), the component of \(u\) under \(s,i\) is exactly its \(f\)-orbit. The two roots therefore lie in one graph component exactly when \(f^j(u)=-u\) for some integer \(j\).

The determinant of \(T_a\) is \(a\ne0\); its characteristic discriminant is \(a(a-4)\ne0\), so it has distinct eigenlines over an algebraic closure. The point \(u\) is not one of these eigenlines: indeed \(f(u)=a-u=u\) would imply \(u=2\) and \(a=4\). It follows that the orbit of \(u\) under \(f\) has full projective order \(m=m_p(a)\): for a diagonalizable projective map with two distinct eigenlines, every nonfixed point has orbit length equal to the order of the eigenvalue ratio.

If \(f^j(u)=-u\), applying \(i\) and the relation \(ifi=f^{-1}\) shows \(f^{-j}(u)=-u\), hence \(f^{2j}(u)=u\). Thus \(m\mid2j\). An odd \(m\) forces \(m\mid j\), contradicting \(u\ne-u\). Conversely, if \(m\) is even, then \(i\) fixes \(f^{m/2}(u)\), because \(i f^{m/2}=f^{-m/2}i=f^{m/2}i\). Its only finite fixed points are \(u,-u\). The point cannot be \(u\): \(f^{m/2}\) is a nonidentity power and shares the two eigenlines of \(f\), while \(u\) lies on neither. Therefore \(f^{m/2}(u)=-u\). The two roots are in one component if and only if \(m\) is even.

Finally, for \(a=4\), the matrix \(T_4\) is non-scalar with a repeated eigenvalue \(2\), so its projective order is \(p\) (a nontrivial unipotent has exact order \(p\) in characteristic \(p\)); this is odd. Thus the square-and-even-order criterion also gives zero defect at \(a=4\). Combining the three steps proves the formula in all claimed cases. \(\square\)

## Verification

The standalone program `verify.py` reconstructs forbidden-edge graphs and computes exact independent-set maxima by path/cycle dynamic programming. Separately it derives \(m_p(a)\) by iterating the projective action on \(\infty\), and evaluates the character test by Euler's criterion. These computations agree for all \(4{,}178\) prime-target pairs with \(5\le p\le199\), including \(671\) one-unit-defect pairs. For \(p\le13\), the program additionally exhausts all subsets and directly tests their pairwise sums and products. Run `python3 verify.py`; expected stdout is included in `verification_output.txt`. Finite tests support but do not prove the theorem; the proof above treats every prime and every nonzero target.

## Relationship to prior work

Tang's 2026 theorem proves sharpness of \((p-1)/2\) for the single target \(a=1\), using the two-involution graph and six-cycles. The present target-dependent formula is not a rescaling of that result: multiplying a subset by \(\lambda\) scales forbidden sums by \(\lambda\) but forbidden products by \(\lambda^2\), so these cannot both normalize a general target to \(1\). The varying projective order and the precise one-unit obstruction arise for the broader family of targets. General dense finite-field sum-product bounds concern cardinalities of entire sumsets and product sets, rather than omission of one common prescribed target.

## Limitations

No claim is made for target \(0\), for primes below \(5\), for nonprime finite fields, or for the number of maximizing sets. The formal correctness argument is an ordinary mathematical proof with finite computational cross-checks, not an independently audited certification. The searched indexed literature might omit equivalent earlier formulations, particularly in graph independence or finite-field extremal combinatorics.

## References

1. Q. Tang, *A counterexample to a conjecture of Sárközy on sums and products modulo a prime*, arXiv:2603.29992, first circulated March 31, 2026. In particular, §2, Theorem 2.2 and Remark 2.4. https://arxiv.org/abs/2603.29992
2. X. Shao, *The sum-product phenomenon for dense subsets of finite fields*, arXiv:2604.17117, 2026. https://arxiv.org/abs/2604.17117
3. A. Sárközy, Conjecture 65 in the 2001 unsolved-problems list cited in Tang's paper (historical background only).
