# Exact isolated-gap box and digit distribution for unit-shift generalized repunit semigroups

## Finding

For arbitrary integers \(b\ge2\) and \(n\ge3\), let \(r_j=(b^j-1)/(b-1)\), put \(m=r_n\), and define the numerical semigroup
\[
S=\langle a_1,a_2,\ldots,a_n\rangle,\qquad a_i=m+r_{i-1}\quad(1\le i\le n).
\]
An *isolated gap* is an integer \(x\ge1\) satisfying \(x\notin S\) but \(x-1,x+1\in S\). All the isolated gaps, without repetition, are exactly
\[
\boxed{I(S)=\left\{(b-1)m+b+\sum_{i=3}^{n}d_i a_i:\ d_i\in\{0,1,\ldots,b-1\}\right\}.}
\]
In particular,
\[
\boxed{|I(S)|=b^{n-2},\qquad \sum_{x\in I(S)}z^{\lfloor x/m\rfloor}=z^{b-1}(1+z+\cdots+z^{b-1})^{n-2}.}
\]
The smallest isolated gap is \((b-1)m+b\); the largest is the Frobenius number
\[
\max I(S)=F(S)=\big((n-1)(b-1)+1\big)m-(n-1).
\]
The displayed formula for the Frobenius number is *previously known*; the new contribution asserted here is the exact isolated-gap set, its distinctness, its count, and its distribution among quotient strata.

## Assumptions and scope

Only the unit-shift subfamily of the generalized repunit semigroups is considered: the increment parameter is exactly one, \(b\ge2\) and the embedding dimension is \(n\ge3\). By the known minimal-generator theorem, the displayed \(n\) generators are minimal. Throughout, \(r_0=0\), \(r_1=1\), and \(r_j=1+b+\cdots+b^{j-1}\). The additive monoid \(S\subseteq\mathbb N_0\) has finite complement, since \(\gcd(m,m+1)=1\). The definition uses both nearest neighbors in \(S\), not merely isolated residues or pseudo-Frobenius gaps.

## Proof

**1. Apéry heights and canonical digits.** Branco–Colaço–Ojeda, Theorem 15, gives the Apéry set of this semigroup modulo \(m\) as all sums \(\sum_{i=2}^n u_i a_i\), where \(0\le u_i\le b\), and whenever \(u_j=b\) every earlier digit vanishes. Their canonical vectors form \(R(b,n)\). Under the unit-shift specialization, \(a_i=m+r_{i-1}\), so their residue is \(q=\sum_{i=2}^n u_i r_{i-1}\). Each canonical vector gives a *distinct* integer \(q\in\{0,\ldots,m-1\}\), as follows inductively. For \(n=2\), they are \(0,\ldots,b\). From \(r_n=br_{n-1}+1\), the canonical vectors for \(n\) consist of \(b\) consecutive translated copies of those for \(n-1\), followed by the singleton \(q=br_{n-1}=m-1\). The union covers exactly the consecutive residues \(0,\ldots,m-1\) without collisions.

Write \(L_n(q)=\sum_{i=2}^n u_i\) for the digit sum of the canonical vector representing \(q\). The unique Apéry representative in residue \(q\) is therefore
\[
w(q)=q+mL_n(q).
\]
For any \(x=km+q\), \(k\ge0\), \(0\le q<m\), the Apéry criterion yields
\[
x\in S\quad\Longleftrightarrow\quad k\ge L_n(q).
\]
The height sequence has exact recursion (concatenation of blocks)
\[
L_2=(0,1,\ldots,b),\quad
L_n=(L_{n-1},\ L_{n-1}+1,\ldots,L_{n-1}+b-1,\ b).
\]
Here adding a scalar to a block means adding it to every entry. This is a consequence of the canonical-vector recursion, not an empirical pattern.

**2. Adjacent height increments.** Every difference between adjacent entries in \(L_n\) is either \(+1\) or \(1-b\). Indeed it holds in \(L_2\). Within each translated block it holds inductively. Between blocks, the previous block ends at \(b+j\) (since each \(L_{n-1}\) ends at \(b\)), whereas the next begins at \(j+1\), giving \(1-b\). The last full block ends at \(2b-1\), followed by the singleton \(b\), again giving \(1-b\). In particular, for every \(n\ge3\), \(L_n(m-2)=2b-1\) and \(L_n(m-1)=b\).

Fix \(1\le q\le m-2\) and \(k\ge0\). The integer \(x=km+q\) is an isolated gap precisely when
\[
k<L_n(q),\quad k\ge L_n(q-1),\quad k\ge L_n(q+1).
\]
Because adjacent differences are \(+1\) or \(1-b\), these three inequalities hold precisely when \(L_n(q)-L_n(q-1)=1\) and \(L_n(q+1)-L_n(q)=1-b\), in which case the *only* allowed \(k\) is \(L_n(q)-1\). Thus the interior isolated gaps correspond bijectively to strict local peaks of the height sequence. No \(q=0\) is possible because each nonnegative multiple of \(m\) belongs to \(S\). No \(q=m-1\) is possible for \(n\ge3\): its preceding height \(2b-1\) exceeds its own height \(b\). Hence these are all isolated gaps, including boundary cases.

