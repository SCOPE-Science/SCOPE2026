# A sharp two-jet Hardy quasi-norm transition and an exact second-coefficient frontier

## Finding

Let \(H^{1/2}\) be the analytic Hardy space on the unit disk, with \(\|f\|_{1/2}=(\int_0^{2\pi}|f(e^{i\theta})|^{1/2}\,d\theta/(2\pi))^2\). Write \(a_j(f)=f^{(j)}(0)/j!\). For every real \(\tau\ge0\), the norm of the bounded linear functional \(L_\tau(f)=a_0(f)+\tau a_2(f)\) is

\[
N(\tau)=\sup_{\|f\|_{1/2}\le1}|a_0(f)+\tau a_2(f)|
=\begin{cases}
\dfrac{1+4\tau r}{(1+r^2)^2},&0\le\tau\le\tfrac12,\quad \tau=\dfrac{r}{1-3r^2},\quad0\le r\le\tfrac13,\\[6pt]
\dfrac{27\tau^2}{16\tau-3},&\tau\ge\tfrac12.
\end{cases}
\]

The parameter \(r\) is uniquely determined. At \(\tau=\tfrac12\), both branches equal \(27/20\). The profile is continuously differentiable but not twice differentiable there: \(N''(1/2-)=81/125\), \(N''(1/2+)=486/125\).

All normalized maximizers are described as follows, up to multiplication by a unimodular constant. For \(0\le\tau\le1/2\), the unique maximizer is
\[
f(z)=\left(\frac{1+r z^2}{\sqrt{1+r^2}}\right)^4.
\]
For \(\tau>1/2\), there are precisely two maximizers,
\[
f_{\pm}(z)=\left[A\left(1\pm u z+\tfrac13z^2\right)\right]^4,
\quad A=\sqrt{\frac{9\tau}{16\tau-3}},\quad u=\sqrt{\frac{2\tau-1}{3\tau}}.
\]
Both roots of each quadratic base lie outside the closed unit disk; every displayed extremizer is outer.

As a fixed-origin consequence, for \(81/256\le t\le1\), define
\[
\Phi_2(1/2,t)=\sup\{\operatorname{Re}a_2(f):\|f\|_{1/2}\le1,\ f(0)=t\}.
\]
Then the exact frontier is
\[
\Phi_2(1/2,t)=\begin{cases}
6\sqrt t-\frac{16}{3}t,&81/256\le t\le81/100,\\[4pt]
4t^{3/4}\sqrt{1-\sqrt t},&81/100\le t\le1.
\end{cases}
\]
In particular, the second coefficient and first coefficient share the same optimum on the entire terminal interval \(81/100\le t\le1\): \(\Phi_2(1/2,t)=\Phi_1(1/2,t)\). This proves the \(p=1/2,k=2\) terminal-equality case proposed as Question 2 in Brevig--Grepstad--Instanes, and identifies its sharp transition within the displayed support range.

## Assumptions and scope

The Hardy space and coefficient normalization above are essential. The parameter \(\tau\) is real and nonnegative, and the fixed-origin range explicitly stops at \(t=81/256\); no statement is made about smaller fixed-origin values. An extremizer means a unit-quasi-norm function attaining the absolute functional norm, with global unimodular phase ignored. The finite-dimensional coefficient optimization is justified for ALL Hardy functions by the 2026 outer-extremizer theorem cited below, not by assuming every Hardy function is a fourth power.

## Proof

**Existence and fourth-root reduction.** Each Taylor coefficient is a bounded functional on \(H^{1/2}\); an extremizer of \(L_\tau\) exists by Montel compactness and Fatou lower semicontinuity. By Brevig--Søvik's theorem [1], every extremizer of a nontrivial bounded functional on \(H^p\), \(0<p<1\), is outer. Consequently an extremizer \(f\) is zero-free in the disk and possesses an analytic fourth root \(g=f^{1/4}\in H^2\); its boundary modulus gives \(\|g\|_2^4=\|f\|_{1/2}=1\). Conversely, the fourth power of any \(H^2\) function has \(H^{1/2}\) quasi-norm equal to the fourth power of its \(H^2\) norm, and therefore supplies an admissible test function (regardless of outerness).

