# The complete characteristic-seventeen a-number stratification of a genus-four cyclic-symmetry family

## Finding

Let \(k=\overline{\mathbb F}_{17}\), let \(a,b\in k\), and put
\[
 Q(t)=t^3+t^2+at+b,\qquad
 \Delta(a,b)=a^2-4a^3-4b-27b^2+18ab.
\]
Assume \(b\Delta(a,b)\ne0\). The smooth genus-four hyperelliptic curve
\[
 H_{a,b}:\quad y^2=x^{10}+x^7+ax^4+bx=xQ(x^3)
\]
is the cyclic-symmetry family studied by Kudo, Nakagawa and Takagi. Define the precise polynomial
\[
 B(a,b)=[t^8]Q(t)^8\in\mathbb F_{17}[a,b],
\]
where brackets mean extraction of the indicated coefficient and every operation is in characteristic \(17\). Define the Jacobian's \(a\)-number by
\(\mathsf a(H)=\dim_k\operatorname{Hom}(\alpha_{17},\operatorname{Jac}(H)[17])\), equal to the dimension of the kernel of the Cartier operator on regular differentials.

**Theorem (complete geometric stratification).** For every pair in the stated smooth locus,
\[
\mathsf a(H_{a,b})=
\begin{cases}
4,&(a,b)=(13,12),\\
3,&(a,b)=(4,12)\text{ or }(10,7),\\
2,&B(a,b)=0\text{ and }(a,b)\ne(13,12),\\
1,&\text{otherwise}.
\end{cases}
\]
The conditions are understood in the order displayed. Thus the \(a\)-number-three locus has **exactly two** points in the entire smooth parameter surface over the algebraic closure; the \(a\)-number-four locus has one; the \(a\)-number-two locus is the remaining part of the divisor \(B=0\) inside the smooth locus; and the generic \(a\)-number is one. Neither ordinary curves (\(\mathsf a=0\)) nor any further parameter exceptions occur in this family.

## Assumptions and scope

The ground field is algebraically closed of characteristic exactly \(17\), and the parameters may lie in *any* algebraic extension of \(\mathbb F_{17}\), not only in the prime field. The discriminant condition is necessary and sufficient for the polynomial \(xQ(x^3)\) to have ten distinct roots: \(x=0\) is simple if \(b\ne0\), while substitution \(t=x^3\) is separable away from zero, so its other roots are simple exactly when the cubic \(Q\) is separable. The curve's smooth completion then has genus \(4\).

This is a statement about the particular two-parameter presentation, not about the number of abstract isomorphism classes of its curves. Rank of the first Cartier operator is not asserted to equal the \(17\)-rank (stable Frobenius rank) or to determine the Newton polygon.

## Proof

Write \(f(x)=xQ(x^3)\), and let \(c_j=[x^j]f(x)^8\). Since \(f^8=x^8Q(x^3)^8\), only coefficients with \(j\equiv2\pmod3\) can be nonzero. On the standard basis \(dx/y,x\,dx/y,x^2dx/y,x^3dx/y\), the Cartier–Manin matrix is \(M_{ij}=c_{17i-j}\), with \(1\le i,j\le4\). Consequently it is exactly
\[
M=\begin{pmatrix}
0&0&A&0\\
0&B&0&0\\
C&0&0&D\\
0&0&E&0
\end{pmatrix},
\]
where
\[
\begin{aligned}
 A&=[t^2]Q(t)^8,&B&=[t^8]Q(t)^8,\\
 C&=[t^{14}]Q(t)^8,&D&=[t^{13}]Q(t)^8,\\
 E&=[t^{19}]Q(t)^8.
\end{aligned}
\]
The three row/column blocks have mutually disjoint supports; hence for every specialization (including over the algebraic closure),
\[
\operatorname{rank}M
=\mathbf 1_{B\ne0}
+\mathbf 1_{(A,E)\ne(0,0)}
+\mathbf 1_{(C,D)\ne(0,0)}.
\tag{1}
\]
All coefficient identities in what follows are in \(\mathbb F_{17}[a,b]\). Expansion gives
\[
 A=b^6(8b-6a^2),\qquad
 E=-2a^2+5ab+8a-2b+5.
\]
On the smooth locus \(b\ne0\), \(A=0\) is equivalent to \(b=5a^2\); after this substitution,
\[
 E(a,5a^2)=8(a+4)(a+7)(a-4),\qquad
 B(a,5a^2)=-8(a+3)(a+4)a^8.
\tag{2}
\]
Therefore \((A,E)=(0,0)\) occurs on the smooth locus **only** at the three points
\[
\mathcal E=\{(4,12),(10,7),(13,12)\}.
\]
They are indeed smooth: their respective cubic discriminants are \(3,4,11\) modulo \(17\).

