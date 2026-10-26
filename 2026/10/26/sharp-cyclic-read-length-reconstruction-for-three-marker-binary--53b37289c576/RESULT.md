# Sharp cyclic read-length reconstruction for three-marker binary words

## Finding
Let \(n\ge5\). An **oriented binary necklace** is a binary circular word modulo rotation, *not* reversal. Restrict to necklaces with exactly three occurrences of \(1\). For \(1\le k\le n\), the cyclic \(k\)-spectrum \(\mathcal S_k(w)\) is the multiset of its \(n\) directed contiguous length-\(k\) factors, one from each starting position. Let \(K(w)\) be the least \(k\) for which this multiset identifies \(w\) uniquely among length-\(n\), three-one necklaces.

Write the three cyclic numbers of zeros between consecutive ones as \((g_1,g_2,g_3)\), and sort them as \(a\le b\le c\), with \(a+b+c=n-3\). Then
\[
K(w)=\begin{cases}
a+1,&a=b=c,\\
a+1,&a=b<c=a+1,\\
a+2,&a=b<c\text{ and }c\ge a+2,\\
b+1,&a<b=c,\\
n-c,&a<b<c.
\end{cases}
\]
Here \(a=b<c=a+1\) means \(a=b\) and \(c=a+1\). For the two shorter boundary lengths \(n=3,4\), the unique three-one necklace is already identified by its one-symbol spectrum, so \(K(w)=1\).

For every \(n\ge6\), the **sharp worst-case read length** is
\[
\max_w K(w)=\left\lfloor\frac{2n}{3}\right\rfloor.
\]
Exactly two necklaces attain this maximum when \(n\equiv0,2\pmod3\), and also when \(n=7\); exactly four attain it when \(n\equiv1\pmod3\) and \(n\ge10\). Their gap multisets are, writing \(n=3q+r\): \((q-2,q-1,q)\) for \(r=0\); \((q-2,q-1,q+1)\), and additionally \((q-3,q,q+1)\) for \(r=1\) whenever its entries are nonnegative; and \((q-2,q,q+1)\) for \(r=2\). Each such multiset has two inequivalent cyclic orientations.

There is also an **exact threshold distribution**. Let \(T_n(k)\) count the three-one oriented necklaces with \(K(w)=k\), put \(m=n-3\), and set \([x]_+=\max\{0,x\}\). For every \(n\ge5\),
\[
\begin{aligned}
T_n(k)={}&2\left[\left\lfloor\frac{k-2}{2}\right\rfloor-\max\{0,2k-n-2\}\right]_+\\
&+\sum_{0\le a<c\, :\,2a+c=m}\mathbf1_{\{k=a+1\text{ if }c=a+1,\text{ otherwise }k=a+2\}}\\
&+\sum_{0\le a<b\, :\,a+2b=m}\mathbf1_{\{k=b+1\}}+\mathbf1_{\{3\mid m,\ k=m/3+1\}}.
\end{aligned}
\]
All sums are over nonnegative integers, and \(T_n(k)=0\) outside \(1\le k\le n\). In particular, the number of necklaces in the sample space is \(\bigl(\binom{n-1}{2}+2\mathbf1_{\{3\mid n\}}\bigr)/3\).

Finally, if \(W_n\) is a uniformly random oriented three-one necklace and \(Y_n=K(W_n)/n\), then \(Y_n\) converges in distribution to \(Y\) with
\[
\Pr(Y\le y)=\begin{cases}
0,&y<0,\\
3y^2,&0\le y\le1/2,\\
-9y^2+12y-3,&1/2\le y\le2/3,\\
1,&y>2/3.
\end{cases}
\]
Consequently
\[
\mathbb E[K(W_n)]=\frac7{18}n+o(n),\qquad
\operatorname{Var}(K(W_n))=\frac{13}{648}n^2+o(n^2).
\]

## Assumptions and scope
Letters are \(0\) and \(1\), the number of ones is exactly three, and the circle has a specified direction. A circular factor is allowed to wrap around the displayed linear representative, but has length no more than \(n\). Spectra retain multiplicities and the internal left-to-right order of every factor. Reversal of the entire circle is **not** factored out. These choices are essential: for three distinct gap lengths, the two opposite cyclic orders are separate necklaces and create the principal ambiguity.

