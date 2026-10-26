# A sharp commutation and defect theorem for finite epistemic probabilities

## Finding

On a finite information partition with world-dependent probability assignments, knowledge of the probability of an event equals the probability of knowing that event **for every event valuation** precisely when the probability rows agree on information-cell masses and jointly realize every product-of-cells deterministic selector. A sharp variational formula computes the greatest possible one-sided discrepancy once cell masses agree. Under probabilities supported on the current information cell, commutation occurs precisely for a permutation matrix of point-mass beliefs, and otherwise the quantitative discrepancy measures failure to cover all point masses.

Formally let \(W\) be finite and nonempty, \(E\) an equivalence relation on \(W\), and \(\mu_v\) a probability measure on \(2^W\) for each \(v\in W\). An event \(P\subseteq W\) is any valuation of one propositional atom. For a cell \(C=[w]_E\), define
\[
F_C(P)=\min_{v\in C}\mu_v(P),\qquad
G_w(P)=\mu_w\left(\bigcup\{D\in W/E:D\subseteq P\}\right).
\]
These are, respectively, the truth degrees of \(K\operatorname{Pr}(p)\) and \(\operatorname{Pr}(Kp)\) at \(w\) in finite probabilistic S5 semantics. Let \(\mathcal P=W/E\).

**Exact commutation criterion.** For any fixed \(w\in C\), \(F_C(P)=G_w(P)\) for every \(P\subseteq W\) if and only if both conditions hold:

1. Every \(v\in C\) has the same probability mass \(\alpha_C(D)=\mu_v(D)\) on every target cell \(D\in\mathcal P\).
2. Write \(\mathcal D_C=\{D\in\mathcal P:|D|\ge2,\ \alpha_C(D)>0\}\). For every choice \(s(D)\in D\) of a point of each \(D\in\mathcal D_C\), some \(v\in C\) satisfies \(\mu_v(\{s(D)\})=\alpha_C(D)\) simultaneously for all those \(D\).

The criterion is independent of which \(w\in C\) is selected. It implies the sharp number-of-worlds obstruction
\[
|C|\ \ge\ \prod_{D\in\mathcal D_C}|D|.
\]
Conversely, this lower bound is sufficient to realize every prescribed probability vector \((\alpha_C(D))_{D\in\mathcal P}\) with nonnegative entries summing to \(1\), using probability rows on \(C\). An empty product is \(1\).

**Sharp discrepancy.** Assume the first, cell-mass agreement condition. Define
\[
\Delta_C=\max_{P\subseteq W}\big(F_C(P)-G_w(P)\big),\qquad
A_C=\sum_{D\in\mathcal D_C}\alpha_C(D).
\]
Then \(\Delta_C\) is independent of \(w\in C\), is nonnegative, and is exactly
\[
\boxed{\Delta_C=A_C-\min_{s\in\prod_{D\in\mathcal D_C}D}\ \max_{v\in C}\sum_{D\in\mathcal D_C}\mu_v(\{s(D)\}).}
\]
The maximum is attained by an event excluding exactly one selected point from every \(D\in\mathcal D_C\), and including every other point of \(W\). If \(\mathcal D_C=\varnothing\), then \(\Delta_C=0\).

**Epistemically supported specialization.** Suppose \(\mu_v(C)=1\) for all \(v\in C\), with \(|C|=d\). For \(d\ge2\),
\[
\boxed{\Delta_C=1-\min_{x\in C}\max_{v\in C}\mu_v(\{x\}).}
\]
Universal commutation holds if and only if the \(d\)-by-\(d\) stochastic matrix \((\mu_v(\{x\}))_{v,x\in C}\) is a permutation matrix. If, in addition, the rows are all equal to a common probability law \(\pi\), then
\[
\Delta_C=1-\min_{x\in C}\pi(\{x\})\ \ge\ 1-\frac1d,
\]
with equality exactly for the uniform law. At \(d=1\), universal commutation and \(\Delta_C=0\) hold automatically.

