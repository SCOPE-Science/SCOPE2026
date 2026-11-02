# Sharp small-perimeter-error law and parity of optimal polygon-edge sampling

## Finding

Let \(P\) be any nondegenerate convex planar polygon with \(m\ge3\) genuine vertices, successive edge lengths \(L_i>0\), and interior vertex angles \(0<\alpha_i<\pi\). Choose each of \(n\) independent boundary points by first choosing edge \(i\) with fixed probability \(w_i>0\), \(\sum_i w_i=1\), and then choosing arclength uniformly on that edge. If \(H_n\) is their convex hull, let \(D_n=\operatorname{per}(P)-\operatorname{per}(H_n)\). Set \(\lambda_i=w_i/L_i\) and
\[
F_\alpha(x,y)=x+y-\sqrt{x^2+y^2-2xy\cos\alpha}.
\]
Index all edges and vertices cyclically, with edge \(i\) running from vertex \(i\) to vertex \(i+1\). Then
\[
nD_n\ \xrightarrow{d}\ Z=\sum_{i=1}^{m}F_{\alpha_i}(X_i,Y_i),
\]
where the \(2m\) variables are mutually independent, \(X_i\sim\mathrm{Exp}(\lambda_{i-1})\), and \(Y_i\sim\mathrm{Exp}(\lambda_i)\). Every fixed positive integer moment converges. Most importantly, the limiting law has the exact small-deficit asymptotic
\[
\boxed{\lim_{\varepsilon\downarrow0}\varepsilon^{-m}\Pr(Z\le\varepsilon)
=\frac1{m!}\prod_{i=1}^{m}\frac{\lambda_{i-1}+\lambda_i}{1+\cos\alpha_i}.}
\]

For a regular \(m\)-gon of perimeter \(P_0\), this coefficient is at most
\[
\boxed{\frac1{m!}\left(\frac{2}{P_0[1-\cos(2\pi/m)]}\right)^m.}
\]
When \(m\) is odd, equality holds **only** for \(w_i=1/m\) on every edge. When \(m\) is even, equality holds **exactly** for the positive alternating allocations \(w_{2j}=u\), \(w_{2j+1}=v\), where \(u+v=2/m\). In particular, uniform edge sampling is the unique small-deficit optimal design for regular odd polygons but not for regular even polygons. This is a claim about \(n\to\infty\) followed by \(\varepsilon\downarrow0\), not finite-\(n\) optimality.

For uniform-arclength sampling on the regular polygon, write \(s=\sin(\alpha/2)\), \(c=\cos(\alpha/2)\), \(\alpha=\pi-2\pi/m\). An additional moment identity is
\[
\lim_{n\to\infty}n\mathbb E D_n
=mP_0\left[1-\frac{s^2}{c}\operatorname{arsinh}(c/s)\right].
\]

## Assumptions and scope

The underlying polygon is fixed, convex and two-dimensional. Each vertex is a genuine corner (no adjacent collinear edges), the number \(m\) is fixed, and all sampling weights are fixed positive numbers independent of \(n\). Perimeter is the ordinary Euclidean perimeter of a nondegenerate planar convex set. Exceptional sample configurations with fewer than three noncollinear points may be assigned zero hull perimeter; their probabilities decay exponentially, so they do not affect any asserted limit. The limit \(Z\) has units of length.

## Proof

**1. Exact corner shortcuts.** Let \(A_n\) be the event that every polygon edge contains at least one sample. For vertex \(i\), let \(a_{i,n}\) and \(b_{i,n}\) be the distances from that vertex to the closest samples along the incident preceding and following edges, respectively. On \(A_n\), the hull connects the two closest samples near each vertex by a straight chord and otherwise follows the sampled edge-spans. The two boundary legs displaced by that chord have total length \(a_{i,n}+b_{i,n}\), whereas the chord has length \(\sqrt{a_{i,n}^2+b_{i,n}^2-2a_{i,n}b_{i,n}\cos\alpha_i}\). Therefore, exactly,
\[
D_n=\sum_{i=1}^{m}F_{\alpha_i}(a_{i,n},b_{i,n})\quad\text{on }A_n.
\]
The missing-edge probability satisfies \(\Pr(A_n^c)\le\sum_i(1-w_i)^n\).

**2. Independent exponential endpoint limit.** Fix nonnegative thresholds for all \(2m\) nearest-endpoint distances, scaled by \(n\). For sufficiently large \(n\), their marked arcs are disjoint. A single point falls in their union with probability \(n^{-1}\) times the sum of the thresholds weighted by the respective \(\lambda_i\). Hence the joint avoidance probability equals \((1-B/n)^n\to e^{-B}\), the joint survival function of \(2m\) independent exponentials with the specified rates. Continuous mapping and the exponentially small \(A_n^c\) prove the displayed distributional convergence.

**3. Moment convergence.** Define each nearest-endpoint distance as its edge length when no sample lies on that edge. For any such variable \(M_{i,n}\), \(\Pr(nM_{i,n}>t)\le e^{-\lambda_i t}\) for all \(t\ge0\), using the binomial no-hit formula up to the endpoint and zero thereafter. On \(A_n\), \(0\le F_\alpha(x,y)\le x+y\). On its complement, \(0\le D_n\le\operatorname{per}(P)\). Therefore \(nD_n\) is bounded by a sum of \(2m\) uniformly exponentially tailed variables plus \(n\operatorname{per}(P)\mathbf1_{A_n^c}\). Uniform bounds on every moment of sufficiently higher order follow, giving convergence of every fixed positive integer moment.

