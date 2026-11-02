# Dyadic two-binomial spectra of the regular paperfolding word

## Finding

For each positive integer \(t\), write \(t=2^e u\) with \(u\) odd and define the binary paperfolding word \(p_t=1\) if \(u\equiv1\pmod4\), and \(p_t=0\) otherwise. This convention is the bitwise complement of the convention in Madill--Rampersad (2012); relabeling the alphabet does not change binomial complexity.

For a binary word \(v\), let \(r(v)\) denote its number of ones and let \(q(v)\) denote the number of scattered occurrences of \(01\). Define \(\mathcal B(n)=\{(r(v),q(v)):v\text{ is a length-}n\text{ factor of }p\}\). These are exactly the \(2\)-binomial equivalence profiles at length \(n\).

**Theorem.** For every integer \(k\ge2\), set \(n=2^k\). The set \(\mathcal B(n)\) has three disjoint layers distinguished by their numbers of ones:

1. There are exactly \(n\) profiles with \(r=n/2-1\).
2. There are exactly \(n\) profiles with \(r=n/2+1\). Their \(q\)-value sets coincide with those of the first layer.
3. The profiles with \(r=n/2\) have precisely the \(k+1\) values
   \[
   q=\frac{n(n-2k)}8+\frac n2 j,\qquad j=0,1,\ldots,k.
   \]

Consequently, the \(2\)-binomial complexity is exactly
\[
\boxed{b^{(2)}_p(2^k)=2^{k+1}+k+1\qquad(k\ge2).}
\]
This is a complete characterization of the possible one-letter count and scattered \(01\)-count for factors of these lengths, up to the explicit outer-layer construction in the proof.

## Assumptions and scope

Factors are ordinary *contiguous* finite factors of the one-sided infinite paperfolding word. Inside each factor, subsequence occurrences are *scattered* and counted with multiplicity. Positions of the infinite word start at \(1\); positions within a factor in the moment calculation start at \(1\). All assertions are for \(k\ge2\); no statement about arbitrary lengths is implied.

A binary length-\(n\) factor is \(2\)-binomially classified by \((r,q)\): its \(00\)-count is \(\binom{n-r}{2}\), its \(11\)-count is \(\binom r2\), and its \(10\)-count is \(r(n-r)-q\). Thus the stated set precisely indexes the classes.

## Proof

**1. Four explicit cyclic templates give all factors.** Fix \(n=2^k\), \(k\ge2\), and use residue indices \(0\le h<n\). For \(\alpha,\beta\in\{0,1\}\) define a length-\(n\) word \(W^{\alpha\beta}\) by setting \(W^{\alpha\beta}_0=\alpha\), \(W^{\alpha\beta}_{n/2}=\beta\), and \(W^{\alpha\beta}_h=p_h\) for other residues \(h\). Every length-\(n\) factor is a cyclic rotation of one of these four templates: if \(h\notin\{0,n/2\}\), then \(\nu_2(h)\le k-2\), so adding any multiple of \(n\) to \(h\) preserves its odd part modulo \(4\). Only the two exceptional residues can vary.

Conversely every cyclic rotation of each of the four templates occurs. For a window starting at an absolute position \(an+s\), with \(a\ge1\) and \(0\le s<n\), the exceptional symbols in their residue order are: for \(s=0\), \((p_a,\mathbf 1[a\text{ even}])\); for \(1\le s\le n/2\), \((p_{a+1},\mathbf 1[a\text{ even}])\); and for \(n/2<s<n\), \((p_{a+1},\mathbf 1[a+1\text{ even}])\). In the first case \(a\in\{1,2,3,6\}\), in the second \(a\in\{1,2,4,5\}\), and in the third \(a+1\in\{2,3,5,6\}\) realize all four ordered bit pairs. Hence every phase and choice \((\alpha,\beta)\) occurs. (For \(s=0\), the first template position is the residue \(0\).)

**2. The outer layers have exactly \(n\) values apiece.** For every \(0<h<n\) with \(h\ne n/2\), the residues \(h\) and \(n-h\) satisfy \(p_h+p_{n-h}=1\), because \(2^{k-\nu_2(h)}\) is divisible by \(4\). The fixed positions therefore contain exactly \((n-2)/2\) ones. Thus the four templates have weights \(n/2-1,n/2,n/2,n/2+1\) in the order \(00,01,10,11\).

For any cyclic word \(V\) of length \(n\) and weight \(r\), define its one-position moment in the rotation by \(s\) as \(T_s=\sum_{j=1}^n jV_{(s+j-1)\bmod n}\). Sliding one position gives
\[
T_{s+1}=T_s+nV_s-r.
\]
Hence \(T_s\equiv T_0-rs\pmod n\). For either outer template, \(r=n/2\pm1\) is odd, so \(\gcd(r,n)=1\); the \(n\) moments are pairwise different modulo \(n\), and so are the \(n\) corresponding values of \(q=T_s-r(r+1)/2\). Reverse-complementation of a binary word preserves \(q\), while interchanging \(r\) with \(n-r\). The identity \(W^{11}_h=1-W^{00}_{(-h)\bmod n}\) implies that the outer two \(q\)-value sets are equal.

