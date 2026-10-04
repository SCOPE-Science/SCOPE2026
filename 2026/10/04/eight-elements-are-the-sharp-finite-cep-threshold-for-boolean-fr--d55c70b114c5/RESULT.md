# Eight elements are the sharp finite CEP threshold for Boolean frames
## Finding

A **Boolean frame** is a Boolean algebra equipped with an arbitrary unary operation. Following the congruential-modal-logic literature, such a frame has the **congruence extension property** (CEP) when every congruence of every subalgebra is the restriction of a congruence of the whole frame.

There is a sharp finite threshold.

Every Boolean frame whose Boolean reduct has at most four elements has CEP. The first possible failure occurs on the unique eight-element Boolean algebra
\[
\mathcal P(\{1,2,3\}).
\]
Thus eight is the least finite carrier size of a Boolean frame without CEP.

The entire eight-element layer can be counted exactly. On the fixed labelled Boolean algebra \(\mathcal P(\{1,2,3\})\), there are
\[
8^8=16{,}777{,}216
\]
unary operations. Exactly
\[
1{,}216{,}800
\]
of the resulting Boolean frames fail CEP, while
\[
15{,}560{,}416
\]
have CEP.

Up to Boolean-frame isomorphism, where the three Boolean atoms may be permuted, there are
\[
2{,}804{,}480
\]
isomorphism classes of unary expansions, of which exactly
\[
205{,}724
\]
fail CEP.

The failure already occurs under the strong order-theoretic conditions highlighted in the recent modal-logic literature. Call \(f\) a **normal closure operator** here when
\[
f(0)=0,
\qquad
x\le f(x),
\qquad
x\le y\Rightarrow f(x)\le f(y),
\qquad
f(f(x))=f(x).
\]
On the eight-element Boolean algebra there are exactly
\[
45
\]
such operators. Exactly
\[
13
\]
of them fail CEP, forming exactly four isomorphism classes under the action of \(S_3\) on the Boolean atoms.

Using bitmasks \(0,\ldots,7\) for subsets of \(\{1,2,3\}\), the four failing closure-operator classes have representatives
\[
(0,1,2,3,4,7,7,7),
\]
\[
(0,1,2,7,5,5,7,7),
\]
\[
(0,1,2,7,7,7,7,7),
\]
and
\[
(0,1,2,7,4,7,7,7),
\]
where the tuple lists \((f(0),\ldots,f(7))\). Their orbit sizes are respectively
\[
3,6,3,1,
\]
which sum to the thirteen failing closure operators.

## Assumptions and scope

The signature is the Boolean-algebra signature together with one arbitrary unary operation \(f\), exactly as in the recent work on congruential modal logic. CEP is the ordinary algebraic congruence extension property of the expanded algebra.

The finite threshold is about the size of the Boolean reduct. Finite Boolean algebras have cardinalities that are powers of two, so after the two- and four-element cases the next carrier size is eight.

The term “normal closure operator” in this result means normal, extensive, monotone, and idempotent in the order-theoretic sense above. It is not being used to assert additivity. In particular, these operators need not be modal closure-algebra operators in the stronger additive sense.

The labelled count distinguishes different unary functions on one fixed labelled copy of \(\mathcal P(\{1,2,3\})\). The isomorphism count quotients by the six Boolean automorphisms induced by permutations of the three atoms.

## Proof

For the two-element Boolean algebra there is no proper nontrivial Boolean subalgebra, so CEP is immediate.

Now let the Boolean reduct have four elements. Its only proper Boolean subalgebra is
\[
\{0,1\}.
\]
This is a subalgebra of the expansion only when it is closed under \(f\). If it is not closed, there is no proper subalgebra to check. If it is closed, the two-element expanded algebra has only the identity and universal congruences. Those are restrictions of the identity and universal congruences of the whole algebra. Hence every four-element Boolean frame has CEP.

It remains to show that failure occurs on eight elements. Identify the Boolean algebra with \(\mathcal P(\{1,2,3\})\) and encode subsets by the bitmasks \(0,\ldots,7\). Define
\[
f=(0,1,2,3,4,7,7,7).
\]
Equivalently, \(f\) fixes \(0,1,2,3,4,7\) and sends \(5,6\) to \(7\).

This \(f\) is normal, extensive, monotone, and idempotent. Consider the four-element Boolean subalgebra
\[
C=\{0,4,3,7\}.
\]
It is closed under \(f\). On \(C\), let \(\theta\) be the Boolean congruence with classes
\[
\{0,4\},
\qquad
\{3,7\}.
\]
Because \(f\) fixes all four elements of \(C\), \(\theta\) is a congruence of the expanded subalgebra.

Congruences on \(\mathcal P(\{1,2,3\})\) are indexed by subsets \(K\subseteq\{1,2,3\}\):
\[
X\equiv_KY
\quad\Longleftrightarrow\quad
X\mathbin{\triangle}Y\subseteq K.
\]
For such a congruence to restrict to \(\theta\), it must collapse the Boolean atom \(4\) and not collapse the complementary block \(3\). This forces
\[
K=4.
\]
But \(\equiv_4\) is not compatible with \(f\): the elements \(1\) and \(5\) differ by \(4\), so
\[
1\equiv_4 5,
\]
while
\[
f(1)=1,
\qquad
f(5)=7,
\]
and \(1\mathbin{\triangle}7=6\not\subseteq4\). Thus \(\theta\) has no extension to the whole Boolean frame. CEP fails.

Therefore eight is the sharp finite threshold.

