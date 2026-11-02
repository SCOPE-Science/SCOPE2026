# Sharp first-order fixed-content quasinecklace overhead

## Finding

Let \(n\ge r\ge1\), let \(m=n-r\), and consider binary words of length \(n\) containing exactly \(r\) ones. Let \(Q_r(m)\) count the quasinecklaces of Gabrić--Sawada (over the ordered alphabet \(0<1\)), and let \(N_r(m)\) count the lexicographically least cyclic rotations (necklaces) with the same content. A quasinecklace is a word whose initial run of the least symbol is a longest run of that symbol, whose initial longest run has the smallest following symbol among all such runs, and which cannot end in its minimum symbol unless constant.

The exact finite enumerators are
\[
Q_r(m)=\sum_{h=0}^{m}[x^{m-h}](1+x+\cdots+x^h)^{r-1},\qquad
N_r(m)=\frac1r\sum_{d\mid\gcd(r,m)}\varphi(d)\binom{m/d+r/d-1}{r/d-1}.
\]
Here \([x^j]\) means coefficient extraction, \(\varphi\) is Euler's totient, and the constant word is counted once when \(m=0\). For \(r=1,2\), the two counts coincide exactly. For \(r=3\), the exact excess is
\[
Q_3(m)-N_3(m)=\left\lfloor\frac m2\right\rfloor-\left\lfloor\frac m3\right\rfloor.
\]
For every **fixed integer \(r\ge3\)**, as \(m\to\infty\),
\[
Q_r(m)-N_r(m)=\frac{m^{r-2}}{2r(r-2)!}+O_r(m^{r-3}),\qquad
\frac{Q_r(m)}{N_r(m)}=1+\frac{r-1}{2m}+O_r(m^{-2}).
\]
Thus the extra candidate fraction in fixed-content binary quasinecklace generation has the sharp leading constant \((r-1)/2\) in units of \(1/m\), rather than merely a bounded multiplicative overhead.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\) ordered as written. Words are finite; a necklace means its unique lexicographically least representative under cyclic shifts, not a reflection class. The parameter \(r\) counts occurrences of \(1\), while \(m\) counts occurrences of \(0\). The asymptotic statement fixes \(r\ge3\) before letting \(m\) grow; no uniform claim for growing \(r\) is made. The exact counting formulas apply for all integers \(n\ge r\ge1\), including \(m=0\). In every formula, an empty or negative-degree coefficient is zero except the constant polynomial's coefficient at zero, which is one.

## Proof

**1. Gap encoding.** If \(m>0\), Definition 3 of the cited quasinecklace construction forces a binary quasinecklace to finish with \(1\). Write it uniquely as
\[
0^{g_1}1\,0^{g_2}1\cdots0^{g_r}1,
\qquad g_i\in\mathbb Z_{\ge0},\qquad\sum_{i=1}^{r}g_i=m.
\]
The initial run of zeros must be a longest one, so \(g_1=\max_i g_i\). Every run of that maximum length is followed by \(1\), making the following-symbol tie condition automatic. Conversely, the maximality condition on \(g_1\) suffices for the word to be a quasinecklace. When \(m=0\), the sole word is constant and both counts equal one. Fixing \(g_1=h\) proves the first exact formula by bounded weak-composition counting.

**2. Necklace orbits.** The lexicographically least rotation of a nonconstant binary word begins at the first zero of a longest zero run and terminates with \(1\). Moving among such starts rotates the gap tuple. In each cyclic orbit of length-\(r\) gap tuples there is exactly one lexicographically maximal gap tuple; it codes the least binary rotation. Burnside's lemma for cyclic shifts of \(r\) coordinates gives
\[
N_r(m)=\frac1r\sum_{d\mid\gcd(r,m)}\varphi(d)\binom{m/d+r/d-1}{r/d-1}.
\]
For \(r=1,2\), putting a maximum gap first already chooses the canonical tuple, proving equality.

**3. Exact smallest excess.** For three gaps \((a,b,c)\) with \(a\ge b,c\), the tuple fails to be lexicographically maximal among its cyclic shifts precisely when \(a=c>b\). Such tuples have \(2a+b=m\) with \(m/3<a\le m/2\), so their number is \(\lfloor m/2\rfloor-\lfloor m/3\rfloor\). This proves the weight-three identity for all \(m\ge0\).

