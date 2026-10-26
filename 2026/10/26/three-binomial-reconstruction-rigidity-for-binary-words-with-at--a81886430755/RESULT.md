# Three-binomial reconstruction rigidity for binary words with at most four runs

## Finding

For a finite binary word \(w\) and a binary pattern \(x\), let \(N_x(w)\) denote the number of increasing tuples of positions in \(w\) spelling \(x\). Write \(u\equiv_3v\) when \(N_x(u)=N_x(v)\) for every binary pattern \(x\) of length one, two, or three. A run means a maximal nonempty interval of identical symbols.

**Four-run rigidity.** For any nonempty binary words \(u,v\) with at most four runs,
\[
u\equiv_3v\quad\Longrightarrow\quad u=v\ \text{or}\ u=v^{\mathrm{rev}}.
\]
Every distinct pair is a four-run reversal pair. Up to exchanging zero and one, all such pairs are
\[
0^a1^b0^c1^d\quad\text{and}\quad1^d0^c1^b0^a
\]
with positive integer parameters satisfying
\[
2bc=(a+c)(b+d),\quad\text{equivalently}\quad b(c-a)=d(a+c).
\]
Necessarily \(c>a\). Conversely, every such parameter choice gives a distinct pair with equal decks. A nonredundant parametrization fixes \(a<c\), writes \(g=\gcd(c-a,c+a)\), and takes
\[
b=\frac{a+c}{g}t,\qquad d=\frac{c-a}{g}t,\qquad t\ge1.
\]
All pairs after swapping binary symbols are also included.

**Sharp boundary.** The words `00110001` (four runs) and `01000110` (five runs) share the full fourteen-entry deck but are not reversals. No binary words shorter than eight have a non-reversal collision. Thus four is the maximum guaranteed reconstruction run bound, and length eight is the global earliest non-reversal ambiguity.

## Assumptions and scope

All words are finite, nonempty, over the ordered alphabet \(\{0,1\}\). Subsequence occurrences distinguish index choices, including repeated patterns; they are not contiguous-factor sets or their multiplicities. Reversal \(w^{\mathrm{rev}}\) reverses symbol order without complementing the symbols. The uniqueness conclusion applies when **both** compared words have at most four constant runs; it does not say that a four-run word cannot share its deck with an unrestricted word.

For lengths at least three, the usual length-three deck already determines the shorter decks: if \(y\) is a pattern of length \(j<3\), then
\[
\sum_{|x|=3}N_x(w)N_y(x)=\binom{|w|-j}{3-j}N_y(w).
\]
The word length itself follows from the sum of the length-three deck entries. We use the length-at-most-three version to cover all shorter words without qualification.

## Proof

### 1. Recognizing the run count

If a word has at most four runs, it has both subsequences \(010\) and \(101\) exactly when it has four runs. It has exactly one of them when it has three runs, and neither when it has at most two runs. Indeed, each pattern requires three alternating maximal blocks; four blocks of either alternating orientation contain both. Consequently the deck identifies the run count and, in the three-run case, the orientation.

Words with at most two runs are reconstructed from the one-letter counts and the ordered-pair counts: a word of form \(0^a1^b\) has \(N_{01}=ab>0\) and \(N_{10}=0\), while its reverse has the opposite pair counts. Constant words are fixed by their single-letter counts. For three runs, if \(w=0^a1^b0^c\), then \(N_1=b\), \(N_{01}=ab\), and \(N_{10}=bc\), which reconstruct \(a,b,c\); the complemented case is symmetric. Thus no nontrivial same-deck pairs occur in up-to-three-run words or between these and four-run words.

### 2. Same-orientation four-run reconstruction

For \(w=0^a1^b0^c1^d\), write \(Z=a+c\), \(O=b+d\), and \(P=N_{10}(w)\). Direct counting gives
\[
P=bc,\qquad N_{010}(w)=aP,\qquad N_{101}(w)=dP.
\]
Since \(P>0\), the deck recovers \(a=N_{010}/P\), \(d=N_{101}/P\), then \(c=Z-a\), \(b=O-d\). The same method after swapping symbols reconstructs four-run words starting in one. Thus deck collisions among four-run words of the same initial symbol are equality alone.

### 3. Opposite-orientation rigidity

Let \(u=0^a1^b0^c1^d\) and \(v=1^A0^B1^C0^D\) be equivalent. Their common letter totals are \(Z\) and \(O\). Put \(P=bc=N_{10}(u)>0\) and \(Q=BC=N_{01}(v)>0\). Since \(N_{01}+N_{10}=ZO\), equality of the decks gives \(P+Q=ZO\). Comparing the two alternating three-letter counts gives
\[
aP=DQ,\qquad dP=AQ.
\]
With \(\rho=P/Q>0\), we have
\[
A=\rho d,\quad D=\rho a,\quad B=Z-\rho a,\quad C=O-\rho d.
\]
From the definitions,
\[
Zd+Oa=Q+ad.
\]
Consequently, using \(P+Q=ZO\) and \(P=\rho Q\),
\[
Q=BC=(Z-\rho a)(O-\rho d)=Q+\rho(\rho-1)ad.
\]
Positive \(a,d,\rho\) force \(\rho=1\), hence \((A,B,C,D)=(d,c,b,a)\): \(v=u^{\mathrm{rev}}\).

