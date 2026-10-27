# Exact endpoint Hodge norms and a logarithmic finite-size defect on squared cycles

## Finding

Let \(G_n=C_n^2\), with vertex set \(\mathbb Z/n\mathbb Z\), and undirected unit edges joining cyclic displacements \(1\) and \(2\), for every integer \(n\ge7\). Let \(Q_n\) be the standard Euclidean-orthogonal projection of the real edge-coordinate space onto the cut space, and \(P_n=I-Q_n\) the complementary cycle-space projection. Their induced \(\ell_1\) and \(\ell_\infty\) norms coincide. **In both projections, every maximizing column comes from a displacement-two edge, never a displacement-one edge.**

Put \(q=(\sqrt5-3)/2\), and for \(i=0,\ldots,n-1\) define
\[
 K_{n,i}=\frac{q^i+q^{n-i}}{\sqrt5(1-q^n)},\qquad [u]_+=\max\{u,0\}.
\]
Indices on \(K\) are read modulo \(n\). The exact norms, without any matrix inversion or optimization, are
\[
 \begin{aligned}
 S_n={}&2\sum_{i=0}^{n-1}\left[K_{n,i}+K_{n,i-1}-\frac{2}{5n}\right]_+\\
 &+2\sum_{i=0}^{n-1}\left[\mathbf 1_{\{i=0\}}-K_{n,i}-\frac{4}{5n}\right]_+,\\
 \|Q_n\|_{1\to1}={}&\|Q_n\|_{\infty\to\infty}=S_n,\\
 \|P_n\|_{1\to1}={}&\|P_n\|_{\infty\to\infty}=S_n+1-4(K_{n,0}+K_{n,1})+\frac{8}{5n}.
 \end{aligned}
\]

The positive-part sums also reveal a non-polynomial finite-size correction. With natural logarithms,
\[
 \begin{aligned}
 \|Q_n\|_{1\to1}
 &=\frac{16}{5}-\frac{12}{5\log((3+\sqrt5)/2)}\frac{\log n}{n}+O(n^{-1}),\\
 \|P_n\|_{1\to1}
 &=\frac{11}{5}+\frac{2}{\sqrt5}-\frac{12}{5\log((3+\sqrt5)/2)}\frac{\log n}{n}+O(n^{-1}).
 \end{aligned}
\]
The implied constants are absolute. In particular, the same distance-two edge orbit maximizes both norms for all admissible sizes, even though the cut and cycle norms have different limits.

## Assumptions and scope

All edges have conductance one. Choose arbitrary orientations on the \(2n\) edges and let \(D\) be the vertex-by-edge incidence matrix. Define \(L=DD^{\mathsf T}\), \(Q_n=D^{\mathsf T}L^+D\), and \(P_n=I-Q_n\). The superscript \(+\) on \(L\) denotes its Moore--Penrose inverse; the subscript \(+\) on scalar brackets denotes positive part. Orientation does not affect the reported norms. The restriction \(n\ge7\) excludes small sizes with degeneracies in the two generator orbits. The theorem concerns the **canonical orthogonal** projections, not a minimum over all nonorthogonal projections.

## Proof

**1. Resolvent and electrical columns.** Let \(S\) cyclically shift vertex functions by one place and write \(A=S+S^{-1}\). The ordinary cycle Laplacian is \(L_C=2I-A\); direct multiplication gives
\[
 L=(3I+A)L_C.
\]
The positive-definite operator \(T=3I+A\) commutes with \(L_C\). The convolution inverse \(T^{-1}\) has kernel
\[
 K_{n,i}=\sum_{h\in\mathbb Z}\frac{q^{|i+hn|}}{\sqrt5}
 =\frac{q^i+q^{n-i}}{\sqrt5(1-q^n)},\quad 0\le i<n,
\]
where \(q^2+3q+1=0\), \(-1<q<0\). Indeed \(3a_i+a_{i-1}+a_{i+1}=\mathbf 1_{\{i=0\}}\) for \(a_i=q^{|i|}/\sqrt5\), and periodization preserves the recurrence. Thus \(3K_{n,i}+K_{n,i-1}+K_{n,i+1}=\mathbf 1_{\{i=0\}}\) and \(\sum_iK_{n,i}=1/5\).

