# Logarithmic edge completion of consecutive cycle sums

## Finding

For each integer \(n\ge 8\), put the vertex labels \(1,2,\ldots,n\) in cyclic order on \(C_n\). Let \(\mathrm{mEC}(n)\) be the minimum number of new edges required to make every integer from \(1\) through \(T_n=n(n+1)/2\) equal the sum of labels in some nonempty connected vertex set. Then

\[
\boxed{\mathrm{mEC}(n)\le \lfloor\log_2(n-2)\rfloor.}
\]

In particular \(\mathrm{mEC}(n)=O(\log n)=o(n)\). The bound is constructive: add the chords \(\{n,2^j\}\) for exactly those integers \(j\ge1\) satisfying \(2^j\le n-2\). The chosen edges alone make every target sum attainable. This resolves the sublinear edge-completion direction raised by Marotti and Needleman [1] with a logarithmic bound.

## Assumptions and scope

Here \(C_n\) is the undirected cycle on the *fixed* labels \(1,\ldots,n\), with edges \(\{i,i+1\}\) for \(1\le i<n\) and \(\{n,1\}\). Connectivity means connectivity of the subgraph induced by a chosen vertex subset in the augmented undirected graph; arbitrary extra edges do not change labels. The added chords are distinct, simple, and absent from the original cycle, since \(2\le2^j\le n-2\).

## Proof

Fix \(n\ge8\), and let \(G_n\) be the cycle together with the indicated chords. There are exactly \(\lfloor\log_2(n-2)\rfloor\) such chords, one for each integer \(1\le j\le\lfloor\log_2(n-2)\rfloor\).

Write \(S_t=\sum_{i=t}^{n}i=T_n-(t-1)t/2\) for \(1\le t\le n\). Then \(S_1=T_n\), \(S_n=n\), and \(S_{t-1}-S_t=t-1\) for \(2\le t\le n\). A target \(k<n\) is attained by the single vertex \(\{k\}\), and \(k=T_n\) is attained by all vertices.

For any remaining integer \(n\le k<T_n\), the strict monotonicity of the suffix sums gives a unique index \(t\in\{2,\ldots,n\}\) with

\[
S_t\le k<S_{t-1}.
\]

Consequently the residue \(r=k-S_t\) obeys \(0\le r\le t-2\). Express \(r\) in binary:

\[
r=\sum_{j\in J}2^j,
\]

where \(J\) is a finite subset of \(\{0,1,\ldots\}\). Each selected bit \(2^j\) is no larger than \(r\), so it is at most \(t-2\) and hence lies strictly below the suffix \(\{t,t+1,\ldots,n\}\). Define

\[
A=\{t,t+1,\ldots,n\}\cup\{2^j:j\in J\}.
\]

The union is disjoint and \(\sum_{v\in A}v=S_t+r=k\). The suffix is a connected path ending at \(n\). Every selected bit vertex is adjacent to \(n\): for \(j=0\), this is the original cycle edge \(\{1,n\}\); for \(j\ge1\), the inequality \(2^j\le t-2\le n-2\) ensures that the chord \(\{n,2^j\}\) was added. Thus \(A\) induces a connected subgraph in \(G_n\). All targets are represented, so the explicit number of added edges proves the displayed bound. \(\square\)

## Verification

The companion standalone file `verify_binary_chords.py` computes a binary-suffix witness for each requested target, independently builds the augmented graph edges, recomputes the label sum, and performs breadth-first search on the induced subgraph to test connectivity. Its fixed-seed run exhaustively verified all \(88{,}556\) targets for \(3\le n\le80\), plus \(956\) selected instances at larger sizes up to \(n=65{,}537\). The command is `python3 verify_binary_chords.py`; expected output is provided in `verifier_output.txt`. The finite checks illustrate the construction; the preceding proof establishes the infinite statement.

## Relationship to prior work

Marotti and Needleman [1, Section 5] define the minimum edge-completion number, give the linear upper bound \(\mathrm{mEC}(n)\le n/2-1\), and explicitly ask for sublinear improvement. Their paper classifies incomplete cycles for \(n\ge8\), but it does not supply the power-of-two chord construction or a logarithmic upper bound. The present argument uses the identity \(S_{t-1}-S_t=t-1\) to fill each successive suffix-sum gap by binary representation on independently attached vertices. This is a construction for the specific labeled-cycle completion invariant, not a restatement of the unrestricted subset-sum coin lemma.

## Limitations

The theorem is an upper bound only. It does not prove optimality of the added chords, an exact formula for \(\mathrm{mEC}(n)\), or a matching lower bound. It concerns the consecutive fixed labeling and connected vertex subsets; it does not assert the same bound for arbitrary label permutations or impose additional geometric restrictions on chords.

## References

[1] J. Marotti and J. Needleman, *Consecutive Cycle Sums*, arXiv:2610.08889v1 (first submitted 2026-10-06), Section 5. https://arxiv.org/html/2610.08889v1
