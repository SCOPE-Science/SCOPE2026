# Unicyclic skew-rank distributions and character degrees from a single cycle-cancellation correction

## Finding

Let \(G=(V,E)\) be a finite connected simple unicyclic graph, with unique cycle \(C\), and let \(n=|V|\). Fix any orientation of the edges merely to assign matrix signs. For \(w\in\mathbb F_q^E\), let \(B_G(w)\) be the alternating matrix whose \((i,j)\)-entry is the corresponding oriented edge weight if \(\{i,j}\in E\), and zero otherwise, with \(B_{ji}=-B_{ij}\). Write \(\nu(F)\) for the maximum matching size of the spanning subgraph with edge set \(F\).

Define \(\delta(F)\) to be one precisely when (i) \(C\) has even length, (ii) \(C\subseteq F\), and (iii) **every** maximum matching in \((V,F)\) pairs all cycle vertices to other cycle vertices using exactly \(|C|/2\) cycle edges. In all other cases put \(\delta(F)=0\). This depends only on the abstract graph and not on edge orientations or the field.

**Theorem.** For every prime power \(q\), including even characteristic,
\[
R_G(q,z):=\sum_{w\in\mathbb F_q^E}z^{\operatorname{rank}B_G(w)/2}=
\sum_{F\subseteq E}(q-1)^{|F|}z^{\nu(F)}+
\sum_{F\subseteq E:\,\delta(F)=1}(q-1)^{|F|-1}\bigl(z^{\nu(F)-1}-z^{\nu(F)}\bigr).
\]
In particular the formula gives the exact multiplicity of every alternating-matrix rank for arbitrary unicyclic graphs and all finite fields.

For odd \(q\), let \(\mathbf G_G(\mathbb F_q)\) be the graphical group defined by one vertex-coordinate group and one central edge-coordinate group with commutator pairing specified by adjacency. For every integer \(j\ge0\), the number of ordinary irreducible complex characters of degree \(q^j\) is
\[
\operatorname{ch}(G,j;q)=q^{n-2j}[z^j]R_G(q,z).
\]
Coefficients for unattainable \(j\) are zero. No representation-counting assertion is made in characteristic two.

## Assumptions and scope

All graphs are finite, loopless, simple, connected, and have exactly one cycle, possibly odd. Edge weights range independently through **all** elements of \(\mathbb F_q\). The alternating matrix has a skew-sign convention in odd characteristic and the usual zero-diagonal alternating convention in characteristic two. The polynomial identity does not require \(q\) odd; only the graphical-group character consequence does. The empty support contributes one term of rank zero. In the correction sum \(\nu(F)\ge1\), so there are no negative powers of \(z\).

## Proof

**1. Supports and Pfaffians.** Partition all assignments \(w\) by their nonzero-edge support \(F\). There are exactly \((q-1)^{|F|}\) assignments with that support. Since any nonzero principal Pfaffian of size \(2r\) has a monomial corresponding to an \(r\)-edge matching in the induced support, every alternating matrix with support \(F\) has rank at most \(2\nu(F)\). Conversely, an alternating matrix has rank at least \(2r\) exactly when some principal \(2r\)-Pfaffian is nonzero; this remains valid in characteristic two.

**2. Why a unicyclic graph has at most two Pfaffian terms.** A Pfaffian of a principal vertex-induced submatrix expands over perfect matchings of that induced graph. Distinct perfect matchings have symmetric difference equal to a nonempty disjoint union of even cycles. Because a unicyclic graph has a unique cycle, there cannot be two distinct perfect matchings unless that cycle is even and appears whole in the induced graph. In that case the two matchings differ exactly by switching the two alternating perfect matchings of the cycle, and must be identical outside it. Thus every nonzero principal Pfaffian is either a single nonzero monomial or a sum of two monomials whose quotient is the same oriented ratio of alternating products of the full cycle edges, up to a fixed sign.

**3. The ordinary-support case.** Suppose \(\delta(F)=0\). Choose a maximum matching \(M\) of \((V,F)\) that does **not** internally pair every vertex of the even cycle (or choose any maximum matching when the cycle is odd or absent from \(F\)). Let \(S\) be the \(2\nu(F)\) endpoints of \(M\). If the induced graph on \(S\) possessed a second perfect matching, its symmetric difference with \(M\) would be exactly the even cycle. This would force \(M\) to internally pair every cycle vertex, contrary to the choice of \(M\). Hence that induced graph has exactly one perfect matching; its principal Pfaffian is a nonzero monomial for all nonzero weights. Consequently \(\operatorname{rank}B_G(w)=2\nu(F)\) for *every* nonzero assignment on \(F\).

**4. The exceptional-support case.** Suppose \(\delta(F)=1\). Every maximum matching uses a cycle-perfect matching. Consider a principal \(2\nu(F)\)-Pfaffian. If nonzero as a formal polynomial, its perfect matchings are maximum matchings in \(F\); they therefore internally pair the entire even cycle. Switching its cycle-perfect matching always produces the other perfect matching, with the same outside matching. Hence the Pfaffian is the product of a nonzero outside-edge monomial and one common two-term cycle expression \(P_+\pm P_-\), where \(P_+\) and \(P_-\) are the products of edge weights over the two alternating cycle-edge matchings. The sign is fixed by the selected orientation; switching the order of vertices does not change the zero set. Therefore all top-size Pfaffians vanish **if and only if** \(P_+=\pm P_-\).

