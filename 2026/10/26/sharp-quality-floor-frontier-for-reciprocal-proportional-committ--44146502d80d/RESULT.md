# Sharp quality-floor frontier for reciprocal proportional committee elections

## Finding
For every fixed \(q\in(0,1]\), the sharp worst-case fraction of unrestricted maximum committee quality retained by an **optimally chosen** committee satisfying any one of reciprocal JR, reciprocal EJR, reciprocal threshold-PJR+, and reciprocal value-EJR is
\[
\Phi(q)=\begin{cases}
\frac34,&0<q\le\frac12,\\
1-q+q^2,&\frac12\le q\le1.
\end{cases}
\]
Equivalently, the sharp *quality-price* under each axiom is \(1/\Phi(q)\). The formula is an infimum across finite instances, not a promise that the worst case is attained at a finite committee size. The plateau ends at the exact quality floor \(q=1/2\).

## Assumptions and scope
A finite nonempty voter set \(V\), a finite candidate set \(C\), and an integer committee size \(1\le k\le|C|\) are given. Each candidate \(c\) carries quality \(h_c\in[q,1]\), and each voter \(i\) reports an approval set \(A_i\subseteq C\). In the lower-bound constructions, each candidate is supported by at least one voter. A committee \(W\subseteq C\) must contain exactly \(k\) candidates; its total quality is \(h(W)=\sum_{c\in W}h_c\). Let \(H^*=\max_{|W|=k}h(W)>0\). For an axiom \(\mathcal A\), let \(H_\mathcal A^*\) be the largest \(h(W)\) among \(k\)-committees obeying \(\mathcal A\). The sharp retention fraction is \(\inf_{\text{finite admissible instances}} H_\mathcal A^*/H^*\).

Reciprocal JR says that if a group \(S\) of voters commonly approves an unselected candidate \(c\), and \(|S|k/n\ge1/h_c\), then at least one voter in \(S\) must approve some selected candidate. The other three reciprocal axioms are those of Boehmer, Dong, Kreisel and Utke [1]. All three imply reciprocal JR; moreover, [1, Section 5 and Appendix G] constructs for each an axiom-satisfying committee that quality-greedily completes a *reciprocally affordable* set \(X\):
\[
\sum_{c\in X}\frac1{h_c}\le k.
\]
The theorem uses these established satisfiability and completion properties, rather than asserting a new algorithm or re-proving the axiom hierarchy.

