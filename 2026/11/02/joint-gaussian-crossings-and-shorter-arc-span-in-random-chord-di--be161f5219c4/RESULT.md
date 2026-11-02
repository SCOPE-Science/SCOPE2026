# Joint Gaussian crossings and shorter-arc span in random chord diagrams

## Finding

For the uniform random chord diagram with \(n\ge2\) chords, write \(X_n\) for the number of crossing *pairs* and \(T_n\) for the total shorter-arc length (the number of interior endpoints on the shorter arc, summed over all chords). Then
\[
\frac1{n^{3/2}}
\begin{pmatrix}X_n-\mathbb EX_n\\T_n-\mathbb ET_n\end{pmatrix}
\xrightarrow{d}
\mathcal N_2\!\left(\begin{pmatrix}0\\0\end{pmatrix},
\begin{pmatrix}1/45&1/24\\1/24&1/12\end{pmatrix}\right).
\]
The limit is nondegenerate. In particular the limiting correlation is \(\sqrt{15}/4\), while the proportion of crossing-count variance explained by the optimal linear regression on total shorter-arc length converges to \(15/16\). This is a joint fluctuation statement; no asymptotic independence is asserted.

## Assumptions and scope

The sample space consists of all \((2n-1)!!\) perfect matchings on cyclically ordered positions \(\{1,\dots,2n\}\), each equally likely. Two chords \(\{a,c\}\) and \(\{b,d\}\) cross if \(a<b<c<d\), after relabeling their four endpoints in ascending order. For an edge \(\{a,b\}\), \(a<b\), put \(\ell(a,b)=\min(b-a,2n-b+a)-1\); thus a chord between consecutive points has length zero and a diameter has length \(n-1\). Define \(T_n=\sum_{\{a,b\}\in M_n}\ell(a,b)\). All exact identities below hold for every integer \(n\ge2\); the Gaussian claim is as \(n\to\infty\).

The exact moments are
\[
\mathbb EX_n=\frac{n(n-1)}6,\quad
\operatorname{Var}(X_n)=\frac{n(n-1)(n+3)}{45},\quad
\mathbb ET_n=\frac{n(n-1)^2}{2n-1},
\]
\[
\operatorname{Var}(T_n)=\frac{2n^2(n-1)^2(n^2-n+1)}{3(2n-3)(2n-1)^2},\quad
\operatorname{Cov}(X_n,T_n)=\frac{n^3(n-1)^2}{6(2n-3)(2n-1)}.
\]
Consequently, the finite-size squared correlation and optimal slope for predicting \(X_n\) from \(T_n\) equal
\[
\rho_n^2=\frac{15n^3(n-1)}{8(n+3)(2n-3)(n^2-n+1)},\qquad
\beta_n=\frac{n(2n-1)}{4(n^2-n+1)}.
\]

## Proof

**1. Exact moments.** Put \(N=2n\), \(h_{ab}=\min(b-a,N-b+a)\) for \(a<b\), and \(L_n=T_n+n=\sum_{\{a,b\}\in M_n}h_{ab}\). Any specified edge occurs with probability \(p=(N-1)^{-1}\); two disjoint specified edges co-occur with probability \(q=((N-1)(N-3))^{-1}\), whereas incident distinct edges cannot co-occur. Every row of the symmetric weight matrix \((h_{ab})\) sums to \(n^2\). Its unordered-pair sums satisfy
\[
S_1=\sum_{a<b}h_{ab}=n^3,\quad
S_2=\sum_{a<b}h_{ab}^2=\frac{n^2(2n^2+1)}3,\quad
\sum_a\big(\sum_{b\ne a}h_{ab}\big)^2=2n^5.
\]
Expanding the variance in edge indicators (separating identical, disjoint and incident pairs) gives
\[
\operatorname{Var}(T_n)=(p+q)S_2-q(2n^5)+(q-p^2)S_1^2,
\]
which simplifies to the stated formula; \(\mathbb ET_n=pS_1-n\). For a specified chord of shorter *step* distance \(h\in\{1,\dots,n\}\), the expected crossing count conditional on its inclusion is
\[
\mathbb E[X_n\mid\{a,b\}\in M_n]
=\frac{(n-1)(n-2)}6+\frac{(h-1)(2n-h-1)}{2n-3}.
\]
Indeed, the first term counts crossings between remaining chords, and the second counts the two sides of the specified chord connected by another edge. Subtracting \(\mathbb EX_n\), multiplying by the weighted edge indicators and summing all \(a<b\) gives
\[
\operatorname{Cov}(X_n,T_n)=\frac1{2n-1}\sum_{a<b}(h_{ab}-1)
\left[\frac{(h_{ab}-1)(2n-h_{ab}-1)}{2n-3}-\frac{n-1}{3}\right]
=\frac{n^3(n-1)^2}{6(2n-3)(2n-1)}.
\]
The classical crossing variance can also be recovered by giving chords independent auxiliary labels and using a bounded order-two crossing kernel: distinct chord-pair indicators with no common label are independent, and the shared-label covariance is \(1/45\). This gives \(n(n-1)(n+3)/45\).

