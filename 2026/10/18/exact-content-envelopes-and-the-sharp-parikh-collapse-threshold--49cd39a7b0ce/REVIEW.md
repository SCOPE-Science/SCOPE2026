# Scientific review: exact jumbled-equivalence transition and content envelope

## Correctness — PASS

The theorem has two independently auditable components. The content-envelope upper bound holds for every host word because any feasible pattern contains \(h\) repetitions of its most frequent letter, forcing an LCS of at least \(h\); its length is bounded by the sum of the truncated capacities. The reverse-block witness attains equality: forward and reverse block orders admit no common subsequence containing two different letters, and the selected capacities realize the maximizing \(h\). Empty host, one-letter alphabets, absent letters, and the full range of \(k\) are included. For the equivalence-index statement, the pigeonhole LCS bound implies complete Parikh collapse above the proposed threshold, pure-letter probes distinguish all different capped vectors, and opposite balanced block orders show that exactly one capped-vector fiber splits at every subthreshold budget. Thus the lower bound for index is strict, not merely a non-equivalence example without class-count implications.

The independent finite program checks 191852 ordered host-pattern instances for the threshold formula and 34188 feasible host-pattern comparisons for the content envelope; it also verifies sharp reverse-block witnesses for alphabets larger than the tested word lengths. Finite tests support but do not replace the symbolic proof. No nonstandard external lemma or unverified numerical certificate is required.

## Originality — PASS within inspected evidence

Fleischmann–Huch–Kammholz–Koß, *Jumbled Scattered Factors* (arXiv:2506.03814v1, 2025-06-04), introduces the same model, develops the LCS/jumble connection, addresses jumbled Simon equivalence, and explicitly leaves further class/index analysis open in Section 6. The paper's \(\ell=k-1\) boundary and finite-class statements do not supply the exact host-content envelope or establish the *least* alphabet-dependent stabilization budget.

The follow-up *Jumbled Simon’s Equivalence and Embeddings* by Fleischmann, Huch, Kim, Koß, and Wiards (arXiv:2610.17910v1, 2026-10-13) formalizes the nonnegative-budget convention and states the capped-Parikh equivalence and index in Proposition 10 and Corollary 11 **only at** \(\ell=k-1\). Its Lemma 16 compares LCS profiles for equivalence testing but does not imply the sharp universal \(\ell=k-\lceil k/q\rceil\) threshold or determine the host-content maximization. The latter is not merely substituting \(\ell\) into the published formula: necessity below the threshold requires a separate balanced reverse-block obstruction. Both primary full texts, including their definitions, theorem statements, nearby propositions and concluding sections, were examined.

Searches for jumbled Simon-equivalence index, Parikh stabilization, disorder budgets and anagram LCS extremals did not reveal a covering theorem. Semantic mathematical-record hits about ordinary subsequence universality, Parikh matrices and binary word statistics do not compare the same equivalence quotient or extremize the same LCS deficit. Previously published relevant claims were compared for mathematical implication and did not disclose a covering theorem. Remaining risk: an equivalent extremal statement could exist in unindexed combinatorics-on-words literature or as an unstated implication in uninspected sources. A search failure is not proof of priority; no independent bibliographic audit is claimed.

## Value — PASS

The originating problem asks for the size and structure of jumbled-Simon equivalence classes; the new theorem identifies a sharp, nontrivial parameter transition at which **the full quotient** has the smallest possible number of classes and every class has a simple capped-histogram signature. It simultaneously supplies the exact minimax disorder budget for *each* fixed content vector, not just the alphabet-only worst case. These formulas separate disorder due to sparse content from worst-case balanced content and identify explicit extremal witnesses. This is a naturally motivated infinite-family structural classification; exact subthreshold indices and finer individual-host budgets remain unresolved here.

## Scope, scientific risks and verification limits

The result uses jumbled scattered subsequences, not contiguous jumbled factors; only pattern lengths up to \(k\) are considered. The 2025 paper uses an additional restriction for very short patterns; the adopted nonnegative-budget extension of the 2026 paper handles the empty pattern uniformly. Our nonempty separating witnesses and the quotient-index calculation are unaffected by the empty-pattern convention. The available record search is not exhaustive and publication priority remains open to independent checking. Standalone finite enumeration is intentionally distinguished from proof for arbitrary \(q,k,\ell\) and \(\mathbf c\).

Self-review: passed. Independent audit: not yet performed.
