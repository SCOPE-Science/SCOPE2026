# First-two-nullity control of rank-one nilpotent commutator spectra

## Finding
Fix an integer \(n\geq 3\), a finite field \(k=\mathbb F_q\) of arbitrary characteristic, and a nilpotent matrix \(J\in M_n(k)\). Let
\[\mathcal X=\{X\in M_n(k):\operatorname{rank}X=1,\ X^2=0\}.\]
Write \(b=\dim\ker J\), \(d=\dim\ker J^2\), and \(c=2b-d\). For \(m\geq0\), let \(L_m=(q^m-1)/(q-1)\) (in particular \(L_0=0\)). Define the following integers:
\[
 A=\frac{(q^n-q^d)q^{n-3}}{q-1},\quad
 B=\frac{(q^d-q^b)q^{n-2}}{q-1},\quad
 E=\frac{(q^b-1)q^{n-1}-(q^n-1)}{q-1},
\]
\[
 P=L_{b-c}L_b+(L_b-L_{b-c})L_{b-1},\quad
 Z=(q-1)P,\quad
 U=2\bigl(L_b(q^{n-1}-1)-Z\bigr),\quad
 V=A+B+E-Z-U.
\]
The auxiliary integer \(E\) need not be nonnegative; it is a correction term, not the size of a subset.

**Joint moment census.** For each pair \((t,s)\in k^2\), the number of matrices \(X\in\mathcal X\) satisfying \(\operatorname{tr}(JX)=t\) and \(\operatorname{tr}(J^2X)=s\) is exactly
\[
 H(t,s)=A+\mathbf1_{s=0}B+\mathbf1_{t=s=0}E.
\]
**Complete commutator similarity classification.** Put \(C_X=[J,X]=JX-XJ\). Every such commutator has rank at most two, and its similarity type and multiplicity are determined as follows (multiplicities refer to the indicated moment fiber):

1. When \(t\ne0\) and the characteristic is odd, \(C_X\) is diagonalizable with eigenvalues \(t,-t,0,\ldots,0\), independently of \(s\). For each fixed nonzero \(t\), its total multiplicity over all \(s\) is \(qA+B\). The descriptions at \(t\) and \(-t\) may represent the same similarity class, but the moment fibers are disjoint.
2. When \(t\ne0\) and the characteristic is two, \(C_X\) is similar to \(\operatorname{diag}(t,t,0,\ldots,0)\) if \(s=0\), with fiber size \(A+B\); it is similar to \(J_2(t)\oplus0_{n-2}\) if \(s\ne0\), with fiber size \(A\) per pair \((t,s)\).
3. When \(t=0\ne s\), \(C_X\) is nilpotent of Jordan type \((3,1^{n-3})\), with exactly \(A\) matrices \(X\) per nonzero \(s\).
4. When \(t=s=0\), the numbers producing respectively the zero commutator, nilpotent Jordan type \((2,1^{n-2})\), and nilpotent Jordan type \((2,2,1^{n-4})\) are exactly \(Z,U,V\). The last type has multiplicity zero when \(n=3\).

All counts are nonnegative integers, and the moment fibers partition the full set of \((q^n-1)(q^{n-1}-1)/(q-1)\) matrices. In particular, **the entire moment-refined similarity distribution depends on the Jordan partition of \(J\) only through \(n\), \(\dim\ker J\), and \(\dim\ker J^2\)**. For example, Jordan types \((5,3)\) and \((4,4)\) have identical distributions over every finite field, although their partitions differ.

## Assumptions and scope
The fixed matrix \(J\) may be zero and may have any nilpotent partition; no restriction is placed on the characteristic of \(k\). The moving matrices \(X\) are nonzero, rank one, and square-zero. The moment values \(t,s\) are literal elements of \(k\), not absolute values or conjugacy invariants of the pair without its distinguished \(J\). For \(n=3\), the fourth similarity type in item 4 cannot occur. The theorem does not concern arbitrary-rank moving nilpotents or arbitrary fixed nonnilpotent matrices.

