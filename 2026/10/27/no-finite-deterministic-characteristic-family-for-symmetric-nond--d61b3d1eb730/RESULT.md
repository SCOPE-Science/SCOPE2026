# No finite deterministic characteristic family for symmetric nondeterministic choice

## Finding

For the **dynamic** multiple-conclusion consequence relation of the three-valued symmetric nondeterministic-choice matrix of Aldini–Graziani–Mezzina–Vergottini, **no finite family of finite ordinary deterministic logical matrices** in the same signature is characteristic. This includes, in particular, every individual finite ordinary matrix. The result does not exclude infinite deterministic matrices or infinite families of finite matrices.

The obstruction is uniform and explicit. For every integer \(d\ge1\), let \(L_d=d!\) and write \(\neg^m p\) for the formula with \(m\) nested negations. The following sequent is valid in **every ordinary deterministic matrix having at most \(d\) truth values**, regardless of its designated set or chosen truth functions:
\[
(\neg^{2d}p\;\widetilde\vee\;q)
\quad\Longrightarrow\quad
(\neg^{2(d+L_d)}p\;\widetilde\vee\;q).
\]
It is invalid in the dynamic three-valued nondeterministic-choice matrix. Thus even a finite *family* of matrices can be excluded by using the largest carrier size among them.

## Assumptions and scope

Work in the propositional language with unary negation \(\neg\) and binary connective \(\widetilde\vee\). The nondeterministic matrix has carrier \(V=\{0,1,k\}\), designated set \(D=\{1\}\), and deterministic negation \(\neg0=1\), \(\neg1=0\), \(\neg k=k\). Its symmetric nondeterministic disjunction is given by the table (entry sets of admissible outputs):

| \(\widetilde\vee\) | \(0\) | \(1\) | \(k\) |
|---|---|---|---|
| \(0\) | \(\{0\}\) | \(\{1\}\) | \(\{k\}\) |
| \(1\) | \(\{1\}\) | \(\{1\}\) | \(\{1,k\}\) |
| \(k\) | \(\{k\}\) | \(\{1,k\}\) | \(\{k\}\) |

A *dynamic valuation* assigns one value to each syntactically distinct formula, compatibly with the value sets of its immediate subformulas; two different compound formulas with equal-valued immediate subformulas may choose different admissible outputs. A sequent \(\Gamma\Rightarrow\Delta\) is valid if every dynamic valuation that designates every formula of \(\Gamma\) designates at least one member of \(\Delta\).

An *ordinary deterministic matrix* has a nonempty finite carrier \(A\), an arbitrary designated subset, and a single-valued operation interpreting each connective. To *characterize* the dynamic relation, its matrix consequence must agree on **all finite sequents** in this fixed signature. A family is characteristic when its intersection of consequence relations agrees. No assertion about a change of language, formulas translated to another language, or only theoremhood is made.

## Proof

**Lemma 1 (uniform eventual period).** If \(f:A\to A\) is any function on a nonempty set of size \(r\le d\), then
\[
f^{2d}=f^{2(d+d!)}
\]
as functions on \(A\). Indeed, every forward orbit enters a periodic cycle after at most \(r-1\) steps, and every cycle has length at most \(r\le d\), hence divides \(d!\). Applying \(f\) at least \(2d\) times places every orbit on its cycle; advancing another \(2d!\) steps then does not change its value. The identity holds for all \(a\in A\), without assumptions on \(f\).

**Lemma 2 (deterministic validity).** In any deterministic matrix of size at most \(d\), interpret negation as some unary \(f\) and disjunction as some binary \(h\). For every valuation of \(p,q\), Lemma 1 gives
\[
f^{2d}(v(p))=f^{2(d+d!)}(v(p)).
\]
Consequently the two displayed disjunction formulas have identical matrix truth values, namely \(h(f^{2d}(v(p)),v(q))\). The one-premise one-conclusion sequent is therefore valid regardless of the designated set.

