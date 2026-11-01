# Nonvanishing Fourier transforms of zero-composition matrix pairs in the stable rectangular range

## Finding

Let \(q\ge 2\) be a prime power, and let \(a,b\) be integers with \(a\ge b\ge2\). Put \(V=\mathbb F_q^b\) and \(W=\mathbb F_q^a\). In the additive group
\[
G=\operatorname{Hom}(V,W)\oplus\operatorname{Hom}(W,V),
\]
consider the zero-composition incidence set
\[
Z_{a,b}=\{(X,Y):X:V\to W,\ Y:W\to V,\ XY=0\}.
\]
For a nontrivial additive character \(\psi\) of \(\mathbb F_q\), its unnormalized Fourier transform at \(A:W\to V\) and \(B:V\to W\) is
\[
F(A,B)=\sum_{(X,Y)\in Z_{a,b}}\psi(\operatorname{tr}(AX)+\operatorname{tr}(BY)).
\]
Every \(F(A,B)\) is an integer and satisfies the **uniform congruence**
\[
\boxed{\quad F(A,B)\equiv(-1)^b q^{\binom b2}\pmod{q^{\binom b2+1}}.\quad}
\]
In particular **no Fourier coefficient vanishes**. Unnormalized additive convolution by \(\mathbf1_{Z_{a,b}}\) is invertible on the entire \(q^{2ab}\)-dimensional complex function space. Its exact smallest singular value is \(q^{\binom b2}\), attained when both frequency maps \(A\) and \(B\) have rank \(b\).

The entire spectrum, including individual integer eigenvalues, is supplied by the explicit subspace formula below. The largest singular value is \(|Z_{a,b}|\), so the sharp spectral condition number is \(|Z_{a,b}|/q^{\binom b2}\), where
\[
|Z_{a,b}|=\sum_{d=0}^{b}{b\brack d}_q\,q^{ad}
\prod_{i=0}^{b-d-1}(q^a-q^i).
\]
Here \({b\brack d}_q\) is the Gaussian binomial coefficient and an empty product is one.

## Assumptions and scope

The field can have any characteristic, including characteristic two, and can be a nonprime extension field. The dimension restriction \(a\ge b\ge2\) ensures that injective maps \(V\to W\) exist. The two matrix factors are independently additive, not multiplicative, groups. The pair condition is \(XY=0\), **not** commutation, anticommutation, or the condition \(YX=0\).

All traces are ordinary finite-dimensional matrix traces over \(\mathbb F_q\). No normalized Fourier factors occur. For the Fourier multiplier formula, let \(K\le V\), write \(d=\dim K\), and let \(\pi_K:V\to V/K\) be the quotient map. Set \(r_K=\operatorname{rank}(\pi_K A)\). Define \(\prod_{j=u}^v(\cdot)=1\) when \(u>v\).

## Proof

**Step 1: sum over the second matrix.** For a given \(X\), the condition \(XY=0\) is exactly \(\operatorname{im}Y\subseteq\ker X\). Write \(K=\ker X\). The trace pairing between maps \(W\to K\) and \(K\to W\) is nondegenerate; therefore additive-character orthogonality yields
\[
\sum_{Y:W\to K}\psi(\operatorname{tr}(BY))
=q^{a\dim K}\,\mathbf1_{\{K\subseteq\ker B\}}.
\]
Consequently, if \(S_K(A)\) denotes the character sum over all \(X:V\to W\) with **exact** kernel \(K\), then
\[
F(A,B)=\sum_{K\le\ker B}q^{a\dim K}S_K(A).
\]

**Step 2: evaluate the exact-kernel character sum.** For \(L\le V\), character orthogonality on \(\operatorname{Hom}(V/L,W)\) gives
\[
\sum_{X:L\subseteq\ker X}\psi(\operatorname{tr}(AX))
=q^{a(b-\dim L)}\mathbf1_{\{\operatorname{im}A\subseteq L\}}.
\]
Möbius inversion on the lattice of \(\mathbb F_q\)-subspaces uses
\(\mu(K,L)=(-1)^tq^{\binom t2}\) for \(t=\dim(L/K)\). Set \(m=b-d\) and \(r=r_K\). Among the \(t\)-dimensional subspaces of \(V/K\) containing \(\operatorname{im}(\pi_K A)\), there are \({m-r\brack t-r}_q\). Thus
\[
S_K(A)=\sum_{t=r}^{m}{m-r\brack t-r}_q
(-1)^tq^{\binom t2+a(m-t)}.
\]
The finite Gaussian binomial theorem
\[
\sum_{j=0}^{h}{h\brack j}_q(-1)^jq^{\binom j2}z^j
=\prod_{j=0}^{h-1}(1-zq^j)
\]
now gives the **exact evaluation**
\[
\boxed{\quad S_K(A)=(-1)^{r_K}
q^{\binom{b-d}{2}}
\prod_{j=a-b+d+1}^{a-r_K}(q^j-1).\quad}
\]
This also proves integrality. Substituting yields the full Fourier formula
\[
\boxed{\quad F(A,B)=
\sum_{K\le\ker B}(-1)^{r_K}
q^{a\dim K+\binom{b-\dim K}{2}}
\prod_{j=a-b+\dim K+1}^{a-r_K}(q^j-1).\quad}
\]

