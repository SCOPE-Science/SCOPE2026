# Universal angular Hessian of Baernstein quasi-norm ratios

## Finding

Let \(n\ge2\) be an integer and put
\[
\zeta_j=\exp\!\left(\frac{(2j+1)\pi i}{n}\right),\qquad j=0,\ldots,n-1,
\qquad Q_n(z)=1+z^n.
\]
For every sufficiently small real vector \(\boldsymbol\varepsilon=(\varepsilon_0,\ldots,\varepsilon_{n-1})\), define the monic polynomial
\[
P_{\boldsymbol\varepsilon}(z)=\prod_{j=0}^{n-1}
 \bigl(z-\zeta_je^{i\varepsilon_j}\bigr),\qquad
\overline\varepsilon=\frac1n\sum_j\varepsilon_j,
\qquad D(\boldsymbol\varepsilon)^2=
 \sum_j(\varepsilon_j-\overline\varepsilon)^2.
\]
For every fixed \(0<r<\infty\), where \(\|P\|_r=(\int_{\mathbb T}|P|^r\,dm)^{1/r}\) and \(m\) is normalized Haar measure, the exact local law is
\[
\boxed{\displaystyle
\log\frac{\|P_{\boldsymbol\varepsilon}\|_r}{\|Q_n\|_r}
 =\frac{nr}{8}D(\boldsymbol\varepsilon)^2
 +o\bigl(D(\boldsymbol\varepsilon)^2\bigr)
\quad\text{as }D(\boldsymbol\varepsilon)\to0.}
\]
The remainder is interpreted modulo common rotation: a common phase leaves the norm unchanged; on the hyperplane \(\sum_j\varepsilon_j=0\) the usual multivariate little-o is meant. In particular, for every fixed \(0\le s<t<\infty\), with the Mahler measure convention at \(s=0\),
\[
\boxed{\displaystyle
\log\left(
\frac{\|P_{\boldsymbol\varepsilon}\|_t/\|Q_n\|_t}
{\|P_{\boldsymbol\varepsilon}\|_s/\|Q_n\|_s}
\right)
=\frac{n(t-s)}8D(\boldsymbol\varepsilon)^2
+o\bigl(D(\boldsymbol\varepsilon)^2\bigr).}
\]
Thus, for fixed \(n,s,t\), there is a sufficiently small angular neighborhood of the regular polygon in which this logarithmic gap is at least \(n(t-s)D(\boldsymbol\varepsilon)^2/16\). The coefficient \(n(t-s)/8\) is the **sharp local quadratic coefficient**: increasing it makes such an inequality false along any nonzero transverse direction sufficiently close to the regular polygon. On the quotient by simultaneous root rotation, the entire Hessian is scalar, with no preferred Fourier mode, for every positive finite exponent (including the quasi-norm range \(0<r<1\)).

## Assumptions and scope

The roots are listed and matched to the simple roots of \(Q_n\); perturbations are small enough that they remain distinct and retain their cyclic order. The statement concerns a fixed finite degree and fixed finite exponent pair. Its geometric deviation is the squared Euclidean angular distance to the orbit of rotated regular polygons, using the natural local matching. The norm at exponent zero is the Mahler measure, equal to one for every monic polynomial with all roots on \(\mathbb T\). No estimate at exponent \(+\infty\), no global angular transport estimate, and no neighborhood size uniform in degree or exponent are asserted.

The paper motivating this direction proves that \(\|P\|_r/\|Q_n\|_r\) is nondecreasing in \(r\) for arbitrary polynomials with unimodular roots. The present theorem is the exact *transverse second variation* of its logarithmic two-exponent deficit at the regular-polygon extremizer; it is not another consequence obtained by simply changing the two exponents.

## Proof

**1. Remove the rotation mode.** Multiplying all roots by \(e^{i\eta}\) replaces \(P(z)\) by \(e^{in\eta}P(e^{-i\eta}z)\) and hence leaves all its circle means unchanged. We may therefore assume \(\sum_j\varepsilon_j=0\). The product of the roots, and thus the constant coefficient of \(P_{\boldsymbol\varepsilon}\), is then constant. Together with the unchanged monic coefficient and the unimodularity of all roots, this gives \(P_{\boldsymbol\varepsilon}=P_{\boldsymbol\varepsilon}^{*}\), where the reflection is \(P^{*}(z)=z^n\overline{P(1/\bar z)}\). Consequently \(e^{-int/2}P_{\boldsymbol\varepsilon}(e^{it})\) is real for every real \(t\).

