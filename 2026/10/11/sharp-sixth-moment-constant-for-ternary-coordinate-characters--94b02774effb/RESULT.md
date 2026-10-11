# Sharp sixth-moment constant for ternary coordinate characters
## Finding
Let \(G_n=(\mathbb Z/3\mathbb Z)^n\) with normalized counting measure, let \(\omega=e^{2\pi i/3}\), and let \(r_j(x)=\omega^{x_j}\) be the coordinate characters. For every integer \(n\ge2\) and every complex coefficient vector \(a=(a_1,\ldots,a_n)\),
\[
\left\|\sum_{j=1}^n a_j r_j\right\|_6
\le
\left(6-\frac8n+\frac3{n^2}\right)^{1/6}
\left(\sum_{j=1}^n|a_j|^2\right)^{1/2}.
\]
The constant is sharp. Equality for a nonzero coefficient vector holds exactly when all coefficient moduli are equal and all cubes \(a_j^3\) have one common argument. Equivalently, there are \(r>0\), \(\theta\in\mathbb R\), and \(\eta_j\in\{1,\omega,\omega^2\}\) such that
\[
a_j=r e^{i\theta}\eta_j\qquad(1\le j\le n).
\]
Thus the exact \(\Lambda(6)\) constant of the ternary coordinate system is \(\left(6-8/n+3/n^2\right)^{1/6}\).

## Assumptions and scope
The group is exactly \((\mathbb Z/3\mathbb Z)^n\), Haar measure is normalized counting measure, and the characters are the coordinate projections into the third roots of unity. The statement concerns scalar complex coefficients and the ratio of the \(L^6\) norm to the \(L^2\) coefficient norm. It does not assert an optimal constant for arbitrary character sets, arbitrary bounded orthogonal systems, or other exponents.

## Proof
Put
\[
S=\sum_j|a_j|^2,\qquad Q=\sum_j|a_j|^4,\qquad R=\sum_j|a_j|^6,\qquad T=\sum_j a_j^3.
\]
Expanding the sixth moment and using independence of the coordinate characters gives
\[
\left\|\sum_j a_jr_j\right\|_6^6
=6S^3-9SQ+3R+|T|^2.
\]
Indeed, the terms whose positive and negative multiplicities agree coordinatewise contribute the usual Steinhaus expression \(6S^3-9SQ+4R\). Because each coordinate has order three, there is one additional resonance: three positive copies of coordinate \(i\) can balance three negative copies of coordinate \(j\). Summing these terms gives \(|T|^2-R\), producing the displayed identity.

By homogeneity assume \(S=1\), and put \(x_j=|a_j|^2\). The triangle inequality and Cauchy--Schwarz give
\[
|T|^2\le\left(\sum_jx_j^{3/2}\right)^2
\le\left(\sum_jx_j\right)\left(\sum_jx_j^2\right)=Q.
\]
Hence
\[
\left\|\sum_j a_jr_j\right\|_6^6
\le 6-8\sum_jx_j^2+3\sum_jx_j^3.
\]
Let \(h(t)=3t^3-8t^2\). If two coordinates \(u,v\ge0\) are replaced by their average, while their sum is fixed, then
\[
2h\!\left(\frac{u+v}{2}\right)-h(u)-h(v)
=\frac{(u-v)^2\bigl(16-9(u+v)\bigr)}4.
\]
Since \(u+v\le1\), this is strictly positive unless \(u=v\). Repeated pairwise averaging therefore shows that \(\sum_jh(x_j)\) has its unique maximum on the probability simplex at \(x_1=\cdots=x_n=1/n\). This gives
\[
\left\|\sum_j a_jr_j\right\|_6^6
\le6-\frac8n+\frac3{n^2}.
\]
For equality, pairwise averaging forces \(|a_j|\) to be constant. Equality in the triangle inequality for \(T\) then forces all nonzero \(a_j^3\) to have the same argument. These conditions are also sufficient, so the equality classification is exact.

## Verification
The accompanying script `verify.py` independently enumerates \((\mathbb Z/3\mathbb Z)^n\) for several dimensions, checks the sixth-moment identity on deterministic coefficient samples, checks the claimed extremizers, and stress-tests the sharp inequality. The finite replay is corroborative only; the proof above establishes the theorem for every integer \(n\ge2\).

## Relationship to prior work
Bourgain and Lewko formulate \(\Lambda(p)\) bounds for bounded orthogonal systems and explicitly note that even integer exponents are handled by expanding moments; their paper also records primary classification 43A46. Their statements are qualitative and dimension-uniform and do not give the exact finite-dimensional ternary \(\Lambda(6)\) constant or its equality class. Nayar and Oleszkiewicz derive optimal even-moment Khinchine inequalities for real Rademacher variables and certain rotationally invariant random vectors; their inspected paper does not treat discrete third-root variables. The present calculation isolates the order-three resonance term \(|\sum_j a_j^3|^2\), which is absent in the nonresonant Steinhaus sixth moment and changes both the sharp constant and the extremizers.

## Limitations
The originality check found no statement of this exact ternary constant or equality classification, but terminology varies across Khinchine, \(\Lambda(p)\), and random-root-of-unity literature. The main residual risk is an older finite-root Khinchine result indexed outside the searched harmonic-analysis terminology. No claim is made for higher even moments, vector-valued coefficients, or non-coordinate character systems.

## References
1. J. Bourgain and M. Lewko, *Sidonicity and variants of Kaczmarz's problem*, arXiv:1504.05290, first public 2015-04-21; 2010 MSC 43A46, 42C05.
2. P. Nayar and K. Oleszkiewicz, *Khinchine type inequalities with optimal constants via ultra log-concavity*, Positivity 16 (2012), 359--371, DOI 10.1007/s11117-011-0130-z.
