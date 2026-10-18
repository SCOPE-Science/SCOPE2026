# Rooted Horn-circuit spectrum of Hamming geodesic convexity and a quasipolynomial direct-basis barrier

## Finding

Let \(d,q\ge 2\) be integers, \(V=[q]^d\), and let \(c\) be geodesic convex hull in the Hamming graph \(H(d,q)=K_q\square\cdots\square K_q\). A **nontrivial rooted stem for \(x\in V\)** is an inclusion-minimal set \(B\subseteq V\setminus\{x\}\) such that \(x\in c(B)\). Write \(b_{d,q,r}\) for the number of such stems of cardinality \(r\) for a fixed root \(x\). Then \(b_{d,q,r}=0\) unless \(2\le r\le d\), and in the stated range

\[
\boxed{b_{d,q,r}=\frac1{r!}\sum_{j=0}^{r}(-1)^j\binom rj\bigl(q^r-(q-1)^r-j(q-1)^{r-1}\bigr)^d.}
\]

In particular, \(b_{d,q,d}=(q-1)^{d(d-1)}\), and every intermediate size \(2\le r\le d\) occurs. The complete generating polynomial of **nontrivial prime unit Horn implications** is

\[
\boxed{\mathcal P_{d,q}(z)=q^d\sum_{r=2}^{d}b_{d,q,r}z^r.}
\]

These are precisely the rules \(B\to x\) in the unique inclusion-minimal *single-conclusion, one-simultaneous-pass* basis for \(c\). For any fixed alphabet \(q\ge2\), their total number is \(\exp(\Theta_q(d^2))\), equivalently \(|V|^{\Theta_q(\log |V|)}\), whereas \(c\) has an ordinary, multi-pass unit Horn basis with fewer than \(|V|^3/2\) rules. Thus the requirement of one-pass closure incurs a superpolynomial rule-count blowup in a natural infinite family.

## Assumptions and scope

Here \([q]\) is an arbitrary fixed alphabet of size \(q\), not necessarily a field. Hamming adjacency means differing in exactly one coordinate. The interval \(I(u,v)\) consists of all vertices on shortest \(u,v\)-paths, and a subset is geodesically convex when it contains \(I(u,v)\) for every pair of its vertices. The hull of the empty set is empty. In *one simultaneous pass*, the implications tested on an input \(S\) must use premises contained in the original \(S\), without chaining newly inferred vertices during that pass. A **unit** implication has a single conclusion, and only nontrivial implications with conclusion outside their premise are counted. The statements do not claim a minimum number of grouped or multi-pass implications.

The underlying convex sets have the known rectangular structure (cf. Jiang–Pelayo–Pritikin [5]): for nonempty \(S\subseteq V\),

\[
c(S)=\prod_{i=1}^{d}\pi_i(S),
\]

where \(\pi_i(S)\) is the set of letters appearing in coordinate \(i\) of some member of \(S\). The strict unit-premise spectrum and exact direct-basis versus ordinary-basis separation are the results established here.

## Proof

**1. Rectangular hull.** Graph distance equals the number of unequal coordinates. Hence \(I(u,v)=\prod_i\{u_i,v_i\}\). Every nonempty Cartesian product of coordinate subsets is interval-convex. Conversely, let \(S\) be nonempty. Induct on its cardinality: the hull of the first \(t\) points is their coordinate rectangle, and adjoining a new point \(v\) makes every coordinatewise recombination of an old rectangle point and \(v\) available in \(I(w,v)\). Given any target whose coordinates occur among the \(t+1\) generators, choose \(w\) with each coordinate that does not use \(v_i\) equal to its target coordinate; recombination with \(v\) produces the target. Thus the rectangle equals the hull.

**2. Private-coordinate criterion.** Fix \(x\), and take \(B=\{y_1,\ldots,y_r\}\subseteq V\setminus\{x\}\). For each coordinate \(i\), define the set of matching rows \(M_i=\{a\in[r]: (y_a)_i=x_i\}\). Rectangular hull gives \(x\in c(B)\) iff every \(M_i\) is nonempty. Moreover \(B\) is minimal iff, for every row \(a\), there exists a coordinate \(i\) with \(M_i=\{a\}\): dropping row \(a\) must leave some coordinate with no match to \(x\). Such designated coordinates are pairwise distinct, so \(r\le d\). A singleton \(\{y\}\) cannot generate a different vertex, proving \(r\ge2\).

