# Exact two-phase entry-time distribution for modulo-four cyclic sums at every even length

## Finding
For each even integer \(n\ge 2\), consider the cyclic-sum map
\[
D:(\mathbb Z/4\mathbb Z)^n\longrightarrow(\mathbb Z/4\mathbb Z)^n,\qquad
D(a_0,\ldots,a_{n-1})=(a_0+a_1,\ldots,a_{n-1}+a_0),
\]
where arithmetic is modulo four. Let \(\tau(a)\) be the minimum number of applications of \(D\) required for the orbit of \(a\) to reach a periodic point; a point already on a cycle has \(\tau(a)=0\). Write \(q=2^{\nu_2(n)}\), the largest power of two dividing \(n\). Then the *complete* number of starting vectors with each possible preperiod is
\[
\#\{a:\tau(a)=t\}=\begin{cases}
4^{n-q},&t=0,\\
3\,4^{n-q+t-1},&1\le t\le q/2,\\
4^{n-q}\,2^{q/2+t-1},&q/2<t\le 3q/2,\\
0,&t>3q/2.
\end{cases}
\]
In particular, the maximum possible preperiod is exactly \(3q/2\) and *exactly half* of the \(4^n\) starting vectors attain that maximum. For a uniform random starting vector, the normalized entry-time distribution depends on \(n\) only through \(\nu_2(n)\), not the odd part of \(n\).

Equivalently, for each nonnegative integer \(t\),
\[
\Pr(\tau\le t)=2^{-e_q(t)},\quad e_q(t)=\begin{cases}
2(q-t),&0\le t\le q/2,\\
3q/2-t,&q/2\le t\le 3q/2,\\
0,&t\ge3q/2.
\end{cases}
\]
The duplicated boundary values agree.

## Assumptions and scope
This is the **cyclic modular sum**, not the absolute-difference game over integers. Every coordinate belongs to \(\mathbb Z/4\mathbb Z\), \(n\) is any even integer (not necessarily a power of two), and \(\tau\) counts iterations before the first periodic vector. The exact, not asymptotic, classification covers all starting vectors and all possible times. The primary classification is 11B83 (special sequences of integers and their arithmetic behavior).

## Proof
**1. Split the invertible and nilpotent components.** Represent a vector by its coefficients in
\[
R=(\mathbb Z/4\mathbb Z)[x]/(x^n-1),
\]
so, up to reversing the cyclic order, \(D\) is multiplication by \(1+x\). Put \(n=qh\) with \(h\) odd and \(q\) a positive power of two. The factorization
\[
x^n-1=(x^q-1)Q(x),\qquad Q(x)=\sum_{j=0}^{h-1}x^{jq}
\]
has relatively prime factors modulo two: \(x^q-1\equiv(x+1)^q\) and \(Q(1)\equiv h\equiv1\pmod2\). They are therefore comaximal also over \(\mathbb Z/4\mathbb Z\), by lifting a Bézout relation (a polynomial congruent to one modulo two is invertible modulo four). The Chinese remainder theorem gives
\[
R\cong A\times B,\quad
A=(\mathbb Z/4\mathbb Z)[x]/(x^q-1),\quad
B=(\mathbb Z/4\mathbb Z)[x]/Q(x).
\]
The factor \(B\) has cardinality \(4^{n-q}\), and multiplication by \(1+x\) is a bijection on it. As shown below, multiplication by \(1+x\) on \(A\) is nilpotent. Consequently, a vector is periodic if and only if its \(A\)-component is zero; its entry time is precisely the smallest \(t\) annihilating that component.

