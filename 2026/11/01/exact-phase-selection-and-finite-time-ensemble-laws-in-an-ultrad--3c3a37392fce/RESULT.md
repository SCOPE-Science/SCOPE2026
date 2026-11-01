# Exact phase selection and finite-time ensemble laws in an ultradiscrete FitzHugh–Nagumo map

## Finding

Consider the one-dimensional max-plus map
\[
F(u)=\max\{2u,I\}-\max\{2u,B\},\qquad B>0,\quad I>\frac{3B}{2}.
\]
Set
\[
L=\max\{0,2B-I\},\qquad H=I-B,\qquad q=\frac I3,
\qquad K=[L,H],
\]
and let \(\lambda_K\) be normalized Lebesgue measure on \(K\). The previously identified attracting two-cycle is \(L\leftrightarrow H\), whereas \(q\) is a repelling fixed point. Define the *even-time high phase* to consist of initial values \(u\in K\setminus\{q\}\) satisfying \(F^{2n}(u)=H\) for all sufficiently large integers \(n\).

**Theorem.** The even-time high phase has exact \(\lambda_K\)-probability
\[
w(I,B)=\begin{cases}
\frac13,&\frac{3B}{2}<I\le2B,\\
\frac{2I-3B}{3(I-B)},&I\ge2B.
\end{cases}
\]
It is constant at \(1/3\) below \(I=2B\), then strictly increases to \(2/3\) as \(I/B\to\infty\), crossing \(1/2\) exactly at \(I=3B\). By contrast, every symmetric interval about \(q\) contained in \(K\) has exactly half of its Lebesgue measure in either even-time phase: for every \(0<r\le\min\{q-L,H-q\}\),
\[
\frac{\operatorname{Leb}\big(\{u\in[q-r,q+r]:u\text{ has high even-time phase}\}\big)}{2r}=\frac12.
\]

For all integers \(n\ge0\), the exact even-time distribution is
\[
(F^{2n})_*\lambda_K=4^{-n}\lambda_K+(1-4^{-n})\nu,
\qquad \nu=w\delta_H+(1-w)\delta_L.
\]
In particular, with total variation defined as \(\|\rho-\sigma\|_{\rm TV}=\sup_A|\rho(A)-\sigma(A)|\),
\[
\big\|(F^{2n})_*\lambda_K-\nu\big\|_{\rm TV}=4^{-n}.
\]
For a uniformly chosen initial value \(U\in K\), the first hitting time of the cycle, \(T=\min\{n\ge0:F^n(U)\in\{L,H\}\}\), has the exact geometric law
\[
\mathbb P(T>n)=2^{-n}\quad(n\ge0),\qquad
\mathbb P(T=n)=2^{-n}\quad(n\ge1),\qquad \mathbb E[T]=2.
\]
The entire odd-time distribution is obtained by applying \(F_*\) to the displayed even-time law; it is explicitly computed below. The source's existence and location of the two-cycle are not new claims.

## Assumptions and scope

Parameters \(B,I\) are arbitrary real numbers with \(B>0\) and \(I>3B/2\). The initial ensemble is normalized Lebesgue measure on the *natural cycle interval* \(K=[L,H]\), not arbitrary Lebesgue measure on the full real line. Endpoints and the repelling fixed point are negligible for this initial ensemble. Every assertion about phase refers to the parity of the original discrete-time iteration, with the high phase meaning eventual equality of the *even* iterate to \(H\). The notation \(F^0\) means the identity and \(\delta_y\) is the unit point mass at \(y\).

The map is continuous, piecewise affine and bounded. Since \(I>B\), its branches are \(F(u)=H\) for \(u\le B/2\), \(F(u)=I-2u\) for \(B/2<u<I/2\), and \(F(u)=0\) for \(u\ge I/2\). On \(K\), the last branch is present only if \(I>2B\), and there its value is \(L=0\). Direct substitution verifies \(F(L)=H\), \(F(H)=L\), \(L<q<H\) and \(F(q)=q\).

## Proof

**1. The exact transfer identity.** Write
\[
J=\left(\frac B2,\min\left\{\frac I2,H\right\}\right),\quad
 a=\frac{B/2-L}{H-L},\quad
 b=\frac{H-\min\{I/2,H\}}{H-L}.
\]
These parameters satisfy \(a\ge0\), \(b\ge0\) and \(a+b=1/2\). On \(J\), the affine branch \(u\mapsto I-2u\) maps \(J\) bijectively to the interior of \(K\); the left complement in \(K\) maps to \(H\), and the right complement maps to \(L\). Consequently, for every bounded Borel test function \(\varphi\), by change of variables,
\[
\int_K\varphi(F(u))\,d\lambda_K(u)
=\frac12\int_K\varphi(v)\,d\lambda_K(v)
 +a\varphi(H)+b\varphi(L).
\]
Equivalently,
\[
F_*\lambda_K=\tfrac12\lambda_K+a\delta_H+b\delta_L,
\qquad F_*\delta_H=\delta_L,\quad F_*\delta_L=\delta_H.
\]
The \(n\)-step continuous component therefore has exactly mass \(2^{-n}\) and remains uniformly distributed on \(K\); every other component is supported on the two-cycle.

**2. Exact geometric hitting law and phase weight.** The continuous part is precisely the mass of points not yet captured by the cycle, modulo a Lebesgue-null boundary set. Hence \(\mathbb P(T>n)=2^{-n}\), and the asserted first-hit law and mean follow. All but the fixed point \(q\) are captured after finitely many iterates: if \(u\) stayed in \(J\) forever, \(F^n(u)-q=(-2)^n(u-q)\), contradicting boundedness in \(K\) unless \(u=q\).

