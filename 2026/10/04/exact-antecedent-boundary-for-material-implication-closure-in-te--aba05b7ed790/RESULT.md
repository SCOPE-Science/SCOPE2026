# Exact antecedent boundary for material-implication closure in team semantics
## Finding

Fix a finite nonempty set of valuations \(\Omega\), and let
\[
\mathcal T=\mathcal P(\Omega)
\]
be its team universe. A team proposition is a family
\[
P\subseteq\mathcal T.
\]

For team propositions \(P,Q\), define the truth family of the strong material implication by
\[
M(P,Q)=(\mathcal T\setminus P)\cup Q.
\]
This is exactly the team-proposition form of Barbero and Yang's clause saying that a team satisfies the material implication iff satisfaction of the antecedent implies satisfaction of the consequent.

Define the weak material truth family by
\[
M^\circ(P,Q)=\{\varnothing\}\cup M(P,Q),
\]
matching their weak material implication, which additionally makes the empty team true.

Call \(P\) **nonempty-downward closed** when
\[
T\in P,\quad \varnothing\ne S\subseteq T
\quad\Longrightarrow\quad
S\in P.
\]
Call \(P\) **proper-upward closed** when
\[
T\in P,\quad T\subseteq S\subsetneq\Omega
\quad\Longrightarrow\quad
S\in P.
\]
Call \(P\) **nonempty-proper-upward closed** when the latter implication is required only for nonempty \(T\).

Then:

\[
\boxed{
\begin{aligned}
&\forall Q\text{ union closed},\ M(P,Q)\text{ union closed}
&&\Longleftrightarrow&&
P\text{ nonempty-downward closed},\\
&\forall Q\text{ union closed},\ M^\circ(P,Q)\text{ union closed}
&&\Longleftrightarrow&&
P\text{ nonempty-downward closed},\\
&\forall Q\text{ intersection closed},\ M(P,Q)\text{ intersection closed}
&&\Longleftrightarrow&&
P\text{ proper-upward closed},\\
&\forall Q\text{ intersection closed},\ M^\circ(P,Q)\text{ intersection closed}
&&\Longleftrightarrow&&
P\text{ nonempty-proper-upward closed}.
\end{aligned}
}
\]

Thus the neutral elements of union and intersection are the only exceptions to the naive downward/upward duality: union closure cannot detect a failure involving only \(\varnothing\), while weak material implication also masks intersection failures whose intersection is \(\varnothing\).

There is a sharper source-facing corollary. If \(P\) itself is union closed, then the two material implications preserve union closure against **every** union-closed consequent exactly when
\[
P=\varnothing,
\]
or, for some \(A\subseteq\Omega\),
\[
P=\mathcal P(A)
\qquad\text{or}\qquad
P=\mathcal P(A)\setminus\{\varnothing\}.
\]
If \(P\) is additionally empty-team closed, the nonempty possibilities reduce exactly to
\[
P=\mathcal P(A),
\]
the flat principal ideals familiar from classical team semantics.

Dually, if \(P\) is intersection closed, then strong material implication preserves intersection closure against every intersection-closed consequent exactly when \(P=\varnothing\), or \(P\) is a principal up-set
\[
\{S\subseteq\Omega:B\subseteq S\},
\]
or such a principal up-set with the full team \(\Omega\) deleted.

For \(|\Omega|\ge3\), the antecedents for which the strong material implication is uniformly safe for both union-closed and intersection-closed consequents are exactly five families:
\[
\varnothing,
\]
the family of all nonempty proper teams, that family together with \(\varnothing\), that family together with \(\Omega\), and all teams. For the weak material implication there is one additional simultaneous-safe antecedent:
\[
\{\varnothing\}.
\]

## Assumptions and scope

Barbero and Yang work over a finite set of propositional variables and define a team proposition abstractly as a set of teams. Their material implication satisfies
\[
T\models\varphi\mathbin{\Rightarrow_{\mathrm m}}\psi
\]
iff \(T\models\varphi\) implies \(T\models\psi\), while their weak material implication adds the empty-team case.

The theorem is semantic at the level of team propositions. It does not assume that every antecedent family \(P\) is definable in a fixed object language. When a language is expressively complete for the relevant class, the statement transfers directly to formulas.

The result concerns preservation in the **consequent-uniform** sense: the antecedent \(P\) is fixed, and every consequent with the requested closure property is allowed. This refines the paper's global non-preservation result rather than contradicting it.

