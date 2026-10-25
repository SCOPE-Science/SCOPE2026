# Sharp endpoint Hodge norms and separated phase boundaries for clique-augmented bicliques

## Finding

For integers \(n\ge2\), \(k\ge3\), and \(m\ge k+1\), form the unweighted graph \(G_{m,n,k}\) by adding every edge of a \(k\)-vertex clique within one \(m\)-vertex part of \(K_{m,n}\). Put \(p=m-k\). On the real edge space, let \(Q\) be the Euclidean-orthogonal cut projection and \(P=I-Q\) the cycle projection. Define

\[
q_0=3-\frac2m-\frac2n+\frac2{mn},\qquad
z_0=\frac{4(m-1)(n-1)}{mn}.
\]

Define the following exact rational corrections:

\[
\Delta_Q=\begin{cases}
-\dfrac{(k-1)(n-2)}{n(n+k)},&p\le n,\\[2mm]
\dfrac{(k-1)[np-k(n-2)-2n(n-1)]}{n(n+k)m},&p\ge n,
\end{cases}
\]

\[
\Delta_P=\begin{cases}
-\dfrac{(k-1)(n-4)}{n(n+k)},&p\le n,\\[2mm]
\dfrac{(k-1)[(n+2)p-k(n-4)-2n(n-1)]}{n(n+k)m},&p\ge n.
\end{cases}
\]

The two branches agree at \(p=n\). The exact endpoint norms are

\[
\boxed{\|Q\|_{1\to1}=\|Q\|_{\infty\to\infty}=q_0+\max\{0,\Delta_Q\}},
\]

\[
\boxed{\|P\|_{1\to1}=\|P\|_{\infty\to\infty}=z_0+\max\{0,\Delta_P\}}.
\]

For every \(n\ge5\), put

\[
T_P=\frac{k(n-4)+2n(n-1)}{n+2},\qquad
T_Q=\frac{k(n-2)+2n(n-1)}n.
\]

Then \(n<T_P<T_Q\), with exact gap

\[
T_Q-T_P=\frac{4(k+n)(n-1)}{n(n+2)}>3.
\]

For \(p<T_P\) the two maxima occur only on edges from the \(p\) independent vertices to the opposite part; for \(T_P<p<T_Q\) the cut maximum occurs only on those edges while the cycle maximum occurs only on clique-to-opposite-part edges; and for \(p>T_Q\) both maxima occur only on clique-to-opposite-part edges. At equality with either threshold the corresponding two classes tie. Thus the opposite-maximizer regime contains at least one integer \(p\) for every \(k\ge3,n\ge5\).

Both families have sharp, unattained universal upper bounds:

\[
\boxed{\sup_{m,n,k}\|Q\|=4,\qquad \sup_{m,n,k}\|P\|=5.}
\]

The suprema range over exactly the stated integer domain. For instance \(n=t\), \(k=t^2\), \(p=t^4\) tend to both bounds as \(t\to\infty\). For \((m,n,k)=(10,5,3)\), the cut maximum is \(61/25\) on independent-part edges, whereas the cycle maximum is \(291/100\) on clique-to-opposite-part edges.

## Assumptions and scope

All edges have unit conductance and an arbitrary orientation. The first part consists of a clique \(C\) of size \(k\) and an independent set \(U\) of size \(p=m-k\), with no edges between \(C\) and \(U\). The opposite independent part \(B\) has size \(n\); every vertex of \(B\) is adjacent to every vertex of \(C\cup U\). There are exactly three nonempty edge orbits: \(CC\), \(CB\), and \(UB\). No assertion concerns minimum norms over all nonorthogonal projections.

Let \(D\) be the oriented incidence matrix, \(L=DD^{\mathsf T}\), and \(L^+\) its Moore–Penrose inverse. Then \(Q=D^{\mathsf T}L^+D\). For an edge \(e=(x,y)\), any potential \(v\) satisfying \(Lv=\delta_x-\delta_y\) gives its cut-projection column as the oriented edge differences of \(v\). Its absolute column sum is the total absolute electrical current; its diagonal entry is \(v_x-v_y\). Consequently the corresponding cycle-projection column sum is \(1+S_e-2(v_x-v_y)\), with \(S_e\) the cut-column sum. Symmetry of \(Q\) and \(P\) makes their \(\ell_1\) and \(\ell_\infty\) operator norms equal.

