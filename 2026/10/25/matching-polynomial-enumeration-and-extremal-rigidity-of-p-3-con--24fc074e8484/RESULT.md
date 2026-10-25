# Matching-polynomial enumeration and extremal rigidity of \(P_3\)-convex sets in complete-graph subdivisions

## Finding
For a finite simple graph \(H=(V,E)\), let \(S(H)\) be its **once-subdivided graph**: replace every edge \(e=uv\) by a path \(u,\widetilde e,v\). Write \(P_{S(H)}(z)=\sum_C z^{|C|}\), summing over all \(P_3\)-convex vertex sets \(C\) of \(S(H)\). Then
\[
P_{S(H)}(z)=\sum_{U\subseteq V} z^{|U|+|E(H[U])|}
\sum_{M\in\mathcal M(H[V\setminus U])}
 z^{|M|}\prod_{w\in (V\setminus U)\setminus V(M)}
 \bigl(1+|N_H(w)\cap U|z\bigr),
\]
where \(\mathcal M(J)\) denotes all matchings of \(J\), including the empty matching.

For the complete graph \(K_n\), with \(n\ge2\), this yields the explicit size polynomial
\[
 A_n(z)=\sum_{u=0}^n \binom{n}{u}z^{u+\binom u2}
 \sum_{j=0}^{\lfloor(n-u)/2\rfloor}
 \frac{(n-u)!}{2^j j!(n-u-2j)!}\,z^j(1+uz)^{n-u-2j}.
\]
Let \(a_n=A_n(1)\), with \(a_0=1\). Its exponential generating function is
\[
\boxed{\sum_{n\ge0}a_n\frac{t^n}{n!}=
\exp\bigl(t+\tfrac12t^2+t e^t\bigr).}
\]
In particular, \(a_1,\ldots,a_6=2,7,29,143,797,4945\).

For \(n\ge3\), put \(N=n+\binom n2\). The largest **proper** \(P_3\)-convex set of \(S(K_n)\) has size \(N-(n-1)=n+\binom{n-1}{2}\); there are exactly \(n(n-1)\) such sets. Each contains precisely \(n-1\) original vertices, all subdivision vertices internal to those originals, and exactly one subdivision vertex corresponding to an edge incident with the one omitted original vertex. Thus \([z^j]A_n(z)=0\) whenever \(N-n+2\le j\le N-1\), whereas \([z^N]A_n(z)=1\).

## Assumptions and scope
All graphs are finite, simple and undirected, and a matching may be empty. A subset \(C\) is \(P_3\)-convex exactly when every vertex outside \(C\) has at most one neighbor inside \(C\). Both the empty set and the full vertex set count. The general decomposition applies without connectivity assumptions. The complete-graph enumeration applies to every integer \(n\ge2\); the extremal classification is stated for \(n\ge3\).

## Proof
Write \(C=U\cup\{\widetilde e:e\in F\}\), where \(U\subseteq V(H)\) and \(F\subseteq E(H)\). An omitted edge-vertex \(\widetilde e\) has two selected neighbors exactly when both endpoints of \(e\) lie in \(U\). Hence all edges of \(H[U]\) are forced into \(F\). An omitted original vertex \(w\notin U\) has \(\deg_F(w)\) selected neighbors, so the other necessary and sufficient constraint is \(\deg_F(w)\le1\). No condition is imposed at selected vertices. These two conditions are simultaneously sufficient because every vertex of \(S(H)\) is either an original vertex or an edge-vertex.

Fix \(U\) and put \(W=V(H)\setminus U\). The selected edges inside \(W\) form a matching \(M\). Every vertex of \(W\) covered by \(M\) has exhausted its one permitted selected-edge incidence. Each remaining vertex \(w\in W\setminus V(M)\) independently chooses either no selected cross edge or exactly one among its \(|N_H(w)\cap U|\) edges into \(U\). Their weighted contributions are respectively \(1\) and \(|N_H(w)\cap U|z\). Along with the mandatory \(|E(H[U])|\) edges, this proves the general identity and uniqueness of its decomposition.

