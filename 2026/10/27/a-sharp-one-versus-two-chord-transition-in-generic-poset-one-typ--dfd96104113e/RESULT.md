# A sharp one-versus-two chord transition in generic-poset one-type counts

## Finding
Let \(\mathbb P\) be the countable universal homogeneous strict partial order. For a finite induced parameter poset \(A\), let \(t(A)\) denote the number of complete nonalgebraic one-types over its **individually named** elements. In particular, the new element is different from every parameter.

For every \(n\ge 3\), define the crown \(C_n\) with minimal elements \(a_0,\ldots,a_{n-1}\), maximal elements \(b_0,\ldots,b_{n-1}\), and exactly the comparisons \(a_i<b_i\) and \(a_{i+1}<b_i\), with indices modulo \(n\). A *chord* means an added comparison between a previously incomparable minimal and maximal element. Let \(C_{n;k}\) add \(a_0<b_k\), where \(1\le k\le n-2\).

**One-chord rigidity.** For every \(n\ge5\), set \(\delta_{n,k}=1\) when \(k=1\) or \(k=n-2\), and zero otherwise. Writing \(F_j\) for the Fibonacci numbers with \(F_0=0,F_1=1\), and \(L_j\) for Lucas numbers with \(L_0=2,L_1=1\), one has
\[
t(C_{n;k})=2\bigl(L_{2n}-F_{2k}F_{2(n-k-1)}\bigr)+4n+6+\delta_{n,k}.
\]
The number \(t(C_{n;k})\) decreases strictly as \(\min\{k,n-1-k\}\) increases. Thus within the complete one-chord family it determines the isomorphism type, and specifically determines the chord's distance from the original cycle up to reflection. All these posets have equal cardinality, the same number of comparisons, and the same degree multisets on each level.

**Two-chord failure in an infinite family.** For every \(n\ge5\), put
\[
Q_n=C_n+\{a_0<b_1,\ a_0<b_2\},\qquad
R_n=C_n+\{a_0<b_1,\ a_0<b_{n-2}\}.
\]
These two posets are nonisomorphic yet their ideal counts, complete nonempty common-upper-neighborhood sums, and hence their one-type counts coincide:
\[
\begin{aligned}
|J(Q_n)|=|J(R_n)|&=F_{2n+1}+4F_{2n-5},\\
B(Q_n)=B(R_n)&=4n+20,\\
t(Q_n)=t(R_n)&=2F_{2n+1}+8F_{2n-5}+4n+19.
\end{aligned}
\]
Here \(J(A)\) denotes the set of order ideals, and \(B(A)\) counts ordered pairs of nonempty lower and upper subsets whose every cross pair is comparable in the correct direction (defined precisely below). The two posets also have identical degree multisets on both levels, with a unique degree-four minimum and two degree-three maxima.

The **smallest** two-chord counterexample occurs already on eight parameters (\(n=4\)): the two nonisomorphic extensions of \(C_4\) by chord sets
\[
\{a_0<b_1,a_1<b_3\},\qquad \{a_0<b_1,a_2<b_0\}
\]
both have exactly \(115\) nonalgebraic one-types. No nonisomorphic two-chord pair exists for \(n=3\).

## Assumptions and scope
The index \(n\) is finite, \(\mathbb P\) is the homogeneous Fraïssé limit of **all finite strict posets**, and every parameter is named. These are counts of complete nonalgebraic one-types, not counts of all algebraic and nonalgebraic types, and not counts of unlabeled one-point extensions. In the two-chord assertions the chords are two distinct missing cross-comparisons. The result is restricted to the stated crown perturbations; it does not claim one-type count to be a complete invariant on arbitrary finite posets.

For a height-two poset \(A\) with minimal level \(V\) and maximal level \(W\), let \(N(S)=\{w\in W:(\forall v\in S)\,v<w\}\) for nonempty \(S\subseteq V\), and set
\[
B(A)=\sum_{\varnothing\ne S\subseteq V}\bigl(2^{|N(S)|}-1\bigr).
\]
This agrees with the preceding description of the cross-comparable nonempty pairs.

