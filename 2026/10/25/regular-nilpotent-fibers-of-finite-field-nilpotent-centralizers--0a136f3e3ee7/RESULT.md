# Regular-nilpotent fibers of finite-field nilpotent centralizers

## Finding

Let \(q\) be any prime power, let \(n\geq1\), and fix a nilpotent matrix \(A\in M_n(\mathbb F_q)\) of Jordan partition \(\lambda=(\lambda_1,\ldots,\lambda_k)\). Choose \(B\) uniformly from the **nilpotent centralizer**
\[
\mathcal N(A)=\{B\in M_n(\mathbb F_q):AB=BA,\ B^n=0\}.
\]
Write \(\Phi_m(q)=\prod_{j=1}^{m}(1-q^{-j})\), with \(\Phi_0(q)=1\). Call \(B\) *regular nilpotent* if its Jordan partition is \((n)\), equivalently its nilpotency index is \(n\).

**Theorem (exact regular-nilpotent fiber law).** The nilpotent centralizer has size
\[
|\mathcal N(A)|=q^{\sum_{i,j=1}^{k}\min(\lambda_i,\lambda_j)-k}.
\]
The probability that \(B\) is regular nilpotent is **zero** unless the largest and smallest parts of \(\lambda\) differ by at most one. If \(A\neq0\) and \(\lambda\) is almost rectangular, so that \(1\le k<n\) and
\[
\lambda=((h+1)^r,h^{k-r}),\qquad n=hk+r,\quad 0\le r<k,
\]
then
\[
\boxed{\Pr(B\text{ regular nilpotent})=\Phi_r(q)\Phi_{k-r}(q).}
\]
For \(A=0\), necessarily \(\lambda=(1^n)\), and the probability is instead
\[
\boxed{\Pr(B\text{ regular nilpotent})=\prod_{j=2}^{n}(1-q^{-j}).}
\]
The product for \(n=1\) is empty and equals one.

**Uniformity of the commuting-polynomial parameter.** Suppose \(A\neq0\) and \(\lambda\) is almost rectangular, with \(k<n\). Each regular nilpotent \(B\in\mathcal N(A)\) determines a *unique* polynomial \(f_B(t)\in\mathbb F_q[t]/(t^n)\) satisfying \(A=f_B(B)\). The polynomial has valuation exactly \(k\), and conditional on \(B\) being regular nilpotent it is *uniform* on the \((q-1)q^{n-k-1}\) polynomials
\[
f(t)=c_kt^k+c_{k+1}t^{k+1}+\cdots+c_{n-1}t^{n-1},\qquad c_k\neq0.
\]
In particular, the first nonzero coefficient is uniform on \(\mathbb F_q^\times\), and all subsequent coefficients are independent uniform elements of \(\mathbb F_q\). Each such polynomial is realized by exactly
\[
\boxed{\frac{|C_{\mathrm{GL}_n(\mathbb F_q)}(A)|}{(q-1)q^{n-1}}}
\]
regular nilpotent commuting matrices \(B\), where \(C_{\mathrm{GL}_n(\mathbb F_q)}(A)\) denotes the invertible centralizer.

The probability in the nonzero almost-rectangular case depends only on the number of Jordan blocks and the residue \(r=n\bmod k\), not on the common scale \(h\). For fixed \(q\), as \(k\to\infty\), a single repeated block size gives the limit \(\Phi_\infty(q)\); two adjacent sizes with both multiplicities tending to infinity give \(\Phi_\infty(q)^2\). The zero matrix gives the distinct limit \(\Phi_\infty(q)/(1-q^{-1})\).

## Assumptions and scope

All matrices act on an \(n\)-dimensional vector space over the explicitly specified finite field. The fixed operator \(A\) is nilpotent with arbitrary Jordan partition; no restriction on the characteristic is imposed. The random operator \(B\) is sampled uniformly from the finite set of **nilpotent** matrices commuting with \(A\), not from the entire associative centralizer or from the group of its units. The symbol \((h^m)\) means \(m\) Jordan blocks of size \(h\); no power of a matrix is intended in partition notation.

The exact count of the whole nilpotent centralizer and the existence of a regular commuting nilpotent are standard background ingredients; the asserted joint contribution is the full fixed-partition probability together with the equidistributed polynomial fibers and their size, including all boundary cases.

## Proof

