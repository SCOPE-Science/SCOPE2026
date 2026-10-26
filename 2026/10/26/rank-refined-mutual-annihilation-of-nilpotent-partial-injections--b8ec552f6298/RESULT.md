# Rank-refined mutual annihilation of nilpotent partial injections

## Finding

Let \(\mathcal I_n\) be the symmetric inverse monoid of all partial injective transformations on a labeled \(n\)-element set, with zero the empty partial map. Call an element nilpotent when some positive power is zero. For integers \(n\ge2\) and \(r,s\ge0\), let \(P_n(r,s)\) denote the number of ordered pairs of nilpotent elements \((\alpha,\beta)\) satisfying
\[
\alpha\beta=\beta\alpha=0,\qquad
\operatorname{rank}(\alpha)=r,\quad\operatorname{rank}(\beta)=s.
\]
Write \(h=n-r-s\). The complete bivariate rank distribution is
\[
\boxed{P_n(r,s)=\frac{n!(n-2)!}{r!\,s!\,(h!)^2}\big((n-1)h+rs\big)}
\qquad(0\le r,s\le n-1,\ h\ge0).
\]
When \(r+s>n\) or either rank is at least \(n\), the count is zero. At \(n=1\), the only pair is \((0,0)\), so \(P_1(0,0)=1\). The formula is symmetric under exchanging the two ranks. In particular the sharp joint-rank boundary is \(r+s\le n\), with every rank pair inside this boundary and satisfying \(r,s<n\) realized. At \(r+s=n\) and \(r,s\ge1\), the boundary count simplifies to
\[
P_n(r,s)=n!\binom{n-2}{r-1}.
\]
A supplementary structural statement is the following: for any fixed nilpotent \(\alpha\) of rank \(r\), the number of nilpotent \(\beta\) of rank \(s\) annihilating \(\alpha\) on both sides depends on \(\alpha\) **only** through \(r\) and the number \(c\) of singleton chains (isolated vertices) in its directed-chain decomposition. It equals
\[
\boxed{\binom{n-r}{s}^{\!2}s!-c\binom{n-r-1}{s-1}^{\!2}(s-1)!},
\]
where a term with a negative lower index is zero.

## Assumptions and scope

All sets are labeled. A partial injection is a bijection from a subset (its domain) to another subset (its image); its rank is the cardinality of either subset. Products are compositions. Both orders of composition are required to be the empty partial map, so the composition convention does not affect the claim. Nilpotence means the functional directed graph has no directed cycle, equivalently it is a disjoint union of directed chains, including isolated vertices. The zero map, of rank zero, is nilpotent. We count actual ordered maps, not isomorphism classes, conjugacy orbits, or pairs modulo relabeling. No field is involved.

## Proof

**1. Fixing the first map.** Let \(D=\operatorname{dom}(\alpha)\), \(R=\operatorname{im}(\alpha)\), \(|D|=|R|=r\), and \(m=n-r\). The identity \(\alpha\beta=0\) holds exactly when \(\operatorname{im}(\beta)\subseteq X\setminus D\); the identity \(\beta\alpha=0\) holds exactly when \(\operatorname{dom}(\beta)\subseteq X\setminus R\). Put \(A=X\setminus R\), \(B=X\setminus D\), both of size \(m\). Thus \(\beta\) is an injective partial map from \(A\) to \(B\). The number of such maps of rank \(s\), without nilpotence imposed, is \(\binom ms^2s!\). (The conditions on domain/image follow directly by evaluating both composites at every point.)

