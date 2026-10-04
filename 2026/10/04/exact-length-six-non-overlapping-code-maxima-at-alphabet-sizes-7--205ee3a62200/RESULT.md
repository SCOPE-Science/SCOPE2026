# Exact length-six non-overlapping code maxima at alphabet sizes \(7,8,9\)
## Finding
For a finite alphabet of size \(q\), let \(S(q,6)\) be the largest size of a length-six non-overlapping code. Two codewords are compatible when no nonempty proper prefix of either is a suffix of the other; the definition also applies to a codeword paired with itself.

The exact values at the first three alphabet sizes beyond the published \(q\le 6\) length-six table are
\[
S(7,6)=7776,\qquad S(8,6)=16807,\qquad S(9,6)=33872.
\]
For \(q=7\) and \(q=8\), these equal the best \(k=5\) Blackburn construction \(\max_{1\le \ell<q}\ell^5(q-\ell)\). At \(q=9\), that construction has size \(33614\), so the exact optimum is larger by \(258\).

## Assumptions and scope
The alphabet is an arbitrary set with \(q\in\{7,8,9\}\) symbols, all codewords have length six, and overlap means equality between a nonempty proper prefix and a suffix. No assertion is made for \(q\ge 10\), for variable-length codes, or for the number of inequivalent maximum codes.

Write \(x_i=|L_i|\) and \(y_i=|R_i|\) in the size-partition description of non-overlapping codes. The recurrence is
\[
x_1+y_1=q,\qquad x_i+y_i=\sum_{j=1}^{i-1}x_jy_{i-j},
\]
and the code size at length six is
\[
\sum_{i=1}^5 x_i y_{6-i}.
\]
The structural reduction proved by Stanovnik, Moškon, and Mraz guarantees that some maximum code has \(x_i y_i=0\) for every \(i>3\). Thus an exact search over \(x_1,x_2,x_3\) and the two choices for the nonempty side at levels four and five is exhaustive for the optimum.

## Proof
For each \(q\in\{7,8,9\}\), enumerate \(1\le x_1<q\), set \(y_1=q-x_1\), enumerate every integer \(0\le x_2\le x_1y_1\), and set \(y_2=x_1y_1-x_2\). Next enumerate every integer
\[
0\le x_3\le x_1y_2+x_2y_1
\]
and set \(y_3=x_1y_2+x_2y_1-x_3\). Define
\[
s_4=x_1y_3+x_2y_2+x_3y_1.
\]
The reduction leaves exactly two possibilities at level four, \((x_4,y_4)=(s_4,0)\) or \((0,s_4)\). For either choice define
\[
s_5=x_1y_4+x_2y_3+x_3y_2+x_4y_1,
\]
and again choose \((x_5,y_5)=(s_5,0)\) or \((0,s_5)\). Evaluating the objective over all such states yields exactly \(66148\) reduced states across the three alphabet sizes.

The maxima are, up to exchanging all \(L\)- and \(R\)-parts,
\[
(6,0,0,0,0;1,6,36,216,1296)
\]
for \(q=7\),
\[
(7,0,0,0,0;1,7,49,343,2401)
\]
for \(q=8\), and
\[
(7,2,0,0,0;2,12,88,640,4656)
\]
for \(q=9\). Substitution into \(\sum_{i=1}^5x_i y_{6-i}\) gives \(7776\), \(16807\), and \(33872\).

These vectors are feasible size partitions. The bundled verifier constructs actual partition sets deterministically, forms the resulting code, and directly checks that the set of all proper prefixes is disjoint from the set of all proper suffixes. Hence the displayed values are attained. The structural reduction makes the reduced search an upper bound on every code, so attainment gives equality.

For \(q=9\), the best \(k=5\) Blackburn code has size
\[
\max_{1\le \ell<9} \ell^5(9-\ell)=7^5\cdot2=33614,
\]
which is \(258\) below the exact optimum.

## Verification
Run `python3 verify.py` using the bundled file. It independently enumerates every reduced size state for \(q=7,8,9\), checks the exact maxima and the complete reduced maximizing vectors, constructs one attaining code for each alphabet size, and checks proper-prefix/proper-suffix disjointness directly. The expected terminal line is:

`VERIFY_OK q=7,8,9 reduced_states=66148 direct_codewords=58455`

The exhaustive state counts are \(8872\), \(19180\), and \(38096\) for \(q=7,8,9\), respectively. Finite enumeration supplies the new parameter values; the claim that this finite search covers every global optimum uses the published structural reduction, not an empirical assumption.

## Relationship to prior work
Stanovnik, Moškon, and Mraz define the same invariant \(S(q,n)\), prove the size-partition optimization and the reduction used above, and report exact computations for \(q=2\) through length \(30\) and for \(3\le q\le6\) through length \(16\). Their published computational table therefore stops immediately before the three alphabet sizes treated here.

Blackburn introduced the general construction whose \(k=n-1\) specialization has size \(\ell^{n-1}(q-\ell)\), proved exact formulas only for lengths at most three, and conjectured eventual optimality of this construction for each fixed length as \(q\) grows. The value \(S(9,6)=33872\) is a finite exception to the \(k=5\) construction, but it does not refute that eventual conjecture.

Qin, Chen, and Luo study non-expandability and enlargements of specific cross-bifix-free construction families. Those results do not determine the unrestricted maximum \(S(q,6)\) at \(q=7,8,9\).

## Limitations
This is a finite exact extension, not an all-alphabet formula. It does not determine \(S(q,6)\) for \(q\ge10\), the number of maximum codes, or their isomorphism classes. The upper-bound argument relies on the published theorem that a maximum code has a representative with one-sided partition levels above half the word length. The bundled program verifies the finite arithmetic and explicit attaining codes but does not reprove that published structural theorem.

A residual originality risk remains that an unindexed thesis, appendix, or unpublished computation could contain one or more of these three values. Targeted searches under the non-overlapping, cross-bifix-free, and mutually uncorrelated aliases did not locate such a statement.

## References
1. L. Stanovnik, M. Moškon, and M. Mraz, “In search of maximum non-overlapping codes,” arXiv:2307.12593, first public 2023-07-24; Designs, Codes and Cryptography 92 (2024), DOI 10.1007/s10623-023-01344-z.
2. S. R. Blackburn, “Non-overlapping codes,” arXiv:1303.1026.
3. C. Qin, B. Chen, and G. Luo, “On non-expandable cross-bifix-free codes,” arXiv:2309.08915.
