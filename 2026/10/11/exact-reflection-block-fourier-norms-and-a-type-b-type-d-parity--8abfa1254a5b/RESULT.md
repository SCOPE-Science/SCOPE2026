# Exact reflection-block Fourier norms and a type-B/type-D parity defect

## Finding

The regular-representation Fourier blocks associated with the natural reflection representations of the classical Weyl groups have explicit sharp endpoint norms. Put
\[
 a_j=\frac{\binom{2j}{j}}{2^j(j+1)!},\qquad
 A_n=\sum_{j=0}^{n-1}(-1)^j a_j,\qquad
 c=e^{-1}\bigl(I_0(1)+I_1(1)\bigr).
\]
The two endpoint norms of the type-B projection coincide, and for every integer \(n\ge1\) satisfy
\[
 \boxed{\|P_n^B\|_{\ell^1\to\ell^1}=\|P_n^B\|_{\ell^\infty\to\ell^\infty}=nA_n.}
\]
For every integer \(n\ge3\), the endpoint norms of the type-D projection coincide and satisfy
\[
 \boxed{\|P_n^D\|=\begin{cases}nA_n,&n\ \mathrm{odd},\\[2mm]
 nA_n+\displaystyle\frac{(-1)^{n/2-1}n}{n!}\frac{\binom{n-2}{n/2-1}}{2^{n-2}},&n\ \mathrm{even}.
 \end{cases}}
\]
Here the unadorned norm on the last line denotes either of the stated endpoint operator norms. In particular, the type-B and type-D norms agree **exactly** at all odd ranks, whereas at even ranks their nonzero difference alternates in sign. Their common normalized limit is
\[
 \lim_{n\to\infty}\frac{\|P_n^B\|}{n}=\lim_{n\to\infty}\frac{\|P_n^D\|}{n}=c
 \approx0.67367002294334888537.
\]
The Bessel-limit approximation has a strict certified sign and remainder:
\[
 0<(-1)^n(c-A_n)<a_n\qquad(n\ge1).
\]

## Assumptions and scope

Let \(B_n=C_2^n\rtimes S_n\), represented by orthogonal signed-permutation matrices on \(\mathbb R^n\). For \(n\ge3\), let \(D_n\le B_n\) consist of matrices having an even number of negative signs, **regardless of the sign of the underlying permutation**. Both are finite groups. For \(g=(\varepsilon,\sigma)\), where \(\varepsilon_i\in\{\pm1\}\), their natural character is
\[
 \chi_n(g)=\operatorname{tr}(g)=\sum_{i:\,\sigma(i)=i}\varepsilon_i.
\]
Write \(P_n^B\), respectively \(P_n^D\), for the orthogonal central projection on the entire natural isotypic block of \(\ell^2(B_n)\), respectively \(\ell^2(D_n)\), with counting measure. For clarity, the two sharp endpoint norms are computed for this *entire isotypic projection*, not a projection onto one fixed copy of the natural representation. All formulas are uniform in the indicated positive integer ranks; the type-D boundary \(n=2\) is excluded because its natural two-dimensional representation is reducible. Define the two required Bessel functions directly by
\[
 I_j(z)=\frac1\pi\int_0^\pi e^{z\cos\theta}\cos(j\theta)\,d\theta,
 \qquad j=0,1.
\]

## Proof