**3. Exact peak positions.** The base sequence \(L_2=(0,1,\ldots,b)\) has no interior peak but its final entry is a rising endpoint. Consequently the internal peaks of \(L_3\) occur exactly at residues \(q=b+jr_2\), for integers \(0\le j\le b-1\). Each such peak has height \(b+j\). Once \(n\ge3\), the last entry of \(L_n\) is preceded by a decrease, while each translated full block starts at its smallest height. Therefore the block joins create no new peaks and destroy no existing interior peaks. The peak residues of \(L_{n+1}\) are the \(b\) disjoint translates \(q+jr_n\) of those of \(L_n\), for \(0\le j\le b-1\); their heights increase by \(j\). Induction now gives exactly
\[
q=b+\sum_{i=3}^{n}d_i r_{i-1},\qquad
L_n(q)=b+\sum_{i=3}^{n}d_i,
\]
with independently chosen \(0\le d_i<b\). The recursive disjoint blocks prove distinctness. The corresponding unique isolated gap is \(x=(L_n(q)-1)m+q\), which is the displayed box formula.

**4. Count, distribution, extremes.** There are \(b^{n-2}\) distinct digit vectors. Also \(\lfloor x/m\rfloor=L_n(q)-1=(b-1)+\sum d_i\), establishing the polynomial identity by multiplication of independent digit-generating polynomials. The minimum corresponds to all zero digits. The maximum corresponds to all digits \(b-1\) and is
\[
((n-1)(b-1)+1)m-(n-1),
\]
using \(r_n=br_{n-1}+1\) and the telescoping relation \(\sum_{i=3}^n(b-1)r_{i-1}=m-b-(n-1)\). This equals the known Frobenius formula of Branco–Colaço–Ojeda specialized to unit shift, as an additional consistency check. This completes the proof. \(\square\)

## Verification

Run `python3 verify_repunit_isolated.py` from the extracted package using Python 3 standard library. The verifier independently calculates Apéry sets by Dijkstra's shortest paths on residues using the semigroup generators; it does not use the cited paper's formula to calculate these shortest paths. It compares them with the canonical heights, enumerates *all* gaps through the Frobenius number, checks both neighbors directly, compares the whole isolated-gap set with the proposed bounded box, and checks the count, extrema, and quotient-stratum polynomial. It reports `PASS: 24 complete families; 84180 gaps classified; 1533 isolated gaps; 154 strata checked` for all tested \(2\le b\le6\), \(2\le n\le6\) with \(r_n\le5000\). The test includes dimension two only as a boundary consistency check; the theorem's new domain is \(n\ge3\). Finite testing does not establish the infinite claim, which is proved above.

## Relationship to prior work

Branco–Colaço–Ojeda (2021; arXiv:2112.01106) introduced this larger family and gave canonical Apéry vectors (Theorem 15), minimal generators (Theorem 6), and a Frobenius formula (Theorem 22). These results are used and explicitly credited; the Frobenius formula is not claimed new. The present peak analysis derives a closed, non-overlapping digit box for *all isolated gaps*, not just the Apéry set or standard Frobenius/genus/type invariants. Singh–Ram (2024; arXiv:2406.09848) treats all isolated gaps in embedding dimension two, which does not cover \(n\ge3\). Smith (2022; DOI 10.3906/mat-2107-54) studies general Apéry-gap methods and embedding dimension two, with a related construction of perfect embedding-dimension-three semigroups; only its abstract and secondary discussion were available here. A search of published mathematical-result records and targeted literature did not identify the boxed formula or digit-stratum distribution, but a failed search is not a uniqueness proof.

## Limitations

The theorem concerns only the unit-shift parameter within the generalized repunit family and does not classify nonunit shifts. The dimension-two boundary is known from earlier work. The previously established Frobenius and Apéry theorems carry over unchanged and are not independently original. The exact box follows from, but is not a statement of, the cited Apéry theorem; it could have appeared implicitly elsewhere. Smith's potentially relevant full paper was inaccessible in this review, which leaves a bibliographic risk. The finite verifier is supplementary, not a substitute for the proof.

## References

1. Manuel B. Branco, Isabel Colaço and Ignacio Ojeda, *The Frobenius problem for generalized repunit numerical semigroups*, arXiv:2112.01106 (first public version 2021-12-02), especially Definition 13, Theorem 15 and Theorem 22; https://arxiv.org/html/2112.01106v2 .
2. Shubh N. Singh and Ranjan K. Ram, *On Isolated Gaps of Numerical Semigroups of embedding dimension two*, arXiv:2406.09848 (first public version 2024-06-14); https://arxiv.org/html/2406.09848v1 .
3. Harold J. Smith, *On isolated gaps in numerical semigroups*, Turkish Journal of Mathematics **46** (2022), 123–129, DOI:10.3906/mat-2107-54; https://journals.tubitak.gov.tr/math/vol46/iss1/9/ .
