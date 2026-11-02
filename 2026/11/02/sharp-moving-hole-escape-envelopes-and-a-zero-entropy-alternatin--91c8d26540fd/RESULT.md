# Sharp moving-hole escape envelopes and a zero-entropy alternating phase for the doubling map

## Finding
Let \(T(x)=2x\pmod1\) on \([0,1)\), with independent binary digits initially distributed according to Lebesgue measure. At each integer time \(j\ge0\), an externally prescribed symbol \(s_j\in\{0,1\}\) chooses one of the *equal-length* holes
\[
H_0=[0,1/4),\qquad H_1=[3/4,1).
\]
Write \(P_n(s)=\operatorname{Leb}\{x:T^jx\notin H_{s_j}\text{ for }0\le j<n\}\), with \(P_0=1\). Let \(F_0=0,F_1=1\) be Fibonacci numbers. **For every schedule and every integer \(n\ge0\)**,
\[
\boxed{\frac{n+2}{2^{n+1}}\le P_n(s)\le\frac{F_{n+3}}{2^{n+1}}.}
\]
For \(n\ge2\), the lower equality holds if and only if the first \(n\) symbols alternate, and the upper equality holds if and only if those symbols are constant. If \(L\) denotes the number of hole checks until the first hit, then
\[
3\le\mathbb E[L]\le5,
\]
with the lower equality precisely for an infinitely alternating schedule and the upper equality precisely for an infinite constant schedule.

For a schedule periodic with period \(r\), define
\[
M_0=\begin{pmatrix}0&1\\1&1\end{pmatrix},\quad
M_1=\begin{pmatrix}1&1\\1&0\end{pmatrix},\quad
Q_s=M_{s_0}\cdots M_{s_{r-1}}.
\]
With \(\rho\) denoting matrix spectral radius, its infinite survivor has topological entropy, Hausdorff dimension, and exponential escape rate
\[
h(s)=\frac{\log\rho(Q_s)}r,\qquad
\dim_H\mathcal S(s)=\frac{h(s)}{\log2},\qquad
\gamma(s)=\log2-h(s).
\]
Writing \(\varphi=(1+\sqrt5)/2\), cyclically alternating schedules are **exactly** those with \(h=0\), while constant schedules are **exactly** those with \(h=\log\varphi\); every other periodic schedule has \(0<h<\log\varphi\). Consequently the largest possible periodic escape rate is \(\log2\) and the smallest is \(\log(2/\varphi)\). The survivor for an alternating schedule is countable.

## Assumptions and scope
All holes are half-open to specify binary-cylinder boundaries. The schedule is fixed independently of the starting point; no randomness, feedback, or optimization over trajectories is assumed. Initial points have the Lebesgue distribution. Binary codings of dyadic rationals are chosen consistently; the countable ambiguous set does not affect probabilities or Hausdorff dimensions. The sharp finite-horizon inequalities concern all finite schedules, not only periodic ones. Entropy, dimension and escape-rate formulas concern periodic schedules.

## Proof
**1. Binary coding and finite counting.** For almost every \(x\), write its binary expansion as \(x=0.b_0b_1\ldots\). Avoiding the hole at time \(j\) means the adjacent digits are not both equal to \(s_j\). If \(C_n(s)\) counts admissible words \(b_0\ldots b_n\), then \(P_n=C_n/2^{n+1}\) and
\[
C_n=(1,1)M_{s_0}\cdots M_{s_{n-1}}(1,1)^{\mathsf T}.
\]
For the evolving row \(v_n=(a_n,b_n)\), starting at \((1,1)\), adding a zero-hole maps \((a,b)\mapsto(b,a+b)\), while adding a one-hole maps \((a,b)\mapsto(a+b,a)\). Each step increases the total by respectively \(b\) or \(a\). Both entries remain positive integers, so each increment is at least one; hence \(C_n\ge n+2\). After a zero step the first coordinate is strictly smaller, so adding a one step increases the total by exactly one; after a one step the second is strictly smaller, so adding zero does. A repetition instead adds an integer at least two. Consequently, for \(n\ge2\), \(C_n=n+2\) holds exactly for an alternating prefix.

Moreover, after the most recent step, the *larger* coordinate equals the preceding total \(C_{n-1}\); therefore
\[
C_{n+1}\le C_n+C_{n-1},\qquad C_0=2,\quad C_1=3.
\]
Induction gives \(C_n\le F_{n+3}\). The stepwise equality requires choosing the larger coordinate, which means repeating the previous hole symbol. As soon as a switch occurs there is a strict deficit, propagated by the positive recursion; hence for \(n\ge2\) equality is equivalent to a constant prefix. This proves all finite-horizon assertions.

**2. First-hit expectation.** The tail-sum identity gives \(\mathbb E[L]=\sum_{n\ge0}P_n(s)\). The two bounding series evaluate to
\[
\sum_{n\ge0}\frac{n+2}{2^{n+1}}=3,\qquad
\sum_{n\ge0}\frac{F_{n+3}}{2^{n+1}}=5.
\]
Every nonextremizing schedule differs strictly at some finite horizon, so the two equality characterizations follow.

