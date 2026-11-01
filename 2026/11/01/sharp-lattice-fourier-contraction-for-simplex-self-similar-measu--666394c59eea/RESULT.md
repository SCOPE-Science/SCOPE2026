# Sharp lattice Fourier contraction for simplex self-similar measures

## Finding
For integers \(d\ge2\) and \(b\ge2\), define the simplex digit measure \(\mu_{d,b}\) below. Its largest Fourier–Stieltjes coefficient magnitude at a **nonzero integer lattice frequency** is exactly
\[
C_{d,b}=\prod_{j=1}^{\infty}\frac{\sqrt{d^2+1+2d\cos(2\pi/b^j)}}{d+1}.
\]
For every nonzero \(m\in\mathbb Z^d\),
\[
|\widehat\mu_{d,b}(m)|\le C_{d,b},
\]
with equality precisely at \(m=\pm b^a e_i\) (\(1\le i\le d\)) or \(m=\pm b^a(1,\ldots,1)\), where \(a\ge0\) is integral. In particular \(0<C_{d,b}<1\). For the planar middle-halves Sierpiński gasket measure, \(C_{2,2}\approx0.22646565039707746\).

The convolution operator \(T f=f*\mu_{d,b}\) on the torus \(\mathbb T^d=\mathbb R^d/\mathbb Z^d\) consequently satisfies the **sharp** mean-zero contraction law
\[
\|T^r f\|_{L^2(\mathbb T^d)}\le C_{d,b}^{\,r}\|f\|_{L^2(\mathbb T^d)}\qquad(r=1,2,\ldots),
\]
for every mean-zero \(f\); equality is attained by any maximizing Fourier character.

## Assumptions and scope
Let \(U_1,U_2,\ldots\) be independent uniformly distributed variables on \(D=\{0,e_1,\ldots,e_d\}\), and let \(X=\sum_{j\ge1}b^{-j}U_j\). The probability law of \(X\) is \(\mu_{d,b}\). The Fourier convention is \(\widehat\mu(m)=\int e^{-2\pi i\langle m,x\rangle}\,d\mu(x)\), evaluated at integer \(m\in\mathbb Z^d\). All quantifiers above range over integer dimensions and bases \(d,b\ge2\), nonzero integer vectors, and positive convolution powers. No statement is asserted for arbitrary real-frequency maxima or unequal digit weights.

## Proof
**1. Mask factorization and scaling.** Independence gives
\[
\widehat\mu_{d,b}(m)=\prod_{j=1}^{\infty}\frac{1+\sum_{i=1}^d\exp(-2\pi i m_i/b^j)}{d+1}.
\]
Every factor omitted when replacing \(m\) by \(b m\) is exactly one, so \(\widehat\mu_{d,b}(b^a m)=\widehat\mu_{d,b}(m)\) for integral \(a\ge0\). Hence divide \(m\ne0\) by the largest common power of \(b\), obtaining an integer vector \(q\) with at least one coordinate not divisible by \(b\).

**2. Universal optimal single-scale mask.** At scale \(j\), put \(N=b^j\), \(L=d+1\), \(z_0=1\), and \(z_i=\exp(-2\pi i q_i/N)\). These are \(N\)-th roots of unity and are not all equal, since some \(q_i\not\equiv0\pmod b\). The exact identity
\[
L^2-\left|\sum_{i=0}^d z_i\right|^2=\sum_{0\le r<s\le d}|z_r-z_s|^2
\]
shows the bound. Indeed, any two distinct \(N\)-th roots have squared chord length at least \(4\sin^2(\pi/N)\). A nonconstant multiset of \(L\) values has at least \(L-1=d\) unordered unequal pairs (partition into classes and count cross-class pairs). Thus
\[
\left|\sum_{i=0}^d z_i\right|^2
\le (d+1)^2-4d\sin^2(\pi/b^j)
=d^2+1+2d\cos(2\pi/b^j).
\]
Multiplication over every scale gives the required sharp upper bound. Each majorant factor is positive for \(d\ge2\), and its difference from one is \(O(b^{-2j})\), so the product converges to a strictly positive value; its first factor is strictly below one.

