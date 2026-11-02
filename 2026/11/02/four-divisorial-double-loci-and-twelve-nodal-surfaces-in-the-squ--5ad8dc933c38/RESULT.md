# Four divisorial double loci and twelve nodal surfaces in the square logarithmic discriminant

## Finding

Let \(\mathbb P^3_{[x:y:z:w]}\times\mathbb P^2_{[s:u:v]}\) be defined over \(\mathbb C\). Write \(A=xw\), \(B=yz\), and \(D=A-B\). Consider the square-support logarithmic discriminant hypersurface \(X=V(F)\), where

\[
F=B^2s^2+D\bigl(D(u^2+v^2)-2Bs(u+v)-2(A+B)uv\bigr).
\]

This is precisely Equation (5) in Goertz--Sturmfels--Telen (2026), with \([x:y:z:w]\) replacing their four coefficient variables and \([s:u:v]\) their three exponents. Their Theorem 1.1 establishes that \(X\) is irreducible. Its dimension is \(4\).

**The reduced singular locus has exactly sixteen irreducible components**, four of dimension \(3\) and twelve of dimension \(2\). The four threefolds are

\[
T_{\alpha\beta}=\{\alpha=\beta=0\}\times\mathbb P^2,
\qquad\alpha\in\{x,w\},\quad\beta\in\{y,z\}.
\]

Each is \(\mathbb P^1\times\mathbb P^2\). The twelve surfaces fall into four groups:

1. Four coordinate-plane surfaces \(\{c=0\}\times\{[-1:0:1]\}\) and \(\{c=0\}\times\{[-1:1:0]\}\), for \(c=x,w\).
2. Four coordinate-plane surfaces \(\{c=0\}\times\{[1:0:0]\}\) and \(\{c=0\}\times\{[-1:1:1]\}\), for \(c=y,z\).
3. The two product surfaces \(\{x=w=0\}\times\{s+u+v=0\}\) and \(\{y=z=0\}\times\{u=v\}\).
4. The two quadric surfaces \(\{xw=yz\}\times\{[0:1:0]\}\) and \(\{xw=yz\}\times\{[0:0:1]\}\).

At a general point of a threefold component the analytic normal slice is two smooth branches crossing, \(ab=0\). At a general point of any of the twelve surface components **away from the other singular components**, the analytic normal slice is a three-variable nondegenerate quadratic cone, equivalently \(a^2+bc=0\) (transverse type \(A_1\)). Since the singular locus contains divisors of the irreducible hypersurface, \(X\) fails Serre's \(R_1\) condition and is nonnormal.

## Assumptions and scope

All schemes and analytic germs are over \(\mathbb C\). A singular locus means the closed support of the Jacobian singular subscheme with its **reduced** induced structure; the theorem does not calculate the nilpotents or embedded components of the Jacobian ideal. The word general means on a nonempty Zariski-open subset of the named irreducible component, excluding intersections with all other components. Singularities are those of the full projective product \(\mathbb P^3\times\mathbb P^2\), not just the locus of nonzero coefficients or the likelihood region \(s\ne0\).

## Proof

**Step 1: An exact quadratic-form reduction.** Rewriting the defining equation gives

\[
F=A^2(u-v)^2-2AB\bigl(s(u+v)+u^2+v^2\bigr)+B^2(s+u+v)^2.
\]

The symmetric matrix of the quadratic form in \((s,u,v)\) is

\[
Q=\begin{pmatrix}
B^2&-BD&-BD\\
-BD&D^2&-(A+B)D\\
-BD&-(A+B)D&D^2
\end{pmatrix},\qquad
\det Q=-4A^2B^2D^2.
\]

Where \(ABD\ne0\), the conic \(F=0\) in the exponent projective plane is smooth, so no point of \(X\) can be singular there. Therefore all singularities satisfy \(A=0\), \(B=0\), or \(D=0\).

**Step 2: The three boundary cases.** When \(A=0\) and \(B\ne0\), the equation reduces to \(B^2(s+u+v)^2=0\). The exponent partial derivatives vanish precisely on \(s+u+v=0\). At such a point \(F_B=0\) and \(F_A=4Buv\). By the chain rule, the coefficient differential is therefore \(4Buv\,\mathrm d(xw)\). As \(\mathrm d(xw)=w\,\mathrm dx+x\,\mathrm dw\), singularity occurs exactly when \(uv=0\) or \(x=w=0\). The two possibilities \(u=0\) and \(v=0\) give the first four coordinate-plane surfaces; \(x=w=0\) gives the first product surface.

Similarly, when \(B=0\), \(A\ne0\), the exponent derivatives vanish exactly on \(u=v\); there \(F_A=0\) and \(F_B=-4Au(s+u)\). Since \(\mathrm d(yz)=z\,\mathrm dy+y\,\mathrm dz\), the singularity condition is \(u(s+u)=0\) or \(y=z=0\). This gives four further coordinate-plane surfaces and the second product surface.

When \(D=0\) and \(A=B\ne0\), the equation is \(B^2s^2\), so singular points have \(s=0\). On that locus \(F_A=-4Buv\) and \(F_B=4Buv\). The quadric \(xw=yz\) is smooth in \(\mathbb P^3\); hence \(\mathrm dD\ne0\), and singularity occurs precisely when \(uv=0\). These are the two quadric surfaces.