## Proof

### Union closure

Assume first that \(P\) is nonempty-downward closed and let \(Q\) be union closed. Suppose
\[
A,B\in M(P,Q)
\]
and put
\[
T=A\cup B.
\]
Assume for contradiction that
\[
T\notin M(P,Q).
\]
Then
\[
T\in P\setminus Q.
\]
Neither \(A\) nor \(B\) can be empty while the other equals \(T\), because that other team would then also lie in \(P\setminus Q\) and hence not in \(M(P,Q)\). Thus both \(A\) and \(B\) are nonempty. Since they are subteams of \(T\in P\), nonempty-downward closure gives
\[
A,B\in P.
\]
Their membership in \(M(P,Q)\) therefore forces
\[
A,B\in Q.
\]
Union closure of \(Q\) gives
\[
T=A\cup B\in Q,
\]
a contradiction. Hence \(M(P,Q)\) is union closed.

Exactly the same argument works for \(M^\circ(P,Q)\): if the union \(T\) were a nonempty counterexample, neither input team could be empty, so the extra weak-material truth of \(\varnothing\) is irrelevant.

Conversely, suppose nonempty-downward closure fails. Choose
\[
T\in P,\qquad
\varnothing\ne A\subsetneq T,\qquad
A\notin P.
\]
Put
\[
B=T\setminus A
\]
and
\[
Q=\{B\}.
\]
The family \(Q\) is union closed. We have
\[
A\in M(P,Q)
\]
because \(A\notin P\), and
\[
B\in M(P,Q)
\]
because \(B\in Q\). But
\[
A\cup B=T\in P
\]
and \(T\notin Q\), so
\[
T\notin M(P,Q).
\]
The same witness defeats \(M^\circ(P,Q)\), because \(T\ne\varnothing\). This proves both union statements.

### Intersection closure for strong material implication

Assume \(P\) is proper-upward closed and \(Q\) is intersection closed. Suppose
\[
A,B\in M(P,Q)
\]
but
\[
T=A\cap B\notin M(P,Q).
\]
Then
\[
T\in P\setminus Q.
\]
Neither \(A\) nor \(B\) can equal \(\Omega\), since then the intersection would equal the other input and that input would fail to belong to \(M(P,Q)\). Hence
\[
A,B\subsetneq\Omega.
\]
Because \(T\in P\) and
\[
T\subseteq A,B,
\]
proper-upward closure gives
\[
A,B\in P.
\]
Their membership in \(M(P,Q)\) forces
\[
A,B\in Q,
\]
and intersection closure gives
\[
T=A\cap B\in Q,
\]
a contradiction.

Conversely, if proper-upward closure fails, choose
\[
T\in P,\qquad
T\subsetneq A\subsetneq\Omega,\qquad
A\notin P.
\]
Let
\[
B=T\cup(\Omega\setminus A)
\]
and
\[
Q=\{B\}.
\]
Then \(Q\) is intersection closed,
\[
A\in M(P,Q)
\]
because \(A\notin P\), and
\[
B\in M(P,Q)
\]
because \(B\in Q\). Moreover
\[
A\cap B=T.
\]
Since \(B\ne T\), we have \(T\notin Q\), while \(T\in P\), so
\[
T\notin M(P,Q).
\]
Thus strong material implication fails intersection closure.

### Intersection closure for weak material implication

The preceding sufficiency argument for \(M^\circ\) only needs proper-upward closure when the bad intersection \(T\) is nonempty, because
\[
\varnothing\in M^\circ(P,Q)
\]
always. Hence nonempty-proper-upward closure suffices.

If that condition fails, choose a nonempty
\[
T\in P
\]
and
\[
T\subsetneq A\subsetneq\Omega
\]
with \(A\notin P\). The same
\[
B=T\cup(\Omega\setminus A),\qquad Q=\{B\}
\]
gives
\[
A,B\in M^\circ(P,Q)
\]
but
\[
A\cap B=T\notin M^\circ(P,Q),
\]
since \(T\ne\varnothing\). This proves necessity.

### Union-closed antecedents

Assume now that \(P\) is union closed and nonempty-downward closed. If \(P=\varnothing\), there is nothing to prove. Otherwise put
\[
A=\bigcup P.
\]
Because \(\Omega\) is finite, \(P\) is a finite family; union closure therefore gives
\[
A\in P.
\]
Nonempty-downward closure now gives every nonempty subset of \(A\). No member of \(P\) can contain a point outside \(A\) by definition of \(A\). Consequently
\[
P=\mathcal P(A)\setminus\{\varnothing\}
\]
or
\[
P=\mathcal P(A),
\]
according as \(\varnothing\notin P\) or \(\varnothing\in P\). The converse is immediate.

