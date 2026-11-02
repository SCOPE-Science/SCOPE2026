# A nodal rank-one Rota–Baxter threefold with six automorphism strata
## Finding
Let \(k\) be **any field**, and let \(A=\Lambda_k(k^2)\) have basis \(1,x,y,z\), with \(z=xy=-yx\), \(x^2=y^2=0\), and \(z\) annihilating \(x,y,z\). A weight-zero Rota–Baxter operator is a linear map satisfying
\[
R(a)R(b)=R(R(a)b+aR(b))\qquad(a,b\in A).
\]
Every nonzero rank-one such operator is uniquely expressible as a rank-one tensor \(R=u\otimes\phi\) modulo \((u,\phi)\sim(tu,t^{-1}\phi)\), where
\[
u=ax+by+cz\ne0,\qquad \phi=\alpha\epsilon+\beta x^*+\gamma y^*,\qquad a\beta+b\gamma=0.
\]
Here \(\epsilon\) extracts the coefficient of \(1\), and \(x^*,y^*\) are the dual coordinate functionals. The nonzero functional condition is \((\alpha,\beta,\gamma)\ne(0,0,0)\). This description holds also in characteristic \(2\).

The **reduced projectivization** \(X\) of this rank-one operator locus is the incidence threefold
\[
X\cong\left\{([a:b:c],[\alpha:\beta:\gamma])\in\mathbb P^2_k\times\mathbb P^2_k:\ a\beta+b\gamma=0\right\}.
\]
It is integral, has exactly one geometric singular point, and that singularity is an ordinary quadratic double point. Its local equation is \(a\beta+b\gamma=0\) in four affine coordinates; the singular point corresponds to \(R(1)=z\) and \(R(x)=R(y)=R(z)=0\), up to nonzero scalar.

The full algebra automorphism group has **exactly six conjugacy orbits** on nonzero rank-one weight-zero Rota–Baxter operators, over every field. Representatives \(R=u\otimes\phi\), in the order used below, are
\[
(z,x^*),\quad(z,\epsilon),\quad(z,\epsilon+x^*),\quad
(x,y^*),\quad(x,\epsilon),\quad(x,\epsilon+y^*).
\]
If \(k=\mathbb F_q\), then the six orbit cardinalities are respectively
\[
q^2-1,\quad q-1,\quad(q-1)(q^2-1),\quad
q(q+1)(q-1),\quad q(q+1)(q-1),\quad q(q+1)(q-1)^2.
\]
Consequently the number of **nonzero rank-one** weight-zero Rota–Baxter operators is exactly
\[
\boxed{q^4+2q^3-q^2-q-1},
\]
and the number of points of the projective variety \(X(\mathbb F_q)\) is
\[
\boxed{q^3+3q^2+2q+1}.
\]

The six projective orbit strata have dimensions \(1,0,2,2,2,3\) in the displayed order. Writing \(Z_1,Z_2,Z_3\) for the first three and \(U_1,U_2,U_3\) for the last three, their closures are:
\[
\overline{Z_1}=Z_1,\quad\overline{Z_2}=Z_2,\quad
\overline{Z_3}=Z_1\cup Z_2\cup Z_3,
\]
\[
\overline{U_1}=U_1\cup Z_1,\quad
\overline{U_2}=U_2\cup Z_2,\quad
\overline{U_3}=X.
\]
These closure assertions are statements about reduced projective varieties over \(k\); no description of the possibly nonreduced full Rota–Baxter scheme is claimed.

## Assumptions and scope
The exterior algebra has \(J=(x,y,z)\), with \(J^2=kz\) and \(J^3=0\). The algebra is associative and unital. All automorphisms are unital \(k\)-algebra automorphisms. An operator of rank one is nonzero by definition; the zero map is excluded from the counted locus and added separately only when explicitly stated. The equation \(z=xy=-yx\) is meaningful in characteristic \(2\) as \(xy=yx\).

