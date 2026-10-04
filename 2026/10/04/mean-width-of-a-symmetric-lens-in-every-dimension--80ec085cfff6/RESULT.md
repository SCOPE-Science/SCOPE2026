# Mean width of a symmetric lens in every dimension
## Finding
For an integer \(n\ge2\) and \(0\le c<1\), define the symmetric unit lens
\[
K_n(c)=B^n(c e_1,1)\cap B^n(-c e_1,1).
\]
The two centers have distance \(2c\). For \(u\in S^{n-1}\), put \(t=|u_1|\). Then
\[
h_{K_n(c)}(u)=
\begin{cases}
\sqrt{1-c^2}\sqrt{1-t^2},&0\le t\le c,\\
1-ct,&c\le t\le1.
\end{cases}
\]
Let
\[
C_n=\frac{2\Gamma(n/2)}{\sqrt{\pi}\,\Gamma((n-1)/2)}
\]
and let the incomplete beta function be
\[
B_z(a,b)=\int_0^z s^{a-1}(1-s)^{b-1}\,ds.
\]
With mean width normalized as the spherical average of directional width, one has
\[
w_n(c)=C_n\left[\sqrt{1-c^2}\,B_{c^2}\!\left(\frac12,\frac n2\right)+B_{1-c^2}\!\left(\frac{n-1}{2},\frac12\right)-\frac{2c}{n-1}(1-c^2)^{(n-1)/2}\right].
\]
Moreover \(w_n(c)\) is strictly decreasing for \(0<c<1\), satisfies \(w_n(0)=2\), and tends to \(0\) as \(c\to1^-\). If the balls have radius \(R>0\) and their centers are distance \(d<2R\) apart, scaling gives \(R\,w_n(d/(2R))\).

## Assumptions and scope
All balls are Euclidean closed balls. The mean width is
\[
w(K)=\frac{1}{|S^{n-1}|}\int_{S^{n-1}}\bigl(h_K(u)+h_K(-u)\bigr)\,du.
\]
The lens is centrally symmetric, so its directional width is \(2h_K(u)\). The parameter range \(0\le c<1\) is exactly the nonempty-interior range for two unit balls centered at \(\pm c e_1\). The endpoint \(c=1\) is a singleton limit and is included only through the limit statement.

## Proof
Write a point as \(x=(x_1,x_\perp)\). Membership in both unit balls is equivalent to
\[
(x_1-c)^2+\|x_\perp\|^2\le1,\qquad
(x_1+c)^2+\|x_\perp\|^2\le1.
\]
Hence
\[
\|x_\perp\|^2\le1-(|x_1|+c)^2,
\qquad |x_1|\le1-c.
\]
By reflection symmetry, for a direction \(u\) with \(t=|u_1|\) it is enough to take \(x_1\ge0\) and \(x_\perp\) parallel to the perpendicular component of \(u\). Put \(q=\sqrt{1-t^2}\) and \(y=x_1+c\). Then \(y\in[c,1]\) and
\[
h_{K_n(c)}(u)=\max_{c\le y\le1}\left[t(y-c)+q\sqrt{1-y^2}\right].
\]
The unconstrained maximizer of \(ty+q\sqrt{1-y^2}\) on \([0,1]\) is \(y=t\). Therefore the constrained maximizer is \(y=c\) when \(t\le c\), and \(y=t\) when \(t\ge c\). Substitution gives the displayed piecewise support function.

