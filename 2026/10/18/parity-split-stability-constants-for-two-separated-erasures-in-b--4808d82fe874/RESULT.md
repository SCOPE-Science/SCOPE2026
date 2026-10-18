# Parity-split stability constants for two separated erasures in Berrut interpolation

## Finding

Let \(h\ge 2\) be a fixed integer. For every sufficiently large integer \(N\), remove exactly the nodes \(m_N\) and \(m_N+h\) from the integer grid \(\{0,1,\ldots,N\}\), where for some fixed \(\delta>0\), \(\delta N\le m_N\le(1-\delta)N-h\). Reindex all retained nodes in increasing order and apply Berrut's first barycentric rational interpolant with the alternating weights \((-1)^r\), where \(r\) is the new rank. Denote its operator norm from bounded nodal data to the uniform norm on \([0,N]\) by \(\Lambda_{N,h}\).

Define the positive functions
\[
B(t)=2\sum_{k=1}^{\infty}\frac{(-1)^{k+1}k}{k^2-t^2}
=2\log 2+2\sum_{q=1}^{\infty}\eta(2q+1)t^{2q},\qquad -1<t<1,
\]
where \(\eta(s)=\sum_{k=1}^{\infty}(-1)^{k+1}k^{-s}\) is the alternating zeta function, and
\[
I(p)=\int_0^1\frac{x^{p-1}(1-x)}{1+x}\,dx,\qquad p>0.
\]
For every \(h\ge2\), the strictly convex function
\[
D_h(t)=B(t)+(-1)^hI(h-t),\qquad -1<t<1,
\]
has a unique minimizer \(t_h\) and strictly positive minimum \(d_h=D_h(t_h)\). Then
\[
\boxed{\displaystyle \lim_{N\to\infty}\frac{\Lambda_{N,h}}{\log N}=C_h=\frac{2}{d_h}.}
\]
Moreover, in the unscaled integer-grid coordinate relative to \(m_N\), every sequence of maximizing points has distance tending to zero from the two-point set \(\{t_h,h-t_h\}\); both limiting points lie in the two length-two gaps adjacent to the erasures. More precisely, no subsequential limit of a maximizing point relative to \(m_N\) lies outside that set.

The spacing parity determines the direction of the amplification compared with one isolated erased node:
\[
\boxed{\begin{aligned}
&C_{2}<C_{4}<C_{6}<\cdots<\frac{1}{\log2},\\
&C_{3}>C_{5}>C_{7}>\cdots>\frac{1}{\log2}.
\end{aligned}}
\]
The sharp approach from alternating sides is
\[
\boxed{C_h=\frac1{\log2}-\frac{(-1)^h}{4(\log2)^2h^2}+O(h^{-3}).}
\]
The minimizing point is displaced on alternating sides of its erased node:
\[
\boxed{t_h=\frac{(-1)^{h+1}}{3\zeta(3)h^3}+O(h^{-4}).}
\]
For orientation, the numerical coefficients are \(C_2\approx1.334642697\), \(C_3\approx1.500180056\), \(C_4\approx1.411794833\), and \(C_5\approx1.463423475\). These decimals are checks, not definitions or proofs.

## Assumptions and scope

All interpolation points lie on the real line; affine rescaling makes the unit mesh canonical. Both deleted sites are interior by a fixed positive fraction of the total length; the difference \(h\) is fixed first, and then \(N\to\infty\). The coefficient is not asserted uniformly in growing \(h\), nor for deleted sites approaching an endpoint. The barycentric signs are **reindexed after deletion**; retaining the pre-deletion signs defines a different operator. The real interpolation Lebesgue function is the sum of absolute values of its rational cardinal basis functions, hence the stated norm also holds for complex nodal data.

For retained nodes \(x_0<\cdots<x_{N-2}\) and a non-nodal point \(u\), the Lebesgue function is exactly
\[
L_N(u)=\frac{\sum_r|u-x_r|^{-1}}{\left|\sum_r(-1)^r(u-x_r)^{-1}\right|}.
\]
At retained nodes the continuous limit is \(1\). Thus the operator has no real poles and the maximum defining \(\Lambda_{N,h}\) exists.

## Proof