**Finite-dimensional sharp upper bound.** Write \(g(z)=a+bz+cz^2+\cdots\). Then
\[
a_0(g^4)=a^4,\qquad a_2(g^4)=4a^3c+6a^2b^2,
\]
and \(\sum_{j\ge0}|[z^j]g|^2=1\). It follows that
\[
|L_\tau(f)|\le |a|^4+4\tau|a|^3|c|+6\tau|a|^2|b|^2.
\]
No tail coefficient improves the bound; when \(\tau>0\) and \(a\ne0\), an optimizing triple uses all the available \(\ell^2\) mass. Put \(x=|a|^2\), \(v=|c|^2\), so \(|b|^2=1-x-v\), \(0\le v\le1-x\). The objective is
\[
F_\tau(x,v)=x^2+4\tau x^{3/2}\sqrt v+6\tau x(1-x-v).
\]
For fixed \(0<x\le1\), the dependence on \(v\) is strictly concave, with unconstrained maximizer \(v=x/9\). It is admissible exactly when \(x\le9/10\). Thus for \(0\le x\le9/10\),
\[
\max_v F_\tau=6\tau x+\left(1-\frac{16}{3}\tau\right)x^2,
\]
whereas for \(9/10\le x\le1\), necessarily \(v=1-x\) and \(|b|=0\). Set \(r=\sqrt{(1-x)/x}\in[0,1/3]\) in the latter region; then
\[
\max_v F_\tau=\frac{1+4\tau r}{(1+r^2)^2},\qquad
\operatorname{sign}\frac{d}{dr}\max_v F_\tau=\operatorname{sign}\bigl(\tau(1-3r^2)-r\bigr).
\]
If \(0<\tau<1/2\), the first-region quadratic increases through \(x=9/10\), and the second-region expression has its unique maximum at the root \(r/(1-3r^2)=\tau\) strictly below \(1/3\). At \(\tau=1/2\), the two maxima meet at \(x=9/10\), \(r=1/3\). If \(\tau>1/2\), the first-region quadratic is strictly concave and maximized at \(x_*=9\tau/(16\tau-3)<9/10\), while the second-region expression increases up to the shared boundary. Evaluation at \(x_*\) gives \(27\tau^2/(16\tau-3)\). For \(\tau=0\), the coefficient bound gives \(N(0)=1\), attained only by constants.

**Attainment, phases and root locations.** On the first branch choose \(a=(1+r^2)^{-1/2}\), \(b=0\), \(c=ra\). On the second choose \(a=A\), \(c=A/3\) and \(b=\pm Au\). Each triple gives \(\|g\|_2=1\), attains equality in all coefficient inequalities, and yields the displayed fourth powers. Equality in the triangle inequality (after fixing the phase of \(a\)) forces the phases of \(c\) and \(b^2\) to be positive, hence exactly the stated one or two solutions; vanishing tails follows from equality in Parseval. To verify outerness: \(1+rz^2\) has no zeros in the closed unit disk for \(r\le1/3\). On the second branch \(0<u^2<2/3\); the discriminant of \(1\pm uz+z^2/3\) is negative, and its two conjugate roots have product \(3\), hence modulus \(\sqrt3>1\). This also proves there are no omitted nonouter maximizers.

**Smooth transition.** Differentiating the two explicit formulas and the implicit relation \(\tau=r/(1-3r^2)\) gives common value and first derivative at \(\tau=1/2\); the one-sided second derivatives are \(81/125\) and \(486/125\) respectively. Thus the second-order discontinuity is \(81/25\).

