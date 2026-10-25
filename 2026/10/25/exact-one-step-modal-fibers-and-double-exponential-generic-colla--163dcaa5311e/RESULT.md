# Exact one-step modal fibers and double-exponential generic collapse on Boolean compatibility frames

## Finding
Let \(n\ge 1\), \(U=[n]\), and let \(W_n=\mathcal P(U)\setminus\{\varnothing\}\). Give \(W_n\) the symmetric, reflexive compatibility relation \(SRT\) if and only if \(S\cap T\ne\varnothing\). For an arbitrary proposition \(A\subseteq W_n\), let \(\Diamond A\) and \(\Box A\) be its usual Kripke possibility and necessity sets. We calculate the exact joint image and the size of **every** fiber of the one-step map \(A\mapsto(\Diamond A,\Box A)\).

Define \(P(A)=\bigcup_{T\in A}T\) and \(Q(A)=\bigcup_{T\in W_n\setminus A}T\), both subsets of \(U\). For \(p\ge0\), define the positive integer
\[
H(p)=\sum_{j=0}^{p}(-1)^j\binom pj 2^{2^{p-j}-1},\qquad H(0)=1.
\]
For \(n\ge2\), the joint image consists of precisely \(2^{n+1}-1\) different outputs. Every support pair \((S,U)\) and \((U,S)\), with \(S\subsetneq U\), contributes one different output having exactly \(H(|S|)\) preimages. The remaining output, corresponding to \((U,U)\), has exactly
\[
C_n=2^{2^n-1}-2\sum_{p=0}^{n-1}\binom np H(p)
\]
preimages. The latter output is \((\Diamond A,\Box A)=(W_n,\varnothing)\). For \(n=1\) there are only two possible joint outputs, one for each proposition, and the central fiber is empty.

Under a uniformly random unrestricted valuation \(A\subseteq W_n\), the **exact probability** of a noncentral joint output is
\[
\varepsilon_n=\frac{2\sum_{p=0}^{n-1}\binom np H(p)}{2^{2^n-1}}
\quad\text{and}\quad
\varepsilon_n\sim2n\,2^{-2^{n-1}}\quad(n\to\infty).
\]
This describes a double-exponential generic collapse of the pair of modal outputs, despite the expressive power of specially chosen valuations.

## Assumptions and scope
The frame is the nonzero part of the finite Boolean powerset algebra, and accessibility is **nonempty intersection**. No restriction is placed on the atomic valuation: \(A\) ranges over all \(2^{2^n-1}\) subsets of \(W_n\). All worlds, propositions, and output pairs are labelled; no quotient by permutations is taken. We study **one application** of the pair \((\Diamond,\Box)\) to the *same* input proposition, not the image of arbitrary modal formulas and not unrestricted iterates. In particular, this is distinct from the restricted set-theoretic translation valuations of the motivating paper.

## Proof
**Step 1 (the support identity).** Because \(SRT\) holds exactly when \(S\cap T\ne\varnothing\), the existential clause gives
\[
\Diamond A=\{S\in W_n:S\cap P(A)\ne\varnothing\},
\]
and applying the universal clause to the complement gives
\[
\Box A=\{S\in W_n:S\cap Q(A)=\varnothing\}.
\]
These expressions recover both supports from the output pair: the singleton world \(\{i\}\) lies in \(\Diamond A\) if and only if \(i\in P(A)\), and lies in \(\Box A\) if and only if \(i\notin Q(A)\). Thus distinct support pairs yield distinct joint outputs.

**Step 2 (support dichotomy).** Both supports together cover \(U\), because each singleton world belongs to \(A\) or its complement. Suppose both \(P(A)\) and \(Q(A)\) were proper. Choose \(i\in U\setminus P(A)\) and \(j\in U\setminus Q(A)\). These atoms are distinct, since the supports cover \(U\). The nonempty world \(\{i,j\}\) must lie in \(A\) or its complement. In the first case \(i\in P(A)\), and in the second case \(j\in Q(A)\), a contradiction. Hence one support is all of \(U\).

