# Late-window identifiability conditioning for the modified Omori law

## Finding

Let the modified Omori intensity be \(\lambda(t)=K(t+c)^{-p}\), with \(K,c,p>0\). For three consecutive bins of equal width \(\Delta>0\), beginning at the known time \(T\), define expected counts

\[
B_j=\int_{T+j\Delta}^{T+(j+1)\Delta}K(t+c)^{-p}\,dt,\qquad j=0,1,2,
\]

and log-ratios \(s_0=\log(B_1/B_0)\) and \(s_1=\log(B_2/B_1)\). Set \(u=(T+c)/\Delta\). As \(u\to\infty\), uniformly when \(p\) ranges over any compact subset of \((0,\infty)\),

\[
\begin{aligned}
s_0&=-\frac p u+\frac p{u^2}-\frac{p(p+14)}{12u^3}+O(u^{-4}),\\
s_1&=-\frac p u+\frac {2p}{u^2}-\frac{p(p+50)}{12u^3}+O(u^{-4}).
\end{aligned}
\]

In particular, the Jacobian determinant satisfies

\[
\det\frac{\partial(s_0,s_1)}{\partial(p,c)}
=\frac{p\Delta^3}{(T+c)^4}+O\!\left(\frac{\Delta^4}{(T+c)^5}\right).
\]

The leading coefficient is positive for \(p>0\), so the two ratios are locally identifying for sufficiently large \(u\) when \(p\) is bounded away from zero. Their area sensitivity nevertheless decays as \((T+c)^{-4}\). This gives an explicit conditioning diagnostic for estimating the offset \(c\) from late, binned aftershock data.

## Assumptions and scope

The intensity is exactly \(K(t+c)^{-p}\) on the observation window, with \(K,c,p>0\); time is measured in one consistent unit, and \(T\) and \(\Delta\) are known. The bins are consecutive and have identical width. The asymptotic regime is \((T+c)/\Delta\to\infty\), with \(p\) in a fixed compact subset of \((0,\infty)\). The result concerns expected bin counts, not random realized counts, missed-event mechanisms, a background-rate term, overlapping secondary sequences, or a fitted point-process likelihood.

## Proof

Put \(u=(T+c)/\Delta\). After the change of variables \(t=T+\Delta x\),

\[
B_j=K\Delta^{1-p}\int_j^{j+1}(u+x)^{-p}\,dx.
\]

For \(j=0,1,2\), expand \((u+x)^{-p}=u^{-p}(1+x/u)^{-p}\) through order \(u^{-3}\) and integrate term by term over the bounded interval \([j,j+1]\). The remainder is uniform for \(p\) in a compact subset of \((0,\infty)\). Taking logarithms gives

\[
\log B_j=C-p\log u-\frac{p(j+1/2)}u
+\frac{p(12j^2+12j+p+4)}{24u^2}
-\frac{p(2j+1)(4j^2+4j+p+2)}{24u^3}+O(u^{-4}),
\]

where \(C\) is independent of \(j\). Subtracting the \(j=0\) expansion from \(j=1\), and the \(j=1\) expansion from \(j=2\), yields the two displayed log-ratio expansions.

Differentiating those expansions gives, with derivatives taken in the variables \((p,u)\),

\[
\begin{aligned}
\partial_p s_0&=-u^{-1}+u^{-2}+O(u^{-3}),&
\partial_u s_0&=p u^{-2}-2p u^{-3}+O(u^{-4}),\\
\partial_p s_1&=-u^{-1}+2u^{-2}+O(u^{-3}),&
\partial_u s_1&=p u^{-2}-4p u^{-3}+O(u^{-4}).
\end{aligned}
\]

In the determinant, the order \(u^{-3}\) terms cancel and the order \(u^{-4}\) term is \(p u^{-4}\). Since \(\partial u/\partial c=1/\Delta\), this becomes \(p/(\Delta u^4)+O(1/(\Delta u^5))\), which is the claimed expression in \(T+c\) and \(\Delta\). A nonzero determinant implies local invertibility by the inverse function theorem. No global injectivity or stochastic estimation-error bound is asserted.

## Verification

The coefficient expansions and determinant leading term were checked symbolically with the included `verify_asymptotic.py` script. The script checks the coefficients through order \(u^{-3}\) and the limit \(u^4\det\partial(s_0,s_1)/\partial(p,u)\to p\). The proof above supplies the analytic argument and states the uniformity regime; the symbolic check is a reproducibility aid, not a substitute for the proof.

## Relationship to prior work

The modified Omori law is the standard power-law decay model for aftershock activity. Ogata's 1983 paper develops maximum-likelihood estimation from event times, derives a Fisher-information matrix, and notes that estimates based on binned frequencies depend on bin width. Utsu, Ogata, and Matsu'ura's 1995 review discusses the difficulty of estimating the offset from incomplete early observations and the use of late-time slopes to estimate the decay exponent. The present claim is narrower: it gives the explicit leading Jacobian determinant for the two adjacent log-ratios formed from three equal-width expected-count bins in the late-window regime. The cited works do not state this three-bin determinant expansion. The result does not replace their point-process inference methods.

## Limitations

The determinant measures local area sensitivity of the map from \((p,c)\) to two noiseless log-ratios. It is not itself a Fisher-information determinant, a condition number, or a bound on parameter variance. It does not establish global identifiability, finite-sample estimability, robustness to bin-count noise, or performance under incomplete detection. The asymptotic statement is uniform only for \(p\) in compact subsets bounded away from zero, with known equal-width bins and a single exact modified Omori component.

## References

1. Y. Hainzl, “Dependence of the Omori-Utsu law parameters on main shock magnitude: Observations and modeling,” *Journal of Geophysical Research: Solid Earth* 113 (2008), B10309. First published 14 October 2008. DOI: 10.1029/2007JB005492.
2. Y. Ogata, “Estimation of the Parameters in the Modified Omori Formula for Aftershock Frequencies by the Maximum Likelihood Procedure,” *Journal of Physics of the Earth* 31 (1983), 115–124. DOI: 10.4294/jpe1952.31.115.
3. T. Utsu, Y. Ogata, and R. S. Matsu'ura, “The Centenary of the Omori Formula for a Decay Law of Aftershock Activity,” *Journal of Physics of the Earth* 43 (1995), 1–33. DOI: 10.4294/jpe1952.43.1.
