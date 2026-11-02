# Central-binomial census and geometric center-defect law for modal Kleene chains

## Finding

Let \(m\geq1\), and let \(K_m=\{-m,-m+1,\ldots,m\}\) be the \((2m+1)\)-element bounded De Morgan chain, with \(x\wedge y=\min(x,y)\), \(x\vee y=\max(x,y)\), and involution \(\sim x=-x\). Count all unary operations \(\Box:K_m\to K_m\) making this a modal Kleene algebra in the sense of Celani, Menchón and Miguelez (2026), *without* imposing normality \(\Box m=m\).

**Normal form (a chain specialization of the centered modal identity in the motivating paper).** An operation satisfies the three modal Kleene equations (MK), (Pos), (Con) precisely when it is nondecreasing, \(\Box0\geq0\), and either \(\Box0=0\) or \(\Box x=\Box0\) for **every** \(x\leq0\). The latter case is a strictly positive plateau across the whole negative half of the chain. The two cases are disjoint. The normal form is used to derive the quantitative theorem; the underlying centered modal identity is credited to the motivating paper.

Put \(C_m=\binom{2m}{m}\). The numbers of operations, with fixed labelled chain carrier, are

\[
\begin{aligned}
\text{all modal operators:}\quad &A_m=C_m^2+\binom{2m}{m+1},\\
\text{normal }(\Box m=m):\quad &N_m=\tfrac12(C_m^2+C_m),\\
\text{center-preserving }(\Box0=0):\quad &P_m=C_m^2,\\
\text{normal and center-preserving:}\quad &Q_m=\tfrac12C_m^2.
\end{aligned}
\]

The exact proportion of non-center-preserving operators is

\[
\frac{A_m-P_m}{A_m}
=\frac{m}{(m+1)\binom{2m}{m}+m}
\sim\frac{\sqrt{\pi m}}{4^m}.
\]

Within the normal subclass the corresponding proportion is exactly \(1/(C_m+1)\), with the same asymptotic. Thus center preservation is asymptotically almost certain even though it is not included among the defining axioms.

**Geometric defect law.** Condition on the event \(\Box0>0\), and regard \(\Box0\in\{1,\ldots,m\}\) as the height of the center defect. The exact distribution is

\[
\Pr(\Box0=c\mid\Box0>0)=\frac{\binom{2m-c}{m}}{\binom{2m}{m+1}}
\qquad(1\leq c\leq m).
\]

For each fixed \(c\geq1\), this probability converges to \(2^{-c}\) as \(m\to\infty\); in fact the entire conditional distribution converges in total variation to the geometric distribution with masses \(2^{-c}\). The same limiting law holds when additionally conditioning on normality, with exact numerator \(\binom{2m-c-1}{m-1}\) and denominator \(\binom{2m-1}{m}\).

These exact formulas hold for every positive integer \(m\); the case \(m=1\) agrees with the previously known three-element census, while the quantitative all-size laws are the contribution assessed here.

## Assumptions and scope

The underlying algebra is the **fixed** odd finite chain \(K_m\), not an arbitrary Kleene algebra. It is a Kleene algebra because its De Morgan involution reverses the chain and \(x\wedge\sim x\leq0\leq y\vee\sim y\) for all elements. The modal operation has no independently specified diamond: \(\Diamond x:=\sim\Box\sim x\). The defining equations from Definition 3.5 of Celani–Menchón–Miguelez are:

\[
\begin{aligned}
(\mathrm{MK})\quad&\Box(x\wedge y)=\Box x\wedge\Box y,\\
(\mathrm{Pos})\quad&\sim\Box(z\vee\sim z)\leq\Box(z\vee\sim z),\\
(\mathrm{Con})\quad&\Box(x\vee(z\wedge\sim z))\leq
\Box x\vee\sim\Box(x\vee(z\wedge\sim z)).
\end{aligned}
\]

All quantifiers in these equations range independently over \(K_m\). A normal operator additionally satisfies \(\Box m=m\); a center-preserving one satisfies \(\Box0=0\). No bottom-preservation or modal frame representation is silently assumed.

## Proof

**Step 1 — exact simplification of the axioms.** On a chain, (MK) is equivalent to monotonicity: the forward direction follows from \(a\leq b\Rightarrow\Box a=\Box(a\wedge b)=\Box a\wedge\Box b\), and the converse follows from preservation of minima by any nondecreasing unary map. Also \(z\vee\sim z=|z|\), and the set of possible values \(|z|\) is exactly \(\{0,\ldots,m\}\). Consequently (Pos) says that \(\Box t\geq0\) for every \(t\geq0\); under monotonicity this is equivalent to \(\Box0\geq0\).

Write \(b=\Box(\max(x,-|z|))\) and \(a=\Box x\). Then \(a\leq b\) by monotonicity, and (Con) says \(b\leq\max(a,-b)\). If \(b\leq0\), the inequality is automatic. If \(b>0\), it is equivalent to \(a=b\). Taking \(z=0\) and \(x\leq0\), we obtain \(b=\Box0\). When \(\Box0>0\), (Con) forces \(\Box x=\Box0\) for every \(x\leq0\).

For the converse, suppose \(\Box\) is nondecreasing and \(\Box0\geq0\), with the stated plateau when \(\Box0>0\). If \(x\geq0\), then \(\max(x,-|z|)=x\) and (Con) is immediate. If \(x<0\) and \(\Box0=0\), then \(b\leq0\), so (Con) holds. Finally, if \(x<0\) and \(\Box0>0\), both \(x\) and \(\max(x,-|z|)\) are nonpositive; the plateau gives \(a=b\), so (Con) holds. This proves the structural equivalence in both directions, including all boundaries.

