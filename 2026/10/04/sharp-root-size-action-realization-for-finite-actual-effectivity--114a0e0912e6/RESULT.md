# Sharp root-size action realization for finite actual-effectivity frames

## Finding
Let \(A=\{a_1,\ldots,a_k\}\) with \(k\ge 2\), and let \(F=(W,(\Sigma_i)_{i=1}^k)\) be a finite multi-agent neighborhood frame satisfying the three concurrent-game representability conditions: every \(\Sigma_i(w)\) is nonempty; the unions \(\bigcup\Sigma_i(w)\) are the same for all agents; and every choice \(s_i\in\Sigma_i(w)\) has nonempty intersection \(\bigcap_i s_i\).

For each world \(w\), put
\[
R_w=\bigcup\Sigma_i(w),\qquad r_w=|R_w|,
\]
and define
\[
q_w=\min\{q\ge 1:q^{k-1}\ge r_w\}=\left\lceil r_w^{1/(k-1)}\right\rceil.
\]
Then \(F\) has a concurrent-game realization on the same state set \(W\) in which, at \(w\), each agent \(a_i\) has exactly \(q_w|\Sigma_i(w)|\) available actions and exactly \(q_w\) actions realize each neighborhood \(s\in\Sigma_i(w)\).

The factor \(q_w\) is worst-case sharp. For the frame on \(r\) states with \(\Sigma_i(w)=\{W\}\) for all agents and states, every concurrent-game realization has
\[
\max_i |\operatorname{act}(a_i,w)|\ge \min\{q:q^{k-1}\ge r\}.
\]
Thus the displayed root-size factor is the smallest universal per-neighborhood copy factor in the worst case.

## Assumptions and scope
The frame is finite, there are at least two agents, and the representation target is an ordinary deterministic concurrent game structure on the same state set. The theorem concerns the local number of available actions needed to realize the given actual-effectivity neighborhoods exactly. It does not claim that this construction minimizes action counts for every particular frame.

## Proof
Fix a world \(w\), abbreviate \(R=R_w\), \(r=|R|\), and \(q=q_w\), and let \(Q=\mathbb Z/q\mathbb Z\). Since \(|Q^{k-1}|=q^{k-1}\ge r\), choose a surjection
\[
\pi:Q^{k-1}\twoheadrightarrow R.
\]
Define
\[
H(x_1,\ldots,x_k)=(x_1-x_k,\ldots,x_{k-1}-x_k).
\]
Every one-coordinate slice of \(H\) is a bijection onto \(Q^{k-1}\). If \(x_k\) is fixed and the target is \((y_1,\ldots,y_{k-1})\), take \(x_j=y_j+x_k\). If \(x_i\) is fixed for some \(i<k\), take \(x_k=x_i-y_i\), and for every \(j\ne i,k\) take \(x_j=y_j+x_k\). Hence every one-coordinate slice of \(\pi\circ H\) is surjective onto \(R\).

Give agent \(a_i\) the local action set
\[
\operatorname{act}(a_i,w)=\Sigma_i(w)\times Q.
\]
For each neighborhood tuple \((s_1,\ldots,s_k)\), independence supplies a fixed fallback point
\[
m_w(s_1,\ldots,s_k)\in\bigcap_i s_i.
\]
For an action profile \(((s_1,x_1),\ldots,(s_k,x_k))\), set
\[
z=\pi(H(x_1,\ldots,x_k)).
\]
The outcome is \(z\) when \(z\in\bigcap_i s_i\), and otherwise it is \(m_w(s_1,\ldots,s_k)\).

For a fixed action \((s_i,x_i)\), every compatible profile therefore has outcome in \(s_i\), so its outcome set is contained in \(s_i\). Conversely, let \(u\in s_i\). Uniform range means that for each \(j\ne i\) there is some \(s_j\in\Sigma_j(w)\) containing \(u\). Because the fixed-\(x_i\) slice of \(\pi\circ H\) is onto \(R\), the remaining labels can be chosen so that \(z=u\). Then \(u\in\bigcap_j s_j\), so the outcome is exactly \(u\). Thus the outcome set of \((s_i,x_i)\) is exactly \(s_i\). There are precisely \(q\) such actions for each neighborhood.

For sharpness, take the full-range frame with \(|W|=r\) and \(\Sigma_i(w)=\{W\}\). Write \(d_i=|\operatorname{act}(a_i,w)|\). Fixing one action of agent \(a_i\) leaves only \(\prod_{j\ne i}d_j\) profile completions, yet that action must realize all \(r\) outcomes. Therefore
\[
\prod_{j\ne i}d_j\ge r.
\]
If all \(d_i\le q-1\), then every such product is at most \((q-1)^{k-1}<r\), a contradiction. Hence \(\max_i d_i\ge q\), and the construction above attains equality for this frame.

## Verification
The proof uses only the three representation conditions and the elementary slice-bijection calculation above. A bundled deterministic checker exhaustively verifies the slice lemma for small parameter ranges, reconstructs actual-effectivity frames from many finite deterministic concurrent games, applies the construction, and checks exact equality of all neighborhood families. It also checks the arithmetic used in the worst-case lower bound. The checker returns `VERIFY_OK`.

## Relationship to prior work
Ciardelli's 2026 representation theorem characterizes exactly which multi-agent neighborhood frames arise from concurrent game structures. In its constructive direction, an action realizing a neighborhood \(s\) is paired with a state label \(v\in W\), so the displayed construction uses one state-sized label set per neighborhood. The theorem above leaves that qualitative representation unchanged but replaces the state label by a local root-sized label set whose induced array is surjective on every one-coordinate slice.

Earlier coalition-effectivity representation work, including Goranko and Jamroga's state/path effectivity framework, studies a different upward-closed coalitional abstraction and does not supply the exact individual-action multiplicity bound proved here. Latin-hypercube and quasigroup constructions provide combinatorial background for slice-surjective arrays; no novelty is claimed for that general combinatorial device itself.

## Limitations
The lower bound is worst-case, not a formula for the minimum number of actions for each individual frame. When \(k=2\), the exponent gives \(q_w=r_w\), so there is no asymptotic improvement over a linear label set. The result is purely finite and local; it does not bound the number of states needed for a formula, nor does it by itself improve a decision-complexity upper bound.

## References
1. Ivano Ciardelli, *Inquisitive Action Logic*, arXiv:2606.31866, first public version 2026-06-30; EPTCS 447 (2026), DOI 10.4204/EPTCS.447.13.
2. Valentin Goranko and Wojciech Jamroga, *State and path coalition effectivity models of concurrent multi-player games*, Autonomous Agents and Multi-Agent Systems 30 (2016), DOI 10.1007/s10458-015-9294-4.
3. Billy Child and Ian M. Wanless, *Latin hypercubes with restricted transversals*, arXiv:2605.01813, first public version 2026-05-03.
