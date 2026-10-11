# Blade-permutation homology of Dutch windmill matching complexes
## Finding
Let \(D_m^n\) be the graph obtained from \(n\ge2\) copies of the cycle \(C_m\) by identifying one vertex from every copy to a single common center. The symmetric group \(S_n\) acts by permuting the \(n\) cycle blades. Write
\[
\mathrm{Std}_n=\{(x_1,\ldots,x_n)\in\mathbb Q^n:\;x_1+\cdots+x_n=0\}
\]
for the standard representation and \(\operatorname{sgn}_n\) for the sign representation.

For every \(k\ge1\), the blade-permutation action on the nonzero reduced rational homology is
\[
\widetilde H_{nk-1}(\mathcal M(D_{3k+1}^n);\mathbb Q)
\cong \operatorname{sgn}_n^{\otimes k},
\]
and
\[
\widetilde H_{nk}(\mathcal M(D_{3k+2}^n);\mathbb Q)
\cong \operatorname{sgn}_n^{\otimes k}\otimes(\mathbf 1\oplus2\,\mathrm{Std}_n).
\]
All other reduced rational homology groups vanish in these two cases. Equivalently, for \(\pi\in S_n\), if \(f(\pi)\) is its number of fixed blades, then the respective characters are
\[
(\operatorname{sgn}\pi)^k
\quad\text{and}\quad
(\operatorname{sgn}\pi)^k(2f(\pi)-1).
\]

## Assumptions and scope
The matching complex \(\mathcal M(G)\) has the edges of \(G\) as vertices and the graph matchings as simplices. After choosing the same cyclic coordinate on every blade with the common center in the same position, the action considered here is the subgroup \(S_n\) that permutes whole blades while preserving that coordinate. The statement is over \(\mathbb Q\). It does not identify the integral lattice action or the additional automorphisms coming from within-blade dihedral symmetries.

The nonequivariant homotopy types used below are Donovan--Scoville, Theorem 5.8:
\[
\mathcal M(D_{3k+1}^n)\simeq S^{nk-1},
\qquad
\mathcal M(D_{3k+2}^n)\simeq\bigvee^{2n-1}S^{nk}.
\]
Thus it remains to determine the character of the natural blade-permutation action on the unique nonzero reduced homology degree.

## Proof
For a path with \(r\) edges define the alternating matching sum
\[
a_r=\sum_{T}(-1)^{|T|},
\]
where the sum runs over all matchings \(T\) of that path, including the empty matching. Splitting according to whether the last edge is used gives
\[
a_r=a_{r-1}-a_{r-2},\qquad a_0=1,\quad a_1=0.
\]
Hence \((a_r)\) is periodic with period six:
\[
1,0,-1,-1,0,1,1,0,-1,-1,0,1,\ldots.
\]

Fix \(\pi\in S_n\). Let \(c(\pi)\) be the number of cycles of \(\pi\) on the blades and let \(f(\pi)\) be the number of fixed blades. Put
\[
A=a_{m-2},\qquad B=a_{m-3}.
\]
A matching on \(D_m^n\) that uses no edge incident with the common center consists of an internal matching on each blade. A \(\pi\)-invariant such matching must repeat the same internal pattern around every cycle of blades, so its alternating orbit sum contributes \(A^{c(\pi)}\).

A matching can contain at most one edge incident with the common center. Such an edge can occur in a \(\pi\)-invariant matching only on a fixed blade. There are two choices of center edge on that blade. Selecting it contributes one additional edge orbit, hence a minus sign, and leaves a path with \(m-3\) available internal edges on that blade. Therefore, if
\[
F(\pi)=\sum_{S}(-1)^{o_\pi(S)},
\]
where the sum is over all \(\pi\)-invariant matchings and \(o_\pi(S)\) is the number of \(\pi\)-orbits on the edges of \(S\), then
\[
F(\pi)=A^{c(\pi)}-2f(\pi)B A^{c(\pi)-1}.
\]
In the two residue classes used below, \(A\) is nonzero, so this displayed expression is literal.

