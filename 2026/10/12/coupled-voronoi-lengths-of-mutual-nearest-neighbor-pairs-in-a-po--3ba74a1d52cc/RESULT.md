# Coupled Voronoi lengths of mutual nearest-neighbor pairs in a Poisson line

## Finding

Consider a stationary homogeneous Poisson process of intensity \(\lambda>0\) on the real line under its point Palm distribution. The point at the origin and its immediately adjacent point on the right constitute a mutual nearest-neighbor pair precisely on the event \(M\) defined below. Let \(V_0,V_1\) denote their actual one-dimensional Voronoi-cell lengths. Conditional on \(M\), their **complete joint law** is

\[
(V_0,V_1)\ \stackrel{d}{=}\ (Z+U_0,Z+U_1),
\quad Z\sim\operatorname{Exp}(3\lambda),\quad
U_0,U_1\mathrel{\mathop{\sim}^{\mathrm{iid}}}\operatorname{Exp}(2\lambda),
\]

with all three variables independent and the rate parameterization of the exponential distribution. Equivalently, for all \(s,t\ge0\),

\[
\mathbb E[e^{-sV_0-tV_1}\mid M]
=\frac{3\lambda}{3\lambda+s+t}\frac{2\lambda}{2\lambda+s}\frac{2\lambda}{2\lambda+t}.
\]

Consequently

\[
\operatorname{Corr}(V_0,V_1\mid M)=\frac4{13}
\quad\text{versus}\quad
\operatorname{Corr}(V_0,V_1)=\frac12,
\]

where the latter is for a right-adjacent pair selected without the mutual-neighbor condition. The conditional mean of either cell length is \(5/(6\lambda)\); conditional covariance is \(1/(9\lambda^2)\), and conditional variance is \(13/(36\lambda^2)\). The conditional joint upper diagonal tail is

\[
\mathbb P(V_0>u,V_1>u\mid M)
=4e^{-3\lambda u}-3e^{-4\lambda u},\qquad u\ge0.
\]

For the unconditioned Palm-typical point, write \(J\) for the event that it belongs to a mutual nearest-neighbor pair on either side, and \(V\) for its Voronoi-cell length. Then \(\mathbb P(J)=2/3\), and a regular conditional probability is

\[
\mathbb P(J\mid V=v)=\frac{1-e^{-\lambda v}}{\lambda v},\qquad v>0.
\]

This function decreases strictly from \(1\) to \(0\) as \(v\) increases. These statements describe one joint conditional law and its direct geometric and probabilistic consequences, not separate findings.

## Assumptions and scope

The process is simple and homogeneous on all of \(\mathbb R\), and \(\lambda\in(0,\infty)\) is arbitrary. Palm conditioning puts a point at the origin without altering the independent Poisson configurations on either half-line. Write \(A\) for the gap to the nearest point to the left, \(B\) for the gap to the nearest point to the right, and \(C\) for the gap from that right point to its next right neighbor. Then \(A,B,C\) are independent rate-\(\lambda\) exponential random variables. Set \(M=\{B<A,\ B<C\}\), which has probability \(1/3\). All ties have probability zero. The cells \(V_0=(A+B)/2\) and \(V_1=(B+C)/2\) are the genuine full Voronoi cells, not balls whose radius is a nucleus's nearest-neighbor distance. This theorem is one-dimensional and does not assert an analogous law in higher dimensions or for non-Poisson point processes.

## Proof

**Conditional exponential spacings.** On \(M\), the joint (unnormalized) density of \((B,A-B,C-B)=(b,x,y)\) for positive arguments is \(\lambda^3e^{-\lambda(3b+x+y)}\). Integrating gives \(\mathbb P(M)=1/3\). After division by this probability, the density factors as

\[
(3\lambda e^{-3\lambda b})(\lambda e^{-\lambda x})(\lambda e^{-\lambda y}).
\]

Hence, conditional on \(M\), \(B\sim\operatorname{Exp}(3\lambda)\) and the two excesses \(A-B,C-B\) are independent rate-\(\lambda\) exponentials, independent of \(B\). Every one-dimensional Voronoi cell extends halfway to its nearest site on each side. Therefore \(V_0=B+(A-B)/2\) and \(V_1=B+(C-B)/2\). Scaling a rate-\(\lambda\) exponential by \(1/2\) gives a rate-\(2\lambda\) exponential. This proves the common-shock representation and its Laplace transform for all nonnegative \(s,t\).

**Moments and survival.** The common random summand \(B\) has variance \(1/(9\lambda^2)\); each independent residual has variance \(1/(4\lambda^2)\). Thus the covariance is \(1/(9\lambda^2)\) and each marginal variance is \(13/(36\lambda^2)\), yielding correlation \(4/13\). Before conditioning, the two cells share only the exponential spacing \(B/2\); their covariance is \(1/(4\lambda^2)\) and each variance is \(1/(2\lambda^2)\), giving correlation \(1/2\). For \(u\ge0\), condition on the common shock \(Z\):

