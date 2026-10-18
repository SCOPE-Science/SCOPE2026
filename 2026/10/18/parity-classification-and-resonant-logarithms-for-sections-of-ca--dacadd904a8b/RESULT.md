# Parity classification and resonant logarithms for sections of Cartesian products of Euclidean balls

## Finding
For integers \(m,n\ge1\), let \(K=B_2^m\times B_2^n\subset\mathbb R^{m+n}\). Its parallel-hyperplane section-volume function along **every** direction is algebraic in the offset if and only if **both factors have odd dimensions**. More strongly, the cutoff-volume function \(C_K(\xi,s)=\operatorname{vol}_{m+n}\{x\in K:\xi\cdot x\le s\}\) satisfies one nonzero polynomial equation in \((\xi,s,C_K)\) on its entire natural domain if and only if \(m,n\) are both odd.

For each unit \(\xi=(\xi_1,\xi_2)\) with \(a=\|\xi_1\|>0\) and \(b=\|\xi_2\|>0\), the section profile is a finite piecewise polynomial if \(m,n\) are odd. If exactly one dimension is even, an inverse-sine term with a nonzero polynomial coefficient prevents algebraicity. If both dimensions are even, a nonzero logarithmic singularity prevents algebraicity; when \(a=b\), its usual first logarithmic coefficient can cancel, but a higher even-order logarithm necessarily remains.

In particular, products such as \(B_2^1\times B_2^3\subset\mathbb R^4\) are nonpolyhedral convex bodies with curved boundary portions and globally algebraic cutoff volume, despite their lack of smooth boundary. This distinguishes the nonsmooth case from rigidity theorems assuming smoothness.

## Assumptions and scope
Let \(B_2^k=\{x\in\mathbb R^k:\|x\|_2\le1\}\), \(\kappa_k=\pi^{k/2}/\Gamma(k/2+1)\), \(p=(m-1)/2\), and \(q=(n-1)/2\). A real-valued function of an offset is **algebraic** if it satisfies a nonzero polynomial relation with real coefficients in offset and function value on every point of its domain; it may have different algebraic branches on different subintervals. **Joint algebraicity** means a single nonzero polynomial relation with real coefficients involving all Cartesian components of the nonzero hyperplane normal, the offset, and the cutoff volume. Coefficients may contain constants such as \(\pi\).

When \(\|\xi\|=1\), write \(A_\xi(t)=\operatorname{vol}_{m+n-1}(K\cap\{\xi\cdot x=t\})\), \(a=\|\xi_1\|\), \(b=\|\xi_2\|\). For \(a,b>0\), define \(L=\max(-a,t-b)\) and \(U=\min(a,t+b)\). Fubini and the coarea formula yield
\[
A_\xi(t)=\frac{\kappa_{m-1}\kappa_{n-1}}{a^m b^n}
\int_L^U (a^2-v^2)^p\bigl(b^2-(t-v)^2\bigr)^q\,dv,
\]
with value zero when \(L\ge U\). For \(ab=0\), the profile is a constant multiple of a single-ball section \((1-t^2)^{(k-1)/2}_+\), hence algebraic for all \(m,n\).

## Proof
### 1. Convolution and odd dimensions
The pushforward of Lebesgue measure on \(B_2^m\) by the linear map \(x\mapsto\xi_1\cdot x\) has density \(\kappa_{m-1}a^{-m}(a^2-v^2)^p_+\); similarly for the second factor. Their convolution equals the displayed section profile because the full normal is a unit vector. If \(m,n\) are odd, \(p,q\) are nonnegative integers. Thus the integrand is a polynomial, and each endpoint \(L,U\) is one of the affine expressions \(-a,a,t-b,t+b\). Integration gives finitely many polynomial branches in \((a,b,t)\) multiplied by powers of \(a^{-1},b^{-1}\) and \(\kappa_{m-1}\kappa_{n-1}\). Every such branch is algebraic in \((\xi,t)\), as \(a^2=\sum_i\xi_{1i}^2\) and \(b^2=\sum_j\xi_{2j}^2\). Integration once more in the offset gives a finite collection of algebraic expressions for the cutoff volume. A product of the finitely many algebraic minimal relations, with denominators eliminated, supplies one nonzero global polynomial relation in \((\xi,s,C_K)\). Axial normals \(ab=0\) are included by continuity, or directly using the odd-dimensional ball factor. This establishes joint algebraicity.

