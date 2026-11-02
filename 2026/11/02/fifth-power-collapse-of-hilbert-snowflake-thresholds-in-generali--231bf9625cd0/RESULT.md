# Fifth-power collapse of Hilbert snowflake thresholds in generalized-hexagon incidence metrics

## Finding

Let \(q\ge100\) be an integer for which a finite generalized hexagon of order \((q,q)\) exists. Let \(X_q\) be its point–line incidence graph with unit-edge shortest-path distance \(d\). Define the supremal negative-type exponent
\[
\wp(X_q)=\sup\{p\ge0:\ \sum_{x,y\in X_q}a_xa_y d(x,y)^p\le0\ \text{whenever}\ \sum_xa_x=0\},
\]
with the usual convention that \(d(x,x)^0=0\) and \(d(x,y)^0=1\) for distinct vertices.

Put
\[
F_q(p)=-(q+1)+(q+1)q2^p-(q+1)q^2 3^p+(q+1)q^3 4^p-(q+1)q^4 5^p+q^5 6^p.
\]
There is exactly one root \(\alpha_q\) of \(F_q\) in \((0,10/q^5)\), and
\[
\boxed{\wp(X_q)=\alpha_q.}
\]
For \(0\le p<\alpha_q\) the metric has **strict** \(p\)-negative type. At \(p=\alpha_q\), the sole zero-sum equality direction is the vector constant \(+1\) on the points and \(-1\) on the lines, up to scalar. Negative type fails for every \(p>\alpha_q\).

The threshold is independent of the isomorphism type of the generalized hexagon, and has the **two-term asymptotic expansion**
\[
\boxed{
\alpha_q=
\frac{1}{q^5\log(6/5)}+
\frac{\log(5/4)}{q^6\log^2(6/5)}+
O(q^{-7})
}\quad(q\longrightarrow\infty).
\]
In particular, \(q^5\wp(X_q)\to1/\log(6/5)\). By Schoenberg's theorem, the metric \(d^{p/2}\) embeds isometrically into a real Hilbert space exactly for \(0\le p\le\alpha_q\). Its minimum affine Euclidean embedding dimension is \(|X_q|-1\) below the threshold and \(|X_q|-2\) at the threshold.

## Assumptions and scope

A finite generalized hexagon of order \((q,q)\) has \(q+1\) points per line and \(q+1\) lines per point; its connected incidence graph is bipartite, distance-regular, of girth twelve and diameter six. Its intersection array is
\[
\{q+1,q,q,q,q,q;\ 1,1,1,1,1,q+1\}.
\]
The graph has \(2(q^5+q^4+q^3+q^2+q+1)\) vertices. The claim applies to **every** such graph if \(q\ge100\), including the known split-Cayley-hexagon examples at prime-power orders. The condition \(q\ge100\) is an explicit sufficient bound for the uniform estimates below; it is not asserted to be the sharp first valid order. Smaller orders are outside the proved universal theorem.

For any real \(p\ge0\), the distance-power matrix is \(D_p=(d(x,y)^p)_{x,y}\), with zero diagonal. A finite metric has \(p\)-negative type exactly when \(D_p\) is negative semidefinite on the real zero-sum subspace; strictness means negative definiteness there. This is not a statement about \(\ell_p\) embeddings or the geometric-sum \(q\)-distance matrix.

## Proof

