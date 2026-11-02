# Logarithmic online shattering of minimum dominating sets on connected cycles

## Finding
Let \(k\ge1\), \(n=3k+2\), and let \(\mathcal G_n\) be the Boolean vertex-membership concept class of every **minimum-cardinality dominating set** of the simple cycle \(C_n\). Then
\[
|\mathcal G_n|=n,\qquad \operatorname{VCdim}(\mathcal G_n)=2,
\]
and its Littlestone dimension obeys the two-sided bounds
\[
\max\{3,\lfloor\log_2(k+1)\rfloor\}
\le \operatorname{Ldim}(\mathcal G_n)\le\lfloor\log_2(3k+2)\rfloor
\quad(k\ge3).
\]
For \(k=1,2\) the Littlestone dimension is exactly \(2\); for \(k=3\) it is exactly \(3\). Consequently, the first strict static/adaptive gap in this residue class occurs at \(C_{11}\); all \(k\ge3\) have a strict gap, and
\[
\operatorname{Ldim}(\mathcal G_{3k+2})=\log_2(3k+2)+O(1)
\]
with a uniformly bounded additive error. In particular, the difference \(\operatorname{Ldim}-\operatorname{VCdim}\) is unbounded along **connected, vertex-transitive, 2-regular** graphs.

## Assumptions and scope
The vertex set of \(C_n\) is \(\mathbb Z/n\mathbb Z\), and a dominating set meets the closed neighborhood of every vertex. A \(\gamma\)-set means a dominating set of minimum possible cardinality, not an arbitrary inclusion-minimal dominating set. Each hypothesis is the indicator function of a \(\gamma\)-set; a query at vertex \(v\) reveals the indicator there. VC dimension uses simultaneous shattering of fixed query sets. Littlestone dimension uses complete binary mistake trees with potentially adaptive queries and distinct witnessing hypotheses along every leaf.

For \(k\ge1\), define
\[
P_k=\{0\}\cup\{3a-1:1\le a\le k\}\subset\mathbb Z/(3k+2)\mathbb Z,
\qquad D_t=t+P_k \quad(0\le t<n).
\]

## Proof
**1. Classification of hypotheses.** Every vertex of \(C_n\) dominates at most three vertices, hence every dominating set has at least \(\lceil n/3\rceil=k+1\) vertices. \(P_k\) has \(k+1\) vertices and cyclic successive spacings \(2,3,\ldots,3\), so it dominates. Thus the domination number equals \(k+1\). For any minimum dominating set, list its selected vertices in cyclic order. Each clockwise spacing is at most three (otherwise the middle of an uncovered run is undominated). There are \(k+1\) spacings summing to \(n=3(k+1)-1\). All spacings must therefore be three except exactly one of size two. Its position uniquely specifies the set as one \(D_t\). Distinct \(t\) yield different sets, so there are exactly \(n\) hypotheses.

**2. The exact VC bound.** The pair \(\{0,2\}\) is shattered: precisely one \(D_t\) includes both (its unique two-spacing starts at zero). Each vertex belongs to \(k+1\) translated sets, so the number of hypotheses realizing the four possible patterns on \(\{0,2\}\) is \(1,k,k,k+1\), respectively; all are positive.

