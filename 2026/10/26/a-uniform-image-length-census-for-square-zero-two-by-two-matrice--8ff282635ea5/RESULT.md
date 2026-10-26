# A uniform image-length census for square-zero two-by-two matrices over finite chain rings

## Finding

Let \(R\) be any finite commutative chain ring of length \(n\ge1\), with maximal ideal \((\pi)\) and residue field of cardinality \(q\). For each \(X\in M_2(R)\) with \(X^2=0\), let \(r(X)=\log_q|\operatorname{im}_R(X)|\). The integer \(r(X)\) is the module length of the image; it ranges from zero through \(n\).

Put \(f=\lfloor n/2\rfloor\), \(h=\lceil n/2\rceil\), and, for each integer \(e\ge1\), set
\[
G_e=(q^2-1)(q^2-q)q^{4(e-1)},\qquad
U_e=(q-1)(q+1)^2q^{3(e-1)},
\]
\[
P_e(z)=G_ez^{2e}+U_e\left(z^e+(q-1)\sum_{v=1}^{e-1}q^{e-v-1}z^{2e-v}\right).
\]
An empty sum is zero. Then the entire finite-field-independent image-length enumerator is
\[
\boxed{\sum_{\substack{X\in M_2(R)\\X^2=0}}z^{r(X)}
=1+\sum_{e=1}^{f}P_e(z)
+\sum_{k=0}^{h-1}(q^2-1)q^{2n-2-k}
\left(z^{n-k}+(q-1)\sum_{j=1}^{k}q^{j-1}z^{n-k+j}\right).}
\]
In particular, the answer depends only on \(n\) and \(q\), not on the isomorphism type or characteristic of the chain ring. Setting \(z=1\) gives the exact total
\[
\boxed{N_n(q)=q^{4\lfloor n/2\rfloor}
+\lceil n/2\rceil(q^2-1)q^{2n-2}.}
\]
For a fixed prime power \(q\), this yields a rational counting series over any complete discrete valuation ring with residue size \(q\), using its length-\(n\) quotients:
\[
\boxed{\sum_{n\ge0}N_n(q)T^n
=\frac{1+q^2T-q^2T^2-q^4T^3}{(1-q^4T^2)^2},\qquad N_0(q)=1.}
\]
The coefficient of \(z^n\) counts precisely the square-zero regular-module differentials whose homology vanishes. This coefficient equals
\[
(q^2-1)q^{2n-2}
+(h-1)(q^2-1)(q-1)q^{2n-3}
+\mathbf1_{2\mid n}(q^2-1)(q^2-q)q^{4(f-1)}.
\]
For \(n=1\), the middle term is understood as zero; the last term occurs only for positive even \(n\).

## Assumptions and scope

A finite commutative chain ring is a local commutative principal ideal ring with ideals \(R\supset(\pi)\supset\cdots\supset(\pi^n)=0\) and successive quotients of size \(q\). Neither equal characteristic nor unramifiedness is assumed. A matrix's image length is the base-\(q\) logarithm of the number of vectors in its image, an intrinsic module invariant. No division by two is used.

## Proof

**1. Primitive image-length fibers.** Call a matrix over a length-\(e\) chain ring *primitive* if at least one entry is a unit. A primitive matrix has Smith normal form \(\operatorname{diag}(1,d)\), so its image has length \(2e-\nu(d)\), with \(\nu(0)=e\). If the determinant is a unit, the primitive matrix is invertible; the number of such matrices is \(G_e=|\operatorname{GL}_2(R)|\).

If the reduction has rank one, there are \((q-1)(q+1)^2\) choices for its reduction. The determinant map has a unit partial derivative at each such matrix. Thus for any fixed determinant in \(\pi R\), each residue matrix has \(q^{3(e-1)}\) lifts, giving precisely \(U_e\) matrices. For \(1\le v<e\), there are \((q-1)q^{e-v-1}\) determinant values of valuation \(v\), while zero is the unique determinant of valuation \(e\). This proves the polynomial \(P_e(z)\) without any square-zero restriction.

**2. Valuation shells with automatic square-zero property.** For nonzero \(X\), let \(k\) be the minimum valuation of its entries. Write \(X=\pi^kB\) with \(B\) primitive over the quotient of length \(e=n-k\). If \(2k\ge n\), then \(X^2=0\) automatically and the image of \(X\) has the same length as the image of \(B\) over length \(e\). The possible \(e\)'s are \(1\le e\le f\); their disjoint contribution is \(\sum_{e=1}^{f}P_e(z)\). Together with the zero matrix they contribute exactly \(q^{4f}\) matrices, as a check.

**3. Valuation shells constrained by a quadratic equation.** Now suppose \(0\le k<h\), and set \(e=n-k\), \(m=n-2k>0\). The condition on the primitive matrix is \(B^2\equiv0\pmod{\pi^m}\). Its reduction is a nonzero square-zero matrix over the residue field, necessarily a single rank-one nilpotent Jordan block. It has a cyclic vector: some \(w\) makes \((w,Bw)\) an invertible basis over the quotient, so the two-by-two companion-matrix identity implies
\[
B^2\equiv0\pmod{\pi^m}
\quad\Longleftrightarrow\quad
\operatorname{tr}B\equiv\det B\equiv0\pmod{\pi^m}.
\]
The forward implication follows from cyclicity and the Cayley–Hamilton relation; the reverse follows from Cayley–Hamilton over every commutative ring. This argument does not assume characteristic different from two.

