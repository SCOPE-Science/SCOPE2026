# Joint nearest-cover multiplicities of binary extended Hamming codes

## Finding
For integers \(m\ge 2\) and \(t\ge 1\), let \(H\) be the \((m+1)\times 2^m\) binary matrix with one column \(h_a=(1,a)^\mathsf T\) for each \(a\in\mathbb F_2^m\), and let \(C=\ker H\), the binary extended Hamming code \(\mathrm{RM}(m-2,m)\). For each \((m+1)\times t\) syndrome matrix \(S\), define \(\lambda(S)\) to be the fewest nonzero rows of any \(2^m\times t\) matrix \(E\) satisfying \(HE=S\), and \(M(S)\) the number of such matrices attaining \(\lambda(S)\). Write \(r=\operatorname{rank}_{\mathbb F_2}S\), and let \(u\) be the first row of \(S\). Set \(G_r=|\mathrm{GL}_r(\mathbb F_2)|=\prod_{i=0}^{r-1}(2^r-2^i)\).

The *complete joint nearest-cover profile* is:

\[
(\lambda(S),M(S))=\begin{cases}
(0,1),&S=0,\\
\left(r,\dfrac{G_r}{(2^r-1)r!}\right),&u\ne0,\\
\left(r+1,\dfrac{2^mG_r}{(r+1)!}\right),&u=0,\ S\ne0.
\end{cases}
\]

Both displayed multiplicities are integers and count distinct minimizing correction matrices, not merely their possible ranks. To count every syndrome type, put \(N_{a,t}(0)=1\), \(N_{a,t}(r)=0\) if \(r>\min(a,t)\), and otherwise
\[
N_{a,t}(r)=\prod_{i=0}^{r-1}\frac{(2^a-2^i)(2^t-2^i)}{2^r-2^i}.
\]
For each positive \(r\), exactly \(N_{m+1,t}(r)-N_{m,t}(r)\) syndromes have \(u\ne0\) and rank \(r\), and exactly \(N_{m,t}(r)\) have \(u=0\) and rank \(r\); the zero syndrome is unique. These counts, together with the profile, specify the joint distribution of optimal access count and number of optimal solutions for every \(m,t\).

For fixed \(t\) and \(m\to\infty\), a uniformly random syndrome requires the maximum \(t+1\) accesses with probability approaching \(2^{-t}\). Conditional on this event, its number of optimal corrections is exactly \(2^mG_t/(t+1)!\). In particular, the expected number of optimal corrections is asymptotic to \(2^{m-t}G_t/(t+1)!\). This rare but exponentially large multiplicity is invisible in the previously known generalized covering-radius value.

## Assumptions and scope
Matrices, ranks, and spans are over \(\mathbb F_2\). A column is accessed if any of its \(t\) error coordinates is nonzero. Thus the problem is nearest-cover decoding of \(t\) simultaneous words by \(C^t\) in the column-support metric, equivalently expressing \(t\) simultaneous syndromes using the smallest common set of parity-check columns. No stochastic channel model is assumed. Counts of syndromes correspond to the uniform distribution on the \(2^{(m+1)t}\) possible syndrome matrices; received arrays are uniform over syndromes because \(H\) has full row rank.

## Proof
Put \(W=\operatorname{im}S\le\mathbb F_2^{m+1}\), so \(\dim W=r\). Each nonzero row of a correction \(E\) contributes one rank-one matrix \(h_a e_a\), with \(h_a\) in the affine hyperplane \(\mathcal A=\{(1,a):a\in\mathbb F_2^m\}\) and \(e_a\in\mathbb F_2^{1\times t}\setminus\{0\}\). Therefore \(W\) lies in the span of the accessed \(h_a\), and at least \(r\) columns are needed.

If \(u\ne0\), the restriction to \(W\) of the first-coordinate functional is nonzero. A basis of \(W\) can be chosen entirely in \(W\cap\mathcal A\): choose one affine vector \(v\) and vectors \(v+w_i\) for a basis \(w_i\) of the codimension-one kernel. Hence \(r\) columns suffice. Any minimizing \(r\)-column support must be an all-affine basis of \(W\), and conversely each such basis gives a *unique* factorization \(S=H_BE_B\), since \(H_B\) has full column rank. The coefficient map \(E_B\) has rank \(r\) and so no coefficient row vanishes. To count bases, the ordered bases of \(W\) correspond to \(\mathrm{GL}_r(2)\); the vector of first-coordinate functional evaluations on an ordered basis is uniformly distributed over the \(2^r-1\) nonzero binary rows. Exactly \(G_r/(2^r-1)\) ordered bases have all evaluations equal to one. Dividing by \(r!\) gives the stated multiplicity.

