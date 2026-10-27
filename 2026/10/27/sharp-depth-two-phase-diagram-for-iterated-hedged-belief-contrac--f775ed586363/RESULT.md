# Sharp depth-two phase diagram for iterated hedged belief contraction

## Finding

For a one-agent finite Kripke model, repeat the same Belardinelli--Zhang hedged contraction on one of the four formulas of modal depth two, \(\Diamond\Box p\), \(\Box\Box p\), \(\Diamond\Diamond p\), or \(\Box\Diamond p\). Let \(h_\varphi(M)\) be the number of strict accessibility-relation updates before the first fixed point. **The four exact worst-case lifetimes, for every \(n\ge3\), are respectively**
\[
\begin{array}{c|cccc}
\varphi&\Diamond\Box p&\Box\Box p&\Diamond\Diamond p&\Box\Diamond p\\
\hline
\max_{|W|=n}h_\varphi&1&2&n-1&n.
\end{array}
\]
For \(n=1\) all four maxima are \(0\); for \(n=2\) all are \(1\). Thus even at exactly the same syntactic modal depth, the order of the box and diamond has a sharp qualitative effect: the lifetime can be uniformly bounded or linear in the model size.

## Assumptions and scope

Let \(M=(W,R,V)\) be any **one-agent** finite Kripke model with nonempty labelled carrier \(W\), cardinality \(n\ge1\), unrestricted \(R\subseteq W\times W\), and fixed truth set \(P=V(p)\). The modal clauses are \(M,w\models\Box\theta\) iff every successor satisfies \(\theta\), and \(M,w\models\Diamond\theta\) iff some successor satisfies \(\theta\); the empty conjunction is true and the empty disjunction false.

For any fixed \(\varphi\), put \(T_t=\{w:M_t,w\models\varphi\}\) and \(N_t=W\setminus T_t\), starting at \(M_0=M\). The hedged update is
\[
R_{t+1}(w)=\begin{cases}R_t(w)\cup N_t,&w\in T_t,\\ R_t(w),&w\in N_t.\end{cases}
\]
Valuations and worlds never change. We define \(h_\varphi(M)\) to be the least \(t\ge0\) with \(R_{t+1}=R_t\). Equivalently, there have been exactly \(t\) strict global relation updates. All maxima range over both the relation and the valuation; formulas are not reinterpreted as announcements deleting worlds.

## Proof

**Common observation.** If \(T_{t+1}=T_t\), then after the update at stage \(t\) the active rows already contain \(N_t=N_{t+1}\), while inactive rows have not changed. Consequently \(R_{t+2}=R_{t+1}\). In particular, the only way to have two strict updates after the first is for the formula's truth set to change.

**Case \(\Diamond\Box p\): bound one.** Write \(G_t=\{w:R_t(w)\subseteq P\}\) for the \(\Box p\)-worlds. As relations expand, \(G_{t+1}\subseteq G_t\). Here \(T_t=\{w:R_t(w)\cap G_t\ne\varnothing\}\). If \(N_0\cap G_0\ne\varnothing\), choose \(y\) in that intersection. Its row is not updated, so \(y\in G_1\), and every initially true world now sees \(y\), hence remains true; initially false worlds have unchanged rows and cannot become true because \(G_1\subseteq G_0\). Thus \(T_1=T_0\). Otherwise \(N_0\cap G_0=\varnothing\). If \(N_0\subseteq P\), then adding these worlds does not destroy any \(\Box p\)-world, so \(G_1=G_0\) and again \(T_1=T_0\). If \(N_0\not\subseteq P\), every initially \(\Box p\)-world belongs to \(T_0\) and loses \(\Box p\) when updated; hence \(G_1=\varnothing\) and \(T_1=\varnothing\). In every subcase a second strict update is impossible. The two-world model \(P=\{1\}\), \(R(0)=\varnothing\), \(R(1)=\{1\}\) changes strictly once.

**Case \(\Box\Box p\): bound two.** Use the same decreasing \(G_t\), but now \(T_t=\{w:R_t(w)\subseteq G_t\}\). The initially false rows are unchanged in stage zero, and any decrease of \(G_t\) cannot make those rows true, so \(T_1\subseteq T_0\). If \(N_0\subseteq P\), then \(G_1=G_0\). Either \(N_0\subseteq G_0\), in which case \(T_1=T_0\), or \(N_0\not\subseteq G_0\), in which case every initial true row becomes false and \(T_1=\varnothing\). Similarly, when \(N_0\not\subseteq P\), every initially true row acquires a non-\(p\) successor and becomes non-\(G_1\); every false row is unchanged. If in addition \(N_0\not\subseteq G_0\), all initially true rows become false at stage one. In the remaining case \(N_0\subseteq G_0\) and \(N_0\not\subseteq P\), the initially true rows become non-\(G_1\), whereas initially false rows keep their old \(G_0\)-status. If \(T_1=T_0\), stabilization follows from the common observation. Otherwise the newly false set \(T_0\setminus T_1\) is nonempty and consists of non-\(G_1\) worlds. Each surviving true row receives all of this set in the stage-one update, and therefore becomes false at stage two. Thus \(T_2=\varnothing\) and no third strict update is possible.

For sharpness on three worlds take \(P=\{1\}\), \(R(0)=\varnothing\), \(R(1)=\{0\}\), and \(R(2)=\{1\}\). The successive true sets are \(T_0=\{0,1\}\), \(T_1=\{0\}\), \(T_2=\varnothing\), and both updates are strict. For every larger size, clone world \(2\) into any number of bisimilar copies, duplicating its incoming and outgoing edges accordingly. The quotient to the original three-world model remains a bounded morphism at each update, since the set of false worlds is saturated in clone fibers. Hence both strict updates persist and no more than two are possible.

