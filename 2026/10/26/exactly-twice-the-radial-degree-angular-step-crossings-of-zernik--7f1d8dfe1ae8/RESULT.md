# Exactly twice the radial degree: angular-step crossings of Zernike disk energy

## Finding
For a nonnegative integer \(k\), a real parameter \(\beta>-1\), and \(0\le t\le1\), define
\[
E_{k,\beta}(t)=(2k+\beta+1)\int_0^t u^\beta\left[P_k^{(0,\beta)}(2u-1)\right]^2\,du,
\]
where the Jacobi polynomials have the standard normalization \(P_k^{(\alpha,\beta)}(1)=\binom{k+\alpha}{k}\). Then, identically on \([0,1]\),
\[
\boxed{\begin{aligned}
E_{k,\beta}(t)-E_{k,\beta+1}(t)&=t^{\beta+1}(1-t)R_{k,\beta}(t),\\
R_{k,\beta}(t)&=\left[P_k^{(0,\beta+1)}(2t-1)\right]^2
 -(1-t)\left[P_{k-1}^{(1,\beta+1)}(2t-1)\right]^2.
\end{aligned}}
\]
For \(k=0\), the second term in \(R_{k,\beta}\) is defined to be zero, so \(R_{0,\beta}=1\). For every \(k\ge1\), the polynomial \(R_{k,\beta}\) has **exactly \(2k\) distinct, simple zeros in \((0,1)\)**. At each, the two normalized energy curves cross and reverse their order; there are no interior tangencies. In contrast, for \(k=0\) the difference is strictly positive on \((0,1)\).

More precisely, let \(0<z_1<\cdots<z_k<1\) be the zeros of \(P_k^{(0,\beta)}(2t-1)\), and let \(c_1,\ldots,c_{k-1}\) be its derivative zeros, interlaced as \(z_1<c_1<z_2<\cdots<c_{k-1}<z_k\). The \(2k\) crossing points lie one each in the consecutive intervals whose endpoints are the ordered list \(0,z_1,c_1,z_2,c_2,\ldots,z_k,1\). This completely locates the crossings relative to the radial nodes and turning points, for every \(\beta>-1\).

## Assumptions and scope
Write \(p(t)=P_k^{(0,\beta)}(2t-1)\), \(q(t)=P_k^{(0,\beta+1)}(2t-1)\), and \(\mu=k+\beta+1>0\). For \(k\ge1\), put \(r(t)=P_{k-1}^{(1,\beta+1)}(2t-1)\); put \(r=0\) for \(k=0\). Then \(R_{k,\beta}=q^2-(1-t)r^2\). All parameters and quantifiers are real as specified; the endpoints \(t=0,1\) are excluded from the crossing count because both energies there are automatically equal.

The normalized complex Zernike mode \(r^mP_k^{(0,m)}(2r^2-1)e^{im\theta}\) on the unit disk has squared-radius cumulative energy \(E_{k,m}(t)\). Thus, for every integer \(m\ge0\), two consecutive angular orders \(m,m+1\) at the **same radial index** \(k\) have precisely \(2k\) interior energy-order reversals. These are individual mode-wise energy fractions, not assertions that different radial modes simultaneously diagonalize every disk-compression operator. On a uniform real \(d\)-ball, the analogous parameter is \(\beta=m+d/2-1\) for \(d\ge2\), with the same conclusion. The compared modes have different total polynomial degrees.

## Proof
The shifted Jacobi equation and contiguous derivative formula give
\[
t(1-t)p''(t)+[(\beta+1)-(\beta+2)t]p'(t)+k\mu p(t)=0,
\qquad p'(t)=\mu r(t),\qquad q(t)=p(t)-(1-t)r(t).
\]
These are standard polynomial identities and remain valid for real \(\beta>-1\), including \(k=0\). Differentiate the contiguous relation and use the Jacobi equation to obtain
\[
tq'(t)=kq(t)+\mu r(t),\qquad
t(1-t)r'(t)=-kq(t)-[\mu-(\mu+1)t]r(t).
\]
For \(k=0\), these are identities with \(p=q=1\) and \(r=0\). Differentiating the explicit boundary expression, substituting these first-order equations, and collecting coefficients yields
\[
\frac{d}{dt}\left[t^{\beta+1}(1-t)(q^2-(1-t)r^2)\right]
=t^\beta\left[(2k+\beta+1)p^2-(2k+\beta+2)tq^2\right].
\]
Both sides of the proposed integrated identity vanish at \(t=0\), because \(\beta+1>0\) and all polynomials remain bounded there. Integration proves the displayed factorization for every real \(\beta>-1\). The Jacobi norm identity
\[
\int_0^1 u^\beta\left[P_k^{(0,\beta)}(2u-1)\right]^2du=\frac1{2k+\beta+1}
\]
shows that both quantities being compared are genuine cumulative fractions from zero to one.

