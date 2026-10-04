# Sharp local-range compression for actual-effectivity representations
## Finding

Ciardelli's representation theorem for actual effectivity functions constructs, from a suitable multi-agent neighborhood frame, a concurrent game structure whose individual-agent output sets are exactly the prescribed neighborhoods.

For a finite frame, the construction can be compressed from the ambient state space to the **local reachable range**.

Let
\[
F=(W,(\Sigma_a)_{a\in\mathcal A})
\]
be a finite multi-agent neighborhood frame with
\[
|\mathcal A|>1
\]
satisfying the three conditions in Theorem 2.2 of the source at every world \(w\):

\[
\Sigma_a(w)\ne\varnothing,
\]
\[
\bigcup\Sigma_a(w)=\bigcup\Sigma_b(w)
\quad\text{for all }a,b,
\]
and, for every choice
\[
s_a\in\Sigma_a(w),
\]
\[
\bigcap_{a\in\mathcal A}s_a\ne\varnothing.
\]

Write the common local range as
\[
O(w)=\bigcup\Sigma_a(w).
\]

Then there is a representing concurrent game structure with
\[
\boxed{
|\operatorname{act}(a,w)|
=
|\Sigma_a(w)|\,|O(w)|
}
\]
for every agent \(a\) and world \(w\).

Thus the ambient multiplicative factor
\[
|W|
\]
in the source construction can be replaced by
\[
|O(w)|.
\]

The improvement is sharp in the worst case. For every integer
\[
r\ge1,
\]
there is a two-agent local frame with
\[
|O(w)|=r
\]
and one neighborhood per agent such that **every** deterministic concurrent game structure representing it requires at least
\[
r
\]
actions for each agent.

Hence no smaller universal multiplicative factor than the local range size can replace
\[
|O(w)|
\]
in a representation theorem of this form.

## Assumptions and scope

The result uses the deterministic concurrent game structures of the source paper: at a world \(w\), every complete action profile has one outcome
\[
\operatorname{out}(w,\tau)\in W.
\]

The neighborhood maps are the individual-agent **actual effectivity functions**:
\[
\Sigma_a(w)
=
\{
O_a(w,\tau_a):
\tau_a\in\operatorname{act}(a,w)
\},
\]
where
\[
O_a(w,\tau_a)
=
\{
\operatorname{out}(w,\tau):
\tau(a)=\tau_a
\}.
\]

The theorem concerns finite \(W\). Finiteness lets us put an explicit cyclic group structure on every local range \(O(w)\), avoiding any choice principle.

The sharpness statement is a worst-case statement. It does not claim that
\[
|\Sigma_a(w)|\,|O(w)|
\]
is the minimum action count for every representable neighborhood frame. Many frames admit smaller realizations.

## Proof

Fix a world \(w\).

By uniform range,
\[
O(w)=\bigcup\Sigma_a(w)
\]
does not depend on the agent.

By existence of actions and independence, \(O(w)\) is nonempty. Indeed, choose one neighborhood for each agent. Their intersection is nonempty, so each chosen neighborhood and therefore their common union is nonempty.

Because \(O(w)\) is finite, choose a cyclic group structure on it. We write the group operation multiplicatively, with identity \(e_w\).

For every agent \(a\), define
\[
\operatorname{act}(a,w)
=
\{
(s,v):
s\in\Sigma_a(w),\ v\in O(w)
\}.
\]

Therefore
\[
|\operatorname{act}(a,w)|
=
|\Sigma_a(w)|\,|O(w)|.
\]

Consider an action profile
\[
\tau=
((s_1,v_1),\ldots,(s_k,v_k)),
\]
where
\[
\mathcal A=\{a_1,\ldots,a_k\}.
\]

Independence guarantees
\[
I_\tau=s_1\cap\cdots\cap s_k\ne\varnothing.
\]

Fix any ordering of the finite set \(O(w)\). Define
\[
\operatorname{out}(w,\tau)
=
\begin{cases}
v_1\cdots v_k,
&
v_1\cdots v_k\in I_\tau,
\\
\min(I_\tau),
&
v_1\cdots v_k\notin I_\tau.
\end{cases}
\]

Since every neighborhood is a subset of \(O(w)\), the output is always an element of \(O(w)\subseteq W\).

We prove that the output set of every action
\[
(s,v)\in\operatorname{act}(a,w)
\]
is exactly \(s\).

The inclusion
\[
O_a(w,(s,v))\subseteq s
\]
is immediate: every profile containing \((s,v)\) has its outcome in the intersection of the selected neighborhoods, hence in \(s\).

For the reverse inclusion, fix
\[
u\in s.
\]
Suppose, without loss of generality, that
\[
a=a_1,
\qquad
(s_1,v_1)=(s,v).
\]

Because
\[
u\in s_1\subseteq O(w),
\]
uniform range implies that for each
\[
i>1
\]
there is some
\[
s_i\in\Sigma_{a_i}(w)
\]
with
\[
u\in s_i.
\]

Choose arbitrary
\[
v_2,\ldots,v_{k-1}\in O(w),
\]
and then choose
\[
v_k
=
(v_1\cdots v_{k-1})^{-1}u.
\]

