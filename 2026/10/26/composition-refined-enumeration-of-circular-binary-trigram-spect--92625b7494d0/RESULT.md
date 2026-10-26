# Composition-refined enumeration of circular binary trigram spectra

## Finding

Let \(w=w_0\cdots w_{n-1}\) be a nonempty binary circular word. Its **cyclic trigram spectrum** is the eight-vector
\[
  c_{ijk}(w)=|\{r\in\{0,\ldots,n-1\}:(w_r,w_{r+1},w_{r+2})=(i,j,k)\}|,
\]
where subscripts of \(w\) are reduced modulo \(n\); this definition also applies for lengths one and two. Rotation does not change the spectrum. Write \(P_{p,q}\) for the number of *different* spectra realized by binary circular words with exactly \(p\) zeros and \(q\) ones, with \(p,q\) nonnegative and \(p+q\ge1\). Put
\[
 F_t(s)=\mathbf1_{\{s=t\}}+\max\{0,\min(t,s-t)\}, \qquad t\ge1,\ s\ge0.
\]
Then
\[
\boxed{P_{p,q}=\begin{cases}1,&pq=0,\\\displaystyle\sum_{t=1}^{\min(p,q)}F_t(p)F_t(q),&pq>0.\end{cases}}
\]
In particular, if \(P_n=\sum_{p+q=n}P_{p,q}\), then
\[
\boxed{\sum_{n\ge1}P_nz^n=\frac{z(2-3z+z^2-z^3+5z^5-5z^6+6z^7-7z^8+3z^9)}{(1-z)^5(1+z)(1+z^2)(1+z+z^2)}.}
\]
Thus \(P_n\sim n^4/288\). The first values \(P_1,\ldots,P_{16}\) are
\[
2,3,4,6,8,13,18,27,38,53,72,98,128,167,214,271.
\]
These counts are also the largest possible sizes of codes selecting length-\(n\) words distinguishable by their **complete cyclic trigram multiplicity vector**, and of such codes constrained to a fixed zero-one composition. Rotations share a spectrum, so no such code can include two rotationally equivalent words.

## Assumptions and scope

The alphabet is labeled \(\{0,1\}\); trigram coordinates are labeled and retain multiplicities. "Circular" means there are exactly \(n\) starting positions with wraparound, not the \(n-2\) substrings of a linear word. Distinct spectra are counted once, regardless of the number of realizing labeled strings or necklaces. The code interpretation assumes noiseless access to the entire eight-vector, not a randomly sampled read or an unordered *set* of trigrams.

## Proof

**1. All realizable spectra.** Associate each trigram \(ijk\) to the directed edge \(ij\to jk\) of the binary order-two de Bruijn graph on vertices \(00,01,10,11\). A circular word yields a closed walk that traverses the edge \(ijk\) precisely \(c_{ijk}\) times. Conversely, a balanced directed edge multiset whose positive-degree support is weakly connected has an Eulerian circuit; its sequence of overlapping vertex labels spells a circular binary word with exactly those trigram multiplicities. This is the standard Eulerian-circuit criterion, applied with parallel edges distinguished only for traversal, not for spectrum counting.

Write \(a=c_{000}\) and \(h=c_{111}\). Balance at \(00\) and \(11\) forces
\[
 c_{001}=c_{100}=x,\qquad c_{011}=c_{110}=y.
\]
The remaining balance equation is \(c_{010}+y=x+c_{101}\). Set
\[
 t=c_{010}+y=x+c_{101},
 \qquad c_{010}=t-y,\quad c_{101}=t-x.
\]
For a nonmonochromatic word, \(t\ge1\) and \(0\le x,y\le t\). The graph on its nonloop edges is connected: the edges \(010\) and \(101\) connect \(01\) with \(10\) when present; positive \(x\) supplies the detour \(10\to00\to01\), while positive \(y\) supplies \(01\to11\to10\). Because \(t\ge1\), at least one of the direct or detour links in each direction exists, so the positive-degree nonloop graph is strongly connected. A \(000\)-loop can belong to the same component precisely when \(x>0\), and a \(111\)-loop precisely when \(y>0\). Therefore the full necessary and sufficient list of nonmonochromatic spectra is
\[
\begin{array}{c|cccccccc}
ijk&000&001&010&011&100&101&110&111\\\hline
c_{ijk}&a&x&t-y&y&x&t-x&y&h
\end{array}
\]
where \(t\ge1\), \(0\le x,y\le t\), \(a,h\ge0\), and \(x=0\Rightarrow a=0\), \(y=0\Rightarrow h=0\). Every parameter tuple gives one **distinct** spectrum. The only other realizable spectra are the pure-zero and pure-one loops. Necessity of the loop restrictions follows because an isolated positive loop cannot lie in a single closed walk with the other nonzero edges; sufficiency follows from connected balance.