**2. Coupling to independent continuous chords.** Let \(Z_i=(U_i,V_i)\), \(1\le i\le n\), be independent, with all \(2n\) coordinates iid uniform on \([0,1]\). Ordering these \(2n\) almost surely distinct endpoints and pairing the two coordinates from each \(Z_i\) induces exactly the uniform matching above. Put \(s_i=|U_i-V_i|\), \(t_i=f(s_i)\), where \(f(s)=\min(s,1-s)\). The \(t_i\) are iid uniform on \([0,1/2]\), so \(\mathbb Et_i=1/4\) and \(\operatorname{Var}(t_i)=1/48\).

The crossing count is \(X_n=\sum_{i<j}k(Z_i,Z_j)\), with \(k\) the crossing indicator. Given \(Z_i\), its conditional expectation is \(p_i=2s_i(1-s_i)\). Set \(\xi_i=p_i-1/3\). The order-two Hoeffding projection yields
\[
X_n-\mathbb EX_n=(n-1)\sum_i\xi_i+R_n,
\quad \mathbb ER_n^2=O(n^2).
\]
Direct integration against the triangular density \(2(1-s)\) of \(s_i\) gives
\[
\operatorname{Var}(\xi_i)=1/45,\quad
\operatorname{Var}(2t_i)=1/12,\quad
\operatorname{Cov}(\xi_i,2t_i)=1/24.
\]

**3. Rank correction for the shorter-arc statistic.** Put \(N=2n\) and let \(F_N\) be the empirical CDF of all endpoint coordinates. Since its values at sample endpoints are their ranks divided by \(N\), the identity
\[
T_n+n=N\sum_i f\big(|F_N(U_i)-F_N(V_i)|\big)
\]
holds exactly. Write \(\Delta_N(x)=F_N(x)-x\) and \(D_N=\sup_x|\Delta_N(x)|\). The Dvoretzky–Kiefer–Wolfowitz bound implies \(D_N=O_p(N^{-1/2})\).

