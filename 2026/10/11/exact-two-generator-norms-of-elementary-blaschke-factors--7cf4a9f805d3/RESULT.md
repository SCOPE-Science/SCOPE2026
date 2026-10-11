# Exact two-generator norms of elementary Blaschke factors

## Finding

Let \(A(\mathbb D)\) be the complex disk algebra with its supremum norm, and for \(a\in\mathbb D\) write \(b_a(z)=(z-a)/(1-\overline a z)\). For any \(a,b\in\mathbb D\), put
\[
\delta=\left|\frac{b-a}{1-\overline a b}\right|,\qquad
\omega=\frac{1-a\overline b}{1-\overline a b},\qquad
\alpha=2\arcsin\delta.
\]
Here \(0\le\delta<1\), \(|\omega|=1\), and \(0\le\alpha<\pi\). For any nonzero \(u,v\in\mathbb C\), set \(\tau=|\operatorname{Arg}(u\omega\overline v)|\in[0,\pi]\), with principal argument. Then the **entire two-generator norm** is
\[
\boxed{\ \|u b_a+v b_b\|_{A(\mathbb D)}^2
=|u|^2+|v|^2+2|u||v|\cos\bigl(\max\{0,\tau-\alpha\}\bigr).\ }
\]
If either coefficient is zero, the norm is the absolute value of the remaining coefficient. This formula also includes the degenerate case \(a=b\).

The **unique best scalar approximation** of \(b_a\) by a multiple of \(b_b\) has coefficient
\[
\boxed{\ \lambda_*=\omega\max\{1-2\delta^2,0\}.\ }
\]
Its distance is
\[
\boxed{\ \operatorname{dist}_{A(\mathbb D)}(b_a,\mathbb C b_b)=
\begin{cases}
2\delta\sqrt{1-\delta^2},&0\le\delta\le1/\sqrt2,\\
1,&1/\sqrt2\le\delta<1.
\end{cases}\ }
\]
In particular, Birkhoff--James orthogonality satisfies the sharp symmetric criterion
\[
\boxed{\ b_a\perp_B b_b\ \Longleftrightarrow\ b_b\perp_B b_a\ \Longleftrightarrow\ \delta\ge1/\sqrt2.\ }
\]
Pairs having the same \(\delta\) have isometric *marked* spans after multiplying one of the two basis vectors by a suitable unimodular scalar; the complete coefficient norm above gives this identification.

## Assumptions and scope

All parameters \(a,b\) lie strictly inside the open unit disk; the scalar field is complex; the norm is the supremum norm of the disk algebra on the closed unit disk. Orthogonality means \(\|f+\lambda g\|\ge\|f\|\) for every \(\lambda\in\mathbb C\). There is no claim for boundary parameters or for products of degree greater than one. The pair may coincide, in which case \(\delta=0\), \(\omega=1\), and the formula reduces to \(\|u b_a+v b_a\|=|u+v|\).

## Proof

**1. Boundary reduction.** Every elementary Blaschke factor is analytic on a neighborhood of the closed disk, has supremum norm one, and has modulus one on \(\mathbb T\). The maximum-modulus principle therefore gives, for arbitrary \(u,v\),
\[
\|u b_a+v b_b\|_{A(\mathbb D)}
=\max_{z\in\mathbb T}|u\,R_{a,b}(z)+v|,
\qquad R_{a,b}(z)=\frac{b_a(z)}{b_b(z)}.
\]
The ratio in this line is considered only on \(\mathbb T\), where the denominator never vanishes.

**2. Exact range of the boundary ratio.** The inverse disk automorphism to \(b_a\) is \(b_a^{-1}(w)=(w+a)/(1+\overline a w)\). Direct substitution gives
\[
b_b(b_a^{-1}(w))=\gamma b_c(w),\qquad
c=\frac{b-a}{1-\overline a b},\qquad
\gamma=\frac{1-\overline a b}{1-a\overline b}=\omega^{-1}.
\]
Consequently \(R_{a,b}(b_a^{-1}(w))=\omega w/b_c(w)\). Writing \(c=\delta e^{i\psi}\) when \(c\ne0\) and substituting \(w=e^{i\psi}t\), \(t\in\mathbb T\), reduces the last ratio to
\[
\frac{t}{b_\delta(t)}=\frac{1-\delta t}{1-\delta\overline t}.
\]
For \(0<\delta<1\), the circle \(1-\delta\mathbb T\) has a strictly positive distance from the origin, and its arguments fill exactly \([ -\arcsin\delta,\arcsin\delta]\): the extremal rays are tangent to that circle. The denominator above is the complex conjugate of the numerator. Doubling these arguments proves the exact image identity
\[
\{R_{a,b}(z):z\in\mathbb T\}
=\{\omega e^{i\theta}:-\alpha\le\theta\le\alpha\},
\qquad \alpha=2\arcsin\delta.
\]
When \(\delta=0\), the ratio is the constant \(1\), which is exactly the same identity with \(\alpha=0\) and \(\omega=1\).

