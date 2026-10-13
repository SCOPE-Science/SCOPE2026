# Narrow-system pruning depends on cofinality, not regularity
## Finding

Let \(\kappa\) be an uncountable cardinal, not necessarily regular. Let \(T\) be a tree of height \(\kappa\), and let
\[
S=\langle S_\alpha:\alpha\in I\rangle
\]
be a subsystem of \(T\), where \(I\subseteq\kappa\) is unbounded. Write
\[
\theta=\operatorname{width}(S)
\]
and define
\[
\lambda_\theta=\max(\omega,\theta^+).
\]

If
\[
\lambda_\theta<\operatorname{cf}(\kappa),
\]
then \(T\) contains a well-pruned subtree of height \(\kappa\).

For infinite \(\theta\), the hypothesis is simply
\[
\theta^+<\operatorname{cf}(\kappa).
\]
For finite \(\theta\), it becomes
\[
\omega<\operatorname{cf}(\kappa).
\]

When \(\kappa\) is regular uncountable and \(S\) is narrow in Adkisson's sense, the hypothesis follows automatically. The statement therefore recovers the one-cardinal pruning theorem in the source and extends it to singular heights of sufficiently large cofinality relative to the subsystem width.

## Assumptions and scope

A tree \(T\) of height \(\kappa\) is ordered so that the predecessors of each node form a well-order. Its \(\alpha\)-th level is denoted by \(T_\alpha\).

A subtree \(U\subseteq T\) is well-pruned of height \(\kappa\) when every node of \(U\) has an extension in \(U\) on every higher level below \(\kappa\).

A subsystem
\[
S=\langle S_\alpha:\alpha\in I\rangle
\]
has \(I\subseteq\kappa\) unbounded, each \(S_\alpha\subseteq T_\alpha\), and for every \(\alpha<\beta\) in \(I\) there are
\[
x\in S_\alpha,\qquad y\in S_\beta
\]
with \(x\le_T y\). Its width is
\[
\theta=\sup_{\alpha\in I}|S_\alpha|.
\]

No regularity of \(\kappa\) is assumed. The only cardinal-arithmetic input in the proof is that fewer than \(\operatorname{cf}(\kappa)\) ordinals below \(\kappa\) have supremum below \(\kappa\).

## Proof

Assume toward a contradiction that \(T\) has no well-pruned subtree of height \(\kappa\).

### Pruning ranks without regularity

Define a decreasing transfinite sequence of subtrees:
\[
T^0=T.
\]
Given \(T^\xi\), let \(T^{\xi+1}\) consist of those nodes \(x\in T^\xi\) whose cone inside \(T^\xi\) meets every higher level below \(\kappa\). At a limit ordinal \(\eta\), set
\[
T^\eta=\bigcap_{\xi<\eta}T^\xi.
\]

If
\[
T^\xi=T^{\xi+1},
\]
then \(T^\xi\) is either empty or is itself a well-pruned subtree of height \(\kappa\). The sequence must stabilize before \(|T|^+\), because every strict successor step removes at least one node. Since \(T\) has no well-pruned subtree, the stable value is empty.

Hence every node \(x\in T\) has a least removal stage
\[
r(x)=\min\{\xi:x\notin T^\xi\}.
\]
This stage is a successor, say
\[
r(x)=\eta+1,
\]
because the limit stages are intersections. Since \(x\) is removed at stage \(\eta+1\), its cone inside \(T^\eta\) is bounded. Therefore there is an ordinal
\[
\delta_x<\kappa
\]
such that every descendant \(y\ge_T x\) with
\[
\operatorname{ht}(y)\ge\delta_x
\]
satisfies
\[
r(y)<r(x).
\]
Indeed, beyond \(\delta_x\) there is no descendant of \(x\) remaining in \(T^\eta\).

This rank-decrease fact is the only pruning property needed below, and its proof uses no regularity assumption on \(\kappa\).

### A cone-covering claim

We claim that there exists some \(\alpha\in I\) such that for every set
\[
A\subseteq T_\alpha,\qquad |A|\le\theta,
\]
and every \(\gamma_0<\kappa\), there is a \(\beta\in I\) with
\[
\beta\ge\gamma_0
\]
for which no member of \(S_\beta\) lies above a member of \(A\).

Suppose not. Then for every \(\alpha\in I\) there are
\[
A_\alpha\subseteq T_\alpha,\qquad |A_\alpha|\le\theta,
\]
and \(\gamma_\alpha<\kappa\) such that, whenever \(\beta\in I\) and
\[
\beta\ge\gamma_\alpha,
\]
the level \(S_\beta\) meets
\[
\bigcup_{x\in A_\alpha}C_T(x).
\]

Put
\[
\lambda=\lambda_\theta=\max(\omega,\theta^+).
\]
By hypothesis,
\[
\lambda<\operatorname{cf}(\kappa).
\]

Construct a strictly increasing sequence
\[
\langle\alpha_\xi:\xi<\lambda\rangle
\]
of members of \(I\). At a successor stage, after choosing \(\alpha_\xi\), choose \(\alpha_{\xi+1}\in I\) above
\[
\alpha_\xi
\]
and above every \(\delta_x\) for
\[
x\in A_{\alpha_\xi}.
\]
This is possible because
\[
|A_{\alpha_\xi}|\le\theta<\operatorname{cf}(\kappa).
\]
At a limit stage \(\zeta<\lambda\), choose \(\alpha_\zeta\in I\) above
\[
\sup_{\xi<\zeta}\alpha_\xi.
\]
This supremum is below \(\kappa\) because
\[
\zeta<\lambda<\operatorname{cf}(\kappa).
\]

