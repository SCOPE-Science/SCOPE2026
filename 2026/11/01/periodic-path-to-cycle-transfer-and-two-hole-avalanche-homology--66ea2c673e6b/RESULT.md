# Periodic path-to-cycle transfer and two-hole avalanche homology

## Finding
Let \(P_{kd}\) denote the consistently oriented path with nonsink vertices \(0,\ldots,kd-1\), arrows \(i\to i+1\), and a terminal sink \(kd\) which never fires. For a binary motif \(R\subseteq\mathbb Z/d\mathbb Z\), put one grain at precisely the positions \(i\) with \(i\bmod d\in R\), and perform synchronous sandpile firing. The avalanche complex \(X_{d,R,k}\) is the downward closure of all sets of nonsink vertices firing in a common round.

**Periodic transfer theorem.** For every integer \(d\ge3\), every integer \(k\ge2\), and every nonempty motif \(R\subseteq\mathbb Z/d\mathbb Z\), there is a homotopy equivalence
\[
X_{d,R,k}\simeq\mathcal A(\overrightarrow C_d,\mathbf1_R),
\]
where the right-hand complex comes from the cyclically oriented \(d\)-cycle. The nerve of the first \(d\) firing simplices is explicitly the complex with facets \(a-R\) for \(a\in\mathbb Z/d\mathbb Z\), hence is isomorphic to the cyclic avalanche complex by the label inversion \(t\mapsto-t\). The assertion is about ordinary homotopy, not an equivariant equivalence.

**Two-missing-residue classification.** Suppose also that \(R=(\mathbb Z/d\mathbb Z)\setminus\{0,h\}\), where \(1\le h<d\). Define
\[
g=\gcd(d,h),\qquad L=d/g,\qquad s=\left\lfloor\frac{L+1}{3}\right\rfloor,\qquad j=d-gs-2,
\]
and
\[
b=\begin{cases}2^g,&3\mid L,\\1,&3\nmid L.\end{cases}
\]
Then for all integers \(i\),
\[
\widetilde H_i(X_{d,R,k};\mathbb Z)\cong
\begin{cases}\mathbb Z^b,&i=j,\\0,&i\ne j.\end{cases}
\]
The groups are torsion-free and independent of the number of complete repetitions \(k\ge2\). A notable subfamily is \(d=3g\), \(h=g\), and \(g\ge2\), where the only nonzero reduced group is \(\widetilde H_{2g-2}\cong\mathbb Z^{2^g}\). Thus a finite terminating path exhibits an exponentially growing higher-dimensional Betti number even though its binary initial state is periodic.

## Assumptions and scope
All indices and arithmetic are integral; \(d\ge3\), \(k\ge2\), and \(R\ne\varnothing\). Every nonsink vertex has outdegree one. A nonsink vertex holding at least one grain fires, loses one grain, and passes it to its right neighbor; the terminal sink absorbs grains without firing. At every round, all eligible vertices fire simultaneously. No vertex initially holds more than one grain. For the second statement, \(R\) has exactly two missing residues, which are distinct. When \(L=2\), an edge component below is interpreted as \(K_2\), not as a multigraph two-cycle. Homology is reduced integral simplicial homology, including degree zero.

## Proof
**Step 1: exact binary dynamics.** Number nonsink vertices from zero. For \(0\le t<kd\) the firing set is exactly
\[
F_t=\{i+t:0\le i<kd-t,\ i\bmod d\in R\}.
\]
Indeed each grain advances exactly one step per round until it reaches the sink, and two grains never collide because they retain their initial separation. Every configuration remains binary. For \(t\ge kd\) the firing set is empty. If \(d\le t<kd\), the inclusion \(F_t\subseteq F_{t-d}\) follows from the fact that each predecessor index \(i\) in the displayed formula satisfies \(i+d<kd\) and \((i+d)\bmod d=i\bmod d\). Hence the \(d\) simplices on \(F_0,\ldots,F_{d-1}\) already cover the entire avalanche complex.

