# Successor knowing-value satisfiability has singly-exponential certificates
## Finding

Consider the announcement-free knowing-value logic with equality and successor introduced by Wang. Let
\[
\varphi
\]
be a formula of symbol length
\[
n\ge2,
\]
where repeated successor symbols are written explicitly in the input.

If \(\varphi\) is satisfiable over the standard arithmetic models of the paper, then it has a standard model with at most
\[
\boxed{N_n=(4n)^{n+1}}
\]
epistemic worlds.

Moreover, every constant \(c\) occurring in \(\varphi\) may be assigned, at every world, a value in
\[
\boxed{\{0,1,\ldots,U_n\}},
\qquad
U_n=(nN_n+1)(n+1).
\]

Consequently the satisfiability problem has nondeterministic running time
\[
\boxed{2^{O(n\log n)}}.
\]
In particular,
\[
\mathrm{SAT}(\mathrm{ELKvSA}^r)\in\mathrm{NEXPTIME},
\]
and by complementation,
\[
\mathrm{VAL}(\mathrm{ELKvSA}^r)\in\mathrm{coNEXPTIME}.
\]

This is a quantitative strengthening of the source's decidability theorem. The paper proves a finite-model property and a finite value-compression argument, but it does not state a complexity upper bound.

## Assumptions and scope

The language and semantics are those of Wang's announcement-free logic \(\mathrm{ELKvSA}^r\). Its terms are generated from \(0\), constants, and the unary successor operation. Thus a term \(S^a c\) contributes at least \(a\) successor symbols to the written formula.

The input-size parameter \(n\) is any ordinary symbol-count or syntax-tree size for which the following standard inequalities hold:
\[
|\operatorname{Sub}(\varphi)|\le n,
\qquad
\operatorname{depth}(\varphi)\le n,
\]
and every explicitly written successor exponent appearing in the formula is at most \(n\).

The result concerns the announcement-free fragment studied in Sections 3--5 of the source. Public-announcement operators are not included in the complexity statement.

The model-size parameter counts epistemic worlds, exactly as in the paper's finite-model theorem. The arithmetic carrier of a standard model remains \(\mathbb N\); the second displayed bound says that only a bounded initial segment of \(\mathbb N\) is needed for values of constants occurring in the input formula.

No lower complexity bound beyond those inherited from known sublanguages is claimed here.

## Proof

Let
\[
\Sigma
\]
be the set of subformulas of \(\varphi\) closed under single negation, as in Wang's finite-model construction. Since a formula has at most \(n\) subformulas,
\[
|\Sigma|\le2n.
\]
Let
\[
D=\operatorname{depth}(\varphi).
\]
Then
\[
D\le n.
\]

Wang's Theorem 5.2 constructs a finite non-standard model by selecting only finitely many witnesses at each modal level. Its stated bound is exponential in the branching parameter \(2|\Sigma|\) and modal depth. A uniform bound that directly dominates the source estimate is
\[
|W|
\le
(2|\Sigma|)^{D+1}
\le
(4n)^{n+1}
=
N_n.
\]

Lemma 5.1 transfers a finite non-standard model to a standard model without changing the epistemic world set. Thus the same \(N_n\) bounds standard witnesses.

The decision proof in Theorem 5.6 then compresses the values of all constants occurring in \(\varphi\). Write \(C_\varphi\) for those constants and put
\[
B=
\max\Bigl(
\{a+b:\ S^a x\approx S^b y\text{ is a subformula of }\varphi\}
\cup\{0\}
\Bigr).
\]
Because successors are explicit,
\[
|C_\varphi|\le n
\qquad\text{and}\qquad
B\le n.
\]

Wang's compression argument bounds every relevant constant value by
\[
(|C_\varphi|\,|W|+1)(B+1).
\]
Substituting the elementary estimates above gives
\[
(|C_\varphi|\,|W|+1)(B+1)
\le
(nN_n+1)(n+1)
=
U_n.
\]

It remains to account for certificate size and verification time.

Only symbols occurring in \(\varphi\) matter. Hence there are at most \(n\) relevant agents, proposition letters, and constants. A guessed standard model may be encoded by:

