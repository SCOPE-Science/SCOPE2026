# Exact two-variable census of cumulative and preferential consequence relations

## Finding

In the full classical propositional language on exactly two variables, with all Boolean combinations available, there are precisely \(336{,}852\) distinct nonmonotonic consequence relations satisfying System C (Reflexivity, Left Logical Equivalence, Right Weakening, Cut and Cautious Monotonicity). Of these, precisely \(596\) also satisfy the preferential Or rule (System P). Thus precisely \(336{,}256\) are cumulative but not preferential in this axiomatic sense.

Under simultaneous permutation of the four classical truth valuations—equivalently, automorphism of their full Boolean algebra of definable truth sets—the corresponding orbit counts are respectively \(14{,}976\) and \(44\). The fixed-point counts for an individual permutation with cycle type \((1^4),(2,1^2),(2^2),(3,1),(4)\), respectively, are

\[
\begin{array}{c|rrrrr}
 & (1^4)&(2,1^2)&(2^2)&(3,1)&(4)\\
\mathrm{System\ C}&336852&3312&484&141&20\\
\mathrm{System\ P}&596&56&16&8&2
\end{array}.
\]

The result counts consequence relations, not presentations of those relations by ranked models or formulas. No consistency-preservation or nonempty-choice assumption is imposed.

## Assumptions and scope

Let \(\Omega=\{00,01,10,11\}\) be the four distinct valuations of two Boolean propositional variables. Every subset \(A\subseteq\Omega\) is definable by a formula, and formulas with equal truth sets are identified only for semantic classification. We count binary relations \(\mathrel{\sim}\) on formulas obeying System C: \(\alpha\sim\alpha\); preservation under classical equivalence of the antecedent; weakening the consequent along classical implication; Cut \((\alpha\wedge\beta)\sim\gamma,\ \alpha\sim\beta\Rightarrow\alpha\sim\gamma\); and Cautious Monotonicity \(\alpha\sim\beta,\ \alpha\sim\gamma\Rightarrow (\alpha\wedge\beta)\sim\gamma\). For System P add \(\alpha\sim\gamma,\ \beta\sim\gamma\Rightarrow(\alpha\vee\beta)\sim\gamma\). These are the precise axiom schemes employed here.

## Proof

**1. Normal form.** Every System C relation corresponds uniquely to a function \(f:\mathcal P(\Omega)\to\mathcal P(\Omega)\) satisfying
\[
 f(A)\subseteq A,\qquad
 f(A)\subseteq B\subseteq A\Longrightarrow f(B)=f(A),
\]
by \(\alpha\sim\beta\) exactly when \(f([\alpha])\subseteq[\beta]\).

To verify the nontrivial direction, for each antecedent truth set \(A\), intersect the truth sets of all its entailed consequents. There are only finitely many possible truth sets. The entailed consequents are closed under conjunction: from \(\alpha\sim\beta\) and \(\alpha\sim\gamma\), Cautious Monotonicity gives \(\alpha\wedge\beta\sim\gamma\), while Reflexivity and Right Weakening give \(\alpha\wedge\beta\sim\beta\); Cut, applied first at antecedent \(\alpha\wedge\beta\) and then at \(\alpha\), yields \(\alpha\sim\beta\wedge\gamma\). Hence the intersection itself is an entailed truth set and determines all consequents by Right Weakening. Reflexivity forces contraction. Cut and Cautious Monotonicity give equality of consequence theories when \(f(A)\subseteq B\subseteq A\), exactly the outcast equation above. Conversely, contraction plus outcast verifies all five axioms immediately; for the two nontrivial rules observe that adding an entailed premise replaces \(A\) with an intermediate \(B\), preserving its chosen set.

**2. The preferential subfamily.** The Or rule holds precisely when
\[
 f(A\cup B)\subseteq f(A)\cup f(B)\qquad(A,B\subseteq\Omega).
\]
Indeed, this inclusion is equivalent to every common superset of \(f(A)\) and \(f(B)\) also containing \(f(A\cup B)\). Under contraction, it is also equivalent to heredity
\[
 B\subseteq A\Longrightarrow f(A)\cap B\subseteq f(B).
\]
For the forward implication, decompose \(A=B\cup(A\setminus B)\), apply the displayed Or inclusion and intersect with \(B\). For the reverse implication, apply heredity separately to \(A\) and \(B\), both inside \(A\cup B\). These equivalences involve no nonemptiness requirement.

