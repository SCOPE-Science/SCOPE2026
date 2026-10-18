# Exact strong-majority vertex-colouring numbers of cycle powers

## Finding

Let \(k\ge2\) and \(n\ge 2k+2\) be integers. The graph \(C_n^k\) has vertex set \(\mathbb Z/n\mathbb Z\), with vertices adjacent precisely at cyclic differences \(\pm1,\ldots,\pm k\). A **strong-majority vertex-colouring** is a (not necessarily proper) colouring such that, at each vertex, no colour appears on more than half its neighbours. Write \(\operatorname{Maj}(G)\) for the smallest number of colours in such a colouring and \(\nu_2(m)\) for the exponent of \(2\) in a positive integer \(m\).

Then the **exact strong-majority number** is
\[
\operatorname{Maj}(C_n^k)=
\begin{cases}
2,&\text{if } k\text{ is even and } n\text{ is even},\\
2,&\text{if }k\text{ is odd and } 2^{\nu_2(k+1)+1}\mid n,\\
3,&\text{otherwise}.
\end{cases}
\]
In particular, for odd \(k\), changing \(n\) by a small amount can change the optimum according to a precise two-adic threshold. There is an explicit uniform three-colour construction for every \(n,k\) in the stated domain.

A further exact counting statement holds whenever \(\gcd(n,k)=1\). Put \(g=\gcd(n,k+1)\). The number of **labelled** strong-majority two-colourings, for the two named colours \(\{+1,-1\}\), is
\[
N_2(n,k)=\begin{cases}2^g,&n/g\text{ is even},\\0,&n/g\text{ is odd}.\end{cases}
\]
Colourings obtained by exchanging the two named colours are counted separately. The counting formula is not asserted for non-coprime \(n,k\).

## Assumptions and scope

All graphs are finite and simple. The inequality \(n\ge 2k+2\) ensures that the \(2k\) cyclic neighbours listed above are pairwise distinct. A colour need not be different from the colour of an adjacent vertex. The count concerns all vertex maps to two named colours satisfying the strong-majority rule; because every vertex has positive degree, both colours necessarily occur. No assumption about the parity of \(n\) or the primality of \(k\) is made unless explicitly stated. The case \(k=1\), the ordinary cycle, is previously known and is not presented as new here.

## Proof

**Binary balance and factorization.** Encode two named colours as \(x_i\in\{+1,-1\}\). Each vertex has \(2k\) neighbours. Both colours occur at most \(k\) times in the neighbourhood exactly when each occurs exactly \(k\) times; equivalently
\[
\sum_{j=1}^k(x_{i-j}+x_{i+j})=0\qquad(i\in\mathbb Z/n\mathbb Z).
\]
Let \(T\) denote cyclic shift, \((Tx)_i=x_{i+1}\), and define \(B=I+T+\cdots+T^{k-1}\) and \(D=I+T^{k+1}\). Multiplication of the adjacency sum by the invertible shift \(T^k\) yields the exact operator identity
\[
T^k\sum_{j=1}^k(T^j+T^{-j})
=\left(\sum_{j=0}^{k-1}T^j\right)(I+T^{k+1})=BD.
\]
Thus two-colour balance is equivalent to \(BDx=0\). Summing the original neighbour equations over all vertices gives \(2k\sum_i x_i=0\). Therefore \(n\) must be even.

**Even powers.** When \(k\) and \(n\) are even, the alternating sequence \(x_i=(-1)^i\) is well-defined on the cyclic indices. Exactly half the distances \(1,\ldots,k\) are odd and half are even; hence every vertex has \(k\) neighbours of each sign. If \(n\) is odd, the preceding sum condition rules out two colours.

**Odd powers: obstruction.** Suppose \(k\) is odd, put \(g=\gcd(n,k+1)\), and suppose \(L=n/g\) is odd. Since \(T^{(k+1)L}=I\), the operator \(D=I+T^{k+1}\) is invertible over \(\mathbb Q\): indeed
\[
(I+T^{k+1})\sum_{j=0}^{L-1}(-T^{k+1})^j=2I
\]
when \(L\) is odd. From \(BDx=0\), commutativity and invertibility imply \(Bx=0\). Applying \(T-I\) gives \((T^k-I)x=0\). Thus every \(k\)-step shift fixes \(x\), while \(Bx\) is the sum of \(k\) signs and must vanish. Because \(k\) is odd, such a sum cannot be zero. Therefore no binary strong-majority colouring exists when \(L\) is odd.

The number \(L=n/\gcd(n,k+1)\) is even precisely when \(\nu_2(n)>\nu_2(k+1)\), equivalently \(2^{\nu_2(k+1)+1}\mid n\). Hence the obstruction has the stated two-adic form.

**Odd powers: construction.** Conversely suppose \(2^{\nu_2(k+1)+1}\mid n\) and set \(p=2^{\nu_2(k+1)}\). Define
\[
x_i=(-1)^{\lfloor i/p\rfloor}\qquad(0\le i<n).
\]
This is a cyclic sign sequence of period \(2p\), because \(2p\mid n\). Since \((k+1)/p\) is odd, shifting by \(k+1\) switches signs: \(T^{k+1}x=-x\). Thus \(Dx=0\), consequently \(BDx=0\), giving the required strong-majority two-colouring.

**Three colours always suffice.** Let \(k\ge3\). Write \(n=3t+r\) with \(0\le r<3\), and take the cyclic word
\[
w=(012)^t\,u_r,\qquad u_0=\varepsilon,\quad u_1=1,\quad u_2=01,
\]
where \(\varepsilon\) denotes the empty word. This uses at most three colours. It consists of a circular periodic \(012\)-word with zero, one, or two inserted letters. In the two-letter insertion the inserted colours are different. The neighbourhood of any vertex is the disjoint union of two cyclic intervals, each of length \(k\). If interval \(j\) contains \(s_j\) of the inserted letters, deleting those letters leaves a consecutive segment of the original \(012\)-periodic word, so it contains any given colour at most \(\lceil(k-s_j)/3\rceil\) times. There is at most one inserted letter of any one colour in the entire graph.

