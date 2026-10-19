# Laguerre-optimal low-frequency discrimination of chiral signed-permutation orbits

## Finding

For every integer \(n\ge1\), the smallest nonzero Fourier contrast between two mirror-related positive rotational signed-permutation orbit measures is homogeneous of degree exactly \(n^2\). Its sharp amplitude and all source/detector directions that maximize the leading coefficient are explicit: the squared coordinates are scaled zeros of the ordinary Laguerre polynomial.

Write
\[
\Delta_n(x)=\prod_{j=1}^n x_j\prod_{1\le i<j\le n}(x_j^2-x_i^2),\qquad
F_n=n!\prod_{j=1}^n(2j-1)!,\quad m=n^2.
\]
For unit vectors \(v,\omega\in\mathbb R^n\), define their mirror-orbit Fourier contrast \(D_v\) as below. Then, uniformly over all unit pairs,
\[
D_v(r\omega)=\frac{2(-2\pi i)^{m}}{F_n}\,
\Delta_n(v)\Delta_n(\omega)\,r^{m}+O_n(r^{m+2})
\qquad (r\downarrow0).
\]
The **exact sharp leading contrast** is
\[
\boxed{\lim_{r\downarrow0}r^{-n^2}\sup_{\|v\|_2=\|\omega\|_2=1}|D_v(r\omega)|=
\frac{2(2\pi)^{n^2}}{F_n}\,
\frac{n!\prod_{j=2}^n j^{2j-1}}{n^{2n^2}}.}
\]
The empty product is one. For each vector at equality, its \(n\) squared coordinates, in any order, are \(z_j/n^2\), where \(z_1<\dots<z_n\) are the positive roots of \(L_n\); every coordinate sign is free. These are all the maximizing pairs for the *leading coefficient*. This does not assert exact finite-frequency optimality.

## Assumptions and scope

Let \(W_n\) denote the orthogonal group of all signed coordinate permutations on \(\mathbb R^n\), of cardinality \(2^n n!\). Let \(G_n=\{g\in W_n:\det g=1\}\) and let \(S\in W_n\) be any element of determinant \(-1\). For \(v\in S^{n-1}\), introduce probability measures
\[
\mu_v=\frac1{|G_n|}\sum_{g\in G_n}\delta_{gv},\qquad
\mu_{Sv}=\frac1{|G_n|}\sum_{g\in G_n}\delta_{gSv}.
\]
Repeated atoms are retained in the normalized group average when \(v\) has a stabilizer. Fourier transformation uses \(\widehat\nu(\xi)=\int e^{-2\pi i\xi\cdot x}\,d\nu(x)\). The difference \(D_v=\widehat\mu_v-\widehat\mu_{Sv}\) is independent of the particular orientation-reversing \(S\) because \(G_n\) is the index-two normal subgroup. The formula covers all positive integers \(n\), including \(n=1\); it makes no assumption of genericity unless a nonzero leading term is requested.

The leading contrast is identically zero if \(\Delta_n(v)=0\): then a determinant-negative reflection fixes \(v\), and the two group-orbit measures agree. If \(\Delta_n(v)\ne0\), the stated order \(n^2\) is actually attained for every \(\omega\) with \(\Delta_n(\omega)\ne0\).

## Proof

**1. Alternating orbit sum.** Since \(W_n=G_n\sqcup G_nS\) and \(|G_n|=|W_n|/2\),
\[
D_v(\xi)=\frac2{|W_n|}\sum_{g\in W_n}\det(g)
 e^{-2\pi i\langle\xi,gv\rangle}.
\]
For every \(h\in W_n\), both \(D_{hv}(\xi)=\det(h)D_v(\xi)\) and \(D_v(h\xi)=\det(h)D_v(\xi)\) hold. In its homogeneous Taylor expansion in \(\xi\), each coefficient is therefore separately alternating in \(v\) and \(\xi\), under each individual coordinate sign flip and each coordinate interchange.

