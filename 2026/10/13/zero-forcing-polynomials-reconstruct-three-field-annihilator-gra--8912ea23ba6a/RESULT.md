# Zero forcing polynomials reconstruct three-field annihilator graphs

## Finding

Let \(R=\mathbb F_{q_1}\times\mathbb F_{q_2}\times\mathbb F_{q_3}\), where every \(q_i\ge3\), and put \(x_i=q_i-1\). Define \[w=(x_2x_3,x_1x_3,x_1x_2,x_3,x_2,x_1),\qquad N=\sum_{j=1}^6w_j.\] For Badawi's annihilator graph \(\operatorname{AG}(R)\), let \(e_k(w)\) denote the elementary symmetric polynomial of degree \(k\) in the six weights and put \(P=x_1x_2x_3\). Then \[\mathcal Z(\operatorname{AG}(R);u)=(e_4(w)-3P^2)u^{N-4}+e_3(w)u^{N-3}+e_2(w)u^{N-2}+Nu^{N-1}+u^N.\] Hence \(Z(\operatorname{AG}(R))=M(\operatorname{AG}(R))=N-4\) and the real symmetric minimum rank is \(4\). Moreover the polynomial recovers the unordered triple \(\{q_1,q_2,q_3\}\), so within this three-field, no-binary-factor class it determines both the annihilator graph and the semisimple ring up to isomorphism.

The leading coefficient counts all minimum zero forcing sets; it is the weighted sum of the twelve forcing four-type complements in the triangular-prism quotient.

## Assumptions and scope

Let
\[
R=\mathbb F_{q_1}\times\mathbb F_{q_2}\times\mathbb F_{q_3},
\qquad q_i\ge3,
\]
and write \(x_i=q_i-1\). Badawi's annihilator graph has the nonzero zero-divisors as vertices.

Afkhami, Khashyarmanesh, and Rajabi partition these vertices into six independent support classes \(A_1,\ldots,A_6\). Their sizes are
\[
w_1=x_2x_3,\quad w_2=x_1x_3,\quad w_3=x_1x_2,\quad
w_4=x_3,\quad w_5=x_2,\quad w_6=x_1.
\]
The quotient adjacency is
\[
\begin{aligned}
A_1&\sim A_2,A_3,A_6,\\
A_2&\sim A_1,A_3,A_5,\\
A_3&\sim A_1,A_2,A_4,\\
A_4&\sim A_3,A_5,A_6,\\
A_5&\sim A_2,A_4,A_6,\\
A_6&\sim A_1,A_4,A_5,
\end{aligned}
\]
which is the triangular prism.

## Proof

Every \(A_i\) is a false-twin class. Thus a zero forcing complement contains at most one vertex from any \(A_i\). Because \(q_i\ge3\), every class has size at least \(2\), so each class always retains a blue representative when one vertex is white. Therefore forcing depends only on the subset of classes containing white representatives.

A direct six-type forcing analysis gives the exact admissible profile census
\[
1,\ 6,\ 15,\ 20,\ 12,\ 0,\ 0
\]
for white-profile sizes \(0,1,\ldots,6\). The only nonforcing four-type profiles are
\[
\{1,2,5,6\},\qquad
\{1,3,4,6\},\qquad
\{2,3,4,5\}.
\tag{1}
\]
Every product of the four class sizes in one of (1) equals
\[
P^2=(x_1x_2x_3)^2.
\]

A white profile \(I\) contributes
\[
\left(\prod_{i\in I}w_i\right)u^{N-|I|}
\]
because one may choose its white representative independently in each selected class. Summing the admissible profiles yields
\[
\mathcal Z(\operatorname{AG}(R);u)
=
(e_4(w)-3P^2)u^{N-4}
+e_3(w)u^{N-3}
+e_2(w)u^{N-2}
+Nu^{N-1}
+u^N.
\tag{2}
\]
In particular,
\[
Z(\operatorname{AG}(R))=N-4.
\]

Let \(B\) be the \(6\times6\) adjacency matrix of the triangular-prism quotient. Exact row reduction gives
\[
\operatorname{rank}_{\mathbb R}B=4.
\]
If \(X\) is the vertex-by-class incidence matrix, then the actual adjacency matrix is
\[
XBX^{\mathsf T}.
\]
Since every class is nonempty, \(X\) has full column rank, so this matrix also has rank \(4\). Hence
\[
\operatorname{mr}(\operatorname{AG}(R))\le4.
\]
The standard inequality \(M(G)\le Z(G)\) gives the reverse minimum-rank bound:
\[
\operatorname{mr}(\operatorname{AG}(R))
=
N-M(\operatorname{AG}(R))
\ge N-Z(\operatorname{AG}(R))=4.
\]
Therefore
\[
\operatorname{mr}(\operatorname{AG}(R))=4,\qquad
M(\operatorname{AG}(R))=Z(\operatorname{AG}(R))=N-4.
\]

