# Uniform near-diameter crossover and sharp anisotropy ordering for ellipsoids

## Finding

**Theorem (moving-eccentricity diameter tail).** Fix an integer \(d\ge 2\), a real \(x>0\), and \(\lambda=(\lambda_1,\dots,\lambda_d)\in[0,\infty)^d\) with \(\min_i\lambda_i=0\). For sufficiently small \(t>0\), let
\[
E_t=\operatorname{diag}(1-t\lambda_1,\dots,1-t\lambda_d)B_2^d.
\]
Take \(X_t,Y_t\) independently with uniform *Euclidean volume probability* on \(E_t\); its diameter is exactly \(2\). Let \(\Theta\) be uniformly distributed on the unit sphere, and put
\[
p=(d+3)/2,\qquad \kappa_j=\pi^{j/2}/\Gamma(j/2+1),\qquad
K_d=\frac{2^{d+1}d\kappa_{d-1}}{(d+1)(d+3)\kappa_d}.
\]
Then, as \(t\downarrow0\),
\[
\Pr\{\|X_t-Y_t\|_2>2-tx\}
=K_dt^p F_{d,x}(\lambda)+O_{d,x,\lambda}(t^{p+1}),
\quad F_{d,x}(\lambda)=\mathbb E_\Theta\!\left[\left(x-2\sum_{i=1}^d\lambda_i\Theta_i^2\right)_+^p\right].\tag{1}
\]
The displayed absolute error estimate is uniform when \(x\) stays in a fixed compact subset of \((0,\infty)\), \(\lambda_i\) stay bounded, and the maximal semiaxis is held at \(1\). It does not assert uniformity for \(\lambda_i\to\infty\) with \(t\).

**Sharp anisotropy ordering.** For \(d\ge3\), fixing \(\sum_i\lambda_i=L>0\), among nonnegative contraction vectors with at least one zero,
\[
F_{d,x}(0,L/(d-1),\ldots,L/(d-1))
\le F_{d,x}(\lambda)
\le F_{d,x}(0,\ldots,0,L).\tag{2}
\]
Equality holds only for permutations of the relevant endpoint vector. Thus the leading rare-distance probability is strictly Schur-convex in the contraction spectrum, and the balanced contraction is uniquely optimal for suppressing near-diametral pairs. Fixing \(L\) fixes the ellipsoid volume loss through first order, since \(\operatorname{vol}(E_t)=\kappa_d(1-Lt+O(t^2))\); hence (2) compares geometrically natural equal-first-order-volume deformations. For \(d=2\) the two endpoint spectra coincide up to permutation.

**Matching across diameter-manifold multiplicity.** Suppose \(1\le k<d\), \(q=d-k\), and \(b_1,\dots,b_q>0\). If \(\lambda(T)=(0^k,Tb_1,\ldots,Tb_q)\), then as \(T\to\infty\), *within the crossover coefficient* (not in a simultaneous \(t,T\) limit),
\[
F_{d,x}(\lambda(T))\sim
\frac{\Gamma(d/2)\Gamma(p+1)}{\Gamma(k/2)\Gamma(p+1+q/2)}
\frac{x^{p+q/2}}{(2T)^{q/2}\sqrt{\prod_{j=1}^q b_j}}.\tag{3}
\]
The power \(p+q/2=d+(3-k)/2\) is the exponent of the fixed-gap ellipsoid result with an \((k-1)\)-dimensional manifold of diameter endpoints. Equation (3) matches exponents but is **not** a uniform two-parameter limit.

**A precise three-dimensional transition.** When \(d=3\) and \(\lambda=(0,0,c)\), (1) becomes \(\Pr\{\|X_t-Y_t\|>2-tx\}=(3/2)t^3G_x(c)+O(t^4)\), where
\[
G_x(c)=\begin{cases}
x^3-2cx^2+\frac{12}{5}c^2x-\frac87c^3,&0\le c\le x/2,\\[3pt]
\frac{16}{35}\frac{x^{7/2}}{\sqrt{2c}},&c\ge x/2.
\end{cases}\tag{4}
\]
For every fixed \(x>0\), \(G_x\) is \(C^3\) but not \(C^4\) at \(c=x/2\):
\[
G_x^{(4)}((x/2)^+)-G_x^{(4)}((x/2)^-)=48/x.\tag{5}
\]
The three-dimensional formula is a specialization of an older exact spheroidal distance-distribution integral; the independently motivated contribution here is its uniform *all-dimensional* scaling theorem together with sharp contraction-spectrum ordering and cross-multiplicity matching.

