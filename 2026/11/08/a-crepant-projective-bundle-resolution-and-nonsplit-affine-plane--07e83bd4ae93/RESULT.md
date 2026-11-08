# A crepant resolution with a nonsplit affine-plane torsor for the characteristic-two conic discriminant

## Finding
Let \(k\) be any field of characteristic two. In \(\mathbb P^5_k\), use homogeneous coordinates \([a:b:c:d:e:f]\), corresponding to the ternary quadratic
\[
q(x,y,z)=ax^2+by^2+cz^2+dyz+ezx+fxy.
\]
The universal discriminant hypersurface, its singular plane, and the polar parameter plane are
\[
D=V(ad^2+be^2+cf^2+def),\qquad L=V(d,e,f),\qquad B=\mathbb P^2_{[D:E:F]}.
\]
Define bundles on \(B\) by
\[
\begin{split}
K_0&=\ker\left(\mathcal O_B^{\oplus3}\xrightarrow{(D^2,E^2,F^2)}\mathcal O_B(2)\right),\\
K&=\ker\left(\mathcal O_B^{\oplus3}\oplus\mathcal O_B(-1)
\xrightarrow{(D^2,E^2,F^2,DEF)}\mathcal O_B(2)\right).
\end{split}
\]
Both maps are surjective. The principal claims, valid over every field of characteristic two, are:

1. The hypersurface \(D\) is geometrically integral and normal; its blowup along \(L\) is the **smooth crepant resolution**
\[
\pi:\widetilde D=\operatorname{Bl}_L(D)\overset{\sim}{\longrightarrow}\mathbb P_B(K),
\qquad K_{\widetilde D}=\pi^*K_D.
\]
2. Its exceptional divisor is \(\mathbb P_B(K_0)\). It is smooth over \(k\), a \(\mathbb P^1\)-bundle over \(B\), but over a geometric point of \(L\) its fiber is a nonreduced double line.
3. The morphism \(U=D\setminus L\to B\), with \([a:b:c:d:e:f]\mapsto[d:e:f]\), is a Zariski-locally trivial \(\mathbb A^2\)-torsor under \(K_0(1)\). **It has no global section**. Its class generates the one-dimensional space \(H^1(B,K_0(1))\cong k\).
4. Writing \(\mathbb L=[\mathbb A^1_k]\), the Grothendieck class and finite-field point counts are
\[
[D]=(1+\mathbb L+\mathbb L^2)(1+\mathbb L^2),
\qquad \#D(\mathbb F_q)=(q^2+q+1)(q^2+1)
\quad(q\text{ an even prime power}).
\]
Equivalently the zeta function is
\[
Z(D/\mathbb F_q,T)=
\frac{1}{(1-T)(1-qT)(1-q^2T)^2(1-q^3T)(1-q^4T)}.
\]

## Assumptions and scope
The base is any field \(k\) of characteristic two; no perfection assumption is needed. Projectivizations parametrize **lines** in vector bundles. The class \([D]\) is computed in the Grothendieck ring of finite-type \(k\)-varieties, where the scissor relation applies. The affine bundle assertion is about the indicated morphism to \(B\), not an abstract isomorphism with the product \(B\times\mathbb A^2\). The crepant formula is an equality of canonical line bundles since the hypersurface is Gorenstein. The coefficient \(DEF\) is a cubic section on \(B\), not the discriminant equation itself.

## Proof
**1. Discriminant and normality.** The polar bilinear form of \(q\) has alternating matrix with kernel vector \((d,e,f)\) whenever \((d,e,f)\neq0\). Evaluating \(q(d,e,f)\) in characteristic two gives \(ad^2+be^2+cf^2+def\), hence the equation of the singular-conic locus. Its partial derivatives are precisely
\[
(d^2,e^2,f^2,ef,df,de)=(d,e,f)^2.
\]
Thus the singular support is exactly \(L\), of codimension two in the fourfold \(D\). The defining cubic is geometrically irreducible: it is primitive and linear in \(a,b,c\), with no nonconstant common divisor of its coefficients \(d^2,e^2,f^2,def\), and the same argument survives every field extension. The hypersurface is Cohen–Macaulay (\(S_2\)) and regular outside \(L\) (\(R_1\)), so it is geometrically normal.

**2. Blowup and smoothness.** The graph of \([d:e:f]\) is \(\operatorname{Bl}_L\mathbb P^5\). It is the projectivization over \(B\) of \(\mathcal O_B^{\oplus3}\oplus\mathcal O_B(-1)\): a line has first three coefficients \((a,b,c)\) and remaining vector \(t(D,E,F)\). Substitution into the discriminant gives
\[
\Delta=t^2(aD^2+bE^2+cF^2+tDEF).
\]
Removing the exceptional factor \(t^2\), the proper transform is the relative hyperplane \(\mathbb P_B(K)\). Because \(D^2,E^2,F^2\) have no simultaneous zero on \(B\), \(K\) is locally free of rank three, and its projectivization is smooth. Equivalently, in the standard \(D\neq0\) chart with \((d,e,f)=(t,tu,tv)\), the strict transform has equation
\[
a+bu^2+cv^2+tuv=0,
\]
which is smooth by its coefficient of \(a\); the other two charts are analogous. The blowup is an isomorphism away from \(L\), hence is a resolution.

The center \(L\) has codimension three in smooth \(\mathbb P^5\), while \(D\) has multiplicity two along \(L\). With \(H\) the pulled-back hyperplane and \(E\) the ambient exceptional divisor,
\[
K_{\operatorname{Bl}_L\mathbb P^5}=-6H+2E,
\quad\widetilde D\sim3H-2E,
\quad K_{\widetilde D}=(-6H+2E+3H-2E)|_{\widetilde D}=-3H|_{\widetilde D}.
\]
Since \(K_D=\mathcal O_D(-3)\), the resolution is crepant.