For the exact census, note that the proper Boolean subalgebras of \(\mathcal P(\{1,2,3\})\) are exactly
\[
\{0,7\},
\quad
\{0,1,6,7\},
\quad
\{0,2,5,7\},
\quad
\{0,4,3,7\}.
\]
For each of the \(8^8\) unary operations, the verifier performs the definition of CEP directly:

- it determines which of these four Boolean subalgebras are closed under \(f\);
- it enumerates every Boolean congruence on each closed subalgebra and keeps those compatible with \(f\);
- it enumerates the eight Boolean congruences of the whole algebra and keeps those compatible with \(f\);
- it tests whether each local congruence is the restriction of at least one compatible global congruence.

This is exhaustive because every congruence of a finite Boolean algebra is determined by the set of Boolean atoms in its kernel ideal.

The exact labelled result is
\[
1{,}216{,}800
\]
failures and
\[
15{,}560{,}416
\]
passes.

For the isomorphism count, the Boolean automorphism group is \(S_3\). Under conjugation of unary operations, Burnside's lemma uses the following fixed-point counts:
\[
\begin{array}{c|ccc}
\text{atom permutation type}&1&\text{transposition}&\text{3-cycle}\\
\hline
\text{all unary operations}&16{,}777{,}216&16{,}384&256\\
\text{CEP failures}&1{,}216{,}800&5{,}832&24.
\end{array}
\]
There are three transpositions and two 3-cycles, so the number of failure orbits is
\[
\frac{1{,}216{,}800+3\cdot5{,}832+2\cdot24}{6}
=205{,}724.
\]
The same calculation gives \(2{,}804{,}480\) total isomorphism classes.

Finally, direct filtering by the four closure identities leaves exactly \(45\) normal closure operators. Thirteen fail CEP. Their Burnside fixed counts are
\[
\begin{array}{c|ccc}
\text{atom permutation type}&1&\text{transposition}&\text{3-cycle}\\
\hline
\text{closure operators}&45&11&3\\
\text{CEP-failing closure operators}&13&3&1.
\end{array}
\]
Hence the numbers of closure-operator isomorphism classes and failing classes are
\[
\frac{45+3\cdot11+2\cdot3}{6}=14,
\qquad
\frac{13+3\cdot3+2\cdot1}{6}=4.
\]
The four displayed representatives have orbit sizes \(3,6,3,1\), completing the closure-operator classification.

## Verification

The bundled `verify.c` is a standalone exhaustive verifier using only integer bitmasks.

It first checks the sharp lower boundary by exhausting all \(4^4=256\) unary operations on the four-element Boolean algebra and confirming that none fails CEP.

It then exhausts all
\[
8^8=16{,}777{,}216
\]
unary operations on the eight-element Boolean algebra. Congruences are checked directly through symmetric-difference kernel ideals; no SAT solver, random sampling, or timeout inference is used.

The verifier independently counts fixed operations under all six atom permutations, applies Burnside's lemma, filters the closure operators, checks the four canonical failing closure representatives, and prints `VERIFY_OK` only after every exact count matches the theorem.

A typical optimized run completes in a few seconds on a standard compiler, but the correctness claim does not depend on a timing bound.

## Relationship to prior work

Gyenis, Molnár, and Öztürk study the relation between additivity and deduction theorems in congruential modal logic through the CEP of Boolean frames. Their 2026 paper defines CEP for Boolean frames, gives a finite eight-element Boolean frame with CEP that is strongly non-additive, proves large families of strongly non-additive varieties with CEP, and shows that the class of Boolean frames with CEP is not elementary. The paper does not state the least finite carrier on which CEP itself can fail or enumerate the eight-element layer.

Gyenis and Molnár's earlier work proves the existence of many varieties without CEP, including examples satisfying combinations of normality, monotonicity, extensiveness, and idempotence. Their constructions are aimed at varieties and logical properties, not at the minimum size of an individual finite Boolean frame or a complete census on the first possible carrier.

The new threshold result therefore complements the recent structural theory in a finite direction: the four-element Boolean algebra is too small to exhibit a local congruence-extension obstruction, while the eight-element algebra is already large enough, even for normal closure operators. The complete eight-element census quantifies how frequently that obstruction occurs and identifies all closure-operator failures up to Boolean-frame isomorphism.

Targeted searches for the smallest finite Boolean frame without CEP, eight-element CEP censuses, and closure-operator counterexamples did not locate these exact statements or counts.

## Limitations

The exact census is only for the first nontrivial carrier \(\mathcal P(\{1,2,3\})\). The number of unary operations grows as \((2^n)^{2^n}\), so direct exhaustive enumeration becomes infeasible quickly.

The four isomorphism classes classify only the CEP-failing normal closure operators on eight elements, not all CEP-failing unary operations up to a finer structural invariant.

CEP of an individual algebra is weaker than CEP of the variety it generates. The theorem classifies finite Boolean frames themselves; it does not assert that every CEP-passing eight-element frame generates a CEP variety.

## References

[1] Zalán Gyenis, Zalán Molnár, and Övge Öztürk, “More on modal logics and deduction,” *Bulletin of the Section of Logic* (2026). arXiv:2603.17724, first posted 18 March 2026.

[2] Zalán Gyenis and Zalán Molnár, “Varieties of Modal Algebras Without the Congruence Extension Property,” *Notre Dame Journal of Formal Logic* 67(2) (2026), 159–176. DOI:10.1215/00294527-2025-0030. arXiv:2402.07293.

[3] Krzysztof Aleksander Krawczyk, “Deduction Theorem in Congruential Modal Logics,” *Notre Dame Journal of Formal Logic* 64(2) (2023), 185–196. DOI:10.1215/00294527-10670082.
