# Exponential homology growth in circular-ladder two-independence complexes

## Finding
For each integer \(n\ge3\), write \(G_n=C_n\square K_2\), and let \(X_n=\operatorname{Ind}_2(G_n)\) be the simplicial complex of vertex subsets inducing subgraphs of maximum degree at most one. Set
\[
Z_n=\sum_{F\in X_n}(-1)^{|F|}=-\widetilde\chi(X_n),
\]
where the empty face is included. Then
\[
Z_{n+6}=Z_{n+5}+Z_{n+3}-2Z_{n+2}+3Z_{n+1}-Z_n\quad(n\ge3),
\]
with \((Z_3,Z_4,Z_5,Z_6,Z_7,Z_8)=(4,-3,11,10,1,29)\). More strongly, \(Z_n\ne0\) **for every** \(n\ge3\).

Let \(\beta\) be the unique real root greater than one of \(q(x)=x^4-x^2-2x+1\); numerically \(\beta\approx1.386470914\). Then
\[
Z_n=\beta^n+O((131/100)^n),\qquad
\liminf_{n\to\infty}\left(\sum_j\dim_{\mathbb Q}\widetilde H_j(X_n;\mathbb Q)\right)^{1/n}\ge\beta.
\]
In particular, all these two-independence complexes have nontrivial reduced rational homology, and their total rational Betti numbers grow at least exponentially.

## Assumptions and scope
The graph \(C_n\) is the simple cycle on \(\mathbb Z/n\mathbb Z\), with \(n\ge3\). The vertices of \(G_n\) are \((i,j)\) with \(i\in\mathbb Z/n\mathbb Z\) and \(j\in\{0,1\}\); edges are \((i,j)(i\pm1,j)\) and \((i,0)(i,1)\). A face is any subset for which each selected vertex has **at most one selected graph neighbor**. Equivalently, each induced connected component has one or two vertices, so this is both the first higher-independence complex and the dissociation (induced-\(P_3\)-free) complex. The parameter \(n\) denotes rungs, not graph vertices. The statement concerns rational homology over \(\mathbb Q\), without asserting an integral homotopy classification or a distribution of individual Betti degrees.