**Step 3 (every proper support and its fiber).** Fix \(S\subsetneq U\). The condition \(P(A)=S\) says that \(A\) is a family of nonempty subsets of \(S\), whose union is exactly \(S\). Every world using an atom outside \(S\) is therefore in the complement; because \(S\ne U\), the complement contains \(U\) itself, so \(Q(A)=U\). Conversely, any such covering family yields this support pair. By inclusion-exclusion over the atoms omitted from the union, their number is exactly \(H(|S|)\). Dually, the families realizing \((P(A),Q(A))=(U,S)\) are precisely the complements of such covering families, again counted by \(H(|S|)\). This shows that every one of the \(2(2^n-1)\) proper pairs occurs, with its stated fiber size. For \(n\ge2\), \(A=\{U\}\) gives \(P(A)=Q(A)=U\) (the complement contains all singleton worlds), so the central pair also occurs. For \(n=1\), it does not.

**Step 4 (central count).** The total number of input families is \(2^{|W_n|}=2^{2^n-1}\). The proper-pair fibers are disjoint, and their combined cardinality is \(2\sum_{p=0}^{n-1}\binom np H(p)\). Subtraction gives \(C_n\); the support identities show its output is exactly \((W_n,\varnothing)\). This proves all exact statements and the n=1 boundary.

**Step 5 (asymptotic probability).** A uniformly random family of nonempty subsets of a \(p\)-set covers it with probability \(H(p)/2^{2^p-1}\). By the union bound over omitted atoms this probability lies between \(1-p\,2^{-2^{p-1}}\) and \(1\), so \(H(p)\sim 2^{2^p-1}\) as \(p\to\infty\). The \(p=n-1\) term contributes \(nH(n-1)\), whereas all terms with \(p\le n-2\) together are bounded by \(2^n2^{2^{n-2}-1}\), which is negligible in comparison to \(n2^{2^{n-1}-1}\). Thus the numerator for noncentral inputs is asymptotic to \(2n2^{2^{n-1}-1}\). Dividing by \(2^{2^n-1}\) yields \(\varepsilon_n\sim2n2^{-2^{n-1}}\), as claimed.

## Verification
The standalone `checker.py` implements the Kripke \(\Box\) and \(\Diamond\) clauses by traversing accessibility pairs, independently of the union-support formulas. It exhaustively tests **every** proposition for \(n=1,2,3,4\), checks the predicted support and exact fiber counts, and reports `ALL_CHECKS_OK`. The resulting triples (total valuations, noncentral valuations, central valuations) are respectively \((2,2,0)\), \((8,6,2)\), \((128,38,90)\), and \((32768,942,31826)\). Further arithmetical evaluations agree with the closed forms. These finite tests corroborate the proof but cannot establish its unbounded assertions.

## Relationship to prior work
Jockwich, Tarafder, and Venturi (2026), *The Internal Modal Logic of Forcing*, introduce co-consistency accessibility \(aRb\) when \(a\wedge b\ne0\), analyze finite complete atomic Boolean algebras, and develop translation-based Kripke semantics. Their paper supplies the natural relation and the motivation; the inspected sections on compatibility semantics and the finite Boolean-algebra logics do not state this joint one-step output/fiber classification or its random-input asymptotic. Those translation-based atomic valuations must not be confused with the unrestricted Kripke valuations used here. Standard inclusion-exclusion and elementary union bounds are invoked without claims of novelty.

## Limitations
The theorem concerns the full labelled powerset algebra and the single-step operator pair, not arbitrary finite Boolean-reduct subframes, modal formulas at arbitrary depth, or forcing-translated atomic valuations. The random-input asymptotic uses the uniform measure on **all** propositions; it says nothing about a distribution on Boolean-valued set-theoretic sentences. Priority is conditional on inspected literature; a similar support-enumeration identity may exist elsewhere in hypergraph or modal-algebra combinatorics.

## References
Jockwich, S., Tarafder, S., and Venturi, G. (2026), *The Internal Modal Logic of Forcing*, arXiv:2607.25977v1, first posted 2026-07-28, https://arxiv.org/abs/2607.25977.

