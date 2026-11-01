# Sharp first positive radial-power transition of analytic Bergman-kernel zeros

## Finding

For the analytic weighted Bergman space on the unit disk with radial weight \(|z|^{2\beta}(1-|z|^2)^m\), consider **integer** boundary exponents \(m\in\{0,1,2,3,4\}\) and nonnegative origin exponents \(\beta\ge0\). The reproducing kernel is zero-free for all \(\beta\ge0\) when \(m\le3\). At \(m=4\) it is zero-free precisely when \(0\le\beta\le1\); when \(\beta>1\), its scalar numerator has **exactly two simple zeros in the open unit disk**. Each such scalar zero gives an entire zero fibre of the two-variable kernel. The threshold at \(\beta=1\) is a transversal unit-circle collision: for either entering root \(\zeta(\beta)\),
\[
\left.\frac{d}{d\beta}|\zeta(\beta)|^2\right|_{\beta=1}=-\frac{49}{360}.
\]
Thus \(m=4\) is the first **nonnegative integer boundary exponent** in this finite ordered family at which an increasing positive origin-power weight creates reproducing-kernel zeros. No statement is made for arbitrary real boundary exponents or for meromorphic functions on the punctured disk.

## Assumptions and scope

Write \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), fix \(\beta\ge0\), and let \(m\in\{0,1,2,3,4\}\). The measure is
\[
 d\mu_{m,\beta}(z)=\frac{|z|^{2\beta}(1-|z|^2)^m}{B(\beta+1,m+1)}\,\frac{dA(z)}\pi,
\]
where \(dA\) is planar Lebesgue measure and \(B\) is the beta function. Denote by \(A^2_{m,\beta}\) the Hilbert space of functions **holomorphic on all of** \(\mathbb D\) that are square-integrable for this measure. Only nonnegative monomial powers occur in its orthogonal basis. Set \(b=\beta+1\ge1\), \(s=z\overline w\), and \((u)_j=u(u+1)\cdots(u+j-1)\). A *scalar zero* means a root \(s\in\mathbb D\) of the scalar kernel function; distinct scalar roots correspond to distinct nonempty zero fibres in \(\mathbb D^2\). The zeros are counted with algebraic multiplicity.

## Proof

**1. Exact kernel.** Polar integration gives \(\|z^n\|^2=B(n+b,m+1)/B(b,m+1)\) for every integer \(n\ge0\). Consequently,
\[
 K_{m,\beta}(z,w)=\frac{B(b,m+1)}{m!}\sum_{n=0}^\infty (n+b)_{m+1}s^n
 =\frac{B(b,m+1)}{m!}\frac{P_{m,b}(s)}{(1-s)^{m+2}},
\]
where \(P_{m,b}(s)=(1-s)^{m+2}\sum_{n\ge0}(n+b)_{m+1}s^n\) is polynomial of degree at most \(m+1\). Indeed, \((n+b)_{m+1}\) is a polynomial in \(n\), and the generating series for each power of \(n\) has denominator at most \((1-s)^{m+2}\). In particular,
\[
 P_{m,1}(s)=(m+1)!,\qquad P_{m,b}(1)=(m+1)!
\]
for the indicated parameters. The prefactor is positive and the denominator cannot vanish in \(|s|<1\). Thus only the roots of \(P_{m,b}\) matter. Conversely every \(|s|<1\) can be written as \(z\overline w\) with \(z,w\in\mathbb D\), so the scalar-root count is the exact two-variable zero-fibre count.

**2. Exact boundary-exclusion certificate.** Define \(R_{m,b}(s)=s^{m+1}P_{m,b}(1/s)\). Because \(P_{m,b}\) has real coefficients, a root on \(|s|=1\) must also be a root of \(R_{m,b}\). The following exact polynomial resultants are obtained by expanding the preceding finite generating functions and eliminating \(s\):
\[
\begin{aligned}
\mathcal R_0(b)&=1-2b,\\
\mathcal R_1(b)&=16b^2(2b^2-1),\\
\mathcal R_2(b)&=-432b^2(b+1)^2(2b+1)^3(2b^2+2b-3),\\
\mathcal R_3(b)&=7077888b^2(b+1)^4(b+2)^2(b^2+2b+3)^2
 (2b^4+8b^3+4b^2-8b-3),\\
\mathcal R_4(b)&=-88473600000b^2(b-2)^2(b+1)^4(b+2)^4(b+3)^2(b+5)^2(2b+3)^5\\
 &\hspace{2em}\cdot(2b^4+12b^3+12b^2-18b-5).
\end{aligned}
\]
Here \(\mathcal R_m(b)=\operatorname{Res}_s(P_{m,b}(s),R_{m,b}(s))\), with the usual polynomial-resultant convention. On \(b\ge1\), every displayed factor is nonzero except \((b-2)^2\) in \(\mathcal R_4\). Specifically, the final quartics for \(m=3,4\) equal \(3\) at \(b=1\) and have strictly positive derivatives on \([1,\infty)\): their derivatives are respectively \(8b^3+24b^2+8b-8\) and \(8b^3+36b^2+24b-18\). All other factors are plainly nonzero. Therefore there are no unit-circle roots for \(m\le3\) at any \(b\ge1\), and none for \(m=4\) unless \(b=2\). Root count inside the circle is locally constant away from such boundary crossings, even when the formal degree drops. At \(b=1\) every numerator is a nonzero constant, so \(m\le3\) has no interior roots for \(b\ge1\), and \(m=4\) has no interior roots for \(1\le b<2\).

