# Four-residue orbit, basin, and flip-mask classification for parity dynamics on two-set Kneser graphs

## Finding

**Theorem.** For every integer \(n\geq5\), let \(G_n=KG(n,2)\) be the graph whose vertices are the two-element subsets of \(\{1,\ldots,n\}\), with edges joining disjoint pairs. Set \(N=\binom n2\) and let \(F_n:\mathbb F_2^N\to\mathbb F_2^N\) simultaneously update every binary state by the XOR of the states at all neighboring vertices. Then every initial configuration is periodic immediately or becomes periodic after exactly one update. Only primitive periods one and two occur.

There is a complete four-residue classification. Write \(Q_1\) for the number of fixed states, \(Q_2\) for the number of primitive two-cycle *orbits*, \(P\) for the number of periodic states, and \(b\) for the common number of initial configurations in the basin of each fixed point (the entire basin, including the fixed point):

| \(n\bmod4\) | Identity | \(Q_1\) | \(P\) | \(Q_2\) | \(b\) |
|---|---|---|---|---|---|
| \(0\) | \(F_n^2=I\) | \(2^{N-n+1}\) | \(2^N\) | \((2^N-2^{N-n+1})/2\) | \(1\) |
| \(1\) | \(F_n^3=F_n\) | \(2^{N-n}\) | \(2^{N-n+1}\) | \(2^{N-n-1}\) | \(2^{n-1}\) |
| \(2\) | \(F_n^3=F_n\) | \(2^{N-n+1}\) | \(2^{N-1}\) | \((2^{N-1}-2^{N-n+1})/2\) | \(2\) |
| \(3\) | \(F_n^2=F_n\) | \(2^{N-n}\) | \(2^{N-n}\) | \(0\) | \(2^n\) |

Each primitive two-cycle has an attraction basin of exactly \(2b\) configurations, so the stated table gives the complete basin-size distribution, not just the orbit counts. In the residue class \(0\), the map is bijective and every state is periodic at time zero; in the other three classes the maximum first-periodic-entry time is exactly one.

**Spatial oscillation masks.** For any primitive two-cycle \((x,F_n(x))\), call \(d=x+F_n(x)\) its flip mask (addition modulo two). For \(S\subseteq\{1,\dots,n\}\), write \(\delta(S)\) for the binary indicator of the edges of \(K_n\) crossing from \(S\) to its complement, viewed as a state on the two-subsets. Define the set of **even cuts**
\[
\mathcal C_n=\{\delta(S):|S|\text{ is even}\}.
\]
The distinct nonzero flip masks, together with the number of primitive two-cycle orbits having *each* such mask, are:

| \(n\bmod4\) | Exact allowed nonzero flip masks \(d\) | Two-cycle orbits for each \(d\) |
|---|---|---|
| \(0\) | \((\mathcal C_n\cup({\bf1}_N+\mathcal C_n))\setminus\{0\}\) | \(2^{N-n}\) |
| \(1\) | only \({\bf1}_N\) (every vertex flips) | \(2^{N-n-1}\) |
| \(2\) | \(\mathcal C_n\setminus\{0\}\) | \(2^{N-n}\) |
| \(3\) | none | \(0\) |

In particular, for \(n\equiv1\pmod4\), **every oscillation is a global complement**, while for \(n\equiv2\pmod4\) oscillations flip precisely the pairs crossing an even-cardinality cut. This also specifies exact flip-weight counts: for \(w>0\), the number \(M_n(w)\) of distinct permissible masks of Hamming weight \(w\) is
\[
M_n(w)=\begin{cases}
\tfrac12\!\displaystyle\sum_{\substack{0\le k\le n\\k\ \mathrm{even}}}\!\binom nk\bigl({\bf1}_{\{w=k(n-k)\}}+{\bf1}_{\{w=N-k(n-k)\}}\bigr), &n\equiv0\pmod4,\\
{\bf1}_{\{w=N\}},&n\equiv1\pmod4,\\
\tfrac12\!\displaystyle\sum_{\substack{0\le k\le n\\k\ \mathrm{even}}}\!\binom nk{\bf1}_{\{w=k(n-k)\}},&n\equiv2\pmod4,\\
0,&n\equiv3\pmod4
\end{cases}.
\]
Multiplying by the per-mask orbit count in the preceding table gives the exact Hamming-flip distribution of primitive two-cycle orbits for every graph order.

## Assumptions and scope

All arithmetic is in \(\mathbb F_2\). The update is **neighbor-exclusive**: the old state of a vertex is not separately included unless that vertex is adjacent to itself; here there are no loops. Graphs are finite, simple, undirected, and \(n\ge5\). Configurations are labelled by the underlying two-element subsets. A primitive two-cycle is counted up to cyclic interchange of its two temporal phases, but **not** up to spatial graph automorphisms. For any periodic orbit, the basin comprises all initial states whose forward iterations eventually enter that orbit; entrance time is the least nonnegative such time.

## Proof

