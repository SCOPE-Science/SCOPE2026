# One-point stochastic optimality breaks at two-point planar Gaussian completion

## Finding
Let \(Z\) be a standard Gaussian vector in \(\mathbb R^2\). For a nonempty finite set \(\mathcal U\) of unit vectors, define \(M(\mathcal U)=\min_{v\in\mathcal U}|\langle v,Z\rangle|\). Suppose some directions have already been fixed and only new planar unit directions may be added.

**One-addition theorem.** For every existing finite collection of directions and every \(t>0\), adding one new direction perpendicular to the midpoint of any largest gap between consecutive projective perpendicular lines minimizes \(\Pr\{M(\mathcal U)>t\}\) among all one-direction additions. The choice is unique modulo line sign and ties between largest gaps.

**Two-addition obstruction.** There exist two fixed unit directions for which **no** choice of two additional planar directions stochastically minimizes the resulting Gaussian minimum. Explicitly, fix perpendicular-line angles \(0\) and \(L=13\pi/20\) on the projective circle of circumference \(\pi\), with complementary gap \(S=7\pi/20\). The unique two-addition configuration minimizing \(\mathbb E[M^2]\), called \(A\), subdivides the longer gap into three equal parts and leaves the shorter gap intact. The competitor \(B\) bisects both original gaps. Then
\[
\mathbb E[M_A^2]=1-\frac{3\sin(13\pi/60)+\sin(7\pi/20)}{\pi}
<1-\frac{2\sin(13\pi/40)+2\sin(7\pi/40)}{\pi}=\mathbb E[M_B^2],
\]
but for every sufficiently large \(t\),
\[
\Pr(M_B>t)<\Pr(M_A>t).
\]
Thus no feasible two-addition configuration has a Gaussian minimum dominated in first-order stochastic order by every other feasible configuration. The obstruction persists under sufficiently small perturbations of \(L\), so it is not an isolated angle coincidence.

## Assumptions and scope
The old directions are fixed (their signs do not matter), the new directions lie in the **same** two-dimensional Gaussian factor, and the variance of every Gaussian projection is one. Angles are measured between zero hyperplanes modulo \(\pi\). The one-addition statement allows repeated pre-existing lines, including zero gaps; uniqueness is intended as uniqueness of the added unoriented line when the largest gap is unique. The no-universal-optimizer statement concerns one fixed pair of old directions and **exactly two** additional directions, with all positions otherwise unrestricted. The term “stochastic minimum” means that the proposed completion has upper-tail probability no greater than every other completion for **every** \(t>0\).

