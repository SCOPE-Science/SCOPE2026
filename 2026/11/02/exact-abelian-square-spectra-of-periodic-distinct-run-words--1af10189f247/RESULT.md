# Exact Abelian-square spectra of periodic distinct-run words

## Finding

Fix an integer \(q\ge3\), pairwise distinct letters \(a_0,\ldots,a_{q-1}\), positive integer run lengths \(r_0,\ldots,r_{q-1}\), and an integer \(k\ge1\). Define
\[
P=a_0^{r_0}a_1^{r_1}\cdots a_{q-1}^{r_{q-1}},\qquad
p=\sum_{i=0}^{q-1}r_i,\qquad W_k=P^k.
\]
An *Abelian square* is a nonempty contiguous factor \(UV\) with \(|U|=|V|\ge1\) and equal Parikh vectors (equal numbers of each letter) in \(U\) and \(V\). Here distinct Abelian squares are counted **as distinct factor strings**, not as positions and not up to Abelian equivalence. Let \(T(k)\) be their total number in \(W_k\). Put
\[
d=\sum_i\left\lfloor\frac{r_i}{2}\right\rfloor,\quad
B=p+2\sum_i\left\lfloor\frac{r_i^2}{4}\right\rfloor,\quad
e=1+\left\lfloor\frac{r_0}{2}\right\rfloor+
\left\lfloor\frac{r_{q-1}}{2}\right\rfloor.
\]
Then, for every \(k\ge1\),
\[
\boxed{T(k)=
\begin{cases}
d+\dfrac{k-1}{2}B,&k\text{ odd},\\[2pt]
d+\left(\dfrac{k}{2}-1\right)B+e,&k\text{ even}.
\end{cases}}
\]
In particular the exact **two-power increment** is
\[
\boxed{T(k+2)-T(k)=p+2\sum_i\left\lfloor\frac{r_i^2}{4}\right\rfloor\quad(k\ge1).}
\]
The result also classifies the complete spectrum \(c_k(\ell)\) of distinct Abelian-square factors of length \(2\ell\), for every integer \(1\le\ell\le\lfloor kp/2\rfloor\).

Number positions of the infinite periodic word \(P^\infty\) from zero. Write \(r\equiv\ell\pmod p\) with \(0\le r<p\). A *circular run* is one of the \(q\) maximal same-letter intervals in one cyclic period, with coordinates modulo \(p\). Define the following subsets of residues \(\{0,1,\ldots,p-1\}\):
\[
\mathcal S_r=\begin{cases}
\{0,1,\ldots,p-1\},&r=0,\\
\{s:\text{the circular segment }[s,s+2r)\text{ lies in one run}\},&0<2r\le p,\\
\{s:\text{the circular segment }[s-2(p-r),s)\text{ lies in one run}\},&p<2r<2p.
\end{cases}
\]
All segment coordinates are understood modulo \(p\); endpoints are half-open. Let \(U=kp-2\ell\). The exact spectrum is
\[
\boxed{c_k(\ell)=\begin{cases}
\#\{i:r_i\ge2\ell\},&2\ell<p,\\
\#\bigl(\mathcal S_r\cap\{0,\ldots,\min(p-1,U)\}\bigr),&2\ell\ge p.
\end{cases}}
\]
For the middle case \(2r=p\), the defining run condition is impossible, hence \(\mathcal S_r\) is empty. These formulas determine both the *strings* (via admissible start residues) and their length distribution. Their sum over \(\ell\) is \(T(k)\).

## Assumptions and scope

The alphabet has at least three letters. Each symbol occupies exactly one positive-length run per period, and the period starts at the first run boundary. Only *contiguous* factors, not scattered subsequences, are counted. Factors of different lengths are necessarily distinct. Factor strings with identical Parikh vectors but different order are counted separately. The phase-sensitive term \(e\) depends on the designated first and last runs of the finite host.

The hypothesis \(q\ge3\) cannot simply be dropped: for \(P=01\) and \(k=3\), the three distinct Abelian squares are `0101`, `1010`, and `010101`, whereas the displayed \(q\ge3\) formula would return two.

## Proof

**1. Circular adjacent-window lemma.** In a circular word with at least three runs and a distinct letter in each run, take two adjacent disjoint arcs of the same positive length \(h\), with \(2h\le p\). If their Parikh vectors agree, their union is monochromatic.

