# Fiber-profile domination of complete-graph Sierpiński products

## Finding

Let \(m,n\ge2\) be integers and \(f:[m]\to[n]\) an arbitrary map. In the Sierpiński product \(X_f=K_m\otimes_f K_n\), put \(a_h=|f^{-1}(h)|\), and sort these multiplicities as \(a_1\ge\cdots\ge a_n\ge0\); the sorting is only a relabeling of the second complete graph. Write \(r=|\{h:a_h\ge2\}|\). Then the ordinary domination number of the **individual product for the specified map** is

\[
\gamma(X_f)=
\begin{cases}
m, & a_n=0,\\
\displaystyle\min\left(\{m\}\cup\left\{c^2+\sum_{j=c+1}^{n}\max\{a_j,c\}:1\le c\le r\right\}\right), & a_n\ge1.
\end{cases}
\]

The minimum over the empty indexed set is omitted, so the formula also covers a bijective map, for which \(r=0\) and \(m=n\).

Consequently the lower and upper Sierpiński domination numbers satisfy
\[
\gamma_S(K_m,K_n)=\min\{m,n\},\qquad \Gamma_S(K_m,K_n)=m.
\]
For every surjective \(f\), one has \(\gamma(X_f)\le n^2\), whereas for every nonsurjective \(f\) one has \(\gamma(X_f)=m\). In particular, for every \(m\ge6\), as \(f:[m]\to[2]\) varies, the **complete attainable spectrum** is
\[
\{\gamma(K_m\otimes_f K_2):f:[m]\to[2]\}=\{2,3,4,m\}.
\]
Thus there are arbitrarily long gaps in domination numbers attainable by varying the connection map while keeping both complete-graph factors fixed.

## Assumptions and scope

Graphs are finite, simple, undirected, and domination uses **closed** neighborhoods. The graph \(X_f\) has vertex set \([m]\times[n]\). Each fiber \(\{i\}\times[n]\) induces a clique. For every distinct \(i,j\in[m]\), precisely the additional cross-fiber edge
\[
(i,f(j))\,(j,f(i))
\]
is present. A dominating set is a vertex set meeting the closed neighborhood of every vertex. All statements quantify over **all** maps \(f\), including nonsurjective maps, and all integers \(m,n\ge2\). This is a one-step Sierpiński product, not an iterated generalized Sierpiński graph.

## Proof

**1. Empty-fiber constraint.** Fix a dominating set \(D\) of \(X_f\). Let \(E\subseteq[m]\) comprise the indices of fibers disjoint from \(D\), and set \(U=[m]\setminus E\). If \(E=\varnothing\), then \(|D|\ge m\), with equality achieved by taking one vertex in each clique fiber. Suppose \(E\ne\varnothing\). For an empty fiber \(i\in E\), a vertex \((i,h)\), with \(h\in[n]\), can only be dominated from another fiber by a selected vertex \((j,f(i))\), where \(j\in U\) and \(f(j)=h\). Therefore \(f(U)=[n]\), and in particular \(f\) is surjective.

Put \(C=f(E)\) and \(c=|C|\ge1\). For every \(h\in[n]\), let \(t_h=|U\cap f^{-1}(h)|\ge1\). Each one of the \(t_h\) occupied clique fibers contributes a selected vertex. Also, for every \(z\in C\), domination of the empty fiber(s) with image \(z\) requires a selected vertex \((j,z)\) with \(f(j)=h\); the \(c\) choices of \(z\) give distinct selected vertices. Hence
\[
|D|\ge\sum_{h=1}^n\max\{t_h,c\}. \tag{1}
\]
This lower bound is **attainable for any fixed admissible** \(E\): in the \(t_h\) occupied fibers of image \(h\), select exactly \(\max\{t_h,c\}\) vertices, distributing them so every occupied fiber receives at least one and every second coordinate in \(C\) appears at least once. This is possible because \(c\le n\): if \(t_h\ge c\), assign the \(c\) required coordinates to distinct fibers; if \(t_h<c\), assign them across all \(t_h\) fibers, allowing more than one vertex in a fiber. All occupied fibers are dominated internally, and every empty fiber is dominated externally. Thus (1) is the exact minimum over dominating sets whose empty fibers are precisely \(E\).

