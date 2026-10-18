# Six-line incidence obstruction to a pure-triple degree-eight conic arrangement

## Finding
There is no reduced arrangement in \(\mathbb P^2_{\mathbb C}\) consisting of one smooth conic and six distinct lines whose entire singular locus consists of exactly nine ordinary triple points. Equivalently, the weak-combinatorial type \((d,k;n_2,t,n_3)=(6,1;0,0,9)\), in the notation of Gałecka, is not geometrically realizable.

This is an exclusion of a numerically admissible candidate in the degree-eight nearly-free conic–line problem: its total Tjurina number would be \(36\), matching the necessary numerical nearly-freeness identity with exponents \((4,4)\). The theorem does not assume freeness or near freeness.

## Assumptions and scope
Work over the complex projective plane. An *ordinary triple point* is a point where precisely three smooth local branches meet with three distinct tangent directions. All six lines are distinct; the conic is smooth and irreducible; no other component is present. Any intersection of two components is counted with its local Bézout multiplicity. Nodes, tangencies, singularities of higher multiplicity, and nonordinary triple points are forbidden by the hypothesis.

## Proof
**1. Forced intersection distribution.** Six lines have \(\binom{6}{2}=15\) line–line pair intersections counted with multiplicity. The conic meets the lines in \(6\cdot2=12\) pair intersections counted with multiplicity. Every allowed singularity is either a triple of three lines or a triple of two lines and the conic. Write \(a\) for the second type and \(b\) for the first. The line–conic count gives \(2a=12\), hence \(a=6\). The line–line count gives \(a+3b=15\), hence \(b=3\). Thus the six lines alone must have exactly three ordinary triple points and six ordinary double points; **all six double points must lie on the conic**.

**2. The unique six-line incidence pattern.** Each pair of the three line-only triple points can be joined by at most one of the six lines. The number of line–triple incidences is nine. A line through all three triple points would force six additional distinct lines (two other lines at each triple point), exceeding the six available. Consequently, each line occurs in at most two triple points. At most three lines can occur twice, one joining each pair of triple points. Since the total number of incidences is nine on six lines, exactly three must occur twice and the others once. The former three are the sides of a triangle; the latter three pass one through each of its vertices.

Choose homogeneous coordinates so that the sides are \(x=0\), \(y=0\), and \(z=0\). Because no two lines coincide, a diagonal projective scaling places the other three lines in the form
\[
y=z,\qquad z=x,\qquad x=uy,
\]
where \(u\in\mathbb C\setminus\{0,1\}\). The restriction \(u\ne0\) prevents a repeated coordinate line; \(u\ne1\) prevents the additional three lines from meeting at a fourth line-only triple point.

**3. Conic interpolation obstruction.** The six ordinary double points of these lines are
\[
(0:1:1),\ (1:0:1),\ (u:1:0),\ (1:1:1),\ (u:1:1),\ (u:1:u).
\]
For a homogeneous quadratic \(Q=A x^2+B y^2+C z^2+Dxy+Exz+Fyz\), evaluation at those six points yields the matrix
\[
M(u)=\begin{pmatrix}
0&1&1&0&0&1\\
1&0&1&0&1&0\\
u^2&1&0&u&0&0\\
1&1&1&1&1&1\\
u^2&1&1&u&u&1\\
u^2&1&u^2&u&u^2&u
\end{pmatrix}.
\]
Its exact determinant is
\[
\det M(u)=u^2(u-1)^2\ne0.
\]
Therefore no nonzero quadratic equation, not even a reducible conic, vanishes at all six double points. This contradicts Step 1 and proves the theorem.

For a direct elimination check, the first, second, and fourth evaluations give \(D=C\), \(E=-A-C\), and \(F=-B-C\). The fifth gives \(A u(u-1)=0\), so \(A=0\). The third then gives \(B=-Cu\). The sixth gives \(C u(u-1)=0\), so \(C=0\) and hence every coefficient is zero.

## Verification
The accompanying `verify.py` uses integer polynomial arithmetic to expand the exact \(6\times6\) conic evaluation determinant, checks the six-line incidence pattern by an exhaustive enumeration of possible triple blocks, and verifies the Bézout and Tjurina identities. Execute with `python verify.py` (Python 3.9 or newer; standard library only). The symbolic determinant and the incidence argument prove the assertion over the complex numbers; the sampled coordinate test in the program is a consistency check, not an infinite proof.

## Relationship to prior work
Gałecka (2022), arXiv:2204.13969, formulates the partial classification of nearly-free conic–line arrangements with nodes, tacnodes and ordinary triples, leaves degrees eight and nine unresolved, and provides the intersection and Tjurina identities used to motivate this numerical type. Her paper does not assert this nonrealizability. Dimca and Pokora (2021 preprint), arXiv:2111.12349, classify *free* conic–line arrangements, including exclusions with six lines (Proposition 5.5); those freeness assumptions do not cover the present realizability result independent of freeness. Roulleau (2023), arXiv:2306.01052, studies a six-line incidence operator starting from six-line arrangements having only double points, so its results do not classify this three-line-triple configuration. The proof above is independent of freeness computations.

## Limitations
Only the single weak-combinatorial type \((6,1;0,0,9)\) is excluded. No claim is made concerning the realizability or near freeness of other degree-eight arrangements, degree-nine arrangements, or broader classes of singularities. The statement does not establish a full classification. Possible unnoticed classical equivalents of the six-point conic-interpolation obstruction remain a bibliographic risk; no independent external mathematical audit has been performed.

## References
1. A. Gałecka, *On the nearly freeness of conic-line arrangements with nodes, tacnodes, and ordinary triple points* (first public preprint 2022-04-29), arXiv:2204.13969; published in *Boletín de la Sociedad Matemática Mexicana* 28 (2022), article 67. https://arxiv.org/abs/2204.13969
2. A. Dimca and P. Pokora, *On conic-line arrangements with nodes, tacnodes, and ordinary triple points* (2021 preprint), arXiv:2111.12349. https://arxiv.org/abs/2111.12349
3. X. Roulleau, *On the dynamics of the line operator* \(\Lambda_{\{2\},\{3\}}\) *on some arrangements of six lines* (2023 preprint), arXiv:2306.01052. https://arxiv.org/abs/2306.01052
