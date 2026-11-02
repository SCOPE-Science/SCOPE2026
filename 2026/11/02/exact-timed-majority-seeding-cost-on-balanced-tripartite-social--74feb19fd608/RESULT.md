# Exact timed majority-seeding cost on balanced tripartite social networks

## Finding

Let \(G=K_{m,m,m}\) be the complete tripartite graph with three independent classes, each containing \(m\ge 1\) agents. Under synchronous non-progressive strict-majority updates, an agent is naturally positive at the next round exactly when at least \(m+1\) of its \(2m\) neighbors are positive now. A controller may temporarily make selected agents positive in any round, paying one unit for each agent-round intervention. Let \(T(m)\) be the minimum total intervention cost needed to reach a round in which **every agent is naturally positive with no intervention**. Then

\[
T(m)=\begin{cases}3,&m=1,\\m+3,&m\ge 2.\end{cases}
\]

For comparison, if interventions are permitted *only in the initial round*, the exact minimum successful initial target set is

\[
U(m)=\left\lceil\frac{3(m+1)}2\right\rceil\qquad(m\ge1).
\]

Thus timing first strictly reduces the optimum at \(m=4\), and \(T(m)/U(m)\to 2/3\). The unbounded additive gap is \(U(m)-T(m)\sim m/2\).

## Assumptions and scope

There are precisely three classes \(A,B,C\), each of size \(m\). Two vertices are adjacent if and only if they belong to different classes. The update is synchronous, deterministic, and non-progressive: positive agents can revert to negative. The strict-majority threshold is \(m+1\) because every degree is \(2m\). Following the timed-target-set convention, define \(Q_0=\varnothing\), choose intervention sets \(S_0,S_1,\ldots,S_{k-1}\), and put

\[
Q_{i+1}=\{v: |N(v)\cap(Q_i\cup S_i)|\ge m+1\},\quad i\ge0.
\]

Success means \(Q_k=V(G)\), with \(S_k=\varnothing\); cost is \(\sum_{i=0}^{k-1}|S_i|\). Repeated targeting is allowed. A static target set means \(S_i=\varnothing\) for all \(i\ge1\). No progressive or asynchronous model is asserted.

## Proof

**Homogeneity lemma.** For every \(i\ge1\), the natural state \(Q_i\) is a union of whole classes, even if \(S_{i-1}\) contains only some vertices of each class. Indeed all vertices of a given class have precisely the same neighbors and threshold. Consequently the natural state consists of zero, one, two, or three entire classes. A single naturally positive class cannot reproduce itself unaided: each outside vertex sees only \(m<m+1\) positive neighbors. Two naturally positive classes, without intervention, update to precisely the third class since that class sees \(2m\ge m+1\) positives, and each of the other two sees only \(m\). A third unforced step gives the empty state.

**Upper bound for timed intervention.** For \(m\ge2\), at time zero intervene on all \(m\) agents of \(C\), together with one agent in each of \(A,B\). This costs \(m+2\). At time one exactly classes \(A,B\) are naturally positive: each receives \(m+1\) positives from the other classes, while agents of \(C\) receive only two, fewer than \(m+1\). At time one intervene on one agent of \(C\), paying one more. At time two every agent is naturally positive, because each agent in \(A,B\) sees the \(m\) positive agents in the other class plus the one targeted member of \(C\), and each agent of \(C\) sees the \(2m\) naturally positive agents of \(A\cup B\). This gives \(T(m)\le m+3\). For \(m=1\), targeting all three vertices at time zero succeeds at time one, costing three.

**Lower bound for timed intervention.** Suppose \(m\ge2\) and, for contradiction, an intervention sequence succeeds with cost at most \(m+2\). Let \(t\) be the first positive time with \(Q_t\ne\varnothing\). Since \(Q_{t-1}=\varnothing\), the first nonempty natural state is determined solely by \(S_{t-1}\). To activate even one complete class requires at least \(m+1\) targeted agents in the other two classes. If two classes, say \(A,B\), become naturally positive together, writing \(a,b,c\le m\) for the previous intervention counts gives \(b+c\ge m+1\) and \(a+c\ge m+1\). Necessarily \(a,b\ge1\) and \(a+b+c\ge m+2\). If all three classes first activate together, adding their three neighbor-count inequalities gives \(2(a+b+c)\ge3(m+1)\), hence the cost is at least \(\lceil3(m+1)/2\rceil\ge m+3\), impossible.

