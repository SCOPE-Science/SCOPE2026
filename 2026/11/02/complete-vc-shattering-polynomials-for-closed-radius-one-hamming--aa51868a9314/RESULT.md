# Complete VC-shattering polynomials for closed radius-one Hamming balls

## Finding
Let \(d\ge1\) and \(q\ge2\) be integers. Let \(H(d,q)\) have vertex set \([q]^d\), where two vertices are adjacent when they differ in exactly one coordinate. For each center \(c\), take its **closed** radius-one Hamming ball \(B(c)=\{x:d_H(x,c)\le1\}\). The concept family is \(\mathcal B_{d,q}=\{B(c):c\in[q]^d\}\), without adding the empty or universal set. Let \(s_k(d,q)\) be the number of \(k\)-point query supports \(S\subseteq[q]^d\) such that every trace \(B(c)\cap S\), as \(c\) varies, occurs. Define \(\Phi_{d,q}(z)=\sum_{k\ge0}s_k(d,q)z^k\), with the empty support contributing one.

The **complete** polynomial is as follows:

\[
\Phi_{d,q}(z)=
\begin{cases}
1, &d=1,\\
1+4z, &(d,q)=(2,2),\\
1+9z+36z^2, &(d,q)=(2,3),\\
1+q^2z+\dfrac{q^2(q-1)(q+1)}2z^2
 +q^2(q-1)^2(q-2)z^3, &d=2,\ q\ge4,\\
1+q^dz+\dfrac{q^d}{2}\left[d(q-1)+\binom d2(q-1)^2\right]z^2
 +q^d(q-1)^3\binom{d+1}{3}z^3, &d\ge3.
\end{cases}
\]

There are no shattered supports of size four or larger. In the full-dimensional regime \(d\ge3\), the number of shattered triples factorizes as \(q^d(q-1)^3\binom{d+1}{3}\), a coefficient not implied by merely knowing that VC dimension is three. The resulting VC dimensions are \(0\) for \(d=1\), \(1\) for \((d,q)=(2,2)\), \(2\) for \((d,q)=(2,3)\), and \(3\) otherwise. These dimension values are stated only as consequences and are **not** asserted as a new dimension classification; the new assertion is the full coefficientwise profile and support classification.

## Assumptions and scope
The alphabet \([q]=\{0,1,\ldots,q-1\}\) is only a finite set; no field or arithmetic structure is assumed. Hamming distance \(d_H\) counts unequal coordinates. A support \(S\) is VC-shattered if for every \(T\subseteq S\) there exists \(c\in[q]^d\) with \(B(c)\cap S=T\). A ball includes its center. No graph-induced-subgraph assertion, larger ball radius, or adaptive dimension statement is made. The displayed formulas cover every integer \(d\ge1\), \(q\ge2\), including the small parameter exceptions.

## Proof
**1. Geometry of a ball.** Fix a reference center \(o\). Every element of \(B(o)\) is either \(o\) or differs from \(o\) in one coordinate. Partition \(B(o)\setminus\{o\}\) into \(d\) coordinate groups, each having \(q-1\) members. If \(c\ne o\), the intersection \(B(c)\cap(B(o)\setminus\{o\})\) has one of these forms: all of one coordinate group when \(d_H(c,o)=1\); at most two members, from two distinct groups, when \(d_H(c,o)=2\); and the empty set when \(d_H(c,o)\ge3\). The first assertion includes all members of a coordinate group because a ball centered on its coordinate line contains the entire line; the second follows by the two possible coordinate recombinations. For any fixed coordinate line, an arbitrary radius-one ball meets that line in either the entire line, one point, or the empty set.

