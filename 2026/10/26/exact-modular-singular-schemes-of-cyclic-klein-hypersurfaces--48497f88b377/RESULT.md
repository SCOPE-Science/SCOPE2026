# Exact modular singular schemes of cyclic Klein hypersurfaces

## Finding
Let \(k\) be algebraically closed of characteristic \(p>0\), and let \(d\ge3\), \(m\ge3\) be integers with \(p\mid d\). Consider the coefficientwise-defined cyclic Klein hypersurface
\[
X_{d,m}=V(F_{d,m})\subset\mathbf P_k^{m-1},\qquad
F_{d,m}=\sum_{i\in\mathbf Z/m\mathbf Z}X_i^{d-1}X_{i+1}.
\]
If \(p\nmid m\), this hypersurface is smooth. If \(p\mid m\), put
\[
a_j=\frac{1-(1-d)^j}{d}\in\mathbf Z,\qquad
N=|a_m|,\qquad\nu=v_p(N).
\]
Then its **entire projective singular subscheme**, including nilpotents, is
\[
\operatorname{Sing}(X_{d,m})\simeq\operatorname{Spec}k[t]/(t^N-1),
\quad t\longmapsto[1:t^{a_1}:t^{a_2}:\cdots:t^{a_{m-1}}].
\]
Negative powers are defined because \(t^N=1\) makes \(t\) invertible. It consists of exactly \(N/p^\nu\) geometric points, with **curvilinear local singular-scheme length \(p^\nu\)** at every point. For odd \(p\), or for \(p=2\) with \(4\mid d\), one has \(\nu=v_p(m)\); for \(p=2\), \(d\equiv2\pmod4\), necessarily \(m\) even and
\[
\nu=v_2(d-2)+v_2(m)-1.
\]
The final case exhibits a characteristic-two multiplicity enhancement not determined by \(v_2(m)\) alone. Over \(\mathbf F_p\), Frobenius acts on the reduced singular points by \(t\mapsto t^p\), and their number rational over \(\mathbf F_p\) is \(\gcd(N/p^\nu,p-1)\).

For instance, \((p,d,m)=(2,4,4)\) gives five singular points of length four; \((2,6,4)\) gives thirteen of length eight; \((5,5,5)\) gives forty-one of length five; and \((3,3,9)\) gives nineteen of length nine. These numerical examples follow from the full formula, not merely finite searches.

## Assumptions and scope
The singular scheme is defined by the homogeneous ideal \((F_{d,m},\partial_{X_0}F_{d,m},\ldots,\partial_{X_{m-1}}F_{d,m})\), with the standard projective scheme structure; this is not solely the reduced singular-point set. The theorem covers every prime \(p\mid d\), arbitrary \(m\ge3\), and each algebraic closure of \(\mathbf F_p\). It concerns the specified coefficientwise integral model rather than all projectively equivalent models or a moduli stack. It does not assert a classification of completed hypersurface germs, resolutions, or stable reduction.

## Proof
All indices below are read cyclically modulo \(m\). Since \(d\equiv0\pmod p\), the gradient equations in \(k\) are exactly
\[
0=\partial_{X_i}F_{d,m}=X_{i-1}^{d-1}-X_i^{d-2}X_{i+1}.
\tag{1}
\]
If any homogeneous coordinate vanishes at a geometric solution to (1), the preceding coordinate vanishes, and cyclic induction forces all coordinates to vanish. Thus the projective gradient scheme has support in the torus where every \(X_i\) is nonzero. In particular it is entirely contained in the affine chart \(X_0=1\), and every coordinate is a unit in its coordinate ring. This passage uses the support of a scheme, not merely a set-theoretic identification: the closed complement is empty, so the indicated principal opens cover the whole gradient scheme.

Write \(t=X_1\). The equation with \(i=1\) gives \(X_2=t^{-(d-2)}\). Recursively the equations with \(1\le i\le m-2\) force
\[
X_i=t^{a_i},\quad a_0=0,\ a_1=1,\quad
 a_{i+1}=(d-1)a_{i-1}-(d-2)a_i.
\]
The closed form \(a_i=(1-(1-d)^i)/d\) solves this recurrence, with every \(a_i\in\mathbf Z\). The final two gradient equations, for \(i=m-1\) and \(i=0\), become respectively
\[
t^{-a_m}=1,\qquad t^{(d-1)a_{m-1}-1}=t^{-a_m}=1,
\]
where \(a_m+(d-1)a_{m-1}=1\). Every elimination step uses multiplication by a coordinate known to be a unit, so these equations establish an **isomorphism of coordinate rings**, not only a bijection of geometric points:
\[
\mathcal O(\operatorname{Grad}(F_{d,m}))
 \cong k[t,t^{-1}]/(t^{a_m}-1)
 \cong k[t]/(t^N-1).
\tag{2}
\]
Multiplying each equation (1) by \(X_i\) shows that all cyclic monomials \(T_i=X_i^{d-1}X_{i+1}\) agree on the entire gradient scheme. Thus \(F_{d,m}=mT_0\) there. Since \(T_0\) is a unit, imposing \(F_{d,m}=0\) makes the scheme empty if \(p\nmid m\), and imposes no further equation if \(p\mid m\). This proves both the smoothness boundary and the claimed exact singular-scheme presentation.

