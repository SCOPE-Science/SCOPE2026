# A matching criterion for single-premise entailment between two-disjunct functional dependencies

## Finding
Let \(U\) be a finite attribute set. For \(i=1,2\), write \(d_i=(X_i\to y_i)\), and for \(j=1,2\), write \(e_j=(A_j\to b_j)\). Assume that all four dependencies are nontrivial: \(y_i\notin X_i\) and \(b_j\notin A_j\). Then, over all finite teams (equivalently over all teams),
\[
(d_1\vee d_2)\models(e_1\vee e_2)
\quad\Longleftrightarrow\quad
[(d_1\models e_1\land d_2\models e_2)\lor(d_1\models e_2\land d_2\models e_1)].
\]
For ordinary nontrivial functional dependencies, \((X\to y)\models(A\to b)\) if and only if \(y=b\) and \(X\subseteq A\). Thus the criterion is a perfect matching condition on a bipartite graph with two vertices in each part. It is decided by four elementary subset comparisons; when the condition fails, a finite counterexample is given constructively below.

## Assumptions and scope
An assignment is a row with one value per attribute in the fixed finite set \(U\). A team is a set of rows over a common, unrestricted value domain. It satisfies \(X\to y\) if any two rows agreeing on \(X\) agree on \(y\). Lax splitting disjunction means that \(T\models\phi\vee\psi\) if and only if \(T=T_1\cup T_2\) for some (possibly overlapping) subteams satisfying \(\phi\) and \(\psi\), respectively. Since FDs are downward closed, overlapping covers can always be made disjoint. The empty team satisfies every dependency. No restriction on the size of finite teams or the domain is assumed. The theorem concerns a *single* disjunctive premise, not a collection of premises. Multiple attributes may occur in determinants, but every consequent is one attribute.

## Proof
Write \(d\preceq e\) when the single FD \(d\) entails the single FD \(e\). For nontrivial \(d=(X\to y)\) and \(e=(A\to b)\), this happens exactly when \(b=y\) and \(X\subseteq A\). The forward implication of this statement follows by taking a full product of independent attribute values except that \(y\) is a function of the values of \(X\); if \(b\ne y\), vary \(b\) independently, and if \(b=y\) but \(X\not\subseteq A\), vary one missing coordinate of \(X\). The reverse implication is immediate.

If a perfect matching exists, any cover of \(T\) by a \(d_1\)-team and a \(d_2\)-team is also a cover by the two respective target dependencies, proving sufficiency.

We prove necessity using the following density observation. For a finite team \(T\) and an FD \(e=(A\to b)\), every \(e\)-satisfying subteam has at most
\[
M_e(T)=\sum_{a\in\pi_A(T)}\max_v\big|\{t\in T:t(A)=a,\ t(b)=v\}\big|
\]
rows. Indeed, each determinant fiber in an \(e\)-team can retain only one consequent value. Therefore, if \(M_{e_1}(T)+M_{e_2}(T)<|T|\), the team cannot satisfy \(e_1\vee e_2\). All constructions below use arithmetic in \(\mathbb F_3\) and pair-valued coordinates \((u_a,v_a)\in\mathbb F_3^2\). A finite common value domain can encode these pairs together with tagged values.

**Case 1: some source dependency, say \(d_i=(X\to y)\), entails neither target.** Enumerate the full Cartesian grid of all pair-valued assignments to attributes other than \(y\). On every row put \(y=\sum_{a\in X}u_a\) in \(\mathbb F_3\), using zero for an empty sum. The resulting team \(T\) satisfies \(X\to y\), and so satisfies the premise. Fix an arbitrary nontrivial target \(e=(A\to b)\) not implied by \(d_i\). If \(b\ne y\), the second coordinate \(v_b\) remains uniform and independent when the determinant values \(A\) are fixed (recall \(b\notin A\)). If \(b=y\), then \(X\not\subseteq A\), and at least one first coordinate \(u_a\), with \(a\in X\setminus A\), remains uniform when \(A\) is fixed; the sum defining \(y\) is consequently uniform. In either case each determinant fiber has three equally populated consequent classes, so \(M_e(T)\le |T|/3\). This holds for both targets, and \(2|T|/3<|T|\); the conclusion fails.