**2. Determine the nilpotent local ring and all image sizes.** Set \(y=1+x\). The intermediate binomial coefficients of \((y-1)^q\) are divisible by four except the middle one, whose valuation is exactly one; this follows from \(\nu_2\binom qj=\nu_2(q)-\nu_2(j)\) for \(1\le j<q\). The sign of the middle term is immaterial modulo four. Thus
\[
A\cong(\mathbb Z/4\mathbb Z)[y]/(y^q+2y^{q/2}),
\quad y^q=2y^{q/2},\quad y^{3q/2}=0.
\]
The displayed quotient is free with basis \(1,y,\ldots,y^{q-1}\) over \(\mathbb Z/4\mathbb Z\). Write \(I_t=y^t A\). For \(0\le t\le q/2\), the image is free on \(y^t,\ldots,y^{q-1}\), hence \(\lvert I_t\rvert=4^{q-t}\). For \(q/2\le t\le q\), the image has free coordinates \(y^t,\ldots,y^{q-1}\), together with independent order-two coordinates \(2y^{q/2},\ldots,2y^{t-1}\), giving \(\lvert I_t\rvert=4^{q-t}2^{t-q/2}=2^{3q/2-t}\). For \(q\le t\le3q/2\), it has order-two coordinates \(2y^{t-q/2},\ldots,2y^{q-1}\), again giving \(\lvert I_t\rvert=2^{3q/2-t}\). For larger \(t\), \(I_t=0\). Therefore
\[
\lvert I_t\rvert=2^{e_q(t)},\qquad t\ge0.
\]
In particular \(y^{3q/2-1}=2y^{q-1}\ne0\), verifying sharp nilpotency index \(3q/2\).

**3. Count all entry times.** The fiber of the endomorphism \(y^t:A\to A\) has cardinality \(\lvert A\rvert/\lvert I_t\rvert\). The periodic \(B\) component can be chosen arbitrarily. Hence
\[
\#\{a:\tau(a)\le t\}
=4^{n-q}\cdot\frac{4^q}{\lvert I_t\rvert}
=4^n2^{-e_q(t)}.
\]
Taking successive differences yields the stated three regimes. At \(t=3q/2\), the number with *exact* entry time \(t\) is \(4^n-4^n/2=4^n/2\), proving the half-of-all-vectors assertion. No counting limit or experiment is used in the proof.

## Verification
The companion file `verify.py` implements two complementary finite tests of the formulas using Python's standard library. First, it computes the images of the actual circulant matrices of \(D^t\) over \(\mathbb Z/4\mathbb Z\), using elementary invertible row and column operations to determine their cardinalities for 12 even lengths up to 32 and all relevant powers. Second, it enumerates all initial vectors and traces their exact first entrance into the periodic-point set for lengths \(2,4,6,8\). The completed checks give `VERIFY_OK exhaustive_tuples=69904 matrix_checks=165 even_lengths=12`. These computations are finite consistency tests; the preceding algebra proves the statements for arbitrary even \(n\).

## Relationship to prior work
Dular's *Cycles of Sums of Integers* (arXiv:1905.01765, first posted 2019-05-05) studies exactly this cyclic-sum operator for general residue rings and tuple lengths, characterizing cycles and their periods. Its Section 8 asks for the largest possible preperiod. Lewis and Tefft (arXiv:2401.17502, first posted 2024-01-30) establish the maximal vanishing time \((\ell+1)2^{k-1}\) when the tuple length and modulus are powers of two, including \(3q/2\) when the modulus is four. Their further work (arXiv:2410.18204, first posted 2024-10-23) analyzes maximal entry time at all even lengths. These previously known results on the **maximum** are not claimed as new here. The present theorem determines the **complete number of starting tuples at every entry time** and the odd-multiplier invariance of the entire normalized distribution. The full accessible versions of these three papers were compared for covering statements and implications, including the cycle-characterization sections and maximal-length proofs; none of the inspected statements gives the whole distribution. A stronger implicit result in older literature remains a possible bibliographic risk.

## Limitations
This result concerns only modulus four and even tuple lengths. It does not classify the distribution of periods within cycles, higher prime-power moduli, or odd tuple lengths. The theoretical proof is complete within these hypotheses; earlier implicit formulations in unindexed or inaccessible literature cannot be ruled out absolutely. The attached test suite is not an independent mathematical audit.

## References
1. Bruno Dular, *Cycles of Sums of Integers*, arXiv:1905.01765 (2019), https://arxiv.org/abs/1905.01765.
2. Mark L. Lewis and Shannon M. Tefft, *The Period of Ducci Cycles on \(\mathbb Z_{2^\ell}\) for Tuples of Length \(2^k\)*, arXiv:2401.17502 (2024), https://arxiv.org/abs/2401.17502.
3. Mark L. Lewis and Shannon M. Tefft, *The Maximum Length for Ducci Sequences on \(\mathbb Z_m^n\) when \(n\) is Even*, arXiv:2410.18204 (2024), https://arxiv.org/abs/2410.18204.
