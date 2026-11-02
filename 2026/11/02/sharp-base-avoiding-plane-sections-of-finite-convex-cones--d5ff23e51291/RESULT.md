# Sharp base-avoiding plane sections of finite convex cones

## Finding

Let \(B\subset\mathbb R^2\) be any full-dimensional, origin-symmetric compact convex body of perimeter \(2\pi r\), where \(r>0\). For \(H>0\) consider the finite three-dimensional cone
\[
K_H(B)=\operatorname{conv}\bigl(\{(0,0,0)\}\cup (B\times\{H\})\bigr).
\]
Draw an unoriented affine plane from Euclidean-motion-invariant plane measure, conditional on hitting \(K_H(B)\). Write \(p_H(B)\) for the probability that this plane misses the designated base \(B\times\{H\}\). Tangencies have measure zero. Set
\[
a=\frac{\pi r}{2},\quad F_H(s)=H-s\arctan(H/s)\quad(s>0),\quad F_H(0)=H,
\]
and use \(\langle f\rangle=(2\pi)^{-1}\int_0^{2\pi}f(\varphi)\,d\varphi\). Let \(h_B(\varphi)\) denote the planar support function of \(B\) in direction \((\cos\varphi,\sin\varphi)\). Define
\[
N_H(B)=\langle F_H(h_B)\rangle,\quad N_-=H-r\arctan(H/r),\quad N_+=\sqrt{H^2+a^2}-a.
\]
Then
\[
\boxed{p_H(B)=\frac{N_H(B)}{\pi r+N_H(B)}}
\]
and its *entire sharp range* over the stated bases is
\[
\boxed{\frac{N_-}{\pi r+N_-}\le p_H(B)<\frac{N_+}{\pi r+N_+}.}
\]
Equality in the lower bound holds exactly for the radius-\(r\) disk centered at the apex projection. The upper bound is strict for every full-dimensional base, is approached by increasingly thin centrally symmetric rectangles, and every intermediate value is realized by a full-dimensional origin-symmetric base.

There is also quantitative rigidity. With
\[\operatorname{Var}_{\varphi}h_B=\langle(h_B-r)^2\rangle,\]
one has
\[
\boxed{
 p_H(B)-p_H(rD)
 \ge\frac{\pi r H^3\operatorname{Var}_{\varphi}h_B}
 {(H^2+a^2)^2(\pi r+N_+)(\pi r+N_-)}.
}
\]
Here \(D\) is the planar Euclidean unit disk. The displayed constant is not claimed optimal.

Finally, this sharp range has a singular thin-base transition. Suppose \(H\downarrow0\) and \(B_H=[-a_H,a_H]\times[-b_H,b_H]\) is a full-dimensional rectangle with \(a_H+b_H=a\) and \(b_H/H\to\kappa\in[0,\infty)\). Then
\[
\boxed{\lim_{H\downarrow0}\frac{p_H(B_H)}{H^2}
=\frac2{\pi^3r^2}\big[(1+\kappa^2)\arctan(1/\kappa)-\kappa\big],}
\]
with \(\arctan(1/0)=\pi/2\). In contrast, for each fixed full-dimensional origin-symmetric \(B\),
\[
\boxed{p_H(B)=\frac{H^3}{3\pi r}\langle h_B^{-2}\rangle+O_B(H^5).}
\]
Thus generic fixed bases exhibit cubic small-height decay, while rectangles whose short half-width is comparable to cone height exhibit quadratic decay.

## Assumptions and scope

All objects are Euclidean. Origin symmetry \(B=-B\) is essential to the support-function representation and to the equality classification; no arbitrary asymmetric-base theorem is asserted. The base has a nonempty planar interior. The apex lies directly below the symmetry center and the cone is the convex hull of the apex and its single planar base, not a cylinder. The random-plane law is the unique motion-invariant measure on unoriented affine planes restricted and normalized to planes hitting the fixed cone, not a law with independently uniform direction and conditional offset. All displayed probabilities concern the labeled base *as a subset of the solid*; they do not describe the distribution of section area or whether a section is an ellipse. The crossover rectangle is allowed to vary with \(H\) while its perimeter remains fixed.

## Proof

