# The exact Smith form of the Hermitian quintic line lattice

## Finding
Let \(k=\mathbb F_{16}\) and let \(X\subset\mathbb P^3_k\) be the smooth surface
\[
X:\quad x_0^5+x_1^5+x_2^5+x_3^5=0.
\]
Let \(L_1,\ldots,L_{325}\) be its \(k\)-rational projective lines and let \(G=(L_i\cdot L_j)\) be their integer intersection Gram matrix. The full \(325\times325\) integer intersection Gram matrix \(G\) of the \(\mathbb F_{16}\)-rational lines on \(X:\sum_{i=0}^{3}x_i^5=0\subset\mathbb P^3_{\mathbb F_{16}}\) has rank \(53\) and Smith normal form \(\operatorname{diag}(1^{37},2^{16},0^{272})\). Its diagonal entries are displayed explicitly as
\[
\operatorname{diag}(\underbrace{1,\ldots,1}_{37},\underbrace{2,\ldots,2}_{16},\underbrace{0,\ldots,0}_{272}).
\]
Equivalently, the nonzero Smith invariant factors are \(1\) with multiplicity \(37\) and \(2\) with multiplicity \(16\); no nonzero factor is divisible by \(4\).

## Assumptions and scope
The field is \(\mathbb F_{16}=\mathbb F_2[a]/(a^4+a+1)\), with Hermitian involution \(z\mapsto z^4\). The surface is the Hermitian/Fermat quintic \(X=\mathcal H(3,16)\), considered in characteristic two. The line set consists of the \(\mathbb F_{16}\)-rational maximal totally isotropic projective lines, not all geometric lines over an algebraic closure. The matrix is the intersection pairing on those line classes. The claim concerns this finite configuration only.

## Proof
Represent elements of \(\mathbb F_{16}\) in the polynomial basis for \(a^4+a+1\). A projective point is normalized so its first nonzero coordinate is \(1\). Exhaustive finite-field enumeration gives \(4369\) projective points, of which \(1105\) satisfy \(\sum_i x_i^5=0\). Pairing isotropic vectors by the Hermitian form and taking their spans yields exactly \(325\) distinct totally isotropic lines, each containing \(17\) rational points; the count agrees with \((q+1)(q^3+1)=325\) for \(q=4\).

For each line, adjunction on a smooth degree-five surface in \(\mathbb P^3\) gives \(L_i^2=2-5=-3\). Two distinct projective lines meet in at most one point, and if they meet on the smooth surface their tangent directions are distinct, so their intersection number is \(1\); otherwise it is \(0\). Harashita’s general intersection formula \(f(j)=(1-(-q)^{j+1})/(q+1)\) gives the same values at \(j=-1,0,1\) for \(q=4\). Thus the matrix is reconstructed exactly from the enumerated point sets, with diagonal entries \(-3\) and off-diagonal entries in \(\{0,1\}\).

Exact modular elimination gives \(\operatorname{rank}(G\bmod 2)=37\) and \(\operatorname{rank}(G\bmod 3)=53\). The middle Betti number of a smooth quintic surface is \(b_2=53\), and the linear-cycle classes span middle cohomology for Hermitian varieties; hence the rational rank is exactly \(53\). Elimination over \(\mathbb Z/4\mathbb Z\) finds \(37\) unit pivots. The remaining block is even, and its half reduced modulo two has rank \(16\), so exactly \(16\) nonzero factors have 2-adic valuation one and no factor has valuation two. Shimada's theorem that the lattice of linear cycles on these Fermat hypersurfaces has discriminant a power of the characteristic excludes odd-prime factors. These facts give the stated Smith form.

The enumeration and modular eliminations are reproducible with the standalone standard-library script `verification/hermitian_quintic_smith.py`. It checks the point, line, rank, and Smith-exponent counts and prints `VERIFY_OK`.

## Verification
The exact script run returned:

- `POINTS=4369`
- `ISOTROPIC_POINTS=1105`
- `TOTALLY_ISOTROPIC_LINES=325`
- `RANK_MOD_2=37`
- `RANK_MOD_3=53`
- `SMITH_2_ADIC_EXPONENT_COUNTS: e0=37, e1=16, e2=0`
- `VERIFY_OK`

The finite computation is exhaustive for the stated field and line set. The rank bound and absence of odd-prime discriminant factors use the cited general results; this computation does not independently re-prove those general theorems.

## Relationship to prior work
Harashita's 2026 treatment of Hermitian varieties proves that the 2-adic elementary-divisor exponents in dimension two are at most \(\nu=2\) when \(q=2^\nu=4\), and explicitly notes in Remark 6.3 that lower bounds on the individual exponents are not determined there. The earlier general lattice theorem of Shimada establishes that the linear cycles span middle cohomology and that their discriminant is a power of the characteristic. Neither accessible statement gives the exact multiplicities \(37\) and \(16\) for this \(q=4\) surface. This calculation refines the general bound \(4\) to the exact nonzero factors \(1\) and \(2\) in this one case.

## Limitations
The result is specific to \(X=\mathcal H(3,16)\) and its \(325\) rational lines. It does not classify Smith forms for other Hermitian varieties, determine the index of the line lattice in the full numerical cycle lattice, or settle whether the line lattice equals that full lattice. The author-hosted full-text PDF of Shimada's 2001 article could not be fetched during this check; its accessible abstract establishes the general rank and characteristic-primary discriminant statements, so an uninspected special-case table in that article remains a bibliographic risk.

## References
1. S. Harashita, “An explicit form of the standard conjecture of Hodge type for Hermitian varieties, with \(p\)-adic applications,” arXiv:2610.01731v1 (2026), especially §§3.3–3.4 and §6, Corollary 6.2 and Remark 6.3.
2. I. Shimada, “Lattices of algebraic cycles on Fermat varieties in positive characteristics,” *Proceedings of the London Mathematical Society* (3) 82 (2001), 131–172. DOI: 10.1112/S0024611500012673.