**4. Dominant ties.** Let \(V_{r,m}\) be the set of all nonnegative \(r\)-tuples summing to \(m\), and let \(t(g)\) be the number of entries equal to the maximum of \(g\). Cyclic symmetry gives the exact identity
\[
Q_r(m)-\frac{|V_{r,m}|}{r}=\frac1r\sum_{g\in V_{r,m}}(t(g)-1),\quad |V_{r,m}|=\binom{m+r-1}{r-1}.
\]
For fixed \(r\), tuples with at least three equal maximum entries contribute only \(O_r(m^{r-3})\): after choosing their positions and common maximum, at most \(r-3\) remaining independent degrees of freedom remain. The number \(T_{r,2}(m)\) of tuples with exactly two maximum entries is
\[
T_{r,2}(m)=\binom r2\sum_{h\ge1}[x^{m-2h}](1+x+\cdots+x^{h-1})^{r-2}.
\]
Expanding the bounded powers by inclusion-exclusion, for fixed \(r\ge3\),
\[
T_{r,2}(m)=\binom r2\sum_{j=0}^{r-2}(-1)^j\binom{r-2}{j}
\sum_{h=1}^{\lfloor m/(j+2)\rfloor}\binom{m-(j+2)h+r-3}{r-3}.
\]
A sum of a degree-\(r-3\) polynomial along this arithmetic progression is
\[
\sum_{h=1}^{\lfloor m/(j+2)\rfloor}\binom{m-(j+2)h+r-3}{r-3}
=\frac{m^{r-2}}{(r-2)!(j+2)}+O_r(m^{r-3}).
\]
The coefficient sum equals
\[
\sum_{j=0}^{r-2}\frac{(-1)^j\binom{r-2}{j}}{j+2}
=\int_0^1 u(1-u)^{r-2}\,du=\frac1{r(r-1)}.
\]
Therefore \(T_{r,2}(m)=m^{r-2}/(2(r-2)!)+O_r(m^{r-3})\), and so
\[
Q_r(m)-\frac{|V_{r,m}|}{r}
=\frac{m^{r-2}}{2r(r-2)!}+O_r(m^{r-3}).
\]

**5. Removing periodic tuples.** Every nonidentity cyclic shift of \(r\) coordinates fixes tuples with at most \(\lfloor r/2\rfloor\) independent positions. For fixed \(r\ge3\), their total contribution to Burnside's count is \(O_r(m^{\lfloor r/2\rfloor-1})=O_r(m^{r-3})\). Hence \(N_r(m)=|V_{r,m}|/r+O_r(m^{r-3})\) and the excess formula follows. Finally
\[
N_r(m)=\frac{m^{r-1}}{r(r-1)!}+O_r(m^{r-2}),
\]
which yields the claimed ratio after division. Every error term is for fixed \(r\) and is valid also when \(r=3\).

## Verification

The independent finite verifier `check_quasinecklace.py` enumerates binary words directly, applies Definition 3 independently of the gap formulas, and tests every word of length at most \(17\) containing between \(1\) and \(8\) ones. It also enumerates gap compositions and their rotation maxima for \(1\le r\le7\) and \(0\le m\le16\), tests the exact weight-three excess through \(m=999\), and compares exact rational leading-term coefficients at \(m=400\) for \(3\le r\le8\). The packaged `check_output.txt` records 502,471 passing comparisons and the observed leading ratios. These experiments corroborate the proof but are not used to assert the infinite asymptotic result.

For example, when \((r,m)=(3,12)\), the exact counts are \(Q_3(12)=33\) and \(N_3(12)=31\). When \((r,m)=(4,12)\), the counts are \(127\) and \(116\), respectively.

## Relationship to prior work

Gabrić and Sawada (arXiv:2607.05324, first posted July 6, 2026) introduce quasinecklaces, prove a constant-factor bound versus necklaces, give a general recurrence for the unconstrained number, and explain bounded-weight generation. Their Definition 3 and the fixed-weight motivation are the inputs here. The present claim is the complete binary fixed-content coefficient formula together with the sharp first-order asymptotic \(1+(r-1)/(2m)+O_r(m^{-2})\), and a specific exact first excess at \(r=3\); the cited paper does not state these conclusions.

Sawada, Williams and Wong (2017) study binary *pseudo*-necklaces, a different auxiliary class that lies inside the 2026 quasinecklaces, and do not determine the excess for the latter. Ruskey and Sawada's fixed-density necklace generation work counts and generates necklaces, not this newer quasinecklace candidate family. Those standard cyclic orbit counts are used only as a baseline.

## Limitations

This theorem is binary and requires fixed \(r\) for its asymptotic; the error bounds are not uniform when \(r\) grows with \(m\). It measures the candidate-count overhead, not every operation of a generator. Earlier unpublished or unindexed equivalent calculations are not ruled out. The result has undergone mathematical and computational checking but not an independent external audit.

## References

1. Daniel Gabrić and Joe Sawada, *Necklaces and Lyndon words in colexicographic order*, arXiv:2607.05324 (2026), https://arxiv.org/abs/2607.05324. First public version: July 6, 2026. Author-posted primary full text: https://www.researchgate.net/publication/408522101_Necklaces_and_Lyndon_words_in_colexicographic_order.
2. Joe Sawada, Aaron Williams and Dennis Wong, *Necklaces and Lyndon words in colexicographic and binary reflected Gray code order*, Journal of Discrete Algorithms 46--47 (2017), 25--35, DOI:10.1016/j.jda.2017.10.002.
3. Frank Ruskey and Joe Sawada, *An Efficient Algorithm for Generating Necklaces with Fixed Density*, SIAM Journal on Computing 29 (2000), 671--684, DOI:10.1137/S0097539798344112.
