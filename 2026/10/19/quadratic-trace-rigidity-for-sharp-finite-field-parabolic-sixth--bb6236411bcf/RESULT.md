# Quadratic-trace rigidity for sharp finite-field parabolic sixth moments

## Finding
Let \(p\ge5\) be prime, \(q=p^n\), \(n\ge1\), and \(\psi(s)=\exp(2\pi i\operatorname{Tr}_{\mathbb F_q/\mathbb F_p}(s)/p)\). For arbitrary complex \(f:\mathbb F_q\to\mathbb C\), put
\[
\mathcal E f(u,v)=q^{-1}\sum_{t\in\mathbb F_q}f(t)\psi(ut+vt^2).
\]
The sharp known inequality is
\[
\sum_{u,v\in\mathbb F_q}|\mathcal E f(u,v)|^6
\le(1+q^{-1}-q^{-2})\left(q^{-1}\sum_t|f(t)|^2\right)^3.
\]
**Every nonzero equality case**, including over every proper extension field \(\mathbb F_{p^n}\), is exactly
\[
 f(t)=\lambda\psi(a t+b t^2),\qquad
 \lambda\in\mathbb C\setminus\{0\},\quad a,b\in\mathbb F_q.
\]
The \(q^2\) pairs \((a,b)\) give **precisely \(q^2\) distinct classes modulo nonzero complex scaling**. No quadratic forms over the prime-field vector space that fail to be field-trace quadratics yield additional extremizers.

## Assumptions and scope
The field has odd characteristic strictly greater than three; \(n\) is arbitrary. Counting measure is used in the extension target, and normalized counting measure \(q^{-1}\) on the parameter line. The sharp constant and the necessity of constant modulus are established in González-Riquelme and Oliveira e Silva [1, Theorem 1.3]; the result here is a complete phase classification over all prime-power fields. All equalities are equalities of complex-valued functions, not only nonnegative inputs.

