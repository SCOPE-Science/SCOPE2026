# Corrected conditional endpoint law for the Feynman checker
## Finding
In the basic Feynman-checker model, write the arrow as \(a(x,t)=a_1(x,t)+i a_2(x,t)\). For \(0<v<1\), define the conditional endpoint statistic
\[
G_t(v)=\frac{2}{t}\sum_{\substack{0\le x\le vt\\x+t\ \mathrm{even}}}\left|\frac{a_2(x,t)}{a(x,t)}\right|^2.
\]
The parity restriction simply selects the reachable sites on the \(t\)-th horizontal. For \(0<x<t\) these amplitudes are nonzero in the basic massive model, so the ratio is well defined.

Put
\[
v_*=\frac1{\sqrt2}.
\]
Then, for every fixed \(0<v<1\),
\[
\lim_{t\to\infty}G_t(v)=G(v),
\]
where
\[
G(v)=\frac14\left(1+2v-\sqrt{1-2v^2}+\log\frac{1+\sqrt{1-2v^2}}2\right),
\qquad 0<v<v_*,
\]
and
\[
G(v)=\frac14+\frac v2+\frac14\left(\log\frac{v}{\sqrt2}+\sqrt{2v^2-1}-\arctan\sqrt{2v^2-1}\right),
\qquad v_*<v<1.
\]
At the wall,
\[
G(v_*)=\frac{1+\sqrt2-\log2}{4},
\qquad
G'(v_*^-)=G'(v_*^+)=\frac{2+\sqrt2}{4}.
\]
More precisely,
\[
G(v)=G(v_*)+\frac{2+\sqrt2}{4}(v-v_*)+\frac{2^{1/4}}3|v-v_*|^{3/2}+O((v-v_*)^2).
\]
Thus \(G\) is \(C^1\) but not \(C^2\) at \(v_*\). This proves the nonanalytic wall transition conjectured in the source.

Problem 4 of Skopenkov--Ustinov proposed, on \(0<v<v_*\), the different expression
\[
\frac12\left(1+v-\sqrt{1-v^2}+\log\frac{1+\sqrt{1-v^2}}2\right).
\]
That proposed expression is not the limit. Its first discrepancy from the correct branch occurs at order \(v^4\) near \(v=0\), and its derivative differs from the exact phase-averaged local density for every \(v>0\). The second branch above also answers the source's request to compute the same limit for \(v_*<v<1\).

## Assumptions and scope
The statement uses Definition 1 of Skopenkov--Ustinov, namely the basic checker with unit lattice step and unit mass normalization, first step upwards-right, and
\[
a(x,t)=2^{(1-t)/2}i\sum_s(-i)^{\operatorname{turns}(s)}.
\]
We use \(a_1=\operatorname{Re}a\) and \(a_2=\operatorname{Im}a\). The sum defining \(G_t(v)\) is over reachable sites \(x+t\) even. The theorem is a fixed-velocity, large-integer-time statement; it does not assert a uniform rate in \(v\) through the wall.

The source interprets \(i a_2/a\) as the conditional amplitude for the last move to be upwards-right, and in the spin-chain interpretation as the conditional endpoint-sign statistic. This is the order parameter appearing in its Problem 4.

## Proof
Write the final time as \(t=n+1\). In the allowed region \(0\le u<v_*\), Theorem 2 of Skopenkov--Ustinov gives, uniformly on compact velocity intervals, the two component asymptotics
\[
a_1(X,n+1)=C_n(X)\sin\theta(X,n)+O(n^{-3/2}),
\]
\[
a_2(X,n+1)=C_n(X-1)\sqrt{\frac{n+X-1}{n-X+1}}\cos\theta(X-1,n)+O(n^{-3/2}),
\]
with \(C_n(X)\asymp n^{-1/2}\). Put \(u=X/n\) and
\[
\phi(u)=\arcsin\frac1{\sqrt{2(1-u^2)}}-u\arcsin\frac{u}{\sqrt{1-u^2}},
\qquad
\alpha(u)=\arcsin\frac{u}{\sqrt{1-u^2}}.
\]
The source phase is \(\theta(X,n)=n\phi(X/n)+\pi/4\), and direct differentiation gives
\[
\phi'(u)=-\alpha(u).
\]
Consequently, uniformly on compact subintervals of \([0,v_*)\), if \(\vartheta=\theta(X-1,n)\) and \(q=(1+u)/(1-u)\), then
\[
\left|\frac{a_2(X,n+1)}{a(X,n+1)}\right|^2
=R(u,\vartheta)+O(n^{-1}),
\]
where
\[
R(u,\vartheta)=
\frac{q\cos^2\vartheta}{\sin^2(\vartheta-\alpha(u))+q\cos^2\vartheta}.
\]
The denominator is a positive quadratic form. Indeed, its determinant is \(q\cos^2\alpha(u)>0\) for \(u<v_*\), so division is uniform on compact allowed-velocity intervals.