A polynomial alternating under all sign flips is divisible by \(\prod_jx_j\). Alternation under swapping coordinates then makes it divisible by \(x_j^2-x_i^2\) for every pair. Thus every nonzero alternating polynomial is divisible by \(\Delta_n(x)\), whose degree is \(n+2\binom n2=n^2\). The terms of Fourier orders below \(m=n^2\) vanish. Under \(x\mapsto-x\), an alternating polynomial has parity \((-1)^n=(-1)^m\); therefore the Fourier term of degree \(m+1\) vanishes too.

**2. Exact leading coefficient.** Let
\[
Q_m(v,\xi)=\sum_{g\in W_n}\det(g)(\xi\cdot gv)^m.
\]
Alternation and degree yield \(Q_m(v,\xi)=c\Delta_n(v)\Delta_n(\xi)\) for some \(c\). The polynomial \(\Delta_n(x)\), up to a harmless sign, is the determinant \(\det[x_i^{2j-1}]_{i,j=1}^n\). In the Fischer derivative pairing, different exponent-permutation monomials are orthogonal, giving
\[
\Delta_n(\partial_x)\Delta_n(x)
=n!\prod_{j=1}^n(2j-1)!=F_n.
\]
On the other hand,
\[
\Delta_n(\partial_\xi)Q_m(v,\xi)
=m!\sum_{g\in W_n}\det(g)\Delta_n(gv)
=m!|W_n|\Delta_n(v).
\]
Therefore \(c=m!|W_n|/F_n\). Multiplying by the Fourier Taylor factor \((-2\pi i)^m/m!\) and the orbit factor \(2/|W_n|\) proves the displayed leading term. Taylor's theorem for the exponential, together with \(|\xi\cdot gv|\le r\) on the unit spheres, makes the remainder \(O_n(r^{m+2})\) uniform. The same alternating argument excludes every order of the opposite parity.

**3. Unique maximizing squared-coordinate pattern.** Put \(a_i=x_i^2\). Within the ordered chamber \(0<a_1<\dots<a_n\), \(\sum a_i=1\),
\[
\log|\Delta_n(x)|=\tfrac12\sum_i\log a_i+
\sum_{i<j}\log(a_j-a_i).
\]
Every summand is concave, the first sum is strictly concave, and the expression tends to \(-\infty\) at each chamber boundary (for \(n=1\), the sole choice is \(a_1=1\)). Hence there is one interior global maximizer. Homogeneity shows the Lagrange multiplier is \(n^2/2\), giving
\[
\frac1{a_i}+2\sum_{j\ne i}\frac1{a_i-a_j}=n^2.
\]
For \(z_i=n^2a_i\), this becomes
\[
\frac1{z_i}+2\sum_{j\ne i}\frac1{z_i-z_j}=1.
\]
The monic polynomial \(p(z)=\prod_i(z-z_i)\) satisfies \(p''(z_i)/p'(z_i)=2\sum_{j\ne i}(z_i-z_j)^{-1}\). Thus \(zp''+(1-z)p'\) equals \(-np\): both sides agree at the \(n\) zeros, and comparison of highest coefficients fixes the polynomial identity
\[
zp''(z)+(1-z)p'(z)+np(z)=0.
\]
The unique monic polynomial solution is \(p(z)=(-1)^nn!L_n(z)\). The ordinary Laguerre polynomial has \(n\) distinct positive zeros with sum \(n^2\), so these squares do satisfy the sphere constraint. Strict chamber concavity proves uniqueness; all signs and permutations furnish exactly \(2^nn!\) maximizers.