**1. Alternating denominator in the first exceptional gap.** Translate by \(m_N\), so the two missing indices become \(0,h\). Up to one harmless overall sign, the signed coefficients at surviving integer positions \(j\) are \((-1)^j\) for \(j<0\), \(-(-1)^j\) for \(0<j<h\), and \((-1)^j\) for \(j>h\). The finite alternating tails converge locally uniformly as the endpoints recede. The two-sided limiting signed denominator is
\[
F_h(t)=\frac{\pi}{\sin(\pi t)}-\frac1t-\frac{(-1)^h}{t-h}
-2\sum_{j=1}^{h-1}\frac{(-1)^j}{t-j},
\]
with removable values interpreted by limits. The partial-fraction identity for \(\pi\csc(\pi t)\) applies with symmetrically paired tails; finite-endpoint errors are \(O(N^{-1})\) on fixed compact subintervals of \((-1,1)\).

With only the node \(0\) removed, the signs on the entire positive half-line flip. Pairing positions \(-k\) and \(k\) gives the denominator \(-B(t)\). The change made by restoring the old signs after the second erasure is, with \(p=h-t>0\),
\[
\begin{aligned}
F_h(t)+B(t)
&=(-1)^h\left[-\frac1p+2\sum_{k=1}^{\infty}\frac{(-1)^{k+1}}{p+k}\right]\\
&=(-1)^h\left[-\frac1p+2\int_0^1\frac{x^p}{1+x}\,dx\right]\\
&=(-1)^{h+1}I(p).
\end{aligned}
\]
For \(-1<t<1\) the nearest two surviving nodes are \(-1,1\) and their reindexed contributions have the same negative sign. Pairing each of the two outward alternating tails shows \(F_h(t)<0\). Therefore \(|F_h(t)|=B(t)+(-1)^hI(h-t)=D_h(t)\).

**2. Positivity and the unique minimum.** In an arbitrary interval between successive surviving nodes, split the absolute signed denominator into the left and right alternating reciprocal sums, each beginning with a positive term. On differentiating twice, each becomes twice an alternating series of inverse cubes of increasing positive distances. Each such series is strictly positive by the alternating-series test. Hence the absolute denominator is strictly convex in every gap; in \((-1,1)\) it blows up at both endpoints. In particular, \(D_h\) has exactly one minimum, and it is positive.

Reflection of the survivor lattice across \(h/2\) carries the gap \((-1,1)\) to \((h-1,h+1)\). The absolute denominator is reflection-invariant; hence the second exceptional gap has the identical minimum \(d_h\), at \(h-t_h\).

**3. The global Lebesgue norm localizes to those gaps.** On any unbroken unit-length cell write the distances to the two adjacent nodes as \(a,b>0\), with \(a+b=1\), and put \(A=1/a+1/b\ge4\). The remaining absolute reciprocal sum is at most \(2H_N\), where \(H_N=\sum_{j=1}^N1/j=\log N+O(1)\). Alternating-sign pairing bounds the signed denominator below by \(A-1/(a+1)-1/(b+1)\ge A-2\). Consequently
\[
L_N(u)\le\frac{A+2H_N}{A-2}\le 2+H_N,
\]
uniformly throughout all unbroken cells, including points arbitrarily close to their endpoints. Thus their normalized contribution has limsup at most \(1\).

For the first two-unit gap, \(m_N+t\) with \(-1<t<1\), the numerator is \(2\log N+O(1)\) locally uniformly away from the two adjacent retained nodes. The denominator converges locally uniformly to \(D_h(t)\), so
\[
\frac{L_N(m_N+t)}{\log N}\longrightarrow\frac2{D_h(t)}.
\]
The same holds after reflection in the second exceptional gap. Near a retained endpoint of either exceptional gap, one outward alternating tail is bounded below by \(1/a-1/(a+1)\), where \(a\) is the distance to that endpoint; the numerator is at most \(1/a+2H_N+O(1)\). Taking first \(N\to\infty\), then \(a\downarrow0\), rules out a competing endpoint maximizer. Finally, \(d_h\le B(0)+I(2)=3/2\) for even \(h\), whereas \(d_h\le B(0)=2\log2\) for odd \(h\). Thus \(C_h\ge4/3>1\), so neither ordinary cells nor nodal boundary layers can maximize asymptotically. Strict convexity yields precisely the asserted two-point localization, and establishes the norm limit.

