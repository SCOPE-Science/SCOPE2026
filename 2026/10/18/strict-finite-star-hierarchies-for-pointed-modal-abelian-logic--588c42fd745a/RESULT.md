# Strict finite-star hierarchies for pointed modal Abelian logic

## Finding
Let \(S_m\) be the nonreflexive rooted Kripke star with exactly \(m\ge1\) terminal successors, and let \(L_m\) consist of all formulas valid at **every** world of \(S_m\) under every bounded real-valued valuation in pointed modal Abelian logic. Then
\[
L_1\supsetneq L_2\supsetneq L_3\supsetneq\cdots.
\]
More precisely, for every integer \(m\ge1\), the **least number of occurrences of the modal operator** \(\Box\) in a formula belonging to \(L_m\setminus L_{m+1}\) is exactly \(m+1\). This least number is attained by a **one-variable formula of modal depth one**. The separating countervaluation uses only truth values in the fixed interval \([0,1]\).

Write \(c\) for the distinguished constant with value \(-1\), \(|t|=t\vee(-t)\), and \(k t\) for the \(k\)-fold additive sum of a term \(t\), with \(0t=0\). An optimal separator is
\[
\Phi_m(x)=\bigvee_{i=0}^{m}\Box\bigl(|2m x+2i c|+c\bigr).
\]
The big disjunction here abbreviates finitely many applications of the ordinary binary lattice connective \(\vee\); there are exactly \(m+1\) occurrences of \(\Box\) and one propositional variable.

## Assumptions and scope
We use the standard pointed Abelian \(\ell\)-group \((\mathbb R,+,-,\vee,\wedge,0,c)\), where \(c=-1\), lattice operations are maximum and minimum, and satisfaction means a formula has value at least \(0\). The modal clause is
\[
V(w,\Box\theta)=\inf\{V(v,\theta):wRv\},
\]
with the stipulated empty-infimum value \(0\). Each propositional-variable valuation must be bounded across the finite frame; this is automatic for finite stars. The root of \(S_m\) accesses the \(m\) distinct terminal leaves and nothing else; each leaf has no successors. Frame validity quantifies over valuations and all worlds, not just the root. We count syntactic occurrences of \(\Box\), including nested occurrences, rather than counting distinct modal subformulas. No other modalities or truth constants are assumed.

## Proof
**1. The monotone hierarchy.** Every valuation on \(S_m\) can be extended to \(S_{m+1}\) by duplicating the complete assignment at any one leaf on the extra leaf. Induction on formulas shows that duplicating a leaf preserves every formula value at the original root, because duplicate entries do not change infima, and every modal formula at a terminal leaf has value \(0\). Thus any failure of validity on \(S_m\) persists on \(S_{m+1}\); equivalently, \(L_{m+1}\subseteq L_m\).

**2. The explicit separator.** For any assignment of real numbers \(a_1,\ldots,a_m\) to \(x\) at the leaves, let
\[
I_i=\{a\in\mathbb R:|2m a-2i|<1\}\qquad(0\le i\le m).
\]
The \(m+1\) open intervals \(I_i\) are pairwise disjoint. Each of the \(m\) leaf values belongs to at most one of them, so some index \(i\) has no leaf value in \(I_i\). For this index, every leaf evaluates \(|2m x+2i c|+c\) to at least \(0\), so its boxed minimum is at least \(0\). Therefore \(V(r,\Phi_m(x))\ge0\). At a terminal leaf, every boxed term evaluates to the empty-infimum value \(0\), and hence \(V(v,\Phi_m(x))=0\). The separator is valid throughout \(S_m\).

On \(S_{m+1}\), enumerate the leaves \(v_0,\ldots,v_m\) and set \(V(v_i,x)=i/m\). These values all lie in \([0,1]\). For each index \(i\), the boxed term has minimum \(-1\): at \(v_i\) the absolute value vanishes, and at every other leaf the absolute value is nonnegative. Hence \(V(r,\Phi_m(x))=-1<0\), so \(\Phi_m\notin L_{m+1}\). This proves every inclusion in the hierarchy is strict.

