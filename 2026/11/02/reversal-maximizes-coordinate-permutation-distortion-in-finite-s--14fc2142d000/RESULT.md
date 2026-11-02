# Reversal maximizes coordinate-permutation distortion in finite Schreier spaces

## Finding
For every integer \(N\ge1\), every real \(1\le p<\infty\), and real or complex scalar field, the coordinate reversal is a maximum-norm coordinate permutation of the first \(N\) coordinates of the order-one \(p\)-convexified Schreier space. Write
\[
m=\left\lfloor\frac{N+1}{2}\right\rfloor,\qquad
C_m=\max\left\{\sum_{i=1}^{m}y_i:\;y_i\ge0,\;
\sum_{i\in F}y_i\le1\ \text{for every }F\subseteq\{1,\ldots,m\},\ 0<|F|\le\min F\right\}.
\]
Let \(P_\pi e_i=e_{\pi(i)}\) and \(R_Ne_i=e_{N+1-i}\). Then
\[
\max_{\pi\in S_N}\|P_\pi\|=\|R_N\|=C_m^{1/p},\qquad
\max_{\pi\in S_N}\|P_\pi\|\,\|P_\pi^{-1}\|=C_m^{2/p}.
\]
Both maxima are attained by reversal. Set \(J=\lfloor\log_2 m\rfloor\). Explicit bounds with an additive gap smaller than one are
\[
J+\frac{m-2^J+1}{2^J}\le C_m\le J+1.
\]
In particular, for each fixed finite \(p\),
\[
\lim_{N\to\infty}\frac{\max_{\pi\in S_N}\|P_\pi\|}{(\log_2 N)^{1/p}}=1,
\qquad
\lim_{N\to\infty}\frac{\max_{\pi\in S_N}\|P_\pi\|\,\|P_\pi^{-1}\|}{(\log_2 N)^{2/p}}=1.
\]
The finite linear program specifying \(C_m\) is exact; no general closed elementary formula for that number is asserted.

## Assumptions and scope
Define \(\mathcal S_N\) to consist of the empty set and all nonempty \(F\subseteq\{1,\ldots,N\}\) with \(|F|\le\min F\). On \(\mathbb K^N\), where \(\mathbb K\) is \(\mathbb R\) or \(\mathbb C\), set
\[
\|x\|_{N,p}=\max_{F\in\mathcal S_N}\left(\sum_{i\in F}|x_i|^p\right)^{1/p}.
\]
The empty sum is zero. All operator norms use this norm on both domain and range. Permutations are bijections of exactly the first \(N\) coordinates, and every inverse is another coordinate permutation. The result covers \(N=1\) and \(p=1\), but not \(0<p<1\), the limiting \(p=\infty\) convention, arbitrary linear isomorphisms, or higher Schreier orders.

## Proof
**1. Cardinality cutoff.** If \(F\in\mathcal S_N\) has \(k\ge1\) members, then its least element is at least \(k\) and its greatest is at least \(2k-1\). Therefore \(k\le m=\lfloor(N+1)/2\rfloor\). Conversely the terminal block \(F_*=\{N-m+1,\ldots,N\}\) is admissible, because \(N-m+1\ge m\).

**2. Compression lemma.** Fix \(A=\{a_1<\cdots<a_k\}\subseteq\{1,\ldots,N\}\). If \(y_i\ge0\) satisfy \(\sum_{i\in F}y_i\le1\) for all \(F\in\mathcal S_N\), put \(z_j=y_{a_j}\). For every \(G\in\mathcal S_k\), the increasing image \(\{a_j:j\in G\}\) belongs to \(\mathcal S_N\), since \(a_j\ge j\) and \(|G|\le\min G\). Hence \(z\) is feasible for the definition of \(C_k\) and
\[
\sum_{i\in A}y_i=\sum_{j=1}^k z_j\le C_k\le C_m.
\]
The last inequality holds because appending zero coordinates preserves feasibility for every Schreier constraint.

**3. Permutation upper bound.** Given nonzero \(x\in X_{N,p}\), normalize it and set \(y_i=|x_i|^p\). Then \(y\ge0\) satisfies every unit Schreier sum constraint. For any coordinate permutation \(\pi\) and any admissible output set \(F\), the preimage \(A=\pi^{-1}(F)\) has size at most \(m\). The compression lemma yields
\[
\|P_\pi x\|_{N,p}^p=\max_{F\in\mathcal S_N}\sum_{i\in\pi^{-1}(F)}y_i\le C_m\|x\|_{N,p}^p.
\]
Thus \(\|P_\pi\|\le C_m^{1/p}\) for every \(\pi\).

**4. Reversal attains the bound.** The reversal sends the initial block \(\{1,\ldots,m\}\) onto the admissible terminal block \(F_*\). Choose a maximizing feasible \(z\in\mathbb R_+^m\) for \(C_m\); existence holds since singleton constraints bound all entries by one. Set \(x_i=z_i^{1/p}\) for \(i\le m\) and zero otherwise. All Schreier sums in the \(N\)-coordinate norm reduce to admissible sums on the first \(m\) coordinates, so \(\|x\|_{N,p}\le1\), while
\[
\|R_Nx\|_{N,p}^p\ge\sum_{j\in F_*}|(R_Nx)_j|^p=C_m.
\]
The matching universal bound gives equality. Since \(R_N^{-1}=R_N\), both its forward and inverse norms equal \(C_m^{1/p}\). Every other coordinate permutation and its inverse satisfy the same upper bound, proving the stated two-sided maximum.

