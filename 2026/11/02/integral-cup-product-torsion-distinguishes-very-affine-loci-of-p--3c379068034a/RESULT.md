# Integral cup-product torsion distinguishes very affine loci of positive Hirzebruch charts

## Finding
Fix an integer \(a\geq1\) and the smooth Hirzebruch surface \(\mathbb F_a\). Give its Cox ring coordinates \(x_0,x_1,y_0,y_1\) the classes
\[
\deg x_0=\deg x_1=F,\qquad \deg y_0=S+aF,\qquad\deg y_1=S,
\]
where \(F\) is a fiber and \(S\) is the negative section. Let \(P_h(x_0,x_1)\) be homogeneous of degree \(a\), with nonnegative real coefficients and positive coefficients on \(x_0^a\) and \(x_1^a\). Define the normalized affine Cox chart
\[
U_P=V(x_0+x_1-1,\;y_0+y_1P_h(x_0,x_1)-1)\subset\mathbb A^4.
\]
This is an affine-plane positive chart for \(\mathbb F_a\). Its very affine locus is \(U_P^\circ=U_P\cap(\mathbb C^*)^4\). Put \(P(s)=P_h(1-s,s)\), and list its **distinct finite roots** \(r_1,\ldots,r_q\) with multiplicities \(m_1,\ldots,m_q\). Necessarily \(P(0)P(1)\ne0\), and \(0\le q\le a\).

