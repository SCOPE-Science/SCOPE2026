# A sharp seven-state associative completion of symmetric-choice error semantics

## Finding

A five-valued deterministic error semantics described by Aldini, Graziani, Mezzina and Vergottini (2026) has carrier \(M=\{0,1,u,e,k\}\), associative disjunction \(\vee\), and a three-valued projection \(\pi:M\to\{0,1,k\}\) fixing \(0,1\) and mapping \(u,e,k\) to \(k\). The possible coarse results of the ordered probes \((1\vee a,a\vee1)\), as \(a\) ranges over the old error values, are \((1,1)\), \((1,k)\), and \((k,k)\). The fourth permitted profile, \((k,1)\), is absent.

**Sharp completion theorem.** Among finite associative deterministic algebras that contain this **exact** five-valued disjunction table as a subalgebra, extend the stated three-valued projection with **every new value projecting to error** \(k\), preserve compatibility with the published symmetric three-valued nondeterministic disjunction, and realize an error value \(r\) with coarse probe profile \((k,1)\), the minimum cardinality is **seven**. A seven-element extension exists with just two additional error values, \(r\) and \(x\). In this extension the four possible one-step ordered profiles are all attained. Furthermore \(x=e\vee r\) is forced to be distinct from both the original five values and \(r\), in **every** associative extension meeting these requirements.

This is a minimum-extension theorem for a specified published algebra, not a claim that the seven-element extension realizes every nondeterministic valuation, or that the extension is unique.

## Assumptions and scope

The original five-element table is as follows. The row is the left operand.

| \(\vee\) | \(0\) | \(1\) | \(u\) | \(e\) | \(k\) |
|---|---|---|---|---|---|
| \(0\) | \(0\) | \(1\) | \(u\) | \(e\) | \(k\) |
| \(1\) | \(1\) | \(1\) | \(1\) | \(1\) | \(k\) |
| \(u\) | \(u\) | \(1\) | \(u\) | \(e\) | \(k\) |
| \(e\) | \(e\) | \(e\) | \(e\) | \(e\) | \(k\) |
| \(k\) | \(k\) | \(k\) | \(k\) | \(k\) | \(k\) |

Here \(0\) is an identity and \(k\) an absorbing element. The published symmetric three-valued nondeterministic disjunction on \(\{0,1,k\}\) agrees with classical disjunction on \(0,1\), has singleton outputs \(0\widetilde\vee k=k\widetilde\vee0=\{k\}\), \(k\widetilde\vee k=\{k\}\), and has output set \(\{1,k\}\) on both ordered mixed pairs \((1,k)\), \((k,1)\).

An **error-only extension** is an algebra \((A,\vee)\) whose named old five values have exactly this multiplication table, together with a map \(\pi:A\to\{0,1,k\}\) extending the published projection, with \(\pi^{-1}(0)=\{0\}\) and \(\pi^{-1}(1)=\{1\}\), and satisfying \(\pi(a\vee b)\in\pi(a)\widetilde\vee\pi(b)\) for all \(a,b\in A\). It must have a new value \(r\) with \(\pi(r)=k\), \(\pi(1\vee r)=k\), and \(\pi(r\vee1)=1\). No assumption of commutativity is imposed. Optional unary negation in the exhibited extension fixes the five error values and exchanges \(0\) and \(1\), thereby extending the original negation and preserving projection. It is not assumed to distribute over disjunction.

## Proof

**Lower bound.** The five old values have coarse probe signatures
\[
 u:(1,1),\qquad e:(1,k),\qquad k:(k,k).
\]
Consequently a value with signature \((k,1)\) must be new. Let \(r\) be such a value. Write \(y=e\vee r\). Associativity and the old identities \(e\vee1=e\) and \(1\vee e=1\) give
\[
 y\vee1=e\vee(r\vee1),\qquad
 1\vee y=(1\vee e)\vee r=1\vee r.
\]
Because the extension adds only error values, the unique value projecting to \(1\) is the original \(1\), so \(r\vee1=1\). Hence \(y\vee1=e\). Within the old five elements, only \(e\) satisfies \(a\vee1=e\); the new \(r\) instead satisfies \(r\vee1=1\). Thus \(y=e\). But then the second displayed identity gives \(1=1\vee e=1\vee r\), contrary to \(\pi(1\vee r)=k\). The same reasoning also shows in **any** error-only extension that \(y=e\vee r\) cannot be any of the old five values or \(r\). Consequently every such completion has at least seven values.

**Seven-element construction.** Let \(A=\{0,1,u,e,k,r,x\}\). Define \(\vee\) by the following entire table, whose upper-left five-by-five block is unchanged.