Suppose a triple \(\{x,y,z\}\) were shattered. It must occur simultaneously in some \(D\). Arrange the three points clockwise. The three arcs between them comprise spacings from \(D\); exactly one of these arcs contains the unique two-spacing. Label that arc \(x\to y\); the other two arcs, from \(y\) through \(z\) to \(x\), consist only of three-spacings. Hence the clockwise length from \(x\) to \(y\) is congruent to two modulo three, and the length from \(y\) to \(z\) is divisible by three. For any other minimum dominating set \(D'\) containing both \(x\) and \(y\), its unique two-spacing must also lie on the clockwise arc \(x\to y\): without that two-spacing, the arc length would be divisible by three. Thus on the complementary arc \(y\to x\), all successive members of \(D'\) are exactly three apart. Since \(z\) is reached from \(y\) by a multiple of three inside this arc, \(z\in D'\). The trace containing \(x,y\) but not \(z\) is therefore impossible, contradicting shattering. No triple is shattered; VC dimension is exactly two.

**3. A uniform depth-three adaptive witness.** For all \(k\ge3\), use this depth-three query tree. Query vertex \(0\) at the root. If the answer is zero, query vertex \(1\); its zero child queries \(4\), and its one child queries \(3\). If the answer at the root is one, query vertex \(5\); its zero child queries \(8\), and its one child queries \(2\). The eight root-to-leaf answer words \(000,001,010,011,100,101,110,111\) are witnessed by the respective shifts
\[
5,\ 2,\ 4,\ 1,\ 9,\ 6,\ 3,\ 0.
\]
These checks are uniform in \(k\ge3\): for query positions \(q\in\{0,1,2,3,4,5,8\}\) and shifts \(t\in\{0,1,2,3,4,5,6,9\}\), membership \(q\in D_t\) is precisely \((q-t\bmod n)\in P_k\). For nonnegative differences among these queries and shifts (all at most eight), only zero and the positive numbers two, five, and eight are eligible; for negative differences \(-r\) with \(1\le r\le9\), the residue \(n-r\) belongs to \(P_k\) exactly when \(r\) is a positive multiple of three. The condition remains valid at \(k=3\), including the boundary \(r=9\). The listed witnesses have the prescribed answers, yielding Littlestone dimension at least three.

**4. A logarithmically deep threshold subclass.** Restrict to the \(k+1\) hypotheses \(D_{3j}\), \(0\le j\le k\). For \(0\le b<k\), use query \(q_b=3b+2\). Direct reduction modulo \(n\) gives
\[
\mathbf1[q_b\in D_{3j}]=\mathbf1[j\le b].
\]
Indeed, when \(j\le b\), the difference is \(3(b-j)+2\in P_k\); when \(j>b\), its representative modulo \(n\) is congruent to one modulo three, hence does not belong to \(P_k\). The restricted class is therefore the ordered-threshold concept class on \(k+1\) distinct positions. Repeated balanced prefix/suffix queries shatter a complete tree of depth \(\lfloor\log_2(k+1)\rfloor\). Hence the same lower bound holds in \(\mathcal G_n\).

**5. Sharp small boundary and growth.** Every shattered mistake tree of depth \(d\) needs at least \(2^d\) distinct hypotheses. Because \(|\mathcal G_n|=n\), the Littlestone dimension is at most \(\lfloor\log_2 n\rfloor\). At \(k=1\), this bound and VC dimension two give Littlestone dimension two. At \(k=2\), each vertex query has only \(k+1=3\) positive hypotheses. A depth-three shattered tree would require its root-positive branch to have at least four hypotheses, so no such tree exists; the dimension is two. At \(k=3\), the fixed depth-three tree meets the upper bound \(\lfloor\log_2(11)\rfloor=3\). For larger \(k\), the fixed tree still gives a strict gap, while the threshold subclass and the cardinality bound differ by at most a constant independent of \(k\), proving logarithmic growth and the unbounded difference.

## Verification
`verify_cycle_gamma.py` independently enumerates all minimum dominating sets by direct domination tests at \(n=5,8,11,14,17,20\), checks the explicit translation formula, tests every three-query support through \(n=77\), verifies the ordered-threshold traces, and recomputes exact Littlestone ranks for the first six parameters by a complete version-space recurrence. The explicit depth-three witness is also checked for all \(3\le k\le25\). `C11_TREE.json` records its full finite binary tree. All programs require Python 3 standard library only and run as `python verify_cycle_gamma.py` from the package directory. These computations are corroboration; the infinite bounds rely on the proof above.

## Relationship to prior work
Hernández-Gómez, Reyna-Hernández, Romero-Valencia, and Rosario Cayetano (2020) classified minimum dominating sets of paths and cycles and their automorphism orbits. In particular their cycle Lemma 5 and Theorem 2 give the cyclic family when the order is one below a multiple of three, but do not analyze VC shattering, Littlestone shattering, online mistake trees, or the logarithmic separation. Malliaris and Moran (2021) provide the general theory and motivation connecting Littlestone dimension to online learning and model-theoretic stability, not a dimension calculation for these domination concepts. The comparison is between mathematical statements: a classification of hypothesis sets supplies the input but does not by itself establish this adaptive/static separation. Earlier findings for **inclusion-minimal** dominating sets of cycles concern a different, larger concept class and do not imply exact dimensions for its minimum-cardinality subfamily.

## Limitations
No exact formula is asserted for Littlestone dimension at every \(k\ge4\); only explicit lower and upper bounds and the proved asymptotic order are given. No claim covers all cycle orders or the family of arbitrary inclusion-minimal dominating sets. The novelty assessment is based on accessible primary and database checks rather than a proof of global historical priority. Independent validation has not been performed.

## References
1. J. C. Hernández-Gómez, G. Reyna-Hernández, J. Romero-Valencia, and O. Rosario Cayetano, *Transitivity on Minimum Dominating Sets of Paths and Cycles*, Symmetry 12 (2020), 2053. DOI: 10.3390/sym12122053. First public version verified 2020-12-11.
2. M. Malliaris and S. Moran, *Agnostic Online Learning and Excellent Sets*, arXiv:2108.05569 (first public 2021-08-12).
