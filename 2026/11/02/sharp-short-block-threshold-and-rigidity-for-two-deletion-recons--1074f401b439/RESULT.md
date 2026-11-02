# Sharp short-block threshold and rigidity for two-deletion reconstruction

## Finding
Let \(\Sigma_q\) be an alphabet with \(q\ge2\). If \(D_j(w)\) is the set of **distinct** subsequences of \(w\) obtained by deleting exactly \(j\) positions, define
\[
N_q(n,2,2)=\max_{\substack{x,y\in\Sigma_q^n\\D_1(x)\cap D_1(y)=\varnothing}}|D_2(x)\cap D_2(y)|.
\]
For all integers \(n\ge3\), the exact short-block and eventual constant profile is
\[
N_q(n,2,2)=\begin{cases}
2,&n=3,\ q=2,\\
3,&n=3,\ q\ge3,\\
4,&n=4,\ q\ge2,\\
4,&n=5,\ q=2,\\
6,&n=5,\ q\ge3,\\
6,&n\ge6,\ q\ge2.
\end{cases}
\]
**Rigidity at the first nonbinary saturation block:** for \(n=5\) and \(q\ge3\), equality with six holds for precisely the unordered center pairs
\[
\{(a,b,c,a,b),(b,a,c,b,a)\},\qquad a,b,c\in\Sigma_q\text{ pairwise distinct}.
\]
There are exactly \(q(q-1)(q-2)/2\) such unordered pairs. The sharp threshold for attaining the universal intersection ceiling is therefore five for nonbinary alphabets, versus six for binary alphabets.

## Assumptions and scope
All words have equal length \(n\), deleted positions may be arbitrary and noncontiguous, and each deletion ball counts distinct resulting subsequences rather than deletion patterns with multiplicity. The condition \(D_1(x)\cap D_1(y)=\varnothing\) means the two centers are distinguishable under one deletion. This result does not assert a corresponding classification for \(n>5\) or for higher deletion radii.

## Proof
**Universal upper bound.** The deletion-ball theorem of Sun and Ge [1], with separation index \(s=2\) and deletion radius \(t=2\), gives
\[
|D_2(x)\cap D_2(y)|\le\binom{4}{2}\binom{n-2}{0}=6
\]
for every eligible ordered pair and every alphabet.

**Exact finite classification independently of alphabet size.** The following finite classification is constructive and exhaustively reproduced by the accompanying `verify.py`. Given two length-\(n\) words, concatenate their \(2n\) coordinate symbols and rename the first appearing distinct symbol as \(0\), the second as \(1\), and so on. This gives exactly one restricted-growth string \(z=(z_0,\dots,z_{2n-1})\), specified by \(z_0=0\) and \(0\le z_i\le1+\max_{j<i}z_j\). Conversely, every such string corresponds to a pair over an alphabet of at least \(1+\max_i z_i\) symbols. Since deletion intersections depend only on equality of symbols, one representative per restricted-growth string suffices for a proof over *all* alphabet sizes.

The verifier enumerates every restricted-growth string of length \(2n\) for \(n=3,4,5\), divides it into two centers, generates every distinct one- and two-deletion descendant by all index subsets, discards the pairs with intersecting one-deletion balls, and counts the two-deletion intersection. The exhaustive totals are \(203,4{,}140,115{,}975\) equality patterns; respectively \(133,3{,}690,113{,}073\) are eligible. For the unrestricted alphabet, the maxima are respectively \(3,4,6\). Restriction to patterns containing at most two symbol classes produces maxima \(2,4,4\). These computations terminate after examining every possible equality pattern, not a random sample or truncated search.

