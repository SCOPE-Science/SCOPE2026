# Exact four-parameter census of two-sided confluent relations between finite two-level orders

## Finding

For integers \(a,c,b,d\ge1\), let \(P=A\oplus C\) and \(Q=B\oplus D\) be two **distinctly specified** finite two-level orders: \(|A|=a\), \(|C|=c\), \(|B|=b\), and \(|D|=d\). Each level is an antichain, every element of a lower level is below every element of its upper level, and all points are labelled. For a relation \(R\subseteq P\times Q\) impose the two confluence requirements
\[
 x\le_P y\ \land\ yRz\ \Longrightarrow\ \exists w\in Q\;(xRw\land w\le_Q z),\tag{DC}
\]
\[
 x\le_P y\ \land\ xRz\ \Longrightarrow\ \exists w\in Q\;(yRw\land z\le_Q w).\tag{FC}
\]

Define four integer expressions
\[
\begin{aligned}
L_{a,c;b,d}&=(2^b-1)^a-2^{ab}+(2^a-1+2^c)^b,\\
U_{a,c;b,d}&=(2^d-1)^c+(2^c+2^a-1)^d-2^{cd},\\
C_{a,c;b,d}&=\sum_{t=1}^{b}\binom bt\bigl[(1+2^t(2^d-1))^c-(2^t(2^d-1))^c\bigr],\\
Z_{a,c;b,d}&=\sum_{s=1}^{d}\binom ds\bigl[(1+(2^b-1)2^s)^a-((2^b-1)2^s)^a\bigr].
\end{aligned}
\]
Then the **exact number** \(N(a,c;b,d)\) of such confluent relations is
\[
\boxed{N(a,c;b,d)=1+L_{a,c;b,d}\,U_{a,c;b,d}+C_{a,c;b,d}+Z_{a,c;b,d}.}\tag{1}
\]
The four summands count disjoint structural strata, namely the empty relation; all lower-source rows meeting \(B\) and every upper-source row meeting \(D\); all lower-source rows meeting \(B\) but some upper-source row avoiding \(D\); and at least one lower-source row avoiding \(B\) in a nonempty relation.

In particular
\[
N(1,1;1,1)=7,\quad N(1,1;2,2)=71,\quad N(2,1;1,2)=69,
\quad N(2,2;2,2)=1867,\quad N(2,2;3,3)=108327.
\]
The theorem counts relations **between two independently chosen ordered carriers**; it is not limited to a self-relation. No monotonicity, totality, surjectivity, or reflexivity is imposed beyond (DC) and (FC).

## Assumptions and scope

The nonempty cardinalities \(a,c,b,d\) are arbitrary positive integers; source and target labels are fixed. An ordinal sum of antichains has only identity comparabilities within each level, and all lower-to-upper comparabilities. The relation is an arbitrary subset of the Cartesian product. Equations (DC) and (FC) are exactly the downward and forward order–relation confluence conditions; when source and target coincide they are the pair appearing in Sedlár–Vigiani's 2026 modal Nelson semantics (their Definition 12, conditions (40) and (41)) and in related intuitionistic modal semantics. Here the same equations are studied for a correspondence between two possibly different posets.

The count is for **binary correspondences** rather than maps or valuation structures. It does not assert that every relation between two distinct carriers is itself the accessibility relation of a single Kripke model. If a source logic additionally requires compatibility with an inconsistent-world predicate, that is not included. The empty relation is counted because the confluence implications hold vacuously.

## Proof

Write the row of each \(i\in A\) as \(R(i)=X_i\cup Y_i\), where \(X_i\subseteq B\) and \(Y_i\subseteq D\). For each \(j\in C\), write \(R(j)=P_j\cup Q_j\), with \(P_j\subseteq B\) and \(Q_j\subseteq D\). Distinct points in a single level are incomparable. Thus only comparisons \(i\in A\) below \(j\in C\) can give nontrivial confluence constraints.

