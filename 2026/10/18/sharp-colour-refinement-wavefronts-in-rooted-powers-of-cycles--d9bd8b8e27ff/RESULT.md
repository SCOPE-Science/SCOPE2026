# Sharp colour-refinement wavefronts in rooted powers of cycles

## Finding

Let \(k\ge 2\) and \(n\ge4k\) be integers. On \(V=\mathbb Z/n\mathbb Z\), let \(G=C_n^{[k]}\) join distinct residues of cyclic distance at most \(k\). Give the vertex \(0\) a unique initial colour and all other vertices one common colour, and apply ordinary synchronous one-dimensional counting colour refinement. Set \(D=\lfloor n/2\rfloor\) and define the reflection shells
\[
S_d=\{x\in V:\min(x,n-x)=d\},\qquad 0\le d\le D,
\]
where residues are represented by \(0,1,\ldots,n-1\).

**Exact partitions.** In round zero the partition is \(\{S_0,\bigcup_{d=1}^D S_d\}\); in round one it is \(\{S_0,\bigcup_{d=1}^k S_d,\bigcup_{d=k+1}^D S_d\}\). When \(n\ge4k+1\), every round \(r\ge2\) has exactly the classes
\[
S_0,S_1,\ldots,S_{\min(rk,D)},\qquad
\bigcup_{d=rk+1}^D S_d,
\]
with empty classes omitted (if the last union contains just one shell it is already a full shell class). At the boundary \(n=4k\), round two has precisely
\[
S_0,S_1,\ldots,S_{2k-2},\quad S_{2k-1}\cup S_{2k},
\]
and round three has all \(2k+1\) shells separately.

**Sharp stabilization depth.** The least number \(R\) of complete refinement rounds needed to reach a stable partition is
\[
R=\begin{cases}
3,&n=4k,\\
\max\left\{2,\left\lceil\dfrac{\lfloor n/2\rfloor-1}{k}\right\rceil\right\},&n\ge4k+1.
\end{cases}
\]
For every allowed pair \((n,k)\), the stable partition is **exactly** the orbit partition of the full colour-preserving graph automorphism group. In particular the boundary transition \(n=4k\) to \(n=4k+1\) lowers the required rounds from three to two, even though the graph gains a vertex.

## Assumptions and scope

All graphs are simple, undirected and finite. The power \(C_n^{[k]}\) is the graph with edge \(\{x,y\}\) precisely when \(1\le\min((x-y)\bmod n,(y-x)\bmod n)\le k\). Rounds are counted from the given colouring as round zero. At each new round a colour records the old colour and the **multiset** of old neighbour colours, so no two previously different classes merge. Stability refers to equality of vertex partitions, not the syntactic names assigned to colours. The theorem concerns only \(k\ge2\), \(n\ge4k\), and one individualized vertex; it does not assert isomorphism identification among arbitrary graphs.

## Proof

**1. The reflection bound.** The transformations \(x\mapsto x+a\) and \(x\mapsto -x\) preserve cyclic distance. Reflection fixes the marked \(0\) and acts transitively on each \(S_d\). Therefore no refinement round can split a shell, and it suffices to compute which shell indices remain fused.

**2. The first two rounds away from the seam.** In the first round the marked vertex, its \(2k\) neighbours \(B=S_1\cup\cdots\cup S_k\), and its non-neighbours have different colours. For \(n\ge4k+1\), a representative of shell \(S_d\) has the following number of neighbours in \(B\):
\[
\beta(d)=\begin{cases}
2k-d-1,&1\le d\le k,\\
2k-d+1,&k+1\le d\le2k,\\
0,&2k<d\le D.
\end{cases}
\]
For \(1\le d\le k\), the \(k-1\) other positive near residues and \(k-d\) negative near residues yield the first expression. For \(k+1\le d\le2k\), exactly the residues from \(d-k\) through \(k\) on the positive side give the second. For \(d>2k\), neither side can meet \(B\) within \(k\) steps: the direct gap exceeds \(k\), and the wraparound gap is at least \(n-D-k>k\) whenever such a shell exists. The counts vary strictly within the two pre-existing non-root colours. Hence round two isolates every shell through \(S_{2k}\) and fuses exactly the more distant shells.

