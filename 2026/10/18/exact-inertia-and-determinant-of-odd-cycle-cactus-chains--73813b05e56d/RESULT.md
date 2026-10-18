# Exact inertia and determinant of odd-cycle cactus chains

## Finding

For every integer \(t\ge3\), let \(G\) be a block-path cactus consisting of \(t\) odd cycle blocks of lengths \(\ell_1,\ldots,\ell_t\ge3\), with each successive pair sharing one vertex and no further overlaps, and with distinct incoming and outgoing attachment vertices in each internal block. Set
\[
H=\frac12\sum_{i=1}^{t}(\ell_i-1),\qquad q=|\{i:\ell_i\equiv1\pmod4\}|.
\]
The line-graph adjacency matrix has no zero eigenvalue and has inertia
\[
\operatorname{In}(A(L(G)))=\begin{cases}(H,0,H+t),&q=0,\\(H+1,0,H+t-1),&q\ge1.\end{cases}
\]
Moreover
\[
\det A(L(G))=\begin{cases}2^t,&q=0,\\(-1)^{q-1}2^{t-1}(4q-2),&q\ge1.\end{cases}
\]
Inertia and determinant are independent of the particular odd lengths except for their residue classes modulo four, and of the attachment positions. The same identities remain valid for the known degenerate block-path cases \(t=1,2\); the new multi-articulation scope is \(t\ge3\).

## Assumptions and scope

All graphs are finite, undirected, loopless, and simple. A cactus has each edge in at most one cycle. The block graph here is a path with blocks exactly the stated odd cycles, not a chain connected by bridge edges; the two cut vertices of each internal cycle are distinct. The line graph has one vertex for each edge of \(G\), with two vertices adjacent precisely when their edges meet. For a real symmetric matrix, inertia is the ordered triple (number of positive eigenvalues, number of zero eigenvalues, number of negative eigenvalues), counted with multiplicity. The result covers all odd lengths and all distinct internal attachment positions, with no bound on \(t\).

## Proof

**1. Passage to the signless Laplacian.** Write \(Q(G)=D(G)+A(G)\), and \(M(G)=Q(G)-2I\). Let \(N\) be the unsigned vertex-edge incidence matrix. Then \(NN^{\mathsf T}=Q(G)\) and \(N^{\mathsf T}N=A(L(G))+2I\). Because \(G\) is connected and contains odd cycles, \(N\) has full row rank. If \(n=|V(G)|=2H+1\) and \(m=|E(G)|=2H+t\), the nonzero eigenvalues of \(NN^{\mathsf T}\) and \(N^{\mathsf T}N\) coincide with multiplicities. Consequently \(A(L(G))\) is spectrally equivalent to \(M(G)\) together with exactly \(m-n=t-1\) eigenvalues equal to \(-2\). In particular its inertia is the inertia of \(M(G)\) with \(t-1\) additional negative entries, and
\[
\det A(L(G))=(-2)^{t-1}\det M(G).
\]

**2. The initial cycle.** For a single odd cycle \(C_{2h+1}\), all degrees are two and hence \(M(C_{2h+1})=A(C_{2h+1})\). Its eigenvalues are \(2\cos(2\pi j/(2h+1))\) for \(0\le j\le2h\), none zero. These give \((h,0,h+1)\) for lengths congruent to three modulo four and \((h+1,0,h)\) for lengths congruent to one modulo four. The adjacency determinant of an odd cycle is \(2\). By Cramer's rule at any vertex \(v\), deleting the row and column leaves the even path \(P_{2h}\); since \(\det A(P_{2h})=(-1)^h\),
\[
(M(C_{2h+1})^{-1})_{vv}=(-1)^h/2.
\]

**3. Eliminate an appended cycle.** Suppose a new odd cycle \(C_{2h+1}\) is coalesced with the current terminal cycle at an available vertex \(v\). Order its \(2h\) new vertices along the path obtained after deleting \(v\), and let \(B=A(P_{2h})\), \(e=e_v\), \(b=e_1+e_{2h}\). The new shifted signless Laplacian is
\[
\widetilde M=\begin{pmatrix}M+2ee^{\mathsf T}& eb^{\mathsf T}\\be^{\mathsf T}&B\end{pmatrix}.
\]
The even path matrix is nonsingular with inertia \((h,0,h)\), determinant \((-1)^h\), zero diagonal in its inverse, and
\[
b^{\mathsf T}B^{-1}b=2(-1)^{h-1},\qquad |(B^{-1}b)_w|=1\quad(1\le w\le 2h).
\]
These identities follow directly from the tridiagonal path recurrence \(x_{j-1}+x_{j+1}=b_j\) with zero boundary values (or multiplication by \(B\)). The Schur complement is
\[
S=M+[2-2(-1)^{h-1}]ee^{\mathsf T}
=\begin{cases}M,&h\text{ odd},\\M+4ee^{\mathsf T},&h\text{ even}.\end{cases}
\]
Congruence gives \(\operatorname{In}(\widetilde M)=\operatorname{In}(S)+(h,0,h)\), and \(\det\widetilde M=(-1)^h\det S\).

