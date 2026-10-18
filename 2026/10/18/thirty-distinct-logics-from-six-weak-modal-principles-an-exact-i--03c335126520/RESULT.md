# Thirty distinct logics from six weak-modal principles: an exact implication classification

## Finding
Let \(\mathsf L_\Lambda\) be the least classical propositional modal logic closed under uniform substitution and modus ponens, together with exactly those optional modal principles in \(\Lambda\subseteq P=\{E,G,M,C,N,K\}\). Here \(E\) is replacement of proved equivalents, \(G\) is necessitation, and \(M,C,N,K\) are the usual conjunction-elimination, conjunction-introduction, boxed-truth, and distribution schemata described below. Define \(\operatorname{cl}_*(\Lambda)\) by repeatedly adding conclusions of the five implications

\[
G\Rightarrow N,\quad (E\wedge N)\Rightarrow G,\quad
(G\wedge K)\Rightarrow E\wedge M\wedge C\wedge N,\quad
(E\wedge M\wedge C)\Rightarrow K,\quad
(E\wedge M\wedge K)\Rightarrow C.
\]

Then \(\mathsf L_\Lambda=\mathsf L_\Gamma\) **if and only if** \(\operatorname{cl}_*(\Lambda)=\operatorname{cl}_*(\Gamma)\); and \(\mathsf L_\Lambda\subseteq\mathsf L_\Gamma\) **if and only if** \(\operatorname{cl}_*(\Lambda)\subseteq\operatorname{cl}_*(\Gamma)\). Exactly **30** subsets are fixed by \(\operatorname{cl}_*\), so the 64 presentations determine **exactly 30 distinct logics**, with their entire implication order characterized by these five rules.

## Assumptions and scope
The language has propositional variables, primitive \(\top\), \(\neg\), \(\to\), and \(\Box\). As in [1], \(\alpha\wedge\beta\) abbreviates \(\neg(\alpha\to\neg\beta)\) at the **syntactic** level; in particular, weak systems need not identify distinct classically equivalent formula strings under \(\Box\). The optional schemata are

\[
M:\Box(\alpha\wedge\beta)\to(\Box\alpha\wedge\Box\beta),\quad
C:(\Box\alpha\wedge\Box\beta)\to\Box(\alpha\wedge\beta),
\]
\[
N:\Box\top,\qquad K:\Box(\alpha\to\beta)\to(\Box\alpha\to\Box\beta).
\]

The inference rule \(E\) carries a theorem \(\alpha\leftrightarrow\beta\) to \(\Box\alpha\leftrightarrow\Box\beta\); \(G\) carries a theorem \(\alpha\) to \(\Box\alpha\). The statement is **only** about these 64 presentations, not all non-normal modal logics. Logical inclusion concerns sets of theorems, not inclusion of particular neighborhood frames.

## Proof
**Step 1: the five implications are valid.** Necessitation gives \(\Box\top\), proving \(G\Rightarrow N\). Since \(\alpha\leftrightarrow\top\) is a theorem for any theorem \(\alpha\), \(E+N\) gives \(G\). Standard normal-modal reasoning shows \(G+K\) yields replacement of equivalents, both conjunction axioms, and boxed truth. Under \(E+M\), classical provable implication \(\alpha\to\beta\) gives \(\Box\alpha\to\Box\beta\): use the equivalence \(\alpha\leftrightarrow(\alpha\wedge\beta)\), \(E\), then \(M\). With this monotonicity, \(C\) yields \(K\): from \(\Box(\alpha\to\beta)\) and \(\Box\alpha\), apply \(C\), then monotonicity to \(\beta\). With \(E+M+K\), from \(\Box\alpha\) monotonicity yields \(\Box(\alpha\to(\beta\to(\alpha\wedge\beta)))\); applying \(K\) twice, with \(\Box\alpha\) and \(\Box\beta\), yields \(\Box(\alpha\wedge\beta)\), proving \(C\).