For the unit source/sink at vertices \(0\) and \(s\), with \(s=1\) or \(2\), the minimum-energy electrical current along the ordinary cycle's consecutive edges is \(\sum_{h=0}^{s-1}\mathbf1_{\{i=h\}}-s/n\). Commutation of cyclic differentiation with \(T\) shows that the corresponding displacement-one currents for \(G_n\) are obtained by convolving this vector with \(K\). A displacement-two current is the sum of two successive displacement-one currents. Consequently, writing \(e_s(i)\) and \(f_s(i)\) for the signed currents across edges \((i,i+1)\) and \((i,i+2)\) under source \((0,s)\), respectively, gives
\[
 \begin{array}{ll}
 e_1(i)=K_{n,i}-1/(5n),&f_1(i)=K_{n,i}+K_{n,i+1}-2/(5n),\\
 e_2(i)=K_{n,i}+K_{n,i-1}-2/(5n),&f_2(i)=\mathbf1_{\{i=0\}}-K_{n,i}-4/(5n).
 \end{array}
\]
The last identity uses the resolvent recurrence. Each of these four cyclic current sequences sums to zero.

**2. Column norms and diagonal corrections.** Translation symmetry leaves two edge-column types, so put \(A_s=\sum_i(|e_s(i)|+|f_s(i)|)\). Since each current sequence has zero sum, its absolute sum is twice its positive-part sum. The effective-resistance diagonal entries for the two types are
\[
 R_1=K_{n,0}-1/(5n),\qquad R_2=2(K_{n,0}+K_{n,1})-4/(5n).
\]
They lie strictly between zero and one because each edge has a parallel alternative path. The corresponding \(P_n\) column sums are \(B_s=A_s+1-2R_s\). Hence \(\|Q_n\|=\max(A_1,A_2)\) and \(\|P_n\|=\max(B_1,B_2)\). Symmetry of both projections proves equality of their induced \(\ell_1\) and \(\ell_\infty\) norms.

**3. Dominance for all sizes.** Put \(r=-q=(3-\sqrt5)/2\). The function \(u\mapsto[u]_+\) is subadditive, and subtracting a positive constant cannot increase it. Periodizing the signed infinite kernels therefore gives
\[
 \begin{aligned}
 A_1&\le2\sum_{j\in\mathbb Z}[q^{|j|}/\sqrt5]_+
 +2\sum_{j\in\mathbb Z}[(q^{|j|}+q^{|j+1|})/\sqrt5]_+\\
 &=\frac65+\frac{4}{\sqrt5(1+r)}=\frac85+\frac2{\sqrt5}<\frac{499}{200}.
 \end{aligned}
\]
The explicit geometric sums use \(0<r<1\). For every \(n\ge7\), the kernel formula and the elementary numerical inequalities \(38/100<r<39/100\), \(447/1000<1/\sqrt5<448/1000\) establish
\[
 \frac{89}{200}<K_{n,0}<\frac9{20},\qquad
 \frac4{25}<-K_{n,1}<\frac{19}{100}.
\]
Consequently \(e_2(0),e_2(1),f_2(0),f_2(1),f_2(n-1)\) are all strictly positive (use \(4/(5n)\le4/35\)). Summing only these five positive entries yields
\[
 A_2\ge 2+2K_{n,0}-\frac{32}{5n}.
\]
For \(n\ge17\), this exceeds \(289/100-32/85>499/200>A_1\). Similarly,
\[
 \begin{aligned}
 B_2-B_1
 &\ge 2-\left(\frac85+\frac2{\sqrt5}\right)-4K_{n,1}-\frac{26}{5n}\\
 &>\frac{29}{200}-\frac{26}{5n}>0\qquad (n\ge36).
 \end{aligned}
\]
For the **remaining finite sizes**, namely \(7\le n\le16\) for \(A_2>A_1\) and \(7\le n\le35\) for \(B_2>B_1\), the attached `checker.py` performs exact rational Gaussian elimination of \(3I+A\), checks its residual identically, evaluates the four formulas and verifies both strict comparisons for every integer \(7\le n\le35\). This is a finite exhaustive certificate, not extrapolation from samples. Its smallest exact margins are \(12/91\) (cut) and \(8/91\) (cycle), both at \(n=7\). Independent direct graph-Laplacian columns for \(7\le n\le12\) verify the factorization and orientation conventions. Thus \(A_2\) and \(B_2\) are the claimed norms for every \(n\ge7\).