To rule out any other rank drops from the independently supported block \((C,D)\), an exact elimination identity is
\[
\operatorname{Res}_b(C,D)
=3a^3(a-6)^{12}(a+4)(a+7)(a-4).
\tag{3}
\]
For each possible root of the right-hand side, computation of the monic gcd in \(\mathbb F_{17}[b]\) gives
\[
\begin{array}{c|ccccc}
a&0&6&13&10&4\\\hline
\gcd(C(a,b),D(a,b))&b&(b-12)^3&b-12&b-7&b-12
\end{array}.
\tag{4}
\]
The first candidate \((0,0)\) is excluded by \(b=0\), and the second \((6,12)\) has \(\Delta(6,12)=0\). The other three are exactly \(\mathcal E\). In particular, equations (3)–(4) certify completeness over the **algebraic closure**, not just the prime field: a common root must be among the resultant roots and the specialized gcds exhaust every common root. Thus on the smooth parameter locus the two nontrivial blocks \((A,E)\) and \((C,D)\) vanish simultaneously and exactly at \(\mathcal E\).

Away from \(\mathcal E\), equation (1) now becomes \(\operatorname{rank}M=2+\mathbf1_{B\ne0}\). At the three points of \(\mathcal E\), the matrix rank is just \(\mathbf1_{B\ne0}\), which by (2) equals zero only at \((13,12)\), and one at each of \((4,12)\) and \((10,7)\). Finally, \(\mathsf a(H)=4-\operatorname{rank}M\), giving exactly the stated four cases. For example, \((a,b)=(0,1)\) has \(\mathsf a=2\) and \((1,1)\) has \(\mathsf a=1\), so both nonexceptional strata occur.

## Verification

The companion `verify.py` recomputes every needed coefficient directly from \(f^8\) in characteristic \(17\), verifies (2), verifies the exact polynomial identity (3), computes all five gcds (4), and checks all three exceptional ranks and discriminants. It also checks every smooth prime-field parameter pair as a *supplementary finite check*. The geometric completeness proof is (2)–(4), not the finite-field enumeration. Replay with Python 3 and SymPy using `python verify.py`.

## Relationship to prior work

Kudo–Nakagawa–Takagi (first public preprint 2022, later published 2023), §3.2, supplies the sparse Cartier–Manin matrix of this family for every characteristic in the stated congruence class; §§4.1–4.2 focus on enumerating **superspecial** members where the whole matrix vanishes. Its earlier cited enumeration by Kudo–Harashita also addresses superspeciality. Elkin's cyclic-cover theorem, reviewed in §2.3 of that paper, provides general rank bounds. None of those inspected statements supplies the complete characteristic-\(17\) decomposition into \(a\)-numbers one, two, three and four or identifies the two exceptional rank-one points. This finding is the full rank-stratification computation, not the previously known sparse matrix or the known superspecial example itself.

## Limitations

No claim is made about \(17\)-rank, Newton polygons, Ekedahl–Oort types, all genus-four hyperelliptic curves, or isomorphism distinctions among parameter values. The special \(a\)-number-four member follows the previously studied superspecial locus and is included solely to make the stratification exhaustive. The novelty comparison is literature-based rather than a proof of uniqueness of publication; an unindexed equivalent calculation remains possible.

## References

Kudo, M., Nakagawa, T., Takagi, T., *Efficient search for superspecial hyperelliptic curves of genus four with automorphism group containing* \(C_6\), arXiv:2210.14822v1 (first public 2022-10-26); *Mathematics in Computer Science* **17** (2023), article 21, DOI 10.1007/s11786-023-00571-w, especially Lemma 3.2.1 and §4.

Kudo, M., Harashita, S., *Superspecial hyperelliptic curves of genus 4 over small finite fields*, WAIFI 2018, DOI 10.1007/978-3-030-05153-2_3 (superspecial enumeration, not intermediate ranks).

Elkin, A., *The rank of the Cartier operator on cyclic covers of the projective line*, *Journal of Algebra* **327** (2011), 1–12, DOI 10.1016/j.jalgebra.2010.09.046 (general cyclic-cover rank bounds).