Let \(B\) be the \(n\times N\) vertex-edge incidence matrix of the complete graph \(K_n\), over \(\mathbb F_2\); each column has two unit entries. Define \(T=B^{\mathsf T}B\), and let \(J\) be the all-ones \(N\times N\) matrix. For two distinct 2-subsets \(S,U\), the entry \(T_{S,U}\) is one exactly when \(S\cap U\) has odd cardinality. Its diagonal entries vanish because each 2-subset has size two. Hence the adjacency matrix \(A\) of \(KG(n,2)\) obeys the exact identity
\[
A=I+T+J.\tag{1}
\]
Indeed, for disjoint distinct subsets, only \(J\) contributes; for meeting distinct subsets, \(T+J\) cancels; and on the diagonal \(I+J\) cancels.

The incidence matrix satisfies
\[
BB^{\mathsf T}=J_n+(n\bmod2)I_n,\qquad B^{\mathsf T}{\bf1}_n=0.
\]
Therefore
\[
T^2=(n\bmod2)T,\quad TJ=JT=0,\quad J^2=(N\bmod2)J.\tag{2}
\]
To check the middle equality, note that \(B{\bf1}_N=(n-1\bmod2){\bf1}_n\), so \(T{\bf1}_N=B^{\mathsf T}B{\bf1}_N=0\); symmetry gives both products. The parity of \(N\) is even for \(n\equiv0,1\pmod4\) and odd for \(n\equiv2,3\pmod4\). Consequently, squaring and cubing (1) in characteristic two proves
\[
A^2=I\ (n\equiv0),\qquad A^3=A\ (n\equiv1,2),\qquad A^2=A\ (n\equiv3)\pmod4.\tag{3}
\]
Each identity implies that \(A\) acts as an involution on its image, or is an involution on the whole space. Thus all eventual periods divide two and each state reaches its eventual orbit by one update.

For ranks, \(\operatorname{im}B\) is precisely the even-weight subspace of \(\mathbb F_2^n\), of dimension \(n-1\), while \(\ker B^{\mathsf T}\) is spanned by \({\bf1}_n\). The latter vector lies in \(\operatorname{im}B\) if and only if \(n\) is even. It follows that
\[
\operatorname{rank}T=\begin{cases}n-2,&n\text{ even},\\ n-1,&n\text{ odd}.\end{cases}\tag{4}
\]
Moreover \({\bf1}_N\notin\operatorname{im}B^{\mathsf T}\): otherwise values \(u_i\in\mathbb F_2\) would satisfy \(u_i+u_j=1\) for every distinct pair \(i,j\), contradicted by adding the three equations on any triangle. Therefore \(\operatorname{im}T\cap\operatorname{im}J=\{0\}\), and since \(T,J\) are symmetric their common kernel has codimension \(\operatorname{rank}T+1\). The fixed-state equation \(Ax=x\) is exactly \((T+J)x=0\). Thus
\[
Q_1=2^{N-\operatorname{rank}T-1},\tag{5}
\]
which produces the stated even and odd cases.

The rank of \(A\) follows without spectral diagonalization. For \(n\equiv0\), (3) makes \(A\) invertible. For \(n\equiv1\), \(T\) is a projector and \(J\) is square-zero; because \(TJ=JT=0\), \(A\) vanishes on \(\operatorname{im}T\) and restricts to the invertible map \(I+J\) on \(\ker T\), so \(\operatorname{rank}A=N-(n-1)\). For \(n\equiv2\), \(J\) is a rank-one projector and \(T\) is square-zero; \(A\) vanishes on \(\operatorname{im}J\) and restricts to the invertible map \(I+T\) on \(\ker J\), so \(\operatorname{rank}A=N-1\). For \(n\equiv3\), both \(T,J\) are annihilating projectors, and \(A=I+T+J\) is the complementary projector of rank \(N-(n-1)-1=N-n\). These four rank formulas give the exponent of \(P=|\operatorname{im}A|\), since every image state is periodic by (3).

There are \(P-Q_1\) states with primitive period two, so \(Q_2=(P-Q_1)/2\). Every state has exactly \(2^{N-\operatorname{rank}A}=b\) preimages under \(A\) whenever the target lies in its image; as \(A\) permutes that image, every periodic orbit receives the same number of preimage fibers per orbit point. Its entire basin therefore has size \(b\) or \(2b\). The projection and noninvertible rank deficits in (4) make one-step entry sharp whenever \(n\not\equiv0\pmod4\). This proves all assertions.


For the stronger spatial flip-mask claim, let \(D=A+I=T+J\). On a periodic orbit, its flip mask is \(Dx\), with \(x\in\operatorname{im}A\). From the identities (2), the linear map \(DA\) is equal to \(D\), \(J\), \(T\), or \(0\) as \(n\equiv0,1,2,3\pmod4\), respectively. Thus the allowed flip masks are precisely the nonzero vectors in \(\operatorname{im}D\), \(\operatorname{im}J\), \(\operatorname{im}T\), or the empty set, respectively. (For \(n\equiv0\), \(A\) is invertible and \(\operatorname{im}D=\operatorname{im}(DA)\).)

