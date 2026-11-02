# Automorphism groups and singleton rigidity of finite rectangular-band power semigroups

## Finding
Let \(I,J\) be finite nonempty sets, with \(|I|=a\) and \(|J|=b\). Equip the rectangular band \(B=I\times J\) with \((i,j)(k,\ell)=(i,\ell)\), and let \(\mathcal P^*(B)\) be its semigroup of **nonempty** subsets under setwise multiplication. Define \(N_{u,v}\) to be the number of subsets of \([u]\times[v]\) meeting every row and column, **excluding** the full rectangle:
\[
N_{u,v}=\sum_{i=0}^u\sum_{j=0}^v(-1)^{i+j}\binom ui\binom vj\,2^{(u-i)(v-j)}-1.
\]
For \(a,b\ge2\), the full automorphism group is
\[
\operatorname{Aut}(\mathcal P^*(B))\cong
\left(\prod_{\substack{\varnothing\ne A\subseteq I\\\varnothing\ne C\subseteq J}}S_{N_{|A|,|C|}}\right)
\rtimes\left(\prod_{u=1}^aS_{\binom au}\times\prod_{v=1}^b S_{\binom bv}\right),
\]
where \(S_0\) and \(S_1\) are trivial, and the right factor acts by relabeling the fibers indexed by subsets of each fixed cardinality. In particular,
\[
\bigl|\operatorname{Aut}(\mathcal P^*(B))\bigr|=
\left[\prod_{u=1}^a\prod_{v=1}^b(N_{u,v}!)^{\binom au\binom bv}\right]
\left[\prod_{u=1}^a\binom au!\right]
\left[\prod_{v=1}^b\binom bv!\right].
\]
For \(\min(a,b)=1\), \(\mathcal P^*(B)\) is a left- or right-zero band of cardinality \(2^{\max(a,b)}-1\); its full automorphism group is consequently \(S_{2^{\max(a,b)}-1}\).

**Singleton-rigidity boundary.** Every automorphism of \(\mathcal P^*(B)\) maps singleton subsets of \(B\) to singleton subsets if and only if either \(a,b\ge2\) or \(a=b=1\). If exactly one dimension equals one and the other exceeds one, there exist automorphisms carrying a singleton to a nonsingleton. In the smallest two-sided case, \(\operatorname{Aut}(\mathcal P^*(B_{2,2}))\cong S_6\times S_2\times S_2\), of order \(2880\), whereas \(\operatorname{Aut}(B_{2,2})\) has order \(4\).

## Assumptions and scope
All underlying sets are finite and nonempty. The empty subset is **excluded** from the power semigroup. Isomorphisms are semigroup automorphisms, without any requirement to preserve inclusion, union, subset cardinality, or the set of original singleton subsets. The formula concerns the full nonempty-subset semigroup, not the monoid of identity-containing subsets. The classification is for fixed \(a,b\) and does not assert the classification of isomorphisms between different rectangular bands' power semigroups.

