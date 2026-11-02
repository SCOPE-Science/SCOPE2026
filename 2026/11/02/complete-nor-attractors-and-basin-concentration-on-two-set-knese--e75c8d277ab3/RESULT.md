# Complete NOR attractors and basin concentration on two-set Kneser graphs

## Finding

For every integer \(n\ge5\), put \(U=\binom{[n]}2\) and let \(KG(n,2)\) be the graph on \(U\) in which two distinct edges of the complete graph are adjacent exactly when they are disjoint. An initial binary configuration is identified with its active-edge set \(S\subseteq U\). The synchronous **open-neighborhood NOR** rule is
\[
 F(S)=\{e\in U:\text{every }s\in S\text{ intersects }e\}.
\]
The state of \(e\) itself is **not** included in the NOR input. Every state reaches a fixed point or primitive two-cycle after at most one update, and this upper bound is sharp.

Write \(\mathcal S_v\) for the full star of vertex \(v\), \(T_{ab}=\mathcal S_a\cup\mathcal S_b\), \(W_{a;bc}=\mathcal S_a\cup\{bc\}\) for distinct \(a,b,c\), and \(\Delta_{abc}=\{ab,ac,bc\}\). Regard an edge family as a simple graph on \([n]\), permitting isolates. The **complete** attractor classification is:

| Type | Number of attractors | Primitive period |
|:--|--:|--:|
| \(\mathcal S_v\) | \(n\) | 1 |
| \(\Delta_{abc}\) | \(\binom n3\) | 1 |
| \(\varnothing\leftrightarrow U\) | 1 | 2 |
| \(\{ab\}\leftrightarrow T_{ab}\) | \(\binom n2\) | 2 |
| \(\{ab,ac\}\leftrightarrow W_{a;bc}\) | \(3\binom n3\) | 2 |
| a matching of two edges \(\leftrightarrow\) its crossing \(4\)-cycle | \(3\binom n4\) | 2 |
| a three-edge path \(\leftrightarrow\) the other three-edge path on the same four vertices | \(6\binom n4\) | 2 |

For the last row, explicitly, \(\{ab,ac,bd\}\leftrightarrow\{ab,ad,bc\}\) for pairwise distinct \(a,b,c,d\). The two period-two rows supported on four vertices together contribute \(9\binom n4\) attractors.

Define the three integers
\[
\begin{aligned}
 g_n&=2^{n-1}-n-\binom{n-1}{2},\\
 h_n&=g_n+1+\binom{n-3}{2},\\
 e_n&=1+2(2^{n-2}-n+1)^2-\binom{n-2}{2},
\end{aligned}
\]
and, with \(m=\binom n2\),
\[
 B_n=2^m-\left(ng_n+\binom n3+\binom n2e_n+3\binom n3h_n+18\binom n4\right).
\]
Here **attraction basin** means the number of initial configurations whose eventual orbit is the indicated attractor, including its periodic states. Every star fixed point has basin \(g_n\); every triangle fixed point has basin \(1\); the empty/full two-cycle has basin \(B_n\); every single-edge/double-star two-cycle has basin \(e_n\); every two-edge-wedge/augmented-star two-cycle has basin \(h_n\); and each remaining four-vertex two-cycle has basin \(2\). There are no other basin sizes or attractors.

In particular the number of fixed points and the number of distinct primitive two-cycles are respectively
\[
 n+\binom n3,\qquad 1+\binom n2+3\binom n3+9\binom n4.
\]
The empty/full two-cycle is the unique largest-basin attractor for all \(n\ge5\). It attracts more than half the initial states **if and only if** \(n\ge6\) within this domain. Its exceptional-basin probability satisfies
\[
 1-\frac{B_n}{2^{\binom n2}}
 =\binom n2\,2^{2n-3-\binom n2}\bigl(1+O(n2^{-n})\bigr)
 \quad(n\longrightarrow\infty).
\]
Thus the fraction of states attracted elsewhere is \(2^{-\Theta(n^2)}\), even though the number of attractors grows polynomially in \(n\).

## Assumptions and scope

The graph is the ordinary simple, loop-free Kneser graph on all unordered two-element subsets of \([n]\), \(n\ge5\). All \(2^{\binom n2}\) binary initial states are counted with equal weight; updates are synchronous and use **open** neighborhoods. The rules for self-inclusive NOR or for exclusive-or parity updates are different and are not included in the theorem. An isolated vertex in an auxiliary edge-family graph is permitted. All counts include labelled vertices and distinguish labelled attractors, not symmetry classes.

## Proof

**1. Symmetric antitone polarity and entrance time.** Define \(e\sim s\) when the two two-sets intersect (including \(e=s\)). This relation is symmetric. If \(F(A)=\{e:e\sim a\ \forall a\in A\}\), then \(A\subseteq F^2(A)\): every \(a\in A\) intersects each element of \(F(A)\). Since \(F\) reverses inclusion, this gives \(F^3(A)\subseteq F(A)\); applying the same inclusion to \(F(A)\) gives the reverse inclusion. Consequently \(F^3=F\), so after one update every trajectory is fixed or two-periodic. This bound is sharp since \(n\ge5\) admits a three-spoke star subset, whose first iterate is the full star and which is not already periodic.

