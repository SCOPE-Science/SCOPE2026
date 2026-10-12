# Counting p-morphisms onto the NAE four-point frame is \(\#\mathsf{P}\)-complete
## Finding

Let \(\mathbf F\) be the irreflexive Kripke frame with worlds
\[
\{r,c,t,f\}
\]
and exactly the arrows
\[
rRc,\qquad cRt,\qquad cRf.
\]

For a finite monotone \(\operatorname{NAE}_3\) instance \(\Phi\) with variable set \(V\) and nonempty clause set \(C\), define a Kripke frame \(\mathbf G_\Phi\) as follows. Its worlds are a root \(\rho\), one world \(q_j\) for every \(j\in C\), and one world \(x_v\) for every \(v\in V\). Its only arrows are
\[
\rho Rq_j\quad(j\in C)
\]
and
\[
q_jRx_v
\]
whenever \(v\) occurs in clause \(j\). Repeated occurrences of one variable in a clause produce the same arrow; this is harmless because a repeated-variable \(\operatorname{NAE}_3\) constraint depends only on whether the occurring variables realize both truth values.

A map \(h\) between Kripke frames is a p-morphism here when it satisfies the usual forth condition
\[
uRv\Longrightarrow h(u)Rh(v)
\]
and the back condition
\[
h(u)Rw'\Longrightarrow \exists v\,\bigl(uRv\land h(v)=w'\bigr).
\]
We count only surjective p-morphisms.

Restriction to the variable worlds gives a bijection
\[
\left\{\text{surjective p-morphisms }\mathbf G_\Phi\to\mathbf F\right\}
\longleftrightarrow
\left\{\text{Boolean assignments satisfying }\Phi\right\}.
\]
Therefore
\[
\#\operatorname{PMor}_{\mathrm{surj}}(\mathbf G_\Phi,\mathbf F)
=
\#\operatorname{NAE}_3(\Phi).
\]

