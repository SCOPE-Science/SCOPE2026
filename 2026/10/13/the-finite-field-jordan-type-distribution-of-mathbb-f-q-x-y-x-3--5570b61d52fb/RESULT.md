# The finite-field Jordan-type distribution of \(\mathbb F_q[x,y]/(x^3,y^3)\)

## Finding

**Theorem (complete multiplication-Jordan census).** Let \(q=p^e\) be any prime power, put \(k=\mathbb F_q\), and let \(A=k[x,y]/(x^3,y^3)\) with maximal ideal \(\mathfrak m=(x,y)\). For each \(u\in\mathfrak m\), let \(P(u)\) be the partition of \(9\) specifying the Jordan blocks of multiplication \(M_u:A\to A\). Write \(N_{\lambda}(q)=\#\{u\in\mathfrak m:P(u)=\lambda\}\), and use exponential partition notation, for instance \((2^3,1^3)=(2,2,2,1,1,1)\).

The following three multiplicities hold in **every** characteristic:

\[
\begin{aligned}
N_{(1^9)}(q)&=1,\\
N_{(2,1^7)}(q)&=q-1,\\
N_{(2^2,1^5)}(q)&=q(q^2-1).
\end{aligned}
\]

For \(p\ne3\), the other seven nonzero multiplicities are

\[
\begin{array}{c|c}
\lambda &N_\lambda(q)\\\hline
(2^3,1^3)&2(q-1)q^3\\
(3,2,1^4)&(q-1)^2q^3\\
(2^4,1)&(q-1)^2q^3\\
(3,2^2,1^2)&(q-1)(q^2-q+1)q^3\\
(3^3)&2(q-1)q^5\\
(4,3,2)&2(q-1)^2q^5\\
\lambda_\mathrm{top}&(q-1)^2q^6
\end{array}
\]

where \(\lambda_\mathrm{top}=(4,4,1)\) if \(p=2\), and \(\lambda_\mathrm{top}=(5,3,1)\) if \(p\ge5\).

For \(p=3\), the **only** other nonzero multiplicities are

\[
N_{(2^3,1^3)}(q)=(q^2-1)q^3,\quad
N_{(3,2^2,1^2)}(q)=(q^3-q^2)q^3,\quad
N_{(3^3)}(q)=(q^2-1)q^6.
\]

Every partition not displayed in the applicable characteristic has multiplicity zero. In all characteristics the sum of the listed multiplicities is exactly \(q^8=|\mathfrak m|\). In particular, the largest Jordan block has size \(5\) when \(p\ge5\), size \(4\) when \(p=2\), and size \(3\) when \(p=3\). The theorem counts all (not necessarily homogeneous) elements of \(\mathfrak m\), including the zero element; scalar-constant units are not in scope.

## Assumptions and scope

The field \(k=\mathbb F_q\) may be a nonprime extension field. The ring is commutative, associative, standard graded, nine-dimensional, and has monomial basis \(\{x^i y^j:0\le i,j\le2\}\). Multiplication by any \(u\in\mathfrak m\) is nilpotent; the phrase Jordan type refers to its nilpotent Jordan partition over \(k\), without extension to an algebraic closure. Let \(\mathfrak m^t\) denote the usual ideal powers, with \(\mathfrak m^5=0\). Only the \(q^8\) coefficients outside the constant term are counted.

## Proof

Write an arbitrary element uniquely as
\[
u=ax+by+cx^2+dxy+ey^2+hx^2y+ixy^2+jx^2y^2,
\quad a,b,c,d,e,h,i,j\in k.
\]
Denote \(r_t=\operatorname{rank}_k(M_u^t)\), so that \(r_0=9\). Since \(M_u^t=M_{u^t}\), these ranks are ranks of principal multiplication operators. The numbers \(r_{t-1}-r_t\) are the column lengths of the Jordan diagram; thus the entire partition follows from \((r_0,r_1,\ldots,r_5)\).

**Case I: \((a,b)\ne(0,0)\).** Multiplication by the degree-one initial form \(ax+by\) has ranks \(1,2,2,1\) on the graded transitions of degrees \(0\to1\), \(1\to2\), \(2\to3\), \(3\to4\). These give six independent leading image directions. Also \(\dim_k A/uA=3\): if \(a\ne0\), the relation \(u=0\) eliminates \(x\) as a formal series in \(y\) in the local quotient, and \(y^3=0\); the remaining relation \(x^3=0\) is automatic because \(x\in(y)\). The symmetric argument applies if \(b\ne0\). Thus \(r_1=6\).

Direct truncated multiplication gives
\[
\begin{aligned}
u^2={}&a^2x^2+2abxy+b^2y^2
+2(ad+bc)x^2y+2(ae+bd)xy^2\\
&+(d^2+2ce+2ai+2bh)x^2y^2,\\
u^3={}&3a^2b\,x^2y+3ab^2\,xy^2
+3(a^2e+2abd+b^2c)x^2y^2,\\
u^4={}&6a^2b^2x^2y^2,\qquad u^5=0.
\end{aligned}
\]
If \(ab\ne0\), the ranks \((r_1,r_2,r_3,r_4)\) are \((6,4,2,1)\) for \(p\ge5\), \((6,4,2,0)\) for \(p=2\), and \((6,3,0,0)\) for \(p=3\). Their partitions are respectively \((5,3,1)\), \((4,4,1)\), and \((3^3)\). There are \((q-1)^2q^6\) elements in this subcase.

If exactly one of \(a,b\) is nonzero, \(r_2=3\). For \(p=3\), \(u^3=0\), so the partition is \((3^3)\). For \(p\ne3\), \(r_3=1\) exactly when the coefficient transverse to the nonzero linear direction is nonzero: \(e\ne0\) when \(a\ne0\), or \(c\ne0\) when \(b\ne0\). These give \((4,3,2)\) with count \(2(q-1)^2q^5\); otherwise the partition is \((3^3)\) with count \(2(q-1)q^5\). For \(p=3\), all \(2(q-1)q^6\) elements of this subcase contribute to \((3^3)\), giving the total \((q^2-1)q^6\) when added to \(ab\ne0\).

**Case II: \(a=b=0\), but \((c,d,e)\ne(0,0,0)\).** Here \(u^3=0\) and
\[u^2=(d^2+2ce)x^2y^2.\]
Set \(\Delta=d^2-ce\) and \(\Gamma=d^2+2ce\). Multiplying \(u\) by \(1,x,y\) and a quadratic monomial exhibits a degree-two direction, a degree-three map with matrix
\[\begin{pmatrix}d&c\\e&d\end{pmatrix}\]
of determinant \(\Delta\), and the socle direction. Consequently
\[
r_1=\begin{cases}3,&\Delta=0,\\4,&\Delta\ne0,\end{cases}
\quad r_2=\begin{cases}0,&\Gamma=0,\\1,&\Gamma\ne0.\end{cases}
\]
The four possible pairs \((r_1,r_2)=(3,0),(3,1),(4,0),(4,1)\) yield \((2^3,1^3)\), \((3,2,1^4)\), \((2^4,1)\), and \((3,2^2,1^2)\), respectively. Each of the two conics \(\Delta=0\) and \(\Gamma=0\) has exactly \(q^2\) rational affine points \((c,d,e)\). For \(p\ne3\), their intersection consists exactly of \(d=0\) and \(ce=0\), hence contains \(2q-1\) points. The four nonzero-triple counts are therefore \(2(q-1)\), \((q-1)^2\), \((q-1)^2\), and \((q-1)(q^2-q+1)\). For \(p=3\), \(\Delta=\Gamma\): the only nonzero-triple types are \((2^3,1^3)\) with \(q^2-1\) and \((3,2^2,1^2)\) with \(q^3-q^2\). In all cases the unrestricted \((h,i,j)\) triple multiplies these counts by \(q^3\).

**Case III: \(a=b=c=d=e=0\).** When \((h,i)\ne(0,0)\), the ideal \((u)\) has dimension \(2\) and \(u^2=0\), yielding \((2^2,1^5)\) in \(q(q^2-1)\) cases. When \(h=i=0\) and \(j\ne0\), the ideal has dimension \(1\), giving \((2,1^7)\) in \(q-1\) cases. Finally \(u=0\) has type \((1^9)\). These three cases exhaust \(\mathfrak m\), and their counts sum to \(q^8\), proving all formulae and emptiness assertions. \(\square\)

## Verification

The accompanying standalone program `check_jordan.py` constructs the nine monomial-basis multiplication matrices and computes exact Gaussian ranks over the finite fields \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5,\mathbb F_7\). It exhaustively verifies all \(2^8=256\) and \(3^8=6561\) maximal-ideal elements in the first two fields, and independently verifies \(2000\) deterministic pseudorandom elements in each of the next three fields. In each test it compares the direct Jordan partition with the proof's coefficient conditions; for the exhaustive cases it also compares full frequency tables with the theorem. The program asserts that formula coefficients sum to \(q^8\). Run with `python3 check_jordan.py`; it finishes with `VERIFY_OK_JORDAN_CI33` on success. These finite tests corroborate, rather than replace, the all-prime-power proof.