**5. Dyadic upper bound.** Partition the prefix \(\{1,\ldots,m\}\) into the \(J+1\) consecutive blocks
\[
B_q=\{2^q,\ldots,\min(2^{q+1}-1,m)\},\quad 0\le q\le J.
\]
Each block lies in \(\mathcal S_m\), because its size is at most its first element \(2^q\). Therefore each feasible \(y\) satisfies \(\sum_{i\in B_q}y_i\le1\), and summing shows \(C_m\le J+1\).

**6. Dyadic lower bound.** For all positive integers \(i\) define \(w_i=2^{-\lfloor\log_2 i\rfloor}\), and restrict this sequence to the first \(m\) indices. It is nonincreasing. For any \(k\ge1\), write \(2^q\le k<2^{q+1}\). Then \([k,2k-1]\) contains \(2^{q+1}-k\) indices of weight \(2^{-q}\) and \(2k-2^{q+1}\) indices of weight \(2^{-(q+1)}\), so
\[
\sum_{i=k}^{2k-1}w_i=(2^{q+1}-k)2^{-q}+(2k-2^{q+1})2^{-(q+1)}=1.
\]
A Schreier set whose first element is \(k\) has at most \(k\) members, all at least \(k\). Monotonicity therefore bounds its total weight by this consecutive-window sum of one. Hence the truncated \(w\) is feasible for \(C_m\), and summing its full dyadic blocks gives
\[
C_m\ge\sum_{i=1}^m w_i=J+\frac{m-2^J+1}{2^J}.
\]
Since \(m\sim N/2\), both bounds are \(\log_2 N+O(1)\), proving the two limits. Every argument applies to both scalar fields because the norm depends only on coordinate moduli.

## Verification
The proof is analytic for all dimensions, exponents, and scalars. The standalone `checker.py` gives supplementary finite tests: exact rational primal-dual linear-program certificates for \(C_m\) when \(1\le m\le13\); exact-rational sliding-window identities through \(k=256\); and 726 finite subset-compression linear programs for \(N\le9\). Sample certified values are \(C_1=1\), \(C_2=2\), \(C_3=2\), \(C_4=5/2\), \(C_5=8/3\), \(C_6=3\), \(C_7=3\), and \(C_8=13/4\). The code uses SciPy to propose extremizers but checks primal feasibility, dual feasibility, and equal objective exactly with rational arithmetic. These finite checks do not prove the unrestricted theorem.

## Relationship to prior work
The classical Schreier family and its Banach space are defined and studied in Antunes–Beanland–Chu (2019). Brech–Ferenczi–Tcaciuc (2019), Brech–Piña (2020), Antunes–Beanland (2021), and Fakhoury (2023) investigate structural and surjective-isometry classifications, including the absence of nontrivial basis permutations in the infinite Schreier setting. Those qualitative classifications do not by themselves imply that reversal maximizes the finite coordinate-permutation operator norm, the exact common reduction to \(C_m\), or the sharp logarithmic growth coefficient. The source sections inspected concern isometries, families, and their geometry, not this quantitative finite-permutation extremum. The precise novelty claim remains conditional on more exhaustive literature checking.

## Limitations
The theorem optimizes among coordinate permutations only; no optimality among general automorphisms, arbitrary operators, or different equivalent norms is claimed. The full finite sequence \(C_m\) is specified by an exact linear program and a sharp-leading-order estimate, not a closed elementary formula. Results about higher-order Schreier families and infinite permutation operators are not asserted. An equivalent statement might exist in unindexed or differently worded work on symmetry constants or permutation unconditionality. No independent scientific audit has been performed.

## References
1. L. Antunes, K. Beanland, H. V. Chu, *On the geometry of higher order Schreier spaces*, arXiv:1903.03492, first submitted 2019-03-08, https://arxiv.org/abs/1903.03492.
2. C. Brech, V. Ferenczi, A. Tcaciuc, *Isometries of combinatorial Banach spaces*, arXiv:1907.06815, first submitted 2019-07-16, https://arxiv.org/abs/1907.06815.
3. C. Brech, C. Piña, *Banach-Stone-like results for combinatorial Banach spaces*, arXiv:2007.11071, first submitted 2020-07-21, https://arxiv.org/abs/2007.11071.
4. L. Antunes, K. Beanland, *Surjective isometries on Banach sequence spaces: a survey*, arXiv:2110.11786, first submitted 2021-10-22, https://arxiv.org/abs/2110.11786.
5. M. Fakhoury, *Isometries of p-convexified combinatorial Banach spaces*, arXiv:2305.13125, first submitted 2023-05-22, https://arxiv.org/abs/2305.13125.