## Assumptions and scope

The dimension \(d\) is fixed, not increasing with \(t\). The separation uses the ambient Euclidean norm. The two sample points are independent and uniform in *volume*, not on the boundary, and the anisotropy scale equals the distance-to-diameter scale. Each coordinate semiaxis is \(1-t\lambda_i>0\) for sufficiently small \(t\). The nonnegative vector has at least one zero, ensuring diameter exactly \(2\). The positive-part convention is \(z_+=\max(z,0)\). The shape coefficient \(F_{d,x}\) is a spherical integral; it may alternatively be integrated against a \(\operatorname{Dirichlet}(1/2,\ldots,1/2)\) law for the squared coordinates.

## Proof

**1. The spherical two-point tail and normalization.** Let \(U,V\) be independent uniform points in \(B_2^d\), let \(W=U-V\), and let \(R=\|W\|\). The density of \(W=w\) equals \(g_d(\|w\|)/\kappa_d^2\), where the overlap volume of two unit balls with center distance \(r\in[0,2]\) is
\[
g_d(r)=2\kappa_{d-1}\int_{r/2}^{1}(1-s^2)^{(d-1)/2}\,ds.
\]
Writing \(r=2-h\), a one-variable Taylor expansion at \(s=1\) gives
\[
g_d(2-h)=\frac{2\kappa_{d-1}}{d+1}h^{(d+1)/2}+O_d(h^{(d+3)/2}).
\]
Multiply by the spherical Jacobian \(d\kappa_d r^{d-1}\), divide by \(\kappa_d^2\), and integrate the resulting radial density from \(r=2-h\) to \(r=2\). This yields, uniformly for \(0\le h\le h_0\) with sufficiently small fixed \(h_0\),
\[
H_d(h):=\Pr\{R>2-h\}=K_d h^p+O_d(h^{p+1}),\qquad
H_d'(h)=pK_d h^{p-1}+O_d(h^p).
\]
These identities also fix every normalization in (1).

**2. A moving ellipsoid is an angular perturbation of a ball.** Set \(A_t=\operatorname{diag}(1-t\lambda_i)\), \(X_t=A_tU\), \(Y_t=A_tV\). Rotational invariance of the ball makes \(W=R\Theta\), with \(R\) independent of Haar-uniform \(\Theta\). For each unit direction, put \(a(\Theta)=\sum_i\lambda_i\Theta_i^2\) and \(\alpha_t(\Theta)=\|A_t\Theta\|\). Uniformly on the sphere, \(\alpha_t=1-ta+O_\lambda(t^2)\), so the required radial deficit is
\[
h_t(\Theta)=\left[2-\frac{2-tx}{\alpha_t(\Theta)}\right]_+
=t(x-2a(\Theta))_++O_{x,\lambda}(t^2).
\]
The positive-part map is Lipschitz. Since \(H_d\) has derivative of order \(h^{p-1}\) at \(0\), substitution into the spherical radial tail and angular integration establish (1), with an absolute remainder \(O(t^{p+1})\). Compact parameter bounds give the asserted uniformity.

**3. Strict Schur order.** The function \(f(z)=(x-2z)_+^p\) is convex on \([0,\infty)\), and strictly convex on \([0,x/2)\) for \(p>1\). Consequently \(\lambda\mapsto \mathbb E f(\sum_i\lambda_i\Theta_i^2)\) is convex and permutation-invariant. The elementary majorization principle implies (2): the balanced vector is majorized by every allowed vector of total mass \(L\), and the single-spike vector majorizes all of them. For strictness, every nontrivial averaging of unequal coordinates gives different linear arguments on a positive-measure open set of directions; because at least one zero coefficient is present and \(x>0\), an open subregion meets the strictly convex active interval. Hence Jensen's inequality is strict unless the spectra agree up to permutation. This also supplies equality characterizations.

**4. Multiplicity matching.** Write \(\Theta=(\sqrt{1-\|y\|^2}\,\eta,y)\) with \(\eta\in S^{k-1}\), \(y\in B_q\). The Haar spherical measure has density proportional to \((1-\|y\|^2)^{(k-2)/2}\,d\eta\,dy\). The positive-part integrand vanishes outside \(\sum_j b_j y_j^2<x/(2T)\). Rescale \(y_j=\sqrt{x/(2Tb_j)}z_j\), apply dominated convergence, and use
\[
\int_{\|z\|<1}(1-\|z\|^2)^p\,dz
=\frac{\pi^{q/2}\Gamma(p+1)}{\Gamma(p+1+q/2}}.
\]
The sphere-area ratio is \(\Gamma(d/2)/(\pi^{q/2}\Gamma(k/2))\), which gives (3). The calculation is separate from, and does not enlarge the uniformity range of, the \(t\downarrow0\) remainder.

