# Four-class analogy theorem for idempotent monounary algebras

## Finding
Let \(A\) be a nonempty set equipped with a unary operation \(f:A\to A\) satisfying \(f(f(a))=f(a)\) for every \(a\in A\). Interpret analogical proportions by the monounary term-justification and directional maximality semantics of Antić [1]. For an ordered arrow \((a,b)\in A^2\), consider the disjoint classes

\[
\begin{aligned}
D&=\{(a,a):a\in A\},\\
F&=\{(a,f(a)):f(a)\ne a\},\\
B&=\{(f(a),a):f(a)\ne a\},\\
O&=A^2\setminus(D\cup F\cup B).
\end{aligned}
\]

**Theorem.** Two arrows \((a,b)\) and \((c,d)\) form an analogical proportion \(a:b::c:d\) **if and only if** they belong to the same one of \(D,F,B,O\). In particular, analogical proportion is an equivalence relation on \(A^2\), so every idempotent monounary algebra satisfies proportion transitivity, including infinite algebras. Empty classes are omitted.

For finite \(A\), put \(n=|A|\) and \(q=|A\setminus\operatorname{Fix}(f)|\). The ordered arrow class sizes are \(n,q,q,n(n-1)-2q\). Thus the exact number of satisfying ordered quadruples is

\[
\boxed{N_{\mathrm{AP}}(A)=n^2+2q^2+\bigl(n(n-1)-2q\bigr)^2},
\]

and the corresponding satisfiability probability for four independent uniform elements is \(N_{\mathrm{AP}}(A)/n^4\). The entire class-size spectrum and degree depend only on \(n\) and the number of fixed points, not on the distribution of nonfixed preimages among those fixed points. For each fixed \(n\ge2\), the degree strictly decreases as \(q\) runs through \(0,1,\ldots,n-1\); the identity operation maximizes it and constant operations minimize it.

## Assumptions and scope
The algebra has exactly one unary function symbol, no named constants, and the original monounary justification-based analogical proportion [1]; it is **not** the similarity-based variant [3]. This theorem holds for nonempty sets of arbitrary cardinality; only the numerical counting and uniform probability statements require finiteness. An *arrow* is an ordered pair, and the four-class conclusion concerns the proportional relation on arrows, not an equivalence on individual elements.

For completeness, let \(f^0\) be the identity map and let \(f^k\) be its \(k\)-th iterate. The formal justification set of an arrow is

\[
J(a,b)=\{(k,\ell)\in\mathbb N_0^2:\exists u\in A,\ f^k(u)=a,\ f^\ell(u)=b\}.
\]

