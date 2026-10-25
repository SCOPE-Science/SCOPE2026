# Illumination rigidity of right regular bipyramids and an asymmetric counterexample

## Finding
Let \(n\ge3\) be an integer, \(h>0\), and
\[
v_k=(\cos(2\pi k/n),\sin(2\pi k/n),0),\quad 0\le k<n.
\]
Define the right regular bipyramid
\[
B_{n,h}=\operatorname{conv}\bigl(\{v_0,\ldots,v_{n-1}\}\cup\{(0,0,h),(0,0,-h)\}\bigr)
\]
and put \(m=\lfloor(n-1)/2\rfloor\). For ordinary directional illumination \(I\) and Naszódi's finite weighted fractional illumination \(I^*\),
\[
\boxed{I(B_{n,h})=2+\lceil n/m\rceil=\begin{cases}6,&n=4,\\5,&n\ne4,\end{cases}\qquad I^*(B_{n,h})=2+n/m.}
\]
These formulas are independent of \(h\). In every *optimal* fractional illumination, the total weights illuminating the upper and lower poles each equal one, no pole-illuminating direction illuminates an equatorial vertex, and every direction illuminating an equatorial vertex with positive weight illuminates exactly \(m\) consecutive equatorial vertices. Grouping these latter directions by their cyclic \(m\)-vertex blocks, the masses are uniquely \(1/m\) on all \(n\) blocks unless \(n\equiv2\pmod4\). In the latter case, writing the alternating block masses as \(a,b\), the complete optimal aggregate family is
\[
\boxed{a,b\ge0,\qquad a+b=2/m.}
\]

The symmetric-height condition is substantive, not merely a choice of coordinates. Let
\[
C=\operatorname{conv}\bigl(\{v_k:0\le k<5\}\cup\{(0,0,1),(0,0,-3)\}\bigr).
\]
Then, for this **unequal-height pentagonal bipyramid**, which has the same face-incidence pattern as \(B_{5,h}\),
\[
\boxed{I(C)=4,\qquad I^*(C)=7/2,}
\]
whereas the equal-height pentagonal bipyramid has \(I=5\) and \(I^*=9/2\). Thus unequal heights can invalidate the exact additive separation between equatorial and pole illumination even when the combinatorial type is unchanged.

## Assumptions and scope
A direction \(u\ne0\) illuminates a boundary point \(x\) of a full-dimensional polytope \(P\) when \(x+tu\in\operatorname{int}P\) for some \(t>0\). A finite family of such directions illuminates \(P\) when every boundary point receives at least one direction. Fractional illumination assigns finitely many nonnegative weights, with total illuminating weight at least one at every boundary point; \(I^*(P)\) is the infimum of the sum of weights. The units of \(u\) do not matter.

For a polytope described by inequalities \(f_j(x)\le b_j\), a direction illuminates a vertex exactly when \(f_j(u)<0\) for every inequality active at that vertex. Illumination of all vertices suffices to illuminate every boundary point: a direction illuminating a vertex of a face satisfies all inequalities active on that face. The weighted version has the same property because a chosen vertex's illuminating directions illuminate that face point. All inequalities below are **strict**.

The symmetry in the first assertion requires the two poles to lie at equal distances above and below the regular equator. The example \(C\) deliberately violates this geometric condition. No assertion is made for an arbitrary irregular base polygon or for the full parameter space of unequal heights.

## Proof
**Facets and exact directional conditions.** Write \(c=\cos(\pi/n)>0\), \(w_j=(\cos((2j+1)\pi/n),\sin((2j+1)\pi/n))\), and split \(u=(s,z)\in\mathbb R^2\times\mathbb R\). The \(2n\) triangular facets of the equal-height bipyramid are precisely
\[
\langle w_j,x\rangle+c z/h\le c,\qquad
\langle w_j,x\rangle-c z/h\le c,\qquad 0\le j<n.
\]
The upper pole has all \(n\) upper inequalities active, the lower pole all \(n\) lower inequalities active, and equatorial vertex \(v_k\) has the upper and lower inequalities indexed by \(k-1,k\) active (indices modulo \(n\)). Thus the upper pole is illuminated precisely when
\[
\langle w_j,s\rangle+c z/h<0\quad\text{for every }j,
\]
and the corresponding lower condition replaces \(z\) by \(-z\). Equatorial \(v_k\) is illuminated precisely when
\[
\langle w_{k-1},s\rangle<-c|z|/h\quad\text{and}\quad
\langle w_k,s\rangle<-c|z|/h.
\]