It remains to reconstruct the field orders from the polynomial. Put
\[
s_1=x_1+x_2+x_3,\qquad
s_2=x_1x_2+x_1x_3+x_2x_3,\qquad
s_3=x_1x_2x_3.
\]
Let \(c_2\) and \(c_4\) be the coefficients of \(u^{N-2}\) and \(u^{N-4}\), respectively. Expanding (2) gives
\[
N=s_1+s_2,
\]
\[
c_2=s_1s_2+s_1s_3+s_2,
\]
and
\[
c_4=s_3(c_2-3s_3).
\tag{3}
\]
Thus \(s_3\) is a root of
\[
3t^2-c_2t+c_4=0.
\]
The other root exceeds \(s_3\), since
\[
c_2-6s_3=s_1s_2+s_2+s_3(s_1-6)>0
\]
for \(x_i\ge2\). Hence \(s_3\) is the smaller positive root and is determined by the polynomial.

Substituting \(s_2=N-s_1\) into the formula for \(c_2\) shows that \(s_1\) satisfies
\[
t^2-(N+s_3-1)t+(c_2-N)=0.
\tag{4}
\]
The other root of (4) is \(s_2+s_3-1>s_1\), so \(s_1\) is again the smaller positive root. Then \(s_2=N-s_1\).

Finally \(x_1,x_2,x_3\), with multiplicity, are the roots of
\[
t^3-s_1t^2+s_2t-s_3.
\]
Therefore the polynomial recovers the unordered triple \(\{x_1,x_2,x_3\}\), hence \(\{q_1,q_2,q_3\}\). Finite fields are determined by their orders, so it also recovers \(R\) up to factor permutation.

## Verification

The accompanying `verify.py` was read from its packaged path before replay. It independently reconstructs the six-type forcing census and the three exceptional four-type profiles.

It exhaustively checks all \(2^{18}\) vertex subsets for the equal small case \(\mathbb F_3^3\), directly constructs \(\mathbb F_3\times\mathbb F_3\times\mathbb F_5\) from coordinate arithmetic and recomputes annihilator adjacency from Badawi's definition, checks exact rank \(4\) for representative blowups, and replays the reconstruction formulas on repeated and unequal field orders.

Exact replay output:

```text
PROFILE_CENSUS_OK {0: 1, 1: 6, 2: 15, 3: 20, 4: 12} [(1, 2, 5, 6), (1, 3, 4, 6), (2, 3, 4, 5)]
FULL_BRUTE_F3_CUBE_OK {14: 864, 15: 504, 16: 132, 17: 18, 18: 1}
DIRECT_UNEQUAL_F3_F3_F5_OK [8, 8, 4, 4, 2, 2] 28
RANK_FOUR_OK
RECOVER (3, 3, 3) -> (3, 3, 3) coeff_min 864
RECOVER (3, 3, 5) -> (3, 3, 5) coeff_min 4160
RECOVER (3, 5, 7) -> (3, 5, 7) coeff_min 48192
RECOVER (4, 5, 9) -> (4, 5, 9) coeff_min 215040
RECOVER (5, 7, 11) -> (5, 7, 11) coeff_min 1604160
VERIFY_OK
```

The finite computations corroborate the symbolic proof; they do not replace it.

## Relationship to prior work

Badawi introduced the annihilator graph and established its foundational ring-theoretic properties. His article has primary Mathematics Subject Classification \(13A15\).

Afkhami, Khashyarmanesh, and Rajabi explicitly give the six independent classes and their triangular-prism adjacency for a product of three arbitrary fields. Their result supplies the structural quotient used here, but it studies clique number, coloring, planarity-type questions, and ring extensions rather than zero forcing.

A recent modular-compression theorem shows generically that the complement of a zero forcing set contains at most one representative from each twin type and reduces the polynomial to a weighted type-subset enumerator. That compression mechanism is therefore prior coverage and is not claimed as new here.

The closest previously obtained annihilator-graph forcing result treats three equal field orders. The present result strictly strengthens it to arbitrary \(q_1,q_2,q_3\ge3\) and adds an inverse theorem: four polynomial coefficients recover the full unordered field-order triple and hence the semisimple ring.

## Limitations

The theorem assumes exactly three field factors and excludes field order \(2\). Binary factors create singleton support classes, so the blue-representative argument requires a separate profile analysis.

The rank statement is over real symmetric graph-pattern matrices.

The six-class triangular-prism decomposition is prior work. The generic twin-class compression is also prior. Originality is restricted to the weighted forcing census in the unequal-field setting, the closed polynomial and rank conclusion together, and especially the inverse reconstruction of all three field orders.

## References

1. A. Badawi, “On the Annihilator Graph of a Commutative Ring,” *Communications in Algebra* 42 (2014), 108–121. DOI: 10.1080/00927872.2012.707262. Published online 18 October 2013.
2. M. Afkhami, K. Khashyarmanesh, and Z. Rajabi, “Some results on the annihilator graph of a commutative ring,” *Czechoslovak Mathematical Journal* 67 (2017), 151–169. DOI: 10.21136/CMJ.2017.0436-15.
3. X. Wang, “Modular Compression of Leaky Forts and Leaky Forcing Polynomials,” preprint, 26 May 2026. DOI: 10.5281/zenodo.20388397.
4. K. Boyer et al., “The zero forcing polynomial of a graph,” *Discrete Applied Mathematics* 258 (2019), 35–48. arXiv:1801.08910.
5. AIM Minimum Rank — Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628–1648. DOI: 10.1016/j.laa.2007.10.009.