For \(k\ge1\), the Jacobi zero theorem provides \(k\) simple interior roots \(z_j\) of \(p\), with exactly one zero \(c_j\) of \(p'\) between successive roots. Since \(p'\) and \(p\) never vanish together, at each \(z_j\) the contiguous relation gives \(q=-(1-t)r\), and hence
\[
R_{k,\beta}(z_j)=-z_j(1-z_j)r(z_j)^2<0.
\]
At every \(c_j\), instead \(r=0\) and \(q=p\ne0\), so \(R_{k,\beta}(c_j)=p(c_j)^2>0\). At \(t=1\) one has \(R_{k,\beta}(1)=q(1)^2=1\). At \(t=0\), the endpoint Jacobi values give \(q(0)=-\mu r(0)/k\), with \(r(0)\ne0\), and consequently
\[
R_{k,\beta}(0)=\left(\frac{\mu^2}{k^2}-1\right)r(0)^2>0,
\]
because \(\mu=k+\beta+1>k\). The sign sequence at the ordered points \(0,z_1,c_1,z_2,\ldots,c_{k-1},z_k,1\) therefore alternates strictly. By the intermediate-value theorem, each of the \(2k\) intervening intervals contains an interior root. Since \(q\) has degree \(k\) and \((1-t)r^2\) has degree at most \(2k-1\), \(R_{k,\beta}\) has degree exactly \(2k\). There are no other roots, and all \(2k\) displayed roots are simple. Because the outside factor is strictly positive for \(0<t<1\), all zeros are genuine sign-changing crossings of the two energies. For \(k=0\) the identity reduces to \(t^{\beta+1}(1-t)>0\) in the interior.

## Verification
The standalone file `verify_jacobi_crossings.py` independently checks the contiguous relation, the differentiated boundary identity for abstract parameter symbols, and the exact integral factorization for \(k=0,1,\ldots,6\) and five rational parameters in the admissible range. It also checks endpoint signs and the predicted interlaced root brackets numerically. Running `python verify_jacobi_crossings.py` with SymPy and SciPy reproduces `verification_output.txt`. These finite computations test the symbolic manipulation but do **not** replace the all-degree, all-real-parameter proof above.

## Relationship to prior work
Greengard and Serkh (2018) give the Zernike–Jacobi normalization, radial polynomials, orthogonality, and recurrence framework used here. In the relevant definitions, relations, inequalities, and integral sections inspected, they do not formulate an adjacent-angular-parameter difference of **cumulative squared energies** or its \(2k\) crossing classification. Driver and Jordaan (2016) examine interlacing of zeros of Jacobi polynomials with shifted parameters, but those raw polynomial-zero statements do not determine the zeros of a difference of integrated squared Jacobi modes. A different established disk-energy identity compares \(E_{k,\beta}\) with \(E_{k-1,\beta+2}\), holding total polynomial degree fixed: it has a nonnegative squared-factor difference and quadratic tangencies. That result does not imply the present sign-changing comparison at fixed radial index \(k\) with shift \(\beta\mapsto\beta+1\). The key qualitative change is **crossing rather than touching**. Mathematical priority beyond inspected indexed material remains unconfirmed.

## Limitations
The result concerns centered-disk or centered-ball **single-mode** cumulative energy and neighboring angular indices while keeping the radial polynomial degree fixed. It does not describe spectra of joint multi-mode compressions, arbitrary apertures, shifts other than one, crossing locations in elementary closed form, or quantitative noise/stability bounds. The classical Jacobi differential and zero identities are used rather than claimed as novel. The literature comparison is best knowledge, not independent proof of global priority.

## References
Greengard, P., and Serkh, K., *Zernike Polynomials: Evaluation, Quadrature, and Interpolation*, Yale Technical Report YALEU/DCS/TR-1539, dated February 20, 2018, https://engineering.yale.edu/application/files/3517/3685/9497/TR1539.pdf ; arXiv:1811.02720 (subsequent public version).

Driver, K., and Jordaan, K., *Zeros of Quasi-Orthogonal Jacobi Polynomials*, SIGMA 12 (2016), 042, https://doi.org/10.3842/SIGMA.2016.042 ; arXiv:1510.08599.

Szegő, G., *Orthogonal Polynomials*, 4th ed., American Mathematical Society, 1975 (classical Jacobi norm, differential identities, and zeros).