**1. Exact random-plane formula.** Parametrize unit normals in the upper hemisphere by \(n=(\sin\theta\,u_\varphi,\cos\theta)\), where \(0\le\theta\le\pi/2\). For fixed \((\theta,\varphi)\), the offsets of planes meeting the designated base form
\[
[H\cos\theta-h_B(\varphi)\sin\theta,\ H\cos\theta+h_B(\varphi)\sin\theta].
\]
Since the apex projects to offset zero, the offsets of planes meeting the solid cone form the convex hull of this interval with \(0\). Those meeting the cone but missing its base form, apart from endpoints,
\[
(0,(H\cos\theta-h_B(\varphi)\sin\theta)_+).
\]
With invariant measure \(d\varphi\,\sin\theta\,d\theta\,dt\), direct integration yields
\[
\int_0^{\pi/2}(H\cos\theta-s\sin\theta)_+\sin\theta\,d\theta
=\tfrac12\bigl(H-s\arctan(H/s)\bigr)=\tfrac12F_H(s).
\]
The interval of base-intersecting offsets has length \(2s\sin\theta\), contributing
\(2s\int_0^{\pi/2}\sin^2\theta\,d\theta=\pi s/2\). Cauchy's perimeter formula gives \(\langle h_B\rangle=r\). Integrating over \(\varphi\) and taking the ratio of base-free to total cone-hit measure proves
\(p_H(B)=N_H(B)/(\pi r+N_H(B))\).

**2. Lower bound and rigidity.** Differentiation gives
\[
F_H''(s)=\frac{2H^3}{(H^2+s^2)^2}>0.
\]
Jensen's inequality gives \(N_H(B)\ge F_H(\langle h_B\rangle)=N_-\), with equality only when \(h_B\) is constant, hence only for the radius-\(r\) disk. Every centrally symmetric planar convex body is a zonoid: it has a nonnegative finite generating measure \(\mu\) on unoriented directions satisfying
\[
h_B(u)=\int|u\cdot v|\,d\mu(v),\qquad\mu(\mathbb{RP}^1)=a=\pi r/2.
\]
Consequently \(0\le h_B(u)\le a\). On \([0,a]\), the second derivative is at least \(2H^3/(H^2+a^2)^2\). The strong-convexity form of Jensen's inequality yields
\[
N_H(B)-N_-\ge\frac{H^3}{(H^2+a^2)^2}\operatorname{Var}_{\varphi}h_B.
\]
Using the exact difference between the two fractions in the first display and the upper bound established next yields the quantitative rigidity inequality.

**3. Sharp upper bound and completeness.** Normalize \(\mu/a\) to a probability on directions. Pointwise Jensen in the zonoid representation gives
\[
F_H(h_B(u))\le\int F_H(a|u\cdot v|)\,\frac{d\mu(v)}a.
\]
Average in \(u\) and use rotational invariance. The resulting upper envelope is the degenerate-segment average \(\langle F_H(a|\cos\varphi|)\rangle\). Differentiating it with respect to \(H\) produces
\[
\left\langle\frac{H^2}{H^2+a^2\cos^2\varphi}\right\rangle
=\frac{H}{\sqrt{H^2+a^2}}.
\]
Its value at \(H=0\) is zero, so integration gives exactly \(N_+\). Strict Jensen for distinct unoriented generating directions implies equality only for a line segment, which is not full-dimensional. Thin centrally symmetric rectangles converge to the segment while preserving perimeter; support functions and probabilities converge. Finally, \((1-t)rD+t[-ae_1,ae_1]\), for \(0\le t<1\), is full-dimensional and origin-symmetric with perimeter \(2\pi r\). Its probability varies continuously between the disk endpoint and the segment limit. Hence every intermediate value occurs.

