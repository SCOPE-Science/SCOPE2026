# An exact all-or-nothing dispersal transition under alternating habitat quality and migration mortality

## Finding

Fix two habitat reproductive multipliers \(B>b>0\) and a migration survival probability \(0<c\le 1\). In the deterministic, density-independent two-patch model defined below, the annual asymptotic population multiplier \(\Lambda(d)\), optimized over the common fraction \(d\in[0,1]\) attempting to move between patches after reproduction, obeys
\[
\max_{0\le d\le 1}\Lambda(d)=\max\{\sqrt{Bb},cB\}.
\]
Every maximizing dispersal fraction is an endpoint: \(d=0\) alone if \(c<\sqrt{b/B}\), \(d=1\) alone if \(c>\sqrt{b/B}\), and exactly \(d=0,1\) if \(c=\sqrt{b/B}\). Every partial strategy \(0<d<1\) is strictly worse than the best endpoint, including at the equality threshold. The switch is discontinuous, and occurs at an explicit strictly intermediate survival cost \(c_* = \sqrt{b/B}\).

Moreover, writing \(u=c(B-b)\) and \(v=2\sqrt{Bb}\), every \(0<d<1\) satisfies the quantitative strict penalty
\[
\max\{\sqrt{Bb},cB\}-\Lambda(d)\ge
\frac{u^2v^2}{4(u^2+v^2)^{3/2}}d(1-d)>0.
\]
This inequality is a deliberately conservative uniform lower bound, not a claimed sharp gap.

## Assumptions and scope

There are two patches, and discrete non-overlapping generations. In odd-numbered reproductive seasons the diagonal fecundity matrix is \(D_1=\operatorname{diag}(B,b)\); in even-numbered seasons it is \(D_2=\operatorname{diag}(b,B)\). Thus the favorable patch alternates deterministically, with identical favorable and unfavorable fecundities each cycle. Following each reproductive season, a fraction \(d\) of individuals in *each* patch attempts to migrate to the other patch and survives the trip independently with mean fraction \(c\); nonmigrants suffer no travel loss. At the deterministic expectation level the corresponding transfer matrix is
\[
P_c(d)=\begin{pmatrix}1-d&cd\\cd&1-d\end{pmatrix}.
\]
The state evolves by \(x_{t+1}=P_c(d)D_{t}x_t\), starting from a vector with two strictly positive components. The asymptotic annual factor is the square root of the spectral radius of the two-season monodromy, \(\Lambda(d)=\rho(P_c(d)D_2P_c(d)D_1)^{1/2}\). This is **not** an evolutionarily stable strategy calculation for competing phenotypes and **not** a stochastic almost-sure growth theorem.

## Proof

Write \(J=\begin{pmatrix}0&1\\1&0\end{pmatrix}\). Since \(D_2=JD_1J\) and \(JP_c(d)=P_c(d)J\), if \(M_1=P_c(d)D_1\), then \(P_c(d)D_2=JM_1J\). Consequently the two-season monodromy equals \((JM_1)^2\). The nonnegative matrix \(JM_1\) is
\[
H(d)=\begin{pmatrix}cdB&(1-d)b\\ (1-d)B&cdb\end{pmatrix}.
\]
It is diagonally similar, via the fixed invertible diagonal matrix \(T=\operatorname{diag}(\sqrt b,\sqrt B)\), to the real symmetric matrix
\[
S(d)=T^{-1}H(d)T=\begin{pmatrix}cdB&\sqrt{Bb}(1-d)\\\sqrt{Bb}(1-d)&cdb\end{pmatrix}.
\]
Because \(H(d)\) is nonnegative, its Perron root is the spectral radius and equals the largest eigenvalue of \(S(d)\). Squaring \(H(d)\) in the monodromy yields \(\Lambda(d)=\lambda_{\max}(S(d))\). The eigenvalue formula gives the exact expression
\[
\Lambda(d)=\frac{cd(B+b)+\sqrt{c^2d^2(B-b)^2+4Bb(1-d)^2}}{2}.
\]
The first summand is affine in \(d\), and the second is the Euclidean norm of the two-dimensional affine vector \((ud,v(1-d))\), divided by two. Since \(u,v>0\), vectors associated with any two distinct \(d\) are never positively proportional: their determinant is \(uv(d_1-d_2)\ne0\). Equality in the Euclidean triangle inequality is therefore impossible for distinct \(d\), so \(\Lambda\) is strictly convex on \([0,1]\). In particular,
\[
\Lambda(d)<(1-d)\Lambda(0)+d\Lambda(1)\le\max\{\Lambda(0),\Lambda(1)\}
\]
for every interior \(d\). Evaluation at the two endpoints gives \(\Lambda(0)=\sqrt{Bb}\) and \(\Lambda(1)=cB\). Comparison yields the complete optimizer classification.

