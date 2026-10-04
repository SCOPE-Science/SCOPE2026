# Sharp Routh-area profile at fixed Ceva product

## Finding
Let \(ABC\) be a nondegenerate Euclidean triangle. Put interior division points \(D\in BC\), \(E\in CA\), and \(F\in AB\), and write
\[
x=\frac{BD}{DC},\qquad y=\frac{CE}{EA},\qquad z=\frac{AF}{FB},
\]
so \(x,y,z>0\). Let \(PQR\) be the triangle cut out by the three cevians \(AD,BE,CF\), and define
\[
\alpha=\frac{[PQR]}{[ABC]},\qquad s=\frac{|\log(xyz)|}{3}.
\]
If \(xyz=1\), Ceva's theorem gives \(\alpha=0\). For every fixed product \(xyz\ne1\), the exact attainable range of \(\alpha\) is
\[
0<\alpha\le F(s):=\frac{2(\cosh s-1)}{2\cosh s+1}.
\]
The upper endpoint is attained exactly when
\[
x=y=z=(xyz)^{1/3}.
\]
The lower endpoint is an infimum and is not attained by positive finite \(x,y,z\).

Equivalently, every configuration with \(\alpha>0\) obeys the sharp inverse inequality
\[
|\log(xyz)|\ge 3\operatorname{arcosh}\!\left(\frac{2+\alpha}{2(1-\alpha)}\right),
\]
with equality exactly for equal positive cevian parameters.

## Assumptions and scope
The points \(D,E,F\) are interior to their respective sides, so all three side ratios are finite and strictly positive. Areas are ordinary unsigned Euclidean areas. The claim concerns the classical Routh triangle and does not assert an extension to negative or infinite directed-ratio parameters.

## Proof
Routh's area formula, in the above ratio convention, is
\[
\alpha=
\frac{(xyz-1)^2}
{(1+x+xy)(1+y+yz)(1+z+zx)}.
\]
The cited 2012 open full text of Bényi and Ćurgus records this formula and its Ceva specialization.

Set
\[
a=\log x,\qquad b=\log y,\qquad c=\log z
\]
and define
\[
\phi(u,v)=\log\!\left(1+e^u+e^{u+v}\right),
\qquad
G(a,b,c)=\phi(a,b)+\phi(b,c)+\phi(c,a).
\]
The function \(\phi\) is strictly convex: it is a log-sum-exp of three affine functions whose gradients \((0,0),(1,0),(1,1)\) affinely span \(\mathbb R^2\). Hence \(G\) is strictly convex. It is also invariant under the cyclic permutation \((a,b,c)\mapsto(b,c,a)\).

Let
\[
m=\frac{a+b+c}{3}.
\]
Averaging the three cyclic permutations gives \((m,m,m)\), so Jensen's inequality and cyclic invariance give
\[
G(m,m,m)
\le \frac{G(a,b,c)+G(b,c,a)+G(c,a,b)}{3}
=G(a,b,c).
\]
Strict convexity shows that equality holds exactly when \(a=b=c\). Exponentiating, with
\[
q=e^m=(xyz)^{1/3},
\]
yields the sharp denominator bound
\[
(1+x+xy)(1+y+yz)(1+z+zx)
\ge (1+q+q^2)^3,
\]
with equality exactly when \(x=y=z=q\).

Substituting this into Routh's formula gives
\[
\alpha\le
\frac{(q^3-1)^2}{(1+q+q^2)^3}
=rac{(q-1)^2}{q^2+q+1}.
\]
Writing \(q=e^u\) and \(s=|u|\), division by \(e^u\) gives
\[
\frac{(q-1)^2}{q^2+q+1}
=rac{2(\cosh s-1)}{2\cosh s+1}=F(s).
\]
Thus the displayed upper envelope is exact, and its equality condition is the equal-parameter branch.

It remains to identify the full range at fixed product. If \(q^3=xyz\ne1\), the fixed-product surface of positive triples is connected, and \(\alpha\) is a positive continuous function on it. The equal triple attains \(F(s)\). On the path
\[
x=t,\qquad y=\frac{q^3}{t},\qquad z=1,
\]
we have the same product and the denominator grows quadratically as \(t\to\infty\), while the numerator stays fixed and positive. Hence \(\alpha\to0\). Connectedness then implies that every value in \((0,F(s)]\) occurs.

Finally, \(F\) is strictly increasing for \(s>0\). Solving \(\alpha\le F(s)\) for \(\cosh s\) gives
\[
\cosh s\ge \frac{2+\alpha}{2(1-\alpha)},
\]
which is exactly the inverse inequality above. Equality again forces the equal-parameter branch.

## Verification
The bundled script `verify_routh_profile.py` evaluates Routh's formula on 30,000 deterministic random positive triples spanning many logarithmic scales, checks the sharp upper envelope and inverse inequality, verifies the complete equality branch, and follows fixed-product paths toward zero area. Its successful replay prints `VERIFY_OK`. These finite checks supplement, but do not replace, the universal convexity proof.

## Relationship to prior work
Bényi and Ćurgus give the classical Routh formula and a six-parameter generalization, together with the Ceva and Menelaus specializations. Their inspected full text discusses equal-coefficient examples such as Feynman's triangle, but does not state an optimization at fixed \(xyz\), the sharp envelope \(F(s)\), or the inverse Ceva-defect inequality.

Abboud's 2014 preprint develops Routh-Steiner area patterns, including symmetric divisions and a parallelogram analogue. Its inspected text likewise does not state a fixed-product optimization or a quantitative area-versus-Ceva-product profile.

Targeted searches for the exact fixed-product optimization, equal-parameter extremizer, logarithmic Ceva defect, and the displayed hyperbolic-cosine envelope did not locate an equivalent published statement. This is evidence for originality, not a proof of exhaustive novelty.

## Limitations
The theorem is restricted to positive finite cevian ratios. It does not address directed exterior cevians, poles where the usual formula changes interpretation, or higher-dimensional Routh-Steiner analogues. Older geometry literature could contain an equivalent inequality under different notation; that residual historical risk remains. Independent audit has not been performed.

## References
1. Á. Bényi and B. Ćurgus, *A generalization of Routh's triangle theorem*, arXiv:1112.4813v1, first posted 2011-12-20; later *American Mathematical Monthly* 120 (2013), 841–846, DOI:10.4169/amer.math.monthly.120.09.841.
2. E. Abboud, *On Routh-Steiner Theorem and Generalizations*, arXiv:1403.5652v1, first posted 2014-03-22; later *The Mathematical Gazette* 99 (2015), 45–53, DOI:10.1017/mag.2014.6.
