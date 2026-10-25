# Complete line-graph adjacency inertia and sharp signature threshold for cycle dumbbells

## Finding
Let \(B(a,b,d)\) be two vertex-disjoint simple cycles of lengths \(a,b\ge3\), joined at distinguished vertices by a path of \(d\ge1\) edges whose internal vertices lie outside the cycles. The adjacency inertia of its line graph is determined exactly by Theorem 1 below. In particular,
\[
\operatorname{sig}(A(L(B(a,b,d))))\le1,
\]
with equality **if and only if** \(d\) is odd, both \(a,b\) are congruent to \(0\) or \(1\) modulo \(4\), and at least one is congruent to \(1\). The theorem also determines every zero-eigenvalue multiplicity, including all singular cases.

**Theorem 1 (complete inertia).** Write \(\operatorname{In}(H)=(n_+(H),n_0(H),n_-(H))\), counting eigenvalues of a real symmetric matrix above, at, and below zero with multiplicity. Put
\[
q(t)=\left\lfloor\frac{t-1}{2}\right\rfloor+\mathbf1_{\{t\equiv2\pmod4\}},\qquad z(t)=\mathbf1_{\{t\equiv0\pmod4\}}.
\]
For a cycle length \(t\not\equiv2\pmod4\), give the corresponding endpoint the weight
\[
w(t)=\begin{cases}1&t\equiv0\pmod4,\\3&t\equiv1\pmod4,\\-1&t\equiv3\pmod4.\end{cases}
\]
An endpoint of residue \(2\) is called *deleted* and has no weight. Define the three-component residual inertia \(U(a,b,d)=(u_+,u_0,u_-)\) as follows.

**No endpoint deleted.** Write \(\alpha=w(a),\ \beta=w(b)\). If \(d=2h\), then
\[
U=\big(h+\mathbf1_{\{\alpha+\beta>0\}},\ \mathbf1_{\{\alpha+\beta=0\}},\ h+\mathbf1_{\{\alpha+\beta<0\}}\big).
\]
If \(d=2h+1\), then \(U=(h,h_0,h)+\operatorname{In}(T)\), where \(h_0=0\), componentwise, and
\[
T=\begin{pmatrix}\alpha&1\\1&\beta\end{pmatrix}.
\]
Here \(\operatorname{In}(T)\) is explicit from its trace \(\alpha+\beta\) and determinant \(\alpha\beta-1\): if the determinant is negative the triple is \((1,0,1)\); if zero, it is \((1,1,0)\) for positive trace or \((0,1,1)\) for negative trace; if positive it is \((2,0,0)\) or \((0,0,2)\) according as the trace is positive or negative.

**Exactly one endpoint deleted.** Let \(w\) be the retained endpoint weight. If \(d=2h\), then \(U=(h,0,h)\). If \(d=2h+1\), then
\[
U=(h+\mathbf1_{\{w>0\}},0,h+\mathbf1_{\{w<0\}}).
\]

**Both endpoints deleted.** For every \(d\ge1\),
\[
U=\left(\left\lfloor\frac{d-1}{2}\right\rfloor,\mathbf1_{\{d\text{ even}\}},\left\lfloor\frac{d-1}{2}\right\rfloor\right).
\]

In all cases, with \(U=(u_+,u_0,u_-)\),
\[
\boxed{\operatorname{In}A(L(B(a,b,d)))=(q(a)+q(b)+u_+,\ z(a)+z(b)+u_0,\ q(a)+q(b)+u_-+1).}
\]
The three entries always sum to \(a+b+d=|E(B(a,b,d))|\).

**Corollary 2 (signature classification).** Let \(r=a\bmod4\) and \(s=b\bmod4\). The signature depends only on \((r,s)\) and the parity of \(d\). For **odd** \(d\): (i) when neither residue equals \(2\), it is \(+1\) if both residues lie in \(\{0,1\}\) and at least one equals \(1\), it is \(0\) if both equal \(0\), it is \(-2\) if both equal \(3\), and it is \(-1\) in the other cases; (ii) when exactly one residue equals \(2\), it is \(-2\) if the other equals \(3\) and \(0\) otherwise; (iii) when both equal \(2\), it is \(-1\). For **even** \(d\): the signature equals \(-1\) if at least one residue equals \(2\), equals \(-2\) when both equal \(3\), equals \(-1\) when the residue multiset is \(\{0,3\}\), and equals \(0\) otherwise. In particular, the signature can be only \(-2,-1,0,1\) for this family.

**Corollary 3 (zero multiplicity).** The zero index equals \(\mathbf1_{\{a\equiv0\pmod4\}}+\mathbf1_{\{b\equiv0\pmod4\}}\) plus exactly one if: (i) \(d\) is odd and \((r,s)=(0,0)\) or \((3,3)\); or (ii) \(d\) is even and either \(\{r,s\}=\{0,3\}\) or \((r,s)=(2,2)\). In all other cases there is no extra zero eigenvalue.