To see this, the nonempty supports of their Parikh vectors must agree. A letter whose single circular run meets both arcs must connect the two arc portions either across their common boundary or along the other way around the circle, through the complement of their union. At most one run can meet both arcs by each route. If two distinct runs use the two routes, the outside-connecting run contains the entire complementary arc, leaving every third-letter run inside exactly one of the two arcs; its counts would differ. Because at least a third run exists, this is impossible. Thus at most one letter appears in both arcs, so equality of their nonempty supports forces each arc to consist of this same letter. The converse is immediate. The argument includes the case \(2h=p\), when the complementary arc is empty: two runs crossing the two boundary points would leave any third run on just one side.

**2. Period reduction.** Write \(\ell=ap+r\), \(0\le r<p\). The Parikh vector of a length-\(\ell\) window at start residue \(s\) is \(a(r_0,\ldots,r_{q-1})\) plus the Parikh vector of the circular length-\(r\) arc beginning at \(s\). The adjacent second half starts at \(s+r\) modulo \(p\). Thus the two halves have equal Parikh vectors if and only if these two circular length-\(r\) arcs do. For \(r=0\), equality holds at every phase.

If \(0<2r\le p\), the arcs are disjoint and adjacent; by Step 1, equality holds exactly when the circular segment of length \(2r\) starting at \(s\) lies within one run. If \(2r>p\), set \(h=p-r\). Each length-\(r\) arc is the complement of a length-\(h\) arc in one period. Equality of the original arc Parikh vectors is equivalent to equality of the complementary arc vectors. Those two complementary arcs are disjoint, adjacent, and together comprise the length-\(2h\) segment ending at \(s\). Step 1 gives the stated final case of \(\mathcal S_r\). This proves the complete membership classification.

**3. From starts to distinct factors.** If \(2\ell<p\), Step 2 says any Abelian-square factor is one repeated symbol, so exactly one length-\(2\ell\) string occurs for each run of length at least \(2\ell\). If \(2\ell\ge p\), a factor contains a full period. Two factors beginning at different residues are different: otherwise the length-\(p\) cyclic shifts of \(P\) at those residues would agree. Such agreement would make \(P\) have a proper cyclic period, impossible when each of at least three distinct letters occupies exactly one nonempty run. The permitted start indices in \(W_k\) are \(0,\ldots,kp-2\ell\); each residue occurring there therefore contributes exactly one distinct factor, and no other residue does. This proves the formula for \(c_k(\ell)\).

**4. Full-phase count.** For any integer \(h\ge1\), a circular monochromatic segment of length \(2h\) has exactly
\[
F_h=\sum_{i=0}^{q-1}\max(0,r_i-2h+1)
\]
possible starting residues. Step 2 therefore gives \(|\mathcal S_0|=p\) and \(|\mathcal S_r|=F_{\min(r,p-r)}\) for \(0<r<p\). There is no segment of length \(p\) within one run because \(q\ge3\). Consequently a complete block of \(p\) consecutive half-length residues has the sum
\[
\sum_{r=0}^{p-1}|\mathcal S_r|
=p+2\sum_{h=1}^{\lfloor(p-1)/2\rfloor}F_h
=p+2\sum_i\left\lfloor\frac{r_i^2}{4}\right\rfloor=B.
\]
The last equality follows by summing the arithmetic progression of starting positions for the even widths \(2,4,\ldots,2\lfloor r_i/2\rfloor\) within run \(i\): it sums to \(\lfloor r_i^2/4\rfloor\).

**5. Initial powers.** For \(k=1\), only the monochromatic squares of lengths below \(p\) occur, giving \(T(1)=d\). For \(k=2\), a full-period square at half-length \(p\) contributes exactly one factor. At half-length \(p-h\), where \(1\le h<p/2\), the allowed starts are \(0,\ldots,2h\). Step 2 requires the circular length-\(2h\) segment ending at the start to lie in one run. Only the starts \(0\) and \(2h\) can achieve this: they work precisely when the last, respectively first, run has length at least \(2h\). Hence \(T(2)=d+e\).

For \(k=3\), each half-length \(p-h\) and \(p+h\), with \(1\le h\le\lfloor(p-1)/2\rfloor\), contributes \(F_h\) factors: in the first case all phases are available, while in the second case the permitted starting interval \(0,\ldots,p-2h\) already contains every possible monochromatic length-\(2h\) segment. The half-length \(p\) contributes all \(p\) cyclic shifts. The possible half-length \(p/2\), when \(p\) is even, contributes none. Thus \(T(3)=d+B\).