For example, for \(m=n=3\) and the **unnormalized** linear functional \(\ell(x,y)=x_1+y_1\), its pushforward density for \(0\le t\le2\) equals
\[
\frac{\pi^2}{30}(2-t)^3(t^2+6t+4),
\]
and is even in \(t\) and zero for \(|t|\ge2\). The corresponding unit-normal hyperplane section has density \(\sqrt2\) times this expression evaluated at \(\sqrt2t\).

### 2. Exactly one even dimension
Interchange the factors if necessary so that \(p\) is a nonnegative integer and \(q=k+1/2\), with \(k\) a nonnegative integer. On the nonempty outer-overlap interval \(|a-b|<t<a+b\), set \(z=(t-a)/b\), so \(-1<z<1\). Substitution \(w=(t-v)/b\) gives
\[
A_\xi(t)=\frac{\kappa_{m-1}\kappa_{n-1}}{a^m}
\int_z^1 [a^2-(t-bw)^2]^p(1-w^2)^k\sqrt{1-w^2}\,dw.
\]
Put \(P(w,t)=[a^2-(t-bw)^2]^p(1-w^2)^k\). Integrating each monomial \(w^j\sqrt{1-w^2}\) expresses this function as the sum of an algebraic function of \(t\) and a polynomial multiple of \(\pi/2-\arcsin z\). The coefficient of this inverse-sine term is \(\pi^{-1}\int_{-1}^1P(w,t)\sqrt{1-w^2}\,dw\), multiplied by the nonzero prefactor. It is a nonzero polynomial in \(t\): its leading coefficient is \((-1)^p\pi^{-1}\int_{-1}^1(1-w^2)^{k+1/2}\,dw\ne0\). Thus the inverse-sine term cannot cancel. Its logarithmic complex continuation (equivalently, infinite additive monodromy) precludes algebraicity. In particular, the complete section profile is nonalgebraic for every oblique direction.

### 3. Both dimensions even: unequal projected radii
Now \(p,q\in\{1/2,3/2,5/2,\ldots\}\), and \(j=p+q+1=(m+n)/2\) is an integer at least two. Suppose, after interchanging factors if needed, \(a>b\) and consider the internal knot \(t_0=a-b\). Set \(\varepsilon=t-t_0\), \(u=a-v\). Near the collision of integration endpoints, the integrand has the exact form
\[
[u(2a-u)]^p[(u+\varepsilon)(2b-u-\varepsilon)]^q,
\qquad u\ge\max(0,-\varepsilon).
\]
The factor from the two nonvanishing parentheses is analytic in \((u,\varepsilon)\) near zero. Its constant term is \((2a)^p(2b)^q\). In the overlap region \(|\varepsilon|\ll u\ll1\), expand
\[
u^p(u+\varepsilon)^q
=\sum_{\ell\ge0}\binom q\ell\varepsilon^\ell u^{p+q-\ell}.
\]
The unique term of degree \(\varepsilon^j\) with exponent \(-1\) in \(u\) occurs at \(\ell=j\). Integration therefore yields a local contribution
\[
-\frac{\kappa_{m-1}\kappa_{n-1}(2a)^p(2b)^q}{a^m b^n}
\binom qj\,\varepsilon^j\log|\varepsilon|.
\]
The displayed coefficient is nonzero because \(q\) is a nonintegral half-integer. More precisely, subtracting finitely many analytic Taylor terms isolates this leading logarithmic contribution; the remaining higher-order terms cannot cancel it. Algebraic functions admit only fractional-power local expansions, never a nonzero logarithmic term, hence the section profile is not algebraic.

### 4. Equal projected radii and resonant cancellation
Suppose \(a=b=r>0\). At the interior knot \(t=0\), the two endpoint collisions contribute the same logarithmic expansion with opposite signs for odd powers of \(t\). Write
\[
C_0=\kappa_{m-1}\kappa_{n-1}\,2^{p+q}r^{p+q-m-n}.
\]
If \(j\) is even, the first surviving logarithmic term is
\[
-2C_0\binom qj\,t^j\log|t|,
\]
which has nonzero coefficient. If \(j\) is odd, those leading contributions cancel; in this case \(p\ne q\) (since equal half-integers would make \(j\) even). Expand the nonvanishing factors one order further:
\[
(2r-u)^p(2r-u-t)^q=(2r)^{p+q}
\left(1-\frac{(p+q)u+qt}{2r}+O(u^2+|ut|+t^2)\right).
\]
The two endpoint contributions to the coefficient of the **next even-order** logarithm add, giving
\[
\frac{C_0}{r}\binom qj\frac{(q-p)j}{j+1}
\,t^{j+1}\log|t|.
\]
Again this coefficient is nonzero. Consequently every oblique direction with both factor dimensions even has a nonalgebraic section profile, including the resonant case \(a=b\).

