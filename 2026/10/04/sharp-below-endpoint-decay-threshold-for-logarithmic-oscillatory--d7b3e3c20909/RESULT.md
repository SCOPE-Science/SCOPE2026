# Sharp below-endpoint decay threshold for logarithmic oscillatory multipliers

## Finding

Let
\[
L(\xi)=\frac12\log(e^2+|\xi|^2)
\]
and
\[
m_{\gamma,\beta}(\xi)
=
L(\xi)^{-\beta}e^{iL(\xi)^\gamma},
\qquad
\gamma>1,
\qquad
\beta\ge0.
\]
For every
\[
1<p<\infty,
\qquad
p\ne2,
\]
boundedness
\[
T_{m_{\gamma,\beta}}:L^p(\mathbb R^d)\to L^p(\mathbb R^d)
\]
forces
\[
\beta
\ge
d(\gamma-1)
\left|
\frac12-\frac1p
\right|.
\]

There is a quantitative localized form. One can choose fixed nonzero functions
\[
\chi,\chi_0\in C_c^\infty(\mathbb R^d\setminus\{0\}),
\]
with
\[
\chi_0=1
\quad\text{on}\quad
\operatorname{supp}\chi,
\]
such that, for all sufficiently large \(R\),
\[
\left\|
T_{\chi_0(\cdot/R)m_{\gamma,\beta}}
\right\|_{L^p\to L^p}
\ge
c
(\log R)^{
d(\gamma-1)|1/2-1/p|-\beta
}.
\]

Consequently the sufficient strong-\(L^p\) threshold proved in the motivating paper cannot be lowered below its critical logarithmic exponent. The equality case is not decided by this lower bound.

## Assumptions and scope

The Fourier multiplier convention is
\[
T_mf=\mathcal F^{-1}(m\widehat f).
\]
The dimension satisfies
\[
d\ge1.
\]
The result concerns the specific logarithmic radial model above, not every symbol in the source's localized logarithmic Miyachi class.

The source's current version proves strong \(L^p\) boundedness whenever
\[
\beta>
d(\gamma-1)
\left|
\frac12-\frac1p
\right|
\]
and proves Lorentz-space estimates at equality. The present theorem supplies the missing strong-\(L^p\) obstruction strictly below equality. It does not prove or disprove strong \(L^p\) boundedness on the critical line itself.

## Proof

It is enough first to treat
\[
2<p<\infty.
\]

Choose a small open set
\[
U\Subset
\left\{
\eta\in\mathbb R^d:
\frac12<|\eta|<2
\right\}
\]
and fixed cutoffs
\[
\chi,\chi_0\in C_c^\infty(U)
\]
such that
\[
\chi\ne0
\]
and
\[
\chi_0=1
\quad\text{on}\quad
\operatorname{supp}\chi.
\]

For large \(R\), define
\[
s_R=\log R
\]
and
\[
\lambda_R
=
\gamma s_R^{\gamma-1}.
\]
On the fixed set \(U\), write
\[
L(R\eta)^\gamma
=
s_R^\gamma
+
\lambda_R\psi_R(\eta),
\]
where
\[
\psi_R(\eta)
=
\frac{
L(R\eta)^\gamma-s_R^\gamma
}{
\gamma s_R^{\gamma-1}
}.
\]
Also write
\[
L(R\eta)^\beta
=
s_R^\beta a_R(\eta).
\]

Because
\[
L(R\eta)
=
\log R+\log|\eta|+O(R^{-2})
\]
with all derivatives uniform on \(U\), one has, for every fixed integer \(N\),
\[
a_R\longrightarrow1
\]
and
\[
\psi_R\longrightarrow\log|\eta|
\]
in
\[
C^N(U).
\]

The limiting phase is nondegenerate. Indeed,
\[
\nabla^2\log|\eta|
=
|\eta|^{-2}I
-
2|\eta|^{-4}\eta\eta^{\mathsf T}.
\]
Its tangential eigenvalues are
\[
|\eta|^{-2}
\]
and its radial eigenvalue is
\[
-|\eta|^{-2},
\]
so
\[
\det\nabla^2\log|\eta|
=
-|\eta|^{-2d}.
\]
After shrinking \(U\), if necessary, and increasing the lower threshold for \(R\), the Hessians
\[
\nabla^2\psi_R
\]
are therefore uniformly nondegenerate on \(U\).

Define a Schwartz function \(f_R\) by
\[
\widehat f_R(\eta)
=
\chi(\eta)
L(R\eta)^\beta
e^{-iL(R\eta)^\gamma}.
\]
The inverse Fourier transform is an oscillatory integral with parameter
\[
\lambda_R.
\]
Uniform stationary phase on the compact support gives
\[
\|f_R\|_{L^p}
\le
C
s_R^\beta
\lambda_R^{-d/2+d/p}.
\]
For completeness, this estimate follows by writing the inverse transform as
\[
s_R^\beta e^{-is_R^\gamma}
\int
e^{i(x\cdot\eta-\lambda_R\psi_R(\eta))}
\chi(\eta)a_R(\eta)\,d\eta.
\]
On the stationary region
\[
x\in
\lambda_R\nabla\psi_R(U)+O(1)
\]
the integral is uniformly
\[
O(\lambda_R^{-d/2}),
\]
while that region has volume
\[
O(\lambda_R^d).
\]
Outside a fixed enlargement of this region, repeated integration by parts gives rapid decay. Integrating the \(p\)-th power yields the displayed norm bound.

