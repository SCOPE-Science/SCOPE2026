# Exact non-Gaussian null fluctuations of a six-pattern quasirandomness statistic

## Finding

Let \(\Pi_n\) be uniform on the symmetric group \(S_n\). For a permutation pattern \(\sigma\) of length \(k\), let \(d(\sigma,\Pi_n)\) be the proportion of the \(\binom nk\) increasing index subsequences whose relative-value ordering equals \(\sigma\). Define, for every integer \(n\ge4\),
\[
T_n=d(123,\Pi_n)+d(321,\Pi_n)+d(2143,\Pi_n)+d(3412,\Pi_n)
+\tfrac12d(2413,\Pi_n)+\tfrac12d(3142,\Pi_n).
\]
Then \(\mathbb E T_n=11/24\) exactly. The first nonzero asymptotic fluctuation occurs at scale \(1/n\):
\[
 n(T_n-11/24)\ \xrightarrow{\ d\ }\ \sum_{j\ge1}\lambda_j(Z_j^2-1),
 \qquad \lim_{n\to\infty}n^2\operatorname{Var}(T_n)=\frac{121}{1800}.
\]
Here \(Z_j\) are independent standard normal variables and \((\lambda_j)\) are the nonzero real eigenvalues, repeated according to multiplicity, of the explicitly specified symmetric kernel operator below. The series converges in \(L^2\), and its law is non-Gaussian. Thus a conventional nondegenerate \(\sqrt n\)-normal approximation is inappropriate for this six-pattern statistic under the independent-ranks null.

## Assumptions and scope

The null model consists of \(n\) independent points \(Z_i=(X_i,Y_i)\), \(i=1,\ldots,n\), uniformly distributed on the unit square. Ordering their \(X\)-coordinates and taking the resulting relative ranks of their \(Y\)-coordinates produces \(\Pi_n\). Ties have probability zero. There are no estimated parameters, distributional ties, or local alternatives in this statement. The source six-pattern functional is the one introduced by Crudele, Dukes and Noel (2023); the present result concerns its *sampling fluctuations under independence*, not a new quasirandom-forcing characterization.

For \(k\in\{3,4\}\), let \(H_k(z_1,\ldots,z_k)\) be the weighted sum of pattern indicators after sorting the points by their first coordinate. The nonzero weights for \(H_3\) are one on \(123\) and \(321\); for \(H_4\) they are one on \(2143\) and \(3412\), and one-half on \(2413\) and \(3142\). The kernels are symmetrized by sorting and are measurable and bounded. Set
\[
\theta_3=\frac13,\quad\theta_4=\frac18,\quad
m_k(z)=\mathbb E[H_k(z,Z_2,\ldots,Z_k)],\quad
b_k(z,w)=\mathbb E[H_k(z,w,Z_3,\ldots,Z_k)].
\]
The principal kernel, for \(z,w\in[0,1]^2\), is
\[
K(z,w)=3\bigl(b_3(z,w)-m_3(z)-m_3(w)+\theta_3\bigr)
+6\bigl(b_4(z,w)-m_4(z)-m_4(w)+\theta_4\bigr).
\]
It is a symmetric, square-integrable, canonical kernel: \(\int_{[0,1]^2}K(z,w)\,dw=0\) for every \(z\) outside a null set. The eigenvalues in the finding are those of \((\mathcal Kf)(z)=\int_{[0,1]^2}K(z,w)f(w)\,dw\) on real \(L^2([0,1]^2)\).

## Proof

**First-order cancellation.** For \(z=(x,y)\), put \(P(t)=6t^2-6t+1\). Direct conditioning on the possible coordinate ranks of a fixed point gives
\[
m_3(x,y)=\frac13+\frac{P(x)P(y)}6,\qquad
m_4(x,y)=\frac18-\frac{P(x)P(y)}8.
\]
Consequently
\[
3(m_3-\theta_3)+4(m_4-\theta_4)=0
\]
pointwise. This cancellation is essential: the two U-statistics separately have nontrivial order-one projections, but their weighted sum has none.

