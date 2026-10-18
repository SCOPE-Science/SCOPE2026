# Exact idempotent–nilpotent factorization fibers over finite dual-number rings
## Finding
Let \(k=\mathbb F_q\) be any finite field and \(R=k[\varepsilon]/(\varepsilon^2)\). For \(A\in M_2(R)\), let
\[
\nu_{IN}(A)=\#\{(E,N): E,N\in M_2(R),\ E^2=E,\ N\text{ nilpotent},\ EN=A\},
\]
and similarly define \(\nu_{NI}(A)\) using \(NE=A\). Write \(\bar A\) for reduction modulo \(\varepsilon\), and write \(\operatorname{tr}\bar A\) for its field trace. Then \(\nu_{IN}(A)=\nu_{NI}(A)=\nu(A)\), with the following complete, disjoint cases:
\[
\nu(A)=\begin{cases}
q^6(q+2)+1, & A=0,\\
q^6+1, & A=\varepsilon B\ne0,\ \operatorname{rank}_k B=1,\\
1, & A=\varepsilon B,\ \operatorname{rank}_k B=2,\\
q^4+1, & \operatorname{rank}_k\bar A=1,\ \det_R A=0,\ \operatorname{tr}\bar A=0,\\
(q-1)q^3, & \operatorname{rank}_k\bar A=1,\ \det_R A=0,\ \operatorname{tr}\bar A\ne0,\\
1, & \operatorname{rank}_k\bar A=1,\ \det_R A\ne0,\ \operatorname{tr}\bar A=0,\\
0, & \operatorname{rank}_k\bar A=1,\ \det_R A\ne0,\ \operatorname{tr}\bar A\ne0,\\
0, & \operatorname{rank}_k\bar A=2.
\end{cases}
\]
The expression \(A=\varepsilon B\) in the radical cases identifies \(B\) uniquely with its coefficient matrix over \(k\). In particular, the numbers of ordered products above different target matrices are not determined by image membership alone. The support of the factorization map has the exact size
\[
\#\{A:\nu(A)>0\}=q^4(2q^2-1).
\]

## Assumptions and scope
All fields \(k\) of prime-power cardinality \(q\) and both orders of the two factors are covered. No characteristic restriction is made. Every nilpotent here means an ordinary nilpotent \(2\times2\) matrix over \(R\), not merely a matrix with trace zero. Nilpotence is equivalent to nilpotence after residue reduction because \(\varepsilon M_2(R)\) is a square-zero ideal: if \(\bar N^2=0\), then \(N^4=0\).

The source article establishes that the IN and NI *sets* over finite commutative local principal rings coincide and counts their elements. The present theorem determines the cardinality of every ordered-fiber for the first nonfield chain-ring family. It does not claim a formula for arbitrary finite local rings or higher matrix sizes.

## Proof
**1. Idempotents and nilpotents.** An idempotent in \(M_2(R)\) is conjugate to a diagonal idempotent with rank \(0\), \(1\), or \(2\), because \(R\) is local and each finitely generated projective \(R\)-module is free. Rank zero and rank two give \(E=0\) and \(E=I\), respectively. The rank-one reductions are projections onto a field line along a distinct line; there are \(q(q+1)\) of them. Each rank-one reduction has exactly \(q^2\) idempotent lifts. One way to see this is to write \(E=E_0+\varepsilon X\) with \(E_0=\operatorname{diag}(1,0)\): the first-order idempotent equation is \(E_0X+XE_0=X\), and it allows precisely the two off-diagonal coefficients. Thus the number of rank-one idempotents is \(q^3(q+1)\).

Over \(k\), the nilpotent \(2\times2\) matrices consist of zero and the \((q+1)(q-1)=q^2-1\) nonzero matrices having a common one-dimensional image and kernel. They number \(q^2\). Each has \(q^4\) arbitrary lifts, all nilpotent, so \(M_2(R)\) has exactly \(q^6\) nilpotent matrices.

**2. Zero target.** If \(E=0\), any of the \(q^6\) nilpotents is possible; if \(E=I\), only \(N=0\) is possible. Fix a rank-one idempotent \(E=\operatorname{diag}(1,0)\). The equation \(EN=0\) forces the first row of \(N\) to vanish; the remaining row has the form \((x,y)\). Such \(N\) is nilpotent precisely when \(\bar y=0\), giving \(q^2\cdot q=q^3\) choices. Thus
\[
\nu_{IN}(0)=q^6+1+q^3\cdot q^3(q+1)=q^6(q+2)+1.
\]

**3. Nonzero radical targets.** Take \(A=\varepsilon B\ne0\). The choice \(E=I,N=A\) contributes one. For rank-one \(E\), the equation \(EN=A\) requires \(\bar E B=B\). If \(B\) is invertible, this is impossible. If \(B\) has rank one, \(\operatorname{im}\bar E\) must equal \(\operatorname{im}B\), leaving \(q\) choices for the complementary line and \(q^2\) idempotent lifts of each: \(q^3\) choices of \(E\). In an adapted basis the target has top row \((\varepsilon a,\varepsilon b)\) and bottom row zero. Solutions of \(EN=A\) have arbitrary bottom row \((x,y)\), and their residue reductions are nilpotent precisely when \(\bar y=0\); there are \(q^3\) choices of \(N\). Hence the rank-one radical fiber is \(q^6+1\), and the rank-two radical fiber is \(1\).