## Proof
**1. The generic triple-fiber condition.** Orthogonality on \(\mathbb F_q^2\) reduces the sixth moment to the ordered threefold convolution. The generic fiber indexed by
\[
  (s,e)=\big(t_1+t_2+t_3,\ t_1^2+t_2^2+t_3^2\big),\qquad e\ne s^2/3,
\]
has constant cardinality \(q-\chi(-3)\), while the critical fibers are indexed by \(e=s^2/3\); see [1, Proposition 3.3 and (6.2)]. Equality in the sharp inequality forces constant modulus by [1, Theorem 1.3]. The proof in [1, Section 6] bounds every generic fiber by Cauchy–Schwarz before further nonnegative estimates. As constants attain every step of these bounds, a maximizer must attain equality in this first Cauchy–Schwarz estimate on each generic fiber. Consequently
\[
 f(t_1)f(t_2)f(t_3)=f(t'_1)f(t'_2)f(t'_3)
\]
whenever both triples share the same \(s,e\) with \(e\ne s^2/3\). Here \(f\) has no zeros.

**2. A universal four-point resonance.** For arbitrary \(a,h\in\mathbb F_q\), the triples \((a,a,a+3h)\) and \((a+2h,a+2h,a-h)\) have equal sum and equal square-sum. For \(h\ne0\), the common fiber is generic, since \(e-s^2/3=6h^2\ne0\). Therefore
\[
 f(a)^2f(a+3h)=f(a+2h)^2f(a-h)\tag{1}
\]
for every \(a,h\), including \(h=0\) trivially.

Fix a nonzero direction \(h\) and any affine prime-field line \(a+\mathbb F_p h\). Set \(z_k=f(a+kh)\) and \(r_k=z_{k+1}/z_k\), with indices modulo \(p\). Equation (1) gives \(r_{k-1}r_{k+2}=r_kr_{k+1}\), so \(r_{k+2}/r_{k+1}=r_k/r_{k-1}\). The consecutive ratios \(r_{k+1}/r_k\) are two-periodic and, because \(p\) is odd, constant, say \(\sigma\). Thus \(r_k=r_0\sigma^k\), and \(p\)-periodicity yields \(\sigma^p=r_0^p=1\). Every line restriction has the form
\[
 f(a+kh)=f(a)r_0^k\sigma^{k(k-1)/2},\qquad k\in\mathbb F_p.\tag{2}
\]
In particular, normalizing by \(f(0)\), equation (2) on each line through zero shows \(f(t)/f(0)\) is a \(p\)-th root of unity. Write \(f(t)=\lambda\exp(2\pi i\varphi(t)/p)\), where \(\varphi:\mathbb F_q\to\mathbb F_p\) and \(\varphi(0)=0\). Every affine \(\mathbb F_p\)-line restriction of \(\varphi\) is a polynomial of degree at most two.

**3. Exact low-degree lemma.** For \(p>3\), such a linewise quadratic function on an \(\mathbb F_p\)-vector space is a polynomial function of total degree at most two. Here is a finite-difference proof. Put \(\Delta_h=T_h-1\), where \(T_h\) translates by \(h\). The line property gives \(\Delta_h^3\varphi=0\) for every \(h\). For directions \(u,v\), write \(x=\Delta_u\), \(y=\Delta_v\). In the commuting translation algebra, \(x^3\varphi=y^3\varphi=0\) and \(\Delta_{u+tv}=(1+x)(1+y)^t-1\). Expansion for \(t\in\mathbb F_p\), after applying to \(\varphi\), gives
\[
0=3t x^2y\varphi+3t^2 xy^2\varphi
 +\frac{3t(5t-1)}2 x^2y^2\varphi.\tag{3}
\]
Since the polynomial has degree at most two and vanishes for all \(p\ge5\) values of \(t\), its two coefficients vanish. Interchanging \(u,v\) then forces \(x^2y^2\varphi=x^2y\varphi=xy^2\varphi=0\) (the key factor is \(3\), invertible for \(p>3\)). Finally, expanding \(\Delta_{u+v+w}^3\varphi=0\) for three directions, all cubic and higher terms vanish except \(6\Delta_u\Delta_v\Delta_w\varphi\); thus this last term vanishes. Vanishing of all third mixed differences is equivalent, by Newton interpolation in a prime-field basis, to
\[
\varphi(t)=L(t)+Q(t),\tag{4}
\]
where \(L\) is \(\mathbb F_p\)-linear and \(Q\) is an \(\mathbb F_p\)-quadratic form (\(Q(ct)=c^2Q(t)\) and its polarization is bilinear).

**4. Generic rotations eliminate exotic quadratic forms.** On the two-dimensional \(\mathbb F_q\)-space
\[
W=\{(x,y,z)\in\mathbb F_q^3:x+y+z=0\}
\]
consider \(S(x,y,z)=x^2+y^2+z^2\), a nondegenerate binary quadratic form because \(p>3\). Let \(F(x,y,z)=Q(x)+Q(y)+Q(z)\), an \(\mathbb F_p\)-quadratic form on \(W\). Equality of generic triple products implies \(F(Rw)=F(w)\) for every \(R\in\mathrm{SO}(W,S)\) and \(w\in W\) with \(S(w)\ne0\); the linear term in (4) cancels because triples have equal sum. If \(S\) is anisotropic, this already covers nonzero \(w\). If split, the same identity holds also on \(S(w)=0\): for a fixed isotropic \(w\), choose \(v\) such that \(S(v),S(v+w),S(v-w)\) are all nonzero. Such \(v\) exists since each forbidden level-zero locus contains at most \(2q\) points and, more directly, in split coordinates the three forbidden loci are two lines each and there exist choices with both coordinates away from the three excluded shifts for \(q\ge5\). The parallelogram identity for the quadratic form \(F\circ R-F\) then forces its value at \(w\) to vanish.

We use the following invariant-form fact, proved by diagonalizing the cyclic rotation group over an algebraic closure: for \(p\ge5\), **every \(\mathbb F_p\)-quadratic form on a nondegenerate binary \(\mathbb F_q\)-quadratic space \((W,S)\) invariant under \(\mathrm{SO}(W,S)\) is \(\operatorname{Tr}(cS)\) for a unique \(c\in\mathbb F_q\)**. For completeness, in the split case the rotation group has order \(q-1\) and weights \(t^{p^i}\) and \(t^{-p^i}\) for \(0\le i<n\); the only opposite weight pairs in its symmetric square have the same \(i\), since \(q-1>2p^{n-1}\). In the anisotropic case the group has order \(q+1\), with weights \(t^{p^i}\), \(0\le i<2n\); the weight products are trivial exactly for pairs \((i,i+n)\) modulo \(2n\). In either case the invariant symmetric forms form an \(n\)-dimensional \(\mathbb F_p\)-space, and \(\operatorname{Tr}(cS)\) already gives all \(n\) dimensions by nondegeneracy of the trace pairing. This proves the invariant-form fact.

Consequently \(Q(x)+Q(y)+Q(z)=\operatorname{Tr}(c(x^2+y^2+z^2))\) on \(W\). Set \((x,y,z)=(t,-t,0)\) to obtain \(2Q(t)=2\operatorname{Tr}(ct^2)\), so \(Q(t)=\operatorname{Tr}(ct^2)\). Likewise, \(L(t)=\operatorname{Tr}(at)\) for some \(a\in\mathbb F_q\). This proves the asserted form of every extremizer.

**5. Converse and distinctness.** Multiplication by \(\psi(at+bt^2)\) translates the extension output by \((a,b)\), so every stated function has exactly the sixth moment of a constant, and equality follows from [1, Theorem 1.3]. If two parameter pairs define the same phase modulo a scalar, evaluating at zero removes the scalar; polarization of the remaining identity \(\operatorname{Tr}((a-a')t+(b-b')t^2)=0\) for all \(t\) forces \(b=b'\) and then \(a=a'\) by trace-pairing nondegeneracy.

## Verification
The standalone file `verify.py` uses exact arithmetic in \(\mathbb F_{25}=\mathbb F_5[z]/(z^2-2)\). It builds all unordered triple fibers, imposes only *generic* equal-product relations, and finds \(2100\) relations of rank \(20\) on \(25\) phase variables over \(\mathbb F_5\). Thus the phase space has dimension \(5=1+2\cdot2\), exactly the global phase plus the four trace-linear and trace-quadratic parameters. It also checks all \(25\) quadratic parameters, the fiber counts \(25\cdot49+600\cdot24=25^3\), and the sixth moment \(405625/25^4=649/625\). These are finite checks of the first proper-extension example; the proof above establishes all prime powers.

Run with `python verify.py` from a directory containing the file. No optional packages are required.

## Relationship to prior work
González-Riquelme and Oliveira e Silva [1] prove the sharp inequality, exhibit constant maximizers, and prove the necessity of constant modulus for every \(q=p^n\), but classify all phases for a *different* paraboloid problem only when the ambient quadratic form splits. Their Theorem 1.3 and Section 6 do not characterize sixth-moment parabolic phases. Two published studies [2,3] classify the prime-field \(n=1\) sixth-moment case. The present assertion addresses arbitrary extension degree, for which prime-field arguments alone do not exclude the many quadratic forms on the \(n\)-dimensional prime-field vector space. The rotation-invariant-form step is what excludes them. The prime-field statements are genuine overlapping special cases, not separately claimed as novel.

## Limitations
This concerns the parabola in one parameter, characteristic \(p\ge5\), and the sixth moment only. It does not extend to characteristic three, higher moments, or general curves. No independent review has been performed. The literature comparison is best-knowledge; an unlocated equivalent all-prime-power classification remains possible.

## References
[1] C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, first posted 2024-05-26, arXiv:2405.16647, especially Theorem 1.3, Proposition 3.3, and Section 6. https://arxiv.org/abs/2405.16647

[2] *Complete sixth-moment extremizers on the prime-field parabola*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-sixth-moment-extremizers-on-the-prime-field-parabola--a84363193055 .

[3] *Prime-field maximizers for the sharp finite-field parabola extension inequality*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-prime-field-maximizers-for-the-sharp-finite-field-parabola-exten--315e8b27dcb6 .
