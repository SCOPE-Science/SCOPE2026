# Local McKinsey correspondence and sparse incidence on symmetric frames

## Finding
Let \(M=\Box\Diamond p\to\Diamond\Box p\) be the McKinsey modal formula, and let \((W,R)\) be **any nonempty symmetric Kripke frame** (finite or infinite), with unrestricted propositional valuations. For \(w\in W\), write \(R(w)=\{u:wRu\}\). Then \(M\) is valid at \(w\) under *every* valuation if and only if there is a \(u\in R(w)\) such that \(R(u)=\{w\}\). This is a first-order *local* correspondence theorem without transitivity or weak-transitivity assumptions.

It follows that \(M\) is globally valid on a symmetric frame if and only if \(R\) is the graph of an involution: every world has exactly one successor and its successor has it as its unique successor. Every such frame is a disjoint union of single reflexive points and irreflexive two-cycles. Among symmetric relations on \(n\ge1\) labelled worlds, the number globally validating \(M\) is
\[
I_n=\sum_{j=0}^{\lfloor n/2\rfloor}\frac{n!}{2^j j!(n-2j)!}.
\]
The nonempty finite validating frames have exactly \(\lfloor n/2\rfloor+1\) isomorphism types. In the irreflexive case, global validity is possible only for even \(n\), and is then equivalent to a perfect matching, giving \(n!/(2^{n/2}(n/2)!)\) labelled frames. Moreover, the modal theory of **all** globally validating symmetric frames is the theory of the one irreflexive two-cycle: testing a modal formula with \(k\) variables reduces to propositional validity in at most \(2k\) truth-value variables.

For a **fixed labelled root** \(w\) in a loop-free undirected graph on \(n\ge2\) labelled vertices, the exact number \(L_n\) of graphs in which \(M\) is valid at \(w\) is
\[
L_n=\sum_{r=1}^{n-1}(-1)^{r+1}\binom{n-1}{r}2^{\binom{n-r}{2}}.
\]
For independent edges with probability \(0<p<1\), the exact probability is
\[
q_n(p)=\sum_{r=1}^{n-1}(-1)^{r+1}\binom{n-1}{r}p^r(1-p)^{r(n-2)-\binom r2}.
\]
For each fixed \(c>0\), in the sparse model with \(p=c/n\), the number of neighbors of \(w\) having degree one converges in distribution to \(\operatorname{Poisson}(ce^{-c})\), and therefore
\[
\lim_{n\to\infty}q_n(c/n)=1-\exp(-ce^{-c}).
\]
This limit has its unique maximum at \(c=1\), with value \(1-\exp(-e^{-1})\approx0.3077993724\). The claimed maximum concerns this **fixed-degree-scale limiting law**, not the optimizer for a fixed finite \(n\).

## Assumptions and scope
A Kripke valuation assigns an arbitrary subset of \(W\) to \(p\). The assertion "valid at \(w\)" quantifies over every such valuation; "globally valid" additionally quantifies over every world. Symmetric means \(wRu\iff uRw\), allowing loops except where the graph is explicitly called loop-free. Singleton-successor means \(R(u)\) equals the set \(\{w\}\), not merely that \(u\) has a small degree in the underlying loop-ignored graph. The finite counting statements assume fixed labels; \(n=1\) has one globally validating symmetric relation, the loop. The random-graph statements use undirected, loop-free, independently present edges, and one predetermined root. They make no independence claim about local-validity events at distinct roots.

## Proof
**Local criterion.** Assume \(u\in R(w)\) and \(R(u)=\{w\}\). Under any valuation, if \(p\) is false at \(w\) then \(u\) refutes \(\Diamond p\), so the antecedent \(\Box\Diamond p\) fails at \(w\). If \(p\) is true at \(w\) then \(u\) satisfies \(\Box p\), so the consequent \(\Diamond\Box p\) holds at \(w\). Thus \(M\) always holds at \(w\).

Conversely, suppose no such \(u\) exists. Set \(p\) true at precisely \(w\). If \(R(w)\) is empty then \(\Box\Diamond p\) is vacuously true and \(\Diamond\Box p\) false. Otherwise, symmetry gives \(w\in R(u)\) for each \(u\in R(w)\); hence every such \(u\) sees a \(p\)-world and \(\Box\Diamond p\) holds at \(w\). By the absence of any singleton successor, each such \(u\) also sees a world other than \(w\), so none satisfies \(\Box p\). Therefore \(\Diamond\Box p\) fails, proving the equivalence.

**Global classification.** If \(M\) holds at every world, select a witness \(u\in R(w)\) with \(R(u)=\{w\}\). Applying the local criterion to \(u\), the only possible witness accessible from \(u\) is \(w\), forcing \(R(w)=\{u\}\). Thus every successor set is a singleton; by symmetry, its successor mapping squares to the identity. Conversely, when all successor sets are singleton, the local criterion holds everywhere. Every finite involution is a disjoint union of fixed points and transpositions. Choosing \(2j\) points and pairing them gives \(n!/(2^j j!(n-2j)!)\), proving the count; the number \(j\) of two-cycles determines the isomorphism type. Excluding loops excludes fixed points and hence requires even \(n\).

**Modal-theory reduction.** On each component of an involution frame, both \(\Box\) and \(\Diamond\) evaluate at the unique partner (possibly oneself), and evaluating either modality twice returns to the starting world. Any failure of a formula occurs on a singleton loop or a two-cycle. A singleton-loop countervaluation pulls back to a two-cycle using the same truth values on both worlds; induction on formula construction preserves all truth values under this pullback. Hence a formula is valid over all involution frames if and only if it is valid on the two-cycle. Replace every variable \(p_i\) by independent Boolean variables \(a_i,b_i\) for the two endpoints, and interpret each modal operator by swapping the endpoint evaluation. This is a linear-size, two-endpoint recursive translation, reducing validity to a Boolean tautology check. Non-modal formulas show that deciding validity for this class remains coNP-hard, while the translation gives coNP membership; satisfiability is analogously NP-complete. These complexity assertions concern formulas on the fixed two-cycle, not arbitrary-frame checking.

