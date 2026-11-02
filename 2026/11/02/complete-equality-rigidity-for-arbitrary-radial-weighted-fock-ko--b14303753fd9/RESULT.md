# Complete equality rigidity for arbitrary radial weighted Fock Korenblum inequalities

## Finding

**Theorem (universal equality classification).** Let \(W:[0,\infty)\to[0,\infty)\) be measurable and nonzero on a set of positive Lebesgue measure, and assume
\[
0<m_j=\int_0^\infty t^jW(t)\,dt<\infty\qquad(j=0,1,2,\ldots).
\]
For entire functions in the radial Hilbert space
\[
\|f\|_W^2=\frac1\pi\int_{\mathbb C}|f(z)|^2W(|z|^2)\,dA(z),
\qquad R=\sqrt{m_1/m_0},
\]
suppose \(|f(z)|\le|g(z)|\) at **every** point with \(|z|>R\). Then equality \(\|f\|_W=\|g\|_W\) occurs if and only if **one** of the following holds:

1. \(f=\eta g\) for some \(|\eta|=1\); or
2. there are \(c\in\mathbb C\setminus\{0\}\), \(a\in\mathbb C\), and \(\omega\in\mathbb C\) with \(|a|<1\), \(|\omega|=1\), such that
   \[
   f(z)=c(az+\omega R),\qquad
   g(z)=c(z+\overline a\,\omega R).
   \]

No monotonicity, continuity, positivity everywhere, or unbounded-support assumption is imposed on \(W\). In particular, these are **all** equality pairs for nonmonotone gamma radial weights, sharply concentrated annular weights, and arbitrary nonnegative radial densities with all moments finite.

## Assumptions and scope

Here \(dA\) is planar Lebesgue area and the factor \(1/\pi\) is part of the norm. All functions are entire on \(\mathbb C\), not merely analytic on the support of a compactly supported weight. Exterior domination is required at all points with \(|z|>R\), including points outside the weight support. The zero pair belongs to the first alternative. The second family has a nonconstant quotient, so it is disjoint from the unimodular-multiple family. The previously established sharp inequality for arbitrary radial weights is used only as contextual motivation: the proof below independently derives its contractive operator mechanism and, crucially, all its equality cases.

The assumptions imply that \(W(t)\,dt/m_0\) is a non-atomic probability distribution with nonzero variance. Orthogonality of monomials yields, for \(f(z)=\sum_{j\ge0}f_jz^j\),
\[
\|f\|_W^2=\sum_{j\ge0}m_j|f_j|^2.
\]
Work in the Hilbert completion \(\mathcal H_W\) of the polynomials in this norm, which contains each entire function of finite displayed integral norm. This removes completeness questions for compactly supported weights.

## Proof

**1. A contractive shift with a unique norm-attaining line.** Strict Cauchy–Schwarz, using the non-atomic weight measure, gives
\[
m_j^2<m_{j-1}m_{j+1}\quad(j\ge1).
\]
In the orthonormal coefficient basis \(e_j=z^j/\sqrt{m_j}\), define the coefficient backward shift \(B\sum f_jz^j=\sum f_{j+1}z^j\) and \(T=RB\). Then
\[
T e_0=0,\qquad T e_j=\tau_j e_{j-1},\qquad
\tau_j=R\sqrt{m_{j-1}/m_j}\quad(j\ge1).
\]
Strict moment log-convexity gives
\[
\tau_1=1>\tau_2>\tau_3>\cdots>0.
\]
Thus \(\|T\|=1\), \(\|Tx\|=\|x\|\) holds exactly when \(x\in\mathbb C e_1\), and the subspace \(E=\overline{\operatorname{span}}\{e_j:j\ge1}\) is invariant under \(T^*\), with
\[
\|T^*|_E\|=\tau_2<1.
\]

**2. The exterior quotient has a bounded rational functional calculus.** If \(g\equiv0\), domination makes \(f\equiv0\). Otherwise, \(h=f/g\) is a meromorphic function. Exterior domination removes all quotient poles on \(|z|>R\) and, by approach from the exterior, on \(|z|=R\). The bound \(|h(z)|\le1\) for \(|z|>R\) removes the singularity at infinity. Poles inside the disk are finite in number (a compact set cannot contain infinitely many isolated zeros of a nonzero entire function). Thus \(h\) is rational on the Riemann sphere.