**2. The first variation and Fourier orthogonality.** For a real direction \(\boldsymbol v\) with \(\sum_jv_j=0\), write \(P_\tau=P_{\tau\boldsymbol v}\) and \(q=Q_n\). Since \(\zeta_j^n=-1\), differentiating the product of roots at \(\tau=0\) gives
\[
\dot P(z)=i\sum_{k=1}^{n-1}S_kz^k,
\qquad S_k=\sum_{j=0}^{n-1}v_j\zeta_j^{-k}.
\]
The finite Fourier identity and \(\sum_jv_j=0\) imply
\[
\sum_{k=1}^{n-1}|S_k|^2=n\sum_jv_j^2.
\]
For any integrable scalar weight \(w(e^{it})\) invariant under \(t\mapsto t+2\pi/n\), the intermediate monomials are orthogonal:
\[
\int_{\mathbb T}w|\dot P|^2\,dm
=\left(\int_{\mathbb T}w\,dm\right)
 \sum_{k=1}^{n-1}|S_k|^2.
\]
Likewise, \(\int_{\mathbb T}|q|^{r-2}\operatorname{Re}(\bar q(P_\tau-q))\,dm=0\) whenever \(r>1\): all coefficients of \(P_\tau-q\) have degrees strictly between zero and \(n\), while \(|q|^{r-2}\bar q\) has only frequencies divisible by \(n\).

**3. Compute the Hessian for \(r>1\).** Put \(M_r(\tau)=\int_{\mathbb T}|P_\tau|^r\,dm\). By the reality statement in Step 1, \(P_\tau(e^{it})e^{-int/2}\) is a real-valued perturbation of \(2\cos(nt/2)\). Its zeros at \(\tau=0\) are simple. Since \(r>1\), the weight \(|q|^{r-2}\) is integrable, and the second-variation formula for a real power gives
\[
M_r(\tau)=M_r(0)+\frac{r(r-1)}2\tau^2
 \int_{\mathbb T}|q|^{r-2}|\dot P|^2\,dm+o(\tau^2).
\]
There is no linear contribution from the second-order change in the polynomial: that term contains only intermediate Fourier degrees, and the preceding orthogonality kills it. Writing \(A_u=\int_{\mathbb T}|1+z^n|^u\,dm\), the beta integral yields, for \(u>-1\),
\[
A_u=\frac{2^u\Gamma((u+1)/2)}{\sqrt\pi\Gamma(1+u/2)},
\qquad \frac{A_{r-2}}{A_r}=\frac{r}{4(r-1)}\quad(r>1).
\]
The preceding finite Fourier identity therefore yields
\[
M_r(\tau)=A_r\left(1+\frac{nr^2}{8}\tau^2
 \sum_jv_j^2+o(\tau^2)\right),\qquad r>1.
\]
Taking the logarithm and dividing by \(r\) proves
\[
\log\frac{\|P_{\tau\boldsymbol v}\|_r}{\|Q_n\|_r}
=\frac{nr}{8}\tau^2\sum_jv_j^2+o(\tau^2)
\quad(r>1).
\]
The same calculation with two directions and polarization identifies the full Hessian, not merely a selected direction.

**4. Cross the apparently singular exponent \(r=1\).** This step is necessary: directly inserting \(0<r\le1\) into the integral involving \(|q|^{r-2}\) is invalid. Instead fix \(\boldsymbol v\). In a neighborhood of each simple boundary zero \(t_j(\tau)=\arg\zeta_j+\tau v_j\), use the moving coordinate \(u=t-t_j(\tau)\). For small \(\tau\), on a fixed sufficiently short interval one has
\[
|P_\tau(e^{it})|=|u|\,b_j(u,\tau),
\]
where \(b_j\) is smooth, strictly positive and bounded away from zero along with its reciprocal. With smooth moving cutoffs, the corresponding integral becomes an integral of \(|u|^r b_j(u,\tau)^r\) times a smooth compactly supported function; on the complement no zero is present. Differentiation twice in \(\tau\) is thus legitimate **after** this coordinate change for every complex \(r\) with \(\operatorname{Re}r>-1\), and the resulting second derivative is holomorphic in \(r\) there. The same is true of the unperturbed integral \(A_r\).

