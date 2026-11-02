# Tail-mass criterion for almost-sure witnessing on infinite Gödel-modal stars

## Finding

Fix a countable bimodal Gödel language whose formulas are constructed from propositional variables \(p_1,p_2,\ldots\), the constant \(\bot\), binary connectives \(\wedge,\vee,\to\), and modalities \(\Box,\Diamond\). Let \(\mu\) be a Borel probability measure on \((0,1]\) with
\[
\mu((0,\varepsilon))>0\qquad (0<\varepsilon\le1),
\]
and define its **lower tail** by \(h(t)=\mu((0,t))\).

**Theorem (sharp zero-one witnessing threshold).** Consider the countably infinite weighted star
\[
W=\{o\}\cup\{u_n:n\ge1\},\qquad
R(o,u_n)=r_n\in(0,1],
\]
with \(R(w,v)=0\) for all other ordered pairs. For each variable \(p_j\) and each leaf \(u_n\), choose \(e(u_n,p_j)\) independently with distribution \(\mu\); the values at the root are arbitrary and may be deterministic. Then
\[
\Pr(\text{every modal occurrence at every world is witnessed})=
\begin{cases}
1,&\displaystyle\sum_{n=1}^{\infty}h(r_n)<\infty,\\
0,&\displaystyle\sum_{n=1}^{\infty}h(r_n)=\infty.
\end{cases}
\]
In the divergent case, a single fixed variable \(p\) suffices: the infimum interpreting \(\Box p\) at \(o\) is almost surely \(0\) and is not achieved by any world. When \(\mu\) is the uniform distribution on \((0,1)\), the exact criterion is \(\sum_n r_n<\infty\).

The theorem concerns the exact probability of **simultaneous** witnessing for every formula in the full countable language, not merely pointwise witnessing of a prescribed finite family of formulas.

## Assumptions and scope

Gödel truth operations on \([0,1]\) are \(a\wedge b=\min(a,b)\), \(a\vee b=\max(a,b)\), and
\[
a\to b=\begin{cases}1,&a\le b,\\b,&a>b.\end{cases}
\]
The modal operations at a world \(w\) are
\[
e(w,\Box\psi)=\inf_{v\in W}\bigl(R(w,v)\to e(v,\psi)\bigr),\quad
e(w,\Diamond\psi)=\sup_{v\in W}\min\{R(w,v),e(v,\psi)\}.
\]
A modal operation is **witnessed at \(w\)** if its indicated infimum/supremum is realized by some \(v\in W\). A model is witnessed if this holds for every modal formula and every world. This is the fuzzy-accessibility definition used in the motivating paper. It does not demand a positive-weight successor when the extremum is attained at an inaccessible world. In particular, every modal operation at each leaf is witnessed because its entire accessibility row is zero.

The infinite sequence \((r_n)\) is deterministic and strictly positive. The independent random choices concern leaf values for every variable, with the same law \(\mu\). The positivity-near-zero condition rules out distributions with a strictly positive minimum possible truth degree; the law need not have a density or be atomless. The root values have no effect on the witnessing test because \(R(o,o)=0\).

## Proof

**Step 1 — selector lemma.** At any leaf \(u_n\), every modal subformula \(\Box\theta\) has value \(1\), and every \(\Diamond\theta\) has value \(0\): all its accessibility weights vanish. For a fixed formula \(\psi\), write \(V(\psi)\) for its finite set of variables. By structural induction,
\[
e(u_n,\psi)\in\{0,1\}\cup\{e(u_n,p):p\in V(\psi)\}.
\tag{1}
\]
Indeed, the atomic and modal cases are immediate. The operations \(\min\) and \(\max\) select one of their inputs, and Gödel implication selects either \(1\) or its consequent. Therefore all connectives preserve (1). In particular, with \(m=|V(\psi)|\),
\[
\Pr\bigl(0<e(u_n,\psi)<r_n\bigr)\le m h(r_n).
\tag{2}
\]
The union bound in (2) does not require any independence between the variables selected by the value of \(\psi\).

**Step 2 — summable case.** Suppose \(\sum_n h(r_n)<\infty\). First, \(r_n\to0\): otherwise some \(\varepsilon>0\) satisfies \(r_n\ge\varepsilon\) for infinitely many \(n\), contradicting convergence since \(h(r_n)\ge h(\varepsilon)>0\).

For each fixed \(\psi\), inequality (2) and the first Borel–Cantelli lemma imply that almost surely only finitely many indices satisfy \(0<e(u_n,\psi)<r_n\). Because there are only countably many formulas, with probability one this is true **simultaneously for every** \(\psi\). Work on this probability-one event.

To check \(\Box\psi\) at the root, put \(b_n=r_n\to e(u_n,\psi)\), where the displayed arrow is Gödel implication. If any \(e(u_n,\psi)=0\), then \(b_n=0\), since \(r_n>0\); thus the infimum is \(0\) and is attained. Otherwise every \(e(u_n,\psi)>0\), and all except finitely many \(b_n=1\), because \(b_n<1\) occurs precisely when \(0<e(u_n,\psi)<r_n\). Hence the infimum over \(\{1,b_1,b_2,\ldots\}\) is the minimum of a finite nonempty set and is attained. The additional \(1\) comes from the root itself, where \(R(o,o)=0\).

