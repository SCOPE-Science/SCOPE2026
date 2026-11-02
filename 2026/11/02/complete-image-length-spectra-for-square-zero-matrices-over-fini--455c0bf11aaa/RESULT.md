# Complete image-length spectra for square-zero matrices over finite chain rings

## Finding

Let \(R\) be **any finite commutative chain ring** of composition length \(n\geq2\), with maximal ideal \((\pi)\) and residue field of cardinality \(q\). For \(0\leq r\leq n\), let \(C_{n,q}(r)\) be the number of matrices \(X\in M_2(R)\) satisfying \(X^2=0\) and \(\operatorname{length}_R(\operatorname{im}X)=r\).

Define \(h=\lceil n/2\rceil\), \(m=\lfloor n/2\rfloor\), \(P_e=(q^2-1)q^{2e-2}\), \(G_e=q^{4e-4}(q^2-1)(q^2-q)\), and \(U=(q-1)(q+1)^2\). Set \(\mathbf1_{r=s}\) equal to one when \(r=s\) and zero otherwise. Then the **full spectrum** is

\[
\begin{aligned}
C_{n,q}(r)={}&\mathbf1_{r=0}
 +\sum_{k=0}^{h-1}P_{n-2k}\left[q^{3k}\mathbf1_{r=n-k}
 +\sum_{j=0}^{k-1}(q-1)q^{4k-j-1}\mathbf1_{r=n-j}\right]\\
&+\sum_{e=1}^{m}\left[G_e\mathbf1_{r=2e}+Uq^{3e-3}\mathbf1_{r=e}
 +\sum_{v=1}^{e-1}U(q-1)q^{4e-v-4}\mathbf1_{r=2e-v}\right].
\end{aligned}
\]

An empty sum equals zero. These counts depend on \(R\) **only through** \(n\) and \(q\), including for mixed-characteristic chain rings.

In particular, the total number and the number with maximal possible image length \(n\) are, respectively,

