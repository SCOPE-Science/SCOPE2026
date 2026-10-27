# The degree-four branch-moduli map of binary-quartic polars

## Finding
For a squarefree binary quartic \(f\) over an algebraically closed field \(k\) of characteristic zero, consider its degree-three polar morphism \(\nabla f:\mathbb P^1\longrightarrow\mathbb P^1\). Its branch quartic \(B_f\) is, up to nonzero scalar and the usual linear target-coordinate change, the discriminant of the binary-cubic pencil \(u f_X+v f_Y\). Write \(j(f)\) for the absolute invariant of the four roots (the elliptic double cover). Then whenever \(j(f)\ne1728\), the branch quartic is squarefree and
\[
\boxed{j(B_f)=\Phi(j(f)),\qquad \Phi(j)=\frac{j(j+13824)^3}{64(j-1728)^3}.}
\]
When \(j(f)=1728\), the branch quartic is instead the square of a squarefree quadratic, and hence has no absolute \(j\)-invariant. The rational map \(\Phi:\mathbb P^1\dashrightarrow\mathbb P^1\), extended to a morphism of degree four, has the following complete ramification portrait:
\[
\Phi^{-1}(0):(3,1),\qquad \Phi^{-1}(1728):(2,2),\qquad\Phi^{-1}(\infty):(3,1).
\]
It is a three-branch-value cover with geometric monodromy \(A_4\). Substituting \(t=(j-1728)/64\) yields
\[\Phi(j)=\frac{(t+27)(t+243)^3}{t^3},\]
identical to the familiar degree-four modular covering formula for \(X_0(3)\to X(1)\). The identity concerns rational covers of the \(j\)-line, not a canonical association of a cyclic three-isogeny to each original binary quartic.

## Assumptions and scope
Work throughout over an algebraically closed field of characteristic zero. A binary quartic \(f=A X^4+B X^3Y+C X^2Y^2+D XY^3+E Y^4\) is **squarefree** when it has four distinct zeros in \(\mathbb P^1\). Define
\[I(f)=12AE-3BD+C^2,\qquad J(f)=72ACE+9BCD-27AD^2-27EB^2-2C^3.\]
Set \(\Delta_0(f)=4I(f)^3-J(f)^2\), so \(\Delta_0(f)\ne0\) is equivalent to squarefreeness, and define
\[j(f)=1728\frac{4I(f)^3}{\Delta_0(f)}.\]
For the degree-three map \([X:Y]\mapsto[f_X:f_Y]\), the binary quartic \(B_f(u,v)\) is the cubic discriminant \(\operatorname{Disc}_{X,Y}(u f_X+v f_Y)\); exchanging target coordinates or multiplying by a scalar does not change \(j(B_f)\). The critical values are the points of \(\{B_f=0\}\), with ramification accounted for by their multiplicity. Statements about the fiber \(j(f)=\infty\) only concern the algebraic extension of \(\Phi\) to compactified moduli, not an asserted polar map for a singular quartic.

## Proof
**Step 1: The polar morphism is finite of degree three.** Since the binary quartic is squarefree, its two partial derivatives have no common zero in \(\mathbb P^1\): by Euler's identity a common zero would be a multiple zero of \(f\). Thus the polar system is base-point-free and defines a degree-three map. A target value \([u:v]\) has nonreduced preimage precisely when the cubic \(u f_X+v f_Y\) has a repeated root. Its discriminant therefore cuts out the branch divisor, with its natural multiplicities.

**Step 2: Reduce to the one-parameter four-point normal form.** Every ordered set of four distinct points of \(\mathbb P^1\), up to projective change of source variables, may be written in the family
\[f_a(X,Y)=X(X+2Y)(X+3Y)(X+aY),\qquad a\notin\{0,2,3\}.\]
(The four roots are \(0,-2,-3,-a\).) Under a source-variable change, the gradient transforms through the contragredient linear map on the target. Therefore both the source \(j\)-invariant and the branch \(j\)-invariant are unchanged. A polynomial identity for all permitted \(a\) establishes the universal statement.

**Step 3: Compute quartic invariants on both sides.** Write \(P=I(f_a)\), \(Q=J(f_a)\). Direct expansion gives
\[P=7a^2-30a+36,\qquad Q=2(a-6)(2a-3)(5a-12),\]
\[4P^3-Q^2=972a^2(a-2)^2(a-3)^2.\]
In the chart \(Y=1\), write \(g_a(x)=f_{a,X}(x,1)\), \(q_a(x)=f_{a,Y}(x,1)\). Explicitly,
\[g_a(x)=4x^3+(3a+15)x^2+(10a+12)x+6a,\]
\[q_a(x)=(a+5)x^3+(10a+12)x^2+18ax.\]
For convenience normalize the branch quartic as \(H_a(t)=\operatorname{Disc}_x(g_a(x)-tq_a(x))/4\). This scalar normalization does not affect its \(j\)-invariant. Expanding the cubic discriminant and applying the quartic formulas yields the exact identities
\[
I(H_a)=144P^4-32PQ^2,\qquad
J(H_a)=3456P^6-1152P^3Q^2+64Q^4,
\]
\[4I(H_a)^3-J(H_a)^2=4096Q^6(4P^3-Q^2).\]
These are polynomial identities in \(\mathbb Z[a]\), verified by the supplied symbolic checker. Since \(4P^3-Q^2\ne0\) on the squarefree locus, \(H_a\) is squarefree exactly when \(Q\ne0\). For quartics of nonzero discriminant, \(Q=0\) is equivalent to \(j(f_a)=1728\).

