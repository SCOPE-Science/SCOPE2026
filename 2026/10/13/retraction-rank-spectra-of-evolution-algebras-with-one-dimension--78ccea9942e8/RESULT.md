# Retraction rank spectra of evolution algebras with one-dimensional square

## Finding

Let \(K\) be any field; let \(V\) be a \(K\)-vector space of dimension \(n\ge 2\), let \(B:V\times V\to K\) be a nondegenerate symmetric bilinear form admitting an orthogonal basis, and fix \(0\ne c\in V\). Make \(E=(V,\cdot)\) the (not necessarily associative or unital) algebra
\[
u\cdot v=B(u,v)c.
\]
Its square is \(E^2=Kc\), and it is an evolution algebra in any orthogonal basis of \(B\). **Every composition-idempotent algebra endomorphism** \(F:E\to E\), meaning \(F(uv)=F(u)F(v)\) and \(F^2=F\), is precisely one of the following: the identity; or a linear projection \(V=W\oplus H\to W\) for which \(B(W,W)=0\) and \(c\in H\). This includes the zero map when \(W=0\). Thus every proper retract has zero multiplication and is isomorphic as an algebra to the zero-product algebra \(K^r\) for some \(0\le r<n\).

For \(K=\mathbb F_q\) with odd prime-power \(q\), write \(I_r(B)\) for the number of totally \(B\)-isotropic \(r\)-subspaces (and set \(I_{-1}=0\)); set \(\tau(c)=1\) when \(B(c,c)=0\) and \(0\) otherwise. If \(c\) is isotropic, let \(B_c\) denote the induced nondegenerate symmetric form on \(c^{\perp}/Kc\), of dimension \(n-2\). Define \(\tau(c)I_{r-1}(B_c)=0\) when \(c\) is anisotropic. Then the full labeled linear-rank polynomial of composition-idempotent algebra endomorphisms is
\[
\boxed{\mathcal R_{E,q}(T)=T^n+\sum_{r=0}^{n-1}q^{r(n-r-1)}\bigl(I_r(B)-\tau(c)I_{r-1}(B_c)\bigr)T^r.}
\]
All coefficients are explicit via the isotropic-Grassmannian product formulas given below. In particular the spectrum depends on the quadratic-space type and, separately, on whether \(c\) is isotropic.

## Assumptions and scope

Endomorphisms are **\(K\)-linear algebra homomorphisms**, not merely idempotent elements of \(E\), and idempotence means under composition. Nondegeneracy means \(B(u,v)=0\) for all \(v\) implies \(u=0\). An evolution algebra admits a natural basis \(e_1,\dots,e_n\) with \(e_i e_j=0\) for \(i\ne j\); an orthogonal basis gives one here. The arbitrary-field classification holds in every characteristic, provided the stated diagonalizability holds. The count is for each **fixed labeled algebra** \((V,B,c)\) over \(\mathbb F_q\), not for isomorphism classes of evolution-algebra multiplication tables. Finite-field formulas are proved for odd \(q\), not asserted for even \(q\).

For completely explicit coefficients let \(d=\dim U\), let \(C\) be a nondegenerate symmetric form over odd \(\mathbb F_q\), and define \(\epsilon(C)=\chi((-1)^{d/2}\det C)\in\{\pm1\}\) when \(d\) is even, where \(\chi\) is the quadratic character. When \(d\) is odd, \(\epsilon(C)\) is not needed. Put
\[
N_d(C)=\begin{cases}
q^{d-1}-1,&d\ge1\text{ odd},\\
q^{d-1}-1+(q-1)\epsilon(C)q^{d/2-1},&d\ge2\text{ even}.
\end{cases}
\]
At each iterative reduction in dimension by two the sign \(\epsilon\) in even dimension remains unchanged; we therefore write \(N_{d-2j}(C)\) for the same parity and sign as \(C\). Let the Witt index \(w(C)\) be \((d-1)/2\) for odd \(d\), \(d/2\) for even \(d\) with \(\epsilon=+1\), and \(d/2-1\) for even \(d\) with \(\epsilon=-1\). For every integer \(r\), the complete formula is
\[
I_r(C)=\begin{cases}
\displaystyle\frac{q^{r(r-1)/2}\prod_{j=0}^{r-1}N_{d-2j}(C)}{\prod_{i=0}^{r-1}(q^r-q^i)},&0\le r\le w(C),\\
0,&\text{otherwise}.
\end{cases}
\]
Empty products are \(1\), so \(I_0(C)=1\), including for zero-dimensional \(C\). If \(c\) is isotropic, its quotient \(B_c\) is obtained by deleting one hyperbolic plane, so it has dimension \(n-2\), the same parity, and (if even) the same \(\epsilon\) as \(B\).

