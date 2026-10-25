# A sharp arity threshold in finite-space neighborhood nerves

## Finding
For integers \(n\ge 3\), \(2\le k\le n-1\), and \(r\ge2\), let \(X_{n,k}\) be the finite \(T_0\) Alexandrov space whose specialization poset has minimal points \(a_1,\ldots,a_n\) and maximal points \(b_T\), one for every \(k\)-subset \(T\subseteq[n]\), with \(a_i<b_T\) exactly when \(i\in T\). Put \(U_x=\{y:x\le y\}\), the minimal open neighborhood of \(x\). Define the \(r\)-wise neighborhood nerve \(N_r(X_{n,k})\) to have vertex set \(X_{n,k}\); a finite set \(F\) is a face if every nonempty \(Q\subseteq F\) of size at most \(r\) satisfies \(\bigcap_{x\in Q}U_x\ne\varnothing\).

There is an exact, sharp phase transition:
\[
N_r(X_{n,k})\simeq\begin{cases}
\mathrm{pt},&2\le r\le k,\\
\displaystyle\bigvee^{\binom{n-1}{k}}S^{k-1},&r\ge k+1.
\end{cases}
\]
For \(r\ge k+1\), the natural \(S_n\)-action on the only nonzero reduced integral homology is, as an **integral** module,
\[
\widetilde H_{k-1}(N_r(X_{n,k});\mathbb Z)\cong\bigwedge^k U_n,
\qquad U_n=\ker\bigl(\mathbb Z^n\xrightarrow{\sum}\mathbb Z\bigr).
\]
If \(g\in S_n\) has cycle lengths \(\ell_1,\ldots,\ell_s\), its full character is
\[
\operatorname{tr}(g\mid\widetilde H_{k-1})=[z^k]\frac{\prod_{j=1}^s(1-(-z)^{\ell_j})}{1+z}.
\]
Moreover \(N_r(X_{n,k})\) is pure of dimension \(k\) but is not Cohen–Macaulay over any field when \(r\ge k+1\). In particular, the clique complex of the pairwise inseparability graph (\(r=2\)) is contractible, while the full common-neighborhood nerve (\(r\ge k+1\)) can have unbounded-dimensional and unbounded-rank homology. The least arity revealing that homology is exactly \(k+1\).

## Assumptions and scope
All sets, groups, and complexes are finite. The Alexandrov convention uses upward-closed opens; reversing the specialization order without also reversing neighborhoods changes the construction. The inclusion \(a_i<b_T\) holds only when \(i\in T\). A clique of the inseparability graph is a set all of whose pairs of minimal open neighborhoods meet, so its clique complex is exactly \(N_2\). The topological equivalence is ordinary nonequivariant equivalence; the displayed homology isomorphism is separately integral and \(S_n\)-equivariant. The claim covers every \(n,k,r\) in the stated ranges, not general finite spaces.

## Proof
**Step 1: determine every possible face.** One has \(U_{a_i}=\{a_i\}\cup\{b_T:i\in T\}\) and \(U_{b_T}=\{b_T\}\). Two distinct maximal points have disjoint minimal opens. A face can therefore contain at most one maximal point; if it contains \(b_T\), all its other vertices must be \(a_i\) for \(i\in T\), and this condition is sufficient for every arity. For a set \(A\) of minimal points alone, any \(j\) distinct neighborhoods meet exactly when \(j\le k\), except that singleton intersections are always nonempty. Indeed, a common upper bound is a maximal \(b_T\) containing all their indices. Consequently all such \(A\) are allowed if \(r\le k\), while \(|A|\le k\) is necessary and sufficient if \(r\ge k+1\).

**Step 2: an equivariant deformation retraction.** Let \(L\) be the full simplex on \(a_1,\dots,a_n\) for \(r\le k\), and its \((k-1)\)-skeleton otherwise. In either case, the entire nerve is \(L\cup\bigcup_{|T|=k}(b_T*\Delta_T)\), where \(\Delta_T\) is the full simplex on \(\{a_i:i\in T\}\). Each cone meets \(L\) in \(\Delta_T\), and distinct cones intersect only in \(L\). Send each \(b_T\) linearly to the barycenter of \(\Delta_T\), and fix every \(a_i\). On each cone the straight-line homotopy to this map lies in that cone, is consistent across overlaps, and fixes \(L\). Thus \(|N_r|\) strongly deformation-retracts onto \(|L|\). The construction commutes with every permutation of the index set.