- at most \(n\) equivalence relations on \(W\), using at most \(nN_n^2\) bits;
- proposition valuations, using at most \(nN_n\) bits;
- constant valuations, using at most \(nN_n\lceil\log_2(U_n+1)\rceil\) bits;
- one distinguished world.

Since
\[
N_n=(4n)^{n+1}=2^{O(n\log n)}
\]
and
\[
\log U_n=O(n\log n),
\]
the whole certificate has length
\[
2^{O(n\log n)}.
\]

A deterministic verifier first checks that each guessed accessibility relation is an equivalence relation. It then evaluates all subformulas bottom-up at all worlds. Ordinary knowledge modalities require scanning accessible worlds. A knowing-value formula can be checked by comparing the term values at pairs of accessible worlds satisfying its condition. Even the naive implementation uses only a polynomial in \(n\) and \(N_n\), for example \(O(nN_n^3)\) elementary operations. Arithmetic terms require only addition of the explicitly written successor offset to a bounded constant value.

Therefore the guessed model can be verified within
\[
2^{O(n\log n)}
\]
time. This proves
\[
\mathrm{SAT}(\mathrm{ELKvSA}^r)
\in
\mathrm{NTIME}(2^{O(n\log n)}).
\]

Finally, \(\varphi\) is valid exactly when \(\neg\varphi\) is unsatisfiable, and negation changes input length by only a constant. Hence validity belongs to the corresponding co-nondeterministic time class and therefore to coNEXPTIME.

## Verification

The source was checked at the three quantitative points on which the proof depends.

Theorem 5.2 gives an explicit finite-world witness bound in terms of the single-negation subformula closure and modal depth.

Lemma 5.1 transfers finite non-standard witnesses to standard arithmetic models while preserving the finite epistemic world set.

Theorem 5.6 compresses all values of constants occurring in the input formula into an explicitly bounded initial segment whose endpoint is
\[
(|C_\varphi|f(|\varphi|)+1)(B+1).
\]
Substituting the explicit world bound for \(f\), and the syntactic estimates \(|C_\varphi|\le n\) and \(B\le n\), gives \(U_n\).

The complexity calculation was then replayed independently from the resulting finite certificate representation. No assumption is made that the source's brute-force enumeration procedure itself runs in nondeterministic exponential time; instead, the theorem uses nondeterministic guessing of one bounded witness model followed by direct semantic verification.

## Relationship to prior work

Wang proves that \(\mathrm{ELKvSA}^r\) has the finite-model property and is decidable. The decision proof explicitly bounds both the number of worlds and the range of relevant constant values, but stops at finiteness and does not assign the problem to a standard complexity class.

Earlier conditional knowing-value logic without successor arithmetic has substantially sharper known complexity results. Ding proves PSPACE-completeness for a closely related knowing-what logic over arbitrary Kripke frames. Those results do not cover the successor-arithmetic extension, whose semantics additionally contains equality constraints between shifted values.

The present result does not claim optimality. It extracts the first direct standard upper class from the new paper's quantitative model construction:
\[
2^{O(n\log n)}
\]
nondeterministic time.

Targeted searches for the exact source together with NEXPTIME, exponential-model, model-certificate, and satisfiability-complexity formulations did not locate this consequence.

## Limitations

The bound is an upper bound only. The exact complexity of \(\mathrm{ELKvSA}^r\) satisfiability remains open here.

The factor \(n\log n\) in the exponent comes from using the paper's general finite-witness construction without attempting tableau sharing, filtration, or a more economical representation of equivalence classes.

The argument treats successor iteration as explicitly written syntax. A succinct input formalism with binary-coded successor exponents would require a different size analysis.

Public-announcement operators are outside the claimed fragment. Although the source reduces the announcement language to the announcement-free language proof-theoretically, this result does not analyze the size blow-up of that reduction.

## References

[1] Hongyi Wang, “Knowing-Value Logic with Successor Arithmetic,” *Electronic Proceedings in Theoretical Computer Science* 447 (2026), 731--749. arXiv:2606.31891. DOI:10.4204/EPTCS.447.41.

[2] Yifeng Ding, “Axiomatization and complexity of modal logic with knowing-what operator on model class K,” arXiv:1609.07684, 2016.
