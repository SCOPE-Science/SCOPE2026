# Exactly \(\binom{p+r}{p}\) ordinary nodes on modular power-sum complete intersections

## Finding
Fix a prime \(p\ge5\) and an integer \(1\le r\le p-1\), and put \(n=p+r\). Over \(k=\overline{\mathbb F}_p\), define the projective scheme
\[
X_{p,r}=V\left(\sum_{i=1}^{n}x_i,\;\sum_{i=1}^{n}x_i^2,\;\sum_{i=1}^{n}x_i^3\right)\subset\mathbb P^{n-1}_k.
\]
Then \(X_{p,r}\) is a geometrically integral normal complete intersection of multidegree \((1,2,3)\), degree \(6\), and dimension \(n-4\). Its scheme-theoretic singular locus is reduced, defined over \(\mathbb F_p\), and consists of exactly
\[
\boxed{\binom{p+r}{p}}
\]
ordinary quadratic double points. They are precisely the projective coordinate permutations of \([1:\cdots:1:0:\cdots:0]\) with \(p\) entries equal to \(1\) and \(r\) entries equal to \(0\). At each such point the completed local ring over \(k\) is isomorphic to
\[
k[[z_1,\dots,z_{n-3}]]/(z_1^2+\cdots+z_{n-3}^2).
\]
In particular, when \((p,r)=(5,1)\), this is a degree-six complete-intersection surface with exactly six \(A_1\) singularities; its minimal resolution is a K3 surface.

## Assumptions and scope
All statements are scheme-theoretic over the algebraic closure of the prime field, with the displayed defining equations interpreted over \(\mathbb F_p\). The range \(p\ge5\) ensures the derivatives of the first three power sums and the quadratic-form diagonalization have the stated properties. The bound \(1\le r\le p-1\) ensures \(p<n<2p\), so the congruence of a multiplicity to zero modulo \(p\) determines that multiplicity uniquely. Singular subscheme means the zeroth degeneracy locus of the Jacobian of this codimension-three complete intersection, equivalently the non-smooth locus with its Jacobian scheme structure.

## Proof
**Regular sequence and dimension.** Write \(s_j=\sum_i x_i^j\) for \(j=1,2,3\), and \(e_j\) for the first three elementary symmetric functions. Newton's identities, in characteristic at least five, are
\[
s_1=e_1,\qquad s_2=e_1s_1-2e_2,\qquad s_3=e_1s_2-e_2s_1+3e_3.
\]
Thus \((s_1,s_2,s_3)=(e_1,e_2,e_3)\). Over any field the ring \(k[x_1,\dots,x_n]\) is free over the symmetric-polynomial ring \(k[e_1,\dots,e_n]\) (the integral monomial basis for the symmetric-group coinvariant construction). Therefore \(e_1,e_2,e_3\) form a regular sequence in the larger polynomial ring. The homogeneous projective scheme is a complete intersection of codimension three, dimension \(n-4\), and degree \(1\cdot2\cdot3=6\).

**Full support of the singular locus.** The three columns of the derivative matrix at coordinates \(x_i\) are \((1,2x_i,3x_i^2)^{\mathsf T}\). Because the characteristic is not \(2\) or \(3\), every three columns belonging to three distinct coordinate values have nonzero Vandermonde determinant. Conversely, if the coordinates have at most two different values then the derivative matrix has rank at most two. Accordingly, singular points of the complete intersection have at most two coordinate values.

Suppose the two values are \(u\ne v\), with positive multiplicities \(a,b\) satisfying \(a+b=n\). The equations \(s_1=s_2=0\) say \(au+bv=au^2+bv^2=0\). The coefficient matrix for \((a,b)\) has determinant \(uv(v-u)\). If \(uv\ne0\), invertibility forces \(a\equiv b\equiv0\pmod p\), which is impossible because \(0<a,b<n<2p\). If \(u=0\) and \(v\ne0\), the first equation forces \(b\equiv0\pmod p\), hence \(b=p\); the other value distribution is symmetric. If all coordinates equal a single nonzero \(u\), the first equation would force \(n\equiv0\pmod p\), contradicting \(n=p+r\) with \(0<r<p\). The all-zero vector is not projective. Thus the singular support consists precisely of the indicated \(\binom np\) points. Conversely those points satisfy all three equations because \(p=0\) in \(k\), and have exactly two coordinate values, hence Jacobian rank two. All are distinct and \(\mathbb F_p\)-rational.

