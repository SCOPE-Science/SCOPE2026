# Sharp fourth-moment phase rigidity for the six-point triangular Fourier aperture

## Finding

Take the canonical degree-two simplex of bivariate frequencies
\[
S=\{(i,j)\in\mathbb Z_{\ge0}^{2}:i+j\le2\}
=\{(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)\}.
\]
For arbitrary unimodular coefficients, let
\[
P(z,w)=\sum_{(i,j)\in S}c_{ij}z^iw^j,
\qquad |c_{ij}|=1.
\]
With normalized Haar measure on \(\mathbb T^2\), the **exact attainable interval** is
\[
\boxed{\left\{\int_{\mathbb T^2}|P|^4\,dm\right\}=[48,102].}
\]
Put \(\omega=e^{2\pi i/3}\) and \(Q(i,j)=\binom{i}{2}+\binom{j}{2}+2ij\). **All** minimizing coefficients, without additional exceptions, are
\[
\boxed{c_{ij}=\lambda\alpha^i\beta^j\omega^{\sigma Q(i,j)}},
\qquad\lambda,\alpha,\beta\in\mathbb T,\quad\sigma\in\{1,-1\}.
\]
These represent exactly two distinct orbits under common-phase and coordinate-phase multiplication; coordinate permutations and reflections are not taken as equivalences. The maximum \(102\) has exactly the character-phase coefficients \(c_{ij}=\lambda\alpha^i\beta^j\).

When all coefficients are binary signs, the sharp minimum is \(54\), with four classes after normalization and exactly 32 sign minimizers. More generally, for \(q\ge2\), among coefficients belonging to the \(q\)-th roots of unity \(\mu_q\), the unrestricted minimum \(48\) is attained **if and only if** \(3\mid q\); in that case it has exactly \(2q^3\) realizations. No exact restricted optimum is claimed for \(3\nmid q>2\).

The same fourth-moment statements and extremizer classifications hold for normalized Fourier averages on \(\mathbb Z_m\times\mathbb Z_n\) whenever both \(m,n\ge5\). In particular, the minimum noncentral squared aperiodic autocorrelation is \(48-36=12\), versus \(54-36=18\) for binary phases. Thus the sharp autocorrelation merit factors, defined as central autocorrelation squared divided by the noncentral energy, are \(3\) and \(2\), respectively.

## Assumptions and scope

All six coefficients have modulus exactly one; no coefficient may vanish. The \(L^4\) moment uses Haar **probability** measure, so \(\int |P|^2=6\). The finite-group statement uses character evaluation \(z=e^{2\pi i k/m}\), \(w=e^{2\pi i\ell/n}\), averaged over all \(m n\) samples, with \(m,n\ge5\). The phase alphabet \(\mu_q\) is the set of all complex \(q\)-th roots of one. The classification is modulo only the indicated three multiplication parameters when speaking of orbits; the raw integer counts stated for discrete alphabets do not quotient by those parameters.

## Proof

**1. Autocorrelation reduction.** For every integer shift \(r=(h,k)\), set
\[
C(r)=\sum_{s\in S\cap(S+r)}c_s\overline{c_{s-r}}.
\]
The Fourier series of \(|P|^2\) has coefficient \(C(r)\), so Parseval gives
\[
\int_{\mathbb T^2}|P|^4\,dm
=\sum_{r\in S-S}|C(r)|^2.
\]
Here \(C(0)=6\), and nonzero shifts occur in nine pairs \(\{r,-r\}\). Six positive representatives have precisely one contributing coefficient pair, hence \(|C(r)|=1\); the other three have three contributing pairs each. The six single-pair representatives are \((2,0),(2,-1),(2,-2),(1,1),(1,-2),(0,2)\), and the three multiple-pair representatives are \((1,0),(0,1),(1,-1)\).

**2. Complete phase gauge.** Multiplying each coefficient by \(\lambda\alpha^i\beta^j\), with \(\lambda,\alpha,\beta\in\mathbb T\), multiplies every \(C(h,k)\) by \(\alpha^h\beta^k\), leaving the moment unchanged. Exactly one such transformation makes \(c_{00}=c_{10}=c_{01}=1\). Write the remaining coefficients as \(u=c_{20}, v=c_{11}, w=c_{02}\), each of unit modulus. The three multiple-pair autocorrelations are, in order,
\[
1+u+v,\qquad 1+v+w,\qquad 1+u\overline v+v\overline w.
\]
Thus there is the **exact identity**
\[
\boxed{\int|P|^4\,dm
=48+2\left(|1+u+v|^2+|1+v+w|^2+
|1+u\overline v+v\overline w|^2\right).}
\tag{1}
\]
In particular \(48\) is a universal lower bound, and \(102\) is a universal upper bound by the triangle inequality.

