# Recognition of finite effective closure models is \(\Pi^0_1\)-complete even under normality

## Finding

Let modal formulas use the countable propositional alphabet \(p_0,p_1,\ldots\), classical Boolean connectives and \(\Box\). A **finite effective closure model** has a nonempty finite world set \(W\), a finite generator \(G(w)\) at each world, a computable atomic valuation, and uniformly decidable membership of formulas in \(H_w=\operatorname{cl}(G(w))\). The input is an effective description, not a finite truth table listing the infinitely many formula memberships. We consider the promised class whose frames satisfy (E), (G), (M), (C), (N), and (K) as defined by Nishimura.

**Theorem.** On this class, deciding whether a finite effective closure model satisfies the same-carrier Kripke-representability condition (KRep) is \(\Pi^0_1\)-complete under computable many-one reductions. The upper bound holds for every finite effective closure model without the normality promise. Hardness persists for a one-world model with empty generator, constant-false atomic valuation, and closure operation \(\operatorname{cl}(X)=X\cup H\) that is extensive, monotone, idempotent, and preserves finite unions. In the hard family, membership in \(H\) is uniformly **primitive recursive**, rather than merely computable. Both outcomes of the reduction have frames satisfying all six named conditions.

In particular, neither a finite world set nor all usual normality axioms makes recognition of same-carrier representation decidable for this effective infinite-language presentation. A finite *explicit* closure table is a different input model and is not covered by the lower bound.

## Assumptions and scope

A finite code for the input supplies the worlds, finitely encoded generators and atomic valuation, and a syntactically specified total procedure deciding membership in every \(H_w\). The complexity upper bound is with respect to the promise that these membership procedures terminate, and the hardness family uses syntactically total primitive-recursive procedures. The six frame conditions are those of Nishimura, Figure 1: (E) equivalent replacement, (G) frame-valid generalization, (M) conjunction elimination, (C) conjunction introduction, (N) truth of \(\top\), and (K) modus ponens inside \(H_w\). (G) quantifies over *all valuations on the frame*, not just its distinguished model valuation.

Define \(E_w=\{v\in W:\mathcal M,v\models\psi\text{ for every }\psi\in H_w\}\). The KRep property is exactly
\[
\forall w\in W\ \forall\varphi:\quad \varphi\in H_w\ \Longleftrightarrow\ E_w\subseteq\llbracket\varphi\rrbracket_{\mathcal M}.
\]
Nishimura's representation theorem equates this property with truth preservation by a Kripke model on the *same world set and valuation*. The statement does not concern unrestricted enlargement of the carrier.

## Proof

**1. The upper complexity bound.** Satisfaction of a given modal formula at any given world is decidable by structural induction: at \(\Box\varphi\), call the promised decision procedure for \(\varphi\in H_w\). Consequently, non-KRep is recursively enumerable. Enumerate a world \(w\), a formula \(\varphi\notin H_w\), and, for every world \(v\) at which \(\varphi\) is false, a formula \(\psi_v\in H_w\) that is false at \(v\). The finitely many witness formulas are encoded in one finite tuple. Such a tuple certifies that no world both satisfies every member of \(H_w\) and falsifies \(\varphi\), so \(E_w\subseteq\llbracket\varphi\rrbracket\) although \(\varphi\notin H_w\). Conversely, if KRep fails, its separation formulation implies precisely such a finite tuple because \(W\) is finite. All tuple tests terminate, so the complement of the index set is computably enumerable; the desired set lies in \(\Pi^0_1\).

**2. A family of uniformly decidable normal theories.** Fix an arbitrary Turing program index \(e\). Let \(a_*\) be the assignment making every \(p_i\) false, and let \(a_n\) make only \(p_n\) true. Form the (abstract) collection of assignments
\[
S_e=\{a_*\}\cup\{a_n: e\text{ halts within }n\text{ steps}\}.
\]
For every modal formula \(\theta\) define \(T_e(\theta,a)\in\{0,1\}\) recursively. Boolean connectives have their usual interpretation; for every assignment \(a\), set
\[
T_e(\Box\chi,a)=1\quad\Longleftrightarrow\quad
\forall b\in S_e\; T_e(\chi,b)=1.
\]
This definition is well-founded on formula complexity because the right-hand side only evaluates the strict subformula \(\chi\). The value of every box is independent of the external assignment \(a\).

Let \(I(\theta)\) be the finite set of atomic indices appearing in \(\theta\). A structural induction proves that \(T_e(\theta,a)\) depends on \(a\) only through its restriction to \(I(\theta)\). Thus \(T_e(\theta,a_n)=T_e(\theta,a_*)\) for all \(n\notin I(\theta)\). The universal test in the box clause therefore reduces to checking \(a_*\) and the finitely many \(a_i\) for \(i\in I(\chi)\) such that the program halts within \(i\) steps. Every such test uses only bounded simulation, and recursion on syntax is primitive recursive for a standard encoding. Define
\[
H_e=\{\theta: \forall a\in S_e\;T_e(\theta,a)=1\}.
\]
Membership in \(H_e\) is uniformly primitive recursive in \(e\) and the code of \(\theta\). Also \(\bot\notin H_e\) because \(S_e\) contains \(a_*\).

