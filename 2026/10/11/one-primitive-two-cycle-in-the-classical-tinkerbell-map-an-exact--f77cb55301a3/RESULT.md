# One primitive two-cycle in the classical Tinkerbell map: an exact global census

## Finding

For the classical Tinkerbell map
\[
F(x,y)=\bigl(x^2-y^2+\tfrac9{10}x-\tfrac{6013}{10000}y,\;2xy+2x+\tfrac12y\bigr),
\]
**there is exactly one unordered orbit of least period two in the whole real plane**. Its two points are approximately
\[
(-1.51720358189108,-1.54736525849683),\qquad
(-0.527485028067661,0.887246432339844).
\]
The two eigenvalues of its two-step derivative are a nonreal conjugate pair of modulus greater than one; hence this unique primitive two-cycle is a hyperbolic repeller. The exact claim concerns all real periodic points of least period two, not only points inside a numerically observed attractor.

## Assumptions and scope

The four coefficients in the displayed polynomial map are *exact rational numbers*. All states lie in \(\mathbb R^2\); no restriction to a trapping region or an attractor is assumed. An unordered two-cycle means a set \(\{p,q\}\) with \(p\ne q\), \(F(p)=q\), and \(F(q)=p\). The derivative and its eigenvalues refer to \(DF^2\) at either point. No statement is made about other prime periods, chaotic invariant sets, or robust persistence under parameter variation.

## Proof

Identify \(\mathbb R^2\) with \(\mathbb C\). The map becomes \(F(z)=z^2+Az+B\bar z\), with
\[
A=\tfrac7{10}+\tfrac{26013}{20000}i,\qquad
B=\tfrac15+\tfrac{13987}{20000}i.
\]
Any primitive two-cycle has the unique unordered description \(\{s-d,s+d\}\) for \(d\ne0\), where \(s\) is its midpoint. Set \(t=\bar d/d\), so \(|t|=1\). Subtracting the two orbit equations gives
\[
(1+2s+A)d+B\bar d=0,\qquad
s=-\frac{1+A+Bt}{2}.
\]
Adding them gives \(d^2=s-s^2-As-B\bar s\). Because \(td^2=|d|^2\), the two-cycle condition is **equivalent** to \(P(t)\) being strictly positive and real, for \(|t|=1\), where
\[
P(t)=-\frac{B^2t^3}{4}-Bt^2+
\left(\frac{A^2}{4}-\frac A2+\frac{\bar A B}{2}+\frac B2-\frac34\right)t
+\frac{|B|^2}{2}.
\]
Indeed, if \(P(t)>0\) is real, choose \(d\) with \(d^2=P(t)/t\); then automatically \(\bar d/d=t\). Its two signs give the same unordered orbit. Conversely every primitive two-cycle gives exactly one such \(t\).

At \(t=-1\), direct substitution yields \(P(-1)=291156169/400000000-(8987/10000)i\), so it is inadmissible. Every other \(t\) on the unit circle has the Cayley parameter \(t=(1+iu)/(1-iu)\) with \(u\in\mathbb R\). Direct rational expansion of \(P(t)=\overline{P(t)}\) gives the sextic equation
\[
\begin{aligned}
Q(u)={}&44935000u^6+3880000u^5-108922000u^4\\
&+267396169u^3-240753000u^2+83880000u+25000000=0.
\end{aligned}
\]
The exact rational Sturm chain of \(Q\) has sign-variation counts \(4\) at \(-\infty\) and \(2\) at \(+\infty\). In particular there are exactly two real roots, with one each in
\[
I_1=(-123/50,-49/20),\qquad I_2=(-183/1000,-181/1000).
\]
The corresponding variation counts at the four consecutive interval endpoints are \(4,3,3,2\), so no other real roots are possible.

The real part of \(P\), evaluated on the unit circle, is exactly
\[
\rho(u)=\frac{291156169u^6-1166544000u^5+1701337014u^4-990336000u^3-266428507u^2+1071376000u-239520000}{400000000(1+u^2)^3}.
\]
Exact Sturm root counts show that the numerator of \(\rho\) has no root on either \(I_1\) or \(I_2\). Rational-midpoint substitution then gives \(\rho>0\) on \(I_1\), but \(\rho<0\) on \(I_2\). Thus exactly the first root represents a real primitive two-cycle, proving global completeness. Its positive value is approximately \(\rho=1.72671922523523\), and reconstructing \(s\) and \(d\) gives the two points stated above.

