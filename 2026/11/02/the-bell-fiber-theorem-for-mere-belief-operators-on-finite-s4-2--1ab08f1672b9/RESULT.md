# The Bell-fiber theorem for mere-belief operators on finite S4.2 frames

## Finding

For each integer \(n\geq 1\), let \(W\) be a fixed labelled set with \(|W|=n\). Write \(\mathcal R_n\) for the reflexive, transitive, upward-directed relations on \(W\): for every \(wRu\) and \(wRv\), some \(z\) satisfies \(uRz\) and \(vRz\). For \(R\in\mathcal R_n\) and \(X\subseteq W\), define the *mere-belief operator*
\[
H_R(X)=\{w\in W:(\exists v\in R(w),\ R(v)\subseteq X)
                         \ \land\ R(w)\nsubseteq X\}.
\]
This is the Boolean-set interpretation of \(\Diamond\Box p\land\neg\Box p\), or \(Bp\land\neg Kp\) with \(B=\Diamond\Box\).

**Exact reconstruction and fibers.** The entire operator \(H_R:2^W\to2^W\) recovers the successor set of every nonterminal world and the terminal class reached from it. Set
\[
S_H=\{w:\exists X\subseteq W,\ w\in H_R(X)\},
\]
and, for \(w\in S_H\),
\[
T_H(w)=\bigcap_{\{X:w\in H_R(X)\}}X,\qquad
L_H(w)=\{u:w\in H_R(W\setminus\{u\})\}.
\]
Then \(R(w)=T_H(w)\cup L_H(w)\), and the two sets are disjoint. All worlds outside \(S_H\) are terminal. The union \(V_H=\bigcup_{w\in S_H}T_H(w)\) consists of the terminal classes visible from nonterminal worlds. Put \(U_H=W\setminus(S_H\cup V_H)\). The set \(U_H\) is determined by \(H_R\), and
\[
\boxed{|\{R'\in\mathcal R_n:H_{R'}=H_R\}|=\operatorname{Bell}(|U_H|).}
\]
More precisely, the entire fiber consists of arbitrary equivalence relations on \(U_H\), with the relation fixed everywhere else. In particular, \(H_R\) uniquely identifies \(R\) exactly when \(|U_H|\leq 1\).

**Exact quotient census.** Let \(P_j\) count labelled preorders on a set of size \(j\), with \(P_0=1\), and put \(P(x)=\sum_{j\geq0}P_jx^j/j!\). Let \(Q_n\) count distinct set-functions \(H_R:2^W\to2^W\) as \(R\) ranges over \(\mathcal R_n\). With \(Q_0=1\) as a formal empty-set convention,
\[
\boxed{\sum_{n\geq0}Q_n\frac{x^n}{n!}
=\exp\!\left(x+(e^x-1)(P(x)-1)\right).}
\]
The initial values are \(Q_1,\ldots,Q_7=1,3,22,229,3361,71444,2233351\). These are *operator* counts on a fixed labelled carrier, not counts of modal-equivalence classes of pointed models with a fixed valuation.

## Assumptions and scope

A preorder here is a reflexive and transitive binary relation; antisymmetry is not assumed. An \(\mathsf{S4.2}\) relation is a preorder satisfying the above directedness axiom. All frames are finite and labelled, with no restriction on the valuation of propositional letters. The operator is compared as a set-function on **all** subsets \(X\subseteq W\); equality of operators is stronger than satisfaction of a bounded list of modal formulas. The definitions of \(\operatorname{Bell}(0)=\operatorname{Bell}(1)=1\) are standard.

For \(w\in W\), the \(R\)-cone is \(R(w)=\{v:wRv\}\). Its terminal equivalence class \(T_R(w)\) is the unique maximal strongly connected component of the preorder induced on \(R(w)\). A world is terminal when \(R(w)=T_R(w)\). The relation induced on a terminal class is complete in both directions. A terminal class may be reachable from nonterminal worlds (visible) or may form a component with no incoming edge from any nonterminal world (invisible).

## Proof

