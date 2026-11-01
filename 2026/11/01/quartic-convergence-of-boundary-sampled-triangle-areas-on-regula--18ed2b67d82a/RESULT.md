# Quartic convergence of boundary-sampled triangle areas on regular polygons

## Finding
For an integer \(m\ge3\), let \(P_m\) be a regular Euclidean \(m\)-gon. Choose \(X_1,X_2,X_3\) independently and uniformly by **arclength along its edges**. Let \(T_m=\operatorname{area}(\operatorname{conv}\{X_1,X_2,X_3\})\), \(A_m=\operatorname{area}(P_m)\), and \(Z_m=T_m/A_m\). Then, with \(\theta_m=\pi/m\),
\[
\boxed{\mathbb E Z_m=\frac{1+\tfrac32\cot^2\theta_m}{m^2},\qquad
\mathbb E Z_m^2=\frac{(1+2\cos^2\theta_m)^2}{24m^2\sin^2\theta_m\cos^2\theta_m}.}
\]
The mean \(\mathbb E Z_m\) is **strictly decreasing** over integers \(m\ge3\); in particular,
\[
\boxed{\frac3{2\pi^2}<\mathbb E Z_m\le\frac16,}
\]
with equality at the upper endpoint exactly for \(m=3\), while the lower endpoint is an unattained limit. The convergence to the disk value is quartic, not quadratic:
\[
\mathbb E Z_m=\frac3{2\pi^2}+\frac{\pi^2}{10m^4}+\frac{\pi^4}{63m^6}+O(m^{-8}).
\]
The exact variance is \(\operatorname{Var}(Z_m)=\mathbb E Z_m^2-(\mathbb E Z_m)^2\). Moreover,
\[
\mathbb E Z_m^2=\frac3{8\pi^2}+\frac{\pi^2}{15m^4}+\frac{2\pi^4}{63m^6}+O(m^{-8}),
\]
so \(\operatorname{Var}(Z_m)\to\frac3{8\pi^2}-\frac9{4\pi^4}\), also with a quartic first correction. Here all sampling is on the **continuous polygonal perimeter**; sampling vertices is a different random model.

## Assumptions and scope
The polygon is regular and nondegenerate, with exactly \(m\ge3\) equal Euclidean sides; sampling has the normalized one-dimensional Hausdorff (arclength) measure and is independent with replacement. The three sampled points are almost surely distinct. Ratios and all formulas are invariant under similarity of the containing regular polygon. The assertions do not concern area-uniform interior samples or samples taken from the discrete vertex set.

## Proof
Normalize the circumradius to one, and write \(s=\sin(\pi/m)\), \(c=\cos(\pi/m)\), \(\theta=\pi/m\). Each side has length \(\ell=2s\), its midpoint lies on the circle of radius \(c\), and \(A_m=msc\). Each sample picks one of the \(m\) sides with probability \(1/m\), then a uniform point on that side.

**Distinct-edge contribution.** If the three selected sides have distinct cyclic indices \(i<j<k\), then the three points occur in the same orientation as those sides around the convex boundary. Their positively oriented triangle area is separately affine-linear in the position of each point, so its conditional expectation is the area of the triangle with the three corresponding edge midpoints. Let \(S_m\) be the sum of these midpoint-triangle areas over \(i<j<k\). Writing the positive cyclic index gaps as \(a,b,d\), with \(a+b+d=m\), and summing the standard sine-area formula of an inscribed triangle yields
\[
 S_m=\frac{mc^2}{2}\sum_{a=1}^{m-2}(m-a-1)\sin(2\pi a/m)
 =\frac{m^2c^2}{4}\cot(\pi/m).
\]
For the final equality use \(\sum_{a=1}^{m-1}\sin(2\pi a/m)=0\) and \(\sum_{a=1}^{m-1}a\sin(2\pi a/m)=-(m/2)\cot(\pi/m)\); the term at \(a=m-1\) has coefficient zero. The probability for any unordered distinct-edge triple is \(6/m^3\), so this contribution to \(\mathbb E T_m\) is \(3c^2\cot(\theta)/(2m)\).

