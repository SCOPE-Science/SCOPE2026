# Dihedral reflection characters and quotient homology of cycle-power three-cut complexes

## Finding
Fix integers \(p\ge 2\) and \(n\ge 6p-3\). Let \(G=C_n^p\) have vertex set \(\mathbb Z/n\mathbb Z\), with distinct vertices adjacent when their cyclic distance is at most \(p\). Let \(K=\Delta_3(G)\) be the **ordinary** three-cut complex: its facets are complements of three-element subsets inducing a disconnected graph. The dihedral group \(D_n=\langle r,s:r^n=s^2=1,\ srs=r^{-1}\rangle\) acts by \(r(i)=i+1\), \(s(i)=-i\). Set \(d=n-4\) and \(\mathcal H=\widetilde H_d(K;\mathbb Q)\).

All other reduced rational homology groups vanish, and \(\dim\mathcal H=\beta=1+n(n-4p-1)/2\), as established nonequivariantly in [1]. The **complete dihedral character** \(\chi\) of \(\mathcal H\) is as follows. On rotations, for \(0\le a<n\),
\[
\chi(r^a)=\begin{cases}
\beta,&a=0,\\
(-1)^{n/2}(1-n/2),&n\text{ even and }a=n/2,\\
(-1)^{n-\gcd(n,a)},&\text{otherwise}.
\end{cases}
\]
The rotation restriction was previously established in [4]; it is included here only to state the full character. **The reflection values are the new conclusion**:
\[
\boxed{\chi(r^a s)=\begin{cases}
(-1)^{(n+1)/2}(n-4p+1)/2,&n\text{ odd},\\
(-1)^{n/2}(n/2-2p-1),&n\text{ even},\ a\text{ even},\\
(-1)^{n/2+1}(n/2-2p+1),&n\text{ even},\ a\text{ odd}.
\end{cases}}
\]
Here \(r^a s\) acts as \(i\mapsto a-i\); when \(n\) is even, the even-\(a\) reflections have two fixed vertices and the odd-\(a\) reflections have none.

Consequently the full geometric quotient has reduced rational homology only in degree \(d\), with rank
\[
\boxed{\dim\widetilde H_d(|K|/D_n;\mathbb Q)=
\begin{cases}
0,&n\equiv1\pmod4,\\
(n-4p+1)/2,&n\equiv3\pmod4,\\
(n-4p-4)/4,&n\equiv0\pmod4,\\
(n-4p+2)/4,&n\equiv2\pmod4.
\end{cases}}
\]
All displayed ranks are nonnegative integers in the stated parameter range. In particular, for every odd \(n\equiv1\pmod4\) in that range, the full symmetry quotient is rationally acyclic, whereas for odd \(n\equiv3\pmod4\) its top reduced rational homology has rank \((n-4p+1)/2\).

## Assumptions and scope
The graph is the undirected simple \(p\)-th cycle power, not a directed cycle or a total-cut complex. A disconnected three-set may have zero or one induced edges; the latter case must be retained. The group is the geometric dihedral group of order \(2n\), and the quotient is the topological orbit space of the geometric realization. The pre-existing shellability theorem applies for exactly the stated \(p,n\) range. Coefficients are \(\mathbb Q\); the result is a rational character and rational quotient-homology classification, not an integral equivariant homotopy classification.

## Proof
**1. A two-independence Alexander dual.** Let \(L=K^\vee\) be the combinatorial Alexander dual on the same \(n\)-element ground set. A set \(U\) is a face of \(L\) if and only if **every** three-element subset of \(U\) induces a connected subgraph of \(G\). For a three-element graph, disconnectedness is equivalent to the existence of a vertex with two nonneighbors. Thus
\[
U\in L\quad\Longleftrightarrow\quad
\text{each vertex of }U\text{ has at most one nonneighbor within }U.
\]
In particular, every singleton and pair is a face, so \(L\) is connected. The shellability and Betti formula from [1, Theorem 1.4] give \(K\simeq\bigvee^\beta S^{n-4}\). Combinatorial Alexander duality gives \(\widetilde H^j(L;\mathbb Q)=0\) unless \(j=1\), and \(\dim H^1(L;\mathbb Q)=\beta\). Complementary oriented faces in the ambient simplex yield the equivariant refinement
\[
\mathcal H\cong\operatorname{sgn}_{\mathbb Z/n\mathbb Z}\otimes H^1(L;\mathbb Q),
\]
where the sign is the parity of the permutation of all \(n\) graph vertices. In particular, for an automorphism \(g\), \(\chi(g)=\operatorname{sgn}(g)\operatorname{tr}(g\mid H^1(L;\mathbb Q))\).

