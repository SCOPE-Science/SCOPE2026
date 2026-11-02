# The unique nonordinary member of a characteristic-seven genus-four trigonal pencil

## Finding

Let \(k\) be an algebraic closure of \(\mathbb F_7\). For every \(a\in k\) satisfying \(a^5\ne1\), let \(C_a\) be the smooth projective completion of
\[
 C_a:\qquad y^3=x^5+a x+1.
\]
Every \(C_a\) has genus four. In the holomorphic-differential basis
\[
 \omega_0=\frac{dx}{y},\quad \omega_1=\frac{dx}{y^2},\quad
 \omega_2=\frac{x\,dx}{y^2},\quad \omega_3=\frac{x^2\,dx}{y^2},
\]
the entrywise seventh power of the Cartier matrix (equivalently, its Cartier coefficient matrix) is
\[
 B(a)=\begin{pmatrix}
 2a&0&0&0\\
 0&-2a&-3&a^4\\
 0&0&-a^2&-2a\\
 0&1&0&0
 \end{pmatrix}\quad\text{over }\mathbb F_7[a].
\]
Its determinant is \(2a^2(a^5-1)\). With \(\Delta(a)=\operatorname{disc}_x(x^5+a x+1)=4(a^5-1)\), this is precisely \(4a^2\Delta(a)\). Thus the Hasse degeneracy divisor on the smooth marked parameter line has scheme-theoretic multiplicity two at \(a=0\) and no other support.

For every smooth geometric parameter,
\[
 \bigl(f(C_a),\operatorname{an}(C_a),\operatorname{NP}(\operatorname{Jac}(C_a))\bigr)
 =\begin{cases}
 (4,0,\{0^{\times4},1^{\times4}\}),&a\ne0,\\
 (0,2,\{(1/4)^{\times4},(3/4)^{\times4}\}),&a=0.
 \end{cases}
\]
Here \(f\) is the geometric \(7\)-rank and \(\operatorname{an}\) is the Jacobian \(a\)-number. The nonordinary curve is not supersingular. At \(a=0\), Cartier has successive image dimensions \(2,1,0\), so its nilpotent Jordan lengths are \(3\) and \(1\) over \(\mathbb F_7\).

The exceptional curve is defined over \(\mathbb F_7\) and has zeta function
\[
 Z(C_0/\mathbb F_7,T)=\frac{1-77T^4+2401T^8}{(1-T)(1-7T)}.
\]
For \(q=7^m\), the number of smooth marked parameters is \(q-\gcd(5,q-1)\), of which exactly one (\(a=0\)) is nonordinary. These are parameter counts, not isomorphism-class counts.

## Assumptions and scope

The characteristic is exactly seven. The parameter belongs to the algebraic closure of the prime field; the normalization of the coefficient of \(x^5\) and the constant term to one is part of the chosen marked family. The excluded parameters \(a^5=1\) are singular affine covers and are not included in any rank or Newton-polygon assertion. The zeta function and explicit point counts concern the particular \(\mathbb F_7\)-model \(C_0\), not arbitrary twists or every nonzero-parameter zeta function.

## Proof

