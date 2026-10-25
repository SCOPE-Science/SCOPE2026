# A hub-induced non-Gaussian width law for uniform hypergraphic polytopes

## Finding

For each fixed integer \(k\ge 4\), two canonical \(k\)-uniform hypergraphic polytopes have **exactly the same normalized spherical mean width in every dimension**, yet their random-direction widths have different limiting behavior: one retains an explicitly distributed random hub contribution, while the other has Gaussian fluctuations of order \(n^{-1/2}\). The law at the hub has an exact lower-edge square-root singularity and a sharp shifted-Gaussian upper tail.

Write \(\Delta_E=\operatorname{conv}\{e_i:i\in E\}\subset\mathbb R^{n+1}\), with coordinates indexed by \(\{0,1,\ldots,n\}\). Define the complete and one-hub polytopes
\[
 C_{n,k}=\sum_{E\subseteq\{0,\ldots,n\},\,|E|=k}\Delta_E,
 \qquad
 S_{n,k}=\sum_{T\subseteq\{1,\ldots,n\},\,|T|=k-1}\Delta_{\{0\}\cup T}.
\]
Both have intrinsic dimension \(n\) in parallel translates of \(H_n=\{x:\sum_{i=0}^n x_i=0\}\). Let \(U_n\) be Haar-uniform on the unit sphere of \(H_n\); for a convex body \(P\), use the **full** directional width \(w(P,u)=h_P(u)+h_P(-u)\) (there is no factor of \(1/2\)). Set
\[
 X^C_{n,k}=\frac{\sqrt n\,w(C_{n,k},U_n)}{\binom{n+1}{k}},\qquad
 X^S_{n,k}=\frac{\sqrt n\,w(S_{n,k},U_n)}{\binom n{k-1}}.
\]
Let \(\phi\) and \(\Phi\) denote the standard normal density and distribution function, and let \(Z,Z_1,Z_2,\ldots\) be independent standard normals. For fixed \(k\), define
\[
 \mu_k=\mathbb E\big[\max(Z_1,\ldots,Z_k)-\min(Z_1,\ldots,Z_k)\big],
 \quad F_k(z)=\mathbb E\big[\max(z,Z_1,\ldots,Z_{k-1})-\min(z,Z_1,\ldots,Z_{k-1})\big],
 \quad v_k=\operatorname{Var}(F_k(Z)).
\]
Then the following hold as \(n\to\infty\) through integers \(n\ge k\):

1. **Equal finite-dimensional means:** for every \(n\ge k\),
\[
 \mathbb E X^S_{n,k}=\mathbb E X^C_{n,k}
 =\mu_k\frac{\sqrt n}{\sqrt2\,\Gamma((n+1)/2)/\Gamma(n/2)}.
\]
2. **Different fluctuation regimes:**
\[
 X^S_{n,k}\Rightarrow F_k(Z),\qquad
 \operatorname{Var}(X^S_{n,k})\longrightarrow v_k>0,
\]
whereas
\[
 X^C_{n,k}\longrightarrow\mu_k\quad\text{in probability},
 \qquad \sqrt n\,(X^C_{n,k}-\mu_k)\Rightarrow N(0,\tau_k^2),
 \quad \tau_k^2=k^2v_k-\frac{\mu_k^2}{2}>0.
\]
3. **Explicit hub distribution and its two sharp edges:** set
\[
 a_k=2\int_0^\infty[1-\Phi(t)^{k-1}]\,dt,
 \quad d_k=(k-1)2^{3-k}\phi(0),
 \quad m_{k-1}=\mathbb E\max(Z_1,\ldots,Z_{k-1}).
\]
The function \(F_k\) is even and strictly increases on \([0,\infty)\), with \(F_k(0)=a_k\),
\[
 F_k'(z)=\Phi(z)^{k-1}-(1-\Phi(z))^{k-1},\quad F_k''(0)=d_k>0.
\]
Consequently, if \(t\ge a_k\) and \(b_k(t)\ge0\) is the unique solution to \(F_k(b_k(t))=t\), then
\[
 \mathbb P\{F_k(Z)\le t\}=2\Phi(b_k(t))-1.
\]
The law is supported on \([a_k,\infty)\), with
\[
 \mathbb P\{F_k(Z)\le a_k+\varepsilon\}
 \sim \frac{2}{\sqrt{\pi d_k}}\,\sqrt\varepsilon
 \quad(\varepsilon\downarrow0),
\]
and
\[
 \mathbb P\{F_k(Z)>t\}
 \sim \sqrt{\frac2\pi}\,\frac{\exp(-(t-m_{k-1})^2/2)}{t-m_{k-1}}
 \quad(t\to\infty).
\]
For the first genuinely non-zonotopal simplex size \(k=4\),
\[
 \mu_4=\frac3{\sqrt\pi}+\frac6{\pi\sqrt\pi}\arcsin(1/3)
 =2.0587507460079\ldots,\quad
 a_4=1.7762944847434\ldots,\quad
 v_4=0.1340566897483\ldots,\quad
 \tau_4^2=0.0256797188793\ldots.
\]
The numerical values are supplementary; the theorem is exact through the integral definitions above.

