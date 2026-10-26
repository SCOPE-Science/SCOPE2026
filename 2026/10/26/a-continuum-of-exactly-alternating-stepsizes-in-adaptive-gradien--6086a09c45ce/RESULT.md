# A continuum of exactly alternating stepsizes in adaptive gradient descent-2

## Finding

The stepsize rule of **Algorithm 2** in Malitsky–Mishchenko's *Adaptive Proximal Gradient Method for Convex Optimization* admits a complete continuum of nonconstant exact period-two stepsize orbits, even for the one-dimensional strongly convex quadratic \(f(x)=\lambda x^2/2\). An open interval of ordinary initial stepsizes locks onto one of these orbits immediately (or after one initial step), while the optimization iterates converge geometrically to the unique minimizer. The two-cycle family, its sharp ratio cutoff, and its locally transverse finite-time collapse are proved below; the inverse-square equality used in the derivation is already present in the original paper and is **not** claimed as a new identity.

Put \(\Phi(z)=z/\sqrt{2z^2-1}\) for \(z>1/\sqrt2\), and let \(r_*\) be the unique root in \((1,5/4)\) of
\[
r^3-\frac23r-1=0,
\qquad
 a_* = \sqrt{\frac{1+r_*^2}{2}},\quad b_* = \frac{a_*}{r_*}.
\]
Numerically \(r_*\approx1.21933756736\), \(a_*\approx1.11507490851\), and \(b_*\approx0.91449237550\).

**Classification.** The normalized second-order stepsize map of that algorithm has exactly one positive fixed point, \((1,1)\), and all its nonconstant positive prime-period-two orbits, without exception, are
\[
 (a(r),b(r))\longleftrightarrow(b(r),a(r)),\qquad
 a(r)=\sqrt{\frac{1+r^2}{2}},\quad b(r)=\frac{a(r)}r,
 \quad 1<r\le r_*.
\]
In particular every orbit obeys \(1/a(r)^2+1/b(r)^2=2\). The restriction \(r\le r_*\) is sharp for prime-period-two orbits of this rule.

**Actual runs.** Choose any \(\lambda>0\), \(x^0\ne0\) and the prescribed initialization \(\theta_0=1/3\). If the normalized initial stepsize \(c=\lambda\alpha_0\) lies in \((1,a_*]\), then the entire normalized stepsize sequence is \(a,b,a,b,\ldots\), where \(a=c\), \(b=\Phi(c)\). If \(c\in[b_*,1)\), it is \(b,b,a,b,a,\ldots\), where \(b=c\), \(a=\Phi(c)\). In each case the two alternating values are unequal, all divided differences required by the algorithm are well defined, and the objective iterates tend to zero geometrically. More precisely, once alternating steps are in place,
\[
 x^{k+2}=(1-a)(1-b)x^k,\qquad
 0<(a-1)(1-b)<1.
\]
The initial \(c=1\) is excluded from this assertion because the quadratic is minimized in the first step (which makes the next nontrivial divided difference undefined if the method is needlessly continued).

**Neutral family, exact transverse collapse.** At each interior orbit with \(1<r<r_*\), an open neighborhood in the two-dimensional consecutive-stepsize state is mapped by two steps onto the above one-dimensional family. In suitable consecutive-value coordinates, the two-step map has eigenvalues \(0\) and \(1\), corresponding respectively to exact transverse collapse and the persistent freedom to select another nearby alternating pair. Thus these cycles are not individually asymptotically stable; the family is transversely absorbing.

## Assumptions and scope

Throughout, arithmetic and function evaluations are exact, \(\lambda>0\), and \(f(x)=\frac\lambda2x^2\) on the real line. The original adaptive gradient descent-2 algorithm starts with \(x^0\), \(\alpha_0>0\), \(\theta_0=1/3\), and \(x^1=x^0-\alpha_0\lambda x^0\). For \(k\ge1\), while consecutive iterates are distinct, it computes
\[
 L_k=\frac{|\lambda x^k-\lambda x^{k-1}|}{|x^k-x^{k-1}|},\qquad
 \alpha_k=\min\left\{\alpha_{k-1}\sqrt{\frac23+\theta_{k-1}},\ \frac{\alpha_{k-1}}{\sqrt{[2\alpha_{k-1}^2L_k^2-1]_+}}\right\},
 \qquad \theta_k=\frac{\alpha_k}{\alpha_{k-1}},
\]
then \(x^{k+1}=x^k-\alpha_k\lambda x^k\). A zero denominator in the curvature cap is interpreted as \(+\infty\), hence that cap is inactive. The phase-plane classification concerns the naturally induced map on arbitrary positive pairs of consecutive normalized stepsizes, not arbitrary sequences chosen independently of the method. An orbit is of prime period two only when its values differ.