**3. Equality at the lower bound.** If equality holds at \(48\), all three summands in (1) vanish. Because \(|u|=|v|=1\), the equation \(1+u+v=0\) has exactly two ordered solutions \((u,v)=(\omega,\omega^2)\) and \((\omega^2,\omega)\): the three summands form an equilateral triangle in the complex plane. The equation \(1+v+w=0\) then forces \(w=u\). Either resulting triple also gives \(1+u\overline v+v\overline w=0\), since \(u\overline v\) and \(v\overline u\) are the two nontrivial cubic roots. This proves both necessity and sufficiency. Since \(Q(2,0)=Q(0,2)=1\), \(Q(1,1)=2\), and \(Q\) vanishes on the three gauged positions, undoing the gauge gives exactly the stated two families.

**4. Upper endpoint and all intervening values.** For equality at \(102\), all three complex sums in (1) must have modulus three. The first such equality forces \(u=v=1\), and the second forces \(w=1\); this vector attains \(102\). The original coefficient torus \(\mathbb T^6\) is connected, and the moment map is continuous. Its image therefore contains every real number between the attained endpoints and, by the bounds, no others.

**5. Quantized phases.** For binary signs, each of the three sums in (1) is an odd integer, so its squared modulus is at least one. Hence the moment is at least \(48+6=54\). Equality occurs for exactly four gauged triples
\[
(u,v,w)\in\{(-1,-1,1),(-1,1,-1),(1,-1,-1),(1,-1,1)\},
\]
which proves sharpness and the count \(4\cdot2^3=32\) of raw sign coefficients. In the \(q\)-phase alphabet, equality at \(48\) requires a primitive third root from step 3, so it is possible precisely when \(3\mid q\). When possible, the two normalized triples admit \(q\) independent choices for each of \(\lambda,\alpha,\beta\), giving \(2q^3\) distinct arrays.

**6. Discrete finite tori.** Every difference \(r\in S-S\) lies in \([-2,2]^2\). If \(m,n\ge5\), reducing these differences modulo \((m,n)\) is injective. Orthogonality on \(\mathbb Z_m\times\mathbb Z_n\) therefore reproduces the identical right side of (1); all the preceding bounds, phase gauges and equality conditions remain valid. This argument does not assert the formula on smaller finite grids, where frequency-difference aliasing may occur.

## Verification

Run `python3 checker.py` in the same directory. The dependency-free checker independently enumerates the exact support-difference multiplicities, constructs all autocorrelations over \(\mathbb Z[\omega]\), verifies identity (1) for all normalized binary and ternary phase choices, counts all their minimizers, and checks difference injectivity on representative no-alias finite tori. It also compares finite Fourier-grid fourth moments numerically, as a subsidiary test. Its completed run reported **PASS**, 35 exact algebraic phase configurations, and 95 supplementary quadrature points. None of the finite tests is substituted for the universal proof above.

## Relationship to prior work

The noncentral autocorrelation energy and merit-factor normalization follow standard Fourier/autocorrelation identities. Gu, Zhou, Adhikary, Feng and Fan (2021, arXiv:2108.05657), especially their Section IV, construct **pairs** of two-dimensional complementary arrays with zero-correlation zones. Du and Jiang (2022, arXiv:2204.09372), especially Sections II, IV and V, construct polyphase complementary **pairs and quads**. Those constructions do not give a sharp single-array fourth-moment minimum or a complete equality classification on this six-point triangular support. Katz and Ramirez (2023, arXiv:2307.14566), Sections 1 and 4–5, study the **distribution across binary one-dimensional sequences** of autocorrelation demerit factors, rather than an optimized two-dimensional complex phase aperture. The present statement concerns a different optimization objective even though all of these works share the autocorrelation formalism. No claim of bibliographic exhaustiveness is made.

## Limitations

The theorem is confined to the complete total-degree-two triangular support, unimodular coefficients, fourth moments, and finite tori without frequency-difference aliasing. It does not establish optimal arrays for other apertures, moments, alphabets not divisible by three, smaller discrete tori, peak sidelobes, or Golay complementary pairs. An older equivalent computation in polyphase-array or aperiodic-autocorrelation tables cannot be ruled out by the searches performed; independent mathematical and bibliographic audits have not been performed.

## References

- Z. Gu, Z. Zhou, A. R. Adhikary, Y. Feng and P. Fan, *New Constructions of Golay Complementary Pair/Array with Large Zero Correlation Zone*, arXiv:2108.05657v1, first public 2021-08-12, https://arxiv.org/abs/2108.05657.
- C. Du and Y. Jiang, *Constructions of Polyphase Golay Complementary Arrays*, arXiv:2204.09372v1, first public 2022-04-20, https://arxiv.org/abs/2204.09372.
- D. J. Katz and M. E. Ramirez, *Limiting Moments of Autocorrelation Demerit Factors of Binary Sequences*, arXiv:2307.14566v1, first public 2023-07-27, https://arxiv.org/abs/2307.14566.