For the quantitative bound, put \(g(d)=\sqrt{u^2d^2+v^2(1-d)^2}\). Direct differentiation yields \(g''(d)=u^2v^2/g(d)^3\). Since \(g(d)\le\sqrt{u^2+v^2}\) on \([0,1]\), the second derivative of \(\Lambda\) is at least \(m=u^2v^2/[2(u^2+v^2)^{3/2}]\). The standard strong-convexity chord inequality gives \((1-d)\Lambda(0)+d\Lambda(1)-\Lambda(d)\ge m d(1-d)/2\). The maximum of the endpoints is no smaller than their chord, proving the stated penalty. The endpoint argument includes \(d=0,1\), where the two-season monodromy remains well-defined even though irreducibility can fail. All other steps hold for arbitrary real \(B>b>0\) and \(0<c\le1\).

## Verification

The standalone `verify.py` reconstructs the transfer/product identity in exact rational arithmetic on a representative parameter grid, verifies the independent symmetric characteristic polynomial and the exact positive-definiteness certificate at the threshold witness \((B,b,c)=(4,1,1/2)\), and checks the endpoint switch in examples on each side. These finite checks corroborate the algebra; the proof above establishes the universal real-parameter claim.

At the threshold witness \((4,1,1/2)\), both pure strategies attain annual multiplier \(2\), while a half-dispersing population has
\[
\Lambda(1/2)=\frac{5+\sqrt{73}}8<2.
\]
The strict inequality is exact because \(\sqrt{73}<11\). In fact \(2I-S(d)\) is positive definite for every \(0<d<1\), since its diagonal entries are positive and its determinant is \(3d(1-d)>0\).

## Relationship to prior work

McPeek and Holt (1992) examine selection on patch-independent and patch-specific dispersal in an explicitly density-regulated two-patch ecological model; the accessible original paper's model section assumes no individuals die during dispersal. Their results on high/low disperser polymorphisms are not this optimization of a linear periodic growth exponent with explicit travel mortality. Schreiber and Li (2010), in a full accessible preprint of their periodic population theory, prove broader cost-free qualitative results on dispersal invasion and evolutionary stability; Section 2 explicitly assumes no direct dispersal cost, and their discussion identifies costs of dispersal as an outstanding analytical issue. Their period-two no-cost results contextualize the endpoint \(c=1\), but they do not supply the finite-cost endpoint transition \(c=\sqrt{b/B}\) or the uniform interior penalty for this alternating two-patch specialization. Hutson, Mischaikow, and Poláčik (2001) study reaction–diffusion phenotype competition and its selection outcomes, not the discrete two-patch migration-mortality matrix family. No claim is made that a spectral eigenvalue calculation in itself is novel, or that the present growth maximizer is an ESS.

## Limitations

Perfectly alternating complementary environmental quality is restrictive. Migration happens after reproduction, successful migration has a constant survival fraction, and there is no density dependence, stochastic weather, immigration from outside, variation in patch sizes, or genotype-specific competition. The discontinuous switch need not persist in more general temporal sequences, under unequal stage mortality, or when individuals use environmental information. The result is for population growth of a fixed strategy, not actual evolutionary selection among interacting dispersal genotypes. Related results in older two-patch migration literature may have escaped the accessible searches; no claim of independent verification or complete bibliographic uniqueness is made.

## References

1. M. A. McPeek and R. D. Holt, *The Evolution of Dispersal in Spatially and Temporally Varying Environments*, American Naturalist 140 (1992), 1010–1027. DOI: 10.1086/285453.
2. S. J. Schreiber and C.-K. Li, *Evolution of unconditional dispersal in periodic environments*, arXiv:1007.5267 (first posted 2010-07-29), later Journal of Biological Dynamics, DOI: 10.1080/17513758.2010.525667.
3. V. Hutson, K. Mischaikow and P. Poláčik, *The evolution of dispersal rates in a heterogeneous time-periodic environment*, Journal of Mathematical Biology 43 (2001), 501–533. DOI: 10.1007/s002850100106.
