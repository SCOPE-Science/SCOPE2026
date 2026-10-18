# Sixteen leaves are the sharp threshold for two-moment phylogenetic-rarefaction ambiguity

## Finding

Consider all *unlabelled, non-plane rooted full binary phylogenetic tree shapes* on \(n\) leaves, with length one assigned to **every** edge. Let \(K\) be a uniformly chosen \(k\)-element leaf set, and let \(P_T(k)\) count the edges on the union of all root-to-leaf paths for the leaves in \(K\) (rooted Faith phylogenetic diversity). The complete first- and second-moment profiles are \((\mathbb E P_T(k),\operatorname{Var}P_T(k))_{k=1}^n\).

**Sharp identification and obstruction.** For every \(1\le n\le15\), equality of these profiles implies rooted-shape isomorphism. At \(n=16\), precisely one unordered pair of distinct shapes has the same profile. With \(\bullet\) a leaf, define the distinct four-leaf shapes \(C=(\bullet,(\bullet,(\bullet,\bullet)))\) and \(B=((\bullet,\bullet),(\bullet,\bullet))\). The exceptional pair is

\[
T_A=((C,C),(B,B)),\qquad T_M=((C,B),(C,B)).
\]

For a uniform two-leaf sample, their third binomial moments are separated:

\[
\mathbb E\!\left[\binom{P_{T_M}(2)}3\right]-\mathbb E\!\left[\binom{P_{T_A}(2)}3\right]=\frac1{120}.
\]

Thus the first three complete moment profiles identify every shape on at most sixteen leaves. Conversely, first-two-moment ambiguity occurs for **every** larger leaf count by adding an identical succession of new roots with a single new leaf attached to each tree.

## Assumptions and scope

- The root is distinguished and both children of each internal node are unordered; leaves carry no identifying labels, and every internal vertex has exactly two children.
- The original root has no incoming edge. Each of the \(2n-2\) edges has length exactly one. This unit-edge regime need not be ultrametric; the conclusion is **not** asserted for arbitrary edge lengths or arbitrary ultrametric phylogenies.
- Each of the \(\binom nk\) subsets of \(k\) distinct leaves is equiprobable; sampling is without replacement, one observation per leaf, for every integer \(0\le k\le n\). The empty-set PD is defined to be zero.
- The inverse problem determines an unlabelled rooted topology, not the positions or biological identities of labelled taxa, which sampling statistics alone cannot identify.

## Proof

