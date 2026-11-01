# A cubic-resonance transient law for parity dynamics on complements of spanning 2-factors

## Finding

Let \(H=C_{n_1}\sqcup\cdots\sqcup C_{n_r}\), where \(r\ge1\) and every \(n_i\ge3\), be a spanning 2-factor on \(N=\sum_i n_i\) labelled vertices. Let \(G=K_N\setminus E(H)\). Over any finite field \(\mathbb F_q\) of order \(q=2^h\), \(h\ge1\), evolve a vertex state by the simultaneous **self-exclusive neighbor sum**
\[
(Fz)_v=\sum_{w:\{v,w\}\in E(G)} z_w.
\]
For each deleted cycle define \(e_i=2^{\nu_2(n_i)}\) when \(3\mid n_i\), and \(e_i=0\) otherwise. Set \(\epsilon=N\bmod2\) (either zero or one), \(d=\epsilon+2\sum_i e_i\), and \(K=\max\{\epsilon,e_1,\ldots,e_r\}\).

**Exact nullity and first-periodic-entry theorem.** For every integer \(t\ge0\),
\[
\dim\ker F^t=\epsilon\,\mathbf 1_{\{t\ge1\}}+2\sum_{i=1}^r\min(t,e_i).
\]
An initial configuration \(z\) is called periodic when \(F^p z=z\) for some integer \(p\ge1\); write \(T(z)\) for the least number of updates needed to enter a periodic configuration. Every configuration has \(0\le T(z)\le K\), and \(K\) is attained if positive. Exactly \(q^{N-d}\) configurations are periodic initially, and, for every \(t\ge0\),
\[
\#\{z:T(z)\le t\}=
q^{N-d+\epsilon\mathbf1_{\{t\ge1\}}+2\sum_i\min(t,e_i)}.
\]
In particular, for every \(1\le t\le K\), the exact population first entering a periodic orbit at time \(t\) is the displayed cumulative count at \(t\) minus the cumulative count at \(t-1\). The formulas enumerate first-entry times, not the least periods of individual eventual cycles.

**Near-complete networks with a macroscopic transient.** Let \(s\ge1\) and delete exactly two disjoint cycles of length \(3\cdot2^s\) each. Then \(N=6\cdot2^s\), \(G\) is \((N-3)\)-regular with diameter two, and its edge density is \(1-2/(N-1)\). Its sharp maximal preperiod is
\[
K=2^s=N/6,
\qquad \Pr_{z\ \mathrm{uniform}}\{T(z)=K\}=1-q^{-4}.
\]
By contrast, when \(N\) is even, neighbor-sum evolution on the intact complete graph \(K_N\) is invertible and every state is periodic immediately. Thus deletion of a proportion \(2/(N-1)\) of the edges creates a linear-length transient for a fraction \(1-q^{-4}\) of all initial configurations. For binary states this fraction is exactly \(15/16\), for every \(s\ge1\).

## Assumptions and scope

The graph has simple undirected edges, no loops, and a *spanning* collection of ordinary cycle components of length at least three; no edges are deleted besides those cycle edges. A three-cycle is a legitimate deleted component, even though its complement within its own three vertices has no edges. The field has characteristic two, but may have any finite extension degree. Updates are synchronous neighbor sums without self-states or affine offsets. The theorem allows arbitrary numbers, lengths, and relative labels of the deleted cycles. The terms \(\nu_2(n)\), \(F^0=I\), and \(T(z)\) have the definitions above. A period-one state is counted as periodic.

## Proof

Write \(A_H\) for the adjacency matrix of the deleted 2-factor, \(J\) for the all-ones matrix, and \(B=I+A_H\). All matrices are over \(\mathbb F_q\), with characteristic two. As the complete graph has adjacency \(J+I\), the complement has
\[
F=J+B.
\]
Every vertex of \(H\) has two neighbors, so \(B\mathbf1=\mathbf1\) and \(\mathbf1^{\mathsf T}B=\mathbf1^{\mathsf T}\), whence \(BJ=JB=J\). We first calculate all powers' nullities for the block-diagonal \(B\).

On a deleted cycle of length \(n\), identify the coordinate space with \(R_n=\mathbb F_q[x]/(x^n-1)\), and let its cyclic shift be multiplication by \(x\). The corresponding block \(B_n\) is multiplication by \(x^{-1}(x^2+x+1)\), where \(x\) is invertible in \(R_n\). For every \(t\ge0\) multiplication by any polynomial \(a\) on \(\mathbb F_q[x]/(f)\) has kernel dimension \(\deg\gcd(a,f)\): writing \(g=\gcd(a,f)\), solutions of \(f\mid az\) are exactly multiples of \(f/g\) modulo \(f\), a space of dimension \(\deg g\). It follows that
\[
\dim\ker B_n^t=\deg\gcd\bigl((x^2+x+1)^t,x^n-1\bigr).
\]
Factor \(n=2^u m\) with \(m\) odd. Characteristic two gives \(x^n-1=(x^m-1)^{2^u}\). The quadratic \(Q=x^2+x+1\) divides \(x^m-1\) exactly when \(3\mid m\), because its roots have multiplicative order three. Since \(m\) is odd, the derivative of \(x^m-1\) is \(x^{m-1}\) and is relatively prime to \(x^m-1\); thus \(Q\) occurs with multiplicity exactly \(2^u\) if it occurs at all. This proves
\[
\dim\ker B^t=2\sum_i\min(t,e_i),\quad t\ge0.
\]

If \(N\) is even, then \(J^2=NJ=0\). Consequently \(I+J\) is invertible and \(F=B(I+J)=(I+J)B\). Therefore \(F^t=B^t(I+J)^t\), with its second factor invertible for every \(t\); the kernel dimensions equal those of \(B^t\).

