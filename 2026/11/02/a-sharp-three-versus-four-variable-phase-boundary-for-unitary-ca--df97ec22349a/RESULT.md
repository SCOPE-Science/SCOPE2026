# A sharp three-versus-four-variable phase boundary for unitary Cayley graphs of finite commutative rings

## Finding

Let \(R\) be any finite commutative ring with \(1\ne0\), and let \(G_R\) be its simple unitary Cayley graph: distinct \(a,b\in R\) are adjacent exactly when \(a-b\) is a unit. Let \(\mathcal R\) be the countable random (Rado) graph, in the pure adjacency/equality language. Write \(J(R)\) for the Jacobson radical. The following assertions constitute a sharp classification:

1. \(G_R\equiv_{\mathrm{FO}^{3}}\mathcal R\), with unrestricted quantifier depth and no counting quantifiers, **if and only if** \(J(R)=0\) and \(R\cong\prod_{i=1}^{t}\mathbb F_{q_i}\) for \(t\ge2\) with every \(q_i\ge3\). Equivalently, these and only these rings have a unitary Cayley graph with the complete two-vertex adjacency-extension property (2-existential closure).
2. **No** unitary Cayley graph of a nonzero finite commutative ring is 3-existentially closed; hence **none** is \(\mathrm{FO}^{4}\)-equivalent to \(\mathcal R\). The variable-width boundary at three is sharp.
3. Among graphs satisfying item 1, deletion of **every** single vertex destroys 2-existential closure exactly in the following cases: \(t=2\) and at least one factor has order \(3\), or \(t\ge3\) and every factor has order \(3\). All other graphs in item 1 survive deletion of any one vertex while remaining 2-existentially closed.

In particular, for every prime \(p\ge3\), \(G_{\mathbb F_p\times\mathbb F_p}\equiv_{\mathrm{FO}^{3}}\mathcal R\), while \(\chi(G_{\mathbb F_p\times\mathbb F_p})=p\). Thus the single unrestricted-depth three-variable theory contains finite graphs of unbounded chromatic number. In the cyclic specialization \(R=\mathbb Z/n\mathbb Z\), item 1 holds exactly when \(n\) is odd, squarefree, and has at least two distinct prime factors.

## Assumptions and scope

All rings are finite, commutative, unital, and nonzero. Empty products and the zero ring are excluded. The graph language has one irreflexive symmetric binary adjacency relation and equality, with no ring operations or named constants. A graph is \(k\)-existentially closed (\(k\)-e.c.) if, for every \(k\)-tuple of pairwise distinct anchor vertices and every choice of desired adjacent/nonadjacent links, a distinct witness realizes that pattern. A 2-e.c. graph is 2-e.c.-critical if deletion of any single vertex makes it fail 2-e.c. A formula in \(\mathrm{FO}^{k}\) uses at most \(k\) variable names, reused freely, with unbounded quantifier depth; it has no counting quantifiers.

Every finite commutative ring has a decomposition into local factors. Its radical quotient \(R/J(R)\) is a product of finite fields; it equals \(R\) precisely when \(R\) is reduced. The field orders \(q_i\) are prime powers, not necessarily primes.

## Proof

**1. Local reduction and necessary obstructions.** For any \(j\in J(R)\), an element \(u\) is invertible exactly when \(u+j\) is invertible. If \(0\ne j\in J(R)\), the two different vertices \(0,j\) consequently have identical open neighborhoods. They cannot realize a witness adjacent to exactly one of them; hence 2-e.c. forces \(J(R)=0\).

The structure theorem then gives \(R\cong\prod_{i=1}^t\mathbb F_{q_i}\); two vectors are adjacent precisely when their entries differ in *every* coordinate. If \(t=1\), the graph is complete, so two distinct anchors cannot have a new vertex nonadjacent to both. If some \(q_i=2\), choose anchors differing at coordinate \(i\). No vector is adjacent to both, because there is no third value at that coordinate. Thus 2-e.c. necessitates \(t\ge2\) and all \(q_i\ge3\).