**4. Parity ordering and sharp spacing limit.** Differentiation under the integral sign shows that \(I(p)>0\) decreases strictly with \(p\). The series expansion for \(B\) gives \(B(t)\ge2\log2\), with equality only at \(t=0\). For even \(h\), \(D_h=B+I\) lies strictly above \(B\), so \(C_h<1/\log2\); increasing \(h\) by two decreases \(I(h-t)\) pointwise and strictly increases \(C_h\). For odd \(h\), \(D_h=B-I\), and evaluating at \(t=0\) shows \(d_h<2\log2\); increasing \(h\) by two strictly decreases \(C_h\). Both parity subsequences tend to \(1/\log2\) because \(I(h-t)\to0\) locally uniformly and \(B\) has its unique minimum at zero.

For the quantitative laws use
\[
I(p)=\frac1{2p^2}+O(p^{-3}),\qquad I'(p)=-p^{-3}+O(p^{-4}),
\]
which follow by expanding \((1-x)/(1+x)\) near \(x=1\) under the beta-type integral. In the convergent even power series for \(B\), \(B'(0)=0\) and \(B''(0)=4\eta(3)=3\zeta(3)>0\). The critical equation \(B'(t_h)-(-1)^hI'(h-t_h)=0\), strict convexity and these estimates give
\[
t_h=\frac{(-1)^{h+1}}{3\zeta(3)h^3}+O(h^{-4}),\qquad
d_h=2\log2+\frac{(-1)^h}{2h^2}+O(h^{-3}).
\]
Expanding \(2/d_h\) gives the claimed alternating quadratic correction. This completes the proof.

## Verification

Run \(\texttt{python3 check_two_erasure.py}\) with the Python standard library. The code verifies 244 exact-rational and numerical assertions: exact finite-grid sign reindexing, the infinite-denominator identity, strict parity ordering for sampled separations, finite-section growth comparisons and the spacing-asymptotic coefficient. Results are deterministic apart from ordinary floating-point rounding. The proof above, not the finite checks, establishes all quantified limiting statements.

## Relationship to prior work

Bos, De Marchi and Hormann (2011) prove logarithmic Lebesgue growth for intact equidistant Berrut grids. Bos, De Marchi, Hormann and Sidon (2013) extend logarithmic upper bounds to well-spaced nodes; their Theorem 2.2 gives an order bound, expressly not the sharp leading constant. Both are applicable in the sense of ensuring logarithmic scale, but neither implies the spacing-parity classification or the two-gap localization. Hormann's 2014 survey likewise summarizes the classical pole-free rational formula and logarithmic stability estimates. The known case of one consecutive deletion block is a different topology of missing sites; in particular the contiguous two-deletion case has one gap of length three, whereas the present nonadjacent geometry has two length-two gaps. Their exact coefficients cannot be substituted for one another.

The 2016 Ibrahimoglu--Cuyt result provides sharp bounds for complete equidistant grids, not a cited theorem about two separated erasures. Its full text was not available for this comparison; this is a genuine residual priority uncertainty, not proof of absence. Searches for two missing/nonadjacent Berrut sites, equivalent alternate-sign reciprocal sums, and exact gap-wise Lebesgue coefficients produced no inspected stronger result. The claim is limited to the precise model and asymptotics proved here.

## Limitations

The theorem does not handle a separation \(h\) growing jointly with \(N\), fixed endpoint-distance erasures, non-integer grid defects, arbitrary deletion sets, or interpolation formulas retaining their original weights. No statement is made that absence from searched literature proves worldwide priority. Numerical decimals are illustrative only. No external or independent mathematical audit is asserted.

## References

1. L. Bos, S. De Marchi and K. Hormann, *On the Lebesgue constant of Berrut's rational interpolant at equidistant nodes*, J. Comput. Appl. Math. 236 (2011), 504–510. Lawful author full text: https://www.inf.usi.ch/hormann/papers/Bos.2011.OTL.pdf .
2. L. Bos, S. De Marchi, K. Hormann and J. Sidon, *Bounding the Lebesgue constant for Berrut's rational interpolant at general nodes*, J. Approx. Theory 169 (2013), 7–22. Lawful author full text: https://www.inf.usi.ch/hormann/papers/Bos.2013.BTL.pdf .
3. K. Hormann, *Barycentric Interpolation* (2014 survey), https://www.inf.usi.ch/hormann/papers/Hormann.2014.BI.pdf .
4. B. A. Ibrahimoglu and A. Cuyt, *Sharp Bounds for Lebesgue Constants of Barycentric Rational Interpolation at Equidistant Points*, Exp. Math. 25 (2016), 347–354, https://doi.org/10.1080/10586458.2015.1072862 (abstract and bibliographic information inspected).
