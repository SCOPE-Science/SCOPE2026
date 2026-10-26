# Minimum forts of squared cycles: a cyclic-gap classification and exact enumeration

## Finding
For every integer \(n\ge 6\), let \(G_n=C_n^2\) be the simple graph with vertices \(\mathbb Z/n\mathbb Z\), two distinct vertices being adjacent precisely when their difference is \(\pm1\) or \(\pm2\) modulo \(n\). A **fort** is a nonempty vertex set \(F\) such that every vertex outside \(F\) has either zero or at least two neighbors in \(F\). Write \(f_n\) for the minimum fort size, and \(M_n\) for the number of forts attaining that size, with all \(n\) vertices distinguished. Then

\[
f_n=\left\lceil\frac n3\right\rceil,
\qquad
M_n=\begin{cases}
3,&n\equiv0\pmod3,\\
\dfrac{n(n+5)}6+5\mathbf1_{\{n=10\}},&n\equiv1\pmod3,\\
n,&n\equiv2\pmod3.
\end{cases}
\]

There is also a classification of every fort (not merely the smallest). List the selected vertices of a nonempty \(F\) in cyclic order and let \(g_1,\ldots,g_m\) be their positive cyclic successive gaps, with \(m=|F|\) and \(\sum_i g_i=n\). Then \(F\) is a fort **if and only if** every gap belongs to \(\{1,2,3,4\}\), and whenever \(g_i=4\), both adjacent gaps (with cyclic indices) equal \(1\). This gap rule explicitly describes all minimum forts. In particular, the only minimum forts containing a gap of length \(4\) occur at \(n=10\), when the four gaps alternate \(1,4,1,4\), producing five exceptional forts.

The standard graph-spark and failed zero-forcing identities also give \(\operatorname{spark}(G_n)=\lceil n/3\rceil\) and \(F(G_n)=\lfloor2n/3\rfloor\). These numerical corollaries are recorded for context; they are not asserted to be novel relative to the prior literature on failed zero forcing of circulant graphs. The central contribution is the **complete minimum-fort structure and its exact multiplicity**, including the isolated ten-vertex correction.

## Assumptions and scope
The graph is simple and undirected; all vertices are labeled by residues. The restriction \(n\ge6\) ensures that the four displacement neighbors \(\pm1,\pm2\) of every vertex are distinct. The fort size is a *minimum-cardinality* invariant; this is distinct from counting every inclusion-minimal fort. Cyclic gaps are ordered clockwise in the natural residue order and are counted with positive lengths even for singleton candidate sets. The formula enumerates distinct labeled subsets, not rotation or dihedral orbits.

## Proof
**1. Exact local gap criterion.** Let successive selected vertices be \(u\) and \(u+d\), with no selected vertex strictly between them in cyclic order. If \(d\ge5\), vertex \(u+2\) is not selected and has \(u\) as its unique selected neighbor among its two predecessors and two successors: the next selected vertex is at least three steps ahead of it, and the preceding selected vertex is at least three steps behind it. Thus the fort condition fails. For \(d=2\) the sole unselected vertex lies next to both selected endpoints. For \(d=3\) the two unselected vertices each lie within distance two of both endpoints. For \(d=1\) there is no unselected vertex in the gap. Finally, for \(d=4\), the midpoint \(u+2\) sees both endpoints; \(u+1\) sees the left endpoint but also needs the immediately preceding selected vertex \(u-1\), so the preceding gap must be \(1\); symmetrically \(u+3\) requires the following selected vertex \(u+5\), so the following gap must be \(1\). Conversely these checks cover every unselected vertex, establishing necessity and sufficiency of the stated rule. The argument also excludes singletons, whose only cyclic gap is \(n\ge6\).

**2. Lower bound.** Let \(a,b,c\) count gaps of lengths \(4,1,2\), respectively, in an arbitrary fort; all remaining gaps have length \(3\). A length-\(4\) gap has two neighboring length-\(1\) gaps, whereas a length-\(1\) gap can neighbor at most two length-\(4\) gaps. Counting these incidences gives \(a\le b\). Consequently
\[
n=3m+a-2b-c\le 3m,
\]
so \(m\ge\lceil n/3\rceil\).

**3. Attainment.** If \(n=3t\), use \(t\) gaps of length \(3\). If \(n=3t+2\), use \(t\) gaps of length \(3\) and one of length \(2\). If \(n=3t+1\), use \(t\) gaps of length \(3\) and one of length \(1\). In every case there are \(\lceil n/3\rceil\) gaps, and the gap criterion gives a fort, proving equality in the bound.

**4. Equality configurations.** Put \(m=\lceil n/3\rceil\) and \(\delta=3m-n\in\{0,1,2\}\). The gap counts satisfy
\[
\delta=2b+c-a,
\qquad a\le b,
\quad\text{hence}\quad b+c\le\delta.
\]
If \(\delta=0\), there are no non-three gaps. If \(\delta=1\), the only feasible pattern is one gap of length \(2\): the algebraic alternative with one \(1\) and one \(4\) would force the sole \(1\) to occur on *both* sides of that \(4\), impossible for at least three cyclic gap positions. (Here \(n\ge8\).) If \(\delta=2\), the possibilities are (i) one \(1\); (ii) two \(2\)'s; (iii) one each of \(1,2,4\); or (iv) two \(1\)'s and two \(4\)'s. Configuration (iii) fails the two-neighbor requirement around its single \(4\) because \(m\ge3\). Configuration (iv) forces each \(4\) to have the two \(1\)'s as neighbors. In a cyclic sequence with at least three terms this forces precisely the four-term alternating sequence \((1,4,1,4)\), up to rotation. Its sum is \(10\), so it occurs only for \(n=10\). Thus the listed minimum configurations are exhaustive.

