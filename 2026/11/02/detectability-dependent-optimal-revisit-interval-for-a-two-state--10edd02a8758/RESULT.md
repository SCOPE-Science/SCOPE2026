# Detectability-dependent optimal revisit interval for a two-state ecological occupancy process

## Finding
Consider independent habitat sites whose occupied/unoccupied status follows a stationary continuous-time two-state Markov chain. At each site two instantaneous detection attempts are made, separated by a selectable interval \(\Delta>0\), with independently calibrated probability \(p\in(0,1]\) of detecting the species conditional on occupancy and no false detections. Both the stationary occupancy probability \(q\) and the total status-switching rate \(\gamma\) are unknown. At the nominal design point \(q=1/2\), the **per-site efficient Fisher information for \(\gamma\) after treating \(q\) as a nuisance** is exactly
\[
\mathcal I_{\gamma\mid q}(\Delta;p)=
\frac{p^2\Delta^2 e^{-2\gamma\Delta}}{
(2-p)^2+4(1-p)^2e^{-\gamma\Delta}-p^2e^{-2\gamma\Delta}}.
\]
For every \(p\in(0,1]\), it has a unique global maximum at \(\Delta_*(p)=x_*(p)/\gamma\), where \(x_*(p)\) is strictly decreasing as detection improves. The sharp universal range is
\[
0.796812130020020\ldots=x_*(1)\le x_*(p)<x_0=1.138090854066615\ldots,
\]
with \(x_*(p)\to x_0\) as \(p\downarrow0\). Here \(x_*(1)\) is the unique positive root of \(x=1-e^{-2x}\), and \(x_0\) the unique positive root of \(x=2(1+e^{-x})/(2+e^{-x})\). The optimal gap equals one switching time \(1/\gamma\) **if and only if**
\[
p=p_c=\frac{\sqrt{2e}}{1+\sqrt{2e}}=0.699847881249118\ldots.
\]
It exceeds \(1/\gamma\) for \(p<p_c\) and falls below \(1/\gamma\) for \(p>p_c\). The formula is a local information-design result, not a claim that two binary observations at one site permit reliable finite-sample estimation.

## Assumptions and scope
For every \(q\in(0,1)\) and \(\gamma>0\), the unobserved habitat state \(Z_t\in\{0,1\}\) has transition rates \(0\to1\) at \(q\gamma\) and \(1\to0\) at \((1-q)\gamma\). It starts in its stationary law with \(\Pr(Z_t=1)=q\) and correlation \(\operatorname{Corr}(Z_0,Z_\Delta)=r=e^{-\gamma\Delta}\). Measurements are \(Y_0=Z_0B_0\) and \(Y_\Delta=Z_\Delta B_\Delta\), with independent Bernoulli-\(p\) detectors \(B_0,B_\Delta\), independent of the state process. Detector probability \(p\) is known, common across visits and sites; no false positives, behavioral effects or temporal heterogeneity are allowed. The design fixes two observations per independently replicated site and optimizes their separation without time-horizon or travel-cost constraints. The Fisher information is evaluated at the nominal **true** value \(q=1/2\), but \(q\) is **not held known in inference**: its nuisance score is projected out. The optimization concerns the local asymptotic variance in a growing number of independent sites. No assertion is made for the optimum at other nominal occupancies or when \(p\) must also be estimated.

## Proof
Put \(a=pq\) and \(c=p^2q(1-q)r\). The labeled two-visit observation probabilities, in order \((11,10,01,00)\), are
\[
(a^2+c,\quad a(1-a)-c,\quad a(1-a)-c,\quad (1-a)^2+c).
\]
They are positive for \(0<p\le1\), \(0<q<1\) and \(0<r<1\). Differentiate all four cells with respect to \(q,r\), form the multinomial information matrix \(J_{ij}=\sum_y(\partial_iP_y)(\partial_jP_y)/P_y\), and eliminate nuisance \(q\) by its Schur complement \(J_{rr}-J_{rq}^2/J_{qq}\). Substitution at \(q=1/2\), where \(\partial_q c=0\), reduces **exactly** to
\[
J_{rr\mid q}=\frac{p^2}{D(p,r)},\qquad
D(p,r)=(2-p)^2+4(1-p)^2r-p^2r^2.
\]
Because \(\partial_\gamma r=-\Delta r\), the chain rule gives the displayed efficient information. The Schur reduction was also reconstructed using rational arithmetic in `check.py`.

