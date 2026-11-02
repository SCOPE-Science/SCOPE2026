# The two-failure boundary of Gödel–Dummett prelinearity in finite Heyting algebras

## Finding
Let \(H\) be any finite nontrivial Heyting algebra. Count ordered pairs of valuations that falsify the Gödel–Dummett prelinearity identity:
\[
B(H)=\{(a,b)\in H^2:(a\to b)\vee(b\to a)\ne\top\}.
\]
There are exactly **two** ordered failures if and only if the finite poset \(P\) of join-irreducibles of \(H\), ordered in the downset representation \(H\cong J(P)\), has the form
\[
\boxed{P\cong C_k\oplus A_2\oplus F,\quad k\ge0,\quad F\ne\varnothing,\quad F\text{ a forest poset}.}
\]
Here \(C_k\) is a chain with \(k\) points (possibly empty), \(A_2\) is a two-point antichain, \(\oplus\) is ordinal sum, and a **forest poset** means that every principal downset is a chain. The two failing valuations are precisely the two orderings of the distinct ideals \(C_k\cup\{u\}\) and \(C_k\cup\{v\}\), where \(u,v\) are the two points of \(A_2\). In particular, two is the least positive possible number of ordered failures.

Furthermore, if \(P\) has \(n\ge3\) points, every algebra in this two-failure class has
\[
|H|=k+3+|J(F)|\le 3+2^{n-2}.
\]
The equality case is unique up to poset isomorphism:
\[
\boxed{P\cong A_2\oplus A_{n-2}.}
\]
Consequently, within the **two-failure class**, the satisfiability degree is exactly \(1-2/|H|^2\) and is at most \(1-2/(3+2^{n-2})^2\), with the same unique equality case. The quantitative extremal example is a special weak-order construction already covered by earlier exact weak-order prelinearity counts; the new assertion here is the exhaustive rigidity classification among *all* finite Heyting algebras, including non-weak-order posets.

## Assumptions and scope
A finite poset \(P\) defines the Heyting algebra \(J(P)\) of its order ideals, ordered by inclusion. For downsets \(I,J\), the relative pseudocomplement is
\[
I\to J=\{p\in P:(\downarrow p)\cap I\subseteq J\}.
\]
The displayed set is itself a downset. \(\operatorname{Jirr}(H)\) consists of the nonzero join-irreducible elements of the bounded distributive lattice underlying \(H\). The hypotheses exclude the one-element algebra; no connectedness, chain, width or height assumption is imposed on \(P\). Counts use **ordered** pairs in the full square \(H^2\), including equal pairs. The claimed classification is finite only.

## Proof
**1. The exact obstruction.** For downsets \(I,J\), the prelinearity identity fails at \(p\in P\) if and only if both \((I\setminus J)\cap\downarrow p\) and \((J\setminus I)\cap\downarrow p\) are nonempty. Thus failure is equivalent to the existence of incomparable points \(u\in I\setminus J\), \(v\in J\setminus I\) possessing a common upper bound \(p\). Incomparability follows because both valuations are downsets. Swapping \(I,J\) preserves failure, and no diagonal pair fails. Hence the least positive number of ordered failures is at least two.

**2. A unique unordered failure forces an ordinal sum.** Assume there are exactly two ordered failures, and choose a failing pair \((I,J)\) with witnesses \(u,v,p\) as above. Define the sets
\[
\mathcal X_u=\{K\in J(P):u\in K,\ v\notin K\},\qquad
\mathcal X_v=\{K\in J(P):v\in K,\ u\notin K\}.
\]
Every ordered pair in \(\mathcal X_u\times\mathcal X_v\) fails, witnessed by the same \(u,v,p\). These two sets are nonempty (they contain \(\downarrow u\) and \(\downarrow v\), respectively). Because only one unordered failure is allowed, they must each be singletons: \(\mathcal X_u=\{\downarrow u\}\) and \(\mathcal X_v=\{\downarrow v\}\).

If a point \(w\) satisfied neither \(w\le u\) nor \(v\le w\), then \(\downarrow u\cup\downarrow w\) would be a second, larger member of \(\mathcal X_u\), a contradiction. Thus
\[
P=\downarrow u\cup\uparrow v.
\]
The symmetric argument gives \(P=\downarrow v\cup\uparrow u\). Since \(u,v\) are incomparable, these two coverings partition \(P\) into a common strict lower set \(L\), the pair \(\{u,v\}\), and a common strict upper set \(U\), with all lower points below both middle points and all upper points above both. Hence \(P=L\oplus A_2\oplus U\). The common upper bound \(p\) guarantees \(U\ne\varnothing\).

