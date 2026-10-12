# Singleton-frontier law for modal generators on finite weak orders

## Finding
Let \(W=A_1\sqcup\cdots\sqcup A_h\) be a nonempty finite ordinal sum of antichains, with \(n_i=|A_i|\geq1\) and \(xRy\) exactly when \(x=y\) or \(x\in A_i\), \(y\in A_j\), \(i<j\). Endow \(\mathcal P(W)\) with Boolean operations and the S4 possibility operator \(\Diamond U=\{x:\exists y\in U\ (xRy)\}\). Fix \(r\geq0\) ordered propositional generators, equivalently a labeling \(c:W\to\{0,1\}^r\), and write \(q=2^r\).

**Theorem (complete generation, census, depth).** The \(r\) subsets generate all of \(\mathcal P(W)\) if and only if

1. The labels on each \(A_i\) are pairwise distinct; and
2. Whenever \(A_{i+1}\) is a singleton, its sole label does not occur on \(A_i\).

Writing \((a)_{\underline b}=a(a-1)\cdots(a-b+1)\) for \(a\geq b\geq0\), and \((a)_{\underline b}=0\) if \(b>a\geq0\), the number of ordered generating \(r\)-tuples is
\[
N_r(W)=(q)_{\underline{n_h}}\prod_{i=1}^{h-1}
\left(q-\mathbf 1_{\{n_{i+1}=1\}}\right)_{\underline{n_i}}.
\]
The minimum number of propositional generators is
\[
\left\lceil\log_2 Q_*\right\rceil,\qquad
Q_* = \max\left\{n_h,\ \max_{1\leq i<h}\left(n_i+\mathbf 1_{\{n_{i+1}=1\}}\right)\right\}.
\]
For \(h=1\), the inner maximum is omitted. In particular, \(r=0\) is permitted and occurs for a one-point frame. All subsets are definable by modal formulas of depth at most \(h-1\), and this uniform depth bound is sharp for every \(h\geq2\).

For example, two antichain levels of sizes \((2,2)\) have exactly four generating single-proposition valuations. Levels of sizes \((2,1,1)\) admit no generating single-proposition valuation but have exactly twelve generating colorings with a three-letter alphabet (not itself a Boolean-generator alphabet); two propositions, with four colors available, suffice.

## Assumptions and scope
A finite weak order here means an ordinal sum of nonempty antichains; it is an antisymmetric reflexive transitive relation, **not** a total preorder with mutually accessible nontrivial clusters. All worlds in an antichain level have only their own self-loop and access to every world in strictly higher levels. This distinction is essential. No naming constants, graded modalities, converse, or hybrid nominals are used. The theorem concerns **ordered** propositional tuples; a label is the vector of truth values of those tuples. A color alphabet of arbitrary size \(q\) is used only in the intermediate counting statement; actual \(r\)-variable assignments have \(q=2^r\).

## Proof
**Finite modal types.** For a colored finite frame define \(\tau_0(x)=c(x)\) and recursively
\[
\tau_{t+1}(x)=\left(c(x),\{\tau_t(y):xRy\}\right).
\]
Two points satisfy the same formulas of depth at most \(t\) exactly when their \(\tau_t\)-types agree. The forward direction follows by induction on formulas. The converse follows by building a characteristic formula for each finitely occurring type, with one diamond witness for each successor type and a box restriction to their disjunction. The resulting partitions refine monotonically and stabilize on a finite frame. The generated Boolean modal algebra consists exactly of unions of stabilized classes: every term is constant on each class, while the characteristic formulas give each class as a generated element. Thus full generation is equivalent to all stabilized classes being singletons.

**Necessity.** If distinct \(x,y\in A_i\) have the same label, then \(\{(x,y),(y,x)\}\cup\{(z,z):z\in W\}\) is a color-preserving bisimulation: both points see only themselves and the common strict upper suffix. They cannot be separated. If \(A_{i+1}=\{y\}\) and \(x\in A_i\) has \(c(x)=c(y)\), the relation consisting of \((x,y)\) and all identity pairs is a color-preserving bisimulation (in both directions one matches the self-successor \(x\) against \(y\), and the remaining successors identically). Thus the two conditions are necessary.

**Sufficiency.** Work downwards through the levels. Assume every point in the upper suffix \(U_{i+1}=A_{i+1}\cup\cdots\cup A_h\) has a distinct modal type, and thus a characteristic formula isolating it **inside that suffix**. Formula truth at an upper point is unaffected by adding lower points. Distinct points of the new level \(A_i\) have distinct colors. To distinguish \(x\in A_i\) from an upper point \(y\), consider two cases.