**1. Exact spectral reduction.** Write \(A_j\) for the distance-\(j\) adjacency matrices and \(A=A_1\), with \(A_0=I\). The intersection array gives
\[
AA_1=A_2+(q+1)A_0,\qquad
AA_j=A_{j+1}+qA_{j-1}\quad(2\le j\le4),\qquad
AA_5=(q+1)A_6+qA_4,\quad AA_6=qA_5.
\]
Hence \(A_j=P_j(A)\), where
\[
\begin{aligned}
P_0(t)&=1,\quad P_1(t)=t,\quad P_2(t)=t^2-q-1,\\
P_3(t)&=t(t^2-2q-1),\\
P_4(t)&=t^4-(3q+1)t^2+q^2+q,\\
P_5(t)&=t\bigl(t^4-(4q+1)t^2+3q^2+2q\bigr),\\
P_6(t)&=\frac{t^6-(5q+1)t^4+(6q^2+3q)t^2-q^3-q^2}{q+1}.
\end{aligned}
\]
The terminal recurrence factors as
\[
tP_6(t)-qP_5(t)
=-\frac{t(q-t^2)(3q-t^2)(q-t+1)(q+t+1)}{q+1}.
\]
A distance-regular graph of diameter six has seven distinct adjacency eigenvalues. They are therefore exactly
\[
q+1,\quad -(q+1),\quad 0,\quad \pm\sqrt q,\quad\pm\sqrt{3q}.
\]
The eigenvalue \(-(q+1)\) is simple because the graph is connected, bipartite and \((q+1)\)-regular. Its eigenvector \(u\) takes value \(+1\) on every point and \(-1\) on every line. At this eigenvalue,
\[
P_j(-(q+1))=(-1)^j k_j,
\quad k_j=(q+1)q^{j-1}\ (1\le j\le5),\quad k_6=q^5.
\]
Thus the eigenvalue of \(D_p=\sum_{j=1}^6 j^p A_j\) on \(u\) is exactly \(F_q(p)\). The other five nonconstant adjacency eigenvalues \(t\in\{0,\pm\sqrt q,\pm\sqrt{3q}\}\) carry powered-distance eigenvalue
\[
\Lambda_q(p,t)=\sum_{j=1}^6 j^pP_j(t).
\]
All eigenspaces except the constant one lie in the zero-sum subspace, including \(u\), and \(\Lambda_q(0,t)=F_q(0)=-1\). The latter identity follows from \(A_0+\cdots+A_6=J\), the all-ones matrix.