**3. Periodic entropy, dimension and escape.** Let \(s\) repeat after \(r\) steps. Writing \(Q_s\) for the period product, the count of length \(kr+1\) admissible words is \((1,1)Q_s^k(1,1)^{\mathsf T}\). By Perron–Frobenius theory (including reducible polynomial-growth cases), its exponential growth is \(\rho(Q_s)^k\), which gives \(h=\log\rho(Q_s)/r\) and \(\gamma=\log2-h\). More precisely, the survivor coding is a finite graph-directed collection of disjoint dyadic intervals of contraction \(2^{-r}\). If \(\rho>1\), a Perron eigenmeasure gives a matching lower dimension bound and cylinder counting gives an upper bound, proving \(\dim_H=h/\log2\). If \(\rho=1\), the cylinder count grows subexponentially and the upper dimension bound is zero.

**4. Sharp periodic trichotomy.** The two single-hole matrices are real symmetric with operator norm \(\varphi\). Their opposite-symbol products satisfy
\[
M_0M_1=\begin{pmatrix}1&0\\2&1\end{pmatrix},\quad
M_1M_0=\begin{pmatrix}1&2\\0&1\end{pmatrix},\quad
\lVert M_0M_1\rVert_2=1+\sqrt2<\varphi^2.
\]
A cyclically alternating schedule has even period and a period product conjugate to a power of one of the displayed unipotent matrices; thus \(\rho=1\). A constant schedule has product \(M_i^r\) and \(\rho=\varphi^r\). If a periodic word contains both symbols, cyclically rotate the invertible factors to expose one mixed adjacent pair. Operator-norm submultiplicativity yields \(\rho(Q_s)\le(1+\sqrt2)\varphi^{r-2}<\varphi^r\).

For strict positivity away from alternation, each two-step product is entrywise at least the identity matrix, and a repeated adjacent hole symbol contributes \(M_i^2\) with spectral radius \(\varphi^2>1\). If a periodic schedule is not cyclically alternating, its cyclic word has such an equal adjacent pair. Repeating a period if necessary to make its length even and cyclically rotating the invertible factors puts that pair in a disjoint two-step block. All other blocks are entrywise at least the identity; hence the full nonnegative product dominates \(M_i^2\), so its spectral radius exceeds one. This proves \(0<h<\log\varphi\) for every other periodic schedule.

**5. Countability at alternation.** When \(s_j=j\bmod2\), make the digit change \(c_j=b_j\oplus(j\bmod2)\). The forbidden adjacent word at every time becomes \(01\), so all surviving infinite \(c\)-sequences are of the form \(1^k0^\infty\) for finite \(k\), together with \(1^\infty\). There are countably many. The complementary starting phase is equivalent after flipping digits, and the same conclusion holds.

## Verification
The accompanying `CHECK.py` enumerates all \(2^n\) schedules for each integer \(0\le n\le9\), independently enumerates binary words, and checks the exact matrix counts, both sharp envelopes and their equality cases. It also computes period-product eigenvalues for all \(2^r\) schedules of periods \(1\le r\le10\), confirming the periodic trichotomy in finite cases. All 1023 enumeration comparisons and 2046 spectral comparisons passed, together with rational survival checks. These experiments validate implementations but are **not** substitutes for the infinite proofs above.

## Relationship to prior work
Cheriyath and Agarwal studied symbolic escape through *fixed* cylinders and correlation-polynomial criteria, providing the motivating escape-rate setting (arXiv:1905.11767, first public 2019-05-28). Livorati, Georgiou, Dettmann and Leonel analyzed *time-dependent* holes in the doubling map with oscillating geometries (arXiv:1312.7030), but did not establish these two-hole, all-horizon scheduling extremizers. Atnip, Froyland, González-Tokman and Vaienti developed general random open-system thermodynamic formalism (arXiv:2103.04712). Agarwal, Cheriyath and Tikekar examined static Markov-measure escape (arXiv:2401.05118). Standard transfer-matrix methods underlie the proof, but the claimed result is the joint sharp **all-schedule** comparison, exact waiting-time endpoints, and periodic zero-entropy dichotomy for complementary moving holes.

## Limitations
The results require the two specific complementary binary length-two cylinders, equal fixed hole sizes, deterministic exogenous schedules, and an initial Lebesgue distribution. Periodic schedules alone are covered by the entropy/dimension trichotomy; no classification of arbitrary aperiodic survivor dimensions is claimed. This is an elementary-matrix proof and may be independently derivable from broader products-of-nonnegative-matrices literature; a complete publication-priority survey has not been established.

## References
- H. Cheriyath and N. Agarwal, *Subshifts of Finite Type with a Hole*, arXiv:1905.11767 (version 1, 2019-05-28); DOI 10.1017/S1446788722000052.
- A. Livorati, O. Georgiou, C. P. Dettmann and E. D. Leonel, *Escape through a time-dependent hole in the doubling map*, arXiv:1312.7030 (2013).
- J. Atnip, G. Froyland, C. González-Tokman and S. Vaienti, *Thermodynamic Formalism for Random Interval Maps with Holes*, arXiv:2103.04712 (2021).
- N. Agarwal, H. Cheriyath and S. N. Tikekar, *On Escape Rate for Subshift with Markov Measure*, arXiv:2401.05118 (2024).
