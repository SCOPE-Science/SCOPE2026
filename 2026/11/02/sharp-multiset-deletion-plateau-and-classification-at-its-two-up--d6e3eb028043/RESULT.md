# Sharp multiset-deletion plateau and classification at its two upper endpoints

## Finding

Fix integers \(q\ge3\) and \(k\ge4\), put \(h=k-1\) and \(T=\lfloor(q+1)h/2\rfloor\). For all integers \(n\ge k\) with \(n>T\), the largest length-\(n\), \(q\)-ary multiset code correcting \(n-k\) deletions has size

\[
S_q(n,n-k)=\begin{cases}q+1,&T<n\le qh,\\ q,&n>qh.\end{cases}
\]

The first threshold cannot be decreased: at \(n=T\), there is a correcting code with \(q+2\) codewords. At \(n=qh\), the unique maximum code consists of the \(q\) pure multiplicity vectors \(n e_i\) together with \((h,\ldots,h)\). At \(n=qh-1\), there are exactly \(q^2\) maximum codebooks on a fixed labeled alphabet, explicitly classified in the proof.

## Assumptions and scope

The alphabet has \(q\) distinguishable symbols. A length-\(n\) multiset is its multiplicity vector \(x\in\mathbb Z_{\ge0}^q\), with \(\sum_i x_i=n\). Its intersection size with \(y\) is

\[
I(x,y)=\sum_{i=1}^q\min(x_i,y_i).
\]

Deleting exactly \(n-k\) symbols leaves a multiset of length \(k\). Two codewords have a common possible output if and only if \(I(x,y)\ge k\). Thus a correcting code is exactly a subset of the integer simplex with \(I(x,y)\le h\) for all distinct members. The stated value concerns exact cardinality and, at the two upper endpoints, all labeled optimum codebooks; it is not a claim about ordinary ordered-string deletion channels.

## Proof

**Heavy symbols and light codewords.** Call coordinate \(i\) heavy in \(x\) when \(x_i\ge k=h+1\). A codeword with no heavy coordinate is *light*, with \(x_i\le h\) in each coordinate. A given coordinate cannot be heavy in two different codewords, since their intersection would then be at least \(k\). Therefore at most \(q\) codewords have any heavy coordinate: assign each one of its heavy coordinates, which must be distinct across codewords.

For two light words \(x,y\) of length \(n\),

\[
I(x,y)=2n-\sum_i\max(x_i,y_i)\ge 2n-qh.
\]

If \(n>T\), then \(2n>(q+1)h\), hence \(I(x,y)>h\). There can be at most one light word. Thus \(S_q(n,n-k)\le q+1\). Moreover, a light word needs \(n\le qh\). For \(n>qh\), no light word exists, and the upper bound strengthens to \(q\).

**Attainment.** For every \(n\ge k\), the \(q\) pure words \(n e_i\) have mutual intersection zero. When \(n\le qh\), a light vector of total weight \(n\) exists, and its intersection with every pure word is at most \(h\). Adding it yields \(q+1\) words, completing the two exact-size formulas.

**Sharp lower threshold.** At \(n=T\), we construct two different light words with mutual intersection at most \(h\), then adjoin the \(q\) pure words. If \(q=2r+1\), take \(x=h\sum_{i=1}^{r+1}e_i\) and \(y=h(e_1+\sum_{i=r+2}^{2r+1}e_i)\); each has weight \((r+1)h=T\), and \(I(x,y)=h\). If \(q=2r\), set \(s=\lfloor h/2\rfloor\) and take

\[
x=h\sum_{i=1}^{r}e_i+s e_{r+1},\qquad
 y=h\sum_{i=r+1}^{2r}e_i+s e_1.
\]

Their common weight is \(rh+s=T\), and \(I(x,y)=2s\le h\). In both cases all intersections with pure words are at most \(h\), furnishing \(q+2\) codewords.

