# Arithmetic walks and cubic-time vertex counting for bounded-Lipschitz path balls

## Finding
For every integer \(n\ge2\), set \(S_n=\{0,1,\ldots,n-1\}\) with distance \(d(i,j)=|i-j|\). The real Banach space of functions on this path carries the bounded-Lipschitz norm
\[
N(f)=\max_{0\le i<n}|f_i|+\max_{0\le i<n-1}|f_{i+1}-f_i|.
\]
Every extreme point of its unit ball is either the constant vector \(\mathbf1\) or \(-\mathbf1\), or has the **unique** form
\[
f_i=\frac{2h_i-d}{d+2}\quad(0\le i<n),\qquad 1\le d\le n-1,
\]
where \(h_0,\ldots,h_{n-1}\) is an integer walk with \(0\le h_i\le d\) and each consecutive step in \(\{-1,0,1\}\). Partition its indices into maximal *nonzero-step runs*: a boundary between runs occurs exactly where \(h_{i+1}=h_i\). The walk qualifies precisely when **every run hits at least one of the levels \(0,d\)** and **some run hits both**. No vector is counted twice.

Writing \(W_{n,d}\) for the number of qualifying height walks at level span \(d\), the number of unit-ball vertices is exactly
\[
V_n=2+\sum_{d=1}^{n-1}W_{n,d}.
\]
A transfer dynamic program evaluates this sum using \(O(n^3)\) integer additions and \(O(n)\) simultaneously stored integer cells when the \(d\) layers are processed sequentially. All coordinates of all vertices are rational with denominator at most \(n+1\) (before fraction reduction). The first counts for \(n=2,\ldots,11\) are
\[
4,10,26,64,162,404,998,2454,6014,14632.
\]

## Assumptions and scope
Everything is **real** and finite-dimensional; distances between adjacent path points are exactly \(1\). The maximum adjacent difference equals the Lipschitz constant for this path metric, including all nonadjacent pairs by telescoping. A *run* may consist of one index, in which case it qualifies only if that height is a boundary level. The theorem counts distinct extreme functions, not facets or vertices of a Lipschitz-free unit ball; the Fortet–Mourier max norm is a different norm. Integer-operation complexity is stated for additions, not unit-cost arithmetic on arbitrarily long integers. If \(n=1\), the unit ball is an interval with two vertices and is outside the stated range.

## Proof
**1. Tight equalities characterize extremality.** Let \(f\) be a nonconstant boundary point and put \(a=\max_i|f_i|>0\), \(b=\max_i|f_{i+1}-f_i|>0\), so \(a+b=1\). Mark every index where \(|f_i|=a\), with its sign. Draw an edge \(i\sim i+1\) if \(|f_{i+1}-f_i|=b\). Its connected components are consecutive tight-edge runs.

If a component contains no marked index, translating all its coordinates by a sufficiently small \(\pm\varepsilon\) leaves every marked supremum constraint and every tight difference unchanged, while the remaining inequalities have positive slack. Thus \(f\) is a midpoint of two distinct unit-ball points and is not extreme.

Suppose every component is marked, but none contains marks of both signs. For each component choose its common mark sign \(\sigma\). Every coordinate in the component can be written as \(\sigma a+c_i b\) with integer \(c_i\) obtained by summing oriented tight-edge differences. If several marks appear in that component, all have value \(\sigma a\), so their corresponding \(c_i\) are zero. Replace \(a\) by \(a\pm\varepsilon\), \(b\) by \(b\mp\varepsilon\) simultaneously in every component. The resulting two distinct functions have supremum bounds \(a\pm\varepsilon\) and consecutive-difference bounds \(b\mp\varepsilon\) for all sufficiently small positive \(\varepsilon\), because all inequalities not forced by the tight constraints are strict. Their bounded-Lipschitz norms are at most \(1\) and their midpoint is \(f\). Hence \(f\) is not extreme.

Conversely suppose every tight-edge component has a mark and at least one has both signs. Write \(f=(g+h)/2\) with \(N(g),N(h)\le1\). Convexity of the two separate seminorms, together with \(a+b=1\), forces equality in both convexity inequalities. Each original marked coordinate and each original tight edge consequently enforces the same signed saturation on \(g\) and \(h\). Within the mixed-sign component, following the tight path from a negative mark to a positive mark gives
\[
2a=kb
\]
for some integer \(k\ge1\). The same signed equalities give \(2a_g=kb_g\) and \(2a_h=kb_h\), while \(a_g+b_g=a_h+b_h=1\). Hence \(a_g=a_h=a\) and \(b_g=b_h=b\). Since each tight component contains a marked coordinate, its entire function is then fixed by the saturated signed edge differences. Thus \(g=h=f\); this proves extremality.

**2. Integer-grid rigidity.** In an extreme nonconstant \(f\), the mixed component yields \(2a=db\), for some integer \(1\le d\le n-1\), because the path connecting opposite marks has at least \(d\) tight edges. Solving this with \(a+b=1\) gives
\[
a=\frac d{d+2},\qquad b=\frac2{d+2}.
\]
Every tight component contains at least one signed mark \(\pm a\). Along that component, every coordinate differs from its mark by an integer multiple of \(b\). Since \(2a=db\) is integral in units of \(b\), **all** coordinates lie on the common lattice \(-a+b\mathbb Z\). On an untight adjacent pair the coordinate difference is therefore an integer multiple of \(b\) with absolute value strictly below \(b\), so it must be zero. Thus \(f_i=(2h_i-d)/(d+2)\) with integer \(0\le h_i\le d\) and increments \(0,\pm1\). The tight components are precisely the maximal nonzero-step runs; signed marks are precisely height levels \(0,d\). Step 1 gives exactly the two run conditions.

