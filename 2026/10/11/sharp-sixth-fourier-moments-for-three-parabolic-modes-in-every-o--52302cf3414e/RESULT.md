# Sharp sixth Fourier moments for three parabolic modes in every odd characteristic
## Finding
Let \(q=p^n\) be any odd prime power, let \(\psi\) be a nontrivial additive character of \(\mathbb F_q\), and let \(B=\{t_0,t_1,t_2\}\subset\mathbb F_q\) consist of three distinct elements. For a complex-valued function \(f\) supported on \(B\), define
\[
\mathcal E_q f(X,Y)=\frac1q\sum_{t\in\mathbb F_q} f(t)\psi(Xt+Yt^2),\qquad (X,Y)\in\mathbb F_q^2.
\]
Put \(K_p=11/3\) if \(p=3\), and \(K_p=31/9\) if \(p\ge5\). Then the following is a **sharp** sixth-moment inequality, uniform in the chosen three-point support:
\[
\boxed{\ \sum_{X,Y\in\mathbb F_q}|\mathcal E_qf(X,Y)|^6\le \frac{K_p}{q}\left(\frac1q\sum_{t\in B}|f(t)|^2\right)^3.\ }
\]
For \(p\ge5\), equality for nonzero \(f\) occurs exactly when all three coefficients have one common positive modulus; their complex phases are arbitrary. For \(p=3\), equality for nonzero \(f\) occurs exactly when all coefficients have one common positive modulus **and**
\[
f(t_0)^3=f(t_1)^3=f(t_2)^3.
\]
Modulo multiplication by one common nonzero complex scalar, there are precisely nine such phase patterns in characteristic three. In particular, when \(q=3\), every function has a three-point support constraint automatically, and the globally sharp parabola \(L^2\)-to-\(L^6\) sixth-power constant is \(11/9\).

## Assumptions and scope
The support restriction means \(f(t)=0\) whenever \(t\notin B\); values at members of \(B\) may vanish away from equality. The additive character is any nontrivial one; no assumption of prime rather than extension field is needed. All sums on the Fourier side use unnormalized counting measure. The exponent-six inequality is homogeneous and concerns exactly three available parabola frequencies, not the unrestricted extension problem for field sizes larger than three.

## Proof
Write \(z_i=f(t_i)\), \(a_i=|z_i|^2\), \(S=a_0+a_1+a_2\), \(A_3=\sum_i a_i^3\), \(B_{21}=\sum_{i\ne j}a_i^2a_j\), and \(P=a_0a_1a_2\). Let \(\gamma(t)=(t,t^2)\). The three vectors \(\gamma(t_i)\) are affinely independent over \(\mathbb F_q\): the determinant of their difference vectors equals, up to sign,
\[
(t_1-t_0)(t_2-t_0)(t_2-t_1)\ne0.
\]
Consequently, two sums of three elements of \(\{\gamma(t_0),\gamma(t_1),\gamma(t_2)\}\) coincide if and only if their three multiplicity counts are congruent componentwise modulo \(p\); the counts in either sum total three. This statement uses affine, not linear, independence: the differences of multiplicity vectors have coordinate sum zero.

Expand the cube of the unnormalized extension sum and group ordered triples by their sum in \(\mathbb F_q^2\). Orthogonality of additive characters gives the exact identity
\[
q^4\sum_{X,Y}|\mathcal E_qf(X,Y)|^6
=\sum_{w\in\mathbb F_q^2}\left|\sum_{\substack{i,j,k\in\{0,1,2\}\\\gamma(t_i)+\gamma(t_j)+\gamma(t_k)=w}}z_iz_jz_k\right|^2=:T.
\]
For \(p\ge5\), all ten nonnegative three-count vectors remain distinct modulo \(p\). Their multinomial coefficients are \(1\) for each of three cubes, \(3\) for each of six patterns of type \(2+1\), and \(6\) for the all-distinct pattern. Hence
\[
T=A_3+9B_{21}+36P.
\]
Using \(S^3=A_3+3B_{21}+6P\), direct expansion yields the exact nonnegative deficit
\[
\frac{31}{9}S^3-T
=\frac{22}{9}(A_3-3P)+\frac43(B_{21}-6P).
\]
Each bracket is nonnegative by the arithmetic-geometric mean inequality (applied respectively to the three cubes and to the six \(2+1\) monomials). Equality for nonzero \(f\) forces \(a_0=a_1=a_2>0\), and the displayed formula has no phase dependence. Substituting \(a_i=1\) verifies optimality, with \(T=93\) and \(S^3=27\).