## Proof

**1. Scalar reduction and cap involution.** For all steps with \(x^k\ne x^{k-1}\) the local curvature estimate is exactly \(L_k=\lambda\). Set \(s_k=\lambda\alpha_k\). Given consecutive normalized steps \(p=s_{k-2}>0\) and \(q=s_{k-1}>0\), the next step is
\[
 T(p,q)=\big(q,\ G(p,q)\big),\quad
 G(p,q)=\min\left\{q\sqrt{\tfrac23+\tfrac qp},\ C(q)\right\},
 \quad
 C(q)=\begin{cases}\displaystyle\frac{q}{\sqrt{2q^2-1}},&q>1/\sqrt2,\\ +\infty,&0<q\le1/\sqrt2.\end{cases}
\]
Whenever \(z>1/\sqrt2\), its cap \(C(z)\) is also greater than \(1/\sqrt2\), and
\[
 C(C(z))=z,\qquad z^{-2}+C(z)^{-2}=2.
\]
This last reciprocal-square equality on active curvature branches was already noted in the source paper's Lemma 5. We use, but do not claim to have discovered, that identity.

**2. Complete classification of two-cycles.** A positive fixed state \(T(z,z)=(z,z)\) needs \(z=\min\{z\sqrt{5/3},C(z)\}\). Since the growth candidate strictly exceeds \(z\), the cap must equal \(z\), forcing \(z=1\).

Let distinct positive steps alternate, with larger value \(a\) and smaller value \(b\), so \(r=a/b>1\). On the transition \(a\to b\), the growth candidate is \(a\sqrt{2/3+a/b}>a>b\); it cannot be selected. Necessarily \(b=C(a)\), and therefore \(a>1\), \(1/\sqrt2<b<1\), and \(a=C(b)\). Thus the other transition \(b\to a\) is allowed exactly when the growth candidate does not fall below the cap:
\[
 b\sqrt{\tfrac23+\tfrac ba}\ge a
 \quad\Longleftrightarrow\quad
 r^2\le\tfrac23+\tfrac1r
 \quad\Longleftrightarrow\quad
 r^3-\tfrac23r-1\le0.
\]
For \(r\ge1\) the polynomial's derivative \(3r^2-2/3\) is positive, its value at \(1\) is \(-2/3\), and its value at \(5/4\) is \(23/192>0\). Hence it has exactly one root \(r_*\in(1,5/4)\), and the alternating condition is equivalent to \(1<r\le r_*\). Solving \(a/b=r\) and \(a^{-2}+b^{-2}=2\) gives the displayed formulas for \(a(r)\) and \(b(r)\). Conversely these formulas make \(b=C(a)\), \(a=C(b)\), and the required growth comparison, so every listed pair is indeed a two-cycle. This proves necessity, sufficiency, and sharpness.

**3. Startup from an open interval.** Because \(C\) decreases strictly on its domain and \(C(1)=1\), the allowed large and small members range respectively over \((1,a_*]\) and \([b_*,1)\). If \(s_0=a>1\), the stipulated \(\theta_0=1/3\) makes the first growth candidate exactly \(a\), while the cap is \(C(a)=b<a\). Hence \(s_1=b\), and the two-cycle condition proved above forces all subsequent values to alternate. If \(s_0=b<1\), the first growth candidate is exactly \(b\), and \(C(b)=a>b\); hence \(s_1=b\). The next growth candidate equals \(b\sqrt{5/3}\), whereas the cap equals \(a=br\). Since \(r\le r_*<5/4<\sqrt{5/3}\), we have \(s_2=a\). Thereafter the two-cycle condition applies. The endpoints are admitted: equality of branches at \(r=r_*\) still produces the same step.

Every used step lies in \((b_*,a_*)\) or at one of its endpoints, and no such step equals \(1\) for a nonconstant alternating orbit. Since \(x^0\ne0\), the recursion \(x^{k+1}=(1-s_k)x^k\) makes every finite iterate nonzero and each consecutive difference nonzero; this validates \(L_k=\lambda\) at all the required indices. Furthermore, \(1<a\le a_*<2\), \(0<b<1\), so \(0<(a-1)(1-b)<1\). Multiplying two successive scalar updates proves the exact geometric contraction law, notwithstanding stepsize nonconvergence.