**4. Track the single boundary resolvent.** For an invertible current \(M\), denote \(g=(M^{-1})_{vv}\). The new terminal vertex \(w\) can be any as-yet-unidentified vertex on the appended cycle (distinct from \(v\)). Block inversion and the preceding path identities give
\[
(\widetilde M^{-1})_{ww}=\begin{cases}g,&h\text{ odd},\\g/(1+4g),&h\text{ even},\end{cases}
\]
provided \(1+4g\ne0\), and the determinant ratio is \((-1)^h\) or \((-1)^h(1+4g)\), respectively. Starting with an odd cycle, the boundary value is \(-1/2\) when no \(1\pmod4\) cycle has been encountered, and after exactly \(q\ge1\) such cycles it is \(1/(4q-2)\). Indeed a \(3\pmod4\) attachment leaves it fixed, while a \(1\pmod4\) attachment sends \(-1/2\) to \(+1/2\), then sends \(1/(4q-2)\) to \(1/(4(q+1)-2)\). In every case \(1+4g\ne0\); therefore all shifted signless Laplacians in the induction are nonsingular. This argument works for *every* free outgoing attachment vertex, not just one choice.

**5. Inertia and determinant.** A \(3\pmod4\) attachment contributes \(h\) positive and \(h\) negative eigenvalues to \(M\). A \(1\pmod4\) attachment contributes the same \((h,h)\) from \(B\), and the positive-semidefinite rank-one update \(M\mapsto M+4ee^{\mathsf T}\). Exactly on the first \(1\pmod4\) attachment following one or more \(3\pmod4\) blocks, \(1+4g=-1\); a single negative eigenvalue becomes positive (inertia changes by \((+1,0,-1)\)). After that \(g>0\), the rank-one update changes no signs. The initial cycle has one more negative eigenvalue if it is \(3\pmod4\), and one more positive eigenvalue if it is \(1\pmod4\). Since \(n=2H+1\), the final inertia of \(M\) is \((H,0,H+1)\) for \(q=0\), and \((H+1,0,H)\) for \(q\ge1\). Adding \(t-1\) negative eigenvalues proves the claimed inertia of the line graph.

For determinants, the initial cycle contributes \(2\); each \(3\pmod4\) addition multiplies \(\det M\) by \(-1\). For \(1\pmod4\), the multiplier is \(1+4g\); the first such addition after \(3\pmod4\) blocks contributes \(-1\), and all subsequent ones telescope as \((4(q+1)-2)/(4q-2)\). Therefore
\[
\det M(G)=\begin{cases}2(-1)^{t-1},&q=0,\\(-1)^{t-q}(4q-2),&q\ge1.\end{cases}
\]
Multiplication by \((-2)^{t-1}\) proves the determinant formula. These computations also establish nonsingularity and complete the proof.

## Verification

The accompanying standalone `verify.py` checks the theorem against an independent construction of the line-graph adjacency and of the signless Laplacian, with exact rational inertia via symmetric congruence and integer determinant via the fraction-free Bareiss algorithm. It tests 1,254 odd-cycle chains over block counts one through five, lengths three, five, seven, nine (subject to explicit size cutoffs), varying internal articulation positions. All passed. A non-path branching comparison has inertia \((10,0,10)\) and determinant \(400\). Run `python3 verify.py`; its expected output is embedded in `verification_output.txt`. Exhaustive finite tests confirm cases only; the induction above is the proof for arbitrary lengths and block counts.

## Relationship to prior work

Francis and Uptain (arXiv:2607.22874, first posted 2026-07-24) obtain unbounded *positive* line-graph signature by connecting larger cactus gadgets with **bridges**. Their graph operation and conclusions do not determine exact inertia or determinants for odd-cycle chains **glued at vertices**.

Paone and Paone (DOI:10.5281/zenodo.21744051, posted 2026-08-01) classify the line-graph inertia of **roses** (cycles all incident at a single central vertex) and generalized theta graphs. Their Section 10 gives a one-sided inequality and local elimination recurrences for general bridgeless cacti, but not a complete inertia/determinant formula for the block-path family with distinct successive cut vertices. The instances with one or two cycle blocks are therefore acknowledged as previously covered; the non-rose path family begins at three blocks. The elimination of a leaf cycle parallels their Schur-complement method, while the exact boundary-resolvent induction and determinant classification resolve an additional infinite family.

Wang and Fan (arXiv:1310.1003, 2013) establish general line-graph signature bounds and special families. Their inequalities do not specify the present complete two-case inertia, nonsingularity, or determinant.

## Limitations

Only odd cycle blocks with a **path-shaped** block-cut tree are covered. The path hypothesis cannot simply be removed: a central pentagon with three further pentagons coalesced at three distinct consecutive central vertices has line-graph inertia \((10,0,10)\) and determinant \(400\), whereas the path formula for four pentagons would yield inertia \((9,0,11)\) and determinant \(-112\). No assertion is made for even cycles, bridges, arbitrary branching, weighted edges, or spectra beyond inertia and determinant. Possible equivalent work in unindexed or inaccessible literature remains a residual priority risk. No independent external mathematical audit has occurred.

## References

1. Luke Francis and Trevor Uptain, *The signature of connected line graphs is unbounded*, arXiv:2607.22874v1 (2026-07-24), https://arxiv.org/abs/2607.22874.
2. Andrea Paone and Marco Paone, *Line-graph inertia of roses and generalized theta graphs* (2026-08-01), DOI:10.5281/zenodo.21744051, https://aletheia-technologies.it/en/research/line-graph-inertia-roses-generalized-theta/reader/.
3. Long Wang and Yi-Zheng Fan, *The signature of line graphs and power trees*, arXiv:1310.1003 (2013), https://arxiv.org/abs/1310.1003.
