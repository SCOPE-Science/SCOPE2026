# Real-rooted one-point extension spectra of partial Steiner triple systems
## Finding
Let \(A=(V,\mathcal B)\) be a finite partial Steiner triple system, and let \(L(A)\) be its leave: the graph on \(V\) in which \(uv\) is an edge exactly when no block of \(\mathcal B\) contains the pair \(\{u,v\}\). Fix a new labelled point \(x\). Define an induced one-point extension of \(A\) to be a partial Steiner triple system on \(V\cup\{x\}\) whose restriction to \(V\) is exactly \(A\), and put
\[
E_A(z)=\sum_{A^+}z^{|\mathcal B(A^+)\setminus\mathcal B|}.
\]
If \(m_k(G)\) denotes the number of \(k\)-edge matchings of a graph \(G\), then
\[
\boxed{E_A(z)=\sum_{k\ge0}m_k(L(A))z^k.}
\]
Thus the complete rank-refined spectrum of labelled one-point extensions is the matching generating polynomial of the leave.

Consequently every zero of \(E_A(z)\) is real and negative. If \(\nu=\nu(L(A))\), then Newton's inequalities give
\[
\left(\frac{m_k}{\binom{\nu}{k}}\right)^2
\ge
\frac{m_{k-1}}{\binom{\nu}{k-1}}
\frac{m_{k+1}}{\binom{\nu}{k+1}}
\qquad(1\le k<\nu),
\]
so the extension counts by number of new blocks are ultra-log-concave, hence log-concave and unimodal.

For \(|V|=n\), the total number of induced one-point extensions satisfies the sharp bound
\[
\boxed{E_A(1)\le I_n:=\sum_{k=0}^{\lfloor n/2\rfloor}
\frac{n!}{2^k k!(n-2k)!},}
\]
with equality if and only if \(A\) has no blocks. Hence the unique maximizer is the empty partial triple system, and the maximal totals begin
\[
1,2,4,10,26,76,232,764,\ldots.
\]
At the opposite extreme, if \(A\) is a Steiner triple system then \(L(A)\) is empty and \(E_A(z)=1\).

## Assumptions and scope
A partial Steiner triple system means that every unordered pair lies in at most one block. "Induced one-point extension" means no new block entirely contained in the old vertex set is added; every new block therefore contains the distinguished new point \(x\). The result counts labelled extensions fixing the old set pointwise, not isomorphism classes modulo \(\operatorname{Aut}(A)\).

Barbina and Casanovas use partial Steiner triple systems as relational substructures in their model-theoretic treatment, and recall that every finite partial Steiner triple system embeds, in the model-theoretic sense, into a finite Steiner triple system. Therefore every extension counted by \(E_A\) is a legitimate finite one-new-point relational diagram occurring inside some finite Steiner completion. The result does not claim that these are complete \(1\)-types over a fixed copy of \(A\) in the functional Fraïssé limit.

## Proof
Every new block has the form \(\{x,u,v\}\) with \(u,v\in V\). Such a block is legal only if \(uv\in E(L(A))\), because otherwise the old pair \(\{u,v\}\) is already covered by a block of \(A\).

If two new blocks \(\{x,u,v\}\) and \(\{x,u,w\}\) shared an old point \(u\), then the pair \(\{x,u\}\) would lie in two blocks, contradicting the defining condition for a partial Steiner triple system. Hence the old pairs belonging to the new blocks are pairwise vertex-disjoint: they form a matching in \(L(A)\).

Conversely, for any matching \(M\subseteq E(L(A))\), adjoining the blocks
\[
\{\{x,u,v\}:uv\in M\}
\]
produces a partial Steiner triple system. Old-old pairs are safe because every edge of \(M\) lies in the leave, and every pair \(\{x,u\}\) appears at most once because \(M\) is a matching. This gives a size-preserving bijection between induced one-point extensions with \(k\) new blocks and \(k\)-matchings of \(L(A)\), proving the polynomial identity.