**Pole/equator separation.** Every unit planar direction is within angle \(\pi/n\) of some \(w_j\); hence \(\max_j\langle w_j,s\rangle\ge c\|s\|_2\). To illuminate the upper pole it is necessary that \(-z/h>\|s\|_2\), and the lower pole requires \(z/h>\|s\|_2\). These two pole conditions cannot occur for the same direction. On the other hand, \((w_{k-1}+w_k)/2=c(\cos(2\pi k/n),\sin(2\pi k/n))\); averaging the two strict equatorial inequalities gives \(-c\|s\|_2\le c\langle v_k,s\rangle<-c|z|/h\). Thus illumination of any equatorial vertex forces \(|z|/h<\|s\|_2\), excluding illumination of either pole. This separation is the nontrivial three-dimensional step.

**Equatorial capacity and witnesses.** The equatorial conditions imply \(\langle w_{k-1},s\rangle<0\) and \(\langle w_k,s\rangle<0\). They are precisely the conditions for the horizontal component \(s\) to illuminate vertex \(v_k\) of the regular planar \(n\)-gon. Their directional arcs have angular length \(\pi-2\pi/n\) and equally spaced centers. Therefore an open arc can contain at most
\[
m=\lfloor(n-1)/2\rfloor
\]
centers, and at most \(m\) equatorial vertices can be illuminated in one direction. Conversely, for each cyclic block \(E_j=\{j,j+1,\ldots,j+m-1\}\) one can choose a horizontal direction \(s_j\) opposite the angular midpoint of this block; the center span \((m-1)2\pi/n\) is strictly less than \(\pi-2\pi/n\), so \((s_j,0)\) illuminates all vertices of \(E_j\). This is the exact planar interval argument, independently visible in the cited planar literature.

Each pole needs its own direction, and neither pole direction can illuminate an equatorial vertex. Covering the \(n\) equatorial vertices requires at least \(\lceil n/m\rceil\) further directions. Taking consecutive blocks of length at most \(m\) covers the equator in precisely that number, and the vertical directions \((0,0,-1)\) and \((0,0,1)\) illuminate the two poles. Since \(\lceil n/m\rceil=4\) for \(n=4\) and \(3\) for every other \(n\ge3\), the ordinary formula follows.

For a weighted covering, the pole constraints contribute separate total masses at least one each. Sum the equatorial vertex constraints: every remaining direction covers at most \(m\) equatorial vertices, hence the total equatorial mass is at least \(n/m\). Put weight \(1/m\) on each of the \(n\) horizontal block directions \((s_j,0)\), and unit mass on each vertical pole direction. Each equatorial vertex belongs to exactly \(m\) cyclic blocks; this construction has mass exactly \(2+n/m\). This proves the fractional identity.

**Rigidity of fractional optimizers.** If the total mass equals \(2+n/m\), equality in the pole and summed-equator lower bounds forces pole-illuminating weight one per pole, exactly unit illumination weight at each equatorial vertex, and all positive-weight equatorial directions to cover the maximum \(m\) equatorial vertices. Every maximal angular set is a cyclic block \(E_j\). If \(x_j\ge0\) is the aggregate mass of directions illuminating exactly \(E_j\), each equatorial vertex gives the equality
\[
\sum_{r=0}^{m-1}x_{k-r}=1\qquad(k\in\mathbb Z/n\mathbb Z).
\]
Subtracting consecutive equations yields \(x_k=x_{k-m}\). The number of residue classes is \(g=\gcd(n,m)\). For odd \(n=2m+1\), \(g=1\); for even \(n=2m+2\), \(g=\gcd(m,2)\), so \(g=2\) exactly when \(n\equiv2\pmod4\). If \(g=1\), all \(x_j=1/m\). For \(g=2\), the values alternate \(a,b\), every block sum has \(m/2\) terms of each type, and therefore \(a+b=2/m\). These conditions are also sufficient and attainable using the horizontal directions. The positions of atoms *within* one angular cell, and distributions among pole-illuminating directions, need not be unique.

**Exact asymmetric witness.** Now take the five equally spaced equatorial vertices and pole heights \(1\) and \(-3\). The facets are
\[
\langle w_j,x\rangle+c z\le c,\qquad
\langle w_j,x\rangle-c z/3\le c,
\]
where \(c=\cos(\pi/5)=(1+\sqrt5)/4\). Put \(a=\cos(2\pi/5)=(\sqrt5-1)/4\). Consider the five directions
\[
U_j=(-w_j,-11/10),\qquad 0\le j<5.
\]
At the upper pole their largest active facet value is \(c-(11/10)c<0\), since \(\max_i\langle w_i,-w_j\rangle=c\). At each of the two equatorial vertices \(v_j,v_{j+1}\), the largest active upper facet value is negative and the largest lower value is \(-a+(11/30)c\), which is negative because
\[
30a>11c\quad\Longleftrightarrow\quad19\sqrt5>41
\]
(the latter follows upon squaring positive sides, since \(1805>1681\)). Thus \(U_j\) illuminates the upper pole and the equatorial pair \(v_j,v_{j+1}\). Using \(U_0,U_2,U_4\) and the vertical direction \((0,0,1)\) illuminates all seven vertices of \(C\), proving \(I(C)\le4\).