**3. Exact enumeration.** Label the \(r\) premise rows. A prescribed nonempty matching set \(M_i\subseteq[r]\) allows exactly \((q-1)^{r-|M_i|}\) choices for the \(r\) letters in coordinate \(i\), because matching rows must take \(x_i\) while other rows must avoid it. Summing over all nonempty matching sets gives \(q^r-(q-1)^r\) choices per coordinate. To require that each of the \(r\) singleton matching patterns occurs at least once, apply inclusion-exclusion: forbidding \(j\) named singleton patterns subtracts \(j(q-1)^{r-1}\) from that per-coordinate count. The count of ordered premise rows is therefore

\[
\sum_{j=0}^{r}(-1)^j\binom rj\bigl(q^r-(q-1)^r-j(q-1)^{r-1}\bigr)^d.
\]

The private-coordinate condition itself forces rows to be pairwise distinct: identical rows cannot each possess a singleton matching coordinate. It also forbids a row identical to \(x\) when \(r\ge2\): such a row matches every coordinate and prevents other rows having private coordinates. Thus these ordered objects are precisely permutations of genuine nontrivial stems, each unordered stem counted exactly \(r!\) times. Dividing gives the displayed formula. For \(r=d\), every coordinate must be singleton and every row must have exactly one private coordinate. After pairing rows with their private coordinates, all remaining \(d(d-1)\) letter positions admit \(q-1\) nonmatching values, giving \(b_{d,q,d}=(q-1)^{d(d-1)}\). For \(2\le r<d\), designate \(r\) private coordinates and choose, for each remaining coordinate, at least one matching row; such configurations exist, so every size occurs.

**4. Exact one-pass implication count.** Fix \(x\) and a stem \(B\) for \(x\). If a unit basis computes closure from the original input \(B\) in one pass, it must contain some rule \(A\to x\) with \(A\subseteq B\). Minimality of \(B\) forces \(A=B\). Conversely, every \(x\in c(S)\setminus S\) has a minimal stem \(B\subseteq S\), because \(S\) is finite. Therefore all nontrivial \(B\to x\), and no others, are required for the unique inclusion-minimal direct unit basis. Vertex transitivity makes the stem count independent of \(x\), giving \(\mathcal P_{d,q}\). This is the familiar general stem/prime-implicate characterization specialized and enumerated here, not a claim to originate that characterization.

**5. Quasipolynomial versus polynomial representation.** Put \(r=\lfloor d/2\rfloor\) and restrict to \(d\ge4\). For one fixed root, choose the first \(r\) coordinate columns as the prescribed singleton patterns \(\{1\},\ldots,\{r\}\), using a fixed nonmatching alphabet symbol. For each of the remaining \(d-r\) coordinate columns, use any nonempty matching subset of the rows and the same fixed alternative symbol. This constructs \((2^r-1)^{d-r}\) ordered valid stems, hence at least \((2^r-1)^{d-r}/r!\) unordered stems per root. Their logarithm is \(\Omega(d^2)\) because \(\log_2(2^r-1)\ge r-1\) and \(\log_2(r!)=O(d\log d)\). Conversely, there are at most \(q^d\sum_{r=2}^{d}\binom{q^d}{r}\le q^d d(q^d)^d\) nontrivial rooted rules, an \(\exp(O_q(d^2))\) bound. Therefore \(\mathcal P_{d,q}(1)=\exp(\Theta_q(d^2))\).

For comparison, introduce \(\{u,v\}\to w\) for every unordered vertex pair \(u\ne v\) and each \(w\in I(u,v)\setminus\{u,v\}\). Repeated forward chaining is exactly repeated interval closure, hence reaches \(c\) for all inputs. There are at most \(\binom{|V|}{2}(|V|-2)<|V|^3/2\) such unit implications, polynomial in \(|V|\). Since \(|V|=q^d\), the one-pass minimum is \(|V|^{\Theta_q(\log |V|)}\), superpolynomial in graph size.

## Verification

