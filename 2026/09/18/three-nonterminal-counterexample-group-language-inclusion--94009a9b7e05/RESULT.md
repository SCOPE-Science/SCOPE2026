# A three-nonterminal counterexample to a context-free group-inclusion criterion

## Result

Under the definitions published in Krasimir Yordzhev, *On A. V. Anisimov's problem for finding a polynomial algorithm checking inclusion of context-free languages in group languages* (Filomat 38:12 (2024), 4157--4166; arXiv:2602.18305), Theorem 4.3 and Algorithm 4.4 are false as stated.

A counterexample already exists with three nonterminals. Let
\[
N=\{A_1,A_2,A_3\}
\]
and let the grammar in Chomsky normal form have productions
\[
A_1\to A_2A_3,\qquad A_2\to x_1,\qquad A_3\to x_1'.
\]
Take the terminal alphabet required in Theorem 4.3, with inverse pairs
\[
\Sigma=\{x_1,x_2,x_3,x_1',x_2',x_3'\},
\]
and take \(G\) to be the free group on \(x_1,x_2,x_3\), so \(x_i'\) represents \(x_i^{-1}\). The word problem of \(G\) is decidable.

Then
\[
L(\Gamma,A_1)=\{x_1x_1'\}\subseteq L(G),
\]
because \(x_1x_1'=e\) in \(G\). Nevertheless, Algorithm 4.4 returns `False`.

## Why the published criterion fails

Definition 3.1 constructs
\[
U=\Sigma^*\times T
\]
with componentwise multiplication. Its identity is
\[
1_U=\langle\varepsilon,e\rangle.
\]
The first coordinate is the free-monoid word in \(\Sigma^*\), not its value in \(G\). Therefore
\[
\langle x_1x_1',e\rangle\ne\langle\varepsilon,e\rangle
\quad\text{in }U,
\]
even though \(x_1x_1'=e\) in the group \(G\).

For the grammar above, Definition 3.2 gives the four relevant arcs
\[
A_1\to A_2:\langle\varepsilon,A_3\rangle,\qquad
A_2\to Z:\langle x_1,e\rangle,
\]
\[
Z\to A_3:\langle\varepsilon,A_3'\rangle,\qquad
A_3\to Z:\langle x_1',e\rangle.
\]
Write \(A_4=Z\), as in Section 4, and let
\[
g^k_{ij}=l(K^k_{ij}).
\]
The recurrence used by Algorithm 4.4 is
\[
g^k_{ij}
=
g^{k-1}_{ij}\cup
g^{k-1}_{ik}g^{k-1}_{kj}.
\]

At stage \(k=2\),
\[
\langle x_1,A_3\rangle\in g^2_{14},
\]
coming from the walk \(A_1\to A_2\to Z\). At stage \(k=3\),
\[
\langle x_1',A_3'\rangle\in g^3_{44},
\]
coming from \(Z\to A_3\to Z\). Monotonicity of the recurrence keeps
\(\langle x_1,A_3\rangle\) in \(g^3_{14}\). Hence at stage \(k=4\),
\[
\langle x_1,A_3\rangle
\langle x_1',A_3'\rangle
=
\langle x_1x_1',A_3A_3'\rangle
=
\langle x_1x_1',e\rangle
\in g^4_{14}.
\]
This element is not \(1_U\).

Line 7 of Algorithm 4.4 tests whether \(g^{n+1}_{1,n+1}\) is nonempty and differs from the singleton \(\{1_U\}\); if so, line 8 sets the answer to `False`. Here \(n=3\), so the displayed element proves that
\[
g^4_{14}\ne\varnothing,\qquad
g^4_{14}\ne\{1_U\}.
\]
The algorithm therefore rejects, although the language is contained in the group language.

The same example directly separates conditions (i) and (iv) of Theorem 4.3: condition (i) holds, while \(W_3\) contains the nonidentity element
\(\langle x_1x_1',e\rangle\) of \(U\), so condition (iv) fails.

## Source of the mismatch

The issue is already visible between the paper's earlier and later criteria. Theorem 2.1 states the Anisimov condition in the form
\[
W_1\subseteq L(G).
\]
Theorem 4.3 replaces the corresponding condition by
\[
W_1=\{\varepsilon\}.
\]
These are not equivalent for a nontrivial group language: a nonempty word can represent the identity of \(G\).

Likewise, the semiring in Section 4 stores first coordinates in the free monoid \(\Sigma^*\), while Algorithm 4.4 compares them to the literal empty word through equality with
\(\langle\varepsilon,e\rangle\). Decidability of the group word problem does not change equality inside the published monoid \(U=\Sigma^*\times T\).

## Verification

`artifacts/verify_counterexample.py` implements the published \(K^k\) recurrence for the four vertices \(A_1,A_2,A_3,Z\), using the defining reduction \(AA'=e\) in \(T\). It also freely reduces the terminal word \(x_1x_1'\) in the free group. The recorded output in `artifacts/verification.txt` confirms simultaneously that the language word is a group identity, the label
\(\langle x_1x_1',e\rangle\) appears in \(g^4_{14}\), and the line-7 test rejects.

The script is only a compact reproduction of the four-step calculation above; the counterexample is proved directly from the definitions.

## Scope and limitations

The conclusion is about Theorem 4.3 and Algorithm 4.4 **under the published definitions**, in particular \(U=\Sigma^*\times T\) and \(1_U=\langle\varepsilon,e\rangle\). It does not show that the underlying inclusion problem is undecidable, nor does it rule out a corrected algorithm.

One conceivable modification would be to replace literal equality of the first coordinate by equality in \(G\), or to quotient that coordinate by the group congruence. Such a modification changes the algebra used in Sections 3--4 and would require a new correctness and complexity proof; no claim about that modified construction is made here.

The paper's \(O(n^3)\) statement counts operations in the abstract semiring \(S_U\), and Corollary 4.6 explicitly makes polynomial running time conditional on polynomial-time semiring operations. The present result is a correctness counterexample and does not rely on resolving that separate representation-cost question.

Originality is to the best of our knowledge. Exact-title, DOI, arXiv-identifier, theorem-number, algorithm-number, and synonymous searches located the published paper and mirrors but no erratum, correction, or prior counterexample to Theorem 4.3 or Algorithm 4.4. Informal or poorly indexed observations could nevertheless exist.

## References

1. Krasimir Yordzhev, *On A. V. Anisimov's problem for finding a polynomial algorithm checking inclusion of context-free languages in group languages*, Filomat 38:12 (2024), 4157--4166. https://doi.org/10.2298/FIL2412157Y
2. Krasimir Yordzhev, arXiv:2602.18305v1 (posted 20 February 2026). https://arxiv.org/abs/2602.18305