For \(p=3\), the three count vectors \((3,0,0),(0,3,0),(0,0,3)\) coincide modulo three, while the remaining seven count vectors stay in separate classes. Their aggregate contribution at the zero-sum fiber is \(|z_0^3+z_1^3+z_2^3|^2\), giving
\[
T=|z_0^3+z_1^3+z_2^3|^2+9B_{21}+36P.
\]
Define \(U=\sum_i a_i^{3/2}\) and \(V=\sum_i a_i^2\). The following is an **exact sum of four nonnegative terms**:
\[
\begin{aligned}
\frac{11}{3}S^3-T={}&\frac83(A_3-3P)+(B_{21}-6P)\\
&+(SV-U^2)+(U^2-|z_0^3+z_1^3+z_2^3|^2).
\end{aligned}
\]
The first two are nonnegative by the same arithmetic-geometric mean inequalities; the third is Cauchy-Schwarz (\(U^2=(\sum_i\sqrt{a_i}\,a_i)^2\le (\sum_i a_i)(\sum_i a_i^2)=SV\)); the last is the triangle inequality. The first bracket forces equal positive amplitudes for nonzero equality, and the last forces the three nonzero complex cubes to have the same argument. Since their magnitudes are then equal, the cubes agree. Conversely these conditions annihilate every deficit term. For \(z_0=z_1=z_2=1\), we have \(T=99\), \(S^3=27\), so the coefficient \(11/3\) is sharp. Scaling the exact identity by \(q^{-4}\) gives the announced normalized inequality in either characteristic. For \(q=3\), \(B=\mathbb F_3\); quotienting the equality family by common nonzero complex scaling leaves two independent cubic roots of unity, hence nine projective extremizers.

## Verification
The standalone `checker.py` independently enumerates all ordered three-fold sums for selected distinct support triples in \(\mathbb F_3\), \(\mathbb F_5\), \(\mathbb F_7\), \(\mathbb F_{11}\), \(\mathbb F_9\), and \(\mathbb F_{25}\). In extension fields it uses explicit irreducible quadratic polynomials and trace-defined characters. It compares the direct nine-or-more-point Fourier sixth moment with the convolution calculation and the closed formulas and tests equality cases, completing 460 deterministic checks. Separately, polynomial expansion verifies both displayed deficit decompositions exactly. All such finite checks are corroboration; the all-field result follows from affine independence, character orthogonality, the complete multiplicity-vector argument, and the exact nonnegative identities.

## Relationship to prior work
González-Riquelme and Oliveira e Silva [1] proved a globally sharp \(L^2\)-to-\(L^6\) parabola extension theorem when the characteristic is greater than three, and explicitly exclude characteristic three. Restriction of their global inequality to a three-point frequency support gives only their larger unrestricted coefficient; it does not supply the exact sparse constant or equality conditions, and does not apply to \(q=3\). Later finite-field moment-curve endpoint results [2,3] investigate the exponent associated with all coordinates of the moment curve (for the planar curve, \(L^2\)-to-\(L^4\)), not the present sixth moment. Existing three-sparse Fourier *support-size* classifications count spectral zeros rather than computing the sharp sixth moment. The present result is the exact three-mode sixth-moment boundary in all odd characteristics, including its phase-sensitive ternary transition.

## Limitations
This theorem assumes precisely three *available* frequencies on the parabola and says nothing about whether its coefficient remains sharp for unrestricted functions when \(q>3\). It excludes characteristic two, four or more available frequencies, and extensions of the theorem to other moment exponents. Although the classification holds for arbitrary odd prime powers, an equivalent calculation might appear in work on sparse finite-group hypercontractivity or additive energies under different terminology; the novelty assessment is based on the searched and inspected sources, not on an exhaustive mathematical-literature census.

## References
1. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647v1, first publicly submitted 2024-05-26 (Theorem 1.3 and parabola discussion).
2. C. Biswas, E. Carneiro, T. C. Flock, D. Oliveira e Silva, B. Stovall, and J. Tautges, *Sharp endpoint extension inequalities for the moment curve on finite fields*, arXiv:2508.08377v1 (2025).
3. C. Biswas et al., *Sharp endpoint extension inequalities for the moment curve on finite fields II: An extremal property of the uniform distribution*, arXiv:2609.29882v1 (2026).
