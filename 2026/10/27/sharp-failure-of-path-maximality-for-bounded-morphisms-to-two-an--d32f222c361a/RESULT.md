# Sharp failure of path maximality for bounded morphisms to two- and three-world chains

## Finding

Let \(T\) be a finite nonempty tree with a distinguished root and reflexive ancestor accessibility. Let \(C_j\) be the reflexive linear order on \(j\) worlds, for \(j=2,3\). Denote by \(F_j(T)\) the number of all bounded morphisms \(T\to C_j\), counting distinct vertex maps, **without** a global-surjectivity requirement.

**Exact root recurrences.** For a one-vertex tree, \(F_2(T)=F_3(T)=1\). If the root has nonempty family of child subtrees \(T_1,\ldots,T_d\), then
\[
 F_2(T)=1+\prod_{i=1}^d F_2(T_i),\qquad
 F_3(T)=\prod_{i=1}^d F_3(T_i)+\prod_{i=1}^d F_2(T_i).
\]
The unique minimum at order \(n\ge2\) is \(F_2=F_3=2\), attained by the rooted star. The rooted path \(P_n\), rooted at one end, satisfies
\[
 F_2(P_n)=n,\qquad F_3(P_n)=1+\binom n2.
\]
**Sharp path-breakdown thresholds.** Among all rooted trees on \(n\) vertices, \(P_n\) maximizes \(F_2\) exactly when \(n\le5\), and maximizes \(F_3\) exactly when \(n\le6\). For \(F_2\), the first counterexample (\(n=6\)) is the unique maximizing rooted shape, with a root attached to paths on two and three vertices: it has \(7\) maps versus \(6\) for the path. For \(F_3\), the first counterexample (\(n=7\)) is the unique maximizing rooted shape, with a root attached to two three-vertex paths: it has \(25\) maps versus \(22\) for the path.

The breakdown is not isolated. For every \(k\ge2\) and \(r\in\{0,1\}\), attaching \(k-r\) two-vertex path branches and \(r\) three-vertex path branches to a new root yields \(n=2k+1+r\) and
\[
 F_2(T)=1+2^{k-r}3^r>n\quad\text{for every }n\ge6.
\]
For every \(k\ge2\), \(r\in\{0,1,2\}\), attaching \(k-r\) three-vertex path branches and \(r\) four-vertex path branches to a new root yields \(n=3k+1+r\) and
\[
 F_3(T)=4^{k-r}7^r+3^{k-r}4^r>1+\binom n2\quad\text{for every }n\ge7.
\]
Thus the unrestricted tree maxima exceed the path counts at **every** order beyond the stated thresholds. Moreover, a root attached to \(k\) three-vertex paths has \(F_2=1+3^k\) on \(3k+1\) vertices, while a root attached to \(k\) four-vertex paths has \(F_3=7^k+4^k\) on \(4k+1\) vertices: each p-morphism count can grow exponentially where the corresponding path count is polynomial.

## Assumptions and scope

Every finite rooted tree is considered with the partial order \(x\le y\) iff \(x\) is on the unique root-to-\(y\) path, including equality. The target \(C_j\) is \(\{0,\ldots,j-1\}\) with its usual reflexive order. A bounded morphism is a function \(f:T\to C_j\) obeying:

1. **Forth:** \(x\le y\Rightarrow f(x)\le f(y)\).
2. **Back:** if \(f(x)\le a\) in the target, then some \(y\ge x\) has \(f(y)=a\).

In particular, every leaf must go to the top world. A bounded morphism onto the image need not be onto the full target; requiring global surjectivity would give a different invariant. All trees and maps are unlabeled except that different vertex functions count separately on each fixed source tree; tree isomorphism only identifies source shapes for extremal statements.

## Proof

**Root recurrences.** Suppose the root has child subtrees \(T_i\). Any bounded morphism sends each leaf to the maximum target world. For \(C_2\), a root mapped to the upper world forces the unique constant-upper map. If mapped to the lower world, each child subtree may carry independently any bounded morphism into \(C_2\), and each such map contains an upper-world descendant; this supplies the root's back obligation. Hence \(F_2=1+\prod_iF_2(T_i)\).

For \(C_3\), separate the root's image \(2,1,0\). Root image \(2\) gives one map. Root image \(1\) allows, independently on each child, exactly a bounded morphism into the upper two-world generated subchain; each contains \(2\), so the root back condition holds and yields \(\prod_iF_2(T_i)\) maps. Root image \(0\) permits any child-subtree bounded morphisms into \(C_3\), except the unique choice where every child map is constantly \(2\), because the root must have a \(1\)-world descendant. Every other child choice supplies both \(1\) and \(2\), since each valid child map already contains \(2\). This gives \(\prod_iF_3(T_i)-1\) root-zero maps, and the stated sum follows. At a leaf the sole admissible image is the target top. These arguments prove the recurrences for every finite rooted tree without an assumption on branch lengths or degrees.

**Path and minimum.** Iterating the unary-child recurrence gives \(F_2(P_n)=n\) and \(F_3(P_n)=1+\sum_{j=1}^{n-1}j=1+\binom n2\). For a nontrivial rooted star all children are leaves, hence \(F_2=F_3=2\). If the tree is not a rooted star, some child of its root is internal, with its \(F_2,F_3\) counts at least \(2\). The root recurrences then imply \(F_2\ge3\), \(F_3\ge4\). The rooted star is therefore the unique minimizer for both invariants whenever \(n\ge2\).