Conversely, the two run conditions for such a walk ensure \(\max|f_i|=a\), \(\max|f_{i+1}-f_i|=b\), and its tight components satisfy both conditions of Step 1; hence it is a vertex. Because \(d=2\max|f|/\max|f_{i+1}-f_i|\), different \(d\)'s cannot yield the same vector. The two constants \(\pm\mathbf1\) are extreme: an average of unit-ball vectors attaining coordinate value \(\pm1\) at all entries forces each average component to equal that constant. There are no other constant boundary points.

**3. Exact finite-state counting.** For fixed \(n,d\), let \(D_r(j,m,t)\) be the number of partial height walks of length \(r\) ending at height \(j\), with a two-bit mask \(m\in\{0,1,2,3\}\) tracking whether the **current** run has seen the bottom or top level, and Boolean \(t\in\{0,1\}\) tracking whether a completed or current run has touched *both*. Set \(\beta(j)=1\) for \(j=0\), \(2\) for \(j=d\), and \(0\) otherwise. Initialize \(D_1(j,\beta(j),0)=1\) for all \(0\le j\le d\). Transitions append:

* A step to \(j'=j\pm1\) in range, updating \(m'=m\mathbin{\mathrm{OR}}\beta(j')\), \(t'=t\mathbin{\mathrm{OR}}(m'=3)\).
* A flat step \(j'=j\) is allowed **only if** \(m\ne0\), meaning that the run being closed already touched a boundary. Set \(m'=\beta(j)\), \(t'=t\mathbin{\mathrm{OR}}(m=3)\).

Add the predecessor counts into the successor states. Finally sum \(D_n(j,m,t)\) over all \(j\), all \(m\ne0\), with \(t=1\) or \(m=3\); this is exactly \(W_{n,d}\). For each \(d\), the recurrence uses a constant number of operations on at most \(8(d+1)\) states over \(n-1\) transitions, thus \(O(nd)\) additions and \(O(d)\) storage. Summing \(d=1,\ldots,n-1\) gives \(O(n^3)\) additions and \(O(n)\) reusable storage. Each count has at most \(O(n+\log n)\) bits because the total enumerated walks are bounded above by \(n^2 3^{n-1}\). This proves the counting result.

## Verification
The standalone `verify_path.py` computes the recurrence with arbitrary-precision integers. For every \(2\le n\le9\) and \(1\le d<n\), it independently enumerates all three-choice step words and starting heights and tests the run condition directly: **36 exact layer comparisons** succeeded. The script separately constructs the original inequality representation with auxiliary supremum and Lipschitz bounds, obtains its vertices by a numerical half-space intersection, projects onto the function coordinates, and compares vertex counts for \(2\le n\le6\): **five independent numerical polytope comparisons** succeeded. The numerical checks are corroboration, not the proof. The code records \(V_2,\ldots,V_{20}\), and its recurrence is proved for every integer \(n\ge2\).

Reproduce with `python verify_path.py` from a Python environment; NumPy and SciPy are used for optional numerical cross-checks. The exact recurrence and exact brute-force tests use only the standard library.

## Relationship to prior work
Hille and Theewis (2023, Sections 1 and 6, arXiv:2305.08500v1) study the same additive bounded-Lipschitz norm, obtain norming families of extreme functions, and exhibit finite-space limitations of extension-based and local necessary conditions; they do **not** state the integer-walk parametrization, the all-\(n\) counts or the cubic-time count recurrence. Hille and Theewis (2022, Section 6, arXiv:2206.12234) give a general finite half-space/linear-programming description of dual Dudley norms rather than this explicit vertex census. A broader finite-metric tight-edge component criterion already determines extremality qualitatively. The contribution here is the path-specific integral rigidity, bounded grid denominator, complete canonical walk language and polynomial-time **exact vertex census**, which do not follow as numerical values or an algorithm directly from the qualitative criterion. No assertion of an entirely new general extremality test is made.

## Limitations
The result is specific to real unit-spaced path metrics and the additive bounded-Lipschitz norm. It does not give a closed elementary expression for \(V_n\), nor a polynomial-time algorithm for optimizing a general signed measure over all extreme functions; the latter problem is separate from counting them. The numerical low-dimensional cross-checks cannot establish the all-\(n\) statement without the proof. An unindexed equivalent walk enumeration remains a bibliographic risk. Independent scientific validation has not been performed.

## References
1. S. C. Hille and E. S. Theewis, “Norming and dense sets of extreme points of the unit ball in spaces of bounded Lipschitz functions,” first public 15 May 2023, arXiv:2305.08500v1, https://arxiv.org/html/2305.08500v1, especially Sections 1 and 6.
2. S. C. Hille and E. S. Theewis, “Explicit expressions and computational methods for the Fortet-Mourier distance to finite weighted sums of Dirac measures,” first public 24 June 2022, arXiv:2206.12234v1, https://arxiv.org/html/2206.12234v2, especially Section 6.
