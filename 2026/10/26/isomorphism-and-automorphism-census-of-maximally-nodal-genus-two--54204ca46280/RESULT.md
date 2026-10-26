# Isomorphism and automorphism census of maximally nodal genus-two curves with fixed elliptic normalization

## Finding
Fix an odd prime \(p\), a power \(s=p^r\) with \(r\ge1\), \(q=s^2\), and a maximal elliptic curve \(E/\mathbb F_q\), meaning \(\#E(\mathbb F_q)=(s+1)^2\). Put \(n=s-1\). Let \(\mathcal C(E)\) be the set of \(\mathbb F_q\)-isomorphism classes of geometrically integral projective curves having arithmetic genus \(2\), geometric genus \(1\), precisely one nonsplit rational node, normalization \(\mathbb F_q\)-isomorphic to \(E\), and \(\#C(\mathbb F_q)=q+2s+2\). Then there is a natural bijection
\[
\mathcal C(E)\ \longleftrightarrow\ (E[n]\setminus\{0\})/\operatorname{Aut}_{\mathbb F_q}(E,O),
\]
where \(O\) is any chosen rational origin, the right side consists of orbits on the geometric \(n\)-torsion, and changing the origin yields the corresponding canonical identification. In particular, the following **complete automorphism-order census** holds. Each table entry is the number of isomorphism classes with the displayed full \(\mathbb F_q\)-automorphism-group order; all omitted orders have count zero.

| Characteristic and elliptic invariant | Classes of order \(2\) | Order \(4\) | Order \(6\) | Order \(8\) | Total |
| --- | ---: | ---: | ---: | ---: | ---: |
| \(p\ge5\), \(j(E)\notin\{0,1728\}\) | \((n^2-4)/2\) | \(3\) | \(0\) | \(0\) | \(n^2/2+1\) |
| \(p\ge5\), \(j(E)=1728\) | \((n^2-4)/4\) | \(1\) | \(0\) | \(1\) | \(n^2/4+1\) |
| \(p\ge5\), \(j(E)=0\) | \((n^2-4-2\varepsilon)/6\) | \(1\) | \(\varepsilon\) | \(0\) | \((n^2+2+4\varepsilon)/6\) |
| \(p=3\) (necessarily \(j(E)=0\)) | \((n^2-4)/12\) | \(0\) | \(0\) | \(1\) | \((n^2+8)/12\) |

Here \(\varepsilon=1\) if \(3\mid n\), otherwise \(\varepsilon=0\). The rows are conditional on the existence of an \(E\) with the indicated invariant; no existence claim for every row and base field is made.

## Assumptions and scope
An isomorphism means an isomorphism of projective curves *over \(\mathbb F_q\)*, without a marked normalization, point, or elliptic group origin. A nonsplit rational node has two geometric branches exchanged by \(q\)-Frobenius. No plane embedding is fixed. The full automorphism group is \(\operatorname{Aut}_{\mathbb F_q}(C)\), not a projective stabilizer. In characteristic \(3\), the invariant \(1728\) equals \(0\), and the last row applies. The odd-characteristic hypothesis is essential to the group-type table.

## Proof
**1. Singularization and maximality.** For a degree-two closed point \(P\in E\), let \(C_P\) be the projective pinching of its residue field \(\mathbb F_{q^2}\) to \(\mathbb F_q\): the new local ring is \(\mathbb F_q+\mathfrak m_P\) inside the normalization DVR \(\mathcal O_{E,P}\). Its conductor is \(\mathfrak m_P\), and its normalization-quotient has \(\mathbb F_q\)-length one. Over an algebraic closure, the two branches are transverse; thus it is a nonsplit rational node. The arithmetic genus is \(1+1=2\). The degree-two point is replaced by one rational point, so \(\#C_P(\mathbb F_q)=\#E(\mathbb F_q)+1=(s+1)^2+1=q+2s+2\). Conversely, a curve with the defining properties has exactly this unique local ring at its node (the only codimension-one subalgebra containing the conductor of colength one). Thus it arises from a degree-two closed point of the fixed normalization. A curve isomorphism lifts uniquely to a normalization isomorphism; hence \(C_P\cong C_Q\) precisely when some \(\mathbb F_q\)-automorphism of \(E\) takes \(P\) to \(Q\).

**2. The exact torsion reduction.** Since \(E\) is maximal over the square field, its Frobenius endomorphism \(\pi\) has characteristic polynomial \((T+s)^2\). As elliptic endomorphism algebras have no nonzero nilpotents, \(\pi=[-s]\). Therefore
\[
E(\mathbb F_q)=\ker(\pi-1)=E[s+1],\qquad E(\mathbb F_{q^2})=\ker(\pi^2-1)=E[s^2-1].
\]
Both factors \(s-1\), \(s+1\) are prime to \(p\). Multiplication by \(s+1\) induces an exact sequence of finite abelian groups
\[
0\to E[s+1]\longrightarrow E[s^2-1]\xrightarrow{\ [s+1]\ }E[s-1]\to0.
\]
For a geometric point \(R\) above a degree-two point, the difference \(D=R-\pi(R)=[s+1]R\) is nonzero. Translation by \(E(\mathbb F_q)\) changes \(R\) without changing \(D\), and the Frobenius-conjugate choice \(\pi(R)\) changes \(D\) to \(-D\) because \(\pi(D)=-sD=-D\) on \(E[s-1]\). Every \(\mathbb F_q\)-automorphism of the unpointed elliptic curve is \(R\mapsto uR+T\) with \(T\in E(\mathbb F_q)\) and \(u\in U=\operatorname{Aut}_{\mathbb F_q}(E,O)\). Maximal Frobenius is central, so every geometric origin-preserving automorphism descends to \(\mathbb F_q\). Since \(-1\in U\), closed-point orbits correspond exactly to \(U\)-orbits on \(E[n]\setminus\{0\}\).

**3. Automorphism orders.** If a nonzero difference \(D\) has a \(U\)-orbit of cardinality \(a\), then the full curve automorphism group has order \(2|U|/a\). Indeed, for each \(u\) carrying \(D\) to \(\pm D\), the translation is determined by the target branch. If \(D\ne-D\), there is one translation per qualifying \(u\) and twice as many such \(u\) as the point stabilizer. If \(D=-D\), there are two translations for each point-stabilizing \(u\), exchanging or preserving the two *distinct* branches. Both cases give \(2|U|/a\).

**4. Orbit enumeration, including exceptional characteristics.** As \(p\nmid n\), \(E[n]\cong(\mathbb Z/n\mathbb Z)^2\), and \(n\) is even.

When \(p\ge5\), the group \(U\) is cyclic of order \(2\), \(4\), or \(6\), respectively for generic \(j\), \(j=1728\), and \(j=0\). For \(U=C_2\), the three nonzero two-torsion differences are singleton orbits and every other difference lies in a pair. For \(U=C_4\), the order-four generator fixes exactly one nonzero two-torsion element; the other two nonzero two-torsion elements form one pair and every remaining nonzero difference lies in a four-element orbit. For \(U=C_6\), the three nonzero two-torsion points form one three-element orbit. If \(3\mid n\), the two nonzero fixed points of its order-three subgroup form one two-element orbit; there are none if \(3\nmid n\). All remaining differences form six-element orbits. The rows follow by subtracting these exceptional points from the total \(n^2-1\).

In characteristic \(3\), \(U\) has order \(12\), its center is \(\{\pm1\}\), and its quotient acts as the full permutation group of the three nonzero points of \(E[2]\). Each element of order three has no nonzero prime-to-three torsion fixed point (its origin is its only geometric fixed point), while each order-four element fixes exactly one nonzero two-torsion element. Hence the three nonzero two-torsion elements form one orbit of size three; all \(n^2-4\) remaining differences have orbits of size twelve. This gives the final row and completes the table.

## Verification
A separate finite orbit checker `verify.py` enumerates the indicated actions on \((\mathbb Z/n\mathbb Z)^2\) for the sample powers \(s=3,5,7,9,11,13,17,25,27\) when the corresponding row is algebraically possible. It checks the number of orbits and their stabilizer orders and reports `ALL_ORBIT_CHECKS_PASSED`. Finite enumeration is a consistency check, **not** the proof for all \(s\); the proof is the fixed-point and orbit analysis above. The geometric group classifications and local pinching descriptions are required theoretical inputs.

## Relationship to prior work
Hilario--Salomão--Vidal Martins (arXiv:2609.22557, 2026) study the construction and gonality of maximal singular curves from smooth normalizations and give the non-split node model. Aubry--Iezzi (arXiv:1501.03676 and arXiv:1510.01853, 2015) establish constructions and point-count bounds for singular curves. These sources determine the maximal point count and existence framework, but the inspected discussions do not give the fixed-normalization \(\mathbb F_q\)-isomorphism-class census or the four-row full curve-automorphism distribution. Standard boundary-moduli descriptions of one-nodal genus-two curves conceptually imply the *orbit reduction*, not the four explicit arithmetic orbit-and-stabilizer counts without the finite-field Frobenius specialization and fixed-point calculations.

## Limitations
The classification fixes the \(\mathbb F_q\)-isomorphism class of the maximal elliptic normalization; it does not sum over all maximal elliptic curves. It assumes odd characteristic and does not classify nonmaximal curves, other singularity types, or curves of higher arithmetic genus. Classical point-pair moduli and finite elliptic automorphism theory are known, so implicit priority in a broad moduli point-count reference cannot be excluded; no claim of independent validation is made.

## References
1. C. Hilario, R. Salomão, R. V. Martins, *Maximal singular curves over finite fields from elliptic and hyperelliptic curves*, arXiv:2609.22557 (first posted 2026-09-18), https://arxiv.org/html/2609.22557v2.
2. Y. Aubry, A. Iezzi, *On the maximum number of rational points on singular curves over finite fields*, arXiv:1501.03676 (2015), https://arxiv.org/html/1501.03676v2.
3. Y. Aubry, A. Iezzi, *Optimal and maximal singular curves*, arXiv:1510.01853 (2015), https://arxiv.org/html/1510.01853v1.
4. Standard classifications of automorphisms of elliptic curves and of the irreducible one-node boundary of genus-two stable-curve moduli; used only for the stated group list and normalization-by-two-branches description.
