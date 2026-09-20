# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The central identity is verified by two equivalent derivations.

First, normalize two labeled Euclidean triangles to Bookstein coordinates \(z=x+iy\) and \(w=u+iv\) in the upper half-plane. Their squared sides and areas are
\[
a^2=(1-x)^2+y^2,\quad b^2=x^2+y^2,\quad c^2=1,\quad \Delta=y/2,
\]
and analogously for \(w\). Direct expansion gives
\[
\mathcal P=2((x-u)^2+y^2+v^2),
\]
hence
\[
\mathcal P/(16\Delta\Delta')
=
1+\frac{|z-w|^2}{2\,\operatorname{Im}z\,\operatorname{Im}w}
=\cosh d_{\mathbb H}(z,w).
\]

Second, for squared-side triples \(x,y\), the bilinear form
\[
B(x,y)=(\sum x_i)(\sum y_i)-2\sum x_i y_i
\]
has signature \((1,2)\); Heron's identity gives \(B(x,x)=16\Delta^2\), and \(B(x,y)\) is exactly the Neuberg–Pedoe pairing. Normalization by \(4\Delta\) therefore places each shape on the unit hyperboloid and recovers the same hyperbolic cosine.

The defect formula follows from \(\cosh d-1=2\sinh^2(d/2)\). The unlabeled formula follows by minimizing over the six isometric relabelings and then applying the rearrangement inequality. The equilateral formula is the special case in which the second triangle is equilateral. The isosceles-distance formula is the standard distance to the vertical geodesic \(\operatorname{Re}z=1/2\). The right-angle formula follows by mapping the geodesic with endpoints \(0,1\) to a vertical geodesic; the algebra reduces its signed normal coordinate to \((a^2+b^2-c^2)/(4\Delta)=\cot C\).

Boundary and equality checks are consistent: similar corresponding triangles give \(d=0\) and equality in Pedoe; equilateral triangles give equality in Weitzenböck; approaching a degenerate triangle sends \(\operatorname{Im}z\to0\) and the intrinsic distance to the ideal boundary diverges.

## Originality

**PASS, to the best of our knowledge.** Searches were made under Neuberg–Pedoe/Pedoe, hyperbolic distance, Poincaré metric, Bookstein coordinates, triangle shape space, Lorentz/hyperboloid, Weitzenböck, isosceles locus, and right-triangle locus terminology, including equivalent squared-side formulations.

The classical Pedoe literature supplies the two-triangle inequality and equality characterization. Perdomo–Plaza (2013, 2023) supplies the Poincaré hyperbolic metric on Euclidean triangle similarity space and explicitly writes the half-plane distance formula, but the located text does not identify that distance with the Neuberg–Pedoe pairing. Çoruh Şenocak–Yüce (2024) is the closest conceptual neighbor found: it derives Pedoe-type inequalities for triangles living in the Lorentzian plane using hyperbolic-cosine formulas. Its objects and theorem statements are different from the Euclidean triangle similarity-shape metric here.

No located source states the exact identity
\[
\cosh d_{\rm sh}=\mathcal P/(16\Delta\Delta'),
\]
the sorted-side formula for the unlabeled quotient distance, or the stated exact Weitzenböck/isosceles/right-angle distance dictionary.

The strongest residual risk is Mitrinović–Pečarić (1988), described as a comprehensive treatment of Neuberg–Pedoe and Oppenheim inequalities. Only bibliographic/abstract-level information was inspected, not the full article. Because the present identity is elementary after combining Heron's form with the Poincaré model, an older equivalent formulation under distance-geometry or Lorentz-form language remains possible.

## Value

**PASS.** The result identifies a classical two-triangle inequality with an intrinsic metric rather than merely sharpening its numerical lower bound. It gives:
- an exact defect-to-distance law for Pedoe;
- a Lorentz-hyperboloid coordinate model built directly from squared side lengths;
- a closed formula for the quotient distance between ordinary unlabeled triangle shapes;
- an exact radial interpretation of Weitzenböck's inequality; and
- exact normal-distance formulas for isosceles and right-angle loci.

These relations connect classical triangle inequalities, statistical/mesh triangle shape coordinates, and hyperbolic geometry in a reusable form.

## Scientific limitations

The result uses the Poincaré/Bookstein hyperbolic metric, not Kendall's spherical shape metric. It applies to nondegenerate Euclidean triangles; degenerate triangles lie at the ideal boundary. The labeled identity requires a chosen side correspondence, while the quotient formula separately handles unlabeled shapes. Originality remains to the best of our knowledge because a full-text check of the 1988 comprehensive Neuberg–Pedoe review was not available and equivalent folklore may exist.