**2. Existence and isolation of the bipartition zero.** Differentiating at zero and collecting powers of \(q\) gives
\[
\begin{aligned}
F_q'(0)
={}&q^5\log(6/5)-q^4\log(5/4)
+q^3\log(4/3)\\
&-q^2\log(3/2)+q\log2.
\end{aligned}
\]
In particular \(F_q'(0)>0.179q^5\) for every \(q\ge100\). The sum of the positive shell sizes \(k_1+\cdots+k_6\) is less than \(2.1q^5\). Consequently, throughout \(0\le p\le10q^{-5}\),
\[
|F_q''(p)|\le (k_1+\cdots+k_6)6^p(\log6)^2<7q^5.
\]
It follows that \(F_q'(p)>0.179q^5-70>0\), so \(F_q\) is strictly increasing on this interval. Its endpoint values obey
\[
F_q(0)=-1,\qquad
F_q(10q^{-5})\ge-1+1.79-350q^{-5}>0.
\]
Hence \(F_q\) has a unique root \(\alpha_q\in(0,10q^{-5})\), with a simple sign crossing there.

**3. No competing eigenspace reaches zero first.** Fix \(t\in\{0,\pm\sqrt q,\pm\sqrt{3q}\}\). Because \(|t|\le\sqrt{3q}\), the displayed polynomials give, for \(q\ge100\),
\[
\begin{aligned}
|P_1(t)|&\le2q^{1/2},\quad |P_2(t)|\le4q,\quad |P_3(t)|\le12q^{3/2},\\
|P_4(t)|&\le20q^2,\quad |P_5(t)|\le58q^{5/2},\quad |P_6(t)|\le103q^2.
\end{aligned}
\]
In particular \(\sum_{j=1}^6|P_j(t)|\le199q^{5/2}\). Since \(\sum_{j=1}^6P_j(t)=-1\),
\[
\begin{aligned}
|\Lambda_q(p,t)+1|
&\le\sum_{j=2}^6(j^p-1)|P_j(t)|\\
&\le p(\log6)6^p\sum_{j=1}^6|P_j(t)|\\
&\le4000q^{-5/2}<0.04
\end{aligned}
\]
for every \(0\le p\le10q^{-5}\) and \(q\ge100\). Thus all five competing nonconstant spectral values are **strictly negative** throughout the entire interval. At \(p=\alpha_q\) only the one-dimensional bipartition eigenspace has eigenvalue zero. This proves strict negative type below \(\alpha_q\) and nonstrict negative type at \(\alpha_q\). For larger \(p\), negative type cannot reappear: Schoenberg's monotonicity principle says that \(p\)-negative type implies \(r\)-negative type for each \(0\le r\le p\). Since some exponent immediately above \(\alpha_q\) fails because \(F_q\) is positive, all larger exponents fail as well.

**4. Two-term asymptotic.** Put \(L=\log(6/5)\) and \(B=\log(5/4)\). The derivative formula is
\[
F'_q(0)=q^5\bigl(L-B/q+O(q^{-2})\bigr).
\]
The root belongs to \((0,10q^{-5})\) and \(F''_q=O(q^5)\) there. Taylor's theorem therefore gives
\[
0=F_q(\alpha_q)=-1+\alpha_q F'_q(0)+O(q^5\alpha_q^2),
\quad\text{hence}\quad
\alpha_q=\frac1{F'_q(0)}+O(q^{-10}).
\]
Expanding the reciprocal proves
\[
\alpha_q=\frac1{Lq^5}+\frac{B}{L^2q^6}+O(q^{-7}).
\]
The error term is uniform over all incidence graphs of the stated order because the proof uses only their common intersection array.

**5. Embedding dimension.** Schoenberg's finite-metric criterion identifies \(-\tfrac12CD_pC\) as the centered Gram matrix, where \(C=I-\frac1{|X_q|}\mathbf1\mathbf1^{\mathsf T}\) is the orthogonal centering projection. At \(p<\alpha_q\) the powered-distance matrix is strictly negative on the \(|X_q|-1\) dimensional zero-sum subspace, so this Gram matrix has rank \(|X_q|-1\). At the critical value it loses exactly the one-dimensional bipartition direction, giving rank \(|X_q|-2\). Gram rank is the minimum affine embedding dimension. This proves the final assertion.

## Verification

The accompanying standalone `verify.py` uses exact rational polynomial arithmetic to check the distance-polynomial recurrence, the terminal factorization, shell eigenvalues, and the sum-of-distance-polynomials identity at 128 sample orders. Separately, 75-digit decimal arithmetic tests the small-order examples and several orders in the rigorously controlled large-order regime, including the asserted asymptotic approximation. Run `python3 verify.py` in the directory containing the two files.

The checker reports `CHECK_OK exact_polynomial_identities= 512 finite_spectral_checks= 130 uniform_proof_applies_q>=100`. These finite checks **do not establish** the infinite quantified theorem. That rests on the explicit uniform bounds in Steps 2 and 3. The supplemental smaller-order tests are illustrative and do not extend the theorem's stated range.

## Relationship to prior work

Van Dam and Jazaeri (first posted 2018-08-04) describe precisely the distance-regular incidence graphs of generalized hexagons and study their Cayley-graph properties, not negative type. Robertson (first posted 2023-09-27) develops negative-type criteria for Hilbert embeddings and explicit examples for complete bipartite graphs and Hamming cubes, not generalized-hexagon incidence metrics. Koolen, Abdullah, Gebremichel and Hayat (first posted 2023-05-24) treat generalized \(q\)-distance matrices with entries of geometric-sum form, not powers \(d^p\); their general spectral framework does not supply the threshold, fifth-power asymptotic, or equality space here. Generalized quadrangles and symmetric-design incidence graphs are geometrically distinct: their diameter-four and diameter-three powered-distance calculations do not imply the diameter-six hexagon result by parameter substitution.

The proof uses standard distance-regular graph and Schoenberg machinery; the exact hexagon threshold in the stated range, the two-term sharp asymptotics, and the unique critical eigendirection are the present specific conclusions. Searches cannot establish absolute historical priority; an older equivalent computation under association-scheme or generalized-roundness terminology remains possible.

## Limitations

The theorem proves the universal formula for orders \(q\ge100\) admitting such generalized hexagons, not a theorem for every smaller order. The numerical checks for smaller \(q\) are not a substitute. No claim is made for unequal-order polygons, generalized octagons, edge-weighted incidence metrics, or the exact distortions of nonsnowflaked embeddings. The sufficiency cutoff \(100\) is not asserted sharp. An independent mathematical audit and independent historical-priority certification have not been performed.

## References

1. E. R. van Dam and M. Jazaeri, *Distance-regular Cayley graphs with small valency*, arXiv:1808.01428v1 (2018-08-04), especially Section 3.7 and incidence-graph tables. https://arxiv.org/abs/1808.01428
2. G. Robertson, *Negative type and bi-lipschitz embeddings into Hilbert space*, arXiv:2309.16070v1 (2023-09-27), especially Sections 2 and 4. https://arxiv.org/abs/2309.16070
3. J. H. Koolen, M. Abdullah, B. Gebremichel and S. Hayat, *Distance-regular graphs with exactly one positive q-distance eigenvalue*, arXiv:2305.14636v1 (2023-05-24), especially Sections 2.4, 3.1 and 4. https://arxiv.org/abs/2305.14636
4. I. J. Schoenberg, *Metric spaces and positive definite functions*, Transactions of the American Mathematical Society 44 (1938), 522–536 (classical metric negative-type criterion).
