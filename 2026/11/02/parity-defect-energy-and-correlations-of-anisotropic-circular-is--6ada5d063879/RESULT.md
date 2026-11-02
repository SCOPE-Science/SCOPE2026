# Parity-defect energy and correlations of anisotropic circular Ising ladders

## Finding

For every integer \(n\ge3\) and all leg and rung couplings \(J,K>0\), the classical antiferromagnetic Ising model on the finite circular ladder \(C_n\square K_2\) has an exact fixed-magnetization energy and a parity-sensitive field response. Let \(M\in\{-2n,-2n+2,\ldots,2n\}\) be the total spin and put \(k=n-|M|/2\). The **minimum exchange energy**, without the field term, is

\[
E_{\mathrm{ex,min}}(M)=2nJ+nK-2(2J+K)k+4J\,\mathbf 1_{\{n\text{ odd},\,k=n\}}.
\]

In particular, the excess energy of the zero-magnetization sector on an odd circular ladder is exactly \(4J\), independent of the positive rung coupling. Its finite-size zero-temperature magnetization has an otherwise absent plateau \(M=2\) in positive fields \(K<h<K+2J\); an even circular ladder instead has only \(M=0\) below its saturation field \(h=K+2J\).

The number of labelled ground-state spin configurations is fully determined. For **odd** \(n\), the respective counts on the positive-field intervals \(0\le h<K\), \(h=K\), \(K<h<K+2J\), \(h=K+2J\), \(h>K+2J\) are

\[
2n,\quad 4n,\quad 2n,\quad P_n,\quad 1,
\qquad P_n=(1+\sqrt2)^n+(1-\sqrt2)^n-1.
\]

For **even** \(n\), the counts below, at and above \(h=K+2J\) are respectively \(2\), \(P_n=(1+\sqrt2)^n+(1-\sqrt2)^n+1\), and \(1\). For negative fields, global spin reversal supplies the corresponding energies, magnetizations and multiplicities. At the upper transition, \(P_n\) is the familiar independent-set count of the circular ladder, used here as a credited input rather than asserted as a novel counting formula.

On an odd ladder, let \(\langle\cdot\rangle\) denote the uniform zero-temperature mixture of ground configurations at fixed field. For either row \(a\in\{0,1\}\), either site \(i\), and each \(0\le r<n\), the same-row correlations throughout \(0\le h<K+2J\), including \(h=K\), are

\[
C_n(r)=\langle\sigma_{a,i}\sigma_{a,i+r}\rangle=(-1)^r\left(1-\frac{2r}{n}\right),
\]

where subscripts are modulo \(n\). For the opposite row the correlations at distinct rungs are \(\langle\sigma_{0,i}\sigma_{1,i+r}\rangle=-C_n(r)\) for \(1\le r<n\). Same-rung correlations distinguish the three lower-field regimes:

\[
\langle\sigma_{0,i}\sigma_{1,i}\rangle=
\begin{cases}
-1,&0\le h<K,\\
-1+1/n,&h=K,\\
-1+2/n,&K<h<K+2J.
\end{cases}
\]

These identities give both the complete finite-size phase diagram and exact spatial correlations of the odd-parity defect.

## Assumptions and scope

The graph has labelled vertices \((a,i)\) for rows \(a=0,1\) and indices \(i\in\mathbb Z/n\mathbb Z\). Each row has cycle edges \((a,i)(a,i+1)\), and each rung has an edge \((0,i)(1,i)\). All edges are counted once. The Hamiltonian, with spins \(\sigma_{a,i}\in\{-1,+1\}\), is

\[
\mathcal H(\sigma;h)=J\sum_{a=0}^1\sum_{i=0}^{n-1}\sigma_{a,i}\sigma_{a,i+1}
+K\sum_{i=0}^{n-1}\sigma_{0,i}\sigma_{1,i}
-h\sum_{a,i}\sigma_{a,i}.
\]

Couplings are **strictly positive** and uniform within each edge type, the field \(h\) is real, and all statements concern finite labelled graphs and exact zero temperature. Equal-weight ground-state averages are used for the correlation formulas, including at coexistence. No thermodynamic limit or thermal selection convention is implicit.

