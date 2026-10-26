# An explicit unramified Artin–Schreier quotient in characteristic three of the elementary-symmetric Bring curve

## Finding
Let \(k\) be an algebraically closed field of characteristic \(3\). Write \(e_j\) for the elementary symmetric polynomial of degree \(j\) in five variables \(a,b,c,u,v\). The integral elementary-symmetric Bring model has smooth characteristic-three fibre
\[
C=V(e_1,e_2,e_3)\subset \mathbb P^4_k,
\]
a geometrically integral genus-four curve. The cyclic permutation \(\sigma:(a,b,c,u,v)\mapsto(b,c,a,u,v)\) acts **freely**, giving an étale Galois quotient of degree \(3\).

Set \(A=u+v\), \(W=(a-b)(b-c)(c-a)\), and
\[
D(u,v)=-u^6+u^4v^2+u^3v^3+u^2v^4-v^6.
\]
The quotient is the explicitly presented smooth genus-two curve
\[
Y=C/\langle\sigma\rangle:\qquad W^2=D(u,v)
\]
in the weighted projective space with weights \((1,1,3)\). On the generic chart \(A\ne0\), its complete cyclic function-field extension is **the Artin–Schreier equation**
\[
\boxed{\quad z^3-z=\frac{W}{(u+v)^3},\qquad z=\frac{a-b}{u+v}.\quad}
\]
This equation represents a nonzero class in \(H^1_{\mathrm{\acute et}}(Y,\mathbb Z/3\mathbb Z)\), because the corresponding étale cover is connected. The quotient \(Y\) is ordinary: its Cartier–Manin matrix in the standard hyperelliptic basis is the identity \(2\)-by-\(2\) matrix. Consequently \(C\) is ordinary as well. The principal contribution is the **explicit characteristic-three wild étale torsor and its smooth integral-model geometry**, not the existence of the genus-two quotient in characteristic zero or the general isogeny-theoretic information on the Jacobian.

## Assumptions and scope
All assertions are for the coefficientwise reduction of the *elementary-symmetric* integral model \(V(e_1,e_2,e_3)\). In characteristic zero this agrees with the familiar power-sum Bring complete intersection after inverting \(6\). In characteristic \(3\), however, the third power-sum equation is a consequence of the first; naively reducing the three power-sum equations does **not** give the smooth model here. The rational Artin–Schreier equation describes function fields; the smooth projective model of that function field is the étale cover \(C\). Its apparent order-three poles are not claims of wild ramification.

## Proof
**1. Smoothness and connectedness.** The Jacobian rows of \(e_1,e_2,e_3\), evaluated where the three functions vanish, are
\[
(1)_{i=1}^5,\qquad (-x_i)_{i=1}^5,\qquad (x_i^2)_{i=1}^5.
\]
If their rank is below \(3\), all five coordinates are zeros of a nonzero polynomial of degree at most \(2\), so they assume at most two values. Suppose those values are \(r,s\) with multiplicities \(m,5-m\), and use symmetry to take \(m\le2\). For \(m=1\), \(e_1=0\) forces \(r=-s\), then \(e_2=-s^2\), so all coordinates vanish. For \(m=2\), \(e_1=0\) forces \(r=0\), and then \(e_3=s^3\) forces all coordinates to vanish. One-value tuples are likewise excluded by \(e_1=5r\ne0\) unless \(r=0\). Therefore the projective complete intersection is smooth. It is connected by the connectedness theorem for positive-dimensional projective complete intersections, hence geometrically integral. Adjunction on a smooth \((2,3)\) complete intersection in \(\mathbb P^3\) gives genus \(4\).

The action of \(\sigma\) has no fixed geometric projective point: in characteristic \(3\) its only possible projective eigenvalue is \(1\), so fixedness forces \(a=b=c\). Then \(e_1=0\) gives \(u+v=0\), \(e_2=0\) gives \(uv=0\), hence \(u=v=0\), while \(e_3=a^3\ne0\) for a nonzero projective point. Thus the constant cyclic group of order \(3\) acts freely, and the quotient map is finite étale of degree \(3\).

**2. The quotient equation.** The projection to \([u:v]\) has no base point: if \(u=v=0\) then \(e_1=0\) gives \(c=-a-b\), while \(e_2=0\) and \(e_3=abc=0\) force \(a=b=c=0\). As \(C\) has degree \(6\), this projection is degree \(6\). Write \(s_j\) for elementary symmetric functions in \(a,b,c\). The three equations give
\[
s_1=-A,\qquad s_2=B:=u^2+uv+v^2,\qquad s_3=-A(u^2+v^2).
\]
Thus the ordered triple \((a,b,c)\) consists of the three roots of
\[
T^3+AT^2+BT+A(u^2+v^2).
\]
Its discriminant in characteristic \(3\) is
\[
A^2B^2-B^3-A^4(u^2+v^2)=D(u,v).
\]
The Vandermonde \(W\) is invariant under the three-cycle and has \(W^2=D\); it changes sign under a transposition. The fixed field of the three-cycle is therefore \(k(u/v,W/v^3)\), of degree \(2\) over \(k(u/v)\). The polynomial \(D(T,1)=-T^6+T^4+T^3+T^2-1\) has derivative \(T^3-T\), coprime to \(D(T,1)\) since its values at \(0,1,-1\) are all nonzero. Its degree-six leading coefficient is nonzero, so \(Y\) is a smooth genus-two hyperelliptic curve.