**4. Height transition.** For fixed full-dimensional \(B\), the support function is bounded away from zero. Taylor expansion uniformly in angle gives
\(F_H(h_B)=H^3/(3h_B^2)+O_B(H^5)\), establishing the cubic expansion. For variable rectangles, in the first quadrant
\(h_{B_H}(\varphi)=a_H\cos\varphi+b_H\sin\varphi\). Write \(G(v)=1-v\arctan(1/v)\), continuously extended by \(G(0)=1\). Then \(F_H(s)=H G(s/H)\), and \(0\le G(v)\le\min\{1,1/(3v^2)\}\) for positive \(v\). Set \(\delta=\pi/2-\varphi\), \(x=a_H\delta/H\). Since \(a_H\to a\) and \(b_H/H\to\kappa\), dominated convergence (using \(\sin\delta\ge2\delta/\pi\) to control the tail) yields
\[
\lim_{H\downarrow0}\frac{N_H(B_H)}{H^2}
=\frac2{\pi a}\int_0^\infty G(x+\kappa)\,dx
=\frac{(1+\kappa^2)\arctan(1/\kappa)-\kappa}{\pi a}.
\]
The identity for the integral follows by one integration by parts or direct differentiation of both sides in \(\kappa\), with both vanishing at infinity. Since \(N_H(B_H)=O(H^2)\), replacing the denominator of \(p_H(B_H)\) by \(\pi r\) at leading order and substituting \(a=\pi r/2\) proves the transition formula. In particular its value at \(\kappa=0\) is \(1/(\pi^2r^2)\), the degenerate-segment endpoint coefficient.

## Verification

The companion `check_cone.py` uses independent angular quadrature for disk, ellipse, diamond, rectangle, and limiting segment across five cone heights. It also draws \(500000\) random normals and offsets per tested base in a common bounding interval, conditions on the cone being hit, and compares the observed base-avoiding probabilities with the analytic formula; four shape checks pass their binomial-error thresholds. Finally, direct quadrature for collapsing rectangles at four values of \(\kappa\) agrees with the predicted crossover. These finite computations verify specific examples and identities only; the claims for every convex base and every limiting sequence rely on the proof above.

Reproduce with `python check_cone.py` using Python 3, NumPy and SciPy.

## Relationship to prior work

The motion-invariant joint normal/offset law and its mean-width normalization are standard in integral geometry, explicitly recalled by van der Jagt, Jongbloed, and Vittorietti (2023), §2. The identity between a base-avoiding hitting probability and a relative mean-width increment is not claimed as a new general Crofton principle. Cruz-Orive and Gual-Arnau (2020) study stereological cylinder probes. Finch (2012) explicitly computes mean width of right and oblique circular cones and observes a circular-cone minimization within an equal-volume family of oblique circular cones. For a circular base with \(r=1\), his right-cone formula \(2\operatorname{MW}=H+\pi-rctan H\) matches our total intersecting-plane offset measure \(\pi r+N_H(B)\) exactly, providing an external normalization check. That antecedent covers the circular specialization of mean-width computation, but does not supply the fixed-perimeter extremal classification over arbitrary centrally symmetric bases, its rigidity, or its singular thin-rectangle transition. Here the additional conclusions are the *sharp fixed-perimeter extremizers over arbitrary origin-symmetric planar bases*, the support-variance rigidity bound, and the singular thin-rectangle crossover for finite cones. The circular-cone specialization is in principle recoverable from known cone mean-width data; it is not independently asserted to be novel. Prior work may contain other equivalent formulations, so historical priority is provisional.

## Limitations

Only centered-apex cones over origin-symmetric planar bases are treated; an apex shifted horizontally or a noncentrally symmetric base requires separate analysis. The upper endpoint is a supremum attained only by a degenerate segment outside the full-dimensional class. The crossover assumes short rectangle half-width divided by cone height has a finite limit; it does not cover all possible multi-scale base degenerations. The rigidity coefficient is explicit but not optimal. No independent validation has been performed.

## References

1. L. M. Cruz-Orive and X. Gual-Arnau, *Stereology with Cylinder Probes*, Image Analysis and Stereology 39 (2020), 213–218, DOI: 10.5566/ias.2433 (public November 25, 2020).
2. T. van der Jagt, G. Jongbloed, and M. Vittorietti, *Existence and approximation of densities of chord length- and cross section area distributions*, arXiv:2305.02864 (first public May 4, 2023), especially §2 on IUR planes.
3. S. R. Finch, *Oblique Circular Cones and Cylinders*, arXiv:1212.5946 (first public December 24, 2012), especially §§2–3 on cone mean width; used for historical comparison, not as the selected stereological lead source.
4. Classical Cauchy perimeter formula, planar zonoid representation, and Jensen's inequality, used explicitly in the proof.