**2. Excluding cycles.** Any directed cycle of \(\beta\) lies wholly in \(C=A\cap B=X\setminus(D\cup R)\), whose size \(c\) is the number of isolated vertices in the chain decomposition of \(\alpha\). To count acyclic \(\beta\), perform inclusion–exclusion over all directed cycles supported on \(C\). Select a union of cycles on a \(j\)-element subset of \(C\). Such a union is a permutation of the selected \(j\) elements, weighted by \((-1)^{\text{number of cycles}}\). The remaining rank-\((s-j)\) map has both domain and image chosen from sets of size \(m-j\), so the completion count is \(\binom{m-j}{s-j}^2(s-j)!\). The total signed weight of all permutations of a fixed \(j\)-set is
\[
\sum_{\pi\in S_j}(-1)^{\#\mathrm{cycles}(\pi)}
=(-1)(0)(1)\cdots(j-2),
\]
with the empty-set value one. It is \(-1\) at \(j=1\) and zero for every \(j\ge2\). Therefore the entire cycle sieve collapses to only two terms:
\[
B_{\alpha}(s)=\binom ms^2s!-c\binom{m-1}{s-1}^2(s-1)!.
\]
This proves the conditional assertion, including \(s=0\) under the stated zero convention. The argument does not assume all cycles have the same length: every disjoint selection is included by its permutation and alternating number of cycles.

**3. Summing over nilpotent first maps.** A nilpotent partial injection of rank \(r\) has exactly \(m=n-r\) chains. The number of chain decompositions into \(m\) unlabeled, internally ordered nonempty blocks is the unsigned Lah number
\[
L(n,m)=\frac{n!}{m!}\binom{n-1}{m-1}
=\frac{n!}{m!}\binom{n-1}{r}.
\]
This follows by ordering all \(n\) labels, choosing \(m-1\) cuts among their consecutive gaps, and dividing by \(m!\) to forget the order of the blocks. The sum of the singleton-chain counts \(c\) over all nilpotent rank-\(r\) maps is \(nL(n-1,m-1)\): mark an isolated vertex, remove it, and count the remaining \(m-1\) chains. Adopt \(L(0,0)=1\) and \(L(a,b)=0\) for infeasible parameters. Consequently
\[
P_n(r,s)=L(n,m)\binom ms^2s!
-nL(n-1,m-1)\binom{m-1}{s-1}^2(s-1)!.
\]
For \(m\ge2\), substitute the factorial forms and cancel, obtaining
\[
P_n(r,s)=\frac{n!(n-2)!}{r!s!h!^2}\big((n-1)(n-r)-(n-r-1)s\big)
=\frac{n!(n-2)!}{r!s!h!^2}\big((n-1)h+rs\big).
\]
For \(m=1\), the first map is a single Hamiltonian chain, has \(c=0\), and there are \(n!\) such maps. The only allowed ranks of \(\beta\) are zero and one, with exactly one eligible \(\beta\) for either rank. The displayed symmetric formula gives \(n!\) in both cases, so the boundary is also covered. The case \(n=1\) is checked directly.

**4. Feasibility and boundary.** Any rank-\(s\) partial injection from \(A\) into \(B\) requires \(s\le n-r\), proving \(r+s\le n\). Conversely the numerator of the explicit count is strictly positive for every \(n\ge2\), \(r,s\le n-1\), and \(r+s\le n\): if \(h>0\), the \((n-1)h\) term is positive; if \(h=0\), the rank restrictions force \(r,s\ge1\) and then \(rs>0\). Thus every allowed pair occurs. Substituting \(h=0\) yields \(P_n(r,s)=n!\binom{n-2}{r-1}\).

## Verification

The companion standalone Python standard-library program `verify_nilpotent_mutual_zero.py` generates every partial injection, tests nilpotence by following arrows, tests both zero products by actual compositions for \(n\le5\), and independently tests them via domain–image masks for \(n=6\). For every rank pair, it compares the exact integer count against the theorem. It exhausts all \(1,4,9,16,25,36\) rank cells in sizes \(1\) through \(6\), respectively. The total ordered-pair counts in these sizes are \(1,7,55,565,7141,106891\). The expected successful terminal line is `VERIFY_OK_NILPOTENT_MUTUAL_ZERO_RANKS`. These finite checks support, but cannot replace, the general proof above.

## Relationship to prior work

The classical chain decomposition of nilpotents and its Lah-number census are established in Gomes–Howie (1987) and used here as input, not presented as new. Ganyushkin–Mazorchuk (2005, Sections 2 and 6) study combinatorics of partial injections and distributions of products; their unrestricted product calculations do not give the simultaneous nilpotence, mutual zero-product, and prescribed two-rank distribution here. Their 2004 Annals of Combinatorics paper on nilpotent elements and nilpotent subsemigroups is a relevant predecessor, but its full text could not be obtained. Araújo–Bentz–Konieczny (2012) analyze commuting graphs and commuting nilpotent structures rather than this mutually annihilating rank distribution. Laradji–Umar (2022) treat height, fixed-point count, waist and derangements of individual partial injections, not products of two maps. The new object is a full, symmetric two-rank refinement for *both nilpotent factors*, together with the conditional two-term cancellation that underlies its formula.

## Limitations

Only the finite symmetric inverse monoid of partial injections is addressed; the theorem does not count arbitrary noninjective transformations, nonnilpotent factors, commuting pairs with nonzero products, or orbit classes. The cycle-cancellation argument requires the domain/image restrictions forced by both products vanishing. Search and inspected-source comparisons support the absence of a directly covering result in the checked literature, but cannot establish absolute historical priority; notably, the full text of the plausible Ganyushkin–Mazorchuk (2004) predecessor was inaccessible. An implicit or unindexed equivalent formula may exist. The finite verification is not a substitute for the all-size proof. No independent mathematical audit has been performed.

## References

1. O. Ganyushkin and V. Mazorchuk, *Combinatorics and distributions of partial injections*, first public arXiv version dated 17 November 2005; https://arxiv.org/abs/math/0511431 .
2. G. M. S. Gomes and J. M. Howie, *Nilpotents in finite symmetric inverse semigroups*, Proceedings of the Edinburgh Mathematical Society (1987); DOI: 10.1017/S0013091500026778 .
3. J. Araújo, W. Bentz and J. Konieczny, *The commuting graph of the symmetric inverse semigroup*, arXiv:1205.1664 (first public version dated 8 May 2012); https://arxiv.org/abs/1205.1664 .
4. A. Laradji and A. Umar, *Further combinatorial results for the symmetric inverse monoid*, Algebra and Discrete Mathematics 33 (2022), 78–91; https://admjournal.luguniv.edu.ua/index.php/adm/article/viewFile/1793/pdf .
5. O. Ganyushkin and V. Mazorchuk, *Combinatorics of nilpotents in symmetric inverse semigroups*, Annals of Combinatorics 8 (2004), 161–175, DOI: 10.1007/s00026-004-0213-7 (full text not inspected).
