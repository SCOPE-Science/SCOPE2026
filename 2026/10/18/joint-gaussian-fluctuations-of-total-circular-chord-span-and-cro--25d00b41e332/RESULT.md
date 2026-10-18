# Joint Gaussian fluctuations of total circular chord span and crossings

## Finding

Let \(n\ge2\) and choose uniformly a perfect matching of the \(2n\) cyclically ordered labels \(0,1,\ldots,2n-1\). For a chord \(e=\{a,b\}\), where \(a<b\), define its **shorter-arc span** by
\[
\ell(e)=\min\{b-a-1,\,2n-b+a-1\}.
\]
Let \(L_n=\sum_{e}\ell(e)\) and let \(X_n\) be the number of unordered crossing pairs of chords. The complete finite-sample second moments are
\[
\begin{aligned}
\mathbb E L_n&=\frac{n(n-1)^2}{2n-1},&
\mathbb E X_n&=\frac{n(n-1)}6,\\
\operatorname{Var}(L_n)&=\frac{2n^2(n-1)^2(n^2-n+1)}{3(2n-3)(2n-1)^2},&
\operatorname{Var}(X_n)&=\frac{n(n-1)(n+3)}{45},\\
\operatorname{Cov}(L_n,X_n)&=\frac{n^3(n-1)^2}{6(2n-3)(2n-1)}.
\end{aligned}
\]
The crossing-count variance is already known; the claim of interest is the **joint** span–crossing fluctuation law:
\[
\frac1{n^{3/2}}\begin{pmatrix}L_n-\mathbb E L_n\\X_n-\mathbb E X_n\end{pmatrix}
\ \xrightarrow{\mathrm d}\ N_2\!\left(\begin{pmatrix}0\\0\end{pmatrix},
\begin{pmatrix}1/12&1/24\\1/24&1/45\end{pmatrix}\right).
\]
The covariance matrix is positive definite, with determinant \(1/8640\). Its correlation is \(\sqrt{15}/4\); thus the optimal limiting linear predictor from span explains \(15/16\) of crossing-count fluctuation variance. Equivalently,
\[
\frac{X_n-\mathbb E X_n-\frac12(L_n-\mathbb E L_n)}{n^{3/2}}
\ \xrightarrow{\mathrm d}\ N(0,1/720).
\]
No claim is made that the finite covariance formulas alone are historically new.

## Assumptions and scope

The endpoints are fixed labeled points in cyclic order, the matching is uniform over all \((2n-1)!!\) pairings, and crossings mean geometric alternation of four endpoints. Span is the number of *other labeled endpoints* strictly between chord endpoints along the shorter arc, not Euclidean chord length. When arcs tie, the minimum is well defined. There is no continuum limit of prescribed physical chord lengths and no conditioning on the crossing count. All finite identities hold for each integer \(n\ge2\), and the weak convergence is as \(n\to\infty\).

## Proof

**1. Exact span moments.** Write \(w_{ab}=\min\{b-a-1,2n-b+a-1\}\) for each candidate edge \(\{a,b\}\), and \(J_{ab}\) for its matching indicator. Each edge occurs with probability \(1/(2n-1)\); two disjoint candidate edges occur jointly with probability \(1/((2n-1)(2n-3))\); intersecting candidate edges cannot both occur. Direct circular summation yields
\[
\sum_{a<b}w_{ab}=S_1=n(n-1)^2,\qquad
\sum_{a<b}w_{ab}^2=S_2=\frac{n(n-1)(2n^2-4n+3)}3,
\]
and the sum of weights of edges incident to any fixed vertex is \(d=(n-1)^2\). Consequently
\[
\mathbb E L_n=\frac{S_1}{2n-1},\qquad
\mathbb E L_n^2=\frac{S_2}{2n-1}
+\frac{S_1^2+S_2-2n d^2}{(2n-1)(2n-3)}.
\]
Subtracting the squared mean simplifies to the stated exact variance.

**2. Exact mixed covariance.** Fix label zero and write \(B\) for the span of its incident chord. The distribution is
\[
\Pr(B=k)=\frac2{2n-1}\quad(0\le k\le n-2),\qquad
\Pr(B=n-1)=\frac1{2n-1}.
\]
Conditional on this chord, the other \(n-1\) chords form a uniform matching on the remaining endpoints. Crossings among those remaining chords have conditional expected count \(\binom{n-1}{2}/3\). Among the remaining \(2n-2\) endpoints, the fixed chord separates \(k\) from \(2n-2-k\); the expected number of its crossing partners therefore is \(k(2n-2-k)/(2n-3)\). Thus
\[
\mathbb E[X_n\mid B=k]
=\frac13\binom{n-1}{2}+\frac{k(2n-2-k)}{2n-3}.
\]
Since summing span over all chords is half the sum of the spans incident to all endpoints, circular exchangeability gives \(\operatorname{Cov}(L_n,X_n)=n\operatorname{Cov}(B,X_n)\). Substitution of the displayed distribution of \(B\) gives exactly
\[
\operatorname{Cov}(L_n,X_n)=\frac{n^3(n-1)^2}{6(2n-3)(2n-1)}.
\]
The formula for \(\operatorname{Var}(X_n)\) is the established crossing variance of Flajolet and Noy; its normalization also follows from the independent-pair proof below.

**3. Independent-pair representation.** For each \(1\le i\le n\), independently sample \(A_i=(U_i,V_i)\) with \(U_i,V_i\) independent uniform on the unit circle. Ranking all \(2n\) sampled endpoints and connecting each sampled pair produces a uniform random matching of the ranks. Define \(Q_i=\min\{|U_i-V_i|,1-|U_i-V_i|\}\), using circular coordinates. The \(Q_i\) are independent uniform variables on \((0,1/2)\), with density \(2\).

