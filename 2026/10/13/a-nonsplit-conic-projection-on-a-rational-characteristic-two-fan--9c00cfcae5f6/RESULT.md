# A nonsplit conic projection on a rational characteristic-two Fano threefold
## Finding
Let \(k\) be an algebraically closed field of characteristic \(2\). Consider the smooth bidegree-\((1,2)\) hypersurface
\[
X=\big\{s(x^2+yz)+ty^2+uz^2=0\big\}\subset
\mathbb P^2_{[s:t:u]}\times\mathbb P^2_{[x:y:z]}.
\]
Denote its two projections by \(\pi\) (onto \([s:t:u]\)) and \(\rho\) (onto \([x:y:z]\)). The defining threefold and its triple-line discriminant were given in Tanaka's Example 7.5; those facts are not claimed as new.

**Theorem (two projection structures and nonsplitting).** The projection \(\rho\) is the projectivization of the rank-two bundle \(h^*\Omega^1_{\mathbb P^2}(1)\) for
\[
h:\mathbb P^2\longrightarrow\mathbb P^2,
\quad [x:y:z]\longmapsto[x^2+yz:y^2:z^2],
\]
a finite purely inseparable morphism of degree \(4\). Thus \(X\) is rational. By contrast, the generically smooth conic bundle \(\pi\) has **no rational section**. On the dense affine chart \(s\ne0\), set \(a=t/s\), \(b=u/s\). Its smooth conic
\[
C:\quad x^2+ay^2+bz^2+yz=0
\quad\text{over}\quad K=k(a,b)
\]
represents the **nonzero order-two Brauer class** \(\beta=[ab,b)\in\operatorname{Br}(K)\); it extends to a nontrivial class on \(\mathbb A^2_{a,b}\), where all fibers are smooth. Both \(K(\sqrt a)\) and the separable quadratic field \(K(\theta)\), with \(\theta^2+\theta=ab\), split \(C\). They have the least possible nontrivial extension degree \(2\). The known scheme-theoretic discriminant of \(\pi\) is \(3\{s=0\}\).

## Assumptions and scope
All assertions are over an arbitrary algebraically closed base field \(k\) of characteristic \(2\), including non-algebraic closures of finite fields. Here a rational section means a rational map from the base \(\mathbb P^2_{[s:t:u]}\) to \(X\) right-inverse to \(\pi\), equivalently a \(K\)-point of its generic conic. Write \([c,d)\) for the characteristic-two quaternion algebra with generators \(i,j\) satisfying \(i^2+i=c\), \(j^2=d\), and \(ji=(i+1)j\), or its Brauer class. The pullback of \(\Omega^1(1)\) is from the **target** of \(h\). Projectivization parametrizes one-dimensional subspaces of fibers.

## Proof
**1. Smooth Fano threefold.** Let \(A=x^2+yz\), \(B=y^2\), \(C=z^2\). These three homogeneous quadrics have no common geometric zero: \(B=C=0\) forces \(y=z=0\), and then \(A=x^2\ne0\) on \(\mathbb P^2\). The three partial derivatives of the defining equation with respect to \(s,t,u\) are \(A,B,C\), so the Jacobian criterion makes \(X\) smooth. By adjunction, \(K_X=\mathcal O_X(-2,-1)\), so \(-K_X=\mathcal O_X(2,1)\) is ample. Thus \(X\) is Fano, as in the originating source.

**2. The split projection and its inseparable map.** Since the quadrics have no common zero, \(h=[A:B:C]\) is everywhere defined and \(h^*\mathcal O(1)=\mathcal O(2)\). It is finite because the pullback of the target's ample hyperplane line bundle is ample; its degree is \((2H)^2=4\). In the chart \(z=1\), with \(r=x/z\), \(w=y/z\), the image function coordinates are \(P=r^2+w\), \(Q=w^2\). Consequently \(w^2=Q\) and \(r^4=P^2+Q\), showing that the degree-four function-field extension is purely inseparable. The Euler sequence, pulled back along \(h\), is
\[
0\to E:=h^*\Omega^1_{\mathbb P^2}(1)
\to\mathcal O_{\mathbb P^2}^{\oplus3}
\xrightarrow{(A,B,C)}\mathcal O_{\mathbb P^2}(2)\to0.
\]
At every point \([x:y:z]\), the fiber of \(\rho\) is the line of coefficient vectors \([s:t:u]\) annihilating \((A,B,C)\), hence \(X\cong\mathbb P(E)\). Over the generic point of \(\mathbb P^2_{x,y,z}\) this bundle is \(\mathbb P^1\); therefore \(X\) is rational. For reference, \(c_1(E)=-2H\) and \(c_2(E)=4H^2\).

