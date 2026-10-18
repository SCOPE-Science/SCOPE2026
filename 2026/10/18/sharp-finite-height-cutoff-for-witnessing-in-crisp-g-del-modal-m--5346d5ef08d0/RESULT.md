# Sharp finite-height cutoff for witnessing in crisp Gödel modal models

## Finding
Let \(H\) be a nonnegative integer. For a crisp Gödel–Kripke model with directed accessibility-path height at most \(H\), the following are equivalent: (a) the extrema defining every modal formula are attained at each world with successors (full witnessing); (b) this is so only for modal formulas of nesting depth at most \(H\) (\(H\)-witnessing). The bound is sharp for every positive \(H\): an explicit countable, one-propositional-variable, height-exactly-\(H\) model is \((H-1)\)-witnessed but not \(H\)-witnessed. In the construction there is exactly one infinitely branching world. Moreover, every finitely branching crisp model, and every model in which each atomic proposition has finite global truth-value range, is fully witnessed.

The height restriction is essential for the finite-depth criterion: finite-depth witnessing does not imply unrestricted witnessing over all crisp frames. This is a model-level semantic result, not a statement of completeness for a logic of finite frames.

## Assumptions and scope
Work in the standard propositional Gödel modal language over \([0,1]\), with \(\bot\), \(\wedge\), \(\vee\), \(\to\), \(\Box\), and \(\Diamond\). At each world, \(a\wedge b=\min\{a,b\}\), \(a\vee b=\max\{a,b\}\), and the Gödel implication is \(a\to b=1\) for \(a\le b\) and \(a\to b=b\) otherwise. A crisp accessibility relation \(R\subseteq W\times W\) is used, where \(W\ne\varnothing\) may be infinite. Write \(R[w]=\{v:wRv\}\), and use the usual conventions \(\inf\varnothing=1\), \(\sup\varnothing=0\):

\[
e(w,\Box\varphi)=\inf_{v\in R[w]}e(v,\varphi),\qquad e(w,\Diamond\varphi)=\sup_{v\in R[w]}e(v,\varphi).
\]

A model is **\(h\)-witnessed** (\(h\in\mathbb N_0\)) if for every \(w\) with \(R[w]\ne\varnothing\) and every \(\varphi\) of modal nesting depth \(\operatorname{md}(\varphi)\le h-1\), each of the two displayed extrema equals the value of \(\varphi\) at some successor (possibly a different successor for infimum and supremum). The \(0\)-witnessing condition is vacuous. A model is **fully witnessed** if the same holds with no restriction on modal depth. In the complete crisp semantics, empty-successor worlds are exempt because their extrema have the vacuous default values; in the fuzzy accessibility formulation, any world with accessibility degree zero witnesses those defaults.

A directed \(R\)-path of length \(k\) is a sequence of \(k+1\) worlds joined by \(k\) successive \(R\)-edges, even if vertices repeat. The **path height** is the maximum length of such paths, and is at most \(H\) if no path has length \(H+1\). This notion is deliberately stronger than height of a preorder quotient. It excludes loops, and all successor worlds of a world of remaining height \(h\ge1\) have remaining height at most \(h-1\). The statement includes \(H=0\): then no edges exist and the model is fully witnessed vacuously.

## Proof
**1. Modal-height truncation.** For each \(b\in\mathbb N_0\), define a formula transformation \(T_b\) inductively. It preserves atoms, \(\bot\), and propositional connectives, recursively transforming their arguments with the same index. At index \(0\), replace every subformula \(\Box\alpha\) by \(\top:=\bot\to\bot\) and every \(\Diamond\alpha\) by \(\bot\). At index \(b+1\), set

\[
T_{b+1}(\Box\alpha)=\Box T_b(\alpha),\qquad
T_{b+1}(\Diamond\alpha)=\Diamond T_b(\alpha).
\]

By structural induction, \(\operatorname{md}(T_b(\alpha))\le b\). A simultaneous induction on a formula and the finite remaining height of the evaluated world shows

