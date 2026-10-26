# Parity phase transition and optimal-function census for signed total Roman domination on clique bouquets

## Finding
For integers \(m\ge2\) and \(t\ge3\), let \(W_{m,t}=K_1\vee(mK_t)\) be the graph obtained by joining a single hub to each vertex in \(m\) pairwise disjoint cliques of order \(t\). Then
\[
\gamma_{stR}(W_{m,t})=\begin{cases}3,&t\text{ even},\\m+2,&t\text{ odd}.\end{cases}
\]
All minimum-weight functions label the hub \(2\). Define
\[
H_t=\sum_{\substack{0\le d\le \lfloor(t+1)/3\rfloor\\d\equiv t-1\pmod 2}}\frac{t!}{a_d!\,b_d!\,d!},\qquad a_d=\frac{t-1+d}{2},\quad b_d=\frac{t+1-3d}{2}.
\]
The number \(M_{m,t}\) of functions attaining \(\gamma_{stR}\), with distinct vertices distinguished and labels fixed, is
\[
M_{m,t}=\begin{cases}mH_t\binom{t}{t/2}^{m-1},&t\text{ even},\\H_t^m,&t\text{ odd}.\end{cases}
\]
Thus the minimum weight changes from a constant to a quantity growing linearly in the number of clique blades when the blade order switches parity. The count gives a complete census of optimum labelings, not merely a value of the invariant.

## Assumptions and scope
All graphs are finite, simple, and undirected. The parameters \(m\) and \(t\) are integers with \(m\ge2\) and \(t\ge3\). The graph consists of a hub \(c\) and \(m\) disjoint sets \(B_j\) of \(t\) vertices each; each \(B_j\) induces a clique, every vertex in a blade is adjacent to \(c\), and no edges run between distinct blades.

A *signed total Roman dominating function* is \(f:V(G)\to\{-1,1,2\}\) for which every vertex \(v\) satisfies \(\sum_{u\in N(v)}f(u)\ge1\), and every vertex labeled \(-1\) has a neighbor labeled \(2\). Its weight is \(\omega(f)=\sum_{v\in V(G)}f(v)\), and \(\gamma_{stR}(G)\) is the minimum possible weight. Neighborhoods are **open**, not closed. The count \(M_{m,t}\) includes assignments on the named vertices, without quotienting by graph automorphisms.

## Proof
Fix a feasible function \(f\), let \(s=f(c)\), and put \(w_j=\sum_{v\in B_j}f(v)\). Since every outer vertex in \(B_j\) sees exactly the hub and the other vertices of its blade, the open-neighborhood condition at an outer vertex of label \(a\) is precisely
\[
s+w_j-a\ge1.\tag{1}
\]
The hub's condition is
\[
\sum_{j=1}^{m}w_j\ge1.\tag{2}
\]
If \(s=-1\), no blade can consist entirely of \(-1\) labels, since then (1) fails. Consequently, each blade has a label at least \(1\), and (1) for this label implies \(w_j\ge3\). Therefore \(\omega(f)=s+\sum_jw_j\ge3m-1\).

If \(s=1\), each blade containing a \(-1\) must itself contain a \(2\), by the Roman-neighbor requirement. For such a blade (1), applied at its \(2\)-label, gives \(w_j\ge2\). A blade with no \(-1\) has \(w_j\ge t\ge3\). Thus in all cases \(w_j\ge2\), yielding \(\omega(f)\ge2m+1\).

Suppose \(s=2\). A blade with any \(2\)-label must satisfy \(w_j\ge1\) by (1). A blade containing no \(2\) uses only \(-1\) and \(1\), so (1) requires \(w_j\ge0\). Hence every blade satisfies \(w_j\ge0\). If \(t\) is odd then \(w_j\ne0\): no-\(2\) blades have weight congruent to \(t\) modulo \(2\), whereas a blade with \(2\) has weight at least \(1\). Therefore all odd blades have \(w_j\ge1\), and \(\omega(f)\ge m+2\). If \(t\) is even, (2) instead gives \(\omega(f)\ge3\).

