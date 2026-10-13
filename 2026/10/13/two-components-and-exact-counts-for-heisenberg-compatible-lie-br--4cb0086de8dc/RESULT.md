# Two components and exact counts for Heisenberg-compatible Lie brackets

## Finding

Let \(K\) be any field of characteristic different from \(2\). On the three-dimensional vector space \(V=Kx\oplus Ky\oplus Kz\), fix the Heisenberg bracket
\[
[x,y]=z,\qquad [y,z]=[z,x]=0.
\]
Let \(X_K\) be the **reduced affine variety** of alternating bilinear operations \(\{\cdot,\cdot\}\) for which \(\{\cdot,\cdot\}\) itself is a Lie bracket and all pencils \(s[\cdot,\cdot]+t\{\cdot,\cdot\}\), with \(s,t\in K\), are Lie brackets. The underlying solution set, over every extension field of \(K\), has an explicit two-stratum description. Its geometric reduction has **exactly two irreducible components**, of dimensions \(6\) and \(5\), meeting in a four-dimensional determinantal locus.

For the Lefschetz class \(\mathbb L=[\mathbb A^1_K]\) in the Grothendieck ring of varieties,
\[
\boxed{[X_K]=\mathbb L^6+\mathbb L^5-\mathbb L^3.}
\]
Thus for every odd prime power \(q\),
\[
\boxed{|X_{\mathbf F_q}(\mathbf F_q)|=q^6+q^5-q^3.}
\]
The same formula over every finite extension gives the point-counting zeta function
\[
\boxed{Z(X_{\mathbf F_q},T)=\frac{1-q^3T}{(1-q^5T)(1-q^6T)}.}
\]
These count **actual brackets on the fixed underlying vector space**, not orbits under its automorphism group.

## Assumptions and scope

For all statements involving scheme geometry, \(X_K\) means the reduced variety of solutions to the Jacobi and mixed-Jacobi polynomial identities, not a claim about the scheme structure of the unreduced defining ideal.

The primary source by Ladra, Leite da Cunha and Lopes first appeared publicly as arXiv:2406.04036 on 6 June 2024, with primary Mathematics Subject Classification \(17A30\) listed in the published open-access article. The paper defines compatible Lie brackets and classifies **nilpotent compatible Lie algebras** up to dimension four. Its Examples 2.12 and 2.14 already exhibit distinct compatible second brackets for the fixed three-dimensional Heisenberg bracket, including a second bracket isomorphic to \(\mathfrak{sl}_2\). The question addressed here is the complete parameter variety when the first bracket is fixed but the second need not be nilpotent, together with its geometry and finite-field counts.

## Proof

Write an arbitrary alternating operation as
\[
\begin{aligned}
\{x,y\}&=ax+by+cz,\\
\{y,z\}&=dx+ey+fz,\\
\{z,x\}&=gx+hy+iz,
\end{aligned}
\]
where the nine displayed coefficients range independently through \(K\) before imposing identities.

Since the Jacobiator of an alternating bilinear operation is alternating trilinear, it is sufficient in dimension three to evaluate it at \((x,y,z)\). The mixed-Jacobi identity of the fixed Heisenberg bracket and the second operation has only one potentially nonzero coordinate. Direct substitution gives
\[
g=e.
\]
The Jacobi identity for the second operation, before this substitution, is the vanishing of the vector
\[
\begin{pmatrix}
-ae+bd-di+fg\\
-ah+bg-ei+fh\\
-ai+bf-ce+cg
\end{pmatrix}.
\]
After imposing \(g=e\), set
\[
u=f-a,\qquad v=b-i.
\]
The equations become exactly
\[
\boxed{
\begin{aligned}
eu+dv&=0,\\
hu+ev&=0,\\
bu+av&=0.
\end{aligned}}
\]
Conversely these three equations, together with \(g=e\) and the definitions of \(u,v\), imply both Jacobi identities. They therefore classify **all** compatible brackets, with \(c\) unrestricted.

Let
\[
M=\begin{pmatrix}e&d\\h&e\\b&a\end{pmatrix},\qquad
w=\begin{pmatrix}u\\v\end{pmatrix}.
\]
The solution locus is the incidence condition \(Mw=0\), with one additional free coordinate \(c\). It decomposes into disjoint, locally closed strata:

* \(w=0\). All six parameters \(a,b,c,d,e,h\) are free, giving an affine \(6\)-space \(H\).
* \(w\ne0\). For each fixed nonzero \(w\), the three equations \(Mw=0\) are independent linear conditions on the six variables \(a,b,c,d,e,h\), leaving an affine \(3\)-space. Hence this stratum \(U\) is a rank-three vector bundle over \(\mathbb A^2\setminus\{0\}\).

The second stratum \(U\) is irreducible of dimension \(5\). Its closure \(C\) in the reduced variety is obtained set-theoretically by additionally requiring \(\operatorname{rank}M\le1\), equivalently
\[
e^2-dh=ea-db=ha-eb=0.
\]
Indeed, a nonzero \(w\) in the kernel forces rank at most one. Conversely, when \(w=0\) and rank is at most one, choose nonzero \(w_0\in\ker M\); the curve \((M,tw_0,c)\) lies in \(U\) for \(t\ne0\) and specializes to the required point. Thus \(C\) is irreducible of dimension \(5\), while the irreducible affine subspace \(H\) has dimension \(6\). Neither contains the other, so these are precisely the two irreducible components.

