# Exact modal-depth growth for unary valuations on the natural-number order

## Finding
Let \(F=(\mathbb N,\leq)\) be the reflexive forward-order Kripke frame. Give its sole propositional letter \(p\) any valuation \(X\subseteq\mathbb N\). Let \(\mathcal B_d(X)\) be the Boolean algebra of truth sets of all finite modal formulas of modal depth at most \(d\), using \(p\), the usual Boolean operations, and the forward necessity \(\Box\). Let \(\mathcal B(X)=\bigcup_{d\geq0}\mathcal B_d(X)\).

If both \(X\) and \(\mathbb N\setminus X\) are infinite, then \(|\mathcal B_d(X)|=|\mathcal B(X)|=4\) for every \(d\geq0\). Otherwise the binary word \(1_X(0),1_X(1),\ldots\) is eventually constant. Let \(r=r(X)\geq1\) be its finite number of maximal constant-color intervals (runs), including the final infinite run. Then, for every integer \(d\geq0\),
\[
\boxed{|\mathcal B_d(X)|=2^{\min\{r,d+2\}},\qquad |\mathcal B(X)|=2^r.}
\]
The elements of \(\mathcal B(X)\) are precisely the unions of these \(r\) runs, and the least modal depth realizing every element is exactly \(\max\{0,r-2\}\). In particular, every number \(2^r\), \(r\geq1\), occurs as a one-generator subalgebra size, and modal-depth stabilization is unbounded despite local finiteness.

## Assumptions and scope
The carrier is the standard set of natural numbers including zero, with \(iRj\) precisely when \(i\leq j\). The modal operation is \(\Box Y=\{i:\forall j\geq i,\ j\in Y\}\), with \(\Diamond Y=\mathbb N\setminus\Box(\mathbb N\setminus Y)\). Boolean constants are allowed, but there is exactly one independent atomic proposition. Modal depth counts nested occurrences of \(\Box\) or its dual. The theorem concerns truth sets in this particular model, not equivalence of formulas across a class of all models. No computability or regularity is imposed on \(X\).

## Proof
**Cofinal two-color case.** If both colors occur infinitely often, each color occurs at or above every natural number. Thus \(\Box X=\Box(\mathbb N\setminus X)=\varnothing\), whereas \(\Box\varnothing=\varnothing\) and \(\Box\mathbb N=\mathbb N\). The four-element Boolean algebra \(\{\varnothing,X,\mathbb N\setminus X,\mathbb N\}\), already obtained at depth zero, is therefore closed under \(\Box\). No other truth sets can be generated.

**Eventual-constant case and finite quotient.** List the maximal monochromatic intervals in increasing order as \(I_1,\ldots,I_r\), where the last is infinite and neighboring intervals have opposite colors. Map each natural number in \(I_i\) to the state \(i\) of the finite reflexive chain \(C_r=(\{1,\ldots,r\},\leq)\). This is a surjective bounded morphism: accessibility implies nondecreasing interval index; conversely, from any point in \(I_i\), every interval \(I_j\) with \(j\geq i\) contains an accessible point (use the point itself for \(j=i\)). The valuation is constant on each interval. Consequently a modal formula has a truth set that is a union of runs, and its satisfaction on each run agrees with satisfaction at the corresponding state of \(C_r\), endowed with the alternating valuation.

**Depth types separate exactly the modal formulas.** For a state \(i\) in \(C_r\), let \(c_i\in\{0,1\}\) be its color and recursively put
\[
t_0(i)=c_i,\qquad t_{d+1}(i)=\left(c_i,\{t_d(j):j\geq i\}\right).
\]
For every nonnegative integer \(d\), two states have the same type \(t_d\) if and only if they satisfy the same formulas of modal depth at most \(d\). The forward implication follows by induction on formulas. Conversely, as only finitely many depth-\(d\) types occur, characteristic formulas exist: if \(\chi_t\) isolates type \(t\) at depth \(d\), the formula
\[
\eta_c\wedge\bigwedge_{t\in S}\Diamond\chi_t\wedge\Box\left(\bigvee_{t\in S}\chi_t\right)
\]
isolates the depth-\(d+1\) type \((c,S)\), where \(\eta_1=p\) and \(\eta_0=\neg p\). The empty-conjunction convention applies as usual. Since any subset of the finitely many depth types is a disjunction of characteristic formulas, \(\mathcal B_d(X)\) contains exactly \(2^{q_d}\) sets, where \(q_d\) is the number of distinct depth-\(d\) types in \(C_r\).