**Repeated-edge contribution.** If exactly two samples occupy side \(i\) and the third occupies another side \(j\), the expected separation of the two points along side \(i\) is \(\ell/3\). The average perpendicular distance of a uniform point on side \(j\) from the supporting line of \(i\) is \(h_{ij}=c[1-\cos(2\pi(j-i)/m)]\). Their conditional triangle area is therefore \(\ell h_{ij}/6\). The probability of this edge-label pattern is \(3/m^3\). Since \(\sum_{i=0}^{m-1}\sum_{j\ne i}h_{ij}=m^2c\), the total repeated-edge contribution is \(\ell c/(2m)=sc/m\). Three samples on one side give zero area. Adding contributions and dividing by \(A_m=msc\) proves the first exact formula.

**Second moment.** The sample \(X\) has mean zero by rotational symmetry. Parametrizing an edge by \((1-t)v_i+tv_{i+1}\) with \(t\) uniform on \([0,1]\), direct integration gives \(\mathbb E\|X\|^2=(2+\cos2\theta)/3=(1+2c^2)/3\). Rotational symmetry implies \(\Sigma=\operatorname{Cov}(X)=(1+2c^2)I_2/6\). For three independent centered planar vectors with covariance \(\Sigma\), expanding the oriented determinant and conditioning away the mixed terms gives
\[
 \mathbb E\det(X_2-X_1,X_3-X_1)^2=6\det\Sigma.
\]
Since \(T_m^2=\frac14\det(X_2-X_1,X_3-X_1)^2\), we obtain \(\mathbb E T_m^2=\frac32\det\Sigma=(1+2c^2)^2/24\). Division by \(A_m^2\) completes the exact second-moment formula.

**Strict ordering and rates.** For \(z=\pi/m\), rewrite the normalized mean as
\[
 Q(z)=\frac{z^2}{2\pi^2}\bigl(3\csc^2z-1\bigr).
\]
A derivative calculation shows that the sign of \(Q'(z)\), for \(0<z\le\pi/3\), is the sign of \(H(z)=3(\sin z-z\cos z)-\sin^3z\). Since \(H(0)=0\) and \(H'(z)=3\sin z\,(z-\sin z\cos z)>0\), the function \(Q\) increases strictly with \(z\), hence decreases strictly with \(m\). Substitution \(m=3\) gives \(1/6\); the limit at \(z=0\) is \(3/(2\pi^2)\). Finally, Taylor expansion of the displayed exact formulas at \(z=0\) gives the stated quartic and sixth-order terms. In particular the would-be \(m^{-2}\) terms cancel **exactly** in both moments.

## Verification
The companion standalone `check.py` recomputes the distinct- and repeated-edge contributions numerically from their unsimplified sums; tests the exact mean and second moments against independently sampled triangles for several side counts; and checks the strict sequence ordering and analytic quartic coefficients. The proof above, rather than the finite checks, establishes the claims for every integer \(m\ge3\).

## Relationship to prior work
Reitzner, Schütt and Werner (arXiv:1911.05917, first public November 14, 2019) study random hulls sampled on the boundaries of simple polytopes and prove large-sample volume-deficit asymptotics. Their sample-size limit does not determine the present fixed-three-point moment spectrum as the **number of sides varies**. Madras and KC (2006) give exact mean areas for triangles chosen from **three distinct vertices** of a regular polygon, with a different formula and sampling rule. Here samples may occupy the same edge; the repeated-edge contribution is essential and cancels the quadratic correction after area normalization. The known circle boundary-triangle mean is the limiting value, not a claim of novelty. Earlier exact cases for triangles and parallelograms are special members of the present sequence.

## Limitations
No assertion is made about the full probability distribution, nonregular polygons, other sample sizes, higher-dimensional bodies, or the monotonicity of the variance. Historical priority is provisional; the exact formula may appear in older scattered classical-geometric-probability literature not found in the bounded searches. The second-moment identity is a general covariance identity and is not asserted to be newly discovered on its own.

## References
1. M. Reitzner, C. Schütt and E. M. Werner, *The convex hull of random points on the boundary of a simple polytope*, arXiv:1911.05917 (first public November 14, 2019), https://arxiv.org/abs/1911.05917.
2. A. Madras and S. KC, *Randomly Generated Triangles whose Vertices are Vertices of Regular Polygons*, Rose-Hulman Undergraduate Mathematics Journal **7**(2), Article 12 (2006), https://scholar.rose-hulman.edu/rhumj/vol7/iss2/12/.