After two steps, the continuous mass is \(1/4\), while the two atomic masses are \(a/2+b\) at \(H\) and \(b/2+a\) at \(L\). Since the even-time phase of an initial point cannot change after an even number of iterates, and the residual continuous ensemble remains uniformly distributed, its high-phase probability \(w\) satisfies
\[
w=\left(\frac a2+b\right)+\frac14w,
\qquad\text{thus}\qquad
w=\frac23a+\frac43b=\frac13+\frac23b.
\]
For \(I\le2B\), the right plateau has zero length and \(b=0\). For \(I\ge2B\), \(L=0\), \(H=I-B\) and \(b=(I-2B)/(2(I-B))\). This yields both displayed formulas and their monotonicity, crossover and limits.

For even time \(2n\), the continuous component has mass \(4^{-n}\) and uniform conditional distribution. Exactly \(w\) of the *original* probability belongs to the high phase, so its continuously surviving contribution is \(4^{-n}w\); the remaining high-phase mass \((1-4^{-n})w\) must already sit at \(H\). This proves the even-time measure identity. Because Lebesgue measure is atomless and \(\nu\) is atomic, their total-variation distance equals one, proving the sharp \(4^{-n}\) identity. More explicitly, at odd time \(2n+1\) the continuous component has mass \(2^{-(2n+1)}\), the mass at \(H\) is \((1-4^{-n})(1-w)+4^{-n}a\), and the mass at \(L\) is \((1-4^{-n})w+4^{-n}b\).

**3. Exact mirror balance about the repeller.** For \(u\ne q\), let \(h(u)\in\{0,1\}\) denote the eventual high-even-time phase. Then \(h(F(u))=1-h(u)\) and \(h(F^{2}(u))=h(u)\). On the left plateau of \(K\), \(h=0\); on the right plateau, \(h=1\). Fix \(0<t\le\min\{q-L,H-q\}\). As long as both \(q-t\) and \(q+t\) are in the open affine branch \(J\),
\[
F(q-t)=q+2t,\qquad F(q+t)=q-2t,
\]
so
\[
h(q-t)+h(q+t)=2-h(q-2t)-h(q+2t).
\]
The doubled pair remains in \(K\), since it is the image of the original pair in \(J\). Iterating this identity eventually reaches a scale \(s\) for which at least one of \(q-s\) and \(q+s\) lies outside \(J\), as the positive separation doubles at each preceding step. If both lie outside \(J\), their phases are \(0\) and \(1\). If only \(q-s\) is outside, it is in the left plateau, and \(q+s\) maps to \(q-2s\), which is also in the left plateau, forcing phases \(0\) and \(1\). If only \(q+s\) is outside, the analogous right-plateau argument gives phases \(0\) and \(1\). The equality \(h(q-s)+h(q+s)=1\) therefore propagates backward through every doubling step, proving
\[
h(q-t)+h(q+t)=1.
\]
Integrating this identity for \(0<t<r\) yields the claimed exact half-half selection on every centered subinterval.

## Verification

`verify.py` uses exact rational arithmetic, checks the complete branch and endpoint identities for six distinct parameter ratios, propagates the transfer operator over twenty steps, verifies every even-time atomic coefficient and its geometric surviving mass, and tests mirror pairing at 97 exact rational separations for each parameter ratio. The test cases are not used to establish the universal statements; the preceding analytic derivation covers all real \(B>0\), \(I>3B/2\). Execute with Python 3 as `python verify.py` in the extracted package.

## Relationship to prior work

The map and the attracting two-cycle, including its transition at \(I=2B\), are already described by Ohmori and Yamazaki [1, Section 4, Eq. (39) and Figure 7]; [1] attributes the scalar ultradiscrete model to Sasaki and coauthors [3]. The qualitative cycle and fixed-point information is not claimed to be new. The subsequent study [2] addresses stability and bifurcations of positive and ultradiscrete systems. In the inspected texts [1,2], the *uniform-initialization phase probabilities*, *exact every-time ensemble law*, *sharp total-variation rate* and *radius-independent mirror balance* are not derived. Related general renewal mechanisms and planar ultradiscrete first-exit calculations do not by themselves fix these parameter-dependent one-dimensional phase weights or the mirror symmetry. A literature search cannot rule out equivalent unpublished or unindexed results.

## Limitations

The ensemble statement applies to normalized uniform data on \(K\). Nonuniform data generally have different first-hit and phase distributions. The repelling fixed point \(q\) is exceptional, and \(\delta_q\) is another invariant probability; neither \(\nu\) nor its swapped phase is claimed to be the only invariant measure. The invariant statistical measure supported on the attracting two-cycle is \(\tfrac12(\delta_L+\delta_H)\), independent of the parity-phase selection weight \(w\). The theorem does not address noise-perturbed max-plus maps or full spatially extended FitzHugh–Nagumo dynamics. The earlier Sasaki et al. conference report [3] was not obtained in full, and equivalent unindexed priority remains a possibility.

## References

[1] S. Ohmori and Y. Yamazaki, *Ultradiscrete Bifurcations for One Dimensional Dynamical Systems*, arXiv:2004.13224, first posted 2020-04-28, especially Section 4 and Equation (39). https://arxiv.org/abs/2004.13224

[2] S. Ohmori and Y. Yamazaki, *Relation of stability and bifurcation properties between continuous and ultradiscrete dynamical systems via discretization with positivity: one dimensional cases*, arXiv:2212.03455, first posted 2022-12-07. https://arxiv.org/abs/2212.03455

[3] M. Sasaki, S. Nishioka, F. Hongo and M. Murata, Reports of RIAM Symposium, No. 29AO-S7, 81 (2018), as identified and credited by [1]; the full text was not examined.
