# Full-function Set semantics admits only the terminal generalized Bullet type
## Finding
Naibo and Takahashi prove that for each type \(A\), their generalized Bullet type \(\bullet^A\) is provably isomorphic to \(\bullet^A\to A\) in both generalized Bullet calculi. In any sound extensional Set-valued semantics using full function sets for arrow types, this forces a bijection
\[
D\cong E^D,
\]
where \(E=\llbracket A\rrbracket\) and \(D=\llbracket\bullet^A\rrbracket\). Such a bijection exists exactly when \(E\) is a singleton, and then \(D\) is also a singleton.

Two consequences follow. First, interpreting falsity in the usual set-theoretic way as \(\llbracket\bot\rrbracket=\varnothing\) makes the original Bullet connective \(\bullet=\bullet^\bot\) impossible in this semantic regime. Second, the self-referential type \(\bullet^\ast\) of Section 3.3, for which Proposition 3.7 gives \(\bullet^\ast\cong(\bullet^\ast\to\bullet^\ast)\), must denote a singleton. Hence every term obtained from the paper's translation of untyped \(\lambda\beta\eta\)-calculus has the same denotation under any full-function Set semantics of this kind.

## Assumptions and scope
Fix either of the two generalized Bullet calculi considered by Naibo and Takahashi. Assume a denotational semantics into ordinary sets satisfying the following two conditions.

1. Every function type \(A\to B\) is interpreted by the full set \(\llbracket B\rrbracket^{\llbracket A\rrbracket}\) of all functions from \(\llbracket A\rrbracket\) to \(\llbracket B\rrbracket\).
2. The reduction equalities used to establish the published Bullet type isomorphisms are sound, so the two closed terms witnessing each isomorphism denote mutually inverse functions.

No completeness assumption is made. No assumption of finiteness is made on any denotation. The result concerns this specific full-function Set semantics; it does not cover domain-theoretic, relational, realizability, presheaf, or other categorical semantics in which an arrow object need not be the full set of all functions.

## Proof
Let \(E=\llbracket A\rrbracket\) and \(D=\llbracket\bullet^A\rrbracket\). The published type isomorphism \(\bullet^A\cong(\bullet^A\to A)\), together with soundness of the witnessing reductions, gives a bijection
\[
D\cong E^D.
\]
We classify all pairs of sets \((D,E)\) satisfying this equation.

If \(E=\varnothing\), then there is no solution. When \(D=\varnothing\), the set \(E^D=\varnothing^\varnothing\) contains the unique empty function and is therefore a singleton, so it cannot be bijective with \(D\). When \(D\ne\varnothing\), there is no function from \(D\) to \(E\), so \(E^D=\varnothing\), again preventing a bijection.

If \(|E|=1\), then \(E^D\) is a singleton for every set \(D\). Thus a bijection \(D\cong E^D\) forces \(|D|=1\). Conversely, when both \(D\) and \(E\) are singletons, the required bijection exists.

Finally suppose \(|E|\ge2\). If \(D=\varnothing\), then \(E^D\) is a singleton, so again no bijection exists. If \(D\ne\varnothing\), choose distinct \(e_0,e_1\in E\). Every subset \(S\subseteq D\) determines a distinct characteristic-style map \(f_S:D\to E\), with value \(e_1\) on \(S\) and \(e_0\) on \(D\setminus S\). Hence
\[
|E^D|\ge 2^{|D|}>|D|
\]
by Cantor's theorem. Therefore \(D\) cannot be bijective with \(E^D\).

This proves that \(D\cong E^D\) is possible exactly when \(|E|=|D|=1\). Taking \(A=\bot\) yields the empty-falsity obstruction. For the self-type \(\bullet^\ast\), Proposition 3.7 gives \(D\cong D^D\); applying the same empty/singleton/Cantor trichotomy forces \(|D|=1\). Every translated untyped term has type \(\bullet^\ast\), so all of those terms receive the same denotation.

## Verification
The source was checked at the publisher's open-access HTML version. It states that the article was published online on 13 February 2026 and assigns primary MSC 03A05. Proposition 3.7 explicitly gives closed terms in both \(\lambda^{{\to\bullet}}_{{1\ast}}\) and \(\lambda^{{\to\bullet}}_{{2\ast}}\) whose two composites reduce to the relevant identities, and Corollary 3.8 records the resulting isomorphism \(\bullet^\ast\cong(\bullet^\ast\to\bullet^\ast)\). The preceding generalized construction states the corresponding isomorphism \(\bullet^A\cong(\bullet^A\to A)\) for arbitrary \(A\) in both systems.

The proof above was reconstructed independently from these displayed isomorphisms. The three cardinal cases \(|E|=0\), \(|E|=1\), and \(|E|\ge2\) exhaust all sets, and the last case uses an explicit injection from the power set of \(D\) into \(E^D\), so no choice principle beyond selecting two displayed elements of a non-singleton \(E\) is needed.

## Relationship to prior work
The cardinal obstruction to a nontrivial ordinary set \(D\) satisfying \(D\cong D^D\) is classical in the semantics of untyped lambda calculus and motivated domain-theoretic solutions using restricted function spaces. The new point here is the exact specialization to Naibo--Takahashi's 2026 Bullet systems: the more general equation \(D\cong E^D\) arising from their \(\bullet^A\) type isomorphism has a solution precisely for the terminal target \(E\), which immediately rules out the conventional empty-set interpretation of falsity and forces their untyped-encoding self-type to collapse under full-function Set semantics.

The source paper develops the type isomorphisms and the interpretation of untyped lambda calculus, but does not state this Set-cardinality classification or the empty-falsity no-go consequence. Targeted searches for Set semantics, cardinal collapse, singleton interpretations, and equivalent formulations did not reveal a stronger or equivalent published statement for these Bullet calculi.

## Limitations
The result is a semantic obstruction, not an inconsistency theorem for the calculi. It says nothing against non-Set semantics or Set-based constructions in which arrow objects contain only selected functions rather than every function. The untyped translation is shown to be non-separating only under the stated full-function Set assumptions; no claim is made that the source's computational interpretation itself is defective. The originality assessment is best-of-knowledge and relies on targeted rather than exhaustive literature coverage.

## References
1. Alberto Naibo and Yuta Takahashi, *Paradoxical Connectives: Proof-Theoretic Semantics, Recursion, and Fixed-Point Operators*, The Review of Symbolic Logic 19(2), 317--354 (2026), DOI 10.1017/S1755020326101099. Published online 13 February 2026.
2. H. P. Barendregt, *The Lambda Calculus: Its Syntax and Semantics*, revised edition, North-Holland, 1984. Classical background on set-theoretic obstructions and denotational semantics for untyped lambda calculus.
