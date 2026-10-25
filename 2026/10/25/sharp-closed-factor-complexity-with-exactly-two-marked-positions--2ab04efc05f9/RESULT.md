# Sharp closed-factor complexity with exactly two marked positions

## Finding

For nonnegative integers \(a,b,c\), let \(w=0^a1\,0^b1\,0^c\) and \(n=a+b+c+2\). A nonempty word is **closed** if its length is one or it has a nonempty proper border (a common prefix and suffix) occurring at exactly its two endpoint positions; equivalent standard conventions allow the empty border for one-letter words. Let \(C(w)\) be the number of *distinct, nonempty* closed contiguous factors of \(w\). Put \(A=\min(a,b)\) and \(B=\min(b,c)\). Then

\[
\boxed{C(w)=n+\max(A,B)\bigl(\min(A,B)+1\bigr).}
\]

This is also a complete characterization: the closed factors are exactly all zero-powers occurring in \(w\); the factor \(1\); all \(0^t1\,0^t\) that occur; and the factors \(0^i1\,0^b1\,0^j\) with \(0\le i\le a\), \(0\le j\le c\) satisfying \(i=j\) **or** \((i\le b\text{ and }j\le b)\).

Write \(s=n-2=3k+r\), \(r\in\{0,1,2\}\). The exact maximum over all binary words of length \(n\) with two ones is

\[
\max_{|w|=n,\ |w|_1=2}C(w)=
\begin{cases}
 k^2+4k+2,&r=0,\\
 k^2+4k+3,&r=1,\\
 k^2+5k+5,&r=2.
\end{cases}
\]

Every maximizing ordered zero-gap triple \((a,b,c)\) is as follows. For \(r=0\), only \((k,k,k)\). For \(r=1\), all three permutations of \((k,k,k+1)\), and, when \(k\ge1\), also \((k-1,k+1,k+1)\) and \((k+1,k+1,k-1)\). For \(r=2\), precisely \((k,k+1,k+1)\) and \((k+1,k+1,k)\). The list includes \(n=2\) and \(n=3\).

In particular, the extremal closed-factor count is \(n^2/9+O(n)\) with only **two** occurrences of the minority letter. In contrast, a binary word of length \(n\) with zero or one occurrence of that letter has exactly \(n\) distinct nonempty closed factors. Thus two minority-letter occurrences are the smallest possible fixed minority support that permits quadratic growth. For uniformly chosen weight-two words of length \(n\), the average is \(n^2/36+O(n)\).

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\), the word is linear rather than circular, occurrences and factors are contiguous, factor multiplicities are discarded, and closed factors are counted by distinct **contents**. The empty word is excluded: to use the convention counting it, add one to every count. All displayed identities hold for every integer \(n\ge2\) and all nonnegative gaps. No claim is made about general alphabets, other Hamming weights, or globally maximal closed-factor complexity among unrestricted binary words.

## Proof

**1. Exhaust the possible factors.** Any nonempty factor contains zero, one, or two occurrences of \(1\). The zero-only factors are precisely \(0^t\), \(1\le t\le L:=\max(a,b,c)\), and all are closed. The single-letter factor \(1\) is closed. A factor with one \(1\) is \(0^i1\,0^j\). It cannot have a proper border containing its unique \(1\): two shifted occurrences of such a border would place the \(1\) at two positions. A zero-only border occurs exactly at the endpoints if and only if \(i=j>0\). Hence the other one-marker closed factors are \(0^t1\,0^t\) for \(1\le t\le \max(\min(a,b),\min(b,c))=\min(b,\max(a,c))\).

Every factor with both \(1\)s is uniquely \(f_{ij}=0^i1\,0^b1\,0^j\), where \(0\le i\le a\), \(0\le j\le c\). Any proper border containing a \(1\) must match the first marker with the second, so it exists exactly when \(i\le b\) and \(j\le b\); then \(0^i1\,0^j\) occurs only at the prefix and suffix, since there are only two markers. A border containing both markers is impossible because a nonzero shift cannot preserve the two-element set of marker positions. If there is no marker-containing border, a nonempty border must consist only of zeros. Such a zero-border has no internal occurrence exactly when \(i=j>0\) and the middle gap is shorter than \(i\); if \(i=j\le b\), the preceding marker-border already proves closedness. Consequently, the complete condition for \(f_{ij}\) is \(i=j\) or \((i\le b\text{ and }j\le b)\). The cases \(i=0\) or \(j=0\) follow by the same border argument.

**2. Count all closed factors.** Each palindrome listed above is closed. The distinct palindromic factors comprise the \(L\) zero-powers, \(1\), the \(\min(b,\max(a,c))\) one-marker palindromes beyond \(1\), and the \(\min(a,c)+1\) two-marker palindromes \(f_{ii}\). Their total is

\[
L+1+\min(b,\max(a,c))+\min(a,c)+1=a+b+c+2=n.
\]

Every additional closed factor is a **nonpalindromic** two-marker factor \(f_{ij}\) with \(i\ne j\), \(0\le i\le A\), \(0\le j\le B\). There are \((A+1)(B+1)-(\min(A,B)+1)=\max(A,B)(\min(A,B)+1)\) of them. This gives the exact formula and the explicit factor classification. (A distinct factor may have several occurrences in the ambient word, but each displayed word content is counted just once.)