**Case 2: both source dependencies imply a target but no perfect matching exists.** By the two-by-two Hall condition, both sources then imply the *same* target, say \(e_1=(A\to b)\), and neither implies \(e_2=(B\to c)\). Hence \(d_i=(X_i\to b)\) with \(X_i\subseteq A\). Make two equal-size disjoint teams \(T_1,T_2\), each indexed by the full grid of pair-valued assignments to all attributes except \(b\). On \(T_i\), set the value of \(b\) to a tag identifying \(i\), together with the following optional residue: if \(c=b\), add \(\sum_{a\in X_i}u_a\) as residue modulo three; otherwise choose a constant residue. Distinct tags guarantee that the two teams' \(b\)-values differ. Each \(T_i\) satisfies \(d_i\). Because \(X_i\subseteq A\), fixing \(A\) determines the \(b\)-value separately on each \(T_i\); every \(A\)-fiber in \(T=T_1\cup T_2\) therefore has two equally large classes of distinct \(b\)-values. Thus \(M_{e_1}(T)\le |T|/2\). For \(e_2\), if \(c\ne b\), then \(v_c\) is independent of \(B\) even if \(B\) contains \(b\), since the tag and optional residue in this branch are constant. If \(c=b\), the failure \(d_i\not\preceq e_2\) implies \(X_i\not\subseteq B\); fixing \(B\) leaves at least one summand of the \(b\)-residue uniformly free within \(T_i\). In both cases every \(e_2\)-satisfying subteam of each \(T_i\) has at most \(|T_i|/3\) elements. Intersecting an arbitrary \(e_2\)-satisfying subteam with \(T_i\) preserves satisfaction, so \(M_{e_2}(T)\le |T|/3\). The sum of the two upper bounds is \(5|T|/6<|T|\). Thus \(T\models d_1\vee d_2\) but \(T\not\models e_1\vee e_2\).

The two cases exhaust the failure of a perfect matching. Consequently the matching criterion is necessary. The constructions are finite and use only three coordinate symbols per independent component. This proves the theorem. \(\square\)

## Verification
The standalone `checker.py` exhaustively computes, for the constructed finite witnesses, the largest possible FD-satisfying subteam through determinant-fiber maxima. Its deterministic sample covers 131 nonmatching instances chosen from all nontrivial single-consequent dependencies on three attributes, including repeated dependencies, constant dependencies, and both Hall-failure cases. Each witness satisfies the asserted source branch(es), while the respective target density bounds are verified numerically. The complete mathematical proof above supplies the unbounded-domain guarantee; a finite test does not replace it. Run `python3 checker.py` after extracting the embedded file.

## Relationship to prior work
Fröhlich, Kolaitis and Meier, *Disjunctions of Two Dependence Atoms* (2025 preprint; CSL 2026), give a model-checking complexity classification and coherence results and explicitly propose the implication problem for finite sets of such disjunctions in their final outlook. The present theorem resolves only the single-premise subcase under a nontriviality convention. Ordinary Armstrong entailment for a single FD yields the matrix entries but does not alone settle whether splitting disjunction can create additional entailments; the two finite-density counterteam constructions establish this missing implication. The published article and nearby dependence-logic references inspected did not provide this matching criterion, but equivalent results in other database/constraint literature remain a possible priority risk.

## Limitations
The theorem excludes trivial FD consequents already included in their determinants; such targets are tautological and require separate boundary conventions. It does not classify implication from two or more disjunctive premises, mixed dependence atoms, approximate FDs, fixed tiny domains, or disjunctions with more than two dependence atoms. Its explicit counterteams may have size exponential in the number of attributes; the polynomial-time decision is by the four implication tests, not by constructing these witnesses. Independent expert review has not been performed.

## References
1. N. Fröhlich, P. G. Kolaitis and A. Meier, *Disjunctions of Two Dependence Atoms*, arXiv:2508.16146, first publicly available August 22, 2025; 34th EACSL Annual Conference on Computer Science Logic, DOI: 10.4230/LIPIcs.CSL.2026.10. Relevant material: the definitions of dependence atoms and disjunction, the complexity/coherence classifications, and the concluding open implication problem.
2. S. Abiteboul, R. Hull and V. Vianu, *Foundations of Databases*, Addison-Wesley, 1995, Chapter on functional dependencies and Armstrong implication.
