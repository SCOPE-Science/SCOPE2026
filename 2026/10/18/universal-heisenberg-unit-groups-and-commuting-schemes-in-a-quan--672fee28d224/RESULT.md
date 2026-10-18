# Universal Heisenberg unit groups and commuting schemes in a quantum-exterior family

## Finding

Let \(k\) be any field and \(\lambda\in k\setminus\{1\}\). Consider the unital associative algebra
\[
 A_\lambda=k\langle x,y\rangle/(x^2,y^2,yx-\lambda xy).
\]
For \(\lambda\ne0\) this is a two-generator quantum complete intersection; the parameter \(\lambda=0\) is its monomial endpoint. All these algebras are noncommutative, four-dimensional, split local, and have radical cube zero. Nevertheless, their **algebraic unit-group schemes** are mutually isomorphic, and so are their **schemes of pairwise-commuting ordered tuples of every length**:
\[
 A_\lambda^\times\cong\mathbb G_m\times U_3,
 \qquad
 C_s(A_\lambda)\cong \mathbb A^{2s}\times D_{2,s}^{\le1}\quad(s\ge1).
\]
Here \(U_3\) is the algebraic group of upper unitriangular three-by-three matrices, and \(D_{2,s}^{\le1}\) is the determinantal scheme of two-by-\(s\) matrices of rank at most one. The isomorphisms hold as schemes/groups over \(k\), not merely as bijections on points; they apply in characteristic two as well.

Yet these associative algebras are distinguished by their multiplication parameter: for \(\lambda,\mu\ne1\),
\[
 A_\lambda\cong A_\mu\quad\Longleftrightarrow\quad
 \lambda=\mu\ \text{ or }\ (\lambda\mu=1\text{ with }\lambda\mu\ne0).
\]
Consequently, over \(\mathbb F_q\) the family contains exactly \(\lceil q/2\rceil\) pairwise nonisomorphic algebras sharing those group and commuting-scheme invariants. In particular, for \(q\ge3\), these invariants do not reconstruct the algebra. Dimension four is the smallest dimension for a **noncommutative split local** associative \(k\)-algebra, so the counterexample is dimension-sharp within that natural class.

Over every finite field \(\mathbb F_q\), the exact number of commuting ordered \(s\)-tuples of arbitrary algebra elements is
\[
 \# C_s(A_\lambda)(\mathbb F_q)
 =q^{2s}\big((q+1)q^s-q\big),\qquad s\ge1.
\]
For example, over \(\mathbb F_3\), \(A_0\) and \(A_2\) are nonisomorphic (their radical multiplication matrices have different ranks), but both have unit group \(\mathbb F_3^\times\times U_3(\mathbb F_3)\) of order \(54\), and both have \(2673\) commuting ordered pairs.

## Assumptions and scope

All algebra isomorphisms are unital \(k\)-algebra isomorphisms. A **split local** algebra has Jacobson radical \(J\) with \(A/J\cong k\). The unit-group statement is functorial on commutative \(k\)-algebras and thus an isomorphism of affine algebraic groups. \(C_s(A)\) is the affine scheme defined in \(A^s\) by the coefficient equations \([a_i,a_j]=0\) for all \(i<j\). There are no algebraic-closedness or characteristic restrictions; for the enumerative statement \(k=\mathbb F_q\), with any prime power \(q\).

## Proof

**1. Radical and multiplication.** Let \(z=xy\). The defining relations reduce every word to the four normal forms \(1,x,y,z\), and the multiplication table with \(x^2=y^2=0\), \(xy=z\), \(yx=\lambda z\), and \(Jz=zJ=0\) realizes an associative algebra with these linearly independent basis elements. Thus \(A_\lambda=k1\oplus J\), \(J=kx\oplus ky\oplus kz\), \(J^2=kz\), \(J^3=0\). Since \(A/J=k\) and \(J\) is nilpotent, \(J\) is exactly the Jacobson radical and \(A\) is split local. As \([x,y]=(1-\lambda)z\ne0\), the algebra is noncommutative.

