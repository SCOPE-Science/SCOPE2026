# Noncontingency introspection on finite out-trees: forbidden branches and exact labelled enumeration

## Finding
Let \(T\) be a finite rooted directed tree, with one edge from each parent to each child, no other edges, and no loops. Write \(\Delta\varphi\) for the noncontingency operator: it holds at a vertex when \(\varphi\) has a constant truth value on that vertex's *immediate* children, including the vacuous cases of zero or one child. The following three statements constitute one classification-and-enumeration finding.

1. The schema \(\Delta p\to\Delta\Delta p\) is globally valid under **every** Boolean valuation on \(T\) if and only if no directed edge joins two vertices that each have at least two children.
2. Let \(t_n\) count such rooted out-trees on a fixed \(n\)-element labelled vertex set, with the root free to be any vertex; let \(T(z)=\sum_{n\ge1}t_nz^n/n!\). There is a unique formal power series with zero constant coefficient satisfying
\[
T(z)=z(1+T(z))+z\bigl(e^{z(1+T(z))}-1-z(1+T(z))\bigr).
\]
Its first coefficients give \(t_1,\ldots,t_8=1,2,9,64,565,6036,77749,1176736\). In particular, the first failure occurs on five vertices, where exactly \(60\) of the \(625\) rooted labelled trees fail.
3. The proportion of validating out-trees among all \(n^{n-1}\) rooted labelled trees decays exponentially. More precisely, letting \(\Phi(z,t)=z(1+t)+z\bigl(e^{z(1+t)}-1-z(1+t)\bigr)\), there is a characteristic pair \((\rho,\tau)\), with \(\rho\approx0.446602824618744\), satisfying
\[
\tau=\Phi(\rho,\tau),\qquad \Phi_t(\rho,\tau)=1.
\]
Writing \(c=\sqrt{2\rho\Phi_z(\rho,\tau)/\Phi_{tt}(\rho,\tau)}\approx4.64045184920140\), one has
\[
\frac{t_n}{n^{n-1}}\sim\frac{c}{\sqrt2}\left(\frac{1}{e\rho}\right)^n,
\qquad \frac1{e\rho}\approx0.823728424658966.
\]
The numerical constants are approximations to the explicitly defined real solutions, not independently certified interval enclosures.

## Assumptions and scope
The tree is nonempty, finite, simple, and rooted; it is viewed as the exact outward parent-to-child relation, **not** its reflexive or transitive closure. The truth set of \(p\) may be any subset of the vertices. Empty successor sets make \(\Delta\varphi\) true. The schema is considered at every vertex under every valuation. A labelled rooted tree includes its choice of root; isomorphic label permutations are counted separately. Counts are for \(n\ge1\). All modal semantics are classical Boolean Kripke semantics with \(\Delta\varphi\equiv\Box\varphi\vee\Box\neg\varphi\).

## Proof
**Local characterization.** Let \(\deg^+(v)\) denote the number of children. If every child of a vertex \(v\) has at most one child, then \(\Delta p\) holds at each child for every valuation (indeed any proposition is constant on a set with at most one element); hence \(\Delta\Delta p\) holds at \(v\), regardless of the value of \(\Delta p\) there. Likewise, if \(v\) itself has at most one child, \(\Delta\Delta p\) is automatically true. Thus a tree without an edge between branching vertices validates the schema.

Conversely suppose \(v\) has distinct children \(u,w\) and \(u\) has distinct children \(a,b\). Assign \(p\) the same truth value at **all** children of \(v\) (say false), and opposite truth values at \(a,b\). Make \(p\) constant on all children of \(w\). These prescriptions are compatible: the children of distinct parents in a rooted tree are disjoint, and no grandchild of \(v\) is a child of \(v\). Consequently \(\Delta p\) is true at \(v\), false at \(u\), and true at \(w\). Therefore \(\Delta\Delta p\) is false at \(v\). This proves the converse for all finite out-trees, including those with additional children elsewhere.

**Labelled decomposition.** Define \(\mathcal A\) to be the valid rooted trees whose root has at most one child; \(\mathcal B\) those whose root has at least two children. A root in \(\mathcal A\) has either no child or precisely one child carrying any valid rooted tree, whence \(A(z)=z(1+T(z))\). At a branching root, all child roots must be nonbranching, and each of their subtrees remains valid; the children form an unordered labelled set of at least two \(\mathcal A\)-trees. Hence \(B(z)=z(e^{A(z)}-1-A(z))\). Since \(T=A+B\), the displayed functional equation follows and uniquely defines a formal series recursively by degree. Every tree belongs to exactly one of these cases.