**2. Signed orbit counting.** For any permutation \(g\) of the vertices, let \(m(g)\) be its number of vertex orbits and define
\[
F(g)=\sum_{\substack{U\in L\\gU=U}}(-1)^{o_g(U)},
\]
where \(o_g(U)\) counts \(g\)-orbits contained in \(U\), including \(U=\varnothing\) with \(o_g(\varnothing)=0\). An invariant oriented simplex \(U\ne\varnothing\) has alternating signed Lefschetz contribution \((-1)^{o_g(U)-1}\). Thus the ordinary Lefschetz number is \(\Lambda(g;L)=1-F(g)\). Since \(H^0(L;\mathbb Q)=\mathbb Q\) and all remaining rational cohomology is in degree one, \(\operatorname{tr}(g\mid H^1(L;\mathbb Q))=F(g)\). Hence \(\chi(g)=\operatorname{sgn}(g)F(g)\). For a reflection, every vertex orbit has size one or two, and the empty face and all single-orbit faces together contribute \(1-m(g)\) to \(F(g)\).

**3. Localization of invariant faces for a reflection.** Choose real coordinates along the circle with a reflection acting by \(x\mapsto-x\). Its two geometric axes are at \(0\) and \(n/2\); each is a vertex axis or an edge-midpoint axis. A nonfixed orbit has representative \(x\) with \(0<x<n/2\) and consists of \(\{x,-x\}\), coordinates being integral or half-integral according to the chosen origin. For two distinct such orbits \(x<y\), the two types of interorbit distances are
\[
a=y-x,\qquad b=\min(x+y,n-x-y),\qquad a\le b.
\]
Their four-point union is in \(L\) **if and only if** \(b\le p\). If \(b\le p\), all four interorbit edges are present, and only the two internal mirror-pair edges can be absent, so the condition in step 1 holds. If \(b>p\) and \(a>p\), a vertex has two nonneighbors in the other orbit. In the remaining case \(b>p\ge a\), the two crossed nonedges already consume each vertex's allowed nonneighbor; thus both internal mirror pairs must be edges. Every representative must then lie within \(p/2\) of one of the two axes. If both lie near the same axis, \(b\le p\); if they lie near opposite axes, \(a\ge n/2-p>p\), because \(n\ge6p-3\ge4p+1\). Both contradict the assumed case. Therefore \(b\le p\) is necessary.

Equivalently, two nonfixed orbits can coexist only when \(x+y\le p\) (both near the first axis) or \(n-x-y\le p\) (both near the second). These alternatives cannot mix across a family of three or more nonfixed orbits: their distance regions are disjoint because \(n>4p\), and a representative participating in a near-first-axis pair cannot also participate in a near-second-axis pair. If a reflection fixes a vertex at an axis, that singleton and a mirror pair form a face precisely when the pair is at distance at most \(p\) from the fixed vertex. The two fixed vertices (when present) form a face together, but no nonfixed orbit can be added: one of the antipodal fixed vertices would have two nonneighbors.

**4. Local signed contributions.** Consider invariant faces with at least two reflection orbits; the baseline \(1-m(g)\) was already counted. Near a **vertex axis**, write the nonfixed pair-orbits as \(\{\pm j\}\), for positive integers \(j\). A family of at least two such pairs is admissible exactly when its two largest indices sum to at most \(p\). Adding or removing the fixed central vertex then preserves admissibility, so those contributions cancel in pairs. The only unpaired faces have precisely the fixed vertex and one pair \(\{\pm j\}\), for \(1\le j\le p\). Each contains two orbits and contributes \(+1\); the contribution per vertex axis is therefore \(p\).

Near an **edge-midpoint axis**, write its nonfixed pair-orbits by indices \(j\ge1\), representing distances \(j-1/2\) from the midpoint. Two different such pair-orbits \(j<k\) coexist precisely when \(j+k\le p+1\). An admissible family with at least two pair-orbits is unchanged in admissibility when its nearest pair-orbit, index \(1\), is toggled, provided that removing it leaves at least two pair-orbits. Those terms cancel. The unpaired families are exactly the two-orbit sets \(\{1,j\}\), \(2\le j\le p\), each of sign \(+1\). The contribution per edge-midpoint axis is \(p-1\). Finally, a reflection through two opposite fixed vertices gives one additional admissible two-orbit set consisting of just those two vertices, contributing \(+1\).