**2. Universal unit-group normalization.** Every unit is uniquely \(t(1+ax+by+cz)\) with \(t\in k^\times\); the same description holds on the functor of points over any commutative \(k\)-algebra by replacing invertibility of \(t\) with \(t\) a unit. Radical coordinates multiply by
\[
 (a,b,c)\star(a',b',c')=
 (a+a',\ b+b',\ c+c'+ab'+\lambda ba').
\]
Set \(\kappa=1-\lambda\in k^\times\) and change polynomial coordinates by
\[
 (a,b,c)\longmapsto \big(a,b,(c-\lambda ab)/\kappa\big).
\]
A direct expansion converts \(\star\) into
\[
 (a,b,w)\cdot(a',b',w')=(a+a',b+b',w+w'+ab'),
\]
the multiplication of \(U_3\). Its inverse coordinate change is \(c=\kappa w+\lambda ab\). The scalar factor \(t\) is central, proving the asserted algebraic-group isomorphism in every characteristic.

**3. Identical commuting schemes.** Write \(a_i=t_i1+u_ix+v_iy+w_iz\). Direct multiplication gives
\[
 [a_i,a_j]=\kappa(u_iv_j-u_jv_i)z.
\]
As \(\kappa\) is invertible in \(k\), the defining ideal of \(C_s\) is exactly the ideal of two-by-two minors of the two-by-\(s\) matrix with rows \((u_i)\), \((v_i)\). The \(t_i,w_i\) are free coordinates, proving the scheme isomorphism. This is equality of ideals after an invertible scalar rescaling, not just equality of reduced sets.

**4. Associative isomorphism classification.** Any isomorphism carries \(J\) to \(J\) and \(J^2\) to \(J^2\). Hence it induces \(P\in\mathrm{GL}_2(k)\) on \(J/J^2\), and a nonzero scale on \(J^2=kz\), intertwining the radical multiplication bilinear forms. The relevant two-by-two matrix is
\[
 B_\lambda=\begin{pmatrix}0&1\\ \lambda&0\end{pmatrix}.
\]
For \(\lambda=0\), \(B_\lambda\) has rank one; for \(\lambda\ne0\), it has rank two, so zero cannot be equivalent to a nonzero parameter. For nonzero \(\lambda\), the similarity class of \(B_\lambda^{-1}B_\lambda^T\) is invariant under scalar congruence. This matrix has eigenvalues \(\lambda\) and \(\lambda^{-1}\); equality of characteristic polynomials requires \(\mu\in\{\lambda,\lambda^{-1}\}\), also in characteristic two. Conversely identical parameters give the identity isomorphism, and if \(\mu=\lambda^{-1}\), swapping the images of \(x,y\) and scaling \(z\) constructs an isomorphism. Thus the condition is necessary and sufficient.

**5. Class count and sharp dimension.** In \(\mathbb F_q\), the allowed parameter \(0\) forms one class. Among nonzero parameters other than \(1\), inversion pairs them. If \(q\) is even, inversion has no fixed parameter besides the excluded \(1\), giving \(1+(q-2)/2=q/2\) classes; if \(q\) is odd, \(-1\) is the one remaining fixed parameter, giving \(1+1+(q-3)/2=(q+1)/2\) classes. This is \(\lceil q/2\rceil\).

For any split local \(k\)-algebra of dimension at most three, \(\dim_k J\le2\). If \(J^2=0\), the algebra is commutative. Otherwise \(\dim J=2\), \(\dim J^2=1\), and nilpotence forces \(J^3=0\). A lift \(x\) of a basis of \(J/J^2\) then satisfies \(J^2=kx^2\), so the algebra is spanned by \(1,x,x^2\), hence is commutative. Dimension four is therefore minimal for the noncommutative split-local phenomenon.

**6. Exact finite-field tuple count.** The free coordinates \(t_i,w_i\) contribute \(q^{2s}\). A two-by-\(s\) matrix of rank at most one is either zero, or has a unique one-dimensional column-space line in \(\mathbb F_q^2\). There are \(q+1\) such lines and \(q^s-1\) nonzero tuples of column coordinates per line, for \(1+(q+1)(q^s-1)=(q+1)q^s-q\) possibilities. Multiplication gives the formula for every \(s\ge1\).

## Verification

The standalone `verify.py` uses only Python 3. It independently checks the unit-coordinate map on \(769916\) pairs of radical elements, the scalar-congruence isomorphism criterion on \(57\) parameter pairs over the prime fields of orders \(2,3,5,7\), the determinantal counting formula at \(s=2,3\) over those fields, and the direct whole-algebra commuting-pair cardinalities for \(q=2,3\). It returns `VERIFY_OK`. These finite checks are diagnostics; the preceding algebraic proof establishes all fields and all arities.

## Relationship to prior work

Bergh–Oppermann (2007) study representation dimension of quantum complete intersections, including the nonzero-parameter subfamily here. Fialowski–Penkava (2013, §§2–3) classify the underlying three-dimensional nilpotent associative algebras by bilinear-form congruence over \(\mathbb C\), including parameter interchange; the algebra-isomorphism test is **not** claimed as a new classification method. Grimley (2016) computes parameter-sensitive Hochschild cohomology for quantum complete intersections and their group extensions. These works motivate the question of what simpler invariants retain from the parameter, but none of the inspected full texts gives this simultaneous algebraic-group and all-arity commuting-scheme collapse, or its sharp split-local dimension-four reconstruction consequence. The observations about unit groups and commuting schemes, not the pre-existing quantum-algebra definitions or bilinear-form classification, form the claimed contribution. A separately inspected classification of two-generated short local algebras (published mathematical record dated 2026-09-20) characterizes monomializability via the Segre-quadric position of the multiplication kernel; it does not establish the unit-group or commuting-scheme collapse claimed here. A general unit-group reconstruction result in unlocated literature might subsume this conclusion; the literature search is not an absolute novelty certificate.

## Limitations

The theorem is for the specified two-generator family, not all four-dimensional local algebras. The least-dimension assertion concerns noncommutative **split local** associative algebras. Although \(q\ge3\) produces distinct examples, \(q=2\) has only one class within this family. The point counts are over finite fields, whereas the scheme and group isomorphisms hold over any field. The proof does not assert equality of Hochschild cohomology, algebra automorphism groups, module categories, or other finer invariants.

## References

1. P. A. Bergh and S. Oppermann, *The representation dimension of quantum complete intersections*, arXiv:0710.2606v1 (first public version 2007-10-13), especially §3. https://arxiv.org/html/0710.2606v1
2. A. Fialowski and M. Penkava, *The moduli space of 4-dimensional nilpotent complex associative algebras*, arXiv:1309.5770v1 (2013-09-23), especially §§2–3 on bilinear-form congruence and the three-dimensional nilpotent family. https://arxiv.org/html/1309.5770v1
3. L. Grimley, *Hochschild cohomology of group extensions of quantum complete intersections*, arXiv:1606.01727v1 (2016-06-06), especially §§1, 3.4, 4. https://arxiv.org/html/1606.01727v1
4. *Segre-quadric monomiality criterion for two-generated short local algebras*, published mathematical record, 2026-09-20, https://github.com/published-finding corpus/2026/blob/main/2026/9/20/SCOPE-segre-quadric-monomiality-two-generated-short-local-algebras--0eb926948571/RESULT.md