**Step 4: Eliminate the quartic parameter.** Apply the absolute-invariant formula to the identities above. With \(j=1728\cdot4P^3/(4P^3-Q^2)\), rational simplification gives
\[j(H_a)=\frac{j(j+13824)^3}{64(j-1728)^3}.\]
At \(Q=0\), the special square form of the branch divisor is seen without a limiting argument: all smooth binary quartics of \(j=1728\) are equivalent to \(X^4+Y^4\); its polar map is equivalent to \(x\mapsto x^3\), whose two branch points each have multiplicity two. The associated branch binary quartic is a nonzero scalar multiple of \(u^2v^2\).

**Step 5: Exact ramification and modular form.** The numerator and denominator of \(\Phi\) are coprime. Thus \(\deg\Phi=4\). Its fibers above the three claimed values follow from the factorizations
\[
\Phi(j)=\frac{j(j+13824)^3}{64(j-1728)^3},\qquad
\Phi(j)-1728=\frac{(j^2-34560j-23887872)^2}{64(j-1728)^3}.
\]
The quadratic in the second expression has distinct roots different from \(0,-13824,1728\), giving ramification partitions \((3,1),(2,2),(3,1)\). The total ramification defect is \(2+2+2=6=2\cdot4-2\); by Riemann–Hurwitz there are no other branch values. The three branch permutations have cycle types \((3),(2,2),(3)\), lie in \(A_4\), and generate a transitive subgroup containing a three-cycle and a double transposition; this subgroup is \(A_4\). Finally, substitution \(t=(j-1728)/64\) gives \((t+27)(t+243)^3/t^3\), the classical modular formula for the degree-four covering of \(j\)-lines associated to \(\Gamma_0(3)\). No canonical elliptic three-isogeny attached to \(f\) follows from this equality of covers.

## Verification
Run `python verify.py` in a Python environment with SymPy installed. It regenerates both cubics from the universal quartic, recomputes the discriminant and the four quartic-invariant identities symbolically, checks \(j(B_f)=\Phi(j(f))\), the factorization at \(1728\), the derivative, and the modular-form substitution. Expected output: `VERIFY_OK: quartic invariants, branch invariants, discriminants, degree-four Belyi map and modular identity`. The exact algebraic identities are proof steps, not numerical or finite-field extrapolations; the reduction to a normal form and the separability/ramification arguments are proved above rather than left to software.

## Relationship to prior work
Sanyal–Sturmfels–Vinzant (2011) identify the entropic discriminant as the branch locus of the polar map of a line arrangement. Their Example 3 supplies a coordinate branch quartic for a four-line family and notes a square at a distinguished harmonic configuration. This result uses that established setting, but instead computes the **absolute source-to-branch moduli correspondence**, its complete Belyi ramification, and its identity with a degree-four modular cover; these statements are not asserted in the inspected text. Bhargava–Shankar provide the classical invariant normalization. The modular formula \((t+27)(t+243)^3/t^3\) and the \(X_0(3)\) cover are classical and are not independently claimed as new; the proposed new fact is their exact occurrence as the branch-moduli correspondence of the binary-quartic polar construction.

## Limitations
This is a self-review, not an independent audit. The formula is only a regular moduli correspondence on the squarefree quartic locus excluding \(j=1728\); at that harmonic value the target binary quartic is nonreduced. The characteristic-zero hypothesis is essential to the invariant formulas and all given arguments. The equality of rational covers is not a natural assignment of an elliptic three-isogeny. Prior work already determines coordinate branch equations; the invariant-theoretic comparison is an additional consequence of those equations, and an equivalent result under another parametrization could exist. No uniqueness or priority certification is claimed.

## References
1. R. Sanyal, B. Sturmfels, C. Vinzant, *The Entropic Discriminant*, arXiv:1108.2925 (first public version, 2011-08-15), especially Section 2, Example 3 and Example 29.
2. M. Bhargava, A. Shankar, *Binary quartic forms having bounded invariants, and the boundedness of the average rank of elliptic curves*, arXiv:1006.1002 (2010), invariant normalization.
3. G. Ottaviani, *Some Classical Invariants, from Harmonic Quadruples to Triangle Groups*, arXiv:2603.03413 (2026), background on quartic invariants and modular covers; not used to establish the 2011 archive date.
4. Classical level-three modular Hauptmodul formula, \(j=(t+27)(t+243)^3/t^3\); see tables of genus-zero modular-curve parametrizations (e.g. SIGMA, *Supersingular elliptic curves and moonshine*, 2019).
