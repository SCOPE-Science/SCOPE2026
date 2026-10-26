# Sharp finite convergence of iterated possibility contraction

## Finding

Fix a nonempty finite Kripke model \(M_0=(W,R_0,V)\) with one agent, and a propositional atom \(p\). Let \(M_{t+1}\) be obtained from \(M_t\) by the *hedged public announcement contraction* of Belardinelli--Zhang on the fixed modal formula \(\Diamond p\), with \(\Diamond p:=\neg\Box\neg p\). The accessibility relation may be arbitrary, including nonserial relations. Worlds and the valuation are held fixed.

**Sharp stabilization theorem.** For \(n=|W|\ge1\),
\[
\boxed{R_n=R_{n+1}.}
\]
More precisely, the least \(s\ge0\) with \(R_s=R_{s+1}\) satisfies \(s\le n\), and equality can occur for **every** \(n\ge1\), using only one atom and one agent. For the sharpness model take \(W=\{0,\ldots,n-1\}\), let \(p\) hold exactly at \(0\), and put precisely the edges \(iR_0(i+1)\) for \(0\le i<n-1\). Then the first stationary stage is \(s=n\).

Thus the simplest genuinely modal possibility input changes the situation from the one-step idempotence of propositional hedged contractions to arbitrarily long, but uniformly linearly bounded, finite iteration.

## Assumptions and scope

For an arbitrary Kripke model \(M=(W,R,V)\), Belardinelli--Zhang contraction on a formula \(\varphi\) replaces the successor set \(R(w)\) by
\[
R^{\div\varphi}(w)=
\begin{cases}
R(w)\cup\{v\in W:M,v\models\neg\varphi\},
& M,w\models\Box\varphi,\\
R(w),&\text{otherwise}.
\end{cases}
\]
All truth evaluations are performed in the model *before* the current update. Our theorem applies this exact operation synchronously to all worlds with \(\varphi=\Diamond p\) at every finite stage. The same underlying \(W\) and \(V\) are used at all stages. Only one accessibility relation is considered; no seriality, reflexivity, transitivity, or symmetry is imposed.

Write \(P=V(p)\). For each \(t\ge0\), define
\[
A_t=\{w\in W:R_t(w)\cap P\ne\varnothing\},
\qquad N_t=W\setminus A_t.
\]
These are respectively the worlds satisfying and falsifying \(\Diamond p\) in \(M_t\). With \(S_t(w)=R_t(w)\), the contraction rule reduces exactly to
\[
\boxed{S_{t+1}(w)=
\begin{cases}
S_t(w)\cup N_t,&S_t(w)\subseteq A_t,\\
S_t(w),&S_t(w)\not\subseteq A_t.
\end{cases}}
\tag{1}
\]
The truth set \(P\) remains constant, but \(A_t\) need not remain constant.

## Proof

**Monotonicity of the possibility truth sets.** Formula (1) only adds arrows, whence \(S_t(w)\subseteq S_{t+1}(w)\) for all \(w\). Therefore
\[
A_t\subseteq A_{t+1}\qquad(t\ge0).
\tag{2}
\]

**No-progress lemma.** Suppose \(A_{t+1}=A_t\). We claim \(R_{t+1}=R_{t+2}\). If \(N_t=\varnothing\), equation (1) makes the step from \(t\) to \(t+1\) stationary already. Otherwise, let \(v\) be any world. If \(S_t(v)\not\subseteq A_t\), its successor row already meets \(N_t\) and is unchanged at this step. If \(S_t(v)\subseteq A_t\), equation (1) adds *all* of the nonempty \(N_t\); thus its new successor row also meets \(N_t\). Hence every \(S_{t+1}(v)\) meets \(N_t=N_{t+1}\). No row can satisfy the eligibility condition \(S_{t+1}(v)\subseteq A_{t+1}\), so no row changes in the next update. This proves the claim. In particular, the first step with no growth of \(A_t\) is the last step that might add arrows.

**Upper bound.** Let \(s\) be the least stationary stage. Every strict step \(t<s\) except possibly the final one must strictly enlarge \(A_t\); otherwise the no-progress lemma would force stationarity one step later. If \(A_0\ne\varnothing\), at most \(n-|A_0|\) steps can enlarge \(A_t\), so at most \(n-|A_0|+1\le n\) steps can be strict. If \(A_0=\varnothing\) and \(P=\varnothing\), no \(A_t\) can grow, and the no-progress lemma bounds the number of strict updates by one. Finally suppose \(A_0=\varnothing\) and \(P\ne\varnothing\). The first strict update must occur at a world with an empty successor row (the eligibility condition is then \(S_0(w)\subseteq\varnothing\)), and adds \(N_0=W\) to that row. In particular it introduces a \(p\)-successor, and hence \(A_1\supsetneq A_0\). Thus any strict first step is a growing step. If fewer than \(n\) growing steps occur, adding the at-most-one terminal nongrowing step gives at most \(n\) strict steps. If all \(n\) possible growing steps occur, then \(A_t=W\), so \(N_t=\varnothing\) and no nongrowing strict step can follow. Consequently \(s\le n\) in all cases.