**3. Optimize exactly.** Let \(u=\min(a,c)\), \(v=\max(a,c)\), and put \(p=\min(b,u)\), \(q=\min(b,v)\), so \(0\le p\le q\). Since \(s=a+b+c\), necessarily \(p+2q\le s\). Conversely any integers \(0\le p\le q\) with \(p+2q\le s\) can be realized by \((a,b,c)=(p,q,s-p-q)\), because \(s-p-q\ge q\). Thus the excess to maximize is precisely \(q(p+1)\) over these integer pairs.

For fixed \(q\), the best \(p\) is \(\min(q,s-2q)\). Write \(s=3k+r\) with \(r\in\{0,1,2\}\). For \(q\le k\), the bound \(q(q+1)\) is strictly increasing in \(q\). For \(q\ge k+1\), the bound is \(q(s-2q+1)\), and the difference at consecutive \(q\) is \(s-4q-1<0\). Therefore only \(q=k\) and (when feasible) \(q=k+1\) can maximize. Direct comparison gives maximum excess \(k(k+1)\) for \(r=0,1\) and \((k+1)^2\) for \(r=2\). Tracking the equality constraints \(p+2q\le s\) and the at-most-one unit of slack gives exactly the listed gap triples; for \(s=1\), the infeasible candidate \(q=1\) is discarded. Adding \(n\) yields the stated maximum.

**4. The quadratic threshold and the mean.** With at most one \(1\), the only nonempty closed factors are \(0^t\), \(1\) when present, and symmetric \(0^t1\,0^t\), so their number is exactly the word length. At two ones, the maximum found above is \(n^2/9+O(n)\). For the mean, divide gaps by \(s=n-2\) and use uniform convergence of the lattice-point distribution on \(x+y+z=1\), \(x,y,z\ge0\). The leading excess divided by \(s^2\) tends to \(\min(x,y)\min(z,y)\). With \(t_1\le t_2\le t_3=1-t_1-t_2\), two of the six coordinate orderings give \(t_1^2\), and the other four give \(t_1t_2\). The simplex density is \(2\), so

\[
\begin{aligned}
\mathbb E[\min(X,Y)\min(Z,Y)]
 &=2\int_0^{1/3}\int_{t_1}^{(1-t_1)/2}(2t_1^2+4t_1t_2)\,dt_2\,dt_1\\
 &=\frac1{36}.
\end{aligned}
\]

The integrand is piecewise polynomial and Lipschitz on a compact triangle; the corresponding lattice Riemann-sum error is \(O(1/s)\), giving \(\mathbb E[C(w)]=n^2/36+O(n)\).

## Verification

The included `verify.py` computes closedness directly from all borders and their occurrence multiplicities, without consulting the structural formula. It checks the **entire set** of closed factors against the classification, the exact count, and all maximizing triples for every \(n=2,\ldots,16\) (680 distinct weight-two words). It also tests the formula's maximizing triples by independent integer enumeration through \(n=100\), and the zero/one-marker boundary through \(n=34\). Run `python3 verify.py` from the package directory. These finite checks corroborate, but do not replace, the preceding all-length proof.

## Relationship to prior work

Badkobeh, Fici and Lipták (2013 preprint, 2015 publication) introduced general enumeration of distinct closed factors, established the \(n+1\) lower bound **including the empty word**, and proved that binary words can have quadratically many closed factors. Their general quadratic construction employs two blocks of repeated nonzero letters, while their table gives unrestricted binary maxima for lengths at most 20. The present statement is a different restricted extremum: an exact all-length formula, every optimizer, and a minimum minority-support threshold of **two isolated occurrences**. It is not a numerical reformulation of the unrestricted maxima, whose optimizers need not have weight two.

The 2016 *Closed factorization* work studies general algorithms for longest/shortest closed factors and their factorizations rather than presenting, in its available abstract, an enumeration of distinct closed factors at fixed Hamming weight. Its full text could not be inspected for the present comparison, so priority over any hidden special case is not claimed. The earlier terminology *periodic-like word* and *complete first return* describes the same objects and was included in overlap searches. Existing indexed unrestricted closed-rich maxima at a few larger lengths do not determine this all-length fixed-weight-two formula or its optimizer classification.

## Limitations

The result is mathematical and deterministic. It does not imply the general maximum for arbitrary binary words, nor any claimed new general closed-factor counting algorithm. Searches and accessible primary-source comparisons support, but do not certify, priority: an obscure earlier exact two-marker classification could exist; the full 2016 algorithmic paper was inaccessible. Verification uses finite checks plus the displayed symbolic proof, not formal machine proof or independent external review.

## References

1. G. Badkobeh, G. Fici, and Zs. Lipták, *On the Number of Closed Factors in a Word*, arXiv:1305.6395, first public version 28 May 2013; later in LATA 2015. https://arxiv.org/abs/1305.6395.
2. G. Badkobeh, H. Bannai, K. Goto, T. I, C. S. Iliopoulos, S. Inenaga, S. J. Puglisi, and S. Sugimoto, *Closed factorization*, Discrete Applied Mathematics **212** (2016), 23–29, https://doi.org/10.1016/j.dam.2016.04.009 (early online 14 May 2016).
3. J. Peltomäki, *Introducing Privileged Words: Privileged Complexity of Sturmian Words*, arXiv:1210.3146, first public version 11 October 2012; Theoretical Computer Science **500** (2013), 57–67. Background on complete returns and palindromic richness, not evidence of this formula.
