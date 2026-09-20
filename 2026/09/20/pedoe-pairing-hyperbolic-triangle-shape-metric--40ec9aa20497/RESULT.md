# The Neuberg–Pedoe pairing is the hyperbolic metric on triangle shape space

**Same-model review: passed. Independent audit: not yet performed.**

## Result

Let \(T\) and \(T'\) be nondegenerate labeled Euclidean triangles with corresponding side lengths
\[
(a,b,c),\qquad (a',b',c')
\]
and areas \(\Delta,\Delta'>0\). Define the Neuberg–Pedoe pairing
\[
\mathcal P(T,T')
=(a')^2(b^2+c^2-a^2)
+(b')^2(c^2+a^2-b^2)
+(c')^2(a^2+b^2-c^2).
\]

Represent a labeled triangle shape by its Bookstein coordinate: after an orientation-preserving similarity, put the first two labeled vertices at \(0,1\) and the third at \(z\in\mathbb H\). Let \(d_{\rm sh}(T,T')\) be the Poincaré hyperbolic distance between the two Bookstein coordinates.

Then
\[
\boxed{\;
\cosh d_{\rm sh}(T,T')
=\frac{\mathcal P(T,T')}{16\Delta\Delta'}.
\;}
\]

Consequently, the classical Neuberg–Pedoe inequality is exactly the nonnegativity of hyperbolic distance:
\[
\mathcal P(T,T')\ge 16\Delta\Delta',
\]
and its defect is the exact intrinsic shape-distance defect
\[
\boxed{\;
\mathcal P(T,T')-16\Delta\Delta'
=32\Delta\Delta'\sinh^2\!\left(\frac{d_{\rm sh}(T,T')}{2}\right).
\;}
\]
Equality holds exactly when the two labeled triangles are similar with the prescribed side correspondence.

## Lorentz-hyperboloid formulation

For squared-side triples
\[
x=(a^2,b^2,c^2),\qquad y=((a')^2,(b')^2,(c')^2),
\]
define the bilinear form
\[
B(x,y)=\Bigl(\sum_i x_i\Bigr)\Bigl(\sum_i y_i\Bigr)-2\sum_i x_i y_i.
\]
This form has signature \((1,2)\). Heron's identity gives
\[
B(x,x)=16\Delta^2,\qquad B(y,y)=16(\Delta')^2,
\]
while direct expansion gives
\[
B(x,y)=\mathcal P(T,T').
\]
Thus
\[
\widehat x=\frac{x}{4\Delta},\qquad
\widehat y=\frac{y}{4\Delta'}
\]
lie on the positive unit hyperboloid \(B(v,v)=1\), and
\[
B(\widehat x,\widehat y)=\cosh d_{\rm sh}(T,T').
\]
Hence the squared-side triple, normalized by area, is a Lorentz-hyperboloid coordinate for triangle similarity shape.

## Proof in Bookstein coordinates

Normalize \(T\) to vertices \(0,1,z\), with \(z=x+iy\), \(y>0\), and normalize \(T'\) to \(0,1,w\), with \(w=u+iv\), \(v>0\). Under the usual side convention,
\[
a^2=(1-x)^2+y^2,\qquad b^2=x^2+y^2,\qquad c^2=1,\qquad \Delta=\frac y2,
\]
and analogously
\[
(a')^2=(1-u)^2+v^2,\qquad (b')^2=u^2+v^2,\qquad (c')^2=1,\qquad \Delta'=\frac v2.
\]
Substitution into \(\mathcal P\) yields
\[
\mathcal P(T,T')
=2\bigl((x-u)^2+y^2+v^2\bigr).
\]
Since \(16\Delta\Delta'=4yv\),
\[
\frac{\mathcal P(T,T')}{16\Delta\Delta'}
=
1+\frac{(x-u)^2+(y-v)^2}{2yv},
\]
which is exactly the Poincaré half-plane formula for \(\cosh d_{\rm sh}(z,w)\).

## Corollary 1: an exact unlabeled-shape distance formula

If vertex labels and reflections are forgotten, the quotient shape distance is the minimum over the six side correspondences. Writing
\[
S=\sum_i x_i,\qquad S'=\sum_i y_i,
\]
one obtains
\[
\boxed{\;
\cosh d_{\rm unlab}(T,T')
=
\frac{SS'-2\max_{\sigma\in S_3}\sum_i x_i y_{\sigma(i)}}
{16\Delta\Delta'}.
\;}
\]
By the rearrangement inequality, the maximum is attained by pairing the squared side lengths in the same sorted order. Thus the intrinsic hyperbolic distance between ordinary unlabeled triangle shapes has a closed expression requiring only the two sorted side triples and the two areas.

## Corollary 2: Weitzenböck is an exact radial identity

Let \(E\) be the equilateral shape. Then
\[
\boxed{\;
\cosh d_{\rm sh}(T,E)
=\frac{a^2+b^2+c^2}{4\sqrt3\,\Delta}.
\;}
\]
Therefore Weitzenböck's inequality
\[
a^2+b^2+c^2\ge 4\sqrt3\,\Delta
\]
is the radial inequality \(d_{\rm sh}(T,E)\ge0\), with the exact defect formula
\[
\boxed{\;
a^2+b^2+c^2-4\sqrt3\,\Delta
=
8\sqrt3\,\Delta\,
\sinh^2\!\left(\frac{d_{\rm sh}(T,E)}2\right).
\;}
\]
Equivalently,
\[
\frac{4\sqrt3\,\Delta}{a^2+b^2+c^2}
=\operatorname{sech} d_{\rm sh}(T,E).
\]
Thus near the equilateral shape the normalized Weitzenböck defect is intrinsically quadratic:
\[
\frac{a^2+b^2+c^2}{4\sqrt3\,\Delta}-1
=\frac12 d_{\rm sh}(T,E)^2+O(d_{\rm sh}^4).
\]

## Corollary 3: symmetry and right-angle loci are geodesic coordinates

In Bookstein's upper half-plane, the three isosceles loci are the geodesics fixed by the three vertex transpositions. For example, the locus \(a=b\) is \(\operatorname{Re}z=\tfrac12\), and
\[
\boxed{\;
\operatorname{dist}_{\mathbb H}(T,\{a=b\})
=
\operatorname{arsinh}\!\left(\frac{|a^2-b^2|}{4\Delta}\right).
\;}
\]
The other two formulas follow by permuting the side labels.

Likewise, the locus where the angle \(C\) is right is the hyperbolic geodesic with Euclidean endpoints \(0,1\). Its distance from \(T\) is
\[
\boxed{\;
\operatorname{dist}_{\mathbb H}(T,\{C=\pi/2\})
=
\operatorname{arsinh}\!\left(\frac{|a^2+b^2-c^2|}{4\Delta}\right)
=
\operatorname{arsinh}|\cot C|.
\;}
\]
With a choice of side of the geodesic, the signed normal coordinate is
\[
\operatorname{arsinh}(\cot C)=\log\cot\frac C2.
\]
Hence the sets of Euclidean triangles with a fixed labeled angle are hypercycles parallel to the corresponding right-triangle geodesic.

## Context and relation to prior work

Pedoe's 1941 two-triangle inequality is the classical source of the pairing above, and Mitrinović–Pečarić later gave a broad treatment of Neuberg–Pedoe and Oppenheim inequalities. Separately, Perdomo–Plaza use Bookstein coordinates and the Poincaré hyperbolic metric as a space of Euclidean triangle similarity shapes in work on triangle refinement dynamics. Their 2023 presentation explicitly gives
\[
\cosh d(z,w)=1+\frac{|z-w|^2}{2\,\operatorname{Im}z\,\operatorname{Im}w}.
\]
A 2024 paper of Çoruh Şenocak–Yüce relates Pedoe-type inequalities for triangles *in a Lorentzian plane* to hyperbolic-cosine formulas. That is a different geometric setting from the Euclidean triangle similarity-shape space considered here.

The contribution recorded here is the exact identification of the classical Euclidean Neuberg–Pedoe pairing with the Poincaré distance on Euclidean triangle similarity space, together with the Lorentz squared-side model and the resulting exact unlabeled, equilateral, isosceles, and right-angle distance formulas.

## Limitations

- The metric is the Poincaré/Bookstein hyperbolic metric on triangle shape space; it is not Kendall's spherical/Procrustes shape metric.
- The main identity concerns nondegenerate Euclidean triangles. Degenerate shapes occur at the ideal boundary and are at infinite hyperbolic distance.
- The labeled formula depends on a prescribed side correspondence. The quotient formula above handles relabeling and reflection when ordinary unlabeled shapes are desired.
- Originality is to the best of our knowledge. The identity is algebraically elementary once the two previously separate descriptions are placed side by side, so an equivalent formulation may exist under different terminology.
- The full text of Mitrinović–Pečarić (1988), a comprehensive review of Neuberg–Pedoe refinements, was not inspected; this is the most relevant unresolved literature-coverage risk located.

## References

1. D. Pedoe, “An inequality connecting any two triangles,” *The Mathematical Gazette* 25 (1941), 310–311. https://doi.org/10.2307/3606570
2. D. S. Mitrinović and J. E. Pečarić, “About the Neuberg-Pedoe and the Oppenheim inequalities,” *J. Math. Anal. Appl.* 129 (1988), 196–210. https://doi.org/10.1016/0022-247X(88)90242-9
3. F. Perdomo and Á. Plaza, “Proving the non-degeneracy of the longest-edge trisection by a space of triangular shapes with hyperbolic metric,” *Applied Mathematics and Computation* 221 (2013), 424–432. https://doi.org/10.1016/j.amc.2013.06.075
4. F. Perdomo and Á. Plaza, “Similarity Classes of the Longest-Edge Trisection of Triangles,” *Axioms* 12 (2023), 913. https://doi.org/10.3390/axioms12100913
5. S. Çoruh Şenocak and S. Yüce, “Geometric approaches to establish the fundamentals of Lorentz spaces \(\mathbb R^3_2\) and \(\mathbb R^2_1\),” *Mathematica Bohemica* 149 (2024), 549–567. https://doi.org/10.21136/MB.2024.0111-23
