# Exact reflection spectrum and a sharp reversal barrier for a ternary morphic word

## Finding
Let \(h\) be the nonerasing substitution \(h(0)=01\), \(h(1)=21\), and \(h(2)=0\). Its prolongable fixed point is \(\mathbf p=h^{\omega}(0)=012102101021\cdots\). For every integer \(n\geq 0\), let \(r_{\mathbf p}(n)\) count length-\(n\) factors of \(\mathbf p\) modulo reversal, with the empty factor counted once. Then
\[
r_{\mathbf p}(0)=1,\qquad
(r_{\mathbf p}(1),\ldots,r_{\mathbf p}(7))=(3,3,6,7,10,12,15),
\qquad r_{\mathbf p}(n)=2n+1\quad(n\geq8).
\]
In particular, **length seven is the maximum length of a factor that occurs together with its reversal**, and this threshold is sharp: the palindrome `1012101` occurs. For \(n\geq8\), no length-\(n\) factor appears together with its reversal (not even as a palindrome).

The result follows from a stronger local obstruction. Every ternary word avoiding the seven factors

`00`, `11`, `22`, `20`, `212`, `0101`, `121012`

has the property that none of its length-eight factors can have its reversal in the *same seven-pattern-avoiding language*. More precisely, let \(T_n\) be the set of length-\(n\) ternary words \(u\) such that both \(u\) and its reversal avoid these seven patterns. The complete sets for \(1\leq n\leq7\) are:

| \(n\) | \(T_n\), with elements written as literal words |
|---|---|
| 1 | `0`, `1`, `2` |
| 2 | `01`, `10`, `12`, `21` |
| 3 | `010`, `012`, `101`, `121`, `210` |
| 4 | `0121`, `1012`, `1210`, `2101` |
| 5 | `01210`, `10121`, `12101`, `21012` |
| 6 | `012101`, `101210` |
| 7 | `1012101` |

At \(n=8\), the set \(T_8\) is empty. The displayed sets are also *exactly* the factors of \(\mathbf p\) that have a reversal occurring in \(\mathbf p\).

## Assumptions and scope
All words are over the fixed labeled alphabet \(\{0,1,2\}\). Factors are contiguous; reversal preserves the individual symbols and reverses their order, without a letter permutation. A factor \(u\) is called reflected if \(u^{\mathrm R}\) is also a factor, and a palindrome counts as reflected. The theorem concerns the one-sided infinite fixed point of the stated substitution, not arbitrary ternary words. The seven-pattern obstruction applies to *any* ternary word or factor language avoiding that set, not only to the fixed point.

## Proof
**Step 1: A universal, finite obstruction.** Let \(F=\{00,11,22,20,212,0101,121012\}\). For a fixed length \(n\), enumerate all \(3^n\) ternary words \(u\), testing whether each of the seven literal patterns occurs in either \(u\) or \(u^{\mathrm R}\). Exactly the surviving words listed in the Finding occur at lengths \(1\) through \(7\); none survives at length \(8\). This is a complete finite calculation, not a sample: the attached independent verifier explicitly visits all \(\sum_{n=1}^{8}3^n=9840\) candidates, checks both orientations of all seven patterns, and compares the outputs with the above full lists. The terminal length-eight check is alternatively a finite-state obstruction: extending any eligible length-seven word by a symbol would yield an eligible length-eight word, and the exhaustive length-eight test excludes all extensions. Thus any longer factor likewise cannot have a reversal that also avoids \(F\), because one of its length-eight subfactors would then contradict the calculation.

**Step 2: Transfer to the fixed point.** Currie, Ochem, Rampersad and Shallit [1, Theorem 14] prove that \(\mathbf p\) avoids a ten-element forbidden set containing every pattern in \(F\). Hence each length-\(n\) factor of \(\mathbf p\) whose reversal is also a factor must belong to \(T_n\). Conversely, the explicit length-65 prefix \(h^7(0)\) contains every displayed member of \(T_n\), for \(1\leq n\leq7\), as well as its reversal. It is a prefix because \(h(0)\) begins with \(0\), and direct morphism iteration verifies both its length and all these inclusions. Thus the displayed \(T_n\) are exactly the reflected factors in the infinite fixed point through length seven. At greater lengths, there are none by Step 1. The occurring palindrome `1012101` witnesses the sharpness of seven.

**Step 3: Count reversal classes.** Let \(\rho_{\mathbf p}(n)\) be the ordinary factor complexity. Currie et al. [1, Theorem 1] prove \(\rho_{\mathbf p}(n)=2n+1\) for every \(n\geq1\). If \(b_n\) is the number of *nonpalindromic* reflected factors, then they form disjoint pairs, and therefore \(r_{\mathbf p}(n)=\rho_{\mathbf p}(n)-b_n/2\). From the explicit \(T_n\), the sequence \((b_1,\ldots,b_7)\) is \((0,4,2,4,2,2,0)\), and \(b_n=0\) for \(n\geq8\). Substitution gives the claimed formula. The empty factor is one reversal class by definition.

## Verification
Run `python3 verify.py` using the Python standard library. The checker independently enumerates all ternary words at lengths one through eight (9,840 total), screens both orientations for the seven forbidden patterns, and compares each entire surviving set with the displayed table. It also constructs \(h^7(0)\), verifies every listed reflected word occurs in that length-65 prefix, checks the short ordinary-factor counts, and performs a longer-prefix cross-check through length 24. The infinite conclusion does **not** follow from extrapolating the longer-prefix experiment: it follows from [1, Theorems 1 and 14] plus the exhaustive length-eight obstruction.

## Relationship to prior work
The substitution, the all-length factor-complexity formula, and the underlying ten forbidden patterns were established by Currie, Ochem, Rampersad and Shallit [1]. The reflection-complexity invariant and the qualitative theorem that a uniformly recurrent, non-reversal-closed sequence eventually has no reflected factors were established by Allouche, Campbell, Li, Shallit and Stipulanti [2, Definitions 1–3 and Theorem 11]. That qualitative theorem does **not** give the least cutoff or the preceding reflection counts for this particular sequence. The present contribution is the exact sharp cutoff \(8\), the complete short reflection-orbit classification, and the resulting exact reflection-complexity function. Earlier work by Cassaigne, Labbé and Leroy [3] establishes a related family of ternary words of factor complexity \(2n+1\), but not this reflection classification.

## Limitations
This is an exact result for one fixed nonuniform ternary substitution and one explicit seven-pattern avoidance condition; it is not a classification for all substitutions or all complexity-\(2n+1\) languages. It depends on the published proofs of the factor-complexity and avoidance properties of this infinite word. Its finite pattern calculation is fully reproducible, but the code itself is not an independent proof of those two previously published infinite properties. An equivalent explicit reflection classification in as-yet-unidentified literature remains possible.

## References
[1] J. Currie, P. Ochem, N. Rampersad and J. Shallit, *Properties of a Ternary Infinite Word*, arXiv:2206.01776v1 (first submitted 2022-06-03), especially Theorems 1 and 14. https://arxiv.org/abs/2206.01776

[2] J.-P. Allouche, J. M. Campbell, S. Li, J. Shallit and M. Stipulanti, *The reflection complexity of sequences over finite alphabets*, arXiv:2406.09302 (first submitted 2024-06-13), especially Definition 3 and Theorem 11. https://arxiv.org/abs/2406.09302

[3] J. Cassaigne, S. Labbé and J. Leroy, *A Set of Sequences of Complexity \(2n+1\)*, arXiv:1707.02741v1 (2017-07-10). https://arxiv.org/abs/1707.02741
