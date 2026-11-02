# Exact circular Abelian spectra of finite Cantor words by binary carries

## Finding
Let \(C_0=1\), \(C_n=C_{n-1}0^{3^{n-1}}C_{n-1}\) for \(n\ge1\). Thus \(C_n\) has length \(N=3^n\) and exactly \(T=2^n\) ones. A *circular factor* of length \(\ell\), where \(1\le\ell\le N\), is a string of \(\ell\) successive symbols read modulo \(N\). Let \(p_n^\circ(\ell)\) count the distinct Parikh vectors of these factors; because the alphabet is binary, it counts the distinct attainable numbers of ones.

For a nonnegative integer \(s=\sum_{j\ge0}\epsilon_j 2^j\) with \(\epsilon_j\in\{0,1\}\), define the binary-to-ternary map
\[
 B(s)=2\sum_{j\ge0}\epsilon_j3^j.
\]
Define \(d(1)=1\); for \(m\ge2\), put \(s=m-2\) and
\[
 d(m)=2+B(s)-R(s),\qquad
 R(s)=\begin{cases}
 3^{\lfloor\log_2s\rfloor}-3^{\nu_2(s+1)},&s\ge1\text{ and }\nu_2(s+1)\le\lfloor\log_2s\rfloor,\\
 0,&\text{otherwise}.
 \end{cases}
\]
Here \(\nu_2(a)\) for positive \(a\) is the largest \(r\) such that \(2^r\mid a\). For each \(n\ge1\) and \(1\le m\le2^n\), **\(d(m)\) is the shortest possible length of a circular factor of \(C_n\) containing at least \(m\) ones**. In particular this threshold is independent of \(n\) once \(m\le2^n\).

Put \(M_n(0)=0\) and, for \(0\le\ell\le N\),
\[
 M_n(\ell)=\#\{m\in\{1,\ldots,2^n\}:d(m)\le\ell\}.
\]
Then the complete lengthwise circular Abelian spectrum is
\[
 \boxed{p_n^\circ(\ell)=M_n(\ell)+M_n(N-\ell)-2^n+1}\quad(1\le\ell\le N),
\]
and the exact *total* number of distinct length-tagged circular Parikh classes is
\[
 \boxed{\sum_{\ell=1}^{3^n}p_n^\circ(\ell)=3^n+\frac{2(6^n-1)}5}. \tag{1}
\]
The sequence for \(n=1,2,3,4,5\) is \(5,23,113,599,3353\). Classes at different lengths are counted separately. All statements concern the fixed binary alphabet and at most one complete traversal.

## Assumptions and scope
One positions are zero based. Their increasing list is \(B(0),B(1),\ldots,B(2^n-1)\), since a position is a one exactly when its \(n\)-digit ternary expansion uses only \(0,2\). The circular factor length is an integer between \(1\) and \(3^n\) inclusive. An arc containing at least \(m\) ones may contain more than \(m\); its length counts both endpoints when both are included. The theorem asserts no formula for arbitrary prefixes of the infinite Cantor sequence or for multiple traversals of \(C_n\).

## Proof
**Step 1: the cyclic gap ruler.** Set \(T=2^n\). The successive cyclic gaps between one positions, indexed \(j\) modulo \(T\), have lengths \(g_0=1\) for the wrap from the last one to the first, and
\[
 g_j=B(j)-B(j-1)=1+3^{\nu_2(j)},\qquad 1\le j<T.
\]
Indeed, incrementing \(j-1\) to \(j\) changes its trailing \(\nu_2(j)\) binary ones to zeros and changes the next zero to one, whence the displayed formula. Write \(h_j=g_j-1\), so \(h_0=0\) and \(h_j=3^{\nu_2(j)}\) for nonzero residues.