**3. Critical factorization and direction.** At \(m=4,b=2\), exact simplification gives
\[
P_{4,2}(s)=-120(s-2)(s^2-3s+3)(s^2-s+1).
\]
The only roots in the closed unit disk are \(\zeta_\pm=(1\pm i\sqrt3)/2\), both lying *on* the unit circle. The remaining roots are \(2\) and \((3\pm i\sqrt3)/2\), which lie outside. Since the two critical roots are simple, each extends differentiably in \(b\) by the implicit function theorem, with
\[
 \zeta_+'(2)=-\frac{\partial_bP_{4,b}(\zeta_+)|_{b=2}}
 {\partial_sP_{4,2}(\zeta_+)}.
\]
Direct substitution into the exact polynomial yields
\[
2\operatorname{Re}\!\left(\overline{\zeta_+}\,\zeta_+'(2)\right)=-\frac{49}{360}.
\]
By complex conjugation the identical derivative holds for \(\zeta_-\). Thus both cross *into* the disk as \(b\) rises past \(2\), and both were outside immediately below. The other three roots remain outside near \(b=2\). The nonvanishing of \(\mathcal R_4(b)\) for every \(b>2\) prevents any subsequent boundary crossing, hence there are exactly two scalar roots for every \(b>2\). Their simplicity follows from the exact discriminant
\[
\operatorname{disc}_sP_{4,b}=24883200000b^3(b-1)^4(b+1)^3(b+2)^3(b+3)^3(b+4)^4,
\]
which is nonzero for \(b>1\). The critical value \(b=2\) itself has no interior roots. Replacing \(b\) by \(\beta+1\) completes the classification and the transverse law.

## Verification

The standalone `check.py` constructs each \(P_{m,b}\) from the exact rising-factorial generating series; it checks all five resultants, both endpoint identities, the critical factorization, the discriminant, and the radial derivative by symbolic arithmetic. It also checks sample root counts numerically on both sides of the threshold. Run `python check.py` with SymPy installed. Exact symbolic identities are the algebraic certificates used in the proof; numerical root checks are corroboration only. The positivity of the relevant quartics on \(b\ge1\), constancy of root counts in the absence of boundary crossings, and the direction argument are established analytically above, not inferred from finite samples.

## Relationship to prior work

Antti Perälä's *Vanishing Bergman kernels on the disk* (first public March 17, 2017, arXiv:1703.05976) provides general mechanisms producing finitely many Bergman-kernel zeros from radial weights and proves a finiteness phenomenon; it does not supply this exact bounded-degree positive radial-power classification. Ghiloufi and Snoun's *Zeros of new Bergman kernels* (first public September 9, 2020, arXiv:2009.04307) calculates kernels for a closely related beta-weight family and studies polynomial zeros. **Their principal spaces are holomorphic on the punctured disk and their basis explicitly includes negative powers**, with lower monomial index depending on the origin exponent. Thus their positive-origin-exponent kernel is not the reproducing kernel of the whole-disk analytic subspace here. Their existing negative-origin-exponent thresholds are not claimed as new here. The result does not assert that the formulas for monomial moments themselves are new; it asserts the combined exact positive-power zero-phase and its critical derivative for the explicitly specified analytic spaces.

## Limitations

Only \(\beta\ge0\), integer \(m=0,1,2,3,4\), and whole-disk holomorphic functions are covered. No zero classification is claimed for noninteger boundary powers, for higher integer powers, or for the meromorphic punctured-disk space. The proof characterizes how many scalar zeros occur, not closed-form locations for all parameters. Priority relative to further literature not inspected in full remains an acknowledged risk. Independent mathematical audit and validation have not been performed.

## References

1. A. Perälä, *Vanishing Bergman kernels on the disk*, arXiv:1703.05976 (first posted March 17, 2017), https://arxiv.org/abs/1703.05976.
2. N. Ghiloufi and S. Snoun, *Zeros of new Bergman kernels*, arXiv:2009.04307 (first posted September 9, 2020), https://arxiv.org/abs/2009.04307.
3. Y. E. Zeytuncu, *Weighted Bergman projections and kernels: \(L^p\) regularity and zeros*, arXiv:1009.2806 (first posted September 14, 2010), https://arxiv.org/abs/1009.2806. This concerns radial weights comparable to one, unlike the present positive boundary and origin powers.