## Assumptions and scope
All graphs are finite, simple and undirected. The two cycles are vertex-disjoint before adding their joining path. The path length is the number of *edges*, not internal vertices; in particular \(d=1\) is a single bridge. The indicated cycle lengths and path length are arbitrary integers in their stated ranges. A signature is the number of positive adjacency eigenvalues minus the number of negative ones. All multiplicities include algebraic multiplicity, equal to geometric multiplicity for these real symmetric matrices.

## Proof
**Step 1 (incidence transfer).** Put \(n=a+b+d-1\), \(m=a+b+d=n+1\), \(Q=D+A\) and \(M=Q(B)-2I_n\). With the nonoriented vertex-edge incidence matrix \(N\), one has \(NN^T=Q(B)\) and \(N^TN=A(L(B))+2I_m\). Their nonzero eigenvalues agree, including multiplicity. Their kernels have dimensions differing by \(m-n=1\), whether or not \(B\) is bipartite. Hence
\[
\operatorname{In}A(L(B))=\operatorname{In}M+(0,0,1).
\]
This established incidence identity is not claimed as new.

**Step 2 (each cycle is an exact endpoint gadget).** Denote its attachment vertex by \(v\). In \(M\), the \(t-1\) other vertices of a cycle \(C_t\) form a zero-diagonal unit-weight path matrix \(P_{t-1}\), and they couple to \(v\) by \(b=e_1+e_{t-1}\). The diagonal entry at \(v\) is \(3-2=1\). The other neighbours of \(v\) are only its two cycle neighbours and its joining-path neighbour. The path matrix \(P_j\) has inertia \((\lfloor j/2\rfloor,\mathbf1_{\{j\text{ odd}\}},\lfloor j/2\rfloor)\). For even \(j=t-1\), its inverse has zero endpoint diagonal entries; its corner entry is \(-1\) when \(t\equiv1\pmod4\) and \(+1\) when \(t\equiv3\pmod4\). Thus \(b^TP_{t-1}^{-1}b=-2\) or \(+2\), respectively. The symmetric Schur-complement congruence contributes \(((t-1)/2,0,(t-1)/2)\) and retains \(v\) with modified weight \(1-b^TP^{-1}b=3\) or \(-1\).

For odd \(j=t-1\), the nullvector of \(P_j\) has entries alternating \(+1,0,-1,0,\ldots\), and endpoint signs \(+1,-1\) if \(t\equiv0\), or \(+1,+1\) if \(t\equiv2\). In the former case it is orthogonal to \(b\), and \(b\) lies in the range of \(P_j\), with zero generalized response \(b^TP_j^+b\); this supplies \(((t-2)/2,1,(t-2)/2)\) and retains \(v\) with weight \(1\). In the latter case \(b\) has nonzero component along the path kernel. Eliminate the invertible range first, then use the two-dimensional saddle block on \(v\) and that kernel vector: the block has form \(\left(\begin{smallmatrix}c&\mu\\\mu&0\end{smallmatrix}\right)\) with \(\mu\ne0\), inertia \((1,0,1)\), and its inverse has \((1,1)\) entry zero. Consequently it leaves every coupling between the remaining vertices unchanged and deletes \(v\), adding \((t/2,0,t/2)\) overall. These calculations give precisely \(q(t)\), \(z(t)\), and the weights in the theorem. Each operation is a real invertible congruence, so Sylvester's law applies even to singular branches.

**Step 3 (the joining path).** After the independent cycle eliminations, the leftover vertices are the endpoints of the length-\(d\) connecting path unless the corresponding cycle has residue \(2\) (in which case that endpoint was removed); all surviving internal diagonals are zero and the edges have unit weights. When no endpoint was deleted, this is a tridiagonal path matrix of order \(d+1\) with endpoint weights \(\alpha,\beta\). For even \(d=2h\) the \(d-1\) internal vertices have one nullvector. Hyperbolically pair the internal range, contributing \((h-1,0,h-1)\); coupling its nullvector to the endpoints pairs one more positive and negative direction, and leaves one scalar with the sign of \(\alpha+\beta\), giving \((h+\mathbf1_{\{\alpha+\beta>0\}},\mathbf1_{\{\alpha+\beta=0\}},h+\mathbf1_{\{\alpha+\beta<0\}})\). For odd \(d=2h+1\), elimination of the \(2h\) internal vertices is nonsingular and contributes \((h,0,h)\); its Schur complement is congruent to \(\left(\begin{smallmatrix}\alpha&\pm1\\\pm1&\beta\end{smallmatrix}\right)\), whose offdiagonal sign is removed by changing the sign of one coordinate. This is \(T\).

