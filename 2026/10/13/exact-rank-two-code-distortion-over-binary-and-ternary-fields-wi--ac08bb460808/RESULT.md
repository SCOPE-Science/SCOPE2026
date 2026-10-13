# Exact rank-two code distortion over binary and ternary fields, with a quaternary boundary

## Finding

**Theorem.** Let \(q\in\{2,3\}\), \(n\ge 2\), and let \(C,D\le\mathbb F_q^n\) be two-dimensional linear codes. Let \(a_1\le\cdots\le a_{q+1}\) and \(b_1\le\cdots\le b_{q+1}\) be their positive Hamming weights, one for each one-dimensional projective subspace of the respective code. Put \(r_i=b_i/a_i\). With code distortion defined below, one has
\[
\mathcal D(C,D)=\frac{\max_{1\le i\le q+1}r_i}{\min_{1\le i\le q+1}r_i}\le n.
\]
The formula produces an optimal linear map and gives a linear-time algorithm in the block length for either fixed field. Moreover, \(\mathcal D(C,D)=n\) holds precisely when some \(i<j\) satisfy either \(a_i=1,\ a_j=n,\ b_i=b_j\), or \(b_i=1,\ b_j=n,\ a_i=a_j\). For every \(n\ge3\) the bound \(n\) is attained over both fields. At \(n=2\) every such distortion is one.

The field restriction is essential even for the multiset formula: two length-ten dimension-two codes over \(\mathbb F_4\) can have identical projective weight multisets \(\{6,7,8,9,10\}\) but distortion exactly \(100/81>1\).

## Assumptions and scope

For two codes of the same dimension, \(\mathcal D(C,D)\) denotes the minimum, over all linear isomorphisms \(T:C\to D\), of the ratio between the largest and smallest quantities \(\mathrm{wt}(Tc)/\mathrm{wt}(c)\) for nonzero \(c\). Weight means ordinary coordinate Hamming weight, not Euclidean norm, and zero coordinate columns are allowed. The only general theorem asserted is for dimension two, finite fields of sizes two or three, and common block length \(n\ge2\). Each one-dimensional subspace contributes exactly one projective weight because a nonzero scalar leaves Hamming weight invariant.

## Proof

**The linear maps realize all matchings in the two stated fields.** A basis of each code identifies its projective lines with \(\mathbb P^1(\mathbb F_q)\), a set of \(q+1\) points. An invertible linear map acts through \(\mathrm{PGL}_2(\mathbb F_q)\), whose cardinality is \(q(q^2-1)\). The action is faithful because a projective map fixing three distinct points is the identity. For \(q=2\) and \(q=3\), this cardinality equals respectively \(3!\) and \(4!\), so all permutations of the projective lines are induced. Hence distortion minimization is a minimization over all matchings between the two projective weight multisets.

**Uncrossing proves sorted matching.** Write both weight lists in nondecreasing order. Suppose indices \(i<j\) are paired with target indices \(\ell>k\). The two crossed ratios are \(b_\ell/a_i\) and \(b_k/a_j\), ordered from larger to smaller. Their uncrossed replacements \(b_k/a_i\) and \(b_\ell/a_j\) both lie between those extremes. Replacing a crossing therefore cannot increase the global maximum of all ratios or decrease the global minimum. Repeating adjacent uncrossings yields the identity matching, proving the displayed exact formula. A projective permutation realizing it lifts to a linear isomorphism.

**The sharp universal bound and equality cases.** For \(i<j\), monotonicity gives
\[
\frac{r_j}{r_i}=\frac{b_j/b_i}{a_j/a_i}\le\frac{b_j}{b_i}\le n,\qquad
\frac{r_i}{r_j}=\frac{a_j/a_i}{b_j/b_i}\le\frac{a_j}{a_i}\le n.
\]
Every weight is between one and \(n\); applying these inequalities to indices attaining the largest and smallest ratios proves \(\mathcal D(C,D)\le n\). In the first displayed comparison, equality with \(n\) requires and is implied by \(b_i=1,b_j=n,a_i=a_j\); in the second it requires and is implied by \(a_i=1,a_j=n,b_i=b_j\). This proves the precise equality criterion without assuming either code is constant-weight.

