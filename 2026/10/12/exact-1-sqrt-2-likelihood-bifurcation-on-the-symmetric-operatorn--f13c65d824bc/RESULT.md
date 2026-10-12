# Exact \(1/\sqrt{2}\) likelihood bifurcation on the symmetric \(\operatorname{Gr}(2,4)\) slice
## Finding
Consider the positive Grassmannian likelihood model on \(\operatorname{Gr}(2,4)\) with data restricted to
\[
u_{12}=u_{34}=u_{14}=u_{23}=a,\qquad u_{13}=u_{24}=b,
\]
where \(a,b>0\) and \(2a+b=1\). On the three-coordinate model slice
\[
x_{12}=x_{34}=r,\qquad x_{13}=x_{24}=s,\qquad x_{14}=x_{23}=t,
\]
the Plücker relation is \(r^2+t^2=s^2\). The restricted likelihood has a sharp transition at
\[
b_\star=\frac{1}{\sqrt{2}}.
\]
For \(0<b<b_\star\), there is a unique strict global maximizer and it is the symmetric point \(r=t\). At \(b=b_\star\), the same point remains the unique strict global maximizer, but its first nonzero loss is quartic. For \(b_\star<b<1\), the symmetric point becomes a strict local minimum and there are exactly two symmetric strict global maximizers, with
\[
\frac{t}{r}=q_\pm=\frac{b^2\pm\sqrt{2b^2-1}}{1-b^2},\qquad q_+q_-=1.
\]
Thus the numerically observed multimodality on this slice has an exact one-parameter phase diagram.

## Assumptions and scope
The data weights are positive real numbers; scaling all six data coordinates by the same positive constant does not change the critical points, so the normalization \(2a+b=1\) is only a convenience. The result concerns the likelihood restricted to the source's reflection-symmetric model slice. It does not assert that every critical point of the full positive Grassmannian lies on this slice.

Write the source likelihood as
\[
L_u(x)=\sum_{1\le i<j\le4}u_{ij}\log x_{ij}-
\left(\sum_{1\le i<j\le4}u_{ij}\right)
\log\left(\sum_{1\le i<j\le4}x_{ij}\right).
\]
All coordinates in the present statement are strictly positive, so the logarithms are well defined.

## Proof
Parameterize the positive model slice by
\[
r=s\cos\theta,\qquad t=s\sin\theta,\qquad 0<\theta<\frac{\pi}{2}.
\]
Because \(2a+b=1\), the scale \(s\) cancels from the projective likelihood. Dividing \(L_u\) by the positive constant \(2\), and discarding an additive constant, gives
\[
\ell_b(\theta)=a\log(\sin\theta\cos\theta)-
\log(1+\sin\theta+\cos\theta),
\qquad a=\frac{1-b}{2}.
\]
Set
\[
v=\sin\theta+\cos\theta.
\]
Then \(1<v\le\sqrt{2}\), with equality \(v=\sqrt{2}\) exactly at \(\theta=\pi/4\), and
\[
\sin\theta\cos\theta=\frac{v^2-1}{2}.
\]
Hence, up to another additive constant,
\[
g_b(v)=a\log(v-1)+(a-1)\log(v+1).
\]
Its derivative is
\[
g_b'(v)=\frac{1-bv}{v^2-1}.
\]
The denominator is positive on \((1,\sqrt{2}]\). Therefore:

- if \(b<1/\sqrt{2}\), then \(g_b'(v)>0\) throughout the interval, so the unique maximum occurs at \(v=\sqrt{2}\), equivalently \(r=t\);
- if \(b=1/\sqrt{2}\), then \(g_b'(v)>0\) for \(v<\sqrt{2}\) and vanishes only at the endpoint, so the same point is still the unique strict global maximizer;
- if \(b>1/\sqrt{2}\), then \(v_\star=1/b\) lies strictly inside \((1,\sqrt{2})\), and \(g_b\) increases before \(v_\star\) and decreases after it. Because the map \(\theta\mapsto v\) is symmetric about \(\pi/4\), there are exactly two strict global maximizers, one on each side of \(\pi/4\), while \(\pi/4\) is a strict local minimum.

To solve for their locations, let \(q=\tan\theta=t/r\). The equation \(v=1/b\) is
\[
\frac{1+q}{\sqrt{1+q^2}}=\frac{1}{b},
\]
which is equivalent to
\[
(1-b^2)q^2-2b^2q+(1-b^2)=0.
\]
The two positive roots are exactly
\[
q_\pm=\frac{b^2\pm\sqrt{2b^2-1}}{1-b^2}.
\]
At the threshold, write \(\theta=\pi/4+h\). Then \(v=\sqrt{2}\cos h\). Since \(g_b'(\sqrt{2})=0\) and \(g_b''(\sqrt{2})=-1/\sqrt{2}\) at \(b=1/\sqrt{2}\),
\[
\ell_b\left(\frac{\pi}{4}+h\right)-\ell_b\left(\frac{\pi}{4}\right)
=-\frac{h^4}{4\sqrt{2}}+O(h^6).
\]
Thus the threshold maximizer is strict but quartically flat.

## Verification
A direct symbolic specialization of the degree-six logarithmic-discriminant polynomial displayed for the same data slice in the source gives, on the reflection-symmetric line where the source's data coordinates satisfy \(r=t=a\) and \(s=b\),
\[
2(4a^2+4ab-b^2)^3.
\]
Under \(2a+b=1\), its zero condition is
\[
1-2b^2=0,
\]
which reproduces \(b=1/\sqrt{2}\). This is an independent algebraic cross-check of the one-variable likelihood analysis, not a substitute for the proof above.

For a concrete exact example, take \(b=3/4\) and \(a=1/8\). Then the two maximizing ratios are
\[
q_\pm=\frac{9\pm4\sqrt{2}}{7},
\]
while the symmetric point \(q=1\) is a strict local minimum on the restricted slice.

## Relationship to prior work
Friedman's 2026 preprint introduces this positive-Grassmannian statistical model, computes its maximum-likelihood degree, and in the revised version studies positive critical points of \(\operatorname{Gr}(2,4)\). It gives a degree-six logarithmic discriminant on the three-coordinate data slice and exhibits a numerical data point with two local maxima and one saddle. The source does not give the reflection-symmetric factorization above, the threshold \(1/\sqrt{2}\), the closed-form maximizing ratios, or the quartic threshold expansion.

The earlier squared-Grassmannian model is different: there the probabilities are proportional to squared Plücker coordinates, and every critical point for positive data is a local maximum. That theorem does not imply the phase diagram here because the present model uses unsquared positive Plücker coordinates and has a different likelihood geometry.

## Limitations
The theorem is deliberately restricted to the natural reflection-symmetric data line and the corresponding three-coordinate positive model slice. It does not classify nonsymmetric critical points of the full \(\operatorname{Gr}(2,4)\) model, nor does it address \(\operatorname{Gr}(2,n)\) for \(n>4\). The exact discriminant specialization is checked only against the polynomial printed in the inspected source; no claim is made about unpublished computational files.

## References
1. H. Friedman, *Maximum Likelihood Estimation on the Grassmannian of Lines*, arXiv:2607.19593, first posted 2026-07-21, revised 2026-07-28. MSC2020 begins with 62R01.
2. H. Friedman, *Likelihood Geometry of the Squared Grassmannian*, arXiv:2409.03730; Proc. Amer. Math. Soc. 153 (2025), 4463--4474, DOI:10.1090/proc/17287.
