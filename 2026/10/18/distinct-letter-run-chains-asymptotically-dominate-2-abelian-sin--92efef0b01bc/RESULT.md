# Distinct-letter run chains asymptotically dominate \(2\)-abelian singleton words

## Finding

Fix an alphabet \(\Sigma\) of \(q\ge4\) labeled letters. Two finite words are **\(2\)-abelian equivalent** when they have equal numbers of occurrences of every contiguous factor of length one and two. A **singleton** is a word without any other \(2\)-abelian-equivalent word. Let \(S_q(n)\) count singleton words of length \(n\) over \(\Sigma\).

Let \(B_q(n)\) be the words \(a_1^{m_1}a_2^{m_2}\cdots a_q^{m_q}\), where \((a_1,\ldots,a_q)\) is a permutation of the alphabet and all integers \(m_i\) are positive with \(\sum_i m_i=n\). Then every word in \(B_q(n)\) is a singleton, and

\[
\boxed{S_q(n)=q!\binom{n-1}{q-1}+O_q(n^{q-2})=q\,n^{q-1}+O_q(n^{q-2}).}
\]

More precisely, \(S_q(n)-|B_q(n)|=O_q(n^{q-2})\), while \(|B_q(n)|=q!\binom{n-1}{q-1}\). Hence the conditional probability that a uniformly chosen singleton belongs to \(B_q(n)\) is \(1-O_q(1/n)\). This gives the sharp leading constant and a typical-word description for every fixed alphabet size \(q\ge4\).

## Assumptions and scope

The alphabet is finite, labeled, and fixed as \(n\to\infty\); constants in \(O_q\) may depend on \(q\). A run chain uses each of the \(q\) letters in exactly one nonempty contiguous run. Factor occurrences overlap in the usual way, and words are linear rather than cyclic. The statement does not provide exact lower-order coefficients or uniform asymptotics when \(q\) grows with \(n\).

## Proof

**1. Run chains are singleton words.** For a fixed word \(w\), its directed bigram multigraph has alphabet letters as vertices and one edge per contiguous factor of length two; the initial letter is prescribed. The equivalence of words amounts to equality of this multigraph and the initial letter (the endpoint is then determined by degree balance). If \(w=a_1^{m_1}\cdots a_q^{m_q}\) has distinct \(a_i\), the graph consists of loops at vertex \(a_i\), each with multiplicity \(m_i-1\), and one nonloop edge \(a_i\to a_{i+1}\) for each \(i<q\). Every walk using every edge and starting at \(a_1\) must traverse the loops at \(a_1\) before its sole departure, then the loops at \(a_2\) before its sole departure, and so forth. Thus the edge-label word is unique; \(w\) is a singleton. There are \(q!\) orders and \(\binom{n-1}{q-1}\) positive run-length compositions for \(n\ge q\).

**2. Established singleton structure.** For fixed alphabet and factor length \(k=2\), Karhumäki--Puzynina--Rao--Whiteland, *On cardinalities of k-abelian equivalence classes*, Proposition 5.7, Corollary 5.5, and Lemma 5.10 (arXiv:1605.03319v1), give a finite set (depending only on \(q\)) of singleton decomposition types. A word of one such type comprises \(s\) long periodic runs joined by uniformly bounded pieces. The sets of letters in the primitive cyclic roots of different long runs are disjoint, and each such set is nonempty. Only the integer repetitions of the \(s\) fixed primitive roots vary. Consequently, there are \(O_q(n^{s-1})\) words of any fixed \(s\)-run type of length \(n\), including the bounded-length cases \(s\le1\). In particular, \(s\le q\).

**3. Equality at the maximum run count.** If a decomposition type has \(s=q\), its \(q\) nonempty disjoint subsets of an alphabet of size \(q\) must each be a singleton, and collectively exhaust the alphabet. A primitive cyclic root with only one letter has length one, so the long runs are \(a_i^{m_i}\) with pairwise distinct letters. Corollary 5.5 of the cited source states that every letter belonging to the cyclic root of a long run occurs nowhere outside that run. Because these \(q\) roots exhaust the alphabet, all intervening and exterior connecting pieces are empty; for \(k=2\), different such runs also cannot overlap in letters. The word therefore lies in \(B_q(n)\). The contrapositive is that every singleton outside \(B_q(n)\) admits only decompositions with \(s\le q-1\).

**4. Summation of lower-order contributions.** There are finitely many decomposition types (Lemma 5.10). Summing their \(O_q(n^{s-1})\) bounds over types with \(s\le q-1\) gives \(S_q(n)-|B_q(n)|=O_q(n^{q-2})\). The stars-and-bars formula in step 1 then yields

\[
q!\binom{n-1}{q-1}=q n^{q-1}+O_q(n^{q-2}).
\]

Finally, dividing the complement bound by \(S_q(n)\), whose leading term is positive, gives probability \(1-O_q(1/n)\). This completes the proof for every fixed \(q\ge4\).

## Verification

The accompanying standalone `verification.py` reconstructs \(2\)-abelian signatures from the first symbol and all bigram multiplicities. It enumerates all words for alphabets of sizes two through five in bounded ranges; it checks every distinct-letter run chain is a singleton, counts all singleton words, and compares the binary and ternary results with established exact published formulas. Tests at finite lengths support, but do not replace, the preceding all-length proof. Run `python3 verification.py` with a standard Python 3 interpreter.

## Relationship to prior work

Karhumäki, Puzynina, Rao, and Whiteland (2016), arXiv:1605.03319v1, prove the general upper bound \(S_q(n)=O_q(n^{q-1})\), introduce the finite-type decomposition used above, and conjecture that the exponent is sharp in all \(k\)-abelian cases (Conjecture 7.8). Their article does not give this fixed-\(k=2\) leading coefficient or the typical-word classification.

Cassaigne, Karhumäki, Puzynina, and Whiteland (2016), *k-Abelian Equivalence and Rationality*, Proposition 15, give exact formulas when \((k,q)=(2,2)\) and \((2,3)\): respectively \(2n+4\) and \(3n^2+27n-63\) for sufficiently large \(n\). Those cases already imply the same leading constants \(q\) for \(q=2,3\). They establish rationality of singleton-count generating functions generally, but do not give the all-alphabet sharp coefficient for \(q\ge4\). The present result addresses exactly that remaining parameter family, using the earlier structural lemmas as explicit premises.

## Limitations

The structural finite-type lemmas used in step 2 are previously published theorems rather than reproved here; the deduction from them is fully stated. No exact formulas for all of \(S_q(n)\), no bound uniform in growing \(q\), and no result about \(k\ge3\) are claimed. Exact asymptotic coefficients for \(q\ge4\) could conceivably have been recorded in unindexed work, so priority has not been independently certified.

## References

1. J. Karhumäki, S. Puzynina, M. Rao, M. A. Whiteland, *On cardinalities of k-abelian equivalence classes*, arXiv:1605.03319v1, first public 2016-05-11. Full text: https://arxiv.org/html/1605.03319v1 . See Proposition 5.7, Corollary 5.5, Lemma 5.10, Theorem 6.1 and Conjecture 7.8.
2. J. Cassaigne, J. Karhumäki, S. Puzynina, M. A. Whiteland, *k-Abelian Equivalence and Rationality*, DLT 2016, LNCS 9840, pp. 77--88, DOI:10.1007/978-3-662-53132-7_7. Full text: https://www.utupub.fi/server/api/core/bitstreams/6c4a5f5d-c647-410d-9a5f-bf5b229bfde6/content . See Theorem 9 and Proposition 15.
