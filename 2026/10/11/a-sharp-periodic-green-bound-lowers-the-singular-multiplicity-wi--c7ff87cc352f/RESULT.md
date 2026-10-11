# A sharp periodic Green bound lowers the singular multiplicity window by one quarter
## Finding
Consider
\\[
u''+k u=g(u)+e(t),\qquad u(0)=u(2\\pi),\qquad u'(0)=u'(2\\pi),
\\]
with \\(g\\in C(0,\\infty)\\), \\(k\\in\\mathbb R\\), and \\(e\\in L^1(0,2\\pi)\\). Write
\\[
\\bar e=\\frac1{{2\\pi}}\\int_0^{{2\\pi}}e(t)\\,dt.
\\]
Assume the remaining hypotheses of Theorem 2.1 of arXiv:2610.04501v1: \\(\\operatorname{{ess\\,inf}}e> -\\infty\\), the strong singularity condition \\(\\lim_{{x\\to0+}}\\int_x^1 g(s)\\,ds=+\\infty\\), \\(\\liminf_{{x\\to0+}}g(x)>-\\infty\\), and the existence of an upper function strictly above a number \\(B\\). Suppose there are \\(0<A<B\\) such that
\\[
g(x)-kx<-\\bar e\qquad (A\\le x\\le B)
\\]
and
\\[
B-A\\ge \\frac{{\\pi}}4\\,\\lVert e-\\bar e\\rVert_1.
\\]
Then the problem has at least two positive periodic solutions. The focal theorem uses the stronger requirement \\(B-A\\ge(\\pi/3)\\lVert e-\\bar e\\rVert_1\\).

## Assumptions and scope
The result changes only the quantitative width hypothesis used to construct the lower function. All singularity, forcing, and upper-function hypotheses are retained. The statement does not assert that \\(\\pi/4\\) is the globally optimal multiplicity threshold; it is the sharp constant for the periodic linear-corrector oscillation estimate used here.

## Proof
Put \\(f=e-\\bar e\\), so \\(\\int_0^{{2\\pi}}f=0\\). Let \\(G\\) be the periodic Green kernel for the mean-zero inverse of the second derivative. On the representative \\(0\\le s<2\\pi\\), take
\\[
G(s)=-\\frac{{\\pi}}6+\\frac{s}{2}-\\frac{{s^2}}{{4\\pi}}.
\\]
It is continuous and periodic, its derivative has jump \\(1\\) at the period boundary, and distributionally \\(G''=\\delta_0-(2\\pi)^{{-1}}\\). Hence
\\[
w(t)=\\int_0^{{2\\pi}}G(t-s)f(s)\\,ds
\\]
is periodic and satisfies \\(w''=f\\).

Fix two points whose circular separation is \\(d\\in[0,\\pi]\\). By translation invariance it suffices to study \\(H_d(s)=G(s)-G(s-d)\\), with the second argument reduced modulo \\(2\\pi\\). Direct expansion gives
\\[
H_d(s)=
\\begin{{cases}}
\\dfrac{{(2\\pi-d)(2s-d)}}{{4\\pi}},&0\\le s<d,\\\\[5pt]
\\dfrac{{d(2\\pi+d-2s)}}{{4\\pi}},&d\\le s\\le2\\pi.
\\end{{cases}}
\\]
Thus
\\[
|H_d(s)|\\le \\frac{{d(2\\pi-d)}}{{4\\pi}}\\le\\frac{{\\pi}}4.
\\]
Consequently, for every pair \\(t,r\\),
\\[
|w(t)-w(r)|
\\le \\frac{{\\pi}}4\\lVert f\\rVert_1,
\\]
so
\\[
\\operatorname{{osc}}w\\le\\frac{{\\pi}}4\\lVert e-\\bar e\\rVert_1.
\\]
This constant is sharp for the linear estimate: at separation \\(d=\\pi\\), \\(H_d\\) attains \\(\\pm\\pi/4\\), and zero-mean \\(L^1\\)-normalized smooth functions concentrating positive and negative mass near the two extremizers approach equality.

Now set
\\[
\\sigma_1(t)=A-\\min w+w(t).
\\]
Then \\(\\sigma_1([0,2\\pi])\\subset[A,B]\\) by the new width hypothesis, and \\(\\sigma_1''=e-\\bar e\\). Therefore
\\[
\\sigma_1''+k\\sigma_1
=e-\\bar e+k\\sigma_1
>e+g(\\sigma_1),
\\]
so \\(\\sigma_1\\) is a lower function. Because the inequality is strict on the compact interval \\([A,B]\\), the small downward perturbation of this lower function required in the focal multiplicity proof is also available. The remainder of that proof—one solution trapped between this lower function and the prescribed upper function, followed by the singularity-based construction of a distinct second positive solution—does not use the numerical value \\(\\pi/3\\). Replacing its lower-function construction by the one above therefore proves the stated multiplicity theorem.

## Verification
The exact branch formulas for \\(H_d\\), the endpoint amplitude, and the identity
\\[
\\frac14-\\frac{{a(2-a)}}4=\\frac{{(1-a)^2}}4\qquad(0\\le a\\le1)
\\]
were replayed by `verify_green_bound.py`; the packaged output is `VERIFY_OK`. The proof itself is analytic and does not rely on finite sampling. The focal 2026 proof and its 2001/2003 antecedents were inspected at the lower-function construction and multiplicity steps.

## Relationship to prior work
The 2026 preprint derives \\(\\lVert\\sigma_0\\rVert_\\infty\\le(\\pi/6)\\lVert e-\\bar e\\rVert_1\\) by two Sobolev estimates and hence assumes width \\(\\pi/3\\). The 2003 multiplicity paper states the same \\(\\pi/3\\) condition in Proposition 1.5 and invokes it in Theorem 4.3. The 2001 lower/upper-function construction likewise builds an interval of width \\(\\pi/3\\lVert b\\rVert_1\\). The present argument uses the oscillation of the exact periodic Green corrector rather than twice a centered sup-norm bound, reducing the sufficient width by one quarter.

## Limitations
Only the width constant in this particular sufficient condition is sharpened. The existence of the required upper function remains an assumption. The sharpness statement concerns the linear periodic-corrector inequality, not the full nonlinear multiplicity problem; more flexible lower functions could conceivably yield an even weaker hypothesis.

## References
1. M. Tvrdý, *Multiple solutions of singular periodic problems*, arXiv:2610.04501v1, 3 Oct 2026, especially Theorem 2.1 and its Step 1.
2. I. Rachůnková, M. Tvrdý, I. Vrkoč, *Resonance and multiplicity in periodic boundary value problems with singularity*, Mathematica Bohemica 128 (2003), 45–70, DOI 10.21136/MB.2003.133937, especially Proposition 1.5 and Theorem 4.3.
3. I. Rachůnková, M. Tvrdý, *Construction of Lower and Upper Functions and Their Application to Regular and Singular Periodic Boundary Value Problems*, Nonlinear Analysis 47 (2001), 3937–3948, DOI 10.1016/S0362-546X(01)00513-2, especially Proposition 2.4.
