# Generic recovery of analytic polynomials from derivative intensities at \(2d-1\) roots of unity

## Finding

**Theorem (all degrees at least three).** Fix an integer \(d\ge3\), put \(m=2d-1\), and let \(\omega=\exp(2\pi i/m)\). For Lebesgue-almost every vector \((c_0,\ldots,c_d)\in\mathbb C^{d+1}\), the \(2m\) real intensities
\[
\bigl\{|P(\omega^k)|^2,\ |P'(\omega^k)|^2:0\le k<m\bigr\},\qquad P(z)=\sum_{j=0}^d c_jz^j,
\]
determine \(P\) among **all** polynomials of degree at most \(d\), up to a common complex scalar of modulus one. In fact, the \(m\) derivative intensities together with only the three real statistics
\[
A_0=\frac1m\sum_{k=0}^{m-1}|P(\omega^k)|^2,
\qquad
A_1=\frac1m\sum_{k=0}^{m-1}|P(\omega^k)|^2\omega^{-k}\in\mathbb C
\]
already have this generic uniqueness property.

For a fixed derivative outside an explicitly described null exceptional set, every possible nontrivial alternative is excluded unless the integration constant lies on one of at most \(2^{d-1}-1\) computable circles (allowing empty or degenerate circles) in the complex plane. This is a **sufficient** almost-everywhere sampling theorem, not a universal uniqueness or minimum-sampling theorem.

## Assumptions and scope

Lebesgue-almost every means the complement of a measure-zero set in the real \(2d+2\)-dimensional coefficient space. The derivative is the ordinary complex derivative in \(z\); differentiation of \(P(e^{2\pi it})\) in \(t\) differs by the unit-modulus factor \(e^{2\pi it}\) and the known modulus factor \(2\pi\), so the intensity data are equivalent after a known rescaling. Competitors are arbitrary degree-at-most-\(d\) complex polynomials, not assumed generic.

Write \(Q=P'=\sum_{j=0}^{d-1}q_jz^j\). We work first on the full-measure derivative locus where \(q_0q_{d-1}\ne0\), the \(d-1\) roots \(r_1,\ldots,r_{d-1}\) are distinct, every \(|r_i|\ne1\), no two roots are reciprocal conjugates, and
\[
\prod_{i\in S}|r_i|\ne1
\quad\text{for every nonempty }S\subseteq\{1,\ldots,d-1\}.
\]
The last condition is generic: in ordered nonzero-root coordinates, every nonempty-subset equation is a nonidentically zero real-analytic equation (evaluate at distinct real roots all greater than one). Each equation has Lebesgue-null zero locus. The Vieta map from a nonzero leading coefficient and distinct ordered roots to derivative coefficients is locally an invertible real-analytic map; hence these exceptional loci remain null in derivative coefficient space. Unit-circle roots, reciprocal-root pairs, repeated roots, and zero endpoint coefficients are also proper lower-dimensional algebraic or real-analytic loci. The invertible linear correspondence between nonconstant coefficients of \(P\) and coefficients of \(Q\) preserves null sets.

## Proof

**1. Sampled derivative intensities recover the entire derivative power spectrum.** On the unit circle, the trigonometric polynomial \(|Q(z)|^2\) has Fourier frequencies from \(-(d-1)\) through \(d-1\). These are \(2d-1=m\) distinct residue classes modulo \(m\), so inversion of the \(m\)-point discrete Fourier transform determines every Laurent coefficient of \(|Q|^2\). In particular, all competitors have exactly the same \(|Q(z)|\) for every \(|z|=1\). The outermost Laurent coefficient \(q_{d-1}\overline{q_0}\ne0\) also forces every competitor derivative to have both nonzero endpoint coefficients.

**2. All derivative ambiguities are explicit zero flips.** Factor
\[
Q(z)=a\prod_{i=1}^{d-1}(z-r_i),\qquad a\ne0.
\]
For \(|z|=1\), the identity \(|z-r|=|r|\,|z-1/\overline r|\) holds. Spectral-factor uniqueness, obtained by factoring the reciprocal polynomial \(z^{d-1}|Q(z)|^2\) as an algebraic polynomial with paired roots \(r_i\) and \(1/\overline{r_i}\), shows that, modulo a global unit phase, the complete family of derivatives with the same circle modulus is indexed by subsets \(S\):
\[
Q_S(z)=a\Bigl(\prod_{i\in S}|r_i|\Bigr)
\Bigl(\prod_{i\in S}(z-1/\overline{r_i})\Bigr)
\Bigl(\prod_{i\notin S}(z-r_i)\Bigr).
\]
The empty subset gives \(Q\). For each nonempty \(S\), comparison of the constant terms gives
\[
\frac{|Q_S(0)|}{|Q(0)|}=\prod_{i\in S}|r_i|^{-1}\ne1.
\]
This is the crucial separation of the coefficient multiplying the unknown integration constant in the first autocorrelation.

**3. The first two polynomial intensity moments are unaliased.** Set \(x=c_0\), and for each derivative factor \(Q_S(z)=\sum_{j=0}^{d-1}q_{j,S}z^j\), define
\[
c_{0,S}=x_S,\qquad c_{j,S}=\frac{q_{j-1,S}}{j}\quad(1\le j\le d).
\]
Since \(d\ge3\), the Fourier indices \(0,1\) of \(|P(\omega^k)|^2\) cannot alias with any other coefficients of the Laurent expansion supported in \([-d,d]\): for index \(0\), the nearest nonzero congruent integer is \(m>d\); for index \(1\), the nearest different congruent integer is \(1-m=2-2d<-d\). Thus
\[
A_0=|x|^2+E(Q),\qquad A_1=Q(0)\overline x+K(Q),
\]
where
\[
E(Q)=\sum_{j=1}^d\left|\frac{q_{j-1}}j\right|^2,\qquad
K(Q)=\sum_{j=2}^d\frac{q_{j-1}}j\overline{\left(\frac{q_{j-2}}{j-1}\right)}.
\]
The same two identities hold for each competitor \((Q_S,x_S)\).

**4. A wrong zero flip confines the constant coefficient to a circle.** Equality of \(A_1\) determines the competitor's integration constant uniquely:
\[
x_S=\alpha_Sx+\beta_S,\quad
\alpha_S=\frac{\overline{Q(0)}}{\overline{Q_S(0)}},\quad
\beta_S=\overline{\left(\frac{K(Q)-K(Q_S)}{Q_S(0)}\right)}.
\]
For nonempty \(S\), \(|\alpha_S|\ne1\) by Step 2. Equality of \(A_0\) would therefore force
\[
(|\alpha_S|^2-1)|x|^2
+2\operatorname{Re}(\alpha_Sx\overline{\beta_S})
+|\beta_S|^2+E(Q_S)-E(Q)=0.
\tag{*}
\]
Because the coefficient of \(|x|^2\) is nonzero, equation (*) is not an identity: its zero locus is either empty, a point, or a Euclidean circle. There are at most \(2^{d-1}-1\) nonempty zero-flip subsets. Thus for every admissible derivative the bad integration constants form a finite union of planar null sets. For the empty subset, \(Q_S=Q\) (after fixing global phase), equality of \(A_1\) yields \(x_S=x\); the only remaining equivalence is the unavoidable common unit phase.

**5. Almost-everywhere quantification.** The admissible derivative locus has full Lebesgue measure by the assumptions above. For each derivative there are only finitely many planar zero loci in its integration constant. Tonelli–Fubini applied in derivative-coefficient and integration-constant coordinates shows that the set of all potentially ambiguous \(P\) has Lebesgue measure zero. Every competitor was considered in Steps 1–4, so this proves the stated uniqueness among arbitrary polynomial competitors.

## Verification

The proof is algebraic and measure-theoretic; finite computation does not establish the all-degree statement. A self-contained exact-arithmetic witness script, `scripts/check.py`, enumerates every nonempty zero flip for derivatives with rational simple roots \(2,3,\ldots,d\), for \(3\le d\le7\), and tests the first-moment reconstruction and nonzero energy residual at a Gaussian-rational integration constant. Its recorded stdout is in `scripts/check_output.txt`. The test checked respectively \(3,7,15,31,63\) wrong spectral factors without floating-point comparison. To reproduce, use Python 3 and SymPy and run `python scripts/check.py` from the extracted package root.

The infinite-dimensional quantifier over degrees and the measure-zero conclusion come from the proof, not from the computational witness.

## Relationship to prior work

Jaming and Rathmair, *Uniqueness of phase retrieval from three measurements* (2022), §3.1, Proposition 3.2, establish **universal** recovery of an \(N\)-coefficient analytic polynomial at \(2N-1\) roots of unity using ordinary derivative magnitudes, and Question 3.5 explicitly asks at which sample counts **generic** uniqueness occurs. Setting \(N=d+1\), the present theorem gives a positive generic answer at \(2N-3\) sites for all \(N\ge4\), a strictly smaller grid. Their exhibited nongeneric ambiguities at \(2N-2\) sites do not preclude generic uniqueness at fewer sites.

Király and Ehler (2014) analyze generic algebraic phase retrieval and generic measurement ensembles; their identifiability thresholds do not by themselves supply this deterministic roots-of-unity derivative-mask result. The present proof uses the additional Fourier/spectral-factor structure. Nearby low-degree polynomial phase-retrieval classifications and generic-ensemble results are not implication-equivalent to an all-degree statement on the specified grid. A formulation under phase-retrievable pairs of circulant Fourier masks could still overlap this theorem; no exhaustive bibliographic uniqueness claim is made.

## Limitations

The result is almost-everywhere, not uniform or universal. It establishes sufficiency at \(2d-1\) sites, not the smallest sufficient number. It gives no quantitative noise-stability estimate, complete classification of nongeneric ambiguous fibers, or guarantee that floating-point spectral factorization is well conditioned. The explicit circle cover applies only when derivative roots satisfy the stated genericity conditions. The theorem is for analytic univariate polynomials and paired ordinary-derivative/intensity samples on a complete roots-of-unity grid.

## References

1. Philippe Jaming and Martin Rathmair, *Uniqueness of phase retrieval from three measurements*, arXiv:2205.08753v1 (first publicly posted 2022-05-18), §3.1, especially Proposition 3.2 and Question 3.5. https://arxiv.org/pdf/2205.08753
2. Franz J. Király and Martin Ehler, *The Algebraic Approach to Phase Retrieval and Explicit Inversion at the Identifiability Threshold*, arXiv:1402.4053v1 (2014). https://arxiv.org/pdf/1402.4053