## Proof

**Step 1: the homomorphism equation.** Since \(E^2=Kc\), every algebra endomorphism has \(F(c)=\lambda c\) for a scalar \(\lambda\in K\). The homomorphism identity for arbitrary \(u,v\) is equivalent to
\[
B(Fu,Fv)=\lambda B(u,v)\qquad(\forall u,v\in V).
\]
Indeed, the two sides of \(F(uv)=F(u)F(v)\) are respectively \(\lambda B(u,v)c\) and \(B(Fu,Fv)c\), and \(c\ne0\). If additionally \(F^2=F\), then \(\lambda^2=\lambda\), hence \(\lambda=0\) or \(1\). When \(\lambda=1\), nondegeneracy forces \(F\) to be injective: if \(Fu=0\) then \(B(u,v)=0\) for every \(v\). As an injective idempotent is the identity, \(F=1_V\). When \(\lambda=0\), the homomorphism condition is \(B(FV,FV)=0\), while \(F(c)=0\). Every idempotent linear map gives a decomposition \(V=\operatorname{im}F\oplus\ker F\) and acts as the associated projection. Conversely, any projection onto a totally isotropic \(W\) with \(c\) in its kernel satisfies both identities. The zero map is the \(W=0\) case. This proves the arbitrary-field classification without a hidden division by \(2\) or positivity assumption.

**Step 2: count admissible images.** Fix \(r<n\). The image \(W\) must be a totally isotropic \(r\)-space that does **not** contain \(c\). There are \(I_r(B)\) totally isotropic \(r\)-spaces. If \(c\) is anisotropic, none contains it. If \(c\) is isotropic, those containing \(c\) are exactly the inverse images of totally isotropic \((r-1)\)-spaces of \(c^{\perp}/Kc\), because total isotropy of \(W\) forces \(W\subseteq c^{\perp}\). Hence the admissible number of \(W\)'s is \(I_r(B)-\tau(c)I_{r-1}(B_c)\). For \(r=0\) this is \(1\).

**Step 3: count projections above an image.** For an admissible \(W\), fix any complement \(H_0\) containing \(c\), possible precisely because \(c\notin W\). All other complements are uniquely graphs of \(K\)-linear maps \(\phi:H_0\to W\). The graph contains \(c\) exactly when \(\phi(c)=0\). The vector space of such maps has dimension \(r(\dim H_0-1)=r(n-r-1)\) and thus has \(q^{r(n-r-1)}\) elements. Each complement determines one projection and vice versa. The rank-\(n\) case is only the identity. Multiplying and summing establishes the displayed rank polynomial.

**Step 4: compute \(I_r(C)\) with no unsolved subspace counts.** Let \(Z_d\) be the number of isotropic vectors including zero in a nondegenerate \(d\)-dimensional quadratic space over odd \(\mathbb F_q\). Split off a hyperbolic plane with coordinate product \(xy\). For each vector \(z\) in the \((d-2)\)-dimensional orthogonal complement, there are \(2q-1\) pairs \((x,y)\) with \(xy=0\), and \(q-1\) pairs when \(xy\ne0\), giving \(Z_d=qZ_{d-2}+(q-1)q^{d-2}\). The base values are \(Z_0=Z_1=1\), \(Z_2=2q-1\) for a split plane (the two isotropic lines meet at zero), and \(Z_2=1\) for an anisotropic plane. Solving the recursion separately for the two plane types and the odd sequence gives precisely \(Z_d-1=N_d(C)\) stated above. Every nondegenerate form of dimension at least three over an odd finite field has a hyperbolic plane, so these recursions cover all cases. A totally isotropic ordered independent \(r\)-tuple can be constructed recursively. After choosing an ordered isotropic \(j\)-frame whose span has dimension \(j\), the next vector lives in its perpendicular space, not its span; modulo the span there are \(N_{d-2j}(C)\) possible nonzero isotropic classes and each lifts in \(q^j\) ways. Thus the number of ordered isotropic \(r\)-frames is \(q^{r(r-1)/2}\prod_{j=0}^{r-1}N_{d-2j}(C)\). Each \(r\)-subspace has \(\prod_{i=0}^{r-1}(q^r-q^i)\) ordered bases. Division proves the formula; Witt-index restrictions reflect that the anisotropic core contains no nonzero isotropic vectors. For isotropic \(c\), the hyperbolic reduction \(c^{\perp}/Kc\) has the stated inherited type.