**Lemma 3 (dynamic countervaluation).** Assign \(v(p)=1\) and \(v(q)=k\). The stipulated negation is deterministic and has period two at \(1\), so \(v(\neg^{2d}p)=v(\neg^{2(d+d!)}p)=1\). The two disjunction formulas are syntactically different, since their negation depths differ. Their shared argument pair \((1,k)\) permits either output \(1\) or \(k\). Choose the first disjunction's value as \(1\) and the second disjunction's value as \(k\). This is a legal partial dynamic valuation because neither disjunction formula is a subformula of the other. Extend its assignments to all formulas by choosing any allowed output inductively on formula complexity. The premise is designated and the conclusion is not, refuting the sequent.

**Theorem.** Suppose a finite family of finite ordinary matrices were characteristic. Let \(d\ge1\) be the maximum cardinality among their carriers. Lemma 2 makes the depth-\(d\) sequent valid in every matrix of the family, hence in their intersection. Lemma 3 refutes it in the dynamic three-valued matrix. Contradiction.

## Verification

The accompanying standalone `verify.py` enumerates every unary operation on carriers of sizes \(1,2,3,4\) and directly checks the finite identity from Lemma 1, as well as every entry of the nondeterministic table and the two independent permissible outputs at \((1,k)\). The infinite statement rests on the orbit-and-cycle proof, not on finite enumeration. The decisive distinguishing formulas are given explicitly for every integer \(d\ge1\).

## Relationship to prior work

Aldini, Graziani, Mezzina and Vergottini (2026), §3–§5, introduce exactly the three-valued dynamic matrix used here and prove that projecting their separate **five-valued deterministic** semantics to it sends deterministic valuations to legal dynamic valuations (their Theorem 8). That is one-way semantic refinement and does **not** imply equality of their consequence relations. The present result quantifies the obstruction: **no** finite deterministic matrix—or finite family of them—can have the exact dynamic consequence relation.

Avron and Lev (2005) established finite-Nmatrix versus finite-ordinary-matrix separations in other logics. Avron and Zamansky's survey states a broad no-finite-ordinary-family result for **two-valued** Nmatrices with a properly nondeterministic operation (Theorem 24); the three-valued matrix considered here does not satisfy that theorem's carrier hypothesis. Avron and Konikowska (2005) developed the dynamic/static distinction and sound/complete calculi for general finite Nmatrices; its accessible text does not state the present specific impossibility for the symmetric three-valued choice operation. Thus the current exact-language separation is narrower than a new general determinization theory but is not an identified corollary of the cited two-valued theorem.

## Limitations

This is a separation for **strong multiple-conclusion consequence** with the original two connectives. It does not by itself distinguish sets of valid closed formulas, single-conclusion theoremhood, alternative translations, infinite deterministic matrices, or infinite families. The proof applies to the dynamic, not the static, interpretation. Earlier broad nondeterministic-matrix impossibility results are substantial conceptual precedent; a yet-unidentified stronger general theorem or a direct result in inaccessible historical full text could subsume this application. No independent validation has occurred.

## References

1. A. Aldini, P. Graziani, C. A. Mezzina, and G. Vergottini, *A Logical 3-valued Semantics for Nondeterministic Choice*, arXiv:2607.20178 (first public 2026-07-22), §§3–5, especially its three-valued truth table, dynamic semantics, and Theorem 8. https://arxiv.org/abs/2607.20178
2. A. Avron and B. Konikowska, *Multi-valued Calculi for Logics Based on Non-determinism*, Logic Journal of the IGPL **13** (2005), 365–387, DOI:10.1093/jigpal/jzi030; dynamic/static definitions and §3–§4. https://doi.org/10.1093/jigpal/jzi030
3. A. Avron and I. Lev, *Non-deterministic Multiple-valued Structures*, Journal of Logic and Computation **15** (2005), 241–261, DOI:10.1093/logcom/exi001 (abstract inspected; full original article not obtained). https://doi.org/10.1093/logcom/exi001
4. A. Avron and A. Zamansky, *Non-deterministic Semantics for Logical Systems*, survey, §3, Definitions 14–18 and Theorems 24–25. https://www.cs.tau.ac.il/~aa/articles/nmatrices-survey.pdf