For \(0\le j<T\), we have the exact identity
\[
 h_j=1+2\sum_{a=1}^{n-1}3^{a-1}{\bf1}_{2^a\mid j}
      -3^{n-1}{\bf1}_{j=0\pmod T}. \tag{2}
\]
For any \(0<q<T\), every cyclic interval of \(q\) residue classes has either \(\lfloor q/2^a\rfloor\) or \(\lceil q/2^a\rceil\) multiples of \(2^a\). Comparing such a block \(I\) containing zero to any such block \(J\) avoiding zero, (2) gives
\[
 \sum_{j\in I}h_j-\sum_{j\in J}h_j
 \le 2\sum_{a=1}^{n-1}3^{a-1}-3^{n-1}=-1.
\]
Thus **every** minimum-sum cyclic block of \(q\) consecutive gaps contains the wrap gap \(g_0\). This is stronger than merely exhibiting a good boundary arc. For \(m\ge2\), the minimum span of \(m\) consecutive ones consists of one plus \(m-1\) successive gaps. Since \(m-1<T\), the optimizing gap block includes \(g_0\), and can be written \(-a,\ldots,0,\ldots,b\), where \(a,b\ge0\), \(a+b=m-2\). Symmetry \(h_{-j}=h_j\) and the telescoping identity \(\sum_{j=1}^a h_j=B(a)-a\) yield
\[
 d(m)=m+\min_{a+b=m-2}\left(B(a)-a+B(b)-b\right)
     =2+\min_{a+b=m-2}(B(a)+B(b)). \tag{3}
\]
For \(m=1\), a single one has span one.

**Step 2: solve the binary carry optimization.** Fix \(s\ge0\) and add \(a+b=s\) in base two. Let \(c_j\in\{0,1\}\) be the carry into bit \(j\), with \(c_0=0\), and \(s_j\) the bits of \(s\). From \(a_j+b_j+c_j=s_j+2c_{j+1}\) one obtains exactly
\[
 B(a)+B(b)=B(s)-2\sum_{j\ge1}3^{j-1}c_j. \tag{4}
\]
For \(s\ge1\), put \(h=\lfloor\log_2s\rfloor\). No carries above bit \(h\) are possible. With incoming carry zero, a binary one in \(s\) cannot initiate a carry; therefore all carries \(c_j\) vanish through the initial run of ones. If \(r=\nu_2(s+1)\le h\), the first zero of \(s\) is bit \(r\). The pointwise largest feasible carry pattern is \(c_{r+1}=\cdots=c_h=1\), zero elsewhere: initiate the carry at bit \(r\), propagate it, and terminate at the leading one bit \(h\). At every bit the required sum of the two input bits is \(0,1\), or \(2\), so this pattern is realizable by nonnegative \(a,b\). Since all weights in (4) are positive, it maximizes the reduction. Its contribution is \(2\sum_{j=r+1}^h3^{j-1}=3^h-3^r\). If \(s\) is all ones below and including bit \(h\), or \(s=0\), no nonzero carry can occur. Substituting into (3) gives exactly the stated \(d(m)\).

**Step 3: every lengthwise class.** For a fixed \(\ell\), let \(A_\ell\) be the maximum number of ones in any circular factor of length \(\ell\). Since a factor contains at least \(m\) ones if and only if some circular arc of length at most \(\ell\) contains \(m\), one has \(A_\ell=M_n(\ell)\). Extend shorter arcs to length \(\ell\) if necessary. The minimum one count is \(T-M_n(N-\ell)\), because the complement of a circular length-\(\ell\) factor is a circular factor of length \(N-\ell\). The case \(N-\ell=0\) has maximal one count zero. Adjacent length-\(\ell\) windows have one counts differing by at most one; as the starting point runs around the circle, all integers between the minimum and maximum appear. Thus \(p_n^\circ(\ell)=A_\ell-(T-M_n(N-\ell))+1\), establishing the full spectrum.

