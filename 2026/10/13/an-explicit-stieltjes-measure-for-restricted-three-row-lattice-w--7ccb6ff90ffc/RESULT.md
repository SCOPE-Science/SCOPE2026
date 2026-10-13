# An explicit Stieltjes measure for restricted three-row lattice words

## Finding

For each integer \(k\geq 0\), let \(B_k\) be the number of lattice words with exactly \(k\) occurrences of each of \(1,2,3\), satisfying the prefix inequalities \(\#1\geq\#2\geq\#3\), and with every \(1\) preceding every \(3\). The empty word gives \(B_0=1\). The known enumeration is
\[
 B_k=\binom{3k}{k}-2\binom{3k}{k-1}+\binom{3k}{k-2},
\]
where a binomial coefficient with a negative lower index is zero.

Set, for \(1/2<c<1\),
\[
 X(c)=\frac{(4c^2-1)^3}{4c^2},\qquad
 P(c)=64c^6-112c^4+44c^2+7,\qquad
 w(c)=\frac{P(c)}{4\pi c^2\sqrt{1-c^2}}.
\]
Then, **for every integer \(k\geq0\)**,
\[
 \boxed{B_k=\int_{1/2}^{1}X(c)^k w(c)\,dc.}
\]
The density \(w\) is strictly positive on \((1/2,1)\) and has total mass one. Since \(X\) is strictly increasing from \(0\) to \(27/4\), the push-forward of \(w(c)\,dc\) is a probability measure with support exactly \([0,27/4]\). Thus \((B_k)_{k\geq0}\) is a determinate Stieltjes moment sequence. More strongly, **every finite minor of its infinite Hankel matrix** \(H=(B_{i+j})_{i,j\geq0}\), with distinct increasing row and column indices, is strictly positive. This establishes the \(B\)-sequence half of Conjecture 9.5 of Shankar (2026).

## Assumptions and scope

The theorem concerns ordinary integer-valued counts for all \(k\geq0\). The variable \(c\) is real with \(1/2<c<1\). Endpoint values in the moment formula are understood as improper Lebesgue integrals; the integral converges. A *Stieltjes moment sequence* is a sequence \((m_k)_{k\geq0}\) of the form \(m_k=\int_{[0,\infty)}x^k\,d\mu(x)\) for a nonnegative measure \(\mu\). The strict Hankel-minor claim includes arbitrary finite selections of strictly increasing nonnegative row and column indices; it does not assert total positivity of unrelated matrices. No assertion is made about Shankar's separate sequence \((Q_k)_{k\geq0}\).

## Proof

**1. Established generating function.** Shankar, Theorems 6.2–6.3, proves the displayed binomial expression and the rational parametrization
\[
 T(z)=1+zT(z)^3,\quad T(0)=1,\qquad
 B(z):=\sum_{k\geq0}B_kz^k
 =\frac{T(z)(T(z)-2)^2}{3-2T(z)}.
\]
These are input identities, not new assertions. The branch \(T(0)=1\) extends analytically to \(\mathbb C\setminus[4/27,\infty)\); the sole finite branch point of this branch occurs at \(T=3/2\), \(z=4/27\). Define
\[
 F(s)=\frac{1}{s}B(1/s),\qquad R=\frac{27}{4}.
\]
Then \(F\) is analytic on \(\mathbb C\setminus[0,R]\) and \(F(s)=s^{-1}+O(s^{-2})\) at infinity.

**2. Boundary parametrization.** Parametrize \(0<x<R\) uniquely by \(c\in(1/2,1)\) through \(x=X(c)\). Put \(\phi=\arccos c\), and \(r=(4c^2-1)/(2c)\). On the upper lip of the cut for \(B(z)\), at \(z=1/x>4/27\), the analytic branch has
\[
 T_+(1/x)=r(\cos\phi+i\sin\phi)
 =u+iv,\quad
 u=2c^2-\tfrac12,\quad
 v=\frac{4c^2-1}{2c}\sqrt{1-c^2}.
\]
Indeed, inserting \(T=re^{i\phi}\) into \(z=(T-1)/T^3\) and equating imaginary parts gives \(z=\sin\phi/(r^2\sin3\phi)\); the real part gives \(r=\sin3\phi/\sin2\phi=(4c^2-1)/(2c)\). Hence \(z=4c^2/(4c^2-1)^3\). As \(c\) increases from \(1/2\) to \(1\), this gives the continuous upper branch from \(T=0\) to \(T=3/2\). The lower lip is its complex conjugate.

**3. Jump and explicit density.** A direct expansion valid for real \(u,v\) yields
\[
 \operatorname{Im}\!\left(\frac{(u+iv)(u+iv-2)^2}{3-2(u+iv)}\right)
 =\frac{v\,(-4u^3+17u^2-4uv^2-24u+5v^2+12)}{(3-2u)^2+4v^2}.
\]
Substitution from step 2 simplifies the parenthesis and denominator respectively to
\[
 \frac{P(c)}{4c^2},\qquad
 \frac{(1-c^2)(8c^2+1)}{c^2}.
\]
Because \(1/(x+i0)\) approaches the *lower* lip for \(z\), the positive candidate Stieltjes density is
\[
 h(x)=-\frac1\pi\operatorname{Im}F(x+i0)
 =\frac{cP(c)}{2\pi(4c^2-1)^2(8c^2+1)\sqrt{1-c^2}},\qquad x=X(c).
\]
The strictly positive Jacobian is
\[
 X'(c)=\frac{(4c^2-1)^2(8c^2+1)}{2c^3};
\]
therefore \(h(X(c))X'(c)=w(c)\), as claimed.

**4. All-order moment identity.** The boundary density \(h\) is integrable: near \(x=0\), \(h(x)=O(x^{-2/3})\); near \(x=R\), \(h(x)=O((R-x)^{-1/2})\). Correspondingly, \(F(s)=O(|s|^{-2/3})\) near \(s=0\), and \(F(s)=O(|s-R|^{-1/2})\) near \(s=R\). A keyhole Cauchy contour around \([0,R]\) reconstructs \(F\) from its jump: both endpoint-circle integrals vanish because their respective bounds are \(O(\varepsilon^{1/3})\) and \(O(\varepsilon^{1/2})\); the circle at infinity vanishes after dividing by \(s-\zeta\). Thus for every \(s\notin[0,R]\),
\[
 F(s)=\int_0^R\frac{h(x)}{s-x}\,dx.
\]
Expanding each side at infinity gives, coefficient by coefficient for all \(k\geq0\),
\[
 B_k=\int_0^R x^k h(x)\,dx
 =\int_{1/2}^{1}X(c)^k w(c)\,dc.
\]
The \(k=0\) identity implies total mass one (it can also be checked by integrating \(64\cos^4\phi-112\cos^2\phi+44+7\sec^2\phi\) over \([0,\pi/3]\), obtaining \(4\pi\)). The only endpoint singularities are integrable, so no endpoint atoms were omitted.

**5. Positivity, support, and every Hankel minor.** Writing \(y=c^2\in[1/4,1]\), the numerator is \(P(c)=64y^3-112y^2+44y+7\), whose derivative is \(4(4y-1)(12y-11)\). Its minimum on this interval occurs at \(y=11/12\) and equals \(68/27>0\); the endpoint values are \(12\) and \(3\). Therefore \(w>0\). The derivative \(X'>0\) makes the push-forward support the entire interval \([0,R]\). Compact support gives uniqueness of the representing probability measure.

For any \(m\geq1\), any \(0\leq i_1<\cdots<i_m\) and \(0\leq j_1<\cdots<j_m\), the continuous Cauchy–Binet/Andréief identity gives
\[
 \det[B_{i_a+j_b}]_{a,b=1}^{m}=
 \frac1{m!}\int_{(0,R)^m}
 \det[x_\ell^{i_a}]_{a,\ell=1}^{m}
 \det[x_\ell^{j_b}]_{b,\ell=1}^{m}
 \prod_{\ell=1}^{m}h(x_\ell)\,dx_\ell.
\]
For ordered, distinct positive sample points, each generalized Vandermonde determinant has the same strictly positive sign. The integrand is consequently nonnegative everywhere and strictly positive on a set of positive measure. The minor is strictly positive. This completes the proof.

## Verification

The standalone supplementary script `artifacts/verify_moments.py` uses exact symbolic identities to check the imaginary-part numerator, the trigonometric substitution, the Jacobian and the positivity polynomial; it also checks numerical moment integrals through \(k=14\) to more than 38 decimal places and confirms selected leading and shifted Hankel minors through order six. Run `python3 -m pip install -r artifacts/requirements.txt`, then `python3 artifacts/verify_moments.py`. The recorded output is `artifacts/verification_output.txt`. Finite/numerical checks are corroboration only; the universal claim follows from the contour argument and the generalized Vandermonde identity above.

## Relationship to prior work

Shankar (2026) establishes the counting sequence, its binomial formula and algebraic generating function, and explicitly conjectures Stieltjes positivity for both \(B_k\) and a different sequence \(Q_k\) (Conjecture 9.5). This result proves the \(B\)-part, not the \(Q\)-part. The same integer sequence appears as OEIS A274969, in Borie–Falque's enumeration of constrained binary-tree pairs, and in Inagaki–Pramatarova's semisymmetric-height enumeration. Those enumerations do not supply an explicit nonnegative representing measure. Górska–Penson (2013) proves moment laws for the different multidimensional Catalan sequence (which begins \(1,1,5,42\) in dimension three, versus \(1,1,4,21\) here). Bostan–Elvey Price–Guttmann–Maillard (2020) develops Stieltjes inversion for algebraic generating functions and treats Catalan/Fuss–Catalan moments; the analytic method is relevant background, but the positivity and explicit density for this distinct \(B\)-sequence require the calculations in steps 2–5.

## Limitations

The theorem does not address the separate \(Q\)-sequence from Conjecture 9.5, the real-rootedness conjecture for the descent refinements, or any additional moment sequence not identified here. The density is given by a one-variable parametrization rather than a single elementary expression in \(x\); this is sufficient to determine the unique probability measure exactly. No independent external validation is asserted.

## References

1. U. Shankar, *Avoiding patterns with three distinct letters in Canon permutations*, arXiv:2608.30002 (first public version 2026-08-30), Theorems 6.2–6.3 and Conjecture 9.5. https://arxiv.org/abs/2608.30002
2. N. Borie and J. Falque, *Product-Coproduct Prographs and Triangulations of the Sphere*, arXiv:2202.05757 (2022), Proposition 1. https://arxiv.org/abs/2202.05757
3. R. Inagaki and D. Pramatarova, *On Semisymmetric Height and a Multidimensional Generalization of Weighted Catalan Numbers*, arXiv:2604.04900 (2026), Proposition 5.6. https://arxiv.org/abs/2604.04900
4. A. Bostan, A. Elvey Price, A. J. Guttmann and J.-M. Maillard, *Stieltjes moment sequences for pattern-avoiding permutations*, Electron. J. Combin. 27 (2020), Paper P4.20; arXiv:2001.00393, §§2.1–2.5. https://arxiv.org/abs/2001.00393
5. K. Górska and K. A. Penson, *Multidimensional Catalan and related numbers as Hausdorff moments*, Probab. Math. Statist. 33 (2013), 265–274; arXiv:1304.6008. https://arxiv.org/abs/1304.6008
6. OEIS Foundation, A274969, *Number of walks in the first quadrant...*, https://oeis.org/A274969 (accessed 2026-10-09).