## Assumptions and scope

The world set is finite, probabilities are ordinary nonnegative finitely additive normalized measures on all subsets, and the epistemic relation is an equivalence relation. There is no assumption of epistemic support or introspective agreement of probability distributions in the general theorem. The result concerns the two stated degrees under all Boolean event valuations; it does **not** assert interchangeability of the two operators under arbitrary syntactic contexts, action modalities, infinite worlds, or arbitrary many-valued event predicates. Each agent can be analyzed independently when several agents are present.

## Proof

Fix \(C\). For any cell \(D\in\mathcal P\), take \(P=D\), which is a union of cells. Then \(KP\) is true exactly on \(D\), so the assumed universal equality at \(w\) gives \(\mu_w(D)=\min_{v\in C}\mu_v(D)\). Now take \(P=W\setminus D\): universal equality gives \(1-\mu_w(D)=\min_{v\in C}(1-\mu_v(D))=1-\max_{v\in C}\mu_v(D)\). Thus the minimum and maximum of the \(D\)-masses coincide and all rows in \(C\) have the same \(D\)-mass \(\alpha_C(D)\). This proves condition 1 without assuming it.

For each selector \(s\in\prod_{D\in\mathcal D_C}D\), set \(P_s=W\setminus\{s(D):D\in\mathcal D_C\}\). The cells fully contained in \(P_s\) are precisely the cells outside \(\mathcal D_C\). Since cell masses are constant, \(G_w(P_s)=1-A_C\). Meanwhile
\[
F_C(P_s)=1-\max_{v\in C}\sum_{D\in\mathcal D_C}\mu_v(\{s(D)\}).
\]
Equality implies this finite maximum equals \(A_C\). Each summand is bounded above by \(\alpha_C(D)\), so a maximizing row simultaneously attains all these bounds; in particular its restriction to each selected target cell is the point mass of size \(\alpha_C(D)\) at \(s(D)\). This is condition 2.

Conversely, suppose both conditions. Given any \(P\subseteq W\), classify target cells into those fully inside \(P\), fully outside, and partially intersected. Constant cell totals give the universal lower bound
\[
\mu_v(P)\ge\sum_{D\subseteq P}\alpha_C(D)
\]
for every \(v\in C\). For each partially intersected cell having positive mass choose \(s(D)\in D\setminus P\), and choose arbitrary selectors in the other cells of \(\mathcal D_C\). Condition 2 produces a row placing the entire mass of each partially intersected positive cell outside \(P\); zero-mass cells contribute nothing. That row attains the lower bound. Hence \(F_C(P)=\sum_{D\subseteq P}\alpha_C(D)=G_w(P)\) for all \(w\in C\) and all \(P\).

Different selectors cannot be realized by the same row: each positive-mass nonsingleton cell requires its row to be concentrated at the chosen point. Thus \(|C|\ge\prod_D|D|\). For sharpness enumerate every selector and assign its corresponding product-of-cell point-mass row to a distinct source world in \(C\); on singleton cells assign the prescribed mass to the only point. If additional worlds are available, repeat an existing row. All rows have the prescribed cell totals, and all selectors occur.

For the defect formula, condition 1 implies
\[
F_C(P)-G_w(P)=\min_{v\in C}\sum_{D:\,\varnothing\ne P\cap D\ne D}\mu_v(P\cap D)\ge0.
\]
The preceding calculation of \(P_s\) yields the lower bound \(\Delta_C\ge A_C-\min_s\max_v\sum_D\mu_v(\{s(D)\})\). For the reverse bound, fix arbitrary \(P\). For each partially intersected positive-mass cell \(D\) choose one \(s(D)\in D\setminus P\), and extend these choices to all of \(\mathcal D_C\). Calling the partially intersected positive cells \(U\), for every row
\[
\sum_{D\in U}\mu_v(P\cap D)\le\sum_{D\in U}\big(\alpha_C(D)-\mu_v(\{s(D)\})\big).
\]
Taking minima over rows, then using \(\sum_{D\notin U}\mu_v(\{s(D)\})\le\sum_{D\notin U}\alpha_C(D)\), gives
\[
F_C(P)-G_w(P)\le A_C-\max_{v\in C}\sum_{D\in\mathcal D_C}\mu_v(\{s(D)\})
\le A_C-\min_t\max_{v\in C}\sum_{D\in\mathcal D_C}\mu_v(\{t(D)\}).
\]
This proves exactness and attainment.