The projectivization identifies operators differing by a nonzero scalar; conjugacy classes above instead concern actual nonzero operators, **without** imposing scalar equivalence. The six conjugacy classes happen to remain six after projectivization, because each is stable under all nonzero scalar multiples. The singularity assertion concerns the reduced incidence variety, not the ambient unrestricted operator scheme.

## Proof
**1. The rank-one criterion.** Write \(R(a)=\phi(a)u\), with \(u\ne0\), \(\phi\ne0\). Applying the identity with \(b\in\ker\phi\) and \(\phi(a)\ne0\) gives \(\phi(ub)=0\). Hence \(\phi\circ L_u=c_0\phi\) for some scalar \(c_0\). Applying the identity to \(a,b\) with \(\phi(a)=\phi(b)=1\) yields \(u^2=2c_0u\). If \(u\) were a unit, multiplication by its inverse would give \(u=2c_0\cdot1\); then \(\phi\circ L_u=2c_0\phi=c_0\phi\) forces \(c_0=0\), contrary to \(u\ne0\). Thus \(u\in J\). As \(L_u^3=0\), the eigenvalue equation \(\phi\circ L_u=c_0\phi\) forces \(c_0=0\) over **every characteristic**. Therefore \(\phi(Au)=0\). Conversely, for \(u\in J\), \(u^2=0\) and \(\phi(Au)=0\) imply the Rota–Baxter identity term by term.

**2. Incidence coordinates and singularity.** Put \(u=ax+by+cz\). Since \(Au\) contains \(u\) and, unless \((a,b)=(0,0)\), also \(z\), while \(Az=kz\), the annihilation requirement is exactly \(\phi(z)=0\) and \(a\phi(x)+b\phi(y)=0\). This gives the stated incidence equation. The Segre map from \(\mathbb P(J)\times\mathbb P(A^*)\) identifies a rank-one projective linear operator with a unique pair of projective factors. The hypersurface equation is irreducible; hence \(X\) is integral and three-dimensional. Its gradient in the relevant variables is \((\beta,\gamma,a,b)\). Therefore a singular point requires \(a=b=\beta=\gamma=0\), necessarily giving \(([0:0:1],[1:0:0])\). On the affine chart \(c=\alpha=1\), its equation is precisely \(a\beta+b\gamma=0\); this nondegenerate quadratic form defines a cone over a smooth quadric surface, including in characteristic \(2\).

**3. Automorphism action and six orbits.** Every algebra automorphism fixes \(1\), preserves \(J\) and \(J^2\), and is uniquely of the form
\[
 x\longmapsto a_0x+b_0y+c_0z,\qquad
 y\longmapsto d_0x+e_0y+f_0z,\qquad
 z\longmapsto(a_0e_0-b_0d_0)z,
\]
with \(a_0e_0-b_0d_0\ne0\). Conversely every such map preserves all defining exterior-algebra relations, hence is an automorphism.

There are two invariant possibilities for the image line: \(kz\), or a line outside \(kz\). In the first case choose \(u=z\), so \(\phi=\alpha\epsilon+\ell\) with \(\ell\in\operatorname{span}(x^*,y^*)\). Invertible two-by-two changes of generators, whose determinant scales \(z\), act transitively in each of the three cases \((\alpha=0,\ell\ne0)\), \((\alpha\ne0,\ell=0)\), \((\alpha\ne0,\ell\ne0)\). For the third case, after scaling \(\alpha\) with the determinant, the special linear group is transitive on nonzero covectors.

For a line outside \(kz\), a generator change and a shear put \(u=x\). Its annihilating functional then has the form \(\phi=\alpha\epsilon+\beta y^*\). The stabilizer of the image line contains maps \(x\mapsto sx\), \(y\mapsto tx+vy+wz\) with arbitrary \(s,v\in k^\times\). Conjugation acts on the two functional coefficients by \((\alpha,\beta)\mapsto(s\alpha,(s/v)\beta)\), yielding exactly the remaining three classes. The vanishing/nonvanishing conditions and whether the image lies in \(J^2\) distinguish all six.