Write \(N=p^\nu N_0\) with \(p\nmid N_0\). In characteristic \(p\), \(t^N-1=(t^{N_0}-1)^{p^\nu}\). The polynomial \(t^{N_0}-1\) has \(N_0\) simple distinct roots over \(k\). By the Chinese remainder theorem, each completed local singular-scheme algebra is \(k[[u]]/(u^{p^\nu})\), proving the claimed count, lengths, and curvilinearity. Geometric Frobenius raises a root to its \(p\)-th power; an \(\mathbf F_p\)-rational root is a common root of \(t^{N_0}-1\) and \(t^{p-1}-1\), yielding \(\gcd(N_0,p-1)\).

Finally, \(a_m=(1-(1-d)^m)/d\). For odd \(p\mid d\), the standard lifting-the-exponent identity gives \(v_p((1-d)^m-1)=v_p(d)+v_p(m)\), hence \(\nu=v_p(m)\). For \(p=2\) with \(4\mid d\), the same conclusion holds because \(1-d\equiv1\pmod4\). If \(p=2\) and \(d\equiv2\pmod4\), then \(m\) is even and the even-exponent identity gives
\[
v_2((1-d)^m-1)=v_2(d)+v_2(d-2)+v_2(m)-1.
\]
Subtracting \(v_2(d)=1\) proves the additional formula. All cases are exhaustive.

## Verification
A standalone integer-arithmetic verifier, `verify.py`, checks the exponent recurrence, both closure relations, equality of cyclic monomial exponents, all gradient relations modulo \(N\), valuation formulas, and support counts for eleven representative parameter triples. It returns `VERIFY_OK`. Separately, direct characteristic-\(p\) lexicographic Gröbner calculations of the affine gradient-plus-equation ideals yielded bases with last equations \(t^3-1\) at \((3,3,3)\), \(t^{20}-1\) at \((2,4,4)\), and \(t^{104}-1\) at \((2,6,4)\). These finite calculations are supplementary to, not substitutes for, the universal ring-isomorphism proof (2).

## Relationship to prior work
The classical cyclic Klein hypersurfaces and their characteristic-zero smoothness appear in González-Aguilera and Liendo, *On the order of an automorphism of a smooth hypersurface*, arXiv:1102.3443, Example 3.4. Their argument analyzes the gradient monomials for smooth hypersurfaces but does not supply the positive-characteristic scheme-theoretic singular classification when the characteristic divides both degree and coordinate count. Their earlier cubic hypersurface work arXiv:1002.4136 likewise addresses smooth geometry. More recent work on twisted forms, arXiv:2608.13896, concerns **smooth** Klein models in positive characteristic, not the singular schemes of the exceptional coefficientwise fibres. Individual lower-dimensional bad-reduction computations do not imply the complete bivariate formula or the characteristic-two valuation enhancement.

## Limitations
This statement is limited to primes dividing the degree, and does not classify the other bad-prime cases. The local algebra computed is the **singular subscheme**, not necessarily the complete local ring of the hypersurface. The full text of the 2026 smooth-model study was not available for a comprehensive negative overlap conclusion; an equivalent calculation in further specialized literature remains a novelty risk.

## References
1. V. González-Aguilera and A. Liendo, *On the order of an automorphism of a smooth hypersurface*, arXiv:1102.3443 (first posted 2011-02-16), especially Example 3.4 and its proof. https://arxiv.org/abs/1102.3443
2. V. González-Aguilera and A. Liendo, *Automorphisms of prime order of smooth cubic n-folds*, arXiv:1002.4136 (2010). https://arxiv.org/abs/1002.4136
3. A. Liendo and M. Vásquez, *Twisted forms of classical hypersurfaces*, arXiv:2608.13896 (2026); scope comparison from abstract only. https://arxiv.org/abs/2608.13896
