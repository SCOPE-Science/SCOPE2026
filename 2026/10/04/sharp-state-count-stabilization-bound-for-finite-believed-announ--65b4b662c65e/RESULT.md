# Sharp state-count stabilization bound for finite believed announcements
## Finding

Let
\[
M=(W,\{R_i\}_{i\in G},V)
\]
be a model with finite state set \(W\), and fix any formula \(\varphi\).

Under believed public announcement, the source paper updates each accessibility relation by
\[
R_i^{k+1}
=
R_i^k
\cap
\bigl(
W\times\llbracket\varphi\rrbracket_{M^k}
\bigr).
\]

Define the set of **active targets**
\[
T_k
=
\left\{
v\in W:
\exists i\in G\,
\exists u\in W\;
(u,v)\in R_i^k
\right\}.
\]

Then the iteration reaches a fixed model after at most
\[
|T_0|
\]
strict updates:
\[
\boxed{
\exists k\le |T_0|\le |W|
\quad
M^k=M^{k+1}.
}
\]

This bound is independent of the number of agents and of the number of labelled arrows.

It is also sharp. For every
\[
n\ge1,
\]
there is an \(n\)-state, one-agent model and a fixed formula for which the first fixed stage is exactly
\[
n.
\]

Take the directed cycle
\[
0R1,\ 1R2,\ \ldots,\ (n-2)R(n-1),\ (n-1)R0,
\]
let \(p\) be false exactly at \(n-1\), and announce repeatedly
\[
\varphi
=
p\land\neg\Box\bot.
\]
At each stage exactly one new target loses all incoming arrows. The final arrow disappears at the \(n\)-th update, and the relation is then empty and fixed.

Thus the source paper's general transfinite stabilization proposition has the following sharp finite-state refinement:
\[
\boxed{
\text{finite state space}
\Longrightarrow
\text{stabilization by stage }|W|,
}
\]
with the stronger bound \(|T_0|\) whenever not every state is initially targeted.

## Assumptions and scope

The update is the believed-public-announcement update of Yamada's Definition 5: states and valuations remain fixed while every agent's relation keeps only arrows whose target satisfies the announced formula in the current model.

No frame property such as transitivity, Euclideanness, seriality, or reflexivity is assumed. The upper bound therefore applies to the general models covered by the source's Proposition 3.

The sharpness example is likewise a general-model example. It is not claimed to be a sharp example inside the paper's later \(K45\) subclasses, where additional frame structure can force faster stabilization.

The agent set may be arbitrary. Finiteness is required only for the state set \(W\).

## Proof

Write
\[
M^k=(W,\{R_i^k\}_{i\in G},V).
\]

Because every update is an intersection,
\[
R_i^{k+1}\subseteq R_i^k
\]
for every agent \(i\). Hence
\[
T_{k+1}\subseteq T_k.
\]

Suppose the update at stage \(k\) is strict:
\[
M^k\ne M^{k+1}.
\]
Then some labelled arrow
\[
(u,v)\in R_i^k
\]
is deleted. By the update rule, this can happen only because
\[
M^k,v\not\models\varphi.
\]

The same target test is used for every source and every agent. Therefore **all** remaining arrows into \(v\) are deleted at this update:
\[
(u',v)\notin R_j^{k+1}
\]
for every \(u'\in W\) and every \(j\in G\).

Since \((u,v)\in R_i^k\), we had
\[
v\in T_k.
\]
After the update no incoming arrow to \(v\) remains, so
\[
v\notin T_{k+1}.
\]

Thus every strict update gives a strict inclusion
\[
T_{k+1}\subsetneq T_k.
\]

The finite set \(T_0\) can strictly decrease at most
\[
|T_0|
\]
times. Consequently there is some
\[
k\le |T_0|
\]
such that the update is no longer strict:
\[
M^k=M^{k+1}.
\]

Since
\[
T_0\subseteq W,
\]
we also have
\[
k\le |W|.
\]

For sharpness, fix
\[
n\ge1
\]
and let
\[
W=\{0,1,\ldots,n-1\}.
\]
Use one agent and the directed cycle relation
\[
jR(j+1\bmod n).
\]
Let
\[
V(p)=W\setminus\{n-1\},
\]
and put
\[
\varphi=p\land\neg\Box\bot.
\]

At stage \(0\), every state has a successor, so the only \(\varphi\)-false state is \(n-1\). The first update therefore deletes exactly the arrow into \(n-1\).

After that deletion, \(n-2\) has no successor, so
\[
n-2\models\Box\bot
\]
and hence
\[
n-2\not\models\varphi.
\]
The second update deletes the unique arrow into \(n-2\).

Inductively, after \(r\) updates, exactly the targets
\[
n-r,\ldots,n-1
\]
have lost all incoming arrows, and the next newly false target is
\[
n-r-1.
\]

After
\[
n-1
\]
updates, state \(0\) is a sink, so the \(n\)-th update removes the final arrow
\[
(n-1)R0.
\]
The relation is then empty. The next update changes nothing, so
\[
M^n=M^{n+1},
\]
while
\[
M^r\ne M^{r+1}
\qquad(0\le r<n).
\]

Hence the first fixed stage is exactly
\[
n=|W|=|T_0|.
\]

## Verification

The bundled checker verifies the combinatorial step independently of modal syntax.

For every one-agent relation on carriers of size at most four and every possible truth set \(S\subseteq W\), it applies the abstract update
\[
R\longmapsto R\cap(W\times S)
\]
and checks that whenever the update is strict, the active-target set strictly shrinks.

It then constructs the directed-cycle sharpness family for
\[
1\le n\le12
\]
and evaluates
\[
\varphi=p\land\neg\Box\bot
\]
from the current relation at every round. It confirms that the earliest fixed stage is exactly \(n\).

The finite replay corroborates the proof. The general upper bound does not rely on enumerating formulas or agents.

## Relationship to prior work

Yamada's Proposition 3 proves stabilization for arbitrary models by counting labelled arrows. If
\[
E=\{(i,u,v):(u,v)\in R_i\},
\]
the source obtains a fixed stage below
\[
|E|^+.
\]

For finite state spaces, the target structure of the believed-public-announcement update gives a substantially sharper invariant. A strict update cannot merely remove an isolated labelled arrow: it removes every currently surviving incoming arrow to each target at which the announcement is false. Therefore the relevant finite resource is the number of targeted states, not the number of labelled arrows.

The source later proves a separate finite-stabilization lemma for single-agent \(K45\) generated models using propositional valuation types. That result exploits \(K45\) structure and serves a different purpose. The theorem here applies to every finite-state model, with any agent set, and gives a sharp state-count bound for the general update process itself.

Targeted searches for a finite state-count bound, an active-target formulation, and a sharp \(n\)-round believed-announcement example did not locate an equivalent statement.

## Limitations

The bound is a worst-case statement over general finite models. It need not be sharp in \(K45\), \(KD45\), or \(S5\) subclasses.

For infinite state spaces, the active-target argument still shows that every strict successor step removes at least one target, but it does not turn the transfinite process into a finite one.

The theorem bounds the number of strict model updates, not the syntactic complexity of deciding the truth set
\[
\llbracket\varphi\rrbracket_{M^k}
\]
at each stage.

The sharpness witness uses a directed cycle and therefore does not establish a matching lower bound under epistemic frame conditions.

## References

[1] Eiji Yamada, “Eventual and Strong Eventual Notions in Public Announcements,” arXiv:2609.24006, first posted 21 September 2026.