Now apply the simplicial Lefschetz trace formula. If a nonempty \(\pi\)-invariant matching \(S\) has \(|S|\) edges and \(o_\pi(S)\) edge-orbits, then the orientation sign of \(\pi\) on the corresponding simplex is \((-1)^{|S|-o_\pi(S)}\). Multiplying by the chain-degree sign \((-1)^{|S|-1}\) gives \((-1)^{o_\pi(S)-1}\). After adding the augmented empty-simplex term, the reduced Lefschetz number is therefore
\[
\widetilde L(\pi)=-F(\pi).
\]
Because Donovan--Scoville's theorem concentrates reduced homology in a single degree \(d\), the top-homology character is
\[
\chi(\pi)=(-1)^d\widetilde L(\pi).
\]

If \(m=3k+1\), then the period-six recurrence gives \(A=(-1)^k\), \(B=0\), and \(d=nk-1\). Consequently
\[
\chi(\pi)=(-1)^{k(n+c(\pi))}=(\operatorname{sgn}\pi)^k,
\]
since \(\operatorname{sgn}\pi=(-1)^{n-c(\pi)}\).

If \(m=3k+2\), then \(A=B=(-1)^k\) and \(d=nk\), so
\[
\chi(\pi)=(\operatorname{sgn}\pi)^k(2f(\pi)-1).
\]
The permutation representation of \(S_n\) on the blades has character \(f(\pi)\), while \(\mathrm{Std}_n\) has character \(f(\pi)-1\). Thus \(\mathbf1\oplus2\,\mathrm{Std}_n\) has character \(2f(\pi)-1\). Character equality over \(\mathbb Q\) identifies the claimed representations.

## Verification
The standalone checker `artifacts/verify.py` independently implements the path recurrence, the symbolic fixed-matching formula, and direct enumeration of every matching for \(n\in\{2,3\}\) and \(m\in\{4,5,7,8\}\). For every permutation of the blades in those cases it computes the signed simplicial-chain trace directly and compares it with the closed character formula. The complete output is recorded in `artifacts/verification_output.txt` and ends with `VERIFY_OK`.

The finite computation is a regression check, not the proof of the infinite statement. The proof for all \(n\ge2\) and \(k\ge1\) is the fixed-simplex factorization and recurrence above, together with the published nonequivariant homotopy theorem.

## Relationship to prior work
Donovan and Scoville determine the nonequivariant homotopy type of \(\mathcal M(D_m^n)\) in Theorem 5.8. Their theorem supplies the homology degree and dimension but does not determine how blade permutations act on that homology. A nonequivariant wedge decomposition alone cannot determine a group representation of the same dimension.

Classical representation-theoretic results for matching complexes, such as Dong--Wachs, concern the standard matching complex of a complete graph and its natural symmetric-group action. More recent work on symmetric-group representations of matching complexes of complete hypergraphs likewise concerns a different graph or hypergraph family. Neither specializes to the Dutch windmill blade action considered here.

Exact searches under both “Dutch windmill” and “friendship graph” terminology, together with searches for equivariant homology, sign representations, standard representations, and fixed-point character formulas, found the Donovan--Scoville nonequivariant theorem but no source stating the blade-permutation character above.

## Limitations
The result concerns only the natural \(S_n\) action that permutes blades. It does not classify the representation of the full graph automorphism group, which can also contain symmetries internal to individual blades. The representation is identified over \(\mathbb Q\); no assertion is made about an integral decomposition. The originality search can reduce, but cannot eliminate, the residual possibility of an unindexed computation under different terminology.

## References
1. Connor Donovan and Nicholas A. Scoville, “Star clusters in the matching, Morse, and generalized complex of discrete Morse functions,” New York Journal of Mathematics 29 (2023), 1393–1412; arXiv:2207.13780. See Theorem 5.8.
2. Xun Dong and Michelle L. Wachs, “Combinatorial Laplacian of the Matching Complex,” Electronic Journal of Combinatorics 9 (2002), R17, DOI 10.37236/1634.
3. Michael Bate, Brent Everitt, Sam Ford, and Eric Ramos, “Homology of matching complexes and representations of symmetric groups,” arXiv:2312.13750.
