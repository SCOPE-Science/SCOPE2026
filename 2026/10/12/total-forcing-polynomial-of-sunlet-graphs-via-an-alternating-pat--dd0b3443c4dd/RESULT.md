# Total-forcing polynomial of sunlet graphs via an alternating-path automaton

## Finding
For every integer \(n\ge3\), let \(S_n=C_n\circ K_1\), a cycle with one pendant leaf attached to each cycle vertex. A *total forcing set* is a zero-forcing initial blue set whose induced graph has no isolated vertex. Denote its cardinality enumerator by
\[
T_n(z)=\sum_{X\subseteq V(S_n)\,\colon\,X\text{ is total forcing}}z^{|X|}.
\]
Define formal polynomials \(p_n(z)\) for \(n\ge1\) through
\[
\sum_{n\ge1}p_n(z)u^n=
\frac{(z+z^2)u+4z^2u^2-3z^4u^3-5z^5u^5}
{1-(z+z^2)u-2z^2u^2+z^4u^3+z^5u^5}.
\]
**Theorem.** For every \(n\ge3\),
\[
\boxed{T_n(z)=p_n(z)-4z^n\mathbf 1_{2\mid n}.}
\]
Consequently the minimum total forcing cardinality is exactly \(n\). The formula counts *all* total forcing sets, not merely minimum ones. For example,
\[
\begin{aligned}
T_3(z)&=7z^3+6z^4+3z^5+z^6,\\
T_4(z)&=13z^4+16z^5+10z^6+4z^7+z^8,\\
T_5(z)&=26z^5+40z^6+30z^7+15z^8+5z^9+z^{10}.
\end{aligned}
\]
The number of minimum sets for \(n=3,4,5,6,7,8\) is respectively \(7,13,26,55,106,213\).

## Assumptions and scope
All graphs are finite, simple and undirected. The sunlet has \(n\ge3\) distinct cycle vertices \(v_i\), with private pendant vertices \(w_i\); indices are cyclic modulo \(n\). Under ordinary zero forcing, any blue vertex with exactly one white neighbor can force that neighbor blue, repeatedly. The initial set is *total* when every initially blue vertex has at least one initially blue neighbor. Colors called blue and white indicate membership in the initially chosen set or its evolving closure, not a vertex-coloring invariant.

At each cycle index the initial choice is one of three letters: \(A\) for both \(v_i,w_i\) blue, \(B\) for only \(v_i\) blue, and \(D\) for neither blue. Choosing \(w_i\) without \(v_i\) would isolate an initially blue leaf and is prohibited. Their size contributions are respectively \(2,1,0\).

## Proof
**Step 1: the exact word criterion.** A blue \(A\) vertex has an initially blue leaf and is never isolated. A blue \(B\) root is initially isolated precisely when both its neighboring cycle roots are white, i.e. its cyclic word contains \(DBD\). Thus the totality condition is exactly avoidance of cyclic \(DBD\).

To decide whether the initially white cycle roots can be forced, form an auxiliary graph \(Q\) on the indices labeled \(A\) or \(D\), inserting an edge between cyclically adjacent vertices precisely when their labels differ. The components of \(Q\) are isolated vertices, maximal alternating \(A\)-\(D\) paths, or (only for even \(n\)) one alternating cycle. A root initially labeled \(B\) cannot force any white cycle root: while such a neighbor is white, its own leaf is also white. The same assertion holds for a previously forced \(D\) root, whose leaf remains white whenever another cycle neighbor remains white. An initially \(A\) root can force a white \(D\) root exactly when it has one remaining neighboring \(D\) root; its leaf is already blue.

On any alternating-path component with an \(A\) endpoint, the endpoint \(A\) first forces its neighboring \(D\); the next \(A\) (if present) then has only one unforced \(D\) neighbor and forces it, and the chain propagates. If a path has two \(D\) endpoints, every \(A\) along it initially has two white \(D\) neighbors and no force on that component can begin. A singleton \(D\) is likewise blocked. A perfectly alternating cyclic component has no \(A\) endpoint, so no force can begin. Therefore the initial cycle roots all become blue if and only if every noncyclic component of \(Q\) containing \(D\) has an \(A\) endpoint and \(Q\) is not the full alternating cycle. Once all roots become blue, any still-white private leaf is the only white neighbor of its blue root and is forced. This establishes the claimed if-and-only-if word criterion.

**Step 2: the transfer matrix.** Put \(\mathcal L=\{A,B,D\}\). There are exactly fifteen transfer states \((p,c,s)\): \(p,c\in\mathcal L\); if \(c=B\) take \(s=\bot\); otherwise take \(s\in\{A,D\}\). The tag \(s\) records the first label of the current maximal alternating path. Assign \(w(A)=z^2\), \(w(B)=z\), and \(w(D)=1\).

For \((p,c,s)\longrightarrow(c,d,t)\), prohibit the transition when \((p,c,d)=(D,B,D)\). If \(c,d\in\{A,D\}\) are opposite, require \(t=s\). Otherwise close the current alternating component, prohibiting the transition when \(c=D\) and \(s=D\), and require \(t=\bot\) when \(d=B\) or \(t=d\) otherwise. Every allowed transition contributes weight \(w(d)\). Let \(M(z)\) be this weighted \(15\times15\) matrix. This construction gives exactly 38 nonzero weighted transitions, and all weights and conditions are explicit.