**Second-order kernel.** For fixed \(0<x<u<1\), the conditional probability that the two fixed first-coordinate values occupy ranks \(i<j\) among \(k\) points is
\[
p_{ij}^{(k)}(x,u)=\frac{(k-2)!}{(i-1)!(j-i-1)!(k-j)!}
 x^{i-1}(u-x)^{j-i-1}(1-u)^{k-j}.
\]
For \(0<y<v<1\), the corresponding second-coordinate rank probabilities are \(p_{\ell m}^{(k)}(y,v)\). With pattern weights \(a_\sigma\), this yields the exact conditional expectation
\[
b_k((x,y),(u,v))=\frac1{(k-2)!}
\sum_{i<j}\sum_{\ell<m}p_{ij}^{(k)}(x,u)p_{\ell m}^{(k)}(y,v)
\sum_{\substack{\sigma\in S_k\\\sigma(i)=\ell,\ \sigma(j)=m}}a_\sigma.
\]
The symmetry under reversing either coordinate determines the other three ordering chambers. These formulas specify \(K\) without numerical approximation. Expanding this polynomial on the chamber \(x<u,\ y<v\), squaring and integrating exactly gives
\[
\int_{0<x<u<1}\int_{0<y<v<1}
K((x,y),(u,v))^2\,dy\,dv\,dx\,du=\frac{121}{14400}.
\]
The displayed iterated-integral notation denotes integration with Lebesgue measure over the stated four-dimensional region. Reversal invariance makes the four coordinate-order chambers equal in integral, giving
\[
\lVert K\rVert_{L^2([0,1]^4)}^2=\frac{121}{3600}>0.
\]
In particular, \(K((1/4,1/4),(3/4,3/4))=5/32\), confirming nontriviality.

**Limit and variance.** The Hoeffding decomposition of the two fixed-order U-statistics, together with exact vanishing of the first-order part, gives
\[
T_n-\frac{11}{24}=\binom n2^{-1}\sum_{1\le i<j\le n}K(Z_i,Z_j)+R_n,
\qquad \mathbb E R_n^2=O(n^{-3}).
\]
The canonical order-two spectral U-statistic theorem therefore implies
\[
 n\binom n2^{-1}\sum_{i<j}K(Z_i,Z_j)
\ \xrightarrow{\ d\ }\ \sum_{j\ge1}\lambda_j(Z_j^2-1).
\]
The canonical kernel has mean zero in either argument. Different unordered pairs of kernel evaluations are uncorrelated, including pairs sharing one index. Consequently
\[
\lim_{n\to\infty}n^2\operatorname{Var}(T_n)=2\lVert K\rVert_2^2=\frac{121}{1800}.
\]
The limit has variance \(2\sum_j\lambda_j^2=121/1800>0\). Its fourth cumulant is \(48\sum_j\lambda_j^4>0\), so it is not Gaussian. This proves the finding.

## Verification

The standalone file `verify_null_limit.py` implements the rank-placement formulas using exact SymPy polynomials, independently checks the two first projections and their cancellation, and integrates the squared second projection monomial by monomial. For a monomial \(x^a u^b y^c v^d\) on \(x<u,y<v\), the integral is exactly
\[
\frac{1}{(a+1)(a+b+2)(c+1)(c+d+2)}.
\]
It also exhaustively enumerates every permutation of sizes \(4,5,6,7\) and checks the respective exact variances \(41/576\), \(299/14400\), \(6137/648000\), and \(2677/504000\), with exact mean \(11/24\). Run `python verify_null_limit.py` with SymPy installed. These finite checks corroborate algebra; they do not replace the analytic infinite-sample U-statistic argument.

## Relationship to prior work

Crudele, Dukes and Noel introduced this particular weighted six-pattern functional, established its permuton lower bound \(11/24\), and proposed it as a test of independence in *Six Permutation Patterns Force Quasirandomness* (first public version March 8, 2023). Neither that extremal characterization nor its six patterns is claimed as new here. The separate new quantitative question is its null sampling law and exact leading variance after cancellation of the first projection.

Even-Zohar's *Patterns in Random Permutations* (2018) gives a general projection framework and asymptotic laws for pattern statistics; these foundational results explain why a second canonical U-statistic would have a centered quadratic-normal spectral limit. They do not identify the first-projection cancellation for this subsequently introduced six-pattern combination or its exact \(121/1800\) coefficient. Related work by Janson, Nakamura and Zeilberger develops joint asymptotics for several pattern counts. These broader theories were considered in comparing mathematical implications, not merely titles.

## Limitations

The eigenvalues are specified intrinsically by the exact Hilbert–Schmidt operator; they are not tabulated or claimed to have a finite closed form. The variance constant alone does not give every rejection quantile of the non-Gaussian null distribution. The theorem covers the ideal independent continuous-rank null, not noisy ties, estimated parameters, explicit finite-sample error bounds, or power against alternatives. Historical priority is assessed from inspected accessible sources, not conclusively certified; independent mathematical validation has not been performed.

## References

1. C. Crudele, M. Dukes and J. A. Noel, *Six Permutation Patterns Force Quasirandomness*, first public version March 8, 2023, https://arxiv.org/abs/2303.04776 (full-text https://arxiv.org/html/2303.04776v4).
2. C. Even-Zohar, *Patterns in Random Permutations*, first public version November 19, 2018, https://arxiv.org/abs/1811.07883.
3. S. Janson, B. Nakamura and D. Zeilberger, *On the Asymptotic Statistics of the Number of Occurrences of Multiple Permutation Patterns*, https://sites.math.rutgers.edu/~zeilberg/mamarim/mamarimhtml/smp.html.