**3. Sharp modal-occurrence lower bound.** Fix any formula \(\psi\) containing at most \(k\) syntactic occurrences of \(\Box\), and any valuation on a rooted star with at least \(k\ge1\) leaves. Each modal subformula evaluated at the root that is not syntactically inside another box takes the infimum of its argument's values at terminal leaves. For each such outermost box occurrence select one leaf attaining that infimum. There are at most \(k\) selected leaves. At terminal leaves, the value of *every* subformula is determined by the local propositional values and the fact that all boxes evaluate to \(0\). Therefore retaining all selected leaves preserves the values of all outermost boxed subformulas at the root, as well as all nonmodal subformulas at the root. Induction on the remaining propositional context preserves \(V(r,\psi)\). We may add arbitrary previously existing leaves until the retained star has any prescribed size between the number selected and the original size; this does not change the selected minima. If no box is root-evaluated, one arbitrary leaf suffices. The same argument works for arbitrarily nested modal formulas.

Suppose a formula with at most \(m\) occurrences of \(\Box\) failed on \(S_{m+1}\). If the failure occurs at a terminal leaf, reproduce that local valuation at a leaf of \(S_m\), where all modal values remain unchanged. If it occurs at the root, the preceding witness argument retains at most \(m\) leaves and pads to exactly \(m\), preserving the negative value. In either case the formula fails on \(S_m\). Thus no formula with at most \(m\) boxes belongs to \(L_m\setminus L_{m+1}\). The displayed formula \(\Phi_m\) has exactly \(m+1\), completing the sharpness proof.

## Verification
The accompanying standalone Python 3 checker `check.py` evaluates formulas using exact rational arithmetic, confirms that \(\Phi_m\) has \(m+1\) modal occurrences and value \(-1\) on the prescribed countermodel for \(1\le m\le6\), and tests validity on grids or random finite valuations with \(m\) leaves. It also tests pruning of randomly generated nested modal expressions by retaining root box witnesses. Its reported result is `PASS 28170 finite sample/assertion groups`. These tests are supplementary; the disjoint-interval argument and witness-selection induction establish the all-real, all-formula quantifiers.

## Relationship to prior work
Jankovec and Poiger (2026), Definitions 3.1–3.2, provide exactly the pointed modal Abelian semantics used here, including the constant \(-1\), bounded real valuations, empty-infimum convention, and nonnegative satisfaction condition. Their Lemma 4.2 constructs term functions separating real truth values for a different algebraic purpose, but does not state a strict finite-star frame-validity hierarchy or its optimal number of boxes. Diaconescu, Metcalfe, and Schnüriger (2018) establish finite-model and labelled-tableau results for real-valued modal logic, including modal witness arguments; their cited results do not specify the exact successive-star modal-occurrence threshold. The lower-bound selection step here is a finite instance of familiar modal-witness preservation; novelty is claimed for the combined sharp one-variable hierarchy in these pointed semantics, not for witness selection in isolation. Separate finite-star stabilization results for Gödel modal operations without additive terms do not imply this nonstabilizing hierarchy.

## Limitations
The theorem concerns nonreflexive rooted stars with terminal successors, not arbitrary frames. It does not claim any complexity bound for arbitrary-frame validity, any axiomatization, or an independent formal proof. The separation formulas have coefficients depending on \(m\), and no uniform formula-length bound is asserted. Even though countervaluations lie in \([0,1]\), the logic has its full pointed real-valued additive operations rather than clipped \([0,1]\)-valued operations. An unindexed equivalent finite-star analysis could predate this result.

## References
- Filip Jankovec and Wolfgang Poiger, *Pointed Modal Abelian Logic, Algebraically*, EPTCS 447 (2026), pp. 518–531, DOI: 10.4204/EPTCS.447.29; first arXiv release 2026-06-30, arXiv:2606.31882. See Sections 3.1 and 4.1.
- Denisa Diaconescu, George Metcalfe and Laura Schnüriger, *A Real-Valued Modal Logic*, Logical Methods in Computer Science 14(1:10) (2018), DOI: 10.23638/LMCS-14(1:10)2018, arXiv:1706.02854. See the semantics and finite-model/tableau sections.
