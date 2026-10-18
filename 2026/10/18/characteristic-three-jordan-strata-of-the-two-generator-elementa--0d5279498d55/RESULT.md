# Characteristic-three Jordan strata of the two-generator elementary-abelian group algebra

## Finding

Let \(q=3^f\), with \(f\geq 1\), and let \(E=C_3\times C_3\). Write
\[
A=\mathbb F_q[E]\cong\mathbb F_q[x,y]/(x^3,y^3),\qquad \mathfrak m=(x,y).
\]
For \(a\in\mathfrak m\), multiplication \(L_a:A\to A\) is nilpotent of index at most three. The **joint rank enumerator**, valid for every \(f\geq1\), is
\[
\begin{aligned}
\mathcal J_q(U,V)&=\sum_{a\in\mathfrak m}U^{\operatorname{rank}L_a}V^{\operatorname{rank}L_a^2}\\
&=1+(q-1)U+q(q^2-1)U^2+q^3(q^2-1)U^3\\
&\quad+q^3(q^3-q^2)U^4V+q^6(q^2-1)U^6V^3.
\end{aligned}
\]
In particular, these are **all** Jordan types and their exact multiplicities:

| Jordan partition on the nine-dimensional regular module | Number of elements |
| --- | ---: |
| \((1^9)\) | \(1\) |
| \((2,1^7)\) | \(q-1\) |
| \((2^2,1^5)\) | \(q(q^2-1)\) |
| \((2^3,1^3)\) | \(q^3(q^2-1)\) |
| \((3,2^2,1^2)\) | \(q^3(q^3-q^2)\) |
| \((3^3)\) | \(q^6(q^2-1)\) |

Every type listed occurs for every \(q=3^f\), with no other types. Consequently the only multiplication ranks are \(0,1,2,3,4,6\); rank five cannot occur. Among elements of \(\mathfrak m^2\setminus\mathfrak m^3\), the rank-three stratum consists precisely of those whose quadratic leading part lies in the nonzero affine cone over the projective conic \(\beta^2=\alpha\gamma\); it has a free three-dimensional affine space of higher-degree completions. All other quadratic-leading elements have rank four.

## Assumptions and scope

Throughout, the coefficient field has characteristic three and \(A\) is the ordinary commutative group algebra of the elementary-abelian group of order nine. The augmentation ideal \(\mathfrak m\) has eight coefficient parameters. Operators are multiplication on the **entire** nine-dimensional regular module; units and their nonnilpotent multiplication operators are excluded. For \(a\in\mathfrak m\), Frobenius gives \(a^3=0\), hence the pair of ranks \((\operatorname{rank}L_a,\operatorname{rank}L_a^2)\) completely determines its nilpotent Jordan partition.

## Proof

Equip \(A\) with its standard grading. Its homogeneous dimensions in degrees zero through four are \(1,2,3,2,1\), and no higher terms survive. Write each \(a\in\mathfrak m\) uniquely as \(a=L+Q+C+D\), where the terms have degrees one, two, three, four, respectively. Their coefficient dimensions are \(2,3,2,1\).

**Nonzero linear component.** If \(L\ne0\), choose a linear form \(z\) independent of \(L\). The assignment \(x\mapsto a\), \(y\mapsto z\) defines an algebra endomorphism of \(A\): the cubes of all augmentation elements vanish in characteristic three. Its induced map on \(\mathfrak m/\mathfrak m^2\) is invertible, so its filtered map on the finite local algebra is an automorphism. Thus \(L_a\) is similar to multiplication by \(x\). The latter consists of three Jordan blocks of length three, one for each basis vector \(1,y,y^2\), and has rank pair \((6,3)\). Exactly \((q^2-1)q^6\) choices have a nonzero linear part.

**Nonzero quadratic component, no linear component.** Suppose \(L=0\) and write \(Q=\alpha x^2+\beta xy+\gamma y^2\ne0\). The multiplication map from degree one to degree three, in the bases \((x,y)\) and \((x^2y,xy^2)\), has matrix
\[
M_Q=\begin{pmatrix}\beta&\alpha\\\gamma&\beta\end{pmatrix},\qquad
\det M_Q=\beta^2-\alpha\gamma.
\]
Because \(Q\ne0\), the degree-two-to-degree-four multiplication map is a nonzero functional and hence onto the one-dimensional socle. To compute the total rank of multiplication by \(a=Q+C+D\), first quotient its image by the socle: the degree-one inputs then contribute exactly \(\operatorname{rank}M_Q\), while the degree-zero input contributes one additional line distinguished by its nonzero quadratic component. The surjective degree-two-to-degree-four map supplies the final one-dimensional image in the socle. Thus
\[
\operatorname{rank}L_{Q+C+D}=2+\operatorname{rank}M_Q.
\]
Since \(M_Q\) is a nonzero matrix, its rank is one exactly when \(\beta^2=\alpha\gamma\), and otherwise two. Also
\[
a^2=Q^2=(\beta^2-\alpha\gamma)x^2y^2,
\]
using \(2=-1\) in characteristic three and the fact that all products of total degree at least five vanish. Hence the rank pairs are \((3,0)\) on the projective conic and \((4,1)\) off it, independently of the cubic and quartic perturbations. The affine cone \(\beta^2=\alpha\gamma\) has precisely \(q^2\) triples: if \(\alpha\ne0\), each of \(q-1\) choices of \(\alpha\) and \(q\) choices of \(\beta\) determines \(\gamma\); if \(\alpha=0\), necessarily \(\beta=0\) and \(\gamma\) is arbitrary. Thus its nonzero part has \(q^2-1\) triples, while its complement has \(q^3-q^2\). Every quadratic triple has \(q^3\) independent higher-degree completions, yielding the displayed multiplicities.