For a uniformly distributed \(U\in S^{n-1}\), the random variable \(T=|U_1|\) has density
\[
g_n(t)=C_n(1-t^2)^{(n-3)/2},\qquad 0\le t\le1.
\]
Since the lens is centrally symmetric,
\[
\begin{aligned}
w_n(c)=2C_n\Bigg[&\sqrt{1-c^2}\int_0^c(1-t^2)^{(n-2)/2}\,dt\\
&+\int_c^1(1-ct)(1-t^2)^{(n-3)/2}\,dt\Bigg].
\end{aligned}
\]
The three elementary beta reductions are
\[
\int_0^c(1-t^2)^{(n-2)/2}\,dt
=\frac12B_{c^2}\!\left(\frac12,\frac n2\right),
\]
\[
\int_c^1(1-t^2)^{(n-3)/2}\,dt
=\frac12B_{1-c^2}\!\left(\frac{n-1}{2},\frac12\right),
\]
and
\[
\int_c^1t(1-t^2)^{(n-3)/2}\,dt
=\frac{(1-c^2)^{(n-1)/2}}{n-1}.
\]
Substituting them proves the closed formula.

Differentiation under the two integrals is legitimate for \(0<c<1\); the boundary terms cancel because the two support-function branches agree at \(t=c\). This yields
\[
w_n'(c)=-2C_n\left[\frac{c}{\sqrt{1-c^2}}\int_0^c(1-t^2)^{(n-2)/2}\,dt+\frac{(1-c^2)^{(n-1)/2}}{n-1}\right]<0.
\]
The endpoint values follow directly from the support function. Homogeneity of support functions proves the radius-\(R\) scaling statement.

For \(n=3\), one has \(C_3=1\). Writing \(c=\cos\phi\) and \(\sqrt{1-c^2}=\sin\phi\), the integral form simplifies to
\[
w_3(c)=2-2\cos\phi+\left(\frac\pi2-\phi\right)\sin\phi,
\]
which is exactly the three-dimensional symmetric-lens formula recorded by Finch.

## Verification
The proof is analytic and does not depend on finite enumeration. The accompanying `verify.py` performs three independent numerical diagnostics: it compares the piecewise support function with direct one-variable maximization, checks the spherical one-dimensional integral against Finch's closed \(n=3\) formula at several separations, and checks strict decrease on a grid for several dimensions. These numerical tests are supplementary; the support maximization, beta reductions, and derivative sign above are the proof.

## Relationship to prior work
Finch's 2013 paper *Mutually Equidistant Spheres that Intersect* treats the three-dimensional symmetric lens, records its mean width, gives higher-dimensional formulas for volume and surface area, and then explicitly states that an analogous higher-dimensional formula for mean width was not attempted. The same paper points to older quermassintegral formulas for volume and surface area and notes the three-dimensional relation between mean width and the relevant quermassintegral.

Bezdek's later work on intersections of congruent balls formulates intrinsic-volume inequalities for \(r\)-ball bodies and uses the mean width through the first intrinsic volume, but the inspected statements do not provide the explicit arbitrary-dimensional symmetric-lens mean-width formula above. Drach and Tatarko subsequently prove sharp mean-width extremal theorems for \(\lambda\)-convex lenses in every dimension and use the lens support function abstractly; the inspected full text likewise does not state the closed beta-function evaluation here.

## Limitations
No claim is made that this formula is the first possible derivation from the full historical quermassintegral literature. Finch cites Hadwiger's 1957 book for older quermassintegral expressions, but that source was not available in sufficiently inspectable form here; an equivalent formula hidden there or in other unindexed literature remains the principal originality risk. The result concerns the intersection of exactly two congruent balls. It does not give higher intrinsic volumes of general ball intersections, nor does it reprove the later extremal theorems for all \(\lambda\)-convex bodies.

## References
1. Steven R. Finch, *Mutually Equidistant Spheres that Intersect*, arXiv:1301.5515v1, 2013.
2. Károly Bezdek, *Volumetric bounds for intersections of congruent balls*, arXiv:1912.05118v1; later published in *Aequationes Mathematicae*.
3. Kostiantyn Drach and Kateryna Tatarko, *A solution to Bezdek's conjecture*, arXiv:2511.11901v1, 2025.
4. Hugo Hadwiger, *Vorlesungen über Inhalt, Oberfläche und Isoperimetrie*, Springer, 1957, pp. 215–221, cited by Finch for quermassintegral formulas.