For **odd \(n\)** there is one vertex axis, one edge axis and \(m=(n+1)/2\) vertex orbits. Therefore
\[
F(s)=1-m+p+(p-1)=2p-(n+1)/2.
\]
For **even \(n=2k\)**, \(s(i)=-i\) has two vertex axes and \(m=k+1\), while \(rs(i)=1-i\) has two edge axes and \(m=k\). Hence
\[
F(s)=1-(k+1)+2p+1=2p+1-k,\qquad
F(rs)=1-k+2(p-1)=2p-1-k.
\]
A reflection with \(m\) orbits has permutation sign \((-1)^{n-m}\); multiplying gives exactly the three reflection formulas in the finding. Conjugacy supplies every \(r^a s\).

**5. Rotations and full quotients.** For completeness, the cyclic character [4] can be verified from \(L\). A nonidentity rotation of order at least three fixes no nonempty simplex of \(L\): its orbit contains one vertex and two other vertices at cyclic distance greater than \(p\) from it (choose orbit offset \(\lceil m/3\rceil\) at orbit order \(m\ne4\), and offset one when \(m=4\)). Thus \(\Lambda=0\) and its \(H^1\)-trace is \(1\). When \(n=2k\), the half-turn fixes exactly the \(k\) antipodal two-vertex simplices, each contributing \(+1\) to \(\Lambda\); hence its \(H^1\)-trace is \(1-k\). Multiplication by the permutation sign gives the stated rotations.

Over \(\mathbb Q\), homology of the orbit space by a finite group is the invariant part of the original homology (averaging/transfer). Therefore the full quotient's rank in degree \(d\) is \((2n)^{-1}\sum_{g\in D_n}\chi(g)\). If \(n\) is odd, averaging rotations gives \(b=(n-4p+1)/2\), and all reflections have trace \((-1)^{(n+1)/2}b\); the average is \(0\) or \(b\) as shown. If \(n=2k\), the cyclic-invariant rank is \(k-2p-1\) when \(k\) is even and \(k-2p\) when \(k\) is odd. The sum of the two reflection-class character values is \(-2(-1)^k\). Averaging over the two equal-size reflection classes gives \((k-2p-2)/2\) for even \(k\), and \((k-2p+1)/2\) for odd \(k\), proving the remaining cases.

## Verification
Run `python3 verify.py` with the Python 3 standard library. It directly enumerates invariant faces of the Alexander dual using **connected triples** rather than the proof's local-axis classification, applies actual signed simplex permutations, and checks 90 independent reflection cases for \(2\le p\le7\) near the shellability threshold. It also enumerates the original ordinary cut complex directly for six symmetry instances, recomputes full dihedral character averages from all individual signed dual-chain actions for 21 parameter pairs, and computes dual first mod-two homology from triangle boundary matrices for five parameter pairs. The recorded deterministic output is in `verify_output.txt`. Those finite tests independently stress-test the exact signs, boundaries, and normalization; the all-parameter statement comes from the proof, not the tests.

## Relationship to prior work
Chauhan and Shukla [1] prove shellability and the precise **nonequivariant** sphere count for the cycle powers, and Chauhan, Shukla and Vinayak [2] prove the earlier \(p=2\) special case. Bayer and collaborators [3] determine dihedral representations for ordinary cut complexes of the **unpowered** cycles, not the powers with \(p\ge2\). The published cyclic-representation result [4] already determines every rotational character for the exact same parameters but explicitly leaves the reflection classes and dihedral quotient homology undetermined. The new contribution is the all-parameter reflection computation, which completes the dihedral character and yields the full quotient Betti formula. The assertion is not merely a rephrasing of a known rotation character or of the nonequivariant wedge rank.

## Limitations
No claim is made about integral dihedral module structures, integral orbit homology, homotopy types of the quotients, or parameters below \(n\ge6p-3\). The outside shellability theorem is used as a premise, not reproved here. The reflection localization proof uses the strict spacing \(n>4p\) implied by that range; it must not be extrapolated without checking the spacing condition. Finite computations do not establish infinite formulas. An unindexed equivalent equivariant calculation remains a possible literature-overlap risk.

## References
1. P. Chauhan and S. Shukla, *Shellability of 3-cut complexes of powers of cycle graphs*, arXiv:2603.23155v1, first submitted 2026-03-24, Theorem 1.4, Section 3 and conclusion. https://arxiv.org/abs/2603.23155
2. P. Chauhan, S. Shukla and K. Vinayak, *Shellability of 3-Cut Complexes of Squared Cycle Graphs*, arXiv:2406.01979v2, Theorem 1.4 and Section 4. https://arxiv.org/html/2406.01979v2
3. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158, Section 6.2 and Theorem 6.6. https://arxiv.org/abs/2407.08158
4. *Rational cyclic homology representations of three-cut complexes of cycle powers*, published research record (2026), with exact full cyclic character and stated scope limitation. https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-rational-cyclic-homology-representations-of-three-cut-complexes--dc0f17aad16d/RESULT.md
