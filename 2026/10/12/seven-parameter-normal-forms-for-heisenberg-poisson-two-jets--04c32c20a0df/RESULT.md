# Seven-parameter normal forms for Heisenberg Poisson two-jets

## Finding

Let \(K\) be **any field**, including one of characteristic \(2\) or \(3\), and put
\[
A=K[x,y,z]/(x,y,z)^3,\qquad \mathfrak m=(x,y,z)A.
\]
Consider alternating Poisson brackets on the fixed commutative algebra \(A\) whose induced bracket on \(\mathfrak m/\mathfrak m^2\) is the Heisenberg Lie bracket \(\{x,y\}=z\), \(\{x,z\}=\{y,z\}=0\). Here “induced” means taking the images of brackets modulo \(\mathfrak m^2\), and \(x,y,z\) also denote the classes of the three polynomial generators.

The space of all these **labeled** brackets is an affine space of dimension \(15\). The group \(U\) of commutative-algebra automorphisms of \(A\) acting identically on \(\mathfrak m/\mathfrak m^2\) partitions it into affine cosets of dimension \(8\). Every orbit contains **exactly one** representative with brackets
\[
\begin{aligned}
\{x,y\}&=z,\\
\{x,z\}&=a x^2-2gxy+b xz+c y^2+d yz,\\
\{y,z\}&=e x^2-2a xy+f xz+g y^2-b yz,
\end{aligned}
\]
where \((a,b,c,d,e,f,g)\in K^7\) is arbitrary. Brackets on other elements are obtained uniquely by bilinearity, alternation and the Leibniz rule.

For every prime power \(q\), the exact counts are
\[
\#\{\text{labeled brackets}\}=q^{15},\qquad
\#(\text{brackets}/U)=q^7,
\]
and every \(U\)-orbit has \(q^8\) elements. These statements are valid in **every finite characteristic**. In the language of the three-dimensional Heisenberg Lie algebra \(\mathfrak h\), the associated quadratic infinitesimal deformation space is
\[
\dim_K H^2(\mathfrak h,\operatorname{Sym}^2\mathfrak h)=7,
\]
for the module structure induced by the adjoint action.

## Assumptions and scope

A Poisson bracket means a \(K\)-bilinear **alternating** Lie bracket satisfying \(\{uv,w\}=u\{v,w\}+v\{u,w\}\). Alternating, rather than merely skew-symmetric, is essential in characteristic \(2\). The associative product, the generators, and the Heisenberg first-order Lie bracket are fixed. Automorphism equivalence uses **only** \(U\), the substitutions with identity linear part. This is a classification of framed two-jets, not a classification under every algebra automorphism.

The algebra has dimension \(10\), with basis consisting of \(1\), the three linear monomials, and the six quadratic monomials. No algebraic closedness, restriction on the characteristic, or formal convergence assumption is imposed.

## Proof

**1. Reduction to three quadratic polynomials.** In any Poisson bracket on \(A\), the constant term of every generator bracket vanishes. Indeed, for distinct generator indices \(i\ne j\) the equality \(\{x_i^2x_j,x_k\}=0\) in \(A\), considered modulo \(\mathfrak m^3\), has coefficient equal to the constant term of \(\{x_j,x_k\}\) at the quadratic monomial \(x_i^2\); its other term is a multiple of \(x_ix_j\). Thus all constant terms vanish, regardless of characteristic. With the fixed first-order law there are unique \(P,Q,R\) in
\[
M=\mathfrak m^2=\operatorname{span}_K\{x^2,xy,xz,y^2,yz,z^2\}
\]
such that \(\{x,y\}=z+P\), \(\{x,z\}=Q\), \(\{y,z\}=R\). Conversely, every such alternating assignment extends to a biderivation on \(A\): a bracket of a cubic monomial with a generator has degree at least three, hence the ideal of cubic and higher monomials is Poisson-stable. The Jacobiator of a biderivation is a triderivation, so it suffices to check it on the three generators.

**2. Jacobi equations.** The linear part of the bracket induces derivations on \(M\):
\[
D_x=z\frac{\partial}{\partial y},\qquad
D_y=-z\frac{\partial}{\partial x},\qquad D_z=0.
\]
The Jacobiator at \((x,y,z)\) equals \(D_xR-D_yQ\). Every product involving a quadratic correction in this expression has degree at least three and vanishes. Writing the coefficients of \(Q\) and \(R\) in the ordered basis \((x^2,xy,xz,y^2,yz,z^2)\) as \(q_i\) and \(r_i\), the Jacobi identity is exactly
\[
2q_1+r_2=0,\qquad q_2+2r_4=0,\qquad q_3+r_5=0.
\]
These equations are independent in every characteristic (each has a coefficient \(1\) on a distinct variable). Of the \(18\) coefficients in \(P,Q,R\), precisely \(3\) are constrained. Therefore the labeled bracket variety is \(\mathbb A_K^{15}\), not merely a set of that cardinality over small fields.

