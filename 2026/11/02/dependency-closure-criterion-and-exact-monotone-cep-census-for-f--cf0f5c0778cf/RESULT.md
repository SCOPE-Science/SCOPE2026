# Dependency-closure criterion and exact monotone CEP census for finite Boolean frames

## Finding

For a finite set \(V\), let \(f:\mathcal P(V)\to\mathcal P(V)\) be an arbitrary unary operation. Its **essential-dependency digraph** has an arrow \(i\to j\) exactly when some inputs differing only in membership of \(i\) have outputs differing in membership of \(j\). For every set partition \(\pi\) of \(V\) whose block-union Boolean subalgebra is invariant under \(f\), write \(D_\pi\) for the essential-dependency digraph of the induced function on the blocks. Write \(\operatorname{Reach}_D(S)\) for the least vertex set containing \(S\) and closed under outgoing edges of \(D\).

**Dependency-closure criterion.** The Boolean frame \((\mathcal P(V),f)\) has the congruence extension property (CEP) if and only if, for every such invariant partition \(\pi\) and every union \(J\) of blocks of \(\pi\) that is closed under outgoing edges of \(D_\pi\), the set \(\operatorname{Reach}_{D_f}(J)\) contains no entire block of \(\pi\) outside \(J\).

**Exact first-carrier monotone census.** On the eight-element Boolean algebra \(\mathcal P(\{1,2,3\})\), precisely \(8{,}000\) unary operators are isotone. Of these, exactly \(5{,}249\) have CEP and \(2{,}751\) fail CEP. Exactly \(4{,}520\) CEP-passing monotone operations are non-additive (do not preserve binary joins). Among the \(6{,}859\) normal monotone maps, \(4{,}273\) have CEP and \(2{,}586\) fail. Up to conjugation by Boolean atom permutations there are \(1{,}440\) monotone expansions, exactly \(492\) of which fail CEP.

The first statement applies to all finite Boolean frames, whether monotone or not. The numerical statements classify individual eight-element Boolean frames, *not* the congruence extension property of varieties they generate.

## Assumptions and scope

A Boolean frame is the Boolean algebra \((\mathcal P(V),\cap,{}^c,\varnothing)\) with one unary operation \(f\), which need not preserve any Boolean operation. A congruence of a subalgebra means a congruence for this expanded signature. CEP requires that every congruence of every subalgebra extend to a congruence of the full expansion.

For \(i,j\in V\), the essential-dependency arrow \(i\to j\) is present if and only if there exists \(X\subseteq V\setminus\{i\}\) with
\[
 j\in f(X)\mathbin{\triangle}f(X\cup\{i\}).
\]
Loops are allowed. A partition \(\pi=\{B_1,\ldots,B_k\}\) yields the subalgebra of all unions of its blocks. Invariance means every union of blocks is mapped to another union of blocks. If invariant, the induced operation \(f_\pi:\mathcal P(\pi)\to\mathcal P(\pi)\) is defined without choice: an input subset of blocks represents its union, and the output subset of blocks represents the image under \(f\). For \(J\subseteq\pi\), we write the same symbol \(J\) for its union of vertices in \(V\) when taking \(D_f\)-reachability.

An operation is *isotone* when \(X\subseteq Y\) implies \(f(X)\subseteq f(Y)\); *normal* means \(f(\varnothing)=\varnothing\). Binary-join additivity here means \(f(X\cup Y)=f(X)\cup f(Y)\); it is distinct from normality. A labelled operation fixes the three named atoms. An isomorphism class permits the six permutations of those atoms.

## Proof

**Lemma 1 (congruences and dependency graphs).** For any \(S\subseteq V\), let \(X\equiv_S Y\) mean \(X\triangle Y\subseteq S\). Every Boolean-algebra congruence of \(\mathcal P(V)\) is uniquely of this form. It is compatible with \(f\) exactly when \(S\) is closed under outgoing edges of \(D_f\).

Indeed, Boolean congruences correspond to ideals. Every ideal of a finite powerset Boolean algebra consists exactly of the subsets of one set \(S\), giving \(\equiv_S\). If \(S\) is forward closed and \(X\triangle Y\subseteq S\), transform \(X\) into \(Y\) by toggling the finitely many atoms of their symmetric difference, one at a time. Each toggle at \(i\in S\) alters outputs only at out-neighbors of \(i\); all such neighbors remain in \(S\). Conversely, if \(i\to j\) with \(i\in S\) and \(j\notin S\), the two inputs witnessing this arrow are \(\equiv_S\)-equivalent but their outputs are not, contradicting compatibility. Thus the least compatible global congruence whose kernel contains \(T\subseteq V\) is the one whose kernel is \(\operatorname{Reach}_{D_f}(T)\).

**Lemma 2 (restriction to a partition subalgebra).** Let \(\pi\) be an invariant partition. Every congruence of the induced Boolean frame on the set of blocks \(\pi\) is represented by a \(D_\pi\)-forward-closed subset \(J\subseteq\pi\), by Lemma 1. The restriction of a global congruence \(\equiv_S\) to this subalgebra is the local congruence whose kernel consists of exactly those blocks \(B\in\pi\) with \(B\subseteq S\).

To see the last assertion, two unions of blocks differ by a union of entire blocks. That difference lies in \(S\) precisely when every differing block lies entirely in \(S\). The kernel ideal on the partition subalgebra therefore has exactly the claimed block generators.