For odd \(t\), label the hub \(2\) and each blade with exactly \((t-1)/2\) instances of \(-1\) and \((t+1)/2\) instances of \(1\), so \(w_j=1\). For even \(t\), label the hub \(2\) and take one blade with \(t/2\) instances of \(-1\), \((t-2)/2\) instances of \(1\), and one \(2\), of weight \(1\), and all other blades with equal counts of \(-1\) and \(1\), of weight \(0\). For both constructions the outer inequalities (1), the hub condition (2), and the Roman-neighbor condition hold, since the hub is \(2\). These attain the respective lower bounds.

For \(m\ge2\), the bounds for \(s=-1\) and \(s=1\) strictly exceed both derived optima, so the hub is labeled \(2\) in every optimum. If \(t\) is odd, every blade must have weight \(1\); if \(t\) is even, exactly one blade has weight \(1\) and all others weight \(0\). A weight-zero blade cannot have a \(2\); it therefore has precisely \(t/2\) labels \(-1\) and \(t/2\) labels \(1\), giving \(\binom{t}{t/2}\) assignments. For a weight-one blade, let \(a,b,d\) count respectively labels \(-1,1,2\). Solving \(a+b+d=t\) and \(-a+b+2d=1\) yields \(a=a_d\), \(b=b_d\), with the parity, nonnegativity and upper-bound restrictions in \(H_t\). Every such labeling satisfies (1): its largest label is at most \(2\), so \(2+1-a\ge1\). Each weight-one blade therefore has exactly \(H_t\) admissible assignments. Independent choices across blades yield the stated product formulas. \(\square\)

## Verification
A standalone, standard-library-only Python 3 program, `verify.py`, directly enumerates all possible \(\{-1,1,2\}\)-vertex labelings in seven small cases, tests both feasibility conditions, and compares exact minima and multiplicities with the theorem. A separate blade-profile dynamic computation checks 77 parameter pairs through \(m=8\) and \(t=12\). See `VERIFICATION.md` and the executable source for the command and raw counts. These finite checks support the implementation; the argument above, not finite enumeration, proves the infinite assertion.

## Relationship to prior work
Koster, Volkmann, and Wehrmann (2026, arXiv:2606.27175) define the same signed total Roman condition and determine this invariant on complete multipartite graphs, while studying cubic graphs and signed total Roman domatic parameters. Clique bouquets with at least two blades of order at least three are neither complete multipartite nor cubic; their hub is a cut vertex. The complete-multipartite value in that paper, which is always \(2\) or \(3\) for at least three parts, cannot give the unbounded odd-blade value here. The earlier survey by Chellali, Jafari Rad, Sheikholeslami and Volkmann (2020) reviews signed total Roman domination on classical graph families. Zhao and Miao (2017) treat bicliques and wheels. Those graph families and the published statements inspected do not imply this exact clique-bouquet enumeration. Searches using both 'clique bouquet' and the synonyms 'windmill', 'friendship' and 'block graph' did not identify the present claim; this negative search evidence does not establish absolute historical novelty.

## Limitations
The theorem concerns \(m\ge2\), \(t\ge3\), and a common hub of exactly \(m\) equal-sized cliques; it does not classify arbitrary block graphs, unequal clique bouquets, or signed total Roman **domatic** numbers. The census distinguishes all named vertices. The proof is mathematical and has not been independently audited. A historical-priority risk remains from literature not accessed in full, especially early signed total Roman domination papers and possible alternate terminology.

## References
1. A. M. C. A. Koster, L. Volkmann and M. Wehrmann, *Signed Total Roman Domination and Domatic Numbers: Degree Three and Complete Multipartite Graphs*, arXiv:2606.27175, first posted 2026-06-25. https://arxiv.org/abs/2606.27175
2. M. Chellali, N. Jafari Rad, S. M. Sheikholeslami and L. Volkmann, *Varieties of Roman domination II*, AKCE Int. J. Graphs Combin. 17 (2020), 966--984. https://doi.org/10.1016/j.akcej.2019.12.001
3. Y. Zhao and L. Miao, *Signed Roman (Total) Domination Numbers of Complete Bipartite Graphs and Wheels*, 2017. https://doi.org/10.13447/j.1674-5647.2017.04.04
