# Shared-Gamma Dirichlet correlation: sharp concentration endpoints and categorical coupling

## Finding

**Theorem.** Fix an integer \(d\ge2\), a strictly positive probability vector \(\mu=(\mu_1,\ldots,\mu_d)\), a sharing fraction \(s\in(0,1)\), and a concentration \(c>0\). Let the \(3d\) random variables \(A_i,B_i,D_i\) be mutually independent, with common unit scale and shapes
\[
 A_i,B_i\sim\operatorname{Gamma}((1-s)c\mu_i,1),\qquad
 D_i\sim\operatorname{Gamma}(sc\mu_i,1).
\]
Define \(X_i=(A_i+D_i)/\sum_j(A_j+D_j)\) and \(Y_i=(B_i+D_i)/\sum_j(B_j+D_j)\). Both marginals have law \(\operatorname{Dirichlet}(c\mu)\). Set \(T=\sum_iD_i\), \(U=\sum_iA_i\), \(V=\sum_iB_i\), and \(R=T/(T+U)\), \(S=T/(T+V)\). Then
\[
 \operatorname{Cov}(X,Y)=\rho(s,c)\operatorname{Cov}(X),\qquad
 \rho(s,c)=\frac{c+1}{sc+1}\mathbb E[RS].
\]
Thus \(\operatorname{Corr}(X_i,Y_i)=\rho(s,c)\) for every coordinate. For different coordinates, the cross-correlation is
\[
 \operatorname{Corr}(X_i,Y_j)=-\rho(s,c)
 \sqrt{\frac{\mu_i\mu_j}{(1-\mu_i)(1-\mu_j)}}\qquad(i\ne j).
\]
For all finite positive concentrations there are strict bounds and an exact difference identity:
\[
 \frac{s^2(c+1)}{sc+1}<\rho(s,c)<s,\qquad
 s-\rho(s,c)=\frac{c+1}{2(sc+1)}\mathbb E[(R-S)^2]>0.
\]
The two sharp concentration endpoints are
\[
 \lim_{c\downarrow0}\rho(s,c)=\frac{s}{2-s},\qquad
 \lim_{c\to\infty}\rho(s,c)=s.
\]
The first endpoint holds with a **joint distributional limit**. As \(c\downarrow0\) with \(s,\mu\) fixed, \((X,Y)\) converges weakly to \((e_I,e_J)\), where \(e_i\) denotes the \(i\)-th vertex of the simplex and
\[
 \Pr(I=i,J=j)=\frac{s}{2-s}\mu_i\mathbf1_{i=j}
 +\left(1-\frac{s}{2-s}\right)\mu_i\mu_j
 \quad(1\le i,j\le d).
\]
Equivalently, the limiting categorical draws coincide through one shared draw with probability \(s/(2-s)\), and otherwise are independent draws with category probabilities \(\mu\). The bias normalized by the linear proxy is explicitly \(\frac{s-\rho(s,c)}s\to\frac{1-s}{2-s}\) as \(c\downarrow0\); this uses the proxy, not the actual correlation, as the denominator. None of these limits is asserted uniformly in \(s\) or in the category proportions.

## Assumptions and scope

The Gamma convention uses **shape and unit scale**. All parameters are strictly inside their ranges; no zero-shape Gamma variables occur in the finite-parameter theorem. Covariance matrices are \(d\times d\), with \(\operatorname{Cov}(X,Y)_{ij}=\operatorname{Cov}(X_i,Y_j)\). A zero-variance coordinate is excluded by the strict positivity of \(\mu\) and \(d\ge2\). The limit \(c\downarrow0\) is taken only after the finite model is defined, with \(s,\mu,d\) held fixed.

This proportional-sharing subfamily is the equal-marginal specialization of the shared-Gamma correlated Dirichlet model in Trick, Jäkel, and Rothkopf [1,2]. In the binary case it is also Magnussen's six-Gamma bivariate Beta construction [3]. The ratio \(s\) is exactly the shared shape divided by total marginal shape for *each* coordinate. It is the equal-marginal linear approximation proposed in [2, Equation (33)], not the distinct Taylor approximation in [3].

## Proof

