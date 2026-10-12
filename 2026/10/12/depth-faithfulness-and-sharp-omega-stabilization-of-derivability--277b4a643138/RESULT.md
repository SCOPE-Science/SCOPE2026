# Depth-faithfulness and sharp \(\omega\)-stabilization of derivability-box approximants

## Finding

Write \(\mathsf K\) for the smallest normal classical unimodal logic. In the derivability-box semantics of Bevan (2025), define \(L_0=\mathrm{PC}\) and \(L_{n+1}=V\mathrm{INT}(L_n)\) for every integer \(n\geq0\). Here \(V\mathrm{INT}(\lambda)\) is the logic of formulas valid in every interpretation evaluated using \(\lambda\).

**Finite-depth simulation theorem.** For every integer \(n\geq1\), every interpretation \(I=(M,\Gamma,L_{n-1})\), and every finite set \(\Sigma\) of formulas of modal depth at most \(n\), there exists a finite pointed Kripke tree \((T,w)\), of height at most \(n\), such that
\[
I\models\varphi\quad\Longleftrightarrow\quad (T,w)\models\varphi\qquad(\varphi\in\Sigma).
\]
Consequently, for \(n\geq0\),
\[
L_n\cap\mathrm{Fm}_{\leq n}=\mathsf K\cap\mathrm{Fm}_{\leq n},
\]
where \(\mathrm{Fm}_{\leq n}\) consists of formulas of modal depth at most \(n\). The cutoff is exact: \(\Box^{n+1}\top\in L_{n+1}\setminus L_n\). Hence no finite stage stabilizes, and \(\bigcup_{n<\omega}L_n=\mathsf K\) is reached first at stage \(\omega\).

## Assumptions and scope

The language has countably many propositional atoms, \(\bot\), Boolean implication and one unary box; \(\top:=\neg\bot\). Modal depth is zero on atoms and \(\bot\), unchanged by Boolean connectives except for taking maxima, and increases by one under \(\Box\). Propositional calculus \(\mathrm{PC}\) consists of Boolean tautologies when distinct modal subformulas are viewed as propositional atoms.

An interpretation \(I=(M,\Gamma,\lambda)\) has an atom valuation \(M\), an arbitrary set of assumptions \(\Gamma\), and an evaluation logic \(\lambda\). Its Boolean connectives are classical, and
\[
I\models\Box\psi\quad\Longleftrightarrow\quad\Gamma\vdash_\lambda\psi.
\]
The finitary consequence relation \(\vdash_\lambda\) is Bevan's: \(\Gamma\vdash_\lambda\psi\) iff \(\psi\in\lambda\), or finitely many elements of \(\Gamma\), together with a theorem of \(\lambda\), yield \(\psi\). No consistency or factivity assumption is imposed on \(\Gamma\). Kripke frames have arbitrary accessibility; the finite witness is a rooted tree, not necessarily reflexive or serial. The local simulation concerns each finite set of formulas, not one tree representing the entire infinite theory of an interpretation.

## Proof

**1. Kripke points are realizable by derivability-box interpretations.** Suppose \(\lambda\subseteq\mathsf K\), and fix any pointed Kripke model \((W,R,v),w\). Let \(M\) be the atoms true at \(w\), and let \(\Gamma\) contain exactly the formulas true at every immediate successor of \(w\). For every formula \(\psi\),
\[
\Gamma\vdash_\lambda\psi\quad\Longleftrightarrow\quad\psi\in\Gamma.
\]
The right-to-left implication follows from membership. For the reverse, soundness of \(\lambda\subseteq\mathsf K\) makes every \(\lambda\)-consequence of \(\Gamma\) true at every successor. Thus \((M,\Gamma,\lambda)\) agrees with the Kripke point on each atom and each boxed formula, and therefore on every formula. Initially \(L_0\subseteq\mathsf K\); induction using this observation gives \(L_n\subseteq\mathsf K\) for all \(n\), because validity in all derivability-box interpretations entails validity on all Kripke points.

**2. Inductive local simulation.** The base case \(n=0\) is a single Kripke root realizing any prescribed propositional valuation; it also proves equality between \(\mathrm{PC}\) and the depth-zero part of \(\mathsf K\). Suppose the result about validity is established at depth \(n-1\), namely every \(\mathsf K\)-theorem of depth at most \(n-1\) belongs to \(L_{n-1}\). Let \(I=(M,\Gamma,L_{n-1})\) and finite \(\Sigma\subseteq\mathrm{Fm}_{\leq n}\). Collect all operands \(\psi\) of box subformulas \(\Box\psi\) occurring anywhere in \(\Sigma\); the resulting set \(B\) is finite and every member has depth at most \(n-1\). Put
\[
B^+=\{\psi\in B:\Gamma\vdash_{L_{n-1}}\psi\},\qquad B^-=B\setminus B^+.
\]
For each \(\chi\in B^-\), the formula
\[
\left(\bigwedge_{\psi\in B^+}\psi\right)\wedge\neg\chi
\]
is \(\mathsf K\)-satisfiable. Otherwise \(\mathsf K\) proves \((\bigwedge B^+)\to\chi\). This implication has modal depth at most \(n-1\), so the inductive hypothesis puts it in \(L_{n-1}\). Since \(\Gamma\) derives each member of \(B^+\), ordinary finitary propositional deduction then makes \(\Gamma\vdash_{L_{n-1}}\chi\), contradicting \(\chi\in B^-\). The empty conjunction means \(\top\).