If \(H=K_n\) and \(|U|=u\), then \(|E(H[U])|=\binom u2\), each vertex outside \(U\) has exactly \(u\) neighbors in \(U\), and the number of size-\(j\) matchings in \(K_{n-u}\) is \((n-u)!/(2^j j!(n-u-2j)!)\). Choosing \(U\) in \(\binom nu\) ways proves the explicit size polynomial.

To obtain the exponential generating function, specialize \(z=1\), write \(w=n-u\), and sum over all \(w\) and \(j\). The matching exponential formula gives
\[
\sum_{w\ge0}\frac{t^w}{w!}
\sum_{j=0}^{\lfloor w/2\rfloor}
\frac{w!}{2^j j!(w-2j)!}(1+u)^{w-2j}
=\exp\bigl((1+u)t+\tfrac12t^2\bigr).
\]
Multiplying by \(t^u/u!\) and summing over \(u\ge0\) yields
\[
\exp(t+\tfrac12t^2)\sum_{u\ge0}\frac{(t e^t)^u}{u!}
=\exp(t+\tfrac12t^2+t e^t).
\]
These are identities of formal power series, requiring no analytic convergence assumptions.

For the extremal claim, if \(U=V(K_n)\), every edge-vertex is forced and \(C=V(S(K_n))\). For a proper convex set, therefore, \(u=|U|\le n-1\) and \(w=n-u\ge1\). Every selected edge-vertex not internal to \(U\) is incident to at least one original vertex of \(W\), and each \(w\in W\) is incident to at most one such edge-vertex. Therefore
\[
|C|=u+|F|\le u+\binom u2+(n-u)
=n+\binom u2\le n+\binom{n-1}{2}.
\]
For \(n\ge3\), equality in the second inequality forces \(u=n-1\). Then there is one omitted original vertex; every internal edge-vertex must be selected and the omitted original must see precisely one selected cross-edge-vertex. Choosing that omitted original and one of its \(n-1\) incident edges gives exactly \(n(n-1)\) distinct maximizers. They are convex by the necessary-and-sufficient characterization. The strict upper bound for every other proper set gives the stated top-coefficient gap.

## Verification
The accompanying standalone Python program `verify_subdivision.py` enumerates each vertex subset directly from the subdivided graph's adjacency. It checks the general matching formula on all 75 labelled host graphs with at most four vertices; checks the size-polynomial, count and complete extremizer description for \(S(K_n)\) with \(2\le n\le6\); and compares the exponential-generating-function recurrence with the closed formula for \(0\le n\le30\). The program produced `VERIFY_OK general_hosts= 75 complete_hosts=5 egf_orders=31`. The mathematical proof covers all orders independently of the finite checks.

## Relationship to prior work
Dourado, Grippo, Lin and Protti introduced a systematic 2026 counting study of \(P_3\)-convex sets, including general algorithms, counting hardness and tractable tree and threshold graph subclasses [1]. Their paper supplies the motivating invariant and its established difficulty; the direct finite-alphabet matching decomposition, the explicit family exponential generating function and the extremal rigidity theorem above are not stated among its inspected results. Earlier work by Centeno and collaborators treats partitions into \(P_3\)-convex sets [2], a different enumerative question. Matching enumeration itself is classical; it is the interaction with the \(P_3\) closure condition on subdivisions that yields the formulas. These comparisons do not constitute a proof of historical priority.

## Limitations
This theorem concerns **one** subdivision per edge and the \(P_3\) closure rule, not geodetic, cycle or general path convexities. It does not claim a polynomial-time counting algorithm for arbitrary host graphs, and its complete closed-form EGF and extremal classification concern only complete hosts. Finite computational experiments do not establish the infinite identities or exclusion of stronger published equivalents. Independent validation has not been performed.

## References
[1] M. C. Dourado, L. N. Grippo, M. C. Lin and F. Protti, *Counting \(P_3\)-convex sets in graphs*, arXiv:2603.04706v1 (first publicly available 2026-03-05), https://arxiv.org/html/2603.04706v1.

[2] C. C. Centeno, S. Dantas, M. C. Dourado, D. Rautenbach and J. L. Szwarcfiter, *Convex Partitions of Graphs induced by Paths of Order Three*, Discrete Mathematics & Theoretical Computer Science 12 (2010), https://doi.org/10.46298/dmtcs.502.
