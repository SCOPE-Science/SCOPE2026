# The rational nonsymmetric coincidence sextic for two elliptic quotients of a genus-three curve

## Finding

For any \(a,b\in\mathbb C\) with \(a\ne b\) and \(a,b\notin\{-2,2\}\), let
\[
C_{a,b}:\quad y^2=(x^4+ax^2+1)(x^4+bx^2+1).
\]
This is a smooth genus-three hyperelliptic curve. Its two degree-two elliptic quotients
\[
E_-:y^2=(t^2+a-2)(t^2+b-2),\qquad
E_+:y^2=(t^2+a+2)(t^2+b+2)
\]
are isomorphic over \(\mathbb C\) **if and only if** \(s=a+b=0\) or \(F(s,p)=0\), where \(p=ab\) and
\[
\begin{aligned}
F(s,p)={}&5184p^3+(720s^2+73728)p^2\\
&+(12s^4-14336s^2+344064)p\\
&-s^6-3072s^4-118784s^2+524288.
\end{aligned}
\]
The nonsymmetric component \(F=0\) is geometrically irreducible and rational, including as a curve in the ordered \((a,b)\)-plane; its open subset of smooth genus-three parameters has an explicit rational parametrization over \(\mathbb C\). It is not contained in the previously noted symmetry locus \(a+b=0\).

For example \(a=2+8\sqrt 2/3\), \(b=2-8\sqrt 2/3\) is smooth and has \(s=4\), \(p=-92/9\), so it lies on the nonsymmetric component. Here \(j(E_-)=j(E_+)=1728\), while the third natural elliptic quotient \(E_0:y^2=(t^2+at+1)(t^2+bt+1)\) has \(j(E_0)=-8000/81\). In particular the Jacobian is, up to complex isogeny, \(E_0\times E_-^2\), with \(E_0\) not isogenous to \(E_-\).

## Assumptions and scope

All curves and equivalences are over \(\mathbb C\); the distinguished elliptic quotients are those displayed, rather than arbitrary elliptic isogeny factors. The restrictions on \(a,b\) guarantee eight distinct hyperelliptic branch points: each quartic has distinct roots and distinct quartics have no common roots. The quotient equations are the named degree-two elliptic quotients of Borówka--Shatsila, Proposition 4.3. Isomorphic means isomorphic elliptic curves over \(\mathbb C\), equivalently equal \(j\)-invariants, not merely isogenous.

## Proof

**1. Exact elliptic invariants and a complete criterion.** Put \(A=(a-2)(b-2)\), \(B=(a+2)(b+2)\), and \(D=(a-b)^2\). These are all nonzero on the stated domain. For an elliptic quartic \(y^2=t^4+q t^2+r\), its classical binary-quartic invariants are \(I=q^2+12r\), \(J=2q(36r-q^2)\), and
\[
j=1728\frac{4I^3}{4I^3-J^2}.
\]
Applying these to the displayed quotients yields the identities
\[
 j(E_-)=\frac{16(D+16A)^3}{D^2 A},\qquad
 j(E_+)=\frac{16(D+16B)^3}{D^2 B}.
\]
Their denominators do not vanish. Clearing denominators therefore gives equivalence with
\[
 B(D+16A)^3-A(D+16B)^3
 =(B-A)\bigl(D^3-768DAB-4096AB(A+B)\bigr)=0.
\]
Now \(B-A=4(a+b)=4s\), \(D=s^2-4p\), \(A=p-2s+4\), and \(B=p+2s+4\). Direct expansion gives \(D^3-768DAB-4096AB(A+B)=-F(s,p)\). This proves the exhaustive if-and-only-if assertion without genericity assumptions beyond the smoothness domain.

**2. Rationality and irreducibility of the second component.** Work on the nonempty dense open locus where the following changes of variables are defined:
\[
 u=\frac{a-2}{b-2},\qquad v=\frac{a+2}{b+2}.
\]
The inverse is rational:
\[
 b=\frac{2(u+v-2)}{u-v},\qquad a=ub+2(1-u).
\]
If \(r=\alpha/\beta\), the quartic \(y^2=(t^2+\alpha)(t^2+\beta)\) has invariant
\[
 J_*(r)=\frac{16(r^2+14r+1)^3}{r(r-1)^4}.
\]
For \(T=u+u^{-1}\) and \(U=v+v^{-1}\), define the polynomial
\[
 K(u,v)=u^2v^2\bigl((T-2)^2(U-2)^2-768(T-2)(U-2)-4096(T+U-4)\bigr).
\]
The denominators cancel, and \(K\) has degree four in each of \(u,v\). The exact identity
\[
 J_*(u)-J_*(v)=\frac{16(u-v)(uv-1)K(u,v)}{uv(u-1)^4(v-1)^4}
\]
shows that the first factors correspond to the excluded diagonal and the symmetric locus, whereas \(K=0\) is precisely the second component on the open set. Fix \(i\in\mathbb C\) with \(i^2=-1\). The rational map
\[
 u=z^4,\qquad v=\left(\frac{z+i}{z-i}\right)^4
\]
satisfies \(K(u,v)=0\) identically. To see that it parametrizes the *whole* residual curve birationally, fix generic \(u\): the four choices \(z,iz,-z,-iz\) of fourth root give four distinct values of \(v\) (their rational functions have different poles). Hence \(v\) has degree four over \(\mathbb C(u)\), and the degree-four polynomial \(K(u,v)\) is its minimal polynomial up to a nonzero coefficient. Thus \(K\) is irreducible on this open set and the map from \(\mathbb P^1_z\) is generically one-to-one. The inverse formulas transfer this birational parametrization to \(F(a+b,ab)=0\).

