# The FEPW moment series is not absolutely convergent on its stated parameter space
## Finding
For the flexible exponential power–Weibull (FEPW) distribution, the published reliability function is
\[
S(x)
=
\exp\!\left\{
1-e^{(\tau x)^\eta}-(\kappa x)^\varphi
\right\},
\qquad
\tau,\eta,\kappa,\varphi>0.
\]
For a positive integer \(r\), the raw moment therefore exists and can be written directly as
\[
\mu_r
=
r e
\int_0^\infty
x^{r-1}
e^{-e^{(\tau x)^\eta}}
e^{-(\kappa x)^\varphi}
\,dx.
\]

The source's Theorem 1 instead gives
\[
\mu_r
=
r e
\sum_{i=0}^{\infty}
\sum_{j=0}^{\infty}
\frac{
(-1)^i i^j\tau^{j\eta}
}{
i!j!\varphi\kappa^{r+j\eta}
}
\Gamma\!\left(
\frac{r+j\eta}{\varphi}
\right)
\]
and later states that its infinite-series representations are absolutely convergent for all admissible parameter values.

That global convergence assertion is false at the completely interior parameter point
\[
r=\tau=\eta=\kappa=\varphi=1.
\]
At this point,
\[
\Gamma(1+j)=j!,
\]
so the displayed summand simplifies to
\[
a_{i,j}
=
e\frac{(-1)^i i^j}{i!}.
\]
For the fixed row
\[
i=1,
\]
one has
\[
\boxed{
a_{1,j}=-e
\qquad
\text{for every }j\ge0.
}
\]
Therefore
\[
\sum_{j=0}^{\infty}|a_{1,j}|
=
\infty,
\]
and the inner \(j\)-series does not even satisfy the necessary term condition for convergence. Consequently the published double series cannot be absolutely convergent on the stated parameter space.

This failure is not a nonexistence of the moment. At the same admissible point,
\[
\boxed{
\mu_1
=
e
\int_0^\infty
e^{-e^x-x}\,dx
=
e\,\Gamma(-1,1)
=
0.4036526376768059\ldots .
}
\]
Thus the moment is finite while the proposed global series representation fails.

There is also a useful exact replacement on the equal-shape slice
\[
\eta=\varphi=p>0.
\]
Put
\[
c=\left(\frac{\kappa}{\tau}\right)^p.
\]
After the substitutions
\[
y=(\tau x)^p,
\qquad
z=e^y,
\]
the moment becomes
\[
\boxed{
\mu_r
=
\frac{r e}{p\tau^r}
\int_1^\infty
(\log z)^{r/p-1}
z^{-c-1}e^{-z}\,dz .
}
\]
In particular, when
\[
r=p,
\]
the logarithmic power disappears and
\[
\boxed{
\mu_p
=
e\tau^{-p}
\Gamma(-c,1)
=
e\tau^{-p}
\Gamma\!\left(
-\left(\frac{\kappa}{\tau}\right)^p,1
\right).
}
\]

The issue is therefore not the existence of FEPW moments. It is the source's interchange of an infinite double Taylor expansion with integration and the resulting claim of all-parameter absolute convergence.

## Assumptions and scope
The finding uses the source's positive-parameter interior
\[
\tau,\eta,\kappa,\varphi>0
\]
and a positive integer raw-moment order \(r\). The counterexample uses only the interior point where all five quantities equal one, so it is independent of any boundary-identifiability issue.

All positive integer moments exist. Indeed,
\[
S(x)
=
e\,e^{-e^{(\tau x)^\eta}}e^{-(\kappa x)^\varphi}
\le
e\,e^{-(\kappa x)^\varphi},
\]
and the right-hand side has every positive polynomial moment.

The result rejects the global double-series representation in Eq. (3.2) and its stated absolute-convergence justification. It does not claim that every finite truncation used in the paper is numerically inaccurate for every parameter set. A finite truncation can happen to be useful locally even when the asserted global series theorem is false.

The equal-shape formula is supplied as a convergent analytic replacement on a natural two-shape subfamily. No general closed form is claimed outside that slice.

## Proof
For every nonnegative random variable and every \(r>0\),
\[
\mathbb E[X^r]
=
r\int_0^\infty x^{r-1}S(x)\,dx.
\]
Using the published FEPW reliability function gives
\[
\mu_r
=
r e
\int_0^\infty
x^{r-1}
e^{-e^{(\tau x)^\eta}}
e^{-(\kappa x)^\varphi}
\,dx.
\]

