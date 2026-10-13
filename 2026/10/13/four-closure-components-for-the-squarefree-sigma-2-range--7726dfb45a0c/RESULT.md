# Four closure components for the squarefree \(\sigma_{-2}\) range
## Finding
Let \(S_1\) be the set of squarefree positive integers. For
\[
\sigma_{-2}(n)=\sum_{d\mid n}d^{-2},
\]
the closure of the squarefree range is
\[
\overline{\sigma_{-2}(S_1)}
=
\left[1,\frac{54}{5\pi^2}\right]
\cup
\left[\frac{10}{9},\frac{12}{\pi^2}\right]
\cup
\left[\frac54,\frac{27}{2\pi^2}\right]
\cup
\left[\frac{25}{18},\frac{15}{\pi^2}\right].
\]
The four intervals are pairwise disjoint. Consequently, in Defant's notation for divisor functions with restricted domains, the case \(k=1\), \(r=2\) has exactly
\[
L=4
\]
connected components.

## Assumptions and scope
Write
\[
p_1=2,\quad p_2=3,\quad p_3=5,\ldots
\]
for the primes, and set
\[
a_j=\log\left(1+p_j^{-2}\right).
\]
Because every \(n\in S_1\) is squarefree,
\[
\log \sigma_{-2}(n)=\sum_{p_j\mid n}a_j.
\]
Thus the logarithm of the closure is the set of all convergent subsums of the positive summable sequence \((a_j)\).

The proof uses the consecutive-prime estimate appearing as Lemma 2.1 in Defant's restricted-domain paper:
\[
\frac{p_{j+1}}{p_j}<\sqrt2
\]
for every \(j\notin\{1,2,4\}\). The exceptional transition \(7\to11\) is handled directly.

## Proof
Let
\[
A=\sum_{j=1}^{\infty}a_j.
\]
Euler products give
\[
e^A=\prod_p\left(1+p^{-2}\right)
=\frac{\zeta(2)}{\zeta(4)}
=\frac{15}{\pi^2}.
\]

We first show that the subsums using only primes at least \(5\) fill one interval. Define
\[
F_m=\sum_{j=1}^{m-1}a_j+2a_m.
\]
For every \(m\ge5\), Defant's prime-ratio lemma gives
\[
p_{m+1}^2<2p_m^2.
\]
Hence
\[
1+p_m^{-2}
<
1+2p_{m+1}^{-2}
<
\left(1+p_{m+1}^{-2}\right)^2,
\]
so
\[
a_m<2a_{m+1}.
\]
Therefore
\[
F_{m+1}-F_m=2a_{m+1}-a_m>0.
\]
Since
\[
\lim_{m\to\infty}F_m=A,
\]
it follows that
\[
F_m<A
\]
for all \(m\ge5\), equivalently
\[
a_m<\sum_{j>m}a_j.
\tag{1}
\]

The exceptional index \(m=4\), corresponding to \(p_4=7\), is settled by the exact finite product
\[
1+\frac1{7^2}
=
\frac{50}{49}
<
\frac{122}{121}\frac{170}{169}\frac{290}{289}\frac{362}{361}
=
\frac{128075600}{125495513}.
\]
The product on the right uses the primes \(11,13,17,19\), so
\[
a_4<\sum_{j>4}a_j.
\tag{2}
\]
For \(m=3\), the nonexceptional transition \(5\to7\) gives
\[
a_3<2a_4.
\]
Combining this with (2) yields
\[
a_3<a_4+\sum_{j>4}a_j=\sum_{j>3}a_j.
\tag{3}
\]

We now use the elementary subsum interval lemma: if a positive summable sequence \((b_j)\) satisfies
\[
b_m\le\sum_{j>m}b_j
\]
at every index, then the closure of its finite subsums is the full interval from \(0\) to the total sum. Indeed, at each stage the two possible translated tail intervals overlap; iterating this overlap and passing to the limit fills the entire interval.

By (1)--(3), the tail \((a_j)_{j\ge3}\) satisfies this criterion. Hence its subsum closure is
\[
\left[0,\sum_{j=3}^{\infty}a_j\right].
\]
Exponentiating, the contribution from primes at least \(5\) is exactly
\[
\left[1,R\right],
\qquad
R=\prod_{p\ge5}\left(1+p^{-2}\right).
\]
Since the full Euler product is \(15/\pi^2\),
\[
R=
\frac{15/\pi^2}{(1+2^{-2})(1+3^{-2})}
=
\frac{54}{5\pi^2}.
\]