**1. Necessary and sufficient Jordan shape.** If \(B\) is regular nilpotent, it is similar to the single Jordan block \(J_n\). Its full algebra centralizer is \(\mathbb F_q[B]\cong\mathbb F_q[t]/(t^n)\). Therefore any nilpotent \(A\) commuting with \(B\) equals \(f(B)\), with \(f\) divisible by \(t\). If \(A\neq0\), write \(f(t)=t^k u(t)\), where \(1\le k<n\) and \(u(0)\neq0\). For every integer \(j\ge1\), multiplication by the invertible operator \(u(B)^j\) does not change rank, so
\[
\operatorname{rank}(A^j)=\operatorname{rank}(B^{kj})=\max(n-kj,0).
\]
The sequence of ranks of nilpotent powers determines the Jordan partition, and this sequence is exactly that of \(J_n^k\): its \(k\) blocks have lengths \(h\) and \(h+1\), with \(n=hk+r\). Conversely, every nilpotent operator with this partition is conjugate to \(J_n^k\) and consequently commutes with a regular nilpotent operator. If \(A=0\), any regular nilpotent \(B\) commutes with it. This establishes the exact existence boundary, including \(n=1\).

**2. Number of nilpotent elements in the centralizer.** Regard the underlying vector space as a module over \(\mathbb F_q[t]\), with \(t\) acting as \(A\). It decomposes as \(\bigoplus_i\mathbb F_q[t]/(t^{\lambda_i})\). Its endomorphism algebra \(E\) is the full matrix centralizer of \(A\), and
\[
d=\dim_{\mathbb F_q}E=\sum_{i,j}\min(\lambda_i,\lambda_j),
\]
because \(\operatorname{Hom}_{\mathbb F_q[t]}(\mathbb F_q[t]/t^a,\mathbb F_q[t]/t^b)\) has dimension \(\min(a,b)\). Let \(m_s\) be the number of summands of length \(s\). The canonical map from \(E\) to the endomorphisms of the semisimple heads of the distinct indecomposable isotypic summands has quotient
\[
E/\operatorname{rad}(E)\cong\prod_s M_{m_s}(\mathbb F_q).
\]
To see this explicitly, the diagonal homomorphisms between equal-length indecomposables contribute their constant coefficients, while compositions of off-length homomorphisms returning to an initial length acquire positive powers of \(t\). Hence the discarded homomorphisms form a nilpotent ideal; the surviving constant matrices are exactly the displayed matrix factors. A finite-dimensional algebra element is nilpotent if and only if its image modulo a nilpotent ideal is nilpotent. Since \(M_m(\mathbb F_q)\) has exactly \(q^{m^2-m}\) nilpotent matrices (the classical Fine–Herstein count), it follows that
\[
|\mathcal N(A)|=q^{d-\sum_s m_s^2}\prod_s q^{m_s^2-m_s}
=q^{d-\sum_s m_s}=q^{d-k}.
\]
Likewise, an element of \(E\) is a unit precisely if each surviving constant matrix is invertible; thus
\[
|C_{\mathrm{GL}_n(\mathbb F_q)}(A)|=q^d\prod_s\Phi_{m_s}(q).
\]
These are baseline counts, not a new classification of centralizer algebras.

**3. Uniform-polynomial fiber bijection.** Let \(G=\mathrm{GL}_n(\mathbb F_q)\), fix \(J=J_n\), and fix any polynomial \(f\) of valuation exactly \(k<n\). By Step 1, \(f(J)\) is conjugate to the chosen \(A\). Each \(B\) of the form \(gJg^{-1}\) satisfies \(f(B)=A\) precisely when \(g f(J)g^{-1}=A\). There are exactly \(|C_G(A)|\) such elements \(g\): the set is a torsor for \(C_G(A)\). Two such \(g\) describe the same \(B\) exactly when they differ by an element of \(C_G(J)\). Therefore the fiber size is
\[
\frac{|C_G(A)|}{|C_G(J)|}
=\frac{|C_G(A)|}{(q-1)q^{n-1}}.
\]
For every regular nilpotent \(B\), the polynomial realizing \(A\) is unique modulo \(t^n\), since \(1,B,\ldots,B^{n-1}\) are linearly independent. The fibers for distinct \(f\) are therefore disjoint and exhaustive. There are exactly \((q-1)q^{n-k-1}\) possible polynomials, proving both exact equidistribution and
\[
\#\{B\in\mathcal N(A):B\text{ regular nilpotent}\}
=|C_G(A)|q^{-k}.
\]

**4. Probabilities and the zero boundary.** Divide the last formula by the nilpotent-centralizer count in Step 2. For nonzero almost-rectangular \(A\), its only possibly nonzero multiplicities are \(m_h=k-r\) and \(m_{h+1}=r\); their Euler factors give \(\Phi_{k-r}(q)\Phi_r(q)\). For \(A=0\), \(\mathcal N(A)\) is the entire set of nilpotent matrices, of size \(q^{n^2-n}\), and the regular nilpotent conjugacy class has size \(|G|/[(q-1)q^{n-1}]\). Their ratio is \(\Phi_n(q)/(1-q^{-1})=\prod_{j=2}^n(1-q^{-j})\). If \(\lambda\) is not almost rectangular, Step 1 gives an empty event. Finally, the three stated limits follow by convergence of the positive Euler product \(\Phi_\infty(q)\).