Their intersection is the locus \(w=0\), \(\operatorname{rank}M\le1\). It has dimension \(4\): on the dense open subset \(e\ne0\), the two-by-two minors give a three-parameter family of matrices \(M\), and \(c\) is free; boundary strata have smaller dimension. Over a finite field, the rank-at-most-one matrices \(M\) are counted by their rowspace lines: for each of the \(q+1\) lines there are \(q^2-1\) nonzero matrices respecting the repeated \(e\) entry, plus the zero matrix. The intersection therefore has
\[
q\bigl(1+(q+1)(q^2-1)\bigr)=q^4+q^3-q^2
\]
points.

The disjoint-stratum decomposition yields, in the Grothendieck ring,
\[
[X_K]=[H]+[U]=\mathbb L^6+(\mathbb L^2-1)\mathbb L^3
=\mathbb L^6+\mathbb L^5-\mathbb L^3.
\]
Replacing \(\mathbb L\) by \(q\) gives \(q^6+q^5-q^3\) points over \(\mathbf F_q\). The argument is invariant under replacing \(q\) by \(q^m\), so
\[
\begin{aligned}
Z(X_{\mathbf F_q},T)
&=\exp\left(\sum_{m\ge1}\frac{(q^{6m}+q^{5m}-q^{3m})T^m}{m}\right)\\
&=\frac{1-q^3T}{(1-q^5T)(1-q^6T)}.
\end{aligned}
\]
This completes the description and count.

## Verification

The executable `artifacts/verify.py` derives the complete mixed and ordinary Jacobi vectors symbolically from independent coordinates of the two brackets. It then enumerates all compatible coefficient tuples over \(\mathbf F_3\), \(\mathbf F_5\), and \(\mathbf F_7\), leaving only the provably free coordinate \(c\) unexpanded, and verifies the precise component-stratum counts. In addition it performs a second exhaustive check of all \(3^9=19683\) initial bracket tables directly from the nine original coefficients, before eliminating \(g\) or introducing \(u,v\). It obtains
\[
\begin{array}{c|r|r|r}
q & |X(\mathbf F_q)| & |U(\mathbf F_q)| & |(H\cap C)(\mathbf F_q)|\\\hline
3&945&216&99\\
5&18625&3000&725\\
7&134113&16464&2695
\end{array}
\]
and prints `VERIFY_OK`.

The finite checks do not prove the infinite family; the symbolic reduction, vector-bundle argument, and rank-one stratification above do.

## Relationship to prior work

The source article by Ladra–Leite da Cunha–Lopes treats nilpotent compatible Lie algebras up to dimension four **up to isomorphism**; this is not the same as the full variety of all second Lie brackets compatible with a specified first Heisenberg bracket, because the second bracket need not be nilpotent. In fact the source's Example 2.12 gives a compatible pair whose second bracket is \(\mathfrak{sl}_2\). The article's Example 2.14 already distinguishes compatible pairs with individually isomorphic component Lie algebras. Its 2025 correction concerns orbit calculations for four-dimensional nilpotent extensions, not the fixed-bracket variety counted here.

Liu–Sheng–Bai develop the general Maurer–Cartan and deformation-cohomology formalism for compatible Lie brackets. Panasyuk develops a classification method with a **semisimple** first bracket; the fixed bracket here is nilpotent and nonabelian. Neither accessible source states the present incidence equations, two-component geometry, or exact finite-field formula. Published low-dimensional and finite-field searches were also compared at the statement/implication level rather than inferred from title similarity.

## Limitations

The result counts embedded brackets, not isomorphism orbits. It describes the reduced solution variety only; nilpotent structure of the unreduced defining scheme, cohomological tangent spaces, and singularity types have not been determined. Characteristic \(2\) is excluded to align with the primary convention; the resulting alternating-bracket equations have not been claimed to classify every characteristic-two Lie structure under all conventions. Primary literature and indexed searches cannot exclude an unlocated equivalent formulation in the older Lie-pencil literature.

## References

1. M. Ladra, B. Leite da Cunha, and S. A. Lopes, “A classification of nilpotent compatible Lie algebras,” arXiv:2406.04036v1 (first public 6 June 2024); *Rendiconti del Circolo Matematico di Palermo*, 74, article 70 (2025), DOI `10.1007/s12215-024-01126-z`.
2. M. Ladra, B. Leite da Cunha, and S. A. Lopes, “Correction to: A classification of nilpotent compatible Lie algebras,” *Rendiconti del Circolo Matematico di Palermo*, 74, article 192 (2025), DOI `10.1007/s12215-025-01303-8`.
3. J. Liu, Y. Sheng, and C. Bai, “Maurer–Cartan characterizations and cohomologies of compatible Lie algebras,” arXiv:2102.04742v1; *Science China Mathematics* 66 (2023), 1177–1198.
4. A. Panasyuk, “Compatible Lie Brackets: Towards a Classification,” *Journal of Lie Theory* 24 (2014), 561–623, DOI `10.5802/jolt.797`.