If \(u=0\) but \(S\ne0\), the nonzero space \(W\) lies in the linear hyperplane \(\ker(\text{first coordinate})\). No \(r\) affine vectors can span \(W\): their \(r\)-dimensional span would equal \(W\), while containing an affine vector. Thus at least \(r+1\) columns are required. For any affine \(v\), the affine \(r\)-flat \(v+W\) has \(2^r\) affine points, and any affine basis of \(r+1\) such points forms a linearly independent set whose span contains \(W\). It therefore supplies a unique solution \(E_B\). Because the coefficient image is exactly the even-parity subspace of \(\mathbb F_2^{r+1}\), which has nonzero projection to every coordinate for \(r\ge1\), no row of this solution vanishes. Conversely any minimizing set of \(r+1\) columns spans a space of dimension exactly \(r+1\); its members all lie in one coset \(v+W\) and form an affine basis there. There are \(2^{m-r}\) such cosets. The number of unordered affine bases of an \(r\)-flat is \(2^rG_r/(r+1)!\), by choosing the first point and an ordered basis of its difference space, then forgetting order. Multiplication gives \(2^mG_r/(r+1)!\).

The rank count \(N_{a,t}(r)\) follows by choosing an \(r\)-dimensional image subspace of \(\mathbb F_2^a\) and then a surjection from \(\mathbb F_2^t\) to that subspace. Setting the first syndrome row to zero leaves an arbitrary \(m\times t\) matrix, hence the difference and zero-row counts. Finally, when \(m\ge t\), the largest distance \(t+1\) is attained precisely by zero-first-row syndromes of rank \(t\). Their count is \(N_{m,t}(t)\sim2^{mt}\), giving probability \(2^{-t}\) and correction multiplicity \(2^mG_t/(t+1)!\). Every other type contributes \(o(2^m)\) to the uniform-syndrome expected multiplicity, establishing the asymptotic equivalent.

## Verification
The standalone `check_joint.py` enumerates every distinct nonzero-column correction of weight up to the exact covering radius, without using the closed multiplicity formula in generating corrections. It computes syndromes by binary arithmetic and records the minimum weight and number of minimizing corrections for every syndrome. Exhaustive checks include \((m,t)=(2,1),(2,2),(2,3),(3,1),(3,2),(3,3),(4,1),(4,2)\). The largest enumerates \(188{,}707\) corrections and verifies all \(4096\) possible syndromes for \((m,t)=(3,3)\). All types and multiplicities match the theorem. The verifier's last line is `EXACT_JOINT_LEADERS_VERIFY_OK`. The finite checks are independent corroboration; the proof applies to all stated parameters.

For \((m,t)=(3,2)\), the joint profile is: one syndrome of distance zero with one leader; 24 syndromes of distance one with one leader; 168 syndromes of distance two with one leader; 21 syndromes of distance two with four leaders; and 42 syndromes of distance three with eight leaders. These five classes sum to \(256\) syndromes.

## Relationship to prior work
Generalized covering radii and their interpretation as joint query-access complexity were introduced by Elimelech, Firer, and Schwartz (2021). Elimelech, Wei, and Schwartz (2022), Proposition 11, explicitly established the extended Hamming radius \(R_t=\min(m,t)+1\). Li, Shangguan, and Wei (2026) establish the optimal asymptotic rate of generalized covering codes. Their rates and the earlier radius maximum are credited, not claimed as new. The present contribution is the *per-syndrome joint distance and exact multiplicity of all minimum-support solutions*, including the complete finite profile and its exponential list-size phenomenon. A finite-geometric framework for generalized covering radii is provided by Alfarano, Marino, Neri, and Trombetti (2026); that relevant related paper's full text could not be inspected in this check, so equivalent implicit counting formulas there remain a specific priority risk.

## Limitations
The theorem is for the binary extended Hamming family only and concerns jointly minimizing *column-support*, not separately minimizing each row's Hamming error or decoding a random-noise channel. The expected leader count assumes uniform syndromes, not a specified channel distribution. The exact higher covering radius is known from prior work; only the finer syndrome-by-syndrome enumeration and asymptotic multiplicity are proposed as new. Originality remains subject to independent literature assessment, particularly for older finite-geometric and coset-leader enumeration results.

## References
1. H. Li, C. Shangguan, H. Wei, *The Optimal Asymptotic Rate of Generalized Covering Codes*, arXiv:2608.24856, first posted 2026-08-25, https://arxiv.org/abs/2608.24856.
2. D. Elimelech, M. Firer, M. Schwartz, *The Generalized Covering Radii of Linear Codes*, IEEE Transactions on Information Theory 67 (2021), 8070–8085; arXiv:2012.06467, https://arxiv.org/abs/2012.06467.
3. D. Elimelech, H. Wei, M. Schwartz, *On the Generalized Covering Radii of Reed–Muller Codes*, ISIT 2022, Proposition 11; arXiv:2107.09902, https://arxiv.org/abs/2107.09902.
4. G. N. Alfarano, G. Marino, A. Neri, R. Trombetti, *A geometric approach to generalized covering radii of linear codes*, arXiv:2606.16669, https://arxiv.org/abs/2606.16669.