Write the reduced rational quotient \(h=p/q\), where \(d=\deg q\) and \(\deg p\le d\); all roots of \(q\) satisfy \(|z|<R\). Set
\[
P(w)=w^d p(R/w),\quad Q(w)=w^d q(R/w),\quad
\Phi(w)=P(w)/Q(w)=h(R/w).
\]
The function \(\Phi\) is analytic on a neighborhood of the closed unit disk and \(|\Phi(w)|\le1\) there. The identity \(qf=pg\), followed by \(B^d\), gives
\[
Q(T)f=P(T)g.
\]
Indeed, coefficientwise \(B^d(z^k u)=B^{d-k}u\) for every \(0\le k\le d\), with no assumption that \(z^ku\) belongs to the Hilbert completion. The cancellation of the \(R\)-scaling in the reversed polynomials is exact. Since \(Q\) is zero-free on the closed disk, \(Q(T)\) is invertible; hence
\[
f=\Phi(T)g.
\]
Von Neumann's inequality for rational functions analytic near the closed unit disk gives \(\|\Phi(T)\|\le1\).

**3. Strict equality forces a disk automorphism.** Suppose \(g\ne0\), \(\|f\|=\|g\|\), and \(\Phi\) is not a unimodular constant. If \(\Phi\) is constant with modulus strictly less than one, equality is impossible; thus assume \(\Phi\) is nonconstant. Put \(a=\Phi(0)\), so \(|a|<1\). Schwarz's lemma applied after a disk automorphism defines a Schur function
\[
U(w)=\frac{\Phi(w)-a}{w(1-\overline a\Phi(w))},
\quad |U(w)|\le1\ (|w|\le1),
\]
with a removable singularity at \(w=0\). It is rational and analytic near the closed disk. The Schur identity is
\[
\Phi(w)=\frac{a+wU(w)}{1+\overline a\,wU(w)}.
\]
Set \(Y=TU(T)\). All relevant operators commute and \(\|Y\|\le1\), so
\[
\Phi(T)=(aI+Y)(I+\overline aY)^{-1}.
\]
A direct multiplication yields the **exact defect identity**
\[
I-\Phi(T)^*\Phi(T)
=(1-|a|^2)(I+\overline aY)^{-*}
(I-Y^*Y)(I+\overline aY)^{-1}.
\]
For \(v=(I+\overline aY)^{-1}g\ne0\), equality of norms therefore says \(\|Yv\|=\|v\|\). But
\[
\|Yv\|=\|T U(T)v\|\le\|U(T)v\|\le\|v\|.
\]
All inequalities are equalities. As the norm-attaining subspace of \(T\) is exactly \(\mathbb Ce_1\), it follows that \(U(T)v=ce_1\) for some \(c\ne0\). By taking the inner product with \(e_1\) and using that \(U(T)\) is a contraction, we obtain
\[
\|U(T)^*e_1\|=1.
\]
On the other hand, the \(T^*\)-invariant subspace \(E\) contains \(e_1\), and \(\|T^*|_E\|=\tau_2<1\). Rational von Neumann functional calculus, applied to the conjugate-coefficient Schur function, gives
\[
\|U(T)^*e_1\|
\le\sup_{|w|\le\tau_2}|U(w)|.
\]
If \(U\) is nonconstant, the maximum-modulus principle makes the right side strictly smaller than one; if \(U\) is a constant of modulus less than one, it is again strictly smaller than one. Consequently **\(U\equiv\omega\) with \(|\omega|=1\)**. This is the equality-rigidity step not contained in the pre-existing sharp-radius theorem.

Now \(Y=\omega T\) and \(\|Yv\|=\|v\|\) implies \(v=\gamma e_1\) for some nonzero \(\gamma\). Therefore
\[
g=(I+\overline a\omega T)v
=\gamma(e_1+\overline a\omega e_0),
\qquad
f=(aI+\omega T)v
=\gamma(ae_1+\omega e_0).
\]
Converting \(e_0=1/\sqrt{m_0}\) and \(e_1=z/\sqrt{m_1}\) gives exactly the stated linear family, with \(c=\gamma/\sqrt{m_1}\).