**1. Exact moment fingerprint.** Index the nonroot edges by \(e\), and let \(D_e\) be the descendant leaf set below edge \(e\). Write \(m=2n-2\), \(a_s=\#\{e:|D_e|=s\}\), and let \(b_s\) count unordered pairs of **distinct** edges \(\{e,f\}\) with \(|D_e\cup D_f|=s\). Put

\[
q_s(k)=\frac{\binom{n-s}{k}}{\binom nk},\quad \binom rk=0\ \text{if }k>r.
\]

The indicator that edge \(e\) belongs to the spanned rooted subtree is \(I_e=1-\mathbf1_{\{K\cap D_e=\varnothing\}}\). Hence \(P_T(k)=\sum_e I_e\). By summing its individual and pair expectations,

\[
\begin{aligned}
\mathbb E P_T(k)&=m-\sum_{s=1}^{n-1}a_s q_s(k),\\
\mathbb E[P_T(k)^2]&=(2m-1)\mathbb E P_T(k)-m(m-1)+2\sum_{s=1}^{n}b_s q_s(k).
\end{aligned}
\]

The variance is the displayed second raw moment minus the square of the mean. For \(1\le j\le n-1\), put \(k=n-j\). Then \(q_s(n-j)=0\) for \(s>j\) and \(q_j(n-j)>0\). The resulting coefficient matrix is triangular with nonzero diagonal. Thus the full mean profile determines each \(a_s\), and the full second-moment profile subsequently determines each \(b_s\) for \(s<n\). The remaining \(b_n\) follows from \(\sum_s b_s=\binom m2\). Therefore **two complete mean-and-variance profiles agree if and only if their integer pairs \((a,b)\) agree**. This equivalence replaces comparisons of real-valued curves by exact finite integer signatures.

**2. Exhaustive sharp bound and uniqueness.** Define an unordered binary shape recursively as an unordered pair of two smaller shapes, with \(\bullet\) the unique one-leaf shape. For each split \(n=a+(n-a)\) with \(1\le a\le n-a\), pair every shape of sizes \(a\) and \(n-a\), then canonically sort the children and remove duplicates. The recursion lists every unlabelled non-plane full binary shape exactly once: every shape has a unique pair of root subshapes up to swapping, and induction covers each child. Starting with one leaf, exhaustive generation gives, at consecutive sizes from one to sixteen, exactly

\[
1,1,1,2,3,6,11,23,46,98,207,451,983,2179,4850,10905
\]

shapes. For each shape, enumerate descendant-leaf bit masks in canonical depth-first leaf order. Form \(a_s\) by counting set sizes and \(b_s\) by counting bitwise-union sizes for every edge pair. Hash the resulting exact integer tuples. The number of distinct signatures agrees with the number of shapes through fifteen leaves; at sixteen leaves, all \(10905\) shapes occupy exactly \(10904\) distinct signatures, one with multiplicity two and all other signatures unique. The two shapes in that signature are exactly the displayed \(T_A,T_M\). The self-contained `verify.py` supplies the complete algorithm and all integer assertions; its executable output is `CERTIFICATE.json`. This is exhaustive, not an inference from numerical interpolation.

**3. Structural explanation of the exceptional collision.** Both constructions contain the same four equal-size four-leaf modules, two copies of \(C\) and two of \(B\), and two upper edges descending into eight-leaf groups. Individual descendant-set sizes are unchanged by regrouping. For edge pairs, the cases are: both edges within one module; edges in different modules (always disjoint, irrespective of which eight-leaf group contains them); an upper eight-leaf edge paired with a module edge (one upper edge contains the module and the other is disjoint); and the two upper edges. Each case contributes the same multiset of union sizes in the two constructions. Thus \(a\) and \(b\) match. The root children of \(T_A\) are unlike one another, \((C,C)\) and \((B,B)\); the children of \(T_M\) are isomorphic copies of \((C,B)\). Since \(C\not\cong B\), the full shapes are not isomorphic.

The common single-edge-size histogram is

\[
(a_1,a_2,a_3,a_4,a_8)=(16,6,2,4,2),
\]

with all other entries zero. For edge pairs the nonzero \(b_s\) are, in order of \(s=2,3,4,5,6,7,8,9,10,11,12,16\),

\[
(132,92,65,58,19,6,34,16,6,2,4,1),
\]

whose total is \(435=\binom{30}{2}\).

**4. The third-moment separation.** Exhaustively selecting each of the \(\binom{16}{2}=120\) leaf pairs gives

\[
\sum_{|K|=2}\binom{P_{T_A}(K)}3=5909,\qquad
\sum_{|K|=2}\binom{P_{T_M}(K)}3=5910.
\]

The difference is \(1/120\) after dividing by the 120 equally likely samples. The verifier calculates these integers directly from all subsets, without using the signature construction; it also confirms equality of first and second raw moments for every \(k\) by enumerating every one of the \(2^{16}=65536\) subsets of each tree. Since at most one first-two-moment collision occurs through sixteen leaves, its separation at the third moment yields third-moment identification throughout this finite range.

**5. Extension to every larger leaf count.** Given a tree \(T\) on \(n\) leaves, form \(U(T)=(\bullet,T)\) by attaching a new root with one leaf child. Every old descendant clade remains, and exactly two new edge clades appear: one singleton and one containing all \(n\) old leaves. If two original trees share both \(a\) and \(b\), these new clades contribute the same numbers of all edge-clade sizes and pairwise union sizes in both extensions. Hence equality of both moment curves is preserved. The two extensions remain nonisomorphic because their unique nonleaf child at the root is the original tree. Repetition gives indistinguishable nonisomorphic pairs for all \(n\ge16\).

## Verification

`verify.py` is an executable, dependency-free Python program. Run `python3 verify.py` and compare its standard output byte-for-byte with `CERTIFICATE.json`. It asserts the canonical enumeration counts, the uniqueness and explicit shape of the sixteen-leaf collision, the exact fingerprints, equal first and second raw moments from independent subset enumeration across every sampling depth, and the 5909-versus-5910 third-binomial-moment separation. All calculations use exact integers. For independent implementation checks, recompute sample means from the explicit edge-indicator formula and evaluate the sixteen-leaf witness by enumerating its \(120\) leaf pairs.

## Relationship to prior work

Nipperess and Matsen established exact mean and variance formulas for phylogenetic diversity under rarefaction (first made public in 2012); the general moment-calculation framework is therefore **not** new. The present result concerns the inverse identification of unlabelled topology from the *entire* moment curves and the smallest unavoidable collision. Schwob's work and OEIS A382440 already study subtree-size multisets of binary trees. In the unit-edge regime these are equivalent to **mean-only** rarefaction data, so their existing counts and collisions are not new here. The new finite invariant includes all pairwise unions of descendant clades, capturing variance, and the sixteen-leaf threshold is a different inverse question. Published related results and limits of literature inspection are discussed in the reference list.

## Limitations

The classification through sixteen leaves is computationally exhaustive with a fully specified and replayable combinatorial search, not an analytic closed-form classification for arbitrary \(n\). The infinite collision family is constructive; uniqueness is asserted **only at sixteen leaves**. Unit edge lengths are an exact assumption and may not model molecular-clock trees. No claim is made about identifiability under arbitrary weighted branches, unknown labels, sampling error, noisy empirical PD estimates, or sampling with replacement. Having different third moments does not establish a simple practical estimator under finite sampling.

## References

1. Nipperess, D. A. and Matsen, F. A. IV, *The mean and variance of phylogenetic diversity under rarefaction*, arXiv:1208.6552, first posted 2012-08-31; full technical text: https://arxiv.org/html/1208.6552v2.
2. Schwob, L., *Middle orders: all distributive lattices between weak and Bruhat*, arXiv:2606.12129v1 (2026), especially Section 5.1 on subtree-size multisets: https://arxiv.org/html/2606.12129v1.
3. OEIS A382440, *Number of rooted full binary trees with n internal nodes, up to their multiset of subtree sizes*: https://oeis.org/A382440. These known single-size counts are used only to cross-check the mean-only part.
