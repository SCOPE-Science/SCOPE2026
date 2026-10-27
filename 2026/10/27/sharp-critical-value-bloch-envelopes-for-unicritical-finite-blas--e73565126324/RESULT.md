# Sharp critical-value Bloch envelopes for unicritical finite Blaschke products

## Finding
For every finite Blaschke product \(B\) of degree \(n\ge2\) with precisely one critical point \(c\) of multiplicity \(n-1\), write \(a=|B(c)|\in[0,1)\). Its unnormalized Bloch seminorm is \(\beta(B)=\sup_{z\in\mathbb D}(1-|z|^2)|B'(z)|\). Then
\[
\beta(B)=\max_{s>0}Q_{n,a}(s),\qquad Q_{n,a}(s)=\frac{2n e^{-s}\sinh(s/n)(1-a^2)}{(1-ae^{-s})^2}.
\]
There is exactly one maximizing \(s_n(a)\in(0,n\operatorname{arccoth}n]\), determined by
\[
a=e^{s_n(a)}\frac{\coth(s_n(a)/n)-n}{\coth(s_n(a)/n)+n}.
\]
At \(a=0\), \(\beta_n(0)=\frac{2n}{n+1}\left(\frac{n-1}{n+1}\right)^{(n-1)/2}\). The function \(a\mapsto\beta_n(a)\) is strictly increasing and tends to \(1\) at the upper endpoint; for fixed \(a\), the numbers \(\beta_n(a)\) strictly decrease in integer degree \(n\ge2\). The sharp degree-uniform inequality is
\[
\beta(B)>\mathcal B(a):=\max_{s>0}\frac{2s e^{-s}(1-a^2)}{(1-ae^{-s})^2}.
\]
The bound is approached by canonical products as \(n\to\infty\) but never attained at finite degree. For the unique \(s=s(a)\in(0,1]\),
\[
a=e^s\frac{1-s}{1+s},\qquad \mathcal B(a)=2\cosh s-\left(s+\frac1s\right)\sinh s.
\]
This is strictly increasing with \(a\), equals \(2/e\) at \(a=0\), tends to \(1\) as \(a\uparrow1\), and has \(\mathcal B(a)=2/e+4a/e^2+O(a^2)\) as \(a\downarrow0\). For canonical \(F_{n,a}(z)=(z^n-a)/(1-az^n)\), the norm is attained precisely at \(z=e^{-s_n(a)/n}e^{2\pi ik/n}\), \(0\le k<n\), when \(a>0\). At \(a=0\), every point on the same circle attains the norm. The norming sets for general \(B\) are pulled back by disk automorphisms.

## Assumptions and scope
Critical multiplicity is counted in the unit disk. The modulus \(a\) refers to the **critical value** rather than the location of the critical point. The seminorm includes exactly the weight \(1-|z|^2\). This theorem concerns the unicritical class, not all finite Blaschke products.

## Proof
**Reduction.** Precompose \(B\) with a disk automorphism taking \(0\) to its unique critical point, and postcompose with an automorphism taking the critical value to zero. The resulting proper map of degree \(n\) has a zero of multiplicity \(n\) at the origin (its ramification order is \(n-1\)), and so is a rotation of \(z^n\). Undoing the postcomposition and adjusting rotations yields \(F_{n,a}\). The identity \((1-|z|^2)|\varphi'(z)|=1-|\varphi(z)|^2\) proves that input disk automorphisms preserve \(\beta\), while output rotations preserve derivative modulus.

**Uniqueness.** Direct differentiation gives
\[
(1-|z|^2)|F'_{n,a}(z)|=\frac{n(1-a^2)|z|^{n-1}(1-|z|^2)}{|1-az^n|^2}.
\]
At fixed radius \(z^n=t e^{i\phi}\), the denominator is smallest exactly at \(\phi=0\) if \(a>0\), and is phase independent when \(a=0\). Set \(t=e^{-s}\) to obtain \(Q_{n,a}\), which vanishes at both endpoints \(s=0,\infty\). Its logarithmic critical equation is \(\frac1n\coth(s/n)-1-\frac{2ae^{-s}}{1-ae^{-s}}=0\). With \(c_s=\coth(s/n)>n\), the logarithmic derivative of the resulting expression \(e^s(c_s-n)/(c_s+n)\) is
\[
\frac{2-n^2-c_s^2}{c_s^2-n^2}<0.
\]
That expression decreases continuously from one at \(s=0\) to zero at \(s=n\operatorname{arccoth}n\); beyond this interval no positive \(a\) solves the critical equation. Thus the maximum and its norming points are unique in radius, and all angular equality cases are classified. Substitution gives the stated \(a=0\) value.

**Monotonicity.** Write \(t=e^{-s}\) and
\[
Q_{n,a}(s)=\frac{n\sinh(s/n)}{\sinh s}\left[1-\left(\frac{t-a}{1-at}\right)^2\right].
\]
The first factor increases strictly with \(t\) because \(u\coth u\) increases in \(u>0\); the bracket increases on \(0<t<a\). Hence the maximizing \(t\) exceeds \(a\). At fixed \(s\), \(\partial_a\log Q_{n,a}=2(t-a)/((1-a^2)(1-at))\), positive at the maximum; the envelope rule proves strict monotonicity in \(a\). Schwarz–Pick gives \(\beta_n(a)<1\) for nonautomorphisms, and evaluating at \(t=a\) proves the limit \(\beta_n(a)\to1\). Since \(n\sinh(s/n)=s\sinh(s/n)/(s/n)\) decreases strictly with \(n\), the maxima strictly decrease with degree.

**Limiting envelope.** The pointwise limit as \(n\to\infty\) of \(Q_{n,a}\) is \(2s e^{-s}(1-a^2)/(1-ae^{-s})^2\). Compactness of maximizers follows from uniform small-\(s\) decay and the uniform tail bound \(n\sinh(s/n)\le2\sinh(s/2)\) for \(n\ge2\). Thus maxima converge to the maximum of that limit. Its stationary equation is \(a=e^s(1-s)/(1+s)\), decreasing from one to zero on \((0,1]\), so the maximizer is unique. Substitution yields the formula for \(\mathcal B(a)\). Differentiating the envelope at \(a=0\) gives \(4/e^2\); the same monotonicity argument applies to the limiting profile.

## Verification
Run the accompanying self-contained Python 3 standard-library program `check.py`. It evaluates stationary roots and norms, monotonicity, finite-versus-limit inequalities and nearby off-optimum values. These finite numerical checks corroborate but do not replace the preceding quantified proof.

## Relationship to prior work
Baranov, Kayumov and Nasyrov (arXiv:2203.15142) prove a universal lower bound exceeding \(0.695\) for arbitrary finite Blaschke products and present the monomial limit \(2/e\) as an upper obstruction for a conjecturally optimal universal constant. The present result solves a different sharp critical-value-conditioned problem within the unicritical subclass, with explicit extremizers. Kraus and Roth (arXiv:1303.6769) treat maximal Blaschke products and critical sets rather than these Bloch norm profiles. Colonna's 1987 Bloch-constant article could be a historical priority risk; only its abstract was accessible.

## Limitations
No claim is made for multiply ramified finite Blaschke products, nor that the universal general Blaschke lower constant equals \(2/e\). There is no claim of an independently certified proof or exhaustive historical priority. The parameter endpoint \(a=1\) is excluded.

## References
1. A. Baranov, I. Kayumov, A. Nasyrov, *On Bloch seminorm of finite Blaschke products in the unit disk*, arXiv:2203.15142, first public 2022-03-28.
2. D. Kraus, O. Roth, *Maximal Blaschke Products*, arXiv:1303.6769.
3. F. Colonna, *The Bloch Constant of Bounded Analytic Functions*, J. London Math. Soc. 36 (1987), 95–101, DOI:10.1112/jlms/s2-36.1.95.