**Step 2: an exact separation lemma.** Each fixed-point set \(S=\operatorname{cl}_*(S)\) and each \(x\in P\setminus S\) admit a closure frame satisfying every principle in \(S\) and refuting \(x\). The following two small witness families prove this finite assertion; the attached checker establishes that they cover all 30 fixed points and every omitted coordinate.

**Family A (extensional three-world witnesses).** Let \(W=\{0,1,2\}\), identify subsets with binary integers \(0,\ldots,7\), and choose a neighborhood family \(F\subseteq\mathcal P(W)\), the same at each world. For every valuation, interpret \(\Box\alpha\) at each world by membership of the truth set of \(\alpha\) in \(F\). Translate this model to the closure frame with \(\operatorname{cl}=\mathrm{id}\) and \(G(w)=\{\alpha:\llbracket\alpha\rrbracket\in F\}\), as in [1, Section 4.1]. It satisfies \(E\) automatically; \(G\) holds exactly when \(7\in F\). The other four conditions become the following tests for all \(A,B\subseteq W\): \(M:\ A\cap B\in F\Rightarrow A,B\in F\); \(C:\ A,B\in F\Rightarrow A\cap B\in F\); \(N:\ W\in F\); \(K:\ (W\setminus A)\cup B\in F\ \&\ A\in F\Rightarrow B\in F\). The complete nine feature profiles are witnessed by the following concrete families, where each list contains subset codes:

| Satisfied features | Codes of \(F\) |
| --- | --- |
| \(E\) | 3, 4 |
| \(C,E\) | 0, 3, 4 |
| \(C,E,K\) | 0 |
| \(C,E,G,N\) | 0, 7 |
| \(E,K\) | 1, 2 |
| \(C,E,K,M\) | empty family |
| \(C,E,G,K,M,N\) | 7 |
| \(E,G,M,N\) | 3, 5, 7 |
| \(E,G,N\) | 1, 2, 7 |

No appeal to finite experiments for arbitrary arity is needed: these feature tests are complete because three variables can realize each subset of \(W\), and the modal truth clauses reduce every instance of the schema to the indicated set conditions.

**Family B (syntax-sensitive one-world witnesses).** Take \(W=\{w\}\), \(\operatorname{cl}=\mathrm{id}\), \(G(w)=H\subseteq\mathbf{MF}\). Hence \(\Box\alpha\) holds exactly if \(\alpha\in H\), independently of valuation. Fix distinct atoms \(p,q\) and \(r=\neg\neg p\). For any formula \(\alpha\), let \(\mathrm{fac}(\alpha)\) be the set of leaves obtained by recursively splitting every *syntactically present* \(\wedge\) abbreviation \(\neg(\eta\to\neg\xi)\) at the top level; all other top-level forms give a singleton leaf. Let \(\langle T\rangle_\wedge\) be the smallest set containing the formula seeds \(T\) and closed under forming syntactic conjunctions; a seed may itself be a conjunction. Then the following nine explicit choices have **exactly** the indicated frame principles:

| \(H\) | Exactly satisfied features |
| --- | --- |
| \(\{\alpha:r\notin\mathrm{fac}(\alpha)\}\) | \(G,M,C,N\) |
| \(\mathbf{MF}\setminus\{p\}\) | \(G,C,N\) |
| \(\{\alpha:\{p,q\}\not\subseteq\mathrm{fac}(\alpha)\}\) | \(G,M,N\) |
| \(\langle\{\top,p\wedge q\}\rangle_\wedge\) | \(C,N,K\) |
| \(\langle\{\top,p\}\rangle_\wedge\cup\langle\{\top,q\}\rangle_\wedge\) | \(M,N,K\) |
| \(\langle\{\top,p,p\to q\}\rangle_\wedge\) | \(M,C,N\) |
| \(\langle\{\top\}\rangle_\wedge\) | \(M,C,N,K\) |
| \(\varnothing\) | \(E,M,C,K\) |
| \(\langle\{p\}\rangle_\wedge\) | \(M,C,K\) |

