# Cubic-nilpotent centralizers: a valuation plateau over finite chain rings

## Finding

**Theorem (uniform cubic-nilpotency census and flat shallow valuation strata).** Let \(R\) be any finite **commutative chain ring** of length \(s\ge1\), with maximal ideal \(\mathfrak m=(\pi)\), residue field of order \(q\ge2\), and \(\mathfrak m^s=0\ne\mathfrak m^{s-1}\). Put \(c=\lceil s/3\rceil\). The number of matrices with cube zero is
\[
N_{\le3}(R)=\#\{X\in M_2(R):X^3=0\}
=q^{4(s-c)}+c(q^2-1)q^{3s-2-c}.
\]
For a nonzero matrix \(X\), define its entry valuation \(v(X)\) to be the unique \(v\in\{0,\ldots,s-1\}\) such that \(X\in\mathfrak m^vM_2(R)\setminus\mathfrak m^{v+1}M_2(R)\). For **every** \(0\le v<c\), the number of cube-zero matrices with \(v(X)=v\) is the **same**:
\[
\#\{X:X^3=0,\ v(X)=v\}=(q^2-1)q^{3s-2-c}.
\]
For every \(c\le v<s\), every matrix of exact valuation \(v\) is cube-zero and their number is \((q^4-1)q^{4(s-v-1)}\). The zero matrix is an additional point. No equal-characteristic or odd-characteristic hypothesis is needed.

**Centralizer interpretation.** For a finite field \(k=\mathbb F_q\), let \(B=J_s(0)\oplus J_s(0)\in M_{2s}(k)\), where \(J_s(0)\) is a single nilpotent Jordan block of size \(s\). Since
\[
C_{M_{2s}(k)}(B)\cong M_2\bigl(k[t]/(t^s)\bigr),
\]
the displayed formula also counts the matrices \(X\) commuting with \(B\) for which \(X^3=0\). The number having **nilpotency index exactly three** is \(N_{\le3}(R)-N_{\le2}(R)\), with
\[
N_{\le2}(R)=q^{4\lfloor s/2\rfloor}+\lceil s/2\rceil(q^2-1)q^{2s-2}.
\]
In particular, at \(s=1\) every cube-zero matrix is square-zero; for \(s\ge2\), cube-zero but not square-zero matrices exist.

## Assumptions and scope

A finite commutative chain ring is a finite local principal ideal ring whose ideals are \(R\supset(\pi)\supset\cdots\supset(\pi^s)=0\) and each consecutive quotient has \(q\) elements. For \(0\le m\le s\), write \(R_m=R/(\pi^m)\), of cardinality \(q^m\). The theorem counts *individual matrices*, not centralizer-unit conjugacy orbits, and permits mixed-characteristic rings such as \(\mathbb Z/p^s\mathbb Z\) as well as equal-characteristic rings \(\mathbb F_q[t]/(t^s)\). The interpretation in terms of a nilpotent Jordan centralizer uses the equal-characteristic example only.

## Proof

**1. Primitive cube-zero matrices.** Fix any quotient \(T=R_m\), \(m\ge1\), and call \(U\in M_2(T)\) primitive when at least one of its entries is a unit. Suppose \(U^3=0\). Its residue \(\overline U\in M_2(\mathbb F_q)\) is a nonzero nilpotent matrix. Such a matrix has trace and determinant zero, rank one, and a nonzero off-diagonal entry. There are exactly \(q^2-1\) choices for \(\overline U\): choose the one-dimensional image/kernel \(L\), of which there are \(q+1\), and a nonzero map from \(\mathbb F_q^2/L\) to \(L\), of which there are \(q-1\).

Write \(\tau=\operatorname{tr}(U)\) and \(\delta=\det(U)\). Cayley--Hamilton gives
\[
U^3=(\tau^2-\delta)U-\tau\delta I.
\]
The matrices \(I\) and \(U\) are linearly independent over the local ring \(T\): modulo its maximal ideal the matrices \(I\) and the nonzero rank-one nilpotent \(\overline U\) are linearly independent, so the coordinate map they define has a unit minor and hence is injective over \(T\). Therefore
\[
U^3=0\quad\Longleftrightarrow\quad
\delta=\tau^2\ \text{and}\ \tau^3=0.
\]
Here \(\tau\in(\pi)\), and \(\tau^3=0\) means \(\tau\in(\pi^{\lceil m/3\rceil})\). Thus there are exactly \(q^{m-\lceil m/3\rceil}\) possible traces.

For each chosen residue \(\overline U\), trace \(\tau\) lifting its zero trace, and determinant \(\delta=\tau^2\), there are precisely \(q^{2(m-1)}\) lift matrices. Indeed, when the upper-right residue entry \(\overline b\) is nonzero, choose the upper-left entry \(a\) and the unit upper-right entry \(b\) independently among their \(q^{m-1}\) lifts, and set the lower-right entry to \(\tau-a\) and lower-left entry to \((a(\tau-a)-\tau^2)/b\). If instead \(\overline c\ne0\), exchange the two off-diagonal roles. These constructions solve the prescribed trace and determinant equations uniquely. It follows that
\[
P_m:=\#\{U\in M_2(R_m):U\text{ primitive},\ U^3=0\}
=(q^2-1)q^{3m-2-\lceil m/3\rceil}.
\]