The source's Appendix expands
\[
e^{-e^{(\tau x)^\eta}}
=
\sum_{i=0}^{\infty}
\frac{(-1)^i}{i!}
e^{i(\tau x)^\eta}
=
\sum_{i=0}^{\infty}
\sum_{j=0}^{\infty}
\frac{(-1)^i i^j\tau^{j\eta}}{i!j!}
x^{j\eta}
\]
and integrates term by term against
\[
x^{r-1}e^{-(\kappa x)^\varphi}.
\]
At
\[
r=\tau=\eta=\kappa=\varphi=1,
\]
the resulting integrated coefficient is
\[
e\frac{(-1)^i i^j}{i!j!}\Gamma(1+j)
=
e\frac{(-1)^i i^j}{i!}.
\]
For \(i=1\), this is exactly \(-e\) for every \(j\). Hence the integrated double series is not absolutely summable, and the \(j\)-series for that row diverges by the term test.

The true mean remains finite. At the same parameter point,
\[
\mu_1
=
e
\int_0^\infty
e^{-e^x-x}\,dx.
\]
With
\[
z=e^x,
\qquad
dx=\frac{dz}{z},
\]
one obtains
\[
\mu_1
=
e
\int_1^\infty
z^{-2}e^{-z}\,dz
=
e\,\Gamma(-1,1).
\]

For the equal-shape slice
\[
\eta=\varphi=p,
\]
let
\[
y=(\tau x)^p.
\]
Then
\[
x^{r-1}\,dx
=
\frac{1}{p\tau^r}
y^{r/p-1}\,dy
\]
and
\[
(\kappa x)^p
=
\left(\frac{\kappa}{\tau}\right)^p y
=
cy.
\]
Therefore
\[
\mu_r
=
\frac{r e}{p\tau^r}
\int_0^\infty
y^{r/p-1}
e^{-e^y}
e^{-cy}\,dy.
\]
Finally set
\[
z=e^y.
\]
This gives
\[
\mu_r
=
\frac{r e}{p\tau^r}
\int_1^\infty
(\log z)^{r/p-1}
z^{-c-1}e^{-z}\,dz.
\]
Setting \(r=p\) yields the incomplete-gamma expression.

## Verification
The accompanying checker replays the source's Eq. (3.2) at
\[
r=\tau=\eta=\kappa=\varphi=1.
\]
It verifies symbolically through the coefficient formula that
\[
a_{1,j}=-e
\]
for every tested \(j\), which is the exact algebraic obstruction used in the proof.

It also computes equal rectangular truncations of the published double series. The values do not exhibit the stabilization claimed as a global property; by truncation level \(15\), the magnitude is already above one million at this parameter point. These finite values are illustrative only and are not used as the proof of divergence.

Independently, the checker evaluates
\[
e\int_0^\infty e^{-e^x-x}\,dx
\]
by quadrature and compares it with
\[
e\,\Gamma(-1,1).
\]
The two agree to high precision.

The exact equal-shape formula is also checked numerically at a second positive parameter point by comparing the original survival integral with the transformed integral.

## Relationship to prior work
The FEPW source proves Eq. (3.2) by expanding
\[
e^{-e^{(\tau x)^\eta}}
\]
into a double Taylor series and then integrating term by term. The same article later states that all its infinite-series representations are absolutely convergent for all admissible positive parameters and presents a truncation-stability illustration.

The interior all-one parameter point disproves that global assertion immediately: an entire integrated row consists of the nonzero constant \(-e\). Thus the source's stated convergence justification cannot validate Eq. (3.2) on the full parameter space.

The source's finite truncation illustration does not repair the theorem. A numerical demonstration at one selected parameter configuration cannot establish absolute convergence throughout a four-parameter model.

The earlier generalized extended exponential–Weibull literature supplies background for the distributional construction but does not provide the source-specific correction above. Focused searches using the exact DOI, FEPW name, moment-series language, convergence terminology, and truncation-stability aliases did not locate a published corrigendum or an equivalent correction.

## Limitations
The finding does not classify the exact parameter region, if any, on which a particular rearranged or resummed version of the source's double series is valid.

Only the equal-shape slice is given a new closed integral representation here; the general moment integral may still be evaluated directly by quadrature.

Other infinite-series formulas in the paper are not automatically declared invalid. Each would require its own interchange and convergence analysis.

A very recent unindexed correction could exist outside the sources examined.

## References
1. M. G. M. Ghazal, “Hamiltonian Monte Carlo–based inference for the flexible exponential power–Weibull distribution with applications in reliability analysis,” AIMS Mathematics 11 (2026), 11659–11705. DOI: 10.3934/math.2026481.
2. “A generalized extended exponential-Weibull distribution,” Journal of Statistical Computation and Simulation (2020). DOI: 10.1080/00207160.2019.1605062.