For \(n=5\), **exactly one** canonical ordered-pair equality pattern attains six:
`(0,1,2,0,1 | 1,0,2,1,0)`.
The full eligible intersection histogram, indexed by intersection sizes \(0,1,2,3,4,5,6\), is \((87171,20663,4605,541,86,6,1)\). The unique canonical pattern has precisely three distinct symbols and is exactly the claimed template. Choosing three distinct alphabet symbols gives \(q(q-1)(q-2)\) ordered instances; swapping the two centers interchanges the first two symbols, hence dividing by two gives the unordered count. This simultaneously proves that the length-five nonbinary maximum is six and that no binary pair attains six. Independent brute-force pair enumeration for \(q=3,4,5\) finds respectively \(3,12,30\) unordered maximizers, matching the formula.

**Sharp realizations and length extension.** For \(n=3\), the binary pair \((1,0,0),(0,1,1)\) realizes two, and the ternary pair \((0,1,2),(2,1,0)\) realizes three. For \(n=4\), the binary pair \((1,0,0,1),(0,1,1,0)\) realizes four; at \(n=5\), the binary pair \((0,1,0,0,1),(0,0,1,1,0)\) realizes four. At \(n=5\), the three-symbol template realizes six. At \(n=6\), the binary pair \((1,0,0,1,1,0),(0,1,0,1,0,1)\) realizes six. The code verifies all listed pairs except the elementary length-three witnesses, which follow by direct inspection.

If \(x,y\) are eligible length-\(m\) centers, prepend the same symbol \(a\) to both. The longest-common-subsequence identity \(\operatorname{LCS}(ax,ay)=1+\operatorname{LCS}(x,y)\) preserves one-deletion distinguishability; every common two-deletion descendant \(u\) of \(x,y\) produces the distinct common descendant \(au\). Therefore any six-intersection witness extends to every greater length and reaches the universal bound. Together with the finite classification, this proves the asserted profile.

## Verification
Run `python3 verify.py` with Python 3 standard library only. The `verification_output.txt` artifact records exhaustive restricted-growth scans for lengths three through five, independent direct full-alphabet pair scans for alphabets three through five at length five, and explicit witness checks. Successful output ends with `SHARP_TWO_DELETION_RIGIDITY_VERIFY_OK`. The infinite-length upper bound uses [1] and the extension lemma; finite experiments are not substitutes for those general arguments.

## Relationship to prior work
Wang, Li and Fu [2] study nonbinary reconstruction for sufficiently large blocklength, and their asymptotic structural work features the same five-symbol alternating template for larger deletion radius; the present finite length-five, two-deletion rigidity and exact count are not asserted by their stated asymptotic theorem. Sun and Ge [1] prove the universal intersection bound six but do not give the exact short-block profile and complete five-position equality-pattern census. The binary large-block value and ternary sufficiently-long formulas are established earlier [2,3] and are not claimed as new. The contribution is the earliest saturation boundary and complete count of extremizers at that boundary, not the general upper bound or the template's appearance in other regimes.

## Limitations
The short-block extremizer uniqueness rests on a fully exhaustive, finite restricted-growth enumeration implemented in ordinary Python, rather than a short conceptual classification. Independently checking the complete algorithm is necessary for computational trust. The relationship to older unindexed sequence-reconstruction results and possible implicit specializations of general structural results remains an originality risk. No asymptotic improvement beyond the established ceiling of six is claimed. No independent scientific audit has been performed.

## References
[1] Y. Sun and G. Ge, *Extremal Deletion-Ball Intersections under Run-Count and Lower-Order Deletion-Ball Intersection Constraints*, arXiv:2606.25822, first public June 24, 2026. https://arxiv.org/abs/2606.25822

[2] X. Wang, H. Li and F.-W. Fu, *On Sequence Reconstruction Problem for q-ary Deletion Channels*, arXiv:2609.16837, first public September 15, 2026. https://arxiv.org/abs/2609.16837

[3] X. Wang, H. Li and F.-W. Fu, *Sequence Reconstruction Problem for Ternary Deletion Channels*, arXiv:2509.24237, first public September 29, 2025. https://arxiv.org/abs/2509.24237
