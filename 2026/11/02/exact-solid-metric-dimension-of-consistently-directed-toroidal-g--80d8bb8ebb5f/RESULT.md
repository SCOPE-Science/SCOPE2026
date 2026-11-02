# Exact solid-metric dimension of consistently directed toroidal grids

## Finding

Let \(D_{m,n}=\overrightarrow{C}_m\square\overrightarrow{C}_n\) be the Cartesian product of consistently oriented directed cycles of lengths \(m\) and \(n\). For every pair of integers \(m,n\ge3\), its solid-metric dimension is

\[
\boxed{\beta_S(D_{m,n})=\max\{\max(m,n),\,2\min(m,n)\}.}
\]

Thus a directed toroidal grid needs exactly the larger of its longest circumference and twice its shortest circumference in order to distinguish every vertex from every nonempty vertex subset by distances *from* the chosen landmarks. This is an exact all-parameter formula, not an asymptotic bound. The proof gives explicit optimum landmark sets. In contrast to source-containing orientations treated previously, these directed tori have no forced vertices.

## Assumptions and scope

Write \(\mathbb Z_k\) for residues modulo \(k\). The vertices of \(D_{m,n}\) are \((i,j)\in\mathbb Z_m\times\mathbb Z_n\), with directed arcs \((i,j)\to(i+1,j)\) and \((i,j)\to(i,j+1)\). Both factors have at least three vertices, so they are consistently oriented simple cycles. Distances are directed shortest-path distances:

\[
 d((a,b),(i,j))=((i-a)\bmod m)+((j-b)\bmod n).
\]

For a nonempty vertex set \(X\), define \(d(s,X)=\min_{x\in X}d(s,x)\). A vertex set \(S\) is *solid-resolving* if, whenever \(u\) is a vertex and \(X\) is nonempty with \(X\ne\{u\}\), there is an \(s\in S\) such that \(d(s,u)\ne d(s,X)\). Its minimum cardinality is \(\beta_S\). The equivalent ordered-pair test is: for every two *distinct ordered* vertices \(u,v\), some \(s\in S\) satisfies \(d(s,u)<d(s,v)\). Indeed, a strict inequality against an element of \(X\setminus\{u\}\) distinguishes \(u\) from \(X\); if the ordered-pair test fails for \(u,v\), the set \(\{u,v\}\) cannot be distinguished from \(v\).

By symmetry between coordinates, the proof may assume \(3\le m\le n\).

## Proof

**1. Lower bound from two families of ordered pairs.** Fix \(S\) satisfying the ordered-pair test. For each \(j\in\mathbb Z_n\), compare \(p=(i,j)\) to \(q=(i,j-1)\). The strict inequality \(d(s,p)<d(s,q)\) holds precisely when the second coordinate of \(s\) is \(j\). Thus every one of the \(n\) second-coordinate rows contains an element of \(S\), giving \(|S|\ge n\).

For the other bound, fix any \(a\in\mathbb Z_m\) and \(j\in\mathbb Z_n\), and put \(p=(a-1,j)\), \(q=(a,j-1)\). If \(s=(x,y)\), direct substitution in the distance formula gives the following four values of \(d(s,q)-d(s,p)\):

| Landmark position | Difference |
| --- | ---: |
| \(x\ne a,\ y\ne j\) | \(0\) |
| \(x=a,\ y\ne j\) | \(-m\) |
| \(x\ne a,\ y=j\) | \(n\) |
| \(x=a,\ y=j\) | \(n-m\) |

Since \(n\ge m\), the strict inequality \(d(s,q)<d(s,p)\) is possible **only** when \(x=a\) and \(y\ne j\). The ordered-pair requirement must hold for every \(j\). Hence the column of first coordinate \(a\) must contain at least two landmarks with distinct second coordinates: one alone at \(y=j\) would not work for that \(j\). Every one of the \(m\) first-coordinate columns requires two landmarks. Therefore

\[
 |S|\ge\max\{n,2m\}.
\]

**2. A sufficient interval-expansion condition.** Call a set \(S\subseteq\mathbb Z_m\times\mathbb Z_n\) *expanding* when (i) every second-coordinate row contains a landmark, (ii) every first-coordinate column contains a landmark, and (iii) for every nonempty proper cyclic interval \(I\subsetneq\mathbb Z_m\) of \(k\) consecutive columns, the landmarks with first coordinate in \(I\) occupy at least \(k+1\) distinct second-coordinate rows.

We claim every expanding \(S\) is solid-resolving. Consider distinct \(u=(i,j)\) and \(v=(i+\Delta,j+\delta)\), where \(0\le\Delta<m\) and \(0\le\delta<n\). For any \(s=(a,b)\) write \(X=(i-a)\bmod m\), \(Y=(j-b)\bmod n\). Then

\[
 d(s,v)-d(s,u)=\Delta+\delta-m\,\mathbf1_{X+\Delta\ge m}-n\,\mathbf1_{Y+\delta\ge n}.
\]

If \(\Delta=0\), choose a landmark in row \(b=j\); the difference is \(\delta>0\). If \(\delta=0\), choose a landmark in column \(a=i\); the difference is \(\Delta>0\). Suppose both are positive. If \(\Delta+\delta>m\), a landmark in row \(b=j\) works, because its second-coordinate indicator vanishes and the first-coordinate indicator costs at most \(m\).

