# The exact zeta function of Schur’s quartic in characteristic five

## Finding
Let \(S\subset\mathbb P^3_{\mathbb F_5}\) be the Schur quartic defined by
\[
X^4-XY^3=Z^4-ZW^3.
\]
It is smooth and therefore is a K3 surface. Its numbers of rational points are
\[
\#S(\mathbb F_5)=36,\qquad \#S(\mathbb F_{25})=1176.
\]
The latter count is the exact K3 Weil upper bound \(1+25^2+22\cdot25\). For every integer \(m\ge1\),
\[
\boxed{\#S(\mathbb F_{5^m})=5^{2m}+1+5^m(12+10(-1)^m).}
\]
Equivalently, the Frobenius characteristic polynomial on second \(\ell\)-adic cohomology (\(\ell\ne5\)) is \((U-5)^{12}(U+5)^{10}\), and
\[
\boxed{Z(S/\mathbb F_5,T)=\frac1{(1-T)(1-25T)(1-5T)^{12}(1+5T)^{10}}.}
\]
The Tate theorem for K3 surfaces in odd characteristic then gives geometric Picard number \(22\), so the reduction is supersingular in the sense of Artin.

## Assumptions and scope
The equation is considered over the prime field \(\mathbb F_5\), with its stated integral coefficients and no unrecorded change of model or quadratic twist. Every extension is \(\mathbb F_{5^m}\), \(m\ge1\). This is a zeta and point-count theorem for this explicit arithmetic model, not a classification of all quartic K3 forms. Geometric Picard rank uses the established Tate theorem; no Artin invariant is claimed.

## Proof
**1. Smooth K3 surface.** Write \(f(A,B)=A^4-AB^3\). The four partial derivatives of \(f(X,Y)-f(Z,W)\) are
\[
4X^3-Y^3,\quad -3XY^2,\quad -4Z^3+W^3,\quad 3ZW^2.
\]
In characteristic five, the first two vanish simultaneously only for \(X=Y=0\): if \(XY^2=0\), then either \(X=0\) forces \(Y=0\), or \(Y=0\) forces \(X=0\). The same reasoning applies to the last two. Thus the projective hypersurface is smooth. A smooth quartic surface in \(\mathbb P^3\) is a K3 surface, and its second \(\ell\)-adic Betti number is \(22\).

**2. Fiber identity.** For every finite field \(k\) of order \(q\) and \(v\in k\), let \(n_v=\#\{(a,b)\in k^2:f(a,b)=v\}\). Counting nonzero quadruples modulo the free scalar action gives
\[
\#S(k)=\frac{\sum_{v\in k}n_v^2-1}{q-1}.
\]

**3. Prime field.** Over \(\mathbb F_5\), every nonzero fourth power equals one and the cube map on \(\mathbb F_5^\times\) is bijective. At \(v=0\), there are five pairs with \(a=0\), and four additional pairs with \(a\ne0\) and \((b/a)^3=1\), so \(n_0=9\). For each \(v\ne0\), the expression \(f(a,b)=a^4(1-(b/a)^3)\) gives \(n_v=4\). Therefore
\[
\#S(\mathbb F_5)=\frac{9^2+4\cdot4^2-1}{4}=36.
\]

**4. Quadratic field.** Use \(\mathbb F_{25}=\mathbb F_5[u]/(u^2-2)\) and \(g=2+u\), which has multiplicative order \(24\). Let \(H=\langle g^4\rangle\), the subgroup of fourth powers of order six, and \(H_i=g^iH\) for \(i=0,1,2,3\). The map \(t\mapsto t^3\) has image \(\{0\}\cup\langle g^3\rangle\), with zero having one preimage and every nonzero cube having three. Exact multiplication using \(u^2=2\) yields
\[
\left(\#\{t:1-t^3\in H_i\}\right)_{i=0}^3=(4,0,12,6).
\]
For instance, these four integers can be reproduced by evaluating the nine distinct values of \(t^3\) and assigning the nonzero values of \(1-t^3\) to the four cosets. Each nonzero fourth power has four preimages, so \(n_v=(16,0,48,24)_i\) for every \(v\in H_i\). At zero, \(25\) pairs have \(a=0\), and \(3(25-1)\) further pairs satisfy \(a\ne0\), \((b/a)^3=1\), hence \(n_0=97\). Each \(H_i\) has six elements. Consequently
\[
\#S(\mathbb F_{25})=\frac{97^2+6(16^2+0^2+48^2+24^2)-1}{24}=1176.
\]
The complete fiber distribution and a separate projective-chart enumeration are reproduced by the standalone verifier.

**5. From two counts to every extension.** For a smooth K3 surface, \(H^1=H^3=0\) and \(\dim H^2=22\). Write the eigenvalues of geometric Frobenius on \(H^2\) as \(\alpha_1,\ldots,\alpha_{22}\). Their complex absolute values under every embedding equal five by purity. The Lefschetz formula at degree two gives
\[
1176=1+25^2+\sum_{j=1}^{22}\alpha_j^2
\qquad\Longrightarrow\qquad\sum_j\alpha_j^2=22\cdot25.
\]
Each summand has absolute value \(25\), so equality in the triangle inequality forces every \(\alpha_j^2=25\). Thus all eigenvalues are \(+5\) or \(-5\). The prime-field count gives
\[
\sum_j\alpha_j=36-(1+5^2)=10.
\]
With 22 eigenvalues, the multiplicities are twelve plus signs and ten minus signs. Substituting into the Lefschetz formula for every \(m\ge1\) gives the extension formula and the displayed zeta function. As all 22 eigenvalues become \(5^2\) after quadratic extension, the Tate theorem for K3 surfaces in odd characteristic identifies the geometric Picard rank with 22.

## Verification
Run `python3 verify_schur.py` using Python 3 and no third-party packages. The verifier enumerates every pair over the two explicit fields, independently enumerates every projective point using unique normalized representatives, checks the four coset fiber values and all weighted identities, and checks consistency of the Frobenius multiplicities and formulas. The supplied `verification_output.txt` ends with `VERIFY_OK`. The proof of smoothness, purity, and the cohomological implications are mathematical arguments, not consequences of finite enumeration.

## Relationship to prior work
Rams and Schütt (arXiv:1212.3511, §1) record precisely this Schur quartic and its 64 lines in characteristic different from two and three. That line configuration is known; neither the equation nor the line count is claimed as new here. Katsura, Kondō, and Shimada (arXiv:1312.0687) study different projective models of the characteristic-five supersingular K3 surface of Artin invariant one; their point count \(1176\) over \(\mathbb F_{25}\) for a Kummer model is a distinct arithmetic statement and alone does not imply the count for this exact Schur model or its \(\mathbb F_5\) Frobenius signs. Schütt (arXiv:0804.1558) develops modularity of singular K3 surfaces without tabulating the present Schur quartic reduction. The contribution is the exact zeta function and complete extension-field arithmetic for the displayed characteristic-five Schur model; no historical uniqueness certification is asserted.

## Limitations
No Artin invariant, generators for the Néron–Severi lattice, or model isomorphism to a previously studied Kummer surface is determined. The novelty assessment is qualified by possible unindexed arithmetic computations and by the fact that the full text of Naskręcki–Pokora, arXiv:2607.07898, was not available for complete inspection; its accessible abstract concerns line configurations rather than this zeta calculation. Exhaustive arithmetic occurs only in the fields of orders five and twenty-five. Counts in all higher extensions follow instead from the proven Weil equality and Frobenius reasoning.

## References
1. S. Rams and M. Schütt, *64 lines on smooth quartic surfaces*, arXiv:1212.3511 (first public version 2012-12-14), §1.
2. T. Katsura, S. Kondō and I. Shimada, *On the supersingular K3 surface in characteristic 5 with Artin invariant 1*, arXiv:1312.0687 (2013), especially the Kummer construction and its \(\mathbb F_{25}\) count.
3. M. Schütt, *K3 surfaces with Picard rank 20*, arXiv:0804.1558 (2008).
4. K. Madapusi Pera, *The Tate conjecture for K3 surfaces in odd characteristic*, arXiv:1301.6326 (2013).
5. B. Naskręcki and P. Pokora, *A (24_4,32_3)-configuration on the Schur quartic with logarithmic Chern slope 14/5*, arXiv:2607.07898 (2026), abstract and overview only.