**Step 2 — enumeration with preserved center.** If \(\Box0=0\), the \(m\) negative inputs take an arbitrary weakly increasing sequence in the \(m+1\) values \(-m,\ldots,0\), and the \(m\) positive inputs independently take an arbitrary weakly increasing sequence in \(0,\ldots,m\). Each sequence has \(\binom{2m}{m}=C_m\) choices, by combinations with repetition. Thus there are \(C_m^2\) such maps. Requiring \(\Box m=m\) fixes the last entry of the positive sequence and leaves \(\binom{2m-1}{m-1}=C_m/2\) choices for its remaining \(m-1\) entries. The normal center-preserving count is therefore \(C_m^2/2\).

**Step 3 — enumeration of positive plateaux.** If \(\Box0=c\in\{1,\ldots,m\}\), all inputs \(x\leq0\) have output \(c\). The remaining \(m\) outputs form any weakly increasing sequence in \(\{c,\ldots,m\}\), yielding \(\binom{2m-c}{m}\) choices. Hence the number of non-center-preserving maps is

\[
\sum_{c=1}^{m}\binom{2m-c}{m}
=\binom{2m}{m+1}
=\frac{m}{m+1}C_m.
\]

In the normal subclass, the last positive output must be \(m\). The same argument gives

\[
\sum_{c=1}^{m}\binom{2m-c-1}{m-1}
=\binom{2m-1}{m}=\frac12C_m.
\]

Both identities are the hockey-stick binomial identity; adding the disjoint cases gives \(A_m,N_m,P_m,Q_m\) exactly.

**Step 4 — asymptotics and defect law.** Stirling's formula yields \(C_m\sim4^m/\sqrt{\pi m}\). Substituting this into \(m/((m+1)C_m+m)\) gives \(\sqrt{\pi m}/4^m\) asymptotically. The normal proportion is \(1/(C_m+1)\) and has the same limit ratio. For the conditional center-defect distribution, set \(w_m(c)=\binom{2m-c}{m}\). For fixed \(c\), the ratio \(w_m(c)/\binom{2m}{m+1}\to2^{-c}\). Moreover, \(w_m(c+1)/w_m(c)=(m-c)/(2m-c)\leq1/2\), so the conditional tails are uniformly geometrically bounded. Pointwise convergence with total mass one therefore yields total-variation convergence. For normal operators use \(v_m(c)=\binom{2m-c-1}{m-1}\) instead; \(v_m(c+1)/v_m(c)=(m-c)/(2m-c-1)\leq1/2\), and \(v_m(c)/\binom{2m-1}{m}\to2^{-c}\). This proves the second limit and completes the proof.

## Verification

The standalone Python 3 program `checker.py` evaluates (MK), (Pos), and (Con) directly, independently of the normal form; it also evaluates the proposed normal form and compares them. It exhausts all unary functions for \(m=1,2\), exhausts every monotone unary function for \(m=1,2,3,4\), verifies each of the four counting formulas, and checks both binomial summations for \(1\leq m\leq60\). Run `python3 checker.py` in the directory containing the file.

The exact independent counts for \(m=1,2,3,4\) are respectively \(A_m=5,40,415,4956\); \(N_m=3,21,210,2485\); \(P_m=4,36,400,4900\); and \(Q_m=2,18,200,2450\). The completed check returned `ALL_CHECKS_OK full_functions=3152 monotone_maps=26162 binomial_ranks=60`. The finite computation corroborates, but does not replace, the argument for all \(m\).

## Relationship to prior work

Celani, Menchón and Miguelez introduce precisely the three modal Kleene equations used here and prove categorical and topological representations, including the centered case. Those qualitative results supply the algebraic setting but do not give the chain plateau classification, four enumerators, or the asymptotic fraction. Flaminio, Godo, Menchón and Rodriguez earlier study modal rotations of Gödel algebras into nilpotent-minimum algebras; their centered fixed-point-preserving modal setting and extra modal assumptions do not count all of the present (MK), (Pos), (Con) operations. A published finite Boolean–Kleene product census includes the \(m=1\) three-element case; no priority is asserted for that case. Direct products of two- and three-element carriers are not the odd chains of lengths five and higher.

The centered identity (Cen) in Proposition 3.19 of the 2026 paper already yields the plateau condition in this chain setting; no novelty is claimed for that specialization alone. The quantitative count, exact defect-height distribution, total-variation limit, and their normal-subclass refinements are not given by those qualitative results and require the independent sequence enumeration. Older equivalent results under other names, or indirect implications of more general operator-classification theorems, remain possible.

## Limitations

Only the stated De Morgan/Kleene odd chains and the exact three 2026 axioms are covered. Even chains, nonchains, operators with extra equational constraints, and semiring-based Kleene-star algebras are not classified. Counts are of unary operations on a fixed labelled chain, not arbitrary isomorphism types. This result makes no claim of absolute historical uniqueness; independent mathematical validation has not been performed.

## References

1. S. Celani, P. Menchón, V. Miguelez, *A Modal Expansion of Kleene Algebras via Twist Structures*, arXiv:2608.10937, initial public version 2026-08-11, especially Definition 3.5 and Section 3.1. https://arxiv.org/abs/2608.10937
2. T. Flaminio, L. Godo, P. Menchón, R. O. Rodriguez, *Rotations of Gödel algebras with modal operators*, arXiv:2405.19354, 2024, Section 3. https://arxiv.org/abs/2405.19354
3. *Exact modal-expansion counts on finite Boolean–Kleene products*, related previously published research record; the three-element chain specialization is credited and not claimed as new.
