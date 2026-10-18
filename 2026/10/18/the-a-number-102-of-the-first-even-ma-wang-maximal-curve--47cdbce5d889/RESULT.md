# The \(a\)-number \(102\) of the first even Ma–Wang maximal curve

## Finding
Let \(k=\mathbb F_{3^8}\), choose \(c\in k^*\) satisfying \(c^{81}=-c\), and let \(X/k\) be the smooth projective normalization of the Kummer curve
\[
 z^{82}=c(u^3-u)\bigl(1+(u^3-u)^2\bigr)^{13}.
\]
Then \(X\) has genus \(324\), and over an algebraic closure its Jacobian has exactly
\[
 \boxed{a(\operatorname{Jac}(X))=102}.
\]
Equivalently, the Cartier operator on \(H^0(X_{\overline{k}},\Omega^1)\) has rank \(222\). The curve is the smallest even-index member \((q,n)=(3,4)\) in the recently introduced Ma–Wang maximal-curve construction. Genus and maximality are established in the originating paper; the exact Cartier rank and \(a\)-number are the new assertions.

## Assumptions and scope
All Cartier calculations take place in characteristic \(3\) over \(\overline{k}\), and depend only on the displayed Kummer function field. The coefficient \(c\ne0\) scales each Cartier block by a nonzero scalar, so it does not change its rank. The \(a\)-number is \(\dim_{\overline{k}}\operatorname{Hom}(\alpha_3,\operatorname{Jac}(X)[3])\), equal to the dimension of the kernel of Cartier on regular differentials. The smooth normalization is essential: differential calculations are made in the function field, not on the singular affine plane model.

Set \(A=u^3-u\), \(B=1+A^2\), and \(m=82\). The functions \(A\) and \(B\) have respectively three and six simple, disjoint geometric roots, all in \(\mathbb F_9\). The ten branch places of \(X\to\mathbb P^1_u\) are these nine roots and infinity. All are totally ramified because the orders of the radicand there are \(1,13,-81\), each coprime to \(82\). Riemann–Hurwitz gives \(2g-2=-164+10(81)=646\), hence \(g=324\), agreeing with the originating paper.

## Proof
**Regular-differential basis.** For each \(1\le j\le81\) write
\[
 a_j=\left\lfloor\frac{13j}{82}\right\rfloor,\qquad
 d_j=\max\{0,j-1-6a_j\}.
\]
A basis of the \(j\)-th Kummer character space of regular differentials is
\[
 \omega_{j,s}=u^s B^{a_j}\frac{du}{z^j},\qquad 0\le s<d_j.
\]
At a simple root of \(A\), the valuations of \(z,du\) are \(1,81\); hence every \(j\le81\) is allowed. At a root of \(B\), the valuations of \(z,du,B\) are \(13,81,82\). Thus regularity forces the factor \(B^{\lfloor13j/82\rfloor}\). At infinity,
\[
 (v_\infty(u),v_\infty(z),v_\infty(du),v_\infty(B))=(-82,-81,-83,-492).
\]
The inequality \(v_\infty(\omega_{j,s})\ge0\) reduces to \(s\le j-2-6a_j\), giving precisely \(d_j\) admissible monomials. Character spaces are independent and the arithmetic sum \(\sum_{j=1}^{81}d_j=324=g\), so the displayed forms constitute a full regular-differential basis.