**1. Independent totals and directions.** Summing independent unit-scale Gamma variables gives independent
\[
 T\sim\Gamma(sc,1),\qquad U,V\sim\Gamma((1-s)c,1).
\]
Their respective normalized coordinate vectors \(W_i=D_i/T\), \(P_i=A_i/U\), and \(Q_i=B_i/V\) are mutually independent, independent of the totals, and have Dirichlet shape vectors \(sc\mu\), \((1-s)c\mu\), and \((1-s)c\mu\). Therefore
\[
 X=RW+(1-R)P,\qquad Y=SW+(1-S)Q.
\]
All three direction vectors have expectation \(\mu\). Conditional on the totals, every cross term involving an independently centered direction vanishes. Hence
\[
 \operatorname{Cov}(X,Y)=\mathbb E[RS]\operatorname{Cov}(W)
 =\frac{\mathbb E[RS]}{sc+1}
   \left(\operatorname{diag}(\mu)-\mu\mu^{\mathsf T}\right).
\]
The usual Dirichlet marginal covariance is \(\operatorname{Cov}(X)=\bigl(\operatorname{diag}(\mu)-\mu\mu^{\mathsf T}\bigr)/(c+1)\); this proves the scalar factor and all displayed cross-correlations.

**2. Strict one-sided linear bias.** Both \(R\) and \(S\) have the \(\operatorname{Beta}(sc,(1-s)c)\) distribution. Thus
\[
 \mathbb E[R]=s,\qquad
 \mathbb E[R^2]=\frac{s(sc+1)}{c+1}.
\]
By exchangeability of \(R,S\), \(\mathbb E[(R-S)^2]=2(\mathbb E[R^2]-\mathbb E[RS])\), proving the exact bias identity. Since \(U,V\) are independent and nondegenerate, \(R\ne S\) almost surely, so this bias is strictly positive. Conditional on \(T\), \(R,S\) are independent with the same conditional mean \(h(T)=\mathbb E[T/(T+U)\mid T]\). The function \(h\) is strictly increasing; because \(T\) is nondegenerate,
\[
 \mathbb E[RS]-s^2=\operatorname{Var}(h(T))>0.
\]
This gives the strict lower bound and proves \(0<\rho(s,c)<s\) for every finite \(c>0\).

**3. Large concentration.** Gamma means and variances give \(T/c\to s\), \(U/c\to1-s\), and \(V/c\to1-s\) in probability as \(c\to\infty\). Consequently \(R,S\to s\) in probability. As the products are bounded between zero and one, \(\mathbb E[RS]\to s^2\); the prefactor \((c+1)/(sc+1)\to1/s\). The claimed high-concentration limit follows.

**4. Small-shape Gamma race.** For each fixed \(p>0\), let \(G_{p,c}\sim\operatorname{Gamma}(pc,1)\). Then
\[
 -c\log G_{p,c}\ \Longrightarrow\ \operatorname{Exp}(p)
 \quad\text{as }c\downarrow0.
\]
Indeed for \(z>0\), put \(y=e^{-z/c}\). The Gamma CDF satisfies the elementary bounds
\[
 \frac{e^{-y}y^{pc}}{\Gamma(1+pc)}
 \le\Pr(G_{p,c}<y)
 \le\frac{y^{pc}}{\Gamma(1+pc)},
\]
and both endpoints tend to \(e^{-pz}\). For \(z<0\), Markov's inequality bounds \(\Pr(G_{p,c}\ge e^{-z/c})\) by \(pc\,e^{z/c}\to0\). The limit law is continuous, so these distribution-tail statements imply the asserted weak convergence. Apply the lemma independently to \(T,U,V\), with rates \(s,1-s,1-s\). A continuous-mapping argument at the almost surely distinct exponential race times shows
\[
 (R,S)\Longrightarrow
 \left(\mathbf1_{Z_T<Z_U},\mathbf1_{Z_T<Z_V}\right),
\]
where \(Z_T,Z_U,Z_V\) are independent exponentials of rates \(s,1-s,1-s\). The event that both indicators are one is that the common Gamma total wins the three-way race; its probability is
\[
 \Pr(Z_T<\min(Z_U,Z_V))=\frac{s}{s+2(1-s)}=\frac{s}{2-s}.
\]
Bounded convergence in distribution yields \(\mathbb E[RS]\to s/(2-s)\). The scalar prefactor tends to one as \(c\downarrow0\), giving the first concentration endpoint.