**1. Endpoint norm and irreducibility.** For any finite group \(G\) and irreducible real character \(\chi\) of degree \(d\), the central orthogonal isotypic projection on \(\ell^2(G)\) is convolution by \(K(g)=d\chi(g^{-1})/|G|\). Every row and column of its matrix is a translate of the same kernel. Hence
\[
 \|P_\chi\|_{\ell^1\to\ell^1}=\|P_\chi\|_{\ell^\infty\to\ell^\infty}
 =\sum_{g\in G}|K(g)|=d\,\mathbb E_G|\chi(g)|.
\]
For uniform signed permutations in \(B_n\), the signs are independent with mean zero. Expanding the square of the displayed trace gives \(\mathbb E_{B_n}\chi_n^2=\mathbb E_{S_n}\#\operatorname{Fix}(\sigma)=1\); the latter holds since each coordinate has probability \(1/n\) of being fixed. For \(D_n\), when \(n\ge3\), conditioning the signs on product \(+1\) leaves every one- or two-coordinate sign marginal uniform. The same square-moment computation gives \(\mathbb E_{D_n}\chi_n^2=1\). Character orthogonality therefore proves the natural representations are irreducible on both groups in their asserted rank ranges.

**2. Exact type-B expectation.** Let \(d_m\) be the derangement proportion in \(S_m\), with \(d_0=1\), and let \(s_k\) be the mean absolute displacement of \(k\) independent fair unit signs, with \(s_0=0\). The probability that a permutation of \(n\) symbols has exactly \(k\) fixed points is \(d_{n-k}/k!\), so
\[
 \mathbb E_{B_n}|\chi_n|=\sum_{k=0}^n\frac{s_kd_{n-k}}{k!}.
\]
Using \(d_m=\sum_{j=0}^m(-1)^j/j!\), the ordinary generating series is
\[
 \sum_{m\ge0}d_mz^m=\frac{e^{-z}}{1-z}.
\]
Elementary fair-walk counting yields \(s_{2m}=2m\binom{2m}{m}/4^m\) and \(s_{2m+1}=(2m+1)\binom{2m}{m}/4^m\). Substitution into the exponential generating series gives
\[
 \sum_{k\ge0}\frac{s_kz^k}{k!}=z\bigl(I_0(z)+I_1(z)\bigr).
\]
Thus, as formal power series,
\[
 \sum_{n\ge0}(\mathbb E_{B_n}|\chi_n|)z^n
 =\frac{z}{1-z}\,e^{-z}\bigl(I_0(z)+I_1(z)\bigr).
\]
The integral definitions of the Bessel functions imply
\[
 h(z):=e^{-z}(I_0(z)+I_1(z))
 =\frac1\pi\int_0^\pi e^{-z(1-\cos\theta)}(1+\cos\theta)\,d\theta.
\]
Expanding the exponential and evaluating its beta integral gives
\[
 [z^j]h(z)=\frac{(-1)^j}{\pi j!}
 \int_0^\pi (1-\cos\theta)^j(1+\cos\theta)\,d\theta
 =(-1)^j\frac{\binom{2j}{j}}{2^j(j+1)!}=(-1)^ja_j.
\]
Taking the coefficient of \(z^n\) in \(zh(z)/(1-z)\) proves \(\mathbb E_{B_n}|\chi_n|=A_n\), hence the first boxed identity.

**3. Exact type-D parity defect.** A uniform sign vector conditioned on sign product \(+1\) has the same marginal on every proper subset of coordinates as an unconstrained vector. Consequently, for a permutation other than the identity, the conditional expectation of the absolute trace is unchanged. The entire difference of the type-D and type-B mean absolute characters comes from the identity permutation, of probability \(1/n!\). For \(n\ge3\),
\[
 \mathbb E_{D_n}|\chi_n|-\mathbb E_{B_n}|\chi_n|
 =\frac{T_n}{n!},\qquad
 T_n=\frac1{2^n}\sum_{j=0}^n(-1)^j\binom nj|n-2j|.
\]
For odd \(n\), the terms indexed by \(j\) and \(n-j\) cancel, giving \(T_n=0\). For even \(n=2m\), pairing those terms and applying the alternating binomial identity
\(\sum_{j=0}^r(-1)^j\binom tj=(-1)^r\binom{t-1}{r}\)
reduces the numerator to \(4(-1)^{m-1}\binom{2m-2}{m-1}\). Therefore
\[
 T_{2m}=(-1)^{m-1}\frac{\binom{2m-2}{m-1}}{2^{2m-2}}.
\]
Multiplying by the representation degree \(n\) proves the type-D norm formula, including its sign.

**4. Limit and rigorous error.** The positive coefficients satisfy
\[
 \frac{a_{j+1}}{a_j}=\frac{2j+1}{(j+1)(j+2)}<1
 \quad\text{for every }j\ge0.
\]
The alternating-series theorem applied to \(h(1)=\sum_{j\ge0}(-1)^ja_j\) gives the strict sign-and-size bound for \(c-A_n\). The even-rank type-D correction divided by \(n\) is bounded above by \(1/n!\), and vanishes; its odd-rank counterpart is identically zero. The common limit follows.

## Verification

The standalone `verify.py` uses only the Python standard library. Run `python3 verify.py` in the directory containing that file. It exhaustively enumerates all signed permutations and their traces in ranks \(1\) through \(7\), checks both group expectations and character orthogonality with exact rational arithmetic (the type-D rank range begins at \(3\)), verifies the alternating parity identity for \(1\le n\le100\), and checks \(249\) consecutive coefficient recurrences. The observed output begins `VERIFY_OK direct_signed_group_ranks=1..7 checked=7 parity_moments_n=1..100 checked=100 bessel_coefficients_checked=249`. These finite cases are independent diagnostics; the proof for all ranks is the analytic argument above, not extrapolation.

## Relationship to prior work

The finite-group central-character projection formula, its homogeneous-space analogue, and the representation-theoretic wreath-product decomposition are classical. Scarabotti and Tolli (arXiv:math/0701533v1; initially public 19 January 2007, primary MSC 43A95) provide a directly relevant finite harmonic-analysis setting. Their Corollary 2.15 treats central projections, and Section 5 treats wreath products. These prior general results justify the baseline normalization but do not themselves evaluate the absolute trace expectation, its type-D parity restriction, or the sharp Bessel coefficient above.

Foata and Han study signed permutations and *basic* Bessel functions in generating functions for other permutation statistics; the inspected definitions and introduction do not supply the endpoint norm or the particular parity defect proved here. The 2014 monograph of Ceccherini-Silberstein, Scarabotti, and Tolli surveys wreath-product representation theory, but a full-text implication comparison could not be completed; it remains an explicit residual risk. The direct comparison with the symmetric-group \((n-2,2)\) Fourier-block calculation, with the usual standard-representation calculation for doubly transitive actions, and with finite-cyclic character kernels does not imply the present signed trace/conditioning formulas. General projection formulas are credited and not claimed as new.

## Limitations

The result concerns only the natural real reflection representation and its complete isotypic block, not every irreducible or spectral cutoff of either Weyl group. It does not give \(\ell^p\)-norms at intermediate exponents. The type-D claim excludes rank \(2\) and is not about the determinant-one subgroup (which differs from the even-sign subgroup). The endpoint norm identity is exact at each finite rank; numerical enumeration verifies samples only. A potentially equivalent old treatment hidden under a character-\(L^1\) or wreath-product normalization, particularly in book literature without accessible full text, remains an originality risk.

## References

1. F. Scarabotti and F. Tolli, *Harmonic analysis on a finite homogeneous space*, arXiv:math/0701533v1 (first posted 19 January 2007), especially Corollary 2.15 and Section 5. `https://arxiv.org/abs/math/0701533`; doi:10.1112/plms/pdp027. Primary classification 43A95 as recorded in the preprint and publisher metadata.
2. D. Foata and G.-N. Han, *Calcul Basique des Permutations Signées, II: Analogues Finis des Fonctions de Bessel*, Electronic Journal of Combinatorics 4(2), R9; initially published 4 December 1996. `https://www.combinatorics.org/ojs/index.php/eljc/article/download/v4i2r9/pdf/`; doi:10.37236/1324.
3. T. Ceccherini-Silberstein, F. Scarabotti, and F. Tolli, *Representation Theory and Harmonic Analysis of Wreath Products of Finite Groups*, Cambridge University Press, 2014, Chapter 2; full-text access not confirmed. doi:10.1017/CBO9781107279087.
