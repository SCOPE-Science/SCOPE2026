# The sixth moment resolves a twofold stationary-kurtosis ambiguity for resetting Brownian driving

## Finding
For the Poisson-reset Brownian driving model below, the stationary position's second, fourth and sixth moments determine the *dimensionless memory ratio* \(\beta=r/\mu\) and the *diffusion-to-reset scale* \(s=D/r\) uniquely, for every \(\beta,s>0\). The variance and kurtosis alone do not always identify these quantities. In the ambiguous range, the two candidate ratios have identical standardized fourth moments but strictly ordered standardized sixth moments: the larger ratio always has the larger standardized sixth moment.

Precisely, define \(m_{2j}=\mathbb E[X^{2j}]\), \(K=m_4/(3m_2^2)\) and \(H=m_6/(15m_2^3)\). Then
\[
K(\beta)=\frac{\beta^2+19\beta+12}{(\beta+2)(\beta+3)},\qquad
H(\beta)=\frac{P(\beta)}{(\beta+2)^2(\beta+3)^2(\beta+4)(\beta+5)},
\]
where
\[
P(b)=b^6+61b^5+2393b^4+12443b^3+22614b^2+16344b+4320.
\]
The maximum \(K_{\max}\) is attained uniquely at \(\beta_*=3(\sqrt{22}-1)/7\). For each \(2<K<K_{\max}\), precisely two positive values give that kurtosis; they are exchanged by \(\psi(b)=3(9-b)/(7b+3)\). If \(0<b<\beta_*\), then \(H(b)<H(\psi(b))\). At every other observed kurtosis within the model's range, there is just one candidate. Thus \((K,H)\) is globally injective, and the scale follows from \(s=m_2(1+\beta)/(2\beta^2)\).

## Assumptions and scope
Let \(W\) be standard Brownian motion, and let an independent Poisson clock of rate \(r>0\) reset \(Y\) to zero. Between clock times, \(dY_t=\sqrt{2D}\,dW_t\) with \(D>0\). The position obeys
\[
 dX_t=(-\mu X_t+rY_t)\,dt,\qquad \mu>0,
\]
with no direct thermal forcing or position resets. We work in the unique stationary finite-moment law of \((X,Y)\). All moment quantities are *population* moments, not finite-data estimators. Parameters \(\mu,r,D\) are positive and unrestricted. The model is symmetric about zero, so odd stationary moments vanish.

The source paper gives the forward moments. In terms of \(\beta=r/\mu\), \(s=D/r\), they are
\[
 m_2=\frac{2s\beta^2}{1+\beta},\quad
 m_4=\frac{12s^2\beta^4(\beta^2+19\beta+12)}{(1+\beta)^2(\beta+2)(\beta+3)},
\]
\[
 m_6=\frac{120s^3\beta^6P(\beta)}{(1+\beta)^3(\beta+2)^2(\beta+3)^2(\beta+4)(\beta+5)}.
\]
The question here is which unknown parameters can be inferred *inversely* from these moments.

## Proof
**1. Forward moment reconstruction.** The stationary polynomial generator for \(f(x,y)=x^py^q\) gives
\[
(\mu p+r\mathbf1_{q>0})M_{p,q}
=rpM_{p-1,q+1}+Dq(q-1)M_{p,q-2},
\]
where \(M_{p,q}=\mathbb E[X^pY^q]\), \(M_{0,0}=1\), and terms with negative exponents are zero. The recursion first determines \(M_{0,q}\), then increasing \(p\) at fixed total degree; this independently recovers the three displayed forward moments. Division by powers of \(m_2\) gives exactly \(K,H\) above.

**2. The entire twofold ambiguity.** Set \(p(b)=b^2+19b+12\) and \(q(b)=(b+2)(b+3)\). The exact polynomial identity
\[
p(b)q(c)-p(c)q(b)=-2(b-c)(7bc+3b+3c-27)
\]
shows that distinct \(b,c>0\) with \(K(b)=K(c)\) must satisfy \(c=\psi(b)=3(9-b)/(7b+3)\). Such a second positive candidate can exist only for \(0<b<9\). Furthermore,
\[
K'(b)=-\frac{2(7b^2+6b-27)}{(b+2)^2(b+3)^2},\qquad
K(b)-2=\frac{b(9-b)}{(b+2)(b+3)}.
\]
Hence \(K\) increases from \(2\) to its unique maximum at \(\beta_*\), then decreases toward \(1\); the two-branch range is exactly \(2<K<K_{\max}\). At \(K=2\), the second root \(b=0\) is outside the strictly positive domain.