**Step 3: unique lowest divisibility stratum.** Write \(c=\binom b2\). The contribution from \(K=\{0\}\) is
\[
S_{\{0\}}(A)=(-1)^{\operatorname{rank}A}q^c
\prod_{j=a-b+1}^{a-\operatorname{rank}A}(q^j-1).
\]
Since the product has exactly \(b-\operatorname{rank}A\) factors, each congruent to \(-1\) modulo \(q\), the quotient \(S_{\{0\}}(A)/q^c\) is congruent to \((-1)^b\) modulo \(q\). For any other kernel \(K\) with \(d=\dim K\ge1\), the displayed term has a factor \(q^{ad+\binom{b-d}{2}}\), and the exponent is
\[
ad+\binom{b-d}{2}=c+d(a-b)+\binom{d+1}{2}\ge c+1.
\]
Therefore all nonzero-kernel contributions disappear modulo \(q^{c+1}\), proving the claimed uniform congruence. In particular, every coefficient is divisible by \(q^c\) but not by \(q^{c+1}\), so none can be zero.

**Step 4: sharp singular value and cardinality.** The indicator of \(Z_{a,b}\) is invariant under \((X,Y)\mapsto(-X,-Y)\), so convolution is self-adjoint and its eigenvalues are the real integer Fourier coefficients. Since \(F(A,B)\) is a nonzero multiple of \(q^c\), every singular value is at least \(q^c\). Choose \(B:V\to W\) injective; then \(\ker B=0\), leaving only \(S_{\{0\}}(A)\). Choose \(A:W\to V\) surjective; its rank is \(b\), so the product is empty and \(|F(A,B)|=q^c\). The trivial frequency has eigenvalue \(|Z_{a,b}|\), which is the maximum Fourier modulus by the triangle inequality. Counting kernels \(K\) of each dimension \(d\), injective quotient maps \(V/K\to W\), and then all \(q^{ad}\) maps \(W\to K\), proves the displayed cardinality formula and exact condition number.

## Verification

The included `verify_zero_product_fourier.py` calculates the incidence indicator directly, then its **complete** additive character transform using exact integer Walsh arithmetic for characteristic two and exact Eisenstein-integer arithmetic for the three-element field. For the four-element field, it uses the polynomial relation \(\alpha^2=\alpha+1\) to multiply field elements and the binary Walsh transform of its additive group. It checks every frequency, the congruence, nonvanishing, smallest singular value, and largest singular value for the five cases
\[
(q,a,b)=(2,2,2),(2,3,2),(2,3,3),(3,2,2),(4,2,2).
\]
Run `python3 verify_zero_product_fourier.py` in a directory containing the checker. No third-party Python packages or floating-point thresholds are required. The exhaustive finite tests are consistency checks, not the proof for arbitrary sizes; that is Steps 1–4 above.

## Relationship to prior work

Gadouleau and Yan's rank-metric MacWilliams theory (2007) gives transforms of **one-matrix rank strata** and the associated generalized Krawtchouk coefficients. The exact-kernel transform here shares the same Gaussian-binomial mechanism, but the zero-product incidence condition couples **two independent matrices** through \(K\subseteq\ker B\), and the uniform divisibility and nowhere-zero Fourier conclusion are not stated by those rank-enumerator results.

Ram (2015) calls a pair \((C,A)\) a *zero kernel pair* when an intersection of kernels of \(CA^i\) is zero; this is an observability/reachability condition, not the product-zero relation \(XY=0\). Britnell–Wildon (2010) and Browning–Sawin–Wang (2024) treat **commuting** matrices and commutator character sums; commutation \(XY=YX\) is not product-zero. Finite rank-metric association-scheme methods might yield a different route to the kernel formula, but neither matching names nor general transform technology alone establishes the new global nonvanishing statement.

## Limitations

The proof is restricted to \(a\ge b\ge2\) and fields, and makes no assertion about the opposite rectangular range \(a<b\), nonfield rings, or nonlinear compositions. The spectral formula is a finite subspace sum rather than a small list of distinct eigenvalue multiplicities. A broader historical matrix-incidence or association-scheme identity could potentially imply the same conclusion; priority remains subject to further human literature assessment. Independent mathematical validation has not been performed.

## References

- M. Gadouleau and Z. Yan, *MacWilliams Identity for Codes with the Rank Metric*, arXiv:0706.1751, first public 2007-06-12; see Theorem 1 and Corollary 1, generalized Krawtchouk coefficients.
- S. Ram, *Counting zero kernel pairs over a finite field*, arXiv:1509.08053, first public 2015-09-27; see Definition 2.3 on page 3.
- J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811, first public 2010-01-06.
- T. Browning, W. Sawin and V. Y. Wang, *Pairs of commuting integer matrices*, arXiv:2409.01920, first public 2024-09-03; see section 3 on finite-field commutator sums.
