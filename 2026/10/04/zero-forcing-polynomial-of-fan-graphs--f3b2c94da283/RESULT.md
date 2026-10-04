# Zero forcing polynomial of fan graphs
## Finding
Let \(F_m=K_1\vee P_m\), with \(m\ge2\), be the fan graph whose cone vertex is \(c\) and whose path vertices are \(v_1,\ldots,v_m\). A set containing \(c\) is zero forcing exactly when its path part is zero forcing in \(P_m\). A set omitting \(c\) is zero forcing exactly when it contains \(\{v_1,v_2\}\), or \(\{v_{m-1},v_m\}\), or three consecutive path vertices. Consequently, if \(B_m(x)\) is the weight enumerator of binary strings of length \(m\) having no factor \(111\) and neither beginning nor ending with \(11\), then \[\mathcal Z(F_m;x)=x\mathcal Z(P_m;x)+(1+x)^m-B_m(x).\] For \(m\ge6\), writing \(Q_r(x)\) for the no-\(111\) binary-string enumerator, \[B_m(x)=Q_m(x)-2x^2Q_{m-3}(x)+x^4Q_{m-6}(x),\] where \(Q_0=1\), \(Q_1=1+x\), \(Q_2=1+2x+x^2\), and \(Q_r=Q_{r-1}+xQ_{r-2}+x^2Q_{r-3}\). Thus \(Z(F_m)=2\); there are three minimum zero forcing sets when \(m=2\) and exactly four for every \(m\ge3\).

## Assumptions and scope
All graphs are finite and simple. For \\(m\\ge2\\), the fan graph is
\\[
F_m=K_1\\vee P_m,
\\]
with cone vertex \\(c\\) and path \\(v_1v_2\\cdots v_m\\). A zero forcing set is an initially blue vertex set from which repeated use of the rule “a blue vertex with exactly one white neighbor forces that neighbor blue” colors every vertex.

Write \\(z(G;j)\\) for the number of zero forcing sets of size \\(j\\), and
\\[
\\mathcal Z(G;x)=\\sum_j z(G;j)x^j.
\\]
Let \\(B_m(x)\\) be the weight enumerator of binary strings \\(b_1\\cdots b_m\\) satisfying three conditions: they contain no factor \\(111\\), \\(b_1b_2\\ne11\\), and \\(b_{m-1}b_m\\ne11\\).

## Proof
First suppose \\(c\\) is initially blue. If the path part of the initial set is zero forcing in \\(P_m\\), the same path forces work in the fan because the extra neighbor \\(c\\) is already blue. Conversely, the non-forcing sets of a path are exactly the subsets containing neither endpoint and no two consecutive vertices. For such a set, each blue path vertex has two white path neighbors, while \\(c\\) has at least two white path neighbors, so no force is possible in the fan. Therefore
\\[
S\\ni c\\text{ is zero forcing in }F_m
\\iff S\\setminus\\{c\\}\\text{ is zero forcing in }P_m.
\\]
These sets contribute \\(x\\mathcal Z(P_m;x)\\).

Now suppose \\(c\\notin S\\). Before the center becomes blue, no path vertex can force another path vertex: the white center is already one white neighbor. Hence the first force, if any, must be a path vertex forcing \\(c\\). An endpoint can do this exactly when the adjacent path vertex is blue, giving \\(\\{v_1,v_2\\}\\subseteq S\\) or \\(\\{v_{m-1},v_m\\}\\subseteq S\\). An internal vertex \\(v_i\\) can force \\(c\\) exactly when both \\(v_{i-1}\\) and \\(v_{i+1}\\) are blue, giving three consecutive blue path vertices.

Each of these triggering patterns already contains either a path endpoint or two consecutive path vertices, so after \\(c\\) is forced the blue path vertices force all of \\(P_m\\). Thus the stated trigger condition is both necessary and sufficient.

A center-free subset fails exactly when its binary indicator string has no \\(111\\), does not begin with \\(11\\), and does not end with \\(11\\). Hence the center-free zero forcing sets contribute \\( (1+x)^m-B_m(x)\\), proving
\\[
\\mathcal Z(F_m;x)=x\\mathcal Z(P_m;x)+(1+x)^m-B_m(x).
\\]

