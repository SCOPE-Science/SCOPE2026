# Sharp aridity-balance envelope for spatial calibration bias in Fu's water-balance law

## Finding

Suppose every subcatchment obeys one and the same Fu–Budyko exponent \(w>1\). Pooling their water balances and fitting one exponent to the pooled measurements produces an exponent \(\widehat w\) satisfying \(1<\widehat w\le w\); equality with \(w\) holds **exactly** when the precipitation-to-potential-evaporation ratio is identical in every subcatchment. This is a model aggregation effect even when no local exponent varies.

The more informative quantitative result is a sharp general local law. Let \(n\ge2\), \(a_i>0\), \(\sum_i a_i=1\), and real \(u_i,v_i\) satisfy \(\sum_i u_i=\sum_i v_i=0\). Fix total precipitation \(P>0\) and total potential evaporation \(D>0\). For sufficiently small real \(\epsilon\), set
\[
P_i=P(a_i+\epsilon u_i),\qquad D_i=D(a_i+\epsilon v_i).
\]
Define \(p=P^w/(P^w+D^w)\), the binary entropy \(H(p)=-p\log p-(1-p)\log(1-p)\), and the contrast energy
\[
\mathcal A=\sum_{i=1}^{n}\frac{(u_i-v_i)^2}{a_i}.
\]
Then the unique pooled fitted exponent has the expansion
\[
\boxed{\displaystyle
w-\widehat w(\epsilon)=
\frac{w^2(w-1)}{2}\,\frac{p(1-p)}{H(p)}\,\mathcal A\epsilon^2
+O(\epsilon^3).}
\]
Moreover, the second-order coefficient satisfies the **sharp universal aridity envelope**
\[
\boxed{\displaystyle
\lim_{\epsilon\to0}\frac{w-\widehat w(\epsilon)}{\epsilon^2}
\le\frac{w^2(w-1)}{8\log2}\,\mathcal A.}
\]
When \(\mathcal A>0\), equality holds if and only if \(P=D\) (pooled aridity index one). Thus the largest second-order spurious exponent reduction, at fixed normalized spatial contrast, occurs at *balanced water and potential-energy supply*, not at an extremely wet or dry limit.

A complementary nonperturbative statement holds for two subcatchments: with fixed \(P,D,w\), fixed potential-evaporation share \(0<b<1\), and precipitation share \(0<a<1\), the fitted exponent \(\widehat w(a)\) is strictly increasing for \(0<a<b\), equals \(w\) at \(a=b\), and strictly decreases for \(b<a<1\).

## Assumptions and scope

All \(P_i,D_i\) are strictly positive water-equivalent **volumes** over disjoint regions (not unweighted regional depths). Total precipitation and potential evaporation are \(P=\sum_iP_i\) and \(D=\sum_iD_i\). The Fu–Budyko mean water-balance response is assumed exact within each region with one common finite \(w>1\). Write
\[
F_w(P,D)=(P^w+D^w)^{1/w},\qquad
Q_w(P,D)=F_w(P,D)-D.
\]
Here \(Q_w\) represents annual or multiyear runoff volume under negligible mean water-storage change; actual evaporation is \(P-Q_w\). The fitted pooled exponent is defined by the exact single-catchment calibration equation
\[
Q_{\widehat w}(P,D)=\sum_iQ_w(P_i,D_i).
\]
No claim is made for varying exponents among subcatchments, for physically interacting reservoirs or lateral water transfers, or for actual observations with error.

## Proof

