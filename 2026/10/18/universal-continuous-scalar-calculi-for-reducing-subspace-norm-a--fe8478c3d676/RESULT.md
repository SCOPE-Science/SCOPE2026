# Universal continuous scalar calculi for reducing-subspace norm and minimum attainment

## Finding

Fix \(R>0\) and an infinite-dimensional separable complex Hilbert space \(H\). Let \(f:[0,R]\to[0,\infty)\) be continuous. Write \(\mathcal B_+(H)\) for positive bounded operators whose restriction to **every nonzero closed reducing subspace** attains its norm, and \(\mathcal M_+(H)\) for positive bounded operators whose restriction to every nonzero closed reducing subspace attains its minimum modulus. All universal statements below quantify over **every** positive operator \(A\) with \(0\le A\le RI\).

**Preservation and exchange:** Each of the two implications
\[
A\in\mathcal B_+(H)\Longrightarrow f(A)\in\mathcal B_+(H),\qquad
A\in\mathcal M_+(H)\Longrightarrow f(A)\in\mathcal M_+(H)
\]
holds universally **if and only if** \(f\) is nondecreasing on \([0,R]\). Each of the two implications
\[
A\in\mathcal B_+(H)\Longrightarrow f(A)\in\mathcal M_+(H),\qquad
A\in\mathcal M_+(H)\Longrightarrow f(A)\in\mathcal B_+(H)
\]
holds universally **if and only if** \(f\) is nonincreasing on \([0,R]\).

**Two-sided reflection:** Each of the two equivalences
\[
A\in\mathcal B_+(H)\iff f(A)\in\mathcal B_+(H),\qquad
A\in\mathcal M_+(H)\iff f(A)\in\mathcal M_+(H)
\]
holds universally **if and only if** \(f\) is strictly increasing. Each of
\[
A\in\mathcal B_+(H)\iff f(A)\in\mathcal M_+(H),\qquad
A\in\mathcal M_+(H)\iff f(A)\in\mathcal B_+(H)
\]
holds universally **if and only if** \(f\) is strictly decreasing. These eight characterizations are simultaneous, with all counterexamples realized by positive diagonal operators on \(\ell_2(\mathbb N)\).

## Assumptions and scope

The norm of an operator restriction is its ordinary Hilbert-space operator norm. The minimum modulus of a restriction \(B\) is \(m(B)=\inf_{\|x\|=1}\|Bx\|\); minimum attainment requires that a unit vector attain this infimum. The zero operator belongs to both classes. The continuous functional calculus gives a positive bounded \(f(A)\), and its reducing subspaces are considered independently from the reducing subspaces of \(A\). The space \(H\) is infinite dimensional throughout. Fixed \(R>0\) is arbitrary; varying \(R\) gives the analogous global characterization for continuous nonnegative functions on the half-line.

## Proof

**1. Spectral criterion.** For positive bounded \(A\), the structural theorem of Golla–Osaka–Sequeira [1, Theorem 2.2] states that \(A\in\mathcal B_+(H)\) precisely when \(A\) has a complete orthogonal eigenvector decomposition and its set of distinct eigenvalues contains no infinite strictly increasing sequence. Their Corollary 2.17 [1] states that \(A\in\mathcal M_+(H)\) precisely when it has a complete orthogonal eigenvector decomposition and its distinct eigenvalues contain no infinite strictly decreasing sequence. In particular, no unlisted accumulation point is silently taken to be an eigenvalue.

**2. Sufficiency.** If \(A\) belongs to either class, \(H\) has an orthonormal basis of eigenvectors of \(A\); the same vectors form a complete eigenvector basis for \(f(A)\). Its eigenvalue set is the image under \(f\) of the eigenvalue set of \(A\), possibly with collisions. If \(f\) is nondecreasing, an increasing sequence of distinct image values would have increasing preimages, and a decreasing sequence of distinct image values would have decreasing preimages. Thus both spectral well-ordering directions are preserved. If \(f\) is nonincreasing, the two ordering directions are exchanged. This proves all four forward implications.

If \(f\) is strictly monotone, its inverse \(g\) on the compact interval \(f([0,R])\) is continuous and has the same monotonicity orientation as \(f\). Functional calculus gives \(g(f(A))=A\). Applying the already proved forward implication to \(g\) establishes the four indicated reverse implications and hence the sufficiency of strict monotonicity for each equivalence.

**3. A crossing lemma.** Let \(h\) be continuous on \([a,b]\) with \(a<b\). Suppose first \(h(a)>h(b)\). Choose \(\ell\) strictly between these two values and set
\[
c=\inf\{t\in[a,b]:h(t)<\ell\},\qquad
d=\sup\{t\in[a,b]:h(t)>\ell\}.
\]
Continuity gives \(a<c\le b\), \(a\le d<b\), \(h(c)=h(d)=\ell\), points immediately to the right of \(c\) have values strictly below \(\ell\), and points immediately to the left of \(d\) have values strictly above \(\ell\). Consequently, one can choose a strictly decreasing sequence \(x_n\downarrow c\) with \(h(x_n)\uparrow\ell\) strictly and a strictly increasing sequence \(y_n\uparrow d\) with \(h(y_n)\downarrow\ell\) strictly. To ensure strict image monotonicity, first choose points approaching the respective boundary through the relevant strict sublevel/superlevel sets; continuity makes their images tend to \(\ell\) on one side, and a successive subsequence selection makes the images strictly monotone. All selected points lie in \([a,b]\).

If instead \(h(a)<h(b)\), the same construction with \(<\) and \(>\) interchanged yields \(x_n\downarrow c\) with \(h(x_n)\downarrow\ell\) strictly and \(y_n\uparrow d\) with \(h(y_n)\uparrow\ell\) strictly.