For every such pair \(i,j\), direct consideration of the two target levels shows that (DC) and (FC) are equivalent to the following four simultaneous conditions:
\[
\begin{gathered}
P_j\subseteq X_i,\qquad Y_i\subseteq Q_j,\\
X_i=\varnothing\ \Longrightarrow\ Q_j\subseteq Y_i,\\
Q_j=\varnothing\ \Longrightarrow\ X_i\subseteq P_j.
\end{gathered}\tag{2}
\]
For example, under (DC) each target-lower point in \(P_j\) can only be witnessed by itself in \(X_i\); each target-upper point in \(Q_j\) can be witnessed either by itself in \(Y_i\) or by any point of \(X_i\). The other two clauses arise dually from (FC). This proves necessity and sufficiency of (2) without any assumptions on unlisted edges.

**Stratum I: every \(X_i\) and every \(Q_j\) is nonempty.** Then the last two implications of (2) are vacuous, leaving \(P_j\subseteq\bigcap_i X_i\) and \(\bigcup_iY_i\subseteq Q_j\). Fix the family \((X_i)\) and put \(t=|\bigcap_i X_i|\). Every upper row has \(2^t\) choices for its \(B\)-part. To count the remaining choices of all \(Y_i,Q_j\), consider each of the \(d\) target-upper points independently. If that point belongs to none of the \(Y_i\), its membership in the \(c\) sets \(Q_j\) is arbitrary, giving \(2^c\) possibilities. If it belongs to at least one \(Y_i\), its nonempty membership pattern across the \(a\) lower rows has \(2^a-1\) possibilities and it must belong to every \(Q_j\). This gives \((2^c+2^a-1)^d\) possibilities before enforcing the nonemptiness of every \(Q_j\). When some \(Y_i\) contains a target-upper point, nonemptiness is automatic. When all \(Y_i\) are empty, we must replace the count \(2^{cd}\) by \((2^d-1)^c\). The corrected factor is precisely \(U_{a,c;b,d}\), independent of \(t\).

It remains to sum \(2^{ct}\) over all \(a\)-tuples of nonempty subsets \(X_i\subseteq B\). For \(t\ge1\), the number whose intersection has size \(t\) is
\[
\binom bt(2^a-1)^{b-t}.
\]
Indeed, each of the \(t\) common points is in all \(a\) subsets, and each of the remaining points has any of the \(2^a-1\) membership patterns other than the all-present pattern. The count with empty intersection is
\[
(2^b-1)^a-2^{ab}+(2^a-1)^b.
\]
The weighted sum is therefore
\[
\sum_{X_1,\ldots,X_a\ne\varnothing}2^{c|\cap_iX_i|}
=(2^b-1)^a-2^{ab}+(2^a-1+2^c)^b=L_{a,c;b,d}.
\]
The first nonempty stratum contributes exactly \(L_{a,c;b,d}U_{a,c;b,d}\).

**Stratum II: every \(X_i\ne\varnothing\), but some \(Q_j=\varnothing\).** Because \(Y_i\subseteq Q_j\) for all \(i\), every \(Y_i=\varnothing\); the last clause of (2) then gives \(X_i=P_j\) for all \(i\), so all the \(X_i\) are one common nonempty set \(S\subseteq B\). For fixed \(|S|=t\), each upper row independently has either \((P_j,Q_j)=(S,\varnothing)\), exactly one choice, or a nonempty \(Q_j\subseteq D\) with an arbitrary \(P_j\subseteq S\), giving \(2^t(2^d-1)\) choices. Requiring at least one empty \(Q_j\) gives
\[
(1+2^t(2^d-1))^c-(2^t(2^d-1))^c.
\]
Summing over the \(\binom bt\) choices of \(S\) gives \(C_{a,c;b,d}\).

