# Pole rigidity and a sharp angular subalgebra boundary for Gaussian Fock Toeplitz dilations

## Finding

Write \(\mathcal F^2\) for the standard Gaussian Bargmann–Fock Hilbert space on \(\mathbb C\). For \(|\lambda|\leq1\), write \(C_\lambda h(z)=h(\lambda z)\), and let \(\mathscr T_b=\{T_f:f\in L^\infty(\mathbb C)\}\) denote **single** Toeplitz operators with bounded measurable symbols, not their generated operator algebra.

**Finite-sum rigidity.** Let \(\lambda_1,\ldots,\lambda_m\) be distinct complex numbers in the closed unit disk and let every \(c_j\ne0\). The bounded operator
\[
A=\sum_{j=1}^{m}c_jC_{\lambda_j}
\]
belongs to \(\mathscr T_b\) if and only if neither of the following obstructions occurs:

1. A parameter \(\lambda_j=0\) is present.
2. A nonzero parameter violates \(\Re\lambda_j\ge |\lambda_j|^2\).

When these conditions hold, the representing bounded symbol is unique almost everywhere and is explicitly
\[
f(z)=\sum_{j=1}^{m}\frac{c_j}{\lambda_j}
\exp\left[\left(1-\frac1{\lambda_j}\right)|z|^2\right].
\]
In particular, coefficients attached to **distinct** forbidden parameters cannot cancel each other into a bounded-symbol Toeplitz operator.

**Angular polynomial calculus.** Fix \(0<r<1\), \(\theta\in\mathbb R\), and \(\lambda=re^{i\theta}\). For a polynomial \(P(t)=\sum_{n=0}^{N}a_nt^n\), the operator \(P(C_\lambda)\) belongs to \(\mathscr T_b\) precisely when
\[
\forall n\in\{1,\ldots,N\}:\quad a_n\ne0\implies\cos(n\theta)\ge r^n.
\]
(The constant coefficient is unrestricted.) Let \(\mathscr G_{r,\theta}=\{n\ge0:\cos(n\theta)\ge r^n\}\). If \(\theta/(2\pi)\) is irrational, this set has natural density \(1/2\). If \(\theta/(2\pi)=p/q\) in lowest terms, its natural density is
\[
\frac{1+2\lfloor(q-1)/4\rfloor}{q}.
\]
Moreover the linear space \(\mathbb C[C_\lambda]\cap\mathscr T_b\) is closed under operator multiplication **if and only if** the angular rotation has finite order \(q\in\{1,2,3,4\}\). For every other angle, there exists a positive integer \(n\) such that \(C_\lambda^n\in\mathscr T_b\) but \(C_\lambda^{2n}\notin\mathscr T_b\). The last claim holds for every \(0<r<1\), with no small-radius assumption.

## Assumptions and scope

Normalize
\[
\|h\|_{\mathcal F^2}^2=\frac1\pi\int_{\mathbb C}|h(z)|^2e^{-|z|^2}\,dA(z),
\qquad e_k(z)=\frac{z^k}{\sqrt{k!}}\quad(k\ge0).
\]
The Toeplitz operator is \(T_fh=P(fh)\), with \(P\) the orthogonal Fock projection and \(f\in L^\infty(\mathbb C)\). The finite-sum theorem allows arbitrary complex nonzero coefficients, distinct parameters in \(|\lambda|\le1\), and includes the boundary \(|\lambda|=1\). The angular conclusions require a **strict** contraction \(0<r<1\); no statement about infinite series of dilation operators is made. The symbol is bounded, not required continuous or positive. The finite-rank operator \(C_0\) and the zero operator are different: the former has no bounded Toeplitz symbol, while the latter has symbol zero.

## Proof