### 4. Exactly when reversal preserves the three-deck

Every binary word satisfies \(N_{01}+N_{10}=ZO\), and reversal exchanges these two counts. The patterns \(000\), \(010\), \(101\), and \(111\) are palindromes, so their three-letter counts are invariant under reversal. The remaining triple differences obey the universal identities
\[
2(N_{001}-N_{100})=(Z-1)(N_{01}-N_{10}),
\]
\[
2(N_{011}-N_{110})=(O-1)(N_{01}-N_{10}).
\]
To establish the first identity, sum over each occurrence of \(1\): if \(i\) zeros precede it and \(Z-i\) follow it, its contribution to \(N_{001}-N_{100}\) is \(\binom i2-\binom{Z-i}2\). Summing and using \(\sum i=N_{01}\) gives the stated equality. The other identity follows symmetrically by summing over positions carrying \(0\).

Thus equality of the pair counts \(N_{01}=N_{10}\) is necessary and sufficient for full length-at-most-three equality between a word and its reversal. For the four-run word above, \(N_{10}=bc\) and \(N_{01}=ZO-bc\), so the equality is equivalent to \(2bc=(a+c)(b+d)\), or \(b(c-a)=d(a+c)\). Positive \(b,d,a,c\) imply \(c>a\). Coprimality of \((c-a)/g\) and \((c+a)/g\) establishes the displayed integer parametrization.

### 5. Sharpness at five runs and earliest length

Independent index-subsequence enumeration gives identical fourteen counts for `00110001` and `01000110`, in the binary-pattern order \(0,1,00,01,10,11,000,001,010,011,100,101,110,111\):
\[
(5,3,10,9,6,3,10,12,12,6,6,6,3,1).
\]
They have four and five runs respectively, and neither is the reversal of the other. To establish the separate finite claim that eight is the shortest global non-reversal collision, the attached standalone verifier exhaustively lists all \(2^n\) binary words for each \(1\le n\le8\), groups them by independently computable decks, and checks all collisions; lengths one through seven admit only equal or reversed pairs, while the displayed pair occurs at eight. This finite exhaustive check is not used to prove the unbounded four-run theorem.

## Verification

Run `python3 verify.py` (standard-library Python only). It performs independent direct index enumeration of all subsequences for all binary words of lengths one through nine (1,022 words), compares with streaming dynamic programming, checks the entire family of up-to-four-run words through length nineteen (10,070 inputs), verifies the reconstruction identities and reverse criterion for all 4,096 quadruples with each run length between one and eight, checks 441 arithmetically parameterized reversal examples, and exhaustively establishes the global eight-symbol onset. The expected terminal marker is `VERIFY_OK` with the actual component counts. Exhaustive finite tests corroborate but do not replace the proofs for all positive parameters.

## Relationship to prior work

Lejeune, Rigo and Rosenfeld formalize \(k\)-binomial equivalence and characterize binary \(2\)-binomial equivalence through local switches; their Sections 1–4 and 6 provide the general context, but not this sharper four-run \(3\)-binomial rigidity statement. Chrisnata and coauthors study the cardinality of the global binary \(k\)-deck range and report small-length counts. Their tabulated global result is compatible with the first nontrivial reversal pairs at seven and first non-reversal pair at eight, but the available abstract and table do not establish the structural classification here. The related binary adjacent-pair multispectrum and contiguous-composition reconstruction problems measure different observables from scattered subsequence multiplicities.

## Limitations

No claim is made about arbitrary five-run pair classifications, words with larger numbers of runs, general alphabets, or noisy/partial decks. The sharp first-collision length is established by an exhaustive finite enumeration; the infinite rigidity theorem has an independent complete algebraic proof. Full text of the 2021 Chrisnata et al. journal version and the 2019 conference proceedings was not available for comparison, so a precise previously published specialization in their uninspected sections remains a residual originality risk. Independent validation has not been carried out.

## References

1. Marie Lejeune, Michel Rigo and Matthieu Rosenfeld, *On the binomial equivalence classes of finite words*, arXiv:2001.11732, first posted January 31, 2020. https://arxiv.org/abs/2001.11732.
2. Johan Chrisnata et al., *On the number of distinct k-decks: Enumeration and bounds*, *Advances in Mathematics of Communications* 17 (2023), 960–978, DOI:10.3934/amc.2021032. https://doi.org/10.3934/amc.2021032. Prior six-page ISCIT 2019 proceedings version: DOI:10.1109/ISCIT.2019.8905191.
