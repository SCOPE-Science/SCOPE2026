# Sharp fourth-moment Fourier extension and complete extremizers for square-zero local hyperbolas

## Finding

Let \(R\) be a finite commutative local ring, with maximal ideal \(\mathfrak m\neq\{0\}\), satisfying \(\mathfrak m^2=0\), and having a residue field \(F=R/\mathfrak m\) of odd cardinality \(q\ge3\). Write \(Q=|\mathfrak m|\) and \(U=R^\times\). On the inverse graph
\[
H_R=\{(x,x^{-1}):x\in U\}\subset R^2
\]
define the unnormalized extension operator for any complex function \(f:U\to\mathbb C\) by
\[
\mathcal T_R f(\gamma)=\sum_{x\in U}f(x)\,\gamma(x,x^{-1}),
\qquad \gamma\in\widehat{(R,+)^2}.
\]
Equip the character group with probability measure and \(U\) with counting measure. Then the **sharp fourth-power extension inequality** is
\[
\boxed{\frac1{|R|^2}\sum_{\gamma\in\widehat{R^2}}
|\mathcal T_Rf(\gamma)|^4\le
\frac{3Q}{2}\left(\sum_{x\in U}|f(x)|^2\right)^2.}
\]
Consequently \(\|\mathcal T_R\|_{\ell^2(U)\to L^4(\widehat{R^2})}=(3Q/2)^{1/4}\).

Every nonzero extremizer, and no other, is obtained as follows. Pick a residue class \(a\in F^\times\) **up to replacing \(a\) by \(-a\)**, a lift \(u\in R^\times\) of \(a\), an additive character \(\psi\in\widehat{(\mathfrak m,+)}\), and nonzero complex numbers \(A,B\) with \(|A|=|B|\). Put
\[
\boxed{f(u+v)=A\psi(v),\qquad f(-u+v)=B\psi(v)
\quad(v\in\mathfrak m),}
\]
and set \(f\) to zero on all other unit residue classes. For fixed opposite residue classes, the two displayed fibers are disjoint because the residue characteristic is odd. Up to nonzero complex scaling, the extremizer set is a disjoint union of \(Q(q-1)/2\) circles, parameterized by an opposite residue pair, a radical character, and one relative phase.

There is also an **exact global nonnegative deficit identity**, displaying separately radical Fourier dispersion, antipodal-mass imbalance, and leakage across distinct opposite residue pairs. It is stated below; in particular this result is not merely a constant-input energy computation.

## Assumptions and scope

All statements hold for every such finite commutative local ring, not only for split dual-number algebras. Since \(\mathfrak m^2=0\), the additive ideal \(\mathfrak m\) is an \(F\)-vector space: every lift of \(a\in F\) induces the same multiplication on \(\mathfrak m\). Thus \(Q=q^d\) for some integer \(d\ge1\). The theorem includes both \(\mathbb F_q[\varepsilon_1,\ldots,\varepsilon_d]/(\varepsilon_i\varepsilon_j)\) and \(\mathbb Z/p^2\mathbb Z\) for odd prime \(p\). No coefficient field inside \(R\) is assumed.

Select one representative \(a\) of each pair \(\{a,-a\}\subset F^\times\), and choose its unit lift \(u_a\); use \(-u_a\) as the lift of \(-a\). Call the set of pairs \(I\). For either signed residue \(c\) define the function \(f_c:\mathfrak m\to\mathbb C\) by writing \(f_c(v)=f(u_c+v)\), where \(u_{-a}=-u_a\). Let convolution on the additive group \(\mathfrak m\) be unnormalized, and set
\[
B_c=\|f_c\|_2^2,\qquad
P_a=f_a*f_{-a},\qquad t_a=B_a+B_{-a},\qquad
T=\sum_{a\in I}t_a=\sum_{x\in U}|f(x)|^2.
\]
Each \(f_c\) is indexed by the chosen representative, rather than by an abstract field element independent of this choice. In the formulas, \(a<b\) denotes any fixed total order on \(I\). Set
\[
\mathcal M(f)=|R|^{-2}\sum_\gamma|\mathcal T_R f(\gamma)|^4,
\quad D_c=QB_c^2-\|f_c*f_c\|_2^2,
\quad X_a=QB_aB_{-a}-\|P_a\|_2^2.
\]
With \(\operatorname{Re}\) denoting the real part, the **exact deficit** is
\[
\boxed{\begin{aligned}
\frac{3Q}{2}T^2-\mathcal M(f)
={}&\sum_{a\in I}\bigg[D_a+D_{-a}+4X_a
+\frac Q2(B_a-B_{-a})^2\bigg]\\
&+\sum_{\substack{a,b\in I\\a<b}}
\bigg[(3Q-6)t_at_b
+8\Big(\frac{t_at_b}{4}-\operatorname{Re}\big(P_a(0)\overline{P_b(0)}\big)\Big)\bigg].
\end{aligned}}\tag{1}
\]
**Every displayed term is nonnegative.** Here \(D_c\ge0\) and \(X_a\ge0\) by Young's or Fourier convolution inequality; \(Q\ge3\); and \(|P_a(0)|\le\sqrt{B_aB_{-a}}\le t_a/2\).

