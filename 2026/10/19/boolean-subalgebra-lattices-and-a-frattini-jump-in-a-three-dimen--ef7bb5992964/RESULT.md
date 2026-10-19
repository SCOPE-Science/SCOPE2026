# Boolean subalgebra lattices and a Frattini jump in a three-dimensional evolution family

## Finding

Let \(K\) be a field of characteristic different from \(2\), let \(\lambda\in K^\times\), and define the three-dimensional evolution algebra \(E_\lambda\) with natural basis \(e_1,e_2,e_3\), pairwise zero products of distinct basis elements, and
\[
e_1^2=-e_1-e_3,\quad e_2^2=-2e_1+\lambda e_2+(\lambda-2)e_3,\quad e_3^2=e_1+e_3.
\]
Set
\[
u=e_1+e_3,\quad w=e_1-e_3,\quad v=e_2+e_3,
\quad W=\langle e_1,e_3\rangle,\quad S=\langle u,v\rangle.
\]
When \(\lambda\ne2\), also define
\[
z_\lambda=\frac{1}{\lambda(2-\lambda)}u+\frac1\lambda v.
\]
**Complete ordinary-subalgebra classification:** In all cases the nonzero one-dimensional subalgebras are \(Ku\) and \(Kw\), together with \(Kz_\lambda\) exactly when \(\lambda\ne2\). The two-dimensional subalgebras are exactly \(W\) and \(S\), together with
\[
T=\langle e_2,w\rangle
\]
exactly when \(\lambda=4\). Together with \(0\) and \(E_\lambda\), these are **all** subalgebras, not only evolution subalgebras. In particular, the subalgebra lattices have respectively \(6\), \(7\), and \(8\) elements for \(\lambda=2\), \(\lambda\notin\{2,4\}\), and \(\lambda=4\).

At \(\lambda=4\), the three one-dimensional subalgebras are pairwise distinct and independent; the three two-dimensional subalgebras are their pairwise sums:
\[
W=Ku+Kw,\quad S=Ku+Kz_4,\quad T=Kw+Kz_4.
\]
Thus the **entire subalgebra lattice** of \(E_4\) is the Boolean lattice of rank \(3\). In the sense that every proper subalgebra is an intersection of maximal subalgebras, \(E_\lambda\) is dually atomistic **if and only if** \(\lambda=4\).

For the Frattini subalgebra \(F(E)\), the intersection of all maximal subalgebras, and the Frattini ideal \(\phi(E)\), the largest ideal in that intersection, one has the sharp formula
\[
F(E_\lambda)=\phi(E_\lambda)=
\begin{cases}
Ku,&\lambda\ne4,\\
0,&\lambda=4.
\end{cases}
\]
The Frattini/Boolean threshold \(\lambda=4\) is different from the idempotent-free threshold \(\lambda=2\) of the same non-solvable family.

## Assumptions and scope

Every assertion holds for every field \(K\) with \(\operatorname{char}K\ne2\) and every \(\lambda\in K^\times\), including finite fields and non-algebraically closed fields. A subalgebra is a \(K\)-linear subspace closed under the given multiplication; it need not possess a natural evolution basis. A plane means a two-dimensional subspace of \(E_\lambda\). These hypotheses ensure that polarization is valid and that \(u\) and \(w\) are independent. No assertion is made in characteristic two or at \(\lambda=0\).

## Proof

**1. One-dimensional subalgebras.** Because \(e_1^2=-u\), \(e_2^2=-2u+\lambda v\), and \(e_3^2=u\), the square ideal is \(E_\lambda^2=S\). In its basis \(u,v\), multiplication is
\[
u^2=0,\qquad uv=u,\qquad v^2=-u+\lambda v.
\]
If \(Kx\) is a nonzero one-dimensional subalgebra, then \(x^2=cx\). If \(c\ne0\), the element \(c^{-1}x\) is a nonzero idempotent. Any idempotent is in \(S\). Writing \(x=au+bv\), the equation \(x^2=x\) becomes
\[
2ab-b^2=a,\qquad \lambda b^2=b.
\]
Its only nonzero solution, when one exists, has \(b=1/\lambda\) and \(a=1/[\lambda(2-\lambda)]\); it exists precisely when \(\lambda\ne2\). If \(x^2=0\), write \(x=ae_1+be_2+ce_3\). Comparing \(u,v\) coefficients yields \(b=0\) and \(a^2=c^2\). Since the characteristic is not \(2\), the two nonzero square-zero lines are exactly \(Ku\) and \(Kw\). This proves the line list, without assuming algebraic closure.

**2. Reduction for two-dimensional subalgebras.** Every plane has the form \(P=\ker\ell\), where \(\ell(e_1)=A\), \(\ell(e_2)=B\), \(\ell(e_3)=C\). Put \(\alpha=A+C=\ell(u)\) and \(\beta=B+C=\ell(v)\). For \(x=x_1e_1+x_2e_2+x_3e_3\), direct substitution gives
\[
\ell(x^2)=\alpha(x_3^2-x_1^2)+(\lambda\beta-2\alpha)x_2^2.
\]
By polarization, since \(2\) is invertible, \(P\) is a subalgebra exactly when it is totally isotropic for the symmetric bilinear form with diagonal matrix
\[
\operatorname{diag}(-\alpha,\lambda\beta-2\alpha,\alpha).
\]
If \(\alpha=0\) and \(\beta=0\), then \(P=S\). If \(\alpha=0\) and \(\beta\ne0\), total isotropy forces \(x_2=0\) for all \(x\in P\), so \(P=W\). Both spaces are indeed subalgebras.

