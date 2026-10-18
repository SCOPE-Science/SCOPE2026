# Boolean fibers and exact entropy of finite Alexandrov rough observations

## Finding

**Theorem (Boolean-fiber characterization and entropy collapse).** Let \(P\) be a finite nonempty preorder. Give \(P\) the Alexandrov topology of upper sets and, for \(X\subseteq P\), observe the pair
\[
\rho_P(X)=(I_X,C_X),\qquad
I_X=\{x:\uparrow x\subseteq X\},\quad
C_X=\{x:\uparrow x\cap X\ne\varnothing\}.
\]
The following are equivalent:

1. \(P\) is antisymmetric (equivalently, the finite topology is \(T_0\)).
2. **Every nonempty inverse fiber of \(\rho_P\) is a Boolean interval** in \((\mathcal P(P),\subseteq)\).

When these conditions hold, write \(S_x=\{y:x<y\}\) for the strict upper set. For every realized observation \((I,C)\), define
\[
F(I,C)=\{x\in P:S_x\cap C\ne\varnothing\ \text{and}\ S_x\not\subseteq I\}.
\]
There is a uniquely determined set \(D(I,C)\subseteq P\setminus F(I,C)\) such that
\[
\boxed{\rho_P^{-1}(I,C)=\{D(I,C)\cup Z:Z\subseteq F(I,C)\},\qquad |\rho_P^{-1}(I,C)|=2^{|F(I,C)|}.}
\]
One explicit reconstruction is: for every \(x\notin F\), use \(x\in D\iff x\in C\) if \(S_x\cap C=\varnothing\), and otherwise use \(x\in D\iff x\in I\). These rules agree whenever both apply.

If \(X\) is sampled by independent Bernoulli-\(p\) membership decisions, \(0<p<1\), put \(d_x=|S_x|\) and \(h_2(p)=-p\log_2p-(1-p)\log_2(1-p)\). Its rough observation has **exact Shannon entropy**
\[
\boxed{
H(\rho_P(X))=h_2(p)\left[|P|-\sum_{x:d_x\ge1}\bigl(1-p^{d_x}-(1-p)^{d_x}\bigr)\right].
}
\]
In particular, this entropy depends only on the multiset of strict-upper-set sizes, even though the number of distinct observations need not do so. Moreover, conditioned on any observed pair, the coordinates in \(F(I,C)\) remain independent Bernoulli-\(p\) bits; all other coordinates are fixed by that pair.

## Assumptions and scope

A preorder is a reflexive, transitive relation \(\le\), not assumed antisymmetric at the outset. The upper-set topology has smallest open neighborhood \(\uparrow x=\{y:x\le y\}\). The stated pair is its ordinary topological interior and closure; for general preorders, elements equivalent under mutual comparability may have identical neighborhoods. The entropy formula and the displayed Boolean-fiber description require antisymmetry. There is no connectivity, height, width, or distributional restriction beyond finite nonempty \(P\) and, for entropy, independent identically distributed Bernoulli membership.

The term Boolean interval is literal: a set \(\{Y:D\subseteq Y\subseteq D\cup F\}\) in the full subset lattice. It is not merely an abstract lattice isomorphism to a cube.

## Proof

**Step 1: the two successor tests.** Work first with a finite poset. For any \(x\), transitivity gives
\[
S_x\cap C_X\ne\varnothing\iff S_x\cap X\ne\varnothing,
\qquad
S_x\not\subseteq I_X\iff S_x\setminus X\ne\varnothing.
\]
Indeed a strict successor \(y\) in \(C_X\) has some selected \(z\ge y>x\); conversely a selected strict successor belongs to \(C_X\). The second equivalence is dual: a strict successor outside \(I_X\) has an unselected \(z\ge y>x\), and every unselected strict successor is outside \(I_X\). Thus \(x\in F\) precisely when its strict upper set contains **both** a selected and an unselected point.

**Step 2: fixed coordinates.** If \(S_x\cap C_X=\varnothing\), no strict successor belongs to \(X\); therefore \(x\in C_X\iff x\in X\). If instead \(S_x\subseteq I_X\), every strict successor belongs to \(X\), so \(x\in I_X\iff x\in X\). Each point outside \(F\) satisfies at least one of these tests. It follows that two subsets with the same observation agree on \(P\setminus F\), and their common coordinates there give the proposed \(D\). In the case both tests apply (necessarily \(S_x=\varnothing\)), \(I_X\) and \(C_X\) agree at \(x\), so the reconstruction is consistent.

**Step 3: independent freedom.** Fix a representative \(X\) and its free set \(F\). For \(x\in F\), choose a selected strict successor and keep moving upward through selected vertices of \(F\) for as long as possible. Each selected point of \(F\) has a selected strict successor by Step 1. Finiteness terminates the chain at a selected vertex above \(x\) **outside** \(F\). Repeating the argument with unselected vertices gives an unselected strict successor of \(x\) outside \(F\). Consequently every replacement of \(X\cap F\) by an arbitrary \(Z\subseteq F\) leaves both a selected and an unselected strict successor above every \(x\in F\), forcing \(x\notin I\) and \(x\in C\).

For \(x\notin F\), its own membership is unchanged. If all strict successors were unselected, none is in \(F\) (a selected vertex above such a successor would also be above \(x\)); thus they remain unselected. Similarly, if all strict successors were selected, none is in \(F\) and they remain selected. At least one situation applies to each \(x\notin F\). Hence the two approximation indicators at every point remain unchanged. Together with Step 2 this proves the exact Boolean interval and its cardinality.

