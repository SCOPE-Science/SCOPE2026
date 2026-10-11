# Exact \(J_{X,p}(t)\) profiles and extremizer rigidity of the Euclidean--sup plane
## Finding
For every \(\lambda>0\), let \(Z_\lambda=(\mathbb R^2,N_\lambda)\), where
\[
N_\lambda(u,v)=\bigl(u^2+v^2+\lambda\max\{u^2,v^2\}\bigr)^{1/2}.
\]
For all \(t>0\) and all \(1\le p\le2\), the Zuo--Cui generalized smoothness coefficient is exactly
\[
J_{Z_\lambda,p}(t):=\sup_{x,y\in S_{Z_\lambda}}
\left(\frac{N_\lambda(x+ty)^p+N_\lambda(x-ty)^p}{2}\right)^{1/p}
=\sqrt{1+t^2+\frac{2\lambda t}{\lambda+2}}.
\]
The maximizing unit pairs are precisely the orbit, under signed-coordinate permutations, exchange of the two vectors, and independent vector sign changes, of
\[
x=\frac{(1,1)}{\sqrt{\lambda+2}},\qquad
 y=\frac{(1,-1)}{\sqrt{\lambda+2}}.
\]
This simultaneously gives the complete classical Lindenstrauss smoothness profile
\[
\rho_{Z_\lambda}(t)=\sqrt{1+t^2+\frac{2\lambda t}{\lambda+2}}-1
\]
and the Pythagorean modulus
\[
E(t,Z_\lambda)=2\left(1+t^2+\frac{2\lambda t}{\lambda+2}\right).
\]
In particular, \(\lim_{t\downarrow0}\rho_{Z_\lambda}(t)/t=\lambda/(\lambda+2)>0\). Up to a scalar renorming, \(Z_\lambda\) is the quadratic two-dimensional Lorentz sequence space \(d^{(2)}(\omega,2)\) with \(\omega=1/(1+\lambda)\); the displayed profile becomes \(\sqrt{1+t^2+2(1-\omega)t/(1+\omega)}\).

## Assumptions and scope
All scalars are real. Throughout, \(\lambda>0\), \(t>0\), and \(1\le p\le2\). Write
\[
N_\lambda(z)^2=\|z\|_2^2+\lambda\|z\|_\infty^2,
\qquad
S_\lambda=\{z:N_\lambda(z)=1\}.
\]
The coefficient \(J_{X,p}(t)\) is the two-vector \(p\)-power mean of the norms of the sum and difference, maximized over unit vectors. The classical modulus of smoothness is \(\rho_X(t)=J_{X,1}(t)-1\); the Pythagorean modulus is \(E(t,X)=2J_{X,2}(t)^2\).

The parameter \(t=0\) and the Hilbert endpoint \(\lambda=0\) are excluded from the rigidity statement because their maximizing sets are larger. The profile extends to those endpoints by continuity, but the claimed unique orbit does not.

## Proof
Define the positive quadratic forms
\[
Q_1(z)=(1+\lambda)z_1^2+z_2^2,
\qquad Q_2(z)=z_1^2+(1+\lambda)z_2^2.
\]
Then
\[
N_\lambda(z)^2=\max\{Q_1(z),Q_2(z)\},
\qquad Q_1(z)+Q_2(z)=(\lambda+2)\|z\|_2^2.
\]
For every \(z\),
\[
N_\lambda(z)^2\ge\frac{Q_1(z)+Q_2(z)}2
=\frac{\lambda+2}{2}\|z\|_2^2.
\]
Since \(\lambda>0\), equality holds exactly when \(|z_1|=|z_2|\). In particular, for every \(z\in S_\lambda\),
\[
\|z\|_2^2\le\frac2{\lambda+2}.
\]

Take arbitrary \(x,y\in S_\lambda\) and set \(u=x+ty\), \(v=x-ty\). The sum \(N_\lambda(u)^2+N_\lambda(v)^2\) is the maximum of the four branch sums \(Q_i(u)+Q_j(v)\), for \(i,j\in\{1,2\}\).