For an explicit form, let \\(Q_r(x)\\) count binary strings of length \\(r\\) with no \\(111\\). Splitting by the final block \\(0\\), \\(10\\), or \\(110\\) gives
\\[
Q_r=Q_{r-1}+xQ_{r-2}+x^2Q_{r-3},
\\]
with \\(Q_0=1\\), \\(Q_1=1+x\\), and \\(Q_2=1+2x+x^2\\). For \\(m\\ge6\\), inclusion-exclusion on a forbidden initial \\(11\\) and a forbidden final \\(11\\) gives
\\[
B_m=Q_m-2x^2Q_{m-3}+x^4Q_{m-6}.
\\]
The small boundary polynomials are
\\[
B_2=1+2x,\\quad B_3=1+3x+x^2,\\quad B_4=1+4x+4x^2,\\quad B_5=1+5x+8x^2+3x^3.
\\]
Using the known path formula
\\[
\\mathcal Z(P_m;x)=\\sum_{j=1}^m\\left(\\binom mj-\\binom{m-j-1}{j}\\right)x^j,
\\]
with out-of-range binomial coefficients interpreted as zero, this is a coefficient-explicit formula for every fan.

Finally, \\(F_m\\) has zero forcing number \\(2\\). For \\(m\\ge3\\), its four minimum sets are
\\[
\\{c,v_1\\},\\quad\\{c,v_m\\},\\quad\\{v_1,v_2\\},\\quad\\{v_{m-1},v_m\\}.
\\]
For \\(m=2\\), the fan is \\(K_3\\), so the three two-vertex subsets are the minimum zero forcing sets.

## Verification
The included checker constructs each fan directly for \\(2\\le m\\le17\\). For every vertex subset it runs the color-change process without using the structural theorem, then compares the result with the trigger classification. It separately expands the polynomial formula using integer coefficient arithmetic, checks the no-\\(111\\) recurrence and boundary inclusion-exclusion, and compares every coefficient.

The replay checks \\(524280\\) vertex subsets and \\(464701\\) zero forcing sets across sixteen fan graphs. Every structural decision and polynomial coefficient agrees.

## Relationship to prior work
Boyer et al. introduced the zero forcing polynomial and gave exact formulas for several families, including paths and wheels. Their wheel proof already separates zero forcing sets according to whether the dominating vertex is present, but their full manuscript contains no fan-graph treatment. The path formula used above is their Proposition 5.

Menon and Singh later studied the coefficient counts \\(z(G;j)\\) under graph operations. Their 2024 preprint proves the path-extremal conjecture for all outerplanar graphs and gives a cone lemma yielding coefficient inequalities for cones. Since fans are cones over paths and are outerplanar, those results give useful broader bounds, but they do not determine the exact coefficient sequence of \\(F_m\\). The present trigger classification supplies that missing exact enumeration.

Targeted searches for “zero forcing polynomial” together with “fan graph”, “cone over path”, and \\(K_1\\vee P_m\\) returned the foundational counting papers and general outerplanar/cone results, but no equivalent fan formula.

## Limitations
The theorem concerns ordinary zero forcing, not positive-semidefinite, skew, probabilistic, or failed zero forcing. The finite exhaustive checks through \\(m=17\\) are corroborative only; the all-\\(m\\) result follows from the exact trigger proof. Literature searches cannot exclude a differently phrased or non-indexed exact fan enumeration.

## References
1. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, C. Reinhart, “The zero forcing polynomial of a graph,” arXiv:1801.08910v1, 26 January 2018; Discrete Applied Mathematics 258 (2019), 35–48, DOI 10.1016/j.dam.2018.11.033.
2. K. Menon, A. Singh, “Exploring the Influence of Graph Operations on Zero Forcing Sets,” arXiv:2405.01423v1, 2 May 2024; Discrete Mathematics 348 (2025), 114516, DOI 10.1016/j.disc.2025.114516.