**1. Unique terminal class in every cone.** Quotient a finite preorder by mutual reachability. Its quotient is a finite poset. Directedness means that for any two classes above \([w]\) there is a common upper class. Every finite directed poset has exactly one greatest element: maximal elements exist, and directedness forces any two maximal elements to coincide; every element lies below a maximal element. Its inverse image is a nonempty terminal class \(T_R(w)\), and every member of \(R(w)\) reaches every member of \(T_R(w)\). Each \(v\in R(w)\) consequently has \(T_R(v)=T_R(w)\).

**2. Collapse of the inner positive modality.** For every \(X\subseteq W\),
\[
\exists v\in R(w)\ [R(v)\subseteq X]
\quad\Longleftrightarrow\quad T_R(w)\subseteq X.
\]
For the forward implication, \(v\) reaches all of \(T_R(w)\), so \(T_R(w)\subseteq R(v)\subseteq X\). Conversely take any \(v\in T_R(w)\); then \(R(v)=T_R(w)\subseteq X\). Thus
\[
\boxed{w\in H_R(X)\ \Longleftrightarrow\
T_R(w)\subseteq X\ \text{and}\ R(w)\setminus X\neq\varnothing.}\tag{1}
\]
If \(R(w)=T_R(w)\), the two conditions cannot hold simultaneously. If the inclusion is strict, the choice \(X=T_R(w)\) makes them both true. Therefore the recoverable set \(S_H\) is exactly the set of nonterminal worlds.

**3. Reconstruction.** For \(w\in S_H\), every \(H_R\)-positive set contains \(T_R(w)\), while \(X=T_R(w)\) itself is positive. Their intersection is exactly \(T_R(w)=T_H(w)\). For a singleton deletion \(X=W\setminus\{u\}\), equation (1) says
\[
w\in H_R(W\setminus\{u\})
\quad\Longleftrightarrow\quad
u\in R(w)\setminus T_R(w).
\]
Hence \(L_H(w)=R(w)\setminus T_R(w)\) and the claimed disjoint union follows. This also reconstructs the actual visible terminal classes: \(V_H=\bigcup_{w\in S_H}T_H(w)\).

**4. Exact fibers.** Each \(w\notin S_H\) has a terminal row, so its successors are exactly its terminal equivalence class. Every class meeting \(V_H\) is already fixed by \(T_H(w)\) for some nonterminal \(w\), including all edges within that class. No nonterminal row reaches \(U_H\), by its definition and step 3; no terminal row can lead outside its class. Therefore the only unobserved information is the equivalence partition of \(U_H\). Conversely, replacing that partition arbitrarily leaves every nonterminal row and all its terminal targets unchanged. All terminal rows still yield the identically false operator, and the new relation remains reflexive, transitive, and directed. Each set partition of \(U_H\) gives one relation, proving the Bell fiber size. This also proves the criterion for injectivity at a given relation.

**5. Counting the quotient.** Regard the preorder as a disjoint union of weakly connected components of its underlying undirected comparability graph. Each component of a finite directed preorder has exactly one terminal equivalence class. Indeed, the upward cone of a world is directed, and if two such cones overlap, their terminal classes coincide; the same equality propagates along any comparability path. For a component with \(m\geq2\) worlds that contains a nonterminal world, choose its proper nonempty terminal class \(T\) of size \(t\) and put \(D=C\setminus T\), of size \(m-t\). Every \(d\in D\) reaches every \(t\in T\); there are no edges from \(T\) to \(D\); and the restriction to \(D\) is an arbitrary preorder. Conversely, every such choice yields a single directed component with terminal class \(T\). Hence the number of visible connected components on a fixed \(m\)-element set is
\[
v_m=\sum_{t=1}^{m-1}\binom mt P_{m-t}\quad(m\ge2);
\qquad v_0=v_1=0.
\]
All terminal-only components together contribute precisely one **unordered set of invisible vertices**, rather than a partition: every partition of that set belongs to the same operator fiber. Every operator has a unique decomposition into its distinguishable visible connected components and that set of invisible vertices. The labelled exponential formula gives
\[
\sum_{n\ge0}Q_n x^n/n!
=\exp(x)\exp\!\left(\sum_{m\ge2}v_m x^m/m!\right).
\]
The second exponent is
\[
\sum_{m\ge2}\sum_{t=1}^{m-1}\binom mtP_{m-t}\frac{x^m}{m!}
=(e^x-1)(P(x)-1),
\]
which proves the displayed EGF. It is also computable by the recurrence
\[
Q_0=1,\quad
Q_n=\sum_{k=1}^n\binom{n-1}{k-1}c_kQ_{n-k},
\qquad c_1=1,\quad c_k=v_k\ (k\ge2).
\]
This completes the proof.