## Relationship to prior work

Cook's 2011 work establishes characteristic-dependent Lefschetz criteria for monomial complete intersections; this is the earliest public source used to anchor the historical algebraic question. Iarrobino, Macias Marques, and McDaniel's *Artinian algebras and Jordan type* (in particular Example 3.8 and §3.2) **already explicitly discusses the same ring** \(k[x,y]/(x^3,y^3)\), including the Jordan type of \(x^2+y^2\), and describes possible partitions in suitable large characteristic, attributing a support observation to earlier seminar work. The possible-partition support in characteristic \(p\ge5\) is therefore **not** claimed as new here. Altafi, Iarrobino and Khatami determine Jordan partitions arising from *linear forms* in height-two complete intersections over algebraically closed fields of characteristic zero or sufficiently large characteristic. In contrast, the theorem here counts **each entire finite-field fiber**, including nonhomogeneous elements and positive characteristic \(2\) or \(3\), and provides exact polynomial multiplicities. The above sources do not state the present finite-field census in the inspected relevant sections. A historical calculation elsewhere might be equivalent; the search cannot establish absolute novelty.

## Limitations

This is a finite-field enumeration for one fixed nine-dimensional local algebra, not a uniform formula for other truncation exponents or arbitrary complete intersections. It does not classify automorphism orbits of elements with the same Jordan type. Support classification for large characteristic is partly known, as credited. The proof is exact for all prime powers, while finite program tests cover only the specified fields and elements. Independent mathematical review has not been carried out; the bibliographic review is not exhaustive.

## References

1. David Cook II, *The Lefschetz properties of monomial complete intersections in positive characteristic*, arXiv:1111.4979v1 (first publicly posted 2011-11-21), https://arxiv.org/abs/1111.4979 .
2. Anthony Iarrobino, Pedro Macias Marques, Chris McDaniel, *Artinian algebras and Jordan type*, arXiv:1802.07383, especially Example 3.8 and §3.2, https://arxiv.org/abs/1802.07383 .
3. Nasrin Altafi, Anthony Iarrobino, Leila Khatami, *Complete intersection Jordan types in height two*, arXiv:1810.00716, especially §§2–3, https://arxiv.org/abs/1810.00716 .
