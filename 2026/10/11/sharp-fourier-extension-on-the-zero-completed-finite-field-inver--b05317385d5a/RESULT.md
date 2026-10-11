# Sharp Fourier extension on the zero-completed finite-field inverse graph

## Finding

Let \(F=\mathbb F_q\) have characteristic \(p>3\), and let the **zero-completed inverse graph** be \(S=\{(t,h(t)):t\in F\}\), where \(h(0)=0\) and \(h(t)=t^{-1}\) for \(t\ne0\). For every nontrivial additive character \(\psi:F\to\mathbb C\), define
\[
Tf(u,v)=\sum_{t\in F}f(t)\psi(ut+vh(t)).
\]
The input uses counting-measure \(\ell^2(F)\) and the output uses uniform-probability \(L^4(F^2)\). The exact fourth power of the sharp norm has the arithmetic dichotomy
\[
\|T\|_{\ell^2\to L^4}^4=
\begin{cases}
\dfrac{3(2q-1)}{2q+1},&q\equiv2\pmod3,\\[2mm]
\dfrac{\rho^4+36\rho^2+48\rho+90}{(\rho^2+6)^2},&q\equiv1\pmod3,
\end{cases}
\]
where \(\rho>0\) is the unique positive root of \(2\rho^3+6\rho^2-3\rho-12=0\). The second value is approximately \(3.6562899693108\), independent of the field size.

All nonzero equality cases are as follows. When \(q\equiv2\pmod3\), every nonzero \(t\) satisfies \(|f(0)|^2=3|f(t)|^2/2\), and all products \(f(t)f(-t)\) have the argument of \(f(0)^2\). Conversely, every nonzero function with these properties is an extremizer.

When \(q\equiv1\pmod3\), write \(\mu_6=\{x\in F^\times:x^6=1\}\). Every extremizer has exactly the seven-point support \(\{0\}\cup a\mu_6\), for some \(a\in F^\times\). It has \(|f(0)|=\rho\alpha\) and \(|f(t)|=\alpha>0\) for \(t\in a\mu_6\). Choose \(\lambda\) with \(\lambda^2-\lambda+1=0\), hence of multiplicative order six, and multiply \(f\) by a scalar so that \(f(0)>0\). The necessary-and-sufficient phase vector along \((a,a\lambda,\ldots,a\lambda^5)\) is
\[
(u,v,v-u,-u,-v,u-v)\pmod{2\pi},\qquad u,v\in\mathbb R.
\]
Thus the arithmetic transition changes the entire extremizer geometry: from all nonzero field points to one six-point multiplicative orbit plus the origin. For \(q>7\) in the second case, the sharp extremizers are genuinely sparse.

## Assumptions and scope

The field is a prime-power field of characteristic greater than three; no primality of \(q\) is assumed. The root \(\rho\) and sharp norm are independent of the choice of nontrivial additive character. All norms, exponents, and normalizations refer to the specific spaces above. The treatment excludes characteristic two and three. No statement about the optimal stability modulus or higher Fourier moments is made.

## Proof

**1. Collision fibers and the exact identity.** Put \(c=f(0)\), \(a_t=f(t)\) for nonzero \(t\), and
\[
B=\sum_{t\ne0}|a_t|^2,\quad D=\sum_{t\ne0}|a_t|^4,\quad
H=\sum_{\{t,-t\}}a_ta_{-t},\quad
Q=\sum_{\{t,-t\}}|a_ta_{-t}|^2,
\]
where the latter sums run once over each unordered opposite pair. In the case \(q\equiv1\pmod3\), fix a root \(\lambda\) of \(\lambda^2-\lambda+1=0\) and put
\[
U=\sum_{t\ne0}a_t\overline{a_{\lambda t}a_{\lambda^{-1}t}};
\]
in the other case set \(U=0\). Character orthogonality implies the exact complex-coefficient identity
\[
\boxed{\quad
\|Tf\|_{L^4}^4
=2B^2-D-4Q+|c^2+2H|^2+4|c|^2B
+8\operatorname{Re}(cU).\quad}
\tag{1}
\]
To prove (1), expand the fourth moment as the squared \(\ell^2\)-norm of the ordered-pair convolution on \(S+S\). If \(t,u\ne0\) and \(s=t+u\ne0\), then their second-coordinate sum \(w=t^{-1}+u^{-1}=s/(tu)\) determines the unordered pair from \(s,w\). If \(s=0\), all opposite pairs contribute at output \((0,0)\), along with \((0,0)+(0,0)\), producing \(|c^2+2H|^2\). A remaining collision with a pair containing the origin is possible exactly when \(s=t+u\ne0\) and \(tu=s^2\); the two roots \(t/s,u/s\) then solve \(X^2-X+1=0\). Such roots exist exactly if \(q\equiv1\pmod3\), with solutions \(\lambda\) and \(\lambda^{-1}\); their cross term yields \(8\operatorname{Re}(cU)\). Counting the unique nonzero-sum unordered-pair fibers and the ordinary origin/nonzero fibers gives the remaining terms in (1). In particular, replacing coefficients by their absolute values cannot decrease the fourth moment, and equality of phases can be tested fiber by fiber.