**Case \(\Diamond\Diamond p\): bound \(n-1\).** Let \(D_t=\{w:R_t(w)\cap P\ne\varnothing\}\); both \(D_t\) and \(T_t=\{w:R_t(w)\cap D_t\ne\varnothing\}\) are increasing in \(t\). If there is any strict update then \(T_0\ne\varnothing\), so \(|N_0|\le n-1\). After the first update, each further strict update requires a newly true world, by the common observation. Each time there is still an active row and an actual new target, so the false set \(N_t\) is nonempty; the process cannot add an edge at the step when \(T_t=W\). Accordingly at most \(|N_0|-1\le n-2\) additional strict updates can occur. Total: at most \(n-1\).

For every \(n\ge3\), take the directed cycle \(R(i)=\{(i+1)\bmod n\}\) with \(P=\{0\}\). Initially the only true world is \(n-2\); after each strict update one predecessor becomes newly true. The relation strictly changes for exactly \(n-1\) stages, and then the false set is empty. For \(n=2\), a one-step witness is \(P=\{1\}\), \(R(0)=\varnothing\), \(R(1)=\{1\}\).

**Case \(\Box\Diamond p\): bound \(n\).** Again \(D_t=\{w:R_t(w)\cap P\ne\varnothing\}\) is increasing, now \(T_t=\{w:R_t(w)\subseteq D_t\}\). Suppose a strict update occurs but \(D_{t+1}=D_t\). If \(N_t\subseteq D_t\), all initially true rows remain true on adding \(N_t\), and initially false rows stay false, because their rows and \(D_t\) are unchanged. Thus \(T_{t+1}=T_t\) and that strict update is terminal. If \(N_t\not\subseteq D_t\), fix a world \(y\in N_t\setminus D_t\). Its row is unchanged, hence \(y\notin D_{t+1}\), and every initially true row gains \(y\), so becomes false. Initially false rows stay false. Thus \(T_{t+1}=\varnothing\) and that update is terminal. In short, every strict update except possibly the last strictly enlarges \(D\). If \(D_t\) first becomes all of \(W\), then \(T_t=W\) and no further strict update occurs; otherwise at most \(n-1\) enlargements followed by a terminal update are possible. Hence \(h\le n\).

For sharpness when \(n\ge3\), use the directed path \(R(i)=\{i+1\}\) for \(i<n-1\), \(R(n-1)=\varnothing\), and \(P=\{0\}\). At successive stages \(t=0,1,\ldots,n-1\), the unique true world is \(n-1-t\). Each such row adds at least one new target, so there are exactly \(n\) strict updates. For \(n=2\), take \(P=\varnothing\), \(R(0)=\varnothing\), \(R(1)=\{0\}\), which has exactly one strict update.

Finally, for \(n=1\) the update never changes the relation, since either \(T=W\), whence \(N=\varnothing\), or \(T=\varnothing\), whence no rows update. The \(n=2\) one-step upper bounds for all four formulas also follow from direct inspection of the \(16\) labelled binary relations and the \(4\) valuations of \(p\), exhaustively checked by the accompanying executable enumerator.

## Verification

The standalone `checker.py` enumerates **every** one-agent relation and every valuation on \(n=1,2,3,4\) labelled worlds: respectively \(2^{n^2+n}\) cases per size. The exact maximum for each of the four formulas agrees with the theorem. These are exhaustive finite checks, not an infinite proof. It additionally checks explicit sharp paths for \(3\le n\le35\), directed cycles for \(3\le n\le35\), and cloning-based sharp two-step examples. The uniform bounds for arbitrary \(n\) rest on the preceding symbolic arguments, not on enumeration.

## Relationship to prior work

Belardinelli and Zhang (2026) defined this precise global-falsifier hedged contraction and its modal reduction axioms, and studied preservation, not the simultaneous sharp lifespan classification for all four nested one-variable depth-two triggers. A previously published result on iterating the trigger \(\Diamond p\) gives a sharp general size-dependent bound for that distinct depth-one formula; it does not imply the two constant-time bounds or this complete order-sensitive classification. Published results on idempotence of factual/propositional contraction do not apply to nested modal inputs, whose truth sets are altered by the update. The frame-shrinking dynamics of public announcements are directionally different.

## Limitations

The result is for exactly one agent, one fixed atom and the four positive modal words of **length two**. It does not classify Boolean combinations, alternating contractions, arbitrary-depth inputs, multi-agent iterations or representation-independent semantic changes. The \(n=2\) exceptional bound is independently certified by exhaustive finite case inspection. Priority risk remains from older work on iterated epistemic updates under different terminology; the published sources inspected did not show an equivalent full classification. No independent audit has been performed.

## References

1. Gaia Belardinelli and Snow Zhang, *Belief Contraction in Dynamic Epistemic Logic*, arXiv:2606.31861v1, first posted 2026-06-30, especially Definition 4.1, Theorem 4.2 and Section 5. https://arxiv.org/abs/2606.31861
2. *Idempotence and exact commutation of propositional hedged contractions*, published published-finding corpus finding, identifier `2026/10/4/SCOPE-idempotence-and-exact-commutation-of-propositional-hedged-contra--cac8fc2eab7c`.
3. *Sharp state-count stabilization bound for finite believed announcements*, published published-finding corpus finding, identifier `2026/10/4/SCOPE-sharp-state-count-stabilization-bound-for-finite-believed-announ--65b4b662c65e`.
