# Italian domination polynomial of friendship graphs
## Finding
For every integer \(k\ge 1\), let \(F_k\) be the friendship graph formed from \(k\) triangles with exactly one common vertex \(c\). Write the two noncentral vertices in the \(i\)-th triangle as \(u_i,v_i\). For an Italian dominating function \(f:V(F_k)\to\{0,1,2\}\), every vertex labeled \(0\) must see total neighbor-label at least \(2\). Let
\[
D_I(F_k,x)=\sum_f x^{\sum_v f(v)}.
\]
Define
\[
T(x)=1+2x+3x^2+2x^3+x^4,
\]
\[
A(x)=2x+3x^2+2x^3+x^4,
\]
and
\[
B(x)=3x^2+2x^3+x^4.
\]
Then
\[
D_I(F_k,x)=B(x)^k+xA(x)^k+x^2T(x)^k.
\]
Hence the total number of Italian dominating functions is
\[
D_I(F_k,1)=6^k+8^k+9^k.
\]
Also \(\gamma_I(F_k)=2\) for every \(k\ge1\). For \(k\ge2\), the unique minimum-weight Italian dominating function labels \(c\) by \(2\) and all \(2k\) outer vertices by \(0\).

## Assumptions and scope
Graphs are finite, simple, and undirected. The friendship graph \(F_k\) has vertex set
\[
\{c\}\cup\{u_i,v_i:1\le i\le k\}
\]
and edges \(cu_i,cv_i,u_iv_i\) for every \(i\). The result counts all Italian dominating functions, not only minimum-weight functions. The statement includes \(k=1\), where \(F_1=K_3\); the uniqueness assertion is intentionally restricted to \(k\ge2\).

## Proof
Condition on the label of the common center \(c\).

If \(f(c)=2\), every outer vertex labeled \(0\) already receives neighbor-sum at least \(2\) from \(c\). Thus the two labels on each petal are arbitrary. The one-petal weight enumerator is
\[
(1+x+x^2)^2=T(x),
\]
so this case contributes \(x^2T(x)^k\).

If \(f(c)=1\), an outer vertex labeled \(0\) is valid exactly when its mate on the same triangle has label at least \(1\). Therefore the only forbidden ordered petal-label pair is \((0,0)\). The one-petal enumerator is
\[
(1+x+x^2)^2-1=A(x),
\]
so this case contributes \(xA(x)^k\).

If \(f(c)=0\), an outer vertex labeled \(0\) needs its mate to carry label \(2\). Hence the allowed ordered label pairs on one petal are
\[
(0,2),(2,0),(1,1),(1,2),(2,1),(2,2).
\]
Their weight enumerator is \(B(x)=3x^2+2x^3+x^4\). Every allowed petal has total weight at least \(2\), so for \(k\ge1\) the center itself automatically sees outer-neighbor total at least \(2\). Thus this case contributes \(B(x)^k\).

The three center-label cases are disjoint and exhaustive, proving the displayed polynomial identity. Substituting \(x=1\) gives \(6^k+8^k+9^k\). The term \(x^2T(x)^k\) always supplies a weight-\(2\) function by labeling only the center with \(2\), hence \(\gamma_I(F_k)=2\). For \(k\ge2\), the least exponent in \(xA(x)^k\) is \(k+1\ge3\), and the least exponent in \(B(x)^k\) is \(2k\ge4\), so the coefficient of \(x^2\) comes only from the constant term of \(T(x)^k\) and equals \(1\). This proves uniqueness of the minimum-weight function.

## Verification
A standalone verifier independently constructs \(F_k\), enumerates every labeling in \(\{0,1,2\}^{V(F_k)}\) for \(1\le k\le5\), checks the Italian domination condition vertex by vertex, forms the exact weight distribution, and compares it with the closed polynomial above. It also checks \(D_I(F_k,1)=6^k+8^k+9^k\), the minimum weight, and the minimum-function count. The analytic proof is valid for arbitrary \(k\); the finite computation is corroborative rather than the source of the infinite claim.

## Relationship to prior work
Shao and Zhao introduced the Italian domination polynomial as the weight enumerator of all Italian dominating functions and developed exact algorithms for paths, trees, and cycles. Their contribution summary explicitly lists paths, general trees, cycles, and numerical star tables; the inspected full text contains no friendship-graph or windmill-graph treatment. The present formula moves from tree/cycle dynamic programming to a non-tree block graph family and gives a closed product decomposition rather than a recurrence.

A 2024 survey of Roman \(\{2\}\)-domination predates the Italian domination polynomial and surveys minimum-weight parameters and variants rather than this later all-weight enumerator. Focused literature searches under both “Italian domination” and the older “Roman \(\{2\}\)-domination” terminology, combined with friendship/windmill aliases, found no exact weight-enumerator statement for \(F_k\). published-finding corpus searches likewise returned nearby results for complete multipartite Roman \(\{2\}\)-enumerators and unrelated windmill invariants, but no result implying the friendship polynomial above.

## Limitations
The result is specific to ordinary Italian domination on friendship graphs. It does not claim a formula for arbitrary windmills \(K_1\vee kK_r\), arbitrary block graphs, perfect Italian domination, or other Roman-type variants. The originality search is necessarily subject to indexing lag, especially because the Italian domination polynomial was introduced very recently.

## References
1. P. Shao and C. Zhao, “Counting Weight-\(k\) Italian Dominating Sets on Trees and Cycles,” arXiv:2610.00108v1, first submitted 2026-09-09.
2. A. Almulhim, “Survey on Roman \(\{2\}\)-Domination,” Mathematics 12 (2024), 2771.
3. W. F. Klostermeyer and G. MacGillivray, “Roman, Italian, and 2-Domination,” Journal of Combinatorial Mathematics and Combinatorial Computing 108 (2019), 125–146.
