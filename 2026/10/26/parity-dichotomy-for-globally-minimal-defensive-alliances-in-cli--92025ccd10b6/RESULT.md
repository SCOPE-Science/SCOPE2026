# Parity dichotomy for globally minimal defensive alliances in clique bouquets

## Finding

Let \(t\ge 2\) and let \(r_1,\ldots,r_t\ge2\) be integers. The **clique bouquet**
\[
B(r_1,\ldots,r_t)=K_1\vee\bigl(K_{r_1}\sqcup\cdots\sqcup K_{r_t}\bigr)
\]
has one central vertex \(c\), joined to all vertices of pairwise disjoint peripheral cliques \(B_i\) of orders \(r_i\). A **defensive alliance** is a nonempty set \(S\subseteq V(B)\) such that \(|N[v]\cap S|\ge |N(v)\setminus S|\) for every \(v\in S\). It is **globally minimal** when it has no nonempty proper subset that is itself a defensive alliance. This is stronger than single-deletion (local) minimality.

Put \(a_i=\lfloor r_i/2\rfloor\), \(T=\sum_{i=1}^t a_i\), and \(o=|\{i:r_i\text{ is odd}\}|\). The complete collection of globally minimal defensive alliances consists of exactly the following two disjoint types:

1. **Peripheral type:** for any \(i\), choose exactly \(a_i+1\) vertices from \(B_i\), and no other vertices.
2. **Central type:** choose \(c\) together with exactly \(a_i\) vertices from **each** \(B_i\). This type exists if and only if \(o\le1\).

Consequently the polynomial whose coefficient of \(z^s\) counts globally minimal defensive alliances of cardinality \(s\) is
\[
\boxed{\mathcal A_B(z)=\sum_{i=1}^t\binom{r_i}{a_i+1}z^{a_i+1}
+\mathbf1_{\{o\le1\}}\left(\prod_{i=1}^t\binom{r_i}{a_i}\right)z^{T+1}.}
\]
Terms with the same exponent are added. Thus the smallest cardinality is \(1+\min_i a_i\). The largest is \(T+1\) when \(o\le1\), and \(1+\max_i a_i\) when \(o\ge2\). For all-even uniform blade sizes \(r_i=2h\), with \(h\ge1\), the difference between the largest and smallest globally minimal alliance sizes is \((t-1)h\), unbounded as either parameter grows.

## Assumptions and scope

Graphs are finite, simple, and undirected. Throughout, \(t\ge2\) and \(r_i\ge2\); no assertion is made for pendant singletons or arbitrary block graphs. Global minimality refers to every nonempty proper subset, not only removal of one vertex. There is no requirement that the alliance dominate the whole graph. The definition \(|N[v]\cap S|\ge|N(v)\setminus S|\) is equivalent to \(\deg_S(v)+1\ge\deg_{V\setminus S}(v)\).

## Proof

Write \(z_0=\mathbf1_{\{c\in S\}}\) and \(k_i=|S\cap B_i|\). For every selected peripheral vertex \(v\in B_i\), the degree in \(B\) is \(r_i\), and its number of selected neighbors is \(k_i-1+z_0\). Its defensive inequality is therefore
\[
2(k_i-1+z_0)+1\ge r_i.
\]
When \(z_0=0\), this is \(k_i\ge a_i+1\) for every occupied blade. When \(z_0=1\), it is \(k_i\ge a_i\) for every occupied blade. The equivalences hold for both parities of \(r_i\).

**No center.** If \(c\notin S\), any occupied blade containing at least \(a_i+1\) selected vertices itself contains a defensive alliance comprising exactly \(a_i+1\) of those vertices. Thus a globally minimal set can occupy only one blade, with exactly \(a_i+1\) chosen vertices. Conversely each such subset is defensive, and no nonempty proper subset can meet the threshold of its blade. This proves the first type.

**Center included.** Let \(c\in S\), put \(K=\sum_i k_i\), and write \(R=\sum_i r_i\). The central vertex has degree \(R\), and its defensive inequality reads \(2K+1\ge R\), or \(K\ge\lfloor R/2\rfloor\). Since \(R=2T+o\), this becomes
\[
K\ge T+\lfloor o/2\rfloor.
\]
If any occupied blade has \(k_i\ge a_i+1\), then \(S\) strictly contains a peripheral-type defensive alliance (strictly, because \(c\in S\)) and cannot be globally minimal. Therefore global minimality forces \(k_i\in\{0,a_i\}\) for every blade: a positive count must be at least \(a_i\) by the peripheral inequality, and cannot exceed \(a_i\). In particular \(K\le T\), so the central inequality can hold only when \(\lfloor o/2\rfloor=0\), equivalently \(o\le1\). In that case \(K\ge T\) forces \(K=T\) and, since each \(a_i\ge1\), every blade has exactly \(k_i=a_i\).

