# Sharp Bloch-seminorm splitting hierarchy for centered non-unicritical Blaschke zeros

## Finding

Fix an integer \(n\ge 3\) and a nonzero complex \(n\)-tuple \(a=(a_1,\ldots,a_n)\) satisfying \(\sum_{j=1}^n a_j=0\). Denote its elementary symmetric sums by \(e_j(a)\). Suppose the first nonzero one occurs at an index \(k\) with \(2\le k<n\):
\[
e_1(a)=\cdots=e_{k-1}(a)=0,\qquad e_k(a)\ne0.
\]
For sufficiently small real \(\varepsilon>0\), form the degree-\(n\) Blaschke product
\[
B_\varepsilon(z)=\prod_{j=1}^n\frac{z-\varepsilon a_j}{1-\varepsilon\overline{a_j}z},\qquad |z|<1,
\]
and write \(\beta(f)=\sup_{|z|<1}(1-|z|^2)|f'(z)|\). Set
\[
\rho_n=\sqrt{\frac{n-1}{n+1}},\quad
U_n=n(1-\rho_n^2)\rho_n^{n-1},\quad
C_{n,k}=(1-\rho_n^2)\rho_n^{n-1}
\left[(n+k)\rho_n^k-(n-k)\rho_n^{-k}\right].
\]
Then the exact leading directional change is
\[
\boxed{\beta(B_\varepsilon)=U_n+C_{n,k}|e_k(a)|\varepsilon^k+O_{n,a}(\varepsilon^{k+1}),\qquad C_{n,k}>0.}
\]
Thus the first nonzero symmetric coefficient of the centered splitting determines **both** the exact order of flatness and the positive leading coefficient of Bloch-seminorm growth. Every order \(k=2,\ldots,n-1\) actually occurs. For each fixed integer \(k\ge2\), the sharp coefficient moreover satisfies the sequential degree limit
\[
\boxed{\lim_{n\to\infty,\;n>k}n^3 C_{n,k}=\frac{4k(k^2-1)}{3e}.}
\]
This is a directional statement: \(n\) and \(a\) are fixed before \(\varepsilon\downarrow0\); no uniform joint degree/perturbation limit is asserted.

## Assumptions and scope

The zeros \(\varepsilon a_j\) are counted with multiplicity, may include zero, and all lie in the open disk when \(\varepsilon\max_j|a_j|<1\). The product is written with the unimodular factor equal to one; multiplying by any unimodular constant does not affect \(\beta\). Centering is algebraic, \(e_1(a)=0\). The excluded case \(k=n\), in which the nonzero zeros form a regular \(n\)-gon after a rotation, is the unicritical family \((z^n-t)/(1-\overline t z^n)\) and is not claimed as new. The case \(e_1(a)\ne0\) is also outside this claim because infinitesimal disk-automorphism directions require a different normalization. The primary subject is Bloch seminorms of finite inner functions (MSC2020 30H30).

## Proof

**Step 1: The unperturbed norming circle.** Direct differentiation of \(B_0(z)=z^n\) gives
\[
P_n(r)=n(1-r^2)r^{n-1},\qquad 0\le r\le1.
\]
For \(n\ge3\), \(P_n\) has exactly one positive maximizer \(\rho_n\), determined by \((n-1)-(n+1)\rho_n^2=0\). It is a strict nondegenerate maximum and \(P_n(\rho_n)=U_n\). The maximizing angles at \(\varepsilon=0\) form the full circle.

**Step 2: Uniform first nonvanishing variation.** Expanding the numerator and denominator via elementary symmetric sums gives, uniformly together with the first derivative on the closed unit disk as \(\varepsilon\to0^+\),
\[
B_\varepsilon(z)=z^n+(-1)^k\varepsilon^k\left[e_k(a)z^{n-k}-\overline{e_k(a)}z^{n+k}\right]+O_{n,a}(\varepsilon^{k+1}).
\]
Indeed, all lower elementary symmetric sums vanish, and the denominator has no zeros on the closed disk when \(\varepsilon\) is small. The expansion and its derivative follow from finite polynomial multiplication and the uniformly convergent inverse-denominator Taylor expansion. Near the circle \(r=\rho_n\), division by the nonzero derivative \(nz^{n-1}\) and the differential \(|v+h|=|v|+\operatorname{Re}(h\overline v/|v|)+O(|h|^2/|v|)\) yield
\[
\begin{aligned}
(1-r^2)|B_\varepsilon'(re^{i\theta})|
&=P_n(r)\\
&\quad+(-1)^{k+1}\varepsilon^k(1-r^2)r^{n-1}D_{n,k}(r)
  \operatorname{Re}(e_k(a)e^{-ik\theta})
+O_{n,a}(\varepsilon^{k+1}),\\
D_{n,k}(r)&=(n+k)r^k-(n-k)r^{-k}.
\end{aligned}
\]
The remainder is uniform in \(r,\theta\) in a fixed closed annulus around \(\rho_n\), including one radial derivative. Because the unperturbed maximum is strict in the radial variable and the perturbation is uniformly small on the closed disk, every perturbed global maximizing radius stays near \(\rho_n\). Nondegeneracy and the radial derivative expansion give a displacement of order \(O_{n,a}(\varepsilon^k)\). Substituting this displacement changes the optimized value by at most \(O_{n,a}(\varepsilon^{2k})\), which is contained in \(O_{n,a}(\varepsilon^{k+1})\) since \(k\ge2\).

**Step 3: Positivity and exact angular maximization.** For \(2\le k<n\),
\[
D_{n,k}(\rho_n)>0
\quad\Longleftrightarrow\quad
\frac{n+k}{n-k}>
\left(\frac{n+1}{n-1}\right)^k.
\]
Taking logarithms reduces the inequality to \(\operatorname{artanh}(k/n)>k\operatorname{artanh}(1/n)\). This is strict because the power series \(\operatorname{artanh}(x)/x=\sum_{j\ge0}x^{2j}/(2j+1)\) is strictly increasing for \(0<x<1\) and \(k>1\). Maximizing the real cosine \((-1)^{k+1}\operatorname{Re}(e_k(a)e^{-ik\theta})\) over \(\theta\) gives exactly \(|e_k(a)|\), attained at \(k\) angular directions. Evaluating the radial factor at \(\rho_n\) proves the boxed expansion and strict positivity.

**Step 4: Every flatness order and the degree limit.** For each \(2\le k<n\), choose the first \(k\) entries of \(a\) to be all \(k\)-th roots of unity and let the other \(n-k\) entries be zero. The generating polynomial is \(z^{n-k}(z^k-1)\), whence all lower elementary symmetric sums vanish and \(|e_k(a)|=1\); thus every listed order is realized. For the large-degree coefficient, put \(t_n=\operatorname{artanh}(1/n)\), so \(\rho_n=e^{-t_n}\) and
\[
D_{n,k}(\rho_n)=2\bigl[k\cosh(kt_n)-n\sinh(kt_n)\bigr]
=\frac{2k(k^2-1)}{3n^2}+O_k(n^{-4}).
\]
Since \((1-\rho_n^2)\rho_n^{n-1}=2/(en)+O(n^{-2})\), multiplication gives \(C_{n,k}=4k(k^2-1)/(3en^3)+O_k(n^{-4})\).

## Verification

The included standalone `checker.py` uses high-precision arithmetic to verify positivity and first-variation coefficients for all \(3\le n\le25\), \(2\le k<n\), the fixed-mode degree asymptotic, and non-real centered constellations. Run `python checker.py` in an environment with `mpmath`. The checked coefficient is calculated independently from the exact rational derivative of \(z^{n-k}(z^k-t)/(1-tz^k)\), not by assuming the theorem's expansion. This finite computation corroborates the analytic proof; it cannot establish quantifiers over every degree and direction.

## Relationship to prior work

Baranov–Kayumov–Nasyrov establish universal Bloch-seminorm lower bounds for finite Blaschke products and use the monomial sequence \(z^n\) to obtain the limiting upper value \(2/e\); their inspected theorem and proof do not give a centered zero-splitting expansion or the hierarchy of first nonzero symmetric coefficients. Exact formulas for **unicritical** Blaschke products already describe Möbius transforms of \(z^n\), corresponding to the excluded regular-polygon \(k=n\) family. The present family has \(k<n\), so its zero divisor contains a nonregular centered splitting and is not a disk-automorphic conjugate of the unicritical family. Dubinin's distortion theorem bounds the derivative using critical-value constraints; it does not state this exact directional perturbation formula. These comparisons establish a differentiated claim, not a proof of global novelty.

## Limitations

The theorem does not assert a global minimum of \(\beta\) among all degree-\(n\) Blaschke products, a neighborhood-uniform lower bound over all zero constellations, or the same formula without centering. The constants implicit in \(O_{n,a}\) depend on the fixed splitting and degree, so the coefficient limit for fixed \(k\) is not a joint \(n,\varepsilon\) asymptotic. The excluded unicritical regular-polygon case has prior exact treatment. Historical priority outside the inspected literature remains possible; no independent validation is represented.

## References

- A. D. Baranov, I. R. Kayumov, S. R. Nasyrov, *On Bloch seminorm of finite Blaschke products in the unit disk*, arXiv:2203.15142 (public preprint dated 2022-03-28); *J. Math. Anal. Appl.* 509 (2022), article 125983.
- V. N. Dubinin, *Distortion and critical values of the finite Blaschke product*, arXiv:2003.03884 (public preprint dated 2020-03-09); *Constr. Approx.* 55 (2022), 629–639.
- *Mathematics Subject Classification 2020*, code 30H30 (Bloch spaces).
