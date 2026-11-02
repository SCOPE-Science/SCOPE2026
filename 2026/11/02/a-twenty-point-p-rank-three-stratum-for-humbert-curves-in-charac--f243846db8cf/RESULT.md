# A twenty-point \(p\)-rank-three stratum for Humbert curves in characteristic five

## Finding
Let \(k=\overline{\mathbb F}_5\). For each ordered five-point configuration \((\infty,0,1,u,v)\), with \(uv(u-1)(v-1)(u-v)\ne0\), let \(C_{u,v}\) be its genus-five Humbert curve. Set \(H(A,B)=A^2-AB+B^2\), and write \(r(u,v)\) for the number of the following five equalities that hold:
\[
\begin{aligned}
&H(u,1)=0,\qquad H(v,1)=0,\qquad H(u,v)=0,\\
&H(u-1,v-1)=0,\\
&H(u(v-1),v(u-1))=0.
\end{aligned}
\]
Then \(r(u,v)\in\{0,1,2\}\), and the geometric \(p\)-rank and \(a\)-number of the Jacobian satisfy
\[
f(J(C_{u,v}))=5-r(u,v),\qquad a(J(C_{u,v}))=r(u,v).
\]
Every two of the five equianharmonic divisors intersect transversely in exactly two geometric points; no three meet. Thus there are exactly \(20\) ordered normalized parameters of \(p\)-rank \(3\). These points form one orbit under relabeling the five branch points. They are defined over \(\mathbb F_{25}\), and Frobenius has ten cycles of length two.

For \(q=5^m\), the exact numbers \((N_3(q),N_4(q),N_5(q))\) of normalized ordered \((u,v)\in M_{0,5}(\mathbb F_q)\) yielding the indicated geometric \(p\)-ranks are
\[
(N_3,N_4,N_5)=
\begin{cases}
(0,0,(q-2)(q-3)), &m\text{ odd},\\
(20,10q-70,q^2-15q+56), &m\text{ even}.
\end{cases}
\]
In particular, the \(p\)-rank-three parameter scheme has zeta function \(1/(1-T^2)^{10}\) over \(\mathbb F_5\). No smooth Humbert curve of this type in characteristic five has \(p\)-rank below three.

## Assumptions and scope
The curve is the smooth projective model of the complete intersection in \(\mathbb P^4_k\)
\[
\begin{aligned}
X_3^2-X_1^2+X_2^2&=0,\\
X_4^2-X_1^2+uX_2^2&=0,\\
X_5^2-X_1^2+vX_2^2&=0.
\end{aligned}
\]
The quotient map to \(\mathbb P^1\) is \(t=X_1^2/X_2^2\). Its Galois group \(G\cong(\mathbb Z/2\mathbb Z)^4\) changes independently the signs of the four square roots of \(t,t-1,t-u,t-v\), and its inertia branches are \(\infty,0,1,u,v\). Distinctness of the five points and characteristic unequal to two guarantee smoothness. Riemann--Hurwitz for this degree-\(16\) cover gives \(2g-2=16(-2)+5\cdot8=8\), so \(g=5\). Statements about geometric \(p\)-rank concern the algebraic closure, while finite-field strata count ordered *parameters*, not isomorphism classes of curves.

## Proof
**Elliptic quotient decomposition.** A nontrivial character of \(G\) is ramified over an even-cardinality subset of the five inertia points. Exactly five characters have ramification support of cardinality four, each giving a genus-one double-cover quotient \(E_i\) of \(\mathbb P^1\). The remaining nontrivial characters have support of cardinality two and give genus-zero quotients. The five distinct eigenspaces of regular differentials therefore exhaust the five-dimensional \(H^0(C,\Omega^1)\). The product of pullbacks induces an isogeny \(\prod_{i=1}^5E_i\longrightarrow J(C)\); its dual composition is diagonal with diagonal entries powers of two, by averaging over the sign-change group and character orthogonality. Consequently its kernel is of \(2\)-power order (a standard prime-to-\(5\) group-algebra splitting). Its action on the \(5\)-divisible group and on \(J[5]\) is therefore an isomorphism. Accordingly the \(p\)-rank is the number of ordinary elliptic quotients, and the \(a\)-number the number of supersingular quotients.

**Five supersingular divisors.** An elliptic double cover branched at \(\{\infty,0,1,\lambda\}\) has Legendre form \(y^2=x(x-1)(x-\lambda)\). In characteristic five, its Hasse invariant is, up to nonzero scalar, the coefficient of \(x^4\) in \([x(x-1)(x-\lambda)]^2\), namely \(\lambda^2-\lambda+1\). Thus the elliptic quotient is supersingular exactly when \(\lambda^2-\lambda+1=0\). Evaluating cross-ratios for the five four-point subsets of \(\{\infty,0,1,u,v\}\) gives exactly the five displayed conditions; the homogeneous equation \(H(A,B)=0\) is invariant under multiplying \((A,B)\) by a nonzero scalar.