**Classification at \(n=qh\).** Every code of size \(q+1\) has exactly one light word and exactly \(q\) heavy words with pairwise distinct heavy coordinates. At this length, the light word must be \(w=(h,\ldots,h)\). If \(x\) has heavy coordinate \(i\), then \(I(x,w)\ge h\) from coordinate \(i\) alone. All other coordinates of \(w\) are positive, so compatibility forces \(x_j=0\) for \(j\ne i\). Consequently \(x=ne_i\), proving the unique labeled maximizer.

**Classification at \(n=qh-1\).** Again every size-\(q+1\) code has exactly one light word and one heavy word for each coordinate. The only possible light words have one coordinate \(i\) equal to \(h-1\), all others equal to \(h\). For a heavy word \(x\) whose heavy coordinate is \(j\ne i\), intersection at coordinate \(j\) already equals \(h\). As all other light coordinates are positive, compatibility implies \(x=ne_j\). For the heavy word of coordinate \(i\), the light intersection already contributes \(h-1\). Hence at most one symbol may lie outside \(i\), and the word is either \(ne_i\) or \((n-1)e_i+e_j\) for one \(j\ne i\). Every one of these choices is compatible with the \(q-1\) pure words and the light word. There are \(q\) choices of deficit coordinate and \(q\) choices of the final heavy word, giving precisely \(q^2\) distinct labeled maximum codebooks. The restriction \(q\ge3,k\ge4\) guarantees \(qh-1>T\) and positivity of the light entries throughout. □

## Verification

Run \(`python3 verify.py`\) with Python 3.9 or later (no dependencies). It independently enumerates all multiplicity vectors and fixed-size compatible cliques in ten finite instances, checks the sharp-threshold constructions for six parameter pairs, and checks every claimed upper-endpoint codebook in those instances. See \(`verification_output.txt`\) for exact counts. These finite computations are cross-checks; the inequalities and classifications for arbitrary \(q,k,n\) follow from the proof above.

## Relationship to prior work

Kreindel, Essayag, and Zabokritskiy develop the multiset-deletion model and derive exact statements for one or two surviving symbols, bounds for three survivors, and general constructions. Their January 2026 version and July 2026 revision do not state the simultaneous \(q,k\ge4\) sharp plateau and its two endpoint codebook classifications in the inspected high-deletion sections. Earlier work by Kovačević and Tan develops the discrete-simplex coding framework and broad code bounds. An existing exact three-survivor result is a narrower predecessor; the claim here is deliberately restricted to \(k\ge4\), with a new exact transition and two structural classifications.

## Limitations

The theorem does not determine the optimum for \(n\le T\), except for its lower-bound construction at \(n=T\). It does not enumerate all maximizers at interior lengths \(T<n<qh-1\), characterize unordered-alphabet equivalence classes, or extend to ordered sequence deletion channels. A prior equivalent formulation in literature not indexed or inspected remains a publication-priority risk. No independent external validation is claimed.

## References

1. A. Kreindel, I. B. Essayag, and A. L. Zabokritskiy, *Multiset Deletion-Correcting Codes: Bounds and Constructions*, arXiv:2601.05636v1 (first public 2026-01-09), https://arxiv.org/html/2601.05636v1.
2. A. Kreindel, I. B. Essayag, and A. L. Zabokritskiy, *Multiset Deletion Codes: Cyclic Constructions, Bounds, and Exact Results*, arXiv:2601.05636v2 (2026-07-13 revision), https://arxiv.org/html/2601.05636v2.
3. M. Kovačević and V. Y. F. Tan, *Codes in the Space of Multisets—Coding for Permutation Channels With Impairments*, IEEE Transactions on Information Theory (2018), DOI:10.1109/TIT.2017.2789292.
4. A. Kreindel, I. B. Essayag, and A. L. Zabokritskiy, *Polynomial Constructions and Deletion-Ball Geometry for Multiset Deletion Codes*, arXiv:2603.18322 (2026).