**Step 3: nonequivariant homotopy type.** When \(r\le k\), \(L\) is a simplex. For \(r\ge k+1\), it is the \((k-1)\)-skeleton of the \((n-1)\)-simplex. On this skeleton, match each nonempty face avoiding \(a_n\) and having at most \(k-1\) vertices with its enlargement by \(a_n\). This matching is acyclic: in a gradient path, deleting a vertex other than \(a_n\) strictly decreases the remaining set outside \(a_n\). Exactly one vertex and the \(\binom{n-1}{k}\) faces of size \(k\) avoiding \(a_n\) remain critical. Since \(k\ge2\), these are a single critical zero-cell and \(\binom{n-1}{k}\) critical cells in degree \(k-1\), hence the claimed wedge of spheres.

**Step 4: integral equivariance and character.** Let \(E=\mathbb Z^n\) with its standard permutation basis. Oriented \((k-1)\)-simplices of \(L\) form \(\bigwedge^kE\). The augmented simplicial boundary is contraction by \(\varepsilon:E\to\mathbb Z\), sending all basis vectors to \(1\). Since \(L\) has no \(k\)-simplices, its top reduced homology is \(\ker(\iota_\varepsilon:\bigwedge^kE\to\bigwedge^{k-1}E)\). Splitting \(E=\mathbb Z e_n\oplus U_n\) shows, integrally and naturally as a submodule, that this kernel equals \(\bigwedge^kU_n\). The homotopy of Step 2 is \(S_n\)-equivariant, giving the claimed module for \(N_r\). On a permutation cycle of length \(\ell\), \(\det(I+zg)=1-(-z)^\ell\); dividing by the trivial one-dimensional eigenvalue \(1+z\) gives \(\det(I+zg\mid U_n)\). Its coefficient of \(z^k\) is precisely the character of \(\bigwedge^kU_n\).

**Step 5: pure non-Cohen–Macaulayness and sharp arity.** For \(r\ge k+1\), all maximal faces of \(N_r\) are exactly \(\{b_T\}\cup\{a_i:i\in T\}\), each of dimension \(k\). But the global \((k-1)\)-dimensional reduced homology has rank \(\binom{n-1}{k}>0\), contradicting the global lower-homology vanishing required for Cohen–Macaulayness of a pure \(k\)-complex, over any field. The explicit face criterion proves that all arities \(2,\dots,k\) coincide and that all arities from \(k+1\) onward coincide, making the transition sharp.

## Verification
The supplementary `VERIFY.py` independently enumerates the actual face complexes, computes reduced mod-two boundary ranks, and tests signed equivariant reduced Lefschetz traces against the cycle-type character formula. Its included recorded output reports \(60\) parameter/arity cases, \(15{,}318\) nonempty faces across those cases, \(12\) comparisons against literal intersections of minimal open neighborhoods, and \(612\) signed character checks. All passed. These finite tests check small instances; the infinite integral and equivariant conclusions rest on Steps 1–5.

## Relationship to prior work
Cameron and Kumar (first public arXiv submission October 10, 2026) introduced graphs associated to topological spaces and studied inseparability and higher family-complex constructions using Dowker duality. This theorem studies a specific but parameter-unbounded, naturally symmetric rank-selected Boolean family and **additionally** resolves an explicit all-arity neighborhood-intersection filtration, its sharp topological jump, and its integral permutation representation. The classical homotopy of a simplex skeleton and its augmentation-lattice module are ingredients rather than claimed inventions. The author's October 15 account confirms the motivating pairwise-inseparability viewpoint. Full-text access to the primary preprint was not available here, so a residual risk of uninspected coverage is explicitly acknowledged rather than treating an abstract search as proof of absence.

## Limitations
This does not classify the full family-complex invariants of arbitrary finite spaces. The construction depends on the chosen Alexandrov topology and on passing from pairwise to higher-arity intersection conditions. The initial 2026 source was available as bibliographic metadata/abstract and an author account, but its primary full text was inaccessible; exact independent bibliographic priority remains subject to that limitation. No independent scientific validation has been performed.

## References
1. P. J. Cameron and P. B. Vinod Kumar, *Graphs on Topological Spaces*, arXiv:2610.14783, initial public submission 2026-10-10, https://arxiv.org/abs/2610.14783.
2. P. J. Cameron, *Graphs on topological spaces*, author commentary, 2026-10-15, https://cameroncounts.wordpress.com/2026/10/15/graphs-on-topological-spaces/.
3. Classical augmented simplex chain complex, acyclic matching for skeletons, and integral exterior-power representations; detailed proofs are included above.