**5. Explicit three-dimensional chamber.** For \(d=3\), \(\Theta_3\) is uniform on \([-1,1]\), so \(F_{3,x}(0,0,c)=\int_0^{\min(1,\sqrt{x/(2c)})}(x-2cz^2)^3\,dz\) for \(c>0\), with the continuous value \(x^3\) at \(c=0\). Direct integration gives (4). Differentiating the two elementary branches four times shows agreement through order three and the derivative jump (5).

## Verification

Run the included standalone script with `python verification.py` in an environment with Python 3.9 or later, SymPy, mpmath, and NumPy. A successful execution prints `PASS: 57 independent symbolic and numerical checks`. The checker verifies the exact three-dimensional ball overlap identity, the four matching derivative orders and fourth-derivative jump, the two branches against independently integrated angular laws for 27 parameter choices, the leading coefficient against exactly integrated moving-spheroid laws for 18 parameter pairs, constants in three dimensions, and sampled strict Schur inequalities. These are finite reproducibility diagnostics; the all-dimensional proof is the argument above, not an inference from the numerical tests.

## Relationship to prior work

Schrempp (2017) establishes extremes for smooth bodies with a unique *fixed* diameter pair, including ellipsoids with a separated leading semiaxis. Henze (May 2026) studies the largest distance among many points in a fixed rotational ellipsoid with a two-dimensional major eigenspace. Henze and Jammalamadaka (June 2026) extend this to a fixed ellipsoid with any multiplicity of the largest semiaxis and derive the corresponding two-point small-deficit exponent. Their fixed-gap hypotheses do not supply an estimate uniform when the semiaxis gaps shrink at the same speed as the distance deficit. Our formula (3) matches their exponent without claiming their fixed-gap result as new.

The classical spherical pair-distance density is also well known. In particular, García-Pelayo (2005, Section 3, formula (8)) already gives a general three-dimensional ellipsoid distance distribution as an angular integral and a closed spheroidal formula; thus the *three-dimensional specialization* (4), taken in isolation, is implied by prior exact-distribution work. That source does not establish (1) in arbitrary dimension with a uniform error, the strict all-spectrum Schur extremizers (2), or the cross-multiplicity coefficient (3). Parry and Fischbach (2000) obtain an eccentricity expansion through fourth order in dimensions two and three, not a uniform all-dimensional moving-threshold asymptotic. Earlier exact formulas and their special cases are acknowledged, not claimed as separate discoveries.

## Limitations

This is a geometric probability asymptotic for two uniform interior points, not an extreme-value theorem for a sample of increasing size. The estimate is for fixed \(d,x,\lambda\) and bounded parameter sets; it does **not** prove a joint regime with \(\lambda_i\to\infty\) while \(t\to0\). In dimension three the fixed-spheroid probability law has already been explicitly computed, and (4) is a derived visualization of a more general theorem rather than an independent novelty claim. Some older literature on elliptic distance distributions may contain equivalent asymptotics; historical priority is not certified. No independent mathematical audit has been performed.

## References

1. N. Henze, *A 4/7-limit law for the largest interpoint distance in a rotational ellipsoid* (first posted 2026-05-23), arXiv:2605.24627, https://arxiv.org/abs/2605.24627.
2. N. Henze and S. R. Jammalamadaka, *The limit law of the largest interpoint distance in a d-dimensional ellipsoid* (first posted 2026-06-27), arXiv:2606.29036, https://arxiv.org/abs/2606.29036.
3. M. Schrempp, *Limit laws for the diameter of a set of random points from a distribution supported by a smoothly bounded set* (2017), arXiv:1709.03706, https://arxiv.org/abs/1709.03706.
4. R. García-Pelayo, *Distribution of distance in the spheroid*, J. Phys. A: Math. Gen. **38** (2005), 3475–3482, https://doi.org/10.1088/0305-4470/38/16/001.
5. M. Parry and E. Fischbach, *Probability distribution of distance in a uniform ellipsoid: Theory and applications to physics*, J. Math. Phys. **41** (2000), 2417–2433, https://doi.org/10.1063/1.533249.
6. A. Mayer and I. Molchanov, *A limit theorem for maximal interpoint distance of random sample in unit ball* (2006), arXiv:math/0605289, https://arxiv.org/abs/math/0605289.
