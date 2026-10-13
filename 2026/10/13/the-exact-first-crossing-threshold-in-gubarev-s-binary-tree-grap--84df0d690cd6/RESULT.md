# The exact first-crossing threshold in Gubarev's binary-tree graph
## Finding
Let \(\Gamma_N\) be the directed binary-tree graph used in arXiv:2610.05384v1, and let \(n\mid N\). Write \(L_m=3\cdot2^m-2\) for the length of the recursive word \(\ell_m\). The largest possible number of edges in a crossing-free path is at most
\[
2L_{2n-2}=6\cdot4^{n-1}-4.
\]
For every \(N\ge 2n\) with \(n\mid N\), this upper bound is attained. Therefore the least integer \(E_n\) such that every path of length at least \(E_n\) has a crossing is exactly
\[
E_n=2L_{2n-2}+1=6\cdot4^{n-1}-3.
\]
As a consequence, Theorem 6.2 of the source strengthens to
\[
T_S(f)^{E_n}=0
\]
under exactly the same hypotheses and boundary conditions. The source uses the coarser exponent \(2^{2n+1}\).

## Assumptions and scope
The definitions of height, grid height, crossing, chain, cut tree, and the representation \(T_S\) are those of arXiv:2610.05384v1. The integer \(n\) is positive and divides the chain height \(N\). For the nilpotency consequence, \(f\) is a nonzero polynomial satisfying the source's condition \(\deg f<n\), and the chain satisfies the same boundary conditions \((f,n)\) as in Definition 5.4.

The exactness statement concerns the combinatorial first-crossing threshold. It does not assert that \(E_n\) is the smallest possible nilpotency exponent for every particular \(f\) or every particular chain, and it does not change the later compression bound.

## Proof
The upper bound is already contained in the proof of Lemma 5.2 of the source. If a path has no crossing, then its visited heights lie in an interval of width at most \(2n-2\). A path whose heights lie in an interval of width \(R\) has at most \(2L_R\) edges. Taking \(R=2n-2\) gives
\[
\operatorname{length}(P)\le 2L_{2n-2}=6\cdot2^{2n-2}-4=6\cdot4^{n-1}-4.
\]

It remains to show that this bound is attained. Assume \(N\ge2n\) and \(n\mid N\). Choose a vertex \(v\) of level \(N-2n\); this level is a grid height and the subtree rooted at \(v\) has height \(2n\). Start immediately after the initial \(\mathtt{x}\) of \(v\) and end immediately before its terminal \(\mathtt{y}\). Traverse the two children of \(v\) consecutively. Within either child, take a \(z_1\)-edge across every encountered \(\mathtt{x}\) or \(\mathtt{y}\) above the cutoff, and when a vertex of absolute level \(N-1\) is reached, use its single \(a\)-jump rather than entering its two leaves.

After this cutoff, each child is traversed exactly like the recursive word \(\ell_{2n-2}\), so each contributes \(L_{2n-2}\) edges. The concatenated path therefore has \(2L_{2n-2}\) edges. Its visited heights lie strictly between the two grid heights \(N-2n\) and \(N\), except that it may visit their midpoint grid height \(N-n\). Thus all grid gaps visited by the path have the same height \(N-n\), so the path has no crossing. This proves equality.

Therefore a path of \(2L_{2n-2}+1\) edges must contain a crossing, and the preceding construction shows that one fewer edge does not force a crossing.

For the strengthened nilpotency statement, rerun the first-crossing decomposition of Section 6 with \(e=E_n\). The lower bound on \(e\) is used there only to ensure that every contributing path has a first crossing. The exact threshold just proved supplies that crossing. The remainder of the decomposition and the vanishing of the middle boundary block are unchanged, giving \(T_S(f)^{E_n}=0\).

## Verification
The bundled `verify.py` independently constructs the directed graphs from the recursive tree definition and computes longest crossing-free paths by dynamic programming. For \(1\le n\le6\) at height \(N=2n\), it returns the exact sequence
\[
2,20,92,380,1532,6140,
\]
which equals \(2L_{2n-2}\). It also repeats the computation at \(N=3n\) for \(1\le n\le4\). The recorded output terminates with `VERIFY_OK`.

These finite computations are checks of the construction and formula, not a proof for arbitrary \(n\). The infinite statement is established by the upper-bound argument and the explicit family of attaining paths above.

## Relationship to prior work
Gubarev's Lemma 5.2 states the sufficient threshold \(2^{2n+1}\), while its proof establishes the sharper upper bound \(2L_{2n-2}\) for crossing-free paths. The source does not state that this upper bound is attainable or identify the exact crossing threshold, and its construction later sets the nilpotency exponent to \(2^{2n+1}\). The new part is the matching lower construction, which makes the hidden upper bound exact; the smaller nilpotency exponent is then a consequence.

The older existence proof of a simple nil ring is background for the existence theorem, but the crossing graph and its first-crossing decomposition are specific to the 2026 construction and are the objects analyzed here.

## Limitations
The improvement from \(2^{2n+1}\) to \(6\cdot4^{n-1}-3\) is a uniform improvement for the first-crossing argument. It is not a proof that every admissible representation has nilpotency index exactly \(E_n\), and special polynomials or chains can vanish earlier. No claim is made that the compression loss \(C(f)4^n\) is sharp or improved.

## References
1. V. Gubarev, *A simple construction of a simple nil ring*, arXiv:2610.05384v1, 2026.
2. A. Smoktunowicz, *A simple nil ring exists*, Communications in Algebra 30 (2002), 27–59.