**Intersection geometry.** The polynomial \(z^2-z+1\) has two distinct roots \(\alpha,\beta\in\mathbb F_{25}\setminus\mathbb F_5\) with \(\alpha+\beta=\alpha\beta=1\). Any two four-element subsets of a five-point set share three elements. Normalize those three points to \(\infty,0,1\); the two other points must separately be \(\alpha\) and \(\beta\). Distinctness leaves precisely the two assignments \((\alpha,\beta)\) and \((\beta,\alpha)\), and simple roots make the intersection transverse. For this normalized configuration the three other four-point-subset tests fail: for example \(H(\alpha,\beta)=(\alpha+\beta)^2-3\alpha\beta=1-3=-2\ne0\) in \(\mathbb F_5\), and the other two are obtained by the anharmonic transformations of the shared triple. Hence there is no triple intersection. There are \(\binom52\) unordered pairs of divisors and exactly two intersection points for each, giving \(20\). Each intersection lies in \(M_{0,5}(\mathbb F_{25})\) and is exchanged with its partner by fifth-power Frobenius. Relabeling of the five branch points is transitive on pairs of omitted indices; the permutation of the common triple inducing \(z\mapsto1/z\) interchanges \(\alpha\) and \(\beta\), proving a single \(S_5\)-orbit.

**Finite-field enumeration.** If \(m\) is odd, the roots \(\alpha,\beta\) are not in \(\mathbb F_q\), and no divisor is rationally populated, so all \((q-2)(q-3)\) normalized pairs are ordinary. If \(m\) is even, each of the five divisors has \(2(q-3)\) rational points: for each root of the cross-ratio equation, the other free branch point can be any of the \(q-3\) admissible choices. Summing gives \(10(q-3)\) incidences. Exactly \(20\) parameter points each contribute two incidences, so the number with exactly one supersingular quotient is \(10(q-3)-40=10q-70\). The complement has \((q-2)(q-3)-(20+10q-70)=q^2-15q+56\) points. Together with the quotient decomposition, this proves all claimed strata and point-count formulas.

## Verification
The accompanying standalone Python 3 verifier performs exact arithmetic in \(\mathbb F_{25}=\mathbb F_5[t]/(t^2-2)\). It exhaustively checks all \(506\) normalized ordered parameters, obtains divisor cardinalities \((44,44,44,44,44)\), all ten pairwise intersection cardinalities equal to \(2\), no triple intersections, and the rank profile \((N_3,N_4,N_5)=(20,180,306)\). It checks that the exceptional points have ten Frobenius pairs and that all six normalized \(\mathbb F_5\)-parameters are ordinary. The field-wide and all-extension assertions follow from the proof, not from extrapolating these finite checks.

## Relationship to prior work
The classical Humbert/Edge genus-five curves and the existence of five elliptic quotient factors are established in the literature. Carvacho--Hidalgo--Quispe (2015) give a general Jacobian decomposition of generalized Fermat curves; Auffarth--Lucchini Arteche--Rojas (2019) analyze the Humbert--Edge Jacobian decomposition. Neither decomposition alone supplies the characteristic-five intersection calculus, the exclusion of triple equianharmonic quadruples, or the ordered finite-field p-rank counts. Hidalgo (2017) explicitly analyzes some positive-characteristic cases of generalized Fermat curves, including characteristic three; that does not establish the distinct characteristic-five formula. These quotient decompositions, the genus, and the standard Legendre supersingularity polynomial are not claimed as new. Searches of published literature and mathematical-result records revealed no directly equivalent complete characteristic-five stratification; this is a bounded search, not proof of global priority.

## Limitations
The results are for the ordered, normalized five-point parameter space, not the coarse unlabeled moduli stack or the number of isomorphism classes. The stated \(a\)-number comes from an isogeny with degree prime to five. Nothing is claimed about Newton polygons beyond the ranks given, integral characteristic-zero models, or the global moduli of all genus-five curves. Historical priority could be affected by an older, differently phrased treatment of equianharmonic five-point configurations.

## References
Carvacho, Hidalgo, Quispe, *Isogenous decomposition of the Jacobian of generalized Fermat curves* (first posted 2015-07-10), arXiv:1507.02903, https://arxiv.org/abs/1507.02903.

Hidalgo, *Holomorphic differentials of Generalized Fermat curves* (2017), arXiv:1710.01349, https://arxiv.org/abs/1710.01349.

Auffarth, Lucchini Arteche, Rojas, *A decomposition of the Jacobian of a Humbert-Edge curve* (2019), arXiv:1905.12690, https://arxiv.org/abs/1905.12690.

Edge, *Three Plane Sextics and their Automorphisms* (1969), DOI:10.4153/CJM-1969-139-6 (only abstract/extract inspected).
