# Same-model review

## Correctness

PASS. At the critical planar exponent \(Q=4\),
\[
\widetilde V_4(R_t)
=
2\int_{R_t}(x^2+y^2)\,dx\,dy
=
\frac{16}{3}(1-t^4)
\]
by direct polynomial integration. The source's second-variation formula gives the quadratic sign on either side of \(Q=4\). Its dimension-reduction asymptotic then gives the claimed normalized endpoint limit for \(K_{t,\varepsilon}\) in every dimension. The bundled checker replays the exact polynomial identity and the first nonzero Taylor coefficient.

## Originality

PASS. The primary paper proves failure for \(q>n+2\), validity at \(q=n+2\), and identifies the rectangle second-variation threshold, but does not resolve the critical rectangle after the quadratic term vanishes. Source-text, scientific-index, and targeted literature searches found no fourth-order endpoint profile or equivalent thin-box formula.

## Value

PASS. The result identifies the critical order of the source's canonical obstruction exactly at the paper's sharp symmetric threshold. The quartic law explains how the supercritical rectangle instability meets the positive endpoint theorem and supplies a dimension-explicit benchmark for future stability work.

Same-model review: passed. Independent audit: not yet performed.

## Closest literature and limitations

The closest result is Li--Wan--Zhang itself: Lemma 4.1 gives supercritical quadratic instability, Proposition 4.3 records the second-variation threshold, and Theorem 1.5 proves the endpoint inequality using Hadwiger's moment-of-inertia inequality. None of those results states the critical fourth-order rectangle profile.

The exact formula is family-specific. In dimensions above two the stated quantitative law is a thin-box limit, not an exact finite-thickness identity, and no universal endpoint stability modulus is claimed.
