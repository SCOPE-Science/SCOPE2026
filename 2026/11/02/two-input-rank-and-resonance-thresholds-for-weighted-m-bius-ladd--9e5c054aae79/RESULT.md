# Two-input rank and resonance thresholds for weighted Möbius-ladder consensus

## Finding
For all integers \(n\ge2\) and all real chord conductances \(g>0\), the complete two-adjacent-input Kalman rank and the smallest possible number of independently actuated vertices of a weighted Möbius ladder are given by exact, finite cosine-resonance formulas. In particular, the first loss of two-input controllability is of codimension one for even \(n\), but of codimension four for every odd \(n\ge5\).

Define the collision counts
\[
C_4(n,g)=\#\{(o,e):1\le o<e<n,\;o\equiv1\pmod2,\;e\equiv0\pmod2,\;g=\cos(o\pi/n)-\cos(e\pi/n)\},
\]
\[
C_3(n,g)=\begin{cases}
\#\{o:1\le o<n,\;o\text{ odd},\;g=1+\cos(o\pi/n)\},&n\text{ even},\\
0,&n\text{ odd}.
\end{cases}
\]
Then
\[
\operatorname{rank}[B_{\{0,1\}},L_n(g)B_{\{0,1\}},\ldots,L_n(g)^{2n-1}B_{\{0,1\}}]
=2n-2C_4(n,g)-C_3(n,g).
\]
The exact globally minimum number of independently actuated vertices is
\[
q_n(g)=\begin{cases}
4,&C_4(n,g)>0,\\
3,&C_4(n,g)=0<C_3(n,g),\\
2,&C_4(n,g)=C_3(n,g)=0.
\end{cases}
\]
For every \(n,g\), the minimum is attained by the consecutive vertex set \(\{0,1,\dots,q_n(g)-1\}\). The first positive singular chord conductance is
\[
g_*(n)=\begin{cases}
1-\cos(\pi/n),&n\text{ even},\\
\cos(\pi/n)-\cos(2\pi/n),&n\text{ odd}.
\end{cases}
\]
At this first conductance \(2n-\operatorname{rank}=1\) for even \(n\); it equals \(2\) for \(n=3\) and \(4\) for odd \(n\ge5\). For every \(0<g<g_*(n)\), two adjacent controls are fully controllable.

## Assumptions and scope
Use vertex set \(\mathbb Z/(2n)\) with undirected unit-weight edges \(\{j,j+1\}\) and undirected weight-\(g\) edges \(\{j,j+n\}\), with indices modulo \(2n\). The graph is connected and the Laplacian uses positive edge conductances and nonpositive off-diagonals. The state equation is \(\dot z=-L_n(g)z+B_Uu\), with each column of \(B_U\) a distinct coordinate vector for one independently actuated vertex. Controllability means full real Kalman rank of the resulting linear pair. The two-input formula refers specifically to \(U=\{0,1\}\), while the minimum-number statement optimizes over all vertex subsets. The parameter \(g\) is arbitrary and strictly positive; there is no assumption of generic or random rates.

## Proof
**Fourier spectrum.** Let \(S\) be cyclic translation by one vertex. The Laplacian equals \(L_n(g)=2I-S-S^{-1}+g(I-S^n)\). On the Fourier vectors \(f_k(j)=\exp(\pi i k j/n)\), where \(0\le k<2n\), its eigenvalues are
\[
\Lambda_k(g)=2-2\cos(\pi k/n)+g(1-(-1)^k).
\]
Put \(d_k=2-2\cos(\pi k/n)\) for \(0\le k\le n\). The frequencies \(k\) and \(2n-k\) have the same eigenvalue, furnishing multiplicity two when \(1\le k<n\) and multiplicity one for \(k=0,n\). Since \(d_0<d_1<\cdots<d_n\), eigenvalues from distinct representatives of the same parity cannot collide. The only possible positive-\(g\) collision is an unshifted even representative \(e\) with a shifted odd representative \(o<e\):
\[
2g=d_e-d_o=2\big(\cos(o\pi/n)-\cos(e\pi/n)\big).
\]
When \(e<n\), the two conjugate-frequency pairs create a four-dimensional eigenspace. When \(e=n\), possible only for even \(n\), the endpoint frequency is single and the colliding eigenspace has dimension three. Every other eigenspace has dimension at most two. A single spectral value cannot contain two different representatives of a fixed parity, so all collisions counted by \(C_4\) and \(C_3\) occur at distinct eigenvalues. In particular, no hidden higher multiplicity is possible, even if several distinct collision equalities hold for the same \(g\).

**Exact two-input reachable rank.** For real symmetric \(L_n(g)\), the orthogonal spectral decomposition and the PBH test imply that the reachable dimension equals the sum, over distinct eigenspaces \(E_\lambda\), of the ranks of the control projections onto those eigenspaces. For \(q\) consecutive input vertices \(\{0,\ldots,q-1\}\), a complex Fourier basis of an eigenspace with distinct frequencies \(k_1,\ldots,k_m\) restricts to the rectangular Vandermonde matrix \((\zeta_{k_a}^{\,j})_{0\le j<q,1\le a\le m}\), where \(\zeta_k=\exp(\pi i k/n)\). Its rank is exactly \(\min(q,m)\), since the roots \(\zeta_{k_a}\) are distinct and its relevant square Vandermonde minors do not vanish. Passing from complex Fourier coordinates back to real eigenspaces preserves rank. With \(q=2\), the only lost directions are two per fourfold collision and one per threefold collision. This proves the displayed exact Kalman-rank formula, including simultaneous distinct resonances.