**3. Equality is rigid.** The special primitive vectors \(q=\pm e_i\) and \(q=\pm(1,\ldots,1)\) attain the single-scale bound for *every* \(j\): their masks are respectively \(d+e^{\pm2\pi i/b^j}\) and \(1+d e^{\pm2\pi i/b^j}\), which have identical magnitudes. This proves existence of maximizers.

Conversely, if a primitive \(q\) attains the positive infinite product, then every one of its nonnegative scale-factor inequalities must be equality; one strict factor would make the whole product strictly smaller. Choose \(j\) large enough that \(N=b^j>2\max_{r,s}|q_r-q_s|\), where \(q_0=0\), and \(N>3\). Equality in the pair-counting argument forces exactly two phase classes, one of size one and the other of size \(d\); equality in the chord bound forces the two integer phase representatives to differ by exactly \(1\) or \(-1\). Because the coordinates are small relative to \(N\), no two distinct integer representatives alias modulo \(N\). With \(q_0=0\), this means either precisely one coordinate of \(q\) is \(\pm1\), or all coordinates are the same \(\pm1\). Restoring the common power of \(b\) proves the exhaustive equality classification.

**4. Operator consequence.** On \(L^2(\mathbb T^d)\), the characters indexed by \(m\in\mathbb Z^d\) form an orthonormal basis and convolution acts diagonally with multipliers \(\widehat\mu_{d,b}(m)\). Removing the constant character leaves operator norm \(C_{d,b}\) by the first assertion. The same diagonalization gives \(C_{d,b}^{\,r}\) for the \(r\)-th convolution power. The extremizing characters listed above show sharpness.

## Verification
The attached independent-of-the-proof finite checker recomputes the two expressions for each single-scale mask, tests the explicit discrete chord bound, and enumerates all nonzero frequencies in fixed small boxes for selected bases and dimensions. It also computes rapidly convergent approximations to the constant for these examples. These are *finite consistency checks*, not a substitute for the argument covering all dimensions, bases and frequencies. The exact pairwise chord identity and the equality characterization are proved above without numerical assumptions.

## Relationship to prior work
Self-affine measures on simplex digit sets and their exponential spectrality are studied by Li (2007, 2012) and Yuan (2015). Their spectrality and orthogonality questions concern zeros and exponential bases, whereas the present invariant is the **maximum positive modulus over all nonzero lattice characters and the complete set of equality frequencies**. Li (2007) is available in full and uses compatible pairs and orthogonality, not this extremal lattice multiplier norm. The 2012 and 2015 articles were checked at the available abstract level; they were not treated as full-text evidence of noncoverage. The sharp two-level modulus ordering for the one-dimensional middle-thirds Cantor measure concerns a distinct one-dimensional digit distribution and does not imply this multi-parameter simplex statement.

## Limitations
Originality has been assessed against accessible full text, abstracts, semantic mathematical indexes and recoverable prior statements, not against an exhaustive mathematical bibliography. An older source could contain an equivalent coefficient bound in another language, and the 2012 and 2015 full texts remain a residual comparison risk. The result does not determine the second-largest modulus, the values of individual nonextremal coefficients, or arbitrary real-frequency maxima. No independent mathematical audit has been performed.

## References
1. J.-L. Li, *Spectral self-affine measures in* \(\mathbb R^n\), Proceedings of the Edinburgh Mathematical Society 50 (2007), 197–215, DOI 10.1017/S0013091503000324 (online 2007-02-09).
2. J.-L. Li, *Spectrality of self-affine measures on the three-dimensional Sierpiński gasket*, Proceedings of the Edinburgh Mathematical Society 55 (2012), 477–496, DOI 10.1017/S0013091511000502 (online 2012-04-20).
3. Y. B. Yuan, *Spectral self-affine measures on the generalized three Sierpiński gasket*, Analysis in Theory and Applications 31 (2015), 394–406, DOI 10.4208/ata.2015.v31.n4.5.