**4. The sharp one-corner small-loss constant.** Fix \(0<\alpha<\pi\), independent exponential variables with respective rates \(\lambda,\mu>0\), and put \(q=1+\cos\alpha\in(0,2)\). The function \(F_\alpha(x,y)\) is nondecreasing in each variable, with \(\lim_{x\to\infty}F_\alpha(x,y)=qy\). Solving \(F_\alpha(x,y)=z\) gives, for \(y>z/q\), the threshold
\[
x_z(y)=\frac{z(y-z/2)}{qy-z}.
\]
For \(0<y\le z/q\), every \(x\ge0\) satisfies \(F_\alpha(x,y)\le z\). Consequently its exact cumulative distribution is
\[
\Pr(F_\alpha(X,Y)\le z)=1-e^{-\mu z/q}
+\int_{z/q}^{\infty}\mu e^{-\mu y}(1-e^{-\lambda x_z(y)})\,dy.
\]
Split the integral at \(y=\sqrt z\). On \(y\ge\sqrt z\), \(x_z(y)=z/q+O(z^2/y)\), so the integral is \(\lambda z/q+o(z)\). On the remaining interval the integral is \(O(z^{3/2}+z^2|\log z|)=o(z)\), using the explicit expression for \(x_z(y)\) and \(1-e^{-v}\le\min(1,v)\). Together with \(1-e^{-\mu z/q}=\mu z/q+O(z^2)\), this proves
\[
\Pr(F_\alpha(X,Y)\le z)=\frac{\lambda+\mu}{1+\cos\alpha}\,z+o(z).
\]
The one-corner variables in \(Z\) are independent. Convolution of their near-zero measures over the simplex \(\{t_i\ge0:\sum_i t_i\le1\}\), of volume \(1/m!\), proves the stated sharp \(\varepsilon^m\) coefficient.

**5. Parity and optimal sampling.** For a regular polygon all lengths equal \(L=P_0/m\) and \(1+\cos\alpha=1-\cos(2\pi/m)\). Apart from a fixed positive factor, the small-deficit coefficient is
\[
\prod_{i=1}^{m}(w_{i-1}+w_i).
\]
Their arithmetic mean is \(2/m\), so AM–GM proves the claimed upper bound, with equality precisely when every \(w_{i-1}+w_i=2/m\). These linear equations give \(w_i=w_{i-2}\). For odd \(m\) this forces uniform weights; for even \(m\) it permits exactly two alternating positive values summing to \(2/m\).

**6. Uniform-weight moment identity.** At each corner of a regular polygon, both exponentials have rate \(1/P_0\). Their sum \(T\) is gamma with mean \(2P_0\), and their proportion \(U=X/T\) is independent uniform on \([0,1]\). Thus
\[
\mathbb E F_\alpha(X,Y)=2P_0\left[1-\int_0^1\sqrt{s^2+c^2(2u-1)^2}\,du\right]
=P_0\left[1-\frac{s^2}{c}\operatorname{arsinh}(c/s)\right].
\]
Multiply by the number of vertices and apply Step 3.

## Verification

The complete standalone `verify.py` uses only the Python standard library. Execute `python verify.py`. It checks the exact chord-shortcut decomposition against an independently implemented convex hull for regular triangles, quadrilaterals, pentagons and heptagons, verifies the near-zero one-corner coefficient by direct numerical integration of its exact distribution, checks the AM–GM optimization/parity cases, and compares the regular-polygon mean with independent exponential simulation. All tests returned `ALL_CHECKS_PASSED`. Numerical agreement is not used in place of the proof.

## Relationship to prior work

Reitzner, Schütt and Werner (arXiv:1911.05917, November 14, 2019) study random boundary polytopes, their expected face numbers, and expected missing volume. These results motivate polygon-boundary sampling but do not state the sharp perimeter-deficit small-ball coefficient or its optimizing edge-weight classification. Prochno, Schütt, Sonnleitner and Werner (arXiv:2404.02870, April 3, 2024) establish sharp Hausdorff-distance behavior for randomly inscribed polygons, exploiting independent local endpoint limits; their observable is a maximum-distance statistic rather than the sum of chord-shortcut perimeter losses. Exponential endpoint behavior is an established tool and is not itself claimed as new. An independent earlier missing-area calculation also uses products of endpoint variables but does not imply the present exact perimeter small-ball coefficient and risk-optimal parity classification without additional analysis. The new claim is specifically the sharp small-perimeter-error law and its odd/even sampling rigidity; the limiting representation is supplied to prove and interpret it.

## Limitations

The order of limits is \(n\to\infty\) first, then the permitted perimeter-loss threshold tends to zero; the results do not compare fixed sample sizes or weights that vary with \(n\). The optimizers are for the leading extremely-small-error probability, not for expected perimeter deficit, Hausdorff loss, or missed area. The proof covers neither curved boundaries nor zero-probability edges. No exhaustive historical-priority claim or independent mathematical certification is made.

## References

1. M. Reitzner, C. Schütt, E. M. Werner, *The convex hull of random points on the boundary of a simple polytope*, arXiv:1911.05917 (first version November 14, 2019), https://arxiv.org/abs/1911.05917.
2. J. Prochno, C. Schütt, M. Sonnleitner, E. M. Werner, *Random approximation of convex bodies in Hausdorff metric*, arXiv:2404.02870 (first version April 3, 2024), https://arxiv.org/abs/2404.02870.