## Proof
**(1) Type encoding.** For a new point \(x\), let \(L=\{a\in A:a<x\}\) and \(U=\{a\in A:x<a\}\). The extension defines a partial order precisely when \(L\) is an order ideal, \(U\) is an order filter, and every element of \(L\) is strictly below every element of \(U\) in \(A\). These conditions are necessary by transitivity and sufficient by inspecting all new chains through \(x\). Homogeneity and the extension property of \(\mathbb P\) realize every such pair as exactly one complete nonalgebraic type. If \(J(A)\) is the set of ideals, the cases \(L=\varnothing\) and \(U=\varnothing\) contribute \(2|J(A)|-1\). If both are nonempty in a height-two poset, necessarily \(L\subseteq V\) and \(U\subseteq W\), so there are exactly \(B(A)\) further cases. Therefore
\[
t(A)=2|J(A)|-1+B(A).
\]

**(2) Cycle transfer matrix.** For each choice of minimal elements \(S=\{a_i:x_i=1\}\), a maximal element \(b_j\) may independently be included in an ideal precisely when all its lower neighbors lie in \(S\). On the crown this gives
\[
|J(C_n)|=\sum_{(x_i)\in\{0,1\}^n}\prod_{i=0}^{n-1}2^{x_ix_{i+1}}=\operatorname{tr}(T^n)=L_{2n},\qquad
T=\begin{pmatrix}1&1\\1&2\end{pmatrix},
\]
where indices are cyclic. The matrix has characteristic polynomial \(z^2-3z+1\). In particular \((T^m)_{0,1}=F_{2m}\), proved from the initial values at \(m=0,1\) and the recurrence \(u_{m+2}=3u_{m+1}-u_m\).

The new relation \(a_0<b_k\) changes an ideal weight only when \(x_0=0\) and \(x_k=x_{k+1}=1\). On that event the factor from \(b_k\) changes from two to one; splitting the original cycle at the three fixed binary states gives the *exact* ideal-count deficit
\[
|J(C_n)|-|J(C_{n;k})|=(T^k)_{0,1}(T^{n-k-1})_{1,0}=F_{2k}F_{2(n-k-1)}.
\]
For the unchanged crown, each singleton minimum has two upper neighbors, and each of the \(n\) adjacent minimum pairs has one common upper neighbor. Thus \(B(C_n)=4n\). The chord creates four new nonempty upper subsets over \(S=\{a_0\}\), one new subset over each of \(S=\{a_0,a_k\}\) and \(S=\{a_0,a_{k+1}\}\), and one over their triple. When \(k=1\) or \(n-2\), exactly one of those two pairs already shared an upper neighbor, giving one additional subset. Therefore \(B(C_{n;k})=4n+7+\delta_{n,k}\). Combining these equations proves the one-chord formula.

**(3) Strict recovery and isomorphism.** Put \(h=n-1\) and \(d=\min\{k,h-k\}\). The Fibonacci–Lucas identity gives
\[
F_{2d}F_{2(h-d)}=\frac{L_{2h}-L_{2(h-2d)}}5.
\]
For \(1\le d\le\lfloor h/2\rfloor\), the right side is strictly increasing with \(d\), since the even-index Lucas numbers increase strictly with their nonnegative index. The exceptional correction \(\delta_{n,k}\) is one only for \(d=1\) and zero thereafter, so the entire type count is strictly decreasing. In the bipartite cover graph, the new chord is the unique edge between the unique degree-three minimum and unique degree-three maximum. Deleting it recovers the original cycle, whose two arc lengths between those endpoints determine exactly the unordered pair \(\{k,n-1-k\}\). Reflection interchanges those distances. Hence the claimed numerical recovery agrees exactly with isomorphism classes.

**(4) Two-chord ideal coincidence.** If \(a_0\) is included in the chosen set \(S\) of minimum elements, both extra comparisons impose no further restrictions on the choice of upper elements. The contribution is \((T^n)_{1,1}=F_{2n+1}\). If \(a_0\) is excluded, the maxima \(b_0,b_{n-1}\) are automatically excluded, and the remaining minima form a binary path \(a_1,\ldots,a_{n-1}\), weighted by \(2^{x_ix_{i+1}}\) on successive pairs. In \(Q_n\) the added chords suppress the first two path-edge weights; in \(R_n\) they suppress the first and the last. In either case the path splits into two isolated binary variables and one ordinary weighted path on \(n-3\) variables. The latter's partition sum is \(F_{2n-5}\), by the same recurrence as the matrix, so the excluded-\(a_0\) contribution is \(4F_{2n-5}\) in each case. This proves the exact ideal count.