**Examples and independent contrasts.** Over \(\mathbb F_3\) with \(n=3\), \(B=\operatorname{diag}(1,1,1)\), and \(c=(1,0,0)\) anisotropic, the enumerator is \(1+12T+T^3\). For \(B=\operatorname{diag}(1,1,2)\) and isotropic \(c=(1,0,1)\), it is \(1+9T+T^3\). Over \(\mathbb F_5\) with \(n=4\), \(B=\operatorname{diag}(1,1,1,4)\), the anisotropic choice \(c=(1,0,0,0)\) yields \(1+900T+300T^2+T^4\), whereas the isotropic \(c=(1,0,0,1)\) yields \(1+875T+250T^2+T^4\). Every displayed coefficient counts labeled endomorphisms, not subspaces alone.

## Verification

Run \(\texttt{python3 checker.py}\) using Python 3 with only standard-library modules. The checker independently enumerates all linear maps in seven small odd-prime-field instances, imposes the matrix conditions \(F^2=F\) and \(F(uv)=F(u)F(v)\), measures ranks, and compares each spectrum with the formula. Separately it enumerates isotropic row-reduced subspaces, excludes images containing \(c\), and compares counts in seven additional finite-field instances, up to five generators. Execution on the packaged script gives \(\texttt{VERIFY_OK}\). Exhaustion is confined to these finite samples; the unrestricted theorem follows from Steps 1–4, not from testing.

## Relationship to prior work

Brache–Martín Barquero–Martín González–Sánchez-Ortega, *Evolution algebras with one-dimensional square* (arXiv:2103.01625v1), already establishes the bilinear-form multiplication model and the structural isotropic/anisotropic distinctions for these algebras. **Neither that model nor those distinctions are claimed as new here**. The additional result concerns all composition-idempotent algebra endomorphisms and their complete finite-field rank multiplicities. Calderón Martín–Fernández Ouaridi–Kaygorodov, *Non-degenerate evolution algebras* (arXiv:2303.00862v1), studies structural decompositions, derivations and degeneration questions, rather than this retraction enumerator. Facchini–Heidari Zadeh, *Algebras with a bilinear form, and Idempotent endomorphisms* (arXiv:2210.08230v1), studies weak augmentations and splittings for **unital** algebra constructions; its idempotent maps do not subsume the present nonunital evolution-algebra classification or rank spectrum. Fernández-Ternero–Gómez-Sousa–Núñez-Valdés, DOI:10.1002/cmm4.1200, analyzes when the **fixed evolution operator** \(e_i\mapsto e_i^2\) is a homomorphism, a different question from enumerating all composition-idempotent endomorphisms. These comparisons concern theorem statements and their hypotheses, not title similarity alone.

## Limitations

The form \(B\) is nondegenerate and has an orthogonal basis; the result does not classify degenerate one-dimensional-square evolution algebras or their retracts. The arbitrary-field classification holds in all characteristics, but the explicit isotropic-count product and finite-field rank polynomial are asserted only for odd characteristic. No claim is made that this classifies the evolution algebras themselves, an achievement already present in the cited literature. Possible unlocated equivalent formulations in older algebraic-geometry or orthogonal-group literature remain a bibliographic risk.

## References

1. C. Brache, D. Martín Barquero, C. Martín González, J. Sánchez-Ortega, *Evolution algebras with one-dimensional square*, arXiv:2103.01625v1 (2021-03-02).
2. D. Fernández-Ternero, V. M. Gómez-Sousa, J. Núñez-Valdés, *Evolution algebras whose evolution operator is a homomorphism*, *Computational and Mathematical Methods* (first published 2021-09-30), DOI:10.1002/cmm4.1200.
3. A. Facchini, L. Heidari Zadeh, *Algebras with a bilinear form, and Idempotent endomorphisms*, arXiv:2210.08230v1 (2022-10-15).
4. A. J. Calderón Martín, A. Fernández Ouaridi, I. Kaygorodov, *Non-degenerate evolution algebras*, arXiv:2303.00862v1 (2023-03-01).
