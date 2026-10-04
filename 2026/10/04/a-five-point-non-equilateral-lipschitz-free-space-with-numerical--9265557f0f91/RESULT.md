# A five-point non-equilateral Lipschitz-free space with numerical index one half
## Finding
Let \(W_4=C_4\vee K_1\) be the five-vertex wheel graph with its unweighted shortest-path metric. Then its real Lipschitz-free space satisfies
\[
n(\mathcal F(W_4))=\frac12.
\]
The metric is not equilateral: hub-to-rim and adjacent-rim distances are \(1\), while opposite rim vertices are at distance \(2\). Thus the exact three-point rigidity \(n(\mathcal F(M))=1/2\) if and only if \(M\) is equilateral is genuinely dimension-dependent.

## Assumptions and scope
The scalar field is \(\mathbb R\). The graph \(W_4\) has hub \(0\), rim vertices \(1,2,3,4\), hub-rim edges, and the cycle edges \(12,23,34,41\), all of length \(1\). The basepoint is the hub; changing the distinguished point gives an isometric Lipschitz-free space.

Write \(\delta_i=\delta(i)\) for \(1\le i\le4\), so \(\mathcal F(W_4)\) is represented on the basis \((\delta_1,\delta_2,\delta_3,\delta_4)\). The numerical index is
\[
n(X)=\inf\{v(T): T\in\mathcal L(X),\ \|T\|=1\}.
\]

## Proof
For a finite metric space, extreme points of the free-space unit ball are molecules. In this graph metric, the extreme molecules are exactly the \(16\) oriented edge molecules: every graph edge has length \(1\), while every nonedge pair is joined by a length-two geodesic and its molecule is not extreme.

The dual is \(\operatorname{Lip}_0(W_4)\). With \(f(0)=0\), its unit ball is cut out by
\[
|f_i|\le1,\qquad |f_i-f_j|\le1
\]
for consecutive rim vertices \(i,j\). The defining matrix is a reduced signed incidence matrix, hence totally unimodular. Therefore every vertex is integral. Enumerating the \(3^4\) vectors in \(\{-1,0,1\}^4\) and retaining those with four linearly independent active constraints gives exactly \(26\) extreme dual functionals.

For finite-dimensional real Banach spaces the numerical radius may be evaluated on norming pairs of primal and dual extreme points. Here there are exactly \(128\) pairs \((m,f)\) satisfying \(f(m)=1\). Consequently \(v(T)\le1\) is equivalent to the \(256\) signed linear inequalities
\[
|f(Tm)|\le1
\]
over those norming pairs.

The accompanying exact certificate treats the \(16\) entries of \(T\) as variables. For each of the \(16\cdot26=416\) possible extreme evaluations \(f(Tm)\) that can attain the operator norm, it supplies a nonnegative rational linear combination of the \(256\) numerical-radius inequalities whose coefficient sum is at most \(2\) and whose left-hand side is exactly that evaluation. Hence
\[
\|T\|\le2v(T)
\]
for every operator \(T\), so \(n(\mathcal F(W_4))\ge1/2\).

Equality is attained. In the displayed basis, let
\[
T_0=
\begin{pmatrix}
-1&0&0&0\\
1&0&0&0\\
0&0&1&0\\
1&1&0&1
\end{pmatrix}.
\]
Exact evaluation over all \(128\) norming pairs gives \(v(T_0)=1\), while evaluation over all \(16\cdot26\) primal-dual extreme pairs gives \(\|T_0\|=2\). Therefore \(\frac12T_0\) has norm \(1\) and numerical radius \(1/2\), proving the reverse inequality.

## Verification
Run `python3 artifacts/verify.py`. It uses only the Python standard library and exact rational arithmetic. It reconstructs the \(16\) primal extreme points, the \(26\) dual extreme points, and the \(128\) norming pairs; checks all \(416\) dual certificates coefficient-by-coefficient; and verifies \(v(T_0)=1\) and \(\|T_0\|=2\). The expected output is `VERIFY_OK`.

## Relationship to prior work
Cobollo, Guirao, and Montesinos computed the numerical index of every two-dimensional Lipschitz-free space. Their Corollary 5.3 states that for a three-point metric space \(M\),
\[
n(\mathcal F(M))=\frac12
\]
if and only if \(M\) is equilateral. Their paper explicitly develops the finite-dimensional extreme-point formula for numerical radius used above and frames the work as a starting point for studying numerical radii of Lipschitz-free spaces.

The present calculation is outside that theorem: \(W_4\) has five metric points and \(\dim\mathcal F(W_4)=4\). Targeted searches for the wheel graph, graph metrics, the value \(1/2\), and higher-dimensional Lipschitz-free numerical index did not identify a published statement implying this value. The exact five-point example therefore gives a concrete boundary to the three-point equilateral characterization rather than a reformulation of it.

## Limitations
The claim is only for the single five-point wheel metric \(W_4\); no formula for larger wheels or arbitrary graph metrics is asserted. The originality comparison is literature-based and cannot exclude an obscure equivalent computation under a different polyhedral-space presentation. The proof uses a finite exact certificate together with the standard total-unimodularity fact for graph incidence matrices; it does not rely on floating-point optimization.

## References
1. Ch. Cobollo, A. J. Guirao, V. Montesinos, “The numerical index of \(2\)-dimensional Lipschitz-free spaces,” arXiv:2304.13183, first posted 25 April 2023; Journal of Mathematical Analysis and Applications 538 (2024), 128333, DOI 10.1016/j.jmaa.2024.128333.
