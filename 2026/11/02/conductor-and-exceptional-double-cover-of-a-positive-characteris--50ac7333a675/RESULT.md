# Conductor and exceptional double cover of a positive-characteristic Nash blowup of \(A\)-type surfaces

## Finding
Let \(k\) be an algebraically closed field of prime characteristic \(p\), let \(m\ge1\) be an integer with \(p\mid 2m\), and put
\[
X_m=\operatorname{Spec}k[x,y,z]/(xy-z^{2m}).
\]
The **ordinary (not normalized) Nash blowup** \(B_m\to X_m\) is nonnormal along its complete exceptional reduced curve \(E\simeq\mathbf P^1_k\). Its normalization \(\nu:\widetilde B_m\to B_m\) has two affine charts
\[
\widetilde U_x=\operatorname{Spec}k[x,z,w]/(xw-z^m),\qquad
\widetilde U_y=\operatorname{Spec}k[y,z,w']/(yw'-z^m),
\]
glued by \(w'=w^{-1}\) when \(w\ne0\). Thus \(\widetilde B_m\) has two singularities of type \(A_{m-1}\) when \(m>1\), and is smooth when \(m=1\). (Here \(A_0\) means smooth.)

On the two charts of \(B_m\), the conductor ideals are respectively
\[
\mathfrak c_x=(x,z^m),\qquad \mathfrak c_y=(y,z^m),
\]
and their extensions to the normalization are the principal ideals \((x)\) and \((y)\). The conductor subscheme is a multiplicity-\(m\) thickening of the reduced exceptional curve on both sides (reduced when \(m=1\)). On that reduced curve, the normalization restricts to the degree-two morphism
\[
\widetilde E\simeq\mathbf P^1_k\longrightarrow E\simeq\mathbf P^1_k,
\qquad [u:v]\longmapsto[u^2:v^2].
\]
Consequently, this exceptional conductor cover is **purely inseparable of degree two precisely in characteristic two**. If \(p\ne2\) (necessarily \(p\mid m\)), it is separable of degree two, ramified at two points.

## Assumptions and scope
The claim covers every integer \(m\ge1\) and every algebraically closed field \(k\) of characteristic \(p>0\) dividing \(2m\). It is about the ordinary Nash blowup and its finite normalization, not higher Nash blowups or all possible positive-characteristic surface singularities. The conductor is defined as \(\mathfrak c=\operatorname{Ann}_{\mathcal O_B}(\nu_*\mathcal O_{\widetilde B}/\mathcal O_B)\), equivalently the largest common ideal in the two structure sheaves.

## Proof
**1. Nash ideal and actual blowup charts.** The hypersurface \(xy-z^{2m}\) is normal and has only one singular point, the origin. Its partial derivatives are \(y,x,-2mz^{2m-1}\). Since \(p\mid 2m\), the Jacobian ideal is \((x,y)\). For a hypersurface the ordinary Nash blowup equals the blowup of this Jacobian ideal. Write \(t=y/x\) on the \(x\)-chart and \(s=x/y\) on the \(y\)-chart. Then
\[
U_x=\operatorname{Spec}R_x,\quad R_x=k[x,z,t]/(x^2t-z^{2m}),
\quad U_y=\operatorname{Spec}R_y,\quad R_y=k[y,z,s]/(y^2s-z^{2m}).
\]
These formulas are actual domains: the indicated defining binomials are primitive and irreducible in the corresponding polynomial rings. On their overlap, \(s=t^{-1}\). The inverse image of the origin is \(E\simeq\mathbf P^1\), with charts \(k[t]\) and \(k[s]\).

**2. Normalizations.** In the fraction field of \(R_x\) set \(w=z^m/x\). It satisfies the monic equation \(w^2=t\) and the relation \(xw=z^m\); hence
\[
R_x\subset S_x=k[x,z,w]/(xw-z^m),\qquad t\mapsto w^2.
\]
The extension is finite because \(S_x=R_x+R_xw\). It is birational by the displayed fraction-field formula. The ring \(S_x\) is normal: it is a two-dimensional hypersurface (therefore Cohen--Macaulay) whose singular locus is empty for \(m=1\), and is at most the isolated origin for \(m>1\), even when \(p\mid m\). Serre's \(R_1+S_2\) criterion applies. Thus \(S_x\) is the integral closure of \(R_x\). The identical argument gives \(S_y\) with \(w'=z^m/y\) and \(s=(w')^2\). On the overlap, \(ww'=z^{2m}/(xy)=1\), giving the asserted gluing and two \(A_{m-1}\) chart singularities. Their two singular points are distinct since \(w=0\) and \(w'=0\) are disjoint endpoints of \(\widetilde E\).

**3. The conductor is exact.** Because \(xw=z^m\), every element of \(xS_x\) belongs to \(R_x\); as an ideal of \(R_x\),
\[
xS_x=x(R_x+R_xw)=(x,z^m)R_x.
\]
Conversely, reduce \(R_x\subset S_x\) modulo \(xS_x\). The image of \(R_x\) is precisely \(k[z,w^2]/(z^m)\) inside \(S_x/(x)=k[z,w]/(z^m)\). The latter is free of rank two over the former with basis \(1,w\). Therefore an element in the subring whose product with \(w\) also belongs to the subring must vanish; the conductor of this quotient inclusion is zero. Pulling back gives \(\mathfrak c_{S_x/R_x}=xS_x\), or \((x,z^m)\) in \(R_x\). Repeat for the \(y\)-chart. In particular, the conductor cuts out \(k[z,t]/(z^m)\) on the raw chart and \(k[z,w]/(z^m)\) on the normalized chart. The reduced support is the entire exceptional curve; for \(m>1\) the nilpotent transverse coordinate has nilpotency order \(m\).

**4. Exceptional map and inseparability.** Reducing the normalization morphism modulo the exceptional fibre gives \(t=w^2\) on one chart and \(s=(w')^2\) on the other. Since \(w'=w^{-1}\), these glue to \([u:v]\mapsto[u^2:v^2]\) on \(\mathbf P^1\). Its function-field extension \(k(w)/k(w^2)\) has degree two; the derivative of \(w^2\) vanishes exactly in characteristic two. In characteristic two it is radicial and purely inseparable; otherwise it is separable with ramification at zero and infinity. As the conductor supports all of \(E\), the Nash blowup is nowhere normal along \(E\).

## Verification
The standalone standard-library program `verify_conductor.py` embeds both affine chart rings into \(k[u,v]\) using \(x=u^m\), \(z=uv\), \(t=v^{2m}\), and \(w=v^m\), and compares their affine semigroups and the proposed conductor on a finite exponent box for every \(1\le m\le16\). It outputs `NASH_CONDUCTOR_SEMIGROUP_16_CASES_OK`. This is an independent finite consistency check of the displayed formulas, not a proof for arbitrary \(m\); the proof for all \(m\) is in Steps 1--4.

## Relationship to prior work
Duarte, Jeffries and Núñez-Betancourt establish the prime-characteristic toric logarithmic-Jacobian description of Nash blowups and characteristic independence of **normalized** Nash fans in dimension two. The result here concerns the scheme structure and conductor of the **unnormalized** blowup in a natural \(A\)-type family, including a characteristic-two purely inseparable exceptional cover. Atanasov, Lopez, Perry, Proudfoot and Thaddeus study normalized toric Nash blowups and surface resolution; their general framework does not explicitly provide the claimed conductor thickness and field-extension behavior. The specialization of the general Nash-ideal construction is used, not presented as a new theorem.

## Limitations
The exact conductor calculation depends on \(p\mid2m\). It does not classify ordinary Nash blowups for \(p\nmid2m\), nor characterize all nonnormal Nash blowups. The two normalized chart singularities and the exceptional degree-two map arise in a special, intrinsically motivated infinite family. The proof and finite checks do not establish priority over every unindexed historical computation. Independent external mathematical audit has not been performed.

## References
1. D. Duarte, J. Jeffries, L. Núñez-Betancourt, *Nash blowups of toric varieties in prime characteristic*, arXiv:2208.05599 (first posted 2022-08-11); Collectanea Mathematica 75 (2024), 629--637, DOI 10.1007/s13348-023-00402-y.
2. A. Atanasov, C. Lopez, A. Perry, N. Proudfoot, M. Thaddeus, *Resolving toric varieties with Nash blow-ups*, arXiv:0910.5028 (2009); Experimental Mathematics 20 (2011), 288--303.
3. D. Duarte, *Nash modification on toric surfaces*, arXiv:1110.4346 (2011); Revista de la Real Academia de Ciencias Exactas, Físicas y Naturales Serie A 108 (2014), 153--171.
4. D. Duarte, J. Snoussi, *Nash blowups of normal toric surfaces: the case of one and two segments*, arXiv:2410.15561 (2024); Beiträge zur Algebra und Geometrie 67 (2026), 283--301. This study concerns iteration of Nash blowups; no equivalence to the explicit conductor formula is asserted on the basis of its abstract.
