# Sharp Fourier-positivity threshold for a quadratic Laplace correction on the square norm

## Finding

For \(R(x,y)=\max\{|x|,|y|\}\) in \(\mathbb R^2\), define \(f_c(x,y)=e^{-R(x,y)}(1+cR(x,y)^2)\), \(c\ge0\). The stationary kernel \(K_c(z,w)=f_c(z-w)\) is positive semidefinite for **all** finite configurations if and only if
\[
0\le c\le\frac6{13}.
\]
In the permitted range the kernel is strictly positive definite on distinct sample points. At the endpoint the Fourier density has exactly four zeros, at \((\pm\sqrt{7/5},0)\) and \((0,\pm\sqrt{7/5})\); immediately above the threshold the density is negative at these locations. The profile remains strictly decreasing in radius for \(6/13<c\le1\), so monotonicity cannot prevent loss of positive definiteness.

## Assumptions and scope

Here \(c\) is a nonnegative real parameter, and positive definiteness refers to complex-coefficient Gram matrices on arbitrary finite subsets of \(\mathbb R^2\), with no bound on their cardinality. We use the unnormalized Fourier transform \(\widehat f(\xi,\eta)=\int_{\mathbb R^2}f(x,y)e^{-i(\xi x+\eta y)}\,dx\,dy\). Multiplicative normalization does not change Fourier signs. These profiles are continuous, bounded and integrable. Strict positive definiteness is asserted only for pairwise distinct points.

## Proof

**1. Base transform and parameter differentiation.** For \(a>0\), set \(F_a=\widehat{e^{-aR}}\). The linear change \(u=x+y\), \(v=x-y\) gives \(R=(|u|+|v|)/2\) and Jacobian \(1/2\). Two elementary Laplace integrals yield
\[
F_a(\xi,\eta)=\frac{8a^2}{[a^2+(\xi-\eta)^2][a^2+(\xi+\eta)^2]}.
\]
Differentiation under the integral is justified by exponential decay, so \(\widehat{R^2e^{-R}}=\left.\partial_a^2F_a\right|_{a=1}\). Put \(X=(\xi-\eta)^2\), \(Y=(\xi+\eta)^2\), \(s=X+Y\), and \(p=XY\). Direct differentiation gives
\[
\widehat f_c(\xi,\eta)=\frac{8N_c(s,p)}{(1+X)^3(1+Y)^3},
\]
where
\[
N_c=s^2+(2-6c)ps+(1+2c)p^2+(2-24c)p+(2-2c)s+1+6c.
\]
The denominator is everywhere positive. At \(c=0\), \(N_0=(1+X)^2(1+Y)^2>0\).

**2. Endpoint polynomial certificate.** At \(c_*=6/13\),
\[
13N_{c_*}=25p^2-10ps-118p+13s^2+14s+49.
\]
Write \(x=\sqrt p\ge0\) and \(t=s-2x\ge0\), using \(X,Y\ge0\). Then
\[
13N_{c_*}=13t^2+(52x-10x^2+14)t+(x+1)^2(5x-7)^2.
\]
For \(0\le x\le3\), the coefficient \(52x-10x^2+14\) is at least \(14\), because it is concave and its endpoint values on this interval are \(14\) and \(80\). Thus the expression is nonnegative, with equality only at \(t=0\), \(x=7/5\). For \(x\ge3\), its discriminant as a quadratic in \(t\) is
\[
-48(25x^4-122x^2+49)<0.
\]
Indeed the polynomial in parentheses is positive at \(x=3\) and has positive derivative for \(x\ge3\). This proves nonnegativity everywhere, and identifies all zeros as \(X=Y=7/5\), equivalent to the four frequency points in the finding.

**3. The exact if-and-only-if statement.** For \(0\le c\le c_*\), linearity in \(c\) gives
\[
N_c=\bigl(1-c/c_*\bigr)N_0+(c/c_*)N_{c_*}\ge0.
\]
For \(c>c_*\), substitution \(X=Y=7/5\) yields
\[
N_c=-\frac{3456}{625}(13c-6)<0.
\]
As the Fourier transform is continuous and integrable, Bochner's theorem gives precisely the asserted positive-semidefiniteness criterion. For \(c\le c_*\), the Fourier density is strictly positive on a nonempty open set (in fact everywhere except at four isolated endpoint points). Every nonzero finite exponential polynomial associated with distinct spatial points is nonzero on an open frequency set, and therefore has strictly positive squared integral against this density. This proves strict positive definiteness.

**4. Monotonicity contrast.** The radial derivative is \(e^{-r}[-1+c(2r-r^2)]\). Since \(2r-r^2\le1\) for \(r\ge0\), the profile decreases strictly for \(0\le c<1\), and also strictly for \(c=1\) except at one isolated radius. Thus there are positive, decreasing, non-positive-definite profiles within the same family.

## Verification

The accompanying independent checker `CHECK.py` recomputes the exact rational Fourier formula from symbolic differentiation, verifies the endpoint sum-of-squares-style decomposition, its discriminant, and the exact negative witness at \(c=1/2\), then compares 18 direct oscillatory Laplace integrals to the closed transform at representative spectral parameters. The algebraic proof above treats all real parameters and all frequencies, unlike the finite numerical comparisons. Run `python CHECK.py` using Python with SymPy and mpmath installed.

## Relationship to prior work

Yuan Xu, *Positivity and Fourier integrals over regular hexagon*, arXiv:1508.07615v1 (first publicly posted 2015-08-30), discusses the classical general characterization of \(\ell_1\)- and, under a planar linear change of variables, \(\ell_\infty\)-radial positive-definite functions; Sections 1 and 3 address related hexagonal positive-definite radial profiles. This general representation does not state the sharp coefficient cutoff or the isolated spectral-zero geometry for the quadratic-exponential family treated here. This calculation supplies that explicit finite-parameter boundary; it does not improve or contradict the general characterization. Related work on general norm-radial positive definiteness provides context rather than an equivalent explicit parameter result.

## Limitations

The result is restricted to the two-dimensional square norm and the one-parameter family with quadratic radial correction. It does not classify arbitrary exponential polynomials, higher dimensions, or hexagonal radial profiles. Novelty is assessed against inspected accessible primary literature and indexed research records, not claimed as exhaustive across all publications. Independent scientific validation has not been performed.

## References

1. Yuan Xu, *Positivity and Fourier integrals over regular hexagon*, arXiv:1508.07615v1 (2015-08-30); https://arxiv.org/abs/1508.07615.
2. S. Bochner, *Monotone Funktionen, Stieltjes Integrale und harmonische Analyse* (1933), Fourier representation of positive-definite functions; cited and described in Xu (2015), Section 1.