## Verification

The standalone file `check.py` exhaustively enumerates all matrices for \((q,n)=(2,1),(2,2),(2,3),(2,4),(3,2),(3,3),(4,2)\). Field order four is implemented as \(\mathbb F_2[z]/(z^2+z+1)\). For each nilpotent Jordan shape in those dimensions, it constructs \(A\), enumerates commuting nilpotent \(B\), determines regular nilpotency from the actual least vanishing power, and tests each asserted count and each polynomial fiber directly by matrix evaluation. There are 18 tested fixed-Jordan shapes, 5,192 nilpotent-centralizer elements counted with multiplicity across shapes, 3,293 regular-nilpotent occurrences, and 31 uniform-polynomial fibers. The exact replayed output is in `check_output.txt`. Run `python check.py` using Python 3. The program requires only the standard library.

For example, at \(q=2\), \(n=4\), and \(\lambda=(2,2)\), the theorem gives 64 nilpotent centralizer elements, 24 regular nilpotent elements, and exactly 12 matrices in each of the two polynomial fibers. At \(\lambda=(3,1)\), no commuting regular nilpotent exists. These examples are checked from actual matrices, not by substituting into the formulas alone.

## Relationship to prior work

The centralizer, commuting-Jordan-type, and almost-rectangular existence questions have a substantial literature. Bogdanić, Đurić, Koljančić, Oblak, and Šivic (arXiv:2212.08425, first posted 2022-12-16) classify **which** Jordan types can occur in the nilpotent centralizer of a matrix having two equal-length blocks; their work includes the existence of almost-rectangular types. Britnell and Wildon (arXiv:1001.0811) analyze when nilpotent similarity classes commute. Hua (arXiv:2305.00176) constructs simultaneous-similarity normal forms for commuting nilpotent pairs with two unequal-length blocks. Bondarenko, Futorny, Petravchuk, and Sergeichuk (arXiv:2012.04038) give normal forms when the joint kernel is one-dimensional. The present exact **fiber size and uniformity statement for every fixed Jordan partition**, together with the conditional probabilities and scale invariance, is not stated in those inspected results.

The Fine–Herstein formula for the total number of finite-field nilpotent matrices, and standard centralizer-unit cardinalities, are used as known inputs, not reannounced as discoveries. The general probability follows through a separate orbit/fiber calculation that keeps the fixed matrix, rather than merely the two similarity classes, under control.

## Limitations

The distribution concerns only the **regular-nilpotent** event; it does not determine the full Jordan-partition distribution inside an arbitrary nilpotent centralizer. The event can have probability zero. The finite checker is exhaustive only in its stated small dimensions; it is a cross-check rather than the proof for arbitrary \(n\). Priority is not certified: a general orbit-counting result or a specialized enumeration of nilpotent commuting pairs may implicitly contain the formula, even where searched materials do not present this parameterized law. No claim of independent review is made.

## References

1. D. Bogdanić, A. Đurić, S. Koljančić, P. Oblak, K. Šivic, *Jordan structures of nilpotent matrices in the centralizer of a nilpotent matrix with two Jordan blocks of the same size*, arXiv:2212.08425 (2022), https://arxiv.org/abs/2212.08425.
2. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811 (2010), https://arxiv.org/abs/1001.0811.
3. J. Hua, *Canonical forms for a class of pairs of commuting nilpotent matrices under simultaneous similarity*, arXiv:2305.00176 (2023), https://arxiv.org/html/2305.00176v1.
4. V. M. Bondarenko, V. Futorny, A. P. Petravchuk, V. V. Sergeichuk, *Pairs of commuting nilpotent operators with one-dimensional intersection of kernels and matrices commuting with a Weyr matrix*, arXiv:2012.04038 (2020), https://arxiv.org/abs/2012.04038.
5. M. Gerstenhaber, *On the number of nilpotent matrices with coefficients in a finite field*, Illinois J. Math. 5 (1961), 330–333, https://doi.org/10.1215/ijm/1255629831 (re-proves the Fine–Herstein count).
6. SageMath, *Similarity class types of matrices with entries in a finite field*, documentation for nilpotent-matrix centralizer group cardinalities, https://doc.sagemath.org/html/en/reference/combinat/sage/combinat/similarity_class_type.html.