**Step 2: identify its nerve, with no boundary loss.** The nerve has vertex set \(\mathbb Z/d\mathbb Z\), corresponding to times \(0,\ldots,d-1\). For a nonempty set of times \(T\), the intersection \(\bigcap_{t\in T}F_t\) is nonempty if and only if
\[
\exists a\in\mathbb Z/d\mathbb Z\quad\forall t\in T:\ a-t\in R\pmod d.
\]
The forward implication is reduction of a common physical firing vertex modulo \(d\). Conversely, choose the representative \(0\le a<d\) of the witnessing residue. The physical vertex \(a+d\), lying in \([d,2d-1]\subseteq[0,kd-1]\), belongs to every \(F_t\): its predecessor \(a+d-t\) lies in \([1,2d-1]\) and has the stipulated residue. This is where \(k\ge2\) is used. The nerve therefore has facets \(a-R\) for every \(a\), as claimed. These facets become translates \(-a+R\) after inverting vertex labels, exactly the firing supports on the directed \(d\)-cycle with initial binary support \(R\). Since all nonempty intersections of the firing simplices are simplices and hence contractible, the simplicial nerve theorem gives the claimed homotopy equivalence.

**Step 3: Alexander dual for two holes.** Put \(V=\mathbb Z/d\mathbb Z\). If \(R=V\setminus\{0,h\}\), then the nerve facets are precisely \(V\setminus\{a,a-h\}\). Let \(H\) be the simple graph with edges \(\{a,a-h\}\), where \(a\in V\). Its connected components are the orbits of repeated addition by \(h\): it is the disjoint union of \(g\) ordinary cycles of length \(L=d/g\) when \(L\ge3\), or \(g\) copies of \(K_2\) when \(L=2\). Denote the independence complex by \(I(H)\). The nerve is exactly the combinatorial Alexander dual
\[
K=I(H)^*=\{T\subseteq V:V\setminus T\notin I(H)\},
\]
since \(T\) lies in some facet precisely if its complement contains an edge of \(H\).

**Step 4: calculate the independence homology integrally.** The familiar cycle-independence calculation is
\[
I(C_L)\simeq
\begin{cases}
S^{s-1}\vee S^{s-1},&L\equiv0\pmod3,\\
S^{s-1},&L\equiv1,2\pmod3,
\end{cases}
\]
for \(L\ge3\), with \(s=\lfloor(L+1)/3\rfloor\); for \(L=2\), \(I(K_2)\simeq S^0\), which matches the second case. For completeness, the path recurrence \(I(P_m)\simeq\Sigma I(P_{m-3})\), \(m\ge3\), follows by deleting the second vertex: the deletion has an isolated first vertex and hence is a cone, while the closed-neighborhood deletion is \(P_{m-3}\). Starting with \(I(P_1)\) contractible and \(I(P_2)\simeq S^0\), the recurrence determines all path cases. Deleting one vertex from a cycle yields the cofibre of \(I(P_{L-3})\to I(P_{L-1})\); its map is null because one side is contractible or the source has strictly smaller sphere dimension than the target. The elementary base cases \(L=3,4,5\) complete the stated cycle formula. The independence complex of a disjoint union is the simplicial join of the component independence complexes. Therefore
\[
I(H)\simeq\bigvee^{b}S^{gs-1},
\qquad b=\begin{cases}2^g,&3\mid L,\\1,&3\nmid L.\end{cases}
\]
In particular, this supplies torsion-free integral cohomology concentrated in degree \(gs-1\).

**Step 5: apply integral combinatorial Alexander duality.** The duality theorem on a ground set of \(d\) vertices gives
\[
\widetilde H_i(K;\mathbb Z)\cong\widetilde H^{d-i-3}(I(H);\mathbb Z).
\]
Since \(I(H)\) has reduced cohomology \(\mathbb Z^b\) only in degree \(gs-1\), the sole nonzero reduced homology group of \(K\), and hence of the original avalanche complex, occurs at \(i=d-gs-2\), with rank \(b\). All steps are integral; no inference about integral torsion is made from finite-field experiments. This completes the proof.

