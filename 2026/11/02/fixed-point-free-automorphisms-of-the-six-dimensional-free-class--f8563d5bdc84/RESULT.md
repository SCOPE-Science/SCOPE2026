# Fixed-point-free automorphisms of the six-dimensional free class-two Lie algebra

## Finding

Let \(q\) be any prime power, \(k=\mathbb F_q\), \(V=k^3\), and let \(L=V\oplus\bigwedge^2V\) be the six-dimensional free class-two nilpotent Lie algebra, with bracket \([(v,z),(w,z')]=(0,v\wedge w)\). An automorphism is *fixed-point-free* if its only fixed vector is zero.

**Theorem.** Define \(\epsilon_q=0\) for even \(q\) and \(\epsilon_q=1\) for odd \(q\). The exact number of fixed-point-free \(k\)-linear Lie automorphisms is

\[
\boxed{q^{12}\left(q^6-3q^5+q^4+4q^3+q^2-3q-8-\epsilon_q\right).}
\]

More precisely, every automorphism is uniquely \(\begin{pmatrix}A&0\\B&\bigwedge^2A\end{pmatrix}\), with \(A\in\mathrm{GL}_3(k)\) and \(B\in\operatorname{Hom}_k(V,\bigwedge^2V)\); it is fixed-point-free exactly when the characteristic polynomial \(f_A(T)\) satisfies \(f_A(1)f_A(\det A)\ne0\). The fixed-point-free automorphism locus is a nonempty smooth geometrically irreducible Zariski-open subset of \(\mathrm{GL}_3\times\mathbb A^9\), of dimension \(18\).

## Assumptions and scope

The field is any finite field, including characteristic two. All automorphisms are invertible linear Lie-algebra maps, not automorphisms of an associated finite group. The exterior square is the alternating exterior power over the field; \(v\wedge v=0\) remains valid in characteristic two. The formula counts individual automorphisms with no nonzero fixed vector, not similarity types or automorphisms up to conjugacy. For the geometric assertion, the polynomial conditions are interpreted over every field extension, including an algebraic closure.

## Proof

**1. Automorphisms and fixed vectors.** The derived ideal and center of \(L\) are both \(\bigwedge^2 V\): if \(v\ne0\), then \(v\wedge w\ne0\) for a suitable \(w\in V\). Thus an automorphism preserves the central summand and induces an invertible map \(A\) on \(L/Z(L)=V\). Bracket preservation forces the action on \(Z(L)\) to equal \(\bigwedge^2 A\). Conversely, an arbitrary map \(B:V\to\bigwedge^2V\) produces a bracket-preserving invertible block map, so there are exactly \(q^9\) automorphisms above each \(A\). The characteristic polynomial of this block-triangular map is the product of those of \(A\) and \(\bigwedge^2 A\). Hence the map has no nonzero fixed vector precisely if both diagonal blocks minus the identity are invertible; the choice of \(B\) is irrelevant.

For \(\dim V=3\), the canonical linear-algebra identification \(\bigwedge^2 V\simeq V^*\otimes\det(V)\) identifies \(\bigwedge^2 A\) with \((\det A)A^{-T}\). Therefore

\[
\det(\bigwedge^2 A-I)\ne0
\quad\Longleftrightarrow\quad
\det((\det A)I-A)\ne0.
\]

Together with \(\det(A-I)\ne0\), this is the claimed polynomial criterion. Equivalently, no eigenvalue is \(1\), and no pair of the three eigenvalues (counted with multiplicity over an algebraic closure) has product \(1\).

**2. Exhaustive rational-canonical enumeration.** Write \(\Gamma=|\mathrm{GL}_3(q)|=(q^3-1)(q^3-q)(q^3-q^2)\). Put \(h=\gcd(2,q-1)\), \(r=q-1-h\), \(m=r/2\), and \(t=h-1\). Thus \(r\) is the number of allowed scalar eigenvalues \(\lambda\ne1\) with \(\lambda^2\ne1\), divided into \(m\) inverse pairs, and \(t\) counts the additional self-inverse scalar \(-1\) in odd characteristic.

All degree-three characteristic polynomials and rational-canonical classes fall in exactly five cases. The following quantities count *matrices*, not just characteristic polynomials.

**(a) Irreducible cubic.** All are eligible. There are \((q^3-q)/3\) monic irreducible cubics, and each has one conjugacy class of size \(\Gamma/(q^3-1)\). Contribution:

\[
C_3=\frac{q^3-q}{3}\frac{\Gamma}{q^3-1}.
\]

**(b) Irreducible quadratic times a linear factor.** The linear eigenvalue can be any \(a\in k^\times\setminus\{1\}\), giving \(q-2\) choices. The two conjugate quadratic roots have product equal to the quadratic constant term. Thus the quadratic is excluded exactly when that norm is \(1\). The norm-one subgroup in \(\mathbb F_{q^2}^\times\) has \(q+1\) elements, of which exactly \(h\) are already in \(k^\times\); Frobenius pairs the others, giving \((q+1-h)/2\) forbidden irreducible quadratics. The admissible contribution is

\[
C_{2,1}=(q-2)\left(\frac{q^2-q}{2}-\frac{q+1-h}{2}\right)\frac{\Gamma}{(q^2-1)(q-1)}.
\]

**(c) Three distinct linear eigenvalues.** We must select three values other than \(1\), with no reciprocal pair. We may select at most one from each of the \(m\) inverse pairs, and optionally the single extra self-inverse eigenvalue \(-1\). The number of admissible unordered triples is \(D=8\binom m3+4t\binom m2\), interpreting \(\binom mj=0\) when \(j>m\). Each class has size \(\Gamma/(q-1)^3\), yielding

\[
C_{1,1,1}=\left(8\binom m3+4t\binom m2\right)\frac{\Gamma}{(q-1)^3}.
\]

**(d) Repeated linear root \(\lambda\) twice and another \(\mu\) once.** Eligibility requires \(\lambda^2\ne1\), \(\mu\ne1\), and \(\mu\notin\{\lambda,\lambda^{-1}\}\). This gives \(r(q-4)\) ordered eigenvalue patterns (with the repeated root distinguished). The semisimple and nonsemisimple Jordan forms contribute, in total, \(q^4(q^2+q+1)\) matrices per pattern: their centralizer orders are \(|\mathrm{GL}_2(q)|(q-1)\) and \(q(q-1)^2\), respectively, and one obtains the stated sum upon dividing \(\Gamma\). Thus

\[
C_{2,1}^{\mathrm{split}}=r(q-4)q^4(q^2+q+1).
\]

**(e) One linear root \(\lambda\) of multiplicity three.** It is eligible precisely for \(\lambda^2\ne1\), giving \(r\) choices. The sum of the three conjugacy-class sizes (Jordan types \((1,1,1)\), \((2,1)\), and \((3)\)) is \(q^6\), the number of unipotent \(3\times3\) matrices. Hence

\[
C_{3}^{\mathrm{split}}=rq^6.
\]

The five cases are disjoint and exhaustive; the case expressions with \(r=0\) vanish at the small-field boundaries. Substituting \(h=1\) for even \(q\) and \(h=2\) for odd \(q\) and simplifying their sum gives

\[
C_3+C_{2,1}+C_{1,1,1}+C_{2,1}^{\mathrm{split}}+C_{3}^{\mathrm{split}}
=q^3\left(q^6-3q^5+q^4+4q^3+q^2-3q-8-\epsilon_q\right).
\]

Multiplication by \(q^9\), the number of independent central shears, completes the exact count.

**3. Geometry.** The parameter space of all Lie automorphisms is \(\mathrm{GL}_3\times\mathbb A^9\). Fixed-point-freeness is the nonvanishing of two regular functions \(\det(A-I)\) and \(\det((\det A)I-A)\). It therefore cuts out a Zariski-open subset of this smooth irreducible \(18\)-dimensional variety. It is nonempty over the ground field for every finite \(q\) (the count above is positive), so it is geometrically irreducible, smooth, and of full dimension.

## Verification

The accompanying standalone Python checker independently enumerates all \(q^9\) entries of each \(3\times3\) matrix over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5\), tests invertibility and both polynomial determinants, and compares their exact counts to the theorem. The field of order four is implemented as \(\mathbb F_2[t]/(t^2+t+1)\). It additionally constructs the actual \(6\times6\) Lie-automorphism block matrices with three different central shears and directly checks the rank of the difference from the identity. The admissible matrix counts are respectively \(48,4860,98048,922000\); multiplying by \(q^9\) yields respectively \(24576,95659380,25702694912,1800781250000\) fixed-point-free automorphisms. All tests passed. Execute `python3 verify_fpf_free_two_step_rank3.py` beside this file. These are finite checks; the general result is proved by the rational-canonical enumeration above.

## Relationship to prior work

Free class-two Lie algebras and their automorphism groups are classical. Benito and de-la-Concepción (2014), Section 2, explicitly describe the exterior-square model and the role of general linear automorphisms. Furutani, Markina and Vasil'ev (first publicly posted 2014-10-14), Sections 3–4, use the free class-two algebra as a covering object for pseudo-\(H\)-type quotients. Bryant and Papistas (2000) investigate fixed subalgebras of finite groups acting on relatively free Lie algebras, in a different, often infinite-dimensional setting. A separately indexed exact count for the three-dimensional Heisenberg Lie algebra is a rank-two antecedent; its determinant condition on the one-dimensional center does not determine the reciprocal-eigenvalue condition in rank three. No inspected cited theorem gives this six-dimensional, all-finite-fields count or its parity dependence. This comparison is not an exhaustive claim of publication priority.

## Limitations

The theorem is restricted to rank three and nilpotency class two. It does not count conjugacy classes of automorphisms, cover higher-rank free Lie algebras, or establish analogous formulas for associated finite groups. An independent historical-priority assessment and independent mathematical audit have not been performed. The numerical checker covers four finite fields, not every finite field.

## References

- K. Furutani, I. Markina and A. Vasil'ev, *Free nilpotent and H-type Lie algebras. Combinatorial and orthogonal designs*, arXiv:1410.3767v1 (first posted 2014-10-14), https://arxiv.org/abs/1410.3767 .
- P. Benito and D. de-la-Concepción, *An overview of free nilpotent Lie algebras*, Comment. Math. Univ. Carolin. **55** (2014), 325–339, http://dml.cz/dmlcz/143811 .
- R. M. Bryant and A. Papistas, *On the fixed points of a finite group acting on a relatively free Lie algebra*, Glasgow Math. J. **42** (2000), https://doi.org/10.1017/S0017089500020024 .
- D. Burde and K. Dekimpe, *Fixed-point-free automorphisms of solvable Lie algebras*, https://homepage.univie.ac.at/dietrich.burde/papers/burde_83_fpf.pdf (later contextual comparison only).