Finally, if \(A=B=0\), the expression for \(F\) is homogeneous quadratic in \(A,B\). Thus \(F\) and **every** first partial derivative vanish for all \([s:u:v]\). The locus \(A=B=0\) in coefficient space is the union of the four reduced lines \(\{\alpha=\beta=0\}\), with \(\alpha\in\{x,w\}\) and \(\beta\in\{y,z\}\). Their products with \(\mathbb P^2\) give the four threefolds. These cases cover every singular point by Step 1. Every listed set is an irreducible component because it has a dense open not contained in any of the other listed sets.

**Step 3: Generic normal slices.** At a general point on each coefficient line \(\{\alpha=\beta=0\}\), the functions \(A=xw\) and \(B=yz\) are local transverse coordinates. As a quadratic form in \((A,B)\), the discriminant of \(F\) is

\[
\operatorname{disc}_{A,B}(F)=16uv(s+u)(s+v).
\]

This is nonzero on a dense open of the exponent plane. Over \(\mathbb C\) the transverse quadratic form then factors into two distinct linear factors, establishing the crossing \(ab=0\).

At a general point of a coordinate-plane surface the three transverse coordinates can be chosen as the vanishing coefficient coordinate, the varying exponent coordinate, and the appropriate doubled-line parameter; the quadratic form has shape \(c_1t^2+c_2ab\), with \(c_1c_2\ne0\). At the first product surface, the transverse quadratic part is \(B^2t^2+4Buv\,xw\) with \(t=s+u+v\), nondegenerate for \(Buv\ne0\). At the second product surface, it is \(A^2(u-v)^2-4Au(s+u)yz\), nondegenerate for \(Au(s+u)\ne0\). At either quadric surface, write \(\delta=D\), and use a chart in which the nonvanishing exponent among \(u,v\) equals \(1\). The transverse quadratic part in \((s,\delta,\text{other exponent})\) is \(B^2s^2-2B\delta s+\delta^2-4B\delta\cdot\text{(other exponent)}\), of rank \(3\). All twelve surfaces therefore have ordinary quadratic transverse \(A_1\) type on a dense open. The exhaustive list contains exactly \(4+4+4+2+2=16\) components.

**Step 4: Nonnormality.** The irreducible hypersurface \(X\) is Cohen--Macaulay and thus satisfies \(S_2\). Each \(T_{\alpha\beta}\) has dimension \(3\), hence codimension \(1\) in \(X\). Since it is singular at the generic point, \(X\) violates \(R_1\) and is not normal.

## Verification

The standalone file `verify.py` computes the two defining expressions for \(F\), the determinant of \(Q\), the quadratic discriminant in \(A,B\), and the exact derivative restrictions in each of the three boundary cases. It directly substitutes parametrizations of every proposed singular component into the defining equation and all seven partial derivatives. Five representative transverse Hessians have rank \(3\) for the five kinds of surface components. Running `python verify.py` using SymPy returned `VERIFY_OK`. These finite symbolic checks support the exact algebraic identities; the proof above, not sampled points or a nonexhaustive computer search, establishes completeness.

## Relationship to prior work

Goertz, Sturmfels and Telen introduce \(\Lambda_A\) and explicitly give its equation for the square support (Example 1.2), its Hurwitz-form specialization (Example 1.4), and the scaled binary-independence interpretation (Section 9). Their text does **not** state the sixteen-component singular-locus decomposition, the divisorial nonnormality, or the generic transverse types. Merely knowing their polynomial does not specify the complete singular geometry without the boundary/Jacobian analysis here. In particular the perfect-square restriction over the coefficient quadric \(xw=yz\) does not by itself identify the full singular locus.

Kayser--Kretschmer--Telen analyze discriminants of hyperplane arrangements and Hurwitz forms in a different, fixed-arrangement setting. Clarke--Hoşten--Kushnerchuk--Oldekop classify variations of ML degree under scalings, not the Jacobian singularities of the bidegree-\((4,2)\) discriminant. Barnhill--Cobb--Faust treat likelihood ideals of toric statistical models, not this discriminant's singular-locus decomposition. A classical hyperdeterminant provides an alternative description of the **ambient Hurwitz form**; the required singularity analysis after a nontrivial specialization is not implied by a generic hyperdeterminant singular-locus result alone.

## Limitations

The result describes the reduced singular support and *generic* transverse analytic types. It does not determine Jacobian-scheme multiplicities or the analytic types at intersections of singular components, the normalization morphism or conductor, and it does not extend to higher-dimensional cube supports. Historical literature may contain an implicit equivalent treatment of this special quartic discriminant; the priority search is not an independence or exhaustive-literature certification.

## References

1. M. Goertz, B. Sturmfels, S. Telen, *The Logarithmic A-Discriminant*, arXiv:2610.29204v1 (first publicly posted 2026-10-21), Example 1.2, Example 1.4, Sections 8--9. https://arxiv.org/html/2610.29204v1
2. L. Kayser, A. Kretschmer, S. Telen, *Logarithmic Discriminants of Hyperplane Arrangements*, arXiv:2410.11675 (2024), Sections 1, 6--7. https://arxiv.org/abs/2410.11675
3. O. Clarke, S. Hoşten, N. Kushnerchuk, J. Oldekop, *Matroid Stratification of ML Degrees of Independence Models*, arXiv:2312.10010v2 (2024), Sections 1--2. https://arxiv.org/html/2312.10010v2
4. D. Barnhill, J. Cobb, M. Faust, *Likelihood Correspondence of Toric Statistical Models*, ISSAC 2026, doi:10.1145/3815436.3815479, Sections 2--3. https://doi.org/10.1145/3815436.3815479
