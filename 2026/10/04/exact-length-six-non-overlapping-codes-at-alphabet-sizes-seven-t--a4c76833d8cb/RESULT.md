# Exact length-six non-overlapping codes at alphabet sizes seven through nine

## Finding
Let \(S(q,6)\) denote the largest cardinality of a non-overlapping code in \(\Sigma^6\) over an alphabet \(\Sigma\) of size \(q\), and let \(N(q,6)\) denote the number of distinct maximum codes. Then
\[
S(7,6)=7776,\qquad N(7,6)=14,
\]
\[
S(8,6)=16807,\qquad N(8,6)=16,
\]
and
\[
S(9,6)=33872,\qquad N(9,6)=6552.
\]
For \(q=7\) and \(q=8\), every maximum code is, up to reversal, of the form \(AB^5\) with \(|A|=1\) and \(|B|=q-1\). For \(q=9\), every maximum code has, up to reversal, partition-size profile
\[
(x_1,y_1,x_2,y_2,x_3,y_3,x_4,y_4,x_5,y_5)
=(2,7,12,2,88,0,640,0,4656,0).
\]
The resulting size \(33872\) is larger by \(258\) than the best \(k=5\) Blackburn code, whose size is \(7^5\cdot2=33614\).

## Assumptions and scope
A length-six code \(C\subseteq\Sigma^6\) is non-overlapping when no nonempty proper prefix of any codeword is a suffix of any codeword. The proof uses the integer formulation SQN of Stanovnik, Moškon and Mraz. Write \(x_i=|L_i|\) and \(y_i=|R_i|\). Feasible profiles satisfy
\[
x_1+y_1=q,
\qquad
x_i+y_i=\sum_{j=1}^{i-1}x_jy_{i-j}
\quad(2\le i\le5),
\]
with \(x_1,y_1>0\) and all variables integral and nonnegative. The objective is
\[
\sum_{i=1}^5x_i y_{6-i}.
\]
For \(q\ge3\), each maximal code corresponds to a unique partition system, so optimal integer profiles can also be counted without ambiguity.

## Proof
Global reversal exchanges every \(x_i\) and \(y_i\), so it is enough to enumerate \(x_1\le y_1\). Fix \(x_1,y_1,x_2,y_2,x_3,y_3\) satisfying the recurrences, and put
\[
m_4=x_1y_3+x_2y_2+x_3y_1.
\]
Then \(y_4=m_4-x_4\). Next,
\[
m_5=x_1y_4+x_2y_3+x_3y_2+x_4y_1
\]
and \(y_5=m_5-x_5\). For fixed earlier variables, the length-six objective is affine in \(x_5\), with coefficient \(y_1-x_1\ge0\). Thus an optimum may be taken with \(x_5=m_5\). After this substitution, the objective is affine in \(x_4\), so an optimum occurs at \(x_4=0\) or \(x_4=m_4\). Consequently exhaustive exact enumeration needs only \(x_1\), \(x_2\), \(x_3\), and the two endpoints for \(x_4\); no heuristic pruning is used.

The exhaustive enumeration gives a unique reduced optimum in each of the three cases:
\[
q=7:\ (1,6,6,0,36,0,216,0,1296,0),
\]
\[
q=8:\ (1,7,7,0,49,0,343,0,2401,0),
\]
\[
q=9:\ (2,7,12,2,88,0,640,0,4656,0).
\]
For \(q=7\) and \(q=8\), the only nonzero contribution to the objective is \(x_5y_1\), giving respectively \(6^5=7776\) and \(7^5=16807\). These profiles force the code to be \(AB^5\) or its reversal.

For \(q=9\), the recurrences are
\[
x_2+y_2=14,\quad x_3+y_3=88,\quad x_4+y_4=640,\quad x_5+y_5=4656,
\]
and the optimum contributes
\[
x_4y_2+x_5y_1=640\cdot2+4656\cdot7=33872.
\]
The best \(k=5\) Blackburn size is
\[
\max_{1\le a\le8}a^5(9-a)=7^5\cdot2=33614,
\]
so the exact optimum is larger by \(258\).

For the number of maximum codes, Proposition 11 of Stanovnik–Moškon–Mraz gives, for each optimal profile, the product of binomial choices at every partition level. The \(q=7\) and \(q=8\) profiles have respectively \(7\) and \(8\) choices in one orientation and all later choices are forced; reversal doubles these counts. For \(q=9\), one orientation has
\[
\binom{9}{2}\binom{14}{12}=36\cdot91=3276
\]
codes and all later partitions are forced; reversal gives \(N(9,6)=6552\).

## Verification
The standalone verifier `artifacts/verify.py` performs the exact reduced enumeration above using only integer arithmetic. It examines \(1109\), \(2950\), and \(4762\) triples \((x_1,x_2,x_3)\) for \(q=7,8,9\), respectively, and checks both possible endpoints for \(x_4\). It reproduces all three optimum values, the unique reduced profiles, the code counts, and the Blackburn comparison; its archived output ends in `VERIFY_OK`.

As a separate implementation check, the public `compute_sqn.c` solver accompanying Stanovnik–Moškon–Mraz reproduces the same three optimum values and the same reduced profiles. This second computation is corroborative; the proof of exhaustiveness is the explicit finite reduction above.

## Relationship to prior work
Chee, Kiah, Purkayastha and Wang (2012 preprint) and Blackburn (2013 preprint) developed general constructions and bounds for cross-bifix-free/non-overlapping codes. Blackburn's construction is optimal when the code length divides the alphabet size and supplies the \(k=5\) benchmark used above.

Stanovnik, Moškon and Mraz formulated the exact SQN optimization and proved that it captures maximum non-overlapping codes. Their published exact computations cover \(5\le n\le16\) for \(3\le q\le6\), with Table 1 restricted to \(2\le q\le6\). Thus \(q=7,8,9\) at length six are the first three alphabet sizes immediately beyond that published table. Their general public solver applies to these cases, but the inspected article and its displayed exact tables do not state the three values or the \(q=9\) structural transition reported here.

Targeted semantic searches in published-finding corpus for length-six non-overlapping codes, \(S(9,6)\), cross-bifix-free aliases, and the Blackburn construction returned exact length-five records as the closest matches, not the present length-six statement.

## Limitations
The result is an exact finite classification only for \(q\in\{7,8,9\}\) and length six. It does not give a formula for larger alphabets or other lengths. The originality check cannot exclude an obscure unindexed computation or unpublished run of the general solver. The public 2024 algorithm makes these instances computable, so the scientific value here is the exact frontier extension together with the complete maximum-code counts and the explicit \(q=9\) failure of the simple \(k=5\) extremal form, not a new general optimization framework.

## References
1. Y. M. Chee, H. M. Kiah, P. Purkayastha, C. Wang, “Cross-Bifix-Free Codes Within a Constant Factor of Optimality,” arXiv:1209.0236v1, 2012.
2. S. R. Blackburn, “Non-overlapping codes,” arXiv:1303.1026v1, 2013; IEEE Transactions on Information Theory 61(9), 2015.
3. L. Stanovnik, M. Moškon, M. Mraz, “In search of maximum non-overlapping codes,” arXiv:2307.12593v1; Designs, Codes and Cryptography 92, 1299–1326 (2024), DOI:10.1007/s10623-023-01344-z.
4. Public companion code for reference implementation: `magdevska/nono-codes`, file `compute_sqn.c`.