Write \(x=\gamma\Delta\), \(r=e^{-x}\), \(A=(2-p)^2\), \(B=4(1-p)^2\), \(C=p^2\). Maximizing information is equivalent to maximizing
\[
f_p(x)=\frac{x^2e^{-2x}}{A+Br-Cr^2},\qquad x>0,
\]
since the omitted factor \(p^2/\gamma^2\) is independent of \(x\). Its logarithmic derivative has the **opposite sign** of
\[
g_p(x)=x(2A+Br)-2(A+Br-Cr^2),
\]
whose derivative is \(g_p'(x)=2A+Br(3-x)-4Cr^2\).

For \(0<x\le\log2\), \(g_p(x)\) is strictly increasing in \(p\in[0,1]\), because the coefficients multiplying the derivatives of \(A,B,C\) have respectively signs negative, negative and positive. Thus \(g_p(x)\le g_1(x)=2(x-1+e^{-2x})<0\): the last strict inequality follows from strict convexity of \(x-1+e^{-2x}\), its zero at \(x=0\), and \(\log2-3/4<0\) at \(x=\log2\). For \(\log2\le x\le3\), \(r\le1/2\) and \(Br(3-x)\ge0\), so
\[
g_p'(x)\ge2(2-p)^2-p^2\ge1>0.
\]
For \(x\ge3\), \((x-3)e^{-x}\le e^{-4}\), hence \(g_p'(x)\ge 2-4e^{-4}-4e^{-6}>0\). Since \(g_p(x)\to\infty\) as \(x\to\infty\), exactly one positive root exists, located beyond \(\log2\). The information tends to zero at both endpoints \(x\downarrow0\) and \(x\to\infty\); its sole stationary point is therefore its unique global maximum.

For strict monotonicity with respect to \(p\), let \(S_p(x)=\partial_x\log f_p(x)=2/x-2+rD_r/D\). Direct differentiation gives
\[
\partial_pS_p(x)=\frac{8r}{D^2}H(p,r),\quad
H(p,r)=p^2(r^2+r-1)+p(3-2r-r^2)-2.
\]
At each maximizer \(x>\log2\), we have \(0<r<1/2\). For such \(r\), \(\partial_pH>0\) on \(0\le p\le1\), while \(H(1,r)=-r<0\); consequently \(\partial_pS_p<0\). The derivative \(\partial_xS_p=-g_p'/(xD)<0\) at the root. The implicit function theorem therefore yields \(x_*'(p)<0\) on \((0,1)\). Continuity gives the limiting design equation at \(p\downarrow0\), and the perfect-detector equation at \(p=1\). These have unique positive roots by the already proved uniqueness argument. Finally, substituting \(x=1\) into \(g_p\) yields \(g_p(1)=-4(1-p)^2/e+2p^2/e^2\); its unique zero in \((0,1)\) is the displayed \(p_c\), and the signs give the exact crossing directions.

## Verification
Run `python3 check.py` using the Python standard library. The checker independently forms all four multinomial-cell derivatives at 460 rational pairs \((p,r)\), computes the nuisance Schur complement without using the closed-form answer as an intermediate expression, and checks its equality to the proposed rational formula. It then locates roots by bisection, checks the three reference constants, compares neighboring objective values, and checks monotonicity and threshold signs over 100 positive detector probabilities. The checked output is `VERIFICATION_OK exact_assertions=2300 numerical_assertions=863 perfect=0.796812130020 low_detection_limit=1.138090854067 crossing=0.699847881249`. The analytic argument above, not finite tests or numerical root finding, establishes uniqueness, monotonicity and global optimality for every admissible detector probability. One independent site provides little data; the Fisher result is interpreted per site and asymptotically across many independently sampled sites.

## Relationship to prior work
MacKenzie et al. (2003) supply the dynamic occupancy and imperfect-detection framework, and Guillera-Arroita et al. (2010) study Fisher-based design in **single-season closed** occupancy with focus on numbers of replicate surveys, not time separation for a changing occupancy process. Fukaya and Royle (2013) and Hines et al. (2014) include observation error or correlated replicated states without the two-visit, nuisance-adjusted lag optimization established here. Michel's publicly available 2018 manuscript proves the perfect-observation symmetric Markov optimum, which is **exactly the \(p=1\) endpoint above**; that endpoint is not claimed new. Mehtälä, Auranen and Kulathinal (2015) optimize observation times for multistate Markov models with observed states and a stationary initial law; accessible bibliographic materials did not settle whether their full general analysis implies the *imperfect-detection* formula. The attempted institutional full-text retrieval was unavailable, leaving a priority risk. The proposed contribution is the explicit all-\(p\) nuisance-adjusted information law, strict detection-monotonicity, the limiting interval and the exact crossing \(p_c\). A general Markov scheduling theorem or a prior specialized hidden-Markov design calculation could subsume this result; no independence or publication priority is certified.

## Limitations
The nominal occupation probability is \(1/2\); this is a local design, not a minimax statement over unknown prevalence. Known detector probability is essential: estimating \(p\) from exactly two visits introduces another nuisance parameter and can destroy full identifiability. The nonzero information and finite optimal gap require \(p>0\). The formal \(p\downarrow0\) design location has vanishing absolute information and must not be interpreted as successful inference at \(p=0\). The sample size per site is two, with many independent sites for usual information interpretations; it is not the asymptotic design for one long temporally dependent record. Finite-window, calendar, cost and travel constraints, misclassification with false positives, non-Markov turnover, covariates, and site heterogeneity are not treated. The present review is not independent validation, and historical priority remains provisional.

## References
- MacKenzie, D. I., Nichols, J. D., Hines, J. E., Knutson, M. G., and Franklin, A. B. (2003). *Estimating site occupancy, colonization, and local extinction when a species is detected imperfectly*. Ecology 84, 2200–2207. https://doi.org/10.1890/02-3090 (first published 2003-08-01).
- MacKenzie, D. I., and Royle, J. A. (2005). *Designing occupancy studies: General advice and allocating survey effort*. Journal of Applied Ecology 42, 1105–1114. https://doi.org/10.1111/j.1365-2664.2005.01098.x.
- Guillera-Arroita, G., Ridout, M. S., and Morgan, B. J. T. (2010). *Design of occupancy studies with imperfect detection*. Methods in Ecology and Evolution 1, 131–139. https://doi.org/10.1111/j.2041-210X.2010.00017.x.
- Fukaya, K., and Royle, J. A. (2013). *Markov models for community dynamics allowing for observation error*. Ecology 94, 2670–2677. https://doi.org/10.1890/12-1540.1.
- Hines, J. E., Nichols, J. D., and Collazo, J. A. (2014). *Multiseason occupancy models for correlated replicate surveys*. Methods in Ecology and Evolution 5, 583–591. https://doi.org/10.1111/2041-210X.12186.
- Mehtälä, J., Auranen, K., and Kulathinal, S. (2015). *Optimal observation times for multistate Markov models—applications to pneumococcal colonization studies*. Applied Statistics 64, 451–468. https://doi.org/10.1111/rssc.12084.
- Michel, J. (2018). *Optimal adaptive sampling for a symmetric two-state continuous time Markov chain*, publicly available preprint dated 2018-02-20. https://bpb-us-w2.wpmucdn.com/u.osu.edu/dist/6/56774/files/2017/12/optimal_sampling_design_ctmc9-1nt190d.pdf (journal article 2020, https://doi.org/10.1080/07474938.2019.1701808).
