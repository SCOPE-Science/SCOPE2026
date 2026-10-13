# Characteristic-dependent polar degree and inseparability of a bitangent conic pencil

## Finding

Let \(k\) be an algebraically closed field, \(m\geq 2\), and let \(a_1,\ldots,a_m\in k^\times\) be pairwise distinct. The reduced conic–line divisor
\[
C=V(F)\subset\mathbb P^2_k,\qquad F=x\prod_{i=1}^{m}(xz+a_i y^2)
\]
is the bitangent-pencil arrangement denoted \(\mathcal{CL}_2\) in the originating paper. Let \(\Phi_F=[F_x:F_y:F_z]\) be its polar (gradient) rational map. For characteristic \(p\neq2\), this map is dominant and generically finite, with **total function-field degree**, including inseparable multiplicity,
\[
[k(\mathbb P^2):\Phi_F^*k(\mathbb P^2)]=
\begin{cases}
2m-1,&p=0\ \text{or}\ (p>2,\ p\nmid m(m+1)),\\
m,&p>2,\ p\mid m,\\
m-1,&p>2,\ p\mid(m+1).
\end{cases}
\]
In characteristic two its image is a line, so the map is not dominant. When \(p>2\) divides \(m+1\), the polar map is generically separable. When \(p>2\) divides \(m\), set \(h(r)=\prod_i(r+a_i)\); then the polar map is inseparable **if and only if**
\[
2h'(r)+r h''(r)=0,
\qquad\text{equivalently}\qquad
h(r)=A(r^p)+r^{p-1}B(r^p)
\]
for polynomials \(A,B\in k[u]\). Both separable and purely inseparable polar maps of total degree \(p\) occur for \(m=p\) and every odd prime \(p\).

## Assumptions and scope