**1. Diagonal moments and an analytic half-plane.** Each \(C_\lambda\) is diagonal in \((e_k)\), with \(C_\lambda e_k=\lambda^k e_k\) (also \(0^0=1\) by the operator's action on constants). Thus
\[
\langle Ae_k,e_k\rangle=\sum_{j=1}^mc_j\lambda_j^k.
\]
Suppose \(A=T_f\) with \(\|f\|_\infty<\infty\). Its radial angular mean
\[
h(t)=\frac1{2\pi}\int_0^{2\pi}f(\sqrt t\,e^{i\phi})\,d\phi
\]
is measurable and bounded for almost every \(t>0\). Polar coordinates give the **exact** identities
\[
\langle T_fe_k,e_k\rangle
=\frac1{k!}\int_0^\infty h(t)e^{-t}t^k\,dt
\qquad(k\ge0).
\]
Consequently
\[
F(z)=\int_0^\infty h(t)e^{-(1-z)t}\,dt
\]
is holomorphic on \(\{\Re z<1\}\) and, by dominated expansion for \(|z|<1\), satisfies
\[
F(z)=\sum_{k\ge0}\langle Ae_k,e_k\rangle z^k
=\sum_{j=1}^m\frac{c_j}{1-\lambda_jz}.
\tag{1}
\]
The finite rational function on the right is initially analytic on \(|z|<1\). By the identity theorem it must agree with \(F\) on the connected left half-plane with its finitely many candidate poles removed. At a nonzero parameter \(\lambda_j\), the candidate pole is \(z=1/\lambda_j\), with nonzero residue \(-c_j/\lambda_j\), because the parameters are distinct. Holomorphy of \(F\) excludes any such pole in \(\Re z<1\). Hence
\[
\Re(1/\lambda_j)\ge1
\quad\Longleftrightarrow\quad
\Re\lambda_j\ge|\lambda_j|^2.
\tag{2}
\]
Also \(|F(-R)|\le\|h\|_\infty/(1+R)\to0\) as \(R\to+\infty\). After excluding all interior poles, the rational expression in (1) tends along this ray to the coefficient of \(\lambda_j=0\), if present. That coefficient must therefore vanish, contrary to the nonzero-coefficient hypothesis. This proves necessity, including the zero-parameter boundary.

**2. Exact sufficiency and uniqueness.** For every nonzero \(\lambda\) satisfying (2), define
\[
f_\lambda(z)=\lambda^{-1}\exp[(1-\lambda^{-1})|z|^2].
\]
Since \(\Re(1/\lambda)\ge1\), \(f_\lambda\) is bounded. Its Toeplitz matrix is diagonal by angular integration. Its \(k\)-th diagonal element is
\[
\frac1{\lambda k!}\int_0^\infty
 e^{-t/\lambda}t^k\,dt=\lambda^k,
\]
where the complex Gamma integral applies because \(\Re(1/\lambda)>0\). Thus \(T_{f_\lambda}=C_\lambda\). Summing gives the stated symbol for \(A\). For uniqueness, \(T_f=0\) implies its Berezin transform \(\pi^{-1}f*e^{-|\cdot|^2}=0\). A bounded function is a tempered distribution, and the Gaussian Fourier multiplier is smooth and nowhere zero, so the convolution is injective (local division in distribution space). Therefore \(f=0\) almost everywhere. This also agrees with the uniqueness theorem of Lin–Lu–Zu.

**3. Polynomial powers and densities.** For \(0<|\lambda|=r<1\), the numbers \(\lambda^n\) for \(n\ge0\) are distinct and \(C_\lambda^n=C_{\lambda^n}\). Apply Steps 1–2 with the nonzero coefficients of \(P\): the condition on index \(n\ge1\) is exactly \(\Re\lambda^n\ge|\lambda|^{2n}\), or \(\cos(n\theta)\ge r^n\). Index zero corresponds to the identity and always qualifies.

For irrational \(\theta/(2\pi)\), the phases \(n\theta\pmod{2\pi}\) are equidistributed. The inclusion for all sufficiently large \(n\), for any \(\varepsilon>0\),
\[
\{n:\cos(n\theta)\ge\varepsilon\}
\subseteq\mathscr G_{r,\theta}
\subseteq\{n:\cos(n\theta)\ge0\}
\]
yields density \(1/2\) on letting \(\varepsilon\downarrow0\). For \(\theta/(2\pi)=p/q\) reduced, multiplication by \(p\) permutes the \(q\) residue phases. Exactly the residues with strictly positive cosine are eventually admissible; zero-cosine residues never are, because \(r^n>0\). Counting the integers \(j\in\{0,\ldots,q-1\}\) with \(j/q\in[0,1/4)\cup(3/4,1)\) gives \(1+2\lfloor(q-1)/4\rfloor\) admissible residues, proving the density formula.

**4. Exact multiplicative-closure boundary.** If \(\theta/(2\pi)\) has reduced denominator \(q\in\{1,2,3,4\}\), \(\cos(n\theta)>0\) holds exactly when \(q\mid n\). Indeed, every other residue has cosine zero or negative. Hence \(\mathscr G_{r,\theta}=q\mathbb N_0\), and
\[
\mathbb C[C_\lambda]\cap\mathscr T_b
=\operatorname{span}_{\mathrm{finite}}
\{C_{\lambda^{qj}}:j\ge0\},
\]
which is multiplicatively closed.

If \(\theta/(2\pi)\) is irrational, choose infinitely many large \(n\) for which \(n\theta\pmod{2\pi}\) belongs to a fixed closed subinterval of \((\pi/4,\pi/2)\). On this interval \(\cos(n\theta)\) is uniformly positive while \(\cos(2n\theta)<0\). Since \(r^n\to0\), a sufficiently large such \(n\) belongs to \(\mathscr G_{r,\theta}\) but \(2n\) does not.

If the reduced denominator is \(q\ge5\), choose an integer \(j\) with \(q/8\le j<q/4\) (such an integer exists for every \(q\ge5\)). Since \(p\) is invertible modulo \(q\), infinitely many \(n\) satisfy \(pn\equiv j\pmod q\). Their phase has positive cosine and doubled phase has nonpositive cosine. For sufficiently large \(n\), again \(n\in\mathscr G_{r,\theta}\) and \(2n\notin\mathscr G_{r,\theta}\). Thus an admissible monomial \(C_\lambda^n\) has an inadmissible square, proving that the intersection is not an algebra. All alternatives are exhaustive.

## Verification

The proof is infinite-dimensional and analytic; finite computations are supplementary. The included standalone `check.py` (Python 3 with `mpmath`) numerically tests complex Gaussian moment identities, forbidden pole positions, rational angle residue counts for denominators from 1 through 128, eventual admissibility patterns and square-instability witnesses. It passed 49,830 diagnostics from the packaged source. The mathematical argument does not infer holomorphy, density or infinite semigroup claims from these finite tests.

An explicit witness is \(\lambda=\frac15 e^{2\pi i/5}\): since \(\cos(2\pi/5)>1/5\), \(C_\lambda\in\mathscr T_b\), while \(\cos(4\pi/5)<0\) gives \(C_\lambda^2\notin\mathscr T_b\). Here the admissible-power density is \(3/5\).

## Relationship to prior work

Lin, Lu and Zu (arXiv:2607.04102, first posted July 5, 2026) prove a general Fourier recognition criterion for bounded-symbol Toeplitz operators and characterize a **single** weighted composition operator; their disk condition \(\Re\lambda\ge|\lambda|^2\) is an established input. The present claim is not that disk condition: it proves a no-cancellation characterization for arbitrary **finite sums of distinct** dilation compositions, including the zero-parameter obstruction, and determines all Toeplitz polynomials, their angular densities and the sharp order-four algebra boundary. The proof uses a distinct rational-pole obstruction in a Laplace half-plane.

Bauer, Fulsche and Rodriguez Rodriguez (arXiv:2405.20792, 2024) distinguish membership in the generated Fock–Toeplitz \(C^*\)-algebra from representability as **one** Toeplitz operator with bounded symbol. Their treatment of differences of weighted composition operators concerns algebra membership, not the finite-sum bounded-symbol criterion here. Choe, Izuchi and Koo (2010) treat boundedness, compactness and Schatten properties of linear sums of two Fock composition operators, and Pham Viet Hai (2021/2022) treats symmetry of finite sums; neither accessible statement provides this bounded-symbol rigidity or the power-semigroup classification. The latter two full texts were not accessible for independent inspection, so an undiscovered equivalent formulation remains a priority risk.

## Limitations

This is a one-variable standard Gaussian Fock-space theorem for finite sums of **centered** composition dilations, and a polynomial functional calculus for one strict contraction. It does not assert finite-sum rigidity for affine translations or nonconstant entire weights, for infinite series, or for unbounded Toeplitz symbols. The density statements are asymptotic and do not supply a uniform discrepancy rate for irrational angles. A general Fourier recognition theorem logically provides a method for testing these operators, so the originality claim is limited to the explicit finite-sum classification and its arithmetic operator-product phase transition, not to invention of Toeplitz recognition. Independent publication-priority assessment has not been performed.

## References

1. Z. Lin, Y. Lu and C. Zu, *A Fourier Criterion for Recognizing Toeplitz Operators on Fock Spaces*, arXiv:2607.04102 (first public version, July 5, 2026), especially Theorems 1.1 and 1.2 and §3.1.
2. W. Bauer, R. Fulsche and M. A. Rodriguez Rodriguez, *Operators in the Fock-Toeplitz Algebra*, arXiv:2405.20792 (2024), especially §3.3, Theorem 3.12 and Corollary 3.15.
3. B. R. Choe, K. H. Izuchi and H. Koo, *Linear sums of two composition operators on the Fock space*, J. Math. Anal. Appl. 369 (2010), 112–119, DOI:10.1016/j.jmaa.2010.02.029 (abstract and bibliographic record inspected).
4. P. V. Hai, *Finite sum of composition operators on Fock space*, Bull. Aust. Math. Soc. 106 (2022), 151–162, DOI:10.1017/S0004972721000988 (abstract and bibliographic record inspected).