**6. The exact increment.** For each \(k\ge2\), the profile at half-length \(\ell+p\) in \(W_{k+2}\) is identical to the profile at half-length \(\ell\) in \(W_k\) whenever \(\ell\ge\lceil p/2\rceil\): both have the same residue class and the same available start bound \(kp-2\ell\). All the other nonmonochromatic-length candidates in \(W_{k+2}\) occur at the \(p\) half-lengths \(\lceil p/2\rceil,\ldots,\lceil p/2\rceil+p-1\). For \(k\ge2\), each of these has at least \(p\) available start positions and therefore realizes every phase of its residue class. By Step 4 their total contribution is exactly \(B\). The monochromatic factors below length \(p\) do not change. Therefore \(T(k+2)-T(k)=B\) for all \(k\ge2\); the case \(k=1\) follows from \(T(3)-T(1)=B\). Combining this recurrence with \(T(1)=d\) and \(T(2)=d+e\) gives the displayed parity-separated formula for every positive \(k\).

## Verification

`verify.py` implements literal, position-based enumeration and independently compares every length-specific distinct-factor count with the circular-run structural formula and with the closed total. Its deterministic test suite covers \(997\) parameter cases, \(14,021\) half-length profiles, and \(4,340\) circular adjacent-arc cases. The successful command and result are recorded in `VERIFICATION.md`. Finite computation is an additional consistency check, not the basis of the all-parameter proof.

As a non-implication witness, run vectors \((4,1,2)\) and \((1,4,2)\) have the same length-by-length counts of Abelian factor *Parikh vectors*, because those counts depend only on the multiset of run lengths, but their distinct Abelian-square totals at \(k=2\) are \(7\) and \(5\), respectively. Therefore ordinary Abelian-factor complexity data alone do not determine the present square statistic.

## Relationship to prior work

Fici, Mignosi and Shallit (arXiv:1701.00948; first public January 4, 2017) define distinct Abelian-square counts and study richness, general bounds, and specific aperiodic families. Sugimoto, Noda, Inenaga, Bannai and Takeda (arXiv:1701.02836; first public January 11, 2017), Section 4 and Theorem 2, give an algorithm for locating Abelian squares in arbitrary run-length-encoded strings. Simpson (arXiv:1802.04481; first public February 13, 2018) surveys extremal counts for linear and circular words. Fici and Puzynina (arXiv:2207.09937, Section 4.3) survey Abelian-square factor enumeration. The cited results give broad background and algorithms, but their inspected statements do not supply this explicit all-parameter formula, the distinct-letter circular-arc criterion, or the two-power increment.

The earlier distinct-Parikh-factor spectrum for the same type of periodic word counts single-window Parikh vectors; it does not test equality of **adjacent** half-window vectors, and its invariance under permuting the run lengths contrasts with the phase-sensitive boundary term above. No novelty is claimed for the definition of an Abelian square, the standard sliding-window algorithm, or the general observation that periodic words have bounded factors of each fixed length.

## Limitations

The theorem requires at least three distinct symbol-runs per cyclic period. It does not classify ordinary binary two-run powers, periods in which letters recur in multiple runs, arbitrary RLE strings, or occurrences counted with multiplicity. The novelty comparison covers the identified and inspected literature and available matching research records; an overlooked exact specialization remains possible. All proof and computational checks reported here are self-review. No independent audit or external mathematical validation has been performed.

## References

1. G. Fici, F. Mignosi, and J. Shallit, *Abelian-Square-Rich Words*, arXiv:1701.00948, first public 2017-01-04. https://arxiv.org/html/1701.00948v3
2. S. Sugimoto, N. Noda, S. Inenaga, H. Bannai, and M. Takeda, *Computing Abelian regularities on RLE strings*, arXiv:1701.02836, first public 2017-01-11. https://arxiv.org/pdf/1701.02836
3. J. Simpson, *Solved and Unsolved Problems about Abelian Squares*, arXiv:1802.04481, first public 2018-02-13. https://arxiv.org/pdf/1802.04481
4. G. Fici and S. Puzynina, *Abelian Combinatorics on Words: a Survey*, arXiv:2207.09937. https://arxiv.org/html/2207.09937v2
