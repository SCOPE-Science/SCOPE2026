# A factorial-moment proof of an arrow-Wilf equivalence

## Finding

Let \(\theta\) be the fundamental transformation that writes a permutation in cycles starting at their largest elements, orders the cycles by those maxima, and deletes the parentheses. Let \(a_n(\alpha)\) be the number of one-line permutations avoiding the arrow pattern \(\alpha\) under the cycle convention \(\theta^{-1}\). For all integers \(n\ge 0\),

\[
 a_n((12;3\to3))=a_n((23;1\to1)).
\]

More precisely, with \(d_0=1\), \(d_n\) the ordinary derangement numbers, and \(D(z)=\sum_{n\ge0}d_nz^n\), their common ordinary generating function is the formal power series

\[
 H(z)=D(z)+\frac{z}{1-z-z^2}D\!\left(\frac{z}{1-z-z^2}\right).
\]

The first coefficients, including the empty permutation, are \(1,1,2,5,17,75,412,2707,20657,179237,1740806\). The result establishes a previously conjectural equality of two arrow-avoidance classes; it does not assert a direct bijection.

## Assumptions and scope

All permutations act on \([n]=\{1,\ldots,n\}\). In standard cycle form each cycle begins at its maximum, and cycles appear in increasing order of their maxima. The resulting word is \(w=\theta(\sigma)\); the arrow condition is interpreted using \(\sigma=\theta^{-1}(w)\). An occurrence of \((12;3\to3)\) consists of an increasing pair of entries \(x<y\) in word order, with a larger fixed point \(f>y\) of \(\sigma\). An occurrence of \((23;1\to1)\) consists of an increasing pair \(x<y\) in word order with a smaller fixed point \(f<x\). The empty permutation avoids both patterns. All generating functions below are *formal*, not analytic assertions of convergence.

For a permutation with at least one fixed point, the first avoidance condition says exactly that the subsequence of \(w\) below its **largest** fixed point is decreasing. The second says exactly that the subsequence above its **smallest** fixed point is decreasing. Fixed-point-free permutations contribute \(d_n\) to both counts.

## Proof

**1. The first avoidance class.** Fix a largest fixed point \(f\ge1\) and write \(b=n-f\). Its singleton cycle separates cycles with maximum below \(f\) from those with maximum above \(f\). Because the letters below \(f\) appear decreasingly, at most one cycle lies entirely below \(f\): two such cycles would introduce an increasing pair of their respective maxima. If this initial cycle has \(s\) letters, they are necessarily the \(s\) largest members of \([f-1]\), in decreasing order. Put \(r=f-1-s\). The remaining \(r\) smaller letters occur after \(f\) and are also ordered decreasingly.

Delete these \(r\) letters from the later cycles. The surviving \(b\) higher letters form an arbitrary permutation \(\tau\in\mathfrak S_b\) in standard cycle form. Reinsert the smaller letters, still in decreasing relative order, into the \(b\) slots immediately following the higher letters. If \(\tau\) has \(j\) singleton cycles, their slots must be nonempty: otherwise a fixed point larger than \(f\) would arise. The number of legal reinsertion schemes with \(r\) small letters is

\[
 \binom{b+r-j-1}{r-j},
\]

interpreted as zero for \(r<j\). When \(b=0\), there is just one permitted configuration (the decreasing cycle on \([f-1]\), if nonempty). Write \(P_b(u)=\sum_{\tau\in\mathfrak S_b}u^{\operatorname{fix}(\tau)}\), with \(P_0=1\). For \(b\ge0\), the generating series in \(r\) for those insertions is \(P_b(u)/(1-u)^b\). Summing over \(f\) and \(r\le f-1\) gives the generating function for permutations with a fixed point:

\[
 F_{12}(z)=\frac{z}{1-z}\sum_{b\ge0}\left(\frac{z}{1-z}\right)^bP_b(z).
\]

The rencontres identity \(P_b(u)=\sum_{j=0}^{b}\binom bj d_{b-j}u^j\) gives, by summing a binomial series,

\[
 \sum_{b\ge0}P_b(u)t^b=\frac{1}{1-ut}D\!\left(\frac{t}{1-ut}\right).
\]

Substitution \(u=z\), \(t=z/(1-z)\) proves

\[
 F_{12}(z)=\frac{z}{1-z-z^2}D\!\left(\frac{z}{1-z-z^2}\right).
\]

**2. The second avoidance class.** Fix instead the smallest fixed point \(f\), and let \(a=f-1\), \(b=n-f\). The letters above \(f\) must appear decreasingly. If \(b\ge1\), all \(b\) of them therefore lie in a *single* cycle, beginning with \(n\): different cycles with higher maxima would display an increasing pair. Choose \(r\) of the \(a\) lower letters to belong to this cycle. The remaining lower letters form an arbitrary fixed-point-free permutation, counted by \(d_{a-r}\), because \(f\) is the smallest fixed point.