**3. The nonsplit conic.** On \(s=1\), the conic is \(q=x^2+ay^2+bz^2+yz=0\). Its fiberwise derivatives in \(y,z\) are respectively \(z,y\); if both vanished on a point of the conic then \(x=0\) too. Hence all fibers over \(\mathbb A^2_{a,b}\) are smooth. To prove anisotropy, let \(r=a^{-1}\) and embed \(K=k(a,b)\hookrightarrow F=k(b)((r))\), equipped with valuation ring \(R=k(b)[[r]]\). Suppose \(C(F)\ne\varnothing\). Rescale the homogeneous coordinates of an \(F\)-point so that \(x,y,z\in R\) and at least one is a unit. The equation reads
\[
x^2+r^{-1}y^2+bz^2+yz=0.
\]
If \(y\) were a unit, only \(r^{-1}y^2\) would have valuation \(-1\), impossible; therefore \(y\in rR\). Reducing the equation modulo \(r\) gives \(\bar x^2+b\bar z^2=0\) in \(k(b)\). Because \(b\notin k(b)^2\), we must have \(\bar x=\bar z=0\). Thus \(x,y,z\in rR\), contradicting normalization. Hence \(C(F)=\varnothing\), so \(C(K)=\varnothing\) and \(\pi\) has no rational section.

**4. Exact Brauer class and splitting fields.** In the equation \(q=0\) substitute \(y=bZ\) and \(z=Y\), then divide by \(b\):
\[
\frac1b x^2+Y^2+YZ+abZ^2=0.
\]
The standard reduced-norm conic of the quaternion \([c,d)\) has equation \(dX^2+Y^2+YZ+cZ^2=0\). Our conic therefore represents \([ab,1/b)=[ab,b)\), since \(1/b\) differs from \(b\) by a square. It is nonzero because the conic is anisotropic, and has order \(2\). Its restriction to the affine base defines a class in \(\operatorname{Br}(\mathbb A^2_{a,b})\): smooth conics are étale-locally projective lines, so their projective-linear transition functions define a Brauer–Severi class; its generic restriction is \(\beta\ne0\).

Over the purely inseparable quadratic extension \(K(\sqrt a)\) the point \([\sqrt a:1:0]\) belongs to \(C\). Over the separable quadratic extension \(K(\theta)\), \(\theta^2+\theta=ab\), the point \([0:\theta/a:1]\) belongs to \(C\). The latter polynomial is irreducible, since a root already in \(K\) would produce a \(K\)-point, contrary to the valuation proof. The original lack of a point makes the smallest splitting extension degree exactly \(2\). The triple-line discriminant \(3\{s=0\}\) follows from the discriminant polynomial \(s^3\), computed in the source; this fact is independent of the nonsplitting proof.

## Verification
The lack of a section uses a discrete valuation argument at \(a=\infty\), not a finite-field experiment. The coefficient identities underlying the quaternion normal form and the two explicit splitting points can be checked by direct substitution in characteristic \(2\). The map degree follows from pullback of hyperplanes, not a numerical sample. The accompanying `verify.py` checks the displayed polynomial identities in a formal polynomial algebra over \(\mathbb F_2\); it does **not** substitute for the valuation proof or assert independent validation.

## Relationship to prior work
Tanaka, *Discriminant divisors for conic bundles* (arXiv:2308.08119v1), Example 7.5, gives precisely the smooth Fano threefold and the triple-line scheme-theoretic discriminant; Example 7.3 includes the affine chart with \(\varphi=1\). Neither the rational-section obstruction nor this specific quaternion class and its splitting behavior is stated there. Auel–Bigazzi–Böhning–Graf von Bothmer (arXiv:1806.02668v2), Section 2, exhibits an **anisotropic but totally singular** fibration \(sx^2+ty^2+uz^2=0\), and their Proposition 3.11 gives the general quaternion/Brauer correspondence. The extra \(syz\) term in the present example makes the generic conic **smooth**, and the prior totally singular anisotropy statement does not itself prove nonsplitting of this altered conic. The exact opposite-projection bundle and the local valuation proof above address that new geometric question.

## Limitations
The conclusion is for this explicit characteristic-two example, not for arbitrary conic bundles or arbitrary \(\varphi\) in Tanaka's larger affine family. The Brauer class is nontrivial on the smooth affine chart, not a claimed new invariant of the rational total space. The classification makes no statement about rational points over finite fields beyond the specified splitting fields. Standard general quaternion and projective-bundle facts are used; discovery of an older implicit calculation of the same explicit class would affect originality. No independent audit has been carried out.

## References
- H. Tanaka, *Discriminant divisors for conic bundles*, arXiv:2308.08119v1 (public 2023-08-16), especially Examples 7.3 and 7.5. https://arxiv.org/abs/2308.08119v1
- A. Auel, A. Bigazzi, C. Böhning, H.-C. Graf von Bothmer, *Unramified Brauer groups of conic bundle threefolds in characteristic two*, arXiv:1806.02668v2 (2018), especially Section 2 and Proposition 3.11. https://arxiv.org/abs/1806.02668v2