For equal branch indices the parallelogram identity of the quadratic form yields
\[
Q_i(u)+Q_i(v)=2Q_i(x)+2t^2Q_i(y)
\le2(1+t^2).
\]
For mixed branch indices, the exact expansion is
\[
Q_1(u)+Q_2(v)
=(\lambda+2)(\|x\|_2^2+t^2\|y\|_2^2)
+2\lambda t(x_1y_1-x_2y_2).
\]
By the preceding unit-sphere estimate and Euclidean Cauchy--Schwarz,
\[
Q_1(u)+Q_2(v)
\le2(1+t^2)+\frac{4\lambda t}{\lambda+2}.
\]
Interchanging the branch indices changes the sign of the cross term; the same upper bound follows. Thus all four branches satisfy
\[
N_\lambda(x+ty)^2+N_\lambda(x-ty)^2
\le2\left(1+t^2+\frac{2\lambda t}{\lambda+2}\right).
\]

For \(1\le p\le2\), the power-mean inequality gives
\[
\left(\frac{N_\lambda(x+ty)^p+N_\lambda(x-ty)^p}{2}\right)^{1/p}
\le\left(\frac{N_\lambda(x+ty)^2+N_\lambda(x-ty)^2}{2}\right)^{1/2}
\le\sqrt{1+t^2+\frac{2\lambda t}{\lambda+2}}.
\]

Let
\[
x_*=\frac{(1,1)}{\sqrt{\lambda+2}},\qquad
y_*=\frac{(1,-1)}{\sqrt{\lambda+2}}.
\]
Both are unit vectors. Since \(t>0\), the first coordinate dominates in \(x_*+ty_*\), and the second dominates in \(x_*-ty_*\). Direct substitution gives
\[
N_\lambda(x_*+ty_*)^2
=N_\lambda(x_*-ty_*)^2
=1+t^2+\frac{2\lambda t}{\lambda+2}.
\]
The two norms on the left agree, so both the branch upper bound and the power-mean inequality are attained for every \(p\in[1,2]\). This proves the exact profile.

To classify equality, suppose a unit pair attains the profile. Because \(\lambda t>0\), the bound for a same-index branch is strictly smaller than the attained squared-norm sum, so equality requires a mixed branch. In the expansion of that branch, equality in the two Euclidean unit-sphere bounds forces both \(x\) and \(y\) onto diagonal directions:
\[
|x_1|=|x_2|=|y_1|=|y_2|=(\lambda+2)^{-1/2}.
\]
Equality in the Euclidean Cauchy--Schwarz step requires \(y\) to be proportional, with the appropriate sign, to \((x_1,-x_2)\). Equal unit norms make the proportionality coefficient a sign. Consequently, after signed-coordinate permutations and vector sign/order symmetries, the pair is \((x_*,y_*)\). Every pair in the listed orbit directly attains the same sharp expression, so the orbit is both necessary and sufficient. No other orbit maximizes.

Finally, the definitions at \(p=1\) and \(p=2\) yield the asserted \(\rho\) and \(E\) formulas. The limit at \(t=0\) follows by differentiating the exact square root. For the Lorentz translation, put \(\omega=(1+\lambda)^{-1}\); then
\[
N_\lambda(z)^2=(1+\lambda)\bigl((\max_i|z_i|)^2+\omega(\min_i|z_i|)^2\bigr).
\]
A common scaling of the norm leaves the normalized coefficient unchanged, so the same theorem holds in the standard quadratic Lorentz notation.

## Verification
The proof treats **all four** combinations of the two quadratic norm branches and proves equality without numerical optimization. For the explicit maximizing pair, direct expansion gives the exact identity
\[
Q_1(x_*+ty_*)=Q_2(x_*-ty_*)
=1+t^2+\frac{2\lambda t}{\lambda+2};
\]
the unused branch is strictly smaller by \(4\lambda t/(\lambda+2)\). The strict separation of equal-index branches, valid only when \(\lambda t>0\), is what makes the maximizing orbit rigid.