**4. Necessity of weak monotonicity.** For every strictly decreasing bounded positive sequence \((u_n)\), the positive diagonal operator \(\operatorname{diag}(u_n)\) belongs to \(\mathcal B_+(\ell_2)\): all its eigenvalue subsets possess a greatest element. If the sequence is strictly increasing, the diagonal operator belongs to \(\mathcal M_+(\ell_2)\). Conversely, a strictly increasing sequence whose supremum is not attained produces a diagonal operator outside \(\mathcal B_+\), while a strictly decreasing sequence whose infimum is not attained produces one outside \(\mathcal M_+\).

If \(f\) is not nondecreasing, there are \(a<b\) with \(f(a)>f(b)\). Apply step 3 with \(h=f\). The operator \(A=\operatorname{diag}(x_n)\) belongs to \(\mathcal B_+\), but \(f(A)\) has strictly increasing diagonal eigenvalues converging to an unattained maximum \(\ell\); thus \(f(A)\notin\mathcal B_+\). Independently, \(A=\operatorname{diag}(y_n)\) belongs to \(\mathcal M_+\), but \(f(A)\) has strictly decreasing eigenvalues converging to an unattained minimum, so \(f(A)\notin\mathcal M_+\). Hence either universal same-class implication forces \(f\) to be nondecreasing.

If \(f\) is not nonincreasing, select \(a<b\) with \(f(a)<f(b)\). The second half of step 3 gives a decreasing diagonal \(A=\operatorname{diag}(x_n)\) in \(\mathcal B_+\) whose image has an unattained minimum, and an increasing diagonal \(A=\operatorname{diag}(y_n)\) in \(\mathcal M_+\) whose image has an unattained maximum. Thus either universal exchange implication forces \(f\) to be nonincreasing.

**5. Necessity of strictness for reflection.** A nondecreasing or nonincreasing continuous function that is not strictly monotone is constant on a nondegenerate interval \([a,b]\subseteq[0,R]\). Choose a strictly increasing sequence \(u_n\uparrow b\) with every \(u_n\in(a,b)\). Then \(A=\operatorname{diag}(u_n)\notin\mathcal B_+\), whereas \(f(A)\) is a scalar operator belonging to both classes. Similarly, choose a strictly decreasing sequence \(v_n\downarrow a\) with every \(v_n\in(a,b)\). Then \(A=\operatorname{diag}(v_n)\notin\mathcal M_+\), although \(f(A)\) belongs to both classes. Weak-monotonicity necessity from step 4 excludes nonmonotone functions from the equivalences. Thus each of the four universal reflection statements requires the specified strict orientation. Together with step 2, the proof is complete. \(\square\)

## Verification

Every counterexample in steps 4–5 is an explicitly bounded positive diagonal operator on the fixed Hilbert space \(\ell_2(\mathbb N)\), not a finite-dimensional surrogate. For a concrete orientation check on \([0,1]\), \(f(t)=t\) meets all same-class equivalences; \(f(t)=1-t\) meets all exchange equivalences; \(f(t)=1/2\) meets every one-way implication but no two-sided equivalence. The crossing construction supplies an obstruction for any failure of weak monotonicity, including nonsmooth and non-piecewise-monotone continuous functions. No numerical approximation, empirical count, or external computation is used as an infinite-dimensional proof.

## Relationship to prior work

Golla–Osaka–Sequeira [1] prove the exact pure-point reverse-well-order characterization of positive \(\beta(H)\), its increasing-order counterpart for \(\mathcal M_r(H)\), and the particular affine duality \(A\mapsto \delta I-A\). These are the **premises**, not new claims here. This theorem classifies *every continuous scalar function* that universally preserves or exchanges these two classes, and separately characterizes universal two-sided reflection; the converse obstructions are explicit and work even when \(f\) has no monotone subinterval. Su–Zhang [2] study density and perturbation stability of the norm-attainment class rather than a universal scalar-calculus classification. Ramesh–Osaka–Udagawa–Yamazaki [3] investigate continuous functional calculus for the smaller class of absolutely norm-attaining operators \(\mathcal{AN}\), which does not by itself supply the universal assertions about \(\beta(H)\) and \(\mathcal M_r(H)\). The full material for [3] was not inspected; this is a residual historical-priority uncertainty, not a claimed proof of novelty from absence.

## Limitations

The assertions concern positive bounded operators on infinite-dimensional separable complex Hilbert spaces and continuous nonnegative scalar functions on a compact spectral interval. The theorem makes no claim about discontinuous Borel maps, nonpositive normal calculi, nonnormal operators, or a corresponding characterization for the stronger absolutely norm-attaining class. The specified spectral criteria from [1] are assumed as published input and their original priority is fully retained. The possibility of an earlier equivalent universal scalar-calculus classification in terminology not inspected remains open to independent literature review.

## References

1. Ramesh Golla, Hiroyuki Osaka, Shanola S. Sequeira, *Quasinormal and hyponormal operators in the \(\beta(H)\)-class*, arXiv:2610.13490v1 (first public October 9, 2026), Theorem 2.2, Corollary 2.17, Proposition 2.18. https://arxiv.org/html/2610.13490v1
2. Zinan Su and Yuanhang Zhang, *The Stability and Density of Norm Attaining Operators on Reducing Subspaces*, arXiv:2609.37621v2 (2026). https://arxiv.org/html/2609.37621v2
3. G. Ramesh, H. Osaka, Y. Udagawa and T. Yamazaki, *Stability of \(\mathcal{AN}\)-Operators under Functional Calculus*, Analysis Mathematica **49** (2023), 825–839, DOI:10.1007/s10476-023-0231-5. https://doi.org/10.1007/s10476-023-0231-5