## Proof
**1. Gap-spectrum lemma.** Fix gaps \(g_1,g_2,g_3\), put \(c=\max g_i\), and suppose \(k<n-c\). Then no length-\(k\) factor contains all three ones: the shortest circular arc containing the three markers skips a longest gap and has length \(n-c\). Set \(t=k-1\). We claim that \(\mathcal S_k(w)\), among all three-one circles having no three-one length-\(k\) factor, determines and is determined by \(n\) together with the **multiset of gaps strictly below \(t\)**.

Every factor with exactly two ones has the unique form \(0^p1\,0^h1\,0^q\), where \(p,q,h\ge0\) and \(p+q=k-h-2\). Its two ones are consecutive cyclic markers. If \(h\le k-2\), each gap of size \(h\) contributes exactly one occurrence for every such pair \((p,q)\): the available adjacent zero gaps both have size at least \(k-h-2\). Indeed, if the other two gaps are \(u,v\), the assumption \(k<n-c\) yields \(k-h-2\le u+v-c\le\min\{u,v\}\), since \(c\ge\max\{u,v\}\). Thus, for each \(h<t\), the multiplicity of \(1\,0^h1\,0^{k-h-2}\) is precisely the number of gaps equal to \(h\). In particular the spectrum recovers every gap strictly below \(t\), with its multiplicity.

For a one-one factor \(0^p1\,0^q\), where \(p+q=k-1\), count the markers with previous gap at least \(p\) and next gap at least \(q\). Inclusion-exclusion gives
\[
3-\#\{g_i<p\}-\#\{g_i<q\}
+\#\{i:g_{i-1}<p,\ g_i<q\}.
\]
The last term is zero: if both inequalities held, the remaining gap would be at least \(n-k\), strictly exceeding \(c\). Hence one-one factor counts depend only on the gap multiset truncated below \(t\). The all-zero factor has multiplicity \(\sum_i(g_i-k+1)_+\), also determined by the total \(n-3\) and the truncated multiset. No other factor types occur. This proves the lemma.

If \(k\ge n-c\), by contrast, some length-\(k\) factor contains all three ones. Its consecutive internal zero gaps give two **ordered** gap values; subtracting them from \(n-3\) gives the third. Thus any necklace producing that factor is the same necklace, proving uniqueness at that \(k\).

**2. Individual thresholds.** If \(a<b<c\), the two opposite cyclic orders of these three distinct gaps are different necklaces and, by the lemma, have equal spectra at every \(k<n-c\). At \(k=n-c\) a triple-marker factor gives uniqueness; hence \(K=n-c\).

When some gap lengths agree, the cyclic orientation of the multiset is unique. For \(a=b=c\), taking \(k=a+1\) forces all three gaps to be at least \(a\), and their sum \(3a\) forces equality. At the preceding \(k=a\), if \(a>0\), \((a-1,a,a+1)\) gives a distinct necklace with the same truncated data. For \(a=b<c=a+1\), \(k=a+1\) forces the sole partition of \(3a+1\) into three gaps at least \(a\); at \(k=a\), for \(a>0\), compare \((a-1,a+1,a+1)\). If \(a=b\) and \(c\ge a+2\), \(k=a+2\) reveals the two short gaps and fixes the remaining gap, whereas at \(k=a+1\) the competitor \((a,a+1,c-1)\) has the same truncated data. Finally, if \(a<b=c\), \(k=b+1\) reveals \(a\), and the two remaining gaps, both at least \(b\), must sum to \(2b\). At \(k=b\), the distinct competitor \((a,b-1,b+1)\) works when \(a<b-1\), and \((b-1,b-1,b+1)\) works when \(a=b-1\). In each comparison the word and its competitor have no length-\(k\) factor containing three ones, so the lemma applies. The one-letter length-\(n=4\) exception is unique simply because only one three-one necklace exists.

**3. Distribution.** A three-gap cyclic orbit has six ordered representatives over its three possible permutations when the lengths are distinct, hence two distinct oriented necklaces; if any two gaps coincide there is only one necklace. For a distinct sorted triple \(a<b<c\), the equality \(K=k\) fixes \(c=n-k\) and \(a+b=k-3\). Therefore
\[
\max\{0,2k-n-2\}\le a\le\left\lfloor\frac{k-4}{2}\right\rfloor,
\]
which contains exactly \(\bigl[\lfloor(k-2)/2\rfloor-\max(0,2k-n-2)\bigr]_+\) integers. The two repeated-gap families and the all-equal family contribute the remaining three terms of the stated formula. Burnside's lemma on cyclic rotations of compositions gives the displayed total number of necklaces.

