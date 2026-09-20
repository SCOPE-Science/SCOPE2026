# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The proof was checked at the level of constants, endpoint cases, sign
patterns, and integrability.

The Baricz--Pogány integral representation gives the exact normalization in
(3). Pairing opposite angles converts the beta comparison term to
\(B(r+1/2,\nu+1/2)\), which simplifies by Legendre duplication to the claimed
right side of (1).

For the sign-change step, logarithmic differentiation of the positive ratio
whose difference is \(G_r\) reduces the derivative sign to
\(c\tanh(2rc)-2r(1-c^2)\). Its derivative is strictly positive, so there is one
critical point; the endpoint behavior then forces exactly one interior zero of
\(G_r\), with positive sign near zero and negative sign near one.

The limiting integral \(F(r)\) is finite despite the factor \((1-c^2)^{-1}\),
because \(G_r(1)=0\) with finite derivative. A matched-cutoff calculation gives
\(F(r)=\psi(r+1/2)-\log r+\operatorname{Ei}(-4r)\). Differentiation yields a
Laplace transform with kernel
\(t/(2\sinh(t/2))-\mathbf 1_{(0,4)}(t)\), negative before 4 and positive after
4. The standard one-sign-change weighting argument proves that \(F'\) has at
most one zero. Since \(F'(0+)=\pi^2/2-4>0\) and \(F\) tends to zero at both
ends, \(F(r)>0\) for all positive \(r\). A second one-sign-change weighting,
now with the decreasing multiplier \((1-c^2)^{\nu+1/2}\), then proves strict
positivity for every \(\nu>-1/2\).

The two boundary cases were checked separately. For \(r=0\), both sides equal
\(2^{-\nu}/\Gamma(\nu+1)\). For \(\nu=-1/2\), the elementary half-order Bessel
formulas make both sides identically \(\sqrt{2/\pi}\). Numerical spot checks over
widely separated positive \(r\) and orders above \(-1/2\) were consistent with
the exact proof but are not used as evidence in place of it.

## Originality

**PASS, to the best of our knowledge.** Baricz and Pogány (2014) explicitly end
their paper with the problem of finding a generalization of their real-variable
Kanter inequality for \(\Phi_\nu\). The primary paper was inspected in full,
including its existing lower/upper bounds and order-convexity results, so the
new inequality is not being inferred from an abstract or snippet.

Searches covered the exact paper title and DOI; the open-problem wording; Kanter
inequalities together with \(\Phi_\nu\); the gamma quotient
\(\Gamma(2r+1)/(\Gamma(r+1)\Gamma(r+\nu+1))\); the equivalent
\({}_1F_1(a;2a+1;-4r)\) formulation; and combinations involving modified Bessel
sums, digamma functions, and exponential integrals.

Veestraeten (2026) is the most directly relevant recent source located. It
revisits \(\Phi_\nu\), expresses the generalized Bessel sum through a single
confluent hypergeometric function, and cites Baricz--Pogány for its properties.
The inspected article does not state the gamma lower bound proved here or a
full-real-order resolution of the 2014 open problem. Mattner--Roos (2007) treats
the original \(\nu=0\) Kanter concentration bound.

No specific inaccessible paper was identified as likely to contain the same
result. Residual risk remains for a differently phrased special-function
inequality, an unindexed source, or unpublished work.

## Value

**PASS.** The result supplies a closed-form, asymptotically sharp extension of a
named Kanter inequality to the entire real parameter range \(\nu\ge-1/2\),
recovers the classical case exactly, and has a clean equivalent confluent-
hypergeometric form. The proof also gives a reusable mechanism: a one-sign-change
kernel plus a decreasing order weight transfers positivity from a boundary
functional to a continuum of parameters.

## Limitations

- The right side is asymptotically sharp, but finite-\(r\) pointwise optimality is not established.
- No probabilistic concentration interpretation is claimed for arbitrary real order \(\nu\).
- Search cannot exclude substantially differently phrased, poorly indexed, or unpublished prior coverage.
- Independent audit has not been performed.