**Vanishing linear and quadratic components.** If \(L=Q=0\) but \(C\ne0\), multiplication by \(C+D\) maps the degree-zero piece nontrivially into degree three and maps the degree-one piece onto the socle via the perfect multiplication pairing \(A_3\times A_1\to A_4\). Its rank is two and its square vanishes; the number of choices is \((q^2-1)q\). If only \(D\ne0\), multiplication has rank one and square zero, with \(q-1\) choices. The zero element is unique.

Finally, for any nilpotent operator \(N\) with \(N^3=0\) on a nine-dimensional vector space, if \(r=\operatorname{rank}N\) and \(s=\operatorname{rank}N^2\), then the multiplicities of Jordan blocks of sizes three, two, and one are respectively \(s\), \(r-2s\), and \(9-2r+s\). Substituting the six rank pairs above proves the partition table and exact enumerator. Their counts sum to \(q^8=|\mathfrak m|\), so no cases are omitted.

## Verification

The companion executable file `verify_jordan_census.py` constructs all nine-by-nine multiplication matrices from the monomial basis and computes ranks of each matrix and its square directly over finite fields, independently of the graded-block rank argument. It exhausts all \(3^8=6561\) augmentation elements over \(\mathbb F_3\); over \(\mathbb F_9\), it checks every quadratic-leading triple with independently selected higher terms, every cubic-leading pair, all quartic-only elements, and one thousand elements with nonzero linear part. The check uses explicit extension-field arithmetic. It additionally verifies the coefficient normalization for \(q=3,9,27,81\). All tested comparisons passed. These finite checks support, but do not establish, the all-\(f\) theorem; the proof above does.

For \(q=3\), the rank counts are \(1,2,24,216,486,5832\), in increasing rank order \(0,1,2,3,4,6\), summing to \(6561\).

## Relationship to prior work

Carlson, Friedlander, and Pevtsova [1] study elementary-abelian group representations via rank-shifted subgroups and the truncated polynomial presentation, mainly restricting to subspaces mapping isomorphically into \(\mathfrak m/\mathfrak m^2\). Their results encompass the constant generic Jordan type for the regular module, but do not supply the finite-field multiplicities of arbitrary elements in the deeper augmentation layers.

Iarrobino, Macias Marques, and McDaniel [2] develop Jordan types of Artinian algebras, explicitly considering \(k[x,y]/(x^3,y^3)\) in Example 3.8. Their calculation assumes characteristic not two or three and is not a count of all elements. Altafi, Iarrobino, and Khatami [3] classify types of linear forms for height-two complete intersections under characteristic-zero or sufficiently large-characteristic hypotheses, not characteristic three and not arbitrary nonlinear augmentation elements. Thus none of these stated results implies the six exact finite-field fibers given here. A differently phrased historical enumeration remains possible; absolute priority is not claimed.

## Limitations

The theorem is restricted to the rank-two elementary-abelian group of exponent three and to fields of characteristic three. It does not assert a distribution for larger elementary-abelian groups, for exponent greater than three, or for noncommutative modules other than the regular module. The exact literature priority of this small but natural complete census is not independently certified.

## References

[1] J. F. Carlson, E. M. Friedlander, and J. Pevtsova, *Representations of elementary abelian p-groups and bundles on Grassmannians*, arXiv:1106.4474v1, first posted 2011-06-22. https://arxiv.org/abs/1106.4474

[2] A. Iarrobino, P. Macias Marques, and C. McDaniel, *Artinian algebras and Jordan type*, arXiv:1802.07383, first posted 2018-02-21; Example 3.8 and Section 3.2. https://arxiv.org/abs/1802.07383

[3] N. Altafi, A. Iarrobino, and L. Khatami, *Complete intersection Jordan types in height two*, arXiv:1810.00716, first posted 2018-10-01; introduction and main hypotheses. https://arxiv.org/abs/1810.00716
