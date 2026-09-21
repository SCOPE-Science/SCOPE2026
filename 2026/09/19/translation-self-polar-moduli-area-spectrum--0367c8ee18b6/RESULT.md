# Exact moduli and area spectrum of a translation-self-polar planar family

## Statement

Let \(0\neq s\in\mathbb R^2\), put \(m=|s|\), rotate coordinates so that \(s=(m,0)\), and consider the planar family constructed by Segal in arXiv:2609.12685. Thus
\[
R=\sqrt{1+\frac{m^2}{4}},\qquad
p(t)=\left(\frac m2+R\frac{1-t^2}{1+t^2},\;R\frac{2t}{1+t^2}\right),
\]
\[
\lambda=\left(\frac{m+\sqrt{m^2+4}}2\right)^2,
\qquad
\Lambda_\alpha=\{0,\infty\}\cup\{\pm\alpha\lambda^n:n\in\mathbb Z\},
\]
and
\[
K_\alpha=\operatorname{conv}\{p(t):t\in\Lambda_\alpha\}.
\]
Segal proved that every \(K_\alpha\) satisfies
\[
K_\alpha^\circ=K_\alpha-s.
\]

Set
\[
\eta=\operatorname{arsinh}(m/2),
\]
so that \(R=\cosh\eta\) and \(\lambda=e^{2\eta}\), and write \(K_x:=K_{e^x}\).

Then the following hold.

1. **Exact parameter and affine-equivalence classification.**
   \[
   K_x=K_y\quad\Longleftrightarrow\quad y\equiv x\pmod{2\eta},
   \]
   while
   \[
   K_x\text{ and }K_y\text{ are affinely equivalent}
   \quad\Longleftrightarrow\quad
   y\equiv \pm x\pmod{2\eta}.
   \]
   Any affine equivalence between two members of the family is automatically a Euclidean congruence. Consequently, the family itself has a circle parameter \(\mathbb R/(2\eta\mathbb Z)\), and its affine-congruence moduli space is the interval
   \[
   \bigl(\mathbb R/(2\eta\mathbb Z)\bigr)/(x\sim -x)\cong[0,\eta].
   \]
   The map from this parameter to convex bodies is Hausdorff-continuous.

2. **Exact area law.** If \(A_\eta(x)=\operatorname{area}(K_x)\), then
   \[
   \boxed{
   A_\eta(x)=\sinh(2\eta)\sum_{n\in\mathbb Z}\operatorname{sech}(x+2n\eta).
   }
   \]
   Hence \(A_\eta\) is even, real analytic and \(2\eta\)-periodic. Poisson summation gives the Fourier series
   \[
   \boxed{
   A_\eta(x)=\frac{\pi\sinh(2\eta)}{2\eta}
   \left[
   1+2\sum_{k\ge1}
   \operatorname{sech}\!\left(\frac{\pi^2k}{2\eta}\right)
   \cos\!\left(\frac{\pi kx}{\eta}\right)
   \right].
   }
   \]

