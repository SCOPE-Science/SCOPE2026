# Minimal total domination of rook graphs: a component census and a forbidden near-maximum size

## Finding

For all integers \(m,n\ge2\), let \(R_{m,n}=K_m\square K_n\), with one vertex for each square of a labeled \(m\)-row, \(n\)-column board. Define
\[
M_{m,n}(z)=\sum_{S\text{ inclusion-minimal total dominating in }R_{m,n}}z^{|S|}.
\]
Put
\[
\begin{aligned}
A(u,v,z)&=v(e^{zu}-1-zu)+\frac{uz^2v^2}{2}
             +u(e^{z^2uv}-1-z^2uv),\\
B(u,v,z)&=A(v,u,z),\\
C(u,v,z)&=\frac{z^2}{2}(uv^2+u^2v).
\end{aligned}
\]
Then the **complete cardinality polynomial** is
\[
\boxed{M_{m,n}(z)=m!n!\,[u^m v^n]\left((e^v-1)e^{A(u,v,z)}
 +(e^u-1)e^{B(u,v,z)}+e^{C(u,v,z)}\right).}
\]
This follows from the complete component classification below, not just a numerical recurrence.

For every integer \(n\ge3\), the **upper total domination number** of the square rook graph is
\[
\boxed{\Gamma_t(R_{n,n})=2n-2.}
\]
For \(n\ge4\), exactly \(2n\,n!\) inclusion-minimal total dominating sets have that maximum cardinality. For every \(n\ge5\), **there is none of cardinality \(2n-3\)**, despite the presence of minimal total dominating sets of larger cardinality.

As concrete checks, \(M_{3,3}(z)=6z^3+45z^4\), \(M_{4,4}(z)=80z^4+96z^5+192z^6\), and \(M_{5,5}(z)=410z^5+5700z^6+1200z^8\). Their evaluations at \(z=1\) are known earlier counts; these values alone are not new claims.

## Assumptions and scope

All graphs are finite, simple, and labeled by board rows/columns. A total dominating set \(S\) satisfies \(N(S)=V(R_{m,n})\) with **open** neighborhoods; it is *inclusion-minimal* if deleting any member destroys total domination. This is different from a set of minimum cardinality, and the polynomial counts actual labeled sets, not isomorphism classes.

Identify \(S\) with the selected-edge set \(F\) of \(K_{m,n}\), joining row vertex \(r\) and column vertex \(c\) when its square is selected. A row or column vertex is *unused* if its degree in \(F\) is zero; the connected components below omit those unused vertices. A two-edge path is written \(P_3\); a *subdivided row star with \(k\) arms* has one central row, \(k\) distinct adjacent columns, and one private pendant row beyond each such column, so it has \(k+1\) rows, \(k\) columns, and \(2k\) selected edges.

The classification consists of exactly three disjoint regimes:

1. **All rows used and at least one column unused:** every nontrivial component of \(F\) is either (a) a column-centered star with at least two row leaves, (b) a row-centered two-edge star \(P_3\) with two column leaves, or (c) a subdivided row star with at least two arms. The unused columns are arbitrary and at least one exists.
2. **All columns used and at least one row unused:** the transpose of regime 1.
3. **All rows and columns used:** every component of \(F\) is exactly a two-edge path \(P_3\), centered either at a row or at a column.

No case containing unused vertices on both sides is total dominating.

## Proof

**1. The two total-domination obstructions.** A board square \((r,c)\) outside \(S\) has no selected neighbor exactly when row \(r\) and column \(c\) both have degree zero. A selected square \((r,c)\) has \(d_F(r)+d_F(c)-2\) selected rook neighbors. Therefore \(S\) is totally dominating if and only if \(F\) has no component consisting of one isolated selected edge and at least one of the two bipartition classes is entirely used. This equivalence includes all boundaries \(m,n\ge2\).

**2. Essential edges.** For a selected edge \(e\), deleting \(e\) can destroy total domination only by either (i) turning a different selected edge into an isolated selected edge or (ii) creating unused vertices in both sides. Mechanism (i) is equivalent to the vertex \(e\) of the line graph \(L(F)\) having a neighbor of degree one there. If all rows and columns of \(F\) are used, mechanism (ii) would require \(e\) to be the sole selected edge incident to both endpoints, prohibited by step 1. Thus every vertex of \(L(F)\) must have a degree-one neighbor. Any degree-one vertex must itself have a degree-one neighbor, which must be its sole neighbor; consequently every component of \(L(F)\) is \(K_2\), and every nontrivial component of \(F\) is \(P_3\). Conversely such a disjoint union, using all vertices of both classes, is minimally total dominating.

**3. Exactly one unused side.** Assume all rows used and some column unused. Now mechanism (ii) holds for \(e=(r,c)\) exactly when \(d_F(r)=1\). Hence every edge at a row of degree at least two must have a degree-one neighbor in \(L(F)\). Such a neighbor \(f\) either shares its row or its column with \(e\). If it shares the row, that row has degree two and the column of \(f\) has degree one. Because \(f\) must itself be essential but cannot empty its row, its sole line-graph neighbor \(e\) must also have line-graph degree one. The component is consequently a row-centered \(P_3\) with two column leaves. Otherwise \(f\) shares column \(c\): this column has degree two and its other row has degree one. Thus a row of degree at least two not belonging to a row-centered \(P_3\) has every incident column of degree two, each joined also to a different degree-one row. Its component is a subdivided row star, with at least two arms. Components with every row of degree one are column-centered stars, with at least two edges because selected-edge isolates are forbidden. These are exactly (a)–(c) in regime 1. Conversely, deleting a row-leaf edge empties its row (the already-unused column then witnesses an uncovered square), while deleting an edge between a nonleaf row and a degree-two column isolates its pendant-row edge; row-centered \(P_3\) edges similarly isolate their partners. Hence every listed component is indeed inclusion-essential. Transposition proves regime 2.

