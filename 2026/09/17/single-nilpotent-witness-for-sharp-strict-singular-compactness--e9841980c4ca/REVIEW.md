# same-model review

## Scope of the check

This record claims a strengthening of the sharpness part of Laustsen--Wirzenius (2026): their non-compact product of k strictly singular operators can, on the same spaces, be replaced by the k-th power of one strictly singular operator which is actually nilpotent of order k+1.

The three axes below were checked separately. This is a same-model review, not independent validation.

## Correctness

### Primary-source dependencies checked

The accessible accepted manuscript of Laustsen--Wirzenius was inspected at the theorem/proof level. The following ingredients were checked directly:

- Theorem 1.1 gives the value of k, compactness of every product of k+1 strictly singular operators, and existence of a non-compact product of k such operators.
- Equation (3.2) states that on a finite direct sum, an operator belongs to an operator ideal if and only if all matrix entries belong to that ideal.
- Lemma 3.7 gives strictly singular formal inclusions R_{Y,Z} whenever Y precedes Z in the paper's linear order.
- In the proof of Theorem 1.1(ii), the family Sigma has cardinality k+1; when ordered as Y_1<...<Y_{k+1}, the composite R_{Y_k,Y_{k+1}}...R_{Y_1,Y_2} is the formal inclusion from Y_1 to Y_{k+1} and is non-compact.
- Remark 1.2(iii) gives B_p direct-sum ell_p isomorphic to B_p and allows the ell_p index set to be enlarged from M to L union M without changing the isomorphism class.
- Remark 1.2(iv) and Remark 3.8 give absorption of c_0 when a Schreier summand is present.

These statements are exactly what the shift proof uses.

### Hidden-hypothesis checks

1. **Complementability.** The proof does not infer complementability of arbitrary block subspaces from unconditionality. The only decompositions used are the explicit absorption isomorphisms B_p plus ell_p isomorphic to B_p and S_p plus c_0 isomorphic to S_p, supported by complemented copies established in the cited papers.

2. **Strict singularity of the shift.** Each nonzero matrix entry is one of the strictly singular formal inclusions. The finite-matrix operator-ideal criterion then gives strict singularity of the whole shift. No infinite-matrix closure argument is used.

3. **Non-compactness of the k-th power.** The (last,first) matrix compression of S^k equals the full formal inclusion R_{Y_1,Y_{k+1}}. If S^k were compact, this compression would be compact, contradicting the primary source.

4. **Similarity transfer.** If U:Z->X is an isomorphism, strict singularity and compactness are preserved under U(·)U^{-1}; powers satisfy (USU^{-1})^j=US^jU^{-1}.

5. **Degenerate case.** k=0 occurs only when L=N=empty and M is a singleton, i.e. X=ell_p. This case is excluded from the nontrivial witness theorem and is correctly described by S(X)=K(X).

6. **Algebraic nontriviality.** A three-dimensional associative algebra with ab=c, ba=-c and all other basis products zero has A^2 nonzero and A^3=0, while x^2=0 for every x. Hence a maximal-length product witness does not generally imply a same-length power witness.

No correctness defect was found.

## Originality

### Internal SCOPE overlap

Repository searches on the current default branch were performed for “strictly singular”, “Baernstein”, “Schreier strictly singular”, and “power compact”. No SCOPE result matching this claim was returned. The current date directory and recent commits were also inspected. GitHub search can lag or miss semantic equivalents, so this is supporting evidence rather than a guarantee; a final semantic/identity check is required immediately before publication.

### External searches

Searches included combinations of:

- square-zero / square zero + strictly singular + Banach / Baernstein / Schreier;
- nilpotent + strictly singular + Baernstein / Schreier;
- power-compact + strictly singular + Baernstein / Schreier;
- single strictly singular operator + power compact;
- the DOI and arXiv identifier of Laustsen--Wirzenius together with “nilpotent operator”, “power compact”, “square-zero”, and “single operator”.

The Laustsen--Wirzenius manuscript itself was searched for “power”, “power-compact”, and equivalent single-operator terminology; no such formulation was located. Its explicit lower-bound proof uses k separately lifted operators.

Laustsen--Smith (2026) establishes compactness of every product of two strictly singular operators on B_p and S_p but the accessible article statements did not locate a non-compact square-zero witness. Their 2025 operator-ideal paper supplies non-compact strictly singular operators but again no square-zero statement was located in the searches performed.

Flores--Hernández--Semenov--Tradacete (2012) is important prior art: it studies power-compact strictly singular operators and uses shift-like constructions on other Banach lattices to obtain operators with non-compact powers. Therefore this record does **not** claim novelty for the abstract shift idea. The apparent old assertion that Baernstein spaces were disjointly homogeneous is not usable coverage: Laustsen--Smith (2025) explicitly identify it as a consequence of an earlier erroneous Baernstein claim and note that it would contradict their non-compact strictly singular operators.

### Originality assessment

To the best of the literature search performed, no source was found stating that the exact Laustsen--Wirzenius nilpotency index is attained by a single strictly singular operator, or the special consequences that B_p and S_p admit non-compact square-zero strictly singular operators. The result is close enough to the 2026 source that an unindexed remark, lecture note, or subsequent note by the same authors remains a realistic residual risk. The claim is therefore “to the best of our knowledge,” not an assertion of exhaustive priority.

No highly relevant inaccessible paper was identified that specifically appears likely to contain this exact strengthening. The most relevant papers listed in RESULT.md were accessible at least at the theorem/statement level; the Laustsen--Wirzenius accepted manuscript was inspected in detail.

## Value

The strengthening distinguishes two notions that coincide in this family but not in arbitrary nilpotent algebras:

- sharp nilpotency witnessed by a product of different elements;
- sharp nilpotency witnessed by powers of one element.

It gives the exact uniform power-compactness exponent of strictly singular operators and realizes the boundary by an operator which is algebraically nilpotent, not merely power-compact. The square-zero corollaries for each individual B_p and S_p are concise structural facts that are not visible from the published “every product of two is compact” theorem alone.

The mechanism is reusable: whenever a sharp chain of ideal maps can be simultaneously realized as direct summands (or absorbed into the ambient space), a one-superdiagonal shift converts the chain into a single nilpotent witness. This is a meaningful structural lemma rather than a numerical parameter variation.

## Verdict

- Correctness: PASS.
- Originality: PASS, to the best of our knowledge, with explicit residual risk from unindexed or subsequent remarks.
- Value: PASS.

Review type: same-model review. Independent validation: false.