**2. Exact extension counts.** Suppose henceforth \(t\ge2\) and \(q_i\ge3\). Fix distinct \(a,b\), and put \(E=\{i:a_i=b_i\}\), \(D=\{i:a_i\ne b_i\}\). Define
\[
N=\prod_{i=1}^tq_i,\qquad
U=\prod_{i=1}^t(q_i-1),\qquad
W=\prod_{i\in E}(q_i-1)\prod_{i\in D}(q_i-2),
\]
with empty products equal to one, and \(\varepsilon=1\) when \(E\) is empty and zero otherwise. The number \(c_{uv}(a,b)\) of **distinct** third vertices adjacent to \(a\) exactly when \(u=1\) and to \(b\) exactly when \(v=1\) is
\[
\begin{aligned}
c_{11}&=W,\\
c_{10}=c_{01}&=U-W-\varepsilon,\\
c_{00}&=N-2U+W-2(1-\varepsilon).
\end{aligned}
\]
Indeed, \(U\) counts neighbors of either anchor and \(W\) counts common neighbors. In the one-sided patterns an adjacent anchor itself must be removed when \(\varepsilon=1\); in the double-nonadjacent pattern both anchors must be removed when \(\varepsilon=0\). These are all the excluded witnesses; the formulas are exact.

The four quantities are positive. For \(c_{11}\), every factor in \(W\) is at least one. To realize a one-sided pattern, select a coordinate where \(a,b\) differ, copy the unwanted anchor there, and choose different values from the wanted anchor elsewhere; a possible accidental anchor can be avoided because there is a second coordinate of size at least three. For \(c_{00}\), if \(a,b\) agree somewhere, copy the shared value there and choose a third value at a coordinate where they differ. If they differ everywhere, choose distinct coordinates \(i,j\), copying \(a_i\) at \(i\) and \(b_j\) at \(j\). Such hybrids are distinct from both anchors. Therefore 2-e.c. holds, proving the equivalence in item 1 at the level of finite adjacency extensions.

**3. Criticality classification.** A 2-e.c. graph is 2-e.c.-critical if and only if at least one anchor pair/pattern has exactly one witness, provided the graph is vertex-transitive. Unitary Cayley graphs are vertex-transitive by translation: if a pattern has a unique witness \(w\), translations make each vertex the unique witness of some translated pattern. Conversely, if every pattern has at least two witnesses, every one-vertex deletion retains all patterns.

For \(t\ge2\), \(c_{11}=1\) occurs precisely when \(E=\varnothing\) and all \(q_i=3\): each equal coordinate contributes \(q_i-1\ge2\), while each differing coordinate contributes \(q_i-2\ge1\). The one-sided counts are always at least two. To see this, choose \(i\in D\), require \(w_i=b_i\) and \(w_j\ne a_j\) for all \(j\ne i\); for \(t\ge3\) this supplies at least \(2^{t-1}-1\ge3\) admissible non-anchor witnesses. For \(t=2\), direct substitution into the formulas gives \(c_{10}\ge2\): when \(E\ne\varnothing\) the value is \(q_j-1\) at the equal coordinate \(j\); when \(E=\varnothing\) it equals \(q_1+q_2-4\).

If \(E=\varnothing\), the two hybrids obtained by interchanging values of \(a,b\) in two different coordinates are distinct double-nonadjacent witnesses, so \(c_{00}\ge2\). If both \(D,E\) are nonempty and \(t\ge3\), choose \(i\in D\), \(j\in E\), fix \(w_j=a_j=b_j\), choose a value other than \(a_i,b_i\) at \(i\), and choose all remaining coordinates freely. This gives at least \(\prod_{\ell\notin\{i,j\}}q_\ell\ge3\) witnesses. Finally, when \(t=2\), \(E=\{j\}\), \(D=\{i\}\), the displayed count simplifies exactly to \(c_{00}=q_i-2\). Hence \(c_{00}=1\) occurs exactly for a two-factor product with a factor of order three. Combining these alternatives proves item 3, including the deletion-resilient cases.

**4. Why three extensions fail.** Take any product of at least two fields as in item 1. Choose distinct coordinate values \(a_i\ne b_i\) in every factor. Let \(c\) be a hybrid, choosing the \(a\)-value in one coordinate and the \(b\)-value in another, and one of those two values elsewhere. Then \(a,b,c\) are pairwise distinct. Any vertex adjacent to both \(a\) and \(b\) differs from each \(c_i\) at every coordinate, so is necessarily adjacent to \(c\). The desired pattern \((1,1,0)\) on \((a,b,c)\) is impossible. Graphs failing 2-e.c. cannot be 3-e.c. either (the smaller-than-four-vertex cases also fail directly). This establishes item 2's combinatorial assertion.