It follows that counting surjective p-morphisms to this one fixed four-point frame is \(\#\mathsf{P}\)-complete under standard polynomial-time counting reductions. The displayed reduction from \(\#\operatorname{NAE}_3\) is parsimonious. The hardness already holds for input frames that are finite, irreflexive, acyclic, rooted, and whose longest directed path has two edges.

## Assumptions and scope

The source problem is monotone Boolean \(\operatorname{NAE}_3\): every constraint says that its three variable occurrences are not all assigned the same truth value. Repetitions are allowed. If the three occurrences collapse to a two-element set, the condition is disequality of those two variables; if they collapse to a singleton, the constraint is unsatisfiable. The incidence-frame construction reproduces these cases exactly.

The clause set is required to be nonempty. This guarantees that a satisfying assignment uses both truth values in at least one clause, so the corresponding p-morphism is automatically onto all four worlds of \(\mathbf F\). The restriction loses no counting hardness because the empty-constraint case is trivial.

The complexity statement concerns the function problem whose input is a finite Kripke frame and whose output is the number of surjective p-morphisms onto the fixed target \(\mathbf F\). Membership in \(\#\mathsf{P}\) uses the direct finite certificate consisting of the map itself.

## Proof

Fix a surjective p-morphism
\[
h:\mathbf G_\Phi\longrightarrow\mathbf F.
\]

First, the root is forced. Since \(h\) is surjective, some source world maps to \(r\). A variable world cannot map to \(r\): it is a sink, while back for \(rRc\) would require a successor. A clause world cannot map to \(r\) either. If \(h(q_j)=r\), back for \(rRc\) forces a successor variable world \(x_v\) with \(h(x_v)=c\), but \(x_v\) is a sink and back for \(cRt\) then fails. Hence
\[
h(\rho)=r.
\]

For every clause \(j\), the source has \(\rho Rq_j\). The target world \(r\) has only one successor, namely \(c\). By forth,
\[
h(q_j)=c.
\]

If \(v\) occurs in a clause \(j\), then \(q_jRx_v\), so forth gives \(h(x_v)\in\{t,f\}\). If \(v\) is isolated, then \(x_v\) is a sink and cannot map to \(r\) or \(c\), because either image has a target successor and would violate back. Thus every variable world maps to \(t\) or \(f\).

Now \(h(q_j)=c\), and \(c\) has precisely the two successors \(t\) and \(f\). Back at \(q_j\) therefore says that \(q_j\) has at least one successor mapped to \(t\) and at least one successor mapped to \(f\). These successors are exactly the variable worlds occurring in clause \(j\). Hence the induced Boolean assignment satisfies every \(\operatorname{NAE}_3\) constraint.

Conversely, given a Boolean assignment satisfying \(\Phi\), define
\[
h(\rho)=r,\qquad h(q_j)=c
\]
for all clauses, and map every variable world to \(t\) or \(f\) according to its Boolean value. Forth is immediate. Back at \(\rho\) is witnessed by any clause world because \(C\ne\varnothing\). Back at each clause world is witnessed by one true and one false variable occurrence. The target worlds \(t\) and \(f\) are sinks and impose no back obligations. Since a satisfying clause realizes both truth values, the map is onto \(r,c,t,f\).

These constructions are inverse, proving the exact bijection.

Checking a proposed finite map for surjectivity, forth, and back is polynomial-time, so the counting problem lies in \(\#\mathsf{P}\). Creignou and Hermann's Boolean counting dichotomy makes \(\#\operatorname{CSP}(\operatorname{NAE}_3)\) \(\#\mathsf{P}\)-complete because the relation \(\operatorname{NAE}_3\subseteq\{0,1\}^3\) has six tuples and is therefore not affine: a nonempty affine Boolean relation has cardinality a power of two. The incidence-frame construction is polynomial and preserves the number of solutions exactly, proving hardness.

## Verification

The bundled `verify.py` reconstructs \(\mathbf F\), the incidence frames, and the p-morphism definition directly. It exhaustively compares the two counts for every nonempty family of distinct three-variable clauses on \(3\) and \(4\) variables. It also exhausts all one- and two-edge rank-at-most-three hypergraphs on at most \(3\) variables, including singleton and two-variable constraints arising from repeated variables. For each tested instance it enumerates every Boolean assignment and every map from the source frame to the four-point target, then checks surjectivity, forth, and back.

The finite computation is a consistency check. The arbitrary-instance theorem follows from the forced-image and clause-back arguments above, not from extrapolation.

## Relationship to prior work

Takahashi's 2026 paper uses this same four-point frame in Remark 2.8 and Figure 1 to explain a decision reduction from monotone \(\operatorname{NAE}_3\)-SAT: the two terminal worlds encode truth and falsity, and the p-morphism back condition enforces that each clause sees both values. The stated consequence there is coNP-completeness of validity for the corresponding Jankov extension, not a counting classification of p-morphic witnesses.

The present result isolates the exact witness correspondence and shows that it is parsimonious. This changes the object of study from existence of a p-morphic image to the number of surjective p-morphisms into one fixed modal frame.

There is also a graph-algorithm literature on locally surjective homomorphisms, the undirected analogue of the same local-surjectivity condition. The inspected recent framework papers concern decision and parameterized complexity rather than the exact directed four-point counting problem proved here. Because terminology differs across modal logic and graph homomorphisms, unindexed counting work under the locally-surjective alias remains a bibliographic risk.

## Limitations

The theorem is a fixed-target counting result, not a dichotomy for all Kripke targets. It does not classify approximate counting, sampling, uniqueness, or counting modulo an integer.

The hardness restriction is to the explicit incidence-frame family above. No claim is made that four target worlds are minimal among all fixed targets capable of \(\#\mathsf{P}\)-hard p-morphism counting.

The locally-surjective graph-homomorphism literature is broad. The searches and inspected sources located decision and parameterized results but no equivalent exact counting theorem for this directed target; an unindexed equivalent result remains possible.

## References

[1] Tenyo Takahashi, “Non-elementary modal logics, assuming \(\mathsf{P}\ne\mathsf{NP}\),” arXiv:2609.10872, first public version 2026-09-09. See Remark 2.8 and Figure 1.

[2] Nadia Creignou and Miki Hermann, “Complexity of Generalized Satisfiability Counting Problems,” *Information and Computation* 125(1), 1–12 (1996), DOI:10.1006/INCO.1996.0016.

[3] Laurent Bulteau, Konrad K. Dabrowski, Noleen Köhler, Sebastian Ordyniak, and Daniël Paulusma, “An Algorithmic Framework for Locally Constrained Homomorphisms,” *SIAM Journal on Discrete Mathematics* 38(2), 1315–1350 (2024), DOI:10.1137/22M1513290.