## Verification

The standalone standard-library `checker.py` enumerates **every** binary relation on labelled carriers of sizes \(1\) through \(4\), filters by reflexivity, transitivity, and directedness, and computes \(H_R\) directly from the original quantified modal clause for **every** truth subset. It independently recovers successor rows from its truth table and groups all frames by their entire operator. The pairs (admissible frames, different operators) are \((1,1),(4,3),(26,22),(255,229)\). For **every** group the measured fiber cardinality equals the Bell number of its reconstructed invisible set. The program independently expands the counting recurrence through \(n=7\), using the known preorder numbers \(P_0,\ldots,P_7\) recorded in OEIS A000798. Its completion marker is `ALL_CHECKS_OK`. These finite tests are checks, not substitutes for the proof for all finite \(n\).

To reproduce from the package, save the embedded `checker.py` bytes and run `python3 checker.py`; no third-party packages or inputs are needed.

## Relationship to prior work

Ding and Yang, *A General Theory of Propositional Modal Bundled Modalities* (arXiv:2603.26268, publicly posted 27 March 2026), introduce a general theory of bundled modalities and study precisely \(\Diamond\Box p\land\neg\Box p\) over \(\mathsf{S4.2}\) frames in Section 5.2. Their neighborhood-bisimulation and completeness results are foundational here, but neither their reconstruction of an intended relation from neighborhood data in Lemma 5.9 nor their characterization of bundled expressivity implies an exact labeled Bell-fiber theorem or its quotient enumeration.

General results about ordered finite topological spaces identify preorders with finite topologies and give the independently established counts \(P_n\), used only as **inputs** to the new quotient formula. Earlier neighborhood logics of false belief study \(\Box p\land\neg p\), a different operator. An existing enumeration of finite-chain S4-like flat frames by a Bell-number difference has different order hypotheses, operators, and counted objects, so the shared Bell terminology does not imply this result.

## Limitations

The theorem is a claim about equality of the *entire complex set-function* \(H_R\) on a fixed labelled finite carrier, not about pointed-modal equivalence of arbitrary models under an individual valuation. It does not extend without additional hypotheses to infinite frames: an upward-directed infinite cone need not have a terminal strongly connected component. It does not claim a classification for arbitrary non-directed preorders or for additional primitive modal operators. Exhaustive computation stops at four worlds; the unbounded conclusion is established symbolically. Historical priority remains conditional on comparison with possibly unindexed older descriptions under algebraic, neighborhood, or finite-topology terminology; a related survey was only available in summary form.

## References

1. Yifeng Ding and Yuanzhe Yang, *A General Theory of Propositional Modal Bundled Modalities*, arXiv:2603.26268 (initial submission 27 March 2026), especially Sections 3 and 5.2 and Lemma 5.9. https://arxiv.org/abs/2603.26268
2. OEIS A000798, *Number of different quasi-orders (or topologies, or transitive digraphs) with n labeled elements*. https://oeis.org/A000798
3. Finite topological space, *Number of topologies on a finite set*, standard preorder/finite-topology correspondence. https://en.wikipedia.org/wiki/Finite_topological_space
4. David R. Gilbert and Giorgio Venturi, *Neighborhood Semantics for Logics of Unknown Truths and False Beliefs*, 2017, https://ojs.victoria.ac.nz/ajl/article/download/4033/3585/15810