**3. Exceptional divisor.** Setting \(t=0\) gives \(\mathbb P_B(K_0)\). The bundle \(K_0\) has rank two, so this is smooth and \(\mathbb P^1\)-fibered over \(B\). Its image in \(L\) is the incidence hypersurface
\[
E=\{([a:b:c],[D:E:F]):aD^2+bE^2+cF^2=0\}\subset L\times B.
\]
Over an algebraic closure of the residue field of \([a:b:c]\), that quadratic equation is \((\sqrt a D+\sqrt b E+\sqrt c F)^2=0\), a double line. This does not contradict smoothness of the total space: the morphism \(E\to L\) is not smooth.

**4. The nonsplit torsor.** Projection to the final summand gives a short exact sequence
\[
0\to K_0\to K\to\mathcal O_B(-1)\to0.
\]
The open complement \(\mathbb P(K)\setminus\mathbb P(K_0)=U\) parametrizes splittings \(\mathcal O_B(-1)\to K\). Such splittings are affine over the vector bundle
\[
\operatorname{Hom}(\mathcal O_B(-1),K_0)=K_0(1).
\]
Local splitting exists because this is a short exact sequence of vector bundles. A **global** section of \(U\to B\) would split the sequence globally, and conversely.

The Frobenius pullback of the Euler sequence identifies \(K_0=F_B^*(\Omega^1_B(1))\). Twisting its defining sequence by \(\mathcal O_B(1)\) gives
\[
0\to K_0(1)\to\mathcal O_B(1)^{\oplus3}
\xrightarrow{(D^2,E^2,F^2)}\mathcal O_B(3)\to0.
\]
On global sections, the image consists of the nine degree-three monomials other than \(DEF\): they are exactly the cubic monomials divisible by one of \(D^2,E^2,F^2\). Since \(H^1(B,\mathcal O_B(1))=0\),
\[
H^1(B,K_0(1))\cong H^0(B,\mathcal O_B(3))
/\bigl(D^2,E^2,F^2\bigr)H^0(B,\mathcal O_B(1))
\cong k\cdot[DEF].
\]
The extension class of \(K\to\mathcal O_B(-1)\) is precisely the connecting image of \(DEF\) (the additional term in its defining map). It is nonzero and generates this cohomology group. Hence \(U\to B\) is a genuinely **nonsplit** \(\mathbb A^2\)-torsor; in particular it has no section and is not the trivial affine-plane bundle over \(B\).

**5. Grothendieck class and arithmetic.** A vector-bundle torsor is Zariski locally trivial, so \([U]=\mathbb L^2[B]\). The closed complement is \(L\cong\mathbb P^2\), hence
\[
[D]=[U]+[L]=\mathbb L^2[\mathbb P^2]+[\mathbb P^2]
=(1+\mathbb L+\mathbb L^2)(1+\mathbb L^2).
\]
Every \(\mathbb F_{q^n}\)-rational fiber of the torsor has exactly \(q^{2n}\) points by elementary linear algebra over that field, and \(\#\mathbb P^2(\mathbb F_{q^n})=1+q^n+q^{2n}\). This proves the counting and zeta formulas.

## Verification
The included script `verify.py` performs exact characteristic-two substitutions on the three blowup charts, checks the derivatives and polar-kernel identity, verifies that the Frobenius–Euler multiplication map has rank nine and cokernel generated by \(DEF\), and exhaustively enumerates \(D(\mathbb F_q)\) and \(E(\mathbb F_q)\) for \(q=2,4,8\). Its recorded stdout appears as `verification_output.txt`; these finite tests corroborate but do not replace the general bundle and cohomology proof.

## Relationship to prior work
The universal characteristic-two conic discriminant equation, its geometric integrality/normality, and its singular-support calculation already appear in Tanaka's *Discriminant divisors for conic bundles* (2023, §3 and Proposition 5.4). Auel–Bigazzi–Böhning–Graf von Bothmer (2018, §2) explicitly study the same smooth incidence of geometrically double-line conics as an independent example; no novelty is asserted for that incidence alone. Totaro (2006) develops the corresponding geometry of quasilinear quadrics. The present statement instead combines a **crepant blowup of the universal discriminant**, a **specific nonzero Frobenius–Euler extension class producing a nonsplit affine-plane torsor**, and its motivic and arithmetic consequences. Relevant accessible primary material and mathematical records did not reveal this joint assertion. Historical priority is provisional, not certified.

## Limitations
The result is specific to ternary quadrics in characteristic two. It does not assert universal novelty of the classical discriminant equation, normality, or the incidence \(E\). The resolution is crepant, but no uniqueness or minimal-model classification is asserted. The torsor is nontrivial **as a bundle over the stated base**; no claim about absolute abstract product decomposition is made. The exact point-count verification is finite, while the arbitrary-field theorem rests on the symbolic and cohomological argument. Independent specialist validation and a complete historical-priority certification have not been performed.

## References
- B. Totaro, *Birational geometry of quadrics in characteristic 2*, arXiv:math/0608098v1, public August 3, 2006; §1–3.
- A. Auel, A. Bigazzi, C. Böhning, H.-C. Graf von Bothmer, *Unramified Brauer groups of conic bundle threefolds in characteristic two*, arXiv:1806.02668v1, public June 7, 2018; §2 and §4.
- H. Tanaka, *Discriminant divisors for conic bundles*, arXiv:2308.08119v1, public August 16, 2023; §3 and Proposition 5.4.
