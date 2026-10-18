# Hasse–Weil zeta function of the ordinary genus-six boundary curve

## Finding

Let \(C/\mathbb F_3\) be the unique smooth projective model of
\[
y^3-y=x+\frac{1}{x^3-x}.
\]
Its complete zeta function is
\[
Z(C,T)=\frac{P_C(T)}{(1-T)(1-3T)},\qquad
P_C(T)=1+16T^3+118T^6+432T^9+729T^{12}.
\]
The numerator factors over the integers as
\[
P_C(T)=(1-T+3T^2)^2(1+T-2T^2+3T^3+9T^4)^2.
\]
In particular, \(\#C(\mathbb F_{3^n})=3^n+1\) for every \(n\ge1\) not divisible by \(3\). Over \(\mathbb F_3\), the Jacobian is isogenous to \(E^2\times A^2\), where \(E\) is the elliptic isogeny class of trace \(1\) and \(A\) is the simple ordinary abelian-surface isogeny class with the displayed quartic numerator. Thus \(\#\operatorname{Jac}(C)(\mathbb F_3)=P_C(1)=1296\).

## Assumptions and scope

Work over the prime field \(\mathbb F_3\). The curve means the smooth projective normalization, not the singular naive plane closure of the affine rational equation. The rational function \(f(x)=x+1/(x^3-x)\) has four simple poles, at \(\infty,0,1,-1\), all rational. At each pole the Artin–Schreier cover has exactly one totally ramified rational point. The resulting cover is geometrically connected because an Artin–Schreier coboundary cannot have a simple pole. By Riemann–Hurwitz, \(g(C)=(3-1)(4\cdot2-2)/2=6\); it is ordinary, of \(3\)-rank \(6\), also recorded in the geometric source. The calculation concerns the rational parameter \(c=1\); it does not assert a formula for general parameters over arbitrary finite fields.

## Proof

**1. A uniform vanishing trace outside multiples of three.** For every \(n\ge1\), put \(q=3^n\) and let \(\mathrm{Tr}:\mathbb F_q\to\mathbb F_3\) be the absolute trace. For \(x\notin\mathbb F_3\), \(f(x+1)=f(x)+1\), since \((x+1)^3-(x+1)=x^3-x\). Translation by \(1\) partitions the \(q-3\) non-poles into free three-element orbits. If \(3\nmid n\), the traces of \(f(x),f(x+1),f(x+2)\) are precisely the three elements of \(\mathbb F_3\). The map \(y\mapsto y^3-y\) has image exactly the trace-zero subspace, each image value having three preimages. Thus precisely one member of each non-pole orbit has three affine points above it. Adding the four totally ramified pole points gives \(N_n:=\#C(\mathbb F_q)=(q-3)+4=q+1\) whenever \(3\nmid n\).

**2. Two exhaustive finite-field evaluations.** In \(\mathbb F_{27}=\mathbb F_3[u]/(u^3+2u+1)\), exact enumeration of the \(24\) non-pole values gives absolute-trace frequency \((24,0,0)\). In \(\mathbb F_{729}=\mathbb F_3[v]/(v^6+v+2)\), enumeration of the \(726\) non-poles gives frequency \((222,252,252)\). Both defining polynomials are irreducible, as established by exhaustive monic-divisor tests of degrees at most half their degrees. Therefore \(N_3=4+3\cdot24=76\) and \(N_6=4+3\cdot222=670\). The attached standalone `verify_zeta.py` independently counts the complete fibres of \(y^3-y\) for each \(1\le n\le6\), without relying on the trace-frequency shortcut. It obtains
\[
(N_1,N_2,N_3,N_4,N_5,N_6)=(4,10,76,82,244,670).
\]
Each finite computation enumerates all relevant field elements; none is extrapolated from sampling.

**3. Completion from the functional equation.** Write \(P_C(T)=\prod_{j=1}^{12}(1-\alpha_jT)=\sum_{k=0}^{12}a_kT^k\), with \(a_0=1\). Let \(s_n=\sum_j\alpha_j^n=3^n+1-N_n\). The preceding calculation gives \(s_1=s_2=s_4=s_5=0\), \(s_3=-48\), and \(s_6=60\). Newton's identities \(k a_k=-\sum_{i=1}^{k}a_{k-i}s_i\) give \(a_1=a_2=a_4=a_5=0\), \(a_3=16\), \(a_6=118\). The genus-six Hasse–Weil functional equation yields \(a_{12-k}=3^{6-k}a_k\) for \(0\le k\le6\). Hence \(a_9=432\), \(a_{12}=729\), and all the other coefficients not displayed in the theorem vanish. This proves the entire zeta function and thus determines every extension-field point count, not merely the six computed counts.

**4. Jacobian factors.** Exact polynomial multiplication verifies the displayed factorization. The reciprocal monic polynomial of the quartic factor is \(R(z)=z^4+z^3-2z^2+3z+9\). It has no integral root among the divisors \(\pm1,\pm3,\pm9\). Any monic integral quadratic factorization would have factors \((z^2+az+b)(z^2+cz+d)\), with \(bd=9\), \(a+c=1\), \(ad+bc=3\), and \(ac+b+d=-2\). For \(b\ne d\), \(a=(3-b)/(d-b)\), and inspection of the four possible ordered pairs \((b,d)=(1,9),(9,1),(-1,-9),(-9,-1)\) rules out an integral \(a\). For \(b=d\), the second relation forces \(b=d=3\), where \(a+c=1\) and \(ac=-8\), of nonsquare discriminant \(33\). Thus \(R\) is irreducible over \(\mathbb Q\), so the quartic is an irreducible Weil factor. The isogeny decomposition of \(\operatorname{Jac}(C)\) follows from the standard finite-field isogeny decomposition theorem. The quadratic factor has Frobenius trace \(1\); the quartic defines a simple dimension-two factor. Since the original curve is ordinary, so are these factors. Evaluation at \(T=1\) gives \((3\cdot12)^2=1296\).

## Verification

From a directory containing the attached file, execute `python3 verify_zeta.py` using only the Python standard library. The checker explicitly constructs six finite fields, tests irreducibility of the specified moduli by complete divisor enumeration, enumerates all \(y\mapsto y^3-y\) fibres and all non-pole \(x\) for every extension of degrees \(1\) through \(6\), cross-checks the two nontrivial absolute-trace histograms, reconstructs the Weil coefficients exactly using rational arithmetic and the functional equation, checks the factorization, and checks the Jacobian order. The irreducible-factor argument and the geometric ramification justification are also supplied in the proof above; the finite-field program alone is not substituted for them.

## Relationship to prior work

Tafazolian's [1, Propositions 8.7–8.8] identifies the ordinary genus-six four-pole family and computes its geometric automorphism group, of order \(72\), but does not compute this prime-field zeta polynomial or its Jacobian isogeny factors. Bouw–Ho–Malmskog–Scheidler–Srinivasan–Vincent [2] determine zeta functions for *different* highly symmetric Artin–Schreier curves of polynomial one-pole form \(y^p-y=xR(x)\) with additive \(R\); those are supersingular, whereas this curve is ordinary with four poles. Lauder–Wan [3] provide a general computational framework for rational Artin–Schreier covers with simple poles, but no exact prime-field polynomial or isogeny identification of the curve here. Known tables of finite-field abelian isogeny classes can contain the individual polynomial factors without identifying this genus-six curve with their square product.

## Limitations

This is a complete arithmetic statement for one explicitly specified \(\mathbb F_3\)-model, not for all \(c\) or all characteristic-three ground fields. The proof of the general \(n\)-degree point counts uses the genus-six functional equation in addition to the finite counts at degrees \(3\) and \(6\). No assertion is made that the underlying curve or its geometric symmetry group is new; only the complete arithmetic identification is at issue. A previously unindexed computation for an equivalent model could still subsume this exact zeta function.

## References

[1] S. Tafazolian, *Sharp bounds and gap phenomena for large \(p\)-subgroups of automorphism groups of curves*, arXiv:2610.05539v1 (2026), Sections 1 and 8. https://arxiv.org/html/2610.05539v1

[2] I. Bouw, W. Ho, B. Malmskog, R. Scheidler, P. Srinivasan, C. Vincent, *Zeta functions of a class of Artin–Schreier curves with many automorphisms*, arXiv:1410.7031v2 (2015), Sections 0.1 and 0.8. https://arxiv.org/html/1410.7031v2

[3] A. Lauder and D. Wan, *Computing zeta functions of Artin–Schreier curves over finite fields II*, Journal of Complexity 20 (2004), 331–349. https://ora.ox.ac.uk/objects/uuid:ca50fdb0-542d-4824-b1e7-906cb2d16184