## Proof

We explicitly solve the Laplacian for one edge in each orbit; additive constants in potentials are immaterial.

**A clique edge.** For \(e=(c_1,c_2)\) in \(CC\), set \(v(c_1)=1/(n+k)\), \(v(c_2)=-1/(n+k)\), and all other potentials to zero. Direct substitution at every vertex gives \(Lv=\delta_{c_1}-\delta_{c_2}\). There are \(2(n+k-1)\) units of current magnitude \(1/(n+k)\), counting the distinguished edge with its doubled potential drop. More precisely,

\[
S_{CC}=2-\frac2{n+k},\qquad Z_{CC}=3-\frac6{n+k}.
\]

**An edge from the unmodified vertices.** For \(e=(u_1,b_1)\) in \(UB\), set

\[
v(u_1)=\frac1n,\quad v(b_1)=-\frac{n-1}{mn},\quad
v(b)=\frac1{mn}\ (b\ne b_1),
\]

and set all other vertex potentials to zero. The Laplacian equation holds at \(u_1\), \(b_1\), all other vertices of \(B\), and all remaining vertices separately. These currents are exactly the single-edge currents of \(K_{m,n}\). Hence

\[
S_{UB}=q_0,\quad R_{UB}=\frac{m+n-1}{mn},\quad Z_{UB}=1+q_0-2R_{UB}=z_0.
\]

**A clique-to-opposite-part edge.** For \(e=(c_1,b_1)\) in \(CB\), take

\[
\begin{array}{c|c}
\text{vertex class}&\text{potential}\\\hline
c_1&(n+1)/(n(n+k))\\
C\setminus\{c_1\}&1/(n(n+k))\\
U&0\\
b_1&-(n-1)/(mn)\\
B\setminus\{b_1\}&1/(mn)
\end{array}
\]

For example, the total clique potential is \(1/n\), so the Laplacian equation at \(b_1\) reads \(m[-(n-1)/(mn)]-1/n=-1\). At \(c_1\), its \(n\) opposite-part edges and \(k-1\) clique edges give total divergence \(1\). At every other vertex the divergence is \(0\). Thus the displayed potential is exact. Its distinguished-edge drop is

\[
R_{CB}=\frac{n+1}{n(n+k)}+\frac{n-1}{mn}.
\]

All positive current magnitudes follow directly from the table except the \((k-1)(n-1)\) edges between \(C\setminus\{c_1\}\) and \(B\setminus\{b_1\}\). Their signed drop is

\[
\frac1{n(n+k)}-\frac1{mn}
=\frac{p-n}{mn(n+k)}.
\]

For clarity the complete absolute sum before simplification is

\[
\begin{aligned}
S_{CB}={}&\frac{k-1}{n+k}+R_{CB}
+(n-1)\left(\frac{n+1}{n(n+k)}-\frac1{mn}\right)\\
&+(k-1)\left(\frac1{n(n+k)}+\frac{n-1}{mn}\right)
+\frac{(k-1)(n-1)|p-n|}{mn(n+k)}
+\frac{2p(n-1)}{mn}.
\end{aligned}
\]

Subtracting \(S_{UB}\) and resolving the sole absolute value at \(p=n\) yields exactly \(S_{CB}-q_0=\Delta_Q\). The corresponding complementary sum is \(Z_{CB}=1+S_{CB}-2R_{CB}\), whence \(Z_{CB}-z_0=\Delta_P\).

**No clique edge can maximize.** If \(p\le n\), direct subtraction gives

\[
S_{CB}-S_{CC}=\frac{(n-1)[n(m-2)+2p]}{mn(n+k)}>0,
\]

\[
Z_{CB}-Z_{CC}=\frac{(n-1)[n(m-4)+4p]}{mn(n+k)}>0.
\]

If \(p\ge n\), the corresponding numerators, after the common positive denominator \(mn(n+k)/(n-1)\), are

\[
m(n+2k)-2k(k+n),
\quad m(n+2k+2)-2k(k+n+1)-2n.
\]