**Realizability and sharpness.** Index the \(q+1\) projective message directions by \(L\). For each \(L\), choose a nonzero linear form \(h_L\) on \(\mathbb F_q^2\) with kernel \(L\). Construct a two-row generator matrix by including \(m_L\) copies of the column representing \(h_L\), and add zero columns until length \(n\). The message line \(L\) then has weight \(\sum_K m_K-m_L\). At least two positive multiplicities on distinct directions ensure rank two.

For \(q=2\) take source kernel multiplicities \((n-1,1,0)\) and target multiplicities \((1,1,1)\) with \(n-3\) zero columns. Their sorted projective weights are \((1,n-1,n)\) and \((2,2,2)\). For \(q=3\) use \((n-1,1,0,0)\) and \((1,1,1,0)\), again with \(n-3\) target zero columns. The sorted weights are \((1,n-1,n,n)\) and \((2,2,2,3)\). The exact formula yields distortion \(n\) in each case for every \(n\ge3\). For \(n=2\) any two-dimensional code equals \(\mathbb F_q^2\), so distortion is one.

**A quaternary obstruction.** Work over \(\mathbb F_4=\mathbb F_2[\omega]/(\omega^2+\omega+1)\). Index the five projective lines in order \(L_0,L_1,L_\omega,L_{\omega^2},L_\infty\), where \(L_t=\langle(1,t)\rangle\) and \(L_\infty=\langle(0,1)\rangle\). Use the same kernel-column construction with, respectively, multiplicities \((0,1,2,3,4)\) and \((1,0,2,3,4)\). Both resulting generator matrices have rank two, have length ten, and yield projective weights \((10,9,8,7,6)\) and \((9,10,8,7,6)\).

Now \(\mathrm{PGL}_2(\mathbb F_4)\) has order \(60\), and its action on these five points consists of even permutations. Indeed translations are double transpositions on the four finite points; nontrivial scalings act as three-cycles; and inversion \(t\mapsto1/t\) is a double transposition. These transformations generate the projective linear group by elementary fractional-linear decompositions, so it equals the alternating subgroup. The unique weight-preserving pairing of the two distinct five-element weight lists is a transposition, which is not induced by any linear map. Every other feasible matching has a ratio above one and another below one (the product of the five ratios is one). With the distinct integer weights between six and ten, any ratio above one is at least \(10/9\), and any ratio below one is at most \(9/10\); consequently distortion is at least \(100/81\). The identity matching attains this lower bound: its ratios are \((9/10,10/9,1,1,1)\). This completes the proof.

## Verification

The accompanying self-contained `verify.py` independently constructs all \(\mathrm{PGL}_2\) projective permutations and codeword weights from explicit kernel-column multiplicities. It exhaustively checks the exact formula, bound, and equality criterion over all ordered pairs of realizable ordered projective weight vectors for binary lengths two through eight and ternary lengths two through five. It separately enumerates all sixty quaternary projective transformations and confirms the exact counterexample distortion \(100/81\). Run `python3 verify.py`; success prints `VERIFY_OK`. These finite checks supplement, but do not replace, the preceding proof for all permitted lengths.

## Relationship to prior work

Bennett, Fox, and Morrell introduced the Code Distortion Problem, proved broad hardness/approximation results, and discussed a general \(n^2\) upper bound for linear transformations in their framework. The present exact rank-two result sharpens that bound in its specifically stated subcase, exploiting complete projective permutation actions for \(q=2,3\), and exhibits the first field-size boundary through \(\mathrm{PGL}_2(\mathbb F_4)\). General facts about projective linear groups and finite linear-code weight enumerators are classical; their use as lemmas does not assert those ingredients are new.

## Limitations

No claim is made for higher-dimensional codes or an exact formula over fields of order at least four. No classification of all quaternary examples is asserted. A comparable earlier finite-field/projective formulation may exist outside the inspected sources. This is a mathematical proof and accompanying finite reproducibility check, not an independently certified result.

## References

1. H. Bennett, M. Fox, and B. Morrell, *The Code Distortion Problem*, arXiv:2607.26261v1 (publicly posted 2026-07-28), https://arxiv.org/abs/2607.26261 .
2. H. Bennett, M. Fox, and B. Morrell, *The Code Distortion Problem*, APPROX/RANDOM 2026, LIPIcs 24, DOI:10.4230/LIPIcs.APPROX/RANDOM.2026.24 (2026-09-09), https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX/RANDOM.2026.24 .
