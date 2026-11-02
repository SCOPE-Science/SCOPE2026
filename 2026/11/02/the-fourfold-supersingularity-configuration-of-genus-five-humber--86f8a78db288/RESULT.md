# The fourfold supersingularity configuration of genus-five Humbert curves in characteristic \(23\)

## Finding
Over \(k=\overline{\mathbb F}_{23}\), let \(C_{u,v}\subset\mathbb P^4_k\) be the smooth genus-five complete intersection
\[
 X_1^2+X_2^2+X_3^2=0,\quad
 uX_1^2+X_2^2+X_4^2=0,\quad
 vX_1^2+X_2^2+X_5^2=0,
\]
where \(uv(u-1)(v-1)(u-v)\ne0\). It is the maximal tame elementary abelian two-cover of \(\mathbb P^1\) branched at the ordered configuration \((\infty,0,1,u,v)\).

The five elliptic quotients of \(C_{u,v}\) cannot be supersingular simultaneously; precisely \(0,1,2,3\), or \(4\) may be supersingular. Their five supersingularity divisors have only transverse intersections of distinct smooth branches. Over \(k\), the arrangement has exactly \(560\) double points, \(60\) triple points, and \(60\) quadruple points, and no points on five divisors. Every triple and quadruple point is rational over \(\mathbb F_{23}\); the double points comprise \(180\) rational points and \(380\) further points defined over \(\mathbb F_{23^2}\) (in \(190\) conjugate pairs). All these counts refer to the ordered marked parameter space, not to isomorphism classes.

In particular, exactly \(60\) marked parameters give Jacobian \(23\)-rank \(1\), and they form one orbit under permutations of the five branch labels. Thus there is a single geometric branch-configuration class with \(23\)-rank \(1\). No member has rank \(0\). If exactly \(s\) elliptic quotients are supersingular, the Jacobian has \(23\)-rank \(5-s\), \(a\)-number \(s\), and Newton slopes \(0^{5-s},(1/2)^{2s},1^{5-s}\).

For every integer \(m\ge1\), put \(q=23^m\), and let \(N_s(q)\) count \(\mathbb F_q\)-rational ordered marked parameters with exactly \(s\) supersingular elliptic quotients. The complete count is
\[
\begin{array}{c|ccccc}
 &N_0(q)&N_1(q)&N_2(q)&N_3(q)&N_4(q)\\\hline
m\text{ odd}&q^2-50q+621&45q-915&180&60&60\\
m\text{ even}&q^2-60q+1031&55q-1705&560&60&60.
\end{array}
\]
In particular every one of the \((23-2)(23-3)=420\) marked smooth curves over \(\mathbb F_{23}\) is nonordinary, whereas over \(\mathbb F_{23^2}\) there are \(249132\) ordinary marked parameters.

## Assumptions and scope
All varieties are over the indicated fields of characteristic \(23\), which is prime to the group order \(16\). The parameters \((u,v)\) are ordered and the five branch points are pairwise distinct. The names of the five elliptic quotients depend on this ordering; the number \(s\) does not. The geometric counts are counts of distinct closed geometric points on the open two-dimensional marked moduli chart; their images in the unmarked moduli space are not counted with weights.

## Proof
**The five elliptic factors.** Let \(G=(\mathbb Z/2\mathbb Z)^4\) be the deck group. The Riemann--Hurwitz formula gives \(2g(C)-2=16(-2)+5(8)=8\), hence \(g(C)=5\). The character-idempotent decomposition of its Jacobian's prime-to-two representation, or equivalently the quotient correspondences from the five degree-eight maps, gives a prime-to-\(23\) isogeny from \(\operatorname{Jac}(C)\) to the product of five elliptic curves. A direct description of the five factors is provided by the four-element subsets of the five branch points, and their Legendre parameters can be chosen as
\[
\lambda_1=u,\quad \lambda_2=v,\quad \lambda_3=\frac vu,\quad
\lambda_4=\frac{v-1}{u-1},\quad
\lambda_5=\frac{u(v-1)}{v(u-1)}.
\]
The last coordinate differs from the choice \(v(1-u)/(v-u)\) in Carvacho--Hidalgo--Quispe by the standard Legendre transformation \(\lambda\mapsto1/(1-\lambda)\). To see directly that its kernel has \(2\)-power order, compose the sum of pullback maps from the five elliptic quotients with the five norm maps: character orthogonality makes cross terms vanish, while each diagonal term is multiplication by \(8\), the degree of the corresponding quotient map. Thus both kernel and cokernel are killed by a power of \(2\). The resulting isogeny identifies the \(23\)-divisible groups and therefore preserves \(23\)-rank, \(a\)-number, and Newton slopes. A supersingular elliptic factor contributes \(23\)-rank \(0\), \(a\)-number \(1\) and two slopes \(1/2\); an ordinary factor contributes rank \(1\), \(a\)-number \(0\), and slopes \(0,1\).

**Exact Hasse roots.** For \(E_\lambda:y^2=x(x-1)(x-\lambda)\), the Hasse invariant vanishes precisely when
\[
H(\lambda)=\sum_{j=0}^{11}\binom{11}{j}^{\!2}\lambda^j=0\pmod {23}.
\]
Indeed this is, up to a nonzero scalar, the coefficient of \(x^{22}\) in \([x(x-1)(x-\lambda)]^{11}\). Direct multiplication in \(\mathbb F_{23}[T]\) gives the exact factorization
\[
H(T)=(T^2-T+1)\prod_{r\in R_1}(T-r),\qquad
R_1=\{2,3,8,11,12,13,16,21,22\}.
\]
The quadratic is separable irreducible over \(\mathbb F_{23}\) (its discriminant is \(-3\), a nonsquare). All \(11\) roots are simple and lie in \(\mathbb F_{23^2}\); exactly \(9\) are rational over \(\mathbb F_{23^m}\) for odd \(m\), and all \(11\) are rational for even \(m\).

