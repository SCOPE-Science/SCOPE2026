# Complete \(\mathbb F_4\) isogeny spectrum of a genus-five Artin–Schreier family

## Finding
Let \(\mathbb F_4=\mathbb F_2(\omega)\), where \(\omega^2+\omega+1=0\). For all \((a,b,c,d)\in\mathbb F_4^4\) with \(c\ne0\), let \(C_{a,b,c,d}\) be the smooth projective curve given on its affine chart by
\[
y^2+y=x^3,\qquad u^2+u=ax+bxy+cx^2y+dy.
\]
The \(192\) parameter quadruples give **exactly fourteen** distinct Hasse–Weil numerator polynomials over \(\mathbb F_4\), hence exactly fourteen \(\mathbb F_4\)-isogeny classes among their Jacobians. The complete list, including the number of parameter quadruples yielding each polynomial, is given below. These multiplicities count **parameter quadruples, not isomorphism classes of curves**.

Write \(L(T)=\sum_{j=0}^{10}c_jT^j\), with \(c_0=1\); the table supplies \((c_1,c_2,c_3,c_4,c_5)\). For each \(0\le j\le4\), the remaining coefficients are \(c_{10-j}=4^{5-j}c_j\). The column “SS” means that the Newton polygon is supersingular.

| Number of quadruples | \((c_1,c_2,c_3,c_4,c_5)\) | SS |
|---:|---|:---:|
| 36 | \((8,32,92,216,448)\) | no |
| 24 | \((4,8,16,32,64)\) | yes |
| 24 | \((4,8,20,40,64)\) | no |
| 24 | \((4,8,12,8,0)\) | no |
| 18 | \((8,32,92,224,480)\) | no |
| 12 | \((4,8,28,64,96)\) | no |
| 12 | \((4,8,4,-32,-96)\) | no |
| 12 | \((0,0,4,-8,0)\) | no |
| 9 | \((8,32,96,256,576)\) | yes |
| 6 | \((0,0,4,0,32)\) | no |
| 6 | \((4,8,16,48,128)\) | yes |
| 3 | \((4,8,16,16,0)\) | yes |
| 3 | \((12,72,288,848,1920)\) | yes |
| 3 | \((0,0,0,0,64)\) | yes |

In particular, the Newton polygon over the algebraic closure is exactly
\[
\operatorname{NP}(C_{a,b,c,d})=
\begin{cases}
(\tfrac12^{[10]}),&c=b^2,\\
(\tfrac13^{[3]},\tfrac12^{[4]},\tfrac23^{[3]}),&c\ne b^2.
\end{cases}
\]
Here the notation \(\lambda^{[r]}\) means that the slope \(\lambda\) has multiplicity \(r\). Thus exactly \(48\) parameter quadruples have supersingular Jacobians, and the other \(144\) have slopes \(1/3,1/2,2/3\). **No member of this \(\mathbb F_4\) parameter family has Newton slopes \(1/4,1/2,3/4\).** This last exclusion is confined to \(\mathbb F_4\)-valued parameters.

## Assumptions and scope
The ground field and all parameters are precisely as specified above. The projective model in coordinates \([X:Y:Z:T:U]\) is the intersection
\[
X^2+YZ=0,\quad T^2+ZT+XY=0,\quad U^2+UZ+aXZ+bXT+cYT+dZT=0.
\]
The unique point on \(Z=0\) is \([0:1:0:0:0]\). The affine equations follow from \(Z=1\), \(X=x\), \(Y=x^2\), \(T=y\), and \(U=u\). This is the four-parameter locus considered in Dragutinović's 2025 work, with the parameters reordered for readability. There is no assertion about the complete algebraic-closure family or the number of distinct geometric curve-isomorphism classes.

## Proof
**Smoothness, irreducibility, and genus.** The first affine equation defines the elliptic function field \(K=\mathbb F_4(x,y)\), \(y^2+y=x^3\). On its elliptic curve \(E\), \(x\) and \(y\) have pole orders \(2\) and \(3\) at infinity. Therefore the function \(f=ax+bxy+cx^2y+dy\) has a unique pole, of order \(7\), since \(c\ne0\). An Artin–Schreier function with an odd pole cannot be of the form \(v^2+v\); thus \(u^2+u=f\) defines a separable degree-two extension of \(K\), totally ramified at infinity and unramified elsewhere. The different exponent there is \(7+1=8\). Riemann–Hurwitz gives \(2g(C)-2=2(2g(E)-2)+8=8\), so \(g(C)=5\). The affine curve is smooth since each Artin–Schreier equation has derivative \(1\) in its new variable. At the unique point at infinity, the differentials of the three projective defining quadrics have independent components in the \(Z\), \(X\), and \(T\) directions (the last coefficient is \(c\ne0\)). Hence the displayed complete-intersection model is the smooth curve and its point at infinity is rational.