The primes \(2\) and \(3\) may each be either absent or present. Their multiplicative factors are
\[
1+2^{-2}=\frac54,
\qquad
1+3^{-2}=\frac{10}{9}.
\]
Therefore
\[
\overline{\sigma_{-2}(S_1)}
=
[1,R]
\cup
\frac{10}{9}[1,R]
\cup
\frac54[1,R]
\cup
\frac{25}{18}[1,R],
\]
which is exactly the four intervals stated in the finding.

It remains only to verify that they do not overlap. From
\[
\zeta(2)
>
1+\frac14+\frac19+\frac1{16}+\frac1{25}+\int_6^\infty x^{-2}\,dx
=
\frac{5869}{3600},
\]
we get
\[
\pi^2=6\zeta(2)>\frac{5869}{600}>\frac{243}{25}.
\]
Consequently
\[
R=\frac{54}{5\pi^2}<\frac{10}{9}<\frac98.
\]
This implies successively
\[
R<\frac{10}{9},
\qquad
\frac{10}{9}R<\frac54,
\qquad
\frac54R<\frac{25}{18}.
\]
Thus all four intervals are pairwise disjoint.

## Verification
The attached `verify.py` reproduces the finite part of Defant's consecutive-prime ratio lemma up to the cutoff used in its proof. It confirms that the only finite violations of
\[
p_{j+1}^2<2p_j^2
\]
are the stated indices
\[
j=1,\quad j=2,\quad j=4.
\]

The checker also verifies by exact rational arithmetic the \(7\)-to-tail product inequality
\[
\frac{50}{49}
<
\frac{122}{121}\frac{170}{169}\frac{290}{289}\frac{362}{361},
\]
the elementary lower bound
\[
\pi^2>\frac{5869}{600}>\frac{243}{25}
\]
used to separate the four intervals, and the exact endpoint algebra.

As a stress test, it enumerates squarefree integers through a finite cutoff and checks that every computed value of \(\sigma_{-2}\) lies in one of the four claimed intervals. The enumeration is corroborative only; the infinite statement follows from the proof.

## Relationship to prior work
Defant introduced the restricted functions \(\sigma_{-r,k}\), where the domain consists of integers not divisible by any \((k+1)\)-st prime power. Thus \(k=1\) is exactly the squarefree domain. The paper proves the density transition for these restricted ranges and closes by asking, for given \(k\) and \(L\), which \(r>1\) produce exactly \(L\) connected components. It does not compute the component decomposition at \(k=1,r=2\).

For comparison, Sanna determined the unrestricted \(r=2\) closure:
\[
\overline{\sigma_{-2}(\mathbb N)}
=
\left[1,\frac{\pi^2}{9}\right]
\cup
\left[\frac{10}{9},\frac{\pi^2}{8}\right]
\cup
\left[\frac54,\frac{\pi^2}{6}\right],
\]
which has three components. That theorem allows arbitrary prime powers and does not imply the squarefree result.

Zubrilina later studied the unrestricted divisor range and proved, among other things, that its connected-component count can never equal \(4\). Again, that statement concerns the full positive-integer domain rather than the squarefree restriction. The present result therefore exhibits a component count that is impossible in the unrestricted problem but occurs naturally in Defant's restricted-domain problem.

Targeted searches for the exact restricted notation, the squarefree \(r=2\) formulation, the four displayed endpoints, and the constant \(54/(5\pi^2)\) found no published source giving this four-component decomposition. The constant itself appears independently in an OEIS product identity, but without the topological range statement.

## Limitations
This result determines one natural point of Defant's two-parameter connected-component problem:
\[
(k,r)=(1,2).
\]
It does not characterize the full set of \(r\) for which \(k=1\) has four components, nor does it determine component counts for arbitrary \(k\).

The proof depends on Defant's published consecutive-prime ratio lemma. The packaged checker replays its finite verification range; the asymptotic prime-gap input beyond that range is cited rather than reproved.

The literature comparison included the primary restricted-domain paper, Sanna's unrestricted closure theorem, Zubrilina's later connected-component paper, exact-formula searches, and the relevant OEIS product entry. An equivalent observation in unindexed notes remains a residual originality risk.

## References
1. C. Defant, “On the Density of Ranges of Generalized Divisor Functions with Restricted Domains,” arXiv:1507.02663v1, first public 9 July 2015; later *Uniform Distribution Theory* 10 (2015), no. 1, 19–33.
2. C. Sanna, “On the Closure of the Image of the Generalized Divisor Function,” arXiv:1507.08091v1, 29 July 2015; later *Uniform Distribution Theory* 12 (2017), no. 2, 77–90.
3. N. Zubrilina, “On the Number of Connected Components of Ranges of Divisor Functions,” arXiv:1711.02871, 2017.