Let
\[
\mu_G(t)=\sum_{k\ge0}(-1)^k m_k(G)t^{n-2k}
\]
be the matching polynomial of an \(n\)-vertex graph. Heilmann and Lieb proved that all zeros of \(\mu_G\) are real. Since
\[
\mu_{L(A)}(t)=t^nE_A(-t^{-2}),
\]
a nonzero root \(z\) of \(E_A\) would give a root \(t=(-z)^{-1/2}\) of \(\mu_{L(A)}\). Real-rootedness of \(\mu_{L(A)}\) forces \(z<0\). Newton's inequalities then yield the displayed ultra-log-concavity inequality.

Finally, \(L(A)\) is a spanning subgraph of \(K_n\). Adding graph edges can only add matchings, hence
\[
E_A(1)\le \sum_k m_k(K_n)=I_n.
\]
The formula for \(I_n\) follows by choosing \(2k\) matched vertices and pairing them. If \(A\) has a block, then three edges of \(K_n\) are absent from its leave, so already the coefficient of \(z\) is strictly smaller than for \(K_n\); therefore equality is possible only for the empty partial triple system.

## Verification
The bundled checker independently enumerates every labelled partial Steiner triple system through seven old points, a total of \(5902\) systems. It computes each leave and its matching polynomial by a vertex-deletion recurrence, verifies the sharp extension-total bound and the normalized Newton inequalities, and checks that the empty system is the unique maximizer for each size.

For all \(35\) labelled partial Steiner triple systems through five points, it also directly enumerates every subset of candidate new blocks \(\{x,u,v\}\), validates the partial-Steiner condition without invoking the matching recurrence, and obtains exactly the same coefficient vector. The maximal totals for \(n=1,\dots,7\) are
\[
1,2,4,10,26,76,232.
\]
The standard Fano plane is checked separately and gives \(E_A(z)=1\). Running `verify.py` prints `VERIFY_OK`.

## Relationship to prior work
Barbina and Casanovas establish the model-completion framework for Steiner quasigroups and explicitly use finite partial Steiner triple systems as relational diagrams; they also recall the finite embedding theorem for partial Steiner triple systems. Andersen, Hilton, and Mendelsohn use the missing-edge graph (the leave) in embedding theory. Matchings in leaves are themselves classical objects: for example, the 1997 paper *Matchings in the Leave of Equitable Partial Steiner Triple Systems* studies existence of large matchings in such leaves. These facts are prior and are not claimed here.

The retained contribution is the full rank-refined identity \(E_A(z)=\sum_km_k(L(A))z^k\), together with its immediate but apparently unstated root-geometric consequence: every local one-point extension polynomial is real-rooted with negative roots, so its extension strata are ultra-log-concave. Targeted published-finding corpus and web searches for one-point extensions, leave matchings, extension polynomials, matching generating polynomials, real-rootedness, and log-concavity did not locate this formulation or consequence.

## Limitations
The basic bijection is short and close to classical embedding constructions that use matchings in leaves, so there is residual folklore risk despite the negative searches. The originality claim is deliberately restricted to the polynomial-level synthesis and its real-rooted/ultra-log-concave extension spectrum, not to the observation that matchings in a leave can be used when adjoining points.

The polynomial counts labelled induced one-point partial extensions only. Quotienting by automorphisms of \(A\), counting full Steiner completions of prescribed order, or translating this polynomial into complete types of the functional model completion requires additional arguments not supplied here.

## References
1. Silvia Barbina and Enrique Casanovas, *Model theory of Steiner triple systems*, Journal of Mathematical Logic 20 (2020), 2050010; arXiv:1805.06767; DOI 10.1142/S0219061320500105.
2. L. D. Andersen, A. J. W. Hilton, and E. Mendelsohn, *Embedding Partial Steiner Triple Systems*, Proceedings of the London Mathematical Society s3-41 (1980), 557-576; DOI 10.1112/plms/s3-41.3.557.
3. Ole J. Heilmann and Elliott H. Lieb, *Theory of monomer-dimer systems*, Communications in Mathematical Physics 25 (1972), 190-232; DOI 10.1007/BF01877590.
4. *Matchings in the Leave of Equitable Partial Steiner Triple Systems*, Journal of Combinatorial Mathematics and Combinatorial Computing 24 (1997), 115-118.
