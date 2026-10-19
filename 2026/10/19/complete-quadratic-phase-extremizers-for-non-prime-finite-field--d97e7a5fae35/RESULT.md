# Complete quadratic-phase extremizers for non-prime finite-field parabola sixth moments

## Finding
Let \(q=p^n\) for any prime \(p\ge5\) and integer \(n\ge2\). Fix a nontrivial additive character \(\psi:\mathbb F_q\to\mathbb S^1\), and define
\[
\mathcal E_q f(x,y)=q^{-1}\sum_{t\in\mathbb F_q}f(t)\psi(xt+yt^2).
\]
The sharp inequality of González-Riquelme and Oliveira e Silva is
\[
\sum_{x,y\in\mathbb F_q}|\mathcal E_q f(x,y)|^6
\le (1+q^{-1}-q^{-2})\bigl(q^{-1}\sum_t|f(t)|^2\bigr)^3.
\]
**Complete equality classification:** every nonzero equality case, and no other, is
\[
f(t)=\lambda\psi(\alpha t+\beta t^2),\qquad
\lambda\in\mathbb C\setminus\{0\},\quad \alpha,\beta\in\mathbb F_q.
\]
There are exactly \(q^2\) distinct equality classes modulo nonzero complex scalar multiplication. The substantive extension beyond prime fields is the absence of any exotic quadratic phases on the additive vector space \(\mathbb F_p^n\).

## Assumptions and scope
The field has characteristic at least five and extension degree at least two. The target \(\mathbb F_q^2\) uses **counting** measure, the source \(\mathbb F_q\) uses normalized counting measure, and \(\psi\) is an arbitrary nontrivial additive character. The proof imports the established sharp inequality and the necessity of constant coefficient magnitude from [1, Theorem 1.3]. It does not claim a new sharp constant. All functions are complex-valued, with nonzero extremizers classified modulo arbitrary nonzero scalar multiplication.