**Theorem.** Integral singular cohomology is torsion-free, with
\[
H^j(U_P^\circ;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&j=0,\\
\mathbb Z^4,&j=1,\\
\mathbb Z^{q+4},&j=2,\\
0,&j\ge3.
\end{cases}
\]
Nevertheless, the intrinsic integral cup-product cokernel
\[
\mathcal Q(U_P^\circ)=H^2(U_P^\circ;\mathbb Z)\Big/\big\langle\alpha\smile\beta:\alpha,\beta\in H^1(U_P^\circ;\mathbb Z)\big\rangle
\]
has the exact structure
\[
\mathcal Q(U_P^\circ)\cong
\begin{cases}
0,&q=0,\\
\mathbb Z^{q-1}\oplus\mathbb Z/\gcd(m_1,\ldots,m_q)\mathbb Z,&q\ge1.
\end{cases}
\]
Here \(\mathbb Z/1\mathbb Z=0\). Consequently, for every fixed \(a\ge2\), the \(a\) choices
\[
P_{a,m,h}=(x_0+x_1)^{a-m}(x_0+2x_1)^m,\quad1\le m\le a,
\]
give \(a\) positive charts on the **same** \(\mathbb F_a\) whose very affine loci all have Betti numbers \((1,4,5)\), but whose integral cohomology rings are pairwise nonisomorphic: \(\mathcal Q\cong\mathbb Z/m\mathbb Z\).

## Assumptions and scope
All varieties and cohomology are over \(\mathbb C\); singular cohomology has integral coefficients. The polynomial \(P_h\) is nonzero and has the full endpoint support specified above, but its dehomogenization \(P\) need not be square-free or have degree exactly \(a\). Only its distinct finite roots and their multiplicities enter the answer. The ordinary cohomology groups are torsion-free; the possible finite group occurs **only after quotienting by the decomposable degree-two classes**. The assertion is for the very affine locus \(U_P^\circ\), not the entire projective Hirzebruch surface or all its affine charts.

The classes \(F\) and \(S+aF\) form the primitive nef generators of \(\mathbb F_a\); they form an integral basis of its Picard group, and their sum is ample. The two equations above therefore constitute the usual positive Cox normalization for the two nef sections. In particular the normalized plane is disjoint from the Cox irrelevant locus: on \(U_P\), neither \((x_0,x_1)\) nor \((y_0,y_1)\) can vanish simultaneously. The nonnegative Cox coordinates are normalized uniquely, and the corresponding quotient gives the positive chart in the sense of Calvo Cortes–Telen.

## Proof
**Step 1: the explicitly punctured affine plane.** Solving the two normalized equations gives \(x_0=1-s\), \(x_1=s\), \(y_1=t\), \(y_0=1-tP(s)\). Thus the very affine locus is the smooth connected affine surface
\[
V_P=\{(s,t)\in\mathbb C^2:s(1-s)t(1-tP(s))\ne0\}.
\]
This description already separates the geometry from the particular homogeneous expression: only the polynomial \(P(s)\) matters. Its values at \(s=0,1\) are the two positive endpoint coefficients of \(P_h\), so its roots avoid those points.

**Step 2: a principal smooth divisor in a product of punctured lines.** Let
\[
B=\mathbb C\setminus\{0,1\},\quad T=B\times\mathbb C^*,\quad D=\{(s,t)\in T:1-tP(s)=0\}.
\]
Then \(V_P=T\setminus D\). The map \(D\to B\) induced by projection is an isomorphism onto \(B\setminus\{r_1,\ldots,r_q\}\), with inverse \(s\mapsto(s,1/P(s))\). In particular \(D\) is a **smooth connected** affine curve even if \(P\) has repeated roots. It is cut out by one global regular function in \(T\); hence its divisor class, and therefore the integral cohomological Gysin pushforward of \(1\), vanishes:
\[
\iota_*(1)=c_1(\mathcal O_T(D))=0\quad\text{in }H^2(T;\mathbb Z).
\]
The spaces \(B\), \(\mathbb C^*\), and \(D\) are punctured complex lines. Their integral cohomology groups are torsion-free and concentrated in degrees zero and one. Specifically,
\[
H^1(T;\mathbb Z)=\mathbb Z^3,\quad H^2(T;\mathbb Z)=\mathbb Z^2,\quad H^1(D;\mathbb Z)=\mathbb Z^{q+2},
\]
and \(H^j(T)=0\) for \(j\ge3\), \(H^j(D)=0\) for \(j\ge2\).

**Step 3: integral Gysin and the Betti groups.** Apply the ordinary integral cohomological Gysin sequence for the smooth divisor \(\iota:D\hookrightarrow T\). The vanishing of \(\iota_*(1)\) gives two short exact sequences
\[
0\to H^1(T)\to H^1(V_P)\overset{\operatorname{res}}\longrightarrow H^0(D)\to0,
\]
\[
0\to H^2(T)\to H^2(V_P)\overset{\operatorname{res}}\longrightarrow H^1(D)\to0.
\]
The quotients are free, so these split as sequences of abelian groups. The same sequence in higher degrees gives \(H^j(V_P)=0\) for all \(j\ge3\). The ranks are \(4\) and \(q+4\), proving the claimed additive cohomology.

**Step 4: an integral basis and multiplicity-sensitive residues.** Let \(\omega_s\), \(\omega_{s-1}\), and \(\omega_t\) denote integral degree-one logarithmic classes \((2\pi i)^{-1}d\log s\), \((2\pi i)^{-1}d\log(s-1)\), and \((2\pi i)^{-1}d\log t\) on \(T\). Let
\[
\eta=(2\pi i)^{-1}d\log(1-tP(s))\quad\text{on }V_P.
\]
Its residue on \(D\) is \(1\); therefore \(\omega_s,\omega_{s-1},\omega_t,\eta\) form an integral basis of \(H^1(V_P)\). The two generators of \(H^2(T)\) are \(\omega_s\smile\omega_t\) and \(\omega_{s-1}\smile\omega_t\), so their images in \(H^2(V_P)\) are already decomposable. (The product of the two classes pulled back from \(B\) vanishes.)

The square of the logarithmic class \(\eta\) vanishes, as it is pulled back from \(H^1(\mathbb C^*;\mathbb Z)\), and the other degree-one products are products of pullbacks from \(T\). The residue/product identity for a principal smooth divisor gives, with an irrelevant common choice of sign,
\[
\operatorname{res}(\eta\smile\omega)=\iota^*\omega\quad\text{for each }\omega\in H^1(T;\mathbb Z).
\]
Choose the standard integral logarithmic basis of \(H^1(D)\) consisting of meridians about \(s=0,1,r_1,\ldots,r_q\). If their cohomology generators are \(e_0,e_1,e_{r_1},\ldots,e_{r_q}\), the restriction map has image generated by
\[
\iota^*\omega_s=e_0,\qquad\iota^*\omega_{s-1}=e_1,\qquad\iota^*\omega_t=-\sum_{i=1}^q m_i e_{r_i},
\]
because \(t|_D=1/P(s)\) and \(P(s)=c\prod_i(s-r_i)^{m_i}\) as a polynomial. Since the two classes from \(H^2(T)\) are decomposable, the quotient of \(H^2(V_P)\) by **all** cup products is exactly the quotient of \(H^1(D)\) by these three restriction classes. Modding out \(e_0,e_1\) leaves
\[
\mathbb Z^q/\mathbb Z(m_1,\ldots,m_q),
\]
which is zero for \(q=0\) and otherwise has Smith normal form \(\mathbb Z^{q-1}\oplus\mathbb Z/g\mathbb Z\) with \(g=\gcd(m_1,\ldots,m_q)\). This establishes the theorem.

**Step 5: fixed-surface separation.** For \(1\le m\le a\), let \(P_{a,m,h}\) be the homogeneous polynomial displayed above. All its homogeneous coefficients are positive; both endpoint coefficients are positive. Under \(x_0=1-s,x_1=s\), it becomes \(P(s)=(1+s)^m\). Thus \(q=1\) and the sole multiplicity is \(m\), so the Betti numbers are always \((1,4,5)\) while \(\mathcal Q(V_P)\cong\mathbb Z/m\mathbb Z\). This quotient is defined intrinsically from the graded integral cohomology ring; nonisomorphic finite cyclic groups force pairwise nonisomorphic rings. All charts are on the same \(\mathbb F_a\), as required.

## Verification
The standalone `verify.py` uses exact integer polynomial arithmetic to expand the homogeneous family, dehomogenize, reconstruct its repeated roots and multiplicities by exact rational factor division, and check the integer Smith invariant for the restriction vector. It checks every \(1\le m\le a\le 12\), two-root examples with both coprime and non-coprime multiplicities, and the constant case. Output is `VERIFY_OK`. These checks are illustrative; the proof in Steps 1–5 establishes the general statement for arbitrary \(a\) and allowed \(P_h\).

As an independent additive consistency check, stratifying the projection \(V_P\to B\) by the roots of \(P\) gives \(\chi_c(V_P)=1+q\): over \(B\setminus\{r_i\}\) each fiber is \(\mathbb C^*\setminus\{\text{one point}\}\), while at a root the fiber is \(\mathbb C^*\). The alternating Betti sum \(1-4+(q+4)=1+q\) agrees. This Euler-characteristic count alone does not recover the integral cup-product torsion.

## Relationship to prior work
Calvo Cortes and Telen, *Positive Charts of Toric Varieties* (arXiv:2602.16414, first publicly submitted 18 February 2026), construct positive charts from smooth nef subcones and study their moment maps. The paper's full accessible HTML was examined, particularly the Cox normalization and Theorem 3.9, Section 4 examples, and Section 5. The present claim concerns an invariant not computed in those statements: the **integral degree-two quotient by products of degree-one cohomology**, and its variability over a fixed toric surface.

Améndola and coauthors, *The Maximum Likelihood Degree of Toric Varieties* (arXiv:1703.02251), specifically Theorem 17 on rational normal scrolls, already give likelihood-degree/root-count results for scrolls. Thus neither the Euler characteristic \(1+q\) nor the generic critical-point count is claimed to be new here. The torsion index \(\gcd(m_1,\ldots,m_q)\) is additional integer-valued information not determined by that count.

Callegaro, D’Adderio, Delucchi, Migliorini and Pagaria, *Orlik-Solomon-type presentations for the cohomology algebra of toric arrangements* (arXiv:1806.02195), give integral cohomology-ring presentations for complements of torus-character level-set arrangements. Their ambient arrangement hypothesis is not met in general by \(1-tP(s)=0\) when \(P\) has zeros on \(B\): the graph escapes the torus over those roots and its defining function is not a torus character. The general Gysin technique is classical; the claim is the specified exact multiplicity-sensitive invariant and the family separation, not novelty of localization theory.

## Limitations
The result is confined to smooth complex Hirzebruch surfaces, the specified full-endpoint nonnegative two-section normalization, and the **very affine** Cox locus. It does not classify all positive charts, determine their entire integral cohomology ring by generators and relations, or claim a new general theorem about smooth-divisor Gysin sequences. Distinct root multiplicities may have the same gcd and produce the same displayed invariant. The result does not assert that every possible positive chart topology is realized. Historical priority remains provisional, especially for older arrangement-complement literature; the existing external results were compared by implication, but no exhaustive historical uniqueness certification is claimed. No independent mathematical audit has been performed.

## References
1. V. Calvo Cortes and S. Telen, *Positive Charts of Toric Varieties*, arXiv:2602.16414 (initial submission 2026-02-18), especially Theorem 3.9 and Sections 3 and 5. https://arxiv.org/html/2602.16414v2
2. C. Améndola, N. Bliss, I. Burke, C. R. Gibbons, M. Helmer, S. Hoşten, E. D. Nash, J. I. Rodriguez, and D. Smolkin, *The Maximum Likelihood Degree of Toric Varieties*, arXiv:1703.02251, especially Theorem 17 and rational normal scroll examples. https://arxiv.org/abs/1703.02251
3. F. Callegaro, M. D’Adderio, E. Delucchi, L. Migliorini, and R. Pagaria, *Orlik-Solomon-type presentations for the cohomology algebra of toric arrangements*, arXiv:1806.02195. https://arxiv.org/abs/1806.02195
4. Standard integral cohomological Gysin sequence, Thom isomorphism, and residue/cup-product identity for a smooth complex divisor (used in the proof in their usual topological form).