**4. Enumerating labeled components.** Let \(u\) mark rows, \(v\) columns, and \(z\) selected squares. A column star of \(k\ge2\) row leaves contributes \(vz^ku^k/k!\); a row-centered \(P_3\) contributes \(uz^2v^2/2\); a subdivided row star of \(k\ge2\) arms contributes \(u(z^2uv)^k/k!\). Summing gives \(A(u,v,z)\). The labeled-set exponential formula takes disjoint unions of these components, while at least one isolated column contributes \(e^v-1\). This produces the first term in the displayed formula. Transposition yields the second term. If neither side has isolates, each \(P_3\) may be centered in either class and the component generating series is \(C(u,v,z)\); its disjoint unions contribute \(e^C\). The three cases are disjoint, so coefficient extraction gives every coefficient of \(M_{m,n}(z)\).

**5. Upper bound, multiplicity, and forbidden gap.** On an \(n\times n\) board consider regime 1. A column star with \(k\ge2\) rows has \(k\) edges (deficit \(2k-k=k\) from twice its row count); a row-centered \(P_3\) has one row and two edges (deficit zero); a subdivided row star with \(k\ge2\) arms has \(k+1\) rows and \(2k\) edges (deficit two). Thus, writing \(\delta=2n-|F|\),
\[
\delta=\sum_{\text{column stars}}k+2\,\#\{\text{subdivided row stars}\}.
\]
Deficit zero would require \(n\) row-centered \(P_3\)'s using \(2n\) columns, contrary to the requirement that some column be unused. Deficit one is impossible. Therefore \(|F|\le2n-2\). Equality cannot involve a column star with two leaves, since its addition to the required \(n-2\) row-centered \(P_3\)'s would use \(2n-3>n-1\) columns for \(n\ge3\). The only possibility is one subdivided row star with \(n-1\) arms and one unused column. There are \(n\) choices of its center row, \(n\) choices of unused column, and \((n-1)!\) bijections between its other rows and occupied columns, giving \(n\,n!\) sets per orientation. Regime 2 contributes the same. Regime 3 has \(2n/3\) two-edge-path components when it exists, so \(|F|=4n/3\); for \(n\ge4\) this is strictly below \(2n-2\), while for \(n=3\) it ties and explains the extra nine maximum sets there. This establishes the upper bound and count for \(n\ge4\).

For \(n\ge5\), cardinality \(2n-3\) would require \(\delta=3\) in regime 1. The only decomposition of that deficit is one column star with three row leaves and \(n-3\) row-centered \(P_3\)'s. These use \(1+2(n-3)=2n-5>n-1\) columns, impossible with one unused column. The transposed case is symmetric, and a regime-3 set has size \(4n/3<2n-3\). Thus the penultimate size is absent.

## Verification

Run `python3 verify.py` using Python 3 standard library. It constructs the exact coefficient-extraction polynomial from the three independently specified component types and compares it to complete brute-force enumeration of inclusion-minimal total dominating sets on ten labeled rectangular boards. The checked boards include every \(m\times n\) square/rectangle listed by the script, with \(124752\) initial subsets evaluated altogether. It additionally checks seven earlier ungraded enumeration totals, including \(7310\) for \(5\times5\). Run `python3 structural_test.py` for a second, direct small-board check of the edge-local necessity conditions, independent of the generating-function expansion. These are finite cross-checks; the general statement is proved in steps 1–5, not extrapolated from them.

## Relationship to prior work

Kazemi–Pahlavsay–Stones, arXiv:1509.08208 (first public posting 2015-09-28), studies \(k\)-tuple total domination, notably minimum *2-tuple* total domination on rook graphs. That parameter is different from inclusion-minimal ordinary total dominating sets. Mertens's 2024 rook-graph domination polynomial counts all **ordinary** dominating sets, not the inclusion-minimal total dominating ones. The directly closest prior data are Howroyd's OEIS A384118 (2025), which gives the total number \(M_{m,n}(1)\) as a rectangular array and a two-parameter counting recurrence. In particular, the values \(51\), \(368\), and \(7310\) are known; those ungraded counts are not claimed as new. The present theorem distinguishes all cardinalities and identifies the square-board near-maximum gap and exact maximum-size multiplicity. Howroyd's related OEIS A384116 counts all total dominating sets without minimality, a different object.

## Limitations

The theorem addresses labeled rectangular rook graphs with both dimensions at least two, not arbitrary Cartesian products. It does not establish a general closed formula for every zero coefficient of \(M_{m,n}(z)\) for rectangular parameters, although the coefficient-extraction expression determines them exactly. Numerical verification covers finite boards only. A recurrence in OEIS A384118 might admit an implicit grading refinement; establishing that this precise full polynomial or upper-size gap is absent from every earlier treatment would require additional independent literature review. The work has not received independent mathematical audit.

## References

1. A. P. Kazemi, B. Pahlavsay, R. J. Stones, *Cartesian product graphs and k-tuple total domination*, arXiv:1509.08208, first posted 2015-09-28, https://arxiv.org/abs/1509.08208 .
2. S. Mertens, *Domination Polynomial of the Rook Graph*, Journal of Integer Sequences 27 (2024), Article 24.3.7, https://cs.uwaterloo.ca/journals/JIS/VOL27/Mertens/mertens6.html .
3. A. Howroyd, OEIS A384118, *Number of minimal total dominating sets in an \(m\times n\) rook graph*, first entry 2025-05-19, https://oeis.org/A384118 .
4. A. Howroyd, OEIS A384116, *Number of total dominating sets in a rook graph*, first entry 2025-05-19, https://oeis.org/A384116 .
