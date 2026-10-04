# Review

## Correctness

PASS. For odd regular polygons, the side normals have equal cone-volume weights and opposite support values \(r\) and \(R\). At a translated center \(x\), the standard \(p\)-measure reduces exactly to
\[
\frac1{nr}\sum_i(R+t_i)^p(r-t_i)^{1-p},
\qquad
t_i=\langle x,u_i\rangle,
\qquad
\sum_i t_i=0.
\]
At \(p=1\) the expression is linear and constant in \(x\). For \(p>1\), the scalar kernel has strictly positive second derivative, so Jensen gives the global minimum and its equality condition. The log endpoint is an equal-atom average of a constant support ratio. The \(p=\infty\) bound follows from the inball/circumball support bounds with equality at side normals.

The packaged checker independently rebuilds the regular polygons, support values, \(p=1\) translation invariance, and \(p>1\) lower-bound behavior for a finite range. The analytic proof, not the enumeration, establishes the infinite theorem.

## Originality

PASS with residual historical risk. The defining log-Minkowski paper was inspected through its definitions, normalized mixed-volume formulas, log section, and \(0<p<1\) section; its accessible full text has no occurrence of “polygon.” The 2015 Guo–Guo–Su paper explicitly asks when \(\operatorname{as}_1=\operatorname{as}_\infty\), hence when all standard \(p\)-measures coincide, but develops coproduct formulas rather than regular polygons.

Targeted searches for regular polygons with \(p\)-measure, \(p\)-Minkowski asymmetry, log-Minkowski asymmetry, mixed-volume asymmetry, and the secant value found no equivalent theorem. The ordinary Minkowski endpoint alone is elementary and may have older coverage, so originality is not claimed for that endpoint in isolation.

## Value

PASS. The \(p\)-measures form a genuine hierarchy on general convex bodies, and prior work specifically identifies coincidence of the \(p=1\) and \(p=\infty\) endpoints as a structural question. Regular polygons are the canonical finite rotationally symmetric test family. The theorem gives a complete exact standard spectrum, includes the log endpoint, and reveals a non-obvious critical-set transition: all interior points minimize at \(p=1\), but strict uniqueness appears immediately for \(p>1\).

Same-model review: passed. Independent audit: not yet performed.