**2. No shattered support of size four.** Suppose four distinct vertices \(S\) are shattered. A ball \(B(o)\) contains all four. If \(o\in S\), the other three vertices are neighbors of \(o\). If all three belong to one coordinate group, the line-intersection property prevents shattering even that triple. Otherwise, by step 1 no ball other than \(B(o)\) can contain all three neighbors, so their trace without \(o\) is impossible. If \(o\notin S\), the four vertices are neighbors of \(o\). If all lie in one coordinate group, no two-positive/two-negative trace is possible. Otherwise choose a triple involving two different coordinate groups. Step 1 says only \(B(o)\) covers this triple; but it also covers the fourth vertex, so the triple-alone trace is impossible. Hence \(s_k=0\) for all \(k\ge4\).

**3. One- and two-point supports.** If \(d=1\), every ball is the whole vertex set and no singleton is shattered. For \(d\ge2\), every singleton is shattered: its own ball includes it, and a word at Hamming distance two excludes it. Any two vertices of Hamming distance exceeding two cannot be shattered because no radius-one ball contains both. For \(d\ge3\), every pair at distance one or two is shattered. The inclusion trace is realized by a center within distance one of both; each singleton trace is realized by changing a coordinate not shared in the same way by the two points (or by the point itself when their distance is two). The empty trace is realized for a distance-one pair by changing two other coordinates; for a distance-two pair it is realized by using a third coordinate and one of the two varying coordinates. All stated constructions use only two alphabet values. For \(d=2,q\ge3\), empty traces instead use a third alphabet value in each of the appropriate coordinates. For \((d,q)=(2,2)\), the four balls are complements of the four antipodes, so no pair is shattered. Consequently for \(d\ge3\), and also for \(d=2,q\ge3\), the pair count is the number of unordered pairs at distances one or two:
\[
 s_2(d,q)=\frac{q^d}{2}\left[d(q-1)+\binom d2(q-1)^2\right].
\]
The \(d=2\) form simplifies to \(q^2(q-1)(q+1)/2\).

**4. All possible triple shapes.** A shattered triple is contained in some \(B(o)\). Three points on the same coordinate line are not shattered because a ball meets that line in only zero, one, or all points. Every remaining triple is of precisely one of the following types, after renaming coordinates and alphabet symbols relative to \(o\):

- Type I (pivot): \(\{o,x_i,x_j\}\), with \(x_i\), \(x_j\) nonzero changes in two different coordinates \(i\ne j\).
- Type II (three axes): \(\{x_i,x_j,x_k\}\), with changes in three distinct coordinates.
- Type III (repeated axis): \(\{x_i,y_i,x_j\}\), where \(x_i,y_i\) are distinct nonzero changes along coordinate \(i\) and \(x_j\) changes a different coordinate.

These types are disjoint according to their pairwise Hamming-distance patterns: respectively \((1,1,2)\), \((2,2,2)\), and \((1,2,2)\). In each case the indicated center \(o\) is unique: the adjacent pivot is unique in I; in II a center distinct from \(o\) cannot cover three different coordinate groups; and in III the unique coordinate-line member covering the third-axis point is \(o\).

**5. Sufficient witnesses and the exceptional second dimension.** Write \(o=0\), and denote a word with one nonzero coordinate \(i\) by \(ae_i\), with two such coordinates by \(ae_i+be_j\); this is only shorthand for coordinate replacement, not arithmetic. Type I with \(S=\{0,ae_i,be_j\}\) is shattered when \(d\ge3\). The full trace has center \(0\); the three two-point traces have centers \(ae_i\), \(be_j\), and \(ae_i+be_j\). Choose a third coordinate \(k\) and nonzero \(t\). Centers \(te_k\), \(ae_i+te_k\), and \(be_j+te_k\) give the singleton traces for \(0\), \(ae_i\), and \(be_j\), respectively; center \(ae_i+be_j+te_k\) gives the empty trace.

Type II with \(S=\{ae_i,be_j,ce_k\}\), \(i,j,k\) distinct, is shattered for \(d\ge3\): center \(0\) gives all, each pairwise coordinate combination gives exactly that pair, each vertex itself gives its singleton, and the three-coordinate combination gives the empty trace.