## Assumptions and scope

The integer \(k\) is fixed before \(n\to\infty\); no claim about simultaneous growth of \(k\) is made. All simplices have unit Minkowski coefficient. Width is Euclidean and intrinsically normalized on \(H_n\). The statements concern Haar-random directions, not random choices of hyperedges or random points inside the polytopes. No independence is assumed between the widths of the two polytopes. The three-variable case has additional zonotopal reductions and is not part of the claimed new regime.

## Proof

**1. Exact support and Gaussian representation.** For arbitrary \(g=(g_0,\ldots,g_n)\), the support function of a coordinate simplex is \(h_{\Delta_E}(g)=\max_{i\in E}g_i\). Minkowski additivity implies
\[
 w(C_{n,k},g)=\sum_{|E|=k}\big(\max_{i\in E}g_i-\min_{i\in E}g_i\big),\qquad
 w(S_{n,k},g)=\sum_{|T|=k-1}\big(\max(g_0,(g_i)_{i\in T})-\min(g_0,(g_i)_{i\in T})\big).
\]
These expressions are unchanged when a common scalar is added to all coordinates and are positively homogeneous. All coordinate differences \(e_i-e_0\) occur in the direction spans of the summand simplices, proving intrinsic dimension \(n\). With independent \(G_i\sim N(0,1)\), put \(\bar G=(n+1)^{-1}\sum G_i\), \(R_n=\|G-\bar G\mathbf1\|\), and \(U_n=(G-\bar G\mathbf1)/R_n\). Then \(U_n\) is Haar-uniform in \(H_n\), \(R_n\) is an independent \(\chi_n\) radius, and
\[
 X^C_{n,k}=\frac{\sqrt n}{R_n}A^C_{n,k},\qquad
 X^S_{n,k}=\frac{\sqrt n}{R_n}A^S_{n,k},
\]
where the \(A\)'s are the averages of the Gaussian ranges displayed in the first two formulas. Each summand has expected range \(\mu_k\), and \(\mathbb E R_n=\sqrt2\,\Gamma((n+1)/2)/\Gamma(n/2)\). Independence of radius and direction gives assertion 1 exactly.

**2. The star law.** Conditional on \(G_0=z\), \(A^S_{n,k}\) is an ordinary \((k-1)\)-sample U-statistic of the independent leaf normals, with kernel \((x_1,\ldots,x_{k-1})\mapsto\max(z,x_1,\ldots)-\min(z,x_1,\ldots)\). Its conditional mean is \(F_k(z)\). The kernel has a finite second moment, and the standard U-statistic overlap decomposition gives
\(\mathbb E|A^S_{n,k}-F_k(G_0)|^2=O_k(n^{-1})\).
The ordinary strong law for U-statistics also gives almost-sure convergence under the natural infinite-Gaussian coupling. Since \(R_n/\sqrt n\to1\) almost surely, \(X^S_{n,k}\to F_k(G_0)\) almost surely under this coupling. To justify the second-moment assertion without hiding a singular radial factor, observe exactly that \(A^S_{n,k}=(R_n/\sqrt n)X^S_{n,k}\), and the radius is independent of \(X^S_{n,k}\); hence
\(\mathbb E(A^S_{n,k})^2=\mathbb E(X^S_{n,k})^2\), because \(\mathbb E R_n^2=n\). The \(L^2\) estimate for \(A^S\), along with the exact mean and the \(\chi_n\)-radius asymptotic, proves \(\operatorname{Var}(X^S_{n,k})\to v_k\).