**3. Sixth-moment separation.** Direct reduction of the two rational functions yields the exact identity
\[
H(b)-H(\psi(b))=-\frac{2(7b^2+6b-27)R(b)}{11(b+2)^2(b+3)^2(b+4)(b+5)(16b+21)(25b+39)},
\]
where
\[
R(b)=357b^6+2030b^5-436986b^4-2517506b^3-4533183b^2-2618136b-449280.
\]
For \(0<b<9\), the elementary inequalities \(b^6<81b^4\) and \(b^5<9b^4\) show that the two positive terms are less than \(47187b^4\), strictly below \(436986b^4\). Therefore \(R(b)<0\) throughout this interval. The denominator is strictly positive. On the lower \(K\)-branch \(0<b<\beta_*\), the factor \(7b^2+6b-27\) is negative, so \(H(b)-H(\psi(b))<0\). At \(b=\beta_*\), the two candidates coincide. On the upper branch the sign reverses. Thus no two *distinct* positive ratios can share both \(K\) and \(H\).

**4. Sharp identification boundary.** Every \(\beta>0\) gives \(m_2>0\), and \(s=m_2(1+\beta)/(2\beta^2)\) is therefore uniquely recovered. Conversely, given any variance \(v>0\) and any \(2<K<K_{\max}\), choose its two positive branches \(b,c\), with scales \(s_b=v(1+b)/(2b^2)\) and \(s_c=v(1+c)/(2c^2)\). They have identical \(m_2\) and \(m_4\) but different \(m_6\). Therefore the first two positive even moments are genuinely insufficient. Finally, scaling \((\mu,r,D)\mapsto(\lambda\mu,\lambda r,\lambda D)\), \(\lambda>0\), leaves \((\beta,s)\) and hence every stationary moment and the stationary law unchanged. The theorem does *not* recover absolute physical rates or diffusivity separately.

## Verification
The companion `checker.py` reconstructs moments directly from the stationary polynomial-generator recursion, independently matches the published closed forms, verifies the two rational-factorization identities *symbolically*, and checks the strict coefficient bound for \(R\). It also constructs exact rational pairs with equal \(K\) and unequal \(H\). The exact proof above holds for every positive parameter, independently of the finite tests.

## Relationship to prior work
Guéneau, Majumdar and Schehr derive the harmonic reset-Brownian model, stationary scaling, and the formulas for \(m_2,m_4,m_6\) in their §4.2 and Appendix E (equations E.2–E.4). Those formulas and the Kesten recursion are **prior results**, not part of the originality claim. The evaluated contribution is the exact two-branch inversion, the strictly separating sixth moment, and the identification/nonidentification distinction.

Di Bello and collaborators study inverse extraction of *Poisson shot-noise kick* statistics in a harmonic bath (§3.2), a different forcing mechanism: independent instantaneous displacement kicks rather than continuous Brownian forcing reset to zero. Olsen studies restarting the *particle position* from a distribution, again distinct from resetting only its Brownian driving signal. None of the examined statements supplies the specific branch involution or sixth-moment separation for the present model.

## Limitations
No finite-sample accuracy, stability, or experimental noise guarantee follows from ideal moment identification. Inversion near the maximum of \(K\) is intrinsically ill-conditioned if one uses kurtosis alone, despite exact uniqueness after the sixth moment is included. Unrestricted non-Poisson resetting, added thermal noise, and nonharmonic potentials are not treated. A general published inverse theorem could subsume this special model; publication priority is not independently certified. The absolute time scale remains unidentifiable from stationary laws.

## References
1. M. Guéneau, S. N. Majumdar and G. Schehr, *Active particle in a harmonic trap driven by a resetting noise: an approach via Kesten variables*, J. Phys. A 56 (2023), 475002; arXiv:2306.09453 (first posted 2023-06-15), §4.2 and Appendix E, equations E.2–E.4. https://arxiv.org/abs/2306.09453
2. C. Di Bello, R. Majumdar, R. Marathe, R. Metzler and É. Roldán, *Brownian particle in a Poisson-shot-noise active bath: exact statistics, effective temperature, and inference*, arXiv:2309.13424 (first posted 2023-09-23), §3.2. https://arxiv.org/abs/2309.13424
3. K. Stølevik Olsen, *Steady-state moments under resetting to a distribution*, Phys. Rev. E 108 (2023), 044120. https://doi.org/10.1103/PhysRevE.108.044120