\[
e(w,\alpha)=e(w,T_b(\alpha))\quad\text{whenever the remaining height of }w\text{ is at most }b.
\]

For the modal step with \(b=0\), the world has no successors, so the two modalities have values \(1\) and \(0\). For \(b>0\), each successor has remaining height at most \(b-1\), and by induction each operand agrees with its \(T_{b-1}\)-transform at every successor. Taking infima and suprema preserves equality. Propositional cases use the truth-functionality of Gödel operations.

Now take a model of height at most \(H\) that is \(H\)-witnessed. Fix an arbitrary formula \(\varphi\) and an arbitrary world \(w\) with successors and remaining height \(h\in\{1,\ldots,H\}\). All successors have remaining height at most \(h-1\), so on every successor \(e(v,\varphi)=e(v,T_{h-1}(\varphi))\). The two desired modal extrema therefore equal those of \(\Box T_{h-1}(\varphi)\) and \(\Diamond T_{h-1}(\varphi)\). Both modal formulas have nesting depth at most \(h\le H\), so the \(H\)-witnessing assumption supplies actual successors attaining each extremum. They also attain the extrema of the original \(\varphi\). Since \(w,\varphi\) were arbitrary, the model is fully witnessed. The converse follows immediately from the definitions.

**2. Sharp countermodels.** Fix \(H\ge1\), and set \(d=H-1\). Construct the model \(\mathfrak M_H\) with worlds

\[
W_H=\{o\}\ \cup\ \{(n,j):n\in\{2,3,\ldots\},\ 0\le j\le d\}.
\]

Let \(oR(n,0)\) for all \(n\ge2\) and \((n,j)R(n,j+1)\) whenever \(j<d\); there are no other edges. Interpret the single distinguished proposition \(p\) by

\[
e((n,d),p)=1/n,\qquad e(w,p)=1\text{ at all other worlds}.
\]

Other propositional letters, if present in the ambient language, are constantly \(1\). The longest paths have \(1+d=H\) edges. The root is the only infinitely branching point, and every non-root world either has exactly one successor or has none. Hence every modal formula is witnessed at every non-root world with successors, regardless of its depth.

For \(d\ge1\), all rooted, atom-valued neighborhoods \((n,0)\) truncated at path-depth \(d-1\) are literally identical (each initial chain position has atomic value \(1\); the first position with value \(1/n\) lies at distance \(d\)). Structural induction on formulas therefore yields

\[
e((n,0),\psi)=e((m,0),\psi)
\quad(\forall n,m\ge2,\ \operatorname{md}(\psi)\le d-1).
\]

This holds for formulas containing either modality and arbitrary Gödel propositional combinations: a modal formula of depth at most \(d-1\) never evaluates an atom at the varying leaf. Thus both extrema at the root are attained for every operand of depth at most \(d-1\), so all modal formulas of depth at most \(d=H-1\) are witnessed there. For \(d=0\) the same conclusion is vacuous. Consequently, \(\mathfrak M_H\) is \((H-1)\)-witnessed.

But the chain below \((n,0)\) is deterministic, so

\[
e((n,0),\Box^{d}p)=1/n.
\]

The convention \(\Box^0p=p\) is used. Therefore the root value of the depth-\(H\) formula \(\Box^{H}p\) is

\[
e(o,\Box^{H}p)=\inf_{n\ge2}(1/n)=0.
\]

No root successor makes its operand \(\Box^{H-1}p\) equal \(0\), since all values \(1/n\) are positive. Hence \(\Box^{H}p\) is not witnessed at the root. This proves sharpness, simultaneously for every positive height \(H\), using one proposition and a countable model.

**3. Additional resource boundaries.** If every world has finitely many successors, every nonempty successor-value set is finite and has an attained minimum and maximum. Thus finitely branching crisp models are fully witnessed.