If \(L\) contained incomparable points \(r,s\), the ideals \(\downarrow r,\downarrow s\) would give another unordered failure (witnessed by common upper bound \(u\)); this is distinct from the exceptional pair because neither ideal contains a middle point. Thus \(L=C_k\) is a chain. If \(U\) contained incomparable \(r,s\) with a common upper bound \(t\) in \(U\), the ideals
\[
L\cup\{u,v\}\cup\downarrow_U r\quad\text{and}\quad L\cup\{u,v\}\cup\downarrow_U s
\]
would yield another failing unordered pair. They also differ from the exceptional pair because both contain \(u,v\). Therefore no incomparable points in \(U\) have a common upper bound: equivalently, each principal downset in \(U\) is a chain, so \(U=F\) is a forest poset.

**3. Converse and exact failures.** Let \(P=C_k\oplus A_2\oplus F\) with nonempty forest \(F\). Every proper ideal of \(C_k\) is comparable with all ideals of \(P\). Every other ideal is exactly one of \(L\), \(L\cup\{u\}\), \(L\cup\{v\}\), or \(L\cup\{u,v\}\cup T\) for an ideal \(T\subseteq F\), where \(L=C_k\) as a set. The only incomparable middle-type ideals are \(L\cup\{u\}\) and \(L\cup\{v\}\); they fail prelinearity because \(F\ne\varnothing\) supplies a common upper bound of \(u,v\). Any two incomparable large ideals have differences wholly in \(F\), and those differences contain no points with a common upper bound by the forest property. They do not fail. Thus the stated two ordered pairs are the only failures.

**4. Counting and the equality classification.** The proper ideals of \(C_k\) contribute \(k\) elements of \(H\); the ideals \(L\), \(L\cup\{u\}\), and \(L\cup\{v\}\) contribute three; the remaining ideals correspond bijectively to the \(|J(F)|\) ideals of \(F\) (including the empty ideal). Therefore \(|H|=k+3+|J(F)|\). Writing \(m=|F|=n-k-2\ge1\), one has \(|J(F)|\le2^m\), with equality precisely when \(F\) is an antichain. Since \(k+2^m\le 2^{m+k}=2^{n-2}\), with strict inequality for \(k\ge1\) and \(m\ge1\), the asserted sharp bound and unique extremizer follow. Divide the two exceptional ordered pairs by \(|H|^2\) to obtain the satisfiability-degree statement.

## Verification
The standard-library Python file `verify_prelinearity.py` enumerates all transitive partial orders compatible with an increasing labeling on at most six points, thereby covering every finite poset isomorphism type of those orders. It independently evaluates the Heyting implication on all pairs of downsets and compares the direct count of failing ordered pairs with the poset normal form. It checks 5,231 such posets and independently checks the extremal count and the construction \(A_2\oplus A_m\) for \(1\le m\le7\). Reproduce by running `python verify_prelinearity.py`. The all-size theorem is deduced from the four proof steps above; finite tests are corroboration, not a substitute for the universal proof.

## Relationship to prior work
Bumpus and Kocsis [1] developed satisfiability-degree questions for finite Heyting algebras, including other classical equations and their possible gaps. Standard finite duality and the Gödel–Dummett prelinearity/forest correspondence are established background [2,3]. Previous exact counting of the Dummett formula on ordinal sums of antichains already covers the special weak-order extremal example \(A_2\oplus A_m\); the new classification does not claim that example as new. The exact **minimal nonzero ordered-failure classification for arbitrary finite Heyting algebras** is not supplied by the inspected primary results or that weak-order formula: arbitrary forests \(F\) in the middle-stage rigidity theorem need not be antichains or weak orders.

## Limitations
The claim concerns ordered evaluation pairs for the single binary prelinearity equation, not all near-valid intuitionistic identities. No classification is asserted for three or more unordered failures, infinite Heyting algebras, or a different weighting of valuations. A complete historical-priority guarantee cannot be inferred from finite searches; earlier equivalent statements under alternative terminology remain a risk. The polynomial finite check is not an infinite proof. Independent scientific validation has not been performed.

## References
[1] B. M. Bumpus and Z. A. Kocsis, *Degree of Satisfiability in Heyting Algebras*, arXiv:2110.11515 (first public version 2021-10-21).

[2] L. Cabrer and H. A. Priestley, *Gödel Algebras: Interactive Dualities and Their Applications*, arXiv:1312.0413 (2013).

[3] N. Bezhanishvili, J. Martins and T. Moraschini, *Bi-intermediate Logics of Trees and Co-trees*, arXiv:2211.14776 (2022).