## Proof
**1. The multiplication and idempotents.** For \(X\subseteq I\times J\) nonempty, define the nonempty row and column projections
\[
R(X)=\{i\in I:\exists j\ (i,j)\in X\},\quad C(X)=\{j\in J:\exists i\ (i,j)\in X\}.
\]
Direct substitution into the rectangular-band operation gives
\[
XY=R(X)\times C(Y),\qquad X^2=R(X)\times C(X).
\]
Consequently an element is idempotent exactly when it is a full nonempty rectangle. The idempotent subsemigroup \(E\) identifies with the rectangular band \(\mathcal P^*(I)\times\mathcal P^*(J)\), with product \((A,C)(A',C')=(A,C')\). Every automorphism of \(E\) has the form \((A,C)\mapsto(\alpha(A),\beta(C))\), for arbitrary permutations \(\alpha\in S_{2^a-1}\) and \(\beta\in S_{2^b-1}\): the \(\mathcal R\)- and \(\mathcal L\)-classes of a rectangular band are intrinsic, so an automorphism independently permutes its row and column classes, and every such pair works.

**2. Support fibers.** For nonempty \(A\subseteq I\), \(C\subseteq J\), set \(F_{A,C}=\{X:R(X)=A,\ C(X)=C\}\). It contains exactly one idempotent, the rectangle \(A\times C\). Inclusion-exclusion on missing rows and columns shows \(|F_{A,C}|=N_{|A|,|C|}+1\). The formula in the finding counts binary incidence matrices with no zero row or column, minus their unique all-one matrix. Since \(X^2=A\times C\), any automorphism of the full power semigroup, whose restriction to \(E\) is \((\alpha,\beta)\), must bijectively send \(F_{A,C}\) onto \(F_{\alpha(A),\beta(C)}\), fixing the prescribed rectangle relative to its destination. Thus it induces arbitrary bijections between the nonidempotent portions of corresponding fibers whenever those portions have the same size.

**3. Intrinsic projection cardinalities.** Assume \(a,b\ge2\). For every fixed \(v\ge2\), the sequence \(N_{1,v},N_{2,v},\dots,N_{a,v}\) is strictly increasing. Indeed, any nonfull incidence pattern with no empty row or column on \(u\times v\) embeds on \((u+1)\times v\) by adjoining one completely filled row; its image is nonfull, and the embedding is injective. The image is a proper subset: on \((u+1)\times v\), the graph with a single missing edge in the newly adjoined row has no isolated vertex but is not in the image (also when \(u=1\)). In addition, for fixed \(u\), \(N_{u,v}\) is nondecreasing with \(v\), by adjoining a completely filled column (the case of a full source gives zero nonfull patterns in both). It follows that
\[
\max_{\varnothing\ne C\subseteq J}(|F_{A,C}|-1)=N_{|A|,b},
\]
which distinguishes \(|A|=1,\dots,a\). Because any automorphism merely permutes the column fibers while sending \(A\) to \(\alpha(A)\), the maximum is invariant. Hence \(|\alpha(A)|=|A|\). By exchanging rows and columns, \(|\beta(C)|=|C|\). Thus \(\alpha\) and \(\beta\) belong precisely to the products of symmetric groups on subsets of each fixed cardinality, respectively.

**4. Sufficiency and semidirect product.** Conversely, choose any such cardinality-preserving pair \((\alpha,\beta)\). On each support fiber choose any bijection onto the corresponding fiber that maps its unique rectangle to its unique target rectangle. The resulting map \(\Phi\) is a permutation of all nonempty subsets. For all nonempty \(X,Y\),
\[
\Phi(XY)=\alpha(R(X))\times\beta(C(Y))=\Phi(X)\Phi(Y),
\]
so it is a semigroup automorphism. This gives all automorphisms by steps 1–3. The kernel of restriction to \(E\) is the product of the full symmetric groups on the nonrectangular elements of each support fiber. Fix an ordering of nonrectangular subsets in each fiber according to the same canonical order on incidence matrices of its dimensions (any consistent choice suffices). Transporting the \(k\)-th nonrectangular element of one fiber to the \(k\)-th of its image produces a homomorphic splitting of restriction to \(E\), proving the asserted semidirect-product description. Taking orders yields the factorial formula.

**5. Boundary and singleton criterion.** If \(a=1\), then \(XY=Y\), a right-zero operation on all \(2^b-1\) nonempty subsets; if \(b=1\), then \(XY=X\), a left-zero operation. Every permutation is then an automorphism. For \(\max(a,b)\ge2\) a permutation can exchange a singleton with a nonsingleton. If \(a=b=1\) there is only one subset. If \(a,b\ge2\), a singleton is the unique member of a fiber whose row and column projections each have cardinality one; since projection cardinalities are invariant, every automorphism sends singleton to singleton. Finally, for \(a=b=2\), all nonrectangular subsets lie in the full-support fiber and number \(N_{2,2}=6\), while each of the two index-set permutation groups has order two. The full group is therefore \(S_6\times S_2\times S_2\) and has order \(720\cdot4=2880\).

## Verification
The standalone script `check.py` uses explicit bit-set multiplication and a separately implemented inclusion-exclusion count. It checks every support fiber for \((a,b)=(1,1),(1,3),(2,2),(2,3),(3,2),(3,3)\), checks the product law for every pair of elements in those finite cases, constructs all \(2880\) automorphisms from the claimed \(2\times2\) description and verifies all \(225\) multiplication identities for each, and constructs four further sample automorphisms for the \(2\times3\) case, checking all \(3969\) product pairs each. Its terminal result is `VERIFY_OK`. The general classification is proved in steps 1–5, not inferred from these computations.

## Relationship to prior work
Liu and Tringali's 2026 paper on Kobayashi's problem proves singleton preservation for power semigroups of inverse semigroups, and explicitly identifies this as a rigidity problem. A rectangular band with both factors nontrivial is a completely simple idempotent semigroup but not an inverse semigroup, so its theorem does not cover the present setting. The singleton-rigidity boundary above provides an exact test case outside their hypothesis.

Tamura and Shafer announced in 1968 that the power semigroup of a rectangular band is a rectangular band of null semigroups; this describes an underlying decomposition but does not, from the accessible abstract alone, settle the present full automorphism-group formula, the factorial enumeration, or the sharp singleton threshold. Tamura's 1984 paper on power semigroups of rectangular groups and 1986 paper on the isomorphism problem for completely \(0\)-simple semigroups are materially relevant historical sources; their complete texts were not accessible for the necessary direct implications comparison. Stronger coverage in one of these sources remains a residual originality risk. General work on isomorphism of power semigroups distinguishes global determination from the stronger property that every isomorphism preserves singleton subsets.

## Limitations
The exact formula is for finite rectangular bands, not arbitrary regular semigroups or Rees matrix semigroups with nontrivial structure groups. It uses the nonempty-subset power semigroup (including all finite subsets because the base is finite). Nothing here classifies isomorphisms between power semigroups of different bands. The use of a symbolic proof and finite checks supports correctness but does not provide independent audit or guarantee absolute historical novelty; in particular the older Tamura papers identified above were not available in full text for assessment.

## References
1. S. Liu and S. Tringali, *Kobayashi's problem for power semigroups of inverse semigroups*, arXiv:2610.29525v1, first public 21 October 2026, https://arxiv.org/abs/2610.29525 . Sections 1, 3–5 of accessible HTML read (especially introduction and statement of rigidity).
2. T. Tamura and J. Shafer, *Power semigroups II*, Notices Amer. Math. Soc. **15** (1968), p. 395, abstract reporting the rectangular-band-of-null-semigroups structure; https://www.ams.org/journals/notices/196802/196802FullIssue.pdf (full PDF inaccessible).
3. T. Tamura, *Power semigroups of rectangular groups*, Math. Japonica **29** (1984), 671–678 (complete text not obtained).
4. T. Tamura, *Isomorphism problem of power semigroups of completely 0-simple semigroups*, J. Algebra **98** (1986), 319–361, https://doi.org/10.1016/0021-8693(86)90002-5 (only bibliographic information and secondary theorem descriptions inspected).
5. S. Tringali and K. Wen, *On the automorphisms of the power semigroups of a numerical semigroup*, Trans. London Math. Soc. (2026), https://doi.org/10.1112/tlm3.70030 , introduction and main statements inspected for distinctions of setting.