For the common-neighborhood term, the crown contributes \(4n\). Adding \(a_0<b_1\) contributes eight: four new upper subsets over the singleton \(\{a_0\}\), three over the two newly incident pairs of minima, and one over their triple. Adding either second chord contributes twelve: eight new upper subsets over \(\{a_0\}\), a total of three over the two newly incident pairs (one of the pairs already had a common upper neighbor), and one over the relevant triple. Thus \(B(Q_n)=B(R_n)=4n+20\). The formula for \(t\) now follows from (1).

The only degree-four minimum is \(a_0\), and the two degree-three maxima are \(b_1,b_2\) in \(Q_n\), but \(b_1,b_{n-2}\) in \(R_n\). The former two share exactly two common lower neighbors, \(\{a_0,a_2\}\), whereas the latter two share only \(\{a_0\}\), for all \(n\ge5\). This incidence invariant proves nonisomorphism without referring to the naming.

**(5) Sharp smallest example.** In the stated \(n=4\) pair, enumerate the sixteen subsets of the four minima. The independent ideal and common-neighborhood sums are \(41\) and \(34\) in both structures, hence \(t=2\cdot41-1+34=115\). Their respective two degree-three minima have three and two common upper neighbors, proving nonisomorphism. For \(n=3\), each of the three minima has exactly one nonneighbor among the three maxima; the three available chords form one orbit under the rotational symmetry, as do their two-element subsets. Hence no nonisomorphic two-chord example occurs at \(n=3\).

## Verification
The standalone `verify.py` independently enumerates all subsets of the minimal level, all eligible ideal choices, and common neighborhoods through \(n=13\). For \(n=5,6\), it also enumerates all three-way order-status assignments for the added point and checks their pairwise consistency directly rather than invoking the transfer-matrix formulas. The small \(n=4\) collision is verified by both methods. The checker tests strict monotonicity, reflection symmetry, closed forms, and the two-chord family. Its recorded output is `checks.txt` and ends in `ALL_CHECKS_PASS`. Finite checks support, but do not replace, the unrestricted proof above.

## Relationship to prior work
The Fraïssé homogeneity of the random partial order is classical; Pach, Pinsker, Pluhár, Pongrácz and Szabó study its reducts [1]. Classical work on crowns enumerates their order ideals; Conflitti [2, Sections 1–2] supplies crown Whitney-number formulas and explicitly cites earlier work of Munarini and Zagaglia Salvi. The cycle ideal count used here is not claimed as a new enumerative identity. Existing general finite-base one-type algorithms, complexity results, and one-comparability response identities subsume the possibility of computing each individual finite instance. They do **not** themselves state the sharp one-versus-two chord recovery/collision transition, the all-size twin constructions, or the shared explicit closed form proved here. A broader article on garland ideals [3] was identified; its abstract was reviewed, but its scan could not be reliably inspected in full, so hidden overlap remains possible.

## Limitations
The invariant is a single scalar one-type count, and its demonstrated failure concerns only the specified perturbations. No global graph/poset reconstruction principle follows. Originality is assessed against accessible primary texts and semantic records; no exhaustive publication search or independent audit is claimed. The full garland article and earlier rank-polynomial article may contain related identities not resolved from available text. The formulas count nonalgebraic types, not algebraic equality types.

## References
[1] P. P. Pach, M. Pinsker, G. Pluhár, A. Pongrácz, C. Szabó, *Reducts of the random partial order*, arXiv:1111.7109 (first posted 2011-11-30), https://arxiv.org/abs/1111.7109.

[2] A. Conflitti, *On Whitney numbers of the Order Ideals of Generalized Fences and Crowns*, arXiv:math/0505636 (first posted 2005-05-30), https://arxiv.org/abs/math/0505636.

[3] E. Munarini, *Enumeration of Order Ideals of a Garland*, Ars Combinatoria 76 (2005), 185–192, https://combinatorialpress.com/ars-articles/volume-076-ars-articles/enumeration-of-order-ideals-of-a-garland/.