**4. Local transverse collapse.** Fix \(1<r<r_*\) and consider the state \((p,q)=(b,a)\). Both consecutive curvature caps are strictly smaller than their respective growth candidates: the high-to-low comparison is strict because \(a>1\), and the low-to-high comparison is strict because \(r<r_*\). By continuity these strict inequalities persist on an open neighborhood of \((b,a)\). On this neighborhood,
\[
 T(p,q)=(q,C(q)),\qquad T^2(p,q)=(C(q),q).
\]
The output lies on the two-cycle curve because \(C(C(q))=q\) and, after possibly shrinking the neighborhood, the ratio remains strictly within the allowed interval. Differentiating, with \(C'(q)=-(2q^2-1)^{-3/2}\), gives
\[
 D(T^2)(b,a)=\begin{pmatrix}0&C'(a)\\0&1\end{pmatrix}.
\]
Its eigenvalues are exactly \(0,1\); the image is the fixed-point curve of the second iterate. The eigenvalue \(1\) forbids individual asymptotic stability; the other normal direction collapses in one two-step return. The proof makes no assertion that the same neighborhood statement holds at the tie endpoint \(r=r_*\).

## Verification

The self-contained `verify.py` uses only Python's standard library. It checks the exact rational squared-value identities for the radical witness
\[
 a=\sqrt{13/12},\qquad b=\sqrt{13/14},\qquad (a/b)^2=7/6,
\]
computes and brackets the unique cutoff using high-precision decimal arithmetic, tests both prescribed initialization branches at 80-digit precision, and verifies the two-step map and local collapsed form numerically at interior points. The exact all-parameter assertions above follow from the displayed algebra and inequalities; a finite verifier is not used as a substitute for those arguments. Reproduce with `python3 verify.py`.

## Relationship to prior work

Malitsky and Mishchenko's paper (arXiv:2308.02261, Algorithm 2 and Lemma 5) supplies exactly the adaptive rule studied here, proves primal convergence, and already explicitly derives the reciprocal-square relation on an active curvature branch. This result does not claim any of those ingredients as new. The additional assertion is the complete sharp continuum of prime-two orbits, a nonempty actual-initialization interval, and the finite-time transverse phase-map property.

Latafat, Themelis, Stella, and Patrinos (arXiv:2301.04431, §4.3) report empirically cyclic stepsizes and expressly identify rigorous explanation as an interesting question, but analyze a distinct cocoercivity-based proximal update, with a different growth factor and curvature cap. It is not identical to Algorithm 2 above. Earlier Malitsky–Mishchenko 2020 adaptive gradient descent uses yet another cap. Consequently their observed cycling or primal convergence does not by itself yield the exact threshold \(r_*\) or classify these period-two states. Nonetheless, the source's already-known inverse-square identity makes this analysis a relatively direct extension; that proximity is acknowledged as an originality limitation.

## Limitations

The result is a classification for the real scalar quadratic and for positive period-two states of the specified stepsize recurrence. It does not classify higher-period cycles, basins outside the stated initial-step interval, arbitrary multi-dimensional Hessians, proximal variants, noise, finite precision, or time-varying curvature. The local transverse statement excludes the cutoff tie. Algorithmic termination at an exactly reached minimizer should not be mistaken for continued evaluation of undefined divided differences. The self-review did not establish global uniqueness relative to every unpublished or differently formulated prior source; independent audit has not been performed.

## References

1. Y. Malitsky and K. Mishchenko, *Adaptive Proximal Gradient Method for Convex Optimization*, arXiv:2308.02261 (initially public 2023-08-04), Algorithm 2, Lemma 5, Theorem 2. https://arxiv.org/html/2308.02261v2
2. P. Latafat, A. Themelis, L. Stella, and P. Patrinos, *Adaptive proximal algorithms for convex optimization under local Lipschitz continuity of the gradient*, arXiv:2301.04431, §4.3. https://arxiv.org/html/2301.04431v4
3. Y. Malitsky and K. Mishchenko, *Adaptive Gradient Descent without Descent*, Proceedings of Machine Learning Research 119 (2020), 6702–6712. https://proceedings.mlr.press/v119/malitsky20a.html