**5. Counting labeled sets.** For any class of allowed cyclic gap words of length \(m\) containing \(n\) total steps, the number of distinct selected subsets is \(n/m\) times the number of gap words rooted at a selected vertex: count pairs consisting of an indexed root \(u\in\mathbb Z/n\mathbb Z\) and a rooted gap word, and note that each \(m\)-element set has exactly \(m\) roots. Therefore all-three gaps yield \(n/m=3\) sets. The single-two pattern has \(m\) rooted words and yields \(n\) sets. In the \(n\equiv1\) case, the single-one pattern contributes \(n\), while choosing the two positions of the two-two gaps contributes \(n\binom m2/m=n(m-1)/2\). Their sum is \(n(m+1)/2=n(n+5)/6\), because \(m=(n+2)/3\) here. The two alternating four-gap words at \(n=10\) contribute an additional \(10\cdot2/4=5\) sets. This proves both the classification and the exact enumeration.

**6. Standard equivalences.** Theorem 2.2 and Observation 2.5 of Deaett et al. identify graph spark with smallest fort size, and ordinary failed zero-forcing number with order minus graph spark. Substituting the proved \(f_n\) gives the stated numerical corollaries. No conclusion is drawn about skew zero forcing.

## Verification
Run `python3 verify.py` using Python 3.8 or later; the program requires only the standard library and has no external inputs. It uses the defining neighborhood test, independently of the cyclic-gap formula, on every nonempty vertex subset for \(6\le n\le14\), checking the biconditional in step 1. It also exhaustively checks all subsets of cardinality up to \(\lceil n/3\rceil\) for every \(6\le n\le24\), establishing no smaller fort and confirming exact minimum-fort counts in those finite cases. The recorded output is in `verification_output.txt`. It additionally isolates exactly five ten-vertex exceptional minimum forts. This finite testing supports but does **not** substitute for the unrestricted proof above.

## Relationship to prior work
Becker, Cameron, Hanely, Ong, and Previte [1] study inclusion-minimal forts and enumerate them for ordinary cycles, paths, spiders, wheels, sunlets, and windmills. Their 2024 full text was examined; its ordinary-cycle statements and graph-product methods do not determine this minimum-size layer for squared cycles. Deaett et al. [2] prove the general spark/fort and failed-zero-forcing identities, which explain the significance of minimum forts but do not specify their multiplicity in squared cycles. Gomez, Rubi, Terrazas, Flórez, and Narayan [3] study the failed zero-forcing number of circulant graphs, so the numerical failed-zero-forcing statement must not be treated as independently new: their public abstract was readable, but the institutional repository full-text endpoint denied access in this review. The exact minimum-fort *enumeration*, the gap classification, and the exceptional \(n=10\) configurations are not implied by knowing only a failed zero-forcing **number**. Johnson et al. [4] address **skew** failed zero forcing for cyclic powers, a different forcing rule, and their reported numerical results do not supply this classification. Potential coverage hidden in an inaccessible full text remains an identified priority risk.

## Limitations
The theorem concerns all \(n\ge6\) at power exactly two, not arbitrary powers of a cycle. It counts minimum-cardinality forts, not every inclusion-minimal fort. The direct counting formula distinguishes vertex labels and does not classify dihedral orbits. Earlier circulant failed-zero-forcing literature may independently give the minimum value; priority for that numerical value is expressly not claimed. One closely relevant original paper [3] was available as an abstract but not as full text; a later or unindexed description of minimum-fort configurations might overlap with the result. Independent mathematical review has not been performed.

## References
[1] P. Becker, T. R. Cameron, D. Hanely, B. Ong, and J. P. Previte, *On the number of minimal forts of a graph*, arXiv:2404.05963v1 (first public 2024-04-09). https://arxiv.org/html/2404.05963v1

[2] L. Deaett, S. Fallat, V. Furst, J. Hutchens, L. Mitchell, and Y. Zhang, *The Spark of Symmetric Matrices Described by a Graph*, arXiv:2307.00376v2, Theorem 2.2 and Observation 2.5 (first public 2023-07-01). https://arxiv.org/html/2307.00376v2

[3] L. Gomez, K. Rubi, J. Terrazas, R. Flórez, and D. A. Narayan, *Failed Zero Forcing Numbers of Trees and Circulant Graphs*, *Theory & Applications of Graphs* 11(1), Article 5 (2025), DOI:10.20429/tag.2024.110105. https://digitalcommons.georgiasouthern.edu/tag/vol11/iss1/5/

[4] A. Johnson, A. Vick, R. Flórez, and D. A. Narayan, *Failed Skew Zero Forcing Numbers of Path Powers and Circulant Graphs*, *AppliedMath* 5(2), Article 32 (2025), DOI:10.3390/appliedmath5020032. https://www.mdpi.com/2673-9909/5/2/32