**4. Primitive targets with zero determinant.** Assume \(\operatorname{rank}\bar A=1\) and \(\det_R A=0\). Its image is a free rank-one direct summand of \(R^2\). In a basis extending a generator of the image, write
\[
A=\begin{pmatrix}a&b\\0&0\end{pmatrix},\qquad (\bar a,\bar b)\ne(0,0),\qquad \bar a=\operatorname{tr}\bar A.
\]
Every rank-one idempotent satisfying \(EA=A\) is
\[
E_s=\begin{pmatrix}1&s\\0&0\end{pmatrix},\qquad s\in R.
\]
The general solution of \(E_sN=A\) is
\[
N=\begin{pmatrix}a-sx&b-sy\\x&y\end{pmatrix},\qquad x,y\in R.
\]
Its reduction is nilpotent if and only if both its trace and determinant vanish, equivalently
\[
\bar y=\bar s\bar x-\bar a,\qquad
(\bar a\bar s-\bar b)\bar x=\bar a^2.
\]
If \(\bar a=0\), then \(\bar b\ne0\), so for every one of the \(q\) values of \(\bar s\) there is exactly one residue solution, \(\bar x=\bar y=0\). If \(\bar a\ne0\), then the unique forbidden value \(\bar s=\bar b/\bar a\) leaves \(q-1\) values, each with one residue solution. Each residue solution in \((s,x,y)\) has \(q^3\) free dual-number lifts, and no further condition is needed because reduction-nilpotence suffices. Consequently rank-one idempotents yield \(q^4\) or \((q-1)q^3\) factorizations, respectively. The choice \(E=I,N=A\) adds precisely one in the trace-zero case.

**5. Primitive targets with nonzero determinant, and rank-two reductions.** A rank-one idempotent \(E\) has determinant zero, so any target \(EN=A\) has determinant zero. Thus for \(\operatorname{rank}\bar A=1\) and \(\det_R A\ne0\), the only possible factorization is \(E=I,N=A\). This is valid if and only if \(\bar A\) is nilpotent, equivalently \(\operatorname{tr}\bar A=0\). If \(\operatorname{rank}\bar A=2\), no product with a nilpotent factor can give \(A\), since the residue reduction of every nilpotent has rank at most one.

**6. Factor order.** Transposition gives a bijection between factorizations \(EN=A^T\) and \(NE=A\) by sending \((E,N)\) to \((N^T,E^T)\). The eight cases depend only on the rank and trace of \(\bar A\), the determinant of \(A\), and (when \(\bar A=0\)) the rank of \(B\), all unchanged by transpose. Therefore \(\nu_{IN}(A)=\nu_{NI}(A)\) for every target.

Finally, counting targets with positive multiplicity gives \(q^4(2q^2-1)\), agreeing with the independently established image-cardinality formula for the chain-ring length-two case.

## Verification
The accompanying standalone `verify.py` uses exact finite-field and dual-number arithmetic, independently enumerating every element of \(M_2(R)\), every idempotent, and every nilpotent, without using the theorem in the enumeration loop. It then checks both ordered-product maps against the eight-case formula for every target. The completed exhaustive cases are \(q=2,3,4\), including the nonprime field \(\mathbb F_4\). The numbers of targets with positive fibers are \(112\), \(1377\), and \(7936\), respectively; the counts of ordered factor pairs are \(1664\), \(80190\), and \(1318912\). The program also checks the total-fiber sum and the image-size formula. Run `python verify.py` using the Python standard library. The general theorem rests on the proof above, not on these finite checks.

## Relationship to prior work
D. Dolžan, *Products of Nilpotent and Idempotent Matrices over Finite Local Rings* (arXiv:2608.20934v1, first publicly posted 21 August 2026), establishes coincidence of the sets of IN and NI products and their total cardinality for finite commutative local principal rings. Its displayed image count at chain length two is \(q^4(2q^2-1)\); a formula for the number of ordered factorizations over each target is a different, finer invariant.

The published result *Exact fibers of idempotent–nilpotent factorizations in two dimensions* gives all ordered fibers over a finite **field**, with zero-target count \(q^3+2q^2+1\) and nonzero singular fibers \(q+1\) or \(q-1\). Its hypotheses exclude the ring with nonzero nilpotent radical studied here; its field formulas do not imply the dual-number fibers or the determinant-stratified splitting.

Călugăreanu and Pop (2024) study **existence** of factorizations over Prüfer and related domains; dual-number rings are not domains, and no dual-number fiber cardinality follows from their existence criteria.

## Limitations
The theorem is restricted to split dual-number rings \(\mathbb F_q[\varepsilon]/(\varepsilon^2)\) and \(2\times2\) matrices. It does not give the fiber multiplicities over arbitrary finite chain rings or in larger matrix sizes. The motivating preprint was available through its abstract but its full text could not be inspected in this investigation; an unexamined intermediate calculation in that paper is a residual originality risk. Other unindexed work could contain an equivalent result. The computations for three fields independently check examples but do not certify the general theorem.

## References
1. D. Dolžan, *Products of Nilpotent and Idempotent Matrices over Finite Local Rings*, arXiv:2608.20934v1, first posted 21 August 2026.
2. *Exact fibers of idempotent–nilpotent factorizations in two dimensions*, published research record, 4 October 2026. https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-exact-fibers-of-idempotent-nilpotent-factorizations-in-two-dimen--376b6f723a17/RESULT.md
3. G. Călugăreanu and H. F. Pop, *2-Products of Idempotent by Nilpotent Matrices*, Bulletin of the Iranian Mathematical Society 50 (2024), article 61. DOI: 10.1007/s41980-024-00883-y.
