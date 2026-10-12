# An explicit \(12+\frac{832}{5227}\) range for improved Riemann-zeta moments
## Finding
Let
\[
M_k(T)=\int_0^T\left|\zeta\!\left(\frac12+it\right)\right|^k\,dt.
\]
Define
\[
k_*=12+\frac{832}{5227}=\frac{63556}{5227}
\]
and
\[
\delta(k)=\frac{520}{445121}-\frac{26135}{3560968}(k-12).
\]
For every fixed real \(k\) with \(12\le k<k_*\) and every \(\varepsilon>0\),
\[
M_k(T)\ll_{k,\varepsilon}T^{1+(k-4)/8-\delta(k)+\varepsilon}.
\]
Since \(\delta(k)>0\) on this interval, this gives an explicit admissible value
\[
\nu=\frac{832}{5227}=0.1591735220\ldots
\]
for the unquantified extension beyond the twelfth moment noted by de Faveri and Pandey.

## Assumptions and scope
The argument is unconditional. It uses the level-set bounds recorded in the proof of Theorem 10.1 of de Faveri--Pandey, arXiv:2610.01035v1, and Bourgain's pointwise bound
\[
\left|\zeta\!\left(\frac12+it\right)\right|\ll_\varepsilon t^{13/84+\varepsilon}.
\]
The parameter \(k\) is fixed as \(T\to\infty\). The claim concerns exponents of \(T\); logarithmic factors are absorbed into \(T^\varepsilon\).

## Proof
Write
\[
\sigma_1=\frac{451}{3688},\qquad
\sigma_2=\frac{58907}{445121},\qquad
\sigma_3=\frac{13}{84}.
\]
The source proof of its twelfth-moment bound uses the following three level-set estimates for the maximal size \(N(T,T^\sigma)\) of a one-spaced set of ordinates with \(\left|\zeta(\tfrac12+it)\right|\ge T^\sigma\):

1. for \(0\le\sigma\le\sigma_1\), the classical estimate gives \(N(T,T^\sigma)\prec T^{1-4\sigma}\);
2. for \(\sigma_1\le\sigma\le\sigma_2\), their equation (70) gives
\[
N(T,T^\sigma)\prec T^{(1070-6164\sigma)/619};
\]
3. for \(\sigma_2\le\sigma\le\sigma_3\), their equation (71) gives
\[
N(T,T^\sigma)\prec T^{1-6\sigma}+T^{593/288-(3587/288)\sigma}.
\]
Bourgain's pointwise bound restricts the dyadic level decomposition to \(\sigma\le\sigma_3\), up to an arbitrarily small change absorbed in \(T^\varepsilon\). Repeating the source's level-set decomposition with the factor \(T^{k\sigma}\) therefore reduces the exponent for \(M_k\) on a dyadic interval to the maximum of the following endpoint expressions:
\[
E_1(k)=1+(k-4)\sigma_1,
\]
\[
E_2(k)=\frac{1070}{619}+\left(k-\frac{6164}{619}\right)\sigma_2,
\]
\[
E_{3a}(k)=1+(k-6)\sigma_3,
\]
and
\[
E_{3b}(k)=\frac{593}{288}+\left(k-\frac{3587}{288}\right)\sigma_2.
\]
The last expression is evaluated at \(\sigma_2\) because
\[
k_*<\frac{3587}{288},
\]
so its coefficient of \(\sigma\) is negative throughout the claimed range. Direct exact arithmetic gives
\[
E_2(12)=E_{3b}(12)=2-\frac{520}{445121}.
\]
The two affine functions \(E_2\) and \(E_{3b}\) have the same slope \(\sigma_2\), hence they are identical. Also
\[
E_1(12)<E_2(12),\qquad \sigma_1<\sigma_2,
\]
so \(E_1(k)<E_2(k)\) for every \(k\ge12\). Finally,
\[
E_{3a}(12)<E_2(12)
\]
and a direct endpoint comparison gives
\[
E_{3a}(k_*)<E_2(k_*),
\]
so affine linearity implies \(E_{3a}(k)<E_2(k)\) throughout \([12,k_*]\). Thus the controlling exponent is exactly
\[
E_2(k)=2-\frac{520}{445121}+\frac{58907}{445121}(k-12).
\]
The classical interpolation exponent at order \(k\) is
\[
B(k)=1+\frac{k-4}{8}=2+\frac{k-12}{8}.
\]
Subtracting gives
\[
B(k)-E_2(k)
=\frac{520}{445121}-
\left(\frac{58907}{445121}-\frac18\right)(k-12)
=\delta(k),
\]
because
\[
\frac{58907}{445121}-\frac18=\frac{26135}{3560968}.
\]
The saving remains positive exactly while
\[
k-12<\frac{520/445121}{26135/3560968}
=\frac{832}{5227}.
\]
Summing dyadic \(T\)-intervals proves the stated bound on \([0,T]\).

## Verification
The accompanying `verify_moment_extension.py` performs exact rational checks of every boundary identity and affine comparison used above. It verifies
\[
E_2(12)=2-\frac{520}{445121},\qquad
B(k_*)=E_2(k_*),\qquad
k_*<\frac{3587}{288},
\]
and checks the dominance of \(E_2\) over the other three endpoint expressions throughout the interval by endpoint-and-slope arguments. A dense rational sample of 1001 points is included only as a supplementary regression check, not as proof. The replay output is recorded in `verification_output.txt`.

## Relationship to prior work
De Faveri and Pandey prove the improved twelfth-moment exponent
\[
2-\frac{520}{445121}
\]
and explicitly state that their estimates also improve moments for \(12\le k<12+\nu\) for some small \(\nu>0\), while saying that they do not optimize the range \(\nu\). Their paper does not state a numerical value of \(\nu\). The calculation above keeps their exact breakpoints and all three level-set regimes from equations (70)--(73), rather than interpolating the twelfth moment with a pointwise estimate, and produces the explicit range \(\nu=832/5227\).

Trudgian--Yang supply the exponent-pair input used in the high-value regime, and Bourgain supplies the \(13/84\) pointwise cutoff. Those works predate the new middle-range estimate and therefore do not contain this combined range calculation. Searches for the exact rational constants, for an explicit \(12+\nu\) range attached to arXiv:2610.01035, and for equivalent moment-envelope statements located no prior statement of the result.

## Limitations
The claim does not improve any large-value estimate used by de Faveri--Pandey. It is an exact optimization of the exponent envelope formed by the displayed estimates in their proof of Theorem 10.1. No claim is made that \(832/5227\) is the largest range obtainable from all currently known analytic-number-theory inputs. At \(k=k_*\), this particular envelope meets the classical interpolation exponent and yields no strict saving, so the asserted improvement uses the strict inequality \(k<k_*\).

## References
1. A. de Faveri and M. Pandey, *The sixth moment of the Riemann zeta function*, arXiv:2610.01035v1 (2026), especially Theorems 1.1--1.3 and equations (69)--(73).
2. J. Bourgain, *Decoupling, exponential sums and the Riemann zeta function*, J. Amer. Math. Soc. 30 (2017), 205--224, DOI 10.1090/jams/860.
3. T. S. Trudgian and A. Yang, *Toward optimal exponent pairs*, Math. Comp. 94 (2025), 1467--1502; arXiv:2306.05599.