The dual principal-up-set statement follows by applying the same argument to intersections, using the least member
\[
B=\bigcap P.
\]

### Simultaneous finite classification

Assume \(|\Omega|\ge3\) and that \(P\) is both nonempty-downward and proper-upward closed. If \(P\) contains a nonempty proper team \(T\), choose \(v\in T\). Then
\[
\{v\}\in P.
\]
For any \(w\in\Omega\), if \(w\ne v\), the two-point team
\[
\{v,w\}
\]
is proper, so proper-upward closure puts it in \(P\), and nonempty-downward closure then gives
\[
\{w\}\in P.
\]
Thus every singleton belongs to \(P\), and proper-upward closure gives every nonempty proper team. The endpoints \(\varnothing\) and \(\Omega\) may then be chosen independently.

If \(P\) contains no nonempty proper team, proper-upward closure excludes \(\varnothing\) and nonempty-downward closure excludes \(\Omega\), so
\[
P=\varnothing.
\]
This yields exactly the five strong-material families listed above.

For weak material implication, nonempty-proper-upward closure places no restriction starting from \(\varnothing\), so the additional family
\[
\{\varnothing\}
\]
is possible and no other case is added.

## Verification

The bundled checker exhaustively enumerates every team proposition \(P\) and every union-closed or intersection-closed consequent \(Q\) for base sets of sizes \(1,2,3\). It directly computes the strong and weak material truth families and verifies all four equivalences above.

It separately enumerates all antecedent families for base size \(4\) and checks the structural corollaries: the union-closed safe antecedents are exactly the principal ideals and punctured principal ideals described above; the strong intersection-closed safe antecedents are the corresponding principal up-sets or full-team-punctured up-sets; and the simultaneous-safe counts are five for strong material implication and six for weak material implication once the base has at least three points.

The finite enumeration is corroborative only. The theorem for arbitrary finite \(\Omega\) follows from the set-theoretic proof.

## Relationship to prior work

Barbero and Yang study conditionals for team logics through preservation of closure properties, Modus Ponens, and the Deduction Theorem. They define the strong and weak material implications used here, characterize them inferentially under expressive-completeness assumptions, and prove by counterexample that neither operator preserves union closure, intersection closure, or convexity in general.

Their Appendix A gives explicit counterexamples to global preservation. The paper does not state an antecedent-wise necessary-and-sufficient criterion for when material implication is nevertheless guaranteed to preserve union or intersection closure against every closure-appropriate consequent. The concluding section explicitly raises the broader question of classifying conditionals under natural lists of requirements.

The present result sharpens the negative preservation statement by locating its exact boundary. On the union side, the neutral element \(\varnothing\) explains why full downward closure is stronger than necessary; on the intersection side, \(\Omega\) plays the dual role, and weak material implication additionally neutralizes an empty intersection. For union-closed and empty-team-closed antecedents, the safe boundary collapses exactly to flat principal ideals, linking the criterion back to the paper's classical-team semantics.

Earlier work on propositional union-closed team logics establishes expressive completeness and proof systems for union-closed languages, but the checked literature did not locate this fixed-antecedent material-implication preservation criterion.

## Limitations

The result classifies closure preservation of material implication at the level of team propositions. It does not classify all conditional operators satisfying a prescribed inferential package.

The statement is finite because the source fixes finitely many propositional variables. The four local equivalences themselves use only binary unions and intersections and extend formally to arbitrary base sets, but the principal-ideal corollary uses finiteness when forming the union of all members of \(P\).

The theorem does not address convexity. Convexity has two-sided interval geometry rather than a single neutral-element obstruction, so its exact antecedent boundary requires a separate analysis.

## References

[1] Fausto Barbero and Fan Yang, “Possible and Impossible Conditionals for Team Logics,” arXiv:2603.02136, first posted 2 March 2026; later published in *Logic, Language, Information, and Computation*, LNCS 16757 (2026), 50–66. DOI:10.1007/978-3-032-33486-2_4.

[2] Fan Yang, “Propositional union closed team logics,” *Annals of Pure and Applied Logic* 173(6) (2022), 103102. DOI:10.1016/j.apal.2022.103102.
