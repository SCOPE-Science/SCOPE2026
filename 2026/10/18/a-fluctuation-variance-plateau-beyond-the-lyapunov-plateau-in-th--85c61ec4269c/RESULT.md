# A fluctuation-variance plateau beyond the Lyapunov plateau in the VGH map

## Finding

For the Varley–Gradwell–Hassell piecewise-affine family below, the stationary branch-occupation process has the **same positive asymptotic variance** at every parameter in the open interval \(2<\beta<3\):
\[
\lim_{n\to\infty}\frac1n\operatorname{Var}_{\mu_\beta}\!\left(\sum_{j=0}^{n-1}\mathbf1_{\{T_\beta^jx>0\}}\right)=\frac{2}{27}.
\]
Consequently the variance per step of the finite-time logarithmic derivative sum is \(2(\log2)^2/27\). Despite this exact plateau, the one-step autocovariance is not constant:
\[
\operatorname{Cov}_{\mu_\beta}(H,H\circ T_\beta)=\frac{\beta-4}{18}.
\]
The previously known constancy of the *mean* exponent is not asserted to be new.

## Assumptions and scope

For each real \(\beta\) satisfying \(2<\beta<3\), let \(I_\beta=[-\beta,\beta]\) and define
\[
T_\beta(x)=\begin{cases}x+2,&x\leq0,\\\beta-2x,&x>0.\end{cases}
\]
Let \(\mu_\beta\) be the invariant probability with density \(\rho_\beta\) from Botella-Soler–Oteo–Ros–Glendinning [2, Appendix A, equation (A.9)]:
\[
\rho_\beta(x)=\begin{cases}
1/18,&-\beta<x<\beta-4,\\
1/6,&\beta-4<x<2-\beta,\\
2/9,&2-\beta<x<\beta-2,\\
1/3,&\beta-2<x<2,\\
1/9,&2<x<\beta.
\end{cases}
\]
Boundary values of both branches and density are immaterial for \(\mu_\beta\). Set \(H(x)=\mathbf1_{(0,\beta]}(x)\) and \(h=H-2/3\). As already known, \(\int H\,d\mu_\beta=2/3\). Here all variances are taken with respect to \(\mu_\beta\), *not* an arbitrary invariant measure.

## Proof

**Step 1: finite transfer calculation.** The Lebesgue-density Perron–Frobenius operator is, almost everywhere on \(I_\beta\),
\[
(\mathcal L f)(x)=\frac12f\!\left(\frac{\beta-x}{2}\right)+\mathbf1_{(2-\beta,2)}(x)f(x-2).
\]
Use the seven intervals with consecutive endpoints
\[
-\beta,\quad\beta-4,\quad2-\beta,\quad0,\quad\beta-2,\quad4-\beta,\quad2,\quad\beta.
\]
They are strictly ordered for every \(2<\beta<3\). On these intervals in order the known density takes the values
\[
\boldsymbol r=(1/18,1/6,2/9,2/9,1/3,1/3,1/9).
\]
Define an auxiliary signed density \(w_\beta\) by its seven respective values
\[
\boldsymbol w=\frac1{81}\big(3-\beta,-3\beta,-4\beta,18-4\beta,18-6\beta,18-6\beta,12-2\beta\big).
\]
Direct inverse-image evaluation of \(\mathcal L\) gives, for any seven-piece vector \(\boldsymbol a\) whose fifth and sixth entries agree,
\[
\mathcal A(\boldsymbol a)=\big(a_7/2,a_5/2,a_1+a_5/2,a_1+a_5/2,a_2+a_5/2,a_3+a_4/2,a_4/2\big).
\]
Substitution verifies \(\mathcal A(\boldsymbol r)=\boldsymbol r\) and the **Poisson identity**
\[
\boxed{\quad w_\beta-\mathcal Lw_\beta=\rho_\beta h.\quad}
\]
These are identities of piecewise-constant functions for every parameter in the specified open interval; their exact-arithmetic verification is supplied separately. Direct integration over the same seven intervals yields
\[
\int\rho_\beta\,dx=1,\qquad\int w_\beta\,dx=0,\qquad
\int h w_\beta\,dx=\frac4{27},\qquad
\int h^2\,d\mu_\beta=\frac29.
\]