By ordinary Kripke completeness and the finite model property of \(\mathsf K\), choose for each \(\chi\in B^-\) a finite pointed Kripke model satisfying every member of \(B^+\) and falsifying \(\chi\). Unravel its reachable part to depth \(n-1\); the relevant formulas, all of depth at most \(n-1\), retain their truth values, and the result is a finite rooted tree. Make all these trees immediate successor subtrees of a new root \(w\), assigning the atoms at \(w\) according to \(M\). When \(B^-=\varnothing\), use a root with no successors. By construction every \(\Box\psi\) occurring in \(\Sigma\) has at \(w\) exactly the truth value it has in \(I\). A structural induction on the Boolean connectives then establishes the asserted simultaneous agreement on \(\Sigma\). The assembled tree has height at most \(n\).

**3. Exact agreement in bounded depth.** Since \(L_n=V\mathrm{INT}(L_{n-1})\), the simulation shows that if \(\varphi\) has depth at most \(n\) and is not in \(L_n\), there is an \(I\) refuting it and hence a finite Kripke model refuting it. Thus \(\mathsf K\cap\mathrm{Fm}_{\leq n}\subseteq L_n\); Step 1 gives the reverse inclusion. The base \(n=0\) was handled above.

**4. Sharp first omission and stabilization.** The map \(\lambda\mapsto V\mathrm{INT}(\lambda)\) is monotone, \(\mathrm{PC}\subseteq L_1\), and every theorem \(\psi\in\lambda\) makes \(\Box\psi\in V\mathrm{INT}(\lambda)\). Hence \(L_n\subseteq L_{n+1}\), and \(\Box^r\top\in L_r\) for all \(r\geq0\). Conversely, \(\Box\top\notin\mathrm{PC}\), since a modal atom can be assigned false in propositional calculus. If \(\Box^r\top\notin L_{r-1}\), the interpretation \((M,\varnothing,L_{r-1})\) refutes \(\Box^{r+1}\top\), for any \(M\); consequently \(\Box^{r+1}\top\notin L_r\). This proves \(\Box^{n+1}\top\in L_{n+1}\setminus L_n\) by induction. Its depth is exactly \(n+1\), while Step 3 shows that no \(\mathsf K\)-theorem of lesser depth can separate the two logics.

Finally, Bevan's Proposition 5 says \(V\mathrm{INT}(\lambda)=\mathsf K_0+\Box\lambda\), where \(\mathsf K_0\) is the logic generated by propositional tautologies and the distribution axiom, without a global necessitation rule. The increasing union \(\bigcup_nL_n\) contains \(\mathsf K_0\), is closed under necessitation by the displayed theorem-lifting property, and is contained in \(\mathsf K\) by Step 1. It therefore equals \(\mathsf K\). Bevan's continuity theorem makes this union a fixed point. Strictness at all finite stages shows that the first stabilization ordinal is exactly \(\omega\).

## Verification

The nonstandard step is the finite-set simulation in Step 2. To check it, fix \(n\), form the finite operand set \(B\), and check separately for each \(\chi\in B^-\) that a hypothetical \(\mathsf K\)-proof of \((\bigwedge B^+)\to\chi\) would, by the depth induction, yield the forbidden \(L_{n-1}\)-derivation of \(\chi\). Kripke completeness supplies a model for each resulting consistent formula. The finite-model and bounded-unravelling steps use only standard modal-logic facts. Step 4 can be checked directly in the empty-assumption interpretation at every index. No finite enumeration is offered as an infinite proof; the argument is deductive and applies to all natural \(n\).

## Relationship to prior work

Bevan (2025), §§1.1 and 1.3, introduces the derivability-box semantics, establishes \(V\mathrm{INT}(\lambda)=\mathsf K_0+\Box\lambda\), and identifies the increasing union of the iterates from \(\mathrm{PC}\) with \(\mathsf K\). The present statement adds a quantified finite-tree simulation for arbitrary fixed-evaluation interpretations and finite modal-depth fragments, proves exact finite-stage depth agreement, and determines the first depth of disagreement and the first stabilization ordinal. The union identity alone does not imply strictness at every finite stage.

Schröder and Pattinson (2007/2009) establish strictly one-step complete rules and shallow-model constructions for \(\mathsf K\). Their one-step methodology is related to the witness construction above, but their investigated semantics are Kripke/coalgebraic rather than Bevan's evaluation-logic interpretations; no theorem about this particular staged \(V\mathrm{INT}\) construction was located. The standard completeness and finite-model properties of \(\mathsf K\) are used as established facts, not claimed as new.

## Limitations

The tree simulation is formula-finite; it does not produce a single finite Kripke tree matching an interpretation on all formulas. No bound tighter than modal depth on tree height or model size is asserted. The exact-rank witness says nothing about minimal proof length. Related results might be formulated in older one-step proof-theoretic language, and the complete text of Bevan's 2022 dissertation could not be compared; the manuscript's available abstract is too general to settle that comparison. These are literature risks, not mathematical exceptions. There has been no independent audit.

## References

1. Michael Bevan, *Logics of Logics*, *The Review of Symbolic Logic* **18** (2025), 1192–1202, DOI: `10.1017/S1755020325100890`, first published online 22 August 2025. See §§1.1–1.3, especially Proposition 5, Theorem 2, Proposition 6 and Corollary 2.
2. Lutz Schröder and Dirk Pattinson, *PSPACE Bounds for Rank-1 Modal Logics*, arXiv:`0706.4044` (2007), later *ACM Transactions on Computational Logic* **10**(2) (2009), Article 13; see Example 3.18 and Theorem 4.9.
3. Michael Bevan, *Logic and Modality*, Oxford DPhil thesis (2022), University of Oxford Research Archive, DOI: `10.5287/ora-pynnb8amq` (metadata and abstract inspected only; full text inaccessible during comparison).
