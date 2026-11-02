# Optimal symmetric realization of co-singleton actual-effectivity frames

## Finding
Let \(W\) be a finite outcome set of cardinality \(n\), and consider two agents whose available *outcome neighborhoods*, at each world, are exactly
\[
\mathcal N=\{W\setminus\{i\}:i\in W\}.
\]
A deterministic concurrent-game realization of these neighborhoods exists if and only if \(n\ge 3\). In every such realization each agent must have at least \(n\) actions at every world. For every \(n\ge3\), this lower bound is attained simultaneously by both agents, with one action labelled \(i\) for each neighborhood \(W\setminus\{i\}\). Moreover, the outcome function can be independent of the current world and *symmetric under exchanging the two agents' actions*: there is an \(f:W\times W\to W\) such that
\[
f(i,j)=f(j,i),\qquad
\{f(i,j):j\in W\}=W\setminus\{i\}
\quad(i\in W).
\]
Thus both agents use exactly \(n\) actions, and their \(n^2\) joint action profiles are the minimum possible with these neighborhoods. The result concerns the minimal number of actions, not the minimum number of worlds.

## Assumptions and scope
A deterministic two-agent concurrent game structure has a nonempty world set \(W\), a nonempty action set for each agent at each world, and a function assigning one successor world to every pair of available actions. For a fixed action of agent one, its outcome neighborhood is the set of successor worlds as agent two's action varies; symmetrically for agent two. The *actual-effectivity family* is the set of these nonempty outcome neighborhoods, ignoring repeated action labels. The specified family \(\mathcal N\) is the same at every world. Worlds and neighborhoods are labelled; the action sets may otherwise differ by world. The assertion is local and holds uniformly at every world by using the same construction.

## Proof
**Necessity and lower bound.** If \(n=1\), the prescribed sole neighborhood is empty, whereas the possible-outcome set of an action in a deterministic concurrent game is nonempty. If \(n=2\), select agent-one's action with neighborhood \(W\setminus\{0\}=\{1\}\) and agent-two's action with neighborhood \(W\setminus\{1\}=\{0\}\). Their joint profile has an outcome belonging to both neighborhoods, impossible. If \(n\ge3\), the \(n\) distinct required neighborhoods must be produced by at least \(n\) distinct actions of each agent; hence the total action-profile count at a world is at least \(n^2\).

It remains to construct a symmetric outcome table meeting the lower bound.

**Odd case.** If \(n\ge3\) is odd, identify \(W\) with \(\mathbb Z/n\mathbb Z\) and let \(2^{-1}\) denote the inverse of \(2\) in this ring. Define
\[
f(i,j)=\begin{cases}
2^{-1}(i+j),&i\ne j,\\
i+1,&i=j.
\end{cases}
\]
This is symmetric. For fixed \(i\), as \(j\) ranges over \(W\setminus\{i\}\), the affine map \(j\mapsto2^{-1}(i+j)\) ranges bijectively over \(W\setminus\{i\}\): it has its unique preimage of \(i\) at \(j=i\). The diagonal value \(i+1\) also lies in this set. Hence the full row has precisely the prescribed range, and symmetry gives the same for every column.

**Even case.** If \(n\ge4\) is even, put \(p=n-1\), which is odd and at least three, and identify \(W\) with \((\mathbb Z/p\mathbb Z)\cup\{\infty\}\). Define, with all finite arithmetic modulo \(p\),
\[
f(i,j)=\begin{cases}
2^{-1}(i+j),&i,j\in\mathbb Z/p\mathbb Z,\ i\ne j,\\
\infty,&i=j\in\mathbb Z/p\mathbb Z,\\
i+1,&i\in\mathbb Z/p\mathbb Z,\ j=\infty,\\
j+1,&j\in\mathbb Z/p\mathbb Z,\ i=\infty,\\
0,&i=j=\infty.
\end{cases}
\]
This is symmetric. Fix a finite \(i\). Its entries at finite columns \(j\ne i\) run through all finite outcomes except \(i\); its diagonal supplies \(\infty\); and its column \(\infty\) supplies the already-present finite outcome \(i+1\). Thus this row has range \(W\setminus\{i\}\). The row at \(\infty\) has, at finite columns \(j\), the entries \(j+1\), which run over all finite outcomes; its diagonal repeats \(0\). Its range is therefore \(W\setminus\{\infty\}\). By symmetry all columns have the corresponding ranges.

For either parity, make both agents' action sets equal to \(W\), let action \(i\) mean vetoing outcome \(i\), and use \(f(i,j)\) as the successor independently of the current world. The verified row and column ranges give exactly the prescribed actual-effectivity neighborhoods, one action per neighborhood, and the minimum number of action profiles. This proves all assertions.

## Verification
The standalone `checker.py` independently constructs the tables and checks both agents' exact row and column outcome sets, absence of either vetoed outcome, and swap symmetry for every order \(3\le n\le200\). It separately exhausts all symmetric tables whose entries avoid their row and column labels for orders \(3\) and \(4\); respectively \(8\) and \(288\) valid tables occur. The checker prints `ALL_CHECKS_OK`. The symbolic two-parity proof, not these finite tests, establishes the theorem for all finite orders.

## Relationship to prior work
Ciardelli's representation theorem for actual-effectivity functions (2026, Theorem 2.2) characterizes which multi-agent neighborhood frames admit a concurrent-game realization by existence of actions, a uniform range, and intersections of simultaneous neighborhoods. It supplies a general construction using extra outcome labels on actions. The present theorem solves a different, action-minimization problem for the natural family of all co-singleton neighborhoods, and supplies an additional swap symmetry not required by general representability. Classical modular midpoint operations supply the elementary combinatorial ingredient of the construction; they are not claimed as new in isolation.

## Limitations
Only two agents, finite nonempty carriers, all co-singleton neighborhoods, and deterministic outcomes are covered. Existence for arbitrary actual-effectivity families is a separate known result. The symmetric table is not claimed unique. The new characterization is not an enumeration of all optimal tables. Classical quasigroup or matrix-construction literature may contain equivalent constructions; a comprehensive historical priority claim is not made. Independent validation of novelty and proof has not been performed.

## References
1. Ivano Ciardelli, *Inquisitive Action Logic* (first public posting 2026-06-30), arXiv:2606.31866, especially Section 2 and Theorem 2.2. https://arxiv.org/abs/2606.31866
2. Classical cyclic-group arithmetic and affine midpoint operations (standard algebraic background).