**3. Coordinate changes and orbit dimension.** Every element of \(U\) is uniquely
\[
\phi(x)=x+H_x,\quad \phi(y)=y+H_y,\quad \phi(z)=z+H_z,
\qquad H_x,H_y,H_z\in M.
\]
The inverse is obtained by subtracting the three \(H\)'s modulo cubic monomials; composition adds the \(H\)'s. Define the transformed bracket by \(\{u,v\}'=\phi^{-1}\{\phi(u),\phi(v)\}\). Its coefficients change by
\[
(P,Q,R)\longmapsto
(P+D_xH_y-D_yH_x-H_z,\quad Q+D_xH_z,\quad R+D_yH_z).
\]
The possible changes of \(P\) fill \(M\), since \(H_z\) is arbitrary. Write \(W=D_xM+D_yM\). Directly from the monomial basis,
\[
W=\operatorname{span}_K\{xz,yz,z^2\}.
\]
Changes with \(P=0\) preserved require \(H_z\in W\), and their effects on \((Q,R)\) form
\[
\{(\lambda z^2,\mu z^2):\lambda,\mu\in K\}.
\]
Indeed \(D_x(yz)=z^2\), \(D_y(xz)=-z^2\), and \(D_x(z^2)=D_y(z^2)=0\). Hence the orbit-translation subspace has dimension \(6+2=8\). Its kernel in the \(18\)-dimensional group \(U\) has dimension \(10\).

**4. Existence and uniqueness of normal form.** First take \(H_z=P\) and \(H_x=H_y=0\), removing \(P\). Then use an element preserving \(P=0\) to remove independently the \(z^2\) coefficients of \(Q\) and \(R\). The three equations from step 2 now force the displayed relations among the other coefficients, leaving precisely the seven free parameters \((a,b,c,d,e,f,g)\). No nonzero residual gauge change modifies any of these seven coefficients, since its only possible action on \(Q,R\) is through their \(z^2\) terms. This proves uniqueness.

**5. Arithmetic and cohomology.** Over \(\mathbf F_q\), an affine \(15\)-space has \(q^{15}\) points. Each orbit is a coset of the same dimension-\(8\) translation subspace, giving \(q^8\) points per orbit and \(q^7\) orbits. Finally, the Jacobi equations are the Chevalley–Eilenberg \(2\)-cocycle conditions for \(\mathfrak h\) acting on \(M=\operatorname{Sym}^2\mathfrak h\); the gauge changes are the \(2\)-coboundaries. Thus the cohomology dimensions are \(15-8=7\), including characteristic \(2\).

## Verification

Run `python3 verify.py` in the directory containing this file and the bundled checker. It uses only the standard library. The checker constructs both the Jacobi and gauge matrices independently using truncated-polynomial biderivation arithmetic, rather than taking the equations from the proof as input. It confirms matrix ranks \(3\) and \(8\) over characteristics \(2,3,5,7,11\), tests random normal forms and gauge translates, exhaustively checks all \(2^{18}\) coefficient assignments in characteristic \(2\), and checks independence of the seven normal-form directions modulo the gauge image. Expected final line: `VERIFY_OK`. This finite computation supplements the characteristic-free algebraic proof; it does not itself prove the claim for arbitrary fields.

## Relationship to prior work

Abdelwahab, Fernández Ouaridi and Martín González, *Degenerations of Poisson algebras* (arXiv:2209.09150v1, first public submission September 19, 2022), introduced a systematic classification method for Poisson brackets on a fixed commutative algebra and classified all complex three-dimensional cases, plus higher-dimensional null-filiform and filiform cases. Our underlying associative algebra is instead the ten-dimensional local algebra with Hilbert function \((1,3,6)\); the claim determines a fixed-Heisenberg first-jet fiber and its gauge quotient, not the classification treated there. The general orbit-method framework is explicitly acknowledged.

Huang, Tang, Wang and Zhang, *Weighted Poisson polynomial rings in dimension three* (arXiv:2309.00714, first posted September 1, 2023), study weighted Poisson structures and cohomology on the untruncated polynomial ring in three variables, primarily in characteristic zero. Their potential-based results have different hypotheses and do not provide the finite cube-zero Heisenberg two-jet orbit count. The general interpretation through Lie algebra cohomology is standard; only its exact evaluation and unique seven-parameter normal form here are claimed.

## Limitations

The \(q^7\) count is **not** the number of unframed Poisson-isomorphism classes: automorphisms acting nontrivially on \(\mathfrak m/\mathfrak m^2\) may identify additional normal forms. No assertion about lifting these two-jets to a full formal Poisson structure, about higher truncation order, or about uniqueness relative to all unpublished literature is made. The cohomology conclusion uses the specific \(\operatorname{Sym}^2\mathfrak h\) adjoint module. Residual originality risk remains for equivalent calculations under deformation- or jet-theoretic terminology.

## References

1. H. Abdelwahab, A. Fernández Ouaridi, and C. Martín González, *Degenerations of Poisson algebras*, arXiv:2209.09150v1 (2022), https://arxiv.org/abs/2209.09150 .
2. H. Huang, X. Tang, X. Wang, and J. J. Zhang, *Weighted Poisson polynomial rings in dimension three*, arXiv:2309.00714v1 (2023), https://arxiv.org/abs/2309.00714 .
3. H. Abdelwahab, E. Barreiro, A. J. Calderón, and A. Fernández Ouaridi, *The algebraic classification and degenerations of nilpotent Poisson algebras*, J. Algebra 615 (2023), 243–277, https://doi.org/10.1016/j.jalgebra.2022.10.018 .