**Step 4: closed total.** Each threshold \(d(m)\) contributes to \(M_n(\ell)\) for exactly \(N-d(m)+1\) lengths \(1\le\ell\le N\), and to \(M_n(N-\ell)\) for exactly \(N-d(m)\) such lengths. Therefore
\[
 \sum_{\ell=1}^N p_n^\circ(\ell)
 =N+(N+1)T-2\sum_{m=1}^T d(m). \tag{5}
\]
It remains to evaluate the threshold sum. Let \(s=m-2\). The binary-to-ternary digit sum satisfies
\[
 \sum_{s=0}^{2^n-2}B(s)=(2^{n-1}-1)(3^n-1).
\]
For \(h=1,\ldots,n-1\), exactly \(2^{h-r-1}\) numbers \(s\) have leading bit \(h\) and first zero bit \(r<h\). Their aggregate carry reductions are
\[
 \sum_{r=0}^{h-1}2^{h-r-1}(3^h-3^r)=6^h-2\cdot3^h+2^h.
\]
Summing over \(h\) yields
\[
 \sum_{s=0}^{2^n-2}R(s)=\frac{6^n-6}{5}-3^n+2^n+1.
\]
Together with \(d(1)=1\), this gives
\[
 \sum_{m=1}^{T}d(m)
 =\frac{T(N+1)}2-\frac{6^n-1}{5}.
\]
Substitution into (5) proves (1).

## Verification
Run `python3 checker.py` in the same directory as this document. It independently constructs \(C_n\), finds the shortest cyclic spans of all possible one counts by direct enumeration of positions, and separately enumerates the minimum and maximum one counts of every circular factor length. It compares those results against the digit formula, the full lengthwise spectrum, the total count, and the threshold-sum identity, for each rank \(1\le n\le7\). All checks passed. This finite replay does not replace the unrestricted proof above.

## Relationship to prior work
Cassaigne, Fici, Sciortino and Zamboni (arXiv:1402.5843, first public version 24 February 2014) study *conjugacy classes of contiguous factors of infinite words*, called cyclic complexity. Here factors themselves wrap around one **finite** Cantor iterate and are compared only by Parikh vectors; these equivalence relations and source languages differ. Lü, Chen, Guo and Wen (DOI 10.1016/j.tcs.2015.12.022, 2016) investigate factor and permutation complexity of infinite Cantor-like sequences. Chen, Lü and Wu (arXiv:1703.04063, 2017), Section 2, show that the maximal one count of an ordinary factor of the *infinite* Cantor sequence is attained at its prefix and derive 3-regularity. Their result does not directly compute circular factors of a finite iterate or the binary-carry gap minimization and total (1). Bulgakova, Buzhinsky and Goncharov (arXiv:2012.15818, 2020) classify balanced circular words over a ternary alphabet under a small Abelian-complexity bound, a different domain. These are precise non-implication comparisons of the inspected statements, not an assertion of exhaustive historical priority.

## Limitations
All formulas require complete finite Cantor iterates over the binary alphabet. The count is length-tagged and does not count distinct strings, cyclic conjugacy classes, or occurrences. No claim about non-complete prefixes, factors traversing the circle more than once, or arbitrary Cantor-like substitutions follows. A literature search, even when negative, cannot prove novelty; an independently conducted priority check and external mathematical validation have not been performed.

## References
1. J. Cassaigne, G. Fici, M. Sciortino and L. Q. Zamboni, *Cyclic Complexity of Words*, arXiv:1402.5843 (first version 2014-02-24), https://arxiv.org/abs/1402.5843.
2. X.-T. Lü, J. Chen, Y.-J. Guo and Z. Wen, *On the permutation complexity of the Cantor-like sequences*, Theoretical Computer Science 616 (2016), 100–110, https://doi.org/10.1016/j.tcs.2015.12.022.
3. J. Chen, X. Lü and W. Wu, *On the \(k\)-Abelian complexity of the Cantor sequence*, arXiv:1703.04063 (first version 2017-03-12), https://arxiv.org/abs/1703.04063.
4. D. V. Bulgakova, N. Buzhinsky and Y. O. Goncharov, *On balanced and abelian properties of circular words over a ternary alphabet*, arXiv:2012.15818 (first version 2020-12-31), https://arxiv.org/abs/2012.15818.
