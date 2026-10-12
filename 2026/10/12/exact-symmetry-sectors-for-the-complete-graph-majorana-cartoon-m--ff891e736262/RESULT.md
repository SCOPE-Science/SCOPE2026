# Exact symmetry sectors for the complete-graph Majorana cartoon matrix model

## Finding

For the complete-graph Majorana model of Lucas and Osborne, let \(N\in4\mathbb Z_{{>0}}\), let \(\psi_e\) be the Hermitian Majorana operator on edge \(e\) of \(K_N\), and let \(H\) be the cycle Hamiltonian for which Proposition 3.3 proves commutation with the vertex-star products. With the paper's raw definition
\[
\Psi_v:=\prod_{{e\ni v}}\psi_e,
\]
the product contains exactly \(N-1\) mutually anticommuting Majoranas. As written, \(\Psi_v\) is therefore anti-Hermitian and satisfies \(\Psi_v^2=-I\), rather than being a Hermitian involution. The phase-corrected star
\[
S_v:=i\Psi_v
\]
is a Hermitian involution, and the commutation relations proved in the source become
\[
[S_v,H]=[S_u,S_v]=0.
\]

Choose any one vertex to omit. The remaining \(N-1\) corrected stars have exactly \(2^{{N-1}}\) nonzero joint eigenspaces, all of the same dimension
\[
2^{{(N-1)(N-4)/4}}.
\]
The omitted star contributes no further split: its eigenvalue is fixed by one scalar relation among all \(N\) stars. Consequently \(H\) is exactly block diagonal over \(2^{{N-1}}\) equal-dimensional symmetry sectors. These commuting symmetries alone do not force equality of eigenvalues between different sectors, so they imply a block decomposition rather than an exponential spectral degeneracy.

## Assumptions and scope

The claim uses exactly the model and Hilbert space of arXiv:2007.07165v1, Sections 3.2–3.3. The source takes \(N\in4\mathbb Z_{{>0}}\),
\[
\mathcal H=(\mathbb C^2)^{{\otimes N(N-1)/4}},
\]
places one Hermitian Majorana \(\psi_e\) on each edge of \(K_N\), and imposes
\[
\{{\psi_e,\psi_f\}}=2I\,\mathbf 1[e=f].
\]
The edge order inside a monomial is prescribed only to fix an overall sign. The result applies to every Hamiltonian covered by Proposition 3.3. It does not assume generic couplings, randomness, permutation symmetry, or any statement about level statistics.

## Proof

Put \(k=N-1\). For any ordered product \(\Psi=\psi_1\cdots\psi_k\) of distinct Hermitian Majoranas,
\[
\Psi^\dagger=(-1)^{{k(k-1)/2}}\Psi,
\qquad
\Psi^2=(-1)^{{k(k-1)/2}}I.
\]
If \(N=4m\), then \(k=4m-1\) and
\[
\frac{{k(k-1)}}2=(4m-1)(2m-1)
\]
is odd. Hence every raw star obeys
\[
\Psi_v^\dagger=-\Psi_v,
\qquad
\Psi_v^2=-I.
\]
Changing the prescribed ordering multiplies \(\Psi_v\) only by \(-1\), so these two conclusions are ordering-independent. Therefore \(S_v=i\Psi_v\) is Hermitian and \(S_v^2=I\). Multiplication by the scalar \(i\) preserves the commutators established in Proposition 3.3.

Fix a distinguished vertex \(v_0\). For a subset \(T\subseteq V\setminus\{{v_0\}}\), multiply the corrected stars \(S_v\) with \(v\in T\). Every edge with either zero or two endpoints in \(T\) occurs an even number of times and cancels up to a scalar phase; every edge with exactly one endpoint in \(T\) occurs once. Thus, up to a unit scalar, the Majorana support of the product is exactly the cut
\[
\delta(T)=\{\{a,b\}:a\in T,\ b\notin T\}.
\]
If \(T\ne\varnothing\), then \(T\) is a proper nonempty subset of the connected graph \(K_N\), so \(\delta(T)\ne\varnothing\). Proposition 3.2 of the source proves that every nontrivial Majorana monomial is traceless. Hence
\[
\operatorname{{tr}}\!\left(\prod_{{v\in T}}S_v\right)=0
\]
for every nonempty \(T\subseteq V\setminus\{{v_0\}}\).

The cuts are distinct on this restricted family. Indeed, if \(\delta(T)=\delta(U)\), then \(\delta(T\mathbin{{\triangle}}U)=\varnothing\). Connectivity of \(K_N\) forces \(T\mathbin{{\triangle}}U\) to be either empty or all of \(V\); the latter is impossible because both \(T\) and \(U\) omit \(v_0\). Thus \(T=U\). The \(N-1\) corrected stars are therefore independent commuting involutions.

