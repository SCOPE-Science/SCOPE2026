# A missing conic point forces antipodal extinction at the sharp finite-field extension norm

## Finding

Let \(q\ge 3\) be an odd prime power, let \(\delta\in\mathbb F_q^\times\) be a nonsquare, and let
\[
C=\{(x,y)\in\mathbb F_q^2:x^2-\delta y^2=1\}.
\]
For any fixed \(w\in C\), delete that single point to form \(A=C\setminus\{w\}\). Thus \(|C|=q+1\) and \(|A|=q\). Given any nontrivial additive character \(\psi:\mathbb F_q\to\mathbb C\), define
\[
\mathcal E_A f(\xi)=\frac1q\sum_{u\in A}f(u)\psi(\xi\cdot u),\qquad \xi\in\mathbb F_q^2.
\]
For all complex-valued functions on \(A\), the optimal constant in
\[
\sum_{\xi\in\mathbb F_q^2}|\mathcal E_A f(\xi)|^4
\le C_q\left(\frac1q\sum_{u\in A}|f(u)|^2\right)^2
\]
is exactly
\[
\boxed{C_q=\begin{cases}5/3,&q=3,\\3-3/(q-1),&q\ge5.\end{cases}}
\]
If \(q\ge5\), every nonzero maximizer vanishes at the **retained antipode of the missing point**: \(f(-w)=0\). The remaining \(q-1\) coordinates split into \((q-1)/2\) opposite pairs; for arbitrary representatives \(u_1,\ldots,u_{(q-1)/2}\), every maximizer and only a maximizer has the form
\[
\boxed{f(u_j)=\lambda e^{i\theta_j},\qquad f(-u_j)=\lambda e^{-i\theta_j},\qquad f(-w)=0}
\]
with \(\lambda\in\mathbb C\setminus\{0\}\) and arbitrary real \(\theta_j\). For \(q=3\) there is a different equality law: every nonzero maximizer has equal nonzero modulus at **all three retained points**, with arbitrary phases. The zero function attains equality trivially in all cases.

## Assumptions and scope

The characteristic is odd and the quadratic form is nonsplit because \(\delta\) is a nonsquare. The theorem covers all finite fields of odd order, including nonprime orders, all choices of \(\delta\) and \(w\), and all nontrivial additive characters. The ambient-frequency fourth norm uses unnormalized counting measure; the input quadratic average and extension operator both use the divisor \(q=|A|\). No statement about other exponents, degenerate conics, or multiple deletions is made.

## Proof

Write \(Q(x,y)=x^2-\delta y^2\) and \(B((x,y),(u,v))=xu-\delta yv\). In the quadratic extension \(\mathbb F_q(\sqrt\delta)\), \(Q\) is the field norm; therefore its norm-one kernel has exactly \(q+1\) elements. Since \(\delta\) is nonsquare, \(Q(v)\ne0\) for any nonzero vector \(v\).

**Two-sum geometry.** For each \(s\ne0\), if \(u\) and \(s-u\) both lie in \(C\), subtracting the two norm equations yields \(2B(s,u)=Q(s)\). As \(s\ne0\), this is a genuine affine line in \(u\); its direction \(v\ne0\) has \(Q(v)\ne0\), so the restriction of \(Q(u)=1\) is a quadratic polynomial with nonzero leading coefficient. There are at most two intersection points. The involution \(u\mapsto s-u\) exchanges them (possibly fixing a tangent point). Hence every nonzero two-sum has a **unique unordered representation**, including the diagonal case. The only distinct unordered pairs with the same sum are the opposite pairs, all summing to zero.

Choose representatives \(u_1,\ldots,u_k\) of the full opposite pairs in \(A\), where \(k=(q-1)/2\). The sole unpaired point is \(-w\). Put
\[
\begin{gathered}
 a_j=|f(u_j)|^2,\quad b_j=|f(-u_j)|^2,\quad
 t_j=a_j+b_j,\quad z_j=f(u_j)f(-u_j),\quad v_j=|z_j|=\sqrt{a_jb_j},\\
 c=|f(-w)|^2,\qquad T=\sum_{j=1}^k t_j,\qquad S=T+c.
\end{gathered}
\]
Let \(F(s)=\sum_{u,v\in A:\,u+v=s}f(u)f(v)\) be the unnormalized ordered self-convolution. By the unique nonzero-sum geometry, every diagonal pair contributes \(|f(u)|^4\), every off-diagonal nonopposite pair contributes \(4|f(u)|^2|f(v)|^2\), and the special zero fiber contributes \(4|\sum_jz_j|^2\). Consequently, exactly
\[
\boxed{M:=\sum_s|F(s)|^2
=2S^2-\sum_jt_j^2-c^2-2\sum_jv_j^2
 +4\left|\sum_jz_j\right|^2.} \tag{1}
\]
Here the term \(-2\sum_jv_j^2\) correctly removes each opposite-pair contribution from the generic two-sum count; this exact identity covers tangent sums as well.

