# The complete \(A_1\)–\(A_3\)–\(A_5\) singularity stratification of genus-five Howe sextics

## Finding
Let \(k\) be algebraically closed of characteristic zero or characteristic at least \(5\), and let \(P,Q\in k[x]\) be monic squarefree quartics with no common root. Put \(h=P-Q\), \(s=P+Q\), and \(d=\deg h\in\{0,1,2,3\}\), and let \(C\subset\mathbf P^2_k\) be the degree-six projective closure of
\[
f(x,y)=y^4-2s(x)y^2+h(x)^2=0.
\]
Then \(C\) is geometrically integral, its normalization has genus \(5\), and **every singularity is a two-branch \(A\)-type singularity**. The complete list, with no other singularities, is:

1. For every distinct root \(r\) of \(h\) of multiplicity \(e\), \((r:0:1)\) has completed local form \(v^2-u^{2e}=0\), hence type \(A_{2e-1}\), \(\delta=e\), \(\mu=\tau=2e-1\).
2. \((0:1:0)\) always has completed local form \(v^2-u^4=0\), hence type \(A_3\), \(\delta=2\).
3. If \(d<3\), \((1:0:0)\) has completed local form \(v^2-u^{2(3-d)}=0\), hence type \(A_{2(3-d)-1}\), \(\delta=3-d\). If \(d=3\), this point is not on \(C\).

In all cases the total \(\delta\)-invariant is precisely \(2+d+(3-d)=5\), and the singularities have smooth local branches, so **no cusps occur**. The seven exhaustive root-partition strata (all nonempty) are:

| Degree and multiplicities of \(h\) | Singularities at finite points | Singularities at infinity | Total basket |
|---|---|---|---|
| \(3:(1,1,1)\) | \(3A_1\) | \(A_3\) | \(3A_1+A_3\) |
| \(3:(2,1)\) | \(A_3+A_1\) | \(A_3\) | \(A_1+2A_3\) |
| \(3:(3)\) | \(A_5\) | \(A_3\) | \(A_3+A_5\) |
| \(2:(1,1)\) | \(2A_1\) | \(A_3+A_1\) | \(3A_1+A_3\) |
| \(2:(2)\) | \(A_3\) | \(A_3+A_1\) | \(A_1+2A_3\) |
| \(1:(1)\) | \(A_1\) | \(2A_3\) | \(A_1+2A_3\) |
| \(0:(\varnothing)\) | none | \(A_3+A_5\) | \(A_3+A_5\) |

## Assumptions and scope
The quartic branch sets are individually simple and disjoint. No restriction on moduli besides these hypotheses is needed. The theorem holds over algebraically closed fields of characteristic zero or \(p\ge5\); the listed analytic equivalences mean isomorphisms of completed local \(k\)-algebras. It is **not** a claim about a different Howe sextic arising from two genus-two covers with four common branch points.

## Proof
Set \(S=P+Q\), \(D=P-Q\). Since both are monic quartics, \(0\le d=\deg D\le3\). The function field of the affine equation is \(k(x)(\sqrt P,\sqrt Q)\): indeed set \(y=\sqrt P+\sqrt Q\), then \(D/y=\sqrt P-\sqrt Q\), so the two square roots are recovered as \((y\pm D/y)/2\). Their branch divisors are disjoint, so their squareclasses are independent; the resulting degree-four field extension is a field. The curve is geometrically integral. Its degree-four map to \(\mathbf P^1\) has eight distinct branch values, each of inertia order two; Riemann–Hurwitz gives \(2g-2=-8+8(2)=8\), hence \(g=5\).

For affine points, \(f_y=4y(y^2-S)\). If \(y\ne0\), the simultaneous equations \(f=f_y=0\) give \(y^2=S\) and \(0=f=-4PQ\), so one branch quartic, say \(P\), vanishes simply while \(Q\ne0\). Then \(f_x=-4P'Q\ne0\); hence there is no affine singularity with \(y\ne0\). If \(y=0\), \(f=D^2\) and \(f_x=2DD'\), so the singular points are exactly the roots of \(D\), and they lie on \(C\). At such a root \(r\), \(S(r)=2P(r)\ne0\). In \(k[[t,y]]\), with \(t=x-r\), the element \(2S(x)-y^2\) is a unit admitting a square root. The new coordinate \(v=y\sqrt{2S(x)-y^2}\) changes \(f\) to \(D(x)^2-v^2\). Writing \(D(x)=t^eu(t)\), \(u(0)\ne0\), and replacing \(v\) with \(v/u(t)\) yields the stated exact \(A_{2e-1}\) normal form, because unit multiplication does not change the hypersurface germ.

Let \(P_4(X,Z)=Z^4P(X/Z)\), \(Q_4(X,Z)=Z^4Q(X/Z)\), and \(D_3(X,Z)=Z^3D(X/Z)\). The homogeneous sextic is
\[
F(X,Y,Z)=Y^4Z^2-2(P_4+Q_4)(X,Z)Y^2+D_3(X,Z)^2.
\]
On \(Z=0\) it is \(X^4(-4Y^2+c^2X^2)\), where \(c\) is the cubic coefficient of \(D\). Thus the only candidate singularities at infinity are \((0:1:0)\) and (if \(c=0\)) \((1:0:0)\); the other two points when \(c\ne0\) are smooth since the \(Y\)-derivative is nonzero.