Again using
\[
\lambda<\operatorname{cf}(\kappa),
\]
choose a single \(\gamma\in I\) above every \(\alpha_\xi\) and every \(\gamma_{\alpha_\xi}\) for \(\xi<\lambda\).

For each \(y\in S_\gamma\), define
\[
B_y=
\left\{
\xi<\lambda:
(\exists x\in A_{\alpha_\xi})\ x\le_T y
\right\}.
\]

Every \(B_y\) is finite. Otherwise choose an increasing sequence
\[
\xi_0<\xi_1<\xi_2<\cdots
\]
from \(B_y\), and for each \(n\) choose
\[
x_n\in A_{\alpha_{\xi_n}}
\]
with \(x_n\le_T y\). Since the \(x_n\) are predecessors of the same node and their levels strictly increase,
\[
x_0<_T x_1<_T x_2<_T\cdots.
\]
The construction of the \(\alpha_\xi\)'s ensures that \(x_{n+1}\) lies above the rank-drop threshold for \(x_n\). Consequently,
\[
r(x_0)>r(x_1)>r(x_2)>\cdots,
\]
an impossible infinite descending sequence of ordinals.

On the other hand, the assumed cone-covering property says that for every \(\xi<\lambda\),
\[
S_\gamma\cap
\bigcup_{x\in A_{\alpha_\xi}}C_T(x)
\neq\varnothing.
\]
Hence
\[
\lambda=\bigcup_{y\in S_\gamma}B_y.
\]

But
\[
|S_\gamma|\le\theta.
\]
If \(\theta\) is finite, a union of at most \(\theta\) finite sets is finite and cannot equal
\[
\lambda=\omega.
\]
If \(\theta\) is infinite, such a union has cardinality at most \(\theta\) and cannot equal
\[
\lambda=\theta^+.
\]
This contradiction proves the cone-covering claim.

### Contradiction with subsystem coherence

Take the \(\alpha\in I\) supplied by the claim and set
\[
A=S_\alpha.
\]
Then
\[
|A|\le\theta.
\]
The claim yields arbitrarily high \(\beta\in I\) for which no member of \(S_\beta\) lies above any member of \(S_\alpha\).

This contradicts the subsystem axiom requiring that, for every
\[
\alpha<\beta
\]
in \(I\), some
\[
x\in S_\alpha,\qquad y\in S_\beta
\]
satisfy \(x\le_T y\).

Therefore \(T\) contains a well-pruned subtree of height \(\kappa\).

## Verification

The primary source was inspected at its definitions of trees, systems, subsystems, fanlike trees and well-pruned trees, together with the pruning lemmas and Theorem 3.13.

Adkisson's Theorem 3.13 assumes that \(\kappa\) is regular and derives a well-pruned subtree from a narrow subsystem. Its proof uses a long sequence of indexed levels and then takes suprema of the associated bounds. The argument above reconstructs this mechanism without importing regularity wholesale: every supremum is taken over a family of size strictly below
\[
\operatorname{cf}(\kappa).
\]

The pruning-rank argument was rebuilt directly rather than assuming that the source's fanlike definitions, which are introduced under a regularity convention, automatically extend to singular heights.

The finite-width case is treated separately through
\[
\lambda_\theta=\max(\omega,\theta^+),
\]
so that the rank-descent contradiction always has an infinite sequence available.

No finite experiment, external computation, or unproved cardinal-arithmetic assumption is used.

## Relationship to prior work

Adkisson proves the regular-height theorem and develops the pruning/fanlike machinery that motivates it. The paper explicitly formulates the one-cardinal framework with regular \(\kappa\) and does not state a singular-height or cofinality-local version of Theorem 3.13.

Lambie-Hanson's earlier work studies narrow systems and generalized narrow system properties, especially at regular cardinals and in applications to successors of singular cardinals. It supplies the broader set-theoretic context but does not state the present width-versus-cofinality pruning criterion.

Targeted searches for singular-height narrow systems, cofinality versions of the well-pruned-subtree theorem, and fanlike-tree formulations did not locate an equivalent statement.

The point of the finding is therefore not a new forcing construction but an exact localization of the regularity used by the recent pruning theorem: the proof only needs enough cofinality to dominate the width and the length of the rank-descent counting argument.

## Limitations

The condition
\[
\max(\omega,\theta^+)<\operatorname{cf}(\kappa)
\]
is sufficient; no claim of sharpness is made.

The result does not cover singular heights whose cofinality is too small relative to the subsystem width.

It concerns ordinary one-cardinal tree subsystems. The two-cardinal part of the source uses additional closure structure, and no analogous singular-parameter extension is asserted here.

The theorem guarantees a well-pruned subtree, not a cofinal branch.

## References

[1] William Adkisson, “A Note on Narrow Systems,” arXiv:2610.00934v1, first posted 1 October 2026.

[2] Chris Lambie-Hanson, “Narrow systems revisited,” arXiv:2304.02132; *Bulletin of the London Mathematical Society* 56 (2024), 1645–1668.
