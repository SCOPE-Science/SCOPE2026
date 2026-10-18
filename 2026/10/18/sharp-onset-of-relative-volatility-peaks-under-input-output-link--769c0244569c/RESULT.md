# Sharp onset of relative-volatility peaks under input-output link changes

## Finding

**Theorem (one-link rigidity and a sharp two-link, three-sector reversal).** Let \(n\ge1\), let \(A(t)\) be a nonnegative \(n\times n\) technical-coefficient matrix with \(\rho(A(t))<1\) on an interval containing \(t=0\), and let the random final-demand vector \(D\) have fixed componentwise positive mean \(\mu\) and positive-semidefinite covariance matrix \(\Sigma\). Define gross output \(Y(t)=\mathbf 1^{\mathsf T}(I-A(t))^{-1}D\) and squared relative volatility \(V(t)=\operatorname{Var}(Y(t))/\mathbb E[Y(t)]^2\).

(i) If \(A(t)=A(0)+t e_i e_j^{\mathsf T}\) and \(t\ge0\) is restricted to the productive interval, \(V\) cannot have a strict interior local maximum. It is constant, strictly monotone, or decreases to a unique strict minimum and then increases; restriction to the productive interval can truncate the monotone pieces. This conclusion permits arbitrary covariance, including correlated and negatively correlated sectoral demand shocks.

(ii) If \(n\le2\) and \(A(t)=A(0)+tB\) for any fixed matrix \(B\), subject to nonnegativity and productivity on the interval, \(V\) likewise has no strict interior local maximum.

(iii) Both restrictions are sharp. For three sectors, strengthening exactly two links together, with
\[
A(t)=t\begin{pmatrix}0&1&0\\0&0&1\\0&0&0\end{pmatrix},\qquad
D=\operatorname{diag}(1,1/10,1/10000)Z,
\]
where the three \(Z_i\) are independent, strictly positive random variables with mean and variance both one (for example, exponential variables), produces at least **two distinct strict interior local minima** and **one strict interior local maximum** of \(V(t)\) on \(t>0\). Every \(A(t)\) in this construction is productive. Thus three sectors and two simultaneously changing technical coefficients are the smallest dimension and support size allowing an interior relative-volatility peak among affine nonnegative technological changes.

## Assumptions and scope

The Leontief convention is \(x=A x+D\): \(A_{ij}\) is the amount of input from sector \(i\) required per unit of output in sector \(j\). Gross output is the sum of all sectoral outputs, not value added, welfare or GDP. Random final demand has finite second moments and a fixed, strictly positive mean vector; the distribution does not vary with technological intensity. Productivity \(\rho(A)<1\) guarantees the nonnegative Leontief inverse \(L=(I-A)^{-1}\). A strict interior local maximum is a point with strictly smaller values at all sufficiently close distinct parameter values. A constant risk function is therefore not counted as having a peak. No symmetry, independence, or nonsingularity is imposed on \(\Sigma\) for parts (i) and (ii).

## Proof

Write \(L_0=(I-A(0))^{-1}\) and \(w(t)^{\mathsf T}=\mathbf1^{\mathsf T}(I-A(t))^{-1}\). Then \(\mathbb E[Y(t)]=w(t)^{\mathsf T}\mu>0\) and
\[
V(t)=\frac{w(t)^{\mathsf T}\Sigma w(t)}{(w(t)^{\mathsf T}\mu)^2}.
\]
For (i), the Sherman–Morrison identity gives
\[
(I-A(0)-t e_i e_j^{\mathsf T})^{-1}
=L_0+\frac{t}{1-t\ell}L_0e_i e_j^{\mathsf T}L_0,\qquad
\ell=e_j^{\mathsf T}L_0e_i\ge0.
\]
Every productive \(t\ge0\) satisfies \(1-t\ell>0\): if \(\ell>0\), this follows from the matrix determinant lemma and the nonsingular \(M\)-matrix property, or directly from the Neumann series; if \(\ell=0\), the denominator is one. Set \(c=\mathbf1^{\mathsf T}L_0e_i>0\), \(q=L_0^{\mathsf T}e_j\ge0\), and \(u(t)=ct/(1-t\ell)\). Then \(w(t)=w_0+u(t)q\), with \(u\) strictly increasing, \(q\ne0\) and \(\mu^{\mathsf T}q>0\).

Normalize \(a=w_0/(\mu^{\mathsf T}w_0)\), \(b=q/(\mu^{\mathsf T}q)\), and
\[
\lambda(t)=\frac{u(t)\,\mu^{\mathsf T}q}{\mu^{\mathsf T}w_0+u(t)\,\mu^{\mathsf T}q}.
\]
The normalized multiplier vector is exactly \((1-\lambda)a+\lambda b\), and \(\lambda(t)\) increases strictly. Therefore
\[
V(t)=a^{\mathsf T}\Sigma a+2\lambda(t)(b-a)^{\mathsf T}\Sigma a
+\lambda(t)^2(b-a)^{\mathsf T}\Sigma(b-a).
\]
The last coefficient is nonnegative because \(\Sigma\) is positive semidefinite. Hence \(V\) is a convex quadratic in a strictly increasing parameter; it admits no strict interior maximum and at most one strict minimum. If \(h=(b-a)^{\mathsf T}\Sigma(b-a)>0\), its formal minimizer is exactly \(\lambda_*=- (b-a)^{\mathsf T}\Sigma a/h\); the observed minimum exists precisely when \(\lambda_*\) lies in the interval traced by \(\lambda(t)\). If \(h=0\), positive semidefiniteness forces \(\Sigma(b-a)=0\), so \(V\) is constant. This also supplies a complete trichotomy (including endpoint-truncated cases).