For a colour absent from the inserted letters in the two neighbourhood intervals, its total frequency is at most \(2\lceil k/3\rceil\le k\). If a colour is represented by an inserted letter in a neighbourhood interval, at least one of \(s_1,s_2\) is positive; its frequency is at most
\[
\left\lceil\frac{k-1}{3}\right\rceil+
\left\lceil\frac{k}{3}\right\rceil+1\le k,
\]
for every integer \(k\ge3\). Both bounds are elementary checks by reduction modulo three. This proves the strong-majority property.

For \(k=2\), periodic stretches of \(012\) satisfy the rule directly. All length-five centred windows encountering an inserted letter are among
\[
\begin{aligned}
 r=1:&\quad 01210,\ 10120,\ 12101,\ 20121,\ 21012;\\
 r=2:&\quad 01012,\ 01201,\ 10120,\ 12010,\ 20101,\ 20120.
\end{aligned}
\]
Deleting the middle character from each such word leaves four neighbour colours, with no colour occurring more than twice. The assumption \(n\ge6\) ensures that there is no second insertion in a length-five window. Thus the same construction works for \(k=2\). One colour is impossible on a graph of positive degree, proving the exact values \(2\) and \(3\).

**The coprime enumeration.** If \(\gcd(n,k)=1\), then \(B\) is invertible on \(\mathbb Q^n\). Indeed, \(Bx=0\) implies \((T^k-I)x=0\), hence \(Tx=x\) by coprimality, and \(Bx=kx=0\) gives \(x=0\). Therefore binary solutions of \(BDx=0\) are exactly the solutions of \(T^{k+1}x=-x\). Shifting cyclic indices by \(k+1\) has \(g=\gcd(n,k+1)\) disjoint cycles, each of length \(L=n/g\). On each cycle the signs must alternate, which is possible if and only if \(L\) is even; in that case one initial sign can be chosen independently on each of the \(g\) cycles. The number is exactly \(2^g\), as asserted.

## Verification

Run the standalone Python 3 program `python3 verify_cycle_majority.py` from the directory containing this document. The checker independently constructs every neighbourhood, validates all displayed binary and ternary constructions for thousands of parameter pairs, brute-forces every binary colouring for the stated small orders, and checks the exact coprime counting formula. It also explicitly enumerates the eleven local length-five windows used at \(k=2\). The verification script depends only on the Python standard library. The general result follows from the preceding proof, not from finite experimentation.

## Relationship to prior work

Kalinowski, Kamyczura, Pilśniak and Woźniak introduced strong-majority vertex-colouring and determined the exact strong-majority number for ordinary cycles (the previously known \(k=1\) case) and for complete graphs. Their 2026 paper does not give the cycle-power formula for the noncomplete powers considered here.

Freyberg and Marr (2024) earlier defined **neighbourhood-balanced two-colourings**, exactly equivalent to two-colour strong-majority colourings on the even-regular graphs here. Their classification of all quartic circulants (Theorem 9) includes the \(k=2\) two-colour criterion as a special case; this known instance is included only for a coherent formula and is not a novelty claim. Their theorem is specific to degree four and does not cover arbitrary odd powers \(k\ge3\), the two-adic threshold, the exact strong-majority number of these powers, or the coprime labelled count. The 2025 closed-neighbourhood paper investigates a different closed-neighbourhood condition and gives some sufficient constructions for open-neighbourhood balance, not a converse for all consecutive-generator circulants. Minyard--Sepanski (2026) require exact equality of all three neighbourhood colour frequencies, a strictly different predicate from the at-most-half requirement (and impossible at degrees not divisible by three), so that work does not cover the universal three-colour bound. In particular, the even-\(k\) alternating construction is elementary and related to known parity constructions; the nontrivial new component is the sharp odd-\(k\) obstruction combined with the universal three-colour construction.

## Limitations

The theorem applies only to noncomplete powers \(n\ge2k+2\). It does not enumerate all two-colourings when \(\gcd(n,k)>1\), nor does it count three-colourings. Results for ordinary cycles and the quartic two-colour case are acknowledged as previously known. The originality comparison is bounded by the accessible literature: equivalent results under equitable-partition, perfect-colouring, or circulant-kernel terminology may exist outside the inspected sources. No independent mathematical audit has been performed.

## References

1. R. Kalinowski, M. Kamyczura, M. Pilśniak, and M. Woźniak, *Strong majority colorings of graphs*, arXiv:2605.23828v1, posted 22 May 2026. https://arxiv.org/abs/2605.23828
2. B. Freyberg and A. Marr, *Neighborhood Balanced Colorings of Graphs*, Graphs and Combinatorics 40, article 41 (2024), published 26 March 2024, DOI:10.1007/s00373-024-02766-9. https://link.springer.com/article/10.1007/s00373-024-02766-9
3. K. L. Collins and collaborators, *Closed Neighborhood Balanced Coloring of Graphs*, Graphs and Combinatorics 41, article 88 (2025), published 28 July 2025, DOI:10.1007/s00373-025-02950-5. https://link.springer.com/article/10.1007/s00373-025-02950-5
4. M. Minyard and M. R. Sepanski, *Neighborhood 3-Balanced Graphs*, Graphs and Combinatorics 42, article 50 (2026), published 5 May 2026, DOI:10.1007/s00373-026-03038-4. https://link.springer.com/article/10.1007/s00373-026-03038-4