The incidence operator maps a vertex indicator \({\bf1}_S\in\mathbb F_2^n\) to the cut indicator \(B^{\mathsf T}{\bf1}_S=\delta(S)\). For even \(n\), the column space of \(B\) consists of even-weight vertex indicators, and therefore \(\operatorname{im}T=\mathcal C_n\). The vector \({\bf1}_N\) is not in that image, so \(\operatorname{im}(T+J)=\mathcal C_n\mathbin\oplus\langle{\bf1}_N\rangle\). For odd \(n\), \(\operatorname{im}J=\langle{\bf1}_N\rangle\). This proves the three nontrivial flip-mask classes. Their vector-space dimensions are respectively \(n-1\), \(1\), and \(n-2\); the zero class is clear. The restriction \(D|_{\operatorname{im}A}\) has those images and constant fibers of sizes \(2^{\operatorname{rank}A-\dim\operatorname{im}(DA)}\). Each nonzero mask occurs in exactly half as many two-cycle orbits as periodic states realizing it. Substituting the already proved ranks gives the per-mask orbit counts.

For the weight formula, \(\delta(S)\) has exactly \(|S|(n-|S|)\) ones. Because \(n\) is even in the relevant residues, \(S\) and \(S^c\) are both even or both odd, and each even cut is represented by exactly two even subsets. The complementary mask \({\bf1}_N+\delta(S)\) has weight \(N-|S|(n-|S|)\), and never equals an ordinary cut (no nonempty complete-graph cut has complement itself a cut on a triangle). Summing binomial choices and dividing by two gives the stated expression for every \(w>0\). The odd classes follow immediately. This completes the mask and multiplicity classification.

## Verification

The attached standalone script `check_linear.py` constructs the full binary adjacency matrix independently from disjointness of two-element subsets, performs exact Gaussian elimination over \(\mathbb F_2\), and verifies all four formulas, fixed-state ranks and operator identities for every \(5\le n\le17\). Execute `python3 check_linear.py`; the provided `check_linear.out` ends with `LINEAR_VERIFY_OK`.

The additional `check_flips.py` independently constructs the image of the two-cycle flip map and enumerates its cut masks for \(5\le n\le16\), checking that the per-mask two-cycle multiplicities sum to the orbit census. Run `python3 check_flips.py`; `check_flips.out` ends with `FLIPS_VERIFY_OK`.

The independently written C++ program `check_states.cpp` uses bit-parity neighbor masks and tests every labelled initial configuration for \(n=5,6,7\), totaling \(2^{10}+2^{15}+2^{21}=2{,}130{,}944\) configurations; it checks the actual sequence of iterates and exactly counts fixed points, two-cycle states, and first-periodic-entry times. Rebuild with `c++ -O2 -std=c++17 check_states.cpp -o check_states` and run `./check_states`; `check_states.out` ends with `STATES_VERIFY_OK`.

These finite checks are illustrations and independent error-detection, **not** replacements for the all-\(n\) proof above. No assumption about untested configurations enters the proof.

## Relationship to prior work

The exact characteristic-two incidence calculation is related to classical work on modular ranks of graph adjacency matrices. Van Eijl's 1991 thesis, Section 2.2, Proposition 2.5, computes the integral Smith normal form of the adjacency matrix of the *triangular graph* \(T(n)=L(K_n)\), which is the complement of \(KG(n,2)\). That is an important algebraic antecedent, but its stated calculation is not a dynamical orbit or basin theorem. Brouwer and Fiol's 2014 paper studies Kneser distance graphs through ordinary eigenspaces and Bose–Mesner algebras; its conclusions do not assert the binary parity-update identities or the four-residue attraction-basin census here. The present theorem concerns the binary update itself and the resulting labelled functional graph.

## Limitations

The result covers only two-set Kneser graphs, binary arithmetic, and exclusive-neighbor XOR updating. It does not classify other Kneser parameters, nonlinear majority updates, spatial orbit equivalence classes, or arbitrary finite graph dynamics. Closely related historical p-rank results make some rank information accessible by other routes; the distinction claimed here is the complete time-dynamical classification, not a claim to have first calculated every related matrix rank. An unindexed earlier dynamical formulation remains possible. The report has received self-review only; no independent audit is claimed.

## References

- A. E. Brouwer and M. A. Fiol, *Distance-regular graphs where the distance-d graph has fewer distinct eigenvalues*, first made public September 1, 2014, arXiv:1409.0389, https://arxiv.org/abs/1409.0389.
- C. A. van Eijl, *On the p-rank of the adjacency matrices of strongly regular graphs*, master's thesis, Eindhoven University of Technology, October 1991, Section 2.2, Proposition 2.5, https://aeb.win.tue.nl/preprints/361304.pdf.
- A. E. Brouwer and C. A. van Eijl, *On the p-rank of the adjacency matrices of strongly regular graphs*, Journal of Algebraic Combinatorics 1 (1992), 329–346.
