# A two-marker normal form for the four-run binary Burrows–Wheeler transform

## Finding
Let \(a,b,c,d\) be positive integers and let \(w=0^a1^b0^c1^d\). Append one unique sentinel \(\$\) with \(\$<0<1\); sort the suffixes of \(w\$\) lexicographically and read, in that order, their preceding symbols (with the sentinel's predecessor interpreted cyclically). This is the **sentinel suffix-array BWT**, denoted \(\operatorname{BWT}(w\$)\). Every sentinel is counted as its own letter when counting maximal constant runs.

Write \(Z=a+c\), \(O=b+d\), \((x)_+=\max(0,x)\), and define the following **one-based** positions:
\[
\begin{aligned}
u&=1+(c-a)_++\mathbf1_{\{c\ge a,\ b\ge d\}},
&v&=1+(a-c)_++\mathbf1_{\{a\ge c,\ b<d\}},\\
p&=\min(2b,b+d),
&q&=\min(2d-1,b+d).
\end{aligned}
\]
Let \(X\) be the length-\(Z\) string consisting of zeros, except \(X_u=\$\) and \(X_v=1\). Let \(Y\) be the length-\(O\) string consisting of ones, except \(Y_p=Y_q=0\). These exceptional positions are pairwise distinct within their respective strings. Then the **entire transform** has the explicit normal form
\[
\boxed{\operatorname{BWT}(w\$)=1XY.}
\]

Put \(L=\$\) if \(u=Z\), \(L=1\) if \(v=Z\), and \(L=0\) otherwise; put \(F=0\) if \(q=1\), and \(F=1\) otherwise. Its exact number \(r(a,b,c,d)\) of equal-letter runs is
\[
\boxed{\begin{aligned}
r(a,b,c,d)=9
&-\mathbf1_{\{\max(u,v)=Z\}}-\mathbf1_{\{|u-v|=1\}}\\
&-\mathbf1_{\{q=1\}}-2\mathbf1_{\{|p-q|=1\}}\\
&-\mathbf1_{\{v=1\}}-\mathbf1_{\{L=F\}}.
\end{aligned}}
\]
In particular, \(r(a,b,c,d)\le9\), with equality **if and only if**
\[
\boxed{\bigl(a>c\ge2\ \text{and}\ d\ge b+2\bigr)
\quad\text{or}\quad
\bigl(a\ge c+2\ \text{and}\ b>d\ge2\bigr).}
\]
All values \(3,4,5,6,7,8,9\) occur: respective witnesses are `(1,1,1,1)`, `(1,1,1,2)`, `(1,1,2,2)`, `(1,1,1,3)`, `(1,1,2,3)`, `(1,1,3,3)`, and `(3,1,2,3)`. The first possible length attaining nine BWT runs is \(9\).

For \(n\ge4\), let \(Q_n\) be the number of positive quadruples of sum \(n\) having nine BWT runs. The exact extremizer series and coefficient formula are
\[
\boxed{\sum_{n\ge4}Q_nz^n=\frac{2z^9}{(1-z)^2(1-z^2)^2},\qquad
Q_n=2\sum_{j=0}^{\lfloor(n-9)/2\rfloor}(j+1)(n-8-2j)\quad(n\ge9).}
\]
For a uniformly sampled positive composition of \(n\), the BWT-run count converges in distribution to an equiprobable two-point law:
\[
\boxed{\Pr(r=8)\longrightarrow\tfrac12,\qquad
\Pr(r=9)\longrightarrow\tfrac12,\qquad
\Pr(r\notin\{8,9\})\longrightarrow0.}
\]
The greatest possible run count over such words of length \(n\) is \(3\) for \(n=4\), \(5\) for \(n=5\), \(n\) for \(6\le n\le8\), and \(9\) for every \(n\ge9\).

Finally, if the same sentinel-BWT convention is applied to the reverse \(w^{\mathrm R}\), then
\[
\boxed{\frac{r(w\$)}{r(w^{\mathrm R}\$)}\le\frac94,}
\]
and equality is realized at \((a,b,c,d)=(3,3,1,2)\): the respective transforms are `1$01011010` and `00011111$0`.

## Assumptions and scope
All four run lengths are arbitrary **positive integers**; the initial symbol is zero and the final symbol is one. The lexicographic order is fixed as \(\$<0<1\). The sentinel is appended **once** and is counted as its own run. The theorem does *not* concern a sentinel-free cyclic BWT or a bijective BWT. For the random-word statement, the sample space consists of the \(\binom{n-1}{3}\) equally likely positive compositions, not uniformly random unrestricted binary words.

## Proof
**1. Suffix order.** The suffix beginning at \(\$\) is first and contributes the preceding symbol \(1\) to the BWT. Next come exactly the \(a+c=Z\) suffixes beginning with \(0\). For \(1\le k\le a\), the suffix starting \(k\) zeros before the end of the first zero run is \(0^k1^b0^c1^d\$\). For \(1\le k\le c\), the corresponding suffix from the second zero run is \(0^k1^d\$\). Larger \(k\) sorts earlier. If the two values of \(k\) tie, the first-run suffix sorts earlier precisely when \(b<d\): it then exposes a zero while the other still has a one; otherwise the second-run suffix first exposes the sentinel. The BWT predecessor of the first-run suffix is zero except when \(k=a\), where it is \(\$\), and the predecessor of the second-run suffix is zero except when \(k=c\), where it is one. Counting suffixes ahead of those two exceptions gives precisely positions \(u\) and \(v\). Thus the complete zero-leading block is \(X\).

The remaining \(b+d=O\) suffixes begin with one. A suffix beginning with exactly \(k\) ones sorts before a suffix beginning with more ones, because the former then exposes either zero or the sentinel. For tied \(k\), the last-run suffix \(1^k\$\) sorts before the first-one-run suffix \(1^k0^c1^d\$\). Their predecessors are one except at the beginning of each one run, giving one zero at \(k=b\) in the first one run and one zero at \(k=d\) in the last. Direct rank counting yields positions \(p=\min(2b,b+d)\) and \(q=\min(2d-1,b+d)\), respectively. Hence this block is \(Y\), proving the entire normal form. These rank calculations also prove \(u\ne v\) and \(p\ne q\).

**2. Exact runs.** Among the sorted zero-leading suffixes the **first** predecessor is necessarily either \(\$\) or \(1\), since it starts with the longer zero run; hence \(\min(u,v)=1\). The internal number of adjacent-symbol changes in \(X\) is exactly
\[
3-\mathbf1_{\{\max(u,v)=Z\}}-\mathbf1_{\{|u-v|=1\}}.
\]
Indeed, its two exceptional symbols are distinct, so two separated interior exceptions contribute four changes; an exception at either boundary or an adjacency deletes one of these changes, and the initial exception is always at position one.

Likewise, \(\max(p,q)=O\). Both exceptions in \(Y\) are zeros against a background of ones, so their adjacency deletes **two** changes. The internal number of changes in \(Y\) is
\[
3-\mathbf1_{\{q=1\}}-2\mathbf1_{\{|p-q|=1\}}.
\]
Here the first exception is at position one exactly when \(d=1\), equivalently \(q=1\). The transition from the initial BWT character one to the beginning of \(X\) is absent exactly when \(v=1\). The transition between \(X\) and \(Y\) is absent exactly when their boundary symbols \(L,F\) agree. Starting with one run and adding these changes gives the displayed exact run-count formula.

**3. Nine-run classification.** Every correction subtracted from \(9\) is nonnegative. Thus equality requires that all six displayed correction indicators vanish. In particular \(v\ne1\), so \(u=1\). This means either \(a>c\), or \(a=c,b<d\). The equality case \(a=c\) makes \(|u-v|=1\), so \(a>c\) is necessary. In that regime \(u=1\) and
\[
v=1+a-c+\mathbf1_{\{b<d\}}.
\]
For \(b<d\), requiring \(v\ge3\) and \(v<Z\) is equivalent to \(c\ge2\); the nonadjacency of the two zero exceptions in \(Y\), along with \(q>1\), is equivalent to \(d\ge b+2\). For \(b>d\), the same conditions on \(X\) are equivalent to \(a\ge c+2\), and those on \(Y\) to \(d\ge2\). The case \(b=d\) forces adjacent exceptions in \(Y\). Conversely, both stated parameter families make all the corrections zero: the last symbol of \(X\) is zero and the first symbol of \(Y\) is one, so the final boundary correction also vanishes. This proves the complete equality classification and the sharp bound. The smallest admissible quadruples are \((3,1,2,3)\) and \((3,3,1,2)\), both of total length nine; increasing their leading zero run produces a nine-run example at every larger length.

**4. Counting and limiting law.** In the first equality family, write \(c=2+C\), \(a=c+1+A\), \(b=1+B\), and \(d=b+2+D\), where \(A,B,C,D\ge0\). Then \(n=9+A+D+2B+2C\). The second family similarly has \(c=1+C\), \(a=c+2+A\), \(d=2+D\), and \(b=d+1+B\), producing the same weight. Summing the two disjoint families gives
\[
\frac{2z^9}{(1-z)^2(1-z^2)^2},
\]
and extracting the coefficient yields the exact expression for \(Q_n\). Its pole of order four at \(z=1\) has leading coefficient \(1/2\), so \(Q_n=n^3/12+O(n^2)\). Since \(\binom{n-1}{3}=n^3/6+O(n^2)\), the proportion of nine-run words tends to one-half.

For the remaining mass, exclude compositions with any run length below two or either \(|a-c|\le1\) or \(|b-d|\le1\). Each excluded class has \(O(n^2)\) members: fixing a small coordinate or one of the indicated bounded differences leaves at most two independent free positive integers. For every remaining composition, direct substitution in the run formula gives \(r=9\) when \(a>c\), and \(r=8\) when \(a<c\). Interchanging \(a\) and \(c\) bijects these two generic sets, so their asymptotic probabilities both tend to one-half. The values for \(4\le n\le8\) are obtained by complete finite enumeration of the \(1,4,10,20,35\) respective compositions; the provided verifier executes this exhaustive calculation. For \(n\ge9\), the optimizer classification proves that the maximum is nine.

**5. Reversal bound.** The reverse word begins with one and ends with zero; its sentinel BWT therefore begins with zero (the predecessor of the sentinel suffix). Among the following zero-leading suffixes there is a suffix at the beginning of a zero run preceded by one. Among the subsequent one-leading suffixes there are distinct predecessors zero (at the second one-run beginning) and \(\$\) (at the whole-word beginning). Thus its BWT contains, in order, a zero, a one, and then both zero and \(\$\) in some order. These four symbols force at least four constant runs. Dividing the sharp forward bound nine by this lower bound four proves the ratio inequality. The displayed length-nine witness attains both bounds.

## Verification
Run `python verify_bwt.py` with Python 3.9 or later. It builds the BWT **independently** by sorting literal suffixes, then compares every output symbol and run count with the arithmetic normal form for all \(8^4=4096\) positive parameter quadruples of run lengths at most eight. It checks a further \(1000\) deterministic random quadruples with run lengths at most 150, exhaustively counts all positive compositions at each total length from \(4\) through \(28\), compares every nine-run optimizer with its classification and the exact coefficient formula, and tests the reverse bound and the sharp witness. Expected final output begins with `VERIFY_OK`. These computations are finite checks only; the unrestricted theorem and limiting distribution follow from the preceding proof.

## Relationship to prior work
The run count of the BWT is an established compressed-indexing measure, and the 2020 work of Giuliani, Inenaga, Lipták, Prezza, Sciortino and Toffanello analyzes dramatic **reversal asymmetry** on Fibonacci/standard-word extensions. Crucially, that paper primarily defines a **sentinel-free cyclic BWT**, so its run counts cannot be directly identified with the sentinel suffix-array convention used here. Nishimoto, Kanda and Tabei (2022) analyze construction of the run-length **suffix-array BWT with a terminal sentinel** in general. Giuliani, Lipták and Masillo (2022) study **where sentinels can be inserted into prospective BWT output words**, focusing on fully clustered output; that inverse-image problem is different from the forward run profile of a prescribed four-run input. These inspected sources do not state the two-exceptional-position normal form, nine-run optimizer classification, or two-point distribution proved here. The general machinery could in principle rederive special cases, and an equivalent unindexed specialization is a residual originality risk.

## Limitations
The bound, optimizer families, generating function, and reversal ratio apply only to the stated four-run orientation, fixed alphabet order, and single-sentinel suffix-array convention. Complementing the input or changing sentinel rules can change the BWT run count. The two-point law samples positive compositions, not unrestricted random binary strings. No assertion is made about optimality over all binary words or about a sentinel-free cyclic BWT. The result has been checked internally but has not received independent mathematical audit, and absolute global literature uniqueness is not claimed.

## References
1. S. Giuliani, S. Inenaga, Z. Lipták, N. Prezza, M. Sciortino, A. Toffanello, *Novel Results on the Number of Runs of the Burrows-Wheeler-Transform*, arXiv:2008.08506v1 (first submitted 2020-08-19), https://arxiv.org/abs/2008.08506 .
2. T. Nishimoto, S. Kanda, Y. Tabei, *An Optimal-Time RLBWT Construction in BWT-runs Bounded Space*, arXiv:2202.07885v1 (first submitted 2022-02-16), https://arxiv.org/html/2202.07885v1 .
3. S. Giuliani, Z. Lipták, F. Masillo, *When a Dollar in a Fully Clustered Word Makes a BWT*, ICTCS 2022, CEUR Workshop Proceedings 3284, pp. 122–135, https://ceur-ws.org/Vol-3284/4242.pdf .