**3. Exact propagation.** Suppose that after round \(r\ge2\) (with \(n\ge4k+1\)) every shell through index \(b=\min(rk,D)\) is a distinct class and the larger indices form one class. If \(b\ge D-1\), the partition already consists of shells and hence is stable, by step 1. Otherwise \(b\le D-2\). For each \(d\) with \(b<d\le\min(b+k,D)\), the vertex \(d\) has a neighbour in the formerly singleton-coloured shell \(S_{d-k}\), and **no** neighbour in any \(S_a\) with \(a<d-k\). Indeed the direct circular gap is \(d-a>k\), and the gap via the opposite arc satisfies
\[
n-d-a\ge 2D-d-a\ge 2(D-d)+k+1>k
\]
whenever \(a\le d-k-1\). Thus the smallest shell index \(a\le b\) represented among its coloured neighbours equals \(d-k\), distinct for different \(d\). A shell \(S_d\) with \(d>b+k\) has no neighbours in any \(S_a\) with \(a\le b\), because both arcs are longer than \(k\): \(d-a>k\) and \(n-d-a\ge D-b>k\). Since the graph is \(2k\)-regular, all these remaining vertices have the same count into the unique unrefined tail class. Hence round \(r+1\) isolates exactly the next \(k\) shells and leaves a single tail class. This proves the asserted partitions by induction.

The partition becomes the shell partition when and only when its tail has at most one shell, i.e. \(rk\ge D-1\). Round one cannot be stable for \(k\ge2\) because \(S_1\) and \(S_2\) are fused there but separated in round two. Therefore the exact depth is \(\max\{2,\lceil(D-1)/k\rceil\}\).

**4. The antipodal seam \(n=4k\).** First-round classes are unchanged. For \(1\le d\le k\), the count into \(B\) is still \(2k-d-1\). For \(k+1\le d\le2k-1\), it is \(2k-d+1\), whereas for the antipodal shell \(d=2k\) the additional neighbour at residue \(-k\) yields the count \(2\). Thus exactly the two distinct shells \(S_{2k-1}\) and \(S_{2k}\) collide in round two; all other shells are separated within their previous first-round classes.

At round two, the shell \(S_{k-1}\) already has its own colour. A vertex in \(S_{2k-1}\) has exactly one neighbour in \(S_{k-1}\), but a vertex in \(S_{2k}\) has none: the former direct distance is \(k\), while each of the latter's two circular distances is \(k+1\). Round three therefore separates the last pair, giving the shell partition. The round-two collision proves the bound three is necessary.

**5. Orbit equality.** Every refinement class at stability is one reflection shell, by the previous steps. All graph automorphisms preserving the marked vertex preserve every refinement class. Conversely the reflection automorphism already acts transitively on each shell. Thus full automorphism orbits and stable refinement classes are exactly the same shells, regardless of whether the unmarked graph has any additional automorphisms. \(\square\)

## Verification

Two standalone Python 3 programs, `checks/direct_refinement.py` and `checks/quotient_signatures.py`, can be run with no third-party dependencies. The first constructs each entire graph and executes ordinary synchronous refinement, comparing **every intermediate partition** with the closed-form description for all \(2\le k\le14\) and \(4k\le n\le10k+12\). The second constructs the independent weighted distance-shell signatures, verifying each predicted equivalence class for \(2\le k\le38\) and \(4k\le n\le7k+15\); it also separately checks the seam witness for \(2\le k\le59\). Recorded outputs are in `checks/direct_output.txt` and `checks/quotient_output.txt`. These are finite regression tests, not exhaustive proofs of the quantified theorem.

## Relationship to prior work

Arvind, Köbler, Rattan and Verbitsky (arXiv:1502.01255, publicly posted 2015-02-04) develop the finite-model-theoretic setting and the distinction between stable colour classes and automorphism orbits, but do not derive a marked-cycle-power wavefront or exact stabilization depths. Kluge (arXiv:2204.01054) treats circulants using group-ring refinement, proving in Lemma 38 an orbit-like stable partition after one marking for **prime-order** Cayley graphs, and studies a general two-dimensional algorithm; it does not furnish these sharp one-dimensional intermediate partitions and round counts for arbitrary \(n\ge4k\). Verbitsky–Zhukovskii (arXiv:2310.05788) studies canonical labelling of random circulants, not deterministic cycle powers or these thresholds. A prior result about unmarked powers of paths considers \(C^2\)-identification among arbitrary graphs and neither implies nor is implied by the present rooted cycle-power round-depth theorem.

## Limitations

Only the interval generating sets \(\{\pm1,\ldots,\pm k\}\) are covered; the theorem does not classify other circulants, denser \(n<4k\), multiple marks, coloured directed powers, or identification among arbitrary graphs. Stabilization rounds do not measure the runtime of a particular implementation. Publication priority is not independently certified; specialist results on equitable partitions of circulants may conceivably imply the theorem without using this terminology.

## References

- V. Arvind, J. Köbler, G. Rattan, O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255 (first public version 2015-02-04), https://arxiv.org/abs/1502.01255.
- L. Kluge, *Combinatorial refinement on circulant graphs*, arXiv:2204.01054 (first public version 2022-04-03), https://arxiv.org/abs/2204.01054.
- O. Verbitsky, M. Zhukovskii, *Canonization of a random circulant graph by counting walks*, arXiv:2310.05788 (first public version 2023-10-09), https://arxiv.org/abs/2310.05788.