**2. Exhaustive image classification.** A nonempty image \(F(S)\) contains some edge \(ab\), so \(ab\) meets every edge of \(S\); equivalently, \(\{a,b\}\) is a vertex cover of the edge-family graph \(S\). Hence \(S\subseteq T_{ab}\). Let \(W=[n]\setminus\{a,b\}\), and write \(S\) uniquely as the optional edge \(ab\), together with the spokes \(\{aw:w\in A\}\) and \(\{bw:w\in D\}\), where \(A,D\subseteq W\). Put \(t=1\) when \(ab\in S\), and \(t=0\) otherwise. Direct intersection gives the exact test
\[
\begin{array}{ll}
 ab\in F(S)&\text{always};\\
 aw\in F(S)&\Longleftrightarrow D\subseteq\{w\};\\
 bw\in F(S)&\Longleftrightarrow A\subseteq\{w\};\\
 wz\in F(S)&\Longleftrightarrow t=0\ \text{and}\ A\cup D\subseteq\{w,z\},\quad w,z\in W.
\end{array}
\]
It remains a finite **symbolic** case distinction independent of \(n\). If \(|A|,|D|\ge2\), the image is the singleton \(\{ab\}\), except when \(t=0\) and \(A=D=\{c,d\}\), when it is the two-edge matching \(\{ab,cd\}\). If \(|A|\ge2,|D|=1\), the image is a two-edge wedge, except that \(t=0\), \(|A|=2\), and \(D\subset A\) give a three-edge path; interchange \(a,b\) for the symmetric case. If \(|A|\ge2,D=\varnothing\), the image is the full star \(\mathcal S_a\), except for \(t=0\) and \(|A|=2\), which add the opposite chord; again there is a symmetric case. Finally \(|A|,|D|\le1\) directly yields an empty-family image's partner \(U\), a double-star \(T_{ab}\), an augmented star, a triangle, a crossing four-cycle or a three-edge path, according to \(t\) and whether the singleton elements of \(A,D\) coincide.

If no two-set covers \(S\), then \(F(S)=\varnothing\). All listed image types are therefore exhaustive. Applying the same test to the ten image shapes \(\varnothing,U,\{ab\},T_{ab},\mathcal S_v,W_{a;bc},\{ab,ac\},\Delta_{abc},\) a two-edge matching, a four-cycle, and a three-edge path (counting the last three as separate types) gives exactly the fixed points and paired shapes in the table. No further dynamical type is possible. For the displayed path example, the intersection constraints give \(F(\{ab,ac,bd\})=\{ab,ad,bc\}\), and then swap back. A four-vertex set has three perfect matchings and twelve undirected three-edge paths; the latter pair into six involution orbits. Together with the direct choices of a vertex, unordered pair and centred wedge, this proves all attractor multiplicities.

**3. Every non-distinguished basin.** For an attractor \(\{P,Q\}\), any initial \(S\) belongs to its basin exactly when \(F(S)\in\{P,Q\}\) (and likewise for a fixed point). Inverting the cover test of step 2 gives:

For a fixed star \(\mathcal S_v\), \(F(S)=\mathcal S_v\) exactly when \(S\) consists of at least three spokes at \(v\). There are \(\sum_{j=3}^{n-1}\binom{n-1}j=g_n\) such configurations. For a fixed triangle \(\Delta_{abc}\), the only preimage is itself, hence its basin is one.

For a wedge \(P=\{ab,ac\}\) and its partner \(Q=W_{a;bc}\), \(F(S)=Q\) only for \(S=P\). Conversely \(F(S)=P\) requires the edge \(bc\), together with either at least three spokes at \(a\), or exactly two spokes at \(a\) whose other ends both lie outside \(\{b,c\}\). This gives \(g_n+\binom{n-3}2\) configurations, and including the sole preimage of \(Q\) gives basin \(h_n\).

For the single-edge/double-star pair \(\{ab\}\leftrightarrow T_{ab}\), \(F(S)=T_{ab}\) occurs only for \(S=\{ab\}\). To obtain \(F(S)=\{ab\}\), the two spoke-end sets \(A,D\subseteq W\) must each have cardinality at least two. For either value of \(t\), this gives \(\bigl(2^{n-2}-n+1\bigr)^2\) choices, but for \(t=0\) the \(\binom{n-2}2\) possibilities \(A=D=\{c,d\}\) have the additional cover \(cd\) and must be removed. Thus the basin has \(e_n\) configurations. The image case distinction also proves that every matching/crossing-four-cycle and every paired-path cycle has precisely its two periodic states as preimages, giving basin \(2\) each.