## Proof
**1. Quality-greedy completion bound.** Let \(X\) be any reciprocally affordable set, and \(X^+\) its size-\(k\) completion with the highest-quality candidates from \(C\setminus X\). Let \(W^*\) be a quality-optimal size-\(k\) committee. Put \(T=X\cap W^*\). If \(T\ne\varnothing\), delete \(T\) from the instance and reduce the committee size to \(k'=k-|T|\). Because every reciprocal cost is at least one, \(X\setminus T\) is still affordable:
\[
\sum_{c\in X\setminus T}h_c^{-1}\le k-\sum_{c\in T}h_c^{-1}\le k-|T|=k'.
\]
The optimal committee in the reduced instance is \(W^*\setminus T\): otherwise adding \(T\) would beat \(W^*\) in the original instance. The completion chooses the same \(k-|X|\) highest-quality candidates of \(C\setminus X\) in either instance. Therefore \(h(X^+)=h(T)+h((X\setminus T)^+)\) and \(h(W^*)=h(T)+h(W^*\setminus T)\). For a target fraction at most one, the disjoint-case bound transfers to the original ratio. If \(k'=0\), the ratio is already one. Hence it suffices to consider \(X\cap W^*=\varnothing\).

Set \(t=|X|\), \(z=t/k\in[0,1]\), and \(B=h(X)\). From the minimum-quality condition and Cauchy–Schwarz,
\[
B\ge qt,\qquad B\,\sum_{c\in X}h_c^{-1}\ge t^2,
\qquad B\ge t^2/k.
\]
The \(k-t\) greedy additions have total quality at least \((k-t)h(W^*)/k\), since \(W^*\) is a size-\(k\) subset of available candidates disjoint from \(X\). Since \(h(W^*)\le k\),
\[
\frac{h(X^+)}{h(W^*)}\ge1-z+\frac B{h(W^*)}\ge1-z+\max\{qz,z^2\}.
\]
For \(0\le z\le q\) the right-hand side is \(1-(1-q)z\), decreasing in \(z\). For \(q\le z\le1\) it is \(1-z+z^2\), decreasing up to \(z=1/2\) and increasing after it. Its global minimum is exactly \(\Phi(q)\). By the cited greedy-completion constructions in [1], this proves the guarantee for reciprocal EJR, reciprocal threshold-PJR+, and reciprocal value-EJR. Each implies reciprocal JR, proving the JR guarantee as well.

**2. Matching worst-case instances.** Fix rational \(r\in[\max\{q,1/2\},1)\). Take any sequence of positive integers \(k\to\infty\) with \(n=rk\in\mathbb N\) and \(n\ge2\). Introduce \(n-1\) disjoint singleton *private* parties: each has one voter who approves exactly one private candidate of quality \(r\). Introduce one final voter who approves exactly \(k\) public candidates, each of quality one. There are \(n\) voters and \(k+n-1\) candidates. Since a private voter has entitlement \(k/n=1/r\), reciprocal JR forces her private candidate to be selected: her singleton group can afford it and approves no other candidate. Therefore **every** reciprocal-JR committee contains the \(n-1\) private candidates; this also applies to any stronger reciprocal axiom. Its quality is at most
\[
(n-1)r+(k-n+1)=k-(1-r)(n-1).
\]
Unrestricted quality optimum is \(k\), selecting all quality-one public candidates. Thus all four axiom-constrained optimal retentions are at most
\[
1-(1-r)\left(r-\frac1k\right).
\]
For a rational \(q\ge1/2\), choose \(r=q\) if \(q<1\). For irrational \(q\ge1/2\), choose rational \(r\downarrow q\); for \(q\le1/2\), choose \(r=1/2\). Taking \(k\to\infty\), and then \(r\downarrow q\) where needed, yields the matching upper bound on each sharp infimum. If \(q=1\), all committees have quality \(k\), so the fraction is one. For completeness, axiom-satisfying committees in every constructed instance exist by the cited results [1]; the upper bound needs only the reciprocal-JR necessity. This proves the formula for every real \(q\in(0,1]\). \(\square\)

## Verification
The accompanying standard-library Python script `check_quality_floor.py` uses exact rational arithmetic. It checks the envelope over rational quality floors, exact minimum candidates and sharp finite witnesses, with asymptotic approach for several rational \(r\). It prints `ALL EXACT CHECKS PASSED (15191 rational tests)` when run. These checks are finite corroboration; the general claim relies on the algebraic arguments above and the explicitly cited existence results.

## Relationship to prior work
Boehmer, Dong, Kreisel and Utke [1, Theorem 5.5, Appendix G] prove the unconstrained \(3/4\) guarantee and its sharpness and show that three stronger reciprocal axioms admit quality-greedy affordable completions. The present result adds the sharp **conditional** dependence on an exogenous lower quality bound \(q\), including a transition at \(1/2\), a strict improvement when \(q>1/2\), and a family attaining the exact worst-case infimum asymptotically. The novelty is the combined \(qt\) and \(t^2/k\) budget envelope and matching many-party witness. Appendix H of [1] concerns a distinct *voter-welfare* objective, not summed candidate quality. No absolute historical-priority claim is made.

## Limitations
The theorem concerns the supremal attainable quality over committees satisfying each axiom; it is not a guarantee for arbitrary axiom-satisfying committees. It assumes exogenous qualities in \((0,1]\), a common positive quality floor, unconstrained size-\(k\) committee selection, and exactly the reciprocal proportionality notions of [1]. The sharpness result is an infimum across growing finite instances; it does not require attainment in a finite instance for \(q<1\). It does not address voter-welfare distortion, arbitrary candidate costs, or alternative fairness axioms. The extremal party-list families have fewer voters than committee seats, which the stated model permits; no sharpness assertion is made after imposing an additional constraint of at least as many voters as seats. Historical priority for the floor-conditioned frontier has not been independently certified.

## References
[1] Niclas Boehmer, Chris Dong, Luca Kreisel, Markus Utke, *Approval-Based Multiwinner Voting with Candidate Qualities*, arXiv:2609.08830, first posted 2026-09-08. https://arxiv.org/abs/2609.08830. Relevant portions: Sections 2, 5.1–5.2, Appendix F.1 and Appendix G (especially Theorem 5.5, Example G.1, Proposition G.3, Proposition G.8 and G.3 value-GCR).