**Sharp optimization.** The triangle inequality and arithmetic–geometric mean give
\[
\left|\sum_jz_j\right|\le\sum_jv_j,\qquad 0\le v_j\le t_j/2.
\]
The expression \(4(\sum_jv_j)^2-2\sum_jv_j^2\) is coordinatewise nondecreasing on nonnegative vectors, since its derivative in coordinate \(j\) is \(4v_j+8\sum_{\ell\ne j}v_\ell\ge0\). Therefore its maximum subject to \(v_j\le t_j/2\) occurs when all \(v_j=t_j/2\). Substitution into (1), followed by Cauchy–Schwarz, yields
\[
M\le2S^2+T^2-c^2-\frac32\sum_jt_j^2
\le2S^2+T^2-(S-T)^2-\frac{3T^2}{2k}
=S^2+2ST-\frac{3T^2}{2k}. \tag{2}
\]
If \(S>0\), set \(\tau=T/S\in[0,1]\); then
\[
\frac M{S^2}\le1+2\tau-\frac{3\tau^2}{2k}. \tag{3}
\]
When \(k\ge2\), the right side is strictly increasing on \([0,1]\) and attains \(3-3/(2k)=3-3/(q-1)\) exactly at \(\tau=1\). Thus \(c=0\). Equality in Cauchy–Schwarz requires all \(t_j\) equal, and equality in arithmetic–geometric mean requires \(a_j=b_j\); equality in the complex triangle inequality requires all nonzero \(z_j\) to have a common phase. These conditions are precisely the displayed phase parametrization, and substituting it in (1) proves it attains equality.

When \(k=1\), the right side of (3) instead has its unique maximum \(5/3\) at \(\tau=2/3\). Equality requires \(a_1=b_1=c=S/3\), with no phase constraint because there is only one opposite pair. Conversely, all such functions attain equality.

Finally, character orthogonality on \(\mathbb F_q^2\) yields
\[
\sum_\xi|\mathcal E_A f(\xi)|^4=q^{-2}\sum_s|F(s)|^2=M/q^2.
\]
Dividing (2)–(3) by \(q^2\) gives exactly the asserted extension constants and all equality cases.

## Verification

The standalone standard-library script `verify.py` realizes prime fields and two explicit quadratic-extension fields with exact integer field arithmetic and Gaussian-integer test coefficients. It checks that \(|C|=q+1\), that each nonzero conic sum has at most one unordered representation, and that prescribed maximizers achieve the claimed exact fourth-moment identity. It also checks \(100\) deterministic random Gaussian-integer coefficient vectors at each of the seven orders \(q\in\{3,5,7,9,11,13,25\}\). It passed all these checks. To reproduce, run `python3 verify.py` from a folder containing the script. Random finite checks do not establish the theorem for untested fields; the proof above does.

## Relationship to prior work

Iosevich and Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields* (arXiv:0804.4505, Theorem 2), prove a **field-size-uniform** \(L^2\to L^4\) estimate for general nondegenerate quadratic curves. That exponent theorem neither determines the exact optimal order-dependent constant for a one-point-deleted conic nor describes its extremizers.

González-Riquelme and Oliveira e Silva, *Sharp extension inequalities on finite fields* (arXiv:2405.16647v1), develop sharp numerical constants and equality classifications for paraboloids, a hyperbolic paraboloid, and higher-dimensional cone families. Their explicit surface list does not include the punctured nonsplit planar conic. The present theorem concerns the natural one-sample deletion of a nonsplit quadratic level set and its unexpected forced extinction at the antipodal retained coordinate. The connected unpunctured and split-curve geometries alone do not entail this special sharp optimization.

The published *Small-field phase dichotomy for anisotropic sphere extremizers* treats **three-dimensional quadratic spheres** over two particular prime fields, not two-dimensional punctured norm-one conics over every odd finite field; its phase classifications do not imply this theorem.

## Limitations

The result concerns only the fourth moment of a single-punctured **anisotropic** planar conic. It gives no lower or upper bounds for other exponents or for puncturing more than one point. Nonindexed or older exact-norm calculations using another geometric or additive-combinatorial formulation could exist; searchable negative results are not a proof of novelty. Finite verifier runs are corroboration and do not independently establish the quantified infinite family. Independent mathematical auditing has not been performed.

## References

1. A. Iosevich and D. Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505v1 (first available 2008-04-28), Theorem 2. https://arxiv.org/abs/0804.4505
2. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647v1 (first available 2024-05-26). https://arxiv.org/abs/2405.16647
3. A. Iosevich, D. Koh, S. Lee, T. Pham, and C.-Y. Shen, *On restriction estimates for the zero radius sphere over finite fields*, arXiv:1806.11387. https://arxiv.org/abs/1806.11387
4. *Small-field phase dichotomy for anisotropic sphere extremizers*, published result and proof: https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-small-field-phase-dichotomy-for-anisotropic-sphere-extremizers--973050ba74a9