**The Cartier blocks.** For every \(j\) there is a unique \(j'=55j\pmod{82}\) with \(1\le j'\le81\), because \(3\cdot55\equiv1\pmod{82}\). Define \(t_j=(3j'-j)/82\in\{0,1,2\}\) and \(h_j=a_j+13t_j\). From the defining equation,
\[
 z^{-j}=z^{-3j'}\,c^{t_j}A^{t_j}B^{13t_j}.
\]
The Cartier identities \(\mathcal C(f^3\eta)=f\mathcal C(\eta)\) and
\[
 \mathcal C_{\mathbb F_3(u)}\!\left(\sum_e b_eu^e\,du\right)
  =\sum_{\ell\ge0}b_{3\ell+2}^{1/3}u^\ell\,du
\]
give the exact image
\[
 \mathcal C(\omega_{j,s})=c^{t_j/3}z^{-j'}
 \mathcal C_{\mathbb F_3(u)}\!\left(u^s A^{t_j}B^{h_j}\,du\right).
\]
By regularity, the polynomial in the output is divisible by \(B^{a_{j'}}\), and the quotient has degree less than \(d_{j'}\). Its coefficients define a \(d_{j'}\times d_j\) Cartier block over \(\mathbb F_3\). Since the map \(j\mapsto j'\) permutes \(1,\ldots,81\), images of distinct source blocks lie in distinct target character spaces; their ranks add.

**Exact coefficient and rank certificate.** With \(h=h_j\), the coefficient of \(u^{3\ell+2}\) in \(u^sA^{t_j}B^h\) is the following *finite integer sum reduced modulo three*:
\[
 \sum_{\substack{0\le v\le h,\ 0\le i\le 2v+t_j\\
                  s+2v+t_j+2i=3\ell+2}}
 (-1)^{2v+t_j-i}\binom{h}{v}\binom{2v+t_j}{i}
 \pmod 3.
\]
This follows from \(B^h=(1+A^2)^h\) and \(A^{2v+t_j}=u^{2v+t_j}(u^2-1)^{2v+t_j}\). Multiplication by the common nonzero polynomial \(B^{a_{j'}}\) is injective on the polynomial ring; therefore the rank of the raw coefficient columns equals that of the divided output block. This permits two genuinely different implementations of the rank calculation: polynomial arithmetic with exact division and a coefficient-by-coefficient binomial sum without division.

The complete rank table for \(j=1,\dots,81\) is embedded in `cartier_blocks.csv`. Over \(\mathbb F_3\), exact row reductions of the displayed coefficient matrices give
\[
 \sum_{j=1}^{81}\operatorname{rank}(\mathcal C_j)=222.
\]
Together with the basis dimension \(324\), this proves \(a(X)=324-222=102\).

## Verification
The archive includes `verify_cartier_polynomial.py`, which constructs each polynomial \(u^sA^{t_j}B^{h_j}\), extracts the degrees congruent to \(2\bmod3\), checks the divisibility by \(B^{a_{j'}}\), checks the output degree limit, and computes exact ranks over \(\mathbb F_3\). The independent `verify_cartier_binomial.py` builds matrices directly from the binomial sum and verifies every entry of the 81-row certificate. Both return genus \(324\), Cartier rank \(222\), and \(a\)-number \(102\). Run `python3 verify_cartier_polynomial.py` and `python3 verify_cartier_binomial.py` in the directory containing the files. An additional `verify_fourth_iterate.py` confirms \(\mathcal C^4=0\) by exact block-matrix multiplication, consistent with the established maximality of this curve over \(\mathbb F_{3^8}\). All reported computations are exact finite-field arithmetic, not heuristic floating-point tests.

## Relationship to prior work
Ma and Wang introduce the Kummer model, prove its genus and maximality, and study the absence of Hermitian coverings and a subgroup of automorphisms; their inspected manuscript does not discuss Cartier rank or the \(a\)-number. The earlier Beelen–Montanucci construction is restricted to odd indices and does not supply this even-index invariant. Elkin establishes general bounds and a Cartier-block method for Kummer covers, which this proof uses conceptually. Evaluating the cited general rank bounds using the current \(d_j\) yields the interval \(151\le\operatorname{rank}\mathcal C\le242\), not the exact number \(222\). The specific rank evaluation and its exact certificate are not claimed in those sources. This is an explicit arithmetic application of classical Cartier theory, not a new general theorem about all Kummer covers.

## Limitations
This establishes the exact geometric \(a\)-number only for the parameter pair \((q,n)=(3,4)\). It does not determine the entire Ekedahl–Oort type, the full \(3\)-torsion group scheme, or a uniform formula for all Ma–Wang curves. The three included verifiers independently calculate the same finite coefficient data but are not a machine-formalized proof of the differential-basis construction. The originality assessment cannot exclude an equivalent unpublished calculation or an unindexed specialized table. Self-review is distinct from independent expert verification.

## References
1. L. Ma and Y. Wang, *A new family of maximal curves not covered by the Hermitian curve*, arXiv:2609.19546v1 (first public 2026-09-17), https://arxiv.org/abs/2609.19546 .
2. A. Elkin, *The Rank of the Cartier operator on cyclic covers of the projective line*, arXiv:0708.0431; *Journal of Algebra* 327 (2011), 1–12, https://arxiv.org/abs/0708.0431 .
3. P. Beelen and M. Montanucci, *A new family of maximal curves*, *Journal of the London Mathematical Society* 98 (2018), 573–592, https://doi.org/10.1112/jlms.12144 .