## Proof
**1. Cyclic transfer formula.** Represent the selected vertices in rung \(i\) by a two-bit vector \(b_i\in\{0,1,2,3\}\), where bit \(j\) records selection of layer \(j\). Let \(S=\{0,1,2,3\}^2\), with a state \((a,b)\) encoding two consecutive rungs. Define a signed integer \(16\times16\) matrix \(T\), with rows and columns indexed by \(S\), by
\[
T_{(a,b),(b',c)}=\begin{cases}
(-1)^{\mathrm{popcount}(b)},&b'=b\text{ and, for each }j\text{ with }b_j=1,\quad a_j+c_j+b_{1-j}\le1,\\
0,&\text{otherwise}.
\end{cases}
\]
Here all symbols \(a_j,b_j,c_j\) are binary bits; \(\mathrm{popcount}\) is their sum over the two layers. The inequality says precisely that a selected vertex in the middle rung has at most one selected neighbor among the preceding rung, the succeeding rung and its partner in the middle rung. For \(n\ge3\), these three neighboring positions are distinct. A length-\(n\) closed walk of \(T\) is uniquely the sequence of \(n\) labelled rung masks \((b_0,\dots,b_{n-1})\), and the product of transition weights is \((-1)^{\sum_i\mathrm{popcount}(b_i)}\) when the selected set is a face, zero otherwise. Consequently
\[
Z_n=\operatorname{tr}(T^n)\qquad(n\ge3).
\]

**2. Exact characteristic polynomial.** The displayed entry formula determines the complete integer matrix. An exact Faddeev--LeVerrier calculation (fully implemented and checked in `verify_prism.py`) gives
\[
\det(xI_{16}-T)=x^{10}(x^2-x+1)(x^4-x^2-2x+1)
=x^{10}(x^6-x^5-x^3+2x^2-3x+1).
\]
By Cayley--Hamilton or the power-sum identity, its traces obey the order-six recurrence stated above. Direct powers supply \((Z_3,\ldots,Z_{13})=(4,-3,11,10,1,29,4,21,67,6,105)\); all these values are nonzero.

**3. Nonvanishing for all larger rungs.** Put \(q(x)=x^4-x^2-2x+1\). Its derivative factors as
\[
q'(x)=2(x-1)(2x^2+2x+1).
\]
Thus \(q\) decreases strictly below one and increases strictly above one. Also \(q(-t)=(t^2-1/2)^2+3/4+2t>0\) for \(t\ge0\). It follows that \(q\) has exactly two real roots: \(0<\alpha<1<\beta<2\). The remaining roots form a complex-conjugate pair \(\gamma,\overline\gamma\). Direct exact evaluations yield \(q(17/40)>0\) and \(q(69/50)<0\), so \(\alpha>17/40\), \(\beta>69/50\). Since the product of the four roots is one,
\[
|\gamma|^2=1/(\alpha\beta)<2000/1173<(131/100)^2.
\]
The roots of \(x^2-x+1\) are \(e^{\pm i\pi/3}\). Hence, for all \(n\ge3\),
\[
Z_n=\alpha^n+\beta^n+\gamma^n+\overline\gamma^{\,n}+2\cos(\pi n/3).
\]
For each \(n\ge14\),
\[
Z_n\ge\beta^n-2|\gamma|^n-2
>(69/50)^n-2(131/100)^n-2>0.
\]
The final inequality holds at \(n=14\) by exact rational arithmetic; dividing by \((131/100)^n\) makes the left exponential ratio strictly increasing in \(n\) and the right-hand bound \(2+2(100/131)^n\) strictly decreasing, so it holds for all later integers. Together with the eleven checked initial values, this proves \(Z_n\ne0\) for every \(n\ge3\).

**4. Homological consequence.** Since \(Z_n=-\widetilde\chi(X_n)\), the Euler--Poincaré identity gives
\[
\sum_j\dim_{\mathbb Q}\widetilde H_j(X_n;\mathbb Q)\ge|Z_n|>0.
\]
The root decomposition and \(\alpha<1\), \(|\gamma|<131/100<\beta\) show \(Z_n=\beta^n+O((131/100)^n)\). Taking \(n\)-th roots proves the lower growth bound. No finite experiment is used to infer this infinite-family conclusion.

## Verification
Run `python3 verify_prism.py` from the file directory. The script uses only the Python standard library. It constructs all \(16^2\) transfer entries from the local degree condition, derives the characteristic polynomial by exact integer Faddeev--LeVerrier arithmetic, verifies the recurrence and eleven initial traces, and checks the strict root and growth inequalities with `fractions.Fraction`. Separately, it exhaustively enumerates all labelled vertex subsets for \(3\le n\le8\), rechecks the induced-degree predicate and finds precisely the trace-predicted signed face sums. The recorded output is `verification_output.txt`, ending in `ALL_CHECKS_PASS`. The exact proof above, not the finite enumeration alone, establishes the statement for all integers.

## Relationship to prior work
Taylan's archive-era work on matching trees and graph-devoid complexes [1] determines the \(P_k\)-devoid homotopy types of single paths and cycles and forests. It does not classify the cyclic **two-layer Cartesian products** appearing here. Deshpande and Singh [2] treat higher independence of paths, cycles, complete multipartite graphs, whiskered graphs and perfect-ary trees, but do not supply this prism family. Tu, Xiao and Lang [3] establish positive-activity extremal bounds for dissociation polynomials of arbitrary cubic graphs; their theorem has activity in \((0,1]\), whereas the signed Euler--homology obstruction needs evaluation at \(-1\) and an exact cyclic recurrence. Results on ordinary independence, neighborhood, cut or Rips complexes of prism graphs concern different simplicial face conditions, so do not yield the present assertion. An equivalent independently published transfer calculation remains possible.

## Limitations
The result proves nonzero **reduced rational** homology and an exponential lower bound for its total Betti number, but neither determines the particular homology degrees for general \(n\) nor the complete homotopy type or an upper growth bound. The exact characteristic polynomial is computationally reproducible from the fully specified transfer matrix; the independent enumerations only run through eight rungs. No independent mathematical audit or exhaustive publication-priority certification has been performed.

## References
[1] D. Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754, first public version 2015-01-27; https://arxiv.org/abs/1501.06754.

[2] P. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448 (2020); https://arxiv.org/abs/2001.05448.

[3] J. Tu, J. Xiao and R. Lang, *Counting the number of dissociation sets in cubic graphs*, AIMS Mathematics 8 (2023), 10021--10032, DOI:10.3934/math.2023507; https://doi.org/10.3934/math.2023507.