## Proof

**1. Nilpotent coordinates and separated residue pairs.** For \(v\in\mathfrak m\), the square-zero hypothesis yields
\[
(u_a+v)^{-1}=u_a^{-1}-a^{-2}v.
\]
The scalar \(a^{-2}\) is well-defined as an endomorphism of the \(F\)-vector space \(\mathfrak m\). Character orthogonality on the finite additive group \(R^2\) therefore gives
\[
\mathcal M(f)=\sum_{(s,z)\in R^2}
\left|\sum_{\substack{x,y\in U\\x+y=s,\ x^{-1}+y^{-1}=z}}f(x)f(y)\right|^2.
\tag{2}
\]
In the residue field, the unordered pair \(\{a,b\}\subset F^\times\) is uniquely determined by the residue sums \(s_0=a+b\) and \(z_0=a^{-1}+b^{-1}\), **unless** \(b=-a\). Indeed, when \(s_0\neq0\), one has \(z_0=s_0/(ab)\neq0\) and \(a,b\) are the roots, with multiplicities, of \(X^2-s_0X+s_0/z_0\). When \(s_0=0\), necessarily \(z_0=0\), and all antipodal pairs share the same residue sum. Hence no different non-antipodal unordered residue pairs can have the same output in (2).

For two distinct, non-antipodal residues \(a,b\), the nilpotent-coordinate part of the map in (2) sends \((v,w)\in\mathfrak m^2\) to
\[
(v+w,-a^{-2}v-b^{-2}w).
\]
Its determinant is a nonzero scalar because \(a^2\ne b^2\), so the map is bijective. Each unordered residue pair of this kind consequently contributes exactly \(4B_aB_b\). For a repeated residue \(a=a\), the map depends only on \(v+w\), and its contribution is \(\|f_a*f_a\|_2^2\).

For an antipodal residue pair \(\{a,-a\}\), the image of nilpotent parameters depends on \(s=v+w\) and has second coordinate \(-a^{-2}s\). Distinct antipodal pairs have distinct outputs for \(s\ne0\), since their squared residues differ. At \(s=0\), all antipodal pairs meet at the same actual output \((0,0)\); their amplitudes, rather than their squared moduli, must be summed first. Thus the full **exact pair-sum identity** is
\[
\begin{aligned}
\mathcal M(f)={}&\sum_{c\in F^\times}\|f_c*f_c\|_2^2
+4\sum_{\substack{\{c,d\}\subset F^\times\\c\ne\pm d}}B_cB_d\\
&+4\sum_{a\in I}\sum_{s\in\mathfrak m\setminus\{0\}}|P_a(s)|^2
+4\left|\sum_{a\in I}P_a(0)\right|^2.
\end{aligned}\tag{3}
\]
The middle unordered-pair notation means each pair of *different* non-antipodal residue classes is counted once. It is equivalent to \(4\sum_{a<b\in I}t_at_b\). In particular, after expanding the final squared modulus,
\[
\mathcal M(f)=\sum_{a\in I}\big(\|f_a*f_a\|_2^2
+\|f_{-a}*f_{-a}\|_2^2+4\|P_a\|_2^2\big)
+4\sum_{a<b}t_at_b
+8\sum_{a<b}\operatorname{Re}(P_a(0)\overline{P_b(0)}).
\tag{4}
\]

**2. Exact deficit algebra.** Expand \((3Q/2)(\sum t_a)^2\) and subtract (4). For a single opposite pair, the difference is
\[
\frac{3Q}{2}t_a^2-
\big(\|f_a*f_a\|_2^2+\|f_{-a}*f_{-a}\|_2^2+4\|P_a\|_2^2\big)
=D_a+D_{-a}+4X_a+\frac Q2(B_a-B_{-a})^2.
\]
For two different opposite pairs \(a,b\), the cross difference is
\[
3Qt_at_b-4t_at_b-8\operatorname{Re}(P_a(0)\overline{P_b(0)})
=(3Q-6)t_at_b+8\left(\frac{t_at_b}{4}-\operatorname{Re}(P_a(0)\overline{P_b(0)})\right).
\]
This proves (1) as an **identity for every complex input**, independently of any inequalities.

**3. Positivity, sharpness, and every equality case.** For functions \(g,h\) on the additive group of order \(Q\), unnormalized Fourier diagonalization of convolution and Parseval give
\[
\|g*h\|_2^2=\frac1Q\sum_{\xi\in\widehat{\mathfrak m}}
|\widehat g(\xi)|^2|\widehat h(\xi)|^2
\le Q\|g\|_2^2\|h\|_2^2.
\tag{5}
\]
Moreover, when \(g\ne0\), equality in the self-convolution case \(g=h\) holds if and only if \(g\) is a nonzero scalar multiple of a single additive character of \(\mathfrak m\). This follows because the nonnegative Fourier coefficient weights have maximal fourth-to-second-power ratio only when exactly one is nonzero.