With exactly one endpoint deleted, the surviving path has \(d\) vertices and one endpoint weight \(w\): if \(d\) is even, elementary alternating \(2\times2\) pivots give \((d/2,0,d/2)\); if odd, they give \(((d-1)/2,0,(d-1)/2)\) plus the inertia of the scalar \(w\). With both deleted, the remaining unweighted path has \(d-1\) vertices, so its spectrum has the stated positive/zero/negative counts. This proves every residual branch and hence Theorem 1.

**Step 4 (signature and nullity).** The equal local \(q(a)+q(b)\) increments cancel from the signature, while the incidence transfer subtracts one. Therefore \(\operatorname{sig}A(L(B))=u_+-u_--1\). Direct evaluation of \(\alpha,\beta\in\{-1,1,3\}\), the zero determinant cases \(\alpha\beta=1\), and the deleted-endpoint cases yields Corollary 2. The zero component is exactly \(z(a)+z(b)+u_0\); applying the same cases yields Corollary 3, including \(d=1,2\) and both-deleted endpoints. The criterion for signature \(+1\) follows immediately.

## Verification
A standalone Python 3 verifier (`verify.py`) constructs \(B(a,b,d)\), forms the ordinary zero-one adjacency matrix of \(L(B(a,b,d))\), and obtains its inertia by independent *exact rational* symmetric elimination with both one-by-one and two-by-two pivots. The checker compares all three indices and signature with the formulas for every triple \(3\le a,b\le10\), \(1\le d\le8\): \(512\) graph instances. It checks representative singular cases and counts. The recorded stdout appears in `verify_output.txt`; run `python3 verify.py` to reproduce. This is a finite corroboration, not the proof of the all-parameter theorem. The all-parameter result follows from Steps 1–4.

## Relationship to prior work
Akbari–Elphick–Kumar–Pragada–Tang introduced a conjectured upper bound of one for the signature of connected line graphs and noted individual kayak-paddle examples. Francis–Uptain (arXiv:2607.22874; first public 24 July 2026) disproved that general bound and supplied bridge transfer and extremal constructions. Their particular kayak-paddle examples \(B(4,5,1)\) and \(B(5,5,1)\) have signature one and are included here, but a finite list of examples does not imply the full inertia formula or exact equality conditions.

Paone–Paone (2026, DOI:10.5281/zenodo.21744051) established complete inertia formulas for *rose* graphs (cycles sharing a vertex) and *generalized theta* graphs (multiple internally disjoint paths with the same two endpoints); those classes are structurally different from dumbbells. Their Remark 9.2 specifically notes that vertex-disjoint cycles joined by a path are outside both analyzed classes. Their established incidence and path-elimination tools are applicable mathematical background, and the present claim is the explicit full evaluation for the remaining natural connected bicyclic core, including bridge length and every singular residue branch, not priority over those common tools.

Wang–Fan (arXiv:1310.1003) established general line-graph signature bounds and earlier special graph-family results, but those bounds do not yield exact three-index inertia of every dumbbell. Previous spectral-characterization work on dumbbell graphs, notably Liu–Lu (DOI:10.1142/S1793830916500282), concerns the ordinary graph Laplacian and an inverse-spectral question, rather than the adjacency inertia of the line graph. The comparisons are based on the material and source records described in `REVIEW.md` and `AUDIT.json`.

## Limitations
The theorem is restricted to precisely two vertex-disjoint cycles with an otherwise disjoint joining path: adding pendant trees, additional cycles, or chords is not covered. It is a statement about *ordinary unsigned adjacency inertia* of the line graph, not signed-line-graph \(-2\)-eigenspaces, Laplacian spectral determination, or the full adjacency spectrum. The local elimination and incidence identities have prior antecedents; newness is asserted only for the complete parameter evaluation and sharp criterion. Literature searching cannot establish absolute novelty; full text was unavailable for some tangential published inverse-spectral papers. Independent audit and external mathematical validation have not been performed.

## References
1. S. Akbari, C. Elphick, H. Kumar, S. Pragada, Q. Tang, "A new conjecture on the inertia of graphs," *Discrete Mathematics* 349 (2026), 114953; arXiv:2508.01163, https://arxiv.org/abs/2508.01163.
2. L. Francis, T. Uptain, "The signature of connected line graphs is unbounded," arXiv:2607.22874v2 (2026); https://arxiv.org/html/2607.22874v2.
3. A. Paone, M. Paone, "Line-graph inertia of roses and generalized theta graphs," preprint (1 August 2026), DOI:10.5281/zenodo.21744051; full web edition https://aletheia-technologies.it/en/research/line-graph-inertia-roses-generalized-theta/reader/.
4. L. Wang, Y. Fan, "The signature of line graphs and power trees," *Linear Algebra and its Applications* 448 (2014), 264–273; arXiv:1310.1003, https://arxiv.org/abs/1310.1003.
5. X. Liu, P. Lu, "Laplacian spectral characterization of dumbbell graphs and theta graphs," *Discrete Mathematics, Algorithms and Applications* 8 (2016), 1650028; DOI:10.1142/S1793830916500282.
