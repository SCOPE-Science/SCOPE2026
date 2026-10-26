# Exact all-order generalized covering radii of repeated binary simplex codes

## Finding
For each integer \(m\ge1\), form the binary code \(C_m\) by repeating each of the three nonzero columns of a binary two-row simplex generator matrix exactly \(m\) times. It has parameters \([3m,2,2m]_2\). For every integer \(t\ge1\), its generalized covering radius for the column-support (block-Hamming) metric is exactly
\[
R_t(C_m)=3m-\left\lceil\frac{m}{2^t}\right\rceil-\left\lceil\frac{2m}{2^t}\right\rceil.
\]
In particular, the hierarchy reaches the maximal value \(3m-2\) at the first order \(t=\lceil\log_2(2m)\rceil\) and stays there thereafter. For fixed \(t\), the normalized radius tends to \(1-2^{-t}\) as \(m\) tends to infinity.

## Assumptions and scope
Let \(G_m\) be the binary \(2\times3m\) generator matrix consisting of \(m\) copies of each of the columns \((1,0)^{\mathsf T}\), \((0,1)^{\mathsf T}\), and \((1,1)^{\mathsf T}\), in that order. Let \(C_m=\operatorname{rowspan}_{\mathbb F_2}(G_m)\). The three column types yield two nonzero blocks in every nonzero codeword, proving the stated parameters.

For \(t\ge1\), let \(C_m^t\) denote matrices with each of their \(t\) rows in \(C_m\). For matrices \(S,T\in\mathbb F_2^{t\times3m}\), define \(d(S,T)=|\{j:S_{|j}\ne T_{|j}\}|\), the number of differing columns. Define \(R_t(C_m)=\max_{S\in\mathbb F_2^{t\times3m}}\min_{T\in C_m^t}d(S,T)\). This is the standard block-metric version of the generalized covering radius and is meaningful also when \(t\) exceeds the code redundancy, in which case it stabilizes.

## Proof
Put \(Q=2^t\) and identify a \(t\)-bit column with a group element of \(V=\mathbb F_2^t\). Given a target matrix \(S\), let \(A(v)\), \(B(v)\), \(D(v)\) be the multiplicities of the vector \(v\in V\) in the first, second, and third blocks of \(m\) target columns. Thus \(\sum_v A(v)=\sum_v B(v)=\sum_v D(v)=m\).

Every member of \(C_m^t\) is specified by two column vectors \(u,v\in V\) and has three constant blocks with values \(u\), \(v\), and \(u+v\). Therefore its agreement count with \(S\) is
\[
F(u,v)=A(u)+B(v)+D(u+v),
\]
and the distance from \(S\) to \(C_m^t\) is exactly \(3m-\max_{u,v\in V}F(u,v)\). Consequently it suffices to determine \(\min_{A,B,D}\max_{u,v}F(u,v)\) among nonnegative integer multiplicity functions summing to \(m\) each.

Choose \(u\) with \(A(u)\ge\lceil m/Q\rceil\). For this \(u\), as \(v\) ranges over \(V\), the average of \(B(v)+D(u+v)\) is \(2m/Q\). Thus some \(v\) makes that integer at least \(\lceil2m/Q\rceil\). Hence for every target
\[
\max_{u,v}F(u,v)\ge\left\lceil\frac mQ\right\rceil+\left\lceil\frac{2m}Q\right\rceil.
\]

To attain equality, write \(m=sQ+r\) with \(0\le r<Q\). Place \(s\) copies of every element of \(V\) in each of the three blocks; this contributes exactly \(3s\) to every \(F(u,v)\). If \(r=0\), the maximum is \(3s\). If \(1\le r\le Q/2\), choose an index-two subgroup \(H\le V\); place one additional copy of each element of an arbitrary \(r\)-subset of \(H\) in the first and second blocks, and one additional copy of each element of an arbitrary \(r\)-subset of \(V\setminus H\) in the third. The equation \(u+v\in V\setminus H\) cannot hold when both \(u,v\in H\), so no \(F(u,v)\) gains all three extras. Two extras can be realized by choosing \(u,v\) in the first two nonempty selected subsets, and the maximum is \(3s+2\). Finally, if \(Q/2<r<Q\), add one copy of each of any \(r\) elements to each block. Every \(F(u,v)\le3s+3\), and the preceding lower bound equals \(3s+3\), so equality again holds.

These three cases coincide with \(\lceil m/Q\rceil+\lceil2m/Q\rceil\), proving the exact formula for every \(m,t\ge1\). Both ceiling terms are one exactly when \(Q\ge2m\), proving the sharp stabilization threshold. The fixed-order asymptotic follows by dividing the formula by \(3m\). \(\square\)

## Verification
The standalone script `verify_repeated_simplex.py` uses only Python's standard library. It exhausts all triples of nonnegative block histograms at selected \((t,m)\), separately exhausts the raw target matrices in six finite test cases, and checks the explicit subgroup construction plus independently sampled targets at larger parameters. The completed checks cover 104,498 histogram triples, 8,840 directly enumerated matrices, and 960 seeded random cases; the execution concluded with `REPEATED_SIMPLEX_VERIFY_OK`. The infinite theorem depends on the proof above, not finite experiments.

## Relationship to prior work
Elimelech, Firer and Schwartz introduced generalized covering radii and their equivalent block-metric formulation. Yu and Schwartz (2026) investigate generalized packing-covering inequalities at all orders. These works motivate measuring simultaneous approximation but their inspected statements do not imply the explicit all-order ceiling formula for the repeated rank-two simplex family. Contemporary finite-geometric covering formulations likewise give a broader framework rather than the present enumerated hierarchy. The closest accessible full primary text was searched for the family and equivalent repeated-code terminology; no explicit statement was located. This is a best-knowledge comparison, not a proof of historical uniqueness.

## Limitations
The result only concerns binary, dimension-two repeated simplex generators with equal multiplicity on each nonzero projective direction. It does not determine generalized covering radii for arbitrary multiplicity vectors, other linear codes, higher-dimensional simplex families, or nonbinary analogues. Older equivalent results may be indexed under block-metric approximation, multi-covering, or additive histogram balancing terminology. No independent mathematical audit has been performed.

## References
1. W. Yu and M. Schwartz, *On the Generalized Packing and Covering Radii of Codes*, arXiv:2609.14477v1, first submitted 13 September 2026. https://arxiv.org/abs/2609.14477
2. D. Elimelech, M. Firer and M. Schwartz, *The Generalized Covering Radii of Linear Codes*, IEEE Transactions on Information Theory **67** (2021), 8070–8085. https://doi.org/10.1109/TIT.2021.3115433
3. G. N. Alfarano, G. Marino, A. Neri and R. Trombetti, *A geometric approach to generalized covering radii of linear codes*, arXiv:2606.16669v1 (2026). https://arxiv.org/abs/2606.16669