Finally suppose \(\Delta+\delta\le m\). Let \(k=m-\Delta\), so \(1\le\delta\le k<m\). The first-coordinate columns with \(X+\Delta<m\) form a cyclic interval of exactly \(k\) columns. By (iii), landmarks in these columns occupy at least \(k+1\) rows. Only \(\delta\le k\) row residues have \(Y+\delta\ge n\). Hence one landmark has *neither* indicator present, giving positive difference \(\Delta+\delta\). All ordered pairs are resolved.

**3. Optimal expanding constructions.** When \(n\ge2m\), take

\[
 S=\{(j\bmod m,j):0\le j<n\}.
\]

It has \(n\) distinct landmarks and meets every row. Every cyclic interval of \(k\) columns contains the \(2k\) landmarks at second coordinates \(i\) and \(i+m\) for the included residues \(0\le i<m\); these rows are distinct. Thus (iii) holds, and (ii) is immediate.

When \(m\le n<2m\), put \(t=n-m\) and take

\[
\begin{aligned}
S={}&\{(i,i):0\le i<m\}\\
 &\cup\{(i,i+m):0\le i<t\}\\
 &\cup\{(i,(i+1)\bmod m):t\le i<m\}.
\end{aligned}
\]

These \(2m\) landmarks are distinct. All \(n\) rows appear: the diagonal part covers \(0,\ldots,m-1\), while the middle part covers \(m,\ldots,n-1\). Every column has two landmarks. To see interval expansion, let \(I\) be a nonempty proper cyclic interval of \(k\) columns. The diagonal landmarks provide \(k\) distinct rows indexed by \(I\). If \(I\) contains an index \(i<t\), the landmark \((i,i+m)\) contributes a new row outside \(0,\ldots,m-1\). Otherwise, if \(t>0\), \(I\) is an ordinary interval within \(\{t,\ldots,m-1\}\), whose last index has successor outside \(I\); its third-family landmark contributes that successor row. If \(t=0\), any proper nonempty cyclic interval has an index whose cyclic successor is outside \(I\), and again the third family supplies a new row. Hence condition (iii) holds in all cases.

The sufficient condition proves that both sets are solid-resolving. Their cardinalities are exactly \(\max\{n,2m\}\), matching the lower bound. Swapping the two coordinates proves the stated symmetric formula for arbitrary \(m,n\ge3\).

**4. No forced landmarks.** Each \(D_{m,n}\) is vertex-transitive by translation. Its optimum cardinality is strictly smaller than \(mn\). Translating one optimum set therefore gives an optimum set excluding any prescribed vertex, so no vertex belongs to every solid-resolving set.

## Verification

The included `verify.py` constructs the two families of optimal sets and checks the **original** ordered-pair distance inequalities directly for 83 parameter pairs with \(3\le m\le9\). It also independently checks the cyclic-interval expansion condition and exact set sizes. Running `python verify.py` prints `VERIFY_OK` after all tests.

The optional `verify_milp.py` uses a separate integer programming formulation: one binary variable per candidate landmark and one covering constraint per distinct ordered vertex pair. With NumPy and SciPy installed, `python verify_milp.py` verifies exact minimum sizes for ten small parameter pairs, ending in `MILP_VERIFY_OK 10`. Neither finite experiment replaces the all-parameter proof above.

## Relationship to prior work

Hakanen and Pavan introduced solid-resolving sets for digraphs and established the ordered-pair characterization. Their publicly available IWOCA 2026 proceedings chapter first appeared online on 2026-06-07. The expanded arXiv treatment (posted 2026-10-26) develops Cartesian-product results for certain oriented paths and cycles. Its Theorem 6.4 requires every cycle factor to have two sources; Remark 6.5 explicitly discusses why directed cycles with no sources lie outside that forced-vertex framework. The present theorem treats exactly the canonical two-factor **source-free** family, with an unrelated interval-expansion construction. No result about products of source-containing orientations is claimed as new.

Mengesha and Vetrík (2019) study ordinary metric resolving sets for directed Cayley graphs on products of cyclic groups; their definition distinguishes ordinary pairs by unequal distances to landmarks, which does not impose the two ordered strict inequalities needed for solid resolution. Rodríguez-Velázquez, Yero, Kuziak, and Oellermann (2013/2014) study *strong* metric dimension on undirected Cartesian products, based on shortest-path containment, a different condition. Neither of these results gives the formula above.

## Limitations

The formula is proved only for the Cartesian product of **two consistently directed simple cycles**, each of length at least three. It does not classify arbitrary orientations or bidirected cycle factors, products of three or more directed cycles, or all optimal landmark sets. The explicit optimal constructions are not asserted to be the only ones. Priority beyond the specific inspected primary sources remains subject to further literature assessment; absence from searchable records is not a proof of global novelty.

## References

1. A. Hakanen and P. D. Pavan, *Solid-Resolving Sets on Directed Graphs*, Combinatorial Algorithms (IWOCA 2026), LNCS 16587, pp. 327–340, DOI:10.1007/978-3-032-27732-9_23 (first online 2026-06-07); expanded manuscript, arXiv:2610.35041v1 (2026-10-26), especially Definition 1.1, Theorem 2.1, Section 6, Theorem 6.4, and Remark 6.5.
2. D. A. Mengesha and T. Vetrík, *Resolving sets of directed Cayley graphs for the direct product of cyclic groups*, Czechoslovak Mathematical Journal 69 (2019), pp. 621–636, DOI:10.21136/CMJ.2019.0127-17.
3. J. A. Rodríguez-Velázquez, I. G. Yero, D. Kuziak, and O. R. Oellermann, *On the strong metric dimension of Cartesian and direct products of graphs*, Discrete Mathematics 335 (2014), pp. 8–19, arXiv:1307.4722, DOI:10.1016/j.disc.2014.06.023.
