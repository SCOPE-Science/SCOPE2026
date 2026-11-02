# Exact two-rank in a sparse characteristic-two dihedral Kummer family

## Finding
Let \(K\) be an algebraically closed field of characteristic \(2\). For each integer \(h\geq1\), set \(M=4^h+1\), and let \(C_h\) be the smooth projective curve with function field
\[
K(C_h)=K(x,y),\qquad y^3=x^M+x^{-M}.
\]
Then
\[
\boxed{g(C_h)=4^h+1,\qquad \gamma_2(C_h)=2^{h+1},}
\]
where \(\gamma_2\) is the two-rank (the dimension of \(\operatorname{Jac}(C_h)[2](K)\) over \(\mathbf F_2\)). Thus the two-rank is positive and unbounded but its ratio to genus tends to zero. The two-rank equals four for the genus-five member, eight for the genus-seventeen member, and sixteen for the genus-sixty-five member.

## Assumptions and scope
The ground field is algebraically closed of characteristic two; \(h\) is any positive integer. All curves are considered through their nonsingular projective models. Since \(M\) is odd, \(M\equiv2\pmod3\), and \(\gcd(3,M)=1\), the original Kummer cover is separable. This result does not assert a Newton polygon or supersingularity, and makes no claim for other values of \(M\) or other covering exponents.

## Proof
**1. A three-point cyclic cover and genus.** Put \(t=x^M\), \(w=xty\), and \(N=3M\). In characteristic two, \(x^M+x^{-M}=(t+1)^2/t\); therefore
\[
w^N=t^r(t+1)^s,\qquad r=2M+3,\quad s=2M.
\]
The commuting order-\(M\) and order-three actions scaling \(x\) and \(y\) have coprime orders, and \(w\) transforms by a faithful character of their product. Hence this equation presents the full degree-\(N\) cyclic cover over \(K(t)\), rather than a proper subfield. The greatest common divisors are
\[
\gcd(N,r)=\gcd(N,r+s)=1,\qquad \gcd(N,s)=M.
\]
Its ramification indices at \(t=0,1,\infty\) are thus \(N,3,N\), with no other branch points. Tame Riemann--Hurwitz gives
\[
2g-2=-2N+(N-1)+(N-M)+(N-1)=N-M-2,
\]
so \(g=M\).

**2. A complete eigenbasis of differentials.** For each \(1\leq i<N\), define
\[
a_i=\left\lfloor\frac{ir}{N}\right\rfloor,\quad b_i=\left\lfloor\frac{is}{N}\right\rfloor,\quad
\alpha_i=\left\{\frac{ir}{N}\right\},\quad\beta_i=\left\{\frac{is}{N}\right\},
\]
and let \(H=\{i:\alpha_i+\beta_i>1\}\). For \(i\in H\), the differential
\[
\omega_i=\frac{t^{a_i}(t+1)^{b_i}}{w^i}\,dt
\]
is holomorphic. Indeed, at \(t=0\) its valuation is \(N-1-(ir\bmod N)\); at every point over \(t=1\) it is \(2+3\lfloor2i/3\rfloor-2i\), which is either \(0\), \(1\), or \(2\); and at infinity it is \(N(\alpha_i+\beta_i-1)-1\), which is nonnegative exactly when \(i\in H\). These valuations also show that no differential of this displayed form with \(i\notin H\) is holomorphic. The cover's cyclic action makes the nonzero \(\omega_i\) eigenvectors with distinct characters. Their number is \(M\): this follows directly by counting the fractional-part inequalities, or by the sum of eigenspace dimensions in the three-branch tame-cover formula. Hence they constitute a basis of the genus-\(M\) space \(H^0(C_h,\Omega^1)\).

For completeness, the fractional-part count can be verified without an appeal to the tame-cover formula. For \(i\not\equiv0\pmod3\) and \(u=(i\bmod M)/M\in(0,1)\), the membership intervals are \(H:\ u\in(0,1/3)\cup(2/3,1)\) when \(i\equiv1\pmod3\), and \(H:\ u\in(1/3,2/3)\) when \(i\equiv2\pmod3\). In addition, the single index \(i=2M\) belongs to \(H\), while no multiple of three does. Since \(M=3v+2\), the two outer intervals contain \(2v\) admissible residues and the central interval contains \(v+1\); together with the special index this gives \(2v+(v+1)+1=3v+2=M\).

**3. Cartier is a partial permutation.** Given \(i\in H\), let \(j\in\{1,\ldots,N-1\}\) be uniquely determined by \(2j\equiv i\pmod N\). Define
\[
e_r=\left\lfloor 2\left\{\frac{jr}{N}\right\}\right\rfloor,\qquad
e_s=\left\lfloor 2\left\{\frac{js}{N}\right\}\right\rfloor.
\]
Both are zero or one, and direct cancellation using \(w^N=t^r(t+1)^s\) gives the exact identity
\[
\omega_i=\left(\frac{t^{a_j}(t+1)^{b_j}}{w^j}\right)^2t^{e_r}(t+1)^{e_s}\,dt.
\]
The Cartier identities in characteristic two are \(\mathcal C(dt)=0\) and
\(\mathcal C(t\,dt)=\mathcal C((t+1)\,dt)=\mathcal C(t(t+1)\,dt)=dt\). If \(j\in H\), at least one of \(e_r,e_s\) is one. Conversely, if \(i\in H\) but \(j\notin H\), both are zero; otherwise the doubled fractional parts would have sum at most one. Consequently
\[
\mathcal C(\omega_i)=\begin{cases}\omega_j,&j\in H,\\0,&j\notin H.\end{cases}
\]
The stable image of this semilinear partial permutation consists exactly of the indices whose complete doubling orbits modulo \(N\) stay inside \(H\). By the Cartier--Manin/Hasse--Witt characterization, the stable image dimension is the two-rank.