A directed proportion \((a,b)\rightsquigarrow(c,d)\) is satisfied when both justification sets consist only of globally trivial rules, or their intersection \(I\) contains a nontrivial rule and is inclusion-maximal among \(J(a,b)\cap J(c,d')\) as \(d'\) varies with \(c\) fixed. The full analogical relation consists of this directed condition for \((a,b),(c,d)\), the reversed arrows, and the two directions with source and target exchanged [1, §2].

## Proof
Set \(R=\operatorname{Fix}(f)\), and abbreviate the following **sets of formal rule indices**:
\[
\begin{aligned}
J_{00}&=\{(0,0)\},\\
J_{01}&=\{(0,\ell):\ell\ge1\},\\
J_{10}&=\{(k,0):k\ge1\},\\
J_{11}&=\{(k,\ell):k,\ell\ge1\}.
\end{aligned}
\]
Because \(f^k=f\) for \(k\ge1\), direct inspection of the possible witnesses \(u\) gives precisely five justification sets:

* If \(a=b\in R\), then \(J(a,b)=J_{00}\cup J_{01}\cup J_{10}\cup J_{11}\).
* If \(a=b\notin R\), then \(J(a,b)=J_{00}\).
* If \(a\ne b=f(a)\), then \(J(a,b)=J_{01}\).
* If \(b\ne a=f(b)\), then \(J(a,b)=J_{10}\).
* Otherwise \(J(a,b)=\varnothing\).

These cases are disjoint: an off-diagonal arrow cannot be both forward and backward, since that would contradict idempotence. If \(|A|>1\), none of the four rule-index families is globally trivial, because at least one of the possible arrows excludes each family; hence the directed triviality clause applies exactly when both justification sets are empty. For \(|A|=1\), there is only one arrow and the claimed classification is immediate.

Suppose \(|A|>1\). We verify the maximality definition rather than replacing it with mere overlap. For two diagonal arrows, the common justifications contain \(J_{00}\), while no candidate with the **same first coordinate** but different second coordinate contains a rule from \(J_{00}\). Thus all four directed comparisons are maximal, even when one diagonal is at a fixed point and the other is not. For two distinct forward arrows, each forward intersection is exactly \(J_{01}\); the inverse arrows have intersections exactly \(J_{10}\). Since neither can be strictly enlarged after intersection with a source justification set equal to the same singleton family, all required directed comparisons hold. The analogous argument works for two backward arrows. Two arrows in \(O\) and their inverses have empty justification sets, so the triviality clause applies in all four directions.

Different classes cannot be analogous. An arrow in \(O\) has no justifications, whereas every arrow outside \(O\) has some, so a required directed comparison fails. Forward and backward arrows have disjoint nonempty justification sets. A nonfixed diagonal arrow shares no justification with a forward or backward arrow. Finally, if a **fixed-point** diagonal arrow is compared with a backward arrow \((r,u)\) (where \(f(u)=r\ne u\)), the source diagonal's full justification set intersects \(J(r,u)=J_{10}\) in \(J_{10}\), but replacing the target by \((r,r)\) strictly enlarges the intersection to all four families. Thus directional maximality fails. Comparing a fixed-point diagonal arrow to a forward arrow fails by applying this argument to the reversed arrows. This exhausts all pairs of distinct classes and proves the equivalence statement and transitivity.

For finite \(A\), the disjoint classes have sizes \(|D|=n\), \(|F|=|B|=q\), and \(|O|=n^2-n-2q\). The number of ordered pairs of arrows within identical classes is therefore the sum of their squared sizes, as claimed. Every integer \(0\le q\le n-1\) occurs for an idempotent unary function on an \(n\)-element set: choose \(n-q\) fixed points and send the remaining points to any fixed point. For the numerator \(T_n(q)=n^2+2q^2+[n(n-1)-2q]^2\),
\[
T_n(q+1)-T_n(q)=12q+6-4n(n-1)<0
\]
when \(n\ge2\) and \(0\le q\le n-2\): indeed its maximum over that range is \(-4(n-2)^2-2\). This yields the sharp extremal assertions.

## Verification
An independently implemented finite evaluator directly instantiated the term rules with exponents zero or one, used the original **fixed-first-coordinate** inclusion-maximality test, and checked all four directed conditions against the four-class prediction. It checked all 1,308 labelled idempotent unary maps on sets of sizes one through six, plus 67 canonical isomorphism representatives with seven through nine elements, totaling 1,826,684 ordered quadruples. It also checked the exact finite-count formula in every case. Run the included `verify.py` with Python 3; its final output is `VERIFY_OK labelled_maps=1308 canonical_large=67 ordered_quadruples=1826684`. This finite computation is evidence for, not a substitute for, the proof above.

## Relationship to prior work
Antić [1] defines the original monounary term-justification semantics, shows that proportional transitivity fails for general unary maps, and poses the problem of characterizing the monounary algebras for which it holds (Problem 6). The theorem here settles that problem for **every idempotent unary map** and adds the complete proportional-class and exact finite-degree distribution. Antić [2] supplies the general justification framework and [4] develops algorithms for broader finite settings; neither inspected material furnishes this four-class idempotent classification. The similarity-based framework [3] has a different definition and does not imply equivalence for the original relation. A finite-permutation classification addresses a complementary family; its intersection with the present idempotent class is precisely the identity operation, which is included for a uniform statement rather than claimed as a new isolated case.

## Limitations
No characterization of transitivity for arbitrary, non-idempotent monounary maps is asserted. The four equivalence classes do not recover the shape or sizes of individual nonfixed fibers, and equal satisfiability probabilities do not imply isomorphism of unary algebras. The originality comparison cannot exclude earlier equivalent results hidden under alternative terminology; external independent validation has not been performed. The finite verifier is bounded and cannot establish a theorem for infinite sets.

## References
[1] C. Antić, *Analogical proportions in monounary algebras*, arXiv:2208.06829 (first posted 14 August 2022), §§2–3, Problem 6. https://arxiv.org/abs/2208.06829

[2] C. Antić, *Analogical proportions*, arXiv:2006.02854, Annals of Mathematics and Artificial Intelligence **90** (2022), 595–644. https://arxiv.org/abs/2006.02854

[3] C. Antić, *Similarity-based analogical proportions*, arXiv:2402.18360 (2024), §§1–2. https://arxiv.org/abs/2402.18360

[4] C. Antić, *Analogical proportions II*, arXiv:2405.13461 (2024), §§2, 9. https://arxiv.org/abs/2405.13461
