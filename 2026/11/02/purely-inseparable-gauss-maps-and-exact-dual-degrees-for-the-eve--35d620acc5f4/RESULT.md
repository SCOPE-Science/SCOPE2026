# Purely inseparable Gauss maps and exact dual degrees for the even Ma–Wang maximal curves

## Finding
Let \(q=p^e>2\), let \(n\ge4\) be even, and put \(s=q^n\), \(N=s+1\) and \(r=(q^{n-1}-1)/(q-1)\). Over an algebraic closure \(k\) of \(\mathbb F_{q^{2n}}\), choose \(c\in k^\times\) with \(c^s=-c\). Let \(C\) be the normalization of the degree-\(N\) plane curve
\[
 Z^N=c\,(U^q-U)\bigl(1+(U^q-U)^{q-1}\bigr)^r.
\]
Its projective model has precisely \(q^2-q\) singularities, all geometrically unibranch cusps analytically equivalent to \(Y^N=X^r\). The Gauss map \(\gamma:C\to C^\vee\) has purely inseparable degree exactly \(q\), its image function field is \(k(C)^q\), and its dual curve has degree
\[
\boxed{\deg C^\vee=q(q^n+1).}
\]
Thus the normalization of the dual is the \(q\)-Frobenius twist of \(C\). This statement concerns the specified plane model, not all projective embeddings of the abstract curve.

## Assumptions and scope
All geometric assertions are over the algebraically closed field \(k\) of characteristic \(p\). For brevity put \(A=U^q-U\), \(B=1+A^{q-1}=(U^{q^2}-U)/(U^q-U)\), \(h=AB=U^{q^2}-U\), and \(f=AB^r\). The displayed plane equation is interpreted as its degree-\(N\) homogenization \(Z^N=cV f^h(U,V)\) in \(\mathbb P^2\); its function field is \(K=k(u,z)\). The quantity \(r\) is coprime to \(N\) when \(n\) is even, and \(N\) is prime to \(p\). The curve is irreducible because \(f\) has zeros of order one at the \(q\) elements of \(\mathbb F_q\), so it cannot be a nontrivial power in \(k(u)\).

## Proof
**1. Derivative and tangent coordinates.** In characteristic \(p\), one has \(r\equiv N\equiv1\pmod p\), \(A'=-1\), and \(B'=A^{q-2}\), including the case of nonprime \(q\). Therefore
\[
f'=A'B^r+rAB^{r-1}B'=B^{r-1}(-B+A^{q-1})=-B^{r-1}.
\]
Differentiating \(z^N=cf(u)\), substituting the defining equation, and using \(N=1\) in \(k\) gives \(dz/du=-z/h\) on the smooth dense affine locus. Consequently the tangent-line coefficients in the \((u,z)\)-plane give the rational Gauss map
\[
\gamma(u,z)=[1:h(u)/z:-u^{q^2}],
\]
since \(u+h(u)=u^{q^2}\). This formula extends to a morphism from the smooth projective normalization \(C\), by removal of indeterminacies on a smooth complete curve.

