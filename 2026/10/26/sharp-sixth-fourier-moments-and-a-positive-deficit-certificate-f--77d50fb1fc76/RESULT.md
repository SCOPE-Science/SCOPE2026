# Sharp sixth Fourier moments and a positive deficit certificate for cross-polytope spectra

## Finding

For every integer \(d\ge 1\), consider the Laurent polynomial
\[
P(z_1,\ldots,z_d)=\sum_{j=1}^d(a_jz_j+b_jz_j^{-1}),\qquad a_j,b_j\in\mathbb C,
\]
on the probability torus \(\mathbb T^d\). Set \(S=\sum_j(|a_j|^2+|b_j|^2)>0\). The **sharp sixth-power Fourier embedding constant** is
\[
\boxed{\displaystyle\frac{\|P\|_6^6}{S^3}\le C_d
=15-\frac{45}{2d}+\frac{10}{d^2}.}
\]
Equality holds if and only if \(|a_j|=|b_j|=\sqrt{S/(2d)}\) for every \(j\), and the \(d\) complex numbers \(a_jb_j\) all have the same argument. The condition on product arguments is vacuous when \(d=1\).

More strongly, the deficit has the following exact, manifestly nonnegative decomposition. Normalize
\[
s_j=\frac{|a_j|^2+|b_j|^2}{S},\qquad q_j=\frac{a_jb_j}{S},\qquad \sum_js_j=1,
\]
and let \(F=\|P\|_6^6/S^3\). Then
\[
\boxed{\begin{aligned}
C_d-F={}&\sum_{j=1}^d\left(s_j-\frac1d\right)^2
\left(\frac{45}{2}-10s_j-\frac{20}{d}\right)\\
&+\sum_{j=1}^d(18-12s_j)\left(\frac{s_j^2}{4}-|q_j|^2\right)\\
&+36\sum_{1\le i<j\le d}(2-s_i-s_j)
\left(\frac{s_is_j}{4}-\operatorname{Re}(q_i\overline{q_j})\right).
\end{aligned}}
\]
For \(d\ge2\) every displayed coefficient is strictly positive, and all parenthesized differences are nonnegative. For \(d=1\) the first sum is zero and the other terms retain their nonnegative meaning. Thus the identity is also a quantitative rigidity certificate, separating uneven energy across coordinates, imbalance within each antipodal pair, and relative-product-phase misalignment.

The same sharp bound and equality classification hold on every finite product torus \(\prod_{j=1}^d\mathbb Z/N_j\mathbb Z\) with each \(N_j\ge7\), using uniform counting probability measure. This sampling threshold is sharp dimension-by-dimension in the uniform-modulus case: on \((\mathbb Z/6\mathbb Z)^d\), the choice \(a_j=b_j=1/\sqrt{2d}\) has \(S=1\) and
\[
\|P\|_6^6=C_d+\frac{1}{4d^2}>C_d.
\]

## Assumptions and scope

All norms on the continuous torus use normalized Haar probability measure; on finite groups they use normalized counting probability. The input coefficient norm is the unweighted \(\ell^2\) norm. No assumption of real-valuedness or coefficient positivity is imposed. The spectrum is exactly contained in the \(2d\) coordinate characters \(\{\pm e_1,\ldots,\pm e_d\}\), but coefficients are allowed to vanish. The inequality is homogeneous; the deficit formula is stated only for \(S>0\), since the zero polynomial satisfies the unnormalized bound trivially.

## Proof

**Step 1: Fourier expansion.** Orthogonality of distinct characters gives \(\|P\|_2^2=S\). Normalize \(S=1\). Write \(s_j=|a_j|^2+|b_j|^2\) and \(q_j=a_jb_j\). The Fourier support of \(P^3\) splits into disjoint types:

* At \(\pm3e_j\), the coefficients are \(a_j^3\) and \(b_j^3\).
* At \(\pm2e_i\pm e_j\), for distinct indices, coefficients are the corresponding products of three inputs multiplied by \(3\).
* At \(\pm e_i\pm e_j\pm e_k\), for three distinct indices, coefficients are the corresponding products multiplied by \(6\).
* At \(+e_j\) and \(-e_j\), the coefficients are respectively \(3a_j(2Q-q_j)\) and \(3b_j(2Q-q_j)\), where \(Q=\sum_iq_i\).

These statements follow by listing the multisets of three signed coordinate characters having each sum. Plancherel for \(P^3\), expansion of squares, and \(\sum_js_j=1\) give the **exact polynomial identity**
\[
\boxed{\begin{aligned}
F={}&6-9\sum_js_j^2+4\sum_js_j^3\\
&+\sum_j(18-12s_j)|q_j|^2\\
&+36\sum_{i<j}(2-s_i-s_j)\operatorname{Re}(q_i\overline{q_j}).
\end{aligned}}
\]
This is an identity for arbitrary complex coefficients, not an inequality or a numerical approximation.