If \(|A_{i+1}|\geq2\), choose \(z\in A_{i+1}\) not equal to \(y\) when \(y\in A_{i+1}\) (otherwise choose any \(z\in A_{i+1}\)). The point \(x\) sees \(z\), but \(y\) sees no point of the upper suffix with the modal type of \(z\): all upper types are unique and \(y\) cannot access \(z\). Hence \(\Diamond\chi_z\) separates them. If \(A_{i+1}=\{z\}\), then \(c(x)\ne c(z)\) distinguishes \(x\) from \(z\), while for every \(y\) strictly higher than \(z\), \(\Diamond\chi_z\) separates \(x\) and \(y\). So the larger suffix still has pairwise distinct modal types. The top level starts the induction because its own labels are distinct. This proves sufficiency.

**Census and rank.** Choose the ordered, pairwise distinct labels in the top level in \((q)_{\underline{n_h}}\) ways. At step \(i<h\), if \(n_{i+1}>1\), any \(n_i\) distinct labels are allowed, giving \((q)_{\underline{n_i}}\) choices. If \(n_{i+1}=1\), its single known label is forbidden, giving \((q-1)_{\underline{n_i}}\) choices. The restrictions concern only neighboring levels, so multiplication proves the product. All factors are nonzero exactly when \(q\geq Q_*\); the least power of two satisfying this gives the stated rank.

**Depth bound and sharpness.** The downward argument can be made quantitative. At depth zero, all top-level points have distinct types. If the upper suffix is distinguished by depth \(t\), the witness \(\Diamond\chi_z\) (or a depth-zero color distinction at a singleton frontier) distinguishes every new point from every upper point at depth at most \(t+1\). Thus the entire frame is distinguished by depth \(h-1\). For sharpness at each \(h\geq2\), take \(n_i=2\) for all \(i\) and give each level one point of each of two colors. This valuation meets the criterion. Inductively, for each \(t<h-1\), the same-colored points in the two lowest levels have identical depth-\(t\) types: at each step, their successor sets contain the same depth-\((t-1)\) types because all sufficiently low levels have identical palettes of types. The depth-\((h-1)\) partition is discrete by the upper bound. Hence the bound cannot be improved uniformly.

## Verification
The self-contained `verify.py` uses two distinct finite computations: iterative color-sensitive modal partition refinement and direct closure of subsets under Boolean operations and relational preimage. It independently compares exhaustive accepted-label counts with the product formula, checks the rank threshold in the sampled parameter domain, and checks sharpness of the depth bound on uniform two-point levels. The recorded reproducible output is:

`VERIFY_OK exhaustive_labelings 1178754 parameter_censuses 504 direct_boolean_closures 640 random_cases 5000 sharp_depth_heights 14 max_exhaustive_depth 3 examples {'two_by_two': 4, 'two_one_one_q3': 12, 'two_one_one_q2': 0}`

Run with `python3 verify.py` (Python standard library only). These finite checks corroborate but do not replace the unrestricted induction proof.

## Relationship to prior work
Goldblatt, *Modal Logics that Bound the Circumference of Transitive Frames* (arXiv:1905.11617, first public 2019-05-28), studies finite partial-order frames and the varieties generated by their complex modal algebras; the inspected algebraic section does not give this weak-order generating-tuple product or sharp depth law. Shapirovsky, *Satisfiability problems on sums of Kripke frames* (arXiv:2012.15347, first public 2020-12-30), supplies the general sums-of-frames viewpoint and a modal satisfiability complexity analysis, not a census of generating valuations. Bezhanishvili and Henke (2020) give a general model-theoretic account of modal bisimulation, which underlies the type argument. The type-refinement lemma and the use of finite characteristic formulas are classical, not claimed as new.

The present formula specifically concerns ordinal sums of **antichains with self-loops only**, unlike linear chains of complete S4.3 clusters. For instance, the two-level \((2,2)\) weak-order frame has a generating two-color assignment, whereas the complete-cluster chain with the same two block sizes cannot generate with two colors. A general S4 characterization alone does not supply the explicit adjacent-singleton obstruction or its product census.

## Limitations
The result does not classify arbitrary finite posets or finite preorders with nonsingleton strongly connected clusters. It does not assert that no earlier equivalent observation occurs in older finite modal-algebra, automata, or finite-space literature. The finite tests cover only their enumerated parameter ranges. No independent validation or publication is claimed.

## References
1. R. Goldblatt, *Modal Logics that Bound the Circumference of Transitive Frames*, arXiv:1905.11617 (first public 2019-05-28), https://arxiv.org/abs/1905.11617.
2. I. B. Shapirovsky, *Satisfiability problems on sums of Kripke frames*, arXiv:2012.15347 (first public 2020-12-30), https://arxiv.org/abs/2012.15347.
3. N. Bezhanishvili and T. Henke, *A model-theoretic approach to descriptive general frames: the van Benthem characterization theorem*, *Journal of Logic and Computation* **30** (2020), 1331–1355, https://doi.org/10.1093/logcom/exaa040.
