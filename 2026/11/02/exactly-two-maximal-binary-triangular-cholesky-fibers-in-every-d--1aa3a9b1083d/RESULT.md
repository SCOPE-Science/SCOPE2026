# Exactly two maximal binary triangular Cholesky fibers in every dimension

## Finding

For every integer \(n\geq 1\), put \(T_n=\{U\in M_n(\mathbb F_2): U_{ij}=0\text{ if }i>j\}\) and \(G_n=\operatorname{Sym}_n(\mathbb F_2)\). For a target \(A\in G_n\), let
\[
\nu_n(A)=\#\{U\in T_n:U^{\mathsf T}U=A\}.
\]
Write \(E_{nn}\) for the symmetric matrix with its sole nonzero entry at position \((n,n)\). **The exact maximum-fiber theorem** is
\[
\boxed{\nu_n(A)\leq\nu_n(0),\qquad
\nu_n(A)=\nu_n(0)\iff A\in\{0,E_{nn}\}.}
\]
Furthermore, \(\nu_n(A)=\nu_n(A+E_{nn})\) for every target. If \(G_n\) is regarded as an additive group, the function \(\nu_n:G_n\to\mathbb Z_{\geq0}\) has a **nonnegative Fourier transform**; its strictly positive Fourier characters span the codimension-one annihilator of \(E_{nn}\). This Fourier statement is stronger than mere maximality and gives the exact equality cases.

The known zero-fiber cardinalities for dimensions \(1,2,3,4,5\) are \(1,2,6,28,192\), respectively. This finding does not claim those counts as new; it determines where the global maximum occurs among **all** symmetric targets, for **every** dimension.

## Assumptions and scope

All scalars are in \(\mathbb F_2\); the upper triangular constraint uses the fixed coordinate order. The target space comprises every symmetric binary matrix, whether or not the target admits a Cholesky root. The theorem holds for every \(n\ge1\), with no genericity, rank, invertibility, or diagonal assumption. Matrix addition is over \(\mathbb F_2\).

For the Fourier argument, set \(N=n(n+1)/2\). Regard symmetric matrices as binary coordinate vectors indexed by \(1\le i\le j\le n\). The Fourier characters are
\[
\chi_{\lambda}(A)=(-1)^{\sum_{1\le i\le j\le n}\lambda_{ij}A_{ij}},
\]
where \(\lambda\) ranges independently through \(N\) binary coefficients. This *coordinate pairing* is intentional; in characteristic two it must not be replaced by the matrix trace pairing, which would erase the off-diagonal coordinates.

## Proof

**1. Rowwise convolution.** Let \(V_i=\{v\in\mathbb F_2^n:v_1=\cdots=v_{i-1}=0\}\). The independent rows of any \(U\in T_n\) are precisely the elements \(v_i\in V_i\), and
\[
U^{\mathsf T}U=\sum_{i=1}^{n}v_iv_i^{\mathsf T}.
\]
For a character \(\lambda\), define the Boolean quadratic polynomial
\[
Q_{\lambda}(v)=\sum_{1\le a\le b\le n}\lambda_{ab}v_av_b,
\]
and the suffix Gauss sums
\[
g_i(\lambda)=\sum_{v\in V_i}(-1)^{Q_{\lambda}(v)}.
\]
The unnormalized Fourier transform of the fiber-count function factors exactly:
\[
\widehat\nu_n(\lambda)=\sum_{A\in G_n}\nu_n(A)\chi_\lambda(A)=\prod_{i=1}^{n}g_i(\lambda).
\]
This equality is an identity obtained by substituting the rows, not a heuristic or a sampled pattern.

**2. A flat-magnitude lemma for Boolean quadratic Gauss sums.** Let \(Q:W\to\mathbb F_2\) be any quadratic polynomial on an \(m\)-dimensional binary vector space whose constant term is zero; let \(B(x,y)=Q(x+y)+Q(x)+Q(y)\) be its polar bilinear form and \(R=\{h:B(h,x)=0\ \forall x\}\) its radical. For each linear form \(\ell\), put \(S(\ell)=\sum_{x\in W}(-1)^{Q(x)+\ell(x)}\). Then
\[
S(\ell)^2=2^m\sum_{h\in R}(-1)^{Q(h)+\ell(h)}.
\]
Indeed, substitute \(h=x+y\) in the double sum defining \(S(\ell)^2\); summation over \(x\) vanishes unless \(h\in R\). The restriction of \(Q+\ell\) to \(R\) is linear, so its character sum is either \(0\) or \(|R|\). Thus
\[
\boxed{|S(\ell)|\in\{0,\,2^{(m+\dim R)/2}\}}.
\]
In particular, if \(S(0)>0\), then \(|S(\ell)|\le S(0)\) for **every** linear form \(\ell\). The same statement is valid in dimension zero.

**3. Positivity of the full Fourier spectrum.** For each \(i<n\), write the suffix variables as \((s,y)\) with \(s=v_i\) and \(y\in V_{i+1}\), and write
\[
Q_{\lambda}(s,y)=Q_{\lambda}(0,y)
+s\Bigl(\lambda_{ii}+\sum_{j>i}\lambda_{ij}y_j\Bigr).
\]
Consequently,
\[
g_i(\lambda)=g_{i+1}(\lambda)
+(-1)^{\lambda_{ii}}\sum_{y\in V_{i+1}}
(-1)^{Q_\lambda(0,y)+\sum_{j>i}\lambda_{ij}y_j}.
\]
The last suffix sum is \(g_n(\lambda)=1+(-1)^{\lambda_{nn}}\in\{0,2\}\). If \(g_{i+1}(\lambda)>0\), the flat-magnitude lemma bounds the absolute value of the second term by \(g_{i+1}(\lambda)\), so \(g_i(\lambda)\ge0\). Iterating backward, either one factor vanishes or **all** factors are positive. Therefore
\[
\boxed{\widehat\nu_n(\lambda)\ge0\quad\text{for every }\lambda.}
\]