**1. Existence, direction and equality for pooled calibration.** For \(x,y>0\), \(F_\theta(x,y)\) is the ordinary \(\ell^\theta\)-norm. The Minkowski inequality gives
\[
F_w(P,D)\le\sum_i F_w(P_i,D_i)<P+D.
\]
Strictness at the right holds because each subcatchment has both inputs positive and \(w>1\). Equality at the left, for \(w>1\), occurs precisely when the positive vectors \((P_i,D_i)\) are proportional, equivalently all ratios \(P_i/D_i\) agree. Differentiating the exponent at any fixed \(P,D>0\), with \(p_\theta=P^\theta/(P^\theta+D^\theta)\), yields
\[
\frac{\partial}{\partial\theta}\log F_\theta(P,D)
=-\frac{H(p_\theta)}{\theta^2}<0.
\]
Thus \(F_\theta(P,D)\) is strictly decreasing in \(\theta\), from \(P+D\) at \(\theta=1\). The intermediate value theorem gives exactly one \(\widehat w\in(1,w]\) solving the pooling equation. Strict inequality \(\widehat w<w\) is equivalent to differing regional aridities.

**2. Quadratic spatial mismatch.** The Hessian of \(F_w\) at positive \((P,D)\) is
\[
\nabla^2F_w=(w-1)(P^w+D^w)^{1/w-2}
\begin{pmatrix}
P^{w-2}D^w&-P^{w-1}D^{w-1}\\
-P^{w-1}D^{w-1}&P^wD^{w-2}
\end{pmatrix}.
\]
Homogeneity of degree one implies \(\nabla^2F_w(a_iP,a_iD)=a_i^{-1}\nabla^2F_w(P,D)\). Taylor expansion, together with \(\sum_i u_i=\sum_i v_i=0\), eliminates the first-order term and gives
\[
\sum_iF_w(P_i,D_i)-F_w(P,D)
=\frac{w-1}{2}\frac{P^wD^w}{(P^w+D^w)^{2-1/w}}
\mathcal A\epsilon^2+O(\epsilon^3).
\]
The derivative identity from step 1 gives
\[
-\partial_wF_w(P,D)=\frac{F_w(P,D)H(p)}{w^2}.
\]
Applying the implicit-function theorem to \(F_{\widehat w}(P,D)=\sum_iF_w(P_i,D_i)\) and substituting the preceding expansion gives exactly the claimed exponent-deficit coefficient. For \(\mathcal A=0\), the shares satisfy \(u_i=v_i\) for all \(i\), and proportionality holds for every permitted \(\epsilon\), so \(\widehat w(\epsilon)=w\) identically.

**3. Sharp climate envelope.** Let \(z=2p-1\), so \(-1<z<1\) and \(4p(1-p)=1-z^2\). The convergent binary-entropy series reads
\[
H(p)=\log2-\sum_{m=1}^{\infty}\frac{z^{2m}}{2m(2m-1)},
\qquad\sum_{m=1}^{\infty}\frac1{2m(2m-1)}=\log2.
\]
Consequently,
\[
H(p)-(1-z^2)\log2
=\sum_{m=2}^{\infty}\frac{z^2-z^{2m}}{2m(2m-1)}\ge0.
\]
For \(0<p<1\), equality occurs only when \(z=0\). Therefore
\[
\frac{p(1-p)}{H(p)}\le\frac1{4\log2},
\]
with equality exactly at \(p=1/2\), equivalent to \(P=D\). Inserting this sharp ratio into the quadratic coefficient proves the envelope and its attainment condition.

**4. Global two-region monotonicity.** Let \(G(a)=F_w(aP,bD)+F_w((1-a)P,(1-b)D)\). The partial derivative \(\partial_PF_w(P,D)=[1+(D/P)^w]^{-(w-1)/w}\) is strictly increasing in \(P/D\). Hence
\[
\operatorname{sgn}G'(a)=\operatorname{sgn}\left(
\frac a b-\frac{1-a}{1-b}\right)=\operatorname{sgn}(a-b).
\]
The fitted \(\widehat w(a)\) decreases as \(G(a)\) increases because \(F_\theta(P,D)\) decreases strictly in its exponent. This proves the claimed strict rise–fall pattern and the unique maximum \(w\) at \(a=b\).