**Step 2: variance limit without an unproved mixing assumption.** Because \(\rho_\beta\ge1/18\) on its support, the bounded function \(g=w_\beta/\rho_\beta\) is well defined almost everywhere. Let \(P f=\rho_\beta^{-1}\mathcal L(\rho_\beta f)\) be the transfer operator in \(L^2(\mu_\beta)\). The displayed identity says \((I-P)g=h\). Its adjoint relation gives \(P(f\circ T_\beta)=f\). Put \(m=g-(Pg)\circ T_\beta\); then \(Pm=0\), so \(m,m\circ T_\beta,m\circ T_\beta^2,\ldots\) are pairwise orthogonal, centered, and bounded. The exact coboundary decomposition is
\[
\sum_{j=0}^{n-1}h\circ T_\beta^j
=\sum_{j=0}^{n-1}m\circ T_\beta^j+(Pg)\circ T_\beta^n-Pg.
\]
The boundary term is uniformly bounded. Therefore by the Cauchy–Schwarz inequality its contribution to variance divided by \(n\) tends to zero, while the orthogonal sum has variance \(n\int m^2\,d\mu_\beta\). The transfer adjunction and \(g-Pg=h\) imply
\[
\int m^2\,d\mu_\beta
=\int g^2\,d\mu_\beta-\int(Pg)^2\,d\mu_\beta
=2\int h g\,d\mu_\beta-\int h^2\,d\mu_\beta
=2\cdot\frac4{27}-\frac29=\frac2{27}.
\]
Since \(h\) differs from \(H\) by a constant, the asserted branch-count variance follows. For \(\mu_\beta\)-almost every orbit, \(\log|T_\beta'|=(\log2)H\), proving the logarithmic derivative statement.

**Step 3: short-lag nonconstancy.** The event \(H(x)=H(T_\beta x)=1\) is the interval \(0<x<\beta/2\). For \(2<\beta<3\), we have \(\beta-2<\beta/2<2\), whence
\[
\mu_\beta(0<x<\beta/2)=\frac29(\beta-2)+\frac13\left(\frac\beta2-\beta+2\right)=\frac{\beta+4}{18}.
\]
Subtracting \((2/3)^2\) gives \((\beta-4)/18\), a strictly parameter-dependent covariance.

## Verification

The included `verification/check.py` uses exact symbolic arithmetic to verify the transfer matrix, normalized density, seven-piece Poisson identity, all integrals used in Step 2, and the lag-one covariance formula as identities in \(\beta\). Run `python verification/check.py` with SymPy installed. It returns `VERIFY_OK`. The proof does not infer a parameter-uniform identity from a finite sample of parameters. The hypotheses \(2<\beta<3\) are essential to the displayed ordering of partition endpoints. No central-limit theorem, variance outside this interval, uniqueness of invariant measure, or result for other stationary states is claimed.

## Relationship to prior work

Botella-Soler, Oteo, Ros and Glendinning [2, Appendix A] had already derived this precise invariant density and the branch probability \(2/3\); their paper also proved Lyapunov and entropy plateaus. The added information here is the all-lag asymptotic **fluctuation variance** and its exact contrast with a varying one-step covariance, obtained from an explicit signed-density Poisson solution. The earlier map study [1] concerns bifurcations of its power-law origin; the 2013 journal paper [3] treats the plateau phenomenon. Generic transfer-operator or martingale-coboundary methods explain how a Poisson solution can give a variance but do not, without the new explicit solution, specify \(2/27\) for this family.

## Limitations

The variance limit is established only for the specified absolutely continuous stationary measure and the open parameter interval \(2<\beta<3\). The displayed Poisson solution is not a central-limit or large-deviation theorem. Bibliographic overlap cannot be excluded exhaustively, especially through unpublished formulations of correlation statistics. 

## References

[1] V. Botella-Soler, J. A. Oteo, J. Ros, *Dynamics of a map with power-law tail* (2008), arXiv:0812.4551; first posted 2008-12-24. https://arxiv.org/abs/0812.4551

[2] V. Botella-Soler, J. A. Oteo, J. Ros, P. Glendinning, *Families of piecewise linear maps with constant Lyapunov exponent* (2012), arXiv:1205.5360; first posted 2012-05-24. Open preprint: https://eprints.maths.manchester.ac.uk/1835/1/botella.pdf.pdf

[3] V. Botella-Soler, J. A. Oteo, J. Ros, P. Glendinning, *Lyapunov exponent and topological entropy plateaus in piecewise linear maps*, Journal of Physics A 46 (2013) 125101, doi:10.1088/1751-8113/46/12/125101.