**3. The complete-polytope central limit law, including spherical normalization.** With \(N=n+1\), \(A^C_{n,k}\) is the symmetric \(k\)-sample U-statistic of the range kernel \(h(z_1,\ldots,z_k)=\max_i z_i-\min_i z_i\). Its first Hoeffding projection is \(F_k(z)-\mu_k\). Thus
\[
 A^C_{n,k}=\mu_k+\frac{k}{N}\sum_{i=0}^n(F_k(G_i)-\mu_k)+Q_N,
 \qquad\mathbb E Q_N^2=O_k(N^{-2}).
\]
Furthermore the centered Gaussian norm satisfies
\[
 \frac{\sqrt n}{R_n}=1-\frac1{2N}\sum_{i=0}^n(G_i^2-1)+o_{\mathbb P}(N^{-1/2}).
\]
The multivariate ordinary i.i.d. central limit theorem and Slutsky's theorem therefore show that the limiting normal variance is
\[
 \operatorname{Var}\left[k(F_k(Z)-\mu_k)-\frac{\mu_k}{2}(Z^2-1)\right].
\]
To simplify it, Gaussian integration by parts gives
\(\mathbb E[(Z^2-1)F_k(Z)]=\mathbb E[ZF_k'(Z)]\). By symmetry of the \(k\) Gaussian coordinates and Euler's identity for the degree-one homogeneous range function, the right side is \(\mu_k/k\): indeed
\(\sum_{i=1}^k Z_i\partial_i h(Z_1,\ldots,Z_k)=h(Z_1,\ldots,Z_k)\) off a null set. Substitution of \(\operatorname{Var}(Z^2-1)=2\) gives exactly \(\tau_k^2=k^2v_k-\mu_k^2/2\). Cauchy-Schwarz shows this is nonnegative. Equality would force \(F_k(Z)-\mu_k\) to be a multiple of \(Z^2-1\) almost surely; continuity would force equality for all real \(z\), impossible because \(F_k(z)\sim |z|+m_{k-1}\) at infinity. Hence \(\tau_k^2>0\). The U-statistic strong law and the radial strong law also yield \(X^C_{n,k}\to\mu_k\) in probability.

**4. Exact hub distribution and edge asymptotics.** Ties between independent continuous normals occur with probability zero. Differentiating the fixed-hub range according as the hub is largest or smallest gives the displayed formula for \(F_k'\), and differentiation again gives
\[
 F_k''(z)=(k-1)\phi(z)\big[\Phi(z)^{k-2}+(1-\Phi(z))^{k-2}\big]>0.
\]
Symmetry makes \(F_k\) even, with \(F_k(0)=2\mathbb E\max(0,Z_1,\ldots,Z_{k-1})=a_k\). Strict convexity and growth to infinity imply its stated inverse-CDF representation. Since
\(F_k(z)=a_k+\tfrac12d_kz^2+O_k(z^4)\) near zero, the standard normal small-ball expansion gives the exact square-root lower edge.

For \(z>0\), write \(M=\max(Z_1,\ldots,Z_{k-1})\), \(m=\min(Z_1,\ldots,Z_{k-1})\). Directly from the definition,
\[
 F_k(z)=z+\mathbb E[-m]+\mathbb E(M-z)_++\mathbb E(m-z)_+
 =z+m_{k-1}+O_k\big(\phi(z)/z^2\big)
\]
as \(z\to\infty\). The bound follows from \((M-z)_+\le\sum_j(Z_j-z)_+\) and the Gaussian bound \(\mathbb E(Z-z)_+=\phi(z)-z(1-\Phi(z))=O(\phi(z)/z^2)\), with an analogous bound for \((m-z)_+\). Therefore \(b_k(t)=t-m_{k-1}+O_k(\phi(t-m_{k-1})/(t-m_{k-1})^2)\). The two-sided standard normal Mills ratio yields the asserted sharp upper-tail equivalent.

Finally \(\mu_4\) has the stated closed form: integration by parts gives \(\mathbb E\max(Z_1,\ldots,Z_4)=12\int_{\mathbb R}\phi(z)^2\Phi(z)^2\,dz\). For \(Y\sim N(0,1/2)\), the integral equals \((2\sqrt\pi)^{-1}\mathbb E\Phi(Y)^2\). This expectation is an orthant probability of two standard normals of correlation \(1/3\), namely \(1/4+\arcsin(1/3)/(2\pi)\). Doubling the expected maximum gives \(\mu_4\).

## Verification

The attached standalone `width_checker.py` enumerates simplex sums directly for small sizes and compares them with independently derived sorting formulas for the complete and hub polytopes. It checks 1,350 exact-support numerical comparisons, evaluates the one-dimensional integrals for \(k=4,5\), tests the spherical-normalization covariance identity \(\mathbb E[(Z^2-1)F_k(Z)]=\mu_k/k\), and verifies the explicit \(\mu_4\) formula. A simulation of 4,000 Haar directions in intrinsic dimension 180 provides corroborating first two moments. Numerical experiments are not proofs of the limits; the proof above is analytic. The checker may be run with `python width_checker.py` using Python with NumPy and SciPy.

## Relationship to prior work

Agnarsson's *On a special class of hyper-permutahedra* (2017) defines and classifies the complete fixed-cardinality simplex sums and their face structure; in particular the complete-polytope sorted support formula is implicit in its vertex description and is not claimed new here. Benedetti–Bergeron–Machacek (2017/2019) define hypergraphic polytopes by sums of coordinate simplices and study their acyclic orientations and combinatorial properties. Chapoton–Pilaud (2022/2024) investigate deformed-permutahedron shuffles and describe the encompassing hypergraphic-polytope construction. Classical Hoeffding theory provides the general U-statistic laws used here; the exact non-Gaussian hub distribution, its sharp edges, the spherical variance correction, and the comparison between the two geometric families constitute the present theorem. Earlier related research on the simplex-sum stellohedron concerns all connected subsets of a star and a different extreme-value scaling, not the fixed-uniformity hypergraphs here. Other indexed work on star hypergraphic polytopes concerns Euclidean diameters or asymmetry, not this Haar-directional width law.

## Limitations

The theorem is for a fixed \(k\ge4\) and uniform positive simplex weights; no growing-\(k\), arbitrary hypergraph, or independent-audit claim is made. The exact law is a one-dimensional integral/inverse formula, not generally an elementary density. General U-statistic results supply part of the probabilistic machinery and are credited, not rebranded as novel. Although targeted searches and relevant primary materials were examined, unindexed equivalent metric results may exist. No independent review is represented here.

## References

- Geir Agnarsson, *On a special class of hyper-permutahedra*, Electronic Journal of Combinatorics **24** (2017), #P3.46; public version dated 2017-09-08. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v24i3p46/pdf/
- Carolina Benedetti, Nantel Bergeron and John Machacek, *Hypergraphic polytopes: combinatorial properties and antipode*, Journal of Combinatorics **10** (2019), 515–544; arXiv:1712.08848, first submitted 2017-12-23. https://arxiv.org/abs/1712.08848
- Frédéric Chapoton and Vincent Pilaud, *Shuffles of deformed permutahedra, multiplihedra, constrainahedra, and biassociahedra*, Annales Henri Lebesgue **7** (2024), 1535–1601; arXiv:2201.06896, first submitted 2022-01-18. https://arxiv.org/abs/2201.06896
- Wassily Hoeffding, *A class of statistics with asymptotically normal distribution*, Annals of Mathematical Statistics **19** (1948), 293–325.
- Robert J. Serfling, *Approximation Theorems of Mathematical Statistics*, Wiley (1980), chapters on U-statistics.