\[
\begin{aligned}
\mathbb P(V_0>u,V_1>u\mid M)
&=e^{-3\lambda u}+\int_0^u3\lambda e^{-3\lambda z}e^{-4\lambda(u-z)}\,dz\\
&=4e^{-3\lambda u}-3e^{-4\lambda u}.
\end{aligned}
\]

**Size-dependent reciprocity.** Let \(M_R\) denote the mutual relation to the right and \(M_L\) the analogous relation to the left. They are disjoint almost surely since a nearest neighbor is unique, and symmetry gives \(\mathbb P(M_R)=\mathbb P(M_L)=1/3\). Thus \(\mathbb P(J)=2/3\). The point-Palm typical cell has \(V=(A+B)/2\), a two-stage Erlang law with density \(f_V(v)=4\lambda^2v e^{-2\lambda v}\) for \(v>0\). The conditional \(V\mid M_R\) is a sum of independent rate-\(3\lambda\) and rate-\(2\lambda\) exponentials, with density \(6\lambda(e^{-2\lambda v}-e^{-3\lambda v})\). Because the two orientations are disjoint and exchangeable,

\[
 f_{V,J}(v)=2\mathbb P(M_R) f_{V\mid M_R}(v)
=4\lambda(e^{-2\lambda v}-e^{-3\lambda v}).
\]

Bayes' formula and cancellation of the positive density \(f_V(v)\) yield the displayed posterior. Its strict decrease follows from \(1-e^{-x}-xe^{-x}>0\) for \(x>0\); its endpoint limits follow from standard exponential limits. Every assertion holds for all allowable \(\lambda\), without asymptotic extrapolation.

## Verification

The standalone `verify.py` checks direct independent exponential spacings under point Palm against the derived conditioning event for three distinct intensities, with 1,600,000 seeded triples per intensity; independent moment, correlation, two-variable Laplace-transform and bivariate survivor calculations are compared numerically. It separately tests the size-conditioned mutual-pair posterior using bin-averaged empirical proportions and independent numerical integration, as well as positivity and scaling. Numerical agreement is corroboration, not a proof of the statements for all \(s,t,u,\lambda\); the preceding analytic factorization and Bayes argument supply that proof. Execute with `python verify.py` (NumPy is required).

## Relationship to prior work

Rohrmann and Zurbriggen [2] rigorously study nearest-neighbor **available volumes** defined by the ball about a site whose radius is its nearest-neighbor distance, and explicitly identify mutual-nearest-neighbor configurations for Poisson point patterns in dimensions one through three. Their available-volume pair is determined by the shared nearest-neighbor distance and is not the pair of full Voronoi-cell lengths: in the present theorem each cell also depends on a distinct *outer* inter-site gap. Their mutual-pair frequency and gap law are antecedents, not new claims here. Járai-Szabó and Néda [3, Section 2] derive the unconditioned one-dimensional *marginal* Poisson–Voronoi cell-length distribution, but not the pair law after mutual-neighbor selection. Calka and Chenavier [1] analyze extreme cell inradii and circumradii over spatial windows; those are different statistics from the present conditioned adjacent-cell lengths. Baumstark and Last [4] establish broad typical-face Palm descriptions that may provide another route to this calculation. Their complete paper could not be inspected, and this is a material priority risk. The asserted contribution is the explicit **joint conditional full-cell law**, its exact correlation comparison and its size-conditioned mutual-neighbor posterior, not the pre-existing Poisson memorylessness, nearest-neighbor frequency, or unconditioned cell-size law.

## Limitations

This calculation does not establish historical priority beyond the literature actually compared. In particular, a full-text comparison with Baumstark and Last [4] remains outstanding; their general Palm machinery could potentially subsume this special one-dimensional calculation. The distributional claim is conditional on selecting a right-adjacent pair under a point Palm measure; it is not the same as selecting a uniformly random location on a cell boundary or sampling a pair length-biased by the gap. The point-level posterior uses point-Palm sampling and is valid at positive cell lengths. Higher-dimensional geometry and non-Poisson renewal processes are outside scope. Independent external validation has not been performed.

## References

1. P. Calka and N. Chenavier, *Extreme values for characteristic radii of a Poisson-Voronoi tessellation*, arXiv:1304.0170v1 (first submitted 2013-03-31), https://arxiv.org/abs/1304.0170 . Primary MSC 60D05.
2. R. D. Rohrmann and E. Zurbriggen, *Conditional pair distributions in many-body systems: Exact results for Poisson ensembles*, arXiv:1109.6664 (first submitted 2011-09-29), https://arxiv.org/abs/1109.6664 . See Sections II and IV–V and Table III.
3. F. Járai-Szabó and Z. Néda, *On the size-distribution of Poisson Voronoi cells*, arXiv:cond-mat/0406116, https://arxiv.org/abs/cond-mat/0406116 . See Section 2.
4. V. Baumstark and G. Last, *Some distributional results for Poisson–Voronoi tessellations*, Advances in Applied Probability **39** (2007), 16–40, https://doi.org/10.1239/aap/1175266467 . Abstract inspected; full text not obtained.