There are exactly \(q^2-1\) nonzero square-zero two-by-two matrices over \(\mathbb F_q\): choose an image line and a nonzero linear map from its one-dimensional quotient to that line. At each one, the map \(B\mapsto(\operatorname{tr}B,\det B)\) has a surjective differential on the two free matrix coordinates. For each *specified* pair of trace and determinant in \(\pi R_e\), precisely \((q^2-1)q^{2(e-1)}\) primitive matrices have that pair. The statement follows explicitly on the chart where an off-diagonal entry is a unit: the trace and determinant equations uniquely determine the opposite diagonal entry and the other off-diagonal entry, once two free entries are fixed; the second off-diagonal chart handles the complementary residue cases. Equivalently, lift one \(\pi\)-adic digit at a time and solve two independent linear equations at each stage.

For the constrained valuation shell, the trace has \(q^k\) allowed values. The determinant may be zero (one choice, image length \(e=n-k\)) or have valuation \(e-j\), for \(1\le j\le k\), with \((q-1)q^{j-1}\) choices and image length \(e+j=n-k+j\). The count per specified determinant, summed over allowed traces, is
\[
(q^2-1)q^{2(e-1)+k}=(q^2-1)q^{2n-2-k}.
\]
This proves the second sum and its image-length exponents. The deep and shallow valuation shells partition every nonzero matrix, proving the main formula.

**4. Totals, rationality and acyclicity.** Each shallow shell has exactly \((q^2-1)q^{2n-2}\) elements; there are \(h\) such shells. The deep shells including zero contain \(q^{4f}\) elements. This proves the total. Summing the even- and odd-length instances yields the displayed rational generating function. As \(X^2=0\), \(\operatorname{im}X\subset\ker X\). Their lengths are \(r(X)\) and \(2n-r(X)\), so the homology \(\ker X/\operatorname{im}X\) has length \(2n-2r(X)\) and vanishes precisely when \(r(X)=n\). Extracting that coefficient gives the displayed acyclic-differential count.

## Verification

The standalone Python 3 program `verify.py` independently enumerates matrices satisfying the four entries of \(X^2=0\) and computes image length by valuation/Smith form. Its finite-field polynomial-ring backend covers ten parameter cases over residual orders \(2\), \(3\) and \(4\), including an extension field. A separate modular-integer backend covers nine equal- and mixed-characteristic cases, including \(\mathbb Z/16\mathbb Z\), \(\mathbb Z/27\mathbb Z\) and \(\mathbb Z/25\mathbb Z\). All nineteen complete finite enumerations matched every rank coefficient and the stated totals. For example, at \((n,q)=(4,2)\) the rank multiplicities for \(r=0,1,2,3,4\) are \((1,9,78,168,384)\). Finite tests corroborate, but do not replace, the symbolic proof for all \(n\), \(q\), and chain rings.

## Relationship to prior work

The elementary-divisor shape enumeration for matrices over finite chain rings established by Feng, Nóbrega, Kschischang and Silva (2013 preprint) motivates the image-length invariant and supplies conventional matrix-shape background; it counts *all* matrices by shape, rather than the locus satisfying \(X^2=0\). Carnevale, Shechter and Voll (2017) count traceless matrices over local rings with image-size refinements, but impose no determinant-zero equation; a traceless matrix need not be square-zero over a chain ring. Brawley (1982) addresses enumeration by Drazin index over finite rings, and its aggregate results may subsume the unrefined total for some rings. The claimed contribution here is the full simultaneous square-zero and image-length enumerator for *every chain length*, including the determinant-valuation shells and its acyclicity interpretation—not an independent rediscovery claim for aggregate nilpotent counts or basic Smith normal forms.

## Limitations

The theorem covers two-by-two matrices over finite *commutative chain rings*. It does not classify conjugacy classes or module-isomorphism types beyond image length, and does not count square-zero matrices of larger sizes. The reduced geometric structure of the square-zero scheme is not addressed. Historical Drazin-index and nilpotent-matrix enumeration literature was not fully available in every instance, so absolute publication priority and whether particular specializations were previously implicit are not independently established. No independent mathematical audit was performed.

## References

- C. Feng, R. W. Nóbrega, F. R. Kschischang and D. Silva, *Communication over Finite-Chain-Ring Matrix Channels*, arXiv:1304.2523, first version 2013-04-09.
- A. Carnevale, M. Shechter and C. Voll, *Enumerating traceless matrices over compact discrete valuation rings*, arXiv:1709.02717 (2017).
- J. V. Brawley, *Counting Matrices by Drazin Index*, SIAM Journal on Algebraic Discrete Methods **3** (1982), 30–34; doi:10.1137/0603003.
- D. Bollman and H. Ramírez, *On the number of nilpotent matrices over* \(\mathbb Z_m\), cited by Brawley; bibliographic and full-text comparison incomplete.