Under epistemic support, the only positive-mass target cell for \(C\) is \(C\). If \(d\ge2\) then \(A_C=1\), and the one-cell formula yields the displayed defect. The qualitative condition says that the \(d\) probability rows must contain all \(d\) point masses. With exactly \(d\) rows, this is equivalent to being a permutation matrix. For a common row \(\pi\), the defect is \(1-\min_x\pi(x)\), and \(\min_x\pi(x)\le 1/d\), with equality if and only if every mass equals \(1/d\). The singleton case follows directly.

## Verification

The accompanying `checker.py` uses integer numerators with a common positive denominator and no floating-point comparisons. It exhaustively checked the criterion and quantitative defect on all equivalence partitions and all matrices of normalized nonnegative two-unit integer rows for \(|W|=1,2,3\), and checked three representative partitions on \(|W|=4\) for every such matrix. This comprises 31,099 combinations of partition and matrix. It recomputes both modal values for every subset, the selector criterion, and the alleged exact defect from independent formulas; it reports `ALL_CHECKS_OK`. The finite computation checks finitely many rational test instances and is not the proof for arbitrary finite sizes or real probabilities.

Run with Python 3: `python checker.py`.

## Relationship to prior work

Kozhemiachenko and Sedlár (arXiv:2604.22459v1, 24 April 2026) define probabilistic S5 models with world-dependent subjective measures, explicitly distinguish probabilistic event formulas such as \(\operatorname{Pr}_A(K_Ap)\) from epistemic minima such as \(K_A\operatorname{Pr}_A(p)\), and investigate expressivity and satisfiability complexity. Their Sections 2–5 and related-work discussion were inspected for the present universal equality or sharp defect, neither of which is stated there. Their earlier work (arXiv:2511.22389) already develops many-valued modal probability operators and is background for the finite event semantics; it studies complexity, not this structural criterion. The routine observation that a minimum of probabilities need not equal the probability of an information-cell interior is not claimed as new. The contribution proposed here is the exact all-valuation rectangular vertex-covering equivalence, its sharp cell-size obstruction, and the attained quantitative discrepancy formula, including the supported S5 permutation/stability consequences. The result may overlap with older lower-envelope representation theory under a different terminology; no exhaustive priority claim is made.

## Limitations

Independently verified priority has not been established. Finite cardinality, availability of all event subsets, and S5 equivalence are essential for the stated proof. The unrestricted one-sided defect formula requires cell-total agreement; without it the two values may be ordered either way, and the stated nonnegative gap formula must not be applied. The lower cell-size bound is a structural obstruction, not a bound for infinite probability spaces. No broader logical equivalence, machine-checked infinite proof or independent mathematical audit is claimed.

## References

1. D. Kozhemiachenko and I. Sedlár, *Reasoning About Probabilities, Actions, and Knowledge in Fuzzy Modal Logic*, arXiv:2604.22459v1, 24 April 2026. https://arxiv.org/abs/2604.22459
2. D. Kozhemiachenko and I. Sedlár, *Complexity of Łukasiewicz Modal Probabilistic Logics*, arXiv:2511.22389, first publicly available 27 November 2025; also EPTCS 437 (2025), pp. 350–364. https://arxiv.org/abs/2511.22389
3. R. Fagin and J. Y. Halpern, *Reasoning About Knowledge and Probability*, Journal of the ACM 41 (1994), pp. 340–367; relevant background on modal probability structures, not independently re-verified as a comparison for the exact selector criterion.