## Verification

A standalone Python 3 program (`verify.py`) reconstructs the fitted exponent by scalar bisection, tests the exact equality regime, checks pooled strictness on 6,000 seeded random positive configurations, checks the local quadratic coefficient at multiple positive perturbations, tests the two-region monotonicity, and samples the sharp entropy inequality. Finite numerical checks are not used to infer the universal assertions; those follow from the four analytic steps above.

An exact irrational example uses \(w=2\), \(P=D=1\), \((P_1,P_2)=(3/5,2/5)\) and \((D_1,D_2)=(1/2,1/2)\):
\[
\widehat w=\frac{\log2}{\log[(\sqrt{61}+\sqrt{41})/10]}
\approx1.971418157338<2.
\]
For the perturbation \((P_1,P_2)=(1/2+\epsilon,1/2-\epsilon)\), \((D_1,D_2)=(1/2,1/2)\), the universal sharp coefficient is \(2/\log2\approx2.885390081778\).

## Relationship to prior work

Fu's 1981 model and its public 2004 analysis by Zhang and coauthors establish the functional form and water-balance interpretation; neither is claimed as new. The general \(\ell^p\)-norm Minkowski inequality immediately explains the nonnegative aggregation bias and is explicitly prior mathematics. Greve and coauthors (2015) study probabilistic *between-catchment* exponent variation; Abatzoglou and Ficklin (2017) study spatial determinants of calibrated exponents; Koppa and Gebremichael (2017) study errors in remotely sensed water-balance inputs; and Greve, Burek and Wada (2020) calibrate distributions of grid-level exponents. These address related scale and parameter issues. The additional specific result here is the exact common-exponent spatial mixing expansion, its weighted normalized mismatch energy, the sharp binary-entropy envelope, and the location of its aridity maximum.

## Limitations

This is an analytic statement about an idealized algebraic annual-balance model, not field identification of physical catchment properties. Real subcatchments need not share one exponent, precipitation and potential evaporation may be correlated with storage and vegetation, runoff may transfer between delineated regions, and volume aggregation needs area weighting. The local asymptotic coefficient describes small composition differences and does not assert that maximum bias occurs at aridity one for arbitrarily large differences. The sign inequality is a direct classical Minkowski consequence; historical priority for the specialized sharp calibration envelope has not been independently established. The original Fu (1981) work has only a year-verified bibliographic record in the inspected material, while the earliest day-resolved primary source used here is Zhang et al., first published 2004-02-05.

## References

- Fu, B. P. (1981), *On the calculation of the evaporation from land surface*, Scientia Atmospherica Sinica 5(1), 23–31. Original model; publication day not verified. Bibliographic record: https://cir.nii.ac.jp/crid/1371694364625911058
- Zhang, L. et al. (2004), *A rational function approach for estimating mean annual evapotranspiration*, Water Resources Research 40, W02502, first published 2004-02-05. https://doi.org/10.1029/2003WR002710
- Greve, P. et al. (2015), *Introducing a probabilistic Budyko framework*, Geophysical Research Letters 42, 2261–2269. https://doi.org/10.1002/2015GL063449
- Abatzoglou, J. T. and Ficklin, D. L. (2017), *Climatic and physiographic controls of spatial variability in surface water balance over the contiguous United States using the Budyko relationship*, Water Resources Research 53, 7630–7643. https://doi.org/10.1002/2017WR020843
- Koppa, A. and Gebremichael, M. (2017), *A Framework for Validation of Remotely Sensed Precipitation and Evapotranspiration Based on the Budyko Hypothesis*, Water Resources Research 53, 8487–8499. https://doi.org/10.1002/2017WR020593
- Greve, P., Burek, P. and Wada, Y. (2020), *Using the Budyko Framework for Calibrating a Global Hydrological Model*, Water Resources Research 56, e2019WR026280. https://doi.org/10.1029/2019WR026280