**Sharp refinement count.** If \(r=1\), every state is of a single type, hence \(q_d=1\) for every \(d\). Assume \(r\geq2\). At depth zero, states are grouped by the two colors, so \(q_0=2\). More precisely, at depth \(d\) with \(0\leq d\leq r-2\), the final \(d\) states of the chain have pairwise distinct types, different from the types of all preceding states; among the first \(r-d\) states, two have the same type exactly when they have the same color. This holds at depth zero.

For the induction step suppose \(d<r-2\), and set \(h=r-d\geq3\). All states \(i<h\) see both of the two types present in the unresolved prefix \(1,\ldots,h\), as well as every singleton type in the suffix \(h+1,\ldots,r\). State \(h\) sees only its own prefix-color type and those suffix singleton types, so it splits off. The earlier prefix states remain grouped precisely by color. The existing singleton suffix classes stay distinct, because depth-\(d+1\) equivalence refines depth-\(d\) equivalence. Hence, at depth \(d+1\), exactly the final \(d+1\) states are singleton classes and the earlier prefix is grouped by color. This proves \(q_d=d+2\) for \(0\leq d\leq r-2\). Once all \(r\) types are singletons, subsequent modal operators cannot split or merge this discrete partition. Thus \(q_d=\min\{r,d+2\}\) for all \(d\geq0\).

It follows that \(|\mathcal B_d(X)|=2^{\min\{r,d+2\}}\) and \(\mathcal B(X)\) consists of all \(2^r\) unions of runs. For \(r\geq3\), depth \(r-3\) yields fewer than \(r\) atoms and depth \(r-2\) yields all \(r\); for \(r\leq2\), depth zero already suffices. This proves the sharp stabilization depth. Arbitrarily long finite alternating prefixes followed by a constant infinite tail realize every \(r\geq1\), completing the theorem.

## Verification
The accompanying dependency-free Python 3 program `verify.py` independently computes (i) the complete Boolean/modal closure under \(\Box\), and (ii) the successive semantic successor-type partitions. It exhausts all \(510\) binary valuations on finite reflexive chains of lengths \(1\) through \(8\), verifying both formulas in every case and at all depths through length plus one. It also checks \(92\) longer alternating chains of lengths \(9\) through \(100\) at selected depths. Run `python3 verify.py` to reproduce `VERIFY_OK`.

These finite computations are consistency checks, not proofs about the infinite carrier; that conclusion follows from the bounded morphism and the exact type induction above.

## Relationship to prior work
Shapirovsky, *Modal logics of finite direct powers of \(\omega\) have the finite model property* (2019, Example 1 and Theorem 3.1), establishes the local finiteness of the complex algebra of \((\omega,\leq)\) by exhibiting finite tuned refinements. Agnew, *On Local Finiteness of Modal K4 Algebras* (2026, Theorem 3.16 and Proposition 3.18), gives a broad structural characterization and explicitly covers \((\omega,\leq)\). These results establish finiteness qualitatively, but the inspected material does not calculate the exact one-generator size or its modal-depth filtration as a function of the valuation. The present theorem uses the concrete run partition to determine both numerical invariants sharply.

Bounded modal equivalence and bounded bisimulation are standard; Bolander and Burigana (2024) discuss generic bounded bisimulation contractions. Their general equivalence criterion underlies the characteristic-type argument, but no formula for the alternating run model follows without the additional exact refinement count proved here.

## Limitations
This is a special-frame, one-generator theorem; no corresponding profile is asserted for a multi-generator valuation, a strict forward order, other ordinal frames, or arbitrary transitive frames. The search of prior literature cannot exclude an older equivalent one-variable characterization under alternative terminology. The numerical checks do not independently certify the unrestricted theorem.

## References
- G. Agnew, *On Local Finiteness of Modal K4 Algebras*, arXiv:2606.02941 (first posted June 1, 2026), especially Sections 2–3. https://arxiv.org/abs/2606.02941
- I. Shapirovsky, *Modal logics of finite direct powers of \(\omega\) have the finite model property*, arXiv:1903.04614 (2019), especially Example 1 and Theorem 3.1. https://arxiv.org/html/1903.04614v1
- T. Bolander and A. Burigana, *Better Bounded Bisimulation Contractions*, arXiv:2405.00480 (2024). https://arxiv.org/abs/2405.00480