**Exhaustive incidence calculation.** Let \(R\) denote the complete set of \(11\) roots in \(\mathbb F_{23^2}\). For ordered distinct \(u,v\in R\), evaluate \(H\) at each of the five displayed Legendre parameters. The exact field-arithmetic certificate `verify_humbert23.py` enumerates all \(110\) such pairs. It finds exactly \(56\) with \(s=2\), \(18\) with \(s=3\), and \(36\) with \(s=4\), with no other values. Restricting both roots to the nine rational roots gives, respectively, \(18\), \(18\), and \(36\) ordered pairs. All operations take place in \(\mathbb F_{23}[t]/(t^2-5)\); the script checks the Hasse factorization, all roots, and the complete tables without numerical approximation.

Any point on at least two supersingularity divisors can be relabeled so that the two omitted branch points are those corresponding to \(H(u)=H(v)=0\). Hence this root-pair enumeration is exhaustive **over the algebraic closure**, not just for the particular two divisors and not merely over the two small finite fields. The symmetric group \(S_5\) acts transitively on the \(\binom52=10\) pairs of distinct divisors. Therefore if \(A_s(q)\) counts ordered root pairs over \(\mathbb F_q\) with \(s\) supersingular quotients, then
\[
\binom{s}{2}N_s(q)=10A_s(q)\qquad(s\ge2).
\]
This gives \(N_4(q)=60\), \(N_3(q)=60\), and \(N_2(q)=180\) or \(560\), according to parity. For each of the five supersingularity divisors there are exactly \(r(q)(q-3)\) rational points, where \(r(q)\in\{9,11\}\) is the rational Hasse-root count. Summing memberships yields
\[
N_1(q)=5r(q)(q-3)-\sum_{s=2}^4sN_s(q).
\]
Subtracting all strata from the number \((q-2)(q-3)\) of marked smooth pairs gives \(N_0(q)\) and the stated formulas. Because all root pairs are defined over \(\mathbb F_{23^2}\), there can be no further higher-multiplicity points over later extensions.

**Local intersection types and unique rank-one class.** Each individual divisor component is a fiber of a forgetful map \(M_{0,5}\to M_{0,4}\) over a simple Hasse root and is smooth. After relabeling the branch points, the two forgetful maps associated with any two distinct omitted points give the local coordinates \((u,v)\); accordingly, the two divisor branches meet transversely. The certificate also checks pairwise distinct tangent directions directly at every rational triple and quadruple parameter. Thus every multiple point is an ordinary transverse multi-branch point. Finally, relabeling the five branch points of the representative \((u,v)=(6,12)\), followed each time by the unique Möbius normalization taking its first three labeled points to \(\infty,0,1\), produces exactly the \(60\) points with \(s=4\). This proves transitivity and the single geometric branch-configuration class.

## Verification
Run `python3 verify_humbert23.py` from the directory containing the standalone verifier. It requires only Python's standard library. The supplied `verification_output.txt` is its successful actual output ending in `VERIFY_OK`. The program checks the complete degree-eleven Hasse factorization, all \(11\) roots in the quadratic field, both \(110\)- and \(72\)-pair incidence tables, all \(420\) smooth rational marked pairs over \(\mathbb F_{23}\), all \(277202\) smooth marked pairs over \(\mathbb F_{23^2}\), the high-multiplicity tangent tests, and the \(60\)-point branch-label orbit. Its finite checks are accompanied above by a mathematical reduction proving completeness and the all-extension formulas; later finite extensions were not separately enumerated.

## Relationship to prior work
Carvacho--Hidalgo--Quispe establish the genus-five generalized Fermat model and the five elliptic quotient decomposition; Auer--Top study supersingular Legendre parameters. Neither quoted result states the characteristic-\(23\) combined five-divisor intersection arrangement or the \(60\)-point single branch-equivalence class. The traditional Hasse polynomial is an input, not a new contribution. The specific arrangement counts and the resulting complete marked \(23\)-rank distribution are the contribution assessed here. Characteristic-specific rank stratifications at other small primes are different specializations and do not imply the characteristic-\(23\) fourfold incidence data.

## Limitations
This concerns marked parameter pairs; the count of distinct isomorphism classes in other strata, arithmetic twists, automorphism group schemes, and absolute classification across primes are not asserted. The character-isogeny argument uses only odd-characteristic algebraic correspondences, not an unqualified extension of complex-analytic proofs. The theorem does not claim a complete classification of the corresponding Humbert curves in every prime characteristic.

## References
- M. Carvacho, R. A. Hidalgo, S. Quispe, *Isogenous decomposition of the Jacobian of generalized Fermat curves*, arXiv:1507.02903v1, 10 July 2015, especially Section 5.1 and Theorem 5.1. https://arxiv.org/abs/1507.02903
- R. Auer and J. Top, *Legendre Elliptic Curves over Finite Fields*, Journal of Number Theory 95 (2002), 303--312. https://research.rug.nl/en/publications/legendre-elliptic-curves-over-finite-fields/
- Classical Hasse invariant of the Legendre elliptic pencil, here computed directly as the coefficient of \(x^{22}\) in \([x(x-1)(x-\lambda)]^{11}\).