The identity from Step 3 says
\[
\left.\frac{d^2}{d\tau^2}M_r(\tau)\right|_{\tau=0}
=\frac{nr^2}{4}A_r\sum_jv_j^2
\qquad(r>1).
\]
Both sides are holomorphic on the connected half-plane \(\operatorname{Re}r>-1\); the identity theorem extends it throughout that half-plane. The first derivative vanishes there as well, by the same argument applied to its identically zero values for \(r>1\). Therefore the quadratic expansion and the logarithmic norm formula hold for every real \(r>0\), including \(0<r\le1\). The identity is checked on a basis of real mean-zero directions and polarized, and continuous second derivatives yield the multivariate little-o remainder. This justifies the quasi-norm statement without treating nonintegrable formal expressions as integrals.

**5. Two exponents and sharpness.** For \(s>0\), subtract the two established expansions. At \(s=0\), Jensen's formula says \(\|P_\tau\|_0=\|Q_n\|_0=1\), so the same difference formula holds with \(s=0\). Restoring the common rotation replaces \(\sum_j\varepsilon_j^2\) by \(D(\boldsymbol\varepsilon)^2\). Positivity of \(t-s\) and the little-o remainder give the local lower bound with half the limiting constant. Along any fixed nonzero mean-zero vector and \(\tau\downarrow0\), division by \(\tau^2\sum_jv_j^2\) tends exactly to \(n(t-s)/8\); this proves sharpness. Every nonrotational direction has the same second variation, so the transverse Hessian has condition number one.

## Verification

The reproducible program `artifacts/check_hessian.py` checks the finite Fourier identity and numerically evaluates the original boundary integral with the integration intervals split at the *moving* simple zeros, for \(n=2,3,5\), \(r=1/2,1,2,4\) and decreasing nonrotational angular perturbations. It compares the observed gap to the claimed coefficient. This is a numerical diagnostic, not a substitute for the finite Fourier proof or the holomorphic-exponent continuation argument. The exact beta-integral ratio is independently derived above using the gamma recurrence.

## Relationship to prior work

Teng Zhang's October 2026 solution of Baernstein's quasi-norm monotonicity conjecture establishes monotonicity for arbitrary unimodular-root polynomials and all exponent pairs. In Section 1.2 it explicitly distinguishes that distribution-free inequality from a quantitative refinement measuring discrepancy of the zero-counting measure. Its Sections 6 and 7.4–7.5 establish the global inequality, a logarithmic-variance bound and relative-entropy inequalities, but do not calculate the full angular Hessian or this sharp local coefficient.

Two subsequent published mathematical results, *Strict Baernstein monotonicity and quantitative binomial rigidity* and *Equality rigidity and a quantitative defect for Baernstein monotonicity*, establish strictness and positive coefficient/Hardy–Dirichlet defects. Their full scientific statements and proofs were compared: neither states nor implies the exact \(n(t-s)/8\) angular coefficient or isotropy of the entire Hessian for every finite exponent. In particular, a nonoptimal lower bound for a coefficient defect cannot identify the exact second derivative in all root-displacement directions. Lei and Zhang's May 2026 entropy theorem settles equality at a specific exponent, not this local norm-ratio geometry. General Fourier bounds for equidistribution of zeros address different quantities.

## Limitations

The result is local near distinct regular-polygon zeros and applies only to fixed finite exponents and degree. It does not quantify the neighborhood size, establish a degree-uniform stability radius, characterize a global optimum solely from the Hessian, or cover the supremum-norm endpoint. The source search and comparison found no equivalent exact Hessian, but unindexed earlier local-perturbation computations remain a priority risk. Independent validation has not been carried out.

## References

1. T. Zhang, *Baernstein's Quasi-Norm Monotonicity Conjecture for Polynomials with Unimodular Zeros*, arXiv:2610.02009v1 (first public 2026-10-01), especially Sections 1, 2, 6 and 7.
2. J. Lei and T. Zhang, *Proof of the Agler--McCarthy Entropy Conjecture*, arXiv:2605.03949v1 (2026-05-05).
3. J. Agler and J. E. McCarthy, *The Krzyż Conjecture and an Entropy Conjecture*, Journal d'Analyse Mathématique 144 (2021), 207–226.
4. *Strict Baernstein monotonicity and quantitative binomial rigidity*, published mathematical record (2026-10-11), full result inspected.
5. *Equality rigidity and a quantitative defect for Baernstein monotonicity*, published mathematical record (2026-10-11), full result inspected.
6. K. Soundararajan, *Equidistribution of zeros of polynomials*, arXiv:1802.06506 (2018), for comparison with global root-discrepancy methods.
