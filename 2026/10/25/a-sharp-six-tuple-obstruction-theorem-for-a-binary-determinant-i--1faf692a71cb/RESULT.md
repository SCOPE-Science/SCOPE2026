# A sharp six-tuple obstruction theorem for a binary determinant in dependence logic

## Finding

Fix two labelled determinant values \(X=\{0,1\}\) and finite labelled alphabets \(Y,Z\) of sizes \(b,c\ge1\). Under standard lax team semantics, put
\[
\varphi=\operatorname{dep}(x,y)\lor\operatorname{dep}(y,z).
\]
A team \(T\subseteq X\times Y\times Z\) is *minimal failing* if \(T\not\models\varphi\) and every proper subteam satisfies \(\varphi\). Set \(t=\binom{c}{2}\), with the convention that out-of-range binomial coefficients vanish.

**Theorem.** Every minimal failing team has exactly four or six tuples. The respective exact numbers of such labelled teams are
\[
N_4(b,c)=2\binom{b}{2}\binom{c}{2}^{2},\qquad
N_6(b,c)=\left(4\binom{b}{2}+44\binom{b}{3}\right)\binom{c}{2}^{3}.
\]
These equations hold for all \(b,c\ge1\), and there are no other minimal failing teams. For every \(b,c\ge2\), both sizes actually occur. Equivalently, every failing team has a failing subteam of at most six tuples, and six is the least uniform bound, even for \(b=c=2\). If \(b=1\) or \(c=1\), every team satisfies \(\varphi\).

This produces an exact finite forbidden-pattern basis after restricting only the number of values of the first determinant \(x\) to two; no restriction on the positive sizes of the other alphabets is required for the six-tuple bound.

## Assumptions and scope

The underlying team has exactly the variables \(x,y,z\) and consists of a *set* of distinct triples in \(X\times Y\times Z\), with no extra attributes or multiplicities. The alphabets are labelled; the counts are not quotiented by relabellings. The symbols \(\operatorname{dep}(x,y)\) and \(\operatorname{dep}(y,z)\) mean the usual functional dependencies. The disjunction is the standard team-semantic split, not ordinary Boolean disjunction of global dependency assertions. Allowing overlap in a split is equivalent to a partition here by downward closure.

The entire proof is finite combinatorics; no computational test is used to infer a statement for untested alphabet sizes. A fixed ambient universe can be taken as the disjoint tagged union of the three finite alphabets.

## Proof

**1. A two-register normal form.** Given a split \(T=R\cup B\) with \(R\models\operatorname{dep}(x,y)\) and \(B\models\operatorname{dep}(y,z)\), the set of red tuples with first coordinate \(i\in X\) has at most one second-coordinate value. Let \(f_i\in Y\cup\{\bot\}\) name that value, using \(\bot\) if no such red tuple exists. Recolour all tuples with \(y=f_i\) and \(x=i\) red, and the others blue. This preserves the red functional dependency and only *removes* tuples from blue, preserving its functional dependency. Conversely, any such pair \((f_0,f_1)\) for which the blue tuples have a single \(z\)-value in each \(y\)-fibre defines a valid split.

For each \(a\in Y\), define \(A_a=\{z:(0,a,z)\in T\}\) and \(B_a=\{z:(1,a,z)\in T\}\). Thus
\[
T\models\varphi\ \Longleftrightarrow\ \exists(f_0,f_1)\in(Y\cup\{\bot\})^2\ \forall a\in Y:\
\bigg|\!\!\bigcup_{i\in X:\ f_i\ne a}\{z:(i,a,z)\in T\}\bigg|\le1.
\]
Call \(a\) *mixed* if \(|A_a\cup B_a|\ge2\). Every mixed fibre requires \(f_0=a\) or \(f_1=a\). A nonmixed fibre requires no choice and is always harmless on the blue side.

**2. Three or more mixed fibres.** If \(T\) has at least three mixed fibres, choose three distinct such values \(a_1,a_2,a_3\), and from each choose two tuples with distinct \(z\)-values. Their six-tuple union is failing: two registers cannot cover three distinct mixed fibres. Therefore a minimal failing team in this case consists of *exactly* two tuples at each of precisely three mixed values.

Each two-tuple mixed fibre has exactly one of three types: \(L\), both tuples at \(x=0\); \(R\), both at \(x=1\); or \(C\), the tuples have different \(x\)-values. All pairs have distinct \(z\)-values. Their register requirements are respectively \(f_0=a\), \(f_1=a\), and \((f_0=a\lor f_1=a)\). For any two distinct mixed fibres, these requirements are jointly impossible **exactly when** both have type \(L\), or both have type \(R\). Consequently, a six-tuple team on three mixed fibres is minimal failing precisely when its three types contain at most one \(L\) and at most one \(R\). The choices per fibre are \(t,t,2t\) for \(L,R,C\), respectively. The patterns \(CCC\), one \(L\), one \(R\), and one of each contribute
\[
(2t)^3+3t(2t)^2+3t(2t)^2+6t^2(2t)=44t^3
\]
for each fixed three-element subset of \(Y\).

