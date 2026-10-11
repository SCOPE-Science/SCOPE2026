# Exact Ptolemy constant of dual two-dimensional Lorentz spaces below exponent two
## Finding
Let \(1<q<2\), \(0<\omega<1\), and let \(X=d^{(2)}(\omega,q)\) be the real two-dimensional Lorentz sequence space
\[
\|(x_1,x_2)\|_X=\bigl((x_1^*)^q+\omega(x_2^*)^q\bigr)^{1/q},
\]
where \(x_1^*\ge x_2^*\ge0\) is the decreasing rearrangement of \((|x_1|,|x_2|)\). Put
\[
\rho=\omega^{1/(2-q)}.
\]
Then the dual space has exact Ptolemy constant
\[
C_{\mathrm{Pt}}(X^*)
=
(1+\rho^2)^{(2-q)/q}
\max\left\{1,\frac{2}{(1+\omega)^{2/q}}\right\}.
\]
This is exactly the known value of \(C_{\mathrm{Pt}}(X)\). Consequently,
\[
C_{\mathrm{Pt}}\!\left(d^{(2)}(\omega,q)\right)
=
C_{\mathrm{Pt}}\!\left(d^{(2)}(\omega,q)^*\right)
\]
for every \(0<\omega<1\) and every \(1\le q<\infty\).

For \(1<q<2\), the formula has a phase boundary at
\[
\omega=2^{q/2}-1.
\]
Below that boundary the factor \(2/(1+\omega)^{2/q}\) is active; above it the maximum equals \(1\).

## Assumptions and scope
All spaces are real and two-dimensional. For \(X=d^{(2)}(\omega,q)\), the Lorentz norm is defined by decreasing rearrangement:
\[
\|(x_1,x_2)\|_X
=
\bigl((x_1^*)^q+\omega(x_2^*)^q\bigr)^{1/q},
\qquad
0<\omega<1,\quad 1<q<2.
\]
The Ptolemy constant is
\[
C_{\mathrm{Pt}}(Y)
=
\sup
\frac{\|x-y\|\,\|z\|}
{\|x-z\|\,\|y\|+\|z-y\|\,\|x\|},
\]
where the supremum is over nonzero pairwise distinct \(x,y,z\in Y\). The endpoint and super-Hilbert ranges used in the final duality corollary are previously known; the new calculation is the missing dual range \(1<q<2\).

## Proof
Let
\[
p=\frac{q}{q-1}>2.
\]
Because \(X\) is absolute and permutation invariant, the dual norm is also absolute and permutation invariant. For \(u=(u_1,u_2)\), set
\[
M=\max\{|u_1|,|u_2|\},
\qquad
m=\min\{|u_1|,|u_2|\}.
\]
Maximizing \(Mx_1+mx_2\) over
\[
x_1\ge x_2\ge0,
\qquad
x_1^q+\omega x_2^q\le1,
\]
gives
\[
\|u\|_{X^*}
=
\begin{cases}
\bigl(M^p+\omega^{1-p}m^p\bigr)^{1/p},
&
m\le\omega M,\\[4pt]
\dfrac{M+m}{(1+\omega)^{1/q}},
&
m\ge\omega M.
\end{cases}
\]
Indeed, the unconstrained Hölder optimizer satisfies
\[
\frac{x_2}{x_1}
=
\left(\frac{m}{\omega M}\right)^{1/(q-1)},
\]
and lies in the ordered cone exactly when \(m\le\omega M\); otherwise the optimum occurs at \(x_1=x_2\).