**4. Identification of the positive Fourier span.** Since \(g_n=0\) when \(\lambda_{nn}=1\), every positive Fourier character has \(\lambda_{nn}=0\). Conversely, consider any indices \(i<j\). If the only nonzero coefficient is \(\lambda_{ij}=1\), then \(Q_\lambda(v)=v_iv_j\). Every suffix Gauss sum is strictly positive: suffixes containing both variables contribute the positive two-variable sum \(2\), and later suffixes have constant character \(+1\). Thus this off-diagonal coordinate character has positive Fourier coefficient.

If \(i<n\), take instead \(\lambda_{ii}=\lambda_{i,i+1}=1\), all other coefficients zero. Here \(Q_\lambda(v)=v_i+v_iv_{i+1}\). The two-variable sign sum is again \(2>0\), and every suffix sum is positive. The corresponding character is positive. Subtracting (equivalently, adding over \(\mathbb F_2\)) the preceding off-diagonal coefficient produces the character supported only on diagonal coordinate \((i,i)\). Therefore the linear span of all strictly positive Fourier indices is exactly
\[
H=\{\lambda:\lambda_{nn}=0\},
\]
a subspace of codimension one in the \(N\)-dimensional character space. The argument also covers \(n=1\): then \(H=\{0\}\).

**5. Sharp maximum and equality.** Fourier inversion, with the above unnormalized convention, gives
\[
\nu_n(0)-\nu_n(A)
=2^{-N}\sum_\lambda\widehat\nu_n(\lambda)
\bigl(1-\chi_\lambda(A)\bigr)\ge0.
\]
All summands are nonnegative. Equality holds precisely when every character with strictly positive Fourier coefficient takes value \(+1\) on \(A\). The positive indices span \(H\), so this means that \(A\) lies in its annihilator, \(H^\perp=\{0,E_{nn}\}\). This proves both optimality and the **only** equality cases, without enumerating targets or assuming an unproved monotonicity principle. Finally, complementing the single triangular entry \(U_{nn}\) toggles exactly the entry \((U^{\mathsf T}U)_{nn}\); it gives a bijection between the fibers of \(A\) and \(A+E_{nn}\). Thus the paired-fiber statement holds for every target. \(\square\)

## Verification

Two standalone standard-library Python programs provide independent finite corroboration.

Run `python verify.py`. It enumerates every upper triangular matrix through dimension five; independently takes an integer Walsh–Hadamard transform of the complete fiber array; recomputes every Fourier coefficient as the product of rowwise quadratic Gauss sums; verifies that all coefficients are nonnegative; checks the positive Fourier span has rank \(N-1\); and determines the exact maximizers. It additionally checks the flat quadratic Gauss-magnitude property for every quadratic polynomial in up to four binary variables.

Run `python verify_recursion.py`. It uses a separate memoized first-pivot recurrence and compares **every** symmetric target with direct enumeration through dimension five. Both programs end in `VERIFY_OK`. Their exact recorded outputs appear in `verification/verify_output.txt` and `verification/recursion_output.txt`. These finite checks corroborate, but do not replace, the proof for all dimensions.

## Relationship to prior work

Wu and Zhou, *Singular Cholesky Fibers over Finite Fields* (first posted September 1, 2026, arXiv:2609.00533v1), establish a fixed-target recursion, an explicit binary zero-fiber bijection, and zero-fiber rank distributions. Their Theorem 3.1 is compatible with this result and can independently check finite cases, but the inspected article does not state the global maximum over all targets, its two equality cases, or nonnegative Fourier spectrum. Cooper and Whitlatch, *Counting Cholesky factorizations of the zero matrix over* \(\mathbb F_2\) (first posted December 13, 2025, arXiv:2512.12496v1), determine the zero-fiber count and give a count for the restricted leading-principal-nonsingular form. Their Corollary 2 is not a uniform bound for arbitrary targets and does not determine the global maximizing set. Earlier work of Whitlatch (arXiv:2109.06130) studies the zero fiber. Known zero-fiber counts are not claimed as new.

The structural contribution here is the *Fourier positivity and positive-support span*, yielding an exact all-target extremal classification. Search and source inspection cannot rule out every implicit consequence of older quadratic Gauss-sum literature; priority is not asserted absolutely.

## Limitations

The theorem is specific to \(\mathbb F_2\) and the standard upper triangular flag. It does not claim the same maximal targets over extension fields, odd finite fields, or under arbitrary changes of flag. Its zero-fiber cardinalities come from existing literature; no new closed formula for these numbers is claimed. The computational checks stop at dimension five. No independent external mathematical audit has been performed.

## References

1. H. Wu and K. Zhou, *Singular Cholesky Fibers over Finite Fields*, arXiv:2609.00533v1, 2026-09-01. https://arxiv.org/html/2609.00533v1
2. J. Cooper and H. Whitlatch, *Counting Cholesky factorizations of the zero matrix over* \(\mathbb F_2\), arXiv:2512.12496v1, 2025-12-13. https://arxiv.org/pdf/2512.12496
3. H. Whitlatch, *On the Number of Cholesky Roots of the Zero Matrix over* \(\mathbb F_2\), arXiv:2109.06130, 2021-09-13. https://arxiv.org/abs/2109.06130
4. OEIS A008964, binary upper triangular square-zero counts, https://oeis.org/A008964