**Stratum III: at least one \(X_i=\varnothing\).** By (2), all \(P_j\) vanish. For any lower row with \(X_i=\varnothing\), the two inequalities for \(Y_i,Q_j\) force \(Y_i=Q_j\), for every upper row \(j\). Thus the \(Q_j\) all equal a common set \(T\subseteq D\). If \(T=\varnothing\), (2) forces every row empty, so the relation is empty. Otherwise let \(|T|=s\ge1\). Any lower row is now either \((X_i,Y_i)=(\varnothing,T)\), one possibility, or has a nonempty \(X_i\subseteq B\), \(2^b-1\) possibilities, and an arbitrary \(Y_i\subseteq T\), \(2^s\) possibilities. At least one lower row must be of the first type. This yields
\[
(1+(2^b-1)2^s)^a-((2^b-1)2^s)^a.
\]
Summing over \(\binom ds\) choices of the nonempty \(T\) gives \(Z_{a,c;b,d}\). The empty relation contributes one additional case. The four classes are disjoint and exhaustive, proving (1).

## Verification

The accompanying standalone `checker.py` separately implements (1) and literal exhaustive checking of the quantified confluence clauses. For each \(a,c,b,d\in\{1,2,3\}\) with \(a+c\le4\) and \(b+d\le4\), the checker examines all \(2^{(a+c)(b+d)}\) relations and compares direct counts to (1), obtaining **36 exact agreements**. It also verifies the order-reversal symmetry \(N(a,c;b,d)=N(c,a;d,b)\) on \(5^4=625\) parameter choices and tests numerical instances against a literal confluence predicate independent of the counting formula. The output ends with `ALL_CHECKS_OK`.

Finite exhaustive tests do not prove formula (1) for arbitrary parameters; the complete partition into strata I–III and identity (2) supply the general proof. Because the checker is self-contained, reproduction requires only Python 3 and the embedded file.

## Relationship to prior work

Sedlár and Vigiani (2026, Definition 12) supply precisely the downward and forward confluence implications on a **single** ordered Kripke carrier and establish their semantic role; their inspected paper does not enumerate correspondences between different height-two orders. Sato (2026) and Balbiani–Gao–Gencer–Olivetti (2024) give other semantic settings with these confluence conditions. Kozicki and Kavvos (2026) motivate relations between distinct systems in a categorical duality framework, but their (bi)simulation conditions are not identified with (DC)–(FC) here, and their inspected full text does not provide the four-parameter census.

A previously obtained coalescing-fan count for a single order with one greatest point coincides with the specialization \(a=b\), \(c=d=1\) of the current theorem and is **not** claimed again as a new result. The substantive new domain is the complete four-independent-parameter family of relations between *possibly different* two-level orders; for example, \(N(2,2;2,2)=1867\) counts a regime absent from the single-greatest-point special case. Published finite-chain endpoint normal forms and finite weak-order **function** counting formulas do not imply the exact count of arbitrary multi-valued correspondences here. The main remaining priority risk is a general order-compatible multirelation theorem elsewhere in the relation-algebra literature that subsumes (1) under different terminology.

## Limitations

The enumeration assumes exactly two nonempty antichain levels in both ordered carriers; it does not provide an all-height recurrence, and is not an enumeration of full modal models. Confluence alone should not be conflated with bisimulation of arbitrary additional modal transitions or with bounded morphisms. All calculations count relations on labelled, fixed carriers; automorphism orbits are not counted. A previous single-carrier fan enumeration supplies a special case, so the new claim is the two-carrier four-parameter classification and not a new proof of that older subcase. External priority beyond inspected sources is not certified, and independent mathematical audit has not been performed.

## References

[1] Igor Sedlár and Pietro Vigiani, *Modal Extensions of Generalised Nelson Logics*, arXiv:2610.10008v1, first publicly posted 2026-10-07, Definition 12.

[2] Yuta Sato, *Intuitionistic and Constructive Modal Logics for Classical Modal Logicians*, arXiv:2608.29708v1, first publicly posted 2026-08-30.

[3] Philippe Balbiani, Han Gao, Çiğdem Gencer, and Nicola Olivetti, *Local Intuitionistic Modal Logics and Their Calculi*, arXiv:2403.06772 (2024).

[4] Piotr Kozicki and G. A. Kavvos, *Relational Dualities and Bisimulation*, FSCD 2026, DOI:10.4230/LIPIcs.FSCD.2026.20.
