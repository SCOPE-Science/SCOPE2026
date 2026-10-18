# A singular normal quotient of the characteristic-two Anick involution

## Finding

Let \(k\) be an algebraically closed field of characteristic \(2\), let \(R=k[x,y,z,t]\), and set \(\Delta=xz+yt\). Consider
\[
\sigma(x)=x+t\Delta,\quad \sigma(y)=y+z\Delta,\quad
\sigma(z)=z,\quad \sigma(t)=t.
\]
Then \(\sigma\) is a nonidentity polynomial involution. Put
\[
U=x^2+t\Delta x,\qquad V=y^2+z\Delta y.
\]
Its **entire invariant ring** is
\[
\boxed{\quad
R^{\langle\sigma\rangle}
 \simeq k[z,t,D,U,V]\big/
 \big((1+zt)D^2+z^2U+t^2V\big),\quad D\longmapsto\Delta.
\quad}
\]
The affine categorical quotient \(Q=\operatorname{Spec}R^{\langle\sigma\rangle}\) is an integral, normal, four-dimensional hypersurface. Its reduced singular locus is exactly the plane \(z=t=D=0\). Its **scheme-theoretic Jacobian singular locus** has defining ideal \((z^2,t^2,D^2)\) inside the displayed quotient ring; equivalently its coordinate ring is
\[
k[z,t,D,U,V]/(z^2,t^2,D^2),
\]
free of rank \(8\) over \(k[U,V]\). Thus the singular plane carries a uniform transverse length-eight Jacobian thickening. Moreover, \(\sigma\) is **not polynomially conjugate to any linear involution** of affine four-space over \(k\).

## Assumptions and scope

All rings are commutative. The characteristic is exactly \(2\). The source automorphism is the characteristic-two reduction of the four-variable Anick map, not the different three-variable free-associative-algebra automorphism sometimes also called Anick's automorphism. Linearizability means conjugacy within \(\operatorname{Aut}_k(k[x,y,z,t])\) to a linear \(k\)-automorphism. No claim about tameness or wildness in the polynomial-automorphism sense is made.

## Proof

**1. Action and invariants.** In characteristic \(2\),
\[
\sigma(\Delta)=(x+t\Delta)z+(y+z\Delta)t
=\Delta+2zt\Delta=\Delta.
\]
Consequently \(\sigma^2=\mathrm{id}\), while \(\sigma(x)\ne x\). The polynomials \(z,t,\Delta\) are fixed. Also
\[
\sigma(U)=(x+t\Delta)^2+t\Delta(x+t\Delta)=U
\]
because the two added copies of \(t^2\Delta^2\) cancel, and similarly \(\sigma(V)=V\). Direct expansion yields the exact relation
\[
z^2U+t^2V=(1+zt)\Delta^2. \tag{1}
\]

**2. No unlisted polynomial invariants.** Let \(P=k[z,t,D,U,V]\) and \(F=(1+zt)D^2+z^2U+t^2V\). The polynomial \(F\) is primitive and of degree one in the pair \((U,V)\) over \(k[z,t,D]\): the coefficient polynomials \(z^2\) and \(t^2\) are coprime. It is consequently irreducible in the polynomial UFD \(P\); \(B=P/(F)\) is an integral hypersurface of dimension \(4\).

Equation (1) gives a map \(B\to R\) with image \(S=k[z,t,\Delta,U,V]\subseteq R^{\langle\sigma\rangle}\). Both \(x\) and \(y\) are integral over \(S\), since they satisfy the monic equations
\[
x^2+t\Delta x+U=0,\qquad y^2+z\Delta y+V=0.
\]
Thus \(R\) is a finite integral \(S\)-algebra, so \(\dim S=\dim R=4\). Since \(\dim B=4\) and \(B\) is a domain, the kernel of \(B\to S\) is zero: any nonzero prime kernel in a four-dimensional domain would lower the quotient's dimension. Hence \(B\cong S\).

Write \(K=\operatorname{Frac}(R)\) and \(L=\operatorname{Frac}(B)\). In \(K\), since \(t\ne0\),
\[
y=(\Delta+zx)/t.
\]
The quadratic equation for \(x\) shows \([K:L]\le2\). Because \(\sigma\) is a nontrivial \(L\)-automorphism of \(K\), this degree is exactly \(2\); therefore \(K^{\langle\sigma\rangle}=L\).

To show \(B\) is normal, compute its five partial derivatives:
\[
\partial_zF=tD^2,\qquad
\partial_tF=zD^2,\qquad
\partial_DF=0,\qquad
\partial_UF=z^2,\qquad
\partial_VF=t^2.
\]
Over the perfect field \(k\), the common zero locus of \(F\) and these derivatives is exactly \(z=t=D=0\). This is a plane of dimension \(2\), hence codimension \(2\) in the fourfold \(Q\). Thus \(B\) satisfies \(R_1\); as a hypersurface it is Cohen--Macaulay and satisfies \(S_2\). Serre's criterion gives normality.