**Smoothness and genus.** Put \(F_a(x)=x^5+a x+1\). The affine equation is singular precisely when \(y=0\) and \(F_a(x)=F'_a(x)=0\). If the two polynomials have a common root, the derivative equation gives \(5x^4=-a\). If \(a=0\), this forces \(x=0\), which is not a root of \(F_a\). Otherwise the two equations imply \(x=-5/(4a)\) and hence
\[
 5^5+4^4a^5=0,\qquad\text{equivalently }\quad a^5=1
 \quad\text{in }\mathbb F_7.
\]
Conversely this condition produces a common root. The standard discriminant of a monic quintic of the form \(x^5+a x+1\) is \(5^5+4^4a^5=4(a^5-1)\) after reduction modulo seven. Since \(\gcd(3,5)=1\), the tame cyclic degree-three completion has one smooth point above infinity. For squarefree \(F_a\) it ramifies totally at its five finite roots and infinity. Riemann–Hurwitz yields
\[
 2g-2=3(-2)+6(3-1)=6,
\]
so \(g=4\). The separable degree-three extension is geometrically connected because \(F_a\) has simple roots and is not a cube in \(k(x)\).

**Differentials.** At each finite branch point, \(y\) is a uniformizer and \(dx\) has order two; thus the four displayed differentials are regular there. At infinity, \(v_\infty(x)=-3\), \(v_\infty(y)=-5\), and \(v_\infty(dx)=-4\). The four differentials have respective valuations \(1,6,3,0\), all nonnegative and distinct. They form a basis of the four-dimensional differential space.

**Cartier calculation.** For \(j\in\{1,2\}\) and each relevant \(i\), use the Cartier identities \(\mathcal C(h^7\eta)=h\mathcal C(\eta)\) and \(y^{3}=F_a(x)\) to obtain
\[
 \mathcal C\left(\frac{x^i dx}{y^j}\right)
 =\frac1{y^j}\mathcal C\left(x^i F_a(x)^{2j}dx\right).
\]
The coefficient in row \(k\), column \(i\) of the seventh-power Cartier matrix for this character block is
\[
 [x^{7(k+1)-1-i}]F_a(x)^{2j}.
\]
For \(j=1\) this coefficient is \([x^6]F_a^2=2a\). For \(j=2\) and \(0\le i,k\le2\), the resulting block is
\[
 \begin{pmatrix}-2a&-3&a^4\\0&-a^2&-2a\\1&0&0\end{pmatrix}.
\]
These are identities in \(\mathbb F_7[a]\), not just evaluations at rational parameters. The block determinant is \(a^6+6a=a(a^5-1)\), giving \(\det B=2a^2(a^5-1)=4a^2\Delta\). Since \(\Delta\) is a unit on the smooth parameter space, exactly \(a=0\) is nonordinary; the Hasse divisor is \(2[0]\).

**Rank and \(a\)-number at the exceptional point.** The entire matrix at \(a=0\) has entries in \(\mathbb F_7\). Its rank is two, its square has rank one, and its cube is zero. The Cartier semilinearity introduces no coefficient twists at this point. Thus stable Frobenius rank is zero and the Cartier kernel dimension is two. For every other smooth parameter, the Cartier matrix is invertible, so the Jacobian is ordinary, with \(7\)-rank four and \(a\)-number zero.

**Zeta function and Newton polygon.** An exhaustive arithmetic calculation over the explicit fields \(\mathbb F_{7^m}\), \(m=1,2,3,4\), gives
\[
 \#C_0(\mathbb F_7)=8,\quad \#C_0(\mathbb F_{49})=50,\quad
 \#C_0(\mathbb F_{343})=344,\quad \#C_0(\mathbb F_{2401})=2094.
\]
The attached standalone verifier constructs each field, proves that every nonzero residue class is invertible, enumerates both the values of \(y^3\) and all right-hand sides \(x^5+1\), and cross-checks with cubic-residue exponentiation. These are complete finite field enumerations, not samples. The unique point at infinity contributes one.

Write the degree-eight numerator as \(L(T)=\sum_{i=0}^8c_iT^i\). The four power sums \(7^m+1-\#C_0(\mathbb F_{7^m})\) are \(0,0,0,308\). Newton identities give \(c_1=c_2=c_3=0\), \(c_4=-77\). The functional equation of the smooth genus-four curve gives \(c_{8-i}=7^{4-i}c_i\) for \(0\le i\le4\), hence
\[
 L(T)=1-77T^4+7^4T^8.
\]
The lower Newton polygon has vertices \((0,0)\), \((4,1)\), \((8,4)\), since \(v_7(77)=1\) and \(v_7(7^4)=4\). It has four slopes \(1/4\) and four slopes \(3/4\). This determines the remaining assertion and proves that \(C_0\) is not supersingular.

**Point counts for all extensions and parameters.** Let \(U_0=2\), \(U_1=77\), and \(U_r=77U_{r-1}-2401U_{r-2}\) for \(r\ge2\). The factorization of \(L(T)\) as a quadratic in \(T^4\) gives, for every integer \(m\ge1\),
\[
 \#C_0(\mathbb F_{7^m})=\begin{cases}
 7^m+1,&4\nmid m,\\
 7^m+1-4U_{m/4},&4\mid m.
 \end{cases}
\]
The polynomial \(a^5-1\) has exactly \(\gcd(5,7^m-1)\) roots in \(\mathbb F_{7^m}\), giving the stated exact counts of smooth, ordinary and nonordinary marked parameters.

## Verification

Run `python3 verify.py` in the directory containing the embedded verification files. It uses only Python's standard library. It reconstructs each Cartier coefficient by integer multinomial expansion reduced modulo seven; verifies the displayed matrix and determinant factors; computes the ranks of three successive Cartier powers; certifies the finite extension rings are fields by checking that every nonzero element has multiplicative inverse; enumerates all \(y\)-cubes and all \(x\)-inputs for the first four extensions, using a second exponentiation-based count; and reconstructs the zeta numerator by Newton identities. The expected final line is `VERIFY_OK`.

The independent point-count implementation for the ordinary test fiber \(a=2\) yields \(5,47,389,2379\) points over the same four extensions, providing an additional arithmetic cross-check. The calculation of the zeta function is an exact finite certificate combined with the general functional equation, not extrapolation of finite data.

## Relationship to prior work

Baldwin, Eilbeck, Gibbons and Ônishi study the general cyclic trigonal \((3,5)\) curve and its complex Abelian functions; their work provides the motivating geometric family, not the characteristic-seven stratification. Bouw studies the generic \(p\)-rank of prime-to-characteristic cyclic covers; Johnston gives general Cartier/Frobenius coefficient formulas and bounds for Kummer covers. Such formulas motivate the method but do not, without this specialization and determination of the exceptional arithmetic, state the unique nonordinary point, its double Hasse multiplicity, or its Newton polygon. Kudo and Harashita's absence of superspecial genus-four curves in characteristic seven is consistent with the exceptional \(a\)-number two. Camacho-Navarro surveys genus-four \(p\)-rank and \(a\)-number data over finite fields, without supplying this full geometric parameter classification. Classical Jacobi-sum theory can in principle recover the special Fermat-type zeta numerator; independent priority is not claimed for that isolated specialization. The contribution assessed here is the complete parameterwise Newton stratification and discriminant/Hasse-divisor identity.

## Limitations

The result concerns this normalized one-parameter family in characteristic seven; it is not a classification of all cyclic trigonal curves or their isomorphism classes. The zeta function is explicitly determined only for the exceptional \(a=0\) fiber. The complete Ekedahl–Oort type is not asserted. External independent audit and historical-priority certification have not been performed; the literature comparison is bounded by accessible sources and searches.

## References

1. S. Baldwin, J. C. Eilbeck, J. Gibbons, Y. Ônishi, *Abelian Functions for Cyclic Trigonal Curves of Genus Four* (first arXiv posting 2006-12-21), https://arxiv.org/abs/math/0612654.
2. I. I. Bouw, *The p-Rank of Ramified Covers of Curves*, Compositio Mathematica **126** (2001), 295–322, https://doi.org/10.1023/A:1017513122376.
3. O. Johnston, *A Note on the a-numbers and p-ranks of Kummer Covers* (arXiv, 2007-10-10), https://arxiv.org/abs/0710.2120.
4. M. Kudo and S. Harashita, *Superspecial curves of genus 4 in small characteristic* (first arXiv posting 2016-07-05), https://arxiv.org/abs/1607.01114.
5. C. Camacho-Navarro, *The a-number, p-rank and Cartier points of genus 4 curves* (arXiv, 2020-12-16), https://arxiv.org/abs/2012.08705.
