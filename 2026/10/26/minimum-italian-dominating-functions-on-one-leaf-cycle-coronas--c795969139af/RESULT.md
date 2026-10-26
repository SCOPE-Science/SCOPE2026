# Minimum Italian dominating functions on one-leaf cycle coronas

## Finding
Let \(H\) be an arbitrary finite simple graph with vertex set \(V\) of order \(q\ge1\), and write \(H\circ K_1\) for the graph formed by adjoining one private leaf to every vertex. For a subset \(B\subseteq V\), let \(U_H(B)=V\setminus N_H[B]\), with \(N_H[B]\) the closed neighborhood of \(B\). Let \(\gamma(H)\) be the ordinary domination number. The total number \(F(H)\) of minimum-weight Italian dominating functions on the corona has the structural identity
\[
\gamma_I(H\circ K_1)=q+\gamma(H),\qquad
F(H)=\sum_{\substack{B\subseteq V\\|B|+|U_H(B)|=\gamma(H)}}2^{|B|}.
\]
In particular, for the labeled sunlet \(S_n=C_n\circ K_1\) with \(n\ge3\), put \(n=3m+r\), where \(r\in\{0,1,2\}\) and \(m=\lfloor n/3\rfloor\). Its minimum weight is \(n+\lceil n/3\rceil\), and its **exact number** \(I_n\) of minimum-weight Italian dominating functions is
\[
 I_n=\begin{cases}
 3\,2^m,&r=0,\\
 n(m+3)\,2^m,&r=1,\\
 n\,2^{m+1},&r=2.
 \end{cases}
\]
Vertices and their private leaves are individually distinguished; the labels \(0,1,2\) are fixed, and no quotient is taken by graph automorphisms.