Suppose instead each propositional letter has finite image across the entire model. Fix a formula \(\theta\), and let \(F\) contain \(0,1\) and all truth values taken by the finitely many letters occurring in \(\theta\). This set is finite. By induction, every subformula of \(\theta\) takes its values in \(F\): the Gödel propositional connectives return either an input value or \(1\), and crisp modal infimum/supremum of a subset of finite \(F\) belongs to \(F\) (with default values \(1,0\)). At any nonempty successor set, both extrema therefore belong to the set of actual successor values and are attained. Since \(\theta\) was arbitrary, the model is fully witnessed. In particular, one atomic variable with infinitely many distinct truth values and an infinitely branching world are both necessary for the sharp counterexample; the construction realizes these resource minima.

## Verification
A standalone checker `witness_depth_check.py` evaluates exact rational Gödel truth values in the finite truncations \(2\le n\le N\), for all \(0\le d\le5\) and \(4\le N\le11\). It checks the exact expression \(e(o,\Box^{d+1}p)=1/N\), the distinct successor values \(1/n\), and \(8{,}000\) generated depth-bounded operand comparisons. The run completed with `WITNESS_DEPTH_FINITE_STRESS_OK shallow_formula_comparisons= 8000`.

These **finite truncated models themselves are fully witnessed**. The program tests formula evaluation and the intended progression only; the infinite nonattainment follows from \(\inf_{n\ge2}1/n=0\) and \(1/n>0\) for each \(n\), and the universally quantified height-cutoff conclusion is proved by structural induction above. No finite experiment is presented as an infinite proof.

## Relationship to prior work
Ferrari, Fiorentini, Giardini, and Rodriguez (2026) introduce full witnessed Gödel-modal semantics and prove calculus completeness and the finite-model property. Their 2025 crisp-model precursor defines the same attained successor extrema for crisp accessibility. Vidal and Rodriguez (2026) study finite-model axiomatizations and partial witnessing in a **different dimension**: \(\Diamond\)-only and top-value witnessing, rather than a nesting-depth cutoff. Its Section 0.2 discusses bounded-depth tree models for local completeness; that observation is related to modal locality but does not state that every height-\(H\) model becomes fully witnessed after checking all modal formulas through depth \(H\), or give the sharp \((H-1)\)-witnessed countermodels at each height.

The present result is a semantic depth-versus-path-height theorem about **individual infinite crisp models**, not a stronger completeness, decidability, or finite-model statement. It restricts to crisp \(R\); the argument is not asserted for general fuzzy accessibility. Its proof uses the standard locality of bounded-depth modal formulas; that familiar principle by itself does not furnish the stated exact witnessing obstruction without the limit-valuation construction.

## Limitations
Originality cannot be conclusively established by indexing searches; an unpublished, unindexed, or differently phrased depth-cutoff statement may exist, particularly within older fuzzy modal semantics or adjacent finite-height modal-logic work. The general model-level result is self-contained; no characterization of fuzzy-accessibility models is claimed. Finite stress tests are evidence of correct formulas, not exhaustive or infinitary certification. No independent audit has been performed.

## References
1. M. Ferrari, C. Fiorentini, P. Giardini, R. O. Rodriguez, *A Gödel Modal Logic Over Witnessed Models* (first public 2026-06-30), arXiv:2606.31906, https://arxiv.org/abs/2606.31906 .
2. M. Ferrari, C. Fiorentini, R. O. Rodriguez, *A Gödel Modal Logic over Witnessed Crisp Models* (TABLEAUX 2025), DOI:10.1007/978-3-032-06085-3_8, https://link.springer.com/chapter/10.1007/978-3-032-06085-3_8 .
3. A. Vidal, R. O. Rodriguez, *Axiomatizing logics of finite Gödel-Kripke models* (first public 2026-05-15), arXiv:2605.15810, https://arxiv.org/abs/2605.15810 .
4. X. Caicedo, R. O. Rodriguez, *Standard Gödel Modal Logics* (2010), Studia Logica, DOI:10.1007/s11225-010-9247-6.