**Exact point-count identity.** For every integer \(m\ge1\), let \(q=4^m\) and \(\operatorname{Tr}\) be the absolute trace \(\mathbb F_q\to\mathbb F_2\). Since \(v\mapsto v^2+v\) has exactly two preimages when \(\operatorname{Tr}(v)=0\) and none otherwise, the point count is the exact integer
\[
N_m(a,b,c,d)=1+2\#\{(x,y)\in\mathbb F_q^2:y^2+y=x^3,\ \operatorname{Tr}(ax+bxy+cx^2y+dy)=0\}.
\]
No randomness, approximate arithmetic, or searches for rational points with unbounded denominators enter this formula.

**Exhaustion and polynomial reconstruction.** The artifact `verify.py` enumerates all \(4\cdot4\cdot3\cdot4=192\) parameter quadruples. For \(m=1,2,3,4,5\), it uses irreducible binary polynomials of degrees \(2m\) to implement the fields \(\mathbb F_{4^m}\) exactly, enumerates every elliptic pair, evaluates the trace condition, and computes \(N_m\) for every quadruple. Irreducibility of each defining polynomial is also checked in the script. For each parameter, set \(S_m=4^m+1-N_m\). Newton's identities give
\[
c_0=1,\qquad c_n=-\frac1n\sum_{i=1}^{n}c_{n-i}S_i\quad(1\le n\le5).
\]
The genus-five Weil functional equation supplies \(c_{10-j}=4^{5-j}c_j\) for \(0\le j\le4\). Thus the five exact counts determine the **entire** Weil polynomial. The exhaustive frequency counter produces exactly the fourteen rows displayed above. A second, direct enumeration of all triples \((x,y,u)\) independently checks representative parameters over \(\mathbb F_4\), \(\mathbb F_{16}\), and \(\mathbb F_{64}\).

**Slope and isogeny conclusions.** Take the lower convex hull of the points \((j,v_2(c_j))\), \(0\le j\le10\), and divide its segment slopes by \(v_2(4)=2\). Computing these exact rational slopes for the fourteen coefficient rows gives only the two Newton polygons displayed. For each row, the same exhaustive table identifies whether its contributing parameters obey \(c=b^2\); there are no mixed rows. Finally, Tate's isogeny theorem over finite fields says that two abelian varieties are isogenous over \(\mathbb F_4\) precisely when their characteristic Frobenius polynomials agree. The fourteen pairwise distinct Weil polynomials therefore identify exactly fourteen Jacobian isogeny classes represented in the parameter family.

## Verification
Run `python3 verify.py` with a standard Python 3 interpreter. It requires no external packages, lookup tables, online services, or random seeds. The expected terminal output begins `VERIFY_OK`. The `zeta_table.csv` artifact gives the complete same table in machine-readable form. The verifier checks every coefficient row and multiplicity, irreducibility of its finite-field models, both Newton-polygon types and the square-class partition, and independently enumerates selected small extensions by testing all \((x,y,u)\) triples.

The proof uses finite exhaustive enumeration only for a **finite**, completely stated domain of \(192\) parameter quadruples, and the functional equation for full-polynomial reconstruction. Computations at \(\mathbb F_4\) do not prove any claim for arbitrary algebraically closed characteristic-two parameter fields.

## Relationship to prior work
Dragutinović's 2025 work provides the original four-dimensional characteristic-two family, its supersingular subfamily, geometric automorphism classification, and Newton-polygon questions. Its preprint Corollary 4.4 discusses the generic Newton polygon and a concrete \(\mathbb F_2\) example, not the fourteen Weil polynomials or their multiplicities for all \(\mathbb F_4\) coefficient quadruples. The author's earlier paper, *Computing binary curves of genus five* (2024), enumerates genus-five curves over \(\mathbb F_2\), not the present \(\mathbb F_4\) family. The family and the supersingularity direction \(c=b^2\Rightarrow\) supersingular are **prior results**, not claimed as new here. The contribution is the exact fourteen-class arithmetic distribution and its full two-type Newton classification over the first quadratic coefficient extension.

## Limitations
Counts represent parameter choices, not \(\mathbb F_4\)- or algebraic-closure isomorphism classes of curves. A specific Weil polynomial may arise from several nonisomorphic curves. The result is a finite-base-field classification only; it does **not** prove that the Newton type \((1/4,1/2,3/4)\) never occurs elsewhere in the four-dimensional family, nor does it settle any global Newton-stratification or supersingular-component conjecture. The result does not construct explicit isogenies or determine polarizations. Priority against unidentified databases or alternate models remains provisional; the mathematical proof is exact conditional only on standard Artin–Schreier, Weil, and finite-field isogeny theorems.

## References
1. D. Dragutinović, *An unusual family of supersingular curves of genus five in characteristic two*, arXiv:2507.03519 (first publicly submitted 2025-07-04); *Finite Fields and Their Applications* **110** (2026), 102736, doi:10.1016/j.ffa.2025.102736.
2. D. Dragutinović, *Computing binary curves of genus five*, arXiv:2202.07809; *Journal of Pure and Applied Algebra* **228** (2024), 107522.
3. Standard Artin–Schreier ramification theory, genus formula, Newton identities, Weil functional equation, and Tate's isogeny theorem for abelian varieties over finite fields.