Conversely suppose \(o\le1\) and take \(c\) and exactly \(a_i\) vertices from every blade. The peripheral inequalities hold, while \(K=T=\lfloor R/2\rfloor\) proves the central inequality. If a proper nonempty subset omits \(c\), it uses at most \(a_i\) vertices from each blade and thus cannot be defensive. If it retains \(c\), it contains at most \(T-1\) peripheral vertices and violates the central inequality. Hence this set is globally minimal, proving the second type.

The two types are disjoint because only the second contains \(c\). Choosing vertices within each blade yields \(\binom{r_i}{a_i+1}\) peripheral sets and, when permitted, \(\prod_i\binom{r_i}{a_i}\) central sets. Their cardinalities give the stated polynomial, and its extreme exponents give the smallest and largest sizes. For the all-even uniform case, \(T=th\) and the extreme exponents are \(h+1\) and \(th+1\), proving the gap formula. \(\square\)

## Verification

The accompanying `verify.py` builds the graphs directly from their clique adjacencies, checks \(2\deg_S(v)+1\ge\deg(v)\) on candidate vertex subsets, constructs the actual globally minimal sets by removing supersets of already found defensive alliances, and compares the resulting set families and exact cardinality coefficients with the theorem. Running `python3 verify.py` completes exhaustive checks for 21 parameter tuples, comprising 18,891 nonempty candidate vertex subsets; the stored `verification_output.txt` records the checks. The finite experiment is independent of the analytic proof and does not establish its infinitely quantified statement by itself.

For example, \(B(2,4,4)\) has exactly \(81\) globally minimal defensive alliances, with polynomial \(z^2+8z^3+72z^6\). A bouquet with two or more odd-size blades has no central-type globally minimal defensive alliance.

## Relationship to prior work

Feng, Fernau, and Mann study enumeration and counting of locally and globally minimal defensive alliances in general graphs and several special graph classes; they state the distinction between global and local minimality and present algorithms and tree results. Their results motivate a closed classification for clique bouquets but do not state the above parity dichotomy or coefficient formula. Bazgan, Fernau, and Tuza study the upper defensive alliance problem and testing global minimality, rather than the present familywise polynomial. Ibrahim's defensive-alliance-polynomial treatment includes friendship graphs as a graph-recognition example, not the globally minimal alliance distribution. Gaikwad and Maity establish parameterized complexity results for global minimality, not this structural classification. A later treatment of **total** defensive alliances in graph joins concerns a different requirement and does not provide the globally minimal enumeration here.

The friendship graph is the uniform special case \(r_i=2\); the new theorem also handles all heterogeneous clique bouquets. These comparisons do not establish absolute bibliographic uniqueness: unindexed equivalent treatments remain possible.

## Limitations

The result is restricted to ordinary (not necessarily total, global-dominating, offensive, or strong) defensive alliances, and to the one-apex clique-bouquet family with each \(r_i\ge2\). It is a mathematical classification, not an algorithmic complexity result for general graphs. Computational enumeration is finite corroboration only. No independent mathematical validation is asserted.

## References

1. Z. Feng, H. Fernau, K. Mann, *Enumerating Defensive Alliances*, arXiv:2312.11963 (first public preprint 2023-12-19), https://arxiv.org/abs/2312.11963.
2. C. Bazgan, H. Fernau, Z. Tuza, *Aspects of upper defensive alliances*, Discrete Applied Mathematics **266** (2019), 111–120; author-hosted full text https://www.lamsade.dauphine.fr/~bazgan/Papers/DAM19a.pdf.
3. H. Ibrahim, *Defensive alliance polynomial*, JCMCC **115** (2020), 69–94, https://combinatorialpress.com/article/jcmcc/Volume%20115/Defensive%20alliance%20polynomial.pdf.
4. A. Gaikwad, S. Maity, *Globally Minimal Defensive Alliances: A Parameterized Perspective*, arXiv:2202.02010, https://arxiv.org/abs/2202.02010.
5. R. S. Oñate and I. S. Cabahug Jr., *Total Defensive Alliances in Graphs* (2026), https://www.researchgate.net/publication/405151411_TOTAL_DEFENSIVE_ALLIANCES_IN_GRAPHS.