\[
\boxed{\#\{X:X^2=0\}=\lceil n/2\rceil(q^2-1)q^{2n-2}+q^{4\lfloor n/2\rfloor}}
\]

and

\[
\boxed{C_{n,q}(n)=(q^2-1)q^{2n-3}\bigl(q+\lfloor n/2\rfloor(q-1)\bigr).}
\]

More sharply, for every \(0\leq k<\lceil n/2\rceil\), the number of square-zero matrices whose smallest entry valuation is exactly \(k\) is the **same number**, namely \((q^2-1)q^{2n-2}\). Each positive entry-valuation layer contributing maximal-length images contributes exactly \((q^2-1)(q-1)q^{2n-3}\) such matrices.

**Commuting-matrix consequence.** For \(R=\mathbb F_q[t]/(t^n)\), choose \(J=J_n(0)\oplus J_n(0)\) on \(\mathbb F_q^{2n}\). Then \(\operatorname{Cent}(J)\cong M_2(R)\); consequently \(C_{n,q}(r)\) is exactly the number of matrices \(X\) with \(XJ=JX\), \(X^2=0\), and Jordan type \((2^r,1^{2n-2r})\). Every integer \(0\le r\le n\) occurs.

## Assumptions and scope

A finite commutative chain ring is a finite local principal ideal ring whose ideals are \(R\supset(\pi)\supset\cdots\supset(\pi^n)=0\), with strict inclusions through \(\pi^{n-1}\). Write \(R_e=R/(\pi^e)\) for \(1\leq e\leq n\), so \(|R_e|=q^e\). A matrix over \(R_e\) is *primitive* if at least one entry is a unit. For \(X\neq0\), its entry valuation \(\nu(X)\) is the minimum of the \(\pi\)-adic valuations of its four entries, in \(\{0,\dots,n-1\}\); define \(\nu(0)=n\). The image length equals the base-\(q\) logarithm of the finite cardinality of the image. The rank terminology in the commuting-matrix consequence is ordinary \(\mathbb F_q\)-linear rank.

The classification includes all residue characteristics and all ramification types; it makes no claim about arbitrary finite local rings with nonprincipal maximal ideal, larger matrix size over a chain ring, or the full nilpotent cone (only index at most two).

## Proof

**1. Primitive square-zero conjugacy.** Over a chain ring \(R_e\), any primitive \(B\in M_2(R_e)\) with \(B^2=0\) has a vector \(v\) for which \(Bv\) is primitive. Modulo \(\pi\), the nonzero square-zero matrix \(\overline B\) has rank one. Hence \(Bv,v\) form a basis: their residue classes are independent, because \(\overline B^2=0\) and \(\overline Bv\ne0\). In this basis \(B\) is \(\begin{psmallmatrix}0&1\\0&0\end{psmallmatrix}\). Its invertible centralizer consists of \(\begin{psmallmatrix}a&b\\0&a\end{psmallmatrix}\), with \(a\in R_e^\times\), \(b\in R_e\). Since \(|GL_2(R_e)|=q^{4(e-1)}(q^2-1)(q^2-q)\), orbit-stabilizer gives

\[
\#\{B\text{ primitive}:B^2=0\}=\frac{|GL_2(R_e)|}{q^e(q^e-q^{e-1})}=P_e=(q^2-1)q^{2e-2}.
\]

**2. The low valuation layers.** If \(0\leq k<h\) and \(\nu(X)=k\), multiplication by \(\pi^k\) identifies \(X\) uniquely with \(\pi^kB\), where \(B\in M_2(R_{n-k})\) is primitive. Put \(e=n-2k\ge1\). The equality \(X^2=0\) is equivalent to requiring the reduction \(B_0\in M_2(R_e)\) to satisfy \(B_0^2=0\). Each primitive square-zero \(B_0\) has exactly \(q^{4k}\) lifts \(B\), so this layer has cardinality \(P_e q^{4k}=(q^2-1)q^{2n-2}\), independent of \(k\).

The determinant of each \(B\) belongs to \(\pi^e R_{n-k}\). For each fixed \(B_0\), the determinant is uniformly distributed over this ideal: an entry opposite a unit cofactor can be adjusted independently among its \(q^k\) lifts, and the determinant changes by a unit multiple of that adjustment. Each possible determinant therefore has \(q^{3k}\) lifts. For \(0\le j<k\), the number of determinant values of exact valuation \(e+j\) is \((q-1)q^{k-j-1}\); there is one zero value.

Since \(B\) is primitive, invertible row and column operations over \(R_{n-k}\) transform it to \(\operatorname{diag}(1,\det B)\), up to a unit in the second diagonal entry. Thus \(X\) has image length \(n-j\) when \(\nu(\det B)=e+j\), and image length \(n-k\) when \(\det B=0\). Multiplying the numbers of allowable \(B_0\)'s, determinant values and lifts gives exactly the \(k\)-sum in the stated spectrum. In particular, the \(k=0\) layer consists entirely of length-\(n\) images; each \(1\le k<h\) contributes \((q^2-1)(q-1)q^{2n-3}\) length-\(n\) images.

**3. The high valuation cone.** All remaining matrices are divisible by \(\pi^h\). Each can be written uniquely \(X=\pi^hB\) with \(B\in M_2(R_m)\); every such \(X\) is automatically square-zero. Multiplication by \(\pi^h\) identifies the image length of \(X\) with that of \(B\) over \(R_m\).

Classify \(B\ne0\) according to its entry valuation \(a\in\{0,\dots,m-1\}\), and put \(e=m-a\). Its primitive part lies in \(M_2(R_e)\). There are \(G_e\) such primitive parts with invertible reduction, with image length \(2e\). There are \(U=(q^2-1)^2/(q-1)\) nonzero rank-one matrices over the residue field; each admits \(q^{4(e-1)}\) lifts. For each such residue matrix, the determinant ranges uniformly over \(\pi R_e\), using a unit cofactor. The determinant-zero lifts number \(q^{3e-3}\), while determinant valuation \(v\in\{1,\dots,e-1\}\) occurs \((q-1)q^{4e-v-4}\) times. Elementary Smith reduction identifies image lengths \(e\) and \(2e-v\), respectively. Multiplication by \(U\) and summation over \(e\) yields exactly the final sum of the formula; the zero matrix gives \(\mathbf1_{r=0}\).

**4. Corollaries and boundaries.** Summing the low layers yields \(h(q^2-1)q^{2n-2}\); the high cone has \(q^{4m}\) elements. Only the low layers and, for even \(n\), the invertible matrices in the highest cone can attain image length \(n\). In the even case the latter number is \(|GL_2(R_m)|=(q^2-1)(q-1)q^{2n-3}\); in the odd case its maximum image length is \(2m=n-1\). This proves the displayed maximal-length formula. The exact spectrum yields positivity at every \(0\le r\le n\): in the high cone ranks up to \(2m\) occur via diagonal valuation matrices, while the primitive layer realizes \(n\).

Finally, \(\mathbb F_q[t]/(t^n)\)-linear endomorphisms of a free module of rank two are precisely \(\mathbb F_q\)-linear maps commuting with multiplication by \(t\), whose matrix consists of the two indicated Jordan blocks. A square-zero linear map of rank \(r\) has Jordan type \((2^r,1^{2n-2r})\). This supplies the commuting-matrix interpretation without imposing new hypotheses.

## Verification

Run the standalone dependency-free Python program `check_spectrum.py` with `python3 check_spectrum.py`. It enumerates all matrices in twelve small finite chain rings, including equal-characteristic truncated polynomial rings over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\), and mixed-characteristic rings \(\mathbb Z/2^n\mathbb Z\) and \(\mathbb Z/9\mathbb Z\). The program computes the entire additive image explicitly for every square-zero matrix, so it tests the image-length spectrum independently of the Smith-reduction argument. Every tested histogram equals the displayed finite sum, and the layer and maximal-image counts agree. These finite tests supplement, rather than establish, the all-length theorem.