## Assumptions and scope
An Italian dominating function (also called a Roman \(\{2\}\)-dominating function) on a simple graph \(X\) is a map \(f:V(X)\to\{0,1,2\}\) satisfying \(\sum_{w\in N_X(v)} f(w)\ge2\) for every vertex \(v\) with \(f(v)=0\). Its weight is \(\sum_{v\in V(X)}f(v)\). The corona \(H\circ K_1\) has \(2q\) vertices, with a unique pendant leaf \(v'\) at each original vertex \(v\). The general structural identity holds without connectivity assumptions, including isolated vertices; the closed-form sunlet census applies to simple cycles of lengths \(n\ge3\).

## Proof
**Step 1: exact structure for a general corona.** For any Italian function \(f\), its restriction to the pair \((v,v')\) has sum at least one: if \(f(v')=0\), then the leaf condition requires \(f(v)=2\). A pair of total weight exactly one must therefore be \((0,1)\). Call a pair *charged* when its total weight is at least two, and let \(D\subseteq V\) be the set of its original vertices. Every uncharged original vertex has label zero and leaf label one; the leaf contributes only one toward its defense, so such a vertex must have a positively labeled original neighbor. Every positive original label belongs to a charged pair. Consequently \(D\) dominates \(H\). The weight is at least \(q+|D|\ge q+\gamma(H)\). Taking a minimum ordinary dominating set \(D\), assigning \((1,1)\) on pairs indexed by \(D\), and \((0,1)\) on all other pairs gives a valid Italian function of weight exactly \(q+\gamma(H)\), proving the minimum formula.

In any minimum-weight Italian function, exactly \(\gamma(H)\) pairs are charged, each has total weight two, and all other pairs equal \((0,1)\). Each charged pair has precisely one of the three types \((2,0)\), \((1,1)\), or \((0,2)\), in the order (original vertex, private leaf). Let \(B\) be the set of charged original vertices with positive labels; these have either \((2,0)\) or \((1,1)\), independently giving two choices. Let \(A\) consist of the remaining charged pairs, which are \((0,2)\). Every original vertex outside \(A\cup B\) is zero-labeled and must be adjacent to \(B\), so \(U_H(B)\subseteq A\). The set \(B\cup U_H(B)\) dominates \(H\), whence
\[
\gamma(H)\le |B|+|U_H(B)|\le |B|+|A|=\gamma(H).
\]
Both inequalities are equalities and \(A=U_H(B)\). Conversely any \(B\) with \(|B|+|U_H(B)|=\gamma(H)\), together with an independent choice of \((2,0)\) or \((1,1)\) at each \(v\in B\), gives a legal minimum Italian function by using \((0,2)\) at each member of \(U_H(B)\) and \((0,1)\) at all other pairs. These descriptions are disjoint and exhaustive, giving the claimed formula for \(F(H)\).

**Step 2: reduction to nearly covering subsets of a cycle.** A set of \(k\) vertices in \(C_n\) covers at most \(3k\) vertices. A pattern of vertices spaced at cyclic distances at most three attains ordinary domination number \(k=\lceil n/3\rceil\). For an admissible set \(B\), write \(b=|B|\) and \(u=|U_{C_n}(B)|=k-b\). Since \(n-u\le3b\), necessarily \(n\le k+2b\).

If \(n=3m\), \(k=m\), hence \(b\ge m\) and therefore \(b=m\), \(u=0\). All \(m\) closed neighborhoods of three consecutive vertices must be disjoint, so the centers are exactly one of the three residue classes modulo three. There are three choices and each contributes \(2^m\) labelings.

If \(n=3m+2\), \(k=m+1\) and \(n\le k+2b\) forces \(b=m+1=k\), \(u=0\). Between successive selected centers, write the lengths of the cyclic gaps of unselected vertices. Each gap is in \(\{0,1,2\}\) and their sum is \(n-k=2k-1\), so exactly one gap has length one, and every other gap has length two. Choosing the unique short gap's *following* center gives a bijection with the \(n\) vertices, hence \(n\) sets; each contributes \(2^{m+1}\) labelings.

If \(n=3m+1\), \(k=m+1\) and the inequality restricts \(b\) to \(m\) or \(m+1\). For \(b=m+1=k\), \(u=0\), the cyclic unselected gaps belong to \(\{0,1,2\}\) and sum to \(n-k=2k-2\). The deficit from all gaps having length two is exactly two: either one gap has length zero, or two gaps have length one. For a specified distinguished selected center there are \(k+\binom{k}{2}=k(k+1)/2\) such ordered gap patterns. Every labeled set of \(k\) centers is counted \(k\) times when the distinguished center ranges over the \(k\) selected centers, whereas there are \(n\) available choices of the distinguished labeled vertex. Thus the number of sets is \(n(k+1)/2=n(m+2)/2\). Each gives \(2^{m+1}\) functions, contributing \(n(m+2)2^m\).

For \(b=m\), \(u=1\). The \(m\) size-three closed neighborhoods of selected centers must be pairwise disjoint and cover all but one vertex, since their maximum union size is \(3m=n-1\). Specifying the unique uncovered vertex determines a unique partition of the remaining cyclic path of \(3m\) vertices into successive length-three neighborhoods, and hence uniquely determines the \(m\) centers. Therefore there are exactly \(n\) possibilities, each carrying \(2^m\) choices of charged pair types. This contributes \(n2^m\). Adding the two disjoint contributions gives \(n(m+3)2^m\). This completes the all-order proof.

## Verification
The accompanying standalone Python 3 file `verify.py` implements the zero-neighbor inequality directly, independently enumerates every labeling of the \(2n\) sunlet vertices for \(3\le n\le6\), and compares the smallest weight and its number of realizations with the structural identity and three residue formulas. It also checks all simple base graphs on two, three, and four labeled vertices and checks the closed form by a separate subset enumeration of \(B\) for every \(3\le n\le14\). These finite checks are corroborative: the proof above, not a finite search, establishes the unrestricted statements.

## Relationship to prior work
Shao and Zhao (2026) introduce the Italian domination polynomial and study weight-by-weight Italian functions on paths, trees and cycles, motivating exact-count questions beyond the unmodified cycle. Hernández-Ortiz, Montejano and Rodríguez-Velázquez (2020) study Italian domination *numbers* in rooted products, including coronas. The already accessible numerical minimum formulas are not asserted as new here. The claim is instead the general optimum-*multiplicity* identity and the resulting complete labeled sunlet enumeration, including its residue-three dependence. Accessible descriptions of prior work and dedicated mathematical search records do not imply the displayed multiplicities. This is not a uniqueness certificate; details of unavailable primary full texts remain a publication-priority risk.

## Limitations
The result counts only **minimum-weight** Italian functions; it does not enumerate the entire Italian domination polynomial of a sunlet, nor extend its closed residue formula to arbitrary coronas. Direct brute-force verification is limited to small graphs. The two closest primary articles were accessible only through bibliographic/abstract material, so unexamined lemmas, supplementary sections or equivalent later work could affect a novelty judgment. No independent mathematical audit has been conducted.

## References
1. P. Shao and C. Zhao, *Counting Weight-k Italian Dominating Sets on Trees and Cycles*, arXiv:2610.00108v1, first public 2026-09-09, https://arxiv.org/abs/2610.00108 .
2. R. Hernández-Ortiz, L. P. Montejano and J. A. Rodríguez-Velázquez, *Italian domination in rooted product graphs*, arXiv:2006.02124v1 (2020), https://arxiv.org/abs/2006.02124 ; DOI 10.1007/s40840-020-00962-3.
3. M. Chellali, T. W. Haynes, S. T. Hedetniemi and A. A. McRae, *Roman {2}-domination*, Discrete Applied Mathematics 204 (2016), 22–28.