**3. Full coefficient norm.** If \(u,v\ne0\), write \(u\omega\overline v=|u||v|e^{i\phi}\), where \(\phi\in[-\pi,\pi]\). The squared boundary modulus is
\[
|u\omega e^{i\theta}+v|^2
=|u|^2+|v|^2+2|u||v|\cos(\theta+\phi).
\]
As \(\theta\) runs from \(-\alpha\) to \(\alpha\), the smallest angular distance of \(\theta+\phi\) from a multiple of \(2\pi\) is exactly \(\max\{0,|\phi|-\alpha\}\). The cosine maximum is therefore the cosine of that quantity, proving the boxed norm formula. Zero coefficients cause no division and give the separately stated trivial case.

**4. Unique best scalar.** From the boundary range, minimizing \(\|b_a-\lambda b_b\|\) over \(\lambda\in\mathbb C\) is equivalent, after dividing by \(\omega\), to finding the unique center of the least enclosing Euclidean circle of the closed unit-circle arc \(\{e^{i\theta}:-\alpha\le\theta\le\alpha\}\).

If \(0\le\alpha\le\pi/2\), the endpoints have distance \(2\sin\alpha\), giving a lower bound \(\sin\alpha\) on every enclosing radius. The midpoint \(\cos\alpha\) of the endpoints attains that radius for the entire arc, because \(\cos\theta\ge\cos\alpha\) implies
\[
|e^{i\theta}-\cos\alpha|^2
=1+\cos^2\alpha-2\cos\alpha\cos\theta\le\sin^2\alpha.
\]
Equality in the endpoint lower bound forces the center to be their midpoint; thus it is unique. If \(\pi/2\le\alpha<\pi\), the arc contains the antipodal points \(i\) and \(-i\), whose least enclosing radius is one and whose unique least enclosing center is zero. The full arc lies on the unit circle, so this lower bound is attained. Restoring \(\omega\), together with \(\sin(2\arcsin\delta)=2\delta\sqrt{1-\delta^2}\) and \(\cos(2\arcsin\delta)=1-2\delta^2\), proves both the unique coefficient and the exact distance formula.

**5. Orthogonality and marked spans.** Since \(\|b_a\|=\|b_b\|=1\), the definition of complex Birkhoff--James orthogonality is equivalent to the distance from \(b_a\) to \(\mathbb C b_b\) being one. The distance formula gives \(\delta\ge1/\sqrt2\), a symmetric condition. Finally, replacing the first generator by \(\overline\omega b_a\) removes \(\omega\) from the complete coefficient norm, leaving dependence only on \(\delta\). That furnishes the asserted marked-span isometries.

## Verification

The proof is analytic and does not depend on numerical data. A standalone Python sanity checker, `VERIFY_PROFILE.py`, samples boundary values in 144 deterministic tests (including \(a=b\), the exact transition, and nonreal zeros and coefficients) and compares them with the closed form. It reports a maximum sampled-mesh discrepancy below \(3\times10^{-7}\); the sampling is not an exhaustive or formal verification of the continuum supremum.

## Relationship to prior work

Martín, Merí, Quero, Roy and Sain (arXiv:2306.02638, first posted 2023-06-05), Corollary 3.6 and Example 4.9, give abstract and finite-Blaschke-product characterizations of complex Birkhoff--James orthogonality in a uniform algebra. Their statements provide a *qualitative* boundary-phase test for arbitrary finite Blaschke products. They do not state the complete two-generator norm, the explicit pseudo-hyperbolic formula for best scalar approximation, or the unique minimizing coefficient. The latter formulas require the exact boundary-ratio arc and its least-enclosing-circle analysis. The Birkhoff--James conclusion is presented here as a consequence, not as a claim to have originated the general orthogonality criterion. Classical smallest-enclosing-circle geometry underlies the final minimax step.

## Limitations

The result treats the two-dimensional span of **single** disk automorphisms, not arbitrary finite Blaschke products. The condition \(\delta<1\) is essential to the stated domain. A general Birkhoff--James characterization already exists, and the current result should be regarded as its explicit quantitative specialization plus a full coefficient-norm computation. Published and unindexed equivalent formulations cannot be ruled out solely by searches; independent review has not been undertaken.

## References

1. M. Martín, J. Merí, A. Quero, S. Roy and D. Sain, *A numerical range approach to Birkhoff-James orthogonality with applications*, arXiv:2306.02638 (first posted 2023-06-05), especially Corollary 3.6 and Example 4.9, https://arxiv.org/abs/2306.02638.
2. S. I. Gass and C. J. Witzgall, *On an Approximate Minimax Circle Closest to a Set of Points*, Computers & Operations Research 31 (2004), 493–506, https://www.nist.gov/publications/approximate-minimax-circle-closest-set-points. Background for the classical enclosing-circle minimax viewpoint, not an assertion of a new method for that geometric subproblem.