The two alternating edge sets are disjoint and each contains \(|C|/2\) edges. For nonzero weights, their ratio ranges uniformly over \(\mathbb F_q^\times\). The single relation has exactly the fraction \(1/(q-1)\) of support assignments, i.e. \((q-1)^{|F|-1}\) choices. This includes \(q=2\), when cancellation is automatic on exceptional supports.

To show the rank drops by **exactly two**, choose a maximum matching \(M\) and delete from its endpoint set the two endpoints of one cycle edge belonging to \(M\). The remaining \(2\nu(F)-2\) vertices are perfectly matched by \(M\) minus that edge and do not contain the whole cycle. Their induced graph is a forest and admits a unique perfect matching, so its Pfaffian is a nonzero monomial for every support assignment. Thus, on cancellation, \(\operatorname{rank}B_G(w)=2\nu(F)-2\), never smaller.

**5. Count and representation-theoretic consequence.** Summing the ordinary \((q-1)^{|F|}\) contribution \(z^{\nu(F)}\) over supports, and transferring exactly \((q-1)^{|F|-1}\) assignments from \(z^{\nu(F)}\) to \(z^{\nu(F)-1}\) for each exceptional support, proves the polynomial identity.

For odd field characteristic, the standard orbit-method/central-character description of the two-step graphical group associates to each central functional \(w\in\mathbb F_q^E\) an alternating commutator pairing \(B_G(w)\). Its irreducible representations have degree \(q^{\operatorname{rank} B_G(w)/2}\), and for each \(w\) there are \(q^{n-\operatorname{rank}B_G(w)}\) such irreducibles. Therefore the coefficient of \(z^j\) in \(R_G(q,z)\) is multiplied by \(q^{n-2j}\). The sum of the squares of all resulting character degrees equals \(q^{n+|E|}\), the group order, providing an independent normalization check.

## Verification

The complete standard-library program `unicyclic_rank_check.py` independently enumerates nonzero support sets, maximum matchings, and the exceptional-support condition; separately it enumerates actual field-valued edge weights and computes alternating-matrix ranks by Gaussian elimination. It checks **18 complete cases**, comprising six graphs (triangle, square, square with one pendant leaf, square with a length-two pendant path, triangle with a length-two pendant path, and square with two pendant leaves) over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\). Every rank distribution agrees, and every distribution sums to \(q^{|E|}\). The successful program marker is `UNICYCLIC_SKEW_RANK_CORRECTION_OK 18`.

For a square with a pendant path of length two over \(\mathbb F_3\), the actual rank-half counts for \(j=0,1,2,3\) are respectively \(1,56,384,288\). Hence its ordinary graphical-group character counts in degrees \(1,3,9,27\) are respectively \(729,4536,3456,288\). Their squared-degree sum is \(3^{12}\) as required.

## Relationship to prior work

Mainkar (2010) records the well-established graph-to-two-step-Lie-algebra construction, without a finite-field character-degree census. Li and Yu (2014) determine skew ranks for **oriented** unicyclic graphs with edge weights fixed to \(\pm1\), including orientation-dependent exceptional cycles; their result does not supply the complete weighted rank multiplicities for arbitrary \(\mathbb F_q\). Rossmann (2022), Section 1.6, frames the graphical-group character-degree enumeration question and its connection to alternating commutator ranks but does not give the unicyclic support-correction formula. Previously obtained formulas for trees (whose supports have no cycles) and pure cycles do not themselves state the classification of which supports in a general unicyclic graph exhibit cancellation when pendant trees are present. The theorem here supplies that graph-wide criterion and its exact multiplicities. The possibility of an equivalent formulation in older rank-enumeration literature has not been exhaustively eliminated.

## Limitations

The polynomial identity applies to unicyclic finite simple graphs only, not arbitrary multicyclic graphs; with two or more cycles a principal Pfaffian can have additional terms and cancellations. Finite computational tests alone would not prove the all-field result; the Pfaffian argument supplies the infinite proof. The group-theoretic consequence is limited to **odd** prime powers, where the standard class-two orbit-method correspondence applies in the stated form. No scheme-theoretic multiplicity or conjugacy-orbit classification is claimed. Independent validation and an exhaustive publication-priority investigation have not been performed.

## References

- Meera G. Mainkar, “A short note on 2-step nilpotent Lie algebras associated with graphs,” arXiv:1010.4005v1 (19 October 2010), https://arxiv.org/abs/1010.4005.
- Xueliang Li and Guihai Yu, “The skew-rank of oriented graphs,” arXiv:1404.7230v1 (29 April 2014), https://arxiv.org/abs/1404.7230.
- Tobias Rossmann, “Enumerating conjugacy classes of graphical groups over finite fields,” Bulletin of the London Mathematical Society 54 (2022), 1923–1943, https://doi.org/10.1112/blms.12665; in particular Section 1.6 and Question 1.10.