For the first and third sets, omitted formulas logically entail respectively \(\neg\neg p\) and \(p\wedge q\); neither is valid on this frame (choose \(p\) false), so \(G\) holds. For the second set the only omission is the nonvalid atom \(p\). The \(M,C\) assertions follow immediately from splitting or joining top-level conjunctions. In the four finite-generator examples without an implicative generator, \(K\) is vacuous: no term rooted at \(\to\) belongs to \(H\); when \(p\to q\) is a generator, \(K\) instead fails since \(p,p\to q\in H\) but \(q\notin H\). The omitted primitive principles have explicit witnesses: \(E\) can fail by \(p\leftrightarrow\neg\neg p\) or \(\top\leftrightarrow(p\to p)\); \(M\) fails if \(p\wedge q\in H\) but \(p\notin H\), or if \(p\wedge\top\in H\) while \(p\notin H\); \(C\) fails with \(p,q\in H\) and \(p\wedge q\notin H\); \(N\) fails when \(\top\notin H\); and \(G\) fails whenever a tautology such as \(p\to p\) is omitted. Other \(K\) counterexamples are \(p,p\to\neg\neg p\in H\) but \(\neg\neg p\notin H\), or \(\top,\top\to p\in H\) but \(p\notin H\), or \(p,p\to(p\wedge q)\in H\) but \(p\wedge q\notin H\). Each chosen frame property is schematic over **all** formulas; the syntactic definitions and the top-level shape arguments, not testing finitely many formulas, establish them.

**Step 3: exhaustiveness and distinctness.** The attached checker enumerates all 64 subsets, saturates each under the five proved implications, finds exactly 30 fixed points, independently enumerates all 256 three-world neighborhood families, computes their full feature profiles, and confirms: for every fixed point \(S\) and each omitted primitive \(x\), one of the 17 witnesses satisfies \(S\) but not \(x\). By soundness of closure semantics [1, Theorem 3.3], an omitted principle therefore is not derivable. If two closed sets differ, choose a primitive in one but not the other: its scheme/rule separates the logics. Conversely, all closure additions preserve provability, and inclusions of closed sets imply inclusion of corresponding logics. This proves both the 30-class census and the claimed inclusion order.

## Verification
Run \(\texttt{python3 weak_modal_hierarchy_verify.py}\) in the directory containing the checker. It reconstructs all neighborhood profiles and all closure-fixed sets and checks the separation matrix, returning \(\texttt{WEAK_MODAL_30_VERIFY_OK}\). This is a finite, exhaustive certificate for the 64-presentation **meta**-classification, supported by the preceding all-formula proof of the nine syntactic witness profiles. It does **not** constitute an enumeration of all modal formulas or all frames.

## Relationship to prior work
Nishimura [1] gives exactly these six optional principles, closure-frame semantics, and strong completeness for every combination; the paper notes known equivalences between normal axiomatizations but does not supply the 30-class exact census or this full implication poset. Classical \(E\)-based neighborhood systems, especially the standard \(E,M,C,N\) cube [2,3], are essential established ingredients. This finding counts the distinct resulting logics across the six-parameter lattice, including combinations without replacement or necessitation. The proof uses the syntax-sensitive nature of systems without replacement, and does not claim to have invented neighborhood semantics, necessitation, or normal-modal equivalences.

## Limitations
Historical priority is not proved. A complete older implication table expressed in different weak-modal terminology could subsume the census. Chellas [3] was compared through available bibliographic/secondary material, not a fully inspected book; this is a residual originality risk. The countermodels use arbitrary formula sets, so do not claim effective finiteness of formula generators. No independent audit has been performed.

## References
[1] Y. Nishimura, *Closure Semantics for Weak Modal Logics: Completeness and Representations*, first public 2026-10-01, arXiv:2610.01433, https://arxiv.org/abs/2610.01433; §§2–4.

[2] T. Dalmonte and L. Mazzullo, *CoNP Complexity for Combinations of Non-normal Modal Logics*, 2023, doi:10.1007/978-3-031-43513-3_17.

[3] B. F. Chellas, *Modal Logic: An Introduction*, Cambridge University Press, 1980 (historical background; complete text not inspected).
