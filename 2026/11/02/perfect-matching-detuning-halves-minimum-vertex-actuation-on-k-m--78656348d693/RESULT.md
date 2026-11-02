# Perfect-matching detuning halves minimum vertex actuation on \(K_{m,m}\)

## Finding
Fix an integer \(m\ge2\) and a real conductance \(t>0\). Form the weighted complete bipartite graph with vertices \(a_1,\ldots,a_m,b_1,\ldots,b_m\), weight \(t\) on each paired edge \(a_i b_i\), and weight \(1\) on every other edge \(a_i b_j\). Let \(L(t)\) denote its unnormalized weighted Laplacian. For any subset \(S\) of vertices, let \(B_S\) have as columns the corresponding distinct coordinate vectors, and let \(\rho_t(S)\) be the Kalman rank of \((-L(t),B_S)\). Write \(A=\{i:a_i\in S\}\) and \(D=\{i:b_i\in S\}\).

For the empty set \(S\), \(\rho_t(S)=0\). For every nonempty set, the **exact all-placement formula** is
\[
\rho_t(S)=
\begin{cases}
2+\min(|A|,m-1)+\min(|D|,m-1),&t=1,\\[2mm]
2+2\min(|A\cup D|,m-1),&t\ne1.
\end{cases}
\]

Consequently, when \(t=1\), full controllability holds exactly when each side contains at least \(m-1\) selected vertices. The minimum number of vertex inputs is \(2m-2\), attained by exactly \(m^2\) sets. For every \(t>0\) with \(t\ne1\), full controllability holds exactly when at least \(m-1\) distinct matched-pair indices are represented in \(S\). The minimum is \(m-1\) vertex inputs, attained by exactly \(m2^{m-1}\) sets: omit one pair and select exactly one endpoint from each remaining pair. No other positive value of \(t\) is exceptional.

## Assumptions and scope
The state equation is \(\dot z=-L(t)z+B_Su\), with independent scalar inputs at the chosen vertices. All off-matching edges have unit conductance, all matching edges share the same strictly positive conductance, and the two vertex parts both have size \(m\ge2\). Controllability means ordinary finite-dimensional Kalman controllability of this fixed, symmetric state matrix; it is not generic or strong structural controllability. The theorem covers every real positive \(t\), including irrational values, and every subset of vertices, including sets selecting both vertices of a matched pair.

## Proof
Let \(\mathbf1\in\mathbb R^m\) be the all-ones vector, \(J=\mathbf1\mathbf1^\top\), and \(d=m-1+t\). Ordering vertices by their two parts gives
\[
L(t)=\begin{pmatrix}
dI&-J-(t-1)I\\
-J-(t-1)I&dI
\end{pmatrix}.
\]
Set \(H=\{x\in\mathbb R^m:\mathbf1^\top x=0\}\). An orthogonal direct-sum decomposition into invariant eigenspaces is
\[
\begin{array}{c|c|c}
\text{space}&\text{form}&\text{Laplacian eigenvalue}\\\hline
E_0&(c\mathbf1,c\mathbf1)&0\\
E_c&(c\mathbf1,-c\mathbf1)&2d\\
E_+&(x,x),\ x\in H&m\\
E_-&(x,-x),\ x\in H&m-2+2t.
\end{array}
\]
Both constant spaces have dimension one; both zero-sum spaces have dimension \(m-1\). The four spaces exhaust \(\mathbb R^{2m}\). Since \(t>0\) and \(m\ge2\), the only possible equality between distinct displayed eigenvalue formulas is between \(m\) and \(m-2+2t\), and this occurs exactly at \(t=1\). In that case \(E_+\oplus E_-\) is one merged eigenspace of dimension \(2m-2\).

For a real symmetric matrix, the reachable subspace of \((L,B_S)\) is the orthogonal direct sum over distinct eigenvalues of the ranges of the associated spectral projections applied to \(B_S\). Indeed, multiplication by powers of \(L\) preserves the sum of these ranges, while Lagrange interpolation in the distinct eigenvalues produces each spectral projection as a polynomial in \(L\), proving the reverse inclusion. Changing \(L\) to \(-L\) does not change Kalman rank.

