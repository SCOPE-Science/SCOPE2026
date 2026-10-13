# Projective symmetry is index four in the 285-conic graph symmetry
## Finding
For Degtyarev's unique smooth sextic K3 surface \(X_{285}\subset\mathbb P^4_{\mathbb C}\) containing 285 conics, the full projective stabilizer has order
\[
|\operatorname{Aut}_{\mathbb P^4}(X_{285})|=720.
\]
The abstract dual adjacency graph of the 285 conics has automorphism group of order \(2880\), so precisely an index-\(4\) subgroup of its graph symmetries is induced by projective automorphisms of the embedded K3 surface.

## Assumptions and scope
All varieties are over \(\mathbb C\). The surface \(X_{285}\) is the unique projective-equivalence class singled out in Degtyarev's Theorem 1.1 and equation (8.1). Let \(h\) be its degree-six polarization, let \(N=\operatorname{NS}(X_{285})\), and let \(T=N^\perp\subset H^2(X_{285},\mathbb Z)\). Degtyarev proves that the 285-conic graph determines \(N\), that \(O_h(N)=\operatorname{Aut}(\operatorname{Fn}_2(N,h))\), that this group has order \(2880\), and that the canonical map to the discriminant-form automorphism group is surjective. He also identifies
\[
T\cong\begin{pmatrix}6&0\\0&20\end{pmatrix}.
\]
The claim concerns automorphisms preserving the given degree-six projective model; it does not classify every abstract automorphism of the underlying unpolarized K3 surface.

## Proof
Because \(H^2(X_{285},\mathbb Z)\) is unimodular and \(N\subset H^2\) is primitive, the discriminant forms of \(N\) and \(T\) are anti-isometric. For
\[
T=\langle6\rangle\oplus\langle20\rangle,
\]
we have
\[
A_T=T^\vee/T\cong\mathbb Z/6\oplus\mathbb Z/20,
\qquad
q_T(a,b)=\frac{a^2}6+\frac{b^2}{20}\pmod{2\mathbb Z}.
\]
An exhaustive finite calculation gives
\[
|O(q_T)|=8.
\]
Indeed, the image of \((1,0)\) must be \((\pm1,0)\), while the image of \((0,1)\) can be exactly \((0,u)\) with \(u\in\{1,9,11,19}\pmod{20}\); all eight resulting maps preserve the discriminant form and are automorphisms.

Next, the only vectors of square \(6\) in \(T\) are \(\pm(1,0)\). Hence every integral isometry of \(T\) is a diagonal sign change, and
\[
O(T)\cong C_2\times C_2.
\]
For a positive-definite rank-two transcendental lattice of a singular K3 surface, the Hodge structure is determined by its orientation. Thus the Hodge isometries are the orientation-preserving subgroup
\[
O_{\mathrm{Hdg}}(T)=O^+(T)=\{I,-I\},
\]
whose image in \(O(q_T)\) has order \(2\).

Degtyarev proves that
\[
O_h(N)\longrightarrow O(q_N)
\]
is surjective and that \(|O_h(N)|=2880\). Therefore its kernel has order \(2880/8=360\). By the primitive-gluing criterion, an isometry of \(N\) fixing \(h\) extends to a Hodge isometry of the K3 lattice exactly when its discriminant action matches that of a Hodge isometry of \(T\). Consequently the Hodge-compatible inverse image has order
\[
360\cdot2=720.
\]
Such an isometry preserves the ample class \(h\), hence the Kähler chamber, so global Torelli realizes it by an automorphism of \(X_{285}\). Conversely every projective automorphism preserves \(h\). Since the embedding is the complete linear system of \(h\), polarized automorphisms are exactly projective stabilizers. This proves the claim.

## Verification
The accompanying `verify.py` enumerates all 120 elements of \(A_T\), all possible images of the two standard generators, and every discriminant-form automorphism. It returns exactly eight automorphisms of \(q_T\), verifies that \(O^+(T)=\{\pm I\}\), and checks the numerical consequence \(2880/8\cdot2=720\) and index \(4\).

## Relationship to prior work
Degtyarev proves the extremal classification, gives \(|\operatorname{Aut}(\operatorname{Fn}_2(N,h))|=2880\), identifies \(T=[6,0,20]\), and proves surjectivity to the discriminant-form automorphism group. The source does not state the order of the projective stabilizer of \(X_{285}\). The calculation above supplies the missing Hodge/gluing filter and shows that the combinatorial symmetry group is four times larger than the geometric projective symmetry group. Later work on conics on K3 surfaces uses different extremal constructions and does not provide this stabilizer count.

## Limitations
The result determines the order and the exact index inside the conic-graph symmetry group, but does not identify the abstract isomorphism type of the order-\(720\) projective group or its orbit structure on the 285 conics. It also does not address the full automorphism group of \(X_{285}\) after forgetting the polarization.

## References
1. A. Degtyarev, *Conics in sextic K3-surfaces in \(\mathbb P^4\)*, arXiv:2010.07412v1 (2020), revised v2 (2021); Nagoya Math. J. 246 (2022), 273–304, doi:10.1017/nmj.2021.3.
2. V. V. Nikulin, *Integral symmetric bilinear forms and some of their applications*, Math. USSR Izv. 14 (1980), 103–167.
3. B. Saint-Donat, *Projective models of K3 surfaces*, Amer. J. Math. 96 (1974), 602–639.