**4. Sharp maximum.** For distinct gaps, the largest threshold minimizes their largest gap. The possible minimizing sorted triples are exactly those displayed in the Finding section; substituting yields \(\lfloor2n/3\rfloor\). Direct bounds on the two repeated-gap formulas show their thresholds are smaller for \(n\ge6\). Counting orientations gives the extremizer numbers.

**5. Limit law.** Only \(O(n)\) of the \(\Theta(n^2)\) three-gap necklace orbits have repeated gap lengths. For all other orbits, \(K=n-c\), with \(c\) the largest gap. Uniform sampling of integer compositions of \(n-3\) into three parts, scaled by \(n\), converges to the uniform distribution on the triangle \(x_1+x_2+x_3=1\), \(x_i\ge0\). If \(M=\max\{x_1,x_2,x_3\}\), inclusion-exclusion on the simplex gives \(\Pr(M\le u)=\sum_{j=0}^3(-1)^j\binom3j(1-ju)_+^2\). Therefore \(Y=1-M\) has the displayed distribution. Integrating its tail and second-moment tail gives \(\mathbb E[Y]=7/18\) and \(\operatorname{Var}(Y)=13/648\). Boundedness of \(Y_n\) permits convergence of its first two moments.

## Verification
Run the self-contained Python 3 script `verify.py`. It independently constructs all binary words with three ones at lengths \(3\) through \(28\), reduces them by actual string rotation, builds all cyclic length-\(k\) factor multisets without using the gap lemma, and compares the observed least unique read length with the formula above. It separately checks the closed finite distribution and worst-case extremizer counts. The completed run checked 23,751 raw words, 1,098 necklaces, and 23,841 necklace/read-length spectra, with no discrepancy. These finite experiments support, but are not substitutes for, the preceding all-length proof.

## Relationship to prior work
Pevzner's sequencing-by-hybridization formulation and the Ukkonen reconstruction criterion, as discussed explicitly by Bresler, Bresler, and Tse (2013), give general reconstructibility conditions in terms of interleaved and triple repeats. This work does not claim to introduce cyclic \(k\)-spectrum reconstruction or the general existence of repeat-based uniqueness tests. Its claimed specialization is the explicit **three-marker gap formula**, the exact **distribution of first identifying lengths and all extremizers**, and the **limiting distribution and moments**. These are not stated by the inspected primary sources and are derived here by a direct, all-length truncated-gap argument, without appealing to a generic Eulerian reconstruction algorithm. General repeat criteria address a broader qualitative decision problem, and therefore pose a genuine priority risk for the individual threshold part; the quantitative family-wide enumeration and limit law are the distinguishing claim. Karhumäki, Saarela, and Zamboni (2013) provide related \(k\)-Abelian factor-multiplicity language for linear words, which differs from circular read spectra here.

## Limitations
Only error-free, multiplicity-retaining cyclic spectra are considered; no sequencing errors, missing reads, or reverse-complement identification are allowed. No result for more than three marked symbols is asserted. The finite checker does not prove the all-length statements. A covering unpublished or differently phrased exact enumeration may exist. The historical general reconstruction criteria are credited, and no general reconstruction criterion is claimed as new. The provenance of the oldest historical materials could not be checked from all original full texts.

## References
1. G. Bresler, M. Bresler, and D. Tse, *Optimal Assembly for High Throughput Shotgun Sequencing*, arXiv:1301.0068, first publicly posted 2013-01-01; BMC Bioinformatics **14** (2013), S18. https://arxiv.org/abs/1301.0068 ; https://doi.org/10.1186/1471-2105-14-S5-S18
2. J. Karhumäki, A. Saarela, and L. Q. Zamboni, *On a Generalization of Abelian Equivalence and Complexity of Infinite Words*, arXiv:1301.5104 (2013). https://arxiv.org/abs/1301.5104
3. P. A. Pevzner, *l-Tuple DNA Sequencing: Computer Analysis*, J. Biomolecular Structure and Dynamics **7** (1989), 63–73. https://doi.org/10.1080/07391102.1989.10507752
4. E. Ukkonen, *Approximate String-Matching with q-Grams and Maximal Matches*, Theoretical Computer Science **92** (1992), 191–211. https://doi.org/10.1016/0304-3975(92)90143-4