**Proof of sharp small-order cutoffs.** There are respectively \(1,1,2,4,9,20,48\) rooted tree isomorphism classes in orders \(1,\ldots,7\). The exact maximal pairs \((\max F_2,\max F_3)\) are
\[
 (1,1),(2,2),(3,4),(4,7),(5,11),(7,16),(10,25).
\]
The finite enumeration is exhaustive rather than a sample: each rooted tree is uniquely represented by the sorted multiset of the canonical rooted shapes below its root, and the supplied checker constructs **every** multiset with total order one less than the new root's order. Applying the proved recurrences to this exhaustive list establishes the displayed maxima; the program also independently evaluates the definition of a bounded morphism for every such shape and both targets through order seven. At order six, the sole \(F_2\)-maximizing shape is the root with path branches of orders \(2,3\). At order seven, the sole \(F_3\)-maximizing shape is the root with two path branches of order \(3\). The preceding maxima match the paths, proving the first-failure sharpness assertions.

**Every later order and growth.** The path-branch values are \((F_2,F_3)=(2,2),(3,4),(4,7)\) for path orders \(2,3,4\). Multiplying these values at a new root proves the two explicit families above. For the \(C_2\) family, the base inequalities are \(7>6\) and \(9>7\), and increasing \(k\) by one multiplies \(F_2-1\) by \(2\). Since \(2n-1>n+2\) for \(n\ge4\), induction proves \(F_2>n\) in both residue classes at every \(n\ge6\).

For the \(C_3\) family the three bases are \(25>22\), \(40>29\), and \(65>37\), for \(n=7,8,9\). Increasing \(k\) by one multiplies the first summand by \(4\) and the second by \(3\), so the total at least triples. Writing \(p(n)=1+\binom n2\), we have \(3p(n)-p(n+3)=n^2-4n-1>0\) for all \(n\ge5\). Induction therefore proves the strict inequality for all three residue classes at every \(n\ge7\). Taking identical three-vertex (respectively four-vertex) branches proves the exponential comparisons by the same root formulas. These bounds do not claim to classify the global maximizing tree at every larger order.

## Verification

The accompanying standalone Python checker constructs all canonical unlabeled rooted-tree shapes through order eight; its rooted-isomorphism class counts through order eight are \(1,1,2,4,9,20,48,115\). It computes the recursion for every shape and independently enumerates all vertex functions satisfying the forth/back conditions for each shape through order seven. It asserts the sharp first counterexamples and both infinite explicit-family formulas on a range of parameters. Output ends with `ALL_CHECKS_PASS`. The direct tests are finite corroboration; the root recurrences and subsequent inequalities are proofs for all specified orders.

## Relationship to prior work

The definition and modal significance of bounded morphisms are standard: Goranko and Otto's *Model Theory of Modal Logic* states the forth/back clauses and modal preservation results. Endriss's *Modal Logics of Ordered Trees* studies modal structures based on ordered trees, but its thesis concerns a different semantic system. Rooted-tree optimization appears in Zhang–Zhang–Gray–Wang's work on numbers of graph-theoretic subtrees; that statistic is not the number of bounded frame morphisms.

Related counting work on mappings between finite weak orders, globally surjective morphisms from rooted trees to branching height-three fans, and all maps to the four-world Boolean diamond treats different source–target pairs or different surjectivity assumptions. In particular, the diamond recurrence does not imply the coupled two-/three-chain recurrences or their different first-failure cutoffs. The new assertion is the two-target exact recursion **together with** the sharp path-breakdown thresholds and explicit all-larger-order witnesses, not the classical definition of a bounded morphism or the rooted-tree enumeration method itself.

## Limitations

The theorem treats exactly two- and three-world reflexive chain targets, ancestor-ordered finite rooted trees, and all bounded morphisms. It does not give global maximum counts or maximizer classifications beyond the first-failure orders; it also does not extend the formulas to arbitrary target posets, longer chains, or globally onto maps. Independent review has not been performed. Implicit previous enumeration in specialized modal-frame literature remains an originality risk.

## References

1. O. Esser and R. Hinnion, *Combinatorial Criteria for Ramifiable Ordered Sets*, Mathematical Logic Quarterly 47 (2001), 539–555, first published 3 July 2001, DOI: 10.1002/1521-3870(200111)47:4<539::AID-MALQ539>3.0.CO;2-O.
2. V. Goranko and M. Otto, *Model Theory of Modal Logic*, in *Handbook of Modal Logic* (2007), section 2.2 (bounded morphisms), publicly readable full text: https://www.researchgate.net/publication/286751256_Handbook_of_Modal_Logic_chap.
3. U. Endriss, *Modal Logics of Ordered Trees*, PhD thesis, King's College London (2003), https://staff.science.uva.nl/u.endriss/phd/.
4. X.-M. Zhang, X.-D. Zhang, D. Gray and H. Wang, *Trees with the most subtrees—an algorithmic approach*, Journal of Combinatorics 3 (2012), 207–223, preprint 10 October 2012, arXiv:1210.2871v1.