## Proof
**Step 1: uniform rank-one parametrization.** Every \(X\in\mathcal X\) is \(uv^{\mathsf T}\) for nonzero \(u\in k^n\) and nonzero covector \(v^{\mathsf T}\), with \(v^{\mathsf T}u=0\). Every such \(X\) has exactly \(q-1\) representations \((u,v)\), related by \((u,v)\mapsto(au,a^{-1}v)\) for \(a\in k^\times\). In particular, \(|\mathcal X|=(q^n-1)(q^{n-1}-1)/(q-1)\).

**Step 2: joint moments.** For a fixed nonzero \(u\), the moment conditions are the three linear equations
\[
 v^{\mathsf T}u=0,\qquad v^{\mathsf T}Ju=t,\qquad v^{\mathsf T}J^2u=s.
\]
Because \(J\) is nilpotent, the nonzero vectors in any Jordan chain \(u,Ju,J^2u\) are linearly independent. If \(J^2u\ne0\), these equations are independent and admit \(q^{n-3}\) covectors for every \((t,s)\). There are \(q^n-q^d\) such nonzero \(u\). If \(Ju\ne0\) but \(J^2u=0\), they admit \(q^{n-2}\) covectors exactly for \(s=0\), and there are \(q^d-q^b\) such \(u\). If \(Ju=0\), they admit \(q^{n-1}\) covectors exactly for \((t,s)=(0,0)\), and there are \(q^b-1\) such \(u\). The zero covector was included once for every nonzero \(u\) only in the zero moment fiber; subtract \(q^n-1\) there. Dividing by \(q-1\) proves the formula for \(H(t,s)\).

**Step 3: zero and rank-one commutators.** Let \(K=\ker J\) and \(K^*=\ker J^{\mathsf T}\), each of dimension \(b\). With \(a=Ju\) and \(w^{\mathsf T}=v^{\mathsf T}J\), write \(C_X=a v^{\mathsf T}-u w^{\mathsf T}\). Its rank is at most one precisely when \(u\in K\) or \(v\in K^*\): when neither condition holds, the two left vectors and the two right covectors are respectively independent because \(J\) and \(J^{\mathsf T}\) are nilpotent. It vanishes precisely when both conditions hold. The natural pairing \(K^*\times K\to k\) has rank \(c=2b-d\): in a Jordan basis, each singleton block contributes one nonzero pairing, and every longer block contributes zero. Hence the number of pairs of projective lines \(([u],[v])\) in \(K\) and \(K^*\) with \(v^{\mathsf T}u=0\) equals \(P\). Each pair determines \(q-1\) possible nonzero rank-one matrices, so exactly \(Z=(q-1)P\) commute with \(J\). The set with \(u\in K\) contains \(L_b(q^{n-1}-1)\) matrices, and the same holds for \(v\in K^*\). Their intersection is the commuting set. Inclusion-exclusion yields exactly \(U=2(L_b(q^{n-1}-1)-Z)\) matrices with commutator rank one. Both these ranks necessarily have \(t=s=0\), so the remainder of this fiber, \(V=H(0,0)-Z-U\), has rank two.

**Step 4: similarity type.** Direct multiplication using \(v^{\mathsf T}u=0\) gives
\[
 C_Xu=-tu,\qquad C_X(Ju)=tJu-su,\qquad
 C_X^2=t\bigl((Ju)v^{\mathsf T}+u(v^{\mathsf T}J)\bigr)-sX.
\]
The image lies in \(W=\operatorname{span}\{u,Ju\}\). If \(t\ne0\), this image has dimension two, and the matrix of \(C_X|_W\) in the ordered basis \((u,Ju)\) is \(\begin{psmallmatrix}-t&-s\\0&t\end{psmallmatrix}\). Its nonzero characteristic factor is \((z-t)(z+t)\). In odd characteristic the two eigenvalues differ, so the full operator is diagonalizable, including its zero eigenspace; in characteristic two the restriction is scalar precisely when \(s=0\), otherwise a single size-two Jordan block with eigenvalue \(t\). Since the quotient by \(W\) is annihilated by \(C_X\), and \(t\ne0\), this determines the full similarity type.