**Exact finite rooted count.** In a loop-free graph, the local condition says that the chosen root has a neighbor of degree exactly one. For a prescribed set of \(r\) distinct vertices to be such neighbors, their \(r\) edges to \(w\) must be present, and all other incident edges forbidden. The remaining \(n-r\) vertices (including \(w\)) have \(\binom{n-r}{2}\) freely chosen internal edges. Inclusion-exclusion over candidate leaves proves the displayed \(L_n\). The same intersection event has probability \(p^r(1-p)^{r(n-2)-\binom r2}\): the exponent counts all forbidden edges incident to the \(r\) leaves, correcting for double counting edges between two leaves. Inclusion-exclusion proves \(q_n(p)\).

**Sparse limit.** Let \(Y_n\) count pendant neighbors of \(w\) in \(G(n,c/n)\). For every fixed integer \(r\ge1\), counting ordered candidate tuples gives the factorial moment
\[
\mathbb E[(Y_n)_r]=(n-1)_r(c/n)^r(1-c/n)^{r(n-2)-\binom r2}\longrightarrow (ce^{-c})^r.
\]
The factorial moments converge to those of a Poisson variable, whose distribution is determined by its moments. Hence \(Y_n\) converges in law to \(\operatorname{Poisson}(ce^{-c})\); because it is integer-valued, \(\mathbb P(Y_n>0)\to1-\exp(-ce^{-c})\). Differentiating \(ce^{-c}\) gives \((1-c)e^{-c}\). The map \(x\mapsto1-e^{-x}\) is strictly increasing, so the limit has its sole maximum for \(c>0\) at \(c=1\).

## Verification
The accompanying standalone `checker.py` reconstructs symmetric adjacency relations directly, enumerates **all** valuations at **all** worlds for every labelled symmetric frame on 1 through 5 vertices (loops permitted), and compares local semantic validity, the singleton-successor criterion, global involution recognition and the exact involution counts. It separately enumerates all loop-free graphs through 6 labelled vertices and checks rooted validity against direct modal valuations, the exact rooted counts, the perfect-matching census and a rational-edge-probability inclusion-exclusion identity. Numerical checks at \(n=500\) and five positive constants compare the sparse formula to its limiting value. The recorded result is `ALL_CHECKS_OK 269746`. This finite test corroborates but does not replace the proofs for unrestricted sizes and infinite symmetric frames.

## Relationship to prior work
Van Benthem, ten Cate and Yang (2026) prove that deciding validity of the McKinsey formula over unrestricted finite Kripke frames is coNP-complete (their Theorem 26), and that its finite-frame property is not first-order definable. The present statement imposes symmetry, obtaining a first-order *pointwise* criterion and a sharply smaller globally validating class, then derives an exact labelled census and sparse random-graph incidence.

Chen and Ma (2024, journal issue 2025), Theorems 3.16 and 3.18, derive local first-order correspondence and equivalence to Lemmon's first-order condition in **weakly transitive** frames. Their article also records Lemmon's sufficient singleton-successor-type condition more broadly. The present local equivalence applies to **arbitrary symmetric** frames, including non-weakly-transitive examples (for instance, the second vertex of a 4-vertex path has a leaf neighbor while its two-step graph need not be weakly transitive). The global involution characterization is compatible with their weak-transitive theorem but is not claimed as a new general result for all frame classes.

The numbers \(I_n\) are classical involution/matching numbers, and the Poisson approximation uses standard factorial-moment techniques. They are not presented as novel standalone sequences or a new probabilistic method. The proposed contribution is the exact identification of **which modal validity event** those quantities measure, the symmetry-only local correspondence, and the sharp sparse density location of this event. No priority claim is made for unrelated statements about support vertices in general graph theory.

## Limitations
Symmetry and unrestricted Kripke valuations are essential: without symmetry the rooted criterion is false, and restricted valuations need not detect the singleton-neighbor obstruction. The sparse limit concerns one fixed root and does not imply independence across roots. The formula complexity observation is about testing arbitrary modal formulas on the fixed two-cycle; it is not a new hardness result for arbitrary graphs. Full historical priority over possible older support-vertex probability or relative-correspondence literature cannot be guaranteed. In particular, Chen and Ma's weak-transitivity results are related and could support alternative deductions of portions of the global theorem, while the rooted theorem specifically includes non-weakly-transitive frames. No independent audit has been performed.

## References
1. Johan van Benthem, Balder ten Cate, Xi Yang, *When do modal definability and preservation theorems transfer to the finite?*, arXiv:2603.12171, first posted 12 March 2026, especially Section 5.4, Theorem 26. https://arxiv.org/html/2603.12171
2. Qian Chen and Minghui Ma, *The McKinsey Axiom on Weakly Transitive Frames*, *Studia Logica* 113 (2025), 1543–1566, first published online 29 July 2024, DOI:10.1007/s11225-024-10145-x, especially Sections 2–3 and Theorems 3.16, 3.18. Repository copy: https://pure.uva.nl/ws/files/310087691/s11225-024-10145-x.pdf
3. Robert Goldblatt, *The McKinsey axiom is not canonical*, *Journal of Symbolic Logic* 56 (1991), 554–562, DOI:10.2307/2274699 (historical background).