**Proof of the criterion.** Let \(J\subseteq\pi\) be local-congruence-closed in \(D_\pi\). A global congruence extending this local congruence must have a forward-closed kernel \(S\) containing the union of the blocks in \(J\). Hence it contains \(T=\operatorname{Reach}_{D_f}(J)\). If \(T\) already contains an outside block \(B\in\pi\setminus J\), then every candidate global kernel collapses \(B\) as well, contradicting Lemma 2; no extension exists. Conversely, if \(T\) contains no outside block completely, the global congruence \(\equiv_T\) is compatible with \(f\) by Lemma 1. Its restriction collapses precisely the blocks in \(J\), hence extends the desired local congruence by Lemma 2. This proves both directions for every invariant partition, and all Boolean subalgebras of a finite powerset Boolean algebra arise from partitions. The result includes the one- and full-block partitions, for which extension is automatic.

**Finite census.** A scalar Boolean function on three inputs is monotone if and only if its set of true arguments is an upset of the Boolean three-cube; there are \(20\) such functions. Choosing one independently for each of three output coordinates gives \(20^3=8{,}000\) isotone operators. The checker enumerates each of these with no identification of labelled operators. For each operator it computes CEP by *two* mathematically different tests: (a) direct enumeration of congruences on every invariant Boolean subalgebra, and (b) the independent essential-dependency/partition-reachability criterion. All \(8{,}000\) tests agree and produce exactly \(5{,}249\) CEP passes, \(2{,}751\) failures. Filtering by normality, binary-join additivity, and the closure axioms gives the subsidiary counts in the finding.

For isomorphism classes the automorphism group is \(S_3\). For identity, each of the three transpositions, and each of the two three-cycles, the number of invariant isotone unary maps is, respectively,
\[
8{,}000,\quad 200,\quad 20.
\]
The corresponding CEP-failure fixed-point counts are
\[
2{,}751,\quad 65,\quad 3.
\]
These are determined by direct exact conjugation checks for all six permutations. Burnside's lemma therefore gives
\[
\frac{8{,}000+3\cdot200+2\cdot20}{6}=1{,}440,
\qquad
\frac{2{,}751+3\cdot65+2\cdot3}{6}=492.
\]
An independent canonical-orbit enumeration produces the same answers. Thus the formula and every reported count are finite exact facts, not statistical estimates.

## Verification

The accompanying standalone `checker.py` uses only the Python standard library. Run `python3 checker.py`; success prints `ALL_CHECKS_OK`. It exhausts every one of the \(8{,}000\) monotone functions, compares the direct-congruence method and the graph criterion for every case, computes orbit representatives and Burnside fixed-point counts independently, and compares the two CEP methods on \(500\) additional seeded arbitrary functions to test the nonmonotone scope. It also recovers the previously reported \(45\) normal closure operators and their \(13\) CEP failures as a secondary cross-check.

Successful output includes `MONOTONE_TOTAL 8000`, `CEP_PASS 5249`, `CEP_FAIL 2751`, `NORMAL_PASS_FAIL 4273 2586`, `NONADDITIVE_CEP 4520`, `ORBIT_TOTAL_FAIL 1440 492`, and `ALL_CHECKS_OK`.

The all-carrier dependency-closure criterion is established by Lemmas 1–2 and the extension argument; finite exhaustive checks alone would not establish its universal quantifier. The eight-element counts are complete because \(20^3\) exhausts the entire isotone class.

## Relationship to prior work

Gyenis, Molnár and Öztürk [1] define CEP for Boolean frames, establish interactions with additivity and deduction, and exhibit small nonadditive CEP examples; their emphasis is varieties and logical deduction, not this monotone finite census or the dependency/reachability criterion. Gyenis and Molnár [2] construct varieties without CEP while retaining conditions such as monotonicity, without an enumeration of all isotone unary operators on the first nontrivial Boolean carrier.

The particularly close published finite census [3] proves that among all \(8^8\) unary functions on the eight-element Boolean algebra, exactly \(1{,}216{,}800\) fail CEP, and among \(45\) normal order-theoretic closure operators, \(13\) fail. Its unrestricted aggregate counts do not determine the isotone conditional counts \(2{,}751\) or \(492\) here, and its published theorem does not assert the general dependency-closure test. Our checker deliberately recovers its \(45/13\) subfamily as a consistency comparison, rather than claiming a new closure-operator census.

The dependency graph is an elementary finite representation of congruence compatibility, so equivalent formulations may have appeared in earlier finite-universal-algebra or Boolean-function literature under different names. Accordingly originality is claimed only relative to the specifically inspected primary sources and record searches, not as a proof of historical uniqueness.

## Limitations

The exact labelled and isomorphism counts address only the eight-element Boolean algebra, not higher carrier sizes. The general criterion may require enumerating all partitions and invariant subalgebras, so it is not asserted to be efficient at large order. CEP here is the property of each *individual expanded algebra*, not automatically a property of the variety generated by it. The classification of nonadditive operations is relative to binary-join preservation; it does not classify strong nonadditivity up to term equivalence. Prior-literature search does not eliminate every historical-priority risk.

## References

[1] Z. Gyenis, Z. Molnár and Ö. Öztürk, “More on modal logics and deduction,” arXiv:2603.17724v1, first posted 18 March 2026, https://arxiv.org/html/2603.17724v1.

[2] Z. Gyenis and Z. Molnár, “Varieties of modal algebras without the congruence extension property,” arXiv:2402.07293v1, first posted 11 February 2024, https://arxiv.org/html/2402.07293v1.

[3] “Eight elements are the sharp finite CEP threshold for Boolean frames,” published-finding corpus mathematical research record, https://github.com/Resultary/2026/blob/main/2026/10/4/SCOPE-eight-elements-are-the-sharp-finite-cep-threshold-for-boolean-fr--d55c70b114c5/RESULT.md.