**4. Limits and logarithmic corrections.** Write \(a_j=q^{|j|}/\sqrt5\) for integers \(j\). Apart from exponentially small wraparound errors, the two displacement-two current profiles are obtained by subtracting the constant baselines \(2/(5n)\) and \(4/(5n)\), respectively, from the infinite profiles \(a_j+a_{j-1}\) and \(\mathbf1_{\{j=0\}}-a_j\). Their strictly positive entries consist of two alternating geometric tails of ratio \(r^2\), plus finitely many central terms. Their total positive masses without baselines are, respectively,
\[
 M_1=\frac{2}{\sqrt5(1+r)},\qquad
 M_2=1-\frac1{\sqrt5}+\frac{2r}{\sqrt5(1-r^2)}.
\]
For either profile, the number of positive tail entries exceeding a baseline \(c/n\), for fixed \(c>0\), is \(\log n/\log(1/r)+O(1)\); the omitted geometric tail has total mass \(O(1/n)\). Thus subtracting that baseline decreases positive mass by \((c/\log(1/r))(\log n/n)+O(1/n)\). Periodization changes these sums only by \(O(nr^{n/2})\), which is \(O(1/n)\). It follows that
\[
 A_2=2(M_1+M_2)-\frac{12}{5\log(1/r)}\frac{\log n}{n}+O(n^{-1})
 =\frac{16}{5}-\frac{12}{5\log(1/r)}\frac{\log n}{n}+O(n^{-1}).
\]
Finally \(R_2=1-1/\sqrt5+O(n^{-1})\), so \(B_2=A_2+1-2R_2\) has the stated second asymptotic. Since \(1/r=(3+\sqrt5)/2\), this finishes the proof.

## Verification

Run `python3 checker.py` with Python 3 and no third-party packages. It performs 29 exact finite-size comparisons and 12 independently reconstructed full graph-Laplacian columns. Its output begins `EXACT_SQUARED_CYCLE_OK finite_sizes=29 direct_graph_columns=12`. The proof is analytical for all \(n\ge36\) and uses the executable rational finite certificate only for explicitly enumerated integers below that cutoff. Floating-point asymptotic samples play no role in the proof.

## Relationship to prior work

Dilworth, Kutzarova and Ostrovskii study invariant and minimal cycle-space projections, particularly on Hamming graphs and discrete tori. Their general projection framework motivates the canonical norm comparison, but their inspected Sections 2.1--2.7 contain no squared-cycle endpoint classification. Chair's earlier calculations and Doi and collaborators' later work determine effective resistances or hitting times **on the same squared-cycle graphs**. Such pairwise values determine entries of the transfer-current matrix through polarization and therefore provide underlying electrical data. They do **not** determine the asserted maximizing edge orbit or evaluate the absolute column sums and their logarithmic finite-size defect as stated theorems; obtaining those requires the positivity analysis and global column comparison above. These are the claimed additions. This is not a theorem about the minimum norm among arbitrary cycle-space projections.

## Limitations

All conclusions concern real unweighted graph-edge \(\ell_1\) and \(\ell_\infty\), the canonical Euclidean-orthogonal projectors, and the squares of cycles with \(n\ge7\). No claim is made for general cycle powers, weighted chords, intermediate \(\ell_p\) exponents, or arbitrary nonorthogonal projections. The logarithmic term is a first correction with an \(O(n^{-1})\) remainder; no explicit second-order oscillatory expansion is asserted. The finite computational certificate covers exactly the stated bounded range, while the infinite range relies on the given inequalities and geometric-tail argument.

## References

1. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582, first posted 21 May 2023. https://arxiv.org/abs/2305.12582
2. Y. Doi et al., *On the average hitting times of the squares of cycles*, arXiv:2110.12614, first posted 25 October 2021; *Discrete Applied Mathematics* 313 (2022), 18--28. https://arxiv.org/abs/2110.12614
3. N. Chair, *The effective resistance of the N-cycle graph with four nearest neighbors*, arXiv:1401.5628, first posted 22 January 2014; *Journal of Statistical Physics* 154 (2014), 1177--1190. https://arxiv.org/abs/1401.5628