All terms on the right of (1) are nonnegative: (5) gives \(D_c,X_a\ge0\); \(Q\ge3\) gives \(3Q-6>0\); and Cauchy--Schwarz and arithmetic--geometric mean give \(|P_a(0)|\le\sqrt{B_aB_{-a}}\le t_a/2\). Thus the sharp inequality holds.

Suppose a nonzero \(f\) gives equality. Since \(3Q-6>0\), one and only one \(t_a\) is positive: the function is supported on exactly one pair of antipodal residue fibers. Its remaining deficit forces \(B_a=B_{-a}>0\) and \(D_a=D_{-a}=X_a=0\). By the equality statement after (5), \(f_a=A\psi\) and \(f_{-a}=B\phi\) for radical characters \(\psi,\phi\), with equal coefficient moduli. Their convolution is zero unless \(\psi=\phi\); because \(X_a=0\) and both norms are positive, the characters must agree. These are exactly the stated extremizers. Conversely, their only nonzero convolution fibers have the optimal size and all terms in (1) vanish, so the constant is attained. Finally, there are \((q-1)/2\) choices of opposite residue pair, \(Q\) radical characters, and one free relative phase modulo overall nonzero complex scaling, giving the claimed disjoint circles.

## Verification

The standalone exact-arithmetic script `artifacts/verify.py` constructs all ordered two-sum fibers, compares the direct Gaussian-integer quartic energy against (3), and checks the sharp coefficient and equality constructions. It tests split dual-number rings for residue primes \(p\in\{3,5,7\}\), a two-generator square-zero radical over \(\mathbb F_3\), and nonsplit rings \(\mathbb Z/p^2\mathbb Z\) for \(p\in\{3,5,7\}\). For each ring it tests seven seeded Gaussian-integer coefficient vectors and an explicit equality packet. Run `python3 artifacts/verify.py` with Python 3; successful execution ends with `PASS finite exact identity and sharpness tests (not an infinite proof)`.

The proof for arbitrary finite local rings is the ring-theoretic fiber separation plus exact deficit algebra above; finite checking is corroboration, not a replacement for the general proof. The normalization uses all additive characters of \(R^2\), including the trivial one, with uniform probability measure.

## Relationship to prior work

Mockenhaupt and Tao [1] initiated the finite-field restriction method and its incidence/orthogonality approach. Iosevich, Murphy, and Pakianathan [2] studied this **same inverse-hyperbola object for finite rings**, but measured Fourier coefficients of the *fixed indicator* of the hyperbola and classified ring behavior under the square-root law. Their inspected hyperbola sections do not state a sharp variable-coefficient fourth extension norm or classify its extremizers. Such coefficient optimization cannot be inferred from the maximum magnitude of the fixed indicator transform alone.

Iosevich and Koh [3] analyzed restrictions to nondegenerate quadratic surfaces over finite **fields**, so the square-zero radical and its convolution packets are absent. Hickman and Wright [4] developed restriction and wave-packet theory over residue rings, especially the parabola; the inspected material does not state the present sharp inverse-graph theorem or its complete opposite-fiber equality classification.

A published sharp finite-field inverse-hyperbola result [5] gives a different geometric regime: over a field there is no nonzero radical, and its extremizers have equal magnitudes on *all* inverse-curve points, rather than the two-opposite-fiber localization proved here. A published sharp result for the **parabolic** graph over \(\mathbb Z/p^2\mathbb Z\) [6] has fourth-power constant \(p\) and one-residue-fiber optimizer packets. It does not imply the inverse-hyperbola constant \(3p/2\) or the coupled antipodal packets. Existing ordered two-sum multiplicity profiles do not by themselves establish a sharp quartic inequality for every complex coefficient array; the cross-fiber interference in (3) and the nonnegative deficit in (1) are decisive.

## Limitations

The result applies only to finite *commutative local* rings with nonzero square-zero maximal ideal and odd residue characteristic, and only to this inverse graph and fourth moment. It does not assert corresponding bounds for characteristic two, nonlocal rings, higher nilpotency, or other extension exponents. The finite checks are not exhaustive over all rings or all complex functions. The priority comparison inspected highly related works, but an unidentified broader local-ring restriction theorem could imply this result; independent scientific verification remains outstanding.

## References

[1] G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234, first posted 2002-04-18, https://arxiv.org/abs/math/0204234 .

[2] A. Iosevich, B. Murphy, and J. Pakianathan, *The square root law and structure of finite rings*, arXiv:1405.7657, first posted 2014-05-29, https://arxiv.org/abs/1405.7657 .

[3] A. Iosevich and D. Koh, *Extension theorems for Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505, https://arxiv.org/abs/0804.4505 .

[4] J. Hickman and J. Wright, *The Fourier restriction and Kakeya problems over rings of integers modulo \(N\)*, arXiv:1801.03176, https://arxiv.org/abs/1801.03176 .

[5] *Sharp fourth-moment extension and global deficit identity on the split finite-field hyperbola*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-moment-extension-and-global-deficit-identity-on-the--1c3c2c761f07 .

[6] *Exact parabolic Fourier deficit and extremizer rigidity over prime-square rings*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-parabolic-fourier-deficit-and-extremizer-rigidity-over-pri--227e3af3978b .