**4. Exact maximum without uncomputed roots.** The monic Laguerre polynomial satisfies
\[
p_n(z)=(z-(2n-1))p_{n-1}(z)-(n-1)^2p_{n-2}(z),
\qquad zp_n'(z)=np_n(z)+n^2p_{n-1}(z).
\]
For \(n\ge2\), the first identity implies
\[
|\operatorname{Res}(p_n,p_{n-1})|
=(n-1)^{2(n-1)}|\operatorname{Res}(p_{n-1},p_{n-2})|
=\prod_{j=1}^{n-1}j^{2j}.
\]
At each root \(z_i\) of \(p_n\), the second identity gives \(p_n'(z_i)=n^2p_{n-1}(z_i)/z_i\). Also \(\prod_i z_i=n!\). Multiplying absolute values yields the discriminant
\[
\prod_{i<j}(z_j-z_i)^2
=\prod_i|p_n'(z_i)|
=\prod_{j=2}^n j^{2j-1}.
\]
Consequently
\[
\max_{\|x\|=1}|\Delta_n(x)|^2
=\left(\prod_i\frac{z_i}{n^2}\right)
\left(\prod_{i<j}\frac{z_j-z_i}{n^2}\right)^2
=\frac{n!\prod_{j=2}^n j^{2j-1}}{n^{2n^2}}.
\]
The asymptotic leading contrast factors into independent source and detector terms. Compactness of the product of spheres and the uniform Taylor remainder allow the supremum to pass through the scaled limit, proving both the sharp constant and the complete equality cases.

## Verification

A standalone checker enumerates all signed permutations and computes the exact first nonzero alternating moment in dimensions \(1\) through \(4\). It independently verifies the monic Laguerre discriminant and the maximum formula in those dimensions. For dimension \(3\), direct 105-digit Fourier sums at radii \(1/10\) and \(1/20\) give ratios of the actual contrast to its predicted leading term of approximately \(0.9906406113\) and \(0.9976526138\). The exact assertions for all dimensions are proved analytically above; finite computations are not used as exhaustive certificates.

For example, the dimension-three sharp source discriminant is \(\max_{\|x\|=1}|\Delta_3(x)|=4/729\); the first distinguishable Fourier moment is of order nine. The contrast coefficient is \(2(-2\pi i)^9\Delta_3(v)\Delta_3(\omega)/4320\).

To reproduce the checks, install the packages in `requirements.txt` and run `python checker.py`.

## Relationship to prior work

Klimyk and Patera's *Antisymmetric Orbit Functions* (arXiv:math-ph/0702040, §4.5) already provides the antisymmetrized type-\(B_n\) exponential orbit sum and determinant-of-sines expression. The orbit-sum representation is therefore **not** asserted to be new. Classical Weyl anti-invariants also supply the discriminant and its degree. Marcellán, Martínez-Finkelshtein and Martínez-González's 2005 electrostatic survey recounts Stieltjes' orthogonal-polynomial zero equilibrium framework; the Laguerre differential equation and discriminant recurrence are classical inputs.

The specific claim established here is the **sharp jointly optimized first distinguishable Fourier coefficient for two positive mirror-related rotational orbit measures**, together with its all-dimensional constant and exhaustive maximizing source/detector configurations. Neither of those two inspected primary sources states this joint optimization result; the proof supplies the needed link from the signed orbit contrast to the simplex maximization. Literature absence cannot certify priority: an equivalent result under Weyl denominator extremal norms or chiral multipole sensitivity would cover the claim.

## Limitations

The theorem concerns a fixed unit-radius discrete orbit pair and its small-frequency asymptotic. It does not determine the maximizing source or detector directions at any prescribed nonzero frequency, a finite-band detection optimum, or noise-stable recovery. It does not claim novelty for classical anti-invariants, antisymmetric orbit functions, Laguerre equilibrium, or Laguerre discriminants individually. Published-record searches and source inspections are not an independent or exhaustive novelty certification; older invariant-theory or diffraction literature might contain an equivalent sharp variational identity.

## References

1. A. Klimyk and J. Patera, *Antisymmetric Orbit Functions*, arXiv:math-ph/0702040 (first public 2007-02-12), especially §§3.1 and 4.5. https://arxiv.org/abs/math-ph/0702040
2. F. Marcellán, A. Martínez-Finkelshtein, and P. Martínez-González, *Electrostatic models for zeros of polynomials: old, new, and some open problems*, arXiv:math/0512293 (first public 2005-12-13), §§1–2. https://arxiv.org/abs/math/0512293