A separate randomized unit-sphere test over five positive \(\omega\)-values and five positive \(t\)-values gave no ratio exceeding the closed form; that finite test served only as a search stress test, not as a proof. Symbolic substitution additionally checked the branch identities and the exact improvement over the historical norm-comparison estimate. The analytical argument above is sufficient for all real parameters in the claimed ranges.

## Relationship to prior work
Zuo and Cui introduced the coefficient \(J_{X,p}(t)\) and studied the **same space** \(Z_\lambda\) in their 2009 paper, equations (3.5)--(3.7). They gave a Banach--Mazur comparison bound and expressly noted that exact values were not obtained in those examples. For \(1\le p\le2\), their bound becomes
\[
J_{Z_\lambda,p}(t)^2\le
\frac{2(\lambda+1)}{\lambda+2}(1+t^2).
\]
The exact present squared value is smaller than that upper bound by
\[
\frac{\lambda}{\lambda+2}(t-1)^2,
\]
so the older upper bound is sharp only at \(t=1\), not at general scales.

Zuo's 2011 paper subsequently computed \(J_{Z_\lambda,p}(1)=2\sqrt{(1+\lambda)/(2+\lambda)}\) for \(1\le p\le2\) (Example 2.9), and the equivalent \(t=1\) quantity for two-dimensional Lorentz norms (Example 2.10). That known value agrees exactly with the \(t=1\) specialization here. Neither example determines the **whole** \(t>0\) profile or its complete maximizing-pair orbit.

Gao's 2006 work introduced the Pythagorean approach at \(t=1\); Wang's 2008 work examined the parameterized Pythagorean modulus for classical \(\ell_p\) spaces. The present theorem addresses a specific non-Hilbert family rather than importing those \(\ell_p\) formulas. Related quadratic-Lorentz results for the Jordan--von Neumann, Ptolemy, Banach--Mazur, James, and Zbăganu constants use different extremal quotients and do not imply the full parameterized power-mean profile.

## Limitations
The theorem concerns real dimension two, \(\lambda>0\), \(t>0\), and \(1\le p\le2\). It does not determine \(J_{Z_\lambda,p}(t)\) for \(p>2\), other Lorentz exponents, or higher-dimensional Euclidean--sup sums. At \(t=0\), every unit pair is trivially maximizing; at \(\lambda=0\) the norm becomes Hilbertian and the maximizing-pair set is larger. The smoothness profile shows nonuniform smoothness for every \(\lambda>0\); it does not assert a uniform-smoothness estimate.

A historical exact all-scale computation expressed under a different notation could exist outside the primary literature and semantic searches inspected. The 2006 Lorentz James-constant repository full text was not accessible in the checked route, although its published abstract identifies the distinct minimum-of-two-norms invariant. That access limitation is not used as proof of noncoverage.

## References
1. J. Gao, "A Pythagorean approach in Banach spaces," *Journal of Inequalities and Applications* 2006, Article 94982, DOI 10.1155/JIA/2006/94982, published 2006-01-03.
2. F. Wang, "Some Properties of Pythagorean Modulus," *Journal of Inequalities and Applications* 2007/2008, Article 071012, DOI 10.1155/2007/71012, published 2008-02-05.
3. Z. Zuo and Y. Cui, "A Coefficient Related to Some Geometric Properties of a Banach Space," *Journal of Inequalities and Applications* 2009, Article 934321, DOI 10.1155/2009/934321; notably equations (3.5)--(3.7).
4. Z. Zuo, "A geometrical constant and normal normal structure in Banach Spaces," *Journal of Inequalities and Applications* 2011, Article 16, DOI 10.1186/1029-242X-2011-16, published 2011-06-23; primary MSC 46B20; Examples 2.9 and 2.10.
5. T. Suzuki, A. Yamano, and M. Kato, "The James Constant of 2-Dimensional Lorentz Sequence Spaces," *Bulletin of the Kyushu Institute of Technology. Pure and Applied Mathematics* 53 (2006), 15--24, DOI 10.18997/00002048, public date 2006-03-30.