Compare the dual norm with the Euclidean norm. For an ordered direction \((1,r)\), \(0\le r\le1\), define
\[
F(r)=\frac{\|(1,r)\|_{X^*}}{\sqrt{1+r^2}}.
\]
On \(0\le r\le\omega\),
\[
F(r)
=
\frac{\bigl(1+\omega^{1-p}r^p\bigr)^{1/p}}
{\sqrt{1+r^2}},
\]
and
\[
\frac{F'(r)}{F(r)}
=
\frac{r\bigl(\omega^{1-p}r^{p-2}-1\bigr)}
{\bigl(1+\omega^{1-p}r^p\bigr)(1+r^2)}.
\]
Thus this branch has a unique minimum at
\[
\rho=\omega^{1/(2-q)},
\]
because
\[
\omega^{1-p}\rho^{p-2}=1.
\]
Since \(1/(2-q)>1\) and \(0<\omega<1\), one has \(0<\rho<\omega\). At the minimum,
\[
\omega^{1-p}\rho^p=\rho^2,
\]
so
\[
F(\rho)
=
(1+\rho^2)^{1/p-1/2}
=
(1+\rho^2)^{-(2-q)/(2q)}.
\]

On \(\omega\le r\le1\),
\[
F(r)
=
\frac{1+r}{(1+\omega)^{1/q}\sqrt{1+r^2}},
\]
which is strictly increasing for \(r<1\). Therefore the exact global Euclidean comparison constants are
\[
a
=
(1+\rho^2)^{-(2-q)/(2q)},
\]
and
\[
b
=
\max\left\{
1,\frac{\sqrt2}{(1+\omega)^{1/q}}
\right\},
\]
meaning
\[
a\|v\|_2\le\|v\|_{X^*}\le b\|v\|_2
\qquad(v\in\mathbb R^2).
\]
Euclidean Ptolemy then gives
\[
C_{\mathrm{Pt}}(X^*)
\le
\left(\frac ba\right)^2
=
(1+\rho^2)^{(2-q)/q}
\max\left\{
1,\frac{2}{(1+\omega)^{2/q}}
\right\}.
\]

It remains to attain this upper bound.

First suppose
\[
0<\omega\le2^{q/2}-1.
\]
Then
\[
b=\frac{\sqrt2}{(1+\omega)^{1/q}}.
\]
Put
\[
\lambda=\frac{1-\rho}{1+\rho},
\qquad
x=(\rho,1),
\qquad
y=\lambda(-1,\rho),
\qquad
z=(1-\rho)(-1,1).
\]
Let
\[
A=(1+\rho^2)^{1/p},
\qquad
D=\frac2{(1+\omega)^{1/q}}.
\]
Direct use of the dual norm formula gives
\[
\|x\|=A,
\quad
\|y\|=\lambda A,
\quad
\|x-z\|=A,
\quad
\|z-y\|=\lambda A,
\]
and
\[
\|z\|=(1-\rho)D,
\qquad
\|x-y\|
=
\frac{1+\rho^2}{1+\rho}D.
\]
Hence the Ptolemy ratio is
\[
\frac{2}{(1+\omega)^{2/q}}
(1+\rho^2)^{(2-q)/q}.
\]

Now suppose
\[
2^{q/2}-1\le\omega<1.
\]
Then \(b=1\). Take
\[
x=(1,-\rho),
\qquad
y=(-1,-\rho),
\qquad
z=(0,-\rho-\rho^{-1}).
\]
With the same
\[
A=(1+\rho^2)^{1/p},
\]
the dual norm formula yields
\[
\|x\|=\|y\|=A,
\qquad
\|x-y\|=2,
\qquad
\|z\|=\rho+\rho^{-1},
\]
and
\[
\|x-z\|=\|z-y\|=\frac A\rho.
\]
Thus the Ptolemy ratio is
\[
\frac{1+\rho^2}{A^2}
=
(1+\rho^2)^{(2-q)/q}.
\]
At \(\omega=2^{q/2}-1\), the two formulas agree. Therefore the upper bound is attained throughout \(0<\omega<1\), proving
\[
C_{\mathrm{Pt}}(X^*)
=
(1+\rho^2)^{(2-q)/q}
\max\left\{
1,\frac{2}{(1+\omega)^{2/q}}
\right\}.
\]

The previously established primal formula for \(1\le q<2\) is exactly the same expression, while primal-dual equality was already known for \(q=1\) and \(q\ge2\). Hence the equality
\[
C_{\mathrm{Pt}}\!\left(d^{(2)}(\omega,q)\right)
=
C_{\mathrm{Pt}}\!\left(d^{(2)}(\omega,q)^*\right)
\]
holds for every \(0<\omega<1\) and every \(1\le q<\infty\).

## Verification
The dual norm formula is derived from the defining constrained maximization rather than assumed from numerics. The ordered ratio \(r=m/M\) exhausts all nonzero directions because the norm is absolute and permutation invariant. The derivative of \(F\) has exactly one zero on the first branch, at \(r=\rho\), and the second branch is strictly increasing, so the Euclidean comparison constants are global.

Both lower-bound constructions are symbolic. In the first regime, every vector appearing in the Ptolemy ratio lies in the stated branch of the dual norm because \(0<\rho<\omega<1\). In the second regime, the differences \((1,\pm\rho^{-1})\) have ordered ratio \(\rho<\omega\), so the first branch again applies exactly. No finite sampling, timeout, or numerical optimization is used as a proof.

As a consistency check, the phase boundary is exactly the condition
\[
\frac{\sqrt2}{(1+\omega)^{1/q}}=1,
\]
equivalent to
\[
\omega=2^{q/2}-1.
\]

## Relationship to prior work
Zuo's 2018 treatment of two-dimensional Lorentz sequence spaces gives the primal Ptolemy constant for \(1\le q<2\) and the dual value for \(q=1\) and \(q\ge2\). Its Remark 2 explicitly identifies the dual range \(1<q<2\) as unknown and asks whether a Lorentz space and its dual always have the same Ptolemy constant. The formula proved here fills exactly that missing range.

Zuo's 2012 paper develops the Ptolemy constant for absolute normalized norms on \(\mathbb R^2\), giving the two-dimensional framework and MSC 46B20 ownership used by the later Lorentz calculation. The present proof does not follow merely from the general midpoint criterion there: it uses the explicit Lorentz dual norm and two separate extremizing configurations across the weight phase boundary.

A semantic comparison against indexed exact-constant records located the known \(q=2\) Lorentz identity and the exact Euclidean Banach--Mazur distance of primal Lorentz spaces below exponent two, but neither statement implies the dual Ptolemy equality established here.

## Limitations
The exact new calculation is two-dimensional and assumes \(0<\omega<1\) and \(1<q<2\). The all-\(q\) statement is a corollary obtained by combining this missing range with previously known endpoint and super-Hilbert cases. No claim is made for Lorentz sequence spaces in dimension greater than two or for more general weight vectors.

The checked searches did not locate a later published solution of the 2018 question, but absence from the searched indexes is not a proof of worldwide novelty. A later unindexed solution under different notation remains a bibliographic residual risk.

## References
1. Z. Zuo, “The Ptolemy constant of absolute normalized norms on \(\mathbb R^2\),” *Journal of Inequalities and Applications* 2012, Article 107, DOI 10.1186/1029-242X-2012-107; published 2012-05-17.
2. Z. Zuo, “On the Ptolemy constant of Lorentz sequence spaces and their duals,” *ScienceAsia* 44 (2018), 340--345, DOI 10.2306/scienceasia1513-1874.2018.44.340.
