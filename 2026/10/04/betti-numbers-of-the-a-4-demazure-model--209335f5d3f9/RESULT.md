# Betti numbers of the \(A_4\) Demazure model
## Finding
Let \(Y(A_4)\) be Nicole Lemire's smooth projective four-dimensional Demazure model for the algebraic torus whose character lattice and splitting group are
\[
\bigl(\Lambda(A_4),\operatorname{Aut}(A_4)\bigr).
\]
Then the final smooth fan of \(Y(A_4)\) has exactly
\[
400
\]
rays and
\[
1920
\]
maximal cones. Hence
\[
\rho\bigl(Y(A_4)\bigr)=\operatorname{rank}\operatorname{Pic}\bigl(Y(A_4)\bigr)=396,
\qquad
\chi\bigl(Y(A_4)\bigr)=1920.
\]
Its Poincaré polynomial is
\[
P_{Y(A_4)}(t)=1+396t^2+1126t^4+396t^6+t^8.
\]
Thus the nonzero Betti numbers are
\[
(b_0,b_2,b_4,b_6,b_8)=(1,396,1126,396,1),
\]
and every odd Betti number vanishes.

## Assumptions and scope
The model \(Y(A_4)\) is exactly the smooth projective toric fourfold constructed in Proposition 7.6 and Corollary 7.7 of Lemire's arXiv:2609.30482v1. We use the standard faithful action
\[
\operatorname{Aut}(A_4)\cong S_5\times C_2
\]
on the \(A_4\) root lattice, where \(S_5\) permutes the five coordinates and the extra involution acts by negation. Hence
\[
|\operatorname{Aut}(A_4)|=240.
\]

The statement concerns the split toric Demazure model itself. It does not compute the cohomology of a quotient by a Galois splitting group, the ring structure of cohomology or Chow groups, or equivariant cohomology.

## Proof
Lemire gives six \(\operatorname{Aut}(A_4)\)-orbits of original rays represented by
\[
s_{r,t}=s_{[1,r],[r+1,r+t]},
\qquad
1\le r\le t,\quad r+t\le5,
\]
and three additional ray orbits represented by
\[
v_1=e_1+2e_2-e_3-e_4-e_5,
\]
\[
v_2=2e_1+2e_2-2e_3-e_4-e_5,
\]
\[
v_3=2e_1+3e_2-2e_3-2e_4-e_5.
\]
Immediately before Proposition 7.6, the source gives the stabilizer formula
\[
\operatorname{Stab}(s_{r,t})\cong S_r\times S_t\times S_{5-r-t}
\quad (r<t),
\]
and
\[
\operatorname{Stab}(s_{r,r})
\cong
\bigl((S_r\times S_r)\rtimes S_2\bigr)\times S_{5-2r},
\]
together with
\[
\operatorname{Stab}(v_1)\cong S_3,\qquad
\operatorname{Stab}(v_2)\cong S_2\times S_2,\qquad
\operatorname{Stab}(v_3)\cong S_2.
\]
Orbit--stabilizer therefore gives the nine ray-orbit sizes
\[
20,\ 60,\ 40,\ 10,\ 30,\ 20,\ 40,\ 60,\ 120.
\]
Their sum is
\[
20+60+40+10+30+20+40+60+120=400.
\]

For a smooth complete toric fourfold, the torus-invariant divisor sequence is
\[
0\longrightarrow M
\longrightarrow \mathbf Z^{\Sigma(1)}
\longrightarrow \operatorname{Pic}(Y(A_4))
\longrightarrow0.
\]
Here \(\operatorname{rank}M=4\) and \(|\Sigma(1)|=400\), hence
\[
\rho(Y(A_4))=400-4=396.
\]

It remains to count maximal cones. Proposition 7.6 gives eight \(\operatorname{Aut}(A_4)\)-orbits of smooth maximal cones: one from the \(F_1\) path, two obtained by subdividing the first \(F_2\) path, two from the second \(F_2\) path, and three from the third \(F_2\) path. Using the explicit primitive generators printed immediately before Proposition 7.6, one checks the stabilizer of each of these eight representative cones inside \(S_5\times C_2\). Each stabilizer is trivial. Therefore every maximal-cone orbit has \(240\) elements, so
\[
|\Sigma(4)|=8\cdot240=1920.
\]

A complete toric variety has Euler characteristic equal to the number of zero-dimensional torus orbits, equivalently the number of maximal cones. Thus
\[
\chi(Y(A_4))=1920.
\]
Because \(Y(A_4)\) is smooth and projective, its odd cohomology vanishes, its cohomology is torsion-free, and Poincaré duality gives
\[
b_0=b_8=1,\qquad b_2=b_6=\rho(Y(A_4))=396.
\]
Therefore
\[
b_4
=
1920-(1+396+396+1)
=
1126,
\]
which yields the claimed Poincaré polynomial.

## Verification
The accompanying `verify.py` encodes the nine ray representatives and all eight maximal-cone representatives directly from the formulas in Section 7.3. It enumerates all \(240\) signed coordinate permutations in \(S_5\times C_2\).

For the rays it independently checks the orbit sizes
\[
(20,60,40,10,30,20,40,60,120),
\]
their pairwise disjointness, and total \(400\). For the eight maximal-cone representatives it checks that every stabilizer has order \(1\), that the eight orbits are distinct, and hence that there are \(1920\) maximal cones. It then checks the Picard-rank and Betti-number arithmetic. The saved output ends in `VERIFY_OK`.

The finite computation certifies only these orbit calculations. Smoothness, projectivity, completeness, and the list of orbit representatives are mathematical inputs from Lemire's construction.

## Relationship to prior work
Lemire constructs \(Y(A_4)\), proves that it is a smooth projective Demazure model, states that its fan has eight \(\operatorname{Aut}(A_4)\)-orbits of smooth maximal cones, and gives the nine ray orbits and their stabilizers. The paper also writes the divisor-class exact sequence and explicitly motivates further study of cohomological invariants, Chow groups, and \(K\)-theory of these models.

The inspected paper does not state the total number of rays, the total number of maximal cones, the Picard rank, the Euler characteristic, or the Betti numbers of \(Y(A_4)\). Exact-title, model-name, numerical, and Picard/cohomology searches located no source stating the numerical profile
\[
(1,396,1126,396,1).
\]
Older work cited in the source supplies general Demazure-model and toric techniques and dimension-three comparison models, but not this newly constructed \(A_4\) model with these invariants.

## Limitations
The calculation determines additive cohomological ranks, not the multiplicative cohomology ring. It does not compute intersection numbers, the nef or effective cones, equivariant cohomology, \(K\)-groups, or the cohomology of arithmetic quotients.

Literature searches can miss unindexed or differently phrased calculations. The originality assessment therefore relies most strongly on full-text inspection of the initiating paper and on statement-level comparison, not on search failure alone.

## References
1. N. Lemire, *Demazure Models of Algebraic Tori in Dimension 4*, arXiv:2609.30482v1, submitted 24 September 2026; Proposition 7.6 and Corollary 7.7.
2. D. Cox, J. Little, H. Schenck, *Toric Varieties*, Graduate Studies in Mathematics 124, American Mathematical Society, 2011.