**Local type and reduced singular scheme.** Fix such a point and use the affine chart where one of its nonzero coordinates is \(1\). Write the remaining \(p-1\) originally nonzero coordinates as \(1+u_1,\dots,1+u_{p-1}\), and the originally zero coordinates as \(v_1,\dots,v_r\). The linear terms of the first and second equations are, respectively, \(U+V\) and \(2U\), where \(U=\sum u_i\) and \(V=\sum v_j\). Their differentials are linearly independent. Eliminate one \(u\) and one \(v\) by the formal implicit-function theorem. The remaining equation may be chosen as \(g=s_3-\tfrac32s_2\); its quadratic part on the tangent space \(U=V=0\) is
\[
Q=\tfrac32\left(\sum_{i=1}^{p-1}u_i^2-\sum_{j=1}^{r}v_j^2\right).
\]
After eliminating \(u_{p-1}=-\sum_{i=1}^{p-2}u_i\) and \(v_r=-\sum_{j=1}^{r-1}v_j\) to first order, the Hessian blocks are scalar multiples of \(I_{p-2}+J_{p-2}\) and \(-I_{r-1}-J_{r-1}\). Here \(J_m\) is the all-ones matrix, and an empty block is allowed. The elementary identity \(\det(I_m+J_m)=m+1\) gives determinants \(p-1=-1\ne0\pmod p\) and \(r\ne0\pmod p\). Thus \(Q\) is nondegenerate in \(n-3\) variables. The formal Morse lemma in characteristic different from two gives the stated completed ordinary-double-point equation. The derivatives of this nondegenerate quadratic hypersurface generate its maximal ideal in the completed local ring; hence the local Jacobian singular subscheme is a reduced point. Since all singular points have this form, the entire singular subscheme is reduced.

**Normality and integrality.** The complete intersection is Cohen–Macaulay and its singular locus is finite, whereas \(\dim X_{p,r}=n-4\ge2\). Thus it satisfies Serre's \(S_2\) and \(R_1\) conditions and is geometrically normal. A positive-dimensional projective complete intersection is connected, and a connected normal scheme cannot have two distinct irreducible components because normal local rings are domains. Therefore the scheme is geometrically integral. For \((p,r)=(5,1)\), adjunction gives trivial dualizing sheaf and the complete intersection has vanishing first structure-sheaf cohomology; resolving its six rational double points is crepant and yields a K3 surface.

## Verification
A standalone pure-Python script `verify.py` checks the modular rank obstruction on all two-value patterns over the tested prime fields, the nondegenerate tangent-quadratic determinants in nine parameter pairs, and the complete \(\mathbb F_5\)-rational projective singular census for \((p,r)=(5,1)\). The command `python3 verify.py` returned `VERIFY_OK`, including exactly six rational singular points in the smallest case. These finite checks are corroboration only. The arbitrary-prime classification, the absence of geometric singularities outside \(\mathbb F_p\), scheme reducedness, and integrality follow from the displayed arguments, not numerical extrapolation.

## Relationship to prior work
Giménez, Gottig, Palacios, Pérez and Privitelli establish regular-sequence and radicality properties for broad power-sum systems and provide geometric singular-locus dimension estimates in arXiv:2610.32056v1 (Theorems 3.4, 3.5, 3.7). Their normality theorem for three consecutive exponents demands \(p>n-1\), which does not hold here because \(n=p+r\). The present result determines the *exact singular scheme and analytic local type* in this excluded boundary range; regularity of the sequence itself is not the new conclusion. Conca, Singh and Soundararajan investigate power-sum ideals, primarily with characteristic-zero normality analysis, but the compared statements do not give this positive-characteristic node count. Melánová, Sturmfels and Winter investigate complex power-sum recovery and projective zero fibres; the inspected complex results do not determine the modular node count. Separate characteristic-five analyses of the five-coordinate Bring model use \(n=p\) rather than this theorem's \(n>p\), and the specific six-line reducible geometry in that range does not imply the present nodal classification.

## Limitations
The theorem applies only to the three consecutive power sums of degrees one, two and three, for primes at least five and \(p<n<2p\), over the algebraic closure of the prime field. It gives the ordinary singularity type and reduced Jacobian support but does not compute the zeta function, point counts of the full variety, or any invariant of its resolutions beyond the stated K3 consequence. There is a residual priority risk of an equivalent singular-locus theorem described under symmetric-invariant terminology or in unpublished literature. No independent mathematical validation is asserted.

## References
1. N. Giménez, J. F. Gottig, M. Palacios, M. Pérez, M. Privitelli, *Power Sum Varieties over Finite Fields*, arXiv:2610.32056v1 (23 October 2026), https://arxiv.org/html/2610.32056v1, especially Theorems 3.4, 3.5 and 3.7.
2. A. Conca, A. K. Singh, K. Soundararajan, *Ideals generated by power sums*, arXiv:2409.18906v1 (2024), https://arxiv.org/html/2409.18906v1, especially Remark 1.2 and Section 2.
3. H. Melánová, B. Sturmfels, R. Winter, *Recovery from Power Sums*, arXiv:2106.13981v1 (2021), https://arxiv.org/html/2106.13981v1 (Sections 1–4 consulted).
