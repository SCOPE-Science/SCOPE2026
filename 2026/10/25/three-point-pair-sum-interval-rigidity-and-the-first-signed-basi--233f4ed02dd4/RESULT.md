# Three-point pair-sum interval rigidity and the first signed basis spectra

## Finding

Let \(A=\{a,a+x,a+x+y\}\subset\mathbb Z\) with \(a\in\mathbb Z\) and positive integer gaps \(x,y\). Let \(R(A)\) denote the largest integer \(r\ge0\) such that \(A+A\) contains an interval of \(r+1\) consecutive integers. Then the following complete classification holds:

\[
R(A)=\begin{cases}
4,&(x,y)\in\{(1,1),(1,2),(2,1)\},\\
2,&\min(x,y)=1,\ \max(x,y)\ge3,\\
1,&\min(x,y)\ge2,\ |x-y|=1,\\
0,&\text{otherwise.}
\end{cases}
\]

In particular, a three-element integer set whose two-fold sumset contains four consecutive integers must be a translate of one of \(\{0,1,2\}\), \(\{0,1,3\}\), or \(\{0,2,3\}\). Its sumset then contains five consecutive integers. No three-element set has a pair-sum interval of length exactly three.

For \(0\in A+A\), let \(\ell_2(A)=\max\{n\ge0:[0,n]\subseteq A+A\}\). The exact signed and nonnegative spectra are

\[
\{\ell_2(A):A\subset\mathbb Z,\ |A|=3,\ 0\in A+A\}=\{0,1,2,4\},
\]
\[
\{\ell_2(A):A\subset\mathbb Z_{\ge0},\ |A|=3,\ 0\in A+A\}=\{0,2,4\}.
\]

Thus allowing negative generators creates the new initial coverage length one but does not create length three. Moreover the unconstrained-interval spectrum is \(\{0,1,2,4\}\), even when \(A\) is required to be nonnegative.

## Assumptions and scope

All sets have exactly three **distinct integers**. The two-fold sumset \(A+A\) allows repetitions. The interval length is endpoint difference, so five consecutive integers have length four. A singleton is counted as an interval of length zero; thus \(R(A)=0\) when every pair sum is isolated. This convention agrees with the interval definition in Nathanson's revised version. The origin-anchored length \(\ell_2(A)\) is considered only if \(0\in A+A\); sets for which it is undefined are excluded from its spectrum. No restriction on magnitude or sign of generators is imposed in the signed theorem. The classification is pointwise for all integer triples, not merely computationally sampled triples.

## Proof

Write \(A=\{a,a+x,a+x+y\}\), where \(x,y\ge1\). Subtracting \(2a\) from the two-fold sumset gives exactly the (possibly repeated) values

\[
0,\quad x,\quad 2x,\quad x+y,\quad 2x+y,\quad 2x+2y.
\]

If \(x<y\), these are strictly increasing in the order displayed and their successive gaps are \(x,x,y-x,x,y\). If \(x>y\), their increasing order is \(0,x,x+y,2x,2x+y,2x+2y\), with successive gaps \(x,y,x-y,y,y\). If \(x=y\), the distinct sums are \(0,x,2x,3x,4x\). For \(x\ne y\), the length of a largest interval of consecutive sums equals the largest number of successive unit gaps in the appropriate list.

In the first ordering, three or more consecutive unit gaps occur only for \((x,y)=(1,2)\); in the second ordering this happens only for \((x,y)=(2,1)\); in the equality case it happens only when \(x=y=1\). The three exceptional normalized sumsets are, respectively,

\[
\{0,1,2,3,4,6\},\quad
\{0,2,3,4,5,6\},\quad
\{0,1,2,3,4\}.
\]

For a gap equal to one but no three consecutive unit gaps, inspection of the two ordered gap lists yields exactly the remaining rows of the displayed classification: minimum gap one and other gap at least three gives a longest chain of two unit gaps; if both gaps are at least two and differ by one, there is exactly one unit gap; all other cases have none. This proves the pointwise statement and that the only possible interval lengths are \(0,1,2,4\).