**2. Optimize the empty fibers.** Fix the nonempty set \(C=f(E)\) of cardinality \(c\). Since every image color must still occur in \(U\), each \(h\in C\) must satisfy \(a_h\ge2\). Conversely, any nonempty \(C\subseteq\{h:a_h\ge2\}\) is admissible: leave one occupied fiber of each image \(h\in C\), empty its other fibers, and keep all fibers of the other colors occupied. For each \(h\in C\) we have \(1\le t_h<a_h\). The expression \(\max\{t_h,c\}\) is minimized at \(t_h=1\), yielding \(c\). For \(h\notin C\), necessarily \(t_h=a_h\). Hence the optimum for this choice of \(C\) is exactly
\[
c^2+\sum_{h\notin C}\max\{a_h,c\}. \tag{2}
\]
For fixed \(c\), choosing a color \(h\) for \(C\) replaces its baseline contribution \(\max\{a_h,c\}\) with \(c\). The saving \(\max\{a_h-c,0\}\) is nondecreasing in \(a_h\). Therefore an optimal \(c\)-element choice of \(C\) consists of the \(c\) largest multiplicities, provided \(1\le c\le r\). Formula (2) becomes \(c^2+\sum_{j=c+1}^{n}\max\{a_j,c\}\). Taking the minimum with the all-occupied value \(m\) proves the stated formula. If \(f\) is nonsurjective, Step 1 forbids empty fibers, giving \(\gamma(X_f)=m\).

**3. Optimize over maps and derive gaps.** An empty fiber always forces at least one selected vertex with a different first coordinate for each of its \(n\) second coordinates, so any dominating set has at least \(\min\{m,n\}\) vertices. Selecting one vertex per fiber gives \(m\). If \(m>n\), choose a surjective map with multiplicities \((m-n+1,1,\ldots,1)\). The formula with \(c=1\) gives \(n\), establishing the lower Sierpiński domination value; for \(m\le n\), no improvement below \(m\) is possible. A constant map is nonsurjective for \(n\ge2\), proving the upper value \(m\).

If \(f\) is surjective and \(r=0\), then \(m=n\) and \(\gamma(X_f)=n\le n^2\). If \(r\ge1\), take \(c=r\): all unchosen multiplicities equal one, so formula (2) equals \(r^2+(n-r)r=nr\le n^2\). For \(n=2\), write the surjective multiplicities as \(a_1\ge a_2=b\ge1\). The displayed formula yields \(\gamma(X_f)=2\) for \(b=1\), \(3\) for \(b=2\), and \(4\) for \(b\ge3\), while nonsurjective maps have value \(m\). If \(m\ge6\), all three surjective cases and the nonsurjective case occur. This proves the claimed full spectrum and its unbounded missing interval \(\{5,\ldots,m-1\}\) when \(m\ge7\).

## Verification

The standalone standard-Python program `code/verify.py` independently builds the graph's closed neighborhoods from the defining edges, exhaustively checks candidate dominating subsets, and compares their true minimum to the formula. It covers 82 sorted multiplicity profiles: all profile representatives with \(2\le m\le9\) for \(n=2\), \(2\le m\le7\) for \(n=3\), and \(2\le m\le6\) for \(n=4\). Each tested profile agrees. The reduction to sorted profiles is justified by relabeling domain vertices and codomain colors in the two complete factors. The computation is a finite falsification check, not a substitute for Steps 1–3.

Reproduce using `python3 code/verify.py` from the extracted package root. Only the Python 3 standard library is needed.

## Relationship to prior work

Kovič, Pisanski, Zemljič, and Žitnik introduced the Sierpiński product and its dependence on a map in 2019 [1]. Henning, Klavžar, Kleszcz, and Pilśniak introduced lower and upper Sierpiński domination in 2023 [2]. Their general bound, upper extremal criterion (Theorem 2.2), and degree criterion (Proposition 2.3) imply some boundary values, including the upper complete-graph value and the case \(m\le n\). Their main explicit determinations concern two cycle factors, not the complete-graph map-multiplicity profile. The proof above independently establishes the full map-specific formula for complete factors; it does not claim those earlier definitions or bounds as new.

## Limitations

This result concerns ordinary vertex domination only, for one-step products of complete graph factors. It is not a classification for arbitrary factors, iterated Sierpiński graphs, or other domination variants. The computational cross-check is finite; the infinite formulas are established by the combinatorial argument. Literature searching cannot rule out equivalent prior work under alternative product or clique-fiber terminology; independent mathematical and priority review has not been performed.

## References

[1] J. Kovič, T. Pisanski, S. S. Zemljič, A. Žitnik, *The Sierpiński product of graphs*, arXiv:1904.04180v1 (public 2019-04-08), https://arxiv.org/abs/1904.04180 .

[2] M. A. Henning, S. Klavžar, E. Kleszcz, M. Pilśniak, *The Sierpiński Domination Number*, arXiv:2309.15409v1 (public 2023-09-27), https://arxiv.org/abs/2309.15409 ; Ars Mathematica Contemporanea 24 (2024), article P3.06, DOI:10.26493/1855-3974.2892.f07.
