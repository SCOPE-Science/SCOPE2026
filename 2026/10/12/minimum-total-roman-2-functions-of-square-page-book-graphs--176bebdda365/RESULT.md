# Minimum total Roman \(\{2\}\) functions of square-page book graphs
## Finding
For every integer \(m\ge2\), let \(B_m\) be the square-page book graph formed from \(m\) copies of \(C_4\) sharing the common edge \(xy\), with page \(i\) equal to \(xu_iv_iyx\). Then
\[
\gamma_{t\{R2\}}(B_m)=4.
\]
If \(m\ge3\), the minimum function is unique:
\[
f(x)=f(y)=2,
\]
and every page vertex has label \(0\).

For \(m=2\), there are exactly six minimum functions: the spine function \(f(x)=f(y)=2\); the all-page-ones function with \(f(x)=f(y)=0\); and four functions with \(f(x)=f(y)=1\) and exactly one of \(u_i,v_i\) labeled \(1\) on each page.

## Assumptions and scope
A total Roman \(\{2\}\)-dominating function is a map
\[
f:V(G)\to\{0,1,2\}
\]
such that every zero-labeled vertex \(z\) satisfies
\[
\sum_{w\in N(z)}f(w)\ge2,
\]
and every positive-labeled vertex has a positive-labeled neighbor.

Write
\[
a=f(x),\quad b=f(y),\quad p_i=f(u_i),\quad q_i=f(v_i).
\]
For every page,
\[
p_i=0\Longrightarrow a+q_i\ge2,\qquad
q_i=0\Longrightarrow p_i+b\ge2.
\]
The boundary \(B_1=C_4\) is excluded because its optimum is \(3\).

## Proof
The labeling \(f(x)=f(y)=2\), with all page vertices zero, is feasible and has weight \(4\).

Fix \((a,b)\). Minimizing \(p_i+q_i\) subject to the two page implications gives:
- for \((a,b)=(2,2)\), page minimum \(0\), uniquely at \((0,0)\);
- for \((a,b)=(0,0)\), page minimum \(2\), at \((0,2),(1,1),(2,0)\);
- for every other spine pair, page minimum \(1\).

Suppose \(m\ge3\). If \((a,b)=(0,0)\), the total weight is at least \(2m\ge6\). If \((a,b)\ne(0,0),(2,2)\), then every page has weight at least \(1\), so
\[
\omega(f)\ge a+b+m.
\]
For \(m\ge4\), equality with \(4\) is impossible. For \(m=3\), equality could occur only when \(a+b=1\). If \((a,b)=(1,0)\), every page must have \((p_i,q_i)=(0,1)\), making every positive \(v_i\) isolated; the symmetric case is identical. Hence only \((a,b)=(2,2)\) can attain weight \(4\), and then every page is \((0,0)\). This proves uniqueness for \(m\ge3\).

Now let \(m=2\) and \(\omega(f)=4\). For \((a,b)=(2,2)\), both pages are zero. For \((a,b)=(0,0)\), each page has weight \(2\); totality rules out \((0,2)\) and \((2,0)\), leaving \((1,1)\) on both pages. If \(a+b=2\), the only feasible spine pair is \((1,1)\), with each page independently \((1,0)\) or \((0,1)\), giving four functions; the pairs \((2,0)\) and \((0,2)\) isolate every page-positive vertex. If \(a+b=1\), the two page minima leave only one spare unit, but both page-positive vertices would need positive mates, requiring at least two extra units. Larger spine sums exceed weight \(4\). Thus exactly the six listed functions are minimum.

## Verification
The included checker directly evaluates both defining conditions for every labeling of weight at most the relevant optimum for \(1\le m\le12\). It recovers the excluded boundary \(B_1\), the six minimum functions for \(B_2\), and the unique spine function for every tested \(m\ge3\).

## Relationship to prior work
The 2019 introducing paper defines total Roman \(\{2\}\)-domination, gives general inequalities and complexity results, and contains no book-graph or theta-graph specialization in its searchable author manuscript. A second foundational study gives further structural, extremal, and bounded-clique-width results, again without a book or theta theorem.

Square-page books with \(m\ge2\) are not complete multipartite: the four page vertices from two pages induce two disjoint edges. Thus complete-multipartite formulas for neighboring Roman parameters do not specialize to this family.

The equality structure shows a sharp rigidity threshold: \(B_2\) has six optima, while every \(B_m\) with \(m\ge3\) has a unique optimum concentrated on the spine.

## Limitations
The theorem classifies minimum functions only, not all feasible functions by weight. The finite computation through \(m=12\) is corroborative only. A differently phrased or non-indexed book-graph treatment may exist.

## References
1. S. Cabrera García, A. Cabrera Martínez, F. A. Hernández Mira, I. G. Yero, “Total Roman \(\{2\}\)-domination in graphs,” Quaestiones Mathematicae 44(3) (2021), 411–434, DOI 10.2989/16073606.2019.1695230; published online 28 November 2019.
2. H. Abdollahzadeh Ahangar, M. Chellali, S. M. Sheikholeslami, J. C. Valenzuela-Tripodoro, “Total Roman \(\{2\}\)-Dominating Functions in Graphs,” Discussiones Mathematicae Graph Theory 42(3) (2022), 937–958, DOI 10.7151/dmgt.2316.