## Proof
Write \(Z=R(\cos U,\sin U)\), with \(U\) uniform modulo \(\pi\), independent of the Rayleigh radius \(R\). The perpendiculars to the chosen unit vectors split the projective circle into cyclic gaps \(d_1,\ldots,d_m\ge0\) summing to \(\pi\). In a gap the closest perpendicular has angular distance \(\min\{u,d_j-u\}\). Conditioning on the angle and using \(\Pr(R>r)=e^{-r^2/2}\) gives, for every \(t>0\),
\[
\Pr(M>t)=\sum_{j=1}^m F_t(d_j),\qquad
F_t(d)=\frac2\pi\int_0^{d/2}\exp\!\left(-\frac{t^2}{2\sin^2u}\right)\,du,
\]
where the integrand at zero is defined by its limit zero. Differentiating on \(0<d<\pi\) shows that \(F_t'(d)=\pi^{-1}\exp[-t^2/(2\sin^2(d/2))]\) is strictly increasing. Hence \(F_t\) is strictly convex and \(F_t(0)=0\).

For one additional perpendicular in a gap of length \(d\), splitting at \(a\in[0,d]\) replaces \(F_t(d)\) by \(F_t(a)+F_t(d-a)\); strict convexity gives the unique minimum at \(a=d/2\). Its improvement is \(I_t(d)=F_t(d)-2F_t(d/2)\), with derivative \(I_t'(d)=F_t'(d)-F_t'(d/2)>0\). Thus choosing a largest gap and bisecting it gives the minimum simultaneously at every \(t>0\), proving the first assertion.

For the two-addition assertion, angular integration yields the exact second-moment identity
\[
\mathbb E[M^2]=\frac4\pi\sum_j\int_0^{d_j/2}\sin^2u\,du
=1-\frac1\pi\sum_j\sin d_j.
\]
For a fixed old gap \(d\) subdivided into \(r\ge1\) positive pieces, strict concavity of sine on \((0,\pi)\) shows that the maximum attainable sum of their sines is \(r\sin(d/r)\), with unique equality when every piece is \(d/r\). Two new lines therefore permit only the subdivision counts \((r_L,r_S)=(3,1),(2,2),(1,3)\) at an optimum. Their sums of sines are respectively
\[
A_2=3\sin(13\pi/60)+\sin(7\pi/20),\quad
B_2=2\sin(13\pi/40)+2\sin(7\pi/40),\quad
C_2=\sin(13\pi/20)+3\sin(7\pi/60).
\]
The strict inequalities \(A_2-B_2>0.028\) and \(A_2-C_2>0.8\) hold. For a completely rational enclosure, use Machin's identity \(\pi=16\arctan(1/5)-4\arctan(1/239)\), truncated alternating arctangent series, and alternating sine Taylor bounds through degrees nine and eleven. These give \(3.14159265<\pi<3.14159266\) and, by rational interval evaluation, \(0.028690156<A_2-B_2<0.028690331\), \(A_2-C_2>0.812794495\). The included verifier calculates the rational bounds without using floating-point values of \(\pi\) as evidence. Consequently \(A\), with gaps \((L/3,L/3,L/3,S)\), is the unique global second-moment minimizer.

Finally, for **any** nonempty finite gap family with \(d_{\max}=\max_j d_j>0\), the exact tail integral has the Laplace exponent
\[
\lim_{t\to\infty}\frac1{t^2}\log\Pr(M>t)
=-\frac1{2\sin^2(d_{\max}/2)}.
\]
Indeed, the integrand never exceeds its value at the largest available gap endpoint, yielding the upper bound. For every fixed small \(\varepsilon>0\), integrate over a positive-length angular interval immediately below that endpoint to obtain a matching lower logarithmic bound, then send \(\varepsilon\downarrow0\). For \(A\) the largest gap is \(S=14\pi/40\), whereas for \(B\) it is \(L/2=13\pi/40\). The displayed Laplace rates therefore imply \(\Pr(M_B>t)<\Pr(M_A>t)\) for all sufficiently large \(t\). Any stochastic minimizer would also minimize \(\mathbb E[M^2]=2\int_0^\infty t\Pr(M>t)\,dt\), forcing it to equal \(A\); the large-tail comparison rules this out.

Continuity of the strict trigonometric comparison and of the strict largest-gap comparison in \(L\) proves persistence on a nonempty open interval around \(13\pi/20\).

## Verification
Run `python3 verify_completion.py` using the Python standard library. It constructs the rational \(\pi\) enclosure from Machin's identity, checks rational Taylor intervals for the two strict allocation comparisons, separately integrates the angular second moments, and performs 140 finite one-insertion checks plus tail quadratures for the two configurations. The program's output is provided as `verification_output.txt`. The analytic convexity and Laplace-principle arguments, not the finite numerical checks, establish the theorem for every threshold and every allowable completion.

## Relationship to prior work
Kunisky's 2026 Gaussian-minimum manuscript introduced the cosine covariance and conjectured unconstrained first-order stochastic extremality, and explicitly derived the regular cosine law. A later 18 October 2026 paper, *Local stability of cosine configurations for Gaussian minima*, establishes the **unconstrained** planar equal-gap comparison and publishes the general planar gap formulas. Those formulas and the radial representation are therefore **not claimed as new here**. The present constrained-addition question fixes part of the configuration: the positive one-addition rule and the negative two-addition theorem concern optimal *completion under fixed anchors*. Neither source states a simultaneous-tail completion theorem or the loss of a universal optimizer after two additions. The earlier work on Gaussian **maxima** and full-rank perturbative local stability does not imply this anchor-constrained two-choice obstruction.

## Limitations
This proves no new statement about all-rank unconstrained correlation matrices. It does not classify all fixed-anchor collections for which two-point stochastic optimality fails, locate every crossing threshold, or prove uniqueness of a tail-optimal design for each finite threshold. The one-addition component is an elementary consequence of previously known gap convexity; originality resides in the exact two-addition incompatibility and its sharp distinction from one-addition universality. Historical priority for an equivalent constrained circular-zone optimization is not conclusively established. Independent mathematical audit has not been performed.

## References
1. D. Kunisky, *A revision of Litvak's conjecture on Gaussian minima and a volumetric zone conjecture*, arXiv:2605.02023v1, first submitted 2026-05-03, https://arxiv.org/html/2605.02023v1. See Proposition 2.1 and Conjecture 3.1.
2. *Local stability of cosine configurations for Gaussian minima*, anonymous research release, 2026-10-18, DOI 10.5281/zenodo.23453252, https://github.com/ipitchford/gaussian-cosine-local-stability/blob/main/paper.md. See Proposition 2, “The planar comparison.”