**2. Nonresonant case.** Suppose \(q\equiv2\pmod3\), and first take all coefficients nonnegative. Let \(N=q-1\) and \(M=N/2\). For each opposite pair define its squared-mass sum \(s_j=b_t^2+b_{-t}^2\) and product \(p_j=b_tb_{-t}\), and let \(P=\sum_jp_j\). Then \(P\le B/2\), and Cauchy–Schwarz gives
\[
D+4Q=\sum_j(s_j^2+2p_j^2)\ge\frac{B^2+2P^2}{M}.
\]
Equation (1) is strictly increasing in \(P\) for fixed \(B,c\) on \(0\le P\le B/2\), and hence
\[
\|Tf\|_4^4\le c^4+6c^2B+
\left(3-\frac3N\right)B^2,
\]
with equality, for \(B>0\), only when all \(b_t\) for nonzero \(t\) coincide. Maximizing the last expression over \(c^2+B=1\) gives \(c^2/B=3/(2N)\) and the sharp value \(3(2q-1)/(2q+1)\). For complex coefficients, equality in the zero-sum convolution fiber forces all products \(f(t)f(-t)\) to have the argument of \(f(0)^2\), and imposes no further phases because the other nonzero-sum pair fibers are unique. This proves necessity and sufficiency.

**3. Resonant six-cycles.** Suppose \(q\equiv1\pmod3\), and again let \(c\ge0\) and \(b_t\ge0\). Partition \(F^\times\) into the orbits \(O_j=a_j\mu_6\). Put \(B_j=\sum_{t\in O_j}b_t^2\), and let \(P_j\) and \(V_j\) be respectively the sums of opposite-pair products and the sums of \(b_t^4+4b_t^2b_{-t}^2\) over the orbit (each opposite pair counted once). Set
\[
U_j=\sum_{t\in O_j}b_tb_{\lambda t}b_{\lambda^{-1}t}.
\]
For each orbit the inequalities
\[
0\le P_j\le B_j/2,\qquad
V_j\ge\frac{B_j^2+2P_j^2}{3},\qquad
U_j\le B_j^{3/2}/\sqrt6
\tag{2}
\]
hold. The final bound is sharp precisely when the six \(b_t\) on the orbit coincide (if \(B_j>0\)). To see it, split the cyclic six-tuple into even and odd vertices of squared-mass totals \(X,Y\). The three centered terms of each parity obey, by Cauchy–Schwarz and \(\sum_{i<j}x_i^2x_j^2\le(\sum_i x_i^2)^2/3\), the bounds \(X\sqrt{Y/3}\) and \(Y\sqrt{X/3}\). Their sum is at most \((X+Y)^{3/2}/\sqrt6\), with equality only at balanced uniform amplitudes.