Finally each element of \(R^{\langle\sigma\rangle}\) is integral over \(B\), because \(R\) is integral over \(B\), and it belongs to the invariant fraction field \(L\). Normality of \(B\) forces it to lie in \(B\). Therefore \(R^{\langle\sigma\rangle}=B\), not merely a subring or a normalization.

**3. Full Jacobian singular scheme.** Inside \(B\), the Jacobian ideal is
\[
J=(tD^2,\ zD^2,\ z^2,\ t^2).
\]
The defining relation supplies an explicit certificate for \(D^2\in J\):
\[
D^2=F+z^2U+t^2V+z(tD^2)\quad\text{in }P
\]
(where all signs are plus in characteristic \(2\)). Therefore \(J=(D^2,z^2,t^2)\). After quotienting by this ideal the defining equation \(F\) vanishes identically, giving
\[
B/J\simeq k[U,V,z,t,D]/(z^2,t^2,D^2).
\]
The monomials \(z^at^bD^c\) for \(a,b,c\in\{0,1\}\) are a free \(k[U,V]\)-basis, proving rank \(8\) and the reduced support as asserted.

**4. Obstruction to linearization.** The fixed-point scheme of \(\sigma\) on \(\mathbb A^4\) has ideal
\[
(\sigma(x)-x,\ \sigma(y)-y)=(t\Delta,z\Delta).
\]
Its reduced support is the irreducible determinant quadric \(\Delta=xz+yt=0\): indeed \((z,t)\) contains \(\Delta\), so the only minimal prime is \((\Delta)\). This three-dimensional quadric cone is singular at the origin, as all four partial derivatives of \(\Delta\) vanish there. In contrast, the reduced fixed locus of any linear involution of affine space is a linear subspace, hence smooth. Polynomial conjugation induces an isomorphism on reduced fixed loci, preserving smoothness. This contradiction proves that \(\sigma\) is not polynomially linearizable.

Independently, the computed singular quotient provides a second obstruction in this particular situation: a nonidentity linear involution with a codimension-one fixed locus is a rank-one transvection in characteristic \(2\), and its invariant ring is polynomial, whereas \(B\) is singular.

## Verification

A standalone standard-library Python checker, `verify.py`, performs all needed characteristic-two polynomial substitutions with sparse monomials. It checks \(\sigma(\Delta)=\Delta\), \(\sigma^2=\mathrm{id}\), invariance of \(U,V\), relation (1), the five displayed partial derivatives, and the displayed algebraic identity exhibiting \(D^2\in J\). It also exhaustively checks the sixteen \(\mathbb F_2\)-rational input points: ten are fixed and the other six lie in three two-cycles. Run `python verify.py`; expected output begins `PASS: order-two action`.

The finite-field point test is a consistency check only. The infinite-field claims, ring equality, normality and non-linearizability follow from the proofs above, not from finite enumeration.

## Relationship to prior work

Miasnikov--Shestakov, arXiv:2610.11013v1, study the exact four-variable polynomial map used here and give an explicit tame factorization under the assumption that the ground field has characteristic different from \(2\). Their construction explicitly relies on inverses of \(2\) and they assert no characteristic-two conclusion. They do not determine the characteristic-two invariant ring, quotient singular scheme, or polynomial linearizability.

The work of Drensky--Yu on the Anick automorphism of a free associative algebra concerns a different algebra and wild-coordinate assertions; such results do not determine this commutative four-variable cyclic quotient. Hakuta's characteristic-two finite-field permutation-sign calculation uses the three-variable Anick/Nagata--Anick maps and does not imply the invariant-ring presentation above. Existing general methods for finite modular group invariant rings motivate the calculation but do not, by themselves, supply this explicit singular scheme or linearization obstruction.

## Limitations

No statement is made about whether this characteristic-two polynomial involution is tame, stably tame, or generates an algebraically nontrivial finite subgroup scheme; a reduced abstract cyclic group of order \(2\) is all that is used. The computation is over an algebraically closed characteristic-two field; the polynomial identities are valid over every field of characteristic two, but all geometric singularity and fixed-locus statements here are stated over \(k\). Non-linearizability does not follow merely from positive-characteristic wildness of the group action. Complete coverage of unpublished or unindexed invariant-theory computations has not been established.

## References

1. A. Miasnikov and I. Shestakov, *An explicit tame factorization of the four-variable Anick automorphism*, arXiv:2610.11013v1 (first publicly posted October 7, 2026), https://arxiv.org/html/2610.11013v1.
2. V. Drensky and J.-T. Yu, *Automorphisms fixing a variable of \(K\langle x,y,z\rangle\)*, arXiv:math/0406207 (2004), https://arxiv.org/abs/math/0406207.
3. K. Hakuta, *Sign of Permutations Induced by Anick and Nagata-Anick Automorphisms over Finite Fields*, Journal of Mathematics Research 9(4) (2017), 23--29, DOI:10.5539/jmr.v9n4p23.
4. The Stacks Project, *Serre's criterion for normality*, standard \(R_1+S_2\) criterion for Noetherian domains.