**3. The Artin–Schreier cocycle.** Put \(z=(a-b)/A\). Directly \(\sigma(z)=(b-c)/A=z+1\), because \(a+b+c=-A\). Also \(c-a=A(z-1)\). Consequently
\[
W=(a-b)(b-c)(c-a)=A^3z(z+1)(z-1)=A^3(z^3-z),
\]
which proves the displayed Artin–Schreier equation. Its extension has degree \(3\) by the already-proved degree of \(C\to Y\); hence the Artin–Schreier class is nontrivial. Freeness proved in step 1—not an assertion about pole orders of a chosen rational representative—proves that the extension of smooth projective curves is everywhere étale.

**4. Cartier and genus.** For the degree-six hyperelliptic model \(w^2=f(t)\) in characteristic \(3\), the Cartier–Manin matrix is \((c_{3i-j})_{1\le i,j\le2}\), where \(f(t)^{(3-1)/2}=\sum c_nt^n\). Here \(c_2=c_4=1\) and \(c_1=c_5=0\), so this matrix is \(I_2\). Thus \(Y\) has \(3\)-rank \(2\). The Deuring–Shafarevich formula for the unramified cyclic \(3\)-cover gives \(\gamma(C)-1=3(\gamma(Y)-1)\), hence \(\gamma(C)=4\), equal to its genus.

## Verification
Run `python3 verify_bring3.py` with SymPy installed. The program independently recomputes the cubic discriminant and the characteristic-three Artin–Schreier polynomial identity, checks the two-value Jacobian rank-drop exclusions and absence of projection base points, verifies the squarefreeness and Cartier coefficients of the genus-two discriminant sextic, and independently counts the rational points of the five-coordinate complete intersection over \(\mathbb F_3\). It returns `VERIFY_OK`. These exact symbolic checks support, but do not replace, the general connectedness, étale-quotient, and Deuring–Shafarevich arguments above.

## Relationship to prior work
Edge (1978) studies the classical characteristic-zero Bring curve and its canonical projective model. Braden–Northover (2012) supplies a detailed plane model and period matrix but does not compute characteristic-three reduction or an Artin–Schreier torsor. Braden–Disney-Hogg (2023/2024), §4.4, **already identifies the genus-two quotient by a three-cycle over characteristic zero**, using cube-root-of-unity semi-invariants, and Proposition 4.5 determines the characteristic-zero Jacobian's rational isogeny class. Those results are not novelty claims here: the latter isogeny, together with good reduction, also gives independent information consistent with ordinarity. The present statement instead specifies the smooth elementary-symmetric special fibre and the exact free **wild characteristic-three** Artin–Schreier torsor, not obtained simply by reducing the semi-invariant formulas that divide by \(3\).

## Limitations
The statement is model-specific. The naive reduction of the power-sum ideal does not define the same curve in characteristic \(3\). The genus-two quotient in characteristic zero and isogeny-theoretic implications are known prior results. The algebraic class is given by a rational Artin–Schreier function; no integral everywhere-regular affine Artin–Schreier equation is asserted. The result does not classify the full automorphism group in characteristic \(3\), all Jacobian endomorphisms, or stable reduction of arbitrary plane models. An equivalent characteristic-three torsor calculation may exist in less readily searchable literature. Independent validation has not been performed.

## References
- W. L. Edge, "Bring's Curve", *J. London Math. Soc.* 18 (1978), 539–545, doi:10.1112/jlms/s2-18.3.539. Original model and symmetry; historical context.
- H. W. Braden and T. P. Northover, "Bring's Curve: its Period Matrix and the Vector of Riemann Constants", *SIGMA* 8 (2012), 065; published October 2, 2012; doi:10.3842/SIGMA.2012.065. Complete text available at https://www.imath.kiev.ua/~sigma/2012/065/.
- H. W. Braden and L. Disney-Hogg, "Bring's curve: old and new", *European Journal of Mathematics* 10 (2024), article 3; published online December 18, 2023; doi:10.1007/s40879-023-00706-0. See §4.4 and Proposition 4.5 for pre-existing characteristic-zero quotient and isogeny results.
