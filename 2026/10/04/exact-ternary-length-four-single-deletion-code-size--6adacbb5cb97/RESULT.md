# Exact ternary length-four single-deletion code size

## Finding

Let \(B_3=\{0,1,2\}\). For \(x\in B_3^4\), let \(D_1(x)\subseteq B_3^3\) be the set of distinct words obtained by deleting one coordinate of \(x\). A code \(C\subseteq B_3^4\) corrects one deletion when \(D_1(x)\cap D_1(y)=\varnothing\) for every two distinct \(x,y\in C\).

With
\[
N(4,3,1)=\max\{|C|:C\subseteq B_3^4\text{ corrects one deletion}\},
\]
the exact value is
\[
N(4,3,1)=11.
\]

One optimal code is
```text
0000 0011 0022 0120 1100 1111 1122 2102 2200 2211 2222
```

## Assumptions and scope

The alphabet is the ordered ternary alphabet \(B_3\), although the optimum is invariant under relabeling symbols. The channel deletes exactly one coordinate; repeated deletion outputs from the same codeword are counted only once. The claim concerns unrestricted, not necessarily linear or Tenengolts, codes of fixed length four.

The proof uses the substitution normalization and deletion-type count of Kim, Lee, and Oh. Their argument applies to every length-four one-deletion-correcting code up to cardinality-preserving substitutions; the final even-alphabet simplification is not used here.

## Proof

The displayed 11-word code gives the lower bound. Its deletion shadows are
```text
0000 : 000
0011 : 001 011
0022 : 002 022
0120 : 010 012 020 120
1100 : 100 110
1111 : 111
1122 : 112 122
2102 : 102 202 210 212
2200 : 200 220
2211 : 211 221
2222 : 222
```
and these sets are pairwise disjoint.

For the upper bound, apply the Kim–Lee–Oh substitution lemma and their normalized word-type classification. Write \(C_{3,1}\) and \(C_{4,2}\) for their corresponding normalized classes. Their deletion-output count gives, before the final parity specialization,
\[
|C|
\le |U|+\frac12|V|+\frac14|Z|
+\frac12|C_{4,2}|-\frac14|C_{3,1}|.
\]
For \(q=3\),
\[
|U|=3,\qquad |V|=12,\qquad |Z|=6.
\]
A word in \(C_{4,2}\) has type \((a,b,c,a)\) with \(a,b,c\) distinct. For fixed \(a\), two such words cannot coexist unless their unordered middle-symbol pairs are disjoint. With only two symbols other than \(a\), this gives
\[
|C_{4,2}|\le 3.
\]
Consequently
\[
|C|\le 3+6+\frac64+\frac32=12.
\]

Suppose equality \( |C|=12 \) held. Then every inequality above would be tight, so in particular \( |C_{4,2}|=3 \). There must therefore be exactly one \(C_{4,2}\) word for each repeated outer symbol \(a\in\{0,1,2\}\). For each \(a\) there are only two possibilities. Their all-distinct deletion outputs are:
\[
\begin{array}{c|c}
\text{word}&\text{all-distinct deletion outputs}\\ \hline
0120&\{012,120\}\\
0210&\{021,210\}\\
1021&\{021,102\}\\
1201&\{120,201\}\\
2012&\{012,201\}\\
2102&\{102,210\}.
\end{array}
\]
Selecting one row for each outer symbol \(a=0,1,2\) can never give three pairwise disjoint output pairs. Indeed, choosing \(0120\) forces \(1021\) for outer symbol \(1\), after which both choices for outer symbol \(2\) collide; choosing \(0210\) forces \(1201\), after which both choices for outer symbol \(2\) collide. Thus a size-12 code is impossible, and \(N(4,3,1)\le 11\). Together with the displayed code, this proves the claim.

## Verification

`artifacts/verify.py` independently constructs all \(3^4=81\) length-four words and their distinct one-deletion shadows. It verifies the displayed 11-word code, solves the complete finite compatibility graph by an exact maximum-clique search with a coloring bound, and obtains optimum 11. It also checks all \(2^3=8\) equality-case choices of the three possible \(C_{4,2}\) outer symbols and finds no collision-free triple.

The recorded run is:
```text
VERIFY_OK q=3 n=4 optimum=11 words=81 witness_size=11 equality_triples=8 feasible_c42_triples=0 search_nodes=271
```

The finite search is an independent check of this finite parameter. The mathematical upper bound above does not rely on a timeout, numerical optimizer, or unverified solver certificate.

## Relationship to prior work

Kim, Lee, and Oh derive a sharp length-four bound for even alphabet size and explicitly note that their corresponding odd-alphabet bound is not sharp and that obtaining a sharp odd-alphabet bound is difficult. Their normalized deletion-type count is the structural input used above.

Kulkarni and Kiyavash tabulate the exact parameter \(q=3,n=4\). Their numerical fractional-matching upper bound is 12 and the listed Tenengolts-family lower bound is 8; they do not state the integer optimum 11.

Li and Houghten study ternary Tenengolts codes computationally. Their full text lists all ternary Tenengolts-code sizes at length four, with maximum size 8 in that family, and develops extensions of those codes. It does not state a global optimum for unrestricted ternary length-four codes.

A later published published-finding corpus record settles the adjacent quinary parameter \(N(4,5,1)=42\); that statement neither contains nor implies the ternary value. Searches under the exact notation, ternary single-deletion terminology, insertion-deletion metric terminology, and odd-alphabet length-four formulations did not identify a published statement equivalent to \(N(4,3,1)=11\).

## Limitations

The theorem is a single exact small-parameter result, not a formula for all odd alphabet sizes. The proof depends on the published substitution normalization and deletion-type accounting, though the complete \(81\)-word instance is independently replayed by the bundled verifier.

A 2011 master's thesis on ternary one-deletion-correcting codes is highly relevant. Indexed passages and the subsequent 2012 full paper were inspected, but a complete machine-readable inspection of the thesis was not available in this run. This leaves a specific residual priority risk for an unindexed statement in that thesis, rather than a mathematical correctness gap.

## References

1. H. K. Kim, J. Y. Lee, and D. Y. Oh, “Optimal codes in deletion and insertion metric,” arXiv:0810.3729v1, first posted 2008-10-21. A later full version is “Construction of optimal codes in deletion and insertion metric,” arXiv:1003.4057v1, 2010-03-22.
2. A. A. Kulkarni and N. Kiyavash, “Non-asymptotic Upper Bounds for Deletion Correcting Codes,” arXiv:1211.3128v1, 2012-11-13; later IEEE Transactions on Information Theory 59(8), 2013.
3. Z. Li and S. K. Houghten, “Searching for Optimal Deletion Correcting Codes: New Properties and Extensions of Tenengolts Codes,” CIT 2012, DOI 10.1109/CIT.2012.137.
4. Z. Li, “Construction of 1-Deletion-Correcting Ternary Codes,” M.Sc. thesis, Brock University, 2011.