To classify its multipliers, let \(W=-1-Bt\), \(m=|B|^2\), and \(\rho=|d|^2\). The real-linear derivative acts on a complex tangent vector as \(DF_z(h)=(2z+A)h+B\bar h\). Therefore the trace and determinant of the two-step derivative at this cycle are
\[
\begin{aligned}
T&=2\Re\bigl(W^2-4\rho/t+m\bigr),\\
D&=(|W|^2+4\rho-m)^2
-4\rho\bigl(W^2t+2|W|^2+\bar W^2/t\bigr).
\end{aligned}
\]
When \(t=(1+iu)/(1-iu)\) and \(\rho=\rho(u)\), both are rational functions with rational coefficients. The exact rational Sturm check finds no zeros of the numerators or denominators of \(D-1\) and \(T^2-4D\) on \(I_1\). At its rational midpoint these expressions have signs \(+\) and \(-\), respectively. Consequently \(D>1\) and \(T^2-4D<0\) at the unique cycle. Its multipliers are conjugates of modulus \(\sqrt D>1\), proving hyperbolic repulsion.

## Verification

The included standalone script `verification/check.py` reconstructs \(P\), checks the exact Cayley sextic identity, performs rational Sturm real-root counts, certifies the positive/negative branches, and checks strict multiplier inequalities. Its successful execution reports a PASS for all these **finite exact rational symbolic checks**. As a separate descriptive check, the cycle has approximate return trace \(13.74957792992871\), determinant \(73.68658705213559\), and discriminant \(-105.6954549573597\). Floating-point orbit residuals are not used to justify completeness.

## Relationship to prior work

The Tinkerbell map is a standard example in chaotic dynamics. Davidchack, Lai, Klebanoff and Bollt (2001) study numerical detection of its unstable periodic points at exactly these parameters, including periods up to fourteen. Their rigorous completeness analysis is for a one-dimensional root-finding setting, while their two-dimensional completeness conclusions are supported by numerical evidence; they do not provide the global algebraic period-two exclusion and multiplier certificate established here. Goldsztejn, Hayes and Collins (2011) rigorously establish forms of chaos and shadowing at the same parameters using containment and orbit data, but not a global census of all real primitive two-cycles. The earlier textbook by Alligood, Sauer and Yorke (1996) treats nearby Tinkerbell coefficients and changes the first coefficient in a Lyapunov-exponent computer experiment, without classifying its primitive two-cycles. Yuan, Jiang and Jing (2011) investigate parameter-dependent bifurcations and period-two windows; those findings likewise do not supply the stated exact global census at this rational parameter tuple. These are statement-level comparisons, not a claim that an unsuccessful literature search proves novelty.

## Limitations

The theorem applies to **this exact four-parameter map only**. It neither enumerates periods three and higher nor locates the unique orbit inside any chaotic attractor; the certified cycle may lie outside the displayed invariant chaotic set. It does not assert an independent audit. Earlier descriptions or numerical tables may have observed the same orbit; the distinct contribution assessed here is exact whole-plane uniqueness and hyperbolic repulsion by exhaustive algebraic reasoning. The original 1994 numerical-dynamics monograph and its 1997 revised edition could not be checked exhaustively for an equivalent proof, leaving a residual historical-priority risk.

## References

1. R. L. Davidchack, Y.-C. Lai, A. Klebanoff and E. M. Bollt, *Towards complete detection of unstable periodic orbits in chaotic systems*, Physics Letters A 287 (2001), 99–104. DOI: 10.1016/S0375-9601(01)00463-7.
2. A. Goldsztejn, W. Hayes and P. Collins, *Tinkerbell Is Chaotic*, SIAM Journal on Applied Dynamical Systems 10 (2011), 1480–1501. DOI: 10.1137/100819011.
3. S. Yuan, T. Jiang and Z. Jing, *Bifurcation and chaos in the Tinkerbell map*, International Journal of Bifurcation and Chaos 21 (2011), 3137–3156. DOI: 10.1142/S0218127411030581.
4. H. E. Nusse and J. A. Yorke (with E. J. Kostelich on the 1994 edition), *Dynamics: Numerical Explorations*, Springer, first edition 1994 and revised edition 1997; cited in [1].
5. K. T. Alligood, T. D. Sauer and J. A. Yorke, *Chaos: An Introduction to Dynamical Systems*, Springer, 1996, Chapter 5 (Tinkerbell numerical experiments).