## Proof

**1. Negative-set energy identity.** Let \(S\) be the set of negative-spin vertices of cardinality \(m\). At zero field, global spin reversal preserves energy; replace \(S\) by its complement if needed to obtain cardinality \(k=\min(m,2n-m)\le n\). Let \(e_\ell(S)\) and \(e_r(S)\) count the edges internal to \(S\) within the legs and rungs, respectively. Every graph vertex has total weighted degree \(2J+K\), so the weighted spin cut is \((2J+K)k-2Je_\ell(S)-2Ke_r(S)\). Comparing with the all-positive exchange energy \(2nJ+nK\),

\[
E_{\mathrm{ex}}(S)=2nJ+nK-2(2J+K)k+4Je_\ell(S)+4Ke_r(S).
\]

**2. Sharp independent-set bounds and the parity defect.** For even \(n\), one negative spin per rung, alternating between the two rows, is an independent set of size \(n\). Therefore every sector \(0\le k\le n\) has a representative with no internal edge. For odd \(n\), choose a single empty rung and alternate the negative-row choice on the remaining \(n-1\) consecutive rungs. This gives an independent set of size \(n-1\), and its subsets realize every \(k\le n-1\). At \(k=n\) on an odd ladder, one row contains at least \((n+1)/2\) negative spins; an odd \(n\)-cycle has independence number \((n-1)/2\), hence at least one internal leg edge. The lower bound \(Je_\ell+Ke_r\ge J\) is attained by placing exactly one negative spin in each rung, alternating its row except at one leg edge where the same row is used twice. This produces exactly one internal leg edge and zero internal rung edges. Substitution into the preceding identity proves the fixed-magnetization formula for **all** \(n,J,K,M\), including its sharp \(4J\) odd-parity correction.

**3. Field minimization.** For \(h\ge0\), the minimizer may be chosen with nonnegative total magnetization \(M=2(n-k)\). For sectors \(k<n\) the minimum total energy is

\[
2nJ+nK-2nh+2(h-K-2J)k.
\]

For odd \(n\), the exceptional \(k=n\) sector has an additional \(4J\). Its difference from the \(k=n-1\) sector is precisely \(2(h-K)\). Consequently the odd ladder minimizes at \(k=n\) below \(h=K\), at \(k=n-1\) strictly between \(h=K\) and \(h=K+2J\), and at \(k=0\) above saturation, with exactly the stated coexistences. For even \(n\), there is no exceptional sector and the exchange-energy slope gives the single positive transition \(h=K+2J\). At zero field all minimizers have \(M=0\); global spin reversal handles \(h<0\).

**4. Multiplicities.** When \(n\) is odd, the minimizing \(k=n\) configurations have precisely one internal leg edge and no internal rung edges. The location of that edge and the row in which it lies are arbitrary: exactly \(2n\) configurations. The maximizing independent sets of size \(n-1\) have exactly one empty rung and alternate the occupied row along the remaining path: again \(2n\). These sets coexist at \(h=K\), yielding \(4n\). For even \(n\), there are exactly two independent sets of size \(n\), corresponding to the two alternating rows. At \(h=K+2J\), the energy relative to the all-positive configuration for a negative set \(S\) is exactly \(4Je_\ell(S)+4Ke_r(S)\). Therefore every and only independent set is a ground state. On each rung, the independent-set possibilities are empty, top occupied, or bottom occupied. The compatibility matrix for successive rungs is

\[
T=\begin{pmatrix}1&1&1\\1&0&1\\1&1&0\end{pmatrix}.
\]

Its eigenvalues are \(1+\sqrt2\), \(1-\sqrt2\), and \(-1\); hence the total count is \(\mathrm{tr}(T^n)=(1+\sqrt2)^n+(1-\sqrt2)^n+(-1)^n\). This standard independent-set calculation is included to make the complete answer self-contained; the saturation-entropy transfer method is established in the cited literature.

