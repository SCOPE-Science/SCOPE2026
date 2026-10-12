# Complete Hamming spectra of top-degree Cartesian square-free codes

## Finding

Let \(q\ge2\) be any prime power, \(m\ge2\), and \(\mathbb F_q\) the field of order \(q\). Define the homogeneous square-free polynomials
\[
M_i(X)=\prod_{\substack{1\le j\le m\\j\ne i}}X_j,\qquad 1\le i\le m.
\]
The Cartesian square-free evaluation code is
\[
C=\big\{\big(f_a(x)\big)_{x\in\mathbb F_q^m}:a\in\mathbb F_q^m\big\},\qquad
f_a(X)=\sum_{i=1}^m a_i M_i(X).
\]
Here all \(q^m\) evaluation points are retained, including coordinates that vanish identically. Write \(t=q-1\). For \(1\le r\le m\), define the integer
\[
N_r=\frac{t^r+t(-1)^r}{q},\qquad
w_r=t^m-t^{m-r}N_r+r t^{m-1}.
\]
Then \(C\) has length \(q^m\), dimension \(m\), and complete Hamming weight enumerator
\[
\boxed{W_C(z)=1+\sum_{r=1}^{m}\binom mr(q-1)^r z^{w_r}.}
\]
For each nonzero coefficient vector \(a\), the weight depends only on the number \(r\) of its nonzero coefficients and equals \(w_r\). The summands must be combined when two weights coincide; in particular, \(w_1=w_2=q(q-1)^{m-1}\). Thus the minimum distance is \(q(q-1)^{m-1}\), attained by exactly
\[
m(q-1)+\binom m2(q-1)^2
\]
nonzero codewords. If \(q>2\), then \(w_2<w_3<\cdots<w_m\), giving exactly \(m-1\) different nonzero weights for \(m\ge3\). If \(q=2\), then \(w_r=r+(r\bmod2)\); the positive weights are \(2,4,\ldots,2\lceil m/2\rceil\).

For example, for \(q=3\), \(m=4\) the parameters are \([81,4,24]_3\) and
\[
W_C(z)=1+32z^{24}+32z^{36}+16z^{42}.
\]

## Assumptions and scope

The base set is the full Cartesian product \(\mathbb F_q^m\), not the multiplicative torus and not a proper Cartesian subset. The defining polynomials are precisely the \(m\) square-free monomials of homogeneous degree \(m-1\), with no lower-degree monomials. The alphabet may have nonprime prime-power cardinality; the argument requires only finite-field arithmetic and character orthogonality. The exponent in \(W_C\) records ordinary Hamming weight, not generalized Hamming weight.

## Proof

**Injectivity.** Fix \(1\le i\le m\). At the point with \(x_i=0\) and all other coordinates \(1\), one has \(M_i(x)=1\), while \(M_j(x)=0\) for all \(j\ne i\). Hence the evaluation map sends \(a\) to a word which records \(a_i\) at this coordinate. This holds for every \(i\), proving linear independence and dimension \(m\).

**Zero-count lemma.** For every \(r\ge1\), let \(N_r\) be the number of tuples \((y_1,\ldots,y_r)\in(\mathbb F_q^*)^r\) with \(y_1+\cdots+y_r=0\). The character-orthogonality identity
\[
\mathbf 1_{\{u=0\}}=\frac1q\sum_{\chi}\chi(u),
\]
where the sum ranges over all additive characters of \(\mathbb F_q\), gives
\[
N_r=\frac1q\sum_{\chi}\prod_{i=1}^r\sum_{y_i\in\mathbb F_q^*}\chi(y_i)
=\frac{t^r+(q-1)(-1)^r}{q}.
\]
Indeed, the trivial character sums to \(t\) over \(\mathbb F_q^*\), and each of the \(q-1\) nontrivial characters sums to \(-1\). Consequently \(N_r\) is an integer for every prime power \(q\).