For (ii), the adjugate of any \(2\times2\) affine pencil \(I-A(0)-tB\) has entries affine in \(t\). Thus there are fixed vectors \(r,s\in\mathbb R^2\) such that \(w(t)=(r+ts)/\det(I-A(t))\). The common determinant cancels when computing \(V\). On the productive interval containing zero, \(\alpha=\mu^{\mathsf T}r>0\) and \(\alpha+t\beta=\mu^{\mathsf T}(r+ts)>0\), with \(\beta=\mu^{\mathsf T}s\). The normalized multiplier is
\[
\frac{r+ts}{\alpha+t\beta}=\frac r\alpha+
\frac{t}{\alpha+t\beta}\left(s-\frac\beta\alpha r\right).
\]
The scalar \(t/(\alpha+t\beta)\) has strictly positive derivative \(\alpha/(\alpha+t\beta)^2\). Since a positive-semidefinite quadratic form restricted to an affine line is convex, no strict interior maximum is possible. For \(n=1\), \(V=\operatorname{Var}(D_1)/\mathbb E[D_1]^2\) is independent of \(A\).

For (iii), \(A(t)^3=0\), so \((I-A(t))^{-1}=I+A(t)+A(t)^2\). The independent unit-mean, unit-variance shocks have aggregate weights
\[
w_1(t)=1,\quad w_2(t)=\frac{1+t}{10},\quad
w_3(t)=\frac{1+t+t^2}{10000},\qquad
V(t)=\frac{w_1(t)^2+w_2(t)^2+w_3(t)^2}{[w_1(t)+w_2(t)+w_3(t)]^2}.
\]
Direct rational evaluation (reproducible using the enclosed script) gives
\[
\begin{aligned}
V(0)&=33666667/40340667,\\
V(10)&=221012321/445674321,\\
V(100)&=10403030201/14665452201,\\
V(1000)&=2004104002001/4048148024001,\\
V(10000)&=10102020401020001/12104620661042001.
\end{aligned}
\]
Exact cross-multiplication establishes
\[ V(0)>V(10)<V(100)>V(1000)<V(10000). \]
Continuity forces an interior minimum of \(V\) on each of \([0,100]\) and \([100,10000]\), and an interior maximum on \([10,1000]\). The three are distinct because they respectively lie in \((0,100)\), \((10,1000)\) above both valley values, and \((100,10000)\); more precisely one may choose the first minimum in \((0,100)\), the maximum between minima by compactness, then the second minimum in \((100,10000)\). As \(V\) is a nonconstant rational function with a strictly positive denominator, each interior extremum can be chosen isolated and hence strict. This proves (iii) and the simultaneous sharpness of (i) and (ii).

## Verification

Run \(\texttt{python3 verify.py}\) in a directory containing the enclosed standalone Python script. It uses Python's exact rational arithmetic to reconstruct the three-sector Leontief inverse by Cramer's rule at five parameter values, check the four required strict inequalities, and test determinant cancellation for a separate two-sector affine pencil. The universal prohibitions in (i) and (ii) follow from the analytic proof, not from finite sampling.

## Relationship to prior work

Classic input–output sensitivity theory gives the Sherman–Morrison coefficient-update identity and its extension to several changing entries. The 2011/2012 study by Acemoglu and coauthors shows that shock-exposure concentration in economic networks drives aggregate fluctuations. Those established results motivate this distinct fixed-final-demand, mean-normalized gross-output statistic. The theorem here characterizes the global shape of its response to link changes and establishes the sharp simultaneous two-link, three-sector onset of a strict risk peak; neither the Leontief inverse nor the exposure-variance identity is claimed as new. The prior literature studied includes the coefficient-change work of Sonis and Hewings and the later input–output network risk discussion by Kelly and coauthors.

## Limitations

This is a static, linear, demand-driven Leontief model, not a general-equilibrium or nonlinear substitution model. Gross output double-counts intermediate transactions and should not be identified with GDP, welfare or net value added. Coefficient changes are not cost-constrained or required to keep column sums below one; the three-sector witness exploits an acyclic technology, which is productive for all \(t\ge0\) even at large coefficients. No assertion is made that such coefficient values are empirically typical. The positive-semidefinite covariance assumption is automatic for genuine finite-variance random vectors; correlations may otherwise be arbitrary. The result does not claim that two changing entries always create peaks or that exactly three extrema occur in the witness. The closest older coefficient-change article was not verified in full text, so independent literature confirmation remains desirable.

## References
- Acemoglu, Carvalho, Ozdaglar and Tahbaz-Salehi, The Network Origins of Aggregate Fluctuations, MIT Working Paper 11-23 (2011), and Econometrica 80 (2012), 1977–2016. https://economics.mit.edu/sites/default/files/publications/The%20Network%20Origins%20of%20Aggregate%20Fluctuations.pdf
- Sonis and Hewings, Coefficient Change in Input–Output Models: Theory and Applications, Economic Systems Research 4 (1992), 143–158. https://doi.org/10.1080/09535319200000013
- Sonis and Hewings, Matrix Sensitivity, Error Analysis and Internal/External Multiregional Multipliers, Hitotsubashi Journal of Economics 36 (1995), 61–70. https://www.jstor.org/stable/43295983
- Kelly, Tyler and Crawford-Brown, Exploring Vulnerability and Interdependency of UK Infrastructure Using Key-Linkages Analysis, Networks and Spatial Economics 16 (2016), 865–892; first online 2015-09-02. https://doi.org/10.1007/s11067-015-9302-x
- Acemoglu, Akcigit and Kerr, Networks and the Macroeconomy: An Empirical Exploration, Harvard Business School Working Paper 16-006 (2015). https://dash.harvard.edu/entities/publication/73120379-0ab7-6bd4-e053-0100007fdf3b
