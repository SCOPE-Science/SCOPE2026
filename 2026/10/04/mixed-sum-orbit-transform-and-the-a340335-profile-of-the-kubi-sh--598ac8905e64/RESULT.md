# Mixed-sum orbit transform and the A340335 profile of the Kubiś–Shelah torsion-free limit

## Finding
Let \(\mathscr F\) and \(\mathscr G\) be relational Fraïssé classes with disjoint amalgamation, and suppose their numbers of labeled structures on fixed \(p\)-point carriers are finite; write these numbers as \(f_p\) and \(g_p\). Let \(U\) be the Fraïssé limit of the Kubiś–Shelah mixed sum \(\mathscr F\pm\mathscr G\). If \(a_n\) is the number of \(\operatorname{Aut}(U)\)-orbits on injective ordered \(n\)-tuples, then
\[
\boxed{a_n=\sum_{p=0}^n {n\choose p}f_p g_{n-p}2^{p(n-p)}}.
\]

In the concrete Kubiś–Shelah torsion-free example, \(\mathscr F\) is the class of finite pure sets and \(\mathscr G\) is the class of finite linear orders. Thus \(f_p=1\) and \(g_q=q!\), so
\[
\boxed{a_n=n!\sum_{p=0}^n\frac{2^{p(n-p)}}{p!}}.
\]
Starting at \(n=0\), this is
\[
1,2,7,43,441,7241,185233,7252337,429318529,38079107713,5026601726721,\ldots,
\]
which is exactly OEIS A340335. Consequently its exponential generating function is
\[
\sum_{n\ge0}a_n\frac{x^n}{n!}
 =\sum_{p\ge0}\frac{x^p/p!}{1-2^p x}
 =\sum_{q\ge0}x^q e^{2^q x}.
\]
For all ordered tuples, allowing repetitions, the profile is the Stirling transform
\[
\boxed{b_n=\sum_{k=1}^n {n\brace k}a_k},
\]
with initial values
\[
1,2,9,66,750,12833,326602,12323706,690051563,57429171592,7109345894406,\ldots.
\]

## Assumptions and scope
The formula is for the mixed-sum language itself, including the named left and right predicates, the two component signatures, and the bipartite edge relation. The labeled profile \(f_p\) means the number of \(\mathscr F\)-structures on one fixed labeled \(p\)-element set, and similarly for \(g_p\). The finiteness hypothesis is automatic for the usual finite relational signatures considered here; it is stated because an oligomorphic orbit count must be finite.

Kubiś and Shelah define a mixed sum by splitting the carrier into disjoint left and right parts carrying an \(\mathscr F\)- and a \(\mathscr G\)-structure, with an otherwise arbitrary bipartite graph between the parts. Their Lemma 4.1 proves that disjoint amalgamation passes to the mixed sum. Their application takes finite sets on the left and finite linear orders on the right; the resulting limit has torsion-free automorphism group even though its age contains finite structures with every finite symmetric group as an automorphism group.

The first public arXiv version of the source is dated 2018-11-23. The paper lists MSC 20A15, 03C15, and 03C50; this ledger files the result under 03C15 because the contribution is a countable-homogeneous/Fraïssé orbit statement.

## Proof
Fix an injective ordered tuple \(\bar x=(x_1,\ldots,x_n)\) in \(U\). Because \(U\) is homogeneous, two injective ordered tuples lie in the same automorphism orbit exactly when the map \(x_i\mapsto y_i\) is an isomorphism between their induced labeled finite substructures. Therefore the orbit count is the number of mixed-sum structures on the fixed labeled carrier \([n]\).

Suppose the left part has size \(p\). There are \({n\choose p}\) choices for which tuple positions are left. Once those positions are chosen, there are \(f_p\) possible labeled \(\mathscr F\)-structures on them and \(g_{n-p}\) possible labeled \(\mathscr G\)-structures on the complementary positions. Finally, the mixed-sum definition imposes no restriction on the cross relation: each of the \(p(n-p)\) left-right pairs independently may be an edge or a nonedge. Hence there are \(2^{p(n-p)}\) cross-edge choices. Summing over \(p\) proves
\[
a_n=\sum_{p=0}^n {n\choose p}f_p g_{n-p}2^{p(n-p)}.
\]

For the Kubiś–Shelah application, \(f_p=1\) and \(g_{n-p}=(n-p)!\). Since \({n\choose p}(n-p)!=n!/p!\), this becomes
\[
a_n=n!\sum_{p=0}^n\frac{2^{p(n-p)}}{p!}.
\]
Dividing by \(n!\) and summing over \(n\), then writing \(n=p+q\), gives
\[
\sum_{n\ge0}a_n\frac{x^n}{n!}
=\sum_{p,q\ge0}\frac{x^{p+q}2^{pq}}{p!}
=\sum_{p\ge0}\frac{x^p/p!}{1-2^p x},
\]
and exchanging the two summations gives \(\sum_{q\ge0}x^q e^{2^q x}\).

For a possibly noninjective ordered \(n\)-tuple, its equality kernel is a set partition of \([n]\) into, say, \(k\) blocks. Ordering those blocks canonically by their least positions turns the tuple into an injective ordered \(k\)-tuple of realized elements, and this construction is reversible. There are \({n\brace k}\) equality kernels, which proves the Stirling transform for \(b_n\).

## Verification
The bundled standard-library `verify.py` performs an object-level replay of the concrete finite age through \(n=6\). For every labeled carrier it iterates every left subset, every linear order of the right complement, and every cross-edge mask, and checks the resulting counts against the closed formula. It independently checks the OEIS A340335 initial segment through \(n=12\), the exact exponential-generating-function coefficient identity, the Stirling transform for all tuples, and two synthetic specializations of the general mixed-sum transform. Its final line is `VERIFY_OK`.

## Relationship to prior work
Kubiś–Shelah's mixed-sum construction and the Fraïssé/disjoint-amalgamation theorem are prior work, as is their finite-set/linear-order application. OEIS A340335 is also prior: it records exactly the numerical sequence above and the two equivalent exponential generating functions. Those facts are not claimed as new.

The retained contribution is the general labeled-age/orbit transform for a mixed sum and its explicit model-theoretic identification of A340335 as the injective ordered-tuple orbit profile of the Kubiś–Shelah torsion-free limit. Targeted exact-formula, terminology, published-finding corpus, and own-ledger searches found no source stating this bridge. A 2025 classification by J. K. Truss treats homogeneous ordered bipartite graphs, including the one-side-ordered Fraïssé limit, but does not provide this general mixed-sum orbit transform. Because the transform is an immediate but apparently unrecorded consequence of homogeneity and the mixed-sum definition, the originality claim is deliberately narrow.

## Limitations
The search cannot exclude an unindexed or differently phrased folklore observation. The result is enumerative rather than a new structural theorem about automorphism-group universality. The general formula also presupposes finite labeled age profiles \(f_p,g_p\), as needed for finite orbit counts. No independent audit has yet been performed; the current package contains same-model review plus executable finite replay.

## References
1. W. Kubiś and S. Shelah, *Homogeneous structures with non-universal automorphism groups*, arXiv:1811.09650; Journal of Symbolic Logic 85 (2020), 817–827; DOI 10.1017/jsl.2020.10.
2. OEIS Foundation Inc., OEIS A340335, sequence with e.g.f. \(\sum_{m\ge0}x^m e^{2^m x}\).
3. J. K. Truss, *Countable homogeneous ordered bipartite graphs*, Archive for Mathematical Logic 64 (2025), 1165–1180; DOI 10.1007/s00153-025-00986-1.
