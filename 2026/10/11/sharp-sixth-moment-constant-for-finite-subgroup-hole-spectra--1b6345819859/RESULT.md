# Sharp sixth-moment constant for finite subgroup-hole spectra
## Finding
Let \(G\) be a finite abelian group of order \(N\), let \(K\le \widehat G\) be a proper subgroup of order \(k\), and put
\[
H=K^\perp,\qquad m=|H|=N/k\ge2,\qquad \Lambda=\widehat G\setminus K.
\]
With normalized counting measure on \(G\), the exact sixth-moment synthesis constant is
\[
\boxed{K_6(\Lambda)^6=k^2\frac{m^4-5m^3+10m^2-10m+5}{(m-1)^2}}.
\]
Thus for every coefficient family \((a_\chi)_{\chi\in\Lambda}\),
\[
\left\|\sum_{\chi\in\Lambda}a_\chi\chi\right\|_6
\le K_6(\Lambda)\left(\sum_{\chi\in\Lambda}|a_\chi|^2\right)^{1/2}.
\]
Every nonzero extremizer is exactly
\[
a_\chi=A\overline{\chi(y)}\qquad(\chi\in\Lambda)
\]
for some \(A\ne0\) and \(y\in G\). Equivalently, with \(C=y+H\),
\[
f(x)=Ak\bigl(m\mathbf 1_{\{y\}}(x)-\mathbf 1_C(x)\bigr).
\]

## Assumptions and scope
Characters are orthonormal for normalized counting measure. The annihilator \(H=K^\perp\) has \(|H|=m\), and a function has Fourier support in \(\widehat G\setminus K\) exactly when its average on every coset of \(H\) is zero. The result is finite and exact for every finite abelian \(G\) and every proper subgroup \(K\le\widehat G\); no assumption on the isomorphism type of either group is needed.

## Proof
The key local statement is the following sharp zero-sum sixth-moment lemma. If \(z_1,\ldots,z_m\in\mathbb C\) satisfy \(\sum_i z_i=0\), then
\[
\sum_i|z_i|^6\le \alpha_m\left(\sum_i|z_i|^2\right)^3,
\qquad
\alpha_m=\frac{(m-1)^5+1}{m^3(m-1)^2}.
\]
Equality holds exactly, up to permutation and multiplication by a nonzero scalar, for
\[
(m-1,-1,\ldots,-1).
\]
For \(m=2\) this is immediate. Assume \(m\ge3\) and normalize \(\sum_i|z_i|^2=1\). At a constrained maximizer, Lagrange multipliers give
\[
3|z_i|^4z_i-\lambda z_i=\eta
\]
with one real \(\lambda\) and one complex \(\eta\), independent of \(i\). If \(\eta=0\), every nonzero coordinate has the same modulus, so if there are \(r\ge2\) nonzero coordinates then the objective equals \(1/r^2\le1/4\). The displayed equality candidate has value \(\alpha_m>1/4\), so a maximizer has \(\eta\ne0\). Since \(3|z_i|^4-\lambda\) is real, all coordinates are real multiples of \(\eta\); a common phase therefore makes the maximizer real.

A real maximizer has at most two distinct coordinate values. Indeed, choose three coordinates \(x,y,z\) and hold their sum and sum of squares fixed. Writing \(e_1=x+y+z\), \(e_2=xy+xz+yz\), and \(e_3=xyz\), Newton identities give
\[
x^6+y^6+z^6=e_1^6-6e_1^4e_2+6e_1^3e_3+9e_1^2e_2^2-12e_1e_2e_3-2e_2^3+3e_3^2.
\]
For fixed \(e_1,e_2\) this is a strictly convex quadratic in \(e_3\). When \(x,y,z\) are three distinct real roots, their \(e_3\) lies in the interior of the feasible interval; moving to an endpoint preserves the two constraints, produces a repeated root, and strictly increases the sixth-power sum. Hence three distinct coordinate values cannot occur at a maximum.

The maximizer therefore consists of \(r\) copies of \(a>0\) and \(m-r\) copies of \(-b<0\). The zero-sum and unit-square-mass constraints give
\[
a^2=\frac{m-r}{rm},\qquad b^2=\frac{r}{m(m-r)}.
\]
With \(t=r(m-r)\), the sixth-power sum is
\[
\Phi_m(t)=\frac{m^2}{t^2}-\frac5t+\frac5{m^2}.
\]
Because \(t\le m^2/4\),
\[
\Phi_m'(t)=\frac{5t-2m^2}{t^3}<0.
\]
Thus the maximum occurs at the smallest possible \(t=m-1\), namely \(r=1\) or \(r=m-1\), proving the lemma and its equality class.

Now let \(f\) have Fourier support in \(\Lambda\). For each coset \(C\) of \(H\), set
\[
S_C=\sum_{x\in C}|f(x)|^2.
\]
The coset average of \(f\) is zero, so the local lemma yields
\[
\sum_{x\in C}|f(x)|^6\le\alpha_m S_C^3.
\]
Summing over cosets and using \(\sum_C S_C^3\le(\sum_C S_C)^3\),
\[
\|f\|_6^6\le \alpha_mN^2\|f\|_2^6
=k^2\frac{m^4-5m^3+10m^2-10m+5}{(m-1)^2}\|f\|_2^6.
\]
Equality forces exactly one nonzero \(H\)-coset and the local one-outlier equality profile there. Hence
\[
f=c\bigl(m\mathbf1_{\{y\}}-\mathbf1_{y+H}\bigr).
\]
Fourier inversion then gives \(a_\chi=A\overline{\chi(y)}\) for every \(\chi\notin K\), and these coefficient families attain the bound.

## Verification
The included `verifier.py` checks the Newton identity exactly on \(729\) integer triples, verifies the complete two-value optimization exactly for every \(2\le m\le200\), checks the equality vectors and Fourier scaling in \(1185\) cases, and stress-tests \(5700\) random complex zero-sum vectors. Its recorded output is

`VERIFY_OK newton_exact=729 two_value_exact=19900 random_zero_sum=5700 equality_scale=1185 max_random_excess=1.110e-16`

The random tests are regression checks only; the proof above is the infinite-family argument.

## Relationship to prior work
Michels introduced the standard \(\Lambda(p)\)-constant notation and studied infinite \(\Lambda(p)\)-sets and operator-ideal consequences. That framework motivates asking for exact constants, but its stated theorems do not evaluate finite complements of subgroups or their equality cases. A known exact fourth-moment subgroup-hole formula is a lower-moment analogue; it does not imply the sixth-moment theorem because the local optimization changes from a quadratic Gram calculation to a sharp complex zero-sum sixth-moment problem.

Targeted database searches for subgroup-complement \(\Lambda(6)\) constants, finite zero-sum \(L^6/L^2\) inequalities, mean-zero coset formulations, and the exact polynomial in \(m\) did not locate an implication-equivalent statement. Search absence alone is not treated as proof of originality; the residual literature risk is stated below.

## Limitations
The theorem concerns the sixth moment only; it does not give a closed formula for arbitrary \(p\), nor does it address non-subgroup deleted frequency sets. The originality comparison has a residual risk that an older finite-dimensional moment inequality may encode the local zero-sum lemma under different probability or convexity terminology. No independent audit has been performed.

## References
1. Carsten Michels, *\(\Lambda(p)\)-sets and the limit order of operator ideals*, arXiv:math/9904176v1, first public 1999-04-30.