**Fixed-origin frontier.** For \(t\in(81/256,1)\), the displayed extremizer has \(f(0)=t\) for exactly one \(\tau>0\) (first branch if \(t\ge81/100\), second otherwise). Rotating \(f(z)\) in the argument of \(z\) makes \(a_2\) nonnegative without changing \(f(0)=t\). Since \(a_0+\tau a_2\le N(\tau)\), the resulting \(a_2\) value is the exact \(\Phi_2\) maximum. On the first branch \(t=(1+r^2)^{-2}\) and \(a_2=4tr=4t^{3/4}\sqrt{1-\sqrt t}\). On the second \(t=A^4\), \(a_2=4A^4/3+6A^4u^2=6\sqrt t-16t/3\). At \(t=81/256\), letting \(\tau\to\infty\) and using \(N(\tau)/\tau\to27/16\) gives the upper bound \(\Phi_2\le27/16\), and the limiting quadratic fourth power gives equality. At \(t=1\), the only admissible function is constant, giving zero. Finally Brevig--Grepstad--Instanes [3], Theorem 12(ii), yields \(\Phi_1(1/2,t)=4t^{3/4}\sqrt{1-\sqrt t}\) throughout \(t\ge81/100\), proving terminal equality. This threshold is sharp within the stated fixed-origin range. Indeed, the known global first-coefficient bound is \(\Phi_1(1/2,t)\le3\sqrt3/4\) [2,3]. For \(81/256\le t\le1/2\), writing \(y=\sqrt t\) gives \(y\in[9/16,1/\sqrt2]\); by concavity of \(6y-16y^2/3\), its minimum over this interval is strictly larger than \(3\sqrt3/4\). For \(1/2\le t<81/100\), the known high-origin \(\Phi_1\) formula applies and the two squared candidate values differ by \(\frac49y^2(10y-9)^2>0\). Hence \(\Phi_2(1/2,t)>\Phi_1(1/2,t)\) for all \(81/256\le t<81/100\), with equality exactly on the terminal interval in the proved range.

## Verification

The symbolic calculations in `checker.py` verify exact rational transition values, critical slopes and curvature, support frontier junctions, the pure-second-coefficient endpoint, and the explicit normalization of extremal polynomials. Its deterministic sampling tests the analytical upper bound against generic complex coefficient triples. Run `python3 checker.py` with standard-library Python. These finite tests neither establish the infinite-dimensional outer-reduction theorem nor replace the calculus and equality-case arguments above.

## Relationship to prior work

Brevig--Søvik [1] proves outer necessity for arbitrary bounded Hardy functionals but does not compute the mixed functional \(a_0+\tau a_2\). Brevig--Saksman [2] computes the unconditioned sharp second coefficient (recovered as \(\lim_{\tau\to\infty}N(\tau)/\tau=27/16\)); their result does not determine the mixed profile, phase transition, or full fixed-origin frontier. Brevig--Grepstad--Instanes [3] solves \(\Phi_1\) and poses terminal equality of \(\Phi_2\) and \(\Phi_1\) as Question 2; their analysis did not settle that statement for \(p=1/2\). Thus the theorem provides an explicitly delimited affirmative case of their question with sharp threshold within the established support range.

## Limitations

The theorem applies specifically to \(H^{1/2}\), real nonnegative \(\tau\), and jet orders zero and two. The fixed-origin formula is **not** asserted below \(t=81/256\). The result relies on the published outer-extremizer theorem [1] and established high-origin first-coefficient formula [3]; it does not independently reprove their proofs. Stronger equivalent results in older extremal coefficient literature, particularly less accessible classical works, remain a potential historical-priority risk. No independent audit has been performed.

## References

[1] Ole Fredrik Brevig and Øistein Søvik, *Extremals for linear functionals on \(H^p\) are outer when \(0<p<1\)*, arXiv:2610.21788, first submitted October 15, 2026, Theorem 1. https://arxiv.org/abs/2610.21788

[2] Ole Fredrik Brevig and Eero Saksman, *Coefficient estimates for \(H^p\) spaces with \(0<p<1\)*, arXiv:1905.09547, 2019; *Proc. Amer. Math. Soc.* 148 (2020), 3911–3924. https://arxiv.org/abs/1905.09547

[3] Ole Fredrik Brevig, Sigrid Grepstad and Sarah May Instanes, *F. Wiener’s trick and an extremal problem for \(H^p\)*, arXiv:2011.07790 (2020); *Comput. Methods Funct. Theory* 23 (2023), 697–722, Theorem 12 and Question 2. https://doi.org/10.1007/s40315-022-00469-x