For the origin-anchored spectrum, \(\ell_2(A)\le R(A)\), so only length three could additionally require exclusion. In each exceptional pattern with \(R(A)=4\), the unique block of five consecutive sums starts at an **even integer**: it starts at \(2a\) for gaps \((1,1)\) or \((1,2)\) and at \(2a+2\) for gaps \((2,1)\). In the six-sum cases, the remaining point is separated from this block by an absent integer. Therefore, if \(0,1,2,3\in A+A\), these four numbers must lie in the five-term block. If that block begins at the even integer \(b\), the inequalities \(b\le0\) and \(b+4\ge3\) force \(b=0\). Hence \(4\in A+A\), and \(\ell_2(A)\ne3\).

The four signed lengths actually occur: \(A=\{0,2,4\}\) gives length zero; \(A=\{-2,-1,2\}\) gives length one; \(A=\{-1,0,1\}\) gives length two; and \(A=\{0,1,2\}\) gives length four. For nonnegative \(A\), the condition \(0\in A+A\) forces \(0\in A\). A positive covered integer one forces \(1\in A\); then \(2=1+1\) is covered, excluding length one. The examples \(\{0,2,4\}\), \(\{0,1,4\}\), and \(\{0,1,2\}\) realize lengths zero, two, and four, respectively. Finally, any integer triple can be translated into \(\mathbb Z_{\ge0}\) without changing \(R(A)\), giving the unrestricted interval spectrum for nonnegative triples as well.

## Verification

The standalone script `verify.py` implements the exact pair-sum calculation, the pointwise gap classification, and the origin-anchored witnesses. It checks all gap pairs in \([1,100]^2\) and translates the resulting sets across several negative and positive shifts; it also enumerates all three-element subsets of \([-15,15]\). Running `python3 verify.py` reports `VERIFY_OK`. These tests support transcription and boundary checking, while the preceding ordered-gap proof covers every integer triple.

## Relationship to prior work

Nathanson's *Problems in additive number theory, VII: The structure of additive \(h\)-bases for \(n\)* (arXiv:2605.26425, first public 2026-05-26) defines origin-anchored and arbitrary-interval \(h\)-basis spectra and asks for signed and interval spectra and their relationships (Problems 7--9). The full revised paper, sections 2--3, gives the two-generator case and a finite reduction for the nonnegative spectrum, but no pointwise three-generator, two-fold gap classification. In *Positivity and negativity for \(h\)-bases for \(n\)* (arXiv:2610.19470, first public 2026-10-14), van Doorn, Monticone and Nathanson prove the maximum initial coverage permitted by negative generators, including the extremal value for two summands. A maximum does not determine the attainable intermediate lengths, the impossibility of length three, or the full interval-gap table; their paper does not state these classifications. The traditional two-denomination postage-stamp range formula concerns nonnegative initial coverage and does not imply the signed interval classification. The 1989 alternative signed-coefficient postage-stamp problem permits negative *multiplicities*, rather than choosing three signed generators with exactly two summands; the models should not be conflated. General additive-combinatorial inverse methods remain relevant background, but the exact four-row gap table and the signed spectrum were not found in the checked material.

## Limitations

This is the complete first nontrivial three-generator, two-summand case. It makes no claim for four or more generators or three or more summands, where the combinatorics differ. The exhaustive program is finite and does not independently prove the universal statement. Literature searches cannot exclude an unindexed equivalent classification, and independent priority or mathematical audit has not been conducted.

## References

1. M. B. Nathanson, *Problems in additive number theory, VII: The structure of additive \(h\)-bases for \(n\)*, arXiv:2605.26425 (v1 2026-05-26; consulted v3 HTML, sections 2--3), https://arxiv.org/html/2605.26425v3.
2. W. van Doorn, P. Monticone and M. B. Nathanson, *Positivity and negativity for \(h\)-bases for \(n\)*, arXiv:2610.19470 (2026-10-14; consulted complete v1 HTML), https://arxiv.org/html/2610.19470v1.
3. *Postage Stamp Problem*, Wolfram MathWorld, description of the classical two-denomination local range and extremal range, https://mathworld.wolfram.com/PostageStampProblem.html.
4. C. Mitchell, *Another Postage Stamp Problem*, *The Computer Journal* 32 (1989), 374--376, DOI: 10.1093/comjnl/32.4.374 (abstract checked; different signed-coefficient model).
5. L. C. Palais et al., *Algorithms for the local and the global postage stamp problem*, arXiv:2601.21423 (abstract consulted; algorithmic nonnegative model).