This element belongs to the cyclic group \(O(w)\), so
\[
(s_k,v_k)
\]
is a legal action.

For the resulting profile,
\[
u\in s_1\cap\cdots\cap s_k
\]
and
\[
v_1\cdots v_k=u.
\]
Therefore the first branch of the outcome rule applies and
\[
\operatorname{out}(w,\tau)=u.
\]

Since \(u\in s\) was arbitrary,
\[
s\subseteq O_a(w,(s,v)).
\]

Hence
\[
O_a(w,(s,v))=s.
\]

It follows that
\[
\Sigma_a^{\mathcal S}(w)=\Sigma_a(w)
\]
for every agent and world, so the constructed concurrent game structure represents the original neighborhood frame.

The argument is the source construction with one precise change: the auxiliary coordinate ranges over \(O(w)\), not over all of \(W\). The proof still goes through because every outcome that must be realized already belongs to \(O(w)\).

For sharpness, fix
\[
r\ge1
\]
and a set \(O\) with
\[
|O|=r.
\]

Consider two agents \(a,b\) at a world \(w\) with
\[
\Sigma_a(w)=\Sigma_b(w)=\{O\}.
\]

Suppose a deterministic concurrent game structure represents this local frame. Let
\[
m_a=|\operatorname{act}(a,w)|,
\qquad
m_b=|\operatorname{act}(b,w)|.
\]

Every action of agent \(a\) must have exact output set \(O\), because \(O\) is the only member of \(\Sigma_a(w)\).

Fix one action of \(a\). As \(b\) varies its action, there are only
\[
m_b
\]
joint profiles containing the fixed action of \(a\). Each profile has one outcome. Therefore that action can have at most
\[
m_b
\]
distinct possible outcomes.

Its output set must nevertheless contain all
\[
r
\]
elements of \(O\). Hence
\[
m_b\ge r.
\]

By symmetry,
\[
m_a\ge r.
\]

The compressed construction above has exactly
\[
r
\]
actions for each agent in this example, so the lower bound is attained.

## Verification

The bundled checker exhaustively checks the construction for all two-agent local neighborhood frames on carriers of size at most three satisfying:

\[
\Sigma_a\ne\varnothing,
\]
common union, and cross-agent independence.

For each such frame it builds the compressed cyclic-group realization and verifies, action by action, that the induced output-set family is exactly the original neighborhood family.

It also exhaustively checks all three-agent admissible local frames on two-element carriers.

Finally, for every
\[
1\le r\le12,
\]
it checks the sharpness family
\[
\Sigma_a=\Sigma_b=\{O\},
\qquad
|O|=r,
\]
verifying that the cyclic construction uses exactly \(r\) actions per agent and that the elementary slice-cardinality lower bound excludes any smaller action set.

The script prints `VERIFY_OK`.

## Relationship to prior work

Ciardelli's 2026 representation theorem characterizes exactly which systems of individual-agent actual effectivity functions arise from deterministic concurrent game structures. In the constructive direction, the paper defines
\[
\operatorname{act}(a,w)
=
\{
(s,v):
s\in\Sigma_a(w),\ v\in W
\},
\]
equips \(W\) with a group structure, and uses a product-or-fallback rule to realize every element of every selected neighborhood intersection.

The present result observes that the proof never needs auxiliary values outside the common local outcome range
\[
O(w)=\bigcup\Sigma_a(w).
\]
Replacing the group on \(W\) by a cyclic group on \(O(w)\) gives the smaller action space while preserving the proof verbatim at the substantive step.

Chen, Ju, and Ågotnes also study representation of actual powers in concurrent game frames in 2026, particularly in the two-agent setting and across variants obtained by relaxing seriality, independence, and determinism. Their framework is broader at the coalition level and permits generalized outcome behavior. The checked material does not give the local-range action-count refinement for Ciardelli's deterministic individual-agent construction.

Earlier work on basic powers characterizes which families of exact outcome sets arise from games, but the checked representation statements do not provide the local action-count bound or its sharp worst-case lower bound.

Targeted searches for minimal action counts, local-range compression, and action-cardinality bounds in actual-effectivity representations did not locate this refinement.

## Limitations

The result sharpens one representation construction; it does not solve the minimum-action realization problem for an arbitrary actual-effectivity frame.

The worst-case optimality proof uses two agents with a single common neighborhood. Frames with many neighborhoods, small individual neighborhoods, or additional combinatorial structure can require far fewer actions than the displayed upper bound.

The theorem is stated for deterministic concurrent game structures. Generalized game frames with set-valued outcomes can have different action-count behavior.

The result concerns individual-agent actual effectivity functions, matching the source theorem. It does not characterize minimal action counts for proper coalitions.

## References

[1] Ivano Ciardelli, “Inquisitive Action Logic,” arXiv:2606.31866, first posted 30 June 2026.

[2] Zixuan Chen, Fengkui Ju, and Thomas Ågotnes, “Representation theorems for actual and alpha powers over two-agent general concurrent game frames,” arXiv:2603.04160, first posted 4 March 2026.

[3] Johan van Benthem, Nick Bezhanishvili, and Sebastian Enqvist, “A New Game Equivalence, its Logic and Algebra,” *Journal of Philosophical Logic* 48 (2019), 649–684.
