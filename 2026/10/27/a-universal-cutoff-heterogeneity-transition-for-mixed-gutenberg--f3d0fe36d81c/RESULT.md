# A universal cutoff–heterogeneity transition for mixed Gutenberg–Richter slopes

## Finding

Suppose a complete earthquake-magnitude distribution above a reference magnitude is a nondegenerate mixture of Gutenberg–Richter exponential tails. Under a hard upper magnitude bound, the *local logarithmic slope* has either no interior turning point or exactly one strict minimum. A sharp, distribution-free-in-form cutoff test determines which happens. For finite mixtures, the large-cutoff minimum location is governed by just the two smallest exponential rates.

Formally, let \(\mu\) be a probability distribution on \((0,\infty)\), not concentrated at one rate, such that \(\int r^3\,\mu(dr)<\infty\). For \(x\ge0\), define
\[
 A(x)=\int e^{-rx}\,\mu(dr),\quad
 B(x)=\int r e^{-rx}\,\mu(dr),\quad
 C(x)=\int r^2 e^{-rx}\,\mu(dr),\quad
 E(x)=\int r^3 e^{-rx}\,\mu(dr).
\]
For a finite hard cutoff \(U>0\), the survival function conditional on a magnitude offset smaller than \(U\) is \([A(x)-A(U)]/[1-A(U)]\), for \(0\le x<U\). Its effective local slope in natural-log units is
\[
 h_U(x)=-\frac{d}{dx}\log(A(x)-A(U))
       =\frac{B(x)}{A(x)-A(U)}.
\]
Let \(m_j=\int r^j\,\mu(dr)\) and put
\[
 H=1-\frac{m_1^2}{m_2}=\frac{\operatorname{Var}_{\mu}(r)}{m_2}\in(0,1).
\]
There exists one and only one cutoff \(U_c>0\) solving \(A(U_c)=H\). Then:

1. If \(0<U\le U_c\), the function \(h_U\) is strictly increasing on \((0,U)\). At equality, only its derivative at the excluded left endpoint can vanish.
2. If \(U>U_c\), the function \(h_U\) first decreases strictly, attains exactly one strict global minimum at \(x_*(U)\in(0,U)\), and then increases strictly. The minimizer is uniquely characterized by
\[
 A(U)=A(x_*)-\frac{B(x_*)^2}{C(x_*)}.
\]
It increases strictly with \(U\), and at the critical cutoff obeys
\[
 x_*(U)=\frac{B(U_c)}{-Q'(0)}(U-U_c)+o(U-U_c),
 \qquad Q(x)=A(x)-\frac{B(x)^2}{C(x)},
\]
where \(Q'(0)=m_1(1-m_1m_3/m_2^2)<0\).
3. If \(\mu=\sum_{i=1}^k w_i\delta_{r_i}\) has distinct rates \(0<r_1<r_2<\cdots<r_k\), \(k\ge2\), and weights \(w_i>0\) summing to one, then
\[
 x_*(U)=\frac{r_1}{r_2}U+
 \frac1{r_2}\log\left(\frac{w_2(r_2-r_1)^2}{w_1r_1^2}\right)+o(1)
 \qquad (U\longrightarrow\infty).
\]
Thus the leading cutoff fraction depends on the *two slowest rate classes*, not the number or rates of faster classes.

These assertions concern the differential log-survival slope, **not** the finite-sample maximum-likelihood estimator of a fitted single Gutenberg–Richter exponent.

## Assumptions and scope

Each component tail is \(\Pr\{X>x\mid r\}=e^{-rx}\) for \(x\ge0\), where \(X\) is magnitude above a fixed completeness reference. The rate \(r\) is positive, nondegenerate under \(\mu\), and has finite third moment. The upper bound means conditioning on \(X<U\), rather than censoring, binning, or clipping recorded magnitudes. No dependence between earthquake occurrences or empirical sampling mechanism is asserted. For conventional base-ten Gutenberg–Richter exponents \(b\), set \(r=b\log 10\); the differential base-ten slope is \(h_U/\log 10\).

The rates and weights are exact model parameters. The theorem includes arbitrarily many or continuously distributed rates. The asymptotic formula in item 3 requires a *finite* rate mixture with its smallest two rates strictly positive and distinct. When \(\mu\) is a point mass, the cutoff-conditioned slope increases strictly for every \(U>0\), a separately covered boundary case.

## Proof

All four moment functions exist and are continuous on \([0,\infty)\), since the third moment is finite. Differentiation under the integral yields \(A'=-B\), \(B'=-C\), and \(C'=-E\). Since \(r>0\), \(A,B,C,E>0\). Put
\[
 Q(x)=A(x)-\frac{B(x)^2}{C(x)}.
\]
By Cauchy–Schwarz applied to \(e^{-rx/2}\) and \(r e^{-rx/2}\), \(B(x)^2<A(x)C(x)\), so \(0<Q(x)<A(x)\) for nondegenerate \(\mu\). Another Cauchy–Schwarz inequality, this time applied to \(r^{1/2}e^{-rx/2}\) and \(r^{3/2}e^{-rx/2}\), gives \(C(x)^2<B(x)E(x)\). Both inequalities are strict because the rate is not almost surely constant. Direct differentiation now yields
\[
 Q'(x)=B(x)\left(1-\frac{B(x)E(x)}{C(x)^2}\right)<0.
\]
Thus \(Q\) is strictly decreasing. Differentiating the truncated slope gives the exact sign identity
\[
 h_U'(x)=\frac{C(x)\left[A(U)-Q(x)\right]}{[A(x)-A(U)]^2}.
\]
We have \(Q(0)=1-m_1^2/m_2=H\), and at the right boundary
\[
 A(U)-Q(U)=\frac{B(U)^2}{C(U)}>0.
\]
The function \(A(U)\) decreases strictly and continuously from \(1\) to \(0\) as \(U\) goes from zero to infinity, by monotone convergence and the assumption \(r>0\). Since \(0<H<1\), there is a unique \(U_c\) with \(A(U_c)=H\). For \(U\le U_c\), \(A(U)\ge Q(0)>Q(x)\) for \(x>0\), proving strict increase of \(h_U\). For \(U>U_c\), \(A(U)<Q(0)\), while \(A(U)>Q(U)\); strict decrease of \(Q\) gives a unique \(x_*\in(0,U)\) with \(A(U)=Q(x_*)\). The displayed derivative changes from negative to positive there, making it the unique strict global minimum.

Implicit differentiation of \(Q(x_*(U))=A(U)\) gives
\[
 \frac{dx_*}{dU}=\frac{-B(U)}{Q'(x_*(U))}>0.
\]
Since \(Q'(0)<0\) and \(A'(U_c)=-B(U_c)\), the implicit-function theorem at \((x,U)=(0,U_c)\) yields the stated linear onset.

For the finite mixture, the two smallest distinct rates dominate the large-\(x\) expansion. Writing \(\varepsilon=(w_2/w_1)e^{-(r_2-r_1)x}\) and expanding the quotient defining \(Q\), while noting that faster-rate terms are smaller, gives
\[
 A(U)=w_1e^{-r_1U}(1+o(1)),\qquad
 Q(x)=\frac{w_2(r_2-r_1)^2}{r_1^2}e^{-r_2x}(1+o(1)).
\]
Because \(A(U)\to0\), the unique root \(x_*(U)\to\infty\). Equating these asymptotics at the root, taking logarithms, and rearranging yields the stated large-cutoff formula, including the constant term. These asymptotics are for each fixed finite mixture; no uniformity in coalescing or vanishing component rates is claimed.

For a point mass at \(r\), \(Q\equiv0\), so the same derivative formula is positive throughout \((0,U)\).

## Verification

For two equally weighted rate classes \(r_1=1\) and \(r_2=2\), the heterogeneity index is \(H=1/10\), and the exact threshold is
\[
 U_c=-\log\left(\frac{\sqrt{9/5}-1}{2}\right)
 =1.767142606336\ldots .
\]
The slope increases strictly for \(U=1\). For \(U=3\), the unique minimum occurs at \(x_*=1.033068418354\ldots\), where \(h_U(x_*)=1.415828609473\ldots\); the starting slope is \(h_U(0)=1.540251247652\ldots\). The two-rate asymptotic gives \(x_*(U)=U/2+o(1)\).

The included standalone `verify.py` checks these figures, exercises 3,000 randomly seeded nondegenerate finite mixtures on both sides of each computed threshold (6,000 shape tests), compares 6,000 analytical derivatives to symmetric finite differences, and checks finite-support large-cutoff asymptotics. Run with `python verify.py` using the Python standard library. The analytic argument above proves the universal theorem; random tests do not replace it.

## Relationship to prior work

The Gutenberg–Richter exponential magnitude law (Gutenberg and Richter, 1944) and the use of mixtures of different \(b\)-values are classical. Godano, Lippiello and de Arcangelis (2014, eqs. 1, 2 and 6 and Fig. 2) give differential effective slopes for untruncated mixtures, discuss the observed decrease followed by an upper-tail increase, and simulate the effect of finite magnitude cutoffs. Those observations, formulas and simulation phenomena are **not** claimed here. The distinction in this finding is the general *necessary-and-sufficient* cutoff criterion \(A(U_c)=\operatorname{Var}(r)/m_2\), the proof of exactly one possible interior minimum for every positive rate mixture with finite third moment, the rigorous movement/onset of the minimum, and its two-slowest-rate asymptotic. Their analysis does not state these universal sharp formulas. General reliability work on bathtub hazard mixtures gives broader context but typically mixes increasing-hazard and exponential components, rather than conditioning an arbitrary mixture of exponential tails on a hard upper endpoint.

The effective differential slope is not automatically equal to the Gutenberg–Richter exponent obtained by refitting a one-component statistical model to a finite, binned catalog. This limits the direct implication from the present theorem to the empirical estimator curves in the cited work.

## Limitations

No inference is made about actual earthquake magnitude mixtures, maximum earthquake sizes, catalog completeness, statistical estimation uncertainty, or seismic risk. A random catalog maximum or right-censoring mechanism differs from a fixed hard upper conditioning cutoff. The theorem does not address continuous mixing laws with infinite third rate moment; the large-cutoff two-slowest-rate formula is restricted to finite mixtures with a positive isolated second rate. The originality comparison cannot exclude all older reliability-theory equivalents, especially works not accessible in full text. No independent mathematical audit has been performed.

## References

1. B. Gutenberg and C. F. Richter, “Frequency of earthquakes in California,” *Bulletin of the Seismological Society of America* **34** (1944), 185–188.
2. C. Godano, E. Lippiello and L. de Arcangelis, “Variability of the b value in the Gutenberg–Richter distribution,” *Geophysical Journal International* **199** (2014), 1765–1771. DOI: 10.1093/gji/ggu359. First publicly published 2014-10-21.
3. J. Navarro, A. Guillamón and M. del C. Ruiz, “Generalized mixtures in reliability modelling: Applications to the construction of bathtub shaped hazard models and the study of systems,” *Applied Stochastic Models in Business and Industry* **25** (2009), 323–337. DOI: 10.1002/asmb.750.
4. H. W. Block, Y. Li, T. H. Savits and J. Wang, “Continuous mixtures with bathtub-shaped failure rates,” *Journal of Applied Probability* **45** (2008), 260–270. DOI: 10.1239/jap/1208358966.