**4. Reduction to a two-symbol expansion map.** No stable index is divisible by three. Neither is any stable index divisible by \(M\): of the two nonzero multiples of \(M\), the one in \(H\) is sent by doubling to the other, outside \(H\). For \(i\equiv1\pmod3\), let \(u=(i\bmod M)/M\), with \(0<u<1\). Elementary fractional-part calculations give
\[
i,2i\in H\quad\Longleftrightarrow\quad
u\in J:=\left(\frac16,\frac13\right)\cup\left(\frac23,\frac56\right).
\]
Each second doubling changes \(u\) to \(f(u)=\{4u\}\). Thus the stable indices of residue one correspond to \(u=q/M\) whose complete forward \(f\)-orbit lies in \(J\). The reflection \(R(u)=1-u\) preserves \(J\), and because \(4^h\equiv-1\pmod M\), one has \(f^h(q/M)=R(q/M)\). Therefore it suffices to test the first \(h\) iterates.

**5. Exact binary-itinerary count.** Write \(J_0=(1/6,1/3)\) and \(J_1=(2/3,5/6)\). For every ordered pair \((a,b)\in\{0,1\}^2\), the map \(f(u)=\{4u\}\) admits exactly one inverse branch from \(J_b\) into \(J_a\), affine of slope \(1/4\), and it maps closed intervals into the corresponding closed intervals. Fix an arbitrary binary word \((s_0,\ldots,s_{h-1})\), and append \(s_h=1-s_0\). Composing its \(h\) inverse branches gives a contraction \(B:\overline{J}_{s_h}\to\overline{J}_{s_0}\) with slope \(4^{-h}\). Because reflection sends \(\overline{J}_{s_0}\) onto \(\overline{J}_{s_h}\), the contraction \(B\circ R\) has exactly one fixed point \(u\in\overline{J}_{s_0}\). This point satisfies \(f^h(u)=1-u\), hence \((4^h+1)u\) is an integer. It cannot be an endpoint of either interval: the endpoints have denominator three or six, while \(\gcd(M,6)=1\). Thus \(u=q/M\) lies in the interiors, realizes precisely that itinerary, and survives all iterations by reflection symmetry. Different binary words give different points. Conversely every surviving \(q/M\) has one such word. Hence there are exactly \(2^h\) stable indices of residue one modulo three. Multiplication by two bijects the stable residue-one and residue-two sets. The stable Cartier rank is therefore \(2\cdot2^h=2^{h+1}\), as claimed.

## Verification
The standalone `verify.py` uses exact modular arithmetic to enumerate both the Cartier-stable character orbits and the finite-interval itineraries for \(1\leq h\leq8\) (genus through \(65,537\)). It verifies the two independent counts coincide with \(2^{h+1}\). As an independent small-instance check, the program counts points over \(\mathbf F_{2^r}\) for \(1\leq r\leq5\) on the genus-five member, recovers its zeta numerator through degree five, and obtains the polynomial coefficients \((1,0,2,0,7,0)\), of degree four modulo two. The program prints `VERIFY_OK`. Only the preceding proof covers every \(h\).

## Relationship to prior work
Timpanella (2026, Proposition 4.6) introduced the relevant dihedral Kummer family and proved the upper bound \(\gamma_2(C_{k,M})\leq g-(k-1)/2\) and the parity relation for its two-rank. His Example 4.7 treats \((k,M)=(3,5)\) and states only \(\gamma_2\leq4\). The result here gives an exact exponentially growing rank for the infinite arithmetic subfamily \(M=4^h+1\). The broad Shimura--Taniyama method for three-point cyclic covers is reviewed by Li--Mantovan--Pries--Tang (2018), and its orbit-based Newton-slope formula supplies independent conceptual context. The new arithmetic component is the exact binary-itinerary enumeration uniformly for all \(h\), not the general method for computing a Newton polygon of a given three-point cover. Priority relative to other older exact cyclic-cover calculations is not established by the available comparisons.

## Limitations
The result computes only the two-rank, not the complete Newton polygon or Ekedahl--Oort type. It is specific to the characteristic-two family with exponent three and the sparse arithmetic sequence \(M=4^h+1\). Finite verifier tests do not prove the unbounded parameter statement. Independent mathematical validation has not been performed.

## References
1. Marco Timpanella, *Large cyclic automorphism groups and cyclic subgroups of index two in characteristic two* (first publicly posted 2026-09-28), arXiv:2609.34709, especially Theorem 1.2, Proposition 4.6 and Example 4.7. https://arxiv.org/abs/2609.34709
2. Wanlin Li, Elena Mantovan, Rachel Pries and Yunqing Tang, *Newton polygons of cyclic covers of the projective line branched at three points* (2018), arXiv:1805.04598, Sections 2--3. https://arxiv.org/abs/1805.04598
3. Standard Cartier--Manin/Hasse--Witt interpretation of the two-rank; the explicit differential calculation above is self-contained.