Let \(v_i=e_i-\mathbf1/m\in H\). The orthogonal projections of a left coordinate input \((e_i,0)\) onto \(E_+\) and \(E_-\) are respectively \((v_i,v_i)/2\) and \((v_i,-v_i)/2\). For a right coordinate input \((0,e_i)\), they are \((v_i,v_i)/2\) and \((-v_i,v_i)/2\). Both one-dimensional constant eigenspaces receive nonzero input projection whenever \(S\ne\varnothing\).

The family \(\{v_i:i\in T\}\) has rank \(\min(|T|,m-1)\) for every \(T\subseteq\{1,\ldots,m\}\). If \(|T|<m\), evaluate a putative dependence at an index outside \(T\) to show that its coefficient sum is zero and then that every coefficient is zero. If \(T\) is the whole index set, the sole relation is \(\sum_i v_i=0\).

When \(t\ne1\), the two zero-sum spaces have different eigenvalues. Input projections onto either have rank \(\min(|A\cup D|,m-1)\), regardless of which endpoint of each pair is controlled. Adding the two constant contributions gives the second rank formula.

When \(t=1\), the two zero-sum spaces merge. The projection of \((e_i,0)\) onto the merged space equals \((v_i,0)\), while that of \((0,e_i)\) equals \((0,v_i)\). Their combined rank is \(\min(|A|,m-1)+\min(|D|,m-1)\). Adding the two constant contributions proves the first formula.

Full controllability means rank \(2m\), giving the exact index-coverage conditions above. For \(t\ne1\), a minimum set selects one endpoint from each of \(m-1\) pairs, yielding \(m\cdot2^{m-1}\) choices. At \(t=1\), one vertex may be omitted from each part, yielding \(m^2\) choices. This proves all assertions.

## Verification
A standalone finite-field verifier, `paired_bipartite_rank_verify.py`, computes the Kalman matrix directly from the weighted Laplacian modulo the prime \(1000003\), and independently compares its rank with the claimed formula. It passed \(2450\) comparisons: all nonempty vertex subsets for \(2\le m\le4\) and five indicated rational conductances, plus deterministic sampling for \(5\le m\le8\). Execute with `python paired_bipartite_rank_verify.py` using Python's standard library. The finite tests are not proof for arbitrary \(m\) or real \(t\); the preceding eigenspace argument is that proof.

## Relationship to prior work
Yuan et al. (2013) provide the general spectral-multiplicity and PBH framework for exact network controllability. Xiang et al. (2013) study weighted networks and remedies for symmetry-related failure. Monshizadeh, Zhang and Camlibel (2014) establish zero-forcing tests for controllability across qualitative matrix families. The present result concerns one **fixed** weighted Laplacian family and supplies the explicit Kalman rank for every coordinate-input placement, the unique exceptional conductance, and an enumeration of all minimum placements; these formulas do not appear in the inspected portions of the cited work. The zero-forcing problem over an entire qualitative class is different from controllability at fixed conductances. No claim is made that the general PBH, eigenspace or zero-forcing principles themselves are new.

## Limitations
The exact law does not cover unequal matching weights, unequal part sizes, nonuniform off-matching edges, actuator energy or robustness to parameter uncertainty. For \(t\) near \(1\), Kalman controllability is exact but conditioning can deteriorate; no quantitative controllability-Gramian bound is claimed. The historical literature comparison is limited to the cited sources and targeted searches, and independent review has not been performed.

## References
1. Z. Yuan, C. Zhao, Z. Di, W.-X. Wang and Y.-C. Lai, *Exact controllability of complex networks*, Nature Communications **4**, 2447 (2013), published September 12, 2013. https://doi.org/10.1038/ncomms3447; full text https://pmc.ncbi.nlm.nih.gov/articles/PMC3945876/.
2. L. Xiang, J. J. H. Zhu, F. Chen and G. Chen, *Controllability of Weighted and Directed Networks with Nonidentical Node Dynamics*, Mathematical Problems in Engineering **2013**, 405034, published May 26, 2013. https://doi.org/10.1155/2013/405034.
3. N. Monshizadeh, S. Zhang and M. K. Camlibel, *Zero forcing sets and controllability of dynamical systems defined on graphs*, IEEE Transactions on Automatic Control **59** (2014), 2562–2567; preprint dated March 19, 2014. https://arxiv.org/abs/1403.4868.