**4. Distinguished basin and its threshold.** The disjoint basin partition exhausts the \(2^m\) initial states, so subtracting the counts from step 3 gives the stated closed formula for \(B_n\). Alternatively \(F(S)=\varnothing\) exactly when the auxiliary graph \(S\) has no vertex cover of size at most two; \(S=\varnothing\) is the unique state with \(F(S)=U\). Thus \(B_n=1+\#\{S:\tau(S)\ge3\}\), with \(\tau\) the ordinary vertex-cover number.

For \(n=5\), the explicit basin formulas give \(B_5=389\), while the next-largest basin is \(e_5=30\). For \(n\ge6\), each event that a specified pair covers \(S\) permits exactly \(2^{2n-3}\) of the \(2^m\) states, since \(T_{ab}\) has \(2n-3\) edges. The union bound therefore gives
\[
 1-\frac{B_n}{2^m}
 \le\binom n2\,2^{2n-3-m}.
\]
At \(n=6\) the right side equals \(15/64<1/2\), and the ratio of the right sides at consecutive integers is \(\frac{n+1}{n-1}2^{2-n}<1\) for \(n\ge6\). Hence \(B_n>2^{m-1}\) for all \(n\ge6\), which makes this basin uniquely largest. The calculated \(B_5<2^{10-1}\) establishes the sharp threshold.

For the asymptotic equivalent, denote by \(E_{ab}\) the event that \(\{a,b\}\) covers \(S\), and let \(M_n\) count states in their union. A pair of these events sharing one vertex has exactly \(2^n\) common states: allowed edges are the star at the common vertex plus the edge connecting their other endpoints. Two events on disjoint pairs have exactly \(2^4\) common states: the four crossing edges only. There are \(3\binom n3\) overlapping pairs and \(3\binom n4\) disjoint pairs of events. The first two Bonferroni inequalities therefore yield
\[
 \binom n2\,2^{2n-3}-3\binom n3\,2^n-48\binom n4
 \le M_n\le\binom n2\,2^{2n-3}.
\]
As \(B_n=1+2^m-M_n\), division by \(2^m\) yields the asserted asymptotic with relative error \(O(n2^{-n})\). This completes the proof.

## Verification

The proof is symbolic and applies at every \(n\ge5\). Two executable, separately implemented bit-mask enumerators accompany this result. Running `python3 verify_exhaustive.py` checks every labelled state for \(n=5,6\), including \(F^3=F\), the exact attractor histogram, all aggregate counts and the distinguished basin. Running `g++ -O3 -std=c++17 verify_cpp.cpp -o verifier && ./verifier` repeats those checks using a different implementation for \(n=5,6,7\). The largest exhaustive check covers \(2^{21}=2{,}097{,}152\) states at \(n=7\). Expected counts of attractors are respectively \(101,237,484\), with distinguished basin sizes \(389,27627,2062845\). Packaged outputs give the actual test results. The finite checks corroborate but do not establish the general theorem.

## Relationship to prior work

The survey by Aledo, Martínez and Valverde (2015) discusses periodic-point restrictions for synchronous minterm/maxterm graph dynamics and cites the 2012 primary minterm/maxterm paper. The open-access primary studies by Aledo and collaborators (2017, 2020) analyze their **self-inclusive** dependency rule (local inputs consist of the vertex itself and its neighbors); the present graph dynamics uses **open-neighborhood** NOR, with no self-input. In particular, the present theorem exhibits fixed points and primitive two-cycles simultaneously, whereas the 2017 coexistence restriction applies to the self-inclusive rule; these statements do not contradict or imply each other. The present closed, explicit six-population basin census and sharp \(n=6\) majority threshold were not identified in the examined literature. General statements about periodicity do not supply these individual basins. The theorem uses the classical language of intersecting two-set families and two-vertex covers, but makes no claim to originate that language.

## Limitations

The theorem is limited to ordinary two-set Kneser graphs with \(n\ge5\), binary states and synchronous open-neighborhood NOR; it does not cover \(KG(n,k)\) for \(k\ne2\), self-inclusive NOR, asynchronous schedules, or other Boolean rules. Exhaustive verification stops at \(n=7\), whereas the proof is all-orders. Bibliographic searches cannot prove publication novelty. The original 2012 minterm/maxterm journal article was not inspected in full; its abstract and the later open-access survey were compared, and its precise historical overlap remains a risk. No independent audit has been performed.

## References

1. J. A. Aledo, S. Martínez and J. C. Valverde, “Parallel Dynamical Systems over Graphs and Related Topics: A Survey,” *Journal of Applied Mathematics* (2015), article 594294; first published 24 March 2015. DOI: 10.1155/2015/594294. https://doi.org/10.1155/2015/594294
2. J. A. Aledo, S. Martínez, F. L. Pelayo and J. C. Valverde, “Parallel discrete dynamical systems on maxterm and minterm Boolean functions,” *Mathematical and Computer Modelling* 55 (2012), 666–671. DOI: 10.1016/j.mcm.2011.08.040.
3. J. A. Aledo, L. G. Díaz, S. Martínez and J. C. Valverde, “On the Periods of Parallel Dynamical Systems,” *Complexity* (2017), article 7209762. DOI: 10.1155/2017/7209762.
4. J. A. Aledo, A. Barzanouni, G. Malekbala, L. Sharifan and J. C. Valverde, “Counting Periodic Points in Parallel Graph Dynamical Systems,” *Complexity* (2020), article 9708347. DOI: 10.1155/2020/9708347.