There are now two cases. If exactly two classes first activate, at least \(m+2\) interventions have already been used, leaving none. The next natural state is only the third class, followed by the empty state, so success cannot occur. If exactly one class first activates, at most one intervention remains. From one naturally positive class, no intervention produces an empty next state, while one targeted agent in another class can activate at most the *other* previously inactive class: it brings that class's neighbor count to \(m+1\), but the targeted agent's own class still sees only \(m\) positive neighbors. Thus every subsequent natural state contains at most one class; without further interventions it becomes empty. Full natural positivity is impossible. This proves \(T(m)\ge m+3\). For \(m=1\), a first natural state comprising all three vertices requires all three vertices to have been targeted in the preceding round; if at most two interventions are used, the first nonempty natural state is at most one class and disappears without further intervention. So \(T(1)=3\).

**Static optimum.** Suppose the initially positive target set contains \(a,b,c\) agents of \(A,B,C\). The first natural state contains all three classes precisely when

\[
a+b\ge m+1,\qquad a+c\ge m+1,\qquad b+c\ge m+1.\]

If fewer than three classes appear in the first natural state, the homogeneity lemma shows that unforced evolution can never later reach all three. Thus these inequalities are necessary and sufficient for static success. Adding them gives \(a+b+c\ge\lceil3(m+1)/2\rceil\). Equality is realized by a balanced integer triple: when \(m+1=2h\), choose \((a,b,c)=(h,h,h)\); when \(m+1=2h+1\), choose \((h+1,h+1,h)\). Every count is at most \(m\), including the boundary \(m=1\). This proves the static formula and the asymptotics.

## Verification

The standalone standard-library program `verify_tripartite.py` independently solves the labelled-state finite dynamic program by Dijkstra search over every natural-positive subset and every possible intervention subset for \(m=1,2,3,4\), recovering costs \(3,5,6,7\). It also implements a separate eight-state type-count shortest-path solver for \(1\le m\le60\) and independently enumerates static seed profiles for \(1\le m\le30\). All checks pass. These are finite tests; the proof above is what establishes the theorem for every positive integer \(m\).

## Relationship to prior work

Soltani, Zehmakan, and Hushmandi introduced and studied timed target sets for non-progressive thresholds (arXiv:2307.09111, first public version July 18, 2023). Their strict-majority universal lower bounds and tree algorithm do not state the exact balanced complete-tripartite value or the static-versus-timed gap derived here. Their star example and complete-bipartite tightness example concern bipartite graphs, whereas the present graph contains triangles. Dvořák, Knop, and Toufar's dense-graph target-set algorithms (arXiv:1610.07530) address progressive irreversible activation, not the timed non-progressive process. These differences prevent direct implication from those inspected results; the possibility of another equivalent prior formula remains open.

## Limitations

The formula applies only to equal-sized complete tripartite graphs with strict-majority thresholds and unit per-agent-round intervention costs. It does not classify unequal part sizes, more than three parts, arbitrary threshold vectors, or limited-duration interventions. The proof makes no independent-publication-priority or external-certification claim. Finite computation is supporting evidence rather than proof of the infinite family.

## References

1. H. Soltani, A. N. Zehmakan, and A. B. Hushmandi, *Minimum Target Sets in Non-Progressive Threshold Models: When Timing Matters*, arXiv:2307.09111, first version July 18, 2023. https://arxiv.org/abs/2307.09111
2. P. Dvořák, D. Knop, and T. Toufar, *Target Set Selection in Dense Graph Classes*, arXiv:1610.07530, first version October 24, 2016. https://arxiv.org/abs/1610.07530
