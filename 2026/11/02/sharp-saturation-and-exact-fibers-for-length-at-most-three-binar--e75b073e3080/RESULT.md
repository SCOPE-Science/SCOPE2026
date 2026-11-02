# Sharp saturation and exact fibers for length-at-most-three binary composition reads

## Finding

For an indexed binary word of length \(n\ge3\) and Hamming weight \(w\), observe the **multiplicity-preserving** compositions of all contiguous, nonwrapping substrings of lengths \(1\), \(2\), and \(3\). A length-\(j\) composition is specified by its number of ones. The exact fibers of this observation are given below by a finite truncated-gap formula, valid for every \(n\ge3\) and \(1\le w\le n\). The zero-weight case has one word and one profile.

The number of profiles, equivalently the maximum cardinality of a zero-error code confined to weight \(w\), is *constant in* \(n\) from the **sharp** threshold \(n=3w+2\) onward. For three ones, the complete capacity is

\[
C_{n,3}=\begin{cases}
1,2,6,9,16,21,26,28&\text{respectively for }n=3,4,5,6,7,8,9,10,\\
29&n\ge11.
\end{cases}
\]

Thus the three-marker channel distinguishes at most \(29\) messages irrespective of the number of additional zeros, and the length \(11\) stabilization threshold is exact.

## Assumptions and scope

All strings are **linear and indexed**, not identified under reversal, rotation, or complementation. Fragments overlap and their multiplicities are retained. The receiver knows \(n\), \(w\), and which fragment length each count belongs to. There is no noise or loss of fragments. The restriction to maximum fragment length three is essential.

Every length-\(n\), weight-\(w\) word is written uniquely as

\[
x=0^{g_0}1\,0^{g_1}1\cdots1\,0^{g_w},\qquad
 g_i\in\mathbb Z_{\ge0},\quad \sum_{i=0}^{w}g_i=n-w.
\]