**3. Exactly two mixed fibres.** Let their values be distinct \(a,d\). Any satisfying register pair must be either \((f_0,f_1)=(a,d)\) or \((d,a)\), because both values must be covered. The first orientation fails if \(|B_a|\ge2\) or \(|A_d|\ge2\); the second fails if \(|A_a|\ge2\) or \(|B_d|\ge2\). Thus failure is equivalent to
\[
\bigl(|B_a|\ge2\ \lor\ |A_d|\ge2\bigr)
\ \land\
\bigl(|A_a|\ge2\ \lor\ |B_d|\ge2\bigr).
\]
Choosing one false-orientation witness from each parenthesis gives exactly four possibilities for the placement of the two pairs of offending \(z\)-values: two pairs at \(x=0\) on different fibres (\(L,L\)); two pairs at \(x=1\) on different fibres (\(R,R\)); or one pair at each \(x\)-value on the *same* fibre (\(L\cup R\)), with the other mixed fibre still present. Minimality therefore forces either a four-tuple team consisting of \(L,L\) or \(R,R\), or a six-tuple team consisting of a four-tuple \(L\cup R\) fibre together with one two-tuple, distinct-\(z\), *cross-\(x\)* fibre of type \(C\). A same-\(x\) pair on that remaining fibre would already contain an \(L,L\) or \(R,R\) four-tuple failure.

Each \(L\) or \(R\) pair has \(t\) choices, and a \(C\) pair has \(c(c-1)=2t\) choices. For each unordered pair \(\{a,d\}\subseteq Y\), there are \(2t^2\) four-tuple minimal failures and \(2t^2(2t)=4t^3\) six-tuple minimal failures. Their proper subteams satisfy the formula because deleting a member of a required pair removes one mixed-fibre requirement or restores one of the two orientations.

**4. Zero or one mixed fibre and enumeration.** With no mixed fibres, colour everything blue. With one mixed fibre \(a\), choose \(f_0=f_1=a\) and colour all other fibres blue. Thus no failures exist in these cases. An unmixed fibre may always be removed without changing the satisfaction of any other fibre, so it cannot occur in a minimal failing team. Combining Sections 2 and 3 yields the two stated counting formulas, with no hidden cases. Choosing \(b=c=2\), one four-tuple pattern and one six-tuple pattern are explicitly available. For example, the six-tuple set
\[
\{(0,0,0),(0,0,1),(1,0,0),(1,0,1),(0,1,0),(1,1,1)\}
\]
is of type \((L\cup R,C)\), hence is minimal failing. This proves sharpness. \(\square\)

## Verification

The accompanying standalone `checker.py` implements (i) direct red/blue partition semantics and (ii) the independently coded two-register normal form. It tests all \(256,4096,4096,262144,65536,1048576,65536\) subteams for alphabet pairs \((b,c)=(2,2),(2,3),(3,2),(3,3),(4,2),(5,2),(2,4)\), respectively, totalling \(1,450,240\) subteams. It checks minimality using deletion of each tuple, confirms the size restriction and both exact counting formulas, and cross-checks the original semantics by exhaustive red/blue partitions on the first three test domains. The observed numbers of four- and six-tuple minimal failures are, in the listed order, \((2,4),(18,108),(6,56),(54,1512),(12,200),(20,480),(72,864)\). The checker prints `ALL_CHECKS_OK 11856`.

The mathematical classification above, not the finite checker, proves the formulas for arbitrary positive \(b,c\).

## Relationship to prior work

Fröhlich, Kolaitis, and Meier (arXiv:2508.16146; CSL 2026, Theorem 25) prove that \(\operatorname{dep}(x,y)\lor\operatorname{dep}(y,z)\) is *incoherent* without a bound on the number of first-coordinate values. Their counterexamples use a growing first-coordinate alphabet; this theorem imposes the fixed two-value restriction and provides the sharp obstruction bound, exhaustive structural types, and labelled enumeration. The general normal form by splitting into functional dependencies is standard team semantics, not claimed new.

Barlag et al. (arXiv:2605.31269, Sections 3 and 5) develop general coherence, first-order rewritability, and decision complexity, but do not provide this restricted-value obstruction basis or its counting polynomial. The specialization obtained by imposing \(z=x\) reduces to the different two-variable disjunction \(\operatorname{dep}(x,y)\lor\operatorname{dep}(y,x)\); a result confined to that specialization cannot control freely varying third-coordinate values. The elementary two-register decomposition also explains why a fixed finite-domain promise restores a finite forbidden-pattern description despite the unrestricted case's incoherence.

## Limitations

The two-value restriction on \(x\) is essential to the claim. It is not asserted that six tuples suffice when \(x\) takes three or more values; in particular the unrestricted formula is known to be incoherent. No analogous enumeration is claimed for multiset teams or extra unprojected attributes. Counts assume labelled alphabets and ordinary lax splitting. Novelty assessments remain subject to undiscovered equivalent older formulations of functional-dependency decomposition; no independent external review has been performed.

## References

1. N. Fröhlich, P. G. Kolaitis and A. Meier, *Disjunctions of Two Dependence Atoms*, arXiv:2508.16146 (first posted 2025-08-22), *Computer Science Logic* 2026, DOI: 10.4230/LIPIcs.CSL.2026.10. Full open text: https://drops.dagstuhl.de/storage/00lipics/lipics-vol363-csl2026/html/LIPIcs.CSL.2026.10/LIPIcs.CSL.2026.10.html.
2. T. Barlag, N. Fröhlich, M. Hannula, P. G. Kolaitis, J. Kontinen, A. Meier and J. Väänänen, *Aspects of Coherence in Dependence Logic*, arXiv:2605.31269 (first posted 2026-05-29), https://arxiv.org/abs/2605.31269.
3. J. Kontinen, *Coherence and Complexity in Fragments of Dependence Logic*, PhD thesis, University of Amsterdam (2010), https://eprints.illc.uva.nl/id/eprint/2088/ (historical coherence background).