**5. Correlations.** On an odd ladder, in both the \(M=0\) and \(M=2\) phases, each row has exactly one frustrated leg bond. Its position is uniformly distributed over all \(n\) leg edges in the equal-weight mixture, so a length-\(r\) row segment crosses the frustrated edge with probability \(r/n\). The spin product is \((-1)^r\) without such a crossing and its negative otherwise, proving \(C_n(r)\). In the zero-magnetization phase, opposite-row spins are negatives of one another at every rung. In the \(M=2\) phase, exactly one rung is \((+1,+1)\), and all other rungs have opposite spins. The exceptional rung is uniform among the \(n\) positions. Conditional on its position, the two possible alternating row choices give zero mean at any other rung. The cross-row expectation at distinct rungs therefore equals \(-C_n(r)\), while the same-rung expectation is \(-1+2/n\). At \(h=K\), there are equally many ground configurations from the two sectors, giving \(-1+1/n\). This establishes the claimed correlation laws.

## Verification

`CHECK.py` independently enumerates every labelled spin configuration for \(3\le n\le9\), at three positive integral pairs of couplings, without floating-point arithmetic. It compares all fixed-magnetization minima, all listed field/coexistence counts, and the rational two-point functions for odd sizes up to \(n=7\). `CHECK_OUTPUT.txt` records the output. The checks total 147 fixed-sector comparisons, 126 field-degeneracy comparisons, and 270 rational correlation comparisons; they are finite corroboration, not the proof for all \(n\).

Run with `python3 CHECK.py` in the directory containing the two files. No packages beyond Python's standard library are needed.

## Relationship to prior work

Varma's 2013 study of Ising ladder saturation entropies (arXiv:1305.4606, relevant section II and table II) established the bulk saturation mechanism and the transfer-matrix approach for ladder L1. It discusses a single transition of the unfrustrated periodic pattern and does not provide the odd-length finite-size, anisotropic full-sector profile or the below-saturation two-point functions proved here. The independent-set transfer count at the upper transition, and the general Ising/max-cut relation, are **not** claimed as new. Cen, Das and Fong (2022) directly benchmark circular-ladder MAX-CUT instances but do not state the weighted all-magnetization formula or parity-dependent correlation identities. Jurčišinová and Jurčišin (2014) study a zigzag ladder with multisite interactions rather than this two-parameter periodic nearest-neighbor ladder.

The exact all-field behaviour of Möbius ladders is a relevant related but nonidentical boundary geometry; its analogous finite-size parity phenomenon does not give the present prism-graph weighted constrained energies or same-rung/long-range spin correlations without an additional graph-specific argument. The novelty asserted here is **only** the combined parity-defect, anisotropic fixed-sector and below-saturation correlation classification, not generic transfer-matrix methods or saturated independent-set counting. Historical priority remains provisional pending specialized literature review.

## Limitations

The result does not treat \(J=0\), \(K=0\), ferromagnetic bonds, nonuniform individual rung couplings, quantum spins, thermal fluctuations, or explicit zero-temperature correlations at the saturation field. A finite odd ladder's middle plateau has magnetization fraction \(M/(2n)=1/n\) and disappears as a finite *fraction* in the bulk limit. Exhaustive checks through \(n=9\) do not independently certify the infinite-family theorem. No independent scientific audit has been performed.

## References

1. V. K. Varma, *Saturation field entropies of antiferromagnetic Ising models: Ladders and the kagome lattice*, arXiv:1305.4606 (first publicly posted 2013-05-20), Phys. Rev. B 88, 134421 (2013), https://arxiv.org/abs/1305.4606.
2. Y. Cen, D. Das, X. Fong, *A tree search algorithm towards solving Ising formulated combinatorial optimization problems*, Scientific Reports 12, 14755 (2022), https://doi.org/10.1038/s41598-022-19102-x.
3. E. Jurčišinová and M. Jurčišin, *Solution of the antiferromagnetic Ising model with multisite interaction on a zigzag ladder*, Phys. Rev. E 90, 032108 (2014), https://doi.org/10.1103/PhysRevE.90.032108.