Let \(I_i\) be the shorter open circular arc joining \(U_i\) and \(V_i\). Set \(K_i=\sum_{j\ne i}(\mathbf1\{U_j\in I_i\}+\mathbf1\{V_j\in I_i\})\). The actual rank-defined span of chord \(i\) equals \(\min(K_i,2n-2-K_i)\), whereas \(K_i\) is an oriented short-arc occupancy count. Consequently, defining
\[
L_n^*=\sum_{i=1}^n K_i=\sum_{1\le i<j\le n}h(A_i,A_j),
\]
where \(h(a,b)\) counts endpoints of \(b\) in the shorter arc of \(a\), plus endpoints of \(a\) in the shorter arc of \(b\), gives \(0\le L_n^*-L_n\). Rotational symmetry yields \(\mathbb E h(A_1,A_2)=1\), whence \(\mathbb E L_n^*=\binom n2\). Using the exact mean from Step 1 gives the **exact comparison error**
\[
\mathbb E|L_n^*-L_n|
=\binom n2-\frac{n(n-1)^2}{2n-1}
=\frac{n(n-1)}{2(2n-1)}=O(n).
\]
After centering, Markov's inequality implies that \(L_n\) and \(L_n^*\) have the same \(n^{3/2}\)-scale weak limit.

**4. Joint Hoeffding projections.** Let \(c(a,b)\) indicate that two sampled chords cross. Then \(X_n=\sum_{i<j}c(A_i,A_j)\) exactly. Given \(Q_1=q\), two independent endpoints of \(A_2\) lie on opposite sides of the short arc with probability \(2q(1-q)\), while their expected total number in that arc is \(2q\). By rotational symmetry, the expected count of endpoints of \(A_1\) in the random shorter arc of \(A_2\) is \(1/2\). Therefore
\[
\mathbb E[h(A_1,A_2)\mid Q_1=q]=2q+\tfrac12,
\qquad
\mathbb E[c(A_1,A_2)\mid Q_1=q]=2q(1-q).
\]
The unconditional kernel means are \(1\) and \(1/3\). The centered first-order projections are accordingly
\[
\psi_L(q)=2q-\tfrac12,\qquad
\psi_X(q)=2q(1-q)-\tfrac13.
\]
Direct integration against density \(2\) on \((0,1/2)\) yields
\[
\begin{aligned}
2\int_0^{1/2}\psi_L(q)^2\,dq&=\tfrac1{12},\\
2\int_0^{1/2}\psi_L(q)\psi_X(q)\,dq&=\tfrac1{24},\\
2\int_0^{1/2}\psi_X(q)^2\,dq&=\tfrac1{45}.
\end{aligned}
\]
Both kernels are bounded. For each, the order-two Hoeffding decomposition is \((n-1)\sum_{i=1}^n\psi(Q_i)\) plus a completely degenerate remainder of variance \(O(n^2)\). Dividing by \(n^{3/2}\), the remainder tends to zero in \(L^2\). The iid multivariate central limit theorem applied to the bounded centered vector \((\psi_L(Q_i),\psi_X(Q_i))\), followed by the span approximation in Step 3, proves the asserted bivariate normal limit.

The determinant, limiting correlation, regression coefficient and residual variance follow by direct arithmetic on the displayed covariance matrix.

## Verification

The standalone standard-library script `verify.py` exhaustively enumerates all \((2n-1)!!\) pairings for \(2\le n\le7\), a total of 146,598 perfect matchings. It checks five exact rational moment formulas (both means, both variances, and mixed covariance) at each size. It separately integrates the degree-two projection polynomials exactly over \((0,1/2)\) using rational arithmetic and checks the covariance determinant and residual variance. Execution command: `python verify.py`. Successful output ends with `VERIFY_OK`. This exhaustive finite check does not certify the infinite limit; Steps 3–4 prove that limit.

## Relationship to prior work

Acan's preprint studies this same uniform chord diagram and the shorter-arc span of a **single** chord, including its relationship to crossing degree. In particular, the conditional expected crossing degree in Step 2 follows from that existing local framework. Flajolet and Noy previously established the marginal crossing-count moments and asymptotic normality. The present statement is not the marginal central limit theorem, a conditional degree distribution, or the finite mixed moment considered alone: it concerns the **joint global** fluctuations of the sum of all spans and all crossings and their explicit nondegenerate covariance and regression residual. A joint result might be derivable from more general earlier U-statistic methods; those methods alone do not constitute an earlier published statement about this pair without a matching specialization.

## Limitations

The normal limit is asymptotic and does not supply a convergence rate. The statistic is discrete shorter-arc endpoint count, not physical chord length. Only two global statistics are covered, not the full degree sequence, conditioned chord ensembles or sparse-crossing ensembles. The source comparison does not establish historical uniqueness: a specialized earlier calculation or an implicit consequence of another multivariate matching-statistic theorem may exist. No independent mathematical audit has been performed.

## References

1. Hüseyin Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489v1 (publicly posted 2015-01-07), https://arxiv.org/abs/1501.01489 ; freely available preprint https://arxiv.org/pdf/1501.01489 .
2. Philippe Flajolet and Marc Noy, *Analytic Combinatorics of Chord Diagrams*, INRIA Research Report RR-3914 (March 2000), https://algo.inria.fr/flajolet/Publications/FlNo00.pdf .
3. Hüseyin Acan, *An Enumerative-Probabilistic Study of Chord Diagrams*, PhD thesis (2013), freely accessible via OhioLINK Electronic Theses and Dissertations Center.