**Evaluation stratification.** Fix \(a\) with precisely \(r\) nonzero entries. Every point having at least two zero coordinates satisfies \(f_a(x)=0\), because each \(M_i\) includes all but one variable. At a point with exactly one zero coordinate, at index \(i\), one has \(f_a(x)=a_i\prod_{j\ne i}x_j\); it is nonzero exactly when \(a_i\ne0\). Each such index contributes exactly \(t^{m-1}\) nonzero evaluation values. The total from these strata is \(r t^{m-1}\).

On the torus \((\mathbb F_q^*)^m\), factor
\[
f_a(x)=\left(\prod_{j=1}^m x_j\right)\sum_{i:a_i\ne0}\frac{a_i}{x_i}.
\]
For each nonzero \(a_i\), the substitution \(y_i=a_i/x_i\) permutes \(\mathbb F_q^*\). The remaining \(m-r\) coordinates have \(t^{m-r}\) possible values. Thus the torus has exactly \(N_r t^{m-r}\) zeros and \(t^m-N_rt^{m-r}\) nonzeros. Adding the contribution from points with one zero yields precisely \(w_r\). There are \(\binom mr t^r\) coefficient vectors with this support size, and injectivity ensures they give distinct codewords. Summing these contributions proves the enumerator.

**Weight collisions.** Using the displayed formula for \(N_r\), direct subtraction yields
\[
w_{r+1}-w_r=t^{m-1}+(-1)^r t^{m-r},\qquad1\le r<m.
\]
The first difference vanishes. For \(t\ge2\), every difference after the first is strictly positive. Therefore the only repeated positive weight is \(w_1=w_2=q t^{m-1}\), and this is the minimum. When \(t=1\), the differences are zero for odd \(r\) and two for even \(r\), giving \(w_r=r+(r\bmod2)\). These conclusions cover all boundary cases, including \(m=2\).

## Verification

The companion standard-library script `verify.py` constructs the full generator matrix directly from each finite field and enumerates all \(q^m\) coefficient vectors, independently of the character argument. It checks the predicted enumerator, support-dependent weight, and codeword total in 19 cases: \(q\in\{2,3,4,5,7,8\}\), with dimensions \(m=2\) through \(6\) where computationally feasible. It includes genuine extension-field arithmetic for \(q=4\) and \(q=8\). Running `python3 verify.py` produces `VERIFY_OK`. The infinite family is established by the symbolic proof, not by finite checks.

## Relationship to prior work

Carvalho, López, and San-José introduce Cartesian square-free evaluation codes and compute generalized Hamming-weight formulas, including the relevant homogeneous family. Their generalized-weight results specify minimum supports of subcodes, not the numbers of individual codewords having each weight. This note keeps their family and gives an explicit full weight enumerator and its coefficient-support classification. Earlier work by Patanker and Singh concerns square-free toric evaluation and generalized weights, and does not supply this full-affine enumerator. The present proof uses a direct character sum rather than a footprint bound.

## Limitations

This theorem treats only homogeneous degree \(m-1\) on the full affine grid. It does not classify the enumerators for intermediate square-free degrees or nonuniform Cartesian subsets. The formula counts Hamming weights, not complete symbol-composition enumerators. Coordinate positions with at least two zero input coordinates are identically zero and are retained in the stated code length. The originality comparison cannot exclude every older implicit identity in the broad character-sum or punctured-simplex literature; no priority or independent certification is asserted.

## References

1. C. Carvalho, H. H. López, and R. San-José, *Cartesian square-free codes*, arXiv:2511.08304v1, 11 November 2025, https://arxiv.org/html/2511.08304v1. Later open-access journal version: *Boletín de la Sociedad Matemática Mexicana* 32, article 125 (2026), DOI 10.1007/s40590-026-00963-5.
2. R. Patanker and D. K. Singh, *Generalized Hamming weights of toric codes over hypersimplices and square-free affine evaluation codes*, arXiv:2002.10920, https://arxiv.org/abs/2002.10920.
