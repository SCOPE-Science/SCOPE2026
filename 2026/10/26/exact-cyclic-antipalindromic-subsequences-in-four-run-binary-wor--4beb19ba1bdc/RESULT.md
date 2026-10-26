# Exact cyclic antipalindromic subsequences in four-run binary words

## Finding
For all positive integers \(a,b,c,d\), put \(w=0^a1^b0^c1^d\). Let \(A(w)\) be the maximum length of a scattered subsequence \(v\) of a single cyclic rotation of \(w\) satisfying \(v_i=1-v_{|v|+1-i}\) for every position \(i\). Define
\[
P=\max\{\min(a+c,b),\min(a+c,d),\min(b+d,a),\min(b+d,c)\},
\]
\[
Q=\max\{\min(a,d)+\min(b,c),\ \min(a,b)+\min(c,d)\}.
\]
Then the exact cyclic antipalindromic-subsequence length is
\[
\boxed{A(w)=2\max(P,Q)}.
\]
If the word is balanced, meaning \(a+c=b+d=s\ge2\), then
\[
\boxed{\min_{\substack{a,c,b,d\ge1\\ a+c=b+d=s}} A(0^a1^b0^c1^d)
=2\left\lceil\frac{3s}{4}\right\rceil}.
\]
Thus every balanced binary circle with exactly two runs of each letter has an antipalindromic subsequence of length at least \(3/4\) of its \(2s\) positions. For \(4\mid s\), equality \(A(w)=3s/2\) holds precisely when the cyclic run lengths, up to rotation, are \((s/4,s/2,3s/4,s/2)\). This last extremal configuration was already exhibited in earlier work; the universal matching bound, exact finite-length minimum, and general four-parameter formula are the claims here.

## Assumptions and scope
Words are indexed over \(\{0,1\}\). All four runs are nonempty. Cyclic rotation changes only the start position and retains all letters once; no letter may be reused. A subsequence is scattered, not necessarily contiguous. Antipalindromic means reverse-complement invariant (each opposed pair consists of distinct bits). It is necessarily of even length; the empty subsequence contributes length zero and cannot be maximal here. The first formula does not require equal numbers of zeros and ones. The second and the rigidity assertion do.

## Proof
**Run constraint.** A linearization obtained by cutting a four-run circle at a run boundary has four runs. Cutting inside a run splits that run between both ends, leaving five runs. Every antipalindrome has opposite first and last letters, and its maximal constant runs come in complementary, equal-length mirror pairs; hence it has an even number of runs, here at most four. There are therefore only two forms, up to bit exchange:
\[
0^t1^t\quad\text{or}\quad0^p1^q0^q1^p,
\qquad t,p,q\ge1.
\]

**Two runs.** Any two-run subsequence on a four-run circle is represented by two contiguous arcs of the cut word. If its first color draws from both available runs of that color, its second color can draw from at most one run of the opposite color before the cut; the available pair-count is bounded by one of \(\min(a+c,b),\min(a+c,d)\) or, after color exchange, \(\min(b+d,a),\min(b+d,c)\). Otherwise its first color draws from at most one original run and the second may draw from both opposite-color runs, yielding the same four bounds. Each of these possibilities is attainable by cutting at an appropriate run boundary and retaining the required numbers of letters. Hence the largest two-run antipalindrome has length exactly \(2P\).

**Four runs.** To realize four homogeneous subsequence runs, its four consecutive alternating subsequence runs must come from four successive original run blocks around the circle: skipping an intervening original run would make two consecutive selected blocks have the same color, while drawing from more than four original runs cannot create four alternating blocks in a linearization of at most five runs. If the selected original cyclic run lengths are \((a,b,c,d)\), the first and fourth block lengths must agree, as must the middle two; the optimum has length \(2[\min(a,d)+\min(b,c)]\). Starting at the next original run yields \(2[\min(a,b)+\min(c,d)]\). Reversal or further rotation repeats one of these two quantities. Cutting at the corresponding boundary and using all allowed block letters attains each. Thus the largest four-run antipalindrome has length \(2Q\), completing the exact formula.

