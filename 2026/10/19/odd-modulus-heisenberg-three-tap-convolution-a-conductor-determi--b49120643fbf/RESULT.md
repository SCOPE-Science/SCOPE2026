# Odd-modulus Heisenberg three-tap convolution: a conductor determinant and exact kernel law

## Finding

Let \(n\ge3\) be odd, let \(H_n=H(\mathbb Z/n\mathbb Z)\), and let \(X,Y\) be the standard noncommuting unit generators defined below. For every \((a,b,c)\in\mathbb C^3\), define the left-convolution operator \(T_{a,b,c}=aI+bL_X+cL_Y\) on \(\mathbb C[H_n]\). For \(t\ge1\), write \(\mu_t=\{z\in\mathbb C:z^t=1\}\), and let \(\varphi\) denote Euler's totient. The exact group determinant is

\[
\det T_{a,b,c}=\prod_{m\mid n}\prod_{\eta,\theta\in\mu_{n/m}}
 (a^m+b^m\eta+c^m\theta)^{m\varphi(m)}.
\]

When \((a,b,c)\ne(0,0,0)\), its exact complex nullity is

\[
\dim_{\mathbb C}\ker T_{a,b,c}=\sum_{m\mid n}m\varphi(m)
\#\{(\eta,\theta)\in\mu_{n/m}^2:a^m+b^m\eta+c^m\theta=0\}.
\]

In particular, the **unweighted generating three-tap operator** \(I+L_X+L_Y\) is invertible exactly when \(3\nmid n\); otherwise its kernel dimension is

\[
2\sum_{m\mid n/3}m\varphi(m)
=2\prod_{p^k\parallel n/3}\frac{p^{2k+1}+1}{p+1}.
\]

(The empty product is one.) The formula includes moduli with several distinct odd prime factors. For example, at \(n=3,9,15,27\) the respective complex nullities are \(2,14,42,122\), whereas at \(n=5,7\) the operators are invertible.

## Assumptions and scope

Write a group element as \((x,y,z)\in(\mathbb Z/n\mathbb Z)^3\), with product

