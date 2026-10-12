# Sharp mean-stage obstruction and two-point A-stability frontier for randomized implicit RK2

## Finding

Consider the semi-implicit and implicit randomized two-stage Runge–Kutta updates introduced in [1], but sample each stage fraction independently from an arbitrary common law on \([0,1]\), rather than necessarily uniformly. On the scalar Dahlquist equation \(y'=\lambda y\), with \(z=h\lambda\), both updates have the amplification function
\[
R(z,t)=1+\frac{z}{1-tz}=\frac{1+(1-t)z}{1-tz}.
\]
They are **mean-square A-stable** for a stage law if \(\mathbb E|R(z,T)|^2<1\) for every \(z\in\mathbb C\) with \(\operatorname{Re}z<0\).

**Unified distributional stability theorem.** For independent identically distributed stages \(T\in[0,1]\), the following hold.

1. If \(\mathbb E T=1/2\), then
\[
\lim_{x\to\infty}\mathbb E|R(-x,T)|^2
=\mathbb E\!\left[\frac{(1-T)^2}{T^2}\right]
\ge 1+12\operatorname{Var}(T),
\]
with the quotient defined as \(+\infty\) at \(T=0\). The constant \(12\) is the *largest universal coefficient* valid for all such laws. Hence mean-square A-stability holds among these mean-stage-preserving laws **if and only if** \(T=1/2\) almost surely. For every nondegenerate such law, some sufficiently stiff negative real \(z\) yields exponentially growing expected squared iterates.

2. For every \(a\in(0,1/2)\), choose a two-point stage law
\[
\mathbb P(T=a)=p,\qquad \mathbb P(T=1)=1-p,\qquad 0\le p\le1.
\]
This law is mean-square A-stable **if and only if**
\[
\boxed{\quad p\le p_*(a):=\left(\frac{a}{1-a}\right)^2.\quad}
\]
Thus nonconstant stage randomization can preserve mean-square A-stability even while assigning positive probability to a stage below the deterministic \(1/2\) threshold. At \(a=1/4\), the exact sharp cutoff is \(p_*=1/9\), and the boundary law is genuinely random and mean-square A-stable.

These statements form one stability-design dichotomy for the same amplification map: maintaining the midpoint stage mean forbids nontrivial mean-square A-stable randomization, whereas a quantitatively specified upward bias permits it.

## Assumptions and scope

All statements concern the scalar complex linear test equation \(y'=\lambda y\) with fixed real step \(h>0\), \(z=h\lambda\) in the open left half-plane, deterministic initial value \(y_0\ne0\), and independently identically distributed stage fractions \(T_j\in[0,1]\). The numerical iterates are \(Y_n=y_0\prod_{j=1}^{n}R(z,T_j)\). The denominator \(1-T_j z\) cannot vanish when \(\operatorname{Re}z<0\). By independence,
\[
\mathbb E|Y_n|^2=|y_0|^2\left(\mathbb E|R(z,T)|^2\right)^n.
\]
A law with \(\mathbb E T=1/2\) is called **mean-stage preserving** only in the sense of its stage parameter and scalar local mean amplification through quadratic order; no general order or unbiasedness assertion is made for nonlinear equations.

For completeness, the semi-implicit stage equation is \(W=Y+T h\lambda W\), followed by \(Y^+=Y+h\lambda W\). The fully implicit update is \(Y^+=Y+h\lambda((1-T)Y+TY^+)\). Solving either gives the stated \(R\), without a restriction on the distribution of \(T\) apart from the hypotheses above.

## Proof

**1. Exact stability identity.** Write \(z=-u+iv\), where \(u>0\), \(v\in\mathbb R\), and \(s=|z|^2=u^2+v^2>0\). Directly expanding numerator and denominator gives
\[
|R(z,t)|^2-1=\frac{-2u+(1-2t)s}{1+2tu+t^2s},\qquad 0\le t\le1.
\]
In particular, for \(t=1/2\) this expression is strictly negative at every \(u>0\): the deterministic midpoint method is mean-square A-stable.

**2. Universal mean-stage obstruction and the optimal constant.** Set \(g(t)=((1-t)/t)^2\) for \(t>0\), with \(g(0)=+\infty\). The following is an exact factorization, not a numerical estimate:
\[
\begin{aligned}
g(t)&-\left[1-8\left(t-\tfrac12\right)+12\left(t-\tfrac12\right)^2\right]\\
&=\frac{(1-t)(2t-1)^2(3t+1)}{t^2}\ge0
\qquad(0<t\le1).
\end{aligned}
\]
For \(\mathbb E T=1/2\), expectation cancels the linear term and identifies \(\mathbb E(T-1/2)^2=\operatorname{Var}(T)\), proving \(\mathbb E g(T)\ge1+12\operatorname{Var}(T)\). At an atom \(T=0\), the inequality remains true in the extended-real sense.

For each fixed \(t>0\), \(R(-x,t)\to-(1-t)/t\) as \(x\to\infty\); at \(t=0\) its squared magnitude diverges. Furthermore \(x\mapsto R(-x,t)\) decreases from \(1\) to \(-(1-t)/t\), so \(|R(-x,t)|^2\le\max\{1,g(t)\}\). Dominated convergence gives the stated limit when \(\mathbb E g(T)<\infty\); otherwise Fatou's lemma gives limit \(+\infty\). If \(\operatorname{Var}(T)>0\), the limit exceeds one, so some finite \(x>0\) has \(\mathbb E|R(-x,T)|^2>1\), which yields exponential mean-square growth by the independent-step identity. If \(\operatorname{Var}(T)=0\), the mean constraint forces \(T=1/2\) almost surely, covered by step 1.

To see that \(12\) cannot be increased, for every \(0<\varepsilon<1/2\) let \(T_\varepsilon=1\) with probability \(\varepsilon\) and otherwise
\[
T_\varepsilon=\frac{1/2-\varepsilon}{1-\varepsilon}.
\]
Then \(\mathbb E T_\varepsilon=1/2\), its variance is strictly positive, and exact rational simplification yields
\[
\frac{\mathbb E g(T_\varepsilon)-1}{\operatorname{Var}(T_\varepsilon)}
=\frac{4(\varepsilon-1)(4\varepsilon-3)}{(2\varepsilon-1)^2}
\longrightarrow 12\qquad(\varepsilon\downarrow0).
\]
The sharpness is an infimum; it is not claimed to be attained by a nondegenerate mean-stage-preserving law.

**3. Sharp two-point frontier.** For \(0<a<1/2\), let \(D_a=1+2au+a^2s\) and \(D_1=1+2u+s\), which are both strictly positive. Applying step 1 to the two-point law gives
\[
F_p(z):=\mathbb E|R(z,T)|^2-1
=p\frac{-2u+(1-2a)s}{D_a}
+(1-p)\frac{-2u-s}{D_1}.
\]
At \(p=0\), the right-hand side is strictly negative. At \(p=p_*(a)=a^2/(1-a)^2\), multiply by the positive denominator \(D_aD_1\) and simplify exactly:
\[
D_aD_1F_{p_*}(z)
=-\frac{(1-2a)(1+a)s+2asu+4au^2+2(1-a)u}{1-a}<0.
\]
Every term in the numerator is nonnegative, and the last term is positive. Since \(F_p(z)\) is affine in \(p\), its strict negativity at both endpoints \(p=0\) and \(p=p_*\) proves A-stability for every \(0\le p\le p_*\).

Conversely, taking \(z=-x\) with \(x\to\infty\) gives
\[
\lim_{x\to\infty}\mathbb E|R(-x,T)|^2
=p\left(\frac{1-a}{a}\right)^2.
\]
For \(p>p_*\), this exceeds one, so some negative real step is mean-square unstable. This proves the claimed if-and-only-if boundary, including strict stability for all finite left-half-plane \(z\) when \(p=p_*\).

## Verification

The accompanying standard-library script `verify.py` directly expands the exact polynomial identities after clearing denominators, so those *finite algebraic identities* are verified at the coefficient level rather than by sampling. It also evaluates exact-rational instances of the stability function and the two-point design over 309 cases, including a stiff instability witness above threshold and a sequence tending to the sharp variance coefficient. Reproduce with `python3 verify.py`; the expected completion markers report two exact polynomial identities and 309 rational tests. Universal quantifiers are justified by the displayed analytic proof, not by finite tests.

## Relationship to prior work

The motivating randomized semi-implicit and implicit RK2 schemes are defined by Bochacik and Przybyłowicz [1], which imposes independent uniform stages. Its mean-square stability analysis establishes that the uniform-stage law is not mean-square A-stable and gives its bounded stability region. This finding uses the **same scalar stability map**, changes only the stage distribution, and establishes a sharp distribution-free variance penalty at mean stage \(1/2\) together with an exact two-atom A-stable design threshold. The uniform-law conclusion in [1] does not imply either new quantified or constructive statement.

Earlier randomized **explicit** RK2 stability theory [2] uses a polynomial stability map rather than the present rational one, so it cannot directly imply these distributional conclusions. Eisenmann and coauthors [3] study a different randomized singly diagonally implicit Runge–Kutta tableau whose individual realizations are algebraically stable, with a random parameter supported on \([1/2,1]\); that result does not provide the two-point threshold for [1]'s amplification map with a positive mass below \(1/2\). Higham's classical stochastic-theta study [4] addresses a stochastic differential equation with a noise term and a different parameterization, rather than the distribution of an implicit-stage coefficient on a deterministic Dahlquist equation. An equivalent derivation in specialized literature has not been excluded.

## Limitations

The only stability notion proved is scalar-test mean-square A-stability for independent identically distributed stages. It does not imply B-stability, algebraic stability, nonlinear convergence, pathwise stability under arbitrary dependence, or the stiff accuracy of a general system. The upward-biased two-point stage distribution generally loses the midpoint matching of the scalar local expected amplification through order two: indeed \(\mathbb E R(z,T)=1+z+(\mathbb E T)z^2+O(z^3)\) as \(z\to0\), and at the two-point boundary \(\mathbb E T=1-a^2/(1-a)\ne1/2\). The \(12\) bound is a sharp distribution-free lower bound for a *stiff limit*, not a finite-step rate bound at each fixed \(z\). Independent validation and a complete priority determination are not claimed.

## References

[1] T. Bochacik and P. Przybyłowicz, *Convergence and stability of randomized implicit two-stage Runge–Kutta schemes*, arXiv:2404.19059v1 (first posted 2024-04-29), revised arXiv:2404.19059v3 (2025). https://arxiv.org/abs/2404.19059

[2] T. Bochacik, M. Goćwin, P. M. Morkisz, and P. Przybyłowicz, *Randomized Runge–Kutta method—stability and convergence under inexact information*, arXiv:2006.12131 (2020). https://arxiv.org/abs/2006.12131

[3] M. Eisenmann, M. Jans, R. Kruse, and H. Podhajsky, *Error Bound and Stability Analysis for a Randomized Singly Diagonally Implicit Runge–Kutta Method*, arXiv:2607.18928 (2026), Sections 3 and 5. https://arxiv.org/abs/2607.18928

[4] D. J. Higham, *Mean-square and asymptotic stability of the stochastic theta method*, SIAM Journal on Numerical Analysis **38** (2000), 753–769, DOI:10.1137/S003614299834736X. https://doi.org/10.1137/S003614299834736X
