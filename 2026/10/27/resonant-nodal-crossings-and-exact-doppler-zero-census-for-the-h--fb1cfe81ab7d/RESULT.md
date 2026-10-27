# Resonant nodal crossings and exact Doppler-zero census for the hat-spline ambiguity function

## Finding
Let \(g(t)=(1-|t|)_+\) and define the real, symmetric narrowband ambiguity function
\[
 A(T,\nu)=\int_{\mathbb R}g(t+T/2)g(t-T/2)e^{-2\pi i\nu t}\,dt.
\]
The lag \(T=2/3\) is the resonance at which the inner knots of the window-overlap product are halfway to its outer edges and the two leading Fourier jump coefficients balance. Write \(x=2\pi\nu/3\) and
\[
 Q(x)=1+2\cos x+\frac{2\sin x}{x},\qquad Q(0)=5.
\]
For every real \(\nu\ne0\),
\[
 \boxed{A(2/3,\nu)=\frac{2}{3\pi^2\nu^2}\sin^2(\pi\nu/3)\,Q(2\pi\nu/3).}
\]
The removable value at zero is \(A(2/3,0)=10/27>0\). For each integer \(k\ge0\), \(Q\) has exactly one simple zero in each of the two intervals
\[
 (2\pi k,(2k+1)\pi),\qquad((2k+1)\pi,2\pi(k+1)),
\]
and has no other positive zeros. Consequently, every positive Doppler zero of \(A(2/3,\cdot)\) belongs to exactly one of two classes:

1. Every \(\nu=3n\), integer \(n\ge1\), is a zero of **exact order two** in the Doppler variable.
2. Each of the intervals \((3k,3k+3/2)\) and \((3k+3/2,3k+3)\), integer \(k\ge0\), contains **exactly one simple zero**.

There are no others. If \(N_+(R)\) counts positive Doppler zeros in \((0,R]\) with analytic multiplicity and \(N_+^{\mathrm{distinct}}(R)\) counts distinct positive zeros, then
\[
 N_+(R)=\frac43R+O(1),\qquad
 N_+^{\mathrm{distinct}}(R)=R+O(1)\quad(R\to\infty).
\]
The two simple zeros in the \(k\)-th interval of length three approach the Doppler integers \(3k+1\) and \(3k+2\), respectively, from above, with displacement \(3/(4\pi^2k)+O(k^{-2})\) for \(k\to\infty\).

The double zeros are not merely tangencies of the one-dimensional Doppler trace: **each is a nondegenerate crossing of two genuine real-analytic nodal curves in the delay–Doppler plane**. For every \(n\ge1\),
\[
 \nabla A(2/3,3n)=0,\qquad
 D^2_{(T,\nu)}A(2/3,3n)=
 \begin{pmatrix}0&-2/(9n)\\-2/(9n)&4/(81n^2)\end{pmatrix}.
\]
Its determinant is \(-4/(81n^2)<0\). The two local nodal branches through \((2/3,3n)\) have tangent slopes \(d\nu/dT=0\) and \(d\nu/dT=9n\), respectively.

## Assumptions and scope
All signals and frequencies are real except for the Fourier exponential; the Fourier normalization is \(e^{-2\pi i\nu t}\). The hat spline has support \([-1,1]\), so its overlap is nontrivial only for \(|T|<2\). The exact classification concerns the fixed positive lag \(T=2/3\); its local two-variable statement holds in an open neighborhood of each \((2/3,3n)\). No classification is asserted for arbitrary lag or for complex-frequency zeros. The positive-frequency enumeration includes multiplicity only where explicitly stated.

## Proof
**1. Piecewise overlap and a general identity.** For \(0<T<1\), put \(h=T/2\), \(L=1-T/2\), and \(p_T(t)=g(t+h)g(t-h)\). By evenness, it suffices to specify
\[
 p_T(t)=\begin{cases}
 L^2-t^2,&0\le t\le h,\\
 (1-t)^2-h^2,&h\le t\le L,\\
 0,&t\ge L.
 \end{cases}
\]
The pieces agree at their common endpoints. The distributional second derivative has ordinary density \(-2\) on \((-h,h)\) and \(+2\) on the two flanks, with first-derivative jumps \(-2(1-T)\) at each \(\pm h\) and \(+T\) at each \(\pm L\). For \(\omega=2\pi\nu\ne0\), transforming this distribution and using \(\widehat{p_T''}(\omega)=-\omega^2\widehat{p_T}(\omega)\) yields exactly
\[
 \omega^2 A(T,\nu)=4(1-T)\cos(\omega T/2)-2T\cos(\omega L)
 +\frac{8\sin(\omega T/2)-4\sin(\omega L)}{\omega}.
 \tag{1}
\]
No asymptotic approximation is used.

**2. Resonant factorization.** At \(T=2/3\) we have \(h=1/3\), \(L=2/3\), and the leading cosine coefficients have equal magnitude \(4/3\). Setting \(x=\omega/3\) in (1) gives
\[
 \omega^2 A(2/3,\nu)=\frac43(\cos x-\cos2x)
 +\frac{8\sin x-4\sin2x}{\omega}.
\]
The identities \(\cos x-\cos2x=2\sin^2(x/2)(1+2\cos x)\) and \(8\sin x-4\sin2x=16\sin x\sin^2(x/2)\) give the factorization in the finding. Direct integration or the removable limit gives \(A(2/3,0)=10/27\).