## Verification
Run `python3 check_avalanche.py` with Python 3 and its standard library. The program implements synchronous firing explicitly (including loss at the sink), constructs the actual nerve by all finite intersections of the first \(d\) firing supports, independently constructs the predicted Alexander-dual nerve from the two missing residues, and computes reduced homology from mod-two simplicial boundary ranks. It verified all \(108\) cases with \(3\le d\le11\), \(1\le h<d\), and \(k\in\{2,3\}\). A separate exhaustive check covered \(996\) choices of nonempty arbitrary binary motifs, periods \(3\le d\le8\), and repetition counts \(k\in\{2,3\}\), confirming the general nerve comparison in those cases. The output includes `records_sha256 35432691bbad8b43c8e8863a3431c9f7354afa8f13982896828eda9dc8c078a6`. Finite checks do not prove the infinite-parameter theorem or establish integer torsion-freeness; those follow from the displayed structural proof and integral duality.

## Relationship to prior work
Riihimäki and Smith (2026) introduced avalanche homology, the simplex-cover nerve construction, and homotopy computations for selected directed-path and directed-cycle initial states. Their Lemma 3.7 handles single-residue support on paths, Proposition 3.19 handles two occupied positions on cycles, and Theorem 3.21 handles consecutive occupied positions on cycles. These results cover some small or cyclic special cases of the two-hole formula. In particular, when \(g=1\) the cyclic two-hole complex is isomorphic, by multiplying labels by the inverse of \(h\), to the consecutive-complement case of their theorem. When \(L=2\), their Conjecture 3.18 predicts the relevant cyclic sphere dimension. **No novelty is claimed for those already determined cyclic specializations, for the cyclic two-occupant graph description, or for the classical cycle-independence and Alexander-duality formulas.** The new structural assertion transfers an arbitrary repeated binary initial state on a terminating directed path to a periodic directed-cycle avalanche complex after two repeats, and gives the uniform homological classification of two-hole repeated path states, with exponential ranks for \(3\mid L\) and \(g\ge2\).

The closest indexed complementary-residue avalanche result treats coprime cycle lengths and circular intervals, not the present genuinely periodic sink paths or the noncoprime two-hole family. The new result uses rather than replaces earlier general nerve and Alexander-duality theory. A broader unindexed transfer theorem or an implicit statement in other literature remains possible.

## Limitations
The transfer assumes binary initial states repeated at least twice. It need not hold with a single copy or arbitrary initial grain multiplicities. The explicit homology classification assumes exactly two zero positions per period, with \(d\ge3\) and \(k\ge2\). It determines reduced integral homology, not a wedge-of-spheres homotopy type or a canonical equivariant representation. The finite verifier computes mod-two ranks only; integral torsion-freeness is proven by Alexander duality and the independence-complex calculation. No independent audit has been performed.

## References
1. H. Riihimäki and J. P. Smith, *Avalanche homology of digraphs via sandpile dynamics*, arXiv:2606.26786v1, first posted 2026-06-25. See §§2.1–2.11 and 3.1–3.2, especially Lemma 3.7, Proposition 3.19, and Theorem 3.21. https://arxiv.org/abs/2606.26786 .
2. A. Björner and M. Tancer, *Combinatorial Alexander Duality—a Short and Elementary Proof*, arXiv:0710.1172, Theorem 1.1; *Discrete & Computational Geometry* 42 (2009), 586–593. https://arxiv.org/abs/0710.1172 .
3. D. N. Kozlov, *Complexes of Directed Trees*, *Journal of Combinatorial Theory, Series A* 88 (1999), 112–122, DOI 10.1006/jcta.1999.2984; classical cycle-independence homotopy calculation, reconstructed in the proof above.