Insert (2) in (1). For fixed \(c,B_j\), the resulting upper expression is increasing in every \(P_j\), because its corresponding derivative equals \(4c^2+8\sum_jP_j-4P_j/3\ge0\). Replacing every \(P_j\) by \(B_j/2\) gives
\[
\|Tf\|_4^4\le c^4+6c^2B+3B^2
-\frac12\sum_jB_j^2+
\frac8{\sqrt6}c\sum_jB_j^{3/2}.
\tag{3}
\]
For \(B>0\), normalize \(y=c/\sqrt B\), \(p_j=B_j/B\), and \(t=(\sum_jp_j^2)^{1/2}\in(0,1]\). Cauchy implies \(\sum_jp_j^{3/2}\le t\). With \(K=8/\sqrt6\), equation (3) yields
\[
\frac{\|Tf\|_4^4}{(c^2+B)^2}
\le\frac{y^4+6y^2+3-t^2/2+Kyt}{(1+y^2)^2}.
\tag{4}
\]
If \(0\le y\le1/K\), maximizing the quadratic over \(t\) bounds (4) by \((y^4+(34/3)y^2+3)/(1+y^2)^2\le4169/1225\). This is smaller than the explicit seven-point test at \(y=1/2\), whose ratio is \(13/5+32\sqrt6/75\). Hence no sharp extremizer lies in this regime. When \(y>1/K\), the numerator in (4) is strictly increasing for \(t\in[0,1]\), so \(t=1\) is necessary for sharpness. Since \(\sum_j p_j=1\), this forces **exactly one populated six-cycle**. For a single six-cycle the inequalities above are simultaneously sharp at six equal moduli, and the remaining one-variable ratio is
\[
F(y)=\frac{y^4+6y^2+5/2+(8/\sqrt6)y}{(1+y^2)^2}.
\]
The numerator of \((1+y^2)^3F'(y)\) is \(-8y^3+2y+(8/\sqrt6)(1-3y^2)\). It has exactly one positive root (its derivative is strictly decreasing after one initial rise), which is \(y=\rho/\sqrt6\), where \(2\rho^3+6\rho^2-3\rho-12=0\). Substitution gives the claimed sharp constant and the nonzero amplitude ratio \(\rho\).

Finally, choose the phase of \(c=f(0)\) to be zero. The exceptional fibers in (1) force \(\theta_j=\theta_{j-1}+\theta_{j+1}\pmod{2\pi}\), and the zero-sum fiber forces \(\theta_{j+3}=-\theta_j\pmod{2\pi}\). Their complete solution is the two-parameter phase vector in the finding. It saturates every convolution triangle inequality, completing the equality classification. When \(B=0\), the normalized fourth moment equals one; when \(c=0\), it is at most three. Neither boundary case is sharp.

## Verification

The standard-library checker `artifacts/verify.py` constructs prime fields and two quadratic extension fields, enumerates ordered-pair convolution fibers, compares the resulting fourth moment with (1) for 104 complex-valued test inputs, and tests 24 extremizers with nontrivial compatible phases. It also checks the cubic-root residual. It reports:

`VERIFY_OK fields=8 including F25,F49 complex_convolution_identity_tests=104 sharp_phase_extremizer_tests=24 root_residual=PASS`

Run from the package root with `python3 artifacts/verify.py`. This finite test is not a substitute for the general fiber-classification proof and inequalities (2)–(4).

## Relationship to prior work

Mockenhaupt and Tao [1] introduced a general finite-field Fourier restriction framework and its even-moment method. Iosevich and Koh [2] study quadratic-surface extension, and Koh and Shen [3] establish sharp exponent ranges for general plane algebraic curves. González-Riquelme and Oliveira e Silva [4] address sharp constants and extremizers for several different finite-field surfaces. The hyperbola \(xy=1\) is a split quadratic conic, but adjoining \((0,0)\) creates new sum-fiber collisions with a six-root arithmetic resonance; the existing sharp uncompleted-conic theorem does not determine this sharp completed-graph norm. The new result concerns the exact weighted endpoint and all equality cases for the completed inverse graph, rather than an exponent-only bound or an unweighted energy census.

## Limitations

No originality claim is made for Fourier orthogonality, even-moment convolution, or the established theory of extension on quadratic conics. An equivalent statement could exist under reciprocal-polynomial additive energy or differential-uniformity terminology; literature searches do not prove novelty. The result excludes characteristic two and three; its sharpness statement does not include a quantitative near-extremizer stability coefficient. The checker covers finitely many fields only. Independent external verification has not been performed.

## References

[1] G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234v1 (first public preprint, 2002-04-18), https://arxiv.org/abs/math/0204234.

[2] A. Iosevich and D. Koh, *Extension theorems for Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505v1 (2008-04-28), https://arxiv.org/abs/0804.4505.

[3] D. Koh and C.-Y. Shen, *Sharp extension theorems and Falconer distance problems for algebraic curves in two dimensional vector spaces over finite fields*, arXiv:1003.4240v1 (2010-03-22), https://arxiv.org/abs/1003.4240.

[4] C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647v1 (2024-05-26), https://arxiv.org/abs/2405.16647.
