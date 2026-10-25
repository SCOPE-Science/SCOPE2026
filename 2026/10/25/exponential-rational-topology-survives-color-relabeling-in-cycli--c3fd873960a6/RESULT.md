# Exponential rational topology survives color relabeling in cyclic partial-coloring complexes

## Finding
For all integers \(n\ge3\), \(q\ge1\), put \(X_{n,q}=\operatorname{Ind}(C_n\mathbin{\square}K_q)\) and \(Y_{n,q}=|X_{n,q}|/S_q\), where \(S_q\) permutes the complete-graph coordinate. Let \(D_0=1,D_1=0\), and \(D_j=(j-1)(D_{j-1}+D_{j-2})\) for \(j\ge2\). Define \(L_0(f)=2\), \(L_1(f)=2-f\), and \(L_{n+2}(f)=(2-f)L_{n+1}(f)-L_n(f)\).

The **exact reduced Euler characteristic of the color-unlabeled quotient** is
\[
\widetilde\chi(Y_{n,q})=-\frac1{q!}\sum_{f=0}^q\binom qf D_{q-f}\bigl(f-1+L_n(f)\bigr).
\]
Its growth has a sharp Euler-characteristic transition at five colors: for every fixed \(1\le q\le4\), the quantity \(\widetilde\chi(Y_{n,q})\) is bounded uniformly in \(n\); whereas for each fixed \(q\ge5\), with
\[
\rho_q=\frac{q-2+\sqrt{q(q-4)}}2>1,
\]
we have the genuine asymptotic
\[
\widetilde\chi(Y_{n,q})=\frac{(-1)^{n+1}}{q!}\rho_q^n(1+o(1))\qquad(n\to\infty).
\]
Consequently, for each fixed \(q\ge5\), the total **reduced rational Betti number** of the quotient obeys
\[
\sum_{j\ge0}\dim_{\mathbb Q}\widetilde H_j(Y_{n,q};\mathbb Q)\ \ge\ |\widetilde\chi(Y_{n,q})|\ =\ \frac{\rho_q^n}{q!}(1+o(1)).
\]
No assertion that rational Betti numbers are bounded for \(q\le4\) is made.

## Assumptions and scope
Here \(C_n\) is the simple cycle on vertices \(\mathbb Z/n\mathbb Z\), \(K_q\) the complete graph on \(\{1,\ldots,q\}\), and \(\square\) denotes **Cartesian**, not categorical, graph product. A face of \(X_{n,q}\) is a partial assignment of one of \(q\) colors to some cycle vertices, with unequal colors at adjacent assigned vertices. All group actions and quotients concern geometric realizations. The action is simplicial without inversions: a simplex has at most one color at each position, so no nontrivial permutation can move two vertices within the same simplex.

## Proof
**1. Signed face enumerator.** Let \(Z_{n,f}\) be the sum of \((-1)^{|F|}\) over all faces \(F\) of \(\operatorname{Ind}(C_n\square K_f)\), including the empty face, for positive \(f\). Encode each partial coloring by a circular word with states \(0,1,\ldots,f\), where \(0\) means uncolored. State \(b\) contributes weight \(w_b=1\) when \(b=0\), and \(-1\) otherwise; consecutive states are compatible unless they are the same nonzero color. The transfer matrix \(M_f\) has entries \((M_f)_{ab}=w_b\) for compatible \(a,b\), and zero otherwise. Since the word is cyclic, \(Z_{n,f}=\operatorname{tr}(M_f^n)\) for \(n\ge3\).

On the \((f-1)\)-dimensional color-sum-zero subspace, \(M_f\) acts as the identity. On the span of the empty state and the sum of all colored states, its matrix (in the ordered coordinates empty, uniform color) is
\[
\begin{pmatrix}1&-f\\1&1-f\end{pmatrix},
\]
which has trace \(2-f\) and determinant \(1\). Its eigenvalues solve \(\lambda^2+(f-2)\lambda+1=0\), hence its power traces equal \(L_n(f)\). Therefore \(Z_{n,f}=f-1+L_n(f)\). For the formal case \(f=0\), only the empty word remains, so \(Z_{n,0}=1\); the same expression evaluates to \(-1+2=1\) because \(L_n(0)=2\). Thus the formula holds for every \(f\ge0\).

