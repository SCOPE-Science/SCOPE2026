# A nine-symbol length-six counterexample to a partition cutoff for maximum non-overlapping codes

## Finding

Conjecture 1 of Stanovnik, Moškon and Mraz [1] asserts that for every \(q\ge2\) and \(n\ge3\), there is a **maximum** non-overlapping \(q\)-ary length-\(n\) code with a partition representation of Construction 6 for which \(R_i=\varnothing\) whenever \(i>1+n/(q+1)\). This assertion is **false** for \((q,n)=(9,6)\): every partition representation satisfying the cutoff generates at most \(33614\) words, while an explicit non-overlapping code has \(33872\) words. In particular \(S(9,6)\ge33872>33614\).

## Assumptions and scope

A length-\(n\) code \(C\subseteq\Sigma^n\) is *non-overlapping* if for all ordered pairs \(x,y\in C\), including equal pairs, no nonempty proper prefix of \(x\) equals a suffix of \(y\) of the same length. A *maximum* code has largest cardinality among all such codes; this differs from being merely inclusion-maximal.

The paper's Construction 6 starts with a nontrivial partition \(\Sigma=L_1\sqcup R_1\). For every \(2\le i<n\), partition \(P_i=\bigcup_{j=1}^{i-1}L_jR_{i-j}\) into disjoint sets \(L_i\sqcup R_i=P_i\); concatenation is meant in these products. The resulting length-\(n\) code is \(C=\bigcup_{i=1}^{n-1}L_iR_{n-i}\). The source proves this construction generates non-overlapping codes and that the product terms are disjoint [1, Construction 6 and Theorem 6]. The computational verification below also checks the defining non-overlap condition directly, without invoking those facts.

Here \(\Sigma=\{0,1,2,3,4,5,6,7,8\}\), \(q=9\), and \(n=6\). The conjectured cutoff is \(1+6/(9+1)=8/5\), so the requirement is precisely \(R_2=R_3=R_4=R_5=\varnothing\).

## Proof

**1. All restricted codes have at most \(33614\) words.** Assume the conjectured cutoff holds. Put \(a=|L_1|\), \(b=|R_1|=9-a\), with integer \(1\le a\le8\). Since all \(R_i\) for \(2\le i\le5\) vanish, the partition recurrence forces \(L_i=L_1R_1^{i-1}\) for \(2\le i\le5\). The sole surviving code term is \(C=L_5R_1=L_1R_1^5\), hence \(|C|=a(9-a)^5\). As a real function of \(a\in[1,8]\), the derivative is \((9-a)^4(9-6a)\), so it is strictly decreasing for \(a\ge2\). The only candidates for the integer maximum are \(a=1\) and \(a=2\): their values are \(32768\) and \(33614\), respectively. Thus the restricted upper bound is \(33614\), irrespective of the choice of actual symbols or the existence of other representations.

**2. An explicit admissible construction.** Set

\[
L_1=\{0,1\},\quad R_1=\{2,3,4,5,6,7,8\},\quad
R_2=\{02,03\},\quad L_2=(L_1R_1)\setminus R_2.
\]

For \(i=3,4,5\), set \(R_i=\varnothing\) and \(L_i=\bigcup_{j=1}^{i-1}L_jR_{i-j}\). Every prescribed pair is, by definition, a partition of the set required in Construction 6, so its resulting code \(C=\bigcup_{i=1}^{5}L_iR_{6-i}=L_4R_2\cup L_5R_1\) is non-overlapping [1].

To count, the construction gives \((|L_1|,|R_1|)=(2,7)\) and \((|L_2|,|R_2|)=(12,2)\). Its concatenation sets are pairwise disjoint by the partition construction [1, Theorem 6], yielding successively

\[
|L_3|=2\cdot2+12\cdot7=88,\qquad
|L_4|=12\cdot2+88\cdot7=640,\qquad
|L_5|=88\cdot2+640\cdot7=4656.
\]

Therefore

\[
|C|=640\cdot2+4656\cdot7=33872>33614.
\]

Every maximum non-overlapping code has cardinality at least \(|C|=33872\); no code meeting the conjectured cutoff can attain that cardinality. Consequently Conjecture 1 fails at \(q=9\), \(n=6\). \(\square\)

## Verification

The accompanying standalone `verify.py` constructs every set \(L_i,R_i\) as literal finite sets of integer tuples and all \(33872\) codewords. It checks the exact level cardinalities, that no proper prefix of *any* codeword equals any proper suffix of *any* codeword for each length from \(1\) through \(5\), and all eight possible restricted alphabet partitions \(a=1,\ldots,8\). Run using `python3 verify.py` without third-party dependencies. The successful result is:

```text
VERIFY_OK q=9 n=6 size=33872 L=(2, 12, 88, 640, 4656) R=(7, 2, 0, 0, 0) prefix_suffix_disjoint=yes restricted_max=33614 gap=258
```

Because this is a completely specified finite construction, exhaustive enumeration verifies the existence and properties of the witness; no numerical extrapolation is used. The general statement about all cutoff-restricted constructions follows from the algebraic argument above, not from sampling codes.

## Relationship to prior work

Stanovnik, Moškon and Mraz [1] state the universal cutoff as Conjecture 1. The partition framework, precise definition of non-overlap, and disjoint product-size formula are theirs. A later author's dissertation [2, Chapter 5, Conjecture 5.1] still prints the conjecture and describes calculations primarily for smaller alphabets. A related paper [3] considers additional balance or run-length constraints, not this nine-symbol length-six bound. The counterexample changes the cardinality consequence of the proposed cutoff, so it refutes the *existence of any maximum code* with that cutoff, rather than merely refuting optimality of a chosen restricted construction. Blackburn's distinct conjecture [1, Introduction] concerns sufficiently large alphabets and is not contradicted by a single nine-symbol example.

## Limitations

The proof does not determine the exact maximum \(S(9,6)\), classify extremizers, or identify the smallest alphabet or word length for which the cutoff fails. It does not rule out a modified cutoff or other optimality conditions. Priority may depend on equivalent unindexed constructions; no independent audit has been performed.

## References

[1] L. Stanovnik, M. Moškon, M. Mraz, *In search of maximum non-overlapping codes*, arXiv:2307.12593 (first posted 24 July 2023), revised preprint version 2 (10 January 2024); *Designs, Codes and Cryptography* **92** (2024), 1299–1326, doi:10.1007/s10623-023-01344-z. Full preprint: https://arxiv.org/html/2307.12593v2 .

[2] L. Stanovnik, *Maximal non-overlapping codes as DNA-based storage addresses*, doctoral dissertation, University of Ljubljana (2025), Chapter 5, Conjecture 5.1. Repository text: https://repozitorij.uni-lj.si/Dokument.php?id=220573 .

[3] L. Stanovnik, M. Moškon, M. Mraz, *On maximal almost balanced non-overlapping codes and non-overlapping codes with restricted run-lengths*, arXiv:2410.18458 (2024), https://arxiv.org/html/2410.18458v1 .