Both are positive because \(m=k+p\ge k+n\): the first is at least \(n(k+n)\), and the second is at least \(n(k+n)\). Therefore only \(CB\) and \(UB\) can maximize either norm, proving the stated maximum formulas.

**Separated transitions.** In the branch \(p\ge n\), the signs of \(\Delta_Q\) and \(\Delta_P\) are those of \(p-T_Q\) and \(p-T_P\), respectively. For \(n\ge5\), both corrections are negative in the branch \(p\le n\). Subtraction gives the exact positive gap above. Because the gap exceeds three, a strictly intermediate integer \(p\) exists for every allowed \(n,k\). The named strict edge-orbit regimes and tie boundaries follow.

**Sharp family-wide bounds.** Since \(q_0<3\), \(\Delta_Q\le0\) for \(p\le n\), and \(\Delta_Q<(k-1)/(n+k)<1\) for \(p>n\), every cut norm is strictly below \(4\). For the cycle norm, \(z_0<4(n-1)/n\). If \(p\le n\) and \(n\ge4\), then \(\Delta_P\le0\); if \(n=2,3\), then \(\Delta_P<(4-n)/n\) and the norm is below \(3\). If \(p>n\) and \(n\ge4\), then \(\Delta_P<(n+2)/n\), so the norm is below \(5-2/n\). For \(p>n\), \(n=3\) gives \(\Delta_P<5/3\) and norm below \(13/3\), while \(n=2\) gives \(\Delta_P<2\) and norm below \(4\). Finally \(n=t\), \(k=t^2\), \(p=t^4\) make \(q_0\to3\), \(z_0\to4\), and both corrections tend to \(1\). Thus the bounds are sharp but never attained.

## Verification

Run `python3 check_clique_bipartite.py` from the directory containing this document. The checker uses only Python's standard-library exact fractions; it tests the displayed Laplacian solutions and all three edge-orbit column sums on 5,712 test orbits, plus 23 independent grounded-Laplacian matrix inversions encompassing 1,013 columns. It checks all maxima against the closed formulas and separately tests sharp-limit parameter sequences. The output is `CLIQUE_AUGMENTED_BICLIQUE_EXACT_OK orbit_cases=5712 orbit_edges=882504 grounded_graphs=23 grounded_columns=1013 sharp_limit_samples=3`. The mathematical proof above, not this finite sampling, establishes the result for all parameters.

## Relationship to prior work

Dilworth, Kutzarova, and Ostrovskii (2023) study invariant and minimal graph-cycle projections, concentrating on discrete tori and Hamming graphs; their reported Hamming-cube calculation does not directly cover the present asymmetric clique perturbations. Earlier electrical-network work of Azimi, Bapat, and Farrokhi D. G. (2021) gives pseudoinverse and effective-resistance methods for clique or independent blowups of trees. The present graphs are mixed clique–independent blowups of a three-vertex path, and the result additionally evaluates **absolute-current norms** and their different maximizing-edge thresholds. A separate study of mixed clique/independent blowups with uniform fiber sizes (Sun, Yang, and Xu, 2024) also provides resistance methods, but its cited construction does not furnish the present unequal-size endpoint norm and maximizing-orbit formulas. Those resistance studies are potential sources of computational ingredients, not evidence of uniqueness of this classification.

## Limitations

Only canonical orthogonal projections on finite, unweighted, real graph edge spaces are treated. The result does not determine minimum norms of arbitrary nonorthogonal projections, weighted versions, or intermediate \(\ell_p\) norms. The closest resistance literature may contain an equivalent unpublished or differently stated absolute-current calculation; its complete contents were not all accessible. Neither numerical testing nor nonappearance in searched sources independently certifies novelty.

## References

1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582 (first public version 21 May 2023), https://arxiv.org/abs/2305.12582.
2. A. Azimi, R. B. Bapat, M. Farrokhi D. G., *Resistance distance of blowups of trees*, Discrete Mathematics 344 (2021), 112387, doi:10.1016/j.disc.2021.112387.
3. W. Sun, Y. Yang, S.-J. Xu, *Resistance distance and Kirchhoff index of unbalanced blowups of graphs*, Discrete Mathematics (2024), doi:10.1016/j.disc.2024.114327.
