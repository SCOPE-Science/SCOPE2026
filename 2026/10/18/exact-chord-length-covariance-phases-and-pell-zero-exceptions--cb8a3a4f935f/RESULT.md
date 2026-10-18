# Exact chord-length covariance phases and Pell-zero exceptions

## Finding

Let \(C_n\) denote the number of crossing pairs of chords in a uniformly random perfect matching of \(2n\) cyclically ordered, labeled endpoints, \(n\ge2\). For each integer \(0\le j\le n-1\), let \(L_{n,j}\) count chords whose *shorter cyclic arc* contains exactly \(j\) other endpoints. The case \(j=0\) consists of simple adjacent chords, while \(j=n-1\) consists of diameters. Then
\[
\boxed{\operatorname{Cov}(C_n,L_{n,j})
=\frac{h_{n,j}}{2n-1}\left(\frac{j(2n-2-j)}{2n-3}-\frac{n-1}{3}\right),}
\qquad h_{n,j}=\begin{cases}2n,&0\le j\le n-2,\\ n,&j=n-1.\end{cases}
\]
Let \(t=n-1\) and \(r_n=t-\sqrt{t(t+1)/3}\). For every admissible \(j\), the covariance is **negative** precisely when \(j<r_n\), **positive** precisely when \(j>r_n\), and **zero** precisely when \(j=r_n\). The zero cases form the infinite, exponentially sparse Pell family
\[
\boxed{(n,j)=(4,1),(49,20),(676,285),(9409,3976),\ldots.}
\]
More exactly, all zero pairs with \(n\ge2\) arise, with \(k\ge1\), from
\[
 x_k+b_k\sqrt{12}=(7+2\sqrt{12})^k,\qquad
 n=\frac{x_k+1}{2},\qquad j=\frac{x_k-1}{2}-b_k.
\]
For every \(n\ge2\), no other zero is possible. The complete profile satisfies the exact conservation identity \(\sum_{j=0}^{n-1}\operatorname{Cov}(C_n,L_{n,j})=0\).

## Assumptions and scope

Each of the \((2n-1)!!\) perfect matchings is equally likely, and endpoints lie in cyclic order. If a chord joins positions \(a<b\), its shorter-arc interior endpoint count is \(j=\min\{b-a-1,2n-b+a-1\}\). This fixes the convention for antipodal chords and for the closing adjacency edge. All claims are finite, exact identities; there are no independence assumptions between crossings and the chord-length profile.

## Proof

Fix two distinct endpoints \(a<b\) whose shorter arc contains \(j\) other endpoints, and let \(I_{a,b}\) indicate their matching. Its probability is \(1/(2n-1)\). Conditional on \(I_{a,b}=1\), the remaining \(2n-2\) endpoints have a uniform matching. Their internal crossings have the law of the crossing count for \(n-1\) chords because removing a prescribed chord preserves the cyclic order of all other endpoints. A chord between the \(j\) endpoints inside the shorter arc and the \(2n-2-j\) outside crosses \((a,b)\); each such possible inside–outside chord occurs conditionally with probability \(1/(2n-3)\). Therefore
\[
\mathbb E[C_n\mid I_{a,b}=1]
=\frac{(n-1)(n-2)}6+\frac{j(2n-2-j)}{2n-3}.
\]
The known crossing expectation \(\mathbb EC_n=n(n-1)/6\) can also be proved directly: each ordered four-set supports its unique crossing pairing with probability \(1/[(2n-1)(2n-3)]\). Consequently
\[
\operatorname{Cov}(C_n,I_{a,b})
=\frac1{2n-1}\left(\frac{j(2n-2-j)}{2n-3}-\frac{n-1}3\right).
\]
There are \(2n\) possible chords of each cyclic type \(0\le j\le n-2\), because each has a unique shorter directed arc with \(j\) interior endpoints; there are only \(n\) diameters when \(j=n-1\), as the two directed arcs then tie. Summing the fixed-chord identity proves the boxed covariance formula.

Since the multiplier \(h_{n,j}/(2n-1)\) is positive, the covariance sign is that of
\[
3j(2t-j)-t(2t-1)
=t(t+1)-3(t-j)^2.
\]
For integer \(0\le j\le t\), this expression increases strictly with \(j\). Its sole real root on that interval is \(r_n=t-\sqrt{t(t+1)/3}\), giving the sign classification. A zero occurs exactly when \(t(t+1)=3b^2\) with \(b=t-j\in\mathbb Z_{\ge0}\). Completing a square with \(x=2t+1\) gives
\[
 x^2-12b^2=1,\qquad x\text{ odd},\quad x\ge3.
\]
The positive integer solutions are exactly \(x+b\sqrt{12}=(7+2\sqrt{12})^k\) for \(k\ge1\), by the elementary Pell equation for \(x^2-3y^2=1\) with \(y=2b\): the smallest solution with even \(y>0\) is \((x,y)=(7,4)\), and all even-\(y\) solutions are its powers. Conversely each power gives admissible \(t=(x-1)/2\), \(j=t-b\), since \(0<b<t\) for \(k\ge1\). This proves completeness and infinitude of the zero family.

Finally, \(\sum_{j=0}^{n-1}L_{n,j}=n\) deterministically because every chord has exactly one shorter-arc length type. Its covariance with \(C_n\) vanishes, proving conservation.

## Verification

The standalone Python file `verify.py` enumerates all \((2n-1)!!\) perfect matchings for \(2\le n\le7\), computes every crossing count and every chord-length profile, and checks all predicted covariances using exact rational arithmetic. It checks crossing means, the conservation sum, the zero criterion, and the first four Pell solutions using the exact recurrence. The packaged checker reports **111 exact assertions passed**. Exhaustion applies only to the stated finite cases; the all-size assertions follow from the preceding proof.

## Relationship to prior work

Paguyo's *Convergence rates of limit theorems in random chord diagrams* (arXiv:2104.01134, first submitted April 2, 2021) studies crossing counts and cyclic simple chords; its concluding section introduces length-\(j\) chord counts and discusses their marginal Poisson approximation. The classical crossing mean and conditional probability for a fixed chord are not new. The present contribution is the **complete mixed length–crossing covariance profile**, the sharp sign threshold, and the infinite Pell classification of the exact zeros. The previously recorded simple-chord–crossing covariance is exactly the \(j=0\) specialization and is not asserted to be new here. Young's work on linear chord diagrams treats short-chord marginals, not this finite cyclic length-dependent profile. Search and inspection did not establish an already published equivalent Pell classification; the possibility that a general mixed-moment theory implicitly implies it remains a priority risk.

## Limitations

The result concerns the uniform model with cyclic endpoint ordering, and covariance with the **total crossing count**. It does not characterize the full joint distribution for nonzero chord lengths, independence at the zero points, or covariance between different length classes. The zero cases mean only that one linear covariance vanishes; they do not imply independence. Pell sparseness is with respect to matching size, not a probability statement. Independent mathematical auditing and exhaustive historical-priority confirmation have not been performed.

## References

- J. E. Paguyo, *Convergence rates of limit theorems in random chord diagrams*, arXiv:2104.01134 (first public April 2, 2021), https://arxiv.org/abs/2104.01134 ; full text https://arxiv.org/html/2104.01134
- D. Young, *Linear k-Chord Diagrams*, arXiv:2004.06921 (2020), https://arxiv.org/abs/2004.06921
- P. Flajolet and M. Noy, *Analytic Combinatorics of Chord Diagrams*, Formal Power Series and Algebraic Combinatorics (2000).
- H. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489 (2015), https://arxiv.org/abs/1501.01489