**Sharpness for every size.** For \(W=\{0,\ldots,n-1\}\) take \(P=\{0\}\), the original directed path \(i\to i+1\) for \(i<n-1\), and no arrow out of \(n-1\). Initially \(A_0=\varnothing\). We prove inductively that after exactly \(t\) updates, for \(0\le t\le n\),
\[
A_t=\{n-t,n-t+1,\ldots,n-1\},
\tag{3}
\]
where the right side is empty for \(t=0\), and precisely the last \(t\) rows have been modified. Indeed, for \(t<n\), the next unmodified row \(n-t-1\) is empty if \(t=0\), and otherwise has the single original successor \(n-t\in A_t\). It therefore receives all of \(N_t=\{0,\ldots,n-t-1\}\), including \(0\), and enters \(A_{t+1}\). Every previously modified row has a successor in \(N_t\) (at least \(0\) until the final stage), hence is ineligible. Every still earlier unmodified row points to a world outside \(A_t\), hence is ineligible. Thus only row \(n-t-1\) changes, proving (3) inductively. The first \(n\) updates are all strict, but \(A_n=W\) and therefore \(N_n=\varnothing\), giving \(R_n=R_{n+1}\). No smaller stage is stationary.

The bound and its sharpness are therefore proved for all \(n\ge1\).

## Verification

The standalone `checker.py` represents each successor row and \(P\) by integer bitmasks and implements equation (1), recomputing \(A_t\) from the current rows at each stage. It exhaustively enumerates *every* valuation of \(p\) and *every* directed accessibility relation on labelled carriers of sizes \(1,2,3,4\). All \(1{,}052{,}740\) cases first stabilize by the cardinality bound. The numbers of cases whose first stationary stage is maximal are \(2,2,12,192\), respectively. The script additionally checks the explicit sharpness family, including the active-world invariant (3), for each \(1\le n\le24\). Reproduction: `python3 checker.py` using standard Python alone; expected final line: `ALL_CHECKS_OK`.

Finite tests are supplementary checks, not the basis for the infinite family assertion or the quantified all-model theorem. The proofs above establish those conclusions independently.

## Relationship to prior work

Belardinelli and Zhang introduce the exact hedged contraction rule in Definition 4.1 and prove reduction-axiom completeness and belief-change properties. Their conclusion identifies iterative aspects of generalized dynamic epistemic logic as a direction for future study; their results do not give this repeated \(\div\Diamond p\) convergence theorem.

A published examination titled *Idempotence and exact commutation of propositional hedged contractions* establishes one-step idempotence **when the contraction input is propositional**, by exploiting invariance of propositional truth under updates. Our input \(\Diamond p\) is not propositional, and equation (3) supplies models requiring arbitrarily many iterations. The existing idempotence result consequently does not imply the theorem.

Another published result, *Sharp state-count stabilization bound for finite believed announcements*, analyzes a fundamentally different operation: believed announcements **delete** all arrows into currently falsifying targets. Its sharp \(n\)-stage examples are not instances of the edge-**adding** hedged contraction here. The numerical coincidence in the state-count bounds is not statement equivalence.

The graph-modification literature studies addition of accessibility edges generally, but no equivalence to the specific modal-triggered row operation (1), sharp iteration bound, or directed-path witness was established in the inspected literature.

## Limitations

The theorem is for repeated contraction on the exact formula \(\Diamond p\), one agent, and finite nonempty world sets; it is not a uniform bound for arbitrary modal inputs or arbitrary generalized event models. The sharp witness uses nonserial, nonreflexive frames; sharpness within \(\mathsf{KD45}\), \(\mathsf{S4}\), or \(\mathsf{S5}\) subclasses is not claimed. The result counts the first stage at which the accessibility relation becomes stationary, not the time required to evaluate the formula computationally. Independent external priority checking remains unperformed. The 2026 paper *Suspending Judgement: Belief Contraction in Dynamic Epistemic Logic* was identified by bibliographic searches but its full content was inaccessible for a decisive comparison; it may contain related results under a different contraction semantics.

## References

[1] Gaia Belardinelli and Snow Zhang, *Belief Contraction in Dynamic Epistemic Logic*, EPTCS 447 (2026), 137–157, DOI:10.4204/EPTCS.447.8, arXiv:2606.31861 (first publicly posted 2026-06-30), https://arxiv.org/abs/2606.31861.

[2] *Idempotence and exact commutation of propositional hedged contractions*, published mathematical record, https://github.com/Resultary/2026/blob/main/2026/10/4/SCOPE-idempotence-and-exact-commutation-of-propositional-hedged-contra--cac8fc2eab7c/RESULT.md.

[3] *Sharp state-count stabilization bound for finite believed announcements*, published mathematical record, https://github.com/Resultary/2026/blob/main/2026/10/4/SCOPE-sharp-state-count-stabilization-bound-for-finite-believed-announ--65b4b662c65e/RESULT.md.

[4] Alexandru Baltag, Virginie Fiutek, and Sonja Smets, *Suspending Judgement: Belief Contraction in Dynamic Epistemic Logic*, KR 2026, DOI:10.24963/KR.2026/10 (comparison limited to bibliographic metadata).