To check \(\Diamond\psi\), set \(d_n=\min\{r_n,e(u_n,\psi)\}\). Since \(0\le d_n\le r_n\to0\), the supremum of \(\{0,d_1,d_2,\ldots\}\) is achieved: if it is positive, only finitely many \(d_n\) exceed half its value; if it is zero, it is already achieved at the root. At every leaf both modal extrema are trivially achieved. Thus the entire model is witnessed for **all** formulas on one probability-one event.

**Step 3 — divergent case.** Suppose \(\sum_n h(r_n)=\infty\). Fix any variable \(p\), and let \(U_n=e(u_n,p)\). Then \(U_n>0\) for every \(n\) almost surely, because \(\mu\) is supported on \((0,1]\). For each integer \(k\ge2\) consider independent events
\[
A_{n,k}=\{0<U_n<\min(r_n,1/k)\},\qquad
\Pr(A_{n,k})=h(\min(r_n,1/k)).
\]
For each \(k\),
\[
\sum_n h(\min(r_n,1/k))=\infty.
\tag{3}
\]
If infinitely many \(r_n\ge1/k\), (3) follows from \(h(1/k)>0\). Otherwise (3) follows from divergence of the tail \(\sum_nh(r_n)\). The second Borel–Cantelli lemma shows that for every fixed \(k\), infinitely many \(A_{n,k}\) occur almost surely; intersect these countably many probability-one events. At each such index, \(r_n\to U_n=U_n<1/k\). Consequently,
\[
e(o,\Box p)=\inf\bigl(\{1\}\cup\{r_n\to U_n:n\ge1\}\bigr)=0
\]
almost surely. Nevertheless all terms are strictly positive: \(U_n>0\) and \(r_n\to U_n\in\{1,U_n\}\), while \(R(o,o)\to e(o,p)=1\). The infimum \(0\) is therefore not attained. A witnessed model would have to witness \(\Box p\); hence the probability of a witnessed model is zero. This proves both directions.

**Quantitative refinement.** For each fixed \(\psi\) with \(m\) distinct variables, the same selector lemma gives the explicit tail bound
\[
\Pr\bigl(\exists n\ge N:\ 0<e(u_n,\psi)<r_n\bigr)
\le m\sum_{n\ge N}h(r_n).
\]
Thus the positive half is not merely existential: it controls the chance of late exceptional necessity values.

## Verification

The argument is exact and does not use finite simulation as an infinite-model proof. Its nonstandard point is the selector induction (1) for arbitrary nested Gödel-modal formulas on zero-outgoing-weight leaves. Formula (2) follows by a union bound; both directions then use standard Borel–Cantelli lemmas with independence invoked only for a single fixed variable in the divergent direction. The threshold comparison (3), the implication boundary \(a=b\) (yielding \(1\)), zero accessibility at leaves, and simultaneous countable intersection are explicitly accounted for. The conclusions remain true when \(\mu\) is discrete with atoms away from \(0\).

For example, with uniform truth degrees, \(r_n=1/n\) yields probability zero, while \(r_n=1/n^2\) yields probability one. Although the latter star has infinitely many positive-weight successors, it is almost surely witnessed; this does not imply witnessing for every possible valuation.

## Relationship to prior work

Ferrari, Fiorentini, Giardini and Rodriguez introduce fuzzy-accessibility witnessed Gödel models and study proof search, decidability and finite-model properties, including nonattained extrema on infinite models. Their paper supplies the exact semantic definition and examples motivating the present question, but its argument does not classify random valuations on a fixed infinite frame, nor produce an accessibility-tail criterion. Ferrari, Fiorentini and Rodriguez previously studied **crisp** witnessed Gödel models and a cut-free calculus; crisp frame weights cannot exhibit the same graded tail-mass dependence. Goranko and Kapron study almost-sure **frame validity** for classical random Kripke frames, not almost-sure **modal-extremum attainment** under independent real-valued valuations on deterministic weighted frames. The elementary Borel–Cantelli theorems are standard prior tools, not claimed as original.

The claim of originality is confined to the explicit universal-formula random-valuation threshold on this infinite fuzzy Gödel-modal star (and its lower-tail generalization). Neither the paper's completeness theorem nor a generic modal logic zero-one law is re-proved here.

## Limitations

The result is specific to zero-outdegree leaves and independent, identically distributed atomic values supported in \((0,1]\) with positive mass below every positive threshold. Without these assumptions a different threshold can arise. The theorem does not classify arbitrary infinite Gödel frames, correlated valuations, almost-sure validity of logical formulas, or the complexity of a proof system. The historical search cannot rule out an equivalent result under older stochastic fuzzy-semantics terminology; independent priority assessment remains appropriate.

## References

1. M. Ferrari, C. Fiorentini, P. Giardini and R. O. Rodriguez, *A Gödel Modal Logic Over Witnessed Models*, EPTCS 447 (2026), 355–373, doi:10.4204/EPTCS.447.20; first arXiv posting 2026-06-30, https://arxiv.org/abs/2606.31906.
2. M. Ferrari, C. Fiorentini and R. O. Rodriguez, *A Gödel Modal Logic over Witnessed Crisp Models*, TABLEAUX 2025, pp. 141–160, first online 2025-09-25, doi:10.1007/978-3-032-06085-3_8, https://link.springer.com/chapter/10.1007/978-3-032-06085-3_8.
3. V. Goranko and B. Kapron, *The modal logic of the countable random frame*, Archive for Mathematical Logic 42 (2003), 221–243, doi:10.1007/s001530100135.
4. É. Borel and F. Cantelli, the classical first and second Borel–Cantelli lemmas (standard probability results used in the proof).