The oscillatory-sum argument used by Skopenkov--Ustinov for their large-time distribution applies to Problem 4 explicitly: their Section 12.4 states that results such as Problems 4 and 5 follow the same four-step stationary-phase, oscillatory-sum, Riemann-sum, and boundary-control plan. Expanding the smooth \(\pi\)-periodic function \(R(u,\vartheta)\) in Fourier modes, the nonzero modes vanish after the parity-lattice average by the same exponential-sum estimate. The surviving phase average is
\[
p_-(u)=\frac1\pi\int_0^\pi R(u,\vartheta)\,d\vartheta.
\]
Set \(c=\cos\alpha(u)\), \(s=\sin\alpha(u)\), and \(z=\tan\vartheta\). Then
\[
p_-(u)=\frac q\pi\int_{-\infty}^{\infty}
\frac{dz}{\bigl((cz-s)^2+q\bigr)(1+z^2)}.
\]
Using
\[
\int_{-\infty}^{\infty}
\frac{dz}{\bigl((z-B)^2+A^2\bigr)(1+z^2)}
=rac{\pi(A+1)}{A\bigl((A+1)^2+B^2\bigr)},
\]
with \(A=\sqrt q/c\) and \(B=s/c\), followed by
\[
c=\frac{\sqrt{1-2u^2}}{\sqrt{1-u^2}},
\]
one gets
\[
p_-(u)=\frac12\left(1+\frac{u}{1+\sqrt{1-2u^2}}\right).
\]
The parity spacing is two, so the prefactor \(2/t\) turns the sum into the ordinary integral. Hence
\[
G(v)=\int_0^v p_-(u)\,du,
\]
which gives the first displayed branch.

For the hidden region \(v_*<u<1\), Theorem 4 of Skopenkov--Ustinov, originating in the Sunada--Tate steepest-descent analysis, gives adjacent-site component asymptotics. On any compact hidden-velocity interval the Sunada--Tate proof chooses a compact parameter neighborhood, isolates a unique nondegenerate saddle, and obtains a uniform stationary-phase expansion. For the same final site \(X\), the two source formulas evaluate their rate function at \(X/n\) and \((X-1)/n\). Therefore
\[
\left|\frac{a_2(X,n+1)}{a_1(X,n+1)}\right|
\longrightarrow
\sqrt{\frac{1+u}{1-u}}\exp\frac{H'(u)}2.
\]
For unit mass and lattice step,
\[
H(u)=-2\operatorname{arcosh}\frac1{\sqrt{2(1-u^2)}}
+2u\operatorname{arcosh}\frac{u}{\sqrt{1-u^2}},
\]
and differentiation simplifies to
\[
H'(u)=2\operatorname{arcosh}\frac{u}{\sqrt{1-u^2}}.
\]
If \(s_+(u)=\sqrt{2u^2-1}\), then
\[
r(u):=\lim\left|\frac{a_2}{a_1}\right|=\frac{u+s_+(u)}{1-u},
\]
so the limiting conditional probability is
\[
p_+(u)=\frac{r(u)^2}{1+r(u)^2}
=\frac12+\frac{1+s_+(u)}{4u}.
\]
Compact-uniform convergence gives the Riemann-sum limit away from the wall. Since every summand lies in \([0,1]\), deleting a velocity strip of width \(\delta\) changes \(G_t\) by at most \(\delta+O(t^{-1})\); this boundedness lets \(\delta\downarrow0\) and joins the allowed and hidden pieces. Integrating \(p_+\) from \(v_*\), with the wall value supplied by the first branch, yields the second formula.

Finally, direct expansion of the two elementary branches at \(v_*\) gives
\[
G(v)=G(v_*)+\frac{2+\sqrt2}{4}(v-v_*)
+\frac{2^{1/4}}3|v-v_*|^{3/2}+O((v-v_*)^2),
\]
which proves the stated \(C^1\)-but-not-\(C^2\) transition.

## Verification
The accompanying `check_limit.py` verifies the closed-form derivatives, wall matching, the \(|v-v_*|^{3/2}\) coefficient, the algebraic simplification of the hidden-region local ratio, and the finite-time checker recurrence. The recurrence is used only as a numerical consistency check, not as proof of the infinite-time limit.

A finite recurrence at large time shows the corrected allowed-region curve approaching the data and separates it from the expression printed in Problem 4 near the wall. The analytic proof, not the finite computation, establishes the theorem.

## Relationship to prior work
Skopenkov--Ustinov define exactly this statistic and state Problem 4 as open. They propose an explicit formula for \(0<v<1/\sqrt2\), ask for a proof, and separately ask for the value on \(1/\sqrt2<v<1\). Their Section 12.4 explicitly says that results such as Problem 4 should follow the same four-step oscillatory-sum strategy used for their distributional limit, but it does not carry out the nonlinear phase average.

Sunada--Tate provide the underlying allowed-region oscillatory asymptotics, wall asymptotics, and hidden-region large-deviation asymptotics for one-dimensional quantum walks. Those results control transition amplitudes/probabilities; they do not state the nonlinear conditional ratio average \(G_t\), its piecewise elementary limit, or the wall regularity above.

Targeted searches for the exact Problem 4 statement, conditional chirality/endpoint-sign terminology, the wall \(1/\sqrt2\), and the cumulative ratio did not locate a published formula covering this result. Later papers citing the source that were inspected concern modified checker models, absorption, external fields, number-theoretic properties, or second-quantized variants rather than this order parameter.

## Limitations
The theorem is for the basic unit-step, unit-mass checker and positive velocities. Reflection variants can be studied separately; they are not claimed here. No quantitative global convergence rate uniform through \(v_*\) is asserted. The proof uses published asymptotic expansions on compact subsets and boundedness to cross the wall. The finite checker replay is corroborative only.

An equivalent calculation may exist in unindexed notes or under quantum-walk local-chirality terminology. The literature search found no such covering statement, but absence from the searched sources is not a proof of bibliographic uniqueness.

## References
1. M. B. Skopenkov and A. V. Ustinov, “Feynman checkers: towards algorithmic quantum theory,” arXiv:2007.12879v1; Russian Mathematical Surveys 77 (2022), 445–530, DOI: 10.1070/RM10025.
2. T. Sunada and T. Tate, “Asymptotic behavior of quantum walks on the line,” arXiv:1108.1878v1; Journal of Functional Analysis 262 (2012), 2608–2645, DOI: 10.1016/j.jfa.2011.12.016.