To prove both lower bounds, observe that any direction illuminating the lower pole must have \(z>3\|s\|_2\), using the normal-net maximum as above. But a direction illuminating an equatorial vertex must satisfy \(z<\|s\|_2\), by averaging its two *upper* facet inequalities. Therefore **no direction illuminating the lower pole can illuminate an equatorial vertex**. Every direction can illuminate at most two equatorial vertices, since those conditions imply the planar regular pentagon illumination conditions. A finite fractional illumination therefore needs mass at least one devoted to the lower pole, and at least \(5/2\) disjoint mass to equatorial vertices: \(I^*(C)\ge7/2\). A four-direction ordinary illumination follows from the same lower bound by integrality: \(I(C)\ge\lceil7/2\rceil=4\). Finally, assign weight \(1/2\) to each \(U_j\), and weight one to \((0,0,1)\). Every equatorial vertex is hit by two of the \(U_j\), the upper pole by all five, and the lower pole by the vertical direction, proving \(I^*(C)=7/2\).

All vertex-covering constructions illuminate entire boundaries by the vertex-to-face observation in the scope paragraph. This completes the proof.

## Verification
Run `python3 verify.py` with Python's standard library. The checker independently enumerates exact integer angular sign cells for \(3\le n\le140\), verifies the maximum-block sets and cyclic weighted certificate, solves finite set-cover instances for \(3\le n\le12\), and tests 394,632 strict facet incidences for \(3\le n\le60\) and three equal-height values. It separately checks the asymmetric witness against all ten facet inequalities, and checks the radical strict inequality by exact integer squares. The observed execution output is recorded in `VERIFICATION.md`.

The sweeps and finite set-cover computations are corroboration only. All assertions for every integer \(n\ge3\), every real \(h>0\), and every weighted measure follow from the preceding proof, not from extrapolated computations. The unequal-height classification is established **only** for the explicitly stated pentagonal witness.

## Relationship to prior work
Naszódi introduced fractional illumination and proved general bounds, including a lower bound of \(5/2\) for the planar regular pentagon. Sriamorn's 2023 Theorem 1.8 determines the ordinary multiple-illumination numbers for planar regular polygons; those planar facts are not claimed as new. Gorodzha's September 2026 theorem gives the general fractional bound and its equality cases; it does not compute bipyramid values. Previously available calculations for polygons with equispaced or antipodally paired normal fans similarly supply planar ingredients, not a three-dimensional pole/equator separation theorem.

An existing additivity theorem for \(\ell_1\)-sums of **normed balls** covers centrally symmetric planar bases and therefore the even-\(n\) subfamily here. Its hypotheses fail for the odd-\(n\) regular polygons (and the unequal-height example is not a symmetric norm ball). The new geometric statement is the precise separation for *odd* regular bipolar suspensions, its all-optimal-measures classification and the explicit height-asymmetry obstruction. Odd-\(n\) formulas and the asymmetric example are not logical corollaries of the cited planar or symmetric-norm results. The exact occurrence of analogous statements under alternative terminology remains a priority risk.

## Limitations
The theorem does not determine illumination for arbitrary unequal-height regular bipyramids, nonregular ring polygons or arbitrary pyramidal joins. The optimizer classification concerns aggregate direction cells, not arbitrary individual directional atoms. The finite verifier is not a machine proof of the infinite family; the analytic facet and cyclic-block arguments bear that burden. Historical priority is provisional pending independent literature review; no independent scientific validation is represented.

## References
1. M. Naszódi, *Fractional illumination of convex bodies*, Contributions to Discrete Mathematics **4** (2009), 83–88, DOI: 10.55016/ojs/cdm.v4i2.62022.
2. K. Sriamorn, *On the multiple illumination numbers of convex bodies*, arXiv:2306.13517, first public 2023-06-23, especially Theorem 1.8 and Section 3.3.
3. Y. Gorodzha, *Fractional illumination and the optimal exponential rate in Hadwiger's covering conjecture*, arXiv:2609.23913, first public 2026-09-20, Theorem 1.
4. *Exact fractional illumination of every equiangular polygon*, published-finding corpus public finding (2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-fractional-illumination-of-every-equiangular-polygon--035cb636082a.
5. *Exact multiple illumination and parity rigidity for polygons with antipodal edge-normal fans*, published-finding corpus public finding (2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-multiple-illumination-and-parity-rigidity-for-polygons-wit--f4e6962728dc.