If \(t=0\), the same identities give \(C_X^2=-sX\), \(C_X^3=0\). For \(s\ne0\), its square has rank one, so its nilpotent Jordan form contains one size-three block and no additional nontrivial blocks (as \(\operatorname{rank}C_X\le2\)). For \(s=0\), it is square-zero; rank zero, one, or two yields exactly the three types in item 4. This proves all assertions.

## Verification
A standalone standard-library checker, `check_spectrum.py`, enumerates every projective rank-one factorization \(X=uv^{\mathsf T}\) over the specified finite fields, constructs the commutator by matrix multiplication rather than relying on the counting formula, and independently checks its matrix rank, two moments, square/cube conditions, and all proposed fiber multiplicities. Running `python check_spectrum.py` yields `NILPOTENT_RANK_ONE_COMMUTATOR_MOMENT_SPECTRUM_OK 40 34015`: forty exhaustive Jordan-partition/field configurations, involving 34,015 nonzero rank-one square-zero matrices. Tested prime fields are \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_5\); the extension field \(\mathbb F_4\) is also tested. The proof above, rather than finite testing, establishes the unbounded statement.

## Relationship to prior work
Britnell and Wildon studied which nilpotent similarity classes admit commuting representatives, and Oblak studied the possible Jordan forms inside nilpotent centralizers. These works motivate the use of Jordan partitions and centralizers but concern commuting matrices, rather than the similarity type of the **nonzero difference** \([J,X]\) with a fixed \(J\) and rank-one nilpotent \(X\). Harima and Watanabe also study the centralizer algebra of a nilpotent matrix (under the term “commutator algebra”), not this distribution. Classical work of Guralnick and Neubauer concerns loci where the commutator itself has rank at most one; its accessible abstracts do not establish this complete rank-two and moment-refined finite-field census, but the full texts were not available for comparison. The rank-one-square-zero fixed-matrix special case was previously counted; it is subsumed here, and no novelty is claimed for that special case. The new full-family conclusion relates the entire distribution to the first two kernel dimensions and identifies the characteristic-two similarity refinement.

## Limitations
Historical priority has not been independently certified, and the inaccessible Guralnick and Neubauer papers remain a residual comparison risk. The theorem does not count full simultaneous-conjugation orbits of pairs, general moving nilpotents, or nonsplit eigenvalue strata for a fixed nonnilpotent matrix. Counts refer to actual matrices in the fixed nilpotent similarity class's ambient space, not isomorphism classes of pairs. No independent audit has been performed.

## References
1. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811 (first posted 2010-01-06), later J. London Math. Soc. 83 (2011), 470–492.
2. P. Oblak, *The upper bound for the index of nilpotency for a matrix commuting with a given nilpotent matrix*, arXiv:math/0701561 (first posted 2007-01-19), Linear Multilinear Algebra 56 (2008), 701–711.
3. P. Oblak, *On the nilpotent commutator of a nilpotent matrix*, arXiv:1106.1545 (first posted 2011-06-08), Linear Multilinear Algebra 60 (2012), 599–612.
4. T. Harima and J. Watanabe, *The commutator algebra of a nilpotent matrix and an application to the theory of commutative Artinian algebras*, arXiv:1206.6574 (first posted 2012-06-28).
5. R. M. Guralnick, *A note on pairs of matrices with rank one commutator*, Linear Multilinear Algebra 8 (1979), 97–99, DOI:10.1080/03081087908817305 (abstract consulted; full text unavailable).
6. M. G. Neubauer, *The variety of pairs of matrices with rank at most one commutator*, Proc. Amer. Math. Soc. 105 (1989), 787–792, DOI:10.1090/S0002-9939-1989-0931743-4 (abstract consulted; full text unavailable).