There is no extra irreducible component supported on the excluded coordinate boundaries: on \(A=0\) or \(B=0\) the residual factor specializes to \(D^3\); on \(D=0\) it specializes to \(-4096AB(A+B)\). None of those divisors divides it. Hence the entire nonsymmetric component is irreducible. Its image in the symmetric \((s,p)\)-plane is irreducible and rational as the quotient of a rational curve by \((a,b)\leftrightarrow(b,a)\), by Lüroth's theorem. The displayed polynomial \(F(s,p)\) has total degree six and defines that image without an additional component.

**3. A genuine smooth nonsymmetric witness and isogeny consequence.** The parameters \(s=4,p=-92/9\) give \(A=-128/9\), \(B=16/9\), \(D=512/9\), for which the residual factor vanishes, while \(s\ne0\), \(DAB\ne0\). The exact quartic formulas give \(j(E_-)=j(E_+)=1728\), and the same binary-quartic invariant calculation on \(E_0\) gives \(j(E_0)=-8000/81\). The three elliptic quotient pullbacks span the three-dimensional holomorphic-differential space (or use the Klein-four idempotent decomposition), giving \(\operatorname{Jac}(C_{a,b})\sim E_0\times E_-\times E_+\sim E_0\times E_-^2\). Since \(E_-\) has complex multiplication and \(-8000/81\) is not an algebraic integer, \(E_0\) is not isogenous to \(E_-\).

## Verification

The accompanying `verify.py` uses exact SymPy arithmetic to reconstruct the quartic invariants, check the complete polynomial factorization, identify the bidegree-four residual relation, verify its rational parametrization and rational inverse, and verify the nonsymmetric smooth witness and its three \(j\)-invariants. Its successful output is `VERIFY_OK`. The irreducibility and geometric completeness arguments above are parameter-uniform field-degree proofs, not deductions from finite numerical sampling.

## Relationship to prior work

Borówka--Shatsila (2023), Proposition 4.3, supplies the quotient models; Remark 4.7 notes the component \(b=-a\) but does not state the complete equal-invariant locus or rational residual sextic. Lombardo--Lorenzo García--Ritzenthaler--Sijsling (2020), Proposition 1.1, supplies the general completely split genus-three Jacobian models, not this coincidence classification. Shaska (2013/2014), Section 5.1, computes an equality locus for *two degree-four* elliptic subcovers of a \((2,4,4)\)-split construction; that is not an equality theorem for these explicitly distinguished *degree-two* elliptic quotients, and its five genus-zero components do not imply the displayed sextic identity. Auffarth--Borówka (2021), Section 7, studies complementary elliptic factors and possible cover degrees without this exact locus.

## Limitations

The rationality concerns the specified parameter curve and its marked degree-two quotients; it is not a classification of all genus-three curves whose Jacobians have repeated elliptic isogeny factors, nor a claim about principal polarizations or Prym-map fiber cardinalities. Isomorphism of the two displayed elliptic quotients is strictly stronger than their possible isogeny. No priority search, including mathematical-index searches, establishes absolute novelty; differently marked quotients, unindexed classical formulas, and the later journal version of the originating article are residual comparison risks.

## References

- P. Borówka and A. Shatsila, *Hyperelliptic genus 3 curves with involutions and a Prym map*, arXiv:2308.07038v1 (first public 2023-08-14), Proposition 4.3 and Remark 4.7, https://arxiv.org/html/2308.07038v1.
- D. Lombardo, E. Lorenzo García, C. Ritzenthaler, and J. Sijsling, *Decomposing Jacobians via Galois covers*, arXiv:2003.07774v1, Proposition 1.1 and Table 1, https://arxiv.org/html/2003.07774v1.
- T. Shaska, *Genus 3 hyperelliptic curves with (2,4,4)-split Jacobians*, arXiv:1306.5284v2, Sections 1 and 5.1, https://arxiv.org/html/1306.5284v2.
- R. Auffarth and P. Borówka, *Non-simple polarised abelian surfaces and genus 3 curves with completely decomposable Jacobians*, arXiv:2111.11799v3, Section 7, https://arxiv.org/html/2111.11799v3.