Define the **capped gap vector** \(h_i=\min\{g_i,2\}\), its number of capped-long gaps \(t(h)=\#\{i:h_i=2\}\), and its representative length \(m(h)=w+\sum_i h_i\). Let \(y(h)=0^{h_0}1\cdots1\,0^{h_w}\). For \(j=2,3\) and \(1\le k\le j\), put

\[
 f_{j,k}(y)=\#\{0\le i\le |y|-j: \operatorname{wt}(y_i\cdots y_{i+j-1})=k\},
\]

with an empty range interpreted as zero. Define the five-coordinate signature

\[
\Phi(h)=(f_{2,1}(y(h)),f_{2,2}(y(h)),f_{3,1}(y(h)),f_{3,2}(y(h)),f_{3,3}(y(h))).
\]

The zero-count coordinates and all length-one counts are recovered from \(n,w\) and these five coordinates, so \(\Phi\) specifies the entire observation at fixed \(n,w\).

## Proof

**1. Locality and the exact fiber formula.** If any zero gap of length at least two is lengthened by one, the extra windows of length two or three all have zero ones. Every window with at least one one retains its composition count. Therefore \(\Phi(\min(g,2))\) is the exact nonzero-grade read signature of \(x\). Conversely each capped vector \(h\in\{0,1,2\}^{w+1}\) determines a disjoint collection of sources with that signature.

If \(t(h)=0\), this collection consists of its single representative word exactly when \(n=m(h)\). If \(t(h)>0\), it consists of all ways to distribute \(n-m(h)\) additional zeros over the \(t(h)\) gaps already capped at two. Stars and bars gives

\[
E_{n,w}(h)=
\begin{cases}
\mathbf1_{\{n=m(h)\}},&t(h)=0,\\
\mathbf1_{\{n\ge m(h)\}}
\binom{n-m(h)+t(h)-1}{t(h)-1},&t(h)>0.
\end{cases}
\]

For every possible five-coordinate signature \(s\), the **exact inverse-fiber cardinality**, with no restriction to unique profiles, is therefore

\[
\boxed{F_{n,w}(s)=\sum_{\substack{h\in\{0,1,2\}^{w+1}\\\Phi(h)=s}}E_{n,w}(h).}
\]

This proves both the inverse-fiber classification and the finite exact capacity formula

\[
\boxed{C_{n,w}=\#\{\Phi(h):h\in\{0,1,2\}^{w+1},\ E_{n,w}(h)>0\}.}
\]

The sum of all fibers is \(\binom nw\), since the capped-gap partition is disjoint and exhaustive. One representative from each nonempty fiber is a maximum zero-error code, while at most one representative of a fiber can occur in such a code.

**2. Sharp general saturation.** A capped vector with \(t(h)=0\) has representative length at most \(2w+1\) and cannot occur at larger lengths. Every capped vector has \(m(h)\le3w+2\). Consequently, for every \(n\ge3w+2\), every signature with at least one long capped gap is feasible, and none without one is feasible:

\[
C_{n,w}=\#\{\Phi(h):h\in\{0,1,2\}^{w+1},\ t(h)>0\}.
\]

This is independent of \(n\). The capped vector \((2,\ldots,2)\) is represented by a word whose \(3w\) length-three windows each contain exactly one one. It has \(f_{3,1}=3w\). At length \(n=3w+1\), there are only \(n-2=3w-1\) length-three windows in total, so no profile can have this signature. Since all feasible profiles at \(n=3w+1>2w+1\) arise from vectors with \(t(h)>0\), they are a strict subset of the eventual image. Therefore \(C_{3w+1,w}<C_{3w+2,w}\), and the saturation threshold cannot be lowered for any \(w\ge1\).

**3. Exact three-marker enumeration.** When \(w=3\), there are \(3^4-2^4=65\) capped-gap vectors with at least one coordinate equal to two. Applying the fully explicit definition of \(\Phi\) partitions these into the following \(29\) groups. The displayed four-digit word denotes a capped gap vector (not an observed source); the last column counts capped vectors in its signature class. This is a complete finite certificate: each signature is distinct and the class sizes sum to \(65\).

For a hand-replayable arithmetic reduction of this finite certificate, write \([P]\) for the indicator of proposition \(P\), and set

\[
\begin{aligned}
p&=[h_1=0]+[h_2=0],&q&=[h_1=1]+[h_2=1],&u&=[h_1=h_2=0],\\
b&=[h_0=h_1=0]+[h_2=h_3=0],& e&=[h_0=0]+[h_3=0],\\
a&=2[h_0=0]+[h_0=1\ \mathrm{or}\ h_0=h_1=0]
 +2[h_3=0]+[h_3=1\ \mathrm{or}\ h_2=h_3=0].
\end{aligned}
\]

Directly counting one-incidences and pair-incidences in two- and three-windows yields

\[
\Phi(h)=\bigl(6-e-2p,\ p,\ 9-a-2(2p+q-2u-b)-3u,\ 2p+q-2u-b,\ u\bigr).
\]

These six elementary indicator parameters give an independent finite way to reproduce every row of the table without enumerating long source words.


| Capped gaps \(h_0h_1h_2h_3\) | Signature \((f_{2,1},f_{2,2};f_{3,1},f_{3,2},f_{3,3})\) | Class size |
|---|---|---:|
| `0002` | \(1,2;1,1,1\) | 2 |
| `0020` | \(2,1;2,1,0\) | 2 |
| `1002` | \(2,2;1,2,1\) | 2 |
| `2002` | \(2,2;2,2,1\) | 1 |
| `0102` | \(3,1;1,3,0\) | 2 |
| `0012` | \(3,1;2,2,0\) | 4 |
| `0021` | \(3,1;3,1,0\) | 2 |
| `0202` | \(3,1;3,2,0\) | 2 |
| `0022` | \(3,1;4,1,0\) | 2 |
| `0120` | \(4,0;3,1,0\) | 2 |
| `0220` | \(4,0;5,0,0\) | 1 |
| `1012` | \(4,1;2,3,0\) | 4 |
| `1021` | \(4,1;3,2,0\) | 2 |
| `2012` | \(4,1;3,3,0\) | 2 |
| `1022` | \(4,1;4,2,0\) | 4 |
| `2022` | \(4,1;5,2,0\) | 2 |
| `0112` | \(5,0;3,2,0\) | 2 |
| `0121` | \(5,0;4,1,0\) | 4 |
| `0122` | \(5,0;5,1,0\) | 4 |
| `0221` | \(5,0;6,0,0\) | 2 |
| `0222` | \(5,0;7,0,0\) | 2 |
| `1112` | \(6,0;4,2,0\) | 2 |
| `1121` | \(6,0;5,1,0\) | 2 |
| `2112` | \(6,0;5,2,0\) | 1 |
| `1122` | \(6,0;6,1,0\) | 4 |
| `1221` | \(6,0;7,0,0\) | 1 |
| `2122` | \(6,0;7,1,0\) | 2 |
| `1222` | \(6,0;8,0,0\) | 2 |
| `2222` | \(6,0;9,0,0\) | 1 |

Each representative has \(m(h)\le11\) and contains a capped-long gap. Adding \(11-m(h)\) zeros to such a gap gives a length-eleven witness with the same signature, proving all \(29\) are realized at the threshold. For shorter lengths the exhaustive gap-coordinate ranges \(g_0+g_1+g_2+g_3=n-3\) give:

| \(n\) | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | \(\ge11\) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(C_{n,3}\) | 1 | 2 | 6 | 9 | 16 | 21 | 26 | 28 | 29 |

The attached complete verifier evaluates exactly these finite ranges, the \(65\)-vector certificate, and the general formula against independently enumerated source words. The infinite-length assertions follow from the locality and gap-composition arguments above, not from experimentation.

## Verification

Run `python3 verify.py` with standard Python 3 and no dependencies. Its output ends with `VERIFY_OK`. It independently enumerates all fixed-weight binary words at \(3\le n\le18\), \(0\le w\le\min(n,6)\), and compares **every fiber cardinality**, not merely the number of profiles, to the capped-gap formula (\(106\) parameter cases). It also checks the three-marker formula through length \(30\), sharpness for \(1\le w\le8\), the complete \(29\)-signature certificate, and a distinguishing example between two-length-plus-three-length and three-length-only reads. These finite checks are reproducibility aids; the proof applies to all lengths and weights.

## Relationship to prior work

Ye and Elishco introduced the length-limited substring-composition observation and gave coding constructions when the read limit scales with source length; their relevant Section VIII does not enumerate its exact fibers for a fixed fragment limit. This result specializes that natural channel to the first higher short limit \(r=3\) and resolves the sparse fixed-composition setting by a finite gap state and exact stars-and-bars fibers.

Related results for arbitrary-weight length-two composition profiles, arbitrary-length short-read profiles with two markers, and single-length three-window grade profiles do not imply the present combined length-two-plus-three observation fibers. In particular, `11000000100` and `10100000010` have the same length-three composition counts but different length-two composition counts. Constant-weight prefix/suffix composition reconstruction is another distinct observation model, as are full-length substring-composition multisets.

## Limitations

The observation must retain every fragment with multiplicity, remain noncyclic, and distinguish fragment lengths. The exact \(29\) value is only for weight three; general weights are described by the finite signature formula rather than a closed polynomial in the weight. Nothing is asserted for erroneous or incomplete read multisets or for lengths beyond three. No independent external scientific audit has been carried out. Publication-priority uncertainty remains possible, particularly under equivalent local-pattern or Parikh-spectrum terminology.

## References

1. Zuo Ye and Ohad Elishco, *Reconstruction of a Single String from a Part of its Composition Multiset*, arXiv:2208.14963, first public August 31, 2022. Relevant Section VIII. https://arxiv.org/abs/2208.14963
2. Yaoyu Yang and Zitan Chen, *Reconstruction of multiple strings of constant weight from prefix-suffix compositions*, arXiv:2411.03776, first public November 6, 2024. Distinct prefix/suffix observation model. https://arxiv.org/abs/2411.03776
3. Jayadev Acharya, Hirakendu Das, Olgica Milenkovic, Alon Orlitsky and Shengjun Pan, *String Reconstruction from Substring Compositions*, SIAM Journal on Discrete Mathematics 29 (2015), 1340–1371. Complete-fragment observation rather than a fixed short-read truncation. https://doi.org/10.1137/140962486