**3. The central templates have the same profile set.** Similarly, \(W^{10}_h=1-W^{01}_{(-h)\bmod n}\), and reverse-complementation preserves the scattered \(01\)-count. It is therefore enough to analyze cyclic rotations of \(W_k:=W^{01}\), of weight \(n/2\).

Let \(S_k(s)=\sum_{h=0}^{s-1}(2(W_k)_h-1)\), for \(0\le s\le n\). The moment update gives
\[
T_s=T_0+\frac n2 S_k(s).
\]
We prove by induction that the range of \(S_k(s)\), for \(0\le s<n\), is exactly every integer in \([-1,k-1]\). For \(k=2\), \(W_2=0110\) and the prefix sums (including the final one) are \(0,-1,0,1,0\). For \(k\ge3\), the even-indexed letters of \(W_k\) form \(W_{k-1}\) and the odd-indexed letters alternate \(1,0,1,0,\ldots\). Consequently, for the indicated valid indices,
\[
S_k(2j)=S_{k-1}(j)+(j\bmod2),\qquad
S_k(2j+1)=S_{k-1}(j+1)+(j\bmod2).
\]
By induction, every new prefix sum belongs to \([-1,k-1]\), and \(S_k(1)=-1\). A previous maximum \(k-2\) is attained at a positive index \(j\); if \(j\) is odd, the even prefix \(2j\) attains \(k-1\), and if \(j\) is even, the odd prefix \(2j-1\) attains \(k-1\). In either case the index lies before \(n\). As adjacent prefix sums differ by \(1\) in absolute value, every integer between the two extremes occurs. This proves the range claim.

Finally set \(T_k=\sum_{j=0}^{n-1}(j+1)(W_k)_j\). The same interleaving implies
\[
T_k=2T_{k-1}-\frac n4+\frac{n^2}8,
\]
with \(T_2=5\). Induction yields \(T_k=n(n-k+3)/4\). As \(r=n/2\), the scattered \(01\)-count in rotation \(s\) is
\[
q_s=T_k+\frac n2 S_k(s)-\frac{r(r+1)}2.
\]
Substituting \(S_k(s)=-1,0,1,\ldots,k-1\) gives exactly \(q_s=n(n-2k)/8+(n/2)j\) for \(j=0,\ldots,k\). The central layer thus has \(k+1\) profiles. Together with the two outer layers, this proves the theorem.

## Verification

The standalone `checker.py` computes profiles in two independent ways: from all cyclic rotations of the four explicit templates, and from long literal prefixes of the number-theoretically defined paperfolding word. The literal-prefix method uses a sliding positional moment; an additional direct letter-by-letter subsequence counter is used at smaller scales. All methods agree for \(2\le k\le10\); direct counters are additionally compared for \(2\le k\le7\). The observed profile totals are \(11,20,37,70,135,264,521,1034,2059\). Run `python3 checker.py` from the directory containing the delivered file. This finite verification supplements but does not replace the unrestricted proof.

## Relationship to prior work

Allouche (1992) determines ordinary paperfolding factor complexity \(4n\) for \(n\ge7\). Madill--Rampersad (2012/2013) determine its abelian complexity, using a paperfolding Toeplitz representation and complement-reversal symmetries. Rigo--Salimov (2013/2015) introduce binomial complexity and analyze Sturmian and Thue--Morse words. The present statement refines abelian information *for the paperfolding word itself* at every dyadic length by tracking scattered ordered pairs. The ordinary and abelian counts do not determine the \(2\)-binomial profile spectrum, and the cited Sturmian and Thue--Morse theorems concern different languages.

## Limitations

The formula concerns only the specified paperfolding word and lengths \(2^k\), \(k\ge2\), not arbitrary paperfolding instructions, arbitrary factor lengths, or binomial equivalence of order greater than two. The outside-layer construction is explicit but not simplified into a closed interval of \(q\)-values. A literature search cannot rule out unlocated synonymous statements, and independent mathematical audit has not been performed.

## References

1. J.-P. Allouche, *The Number of Factors in a Paperfolding Sequence*, Bulletin of the Australian Mathematical Society 46 (1992), 23–32, DOI: 10.1017/S0004972700011655.
2. B. Madill and N. Rampersad, *The Abelian Complexity of the Paperfolding Word*, arXiv:1208.2856v1 (first submitted 2012-08-14); Discrete Mathematics 313 (2013), 831–838.
3. M. Rigo and P. Salimov, *Another Generalization of Abelian Equivalence: Binomial Complexity of Infinite Words*, WORDS 2013, LNCS 8079 (2013), 217–228; Theoretical Computer Science 601 (2015), 47–57. DOI: 10.1007/978-3-642-40579-2_23.
4. M. Lejeune, J. Leroy, and M. Rigo, *Computing the k-Binomial Complexity of the Thue–Morse Word*, arXiv:1812.07330v1 (2018); Journal of Combinatorial Theory A 176 (2020), 105284.