**2. Exact inseparability degree.** Set \(t=(r-1)/q=1+q+\cdots+q^{n-3}\) and define \(w=c^{-1/q}z^{q^{n-1}}/B^t\). The defining relation yields
\[
h/z=c^{-1}z^{q^n}/B^{r-1}=w^q.
\]
The coprimality \(\gcd(q^{n-1},N)=1\), together with \(z^N\in k(u)\), implies \(K=k(u,w)\). Since \(t\equiv1\pmod p\), differentiation gives
\[
\frac{dw}{w}=-t\frac{B'(u)}{B(u)}\,du.
\]
The extension \(K/k(u)\) is separable, and \(B'\ne0\); thus \(dw\ne0\). Because \(k\) is perfect and \(K\) has transcendence degree one, \([K:K^q]=q\), and any element with nonzero differential, in particular \(w\), generates \(K\) over \(K^q\). Therefore
\[
K=K^q(w)=k(u^q,w),\qquad
k(C^\vee)=k(u^{q^2},w^q)=K^q.
\]
The Gauss-map extension \(K/k(C^\vee)\) is consequently purely inseparable of degree \(q\), exactly, rather than merely divisible by the characteristic.

**3. Degree of the dual.** The normalization has a unique point \(P_\infty\) over infinity, with \(\operatorname{ord}_{P_\infty}(u)=-N\) and \(\operatorname{ord}_{P_\infty}(z)=-s\). This also follows directly from the Newton polygon at the smooth point \([1:0:0]\). Set \(\eta=h(u)/z\). At a branch point over a root of \(A\), its order is \(N-1\); at a root of \(B\), its order is \(N-r\); elsewhere in the affine chart it has no poles. At infinity its pole order is \(Nq^2-s\), strictly smaller than the pole order \(Nq^2\) of \(u^{q^2}\). Hence the Gauss coordinates \(1,\eta,u^{q^2}\) define a base-point-free linear series of degree \(Nq^2\), with only the infinity point supporting the poles. A general line in the dual plane therefore has \(Nq^2\) preimages counted with multiplicity on \(C\). Since the Gauss morphism has degree \(q\), the image curve satisfies \(q\deg C^\vee=Nq^2\), proving \(\deg C^\vee=qN\).

**4. Complete singularity classification.** The polynomial \(f\) has degree \(s=N-1\). In the homogenized equation, the partial derivative with respect to \(V\) at \([1:0:0]\) is \(-c\), so infinity is smooth. At a finite point the partial derivative with respect to \(z\) is \(z^{N-1}\), hence singular points must have \(z=0\). There \(f'(u)=-B(u)^{r-1}\), so a point is singular exactly when \(B(u)=0\). The roots are the \(q^2-q\) elements of \(\mathbb F_{q^2}\setminus\mathbb F_q\), each simple because \(B'=A^{q-2}\ne0\) at such roots. Near each such point \(f(u)=(u-\alpha)^r g(u)\), where \(g(\alpha)\ne0\); taking a formal \(N\)-th root of the unit transforms the local equation to \(Y^N=X^r\). The equality \(\gcd(r,N)=1\) (as \(r\equiv1\pmod{q+1}\) and \(N=q(q-1)r+q+1\)) makes these branches unibranch. There are no other singularities. As a consistency check, the total delta-invariant \((q^2-q)(N-1)(r-1)/2\) subtracts from the plane arithmetic genus \((N-1)(N-2)/2\) to give the source genus \((q^2-1)q^n/2\).

## Verification
The accompanying `check_gauss.py` uses only Python standard-library integer modular arithmetic. It expands the polynomial derivative identity in the relevant prime characteristics, checks the exact congruences and coprimalities, verifies the cusp delta/genus equality, and calculates the stated dual degrees for sample prime powers and even exponents. Run `python3 check_gauss.py`; the terminal success line is `VERIFY_OK`. The program checks instances only; the symbolic arguments above establish the universal quantifiers.

## Relationship to prior work
Ma and Wang, *A new family of maximal curves not covered by the Hermitian curve*, arXiv:2609.19546 (initial public submission 2026-09-17), introduce this even-exponent Kummer family and determine its genus, maximality and a large automorphism subgroup. The present calculation addresses a different invariant of their specific plane model: the exact inseparability degree of its Gauss map and the dual degree, as well as all plane cusps. Arakelian and Speziali study Gauss inseparability and Frobenius-nonclassical hypersurfaces in a general setting, without the present explicit Kummer plane model or degree calculation. General Kummer Weierstrass-semigroup results concern pole semigroups, not this Gauss-map extension. A nearby mathematical-research record on the Ma–Wang family determines the normalizer of its Kummer automorphisms; automorphism normalizers do not imply the Gauss map or dual degree. These comparisons do not establish exhaustive historical priority.

## Limitations
The formula concerns \(q>2\), even \(n\ge4\), and the specific plane model; the parity hypothesis is essential to the root-valuation and cusp analysis given here. It does not describe the singularities of the dual curve, higher conormal schemes, other embeddings, or the complete automorphism group. The result has received self-review only, without independent validation; older literature under alternate terminology might contain overlapping calculations.

## References
1. L. Ma and Y. Wang, *A new family of maximal curves not covered by the Hermitian curve*, arXiv:2609.19546v1 (2026-09-17), https://arxiv.org/abs/2609.19546.
2. N. Arakelian and P. Speziali, *Curves on Frobenius nonclassical loci of hypersurfaces*, arXiv:2512.08874; *Mathematische Zeitschrift* 314 (2026), article 21, https://doi.org/10.1007/s00209-026-04128-y.
3. Castellanos, Mendoza, and Quoos, general Kummer Weierstrass-semigroup results (2023), https://arxiv.org/abs/2304.02128. This reference is context, not a claim of novelty for Kummer semigroups.
