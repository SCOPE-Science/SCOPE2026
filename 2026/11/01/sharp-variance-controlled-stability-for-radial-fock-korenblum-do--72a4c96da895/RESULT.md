# Sharp variance-controlled stability for radial Fock Korenblum domination

## Finding

Let \(W\) be any measurable nonnegative radial density that is nonzero on a set of positive measure and has all positive finite moments
\[
m_n=\int_0^\infty t^nW(t)\,dt,\qquad n=0,1,\ldots.
\]
On the Hilbert space of entire functions with norm \(\|g\|_W^2=\sum_{n\ge0}m_n|g_n|^2\), let \(R=\sqrt{m_1/m_0}\). Suppose nonzero \(g\) and \(f\) satisfy \(|f(z)|\le|g(z)|\) whenever \(|z|>R\), and their quotient is nonconstant. Define the rational Schur function
\[
H(w)=\frac{f(R/w)}{g(R/w)},\qquad a=H(0),\qquad
\psi(w)=\frac{H(w)-a}{w(1-\overline a H(w))}.
\]
Here \(|a|<1\). On the coefficient Hilbert completion define the contractive backward shift \(T=RB\), where \(Bg(z)=(g(z)-g(0))/z\). Let \(u\) be the unique vector
\[
u=(I+\overline a T\psi(T))^{-1}g.
\]
The **sharp, all-weight quantitative deficit bound** is
\[
\boxed{\ \|g\|_W^2-\|f\|_W^2
\ge (1-|a|^2)\,\delta_W\,
\operatorname{dist}_W(u,\mathbb Cz)^2,\qquad
\delta_W=1-\frac{m_1^2}{m_0m_2}>0.\ }
\]
The coefficient \(\delta_W\) is the largest valid one, **for every fixed weight and every fixed admissible \(a\in\mathbb D\)**. In fact, choosing any \(\eta\in\mathbb T\), the nontrivial pair
\[
g(z)=z(z+\overline a\eta R),\qquad
f(z)=z(az+\eta R)
\]
attains equality in the displayed stability bound. The result is not a claim of a best constant for a metric distance directly between \((f,g)\) and the extremizer family: it controls the intrinsic Schur-normalized state \(u\).

The constant has the variance interpretation
\[
\delta_W=\frac{\operatorname{Var}_\mu(t)}{\mathbb E_\mu[t^2]},
\qquad d\mu(t)=\frac{W(t)}{m_0}\,dt.
\]
For gamma-type Fock weights \(W(t)=t^\beta e^{-\alpha t}\), \(\beta>-1,\alpha>0\), it is exactly \(1/(\beta+2)\). For thin-ring weights \(W(t)=\mathbf1_{[1-d,1+d]}(t)\), \(0<d<1\), it is \(d^2/(3+d^2)\). Thus the sharp transverse stability coefficient degenerates quadratically for collapsing annuli, even though their Korenblum radius stays equal to one.

## Assumptions and scope

Use planar area normalized by \(1/\pi\), so that \(\|g\|_W^2=(1/\pi)\int_{\mathbb C}|g(z)|^2 W(|z|^2)\,dA(z)=\sum_nm_n|g_n|^2\). All functions in the domination statement are entire with finite norm. Exterior domination holds at **every** complex point \(|z|>R\), including points outside the support of a compactly supported weight. No monotonicity, smoothness, or strict positivity of \(W\) is required. For general \(W\), the coefficient Hilbert completion may contain non-entire elements; \(u\) is understood in this completion, and its distance is measured there.

The case \(f/g\) constant is excluded from the formulation only because its Schur residual is unnecessary: if that constant has modulus one, the norm deficit vanishes, while if it has modulus less than one the deficit is directly computable. The bound does not depend on a choice of representative for the rational quotient.

## Proof

**1. Strict moment ratios and the exact transverse shift gap.** Cauchy–Schwarz applied to the non-point-mass measure \(W(t)dt\) gives strict log-convexity \(m_n^2<m_{n-1}m_{n+1}\) for every \(n\ge1\). Consequently the ratios \(m_{n+1}/m_n\) are strictly increasing. With the orthonormal monomial basis \(e_n=z^n/\sqrt{m_n}\), the operator \(T=RB\) satisfies
\[
Te_0=0,\qquad Te_n=w_ne_{n-1},\qquad
w_n^2=\frac{m_1m_{n-1}}{m_0m_n}\quad(n\ge1).
\]
In particular \(w_1=1\), and for all \(n\ge2\), \(0<w_n^2\le w_2^2=m_1^2/(m_0m_2)=1-\delta_W<1\). Hence \(T\) is a contraction and, for every vector \(v\),
\[
\|v\|_W^2-\|Tv\|_W^2
=|\langle v,e_0\rangle|^2+\sum_{n\ge2}(1-w_n^2)|\langle v,e_n\rangle|^2
\ge\delta_W\operatorname{dist}_W(v,\mathbb Ce_1)^2.
\]
The last coefficient is optimal for the shift because equality holds for \(v=e_2\).

**2. Rational Schur realization of exterior domination.** Since \(|f/g|\le1\) outside the disk, zeros of \(g\) in that exterior are canceled by zeros of \(f\). The quotient has no poles on the boundary circle (a pole would be unbounded from the exterior) or at infinity, so its finitely many possible poles lie strictly inside \(|z|<R\). Consequently \(f/g=p/q\) is rational with \(\deg p\le\deg q=d\). Reverse the polynomials by \(P(w)=w^dp(R/w)\) and \(Q(w)=w^dq(R/w)\). Then \(H=P/Q\) is holomorphic on a neighborhood of the closed unit disk and \(|H|\le1\) there. From \(qf=pg\) and \(B^d(z^k v)=B^{d-k}v\) for \(0\le k\le d\), one has \(Q(T)f=P(T)g\). Because \(Q\) has no zeros on the closed disk, \(Q(T)\) is invertible. Thus
\[
f=H(T)g.
\]
This identity does not require polynomial multiplication to be a bounded operation on the Hilbert completion.