The higher letters appear in their unique descending order in the single cycle. Its \(r\) selected lower letters can be permuted and interleaved after \(n\) in exactly

\[
 (b)^{\overline r}=b(b+1)\cdots(b+r-1)
\]

ways, taking \((b)^{\overline0}=1\). When \(b=0\), this expression vanishes for \(r>0\); only a derangement of the \(a\) smaller symbols remains. Thus uniformly for \(a,b\ge0\) the number of configurations with these parameters is

\[
 T_{a,b}=\sum_{r=0}^{a}\binom ar d_{a-r}(b)^{\overline r}.
\]

**3. Equality by a factorial-moment identity.** Define the linear functional \(\mathcal L:\mathbb Q[t]\to\mathbb Q\) by \(\mathcal L(t^k)=k!\). In particular \(d_k=\mathcal L((t-1)^k)\). Comparison of exponential generating functions in \(a\), using \(\sum_{k\ge0}d_kx^k/k!=e^{-x}/(1-x)\), shows

\[
 T_{a,b}=\frac1{b!}\mathcal L\!\left((t-1)^a t^b\right).
\]

Indeed, both sides have exponential generating function \(e^{-x}(1-x)^{-b-1}\) in \(a\). The generating function for the permutations in the second class with at least one fixed point is consequently

\[
 F_{23}(z)=z\mathcal L\!\left(\frac{e^{zt}}{1-z(t-1)}\right).
\]

The functional is applied coefficientwise to formal power series. For every polynomial \(R(t)\), its defining moments imply the formal identity

\[
 \mathcal L(e^{zt}R(t))=\frac1{1-z}\mathcal L\!\left(R\!\left(\frac{t}{1-z}\right)\right).
\]

The identity extends coefficientwise to the rational formal series in this calculation. Put \(q=1-z-z^2\), \(u=z/q\). Algebraically,

\[
 1+z-\frac{zt}{1-z}=\frac{q}{1-z}\bigl(1-u(t-1)\bigr).
\]

It follows that

\[
 \begin{aligned}
 F_{23}(z)
 &=\frac{z}{1-z}\mathcal L\!\left(\frac1{1+z-zt/(1-z)}\right)\\
 &=\frac zq\mathcal L\!\left(\frac1{1-u(t-1)}\right)\\
 &=\frac zq D(u)=F_{12}(z).
 \end{aligned}
\]

Adding the common fixed-point-free contribution \(D(z)\) proves both the equality and the stated generating function, for every \(n\ge0\).

## Verification

The included `verify.py` independently enumerates permutations in both arrow classes through \(n=8\), and checks literal arrow containment (rather than just the fixed-point shortcut) through \(n=7\). It checks both structural sum formulas and the common composition formula through \(n=18\) using exact integer arithmetic. Run `python3 verify.py` from the directory containing that standalone file; its expected final line is `VERIFY_OK`. The mathematical proof above, not the finite checks, establishes the all-order assertion.

## Relationship to prior work

Archer and Laudone introduced the systematic small-arrow enumeration and recorded \((12;3\to3)\) and \((21;3\to3)\) as unresolved in their March 2026 paper. Zhou and Yu subsequently supplied enumerations for those two classes and for \((23;1\to1)\). A September 2026 research summary of Zhou and Yu identifies the equinumerosity of \((12;3\to3)\) and \((23;1\to1)\) as an open question despite agreeing numerical data. The novelty asserted here is *the proof of this cross-pattern equivalence*, not the separate avoidance enumerations or the derangement identities. The full text of Zhou and Yu's paper could not be inspected in this investigation; its accessible abstract and the linked open-problem summary were compared, so an independently verifiable publication-priority risk remains.

## Limitations

No explicit size-preserving bijection between the two avoidance sets is supplied; their cardinalities agree by a formal factorial-moment calculation. The method does not enumerate the separate remaining open class \((32;1\to3)\). The series \(D(z)\) is used formally. Unindexed equivalent proofs may exist, and the full primary text of the September 2026 follow-up was unavailable for comparison. No independent mathematical audit has been conducted.

## References

1. K. Archer and R. P. Laudone, *Arrow pattern avoidance in permutations: structure and enumeration*, arXiv:2603.04218v1 (first public 2026-03-04), https://arxiv.org/abs/2603.04218 . Full 19-page primary PDF inspected, including Definitions 1.1–2 and Section 7.
2. R. D. P. Zhou and X. Yu, *Arrow-Wilf equivalences and enumerative results for short arrow patterns*, arXiv:2609.29392v1 (first public 2026-09-24), https://arxiv.org/abs/2609.29392 . Accessible abstract examined; full text not obtained.
3. *Arrow-Wilf equivalence of (12; 3→3) and (23; 1→1)*, open-question summary referencing Zhou–Yu, https://www.emergentmind.com/open-problems/arrow-wilf-equivalence-12-3-to-3-and-23-1-to-1 (accessed 2026-10-20 UTC). Secondary evidence of the stated unresolved comparison, not a substitute for the primary full text.
