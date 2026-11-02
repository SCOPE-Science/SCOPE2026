# Sharp Fourier-critical-point bifurcations for zero-free reciprocal trinomials

## Finding

For every even integer \(m\ge2\) and every real \(u>-2\), set
\[
P_{m,u}(z)=z^{2m}+uz^m+1,\qquad Q_{m,u}(x)=\left(\frac{P'_{m,u}(x)}{P_{m,u}(x)}\right)'\quad(x\in\mathbb R).
\]
The polynomial has **no real zeros**. Let \(N_m(u)\) be the number of its **distinct nonzero real Fourier critical points**, that is, real nonzero solutions of \(Q_{m,u}(x)=0\). The complete classification is:
\[
N_m(u)=\begin{cases}
4,&-2<u<0,\\
2,&u=0,\\
2,&u>0,\quad m=2,4,\\
2,&0<u<u_c(m),\quad m\ge6,\\
4,&u=u_c(m),\quad m\ge6,\\
6,&u>u_c(m),\quad m\ge6.
\end{cases}
\]
For \(m\ge6\), put
\[
A_m=m^2-6m+1,\qquad B_m=-4m^4+32m^3-52m^2+48m-8,\qquad C_m=-16(2m-1)^3,
\]
and define the unique threshold
\[
u_c(m)=\sqrt{\frac{-B_m+\sqrt{B_m^2-4A_mC_m}}{2A_m}}>2.
\]
Every nonzero critical point occurs in a symmetric pair \(\pm X^{1/m}\), with \(X>0\) a zero of the cubic
\[
S_{m,u}(X)=-2X^3+(m-3)uX^2+(4m-2-u^2)X+(m-1)u.
\]
At \(u=u_c(m)\), its two small positive roots merge to a positive double root \(X_*\); the third root is positive and simple. Thus this is a genuine two-pair creation, not a loss to infinity.

There is also an exact origin transition. For \(-2<u<0\), the smaller positive root satisfies, as \(u\uparrow0\),
\[
X_{\mathrm{in}}(u)=-\frac{m-1}{4m-2}u+O_m(u^2),\qquad
|x_{\mathrm{in}}|\sim \left(\frac{m-1}{4m-2}\right)^{1/m}|u|^{1/m}.
\]
At the upper threshold \(u=u_c(m)\), with \(S=S_{m,u}\), define
\[
\kappa_m=\sqrt{-\frac{2\partial_uS(X_*,u_c(m))}{\partial_X^2S(X_*,u_c(m))}}>0.
\]
The two newly distinct positive roots for \(u>u_c(m)\) satisfy
\[
X_\pm(u)=X_*\pm\kappa_m\sqrt{u-u_c(m)}+O_m(u-u_c(m)).
\]
Hence the two corresponding positive Fourier critical points separate by
\[
\frac{2\kappa_m}{m}X_*^{1/m-1}\sqrt{u-u_c(m)}+O_m(u-u_c(m)).
\]

At \(x=0\), \(Q_{m,u}\) has a zero of multiplicity \(m-2\) when \(m\ge4\) and \(u\ne0\), and multiplicity \(2m-2\) when \(u=0\). For \(m=2\), the origin is a zero only when \(u=0\), in which case its multiplicity is two. These central zeros are not included in \(N_m(u)\). All nonzero zeros are simple except that each of the two points \(\pm X_*^{1/m}\) at \(u_c(m)\) is double.

## Assumptions and scope

All statements concern real \(x\), even integers \(m\ge2\), and real \(u>-2\). Since \(X=x^m\ge0\), the quadratic \(X^2+uX+1\) is strictly positive: for \(-2<u<0\), its minimum on \(X\ge0\) is \(1-u^2/4>0\), and for \(u\ge0\) positivity is immediate. Thus \(P'/P\) and its derivative have no real poles. A Fourier critical point means a zero of \((P'/P)'\), not a zero of \(P'\); multiplicities are analytic zero orders. The root classification is for distinct **nonzero** points; the central multiplicity is separately stated.

## Proof

**1. Exact cubic reduction.** Direct differentiation of
\[
\frac{P'_{m,u}(x)}{P_{m,u}(x)}=\frac{m x^{m-1}(2x^m+u)}{x^{2m}+ux^m+1}
\]
yields the identity
\[
Q_{m,u}(x)=\frac{m x^{m-2} S_{m,u}(x^m)}{(x^{2m}+ux^m+1)^2}.
\]
For nonzero real \(x\), the map \(x\mapsto x^m\) is two-to-one from \(\mathbb R\setminus\{0\}\) onto \((0,\infty)\), and the denominator never vanishes. Hence \(N_m(u)\) is twice the number of distinct positive roots of \(S_{m,u}\).

**2. Negative and zero parameters.** If \(-2<u<0\), then \(S(0)=(m-1)u<0\),
\[
S(1)=(u+2)(2m-2-u)>0,
\]
and \(S(X)\to-\infty\) as \(X\to+\infty\). There are at least two distinct positive roots. The coefficient signs for even \(m\ge2\) show exactly two sign changes (because \(4m-2-u^2>0\)); Descartes' rule therefore gives at most two positive roots, with multiplicity. Both are simple. At \(u=0\),
\[
S_{m,0}(X)=2X(2m-1-X^2),
\]
which has exactly one positive root. Applying the implicit-function theorem at \((X,u)=(0,0)\) and differentiating \(S(X(u),u)=0\) gives
\[
X'(0)=-\frac{m-1}{4m-2}.
\]
This is the claimed inner-pair fractional-power law.

**3. Exact discriminant.** The cubic discriminant is
\[
\operatorname{Disc}_X(S_{m,u})=(u^2-4)\big(A_mu^4+B_mu^2+C_m\big).
\]
The auxiliary quadratic \(q_m(t)=A_mt^2+B_mt+C_m\) satisfies
\[
q_m(0)=-16(2m-1)^3<0,\qquad q_m(4)=-16m^4<0.
\]
For \(m=2,4\), respectively,
\[
q_2(t)=-7t^2+72t-432,\qquad q_4(t)=-7t^2+376t-5488.
\]
Both are strictly negative for all real \(t\): their leading coefficients are negative and their quadratic discriminants are, respectively, \(-6912\) and \(-12288\). For every even \(m\ge6\), \(A_m>0\) and \(C_m<0\), so \(q_m\) has one positive and one negative root. Since \(q_m(4)<0\), its positive root \(t_c>4\) is exactly the stated radical, and \(q_m(t)<0\) for \(0\le t<t_c\), positive for \(t>t_c\).

**4. Positive-parameter root counts.** For sufficiently small \(u>0\), the three roots are continuations of \(-\sqrt{2m-1}\), \(0\), and \(+\sqrt{2m-1}\) at \(u=0\). The root continuing from zero is negative because its derivative is \(-(m-1)/(4m-2)\). Thus exactly one root is positive. A simple root cannot change sign because \(S_{m,u}(0)=(m-1)u>0\); the positive-root count can change only when the cubic discriminant vanishes. At \(u=2\), direct factorization gives
\[
S_{m,2}(X)=-2(X+1)^2(X-(m-1)),
\]
so the repeated root is negative and the positive-root count stays one. For \(m=2,4\), the discriminant has no other positive-parameter zero, proving one positive root for all \(u>0\). For \(m\ge6\), the only other zero is \(u=u_c(m)\).

To determine the number beyond this threshold, set \(X=uy\) and divide by \(u^3\). As \(u\to\infty\), the resulting polynomial converges coefficientwise to
\[
-y\left(2y^2-(m-3)y+1\right).
\]
For \(m\ge6\), its three roots \(0\) and
\[
y_\pm=\frac{m-3\pm\sqrt{m^2-6m+1}}4
\]
are real and simple, with \(y_\pm>0\). Two roots of \(S\) therefore behave like \(uy_\pm>0\); its third root is \((m-1)/u+O_m(u^{-3})>0\), obtained by balancing the constant and linear terms. Hence there are three simple positive roots for sufficiently large \(u\). With no further positive discriminant zeros, there are three positive roots for every \(u>u_c(m)\). At \(u=u_c(m)\) there is one double positive root and one simple positive root; since \(q_m\) has a simple root, the cubic cannot have a triple root (which would make the discriminant vanish to higher order). All assertions concerning \(N_m(u)\) follow.

**5. Multiplicities and the upper fold.** At the origin, the displayed factorization in Step 1 gives exactly order \(m-2\) if \(u\ne0\) and \(m\ge4\), and order \(2m-2\) if \(u=0\). For \(m=2\), these same expansions show \(Q_{2,u}(0)=2u\). A simple positive root of \(S\) gives a simple pair of real zeros; at the double root \(X_*\), it gives a double pair. For \(u>u_c\), the two extra roots split about the smaller local extremum of \(S\), so at the fold \(\partial_X^2S(X_*,u_c)>0\). The discriminant vanishes simply at \(u_c\), forcing \(\partial_uS(X_*,u_c)\ne0\); because the local minimum is negative for \(u>u_c\), this derivative is negative. Taylor's theorem at the fold yields
\[
0=\partial_uS(X_*,u_c)(u-u_c)+\tfrac12\partial_X^2S(X_*,u_c)(X-X_*)^2
 +O_m(|u-u_c|^{3/2}),
\]
for \(X-X_*=O_m(\sqrt{u-u_c})\), and hence the two square-root laws. Applying Taylor's theorem to \(X^{1/m}\) completes the radius separation formula.

## Verification

The standalone `checker.py` checks the symbolic differentiation identity, the full cubic discriminant factorization, the \(u=2\) factorization, the two special quadratic discriminants, the lower and upper transition signs, and several rational-parameter instances using exact Sturm root counts. Run `python -m pip install -r requirements.txt` and then `python checker.py` in the directory containing these files. Finite computations and checker output are consistency tests, not substitutes for the all-even-degree proof above.

## Relationship to prior work

Tyaglov's Hawaii-conjecture theorem gives a universal upper bound for the number of real zeros of \((P'/P)'\) by the number of nonreal zeros of \(P\), not this parameter-dependent exact count. Lande Ma and Zhaokun Ma study geometric root-locus generation of first-kind critical points in their October 2026 work, and second-kind points in a companion preprint. Neither inspected source derives the cubic discriminant, the sharp degree-twelve birth of six nonzero real critical points, or the two quantitative fold laws for this zero-free reciprocal-trinomial family. The general differential-polynomial work of Katkova, Tyaglov and Vishnyakova concerns related real-zero counts without yielding the present parameter classification. The quartic \(P_{2,0}(x)=x^4+1\) appears as a second-kind example in the 2026 companion paper; it is not claimed here as a new example.

## Limitations

This theorem is restricted to even \(m\) and \(u>-2\), and to **real** Fourier critical points. The central inherited multiple zero is counted separately; a total count without that convention would differ. The result does not determine root-locus pairings or global behavior of arbitrary polynomial coefficients. Earlier literature could contain an implicit equivalent of this exact trinomial classification; independent priority verification has not been performed. The source preprints' broad geometric assertions are not used as premises of the proof.

## References

1. L. Ma and Z. Ma, *Comprehensive Resolution of the Gauss-Fourier Conjecture for the First Kind of Zeros*, arXiv:2610.30620v1 (first arXiv posting 2026-10-22), https://arxiv.org/html/2610.30620v1.
2. L. Ma and Z. Ma, *Principle of generating critical points of rational functions and Gauss-Fourier conjecture for second-kind zeros*, arXiv:2610.29790v1 (first arXiv posting 2026-10-21), https://arxiv.org/html/2610.29790v1.
3. M. Tyaglov, *On the number of real critical points of logarithmic derivatives and the Hawaii conjecture*, arXiv:0902.0413, https://arxiv.org/pdf/0902.0413.
4. O. Katkova, M. Tyaglov, and A. Vishnyakova, *On the number of real zeroes of a homogeneous differential polynomial and a generalization of the Hawaii conjecture*, arXiv:2406.00686, https://arxiv.org/abs/2406.00686.