For a coefficient recurrence, let \(a_n=n![z^n]A(z)\) and \(f_n=n![z^n]e^{A(z)}\). Put \(f_0=1\), \(a_1=t_1=1\), and \(a_0=t_0=0\). For \(n\ge1\), the rooted-component-of-label-\(1\) decomposition gives
\[
f_n=\sum_{k=1}^{n}\binom{n-1}{k-1}a_kf_{n-k}.
\]
For \(n\ge2\), \(a_n=nt_{n-1}\) and \(t_n=a_n+n(f_{n-1}-a_{n-1})\). These formulas compute the asserted integers without subtraction ambiguities; \(t_1=1\) separately. The total number of all rooted labelled trees is \(n^{n-1}\) by Cayley's formula and the choice of root.

**Asymptotics.** Write \(T=\Phi(z,T)\). The expansion \(\Phi(z,t)=z(1+t)+z\sum_{k\ge2}z^k(1+t)^k/k!\) has nonnegative coefficients, positive coefficients of every sufficiently high degree, and genuine nonlinearity in \(t\). There is a finite positive radius of convergence because directed rooted paths alone contribute \(n!\) objects on \(n\) labels. Standard positive implicit-function singularity theory applies: its least positive characteristic solution satisfies \(\tau=\Phi(\rho,\tau)\), \(1=\Phi_t(\rho,\tau)\), with \(\Phi_{tt}(\rho,\tau)>0\) and \(\Phi_z(\rho,\tau)>0\). Aperiodicity (a valid path exists for every positive size) yields a single dominant square-root singularity,
\[
T(z)=\tau-c\sqrt{1-z/\rho}+O(1-z/\rho).
\]
Coefficient transfer gives \(t_n\sim c n!\rho^{-n}/(2\sqrt\pi\,n^{3/2})\). By Stirling, \(n^{n-1}\sim n!e^n/(\sqrt{2\pi}\,n^{3/2})\), proving the proportion asymptotic. Eliminating \(\tau\) from the characteristic equations gives the explicit scalar equation
\[
\exp\!\left(1+\rho-\frac{\rho^3}{1-\rho+\rho^2}\right)=\frac{1-\rho+\rho^2}{\rho^2}.
\]
Its characteristic solution is the positive real root near \(0.4466028246\). In particular, \(e\rho>1\), and the proportion decreases exponentially. One elementary check independent of transfer theory is that at \(z=2/5\), \(\Phi(z,1)<1\), so the positive series converges there; this already gives a strictly exponential upper bound for the proportion.

## Verification
The standalone `checker.py` independently constructs every labelled undirected tree by Prüfer codes, orients it from each possible root, and compares the forbidden-edge condition against exhaustive valuation semantics for all rooted trees through six vertices. It compares the structural counts with a separately implemented labelled-set recurrence through seven vertices and also computes the first twelve recurrence values. On replay it reports `ALL_CHECKS_OK`. The proof of the infinite and asymptotic statements rests on the arguments above, not on finite enumeration or floating-point calculations. Replay: `python3 checker.py`.

## Relationship to prior work
Sierra Miranda, Wang and Zenger (arXiv:2609.38975v1, publicly posted 2026-09-30) develop a general labelled-sequent proof theory for noncontingency and generalized path-condition frame classes. Their semantic clause agrees with the one used here, but their principal theorems concern proof calculi and completeness, not enumeration of finite rooted out-trees validating this specific introspection schema. Fan (arXiv:1906.03091v1) studies two *bimodal variants* of noncontingency, expressive power and frame definability. The unary classical operator here is the equal-relations specialization; the finite-tree classification and its labelled species are not among the results inspected there. General frame correspondence and normal-box transitivity results do not themselves imply the stated exact labelled count. Classical labelled-tree methods and the smooth implicit-function schema are used as tools, not claimed as new.

## Limitations
The characterization and counts rely essentially on *immediate* children and the disjoint-subtree property. They do not characterize arbitrary Kripke frames, DAGs with shared successors, reflexive/transitive closures, or modal logics with restricted valuations. The 2015 primary paper of Fan, Wang and van Ditmarsch, *Contingency and Knowing Whether*, could be checked at the citation/abstract level but its relevant full text was not accessible during this comparison; it remains a historical-priority risk. The recent paper's results do not prove absence of older equivalent combinatorial enumeration. Numerical root approximations are not formal interval certificates.

## References
1. B. Sierra Miranda, Y. Wang and L. Zenger, *Proof Theory for Non-Contingency Logic*, arXiv:2609.38975v1 (2026-09-30), https://arxiv.org/html/2609.38975v1.
2. J. Fan, *Two variants of noncontingency operator*, arXiv:1906.03091v1 (2019-06-07), https://arxiv.org/html/1906.03091v1.
3. J. Fan, Y. Wang and H. van Ditmarsch, *Contingency and Knowing Whether*, *Review of Symbolic Logic* 8 (2015), 75–107, DOI:10.1017/S1755020314000343 (abstract/catalogue inspected; full text not assessed).
4. P. Flajolet and R. Sedgewick, *Analytic Combinatorics*, Cambridge University Press (2009), positive implicit-function schema and singularity transfer (standard method).