**Step 2: sharp upper bound.** Arithmetic-geometric mean yields \(|q_j|\le s_j/2\). Cauchy--Schwarz and \(\operatorname{Re}(q_i\overline{q_j})\le|q_i||q_j|\) imply
\[
F\le15-\frac{45}{2}\sum_js_j^2+10\sum_js_j^3=:G(s).
\]
Indeed all coefficients multiplying squared products or cross products in the exact identity are nonnegative, so substitution of the respective upper bounds is valid. Set \(u=1/d\). Using \(\sum_j(s_j-u)=0\), a polynomial expansion yields
\[
C_d-G(s)=\sum_j(s_j-u)^2\left(\frac{45}{2}-10s_j-20u\right).
\]
For \(d\ge2\), each coefficient satisfies
\[
\frac{45}{2}-10s_j-\frac{20}{d}\ge\frac{25}{2}-\frac{20}{d}\ge\frac52>0.
\]
Thus \(G(s)\le C_d\), with equality only at \(s_1=\cdots=s_d=1/d\). The case \(d=1\) is immediate because \(s_1=1\).

**Step 3: the exact deficit and equality.** Subtract the identity for \(F\) from the expression for \(G(s)\), grouping diagonal products and mixed products separately. This gives
\[
G(s)-F=\sum_j(18-12s_j)\left(\frac{s_j^2}{4}-|q_j|^2\right)
+36\sum_{i<j}(2-s_i-s_j)
\left(\frac{s_is_j}{4}-\operatorname{Re}(q_i\overline{q_j})\right).
\]
Combining with the preceding formula for \(C_d-G(s)\) proves the boxed certificate. For every \(j\),
\[
\frac{s_j^2}{4}-|q_j|^2
=\frac{(|a_j|^2-|b_j|^2)^2}{4}\ge0.
\]
Also \(s_is_j/4\ge|q_i||q_j|\ge\operatorname{Re}(q_i\overline{q_j})\). The equality conditions force the stated common moduli and arguments. Conversely those conditions make all three sums vanish. For \(d=1\), only the pair-balance condition remains.

**Step 4: finite-group boundary.** The Fourier support of \(P^3\) lies in the integer cube \([-3,3]^d\). Reduction to \(\prod_j\mathbb Z/N_j\mathbb Z\) is injective on this cube whenever each \(N_j\ge7\). Thus the Parseval calculation and all equality conditions transfer exactly. At modulus \(6\), the characters at \(+3e_j\) and \(-3e_j\) coincide. When each \(a_j=b_j=1/\sqrt{2d}\), the resulting cross term increases the sixth moment by exactly \(2d(2d)^{-3}=1/(4d^2)\); no other triples of the above support collide. This proves the claimed sharp nonaliasing threshold.

## Verification

The accompanying `check_sixth.py` uses Gaussian-integer arithmetic to construct \(P^3\) directly, computes its Fourier \(\ell^2\) energy, and compares that value with the explicit polynomial identity and with the scaled exact deficit. It also checks the sharp constant, extremizing coefficient arrays, the nonaliasing regime at modulus \(7\), and the displayed order-six excess. Running `python3 check_sixth.py` reproduces `check_output.txt`; the recorded execution passed \(2923\) integer/rational assertions. The computation tests finite instances only; the proof above supplies the quantification over all dimensions and complex coefficients.

## Relationship to prior work

Havrilla, Nayar and Tkocz establish Gaussian comparisons for all even moments of type-L random variables and their sums. Their Gaussian sixth-moment upper bound is \(15\) after variance normalization, but this does not imply the dimension-dependent exact deficit \(45/(2d)-10/d^2\) or classify arbitrary pairs of complex Fourier coefficients. Norvidas studies large-sieve sampling inequalities for powers of trigonometric polynomials; that problem controls separated sampled values in terms of continuous norms rather than the sharp continuous coefficient-to-sixth-moment embedding here. Hubert, Metzlaff, Moustrou and Riener optimize pointwise values of already symmetry-invariant trigonometric polynomials supported on crystallographic weight lattices, rather than optimizing the integrated sixth moment over arbitrary complex coefficients of the coordinate cross. Related exact finite-spectrum sixth-moment results on three-character, four-character, and different finite-group spectra do not imply the present coordinate-cross identity without further argument.

## Limitations

The result concerns the sixth moment, not every \(L^p\) exponent, and uses a spectrum contained in antipodal coordinate characters. The finite-group equality classification is asserted only in the nonaliasing regime specified above. The order-six example establishes failure of this same sharp constant at that modulus, not the optimal order-six constant. The exact deficit is coefficient-space rigidity, not an assertion about distance in any stronger function topology. Literature priority has not been independently certified; possible equivalent descriptions through sums of independent arcsine variables remain a bibliographic risk.

## References

1. A. Havrilla, P. Nayar and T. Tkocz, *Khinchin-type inequalities via Hadamard's factorisation*, arXiv:2102.09500, first public version 18 February 2021, especially Theorem 1, Corollary 3 and Section 2. https://arxiv.org/abs/2102.09500
2. S. Norvidas, *On large sieve inequalities involving pth powers of trigonometric polynomials*, arXiv:2209.12294, first public version 25 September 2022, especially Theorem 1. https://arxiv.org/abs/2209.12294
3. E. Hubert, T. Metzlaff, P. Moustrou and C. Riener, *Optimization of trigonometric polynomials with crystallographic symmetry and spectral bounds for set avoiding graphs*, arXiv:2303.09487, first public version 16 March 2023. https://arxiv.org/abs/2303.09487