**2. Refine by composition.** The number of zeros is the sum of counts of trigrams starting with zero, and similarly for ones. For the parametrization above these are
\[
 p=t+x+a,\qquad q=t+y+h.
\]
Fix \(t\ge1\) and \(p\). When \(x=0\), the loop restriction forces \(a=0\) and hence \(p=t\), giving the indicator \(\mathbf1_{\{p=t\}}\). When \(1\le x\le t\), there is exactly one allowable \(a=p-t-x\) if \(x\le p-t\), and none otherwise. The resulting number is \(F_t(p)\). The analogous choice for \((y,h)\) has \(F_t(q)\) possibilities and is independent, proving the displayed formula for \(P_{p,q}\). If \(pq=0\), the sole possible spectrum is the corresponding monochromatic loop.

**3. Rational generating functions.** Define
\[
 B_t(u)=1+\frac{u+\cdots+u^t}{1-u}=1+\frac{u(1-u^t)}{(1-u)^2}.
\]
The generating series for the zero count at fixed \(t\), summed over \(x,a\), is \(u^tB_t(u)\), with an independent analogous factor for the ones. Thus the *composition-refined* generating function is
\[
 \sum_{p,q\ge0\atop p+q\ge1}P_{p,q}u^pv^q
 =\frac{u}{1-u}+\frac{v}{1-v}+\sum_{t\ge1}(uv)^t B_t(u)B_t(v).
\]
In particular this sum is rational. To exhibit a closed bivariate form put \(A(s)=1+s/(1-s)^2\) and \(E(s)=s/(1-s)^2\); since \(B_t(s)=A(s)-E(s)s^t\), geometric summation gives
\[
\begin{aligned}
\mathcal P(u,v)={}&\frac{u}{1-u}+\frac{v}{1-v}
+\frac{A(u)A(v)uv}{1-uv}
-\frac{E(u)A(v)u^2v}{1-u^2v}\\
&-\frac{A(u)E(v)uv^2}{1-uv^2}
+\frac{E(u)E(v)u^2v^2}{1-u^2v^2}.
\end{aligned}
\]
Substitute \(u=v=z\), bring the five rational terms over a common denominator, and cancel to obtain the stated univariate rational function. At \(z=1\), its numerator factor after extracting \(z\) evaluates to \(1\), and the other denominator factors evaluate to \(2\), \(2\), \(3\). Therefore
\[
\mathcal P(z,z)=\frac1{12(1-z)^5}+O((1-z)^{-4})
\]
near \(z=1\). Other poles are roots of unity of order two, three or four; their pole orders are below five. Coefficient extraction gives \(P_n=n^4/288+O(n^3)\). For length-\(n\) codes, each distinct spectrum permits at most one representative and choosing one word per realized spectrum attains that bound, also under fixed composition.

## Verification

Run `python3 verify.py` in the same directory. The script independently enumerates labeled binary words, forms cyclic trigram vectors directly, and compares distinct vector counts against (i) the composition sum and (ii) the parameterization, including short wraparound lengths. It additionally expands the rational generating function using integer polynomial recurrences and tests coefficients through length \(120\). This verifies many finite cases but is not a substitute for the all-length Eulerian proof. The script requires only Python's standard library and reports `VERIFY_OK` on success.

## Relationship to prior work

Chen, Kitaev, Lang, Pyatkin and Tang (first preprint October 25, 2025) develop Eulerian covers of de Bruijn graphs for lossless multiset compression; their general traversal framework supplies the representation motivation but does not enumerate realizable circular binary three-mer count vectors by composition. Zhu, Liu and Liu (February 28, 2026) analyze genome reconstruction via de Bruijn traversal and probabilistic prefix collisions, not the finite exact histogram enumeration proved here. En Gad (September 16, 2026) employs substring-count vectors as ingredients in edit-correcting code constructions, without deriving the circular composition-refined spectrum count. The present claim is an exact count of *feasible observations*, not a claim of unique reconstruction of each input word. Linear-word spectra and cyclic spectra have different Euler-trail boundary constraints and cannot be identified merely by subtracting rotational duplicates.

## Limitations

This is restricted to a binary alphabet, cyclic contiguous reads of length exactly three, and noiseless complete multiplicities. It neither counts the number of necklaces realizing each vector nor establishes uniqueness of circular reconstruction; most vectors can have multiple realizations. General alphabets and read lengths remain untreated. The literature comparison cannot exclude every unpublished or unindexed equivalent formula. Any claim of novelty therefore remains conditional on the examined sources.

## References

1. H. Z. Q. Chen, S. Kitaev, X. Lang, A. Pyatkin, R. Tang, *Efficient k-mer Dataset Compression Using Eulerian Covers of de Bruijn Graphs and BWT*, arXiv:2510.22404 (first posted 2025-10-25), https://arxiv.org/abs/2510.22404.
2. B. Zhu, S. Liu, S. Liu, *Reconstruction of DNA Sequences Through Eulerian Traversal of De Bruijn Graphs*, Mathematics **14** (2026), 832, https://doi.org/10.3390/math14050832 (published 2026-02-28).
3. E. En Gad, *Polynomially larger deletion codes by linear hashing of substring counts*, arXiv:2609.19493 (first posted 2026-09-16), https://arxiv.org/abs/2609.19493.
4. G. Bernardini, H. Chen, G. Loukides, S. P. Pissis, L. Stougie, M. Sweering, *Making de Bruijn Graphs Eulerian*, CPM 2022, https://doi.org/10.4230/LIPIcs.CPM.2022.12.