**3. Schur factorization of the actual deficit.** Nonconstancy of \(H\) implies \(|a|<1\) by the maximum-modulus principle. Schwarz–Pick at zero makes \(\psi\) a Schur function; it is rational and holomorphic on a neighborhood of the closed disk. Von Neumann's inequality yields \(\|\psi(T)\|\le1\). Put \(A=T\psi(T)\), which is a contraction commuting with \(T\). The Schur identity \(H(w)=(a+w\psi(w))/(1+\overline a w\psi(w))\) implies
\[
g=(I+\overline a A)u,\qquad f=(aI+A)u.
\]
Expansion of the two norms gives the **exact defect splitting**
\[
\|g\|_W^2-\|f\|_W^2
=(1-|a|^2)\left(
\|u\|_W^2-\|Tu\|_W^2
+\|Tu\|_W^2-\|\psi(T)Tu\|_W^2
\right).
\]
The second inner difference is nonnegative, since \(\psi(T)\) is a contraction. Apply the sharp shift-gap estimate of Step 1 to the first. This proves the claimed global stability estimate for **all** admissible exterior pairs, not only polynomial pairs.

**4. Optimality and examples.** For fixed \(a\in\mathbb D\) and \(\eta\in\mathbb T\), take \(g=z(z+\overline a\eta R)\) and \(f=z(az+\eta R)\). Directly,
\[
|g(z)|^2-|f(z)|^2
=(1-|a|^2)|z|^2(|z|^2-R^2),
\]
so the exterior domination holds. Here \(H(w)=(a+\eta w)/(1+\overline a\eta w)\), \(\psi\equiv\eta\), and \(u=z^2\). As \(\operatorname{dist}_W(z^2,\mathbb Cz)^2=m_2\),
\[
\|g\|_W^2-\|f\|_W^2
=(1-|a|^2)(m_2-R^2m_1)
=(1-|a|^2)\delta_Wm_2.
\]
Thus no larger constant can hold for any fixed weight or fixed \(a\). Gamma moments and the two elementary annulus moments give the stated formulas for \(\delta_W\). The variance identity follows by dividing \(m_0m_2-m_1^2\) by \(m_0m_2\).

## Verification

All infinite-dimensional assertions follow from strict Cauchy–Schwarz, rational quotient reversal, von Neumann's contraction inequality, and an exact Schur defect identity. The coefficient \(\delta_W\) is proved optimal by explicit quadratic polynomial pairs, not by approximation or numerical search. The optional standalone `CHECK.py` verifies rational moment inequalities and the optimality identity for Gaussian, gamma and compact-annular weights with exact integer or rational arithmetic, as well as independent polynomial-Möbius norm calculations. Execute using `python3 CHECK.py` with the Python standard library.

## Relationship to prior work

Wikström's September 2026 paper proves the sharp Gaussian Korenblum radius, classifies Gaussian equality, and supplies weighted-radius criteria. The later universal radial sharp-radius theorem [2] removes the monotonicity restriction for the domination inequality itself via the contractive weighted backward shift. The distinct rigidity theorem [3] classifies equality for non-increasing radial weights; its equality statement, and the known unrestricted-radial equality classification, are not claimed as new here. None of these inspected scientific statements supplies the **positive, globally sharp variance-dependent transverse gap** for the canonical Schur-normalized state. The new statement is a quantitative refinement; it is **not** another radius calculation or equality classification. The weight-dependent relative variance also quantifies degeneration toward a single-radius measure, including arbitrarily narrow annuli where qualitative sharpness remains valid.

## Limitations

The bound applies only to Hilbert (\(L^2\)) norms and exterior domination by entire functions. It does not provide a best constant for the ordinary Hilbert distance from the *pair* \((f,g)\) to the set of equality pairs, and the Schur-normalized state \(u\) depends nonlinearly on the quotient. If the quotient is constant, the Schur residual is undefined, and that case is handled separately. No claim is made for nonradial weights, bounded-annulus domination, \(L^p\) with \(p\ne2\), or a stability constant uniform over all radial weights. Other equivalent unindexed quantitative formulations remain a residual originality risk.

## References
1. Frank Wikström, *The sharp radius in Korenblum's maximum principle for the Fock space*, arXiv:2609.39622v1 (first publicly posted 2026-09-30), https://arxiv.org/abs/2609.39622.
2. *Sharp Korenblum radius for every radial entire-function \(L^2\) norm*, publicly accessible research result (2026-10-11), https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-sharp-korenblum-radius-for-every-radial-entire-function-l-2-norm--44f533b061f9/RESULT.md.
3. *Universal extremal rigidity for monotone weighted Fock Korenblum radii*, publicly accessible research result (2026-10-11), https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-universal-extremal-rigidity-for-monotone-weighted-fock-korenblum--4bcc547017ec/RESULT.md.
4. JunJie Wee and Le Hai Khoi, *Korenblum constants for various weighted Fock spaces*, Complex Variables and Elliptic Equations 68 (2023), 1385–1406, https://doi.org/10.1080/17476933.2022.2052862.
5. J. von Neumann, *Eine Spektraltheorie für allgemeine Operatoren eines unitären Raumes*, Mathematische Nachrichten 4 (1951), 258–281.