**Sharp minimum actuation.** Every eigenspace of dimension \(m\) requires at least \(m\) independent control columns by PBH; the largest multiplicity here is exactly the specified \(q_n(g)\). The preceding Vandermonde argument shows that \(q_n(g)\) consecutive columns have full projection rank on every eigenspace, proving both feasibility and optimality for all vertex subsets.

**First resonance and its deficit.** Let \(t=\pi/n\). For each even \(e\), the smallest possible positive collision rate with any smaller odd \(o\) is \(\cos((e-1)t)-\cos(et)=2\sin((e-1/2)t)\sin(t/2)\), attained uniquely at \(o=e-1\). The sine factors are smallest at the permitted interval nearest either endpoint of \((0,\pi)\). For odd \(n\), the even indices range from \(2\) through \(n-1\); their minimum occurs at \(e=2\) and \(e=n-1\), with equal value \(\cos t-\cos2t\). At \(n=3\) these are the same collision; for every odd \(n\ge5\) they produce two distinct four-dimensional eigenspaces, hence a deficit of four. For even \(n\), the endpoint \(e=n\), paired with \(o=n-1\), has rate \(1-\cos t=2\sin^2(t/2)\), strictly less than every internal even collision rate (which is at least \(2\sin(3t/2)\sin(t/2)\)). It creates exactly one three-dimensional eigenspace and loses one reachable direction. This proves the first-resonance thresholds and deficits, with all boundary cases \(n=2,3\) included.

## Verification
The standalone `verify.py` constructs every weighted Laplacian directly from its edges and checks its eigenvalues against the Fourier formula, its spectral multiplicities against the proposed resonance sets, and consecutive-control PBH ranks over \(663\) independently selected graph/rate pairs with \(2\le n\le24\), including all explicitly generated resonance rates and several nonresonant rates. It also checks the two-control reachable dimension by independent numerical eigenspace projections at the first resonance through \(n=20\), and computes exact rational Kalman matrices at \((n,g)=(2,1),(3,1),(4,1/2)\). The script reports \(24{,}847\) passing checks. These finite computations test the formula and implementation; the proof of the universal quantifiers is the preceding analytic argument.

For illustration, at \(n=3,g=1\) (six vertices), the two-input rank is \(4\) and four independent controls are required. At \(n=4,g=1-\sqrt2/2\) (eight vertices), the two-input rank is \(7\) and three independent controls are required. At \(n=5,g=1/2\) (ten vertices), the two-input rank is \(6\): two different fourfold spectral collisions coexist, and four independent controls are required.

## Relationship to prior work
Yuan and collaborators (2013) established a general maximum-eigenvalue-multiplicity framework for exact controllability. Nabi-Abdolyousefi and Mesbahi (2013) specifically established a minimum-leader characterization for weighted circulant Laplacians; their abstract is directly relevant to the minimum-actuator part of this theorem. Accordingly **neither the general multiplicity lower bound nor the generic circulant minimum-leader principle is claimed as new**. Monshizadeh, Zhang and Camlibel (2014) give a different strong-structural zero-forcing viewpoint, explicitly citing the earlier circulant result.

The contribution asserted here is the complete conductance-dependent **reachable rank of the two prescribed adjacent controls**, its exact fourfold/threefold collision sets for antipodal weighted cycles, and the sharp parity-dependent first resonance including its two-versus-four-dimensional loss. These statements do not follow from merely knowing that the optimal number of leaders equals the largest eigenvalue multiplicity: that general invariant alone does not determine the reachable rank of a fixed two-vertex control set, nor the number of distinct co-resonant eigenspaces at a given chord weight. The explicit rank formula and its threshold are deductions from the family-specific spectral structure and the restricted Fourier minors.

## Limitations
The theorem concerns constant weight \(g\) on every antipodal matching edge, unit ring weights and independently controlled coordinate inputs. It does not assert robustness to arbitrary perturbations of individual weights, optimal controllability Gramians, bounded control energy, or strong structural controllability under all graph-compatible matrices. The first resonance is a discrete conductance, not a whole interval of uncontrollability; other isolated resonances occur at higher conductances. The full text of the closely related 2013 circulant-control paper could not be inspected, so possible specialized historical coverage remains a significant originality risk. The reported computational checks are finite, and independent mathematical validation has not been performed.

## References
1. Zhengzhong Yuan et al., *Exact controllability of complex networks*, Nature Communications 4:2447 (public September 12, 2013), DOI: https://doi.org/10.1038/ncomms3447; full open-access article: https://pmc.ncbi.nlm.nih.gov/articles/PMC3945876/.
2. Marzieh Nabi-Abdolyousefi and Mehran Mesbahi, *On the Controllability Properties of Circulant Networks*, IEEE Transactions on Automatic Control 58(12), 3179–3184 (2013), DOI: https://doi.org/10.1109/TAC.2013.2259992 (abstract checked; full paper unavailable).
3. Nima Monshizadeh, Shuo Zhang and M. Kanat Camlibel, *Zero forcing sets and controllability of dynamical systems defined on graphs*, arXiv:1403.4868v1 (March 19, 2014), full open-access text: https://arxiv.org/pdf/1403.4868.