**2. Equivariant Euler characteristic.** A permutation \(\sigma\in S_q\) has \(f\) fixed color labels. Every simplex invariant under \(\sigma\) must be fixed vertexwise: since each cycle position supplies at most one vertex, a color orbit of length greater than one cannot occur within an invariant simplex. Consequently, the fixed-point subcomplex of the geometric action is precisely \(X_{n,f}\). By the finite-group Euler-characteristic orbit formula (or Burnside applied to all faces in this no-inversions action),
\[
\widetilde\chi(Y_{n,q})=\frac1{q!}\sum_{\sigma\in S_q}\widetilde\chi(X_{n,f(\sigma)})
=-\frac1{q!}\sum_{\sigma\in S_q} Z_{n,f(\sigma)}.
\]
There are \(\binom qf D_{q-f}\) permutations with precisely \(f\) fixed labels. This proves the displayed finite exact formula. In the empty fixed subcomplex case \(f=0\), its ordinary Euler characteristic is zero and its reduced Euler characteristic is \(-1\), consistent with the empty-face convention; equivalently take the ordinary Euler averages first, then subtract one.

**3. Sharp exponential phase.** For \(0\le f\le4\), the two roots of \(\lambda^2+(f-2)\lambda+1\) have modulus one (a repeated unit root at the boundary), so \(|L_n(f)|\le2\). Thus at fixed \(q\le4\) every summand in the finite formula stays bounded uniformly in \(n\).

When \(f\ge5\), the roots are negative real reciprocals, with absolute values \(\rho_f>1\) and \(\rho_f^{-1}\). The function \(\rho_f\) is strictly increasing for integers \(f\ge5\). The identity permutation in \(S_q\) has \(f=q\); any nonidentity permutation has at most \(q-2\) fixed labels. Hence for fixed \(q\ge5\), the identity's \((-\rho_q)^n\) contribution strictly dominates all other permutation contributions, which are \(o(\rho_q^n)\). The other root of the identity also contributes only \(o(\rho_q^n)\), proving the stated asymptotic and its sign. Finally the alternating sum defining reduced Euler characteristic is bounded in absolute value by the sum of reduced Betti numbers over \(\mathbb Q\), establishing the homological lower bound.

## Verification
The included executable `verify.py` provides two independent finite exact checks: a recurrence/permutation-fixed-point computation of the predicted quotient Euler characteristic and an independent enumeration of canonical color-unlabeled partial assignments; it compares both for \(1\le q\le8\), \(3\le n\le9\). Separately, the labeled signed-face count is enumerated directly for \(1\le q\le5\), \(3\le n\le6\). All 76 comparisons passed. These computations check cases only; the proof above establishes the unbounded assertion.

## Relationship to prior work
Ayzenberg–Khoroshavkina [1], first public 9 February 2026, study homotopy of generalized simplicial inflations and finite étale spaces, motivating the investigation of nondegenerate maps from partial-assignment complexes to simplices. The assignment map of \(X_{n,q}\) supplies a natural nondegenerate example when \(q\ge3\), but their flabby-sheaf wedge theorem does not calculate this quotient's Euler characteristic or its color-invariant rational homology. Carnero Bravo [2] studies independence complexes of graph products, especially path categorical and strong products, not the family of Cartesian cycle–clique products nor its color-permutation quotient. The transfer-matrix and group-Euler tools themselves are standard; the claimed new content is the exact all-parameter quotient formula and its five-color exponential topology transition, not those tools.

## Limitations
The result proves Euler characteristics and an exponential **lower bound** on total reduced rational Betti numbers for \(q\ge5\); it does not determine individual homology groups, torsion, exact homotopy types, or whether total Betti numbers are bounded for \(q\le4\). Color unlabeled quotients are topological orbit spaces, not naive simplicial quotients identifying vertex colors. Although direct known-result comparisons were conducted, unindexed equivalent evaluations of this precise quotient remain a residual originality risk.

## References
1. A. Ayzenberg and N. Khoroshavkina, *Homotopy types of finite étale spaces and generalized inflations*, arXiv:2602.08694v1 (9 February 2026), https://arxiv.org/html/2602.08694v1.
2. A. Carnero Bravo, *On independence complexes of graph products*, arXiv:2505.06457v1 (9 May 2025), https://arxiv.org/html/2505.06457v1.