**4. Converse and boundary sharpness.** The unimodular multiples give immediate equality. For the linear family, direct expansion gives
\[
|g(z)|^2-|f(z)|^2
=|c|^2(1-|a|^2)(|z|^2-R^2).
\]
This is nonnegative on the specified exterior, while orthogonality and \(m_1=R^2m_0\) yield \(\|g\|_W^2-\|f\|_W^2=0\). Hence every listed pair is valid. The proof is complete.

## Verification

The analytic proof reconstructs the exact weighted shift, the strict first-to-second weight gap, the rational quotient identity, the Schur defect factorization, and the strict interior maximum-modulus step. The strict gap depends essentially on the fact that \(W(t)\,dt\) is a nondegenerate density, not a single atomic mass. A standalone exact-rational checker (`CHECK.py`) verifies the moment gap, the norm identities, and a strict higher-degree defect for two nonmonotone examples; finite tests are supplementary and are not used as infinite proofs.

## Relationship to prior work

Wikström's 30 September 2026 preprint, *The sharp radius in Korenblum's maximum principle for the Fock space*, establishes the sharp Gaussian radius and classifies equality for that Gaussian case, together with radius results for monotone radial weights. Its weighted moment-duality method does not classify equality for all measurable radial weights.

The published mathematical note *Sharp Korenblum radius for every radial entire-function \(L^2\) norm* proves the same sharp radius \(\sqrt{m_1/m_0}\) for **all** radial weights, via precisely the contraction and rational-quotient mechanism used above. Its stated limitations explicitly exclude an equality-pair classification. The distinct note *Universal extremal rigidity for monotone weighted Fock Korenblum radii* classifies the same Möbius pair forms, but **requires that the weight be non-increasing**. The present theorem removes this assumption completely, and supplies a different strict Schur-functional-calculus argument that applies to weights with interior peaks or gaps. The result is not a rephrasing of the existing all-weights radius theorem or of the monotone-only equality theorem.

Related disk Bergman work of Efraimidis, Llinares, and Vukotić treats domination on an outer annulus of the unit disk, whereas the present functions are entire and domination holds on an unbounded exterior. The 2023 weighted-Fock analysis of Wee and Le establishes radius upper bounds, not a complete equality classification.

## Limitations

No classification is claimed for weights given by a pure point-mass measure (strict moment log-convexity fails there), for nonradial weights, for \(L^p\) spaces with \(p\ne2\), for domination only on an annulus, or for functions not entire on the plane. The theorem classifies exact equality; it does not quantify near equality. The novelty assessment is relative to inspected texts and database searches; an unindexed equivalent historical result cannot be categorically excluded. Independent mathematical validation has not been performed.

## References

1. Frank Wikström, *The sharp radius in Korenblum's maximum principle for the Fock space*, arXiv:2609.39622v1, first posted 30 September 2026. https://arxiv.org/abs/2609.39622
2. *Sharp Korenblum radius for every radial entire-function \(L^2\) norm*, publicly available mathematical research note, 11 October 2026. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-korenblum-radius-for-every-radial-entire-function-l-2-norm--44f533b061f9
3. *Universal extremal rigidity for monotone weighted Fock Korenblum radii*, publicly available mathematical research note, 11 October 2026. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-universal-extremal-rigidity-for-monotone-weighted-fock-korenblum--4bcc547017ec
4. JunJie Wee and Le Hai Khoi, *Korenblum constants for various weighted Fock spaces*, Complex Variables and Elliptic Equations 68 (2023), 1385–1406, DOI: 10.1080/17476933.2022.2052862.
5. Iason Efraimidis, Adrián Llinares and Dragan Vukotić, *Korenblum's Principle for Bergman Spaces with Radial Weights*, Computational Methods and Function Theory 25 (2025), 239–250. https://doi.org/10.1007/s40315-024-00543-6
6. J. von Neumann, *Eine Spektraltheorie für allgemeine Operatoren eines unitären Raumes*, Mathematische Nachrichten 4 (1951), 258–281.