**3. Exhaustive positive-zero classification of \(Q\).** For each \(k\ge0\), the endpoint values are \(Q(2\pi k)=3\) for \(k\ge1\), \(Q(0)=5\), and \(Q((2k+1)\pi)=-1\). Thus each indicated half-period contains a zero. For \(x>0\),
\[
 Q'(x)=-2\sin x+\frac{2\cos x}{x}-\frac{2\sin x}{x^2}.
\]
At a zero in a positive-sine half-period, \(1+2\cos x=-2\sin x/x<0\), so \(\cos x<-1/2\). All three summands of \(Q'\) are negative, proving every such root crosses strictly downward. At a root in a negative-sine half-period, \(\cos x>-1/2\). If \(\cos x\ge0\), every summand of \(Q'\) is positive. If \(-1/2<\cos x<0\), then \(-\sin x>\sqrt3/2\), and since \(x>\pi\), we have \(Q'(x)>\sqrt3-1/\pi>0\). Hence all roots there cross strictly upward. A continuously differentiable function cannot have two roots crossing in the same strict direction without an intervening opposite-direction root or tangency. The endpoint signs therefore give exactly one root in each specified half-period, and all such roots are simple.

**4. Multiplicities and asymptotic lattice.** At each \(x=2\pi n\), integer \(n\ge1\), the sine-squared factor has a double zero, the remaining factor is \(Q(2\pi n)=3\), and the denominator is nonzero. Other positive roots come from \(Q\) and are simple. Exactly two simple and one double positive roots occur per full successive \(x\)-period of length \(2\pi\), except for a bounded endpoint correction; \(x=2\pi\nu/3\) gives both zero-count estimates. At large \(k\), write \(x_0=2\pi k+2\pi j/3\), for \(j=1,2\). At \(x_0\), the term \(1+2\cos x_0\) vanishes, and a Taylor expansion gives the unique nearby root
\[
 x_{k,j}=x_0+\frac1{x_0}+O(k^{-2}).
\]
Converting to Doppler frequency yields the stated displacement; the asymptotic sign is positive.

**5. Nodal crossings.** Formula (1) is jointly real analytic for \(0<T<1\) and \(\nu>0\), including the resonant points. Differentiate (1) twice, use \(\omega=2\pi\nu\), and evaluate at \((T,\nu)=(2/3,3n)\). The first derivatives vanish and the displayed Hessian results. Its determinant is strictly negative, so the analytic Morse lemma makes the zero level locally two transverse real-analytic arcs. The tangent directions solve the Hessian's null quadratic form:
\[
 (\Delta\nu)\bigl(\Delta\nu-9n\,\Delta T\bigr)=0.
\]
Thus their slopes are zero and \(9n\). This proves that no higher-order degeneracy or isolated double tangency is hidden at the lattice zeros.

## Verification
The standalone script `verify.py` uses exact symbolic trigonometric simplification, direct independent piecewise quadrature, and symbolic differentiation at representative lattice points. It checks nine high-precision ambiguity values, ten lattice-factor evaluations, 24 roots in twelve periods, and the stated Hessian at four sites; saved numerical output is in `verification_output.txt`. These finite computations validate formulas and reproducibility, whereas the exhaustive zero census and all-order nodal crossings follow from steps 3–5 of the analytical proof.

## Relationship to prior work
Jaming, *Zero-free regions of radar ambiguity functions and moments* (arXiv:math/0606397v1, 2006), studies moment-dependent exclusion neighborhoods for general ambiguity functions; it does not classify remote zeros for the explicit hat spline at a fixed nonzero delay. Kloos and Stöckler, *Zak transforms and Gabor frames of totally positive functions and exponential B-splines* (arXiv:1311.7359v1, 2013), analyze Zak zeros and Gabor-frame properties of B-spline windows, not the corresponding self-ambiguity Doppler-zero census. The Fourier transform of a single hat spline and the distributional derivative identity for a compactly supported piecewise polynomial are standard ingredients, not claimed novel.

A nearby analysis of the Haar signed step-pulse ambiguity at lag \(2/3\) classifies a distinct signal, with different zero multiplicities and nodal geometry. Neither that classification nor the cited general framework implies the present exact hat-overlap factorization and its two crossing branches. The literature comparison remains subject to the risk of an unindexed equivalent spline-ambiguity calculation.

## Limitations
The special resonant lag is essential to the displayed factorization. The theorem does not prove a corresponding complete zero census at nearby delays; the local crossing theorem describes only neighborhoods of the points specified. Numerical testing is not a proof that another publication lacks an equivalent result. There is no independent mathematical audit or claim of publication priority.

## References
1. P. Jaming, *Zero-free regions of radar ambiguity functions and moments*, arXiv:math/0606397v1 (first public 2006-06-16). https://arxiv.org/abs/math/0606397
2. T. Kloos and J. Stöckler, *Zak transforms and Gabor frames of totally positive functions and exponential B-splines*, arXiv:1311.7359v1 (first public 2013-11-28). https://arxiv.org/abs/1311.7359
