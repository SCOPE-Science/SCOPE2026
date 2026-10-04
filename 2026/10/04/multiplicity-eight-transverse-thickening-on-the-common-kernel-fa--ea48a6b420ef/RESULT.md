# Multiplicity-eight transverse thickening on the common-kernel Fano component
## Finding
Let \(k\) be an algebraically closed field with \(\operatorname{char} k\ne 2\), and let \(F_2(\mathrm{SD}^3_3)\subset \operatorname{Gr}(3,\operatorname{Sym}^2 k^3)\) be the Fano scheme of projective planes consisting entirely of singular ternary quadrics. Let \(C_2(0)\) be the component whose reduced points are the planes with a common kernel. Then, at every point of \(C_2(0)\), a Grassmann-chart neighborhood of the Fano scheme is isomorphic to
\[
\mathbb A^2\times \operatorname{Spec} R,
\]
where
\[
R=k[A,H,K,C]/(A^2,AH,H^2+2AK,AC-HK,2CH-K^2,CK,C^2).
\]
The radical of the transverse algebra is \((A,H,K,C)\), its maximal ideal has cube zero, and its Hilbert function is \((1,4,3)\). In particular, \(\operatorname{length}_k R=8\). Consequently the common-kernel component occurs with scheme-theoretic multiplicity \(8\) in \(F_2(\mathrm{SD}^3_3)\), and its transverse nilpotent structure is uniform along the component.

## Assumptions and scope
The ground field is algebraically closed of characteristic different from \(2\), matching the standing hypothesis of the primary source. Here \(\mathrm{SD}^3_3\subset\mathbb P(\operatorname{Sym}^2 k^3)\cong\mathbb P^5\) is the cubic determinant hypersurface of singular symmetric \(3\times3\) matrices. The primary source proves that \(F_2(\mathrm{SD}^3_3)\) is the disjoint union of two two-dimensional components \(C_2(0)\) and \(C_2(1)\), that each is a single \(\operatorname{GL}_3\)-orbit in its reduced structure, and that \(C_2(0)\) is generically non-reduced. The claim here refines the scheme structure only along \(C_2(0)\).

## Proof
Choose the common-kernel plane
\[
Q_0=\left\{\begin{pmatrix}x&y&0\\y&z&0\\0&0&0\end{pmatrix}:x,y,z\in k\right\}.
\]
On the standard affine chart of \(\operatorname{Gr}(3,\operatorname{Sym}^2 k^3)\) centered at \(Q_0\), a nearby plane is represented by
\[
M(x,y,z)=
\begin{pmatrix}
x&y&a_1x+b_1y+c_1z\\
y&z&a_2x+b_2y+c_2z\\
a_1x+b_1y+c_1z&a_2x+b_2y+c_2z&a_3x+b_3y+c_3z
\end{pmatrix}.
\]
The Fano condition is the polynomial identity \(\det M(x,y,z)=0\). Equating its ten cubic coefficients gives the chart ideal. Three of those coefficients solve exactly for
\[
a_3=a_1^2+2a_2c_2,\qquad b_3=2b_1b_2,\qquad c_3=2a_1c_1+c_2^2.
\]
Now set
\[
s=a_1,\qquad t=b_1,\qquad A=a_2,\qquad C=c_1,\qquad H=b_2-a_1,\qquad K=c_2-b_1.
\]
After substitution, all dependence on \(s,t\) disappears and the remaining equations are exactly
\[
A^2=AH=H^2+2AK=AC-HK=2CH-K^2=CK=C^2=0.
\]
Thus this Grassmann chart is \(\mathbb A^2_{s,t}\times\operatorname{Spec}R\).

With lexicographic order \(A>H>K>C\), a Gröbner basis of the transverse ideal is
\[
A^2,\ AH,\ 2AK+H^2,\ AC-HK,\ H^3,\ H^2K,\ HK^2,\ 2CH-K^2,\ K^3,\ CK,\ C^2.
\]
Hence the standard monomials are
\[
1,\ A,\ H,\ K,\ C,\ H^2,\ HK,\ K^2.
\]
They form a basis of \(R\), giving Hilbert function \((1,4,3)\) and length \(8\). The same Gröbner basis shows \(A^2=C^2=H^3=K^3=0\), so the radical is the maximal ideal \((A,H,K,C)\); all cubic monomials vanish, so its cube is zero. The reduced chart is therefore the \((s,t)\)-plane, exactly the common-kernel locus near \(Q_0\).

The source proves that \(C_2(0)\) is a single \(\operatorname{GL}_3\)-orbit. Since the \(\operatorname{GL}_3\)-action preserves the Fano scheme, the local chart type above transports to every point of \(C_2(0)\). At the generic point of the reduced component the local ring therefore has transverse length \(8\), which is the scheme-theoretic multiplicity of the component.

## Verification
The bundled `verify.py` reconstructs the determinant from the Grassmann chart, verifies all ten coefficient equations, performs the three eliminations and coordinate change, checks equality with the seven-generator transverse ideal, computes the stated Gröbner basis, and verifies that every cubic monomial in the transverse maximal ideal reduces to zero. It returns `transverse_hilbert_function=1,4,3`, `transverse_length=8`, `local_tangent_dimension=6`, and `VERIFY_OK`. The tangent dimension \(6=2+4\) also matches the primary source's general tangent-excess formula, which gives excess \(4\) over the two-dimensional component in this case.

## Relationship to prior work
Mokhtar's primary source identifies \(F_2(\mathrm{SD}^3_3)\) as two disjoint two-dimensional components and proves that \(C_2(0)\) is generically non-reduced, but its proof uses tangent-space excess and does not determine a transverse local algebra, a multiplicity, or a nilpotence order. Text searches of the accessible full source for “multiplicity”, “local ring”, “thickening”, and “length 8” produced no covering statement. Abdallah--Emsalem--Iarrobino classify projective orbits of nets of conics; that classification concerns reduced orbit geometry rather than this Fano-scheme thickening. Chan--Ilten compute formal neighborhoods for planes on the full \(3\times3\) determinantal hypersurface, where several components and embedded pieces occur, but that ambient nonsymmetric calculation does not imply the local scheme structure of the symmetric common-kernel component computed here.

## Limitations
The calculation is specific to the plane Fano scheme \(F_2(\mathrm{SD}^3_3)\) and to the common-kernel component. Characteristic \(2\) is excluded. The result does not classify arbitrary non-reduced components of \(F_k(\mathrm{SD}^r_n)\), and it does not assert that no equivalent formulation exists outside the searched literature. The orbit-classification paper of Abdallah--Emsalem--Iarrobino was available only through its abstract and secondary bibliographic descriptions during this check; this is retained as a residual literature-access risk, although the current full text of Mokhtar's paper explicitly cites that work only for the reduced orbit classification.

## References
1. Ahmad Mokhtar, *Fano schemes of symmetric matrices of bounded rank*, arXiv:2310.07025. First public version: 2023-10-10. Primary MSC 14M12.
2. Nancy Abdallah, Jacques Emsalem, Anthony Iarrobino, *Nets of Conics and associated Artinian algebras of length 7*, arXiv:2110.04436; European Journal of Mathematics 9 (2023), Paper 22.
3. Melody Chan, Nathan Ilten, *Fano schemes of determinants and permanents*, Algebra & Number Theory 9 (2015), 629–679.