**5. Joint categorical limit.** For fixed \(q>0\), a \(\operatorname{Dirichlet}(qc\mu)\) vector \(H_c\) satisfies
\[
 \mathbb E\sum_iH_{c,i}(1-H_{c,i})
 =\frac{qc\bigl(1-\sum_i\mu_i^2\bigr)}{1+qc}\longrightarrow0.
\]
The simplex is compact and the nonnegative displayed function vanishes precisely at its vertices, so every weak limit is vertex-supported. Since \(\mathbb E H_c=\mu\), its unique possible weak limit assigns probability \(\mu_i\) to vertex \(e_i\). Applying this independently to \(W,P,Q\) and combining with the independent Gamma-total race yields a joint limit of three independent category labels and two selection indicators. If both indicators are one, both vectors select the same label from \(W\); otherwise, the two selected labels are independent with common probabilities \(\mu\). The common-label selection event has probability \(s/(2-s)\), proving the stated joint law.

## Verification

The self-contained companion script `verify.py` performs symbolic rational identity checks, constructs the independent-Gamma coupling directly, and compares empirical cross-covariances with the stated matrix formula. It separately compares finite-concentration evaluations against the source's reported equal-margin example and checks numerical approaches to both endpoint values. Run with `python verify.py` using Python, NumPy and SymPy. The accompanying script was executed successfully; its checks passed. **These finite diagnostics do not prove any infinite-parameter or continuum statement.** The strict inequalities and both limits are established by the arguments above.

## Relationship to prior work

The shared-Gamma Beta construction is due to Magnussen [3]. Trick, Jäkel, and Rothkopf [1] gave exact product moments and extended the construction to paired Dirichlet vectors; Trick, Rothkopf, and Jäkel [2, Section 2.4.4 and Equation (33)] proposed a linear correlation calibration for proportionally shared equal marginals and explicitly left the range of its accuracy open. The present theorem establishes the strict direction of its bias for all finite concentrations and both sharp limiting values, as well as a full categorical joint limit not stated in either source. General expressions for covariance in [1,2] supply background but do not themselves assert the displayed global inequality or endpoint coupling. The generalized Arnold–Ng Gamma family mentioned in [1,2] encompasses the construction, but a general family definition is not a proof of its boundary law. Trick and Rothkopf [4] use correlated Dirichlet vectors for classifier fusion but do not state these calibration limits. A related 2004 algorithm [3] was available only through its abstract for comparison, so priority uncertainty remains.

## Limitations

This result concerns **equal Dirichlet marginals with a common proportional sharing fraction**. It does not prove a corresponding bound for unequal marginals, nonproportional shared components, or a multi-view common-factor construction. No monotonicity in \(c\), uniform error estimate in \(s\), or closed elementary expression for \(\rho(s,c)\) at general finite values is claimed. The low-concentration categorical law is a weak limit; it is not a total-variation convergence of continuous distributions to a discrete law. The mathematical-record comparison is not a universal novelty certificate, and older full texts not available for inspection may contain related statements. Independent validation has not been performed.

## References

[1] S. Trick, F. Jäkel, C. A. Rothkopf, *A Bivariate Beta Distribution with Arbitrary Beta Marginals and its Generalization to a Correlated Dirichlet Distribution*, arXiv:2104.08069 (initially public 16 April 2021). https://arxiv.org/abs/2104.08069

[2] S. Trick, C. A. Rothkopf, F. Jäkel, *Parameter estimation for a bivariate beta distribution with arbitrary beta marginals and positive correlation*, METRON 81 (2023), 163–180, DOI:10.1007/s40300-023-00247-2. https://doi.org/10.1007/s40300-023-00247-2

[3] S. Magnussen, *An algorithm for generating positively correlated Beta-distributed random variables with known marginal distributions and a specified correlation*, Computational Statistics & Data Analysis 46 (2004), 397–406, DOI:10.1016/S0167-9473(03)00169-5.

[4] S. Trick, C. A. Rothkopf, *Bayesian Classifier Fusion with an Explicit Model of Correlation*, arXiv:2106.01770 (2021). https://arxiv.org/abs/2106.01770