**4. Closure relations.** The open stratum \(U_3\) has \((a,b)\ne(0,0)\) and both \(\alpha\) and \((\beta,\gamma)\) nonzero, so it is dense in integral \(X\). The closure of \(U_1\) is the incidence hypersurface on \(\alpha=0\), with the missing \(z\)-fiber precisely \(Z_1\); the closure of \(U_2\) is the whole section \(\phi=\epsilon\), adding only \(Z_2\). The closure of \(Z_3\) is the entire fiber over \(u=z\), adding \(Z_1\) and \(Z_2\). The latter two are closed in \(X\). This proves the six stated closures and their dimensions.

**5. Arithmetic counts.** For \(u\in kz\), projectivization chooses a single image line and \(\phi\) ranges over the nonzero elements of a three-dimensional annihilator: \(q^3-1\) actual operators. There are \(q(q+1)\) projective lines of \(J\) outside \(kz\), each with a two-dimensional annihilator containing \(q^2-1\) nonzero functionals. Hence the total is \((q^3-1)+q(q+1)(q^2-1)\), the asserted polynomial. Splitting functionals by their constant and linear components gives the six orbit sizes above. Since every nonzero operator admits exactly \(q-1\) scalar multiples, dividing by \(q-1\) gives the projective count.

## Verification
Run `python3 verify.py` from the directory containing this document. The verifier independently enumerates every rank-one candidate and checks the Rota–Baxter identity on all sixteen ordered basis pairs for \(q=2,3,5,7\). It constructs the entire algebra automorphism groups for \(q=2,3,5\), computes all six representative orbits, checks pairwise disjointness and exhaustion, and tests the finite-field formulas. Symbolic differentiation checks the defining gradient and full quadratic rank of the nodal chart. The completed run returned `VERIFY_OK`.

## Relationship to prior work
Benito, Gubarev and Pozhidaev (2018, Statement 5.4) give a general coarse automorphism normal form for **all** weight-zero Rota–Baxter operators on the Grassmann plane over fields of characteristic not two, together with a general observation (Corollary 5.3) that operator sets can be projectivized. Shakoor and Noor-ul-Ain (2026, Theorem 4.1) give an explicit matrix classification of all such operators **over the reals**. These stronger *recognition/parameterization* results already cover the existence of the rank-one operators; the existence and the usual rank-one tensor criterion are not presented as independent breakthroughs.

The result here instead computes the reduced rank-one projective variety **as an incidence threefold with its isolated quadratic singularity**, distinguishes its six full automorphism orbits and closure relations over arbitrary fields, and determines their exact counts over every finite field. The earlier normal forms do not state those exact geometric or orbit invariants. A published exact enumeration over \(\mathbb F_2\) already implies the \(q=2\) total \(25\) and provides an overlapping special case; no priority is claimed for that individual count.

## Limitations
The classification concerns rank-one operators of weight zero on exactly the four-dimensional exterior algebra. It does not classify higher-rank operators, nonzero weights, exterior algebras of larger generator rank, or the possibly nonreduced scheme structure of the full Rota–Baxter parameter space. No claim of historical priority beyond the searched literature is warranted; the 2018 coarse normal form is a substantial nearby predecessor. Independent mathematical review has not been performed.

## References
1. K. Shakoor and N.-ul-Ain, *The Classification of the Rota-Baxter Operators on Four-dimensional Grassmann Algebra*, arXiv:2609.07377v1, submitted 7 September 2026; especially Theorem 4.1. https://arxiv.org/abs/2609.07377
2. P. Benito, V. Gubarev and A. Pozhidaev, *Rota–Baxter Operators on Quadratic Algebras*, Mediterranean Journal of Mathematics **15** (2018), article 189; especially Corollary 5.3 and Statement 5.4. https://doi.org/10.1007/s00009-018-1234-5