**Balanced lower bound.** Let \(a+c=b+d=s\). The preceding formula simplifies to
\[
P=\max(a,b,c,d),\qquad
Q=\max\{s-|a+b-s|,\ s-|a-b|\}.
\]
Write \(U=\max\{|a-s/2|,|b-s/2|\}\) and \(V=\min\{|a-s/2|,|b-s/2|\}\). The elementary identity
\[
\min\{|x+y|,|x-y|\}=\big||x|-|y|\big|
\]
gives
\[
P=s/2+U,\qquad Q=s-U+V.
\]
Consequently
\[
\frac{A(w)}2=\max(s/2+U,s-U+V)
\ge\frac{(s/2+U)+(s-U+V)}2
=\frac{3s}{4}+\frac V2\ge\frac{3s}{4}.
\]
The half-length is an integer; hence \(A(w)\ge 2\lceil3s/4\rceil\).

**Exact attainment for every length.** If \(s=2\) or \(s=3\), the positive quadruple \((a,b,c,d)=(1,1,s-1,s-1)\) attains the bound. If \(s\ge4\), write \(s=4m+r\), with integers \(m\ge1\) and \(0\le r\le3\), and choose
\[
(a,b,c,d)=\big(m,\,2m+\lfloor r/2\rfloor,\,3m+r,\,2m+\lceil r/2\rceil\big).
\]
The zero and one totals are both \(s\). Direct substitution yields \(P=3m+r\) and \(Q\le3m+r\); therefore \(A=2(3m+r)=2\lceil3s/4\rceil\).

**Equality when \(4\mid s\).** Equality in the balanced bound with \(s/4\) integral requires \(V=0\) and equality of \(s/2+U\) and \(s-U+V\), hence \(U=s/4\). Therefore one of \(a,b\) equals \(s/2\) and the other is \(s/4\) or \(3s/4\). With \(c=s-a,d=s-b\), these are precisely the cyclic rotations of \((s/4,s/2,3s/4,s/2)\). Conversely these configurations attain equality by the exact formula.

## Verification
Run the standalone Python 3 file `verify.py`. It checks all \(8^4=4096\) positive quadruples with each run at most eight, comparing the closed formula against an independent interval dynamic program evaluated on every rotation. A separate bitmask enumerator tests all \(495\) four-run quadruples of total length at most twelve. Exhaustive finite balanced extrema for \(2\le s\le50\), and explicit constructions over the same range, agree with the exact bound. This computation tests examples; the proof above covers every positive quadruple and every balanced length.

## Relationship to prior work
Müllner and Ryzhikov (2019), *Palindromic Subsequences in Finite Words*, discuss antipalindromic subsequences of balanced circular binary words, motivated by the earlier Lyngsø–Pedersen necklace conjecture. The present four-run formula is a special-geometry exact resolution, not a solution of the unrestricted conjecture. Kynčl, Pach and Tóth (2004/2005) proved general estimates for separated red–blue matchings and stated a run-restricted conjecture whose two-run-per-color coefficient is \(3/4\); their Lemma 2.2 already provides the sharp example. This result adds the matching universal bound at that run count and exact counts for every set of run lengths. Csóka, Blázsik, Király and Lenger (2020) refuted the unrestricted necklace-folding lower-bound conjecture, but their high-run counterexamples do not imply or contradict this four-run theorem. A separated matching on a convex circle has a corresponding antipalindromic order of its matched endpoints, and conversely, which explains the adjacent formulations. The formula is for the subsequence/separated-matching statistic, not for longest noncrossing alternating *paths*, which have different endpoints and potential additive effects.

## Limitations
The theorem is confined to circles with exactly four nonempty monochromatic runs. It does not extend the \(3/4\) guarantee to arbitrary balanced binary circles; broader conjectures have counterexamples. The extremal example itself is prior literature. The originality assessment is based on accessible primary texts, available literature searches and database matching, not an exhaustive theorem index; an equivalent unindexed specialization remains possible. 
## References
1. C. Müllner and A. Ryzhikov, *Palindromic Subsequences in Finite Words*, arXiv:1901.07502 (first submitted 2019-01-22), https://arxiv.org/abs/1901.07502.
2. J. Kynčl, J. Pach and G. Tóth, *Long Alternating Paths in Bicolored Point Sets*, GD 2004 proceedings (LNCS 3383), pages 340–348, https://math.nyu.edu/~pach/publications/alternatingreprint.pdf; DOI: 10.1007/978-3-540-31843-9_34. See Lemma 2.2 and concluding conjecture.
3. E. Csóka, Z. L. Blázsik, Z. Király and D. Lenger, *Upper bounds for the necklace folding problems*, arXiv:2005.12603 (first submitted 2020-05-26), https://arxiv.org/abs/2005.12603.