For Type III, put \(S=\{ae_i,be_i,ce_j\}\) with \(a\ne b\), all three symbols nonzero. Center \(0\) gives all. Centers \(ae_i\), \(ae_i+ce_j\), \(be_i+ce_j\) give the three pairs. Center \(ce_j\) gives its singleton. If \(d\ge3\), choose an additional coordinate \(k\) and nonzero \(t\); centers \(ae_i+te_k\), \(be_i+te_k\), and \(te_k\) give the other singletons and the empty trace. If \(d=2\), the other singleton traces exist by using a value distinct from \(0,c\) in coordinate \(j\). The empty trace requires a center whose coordinate \(i\) avoids all three values \(0,a,b\) and whose coordinate \(j\) avoids \(0,c\). This exists exactly when \(q\ge4\). Type I needs a third coordinate to realize the pivot singleton; Type II needs three coordinate groups. Thus when \(d=2\), only Type III triples survive, and only for \(q\ge4\).

**6. Count without duplication.** Put \(N=q^d\). In dimension at least three, the numbers of the three types are, respectively,
\[
N\binom d2(q-1)^2,\qquad
N\binom d3(q-1)^3,\qquad
Nd(d-1)\binom{q-1}{2}(q-1).
\]
Every triple has exactly one indicated center as shown in step 4, so there is no overcounting. Combining the first and third terms gives \(N\binom d2(q-1)^3\); adding the second gives \(N(q-1)^3\binom{d+1}{3}\) by Pascal's identity. In dimension two with \(q\ge4\), the Type III count is \(q^2(q-1)^2(q-2)\). The other small cases have no shattered triples. Together with steps 2–3 and the empty-support convention, this proves the complete polynomial for every stated parameter.

## Verification
The included standalone `check_hamming_shattering.py` reconstructs every radius-one neighborhood as a bitset and enumerates all possible Boolean traces on candidate supports. It tests sixteen parameter pairs, including complete support checks through size four for nontrivial small cases, and separately evaluates the triple-type count identity. The exact output from a completed run is embedded in `verification_output.txt`. The program uses no external packages. Full enumeration is finite corroboration only; the all-parameter statement follows from the proof above.

## Relationship to prior work
Adler, Benediktsson, and Macpherson (2020) analyze **open** graph neighborhoods of Hamming graphs and prove exact VC-dimension bounds for that different set system (Theorems 4.6–4.8); their abstract also notes bounded VC dimension for closed neighborhoods. Those results do not enumerate closed-ball shattered supports or imply the coefficients here. Coudert, Csikós, Ducoffe, and Viennot (2024) provide general algorithms and bounds for closed-neighborhood graph VC dimension, rather than a Hamming-family coefficientwise enumeration. The static VC-dimension thresholds for closed Hamming balls have also been obtained separately and are not the novelty asserted here. The present contribution is the all-parameter exact enumeration of support sizes zero through three, with the complete three-type classification and exact small-alphabet exceptions.

## Limitations
No historical-uniqueness theorem is claimed. Equivalent enumerations may be recorded under coding-theoretic, incidence, or finite-geometric terminology. The literature comparisons identify no dominating statement in inspected sources, but do not exhaust all publications. The theorem does not address open balls, radii above one, induced subgraphs, or online-learning dimensions.

## References
1. I. Adler, B. G. Benediktsson, and D. Macpherson, *Vapnik–Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042v1 (first publicly posted 2020-07-31), especially Theorems 4.6–4.8; later Discrete Applied Mathematics 312 (2022), 29–44. https://arxiv.org/abs/2007.16042
2. D. Coudert, M. Csikós, G. Ducoffe, and L. Viennot, *Practical Computation of Graph VC-Dimension*, arXiv:2405.07588v1 (first posted 2024-05-13), SEA 2024, Article 8. https://arxiv.org/abs/2405.07588