The accompanying standalone \`verify.py\` uses only the Python standard library. It independently counts stems from coordinate matching and deletion minimality for \((d,q)=(2,2),(3,2),(4,2),(2,3),(3,3),(2,4),(3,4)\), and checks the closed formula and extremal count at each admissible size. It also compares coordinate-product closure with repeated shortest-path interval closure on 984 selected subsets (all subsets in the smallest cases). A verification execution returned \`VERIFY_OK cases=7 independent_subset_hulls= 984 direct_stem_counts=PASS extremal_counts=PASS\`. These finite checks are corroboration only; the proof covers all stated integers.

For direct reproduction: \`python3 verify.py\`. No network, downloaded input, or external package is needed.

## Relationship to prior work

Wild's survey on pure Horn implications [1], especially Sections 3.3 and 3.4, establishes generally that minimal rooted stems encode prime unit implications and direct implicational systems. This general result is explicitly assumed; the present formula does not claim to invent canonical direct bases. Nourine and Vilmin [2], Sections 2 and 4, develop the Carathéodory-number/minimal-generator framework in connection with enumeration algorithms. Their treatment concerns general closure systems and does not state the above Hamming rooted-stem rank polynomial or the quantified direct/non-direct blowup. The geodesic convexity Carathéodory/exchange literature [3] supplies background on graph convexity; the accessible abstract discusses different graph families, and its full text was not obtained in this comparison. Klavžar [4] studies structural embeddings of Hamming graphs rather than enumeration of minimal rooted implications.

The basic box-hull property, general prime-implicate theorem, and standard inclusion-exclusion are established ingredients. There is also a **decisive classical overlap at alphabet size two**: the rank-by-rank counts \(b_{d,2,r}\) are exactly the established numbers of minimal set covers of a \(d\)-element set by \(r\) subsets, apart from the trivial one-subset cover. This is the Hearne–Wagner/Devitt–Jackson enumeration, displayed explicitly by Royle [6] and in MathWorld [7]. The binary table and its asymptotic magnitude are thus NOT asserted to be novel. The claim evaluated beyond that coverage is the **nonbinary weighted-stem all-rank formula and its explicit Horn representation-size separation**, under the geodesic graph interpretation. For nonbinary alphabets the matching pattern of a row subset carries \((q-1)\)-colored nonmatches, which are not represented by the unweighted binary-cover table. These are still elementary weighted-cover techniques, and the possibility that a prior general colored-cover or graph-convexity theorem already implies the full statement remains a genuine priority risk. Expert literature review is needed before a publication-priority assertion.

## Limitations

The result is for shortest-path (geodesic) convexity on equal-alphabet Cartesian powers of complete graphs. It is not about \(P_3\)-convexity, Hamming metric balls, arbitrary Cartesian factors, the size of minimum grouped direct bases, or minimum ordinary bases. The asymptotic statement holds for fixed \(q\) with \(d\to\infty\). An implicit equivalent formula under weighted irredundant coordinate covers cannot be categorically excluded by the available searches. The binary alphabet enumeration is classical [6, 7] and is not claimed as new. The proved separation applies to unit, simultaneous one-pass versus ordinary multi-pass implication systems, not to formula encoding cost or unrestricted algorithms.

## References

[1] M. Wild, *The joy of implications, aka pure Horn functions: mainly a survey*, arXiv:1411.6432 (first public 2014-11-24), Sections 3.3, 3.4. https://arxiv.org/abs/1411.6432

[2] L. Nourine and S. Vilmin, *Enumerating maximal consistent closed sets in closure systems*, arXiv:2102.04245v1 (first public 2021-02-05), Sections 2 and 4. https://arxiv.org/html/2102.04245v1

[3] B. S. Anand et al., *On the Carathéodory and exchange numbers of geodetic convexity in graphs*, *Theoretical Computer Science* 804 (2020), 46–57, DOI:10.1016/j.tcs.2019.10.041 (abstract-level comparison only).

[4] S. Klavžar, *Characterizing subgraphs of Hamming graphs*, *Journal of Graph Theory* 49 (2005), 302–312, DOI:10.1002/jgt.20084 (abstract-level comparison only).

[5] T. Jiang, I. M. Pelayo, and D. Pritikin, *Geodesic Convexity and Cartesian Products in Graphs*, 2004. Convex subsets of Cartesian products are products of convex subsets; full primary text not checked.

[6] G. F. Royle, *Counting Set Covers and Split Graphs*, Journal of Integer Sequences 3 (2000), Article 00.2.6. https://cs.uwaterloo.ca/journals/JIS/VOL3/ROYLE/royle.html

[7] E. W. Weisstein, *Minimal Cover*, MathWorld (classical minimal-cover rank table and formulas). https://mathworld.wolfram.com/MinimalCover.html