For unit normals the same conclusions follow from scaling. For unnormalized equal projected radii \(a=b=1\), the leading logarithmic coefficients are \(2\,t^2\log|t|\) for \((m,n)=(2,2)\), \(-\pi t^4\log|t|/2\) for \((2,4)\), and \(-2\pi^2 t^4\log|t|/3\) for \((4,4)\), modulo analytic terms and higher-order logarithms.

### 5. Cutoff-volume obstruction
For an arbitrary fixed nonzero normal \(\xi\), differentiation of cutoff volume with respect to offset gives \(\partial_s C_K(\xi,s)=A_{\xi/\|\xi\|}(s/\|\xi\|)/\|\xi\|\) at regular offsets. Every differentiable algebraic function has algebraic derivative on its regular branches. Therefore any of the nonalgebraic oblique section profiles just established obstructs joint polynomial algebraicity of the cutoff function. This completes both implications.

## Verification
The standalone `verify.py` uses exact symbolic integration to reproduce the \((3,3)\) polynomial section and exact generalized-binomial identities to reproduce all three logarithmic coefficients above. High-precision one-dimensional quadrature independently checks their leading asymptotic size in three cases, including the cancellation at \((2,4)\). It reports `VERIFY_OK exact_polynomial=1 exact_log_coefficients=3 numerical_log_profiles=3`. Numerical fits are diagnostic and do not prove infinite-dimensional statements or branch singularities; those are justified analytically in the proof.

## Relationship to prior work
The motivating first-public October 7, 2026 preprint of Fish, Ryabogin, Sun, and Yaskin, *On determination of convex bodies by their section functions*, studies rigidity arising from locally separable section profiles; its local-separability hypothesis entails a uniform offset interval over directions and does not assert the parity classification or the internal knots here. The full source was compared, including its rigidity conclusions and assumptions. Agranovsky's 2024 *Convex bodies with algebraic section volume functions* and Agranovsky, Boman, Koldobsky, Vassiliev, and Yaskin's 2022 survey concern smooth-boundary rigidity and broader algebraic integrability. Their stated smoothness hypotheses do not cover these nonsmooth Cartesian products. The classical convolution identity itself is standard, and no originality is claimed for that identity. The candidate contribution is the complete parity criterion together with the explicit nonalgebraic witnesses and resonant logarithmic cancellation.

## Limitations
These statements concern products of **two** Euclidean unit balls and their hyperplane section/cutoff volumes, not arbitrary products of convex bodies. Algebraic means satisfaction of a polynomial relation, not global polynomiality or real analyticity; there are branch changes at support and internal knots. The resonance expansion uses fixed dimensions and fixed positive projected radii; it does not provide parameter-uniform error bounds as radii coalesce. No general classification of all nonsmooth algebraically integrable convex bodies is asserted. Historical priority remains subject to independent expert checking, especially for unpublished or unindexed Radon-transform literature. Independent scientific audit has not been performed.

## References
- P. Fish, D. Ryabogin, Y. Sun, and V. Yaskin, *On determination of convex bodies by their section functions*, arXiv:2610.10229v1, first public October 7, 2026, https://arxiv.org/abs/2610.10229.
- M. Agranovsky, *Convex bodies with algebraic section volume functions*, arXiv:2409.19373v1, first public September 28, 2024, https://arxiv.org/abs/2409.19373.
- M. Agranovsky, J. Boman, A. Koldobsky, V. Vassiliev, and V. Yaskin, *Algebraically integrable bodies and related properties of the Radon transform*, arXiv:2212.07510, first public December 20, 2022, https://arxiv.org/abs/2212.07510.
- A. Koldobsky, A. Merkurjev, and V. Yaskin, *On polynomially integrable convex bodies*, arXiv:1702.00429, first public February 1, 2017, https://arxiv.org/abs/1702.00429.