**3. The one-world closure model and all six frame principles.** Put \(W=\{w\}\), \(G(w)=\varnothing\), assign every atom false at \(w\), and define \(\operatorname{cl}_e(X)=X\cup H_e\). This is extensive, monotone, idempotent and finite-union preserving. By induction, truth of \(\theta\) at \(w\) is \(T_e(\theta,a_*)\).

The set \(H_e\) is the intersection of the classical modal theories \(\{\theta:T_e(\theta,a)=1\}\) for \(a\in S_e\), with boxed subformulas interpreted uniformly across the assignments. Hence \(\top\in H_e\), the set is closed under conjunction and under modus ponens, and conjunction membership implies membership of each conjunct. This proves (M), (C), (N), (K). For (G), if a formula is valid on this one-world *frame* under every valuation, it is true under each assignment \(a\in S_e\), since the modal clause in every case is the fixed membership predicate \(H_e\); therefore it lies in \(H_e\). For (E), if two formulas are equivalent under every valuation on that frame, they have equal values under every \(a\in S_e\), hence either both belong to \(H_e\) or neither does. This independently verifies the frame-level quantification in (G) and (E), rather than just the distinguished valuation.

**4. Exact reduction from nonhalting.** If \(e\) never halts, then \(S_e=\{a_*\}\). The recursion becomes \(T_e(\Box\chi,a_*)=T_e(\chi,a_*)\). Consequently the one-world *reflexive* Kripke model with the same all-false atomic valuation has exactly the same truth value for every formula. Equivalently \(H_e\) is precisely the theory true at the sole world, and (KRep) holds.

If \(e\) halts, choose \(n\ge1\) at least its halting time. Then \(a_n\in S_e\), so \(\neg p_n\notin H_e\), although \(\neg p_n\) is true at the sole actual world. Since \(a_*\in S_e\), every formula in \(H_e\) is true at that world, whence \(E_w=\{w\}\). The semantic consequence criterion in the definition of (KRep) now forces \(\neg p_n\in H_e\), a contradiction. Directly, the only possible one-world Kripke accessibility relations are the empty relation, which would make \(\Box\bot\) true contrary to \(\bot\notin H_e\), and the reflexive relation, which would make \(\Box\neg p_n\) true contrary to \(\neg p_n\notin H_e\). Thus no same-carrier Kripke model represents it.

The map taking \(e\) to this syntactically primitive-recursive closure description is computable and always produces an instance in the promised six-condition class. It is KRep precisely when \(e\) never halts. Nonhalting is \(\Pi^0_1\)-complete. Together with Step 1 this establishes the theorem.

## Verification

The companion `checker.py` implements the recursive membership predicate for small explicitly timed halting and looping programs, enumerates finite formula tests, and checks conjunction, modus ponens, the one-world frame generalization principle on bounded formula/valuation families, and the two Kripke-relation obstructions. Running `python checker.py` prints `ALL_CHECKS_OK (44624 finite diagnostic assertions)`. These are finite diagnostics and do not replace the proof of the reduction or the infinite complexity classification. The checker uses no external datasets or nonstandard libraries.

## Relationship to prior work

Nishimura (2026), Definitions 2.2-2.5 and 4.22, introduces the closure models, frame principles and KRep condition, and Theorem 4.30 gives its equivalence to same-world Kripke representation. Example 4.24 establishes (G)+(K) without KRep on a countably infinite world set. Those semantic existence and translation results are premises, not claims of novelty here. The present result instead analyzes the recognition problem from a *finite effective description*, establishing its exact arithmetical complexity and one-world hardness despite all six principles.

Rudolph (2017) examines representations of closure operators on finite ground sets, a different encoding from decidable membership in sets of infinitely many modal formulas. Chen and Takahashi (2026) study undecidable properties of finitely axiomatized tense logics, not the input model's same-carrier representability. Connections to general index-set and Rice-style phenomena remain possible; the exact promised one-world normality restriction and upper bound were not found in the inspected sources.

## Limitations

The reduction uses countably many available propositional letters. It assumes only a finite world set and finite generator, not a finite list of all formulas in the closure. Its complexity assertion is a promise problem on effective descriptions, with a syntactically total primitive-recursive hard subfamily. The theorem does not contradict decision procedures for particular finitely axiomatized modal logics, does not claim undecidability for explicitly finite Boolean-algebra closure tables, does not concern all enlarged-world representations, and makes no assertion about a fixed finite propositional alphabet. Priority is subject to older results on effective syntactic knowledge or model-representation index sets under other terminology.

## References

1. Y. Nishimura, *Closure Semantics for Weak Modal Logics: Completeness and Representations*, arXiv:2610.01433, first publicly submitted 2026-10-01. In particular Definitions 2.2-2.5 and 4.22, Example 4.24, Theorem 4.30. https://arxiv.org/abs/2610.01433
2. S. Rudolph, *Succinctness and tractability of closure operator representations*, Theoretical Computer Science 658 (2017), 327-345. https://doi.org/10.1016/j.tcs.2015.12.028
3. Q. Chen and T. Takahashi, *Most Properties are Undecidable for Transitive Tense Logics*, arXiv:2606.31863, first submitted 2026-06-30. https://arxiv.org/abs/2606.31863
4. Classical undecidability and completeness of the complement of the Turing halting problem (standard computability-theory fact).
