# A rational-order counterexample to a Bessel complete-monotonicity problem

## Result

Let
\[
F_\nu(x)=x^{\nu+1}e^{-x}I_\nu(x),\qquad x>0,
\]
where \(I_\nu\) is the modified Bessel function of the first kind. At the rational order
\[
\nu=-\frac{15}{16},
\]
one has
\[
F_\nu''(2)<0.
\]
Consequently \(F_{-15/16}\) is not completely monotone, hence not strictly completely monotone (SCM), on \((0,\infty)\).

This gives a negative answer to part (b) of the open problem posed by Baricz (2010), which asked whether \(x^{\nu+1}e^{-x}I_\nu(x)\) is SCM for every \(\nu\in(-1,-1/2]\).

Moreover, since \(\nu\mapsto F_\nu''(2)\) is continuous for \(\nu>-1\), the failure persists for every \(\nu\) in some open interval containing \(-15/16\).

## Proof

Write
\[
a=2\nu+1,\qquad r(x)=\frac{I_{\nu+1}(x)}{I_\nu(x)}.
\]
The standard derivative and recurrence identities give
\[
\frac{F_\nu'(x)}{F_\nu(x)}=\frac{a}{x}-1+r(x),
\qquad
r'(x)=1-\frac{a}{x}r(x)-r(x)^2.
\]
Therefore
\[
\frac{F_\nu''(x)}{F_\nu(x)}
=
2-2r(x)-\frac{2a}{x}+\frac{a\,r(x)}{x}
+\frac{a(a-1)}{x^2}.
\]

Set \(\nu=-15/16\), so \(a=-7/8\), and then set \(x=2\). This reduces to
\[
\frac{F_\nu''(2)}{F_\nu(2)}
=
\frac{841}{256}-\frac{39}{16}r(2).
\]
Thus it is enough to show
\[
r(2)>\frac{841}{624}.
\]

At \(x=2\), the defining positive series for \(I_\nu\) yields
\[
I_{-15/16}(2)=\frac{A}{\Gamma(1/16)},\qquad
I_{1/16}(2)=\frac{16B}{\Gamma(1/16)},
\]
where
\[
A=\sum_{k=0}^{\infty}\frac{1}{k!(1/16)_k},
\qquad
B=\sum_{k=0}^{\infty}\frac{1}{k!(17/16)_k}.
\]
Hence \(r(2)=16B/A\).

Use the first five terms:
\[
A_4=\sum_{k=0}^{4}\frac{1}{k!(1/16)_k}
=\frac{2131411}{82467},
\]
and
\[
B_4=\sum_{k=0}^{4}\frac{1}{k!(17/16)_k}
=\frac{356659}{162435}.
\]
For the summands \(a_k=1/[k!(1/16)_k]\),
\[
\frac{a_{k+1}}{a_k}
=\frac{16}{(k+1)(16k+1)}
\le \frac{16}{325}\qquad(k\ge4).
\]
Since
\[
a_5=\frac{131072}{26801775},
\]
the remaining positive tail satisfies
\[
A<A_4+\frac{a_5}{1-16/325}
=\frac{658737071}{25482303}.
\]
Also \(B>B_4\). Therefore
\[
r(2)>
16\frac{B_4}{658737071/25482303}
=
\frac{58189629168}{42817909615}.
\]
An exact cross multiplication gives
\[
\frac{58189629168}{42817909615}>
\frac{841}{624}.
\]
It follows that
\[
\frac{F_\nu''(2)}{F_\nu(2)}
<
\frac{841}{256}
-\frac{39}{16}
\frac{58189629168}{42817909615}
=
-\frac{23112816509}{843183450880}<0.
\]
Since \(F_\nu(2)>0\), this proves \(F_\nu''(2)<0\). Complete monotonicity would require \(F_\nu''(x)\ge0\) for every \(x>0\), so it fails.

Finally, the positive hypergeometric series for \(I_\nu(2)\) and its order dependence show continuity of the displayed second derivative in \(\nu\) on compact subintervals of \((-1,\infty)\). Hence the strict negative sign persists for orders in a neighborhood of \(-15/16\).

## Context and literature

Baricz (2010) explicitly posed three SCM questions at the end of Section 2. Part (b) asks whether \(x^{\nu+1}e^{-x}I_\nu(x)\) is SCM for all \(\nu\in(-1,-1/2]\). The same paper records positive monotonicity results outside this range and motivates the unresolved interval.

Hornik and Grün (2013) systematically study lower and upper Amos-type bounds for the ratio \(I_{\nu+1}/I_\nu\) for \(\nu\ge-1\). Those ratio bounds are closely related to the present derivative calculation, but the paper does not state the complete-monotonicity classification above.

Salazar (2026) develops Riccati reductions and exact certificates for several modified-Bessel-ratio problems, including a different complete-monotonicity transfer problem of Baricz and other questions. Its stated resolved problems do not include the Section 2(b) question treated here. The finite rational-tail certificate used here is therefore not claimed as a new general methodology.

To the best of our knowledge, searches by the exact function, the 2010 problem statement, modified-Bessel complete monotonicity, relevant ratio formulations, and later citation chains did not locate an earlier counterexample to part (b).

## Reproducibility

`artifacts/verify_counterexample.py` checks the rational tail bound and the resulting strict negative upper bound for \(F''(2)/F(2)\) using exact rational arithmetic only.

## Limitations

- The result disproves the universal statement but does not classify all \(\nu\in(-1,-1/2]\).
- It gives a nonempty open set of failing orders around \(-15/16\), but no optimal endpoints for that set.
- Parts (a) and (c) of Baricz's 2010 open problem are not addressed.
- A differently phrased or non-indexed prior counterexample could still exist.

## References

1. Á. Baricz, *Bounds for modified Bessel functions of the first and second kinds*, Proc. Edinburgh Math. Soc. 53 (2010), 575–599. DOI: 10.1017/S0013091508001016.
2. K. Hornik and B. Grün, *Amos-type bounds for modified Bessel function ratios*, J. Math. Anal. Appl. 408 (2013), 91–101. DOI: 10.1016/j.jmaa.2013.05.070.
3. D. S. P. Salazar, *Riccati Reductions for Modified Bessel Ratios: Bernstein Positivity, Exact Certificates, and Transfer Obstructions*, arXiv:2607.05538 (2026).

**Same-model review: passed. Independent audit: not yet performed.**