3. **Area is a strict moduli coordinate.** Let \(q=e^{-\pi^2/(2\eta)}\), and let \(k\in(0,1)\) be the elliptic modulus with nome
   \[
   q=e^{-\pi K'(k)/K(k)}.
   \]
   Then
   \[
   \boxed{
   A_\eta(x)=\frac{\sinh(2\eta)K(k)}{\eta}\,
   \operatorname{dn}\!\left(\frac{K(k)x}{\eta},k\right).
   }
   \]
   Therefore \(A_\eta\) is strictly decreasing on the fundamental moduli interval \([0,\eta]\). In particular, within Segal's family two bodies are affinely equivalent if and only if they have equal area.

4. **The two phases used by Segal are the unique area extrema modulo congruence.** Segal selected \(K_1\) and \(K_{\sqrt\lambda}\) to obtain two distinct bodies. They are precisely the endpoints \(x=0\) and \(x=\eta\) of the moduli interval, and
   \[
   \max A_\eta=A_\eta(0)=\frac{\sinh(2\eta)K(k)}{\eta},
   \]
   \[
   \min A_\eta=A_\eta(\eta)=\frac{\sinh(2\eta)K(k)}{\eta}\,k',
   \qquad k'=\sqrt{1-k^2}.
   \]
   Equivalently,
   \[
   A_\eta(0)-A_\eta(\eta)
   =\frac{2\pi\sinh(2\eta)}{\eta}
   \sum_{\substack{k\ge1\\k\text{ odd}}}
   \operatorname{sech}\!\left(\frac{\pi^2k}{2\eta}\right)>0.
   \]
   Thus the construction contains uncountably many pairwise non-affinely-equivalent solutions of \(K^\circ=K-s\), not merely two distinct solutions.

The logarithmic-phase mean area is also explicit:
\[
\frac1{2\eta}\int_0^{2\eta}A_\eta(x)\,dx
=\frac{\pi\sinh(2\eta)}{2\eta}.
\]
Since \(K_x^\circ\) is a translate of \(K_x\), the origin-based polar area product satisfies
\[
\operatorname{area}(K_x)\operatorname{area}(K_x^\circ)=A_\eta(x)^2,
\]
so it has the same strict one-parameter variation on the moduli interval.

For the concrete case \(m=2\), one has \(\eta=\operatorname{arsinh}(1)\), \(\lambda=3+2\sqrt2\), and
\[
A_\eta(0)\approx5.1157756461,\qquad
A_\eta(\eta)\approx4.9665016301.
\]

## Proof

### Parameter and affine-equivalence classification

The identity \(\Lambda_{\alpha\lambda}=\Lambda_\alpha\) immediately gives \(K_{x+2\eta}=K_x\). Conversely, every selected point \(p(t)\), \(t\in\Lambda_\alpha\), is an extreme point of \(K_\alpha\): all selected points lie on the strictly convex circle
\[
\Gamma_s=\left\{z:\left|z-\frac s2\right|=R\right\},
\]
and no point of that circle can be a nontrivial convex combination of other points from its closed disk. Thus equality of two bodies forces equality of their extreme-point sets, hence equality of the parameter sets. On the positive orbit this says
\[
e^x\lambda^{\mathbb Z}=e^y\lambda^{\mathbb Z},
\]
which is equivalent to \(y-x\in2\eta\mathbb Z\).

Now suppose an invertible affine map \(F\) sends \(K_x\) onto \(K_y\). It sends extreme points to extreme points. Hence the ellipse \(F(\Gamma_s)\) and the circle \(\Gamma_s\) have infinitely many common points. Two distinct nondegenerate conics have only finitely many intersection points, so \(F(\Gamma_s)=\Gamma_s\). An affine automorphism of a Euclidean circle is a Euclidean isometry; after centering the circle its linear part must satisfy \(A^TA=I\).

The extreme-point set has exactly two accumulation points, \(p(0)\) and \(p(\infty)\), which are antipodal. Therefore the induced circle isometry preserves this unordered pair. In angular coordinates \(\phi=2\arctan t\), the four possibilities are
\[
\phi\mapsto\phi,\quad -\phi,\quad \pi-\phi,\quad \pi+\phi,
\]
corresponding on the extended real parameter line to
\[
t\mapsto t,\quad -t,\quad 1/t,\quad -1/t.
\]
Because \(\Lambda_\alpha\) is sign-symmetric, the first two produce the same parameter orbit, while inversion sends the positive orbit \(e^x\lambda^{\mathbb Z}\) to \(e^{-x}\lambda^{\mathbb Z}\). This proves
\[
K_x\simeq_{\mathrm{aff}}K_y
\iff y\equiv\pm x\pmod{2\eta}.
\]

Hausdorff continuity follows directly from the vertex description. On a compact fundamental range of \(x\), finitely many middle orbit points vary continuously with \(x\), while the two geometric tails converge uniformly to \(p(0)\) and \(p(\infty)\). Convex hull is continuous in the Hausdorff metric.

### Area as a periodized hyperbolic secant

Write
\[
t_n=e^{x+2n\eta},\qquad
\phi_n=2\arctan t_n.
\]
The upper boundary chain has successive central-angle gaps
\[
\Delta_n=\phi_{n+1}-\phi_n.
\]
Put
\[
y_n=x+(2n+1)\eta.
\]
Using \(t_{n+1}=e^{2\eta}t_n\), the tangent subtraction formula gives
\[
\tan\frac{\Delta_n}{2}
=\frac{\sinh\eta}{\cosh y_n}.
\]
Consequently,
\[
\sin\Delta_n
=\tanh\eta\,
\bigl(\operatorname{sech}(y_n-\eta)+\operatorname{sech}(y_n+\eta)\bigr).
\]
The lower chain is the reflection of the upper chain. Triangulating from the center of \(\Gamma_s\), the two halves together give
\[
\operatorname{area}(K_x)=R^2\sum_{n\in\mathbb Z}\sin\Delta_n.
\]
Since \(R=\cosh\eta\), summing the previous identity yields
\[
A_\eta(x)=\sinh(2\eta)\sum_{n\in\mathbb Z}\operatorname{sech}(x+2n\eta).
\]
Absolute and locally uniform convergence follow from exponential decay of \(\operatorname{sech}\).

For the Fourier form, apply Poisson summation to \(f(u)=\operatorname{sech}u\), using the classical transform
\[
\widehat f(\xi)=\pi\operatorname{sech}(\pi\xi/2).
\]
This gives exactly the displayed cosine series.

Finally, the standard Fourier expansion of the Jacobi elliptic function \(\operatorname{dn}\) identifies the same cosine series. With nome \(q=e^{-\pi^2/(2\eta)}\),
\[
A_\eta(x)=\frac{\sinh(2\eta)K(k)}{\eta}
\operatorname{dn}\!\left(\frac{K(k)x}{\eta},k\right).
\]
On \(0<u<K(k)\),
\[
\frac{d}{du}\operatorname{dn}(u,k)
=-k^2\operatorname{sn}(u,k)\operatorname{cn}(u,k)<0.
\]
Hence area is strictly decreasing on \(x\in(0,\eta)\), with endpoint values obtained from \(\operatorname{dn}(0,k)=1\) and \(\operatorname{dn}(K,k)=k'\). The odd-mode difference formula follows directly from the Fourier series.

## Context and originality boundary

Segal's September 2026 preprint supplies the entire infinite-polygon construction, the arbitrary parameter \(\alpha>0\), and the identity \(K_\alpha^\circ=K_\alpha-s\). Those facts are prior work. The preprint then chooses the two phases \(\alpha=1\) and \(\alpha=\sqrt\lambda\) and proves only that they are distinct. Its current text contains no area computation, affine/congruence classification, moduli description, or elliptic-function formulation.

The new contribution here is the exact equality and affine-equivalence classification of Segal's family, the resulting interval of affine-congruence classes, the periodized-sech/Fourier/Jacobi-dn area law, and the conclusion that area is a strict complete coordinate on that interval with Segal's two chosen bodies as the unique endpoint extrema.

Earlier self-polar literature uses different equivalences. Jensen studies polytopes equal to orthogonal transforms of their polars. Fortier studies negatively self-polar ("self-nolar") planar sets satisfying a half-turn version of polarity; the relevant sections include uncountability, boundary length, and a Mahler-product example, but not translated polarity or Segal's geometric-orbit family. Makarov--Protasov study autopolar conic bodies for antinorm duality, again a different polarity setting. The Jacobi-dn Fourier expansion used above is a classical special-function identity rather than an originality claim.

To the best of our knowledge, searches for translated/self-dual polar bodies together with area, congruence, moduli, periodized hyperbolic secant, and Jacobi-elliptic formulations did not locate the theorem above. Because the motivating preprint is very recent, a later revision or an unindexed parallel observation remains a residual originality risk.

## Limitations

This result classifies only Segal's explicit planar \(\alpha\)-family; it does not classify all convex bodies satisfying \(K^\circ=K-s\). The area law is planar and is not asserted for the higher-dimensional bodies of revolution. No stability theorem is proved for perturbations away from this family. The origin-based polar area product above is not a claim about the Santaló-minimized Mahler product. 

## References

1. Alex Segal, *Self-dual sets up to a translation: a negative answer to Milman's question*, arXiv:2609.12685v1, 11 September 2026. https://arxiv.org/abs/2609.12685
2. Alathea Jensen, *Self-Polar Polytopes*, arXiv:1902.00784; later in *Polytopes and Discrete Geometry*, Contemporary Mathematics 764 (2021). https://arxiv.org/abs/1902.00784
3. John-Mark Fortier, *Self-nolar Planar Polytopes: When Finding the Polar is Rotating by Pi*, M.Sc. thesis, Concordia University, 2020. https://spectrum.library.concordia.ca/id/eprint/987044/
4. Maxim Makarov and Vladimir Yu. Protasov, *Autopolar conic bodies and polyhedra*, Mat. Sb. 216 (2025), no. 3, 156--176; arXiv:2407.04137. https://arxiv.org/abs/2407.04137
5. NIST Digital Library of Mathematical Functions, Chapter 22, §22.11, Fourier and hyperbolic series for Jacobian elliptic functions. https://dlmf.nist.gov/22.11