Suppose \(\alpha\ne0\). If \(\gamma=\lambda\beta-2\alpha\ne0\), the bilinear form is nonsingular on the three-space, so it admits no totally isotropic plane: \(P\subseteq P^\perp\) would contradict \(\dim P+\dim P^\perp=3\). Thus \(\gamma=0\). In that case the form has rank two and radical \(Ke_2\); a totally isotropic plane must contain this radical, since its image in the nondegenerate hyperbolic quotient has dimension at most one. It is therefore the span of \(e_2\) and a square-zero direction in \(\langle e_1,e_3\rangle\), namely \(u\) or \(w\). The former is impossible because \(\ell(u)=\alpha\ne0\). The latter gives \(P=T=\langle e_2,w\rangle\), whose normal functional can be chosen as \(\ell(x)=x_1+x_3\). For this functional \(\alpha=2\), \(\beta=1\) and \(\gamma=\lambda-4\). Consequently \(T\) is a subalgebra exactly when \(\lambda=4\). This exhausts all planes.

**3. Incidence and Frattini invariants.** Always \(W\cap S=Ku\). At \(\lambda=4\), the additional intersections satisfy
\[
W\cap T=Kw,\qquad S\cap T=Kz_4,
\]
and the triple intersection is zero. The lines \(u,w,z_4\) are independent because \(u,w\) span \(W\), whereas \(z_4\) has nonzero \(e_2\)-coordinate. The intersection/sum relations yield precisely the Boolean rank-three lattice. At other parameters the only maximal proper subalgebras are \(W,S\), and their intersection is \(Ku\), so no intersection of maximal subalgebras equals \(0\). Thus dual atomisticity occurs exactly at \(4\).

Every maximal subalgebra is among the planes listed, because all one-dimensional subalgebras occur within at least one listed plane. Their intersection is \(Ku\) for \(\lambda\ne4\), and \(0\) at \(4\). Finally \(Ku\) is an ideal because
\[
ue_1=-u,\quad ue_2=0,\quad ue_3=u.
\]
Hence the Frattini ideal equals the Frattini subalgebra in both cases. The entire classification follows.

## Verification

The proof is symbolic and valid over arbitrary fields under the stated hypotheses. The accompanying standalone `verify.py` enumerates all projective lines and hyperplanes in \(K^3\) over prime fields, tests closure under multiplication by direct coordinate arithmetic, and checks the entire predicted subalgebra lists, Frattini intersections, and dual atomisticity. The finite verifications supplement the proof rather than establish the all-field quantifier. Run with `python3 verify.py` (Python 3.8 or newer); it prints `VERIFY_OK 22 complete finite-field configurations` for all \(\lambda\in\mathbb F_p^\times\) with \(p=3,5,7,11\).

## Relationship to prior work

Hu and Wen introduce this exact multiplication family and classify its idempotents, square ideal, and solvability behavior; the full ordinary-subalgebra lattice is not stated in their inspected manuscript. Ladra and Pérez-Rodríguez develop the Frattini subalgebra, Frattini ideal, and dual atomisticity for evolution algebras, including results for restricted structural families; they do not enumerate the planes of this Hu–Wen family. A separate published calculation establishes an automorphism-group jump at \(\lambda=4\), but an automorphism-group formula by itself does not determine either the subalgebra lattice or the Frattini ideal. The rank-three Boolean incidence is therefore a separate statement, even though both invariants jump at the same parameter.

The older three-dimensional evolution-algebra classification concerns isomorphism types rather than a complete ordinary-subalgebra incidence computation for this parameter family. A hidden equivalent characterization in that classification or its descendants cannot be excluded without further bibliographic work.

## Limitations

The result excludes characteristic \(2\) and the zero parameter. It does not classify ideals beyond the displayed Frattini ideal, nor arbitrary three-dimensional evolution algebras. The Boolean-lattice conclusion concerns ordinary subalgebras, not a canonical compatible evolution basis. A case-by-case subalgebra census implicit in an earlier classification remains a residual originality risk. No independent mathematical validation has been performed.

## References

1. X.-Y. Hu and R. Wen, *Idempotent-free non-solvable evolution algebras over* \(\mathbb C\), arXiv:2609.25023v1 (2026); open manuscript also posted at Preprints.org, 2026-09-01.
2. M. Ladra and A. Pérez-Rodríguez, *A Frattini theory for evolution algebras*, arXiv:2507.01935 (2025), especially Sections 2, 4, and 5.
3. X. García-Martínez and A. Pérez-Rodríguez, *A note on complete evolution algebras*, *Archiv der Mathematik* 126 (2026), 597–604.
4. Y. Cabrera Casado, M. Siles Molina, and M. V. Velasco, *Classification of three-dimensional evolution algebras*, *Linear Algebra and its Applications* 524 (2017), 68–108; arXiv:1701.07219.
5. *A single symmetry jump in the* \(E_\lambda\) *evolution-algebra family*, published mathematical research note (2026).