**5. Logical equivalence and sharpness.** The countable random graph realizes every two-anchor adjacency pattern. Between any two graphs with the 2-e.c. property, Duplicator maintains a partial isomorphism on at most three pebbled vertices: when one pebble moves, at most two other pebbles remain, and the requisite extension is provided by 2-e.c.; equality moves are matched directly. The strategy works for arbitrarily many rounds. Therefore all graphs in item 1 share the unrestricted \(\mathrm{FO}^{3}\)-theory of \(\mathcal R\).

Conversely, the conjunction of the four two-anchor extension axioms is a sentence in \(\mathrm{FO}^{3}\). Any graph failing 2-e.c. is therefore not \(\mathrm{FO}^{3}\)-equivalent to \(\mathcal R\). The three-anchor extension axiom for the pattern \((1,1,0)\), with three universally quantified anchors and one existentially quantified witness, is an \(\mathrm{FO}^{4}\) sentence true in \(\mathcal R\) and false in every graph from item 1 by step 4. The other graphs already fail at width three. This proves the sharp full-depth three-versus-four-variable boundary.

Finally, for \(R=\mathbb F_p\times\mathbb F_p\), coordinate projections give a proper \(p\)-coloring. The diagonal vertices \((a,a)\), with \(a\in\mathbb F_p\), form a \(p\)-clique, so \(\chi(G_R)=p\). Unbounded chromatic number follows as \(p\) ranges over odd primes.

## Verification

The package contains two separately implemented finite enumeration programs and their exact recorded outputs. `check_direct.py` builds adjacency bitsets from modular gcd tests for every \(2\le n\le150\), compares the 2-e.c. classification against arithmetic factorization, and separately checks fourteen coordinate-product graphs and their one-deletion-critical status. `check_patterns.py` enumerates all ordered anchor pairs and witnesses for eight coordinate-product graphs, verifies each exact displayed formula, and checks explicit forbidden three-anchor hybrids.

The direct program tested 149 moduli and 14 field-coordinate profiles, finding no disagreements. The separately implemented multiplicity program verified the full pair counts and eight hybrid obstructions. The programs are finite corroboration, not a substitute for steps 1–5 above. They require only Python's standard library; invoke `python check_direct.py` and `python check_patterns.py` from the directory containing the files. Compare printed JSON bytewise with `direct.out` and `patterns.out`, respectively.

## Relationship to prior work

Klotz and Sander (2007) developed unitary Cayley graphs of cyclic rings and calculated chromatic number and common-neighbor counts. Kiani and Molla Haji Aghaei (2012) established the finite-ring product framework and chromatic results. Liu and Zhou (2012) treated spectral properties for commutative rings. These furnish the algebraic graph background, not the two/three-extension phase diagram or three/four-variable boundary proved here. A 2025 paper on critical Cayley graphs provides a general difference-set criterion for the 2-e.c. condition and a sufficient criticality test; the evaluated classification by radical and field factors, exact two-anchor witness counts, nonexistence of 3-e.c. members, and logical equivalence statements are not its stated results. These prior ingredients are acknowledged rather than claimed anew. General pebble-game characterizations of finite-variable logic are standard; the class-specific extension proof is the substantive contribution.

## Limitations

The result treats finite commutative rings, not noncommutative matrix rings or generalized unitary connection sets. The conclusion is equality with the random-graph theory only for three reusable variables, not complete first-order equivalence. The independent finite computations test only displayed sample sizes; the infinite quantification rests on the direct proof. Historical-priority searches did not identify a statement covering all four parts, but literature under different graph-product or model-theoretic terminology might; that uncertainty remains. No independent mathematical audit has been performed.

## References

1. W. Klotz and T. Sander, *Some Properties of Unitary Cayley Graphs*, Electronic Journal of Combinatorics 14 (2007), R45, https://doi.org/10.37236/963 (published 2007-06-21).
2. D. Kiani and M. Molla Haji Aghaei, *On the Unitary Cayley Graph of a Ring*, Electronic Journal of Combinatorics 19 (2012), P10, https://doi.org/10.37236/2214.
3. X. Liu and S. Zhou, *Spectral Properties of Unitary Cayley Graphs of Finite Commutative Rings*, Electronic Journal of Combinatorics 19 (2012), P13, https://doi.org/10.37236/2390.
4. *Existentially Closed Critical Cayley Graphs*, Ars Combinatoria 164 (2025), 19–32, https://doi.org/10.61091/ars164-02.
5. M. Grohe and M. Otto, *Pebble Games and Linear Equations*, Computer Science Logic 2012, https://doi.org/10.4230/LIPIcs.CSL.2012.289.