## Proof
**1. Equality forces triple-product coherence.** For \(s,r\in\mathbb F_q\), put
\[
\mathcal F_{s,r}=\{(a,b,c)\in\mathbb F_q^3:a+b+c=s,\ a^2+b^2+c^2=r\},\quad N_{s,r}=|\mathcal F_{s,r}|,
\]
and \(C_{s,r}(f)=\sum_{(a,b,c)\in\mathcal F_{s,r}}f(a)f(b)f(c)\). Orthogonality gives exactly
\[
\sum_{x,y}|\mathcal E_qf(x,y)|^6=q^{-4}\sum_{s,r}|C_{s,r}(f)|^2.
\]
By [1, Theorem 1.3], a nonzero extremizer is of constant modulus, so after scaling write \(f=h\) with \(|h(t)|=1\). Since constants attain the sharp inequality, and \(|C_{s,r}(h)|\le N_{s,r}\) on every fiber, equality in the global moment forces equality in **every** fiberwise triangle inequality. Thus
\[
h(a)h(b)h(c)=h(a')h(b')h(c')\tag{1}
\]
whenever the two triples have equal sums and equal sums of squares, even when the fiber is nongeneric.

**2. Translated triple collisions give additive degree at most two.** Write \(h(x)=\exp(2\pi i u(x))\), \(u:\mathbb F_q\to\mathbb R/\mathbb Z\). The triples \((x,x,x+3t)\) and \((x+2t,x+2t,x-t)\) have equal first and second power sums. Equation (1) yields
\[
2u(x)+u(x+3t)-2u(x+2t)-u(x-t)=0\quad\text{in }\mathbb R/\mathbb Z.
\]
For the shift \(T_tu(x)=u(x+t)\), this is \((T_t-1)^3(T_t+1)u=0\). Set \(w=(T_t-1)^3u\). Then \(T_tw=-w\) and \(T_t^p=1\). Since \(p\) is odd, \(2w=0\) and \(T_tw=w\). The cyclic orbit sum of \(w\) is zero by telescoping, yet equals \(pw=w\) because \(2w=0\) and \(p\) is odd. Therefore \((T_t-1)^3u=0\) for every \(t\).

The binomial identity \(T_t^p=(1+(T_t-1))^p\), restricted to this cyclic degree-two module, now gives
\[
p\Delta_tu+\binom p2\Delta_t^2u=0,\quad p\Delta_t^2u=0,
\]
where \(\Delta_t=T_t-1\). As \(p\mid\binom p2\), it follows that \(p(u(t)-u(0))=0\) for every \(t\). Hence \(u(t)=u(0)+F(t)/p\pmod1\) for some \(F:\mathbb F_q\to\mathbb F_p\), and \(\Delta_t^3F=0\) for every \(t\).

For completeness, the elementary low-degree lemma used here is: if \(p\ge5\) and a function on \(\mathbb F_p^n\) has vanishing third difference in every direction, it is a total-degree-at-most-two polynomial over \(\mathbb F_p\). Indeed every affine line is a polynomial of degree at most two. Induct on \(n\); writing the last coordinate as \(v\), express the function as \(A(x)+vB(x)+v^2C(x)\) with \(A,B,C\) individually of degree at most two by induction. Restricting to the lines \((x+tw,v+t)\), the resulting polynomial in \(t\) has degree at most four, which is less than \(p\); comparison with its required degree at most two shows from the coefficients of \(t^4\) and \(t^3\) that \(C\) is constant and \(B\) is affine. Thus the total degree is at most two. Consequently
\[
F(t)=c+\ell(t)+Q(t),
\]
where \(\ell:\mathbb F_q\to\mathbb F_p\) is additive and \(Q\) is a homogeneous quadratic form on the \(n\)-dimensional \(\mathbb F_p\)-space \(\mathbb F_q\).

**3. Fiber rotations eliminate non-field-quadratic forms.** Let \(B(s,t)=Q(s+t)-Q(s)-Q(t)\) be the symmetric bilinear form. For any \(a,b\in\mathbb F_q\) with
\[a^2+ab+b^2=1,\tag{2}\]
the triples \((as,bs,-(a+b)s)\) and \((s,-s,0)\) have equal sums and sums of squares. Their phases in (1), after cancelling affine terms, give
\[
Q(as)+Q(bs)+Q((a+b)s)=2Q(s).
\]
Polarization in \(s,t\) gives \(B(as,at)+B(bs,bt)+B((a+b)s,(a+b)t)=2B(s,t)\).

The trace pairing is nondegenerate. Hence a unique \(\mathbb F_p\)-linear map \(L:\mathbb F_q\to\mathbb F_q\) satisfies \(B(s,t)=\operatorname{Tr}_{q/p}(sL(t))\), and every such map has the unique linearized-polynomial form
\[
L(t)=\sum_{j=0}^{n-1}\gamma_jt^{p^j},\qquad \gamma_j\in\mathbb F_q.
\]
Uniqueness follows because a nonzero polynomial of degree at most \(p^{n-1}<q\) cannot vanish everywhere; parameter counting then gives existence. The polarized equation and uniqueness yield
\[
\gamma_j\bigl(a^{p^j+1}+b^{p^j+1}+(a+b)^{p^j+1}-2\bigr)=0\tag{3}
\]
for every pair satisfying (2). For \(j=0\), the parenthesis is zero by (2). We prove that for every \(1\le j<n\) it is **not** identically zero on (2).

Parametrize points of (2) by
\[
a(\theta)=\frac{\theta^2-1}{\theta^2+\theta+1},\qquad
b(\theta)=\frac{-\theta(\theta+2)}{\theta^2+\theta+1},
\]
where the denominator is nonzero. This satisfies (2) identically. Clearing the denominator in the parenthesis of (3) produces a polynomial of degree at most \(2(p^j+1)\). Its formal series at \(\theta=0\) begins \(-3\theta^2\): indeed \(a=-1+\theta+\theta^2+O(\theta^3)\), \(b=-2\theta+\theta^2+O(\theta^3)\), and all terms involving \(\theta^{p^j}\) start at order at least five. Therefore the cleared polynomial is nonzero. It has at most \(2(p^j+1)\) roots, and the denominator removes at most two further parameters. For \(p\ge5\) and \(n\ge2\),
\[
2(p^{n-1}+1)+2<p^n=q.
\]
Thus there is a permitted \(\theta\in\mathbb F_q\) with nonzero parenthesis, forcing \(\gamma_j=0\). For \(n=1\), there are no such indices. Hence \(L(t)=\gamma_0t\) for all extension degrees.

Because \(p\ne2\), \(Q(t)=\tfrac12B(t,t)=\operatorname{Tr}_{q/p}(\gamma_0t^2/2)\). Any additive \(\ell\) has the form \(\operatorname{Tr}_{q/p}(\alpha t)\). Absorbing the constant into a scalar and using an arbitrary nontrivial character instead of the canonical trace character gives precisely \(h(t)=\lambda\psi(\alpha t+\beta t^2)\).

**4. Converse and count.** Multiplying the input by \(\psi(\alpha t+\beta t^2)\) translates the two output frequencies, so every displayed phase attains equality, as constants do. Distinct parameters yield distinct projective classes: if \(\operatorname{Tr}_{q/p}(\alpha t+\beta t^2)=0\) for all \(t\), odd/even separation gives \(\operatorname{Tr}(\alpha t)=0\) and \(\operatorname{Tr}(\beta t^2)=0\); trace nondegeneracy and polarization then imply \(\alpha=\beta=0\). Thus there are exactly \(q^2\) classes for every extension degree at least two.

## Verification
The standalone `phase_extremizers_verifier.py` uses exact finite-field arithmetic and modular linear elimination on every triple-moment fiber for \(q=5,7,25,49\). The verified relation ranks are respectively \(2,4,20,44\), leaving exactly \(1+2n\) degrees of freedom for the constant, linear-trace and quadratic-trace phases. All \(q^3-q^2\) noninitial fiber comparisons are evaluated for each field. It also checks \(\sum_{s,r}N_{s,r}^2=q^4+q^3-q^2\) and finds nonzero Frobenius-obstruction witnesses in both quadratic extension fields. The computation tests finite cases only; the proof for arbitrary \(q\) is Steps 1–4.

## Relationship to prior work
González-Riquelme and Oliveira e Silva [1, Theorem 1.3, §6] proved the sharp inequality for every finite field of characteristic greater than three and the necessity of constant modulus, but did not characterize the remaining phases. Two later prime-field classifications [2,3] prove that all optimizers over \(\mathbb F_p\) are quadratic chirps, with no classification over non-prime fields. The present result handles all extension degrees by eliminating the otherwise possible nonmultiplicative quadratic forms on \(\mathbb F_p^n\). No new extension bound is claimed. Published finite-field moment-curve endpoint results concern different exponents and supports.

## Limitations
The sharp constant and constant-modulus theorem are imported from [1]. The stated classification excludes characteristic two and three, and does not establish quantitative stability for near-extremizers. Finite checks are not substitutes for the uniform algebraic proof. An older equality classification indexed under additive quadratic characters or finite-field Strichartz terminology is a residual bibliographic possibility; no independent audit is claimed.

## References
[1] C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647, first publicly posted 2024-05-26, Theorem 1.3 and §6, https://arxiv.org/pdf/2405.16647.
[2] *Complete sixth-moment extremizers on the prime-field parabola*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-sixth-moment-extremizers-on-the-prime-field-parabola--a84363193055 (Theorem scope: prime fields only).
[3] *Prime-field maximizers for the sharp finite-field parabola extension inequality*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-prime-field-maximizers-for-the-sharp-finite-field-parabola-exten--315e8b27dcb6 (Theorem scope: prime fields only).