**2. Valuation layers.** Fix an entry valuation \(0\le v<c=\lceil s/3\rceil\). Each matrix at this valuation has a unique presentation \(X=\pi^vU\) with \(U\) primitive **modulo \((\pi^{s-v})\)** (uniqueness refers to the quotient class of \(U\)). The condition \(X^3=0\) is exactly \(U^3=0\) modulo \((\pi^{s-3v})\). The quotient map \(R_{s-v}\to R_{s-3v}\) has fibers of size \(q^{2v}\); hence each of the four entries contributes that number of independent lifts. The number of matrices in this valuation layer therefore equals
\[
q^{8v}P_{s-3v}
=(q^2-1)q^{8v+3(s-3v)-2-\lceil(s-3v)/3\rceil}
=(q^2-1)q^{3s-2-c},
\]
where \(\lceil(s-3v)/3\rceil=c-v\). This proves the claimed plateau, including all three residue classes of \(s\) modulo three.

**3. Deep radical and disjoint sum.** Every matrix in \((\pi^c)M_2(R)\) has cube zero because \(3c\ge s\), and this deep-radical block has \(q^{4(s-c)}\) matrices. These matrices are disjoint from the \(c\) shallow valuation layers, so adding gives the theorem. For \(c\le v<s\), the exact valuation count is the difference between two nested radical blocks, namely \(q^{4(s-v)}-q^{4(s-v-1)}\).

**4. Exactly-three index and centralizer.** The identical argument with the square-zero condition, or the previously known square-zero census, gives \(N_{\le2}\) as displayed. Their difference is exactly the index-three stratum, since \(X^3=0\) forces nilpotency index \(1\), \(2\), or \(3\). For \(s\ge2\) the explicit matrix \(\begin{psmallmatrix}\pi^{\lceil s/2\rceil}&1\\0&0\end{psmallmatrix}\) has square nonzero but cube zero (its square has off-diagonal entry \(\pi^{\lceil s/2\rceil}\)), proving existence. Finally, the \(k[t]\)-module underlying two equal Jordan blocks is \((k[t]/t^s)^2\); its module endomorphism ring is the claimed \(2\times2\) matrix algebra, establishing the centralizer count.

## Verification

The standalone script `artifacts/check_cubezero.py` constructs the rings \(\mathbb F_q[t]/(t^s)\) and \(\mathbb Z/p^s\mathbb Z\) as explicit arithmetic tables, forms **actual cubes by multiplication**, and exhaustively enumerates matrices and every nonzero exact-valuation stratum. It uses only the Python standard library, tests 14 ring configurations including \(\mathbb F_4[t]/(t^2)\) with extension-field arithmetic, and prints `CUBE_ZERO_CHAIN_RING_CENSUS_OK 14` on success. Reproduce by running `python3 artifacts/check_cubezero.py`. The recorded result is `artifacts/verification_output.txt`. These computations are corroboration only; the theorem for all lengths and fields follows from the argument above.

## Relationship to prior work

Britnell and Wildon [1] investigate centralizer algebras and commuting nilpotent similarity classes, with the earliest public arXiv version dated January 6, 2010; those results motivate the centralizer viewpoint but concern which classes commute, rather than the number of matrices in the cube-zero locus for each finite chain-ring length. Oblak [2] and the later study of commuting nilpotent matrices [3] develop possible Jordan forms and centralizer geometry, but do not provide the formula or valuation-layer plateau as stated here. Brawley [4] studies counting matrices by Drazin index and references counting nilpotent matrices by their index; indexed accessible material describes such counts as separate input data. Its complete full text was unavailable for inspection, so an earlier equivalent index-three count cannot be ruled out. An earlier count of square-zero matrices over finite chain rings determines \(N_{\le2}\), but does not by itself determine \(N_{\le3}\); the cubic trace--determinant constraint and the valuation plateau are the new features here.

## Limitations

The enumeration is specific to \(2\times2\) matrices over finite commutative chain rings, or to the centralizer of two **equal** Jordan blocks over a finite field. It does not classify higher-size matrices, unequal-block centralizers, matrix conjugacy orbits, or the scheme structure of the cubic-nilpotent locus. Relevant historical literature may already encode the same cardinality through orbit sums or a general finite-ring nilpotency-index theorem; priority remains provisional and independent review has not been performed.

## References

[1] J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811v1 (January 6, 2010), https://arxiv.org/pdf/1001.0811 . Journal of the London Mathematical Society 83 (2011), 470–492, DOI 10.1112/jlms/jdq088.

[2] P. Oblak, *On the nilpotent commutator of a nilpotent matrix*, arXiv:1106.1545, https://arxiv.org/pdf/1106.1545 .

[3] *On commuting nilpotent matrices*, arXiv:2212.08425, https://arxiv.org/pdf/2212.08425 .

[4] J. V. Brawley, *Counting Matrices by Drazin Index*, SIAM Journal on Algebraic and Discrete Methods 3 (1982), DOI 10.1137/0603003. Full text not inspected.