## Relationship to prior work

Nilpotent commuting-matrix Jordan-type existence was studied in Oblak's 2007 preprint and Britnell--Wildon's 2010 preprint. Bogdanić--Đurić--Koljančić--Oblak--Šivic later determined which nilpotent Jordan types intersect the centralizer of a pair of equal Jordan blocks. These are qualitative orbit-existence/classification questions. The present assertion is a finite-field **multiplicity** formula for every square-zero orbit type, together with the more general chain-ring image-length census and a valuation equidistribution result. Ekhad--Zeilberger count square-zero upper-triangular matrices over finite fields, not this centralizer or chain-ring matrix algebra. Historic enumeration of nilpotent matrices over finite rings by Bollman--Ramírez and Brawley is relevant but does not furnish an identifiable version of the joint square-zero/image-length census in the inspected material; full priority remains subject to further historical checks.

## Limitations

The formula concerns the full set of square-zero \(2\times2\) matrices, not nilpotents of higher index or larger matrix size over \(R\). The Jordan-type statement requires \(R=\mathbb F_q[t]/(t^n)\) and the fixed nilpotent type \((n,n)\); mixed-characteristic chain rings have image *lengths*, not an intrinsic \(\mathbb F_q\)-linear Jordan type. It does not count simultaneous similarity orbits of pairs. Independent mathematical audit and exhaustive historical-priority certification have not been performed.

## References

- Polona Oblak, *The upper bound for the index of nilpotency for a matrix commuting with a given nilpotent matrix*, first arXiv version 2007-01-19, arXiv:math/0701561, https://arxiv.org/abs/math/0701561.
- John R. Britnell and Mark Wildon, *On types and classes of commuting matrices over finite fields*, first arXiv version 2010-01-06, arXiv:1001.0811, https://arxiv.org/abs/1001.0811.
- Duško Bogdanić, Alen Đurić, Sara Koljančić, Polona Oblak and Klemen Šivic, *Jordan structures of nilpotent matrices in the centralizer of a nilpotent matrix with two Jordan blocks of the same size*, first arXiv version 2022-12-16, arXiv:2212.08425, https://arxiv.org/abs/2212.08425.
- Shalosh B. Ekhad and Doron Zeilberger, *The Number of Solutions of \(X^2=0\) in Triangular Matrices Over \(GF(q)\)*, Electronic Journal of Combinatorics 3 (1996), R2, https://doi.org/10.37236/1226.
- D. Bollman and H. Ramírez, *On the number of nilpotent matrices over \(\mathbb Z_m\)*, Journal für die reine und angewandte Mathematik 238 (1969), 85–88.
- J. V. Brawley, *Counting Matrices by Drazin Index*, SIAM Journal on Algebraic Discrete Methods 3 (1982), 30–34, https://doi.org/10.1137/0603003.