Define \(a(u,v)=f'(|u-v|)\operatorname{sgn}(u-v)\) away from the measure-zero line \(|u-v|=1/2\). By piecewise linearity of \(f\), the difference between \(T_n+n\) and \(N\sum_i t_i\) equals
\[
N\sum_i a(U_i,V_i)[\Delta_N(U_i)-\Delta_N(V_i)]+o_p(n^{3/2}).
\]
To justify the error explicitly, on \(D_N\le N^{-1/3}\) only chords with \(||U_i-V_i|-1/2|\le2N^{-1/3}\) can cross the cusp of \(f\). Their number is \(O_p(n^{2/3})\) by the iid chord lengths; their total contribution to the Taylor remainder is at most \(O_p(N\,N^{-1/3}n^{2/3})=O_p(n^{4/3})\). This event has probability tending to one.

The linear term can be written \(\sum_{i,j}H(Z_i,Z_j)\), where
\[
H((u,v),(p,q))=a(u,v)\big[
\mathbf1_{p\le u}-\mathbf1_{p\le v}
+\mathbf1_{q\le u}-\mathbf1_{q\le v}-2(u-v)\big].
\]
For independent inputs \(Z,Z'\), \(\mathbb E[H(Z,Z')\mid Z]=0\) because each endpoint of \(Z'\) is uniform. Crucially, the *reverse* conditional mean also vanishes. For any fixed \(x\), with \(g=f'\), define
\[
J(x)=\mathbb E\big[a(U,V)(\mathbf1_{x\le U}-\mathbf1_{x\le V})\big]
=2\int_0^x\int_x^1 g(v-u)\,dv\,du.
\]
Then \(J'(x)=2[f(1-x)-f(x)]=0\), while \(J(0)=0\). Moreover \(\mathbb E[a(U,V)(U-V)]=\mathbb E[s\,g(s)]=2\int_0^1 s(1-s)g(s)\,ds=0\), since \(g\) is antisymmetric about \(1/2\). Thus \(\mathbb E[H(Z,Z')\mid Z']=0\) identically. The off-diagonal double sum is therefore a bounded, doubly degenerate order-two statistic with second moment \(O(n^2)\); the diagonal contributes at most \(O(n)\). Therefore
\[
T_n+n=N\sum_i t_i+o_p(n^{3/2}),\qquad
\frac{T_n-\mathbb ET_n}{n^{3/2}}
=\frac2{\sqrt n}\sum_i(t_i-1/4)+o_p(1),
\]
where the exact mean above ensures that centering differs only by \(O(n)\).

**4. Joint limit and regression.** The iid bivariate central limit theorem applied to \((\xi_i,2(t_i-1/4))\), followed by the two negligible remainder estimates, gives the displayed covariance matrix. Its determinant is \(1/8640>0\). The exact moments yield the finite-size squared correlation and regression coefficient above; taking limits gives \(15/16\) and \(1/2\), respectively.

## Verification

Run `python verify.py` with Python 3 and its standard library, in the directory containing this document. It exhaustively generates all \(135135\) matchings at \(n=7\) (and every smaller size \(2\le n<7\)), independently reconstructs five exact moment identities and checks them as rational numbers. Further checks cover exact variance algebra, conditional-edge moments, and positivity for many finite sizes. A successful execution reports **13,895 exact assertions**, subject to running on a machine able to finish that enumeration. These checks validate finite instances and algebra, not the infinite-dimensional central-limit argument; that argument is proved above.

## Relationship to prior work

Acan [1, §2] introduced exactly this shorter-arc length and derived conditional crossing-degree facts; these are **not** new claims here. Flajolet–Noy [2] gave the univariate crossing-count central limit theorem, subsequently quantified by Paguyo [3, §2]; the univariate variance is also known. Existing covariance computations for higher crossing-clique counts against total chord length and the joint crossing/nesting Gaussian limit concern **different statistics or weaker consequences**. The assessed additional result is joint Gaussian fluctuation of crossing-pair count with total shorter-arc span, including the reverse-degeneracy cancellation and its \(15/16\) regression limit. Neither [1] nor [3] gives this two-coordinate limit in their inspected relevant sections.

## Limitations

The result is asymptotic only in the *joint distribution* statement; it gives no quantitative bivariate normal-approximation rate or non-Gaussian moderate deviations. No independence claim holds: the limiting correlation is large and positive. It does not claim novelty of the component moments, the single-statistic central limit theorem, or Acan's chord-length definition. A specialized equivalent statement elsewhere in the extensive matching literature could alter historical priority; no independent audit has been performed.

## References

[1] H. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489v1, 7 January 2015, https://arxiv.org/html/1501.01489v1 (especially §§1–2).

[2] P. Flajolet and M. Noy, *Analytic combinatorics of chord diagrams*, 2000; crossing-count central limit theorem, as cited in [1, §1] and [3, §1].

[3] J. E. Paguyo, *Convergence rates of limit theorems in random chord diagrams*, arXiv:2104.01134v1, 2 April 2021, https://arxiv.org/html/2104.01134v2 (especially §§1–2).