**3. Exact finite count, not sampling.** Represent a subset of the four valuations by its four-bit integer mask, and process the sixteen masks in increasing cardinality. Once all strict subsets of \(A\) have been assigned, a proposed value \(f(A)=B\subseteq A\) is legal if and only if every previously assigned \(C\) with \(B\subseteq C\subsetneq A\) has \(f(C)=B\). This condition is *exactly* every newly decidable instance of the outcast equation, so the recursion constructs each compliant map once and excludes every noncompliant map. At each completed map the checker evaluates all \(256\) ordered pairs \((A,B)\) for the Or inclusion. The standalone complete recursion `enumerate_cumulative.cpp` returns \(336852\) and \(596\).

An independently structured recursion in `independent_check.py` visits unassigned subsets in decreasing cardinality. Choosing \(f(A)=B\) forces \(f(C)=B\) simultaneously for every \(B\subseteq C\subseteq A\); conflicts reject the branch. This propagating recursion is also bijective with all outcast maps and produces the same totals and permutation fixed-point counts, without depending on the first program's search procedure.

**4. Symmetry reduction.** The group of Boolean-algebra automorphisms permutes the four valuation atoms, so it is \(S_4\). Conjugation sends \(f\) to \(f^\pi(A)=\pi(f(\pi^{-1}A))\), preserving contraction, outcast and Or. Exhaustively checking all \(24\) permutations gives the per-element fixed-point counts in the Finding. Their conjugacy-class multiplicities are \(1,6,3,8,6\). Thus Burnside's lemma gives
\[
 \frac{336852+6(3312)+3(484)+8(141)+6(20)}{24}=14976,
\]
and
\[
 \frac{596+6(56)+3(16)+8(8)+6(2)}{24}=44.
\]
These equalities finish an exhaustive mathematical count for the stated finite domain; no extrapolation to a larger variable language is asserted.

## Verification

Both standalone programs are included. On an ordinary C++17 toolchain, compile and run `enumerate_cumulative.cpp` with `g++ -O3 -std=c++17 enumerate_cumulative.cpp -o count && ./count`. Execute `python3 independent_check.py` with Python 3.8 or later. Expected exact outputs are the totals and five class fixed-point counts above. Both programs completed and agreed; the independent Python script asserts these numerical results. The logic-to-choice correspondence and correctness/completeness of both searches are proved above, so the machine output is a reproducible finite enumeration rather than an unexplained experiment.

## Relationship to prior work

Kontinen, Meier and Sauerwald (2026) establish qualitative representation results for cumulative propositional and team-based logics, including equivalence of their classical System C setting with a cumulative semantic representation. The well-known outcast/Aizerman property is not proposed as new: Lehmann (2021) represents such choice functions by total hyper-orders, and Danilov (2021) studies the conservative choice-function subclass. Those results supply a conceptual background but do not directly state the particular two-variable labelled/orbit System C-versus-System P census here. The numerical value for nonempty conservative choice maps reported in antimatroid enumeration is a different convention: the present \(596\) preferential maps permit empty output on nonempty inputs.

## Limitations

The enumeration pertains to precisely four Boolean valuation atoms (two propositional variables) and the specified System C/P axiom schemes. The symmetry quotient permits *every* Boolean-algebra automorphism, not only syntactic renaming of the two variables. No nonemptiness or consistency-preservation axiom is assumed, and counts with such a restriction differ. Although primary literature and targeted prior-art records were compared, historical priority of the exact numbers is not certified; a preexisting exhaustive choice-function table under another terminology could imply them. This result makes no claim about the general \(m\)-variable counting sequence.

## References

- J. Kontinen, A. Meier, K. Sauerwald, *Representation Theorems for Cumulative Propositional Dependence Logics*, arXiv:2602.21360 (first publicly submitted 2026-02-24), particularly System C and the classical representation discussion.
- D. Lehmann, *Representing choice functions by a total hyper-order*, arXiv:2107.02798 (2021).
- V. Danilov, *Choice functions on posets*, arXiv:2101.11965 (2021).