If \(N\) is odd, the direct sum \(\mathbb F_q^N=\langle\mathbf1\rangle\oplus\ker\mathbf1^{\mathsf T}\) is available because \(\mathbf1^{\mathsf T}\mathbf1=N=1\) in the field. Both summands are \(B\)-invariant. On \(\langle\mathbf1\rangle\), \(B\) acts as the identity and \(F=B+J\) acts as zero. On the zero-coordinate-sum summand, \(J=0\), so \(F=B\). Moreover every vector in \(\ker B^t\), for \(t\ge1\), lies in the zero-coordinate-sum subspace: applying \(\mathbf1^{\mathsf T}\) to \(B^t z=0\) gives \(\mathbf1^{\mathsf T}z=0\). Thus the one-dimensional zero action contributes precisely one additional kernel dimension for each \(t\ge1\), proving the claimed formula for all \(t\).

Finally, the primary decomposition of a linear endomorphism of finite-dimensional vector space splits the state space as \(V=W_0\oplus W_*\), where the first restriction is nilpotent and the second is invertible. The union of periodic states is exactly \(W_*\): every element of \(W_*\) is periodic because its invertible linear map permutes a finite set, while a nonzero nilpotent coordinate cannot return to itself. For every \(t\), an initial state has entered \(W_*\) by time \(t\) exactly when its nilpotent coordinate lies in \(\ker(F|_{W_0})^t\). The nilpotent dimension is the stabilized kernel dimension \(d\), and its exponent is \(K\), as the explicit nullity formula increases at \(t=K\) and stays constant thereafter. Hence the count is \(q^{N-d}\cdot q^{\dim\ker F^t}\), exactly as asserted. When \(K>0\), strict increase of the nullity at \(K\) produces configurations requiring precisely \(K\) updates.

For the two-cycle family, both cycle lengths are \(3\cdot2^s\), hence both \(e_i=2^s\) and \(\epsilon=0\). Inserting these values yields \(d=4\cdot2^s\) and \(K=2^s=N/6\). At \(K-1\) the nullity is \(4(K-1)=d-4\), giving probability \(1-q^{-4}\) of first periodic entry at \(K\). The complement of a 2-factor has \(N(N-3)/2\) edges, hence density \((N-3)/(N-1)=1-2/(N-1)\); for \(N\ge12\) any two distinct nonadjacent vertices share other neighbors, so its diameter is two. For intact \(K_N\) with even \(N\), the adjacency is \(J+I\), with inverse itself because \(J^2=0\). This completes the proof.

## Verification

The companion program `verify/rank_verifier.py` constructs each complemented-2-factor adjacency matrix directly as binary row bitsets, multiplies powers, and computes exact GF(2) ranks by pivot elimination; it does not use the polynomial-gcd proof. It checked the nullity formula on 2,094 cycle multisets (component lengths 3 through 16, up to four components, total vertices at most 40), at all times from zero through two steps beyond the predicted maximum.

The independent `verify/orbit_verifier.py` constructs the same graph family directly from vertex neighborhoods and detects recurrent state cycles separately for every binary configuration. It checked the full first-entry distribution on 83,136 initial states across 16 nonisomorphic choices of component-length multiset, including the mixed-length instance \((3,12)\). The captured stdout in `verify/rank_output.txt` and `verify/orbit_output.txt` documents both executions. Execute the programs with Python 3 using `python3 verify/rank_verifier.py` and `python3 verify/orbit_verifier.py`. These are finite corroborations; the all-parameter theorem is proved above.

## Relationship to prior work

Classical work by Martin, Odlyzko, and Wolfram (1984) analyzes additive cellular automata by polynomial factorization and explains the use of cyclotomic factors such as \(x^2+x+1\) on an individual ring. That local polynomial method is prior art and is not claimed as new. Ciandrini and coauthors (public arXiv manuscript dated 9 September 2008) analyze graph-dependent XOR network dynamics and relate feedback topology to period behavior, without an exact kernel-power and first-entry classification for complete graphs with a spanning 2-factor removed. Ogihara and Uchizawa (2020) study algorithmic questions on general synchronous XOR systems, not this explicit dense graph-family law. The result here combines blockwise cubic-root resonance with the global rank-one coupling matrix \(J\) and yields a sharp full temporal census and a dense-graph linear-delay counterfamily. A covering unindexed or differently worded earlier classification cannot be excluded by the accessible literature comparison.

## Limitations

The formulas determine periodic-state population and transient entrance times, **not** the individual primitive periods, numbers of cycles of each length, or attraction basins of particular cycles. They require characteristic two, a spanning 2-factor consisting of simple cycles of length at least three, an unweighted undirected complement, and self-exclusive synchronous updates. The independence of the transient law from the extension degree does not assert independence of eventual cycle lengths. The literature search is not a proof of priority or uniqueness.

## References

- O. Martin, A. M. Odlyzko, S. Wolfram, *Algebraic Properties of Cellular Automata*, Communications in Mathematical Physics **93** (1984), 219–258. DOI: 10.1007/BF01223745. Author-hosted open text: https://content.wolfram.com/sw-publications/2020/07/algebraic-properties-cellular-automata.pdf
- L. Ciandrini, C. Maffi, A. Motta, B. Bassetti, M. Cosentino Lagomarsino, *Feedback topology and XOR-dynamics in Boolean networks with varying input structure*, arXiv:0809.1526v1, first posted 2008-09-09. https://arxiv.org/abs/0809.1526
- M. Ogihara, K. Uchizawa, *Synchronous Boolean Finite Dynamical Systems on Directed Graphs over XOR Functions*, MFCS 2020, LIPIcs 170, article 76. DOI: 10.4230/LIPIcs.MFCS.2020.76.