Now consider the scaled localized multiplier
\[
M_R(\eta)
=
\chi_0(\eta)m_{\gamma,\beta}(R\eta).
\]
On
\[
\operatorname{supp}\chi
\]
the two oscillatory factors and the two powers of \(L(R\eta)\) cancel exactly, so
\[
M_R(\eta)\widehat f_R(\eta)
=
\chi(\eta).
\]
Thus
\[
\|T_{M_R}f_R\|_{L^p}
=
\|\mathcal F^{-1}\chi\|_{L^p}
=
c_\chi>0.
\]
Consequently
\[
\|T_{M_R}\|_{L^p\to L^p}
\ge
c
s_R^{-\beta}
\lambda_R^{d(1/2-1/p)}.
\]
Since
\[
\lambda_R
=
\gamma(\log R)^{\gamma-1},
\]
this is
\[
\|T_{M_R}\|_{L^p\to L^p}
\ge
c
(\log R)^{
d(\gamma-1)(1/2-1/p)-\beta
}.
\]

Dilation conjugacy gives
\[
\|T_{M_R}\|_{L^p\to L^p}
=
\left\|
T_{\chi_0(\cdot/R)m_{\gamma,\beta}}
\right\|_{L^p\to L^p}.
\]
If the global operator
\[
T_{m_{\gamma,\beta}}
\]
were bounded on \(L^p\), then
\[
T_{\chi_0(\cdot/R)m_{\gamma,\beta}}
=
T_{\chi_0(\cdot/R)}
T_{m_{\gamma,\beta}}.
\]
The first factor has an \(L^p\) norm independent of \(R\), by dilation. Hence the localized multiplier norms would be uniformly bounded. The lower bound therefore forces
\[
\beta
\ge
d(\gamma-1)
\left(
\frac12-\frac1p
\right)
\]
when \(p>2\).

For
\[
1<p<2,
\]
boundedness of \(T_{m_{\gamma,\beta}}\) on \(L^p\) implies boundedness of its adjoint multiplier
\[
T_{\overline{m_{\gamma,\beta}}}
\]
on \(L^{p'}\), where
\[
p'>2.
\]
The same stationary-phase proof applies to the conjugated phase and gives
\[
\beta
\ge
d(\gamma-1)
\left(
\frac12-\frac1{p'}
\right)
=
d(\gamma-1)
\left(
\frac1p-\frac12
\right).
\]
This proves the stated condition for all \(p\ne2\).

## Verification

The proof uses only an explicit localized test and uniform stationary phase.

The phase normalization was checked directly:
\[
\frac{
L(R\eta)^\gamma-(\log R)^\gamma
}{
\gamma(\log R)^{\gamma-1}
}
\longrightarrow
\log|\eta|
\]
in every fixed \(C^N\) norm on compact annuli.

The limiting Hessian has one negative radial eigenvalue and \(d-1\) positive tangential eigenvalues, all of magnitude
\[
|\eta|^{-2},
\]
so there is no rank loss in any dimension.

The test function is chosen so that multiplication by the localized model symbol cancels both its oscillatory phase and its logarithmic amplitude exactly. Thus the output norm is independent of \(R\); all growth is forced into the input stationary-phase norm.

No numerical experiment, finite-frequency extrapolation, or assumption about the unresolved equality case is used.

## Relationship to prior work

Vergara's current preprint develops the logarithmic subdyadic scale
\[
\rho(R)=
\frac{R}{(\log R)^{\gamma-1}}
\]
and proves strong \(L^p\) boundedness above the critical logarithmic line. At equality it obtains Lorentz endpoint estimates. The paper explicitly distinguishes sharpness of its auxiliary geometric maximal operator from a necessity result for the full multiplier class. The theorem proved here supplies precisely that missing necessity for the paper's guiding model strictly below the critical line.

Classical oscillatory-multiplier theory supplies the proof mechanism but not this model statement. In particular, Stolyarov proves sharp large-parameter growth for homogeneous angular symbols of the form
\[
e^{i\lambda\varphi(\xi/|\xi|)}.
\]
That family has a different geometry from the radial logarithmic phase
\[
(\log|\xi|)^\gamma.
\]
The local rescaling here converts the new radial model into a large-parameter phase converging to
\[
\log|\eta|,
\]
whose full nondegenerate Hessian is what produces the exponent
\[
d\left|\frac12-\frac1p\right|.
\]

Miyachi's classical work is part of the background for strongly singular multipliers and is cited by the source. No inspected statement was found that already specializes to the logarithmic phase and gives the quantitative lower bound above.

## Limitations

The result does not settle strong \(L^p\) boundedness on the critical line
\[
\beta=
d(\gamma-1)
\left|
\frac12-\frac1p
\right|.
\]
At that line the lower bound is only constant-order. The motivating source already supplies Lorentz endpoint estimates there.

The result is for the specific radial model multiplier. A necessity theorem for the entire localized logarithmic Miyachi class would require additional structural assumptions because an abstract symbol class can contain cancellation or degeneracy absent from this model.

No best multiplicative constant in the localized lower bound is claimed.

## References

1. V. Vergara, *Logarithmic oscillatory multipliers and log-subdyadic square functions*, arXiv:2605.27746v3, 2026.
2. D. Stolyarov, *On Fourier multipliers with rapidly oscillating symbols*, arXiv:2203.04881; Journal of Fourier Analysis and Applications 30 (2024), Article 5.
3. A. Miyachi, *On some singular Fourier multipliers*, Journal of the Faculty of Science, University of Tokyo, Section IA, Mathematics 28 (1981), 267--315.