The field is algebraically closed and the coefficients are nonzero and pairwise distinct. Consequently \(h(0)\ne0\), \(\gcd(h,h')=1\), and \(h'\ne0\). The displayed degree refers to the extension of rational function fields, not to the number of *distinct* geometric points in an inseparable generic fiber. The theorem concerns the specified homogeneous polynomial and all its admissible coefficient choices. All component conics are smooth, and the underlying reduced intersection configuration does not degenerate in any characteristic: each pair of conics meets at \([1:0:0]\) and \([0:0:1]\), with local intersection multiplicity two at each; the line \(x=0\) is tangent to each conic at \([0:0:1]\).

## Proof

Write \(h(r)=\prod_{i=1}^m(r+a_i)\), and define
\[
D(r)=h(r)+rh'(r),\qquad M(r)=mh(r)-rh'(r).
\]
On the dense source chart \(x=1\), with \(y=s\ne0\) and \(z=rs^2\), direct differentiation of \(F=x\prod(xz+a_i y^2)\) gives
\[
(F_x,F_y,F_z)=s^{2m-2}\bigl(s^2D(r),\ 2sM(r),\ h'(r)\bigr).
\]
Because \(h'\ne0\), the target chart \(F_z\ne0\) is nonempty. For odd characteristic let \(U=F_x/F_z\) and \(V=F_y/F_z\). Then
\[
U=s^2D/h',\quad V=2sM/h',\quad
\frac{V^2}{4U}=\phi(r):=\frac{M^2}{h'D}.
\]
The polynomial \(M\) is not zero: when \(p\nmid m\) its constant coefficient is \(mh(0)\ne0\); when \(p\mid m\) it equals \(-rh'\ne0\). Hence \(s=Vh'/(2M)\), so
\[
k(r,s)=k(r,V),\qquad k(U,V)=k(\phi(r),V).
\]
Here \(V\) is transcendental over \(k(r)\), and the degree of the polar map is exactly the degree of the one-variable rational function \(\phi\), measured after cancelling its numerator and denominator. Nonconstancy of \(\phi\) in each case below proves dominance.

**Ordinary characteristic.** Assume characteristic zero or odd characteristic not dividing \(m(m+1)\). Both leading terms \(h'\) and \(D\) have degrees \(m-1\) and \(m\), respectively. The polynomials \(M\) and \(h'\) are coprime: a common root would satisfy \(mh=0\), contradicting \(\gcd(h,h')=1\). Similarly, \(D+M=(m+1)h\), so a common root of \(D,M\) would also be a root of \(h\); at a root of \(h\), one has \(D=rh'\ne0\) because \(h(0)\ne0\). Therefore \(\gcd(M,h'D)=1\). The denominator of \(\phi\) has degree \(2m-1\) while \(\deg M\le m-1\), giving degree \(2m-1\).

**Characteristic dividing \(m\).** Now assume odd \(p\mid m\). Then \(M=-rh'\), so after cancelling \(h'\),
\[
\phi(r)=\frac{r^2h'(r)}{D(r)}.
\]
The denominator \(D\) has degree \(m\), since its leading coefficient is \(m+1=1\) in \(k\). Moreover \(D(0)=h(0)\ne0\) and \(\gcd(D,h')=\gcd(h,h')=1\); thus the displayed quotient is reduced and has degree \(m\). Direct differentiation yields
\[
\phi'(r)=\frac{r h(r)(2h'(r)+rh''(r))}{D(r)^2}.
\]
A nonconstant rational function on the projective line in positive characteristic is separable if and only if its formal derivative is nonzero. The criterion follows. For \(h=\sum c_i r^i\), the coefficient of \(r^{i-1}\) in \(2h'+rh''\) is \(i(i+1)c_i\); this vanishes identically exactly when every nonzero \(c_i\) has \(i\equiv0\) or \(-1\pmod p\), giving the displayed decomposition in \(r^p\). The criterion is compatible with \(h\) being squarefree.

**Characteristic dividing \(m+1\).** Assume odd \(p\mid(m+1)\). Then \(m=-1\) in \(k\) and \(M=-D\); cancelling \(D\) gives
\[
\phi(r)=\frac{D(r)}{h'(r)}.
\]
The denominator has degree \(m-1\) (leading coefficient \(m=-1\ne0\)); \(\deg D\le m-1\), and \(\gcd(D,h')=1\). Hence the degree is \(m-1\). Since \(m-1\equiv-2\pmod p\) and \(p\) is odd, the total degree is prime to \(p\), forcing separability.

**Characteristic two.** Here \(F_y=0\), so the gradient image lies in the target line with middle coordinate zero. Its other coordinate ratio \(F_x/F_z=s^2D/h'\) is nonconstant because \(D(0)=h(0)\ne0\) and \(h'\ne0\). Thus the image is exactly a line, and the polar map is not dominant.

For the realizability assertion, take \(m=p\) in any odd characteristic. Both monic polynomials
\[
h_{\mathrm{sep}}(r)=r^p-r+1,\qquad
h_{\mathrm{ins}}(r)=r^p+r^{p-1}+1
\]
have nonzero constant term and are squarefree: the first has derivative \(-1\); the second has derivative \(-r^{p-2}\), whose only zero is \(r=0\), not a root. Thus each factors into distinct nonzero linear factors over \(k\), as required. For the first, \(2h'+rh''=-2\ne0\); for the second it vanishes. Both maps have total degree \(p\), so the second is purely inseparable and the first is separable.

Finally, component smoothness is checked from the gradient \((z,2a_i y,x)\) of \(xz+a_i y^2\). At the only possible points where this gradient vanishes, its defining quadratic does not vanish. For two distinct parameters, subtracting their conic equations gives \((a_i-a_j)y^2=0\), and the resulting intersections and multiplicities follow in affine charts centered at the two coordinate vertices. The line \(x=0\) meets each conic as \(a_i y^2=0\), establishing tangency uniformly.

## Verification

The accompanying self-contained Python program checks the reduced one-variable quotient \(\phi\), exact polynomial gcds and formal derivatives in several finite characteristics. Cases include \(p=3,m=2\) with degree one, both degree-\(p\) separability outcomes for \(p=3\) and \(p=5\), the ordinary case, and a further \(p=7\) dividing \(m\). Run `python3 verify.py` and require `VERIFY_OK`. These computations are examples only; the preceding polynomial identities and gcd arguments prove the universal theorem.

## Relationship to prior work

Beorchia and Miró-Roig, *Jacobian schemes of conic-line arrangements and eigenschemes* (arXiv:2303.04665), Example 3.2(4) and Section 4, give the same characteristic-zero bitangent-pencil arrangement, its freeness and its characteristic-zero polar degree \(2m-1\). Those results are prior, not new here. Bignalet-Cazalet, *Plane polar Cremona maps of arbitrarily large degree in positive characteristic* (2021), Example 2, expressly gives the special characteristic-three degree-five curve with two conics and a common tangent as homaloidal. Its birationality is also **prior**: it is the \(m=2,p=3\) case of the degree formula, not an independent new claim. That article's general theorem treats different, near-pencil **line** arrangements, and its displayed conic example does not supply the parameter-uniform degree trichotomy or the inseparability characterization proved above. The present claim is the all-parameter, all-characteristic calculation and its sharp separability boundary; literature searches cannot exclude unindexed antecedents.

## Limitations

The theorem addresses the rational gradient map rather than positive-characteristic freeness, Tjurina schemes, Hessian factorization, or the individual separable and inseparable subdegrees in every inseparable higher-degree case. Total degree in positive characteristic must not be read as the number of distinct points in the generic fiber. The original characteristic-zero family and the characteristic-three quintic homaloidal specialization are not claimed as discoveries.

## References

1. V. Beorchia and R. M. Miró-Roig, *Jacobian schemes of conic-line arrangements and eigenschemes*, arXiv:2303.04665, first version 2023-03-08, Example 3.2(4), Section 4. https://arxiv.org/html/2303.04665v2
2. R. Bignalet-Cazalet, *Plane polar Cremona maps of arbitrarily large degree in positive characteristic*, Geometriae Dedicata 214 (2021), 559–570, especially Example 2 and Theorem A. https://doi.org/10.1007/s10711-021-00628-9
3. R. Bignalet-Cazalet, *Torsion of a finite base locus*, arXiv:1806.00856, for a distinct characteristic-three homaloidal quintic and polar-map methods. https://arxiv.org/abs/1806.00856