\[
(x,y,z)(x',y',z')=(x+x',y+y',z+z'+xy').
\]

Then \(X=(1,0,0)\), \(Y=(0,1,0)\), and \(Z=[X,Y]=(0,0,1)\) satisfy \(XY=ZYX\) and \(X^n=Y^n=Z^n=e\). The operator \(L_g\) is left multiplication by \(g\) in the regular representation; it sends \(\delta_h\) to \(\delta_{gh}\). All ranks and nullities are over \(\mathbb C\). The displayed nullity formula excludes the all-zero coefficient triple, for which the operator is zero and the nullity equals \(n^3\). No analogous formula for even \(n\) is asserted.

## Proof

**(1) Exhaust the irreducible representations.** For every divisor \(m\mid n\), put \(t=n/m\). Choose a primitive \(m\)-th root \(\omega\) for the scalar action of \(Z\), and choose \(\eta,\theta\in\mu_t\). Pick \(\alpha,\beta\in\mathbb C\) with \(\alpha^m=\eta\) and \(\beta^m=\theta\). On an \(m\)-dimensional space with basis \(e_0,\ldots,e_{m-1}\), define

\[
Ue_j=\alpha e_{j+1\ (\mathrm{mod}\ m)},\qquad
Ve_j=\beta\omega^{-j}e_j.
\]

Then \(UV=\omega VU\), \(U^m=\eta I\), \(V^m=\theta I\), and \(U^n=V^n=I\). Consequently \(X\mapsto U\), \(Y\mapsto V\), \(Z\mapsto\omega I\) defines a representation of \(H_n\). It is irreducible: the \(m\) distinct eigenvalues of \(V\), cyclically permuted by \(U\), force every invariant subspace to be either zero or the full space. These representations are inequivalent whenever their central character \(\omega\), or the scalars \(\eta,\theta\), differ. For fixed \(m\), there are exactly \(\varphi(m)t^2\) such representations. Their squared dimensions sum to

\[
\sum_{m\mid n}\varphi(m)t^2m^2
=n^2\sum_{m\mid n}\varphi(m)=n^3=|H_n|.
\]

Thus they exhaust all complex irreducibles. The argument also covers \(m=1\), where the representation is one-dimensional.

**(2) Compute each determinant.** For \(m=1\) the determinant is immediately \(a+b\eta+c\theta\). For \(m>1\), the matrix \(aI+bU+cV\) is a diagonal matrix plus one cyclic shift. Exactly two permutations can contribute to its determinant: the identity and the full \(m\)-cycle. Since \(m\) is odd, their signs are positive; the first contributes

\[
\prod_{j=0}^{m-1}(a+c\beta\omega^{-j})=a^m+c^m\theta,
\]

and the second contributes \(b^m\eta\). Consequently

\[
\det(aI+bU+cV)=a^m+b^m\eta+c^m\theta.
\]

Regular-representation multiplicity equals the irreducible dimension \(m\). Multiplying these determinants with multiplicity \(m\) gives the asserted factorization, with an additional \(\varphi(m)\) from the central characters. This derives an equality of polynomials in \(a,b,c\), including singular cases.

**(3) Establish the exact block-nullity rule.** For \(m>1\) and \(b\ne0\), deleting an appropriate row and column of \(aI+bU+cV\) produces an \((m-1)\)-square triangular submatrix whose determinant is \((b\alpha)^{m-1}\ne0\). Thus a singular block has rank exactly \(m-1\). If \(b=0,c\ne0\), the \(m\) diagonal entries \(a+c\beta\omega^{-j}\) are distinct, so again a singular block has nullity one. If \(b=c=0\) and \(a\ne0\), no block is singular. The assertion for \(m=1\) is immediate. Taking the regular multiplicity \(m\), then summing the indicator of singularity over \(\omega,\eta,\theta\) gives the exact weighted nullity formula.

**(4) Evaluate the unweighted root-of-unity equation.** When \(a=b=c=1\), a block is singular iff \(1+\eta+\theta=0\). Three unit vectors add to zero exactly when \(\eta,\theta\) are the two primitive third roots in opposite order. There are therefore exactly two ordered pairs if \(3\mid t\), and none otherwise. Summing \(m\varphi(m)\) over \(m\mid n/3\) yields the nullity. Finally, the divisor sum \(F(N)=\sum_{m\mid N}m\varphi(m)\) is multiplicative, and direct geometric summation yields \(F(p^k)=(p^{2k+1}+1)/(p+1)\) for each prime power. This proves the product expression and the invertibility dichotomy.

## Verification

The accompanying standalone program `verify.cpp` builds each \(n^3\)-square integer left-regular convolution matrix explicitly and performs finite-field Gaussian elimination over the verified prime \(1004221\). For \(n\in\{3,5,7,9\}\) and coefficient triples \((1,1,1)\) and \((2,3,5)\), it also independently computes the conductor factorization using roots of unity modulo the prime. All eight determinant comparisons agree. The unweighted nullities are respectively \(2,0,0,14\) in these dimensions. These finite checks corroborate, but do not replace, the representation-theoretic proof for all odd moduli. Run using `g++ -std=c++17 -O3 verify.cpp -o verify && ./verify`; the program fails if a determinant comparison or checked expected nullity fails.

## Relationship to prior work

DeDeo, Martínez, Medrano, Minei, Stark and Terras (dated author preprint 19 September 2002; published 2003) construct and enumerate irreducible representations of finite Heisenberg groups over prime-power rings, and study spectra primarily of undirected **four-generator** Cayley graphs. Their representation method supplies the key prior framework, but does not report this **directed generating three-tap** determinant, conductor-resolved weighted kernel formula, or composite-odd-modulus arithmetic nullity law. See especially their Proposition 1 and Sections 2–3.

Mossinghoff and Pinner (arXiv:2108.04870, first public 10 August 2021) give the general Frobenius factorization for the prime-order Heisenberg group and a binomial-in-one-generator determinant identity (their Section 3.1, equation (9)). The \(n=p\) determinant instance here is a direct special case of that identity, and is not claimed as new. The contribution being distinguished is the closed divisor-conductor formula for **arbitrary odd composite moduli** and the exact arithmetic nullity formula, in contrast with that prime case.

Previously established weighted three-tap spectral formulas on exponent-prime Heisenberg groups also cover the \(n=p\) case (including its unweighted nullity), but do not treat exponent-prime-power or general odd composite-ring Heisenberg groups. The published research record on three-tap convolution on ternary extraspecial Heisenberg groups independently includes the \(n=3\) two-dimensional kernel case; no novelty is asserted for these specializations. Results on central representation-degree projectors for \(H(\mathbb Z/n\mathbb Z)\) concern different operators and do not give the present three-tap determinant or singular-block counts.

## Limitations

This theorem does not cover even moduli or arbitrary three-site supports with nongenerating projected differences. The formula is for complex convolution, not spectral stability or condition numbers; a nonzero determinant may be very small for a parameter family. It does not classify Jordan blocks or individual nonzero eigenvalues. Classical finite Heisenberg representation theory and prime-case group determinants are essential cited inputs; the claimed distinction is the exact specialization, divisor summation and singularity classification across all odd moduli. An equivalent older computation in a source not retrieved could still affect publication priority.

## References

1. M. DeDeo, M. Martínez, A. Medrano, M. Minei, H. Stark, A. Terras, *Spectra of Heisenberg Graphs over Finite Rings: Histograms, Zeta Functions and Butterflies*, dated preprint 19 September 2002; revised proceedings *Spectra of Heisenberg graphs over finite rings* (2003), DOI `10.3934/proc.2003.2003.213`. Author preprint: https://mathweb.ucsd.edu/~aterras/heis.pdf.
2. M. J. Mossinghoff, C. Pinner, *The Integer group determinants for the Heisenberg group of order p cubed*, arXiv:2108.04870 (posted 10 August 2021), Section 3.1. https://arxiv.org/html/2108.04870v1.
3. M. Misaghian, *The Representations of The Heisenberg Group over a Finite Field*, Armenian Journal of Mathematics **3** (2011), 162–173. https://armjmath.sci.am/index.php/ajm/article/view/78.