At \((0:1:0)\), write \(u=X/Y,v=Z/Y\). The completed equation is
\[
v^2-2(P_4+Q_4)(u,v)+D_3(u,v)^2.
\]
Its quadratic term is \(v^2\); its order-four term along \(v=0\) is \(-4u^4\) (the squared cubic contributes only at order six). Since \(\partial F/\partial v\) evaluated at \(v=0\) vanishes to order at least three in \(u\), formal completion of the square in \(v\) (or the formal Morse lemma with parameter) removes the nonquadratic \(v\)-terms and leaves \(v'^2-u^4\cdot U(u)\), with \(U(0)=4\ne0\). Rescaling by a square root of \(U\) gives \(A_3\).

If \(d<3\), the second infinity point \((1:0:0)\) has local coordinates \(v=Y/X,z=Z/X\), and
\[
F(1,v,z)=D_3(1,z)^2-v^2\bigl(2(P_4+Q_4)(1,z)-v^2z^2\bigr).
\]
The second factor is a unit with constant term \(4\); its square root gives a local coordinate replacing \(v\), reducing the equation exactly to \(D_3(1,z)^2-v'^2\). As \(D_3(1,z)=z^{3-d}U(z)\), \(U(0)\ne0\), this is \(A_{2(3-d)-1}\). When \(d=3\), \(F(1,0,0)=c^2\ne0\).

An \(A_{2e-1}\) germ \(v^2-u^{2e}\) factors into two smooth branches \(v=\pm u^e\) with intersection multiplicity \(e\), so \(\delta=e\). Since \(2e\in\{2,4,6\}\) is invertible under the characteristic assumptions, its Jacobian and Tjurina algebras have length \(2e-1\). The genus formula and the precise list follow. For each prescribed root partition of degree at most three, choose a nonzero polynomial \(D\) with precisely that partition. As \(P\) varies among monic quartics, each of the three forbidden conditions \(\operatorname{disc}(P)=0\), \(\operatorname{disc}(P-D)=0\), and \(\gcd(P,D)\ne1\) is a proper Zariski-closed condition: the first two discriminants are nonzero polynomials because translation by \(D\) preserves the affine space of monic quartics, and the resultant with fixed nonzero \(D\) is not identically zero. Since \(k\) is infinite, one can avoid their union. Thus all seven strata occur over every permitted algebraically closed ground field, not only in characteristic zero. The explicit witnesses below independently check the seven patterns over the rationals.

## Verification
One uniform rational family realizes every stratum: take \(P=x^4+x+1\), and \(Q=P-D\) for the seven respective differences \(D=x(x-2)(x+2),\ x^2(x-2),\ x^3,\ x(x-2),\ x^2,\ x,\ 1\). The exact checker `verify_howeII_ADE.py` verifies \(\operatorname{disc}(P)=229\), nonzero \(\operatorname{disc}(Q)\), \(\gcd(P,Q)=1\), the root partitions, the sextic homogenization, the leading local coefficients, and \(\sum\delta=5\) in all seven examples. These calculations prove the **nonemptiness** claim over characteristic zero. They are not substituted for the general local normal-form proof.

## Relationship to prior work
M. Kudo, *Explicit construction of a plane sextic model for genus-five Howe curves, II* (first public 2024-01-01, arXiv:2401.00760), constructs exactly this sextic and proves irreducibility, singular-point locations, multiplicity two at each support, and a seven-case table of support counts in Theorem 2, Propositions 4.1.3–4.1.4, Table 1, and Examples 4.2.1–4.2.2. Those contributions are prior work. The present claim strengthens that table to the **complete analytic \(A_{2e-1}\) types at each support**, their exact contact numbers and delta/Tjurina invariants, and the absence of cusps, including the degeneration from a simple node to a tacnode or \(A_5\). It does not claim novelty for root partitions, locations, or the genus. Moriya–Kudo's 2023 companion part I addresses a different genus-two fiber-product branch pattern.

## Limitations
Only this explicit degree-six model is classified, not every plane model of a genus-five curve. Over positive characteristics \(2\) or \(3\) the argument and normal forms require separate analysis. Possible equivalent calculations in the published journal edition or unindexed literature remain a priority risk. No independent external mathematical review has been performed.

## References
1. M. Kudo, *Explicit construction of a plane sextic model for genus-five Howe curves, II*, arXiv:2401.00760 (first publicly posted 2024-01-01), https://arxiv.org/abs/2401.00760 ; J. Comput. Algebra 11 (2024), DOI 10.1016/j.jaca.2024.100019.
2. T. Moriya and M. Kudo, *Explicit construction of a plane sextic model for genus-five Howe curves, I*, arXiv:2310.15993 (2023), https://arxiv.org/abs/2310.15993.