**Step 4: the converse for finite preorders.** Suppose distinct \(a,b\) satisfy \(a\le b\le a\). Transitivity makes \(\uparrow x\) contain \(a\) exactly when it contains \(b\). It follows that \(\rho_P(\{a\})=\rho_P(\{b\})\): the two upper approximations agree, and both lower approximations are empty (no reflexive upper neighborhood can be contained in either singleton). But \(\rho_P(\varnothing)=(\varnothing,\varnothing)\) differs from their observation. Any Boolean interval containing both singletons must also contain their intersection \(\varnothing\). Therefore this inverse fiber is not a Boolean interval, establishing necessity of \(T_0\).

**Step 5: exact entropy.** For a realized observation, Step 3 gives a Cartesian product fiber: fixed coordinates plus independent unrestricted free coordinates. Under the original independent Bernoulli-\(p\) law, conditioning on this fiber fixes the former and leaves the latter independent Bernoulli-\(p\). Therefore
\[
H(X\mid\rho_P(X))=h_2(p)\,\mathbb E|F(\rho_P(X))|.
\]
For a point with \(d_x\ge1\) strict successors, membership in \(F\) means that those \(d_x\) Bernoulli bits are not all zero and not all one; its probability is \(1-(1-p)^{d_x}-p^{d_x}\). Points with \(d_x=0\) never belong to \(F\). Sum the probabilities, then apply \(H(X)=H(\rho_P(X))+H(X\mid\rho_P(X))=|P|h_2(p)\). This yields the formula without asymptotics or independence assumptions on the overlapping successor sets.


**Sharp separation between entropy and observation count.** On five named points \(a,b,c,d,e\), consider the poset \(P_1\) with \(a,b<c,d\) and isolated \(e\), and the poset \(P_2\) with \(a<c,e\) and \(b<c,d\), with no further strict comparabilities. Both have strict-upper-set size multiset \(\{2,2,0,0,0\}\), hence identical Bernoulli observation entropy for every \(p\). But their numbers of distinct rough observations are \(20\) and \(18\): for a fixed assignment to the three maximal points, each lower point has either two possible observable statuses (if its two maxima agree) or only one (if they differ); summing these products over the eight maximal assignments gives the stated totals. Thus the entropy reduction is genuinely coarser than the complete output census.

## Verification

Run the accompanying standard-library program with `python verify_fibers.py`. It enumerates all distinct transitive upper-triangular posets on up to six points (one fixed topological ordering, which represents every finite poset up to relabeling), all subsets of each poset, and 1,000 additional reproducibly sampled posets on seven through ten points. Independently computed fibers are compared with complete Boolean intervals, and both uniform and Bernoulli-\(1/3\) expected free dimensions are compared with the exact formulas. All finite preorders on up to four points are separately enumerated to test the characterization of the \(T_0\) boundary. The program also exhibits the six-element non-cubical ambiguity fiber of the indiscrete three-point space.

Recorded test output:

```text
POSITIVE_N 1 distinct_topologically_sorted_orders 1
POSITIVE_N 2 distinct_topologically_sorted_orders 2
POSITIVE_N 3 distinct_topologically_sorted_orders 7
POSITIVE_N 4 distinct_topologically_sorted_orders 40
POSITIVE_N 5 distinct_topologically_sorted_orders 357
POSITIVE_N 6 distinct_topologically_sorted_orders 4824
PREORDER_N 1 relations 1 interval_iff_T0=PASS
PREORDER_N 2 relations 4 interval_iff_T0=PASS
PREORDER_N 3 relations 29 interval_iff_T0=PASS
PREORDER_N 4 relations 355 interval_iff_T0=PASS
VERIFY_OK preorders 389 sorted_posets_and_samples 6231 realized_fibers 324180 all_boolean_cubes=PASS uniform_and_biased_entropy=PASS non_T0_boundary=PASS
```

These finite computations verify examples and boundary behavior, but the all-poset result is proved by Steps 1–5, not inferred from enumeration.

## Relationship to prior work

Quasiorder rough sets, their complete distributive lattice of **distinct approximation pairs**, and their Alexandrov interpretation are established in Järvinen, Radeleczki and Veres (2009). Järvinen and Radeleczki (2020/2021) characterize **which approximation pairs are realizable** by quasiorders, using three-valued representations. Their 2023 paper addresses algebraic completions for arbitrary reflexive relations. These are essential foundations, but their inspected statements do not give the inverse-image Boolean-interval characterization, the exact free-coordinate test, or the conditional Shannon-entropy collapse proved here. The present theorem concerns the cardinality and internal geometry of the sets of **representatives of each approximation pair**, not just the lattice of possible pairs.

## Limitations

The explicit cube and entropy formulas are restricted to finite \(T_0\) Alexandrov spaces (finite posets); a preorder with a nontrivial equivalence class need not have cubical fibers. A three-point indiscrete class already has an ambiguity fiber of six elements. Neither the number of realized approximation pairs nor the entire distribution of fiber sizes is asserted to be determined by the strict-upper-degree multiset; only the stated Shannon entropy has that invariance. For non-independent or correlated subset distributions, the conditional-product claim and entropy formula need not hold. No publication-priority or independent external validation is asserted.

## References

1. J. Järvinen, S. Radeleczki and L. Veres, *Rough Sets Determined by Quasiorders*, Order **26** (2009), 337–355; arXiv:0810.0633v2 (full text: https://arxiv.org/html/0810.0633v2).
2. J. Järvinen and S. Radeleczki, *Defining rough sets as core-support pairs of three-valued functions*, first public arXiv posting 2020-11-06, arXiv:2011.03461v1; International Journal of Approximate Reasoning **135** (2021), 71–90 (https://arxiv.org/abs/2011.03461).
3. J. Järvinen and S. Radeleczki, *Pseudo-Kleene algebras determined by rough sets*, arXiv:2304.05641v1 (2023); International Journal of Approximate Reasoning **161** (2023), 108991 (https://arxiv.org/abs/2304.05641).