For \(\varepsilon=(\varepsilon_v)_{{v\ne v_0}}\in\{{-1,+1\}}^{{N-1}}\), form the joint spectral projector
\[
P_\varepsilon=2^{{-(N-1)}}\prod_{{v\ne v_0}}(I+\varepsilon_vS_v).
\]
Expanding its trace, every nonidentity term vanishes by the preceding tracelessness argument. Since
\[
\dim\mathcal H=2^{{N(N-1)/4}},
\]
we obtain
\[
\dim P_\varepsilon\mathcal H
=\operatorname{{tr}}P_\varepsilon
=2^{{N(N-1)/4-(N-1)}}
=2^{{(N-1)(N-4)/4}}.
\]
This is positive for every sign vector, so all \(2^{{N-1}}\) sectors occur.

Finally, in the product of all \(N\) corrected stars every edge of \(K_N\) occurs exactly twice. Hence
\[
\prod_{{v\in V}}S_v=\sigma I,
\qquad \sigma\in\{-1,+1\},
\]
where \(\sigma\) depends on the sign/order convention. Therefore the omitted star is a scalar multiple of the product of the other \(N-1\) stars and supplies no additional eigenvalue label. Because every \(S_v\) commutes with \(H\), each joint eigenspace is \(H\)-invariant. Commuting one-dimensional symmetry characters do not impose equality of the spectra of distinct blocks, so no energy degeneracy follows from these symmetries alone.

## Verification

The included `verify.py` implements the Clifford monomial algebra exactly by bit masks and fourth-root-of-unity phases. For \(N=4,8,12,16\) it checks: the odd parity of \((N-1)(N-2)/2\); involutivity of every corrected star; pairwise commutation; the equality between subset-star support and the complete-graph cut; injectivity of all \(2^{{N-1}}\) cuts after one vertex is omitted; scalarity of the full-star product; and the sector-dimension exponent. Its replay output is recorded in `VERIFICATION.md`. These finite checks corroborate the algebra but are not used as a proof for arbitrary \(N\).

## Relationship to prior work

Lucas and Osborne prove the two commutators in Proposition 3.3 and immediately state that the raw \(\Psi_v\) is Hermitian with square \(I\), then speculate that the symmetries may lead to typical spectral degeneracy of order \(\exp(N)\); they explicitly say that they do not study the eigenspectrum. Their own Section 3.2 also states that a generic graph monomial is not necessarily Hermitian and proves that every nontrivial Majorana monomial is traceless. The phase correction and exact sector count above reconcile these facts and replace the degeneracy heuristic by the precise conclusion implied by the commuting stars.

Chen and Lucas study general graph-theoretic bounds on operator growth, not this model's static star-symmetry decomposition. Gubser, Jepsen, Ji, and Trundy classify \(\mathbb Z_2^n\) interaction-vertex symmetries in different melonic theories, but do not derive the complete-graph edge-Majorana cut algebra or the equal sector dimensions here. Pakrouski, Klebanov, Popov, and Tarnopolsky analyze symmetry sectors and degeneracies in a different \(O(4)^3\) tensor Majorana model. Zhang and Gu later study operator-size distributions and cite the cartoon matrix model, but their examples are Brownian and large-\(q\) SYK models rather than this eigenspectrum problem. Targeted searches by source identifier, star-operator notation, symmetry-sector aliases, cut formulations, and degeneracy language located no statement implying the theorem above.

## Limitations

The theorem concerns the exact symmetry decomposition generated by the vertex stars. It does not compute the spectrum inside any block, assert generic simplicity, exclude additional symmetries, or determine degeneracies caused by special choices of couplings. The sign \(\sigma\) in the full-star relation is convention-dependent because the source intentionally leaves monomial ordering unspecified up to sign. The result also does not modify the source's operator-growth bounds, which depend on the commuting selection rule rather than on the missing phase. An equivalent sector decomposition could exist in weakly indexed Majorana or tensor-model literature under different gauge-symmetry terminology; no such coverage was found in the inspected sources.

## References

1. Andrew Lucas and Andrew Osborne, *Operator growth bounds in a cartoon matrix model*, arXiv:2007.07165v1, Journal of Mathematical Physics 61, 122301 (2020), DOI:10.1063/5.0022177.
2. Chi-Fang Chen and Andrew Lucas, *Operator growth bounds from graph theory*, arXiv:1905.03682v1.
3. Steven S. Gubser, Christian Jepsen, Ziming Ji, and Brian Trundy, *Higher melonic theories*, arXiv:1806.04800v1, DOI:10.1007/JHEP09(2018)049.
4. Kiryl Pakrouski, Igor R. Klebanov, Fedor Popov, and Grigory Tarnopolsky, *Spectrum of Majorana Quantum Mechanics with \(O(4)^3\) Symmetry*, arXiv:1808.07455v1, DOI:10.1103/PhysRevLett.122.011601.
5. Pengfei Zhang and Yingfei Gu, *Operator size distribution in large \(N\) quantum mechanics of Majorana fermions*, arXiv:2212.04358v1, DOI:10.1007/JHEP10(2023)018.