For every cyclic word having a break in alternation, the first-label tags are uniquely determined and consistency of the tags around the cycle holds exactly when the word satisfies Step 1. The only exception is a perfectly alternating \(A,D\) cycle when \(n\) is even: it cannot pass the forcing test, yet both arbitrary persistent tag choices are accepted. There are two alternating cyclic words and two false tags for each, yielding precisely four extra weight-\(z^n\) closed walks. Hence
\[
T_n(z)=\operatorname{tr}\!\left(M(z)^n\right)-4z^n\mathbf 1_{2\mid n},\qquad n\ge3.
\]

**Step 3: exact rational form.** The transition definition permits direct exact characteristic-polynomial computation. It yields
\[
\det(\lambda I-M(z))=\lambda^{10}\!
\left(\lambda^5-(z+z^2)\lambda^4-2z^2\lambda^3+z^4\lambda^2+z^5\right).
\]
Set \(Q(u,z)=1-(z+z^2)u-2z^2u^2+z^4u^3+z^5u^5\). The formal trace identity gives
\[
\sum_{n\ge1}\operatorname{tr}(M(z)^n)u^n
=-u\frac{\partial}{\partial u}\log Q(u,z)
=\frac{(z+z^2)u+4z^2u^2-3z^4u^3-5z^5u^5}{Q(u,z)}.
\]
The exceptional alternating cycles are exactly the stated correction for even \(n\ge3\), proving the generating formula. The characteristic identity follows by exact polynomial Newton identities computed from the fifteen explicitly given states; the self-contained verifier reproduces it, independent of numerical interpolation.

**Step 4: minimum size.** In each admissible alternating component with \(D\) vertices and an \(A\) endpoint, the number of \(A\) vertices is at least the number of \(D\) vertices. Summing yields \(a\ge d\), where \(a,b,d\) are the counts of letters \(A,B,D\) in a valid word. Its initial blue cardinality is therefore \(2a+b=n+a-d\ge n\). The all-\(B\) word is valid for \(n\ge3\), with exactly \(n\) initially blue roots; they first force their own leaves. Thus the minimum is attained and equals \(n\).

## Verification
The companion standalone file `verify_total_sunlet.py` implements the fifteen states and their 38 transitions, exact Newton-identity characteristic-polynomial reconstruction, a direct forcing simulation on the original graph, and an independent alternating-path peeling test. Run `python3 verify_total_sunlet.py` with Python 3.10 or later; no nonstandard packages are needed. Output is included in `verification_output.txt`.

Direct enumeration over all \(2^{2n}\) subsets for each \(3\le n\le8\) compares the simulation, the matrix counts and the structural checker, totaling 87,360 subsets. For \(9\le n\le11\), the structural checker and transfer matrix agree without direct subset enumeration. The characteristic identity is checked by exact integer-polynomial arithmetic. All checks passed. These finite checks are corroboration, not a substitute for the proof for arbitrary \(n\).

## Relationship to prior work
Davila and Henning introduced and analyzed the total-forcing invariant and its extremal behavior (arXiv:1702.06035; first publicly posted 20 February 2017). Their work and subsequent tree results concern total-forcing minimum cardinalities and related bounds, not this full sunlet cardinality enumerator. Banot and Baldado (2023) study scalar \(k\)-forcing numbers of sunlet and related cycle graphs, a different condition that does not impose the total-initial-set requirement. Boyer et al. (2018) introduce the ordinary zero-forcing polynomial: it enumerates zero-forcing initial sets *without* the totality constraint. Li and Ji (2025) investigate when ordinary and total minimum forcing numbers agree for unicyclic graphs; this is a later related scalar study, not the all-cardinality claim stated here. The exact polynomial/recurrence and total-set characterization were not identified in the inspected literature; absence from searched sources alone cannot establish global novelty.

## Limitations
The theorem is specific to cycles with one private leaf per root and to the stated version of total forcing. It does not assert a transfer formula for arbitrary coronas, arbitrary unicyclic graphs, or matching-forcing problems. The formal polynomials for \(n=1,2\) are algebraic coefficients of the trace series, not definitions of simple sunlet graphs. Earlier unindexed, differently worded, or implicit equivalent enumerations may exist. Independent validation or external review has not been performed.

## References
- R. Davila and M. A. Henning, *On the Total Forcing Number of a Graph*, arXiv:1702.06035 (2017), https://arxiv.org/abs/1702.06035.
- R. Davila and M. A. Henning, *Matching, Path Covers, and Total Forcing Sets*, arXiv:1801.05318 (2018), https://arxiv.org/abs/1801.05318.
- V. Banot and M. P. Baldado, *k-Forcing Number of Some Cycle-Related Graphs*, Science International 35(4), 455–457 (2023), https://www.sci-int.com/pdf/638268543926230662.pdf.
- K. Boyer et al., *The Zero Forcing Polynomial of a Graph*, arXiv:1801.08910 (2018), https://arxiv.org/abs/1801.08910.
- B. Li and S. Ji, *Total forcing and zero forcing of unicyclic graphs*, Operations Research Transactions 29(1), 198–206 (2025), https://doi.org/10.15960/j.cnki.issn.1007-6093.2025.01.016.