| \(\vee\) | \(0\) | \(1\) | \(u\) | \(e\) | \(k\) | \(r\) | \(x\) |
|---|---|---|---|---|---|---|---|
| \(0\) | \(0\) | \(1\) | \(u\) | \(e\) | \(k\) | \(r\) | \(x\) |
| \(1\) | \(1\) | \(1\) | \(1\) | \(1\) | \(k\) | \(r\) | \(r\) |
| \(u\) | \(u\) | \(1\) | \(u\) | \(e\) | \(k\) | \(r\) | \(x\) |
| \(e\) | \(e\) | \(e\) | \(e\) | \(e\) | \(k\) | \(x\) | \(x\) |
| \(k\) | \(k\) | \(k\) | \(k\) | \(k\) | \(k\) | \(k\) | \(k\) |
| \(r\) | \(r\) | \(1\) | \(r\) | \(k\) | \(k\) | \(r\) | \(k\) |
| \(x\) | \(x\) | \(e\) | \(x\) | \(k\) | \(k\) | \(x\) | \(k\) |

Every associativity instance \((a\vee b)\vee c=a\vee(b\vee c)\) holds. A fully explicit, standalone exhaustive proof certificate in `checker.py` verifies all \(7^3=343\) ordered triples against these literal table entries. This is a complete finite proof, not sampling. For an independent structural check, the four-element subsemigroup \(\{e,r,x,k\}\) is represented by the Boolean matrices
\[
 e=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
 r=\begin{pmatrix}0&1\\0&1\end{pmatrix},\quad
 x=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad
 k=\begin{pmatrix}0&0\\0&0\end{pmatrix}
\]
under Boolean matrix multiplication, where \(x=er\), \(re=k\), and \(x^2=k\). The remaining cases are checked by the full table certificate.

Set \(\pi(0)=0\), \(\pi(1)=1\), and \(\pi(u)=\pi(e)=\pi(k)=\pi(r)=\pi(x)=k\). Each of the \(49\) ordered table entries maps into the corresponding nondeterministic output set, as the checker verifies. The four witnesses for the coarse ordered profiles are
\[
 u:(1,1),\quad e:(1,k),\quad r:(k,1),\quad k:(k,k).
\]
The new compound error \(x=e\vee r\) is generated by the five original values and \(r\). The explicit extension therefore has seven states and achieves the lower bound.

## Verification

Run `python3 checker.py` beside this document. The checker uses Python's standard library only, stores an independently transcribed copy of the published five-state table, and checks preservation of all \(25\) old products, all \(343\) associativity triples, all \(49\) projection cases, involution and projection compatibility of optional negation, each ordered probe signature, the generation of \(x\) from the original values and \(r\), and the algebraic six-state impossibility argument. Its expected output is `ALL_CHECKS_OK 343 associativity triples 49 projection pairs`.

## Relationship to prior work

Aldini, Graziani, Mezzina and Vergottini (2026) define both the symmetric three-valued Nmatrix and exactly the five-valued deterministic algebra used as input here; their Lemma 1 proves associativity of that five-valued operation, and their Theorem 8 proves one-way projection soundness. They do **not** introduce a right-masking dual to \(e\), identify a forced compound error, or establish a minimum associative enlargement. Avron and Konikowska (2009) study a related four-valued deterministic error semantics for Kleene/McCarthy computation errors; its accessible abstract concerns that smaller system, not this specific seven-state completion. Older McCarthy algebra and contaminating-logic literature is relevant background, but equivalent results under alternate semigroup terminology cannot be excluded.

## Limitations

The minimality holds **conditional on retaining the original five-element algebra literally as a subalgebra, introducing only new error-projected values**, and exhibiting the stated missing ordered error profile. It does not imply seven states are necessary for every deterministic refinement of the three-valued Nmatrix from scratch. Capturing four one-step ordered masking profiles does **not** capture all globally static or dynamically nondeterministic valuations. Uniqueness of minimal extensions and an axiomatisation of the seven-state logic are not claimed. Independent validation has not been performed. The 2009 precursor's complete full text was not accessible, leaving a residual priority risk.

## References

1. A. Aldini, P. Graziani, C. A. Mezzina, and G. Vergottini, *A Logical 3-valued Semantics for Nondeterministic Choice* (first public 2026-07-22), arXiv:2607.20178, EPTCS 449 (2026), 1–17, doi:10.4204/EPTCS.449.1. See §§3, 5–6.
2. A. Avron and B. Konikowska, *Proof Systems for Reasoning about Computation Errors*, Studia Logica 91 (2009), 273–293, doi:10.1007/s11225-009-9175-4 (abstract accessible; full text unavailable).
3. B. Konikowska, *McCarthy Algebras: A Model of McCarthy's Logical Calculus*, Fundamenta Informaticae 26 (1996), 167–203, doi:10.3233/FI-1996-26205 (abstract accessible).
