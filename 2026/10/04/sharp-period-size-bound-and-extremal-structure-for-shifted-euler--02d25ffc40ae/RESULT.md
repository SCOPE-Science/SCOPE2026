# Sharp period-size bound and extremal structure for shifted Euler cycles

## Finding
Fix an integer \(k\ge2\) and define
\[
F_k(n)=\varphi(n)+k.
\]
Let
\[
(x_1,\ldots,x_T)
\]
be a periodic orbit of minimal period \(T\), so that the \(x_i\) are distinct and
\[
x_{i+1}=F_k(x_i)
\]
cyclically. Put
\[
M=\max_{1\le i\le T}x_i.
\]
Then
\[
M\le [T(k-1)+1]^2.
\]
Equivalently,
\[
T\ge \frac{\sqrt M-1}{k-1}.
\]

The bound has an exact equality classification. Equality holds if and only if
\[
q=T(k-1)+1
\]
is prime and each of
\[
q^2-j(k-1),\qquad 1\le j\le T-1,
\]
is prime. In that case the cycle is
\[
q^2-(T-1)(k-1)\to q^2-(T-2)(k-1)\to\cdots\to q^2-(k-1)\to q^2\to q^2-(T-1)(k-1).
\]
Thus the extremal cycles are exactly the construction suggested by Leonetti and Luca: all terms except the final one are primes in arithmetic progression, and the final composite term is forced to be the square of a prime.

The equality case is genuinely attained for periods beyond two. For example, with
\[
T=3,\qquad k=3301,\qquad q=9901,
\]
one obtains the exact cycle
\[
98023201\to98026501\to98029801\to98023201,
\]
where the first two terms and \(q=9901\) are prime and
\[
98029801=9901^2=[3(3300)+1]^2.
\]

## Assumptions and scope
Euler's totient is denoted by \(\varphi\), with \(\varphi(1)=1\). The parameter \(k\) is an integer with \(k\ge2\). A period-\(T\) orbit means a minimal periodic orbit containing exactly \(T\) distinct positive integers.

The result concerns the one-step shifted Euler map \(F_k(n)=\varphi(n)+k\). It does not concern the separate two-step recurrence studied in the same source and in a later improvement paper.

No assertion is made that extremal cycles exist for every pair \((T,k)\), or that there are infinitely many extremal periods. The equality criterion converts that existence question into an explicit simultaneous primality problem.

## Proof
Define the cototient
\[
c(n)=n-\varphi(n).
\]
Since
\[
x_{i+1}=\varphi(x_i)+k,
\]
we have
\[
c(x_i)=x_i-x_{i+1}+k.
\]
Summing cyclically over one period makes the telescoping part vanish, so
\[
\sum_{i=1}^{T}c(x_i)=Tk. \tag{1}
\]

No term of the cycle is \(1\): a predecessor would have to satisfy \(\varphi(n)+k=1\), impossible for \(k\ge2\). Hence every \(x_i\ge2\), and therefore
\[
c(x_i)\ge1. \tag{2}
\]
Moreover, equality in (2) occurs exactly when \(x_i\) is prime. Indeed, primes have cototient \(1\), while every composite \(n\) satisfies the stronger bound below.

The maximum \(M\) cannot be prime. If it were prime, then
\[
F_k(M)=M-1+k=M+k-1>M,
\]
contradicting maximality in a periodic orbit. Thus \(M\) is composite.

Let \(p\) be the least prime factor of \(M\). Then \(p\le\sqrt M\), and
\[
\varphi(M)
=M\prod_{r\mid M}\left(1-\frac1r\right)
\le M\left(1-\frac1p\right).
\]
Consequently,
\[
c(M)=M-\varphi(M)\ge\frac Mp\ge\sqrt M. \tag{3}
\]
This is the same standard composite-totient inequality used in the source paper.

Now combine (1), (2), and (3). The other \(T-1\) cototients contribute at least \(T-1\), so
\[
\sqrt M\le c(M)\le Tk-(T-1)=T(k-1)+1.
\]
Squaring gives
\[
M\le[T(k-1)+1]^2.
\]

It remains to classify equality. Equality in the final bound forces equality at every preceding step. Thus
\[
c(M)=\sqrt M=T(k-1)+1
\]
and every other cycle term has cototient \(1\), hence is prime.

Equality in (3) is rigid. Equality in
\[
\varphi(M)\le M\left(1-\frac1p\right)
\]
forces \(p\) to be the only distinct prime factor of \(M\), while equality in
\[
\frac Mp\ge\sqrt M
\]
forces \(p=\sqrt M\). Therefore
\[
M=q^2
\]
for the prime
\[
q=T(k-1)+1.
\]

For a prime \(r\), the map advances by the constant increment
\[
F_k(r)=r+(k-1).
\]
Since all terms preceding the maximum are prime, the cycle must therefore be
\[
q^2-(T-1)(k-1),\ q^2-(T-2)(k-1),\ \ldots,\ q^2-(k-1),\ q^2.
\]
The return from the final square is
\[
F_k(q^2)=q^2-q+k.
\]
Using \(q=T(k-1)+1\), this equals
\[
q^2-(T-1)(k-1),
\]
so the displayed list closes into a cycle.

Conversely, suppose \(q=T(k-1)+1\) is prime and all \(q^2-j(k-1)\) with \(1\le j\le T-1\) are prime. Every prime term advances by \(k-1\), and the calculation above sends \(q^2\) back to the first term. The terms are distinct because \(k-1>0\), so the displayed orbit has minimal period \(T\) and attains equality.

## Verification
The accompanying `verify.py` uses only integer arithmetic and deterministic trial division.

It checks the theorem against all cycles reached from starting values \(1\le x_1\le600\) for every \(2\le k\le80\). For every discovered minimal cycle it verifies the telescoping identity
\[
\sum c(x_i)=Tk,
\]
the period-size bound, and the full equality characterization whenever equality occurs.

The script also verifies from first principles the explicit extremal examples
\[
23\to25\to23
\]
for \((T,k)=(2,3)\),
\[
98023201\to98026501\to98029801\to98023201
\]
for \((T,k)=(3,3301)\), and
\[
1129002001\to1129010401\to1129018801\to1129027201\to1129002001
\]
for \((T,k)=(4,8401)\).

These finite checks are regression tests only. The theorem for all \(k\ge2\) and all finite periods \(T\) is proved symbolically above.

## Relationship to prior work
Leonetti and Luca prove that every orbit of \(F_k(n)=\varphi(n)+k\) is eventually periodic and give an upper bound for a trajectory in terms of its initial value and \(k\). Their paper explicitly leaves sharpness and nontrivial size information as open questions. It then singles out, as a possible construction, a cycle whose terms are primes in arithmetic progression except for the last term.

The result here gives a period-sensitive bound that is independent of the starting point once a periodic orbit is fixed, and it exactly characterizes equality. The source's proposed prime-progression pattern is not merely one possible extremal shape: equality forces it, forces the last term to be a prime square, and forces the square root to satisfy \(q=T(k-1)+1\).

A later paper by Danh, Dung, Hung, Kien, Thinh, Toan, and Tho improves Leonetti and Luca's bound for the different two-step recurrence
\[
x_{n+2}=\varphi(x_{n+1})+\varphi(x_n)+k.
\]
Its stated result therefore does not imply the one-step cycle theorem proved here.

The cototient sequence \(n-\varphi(n)\) is catalogued as OEIS A051953. That entry records the arithmetic function itself and related formulas, but it does not state the cyclic telescoping identity, the period-size bound, or the extremal shifted-Euler classification.

Targeted searches for the exact shifted-Euler map, cototient formulation, period bound, and equality shape did not locate a published statement implying this theorem.

## Limitations
The theorem assumes \(k\ge2\). The cases \(k=0\) and \(k=1\) have different monotonic behavior and are not included.

The equality criterion does not solve the simultaneous-primality problem for arbitrary \((T,k)\), and it does not prove infinitely many extremal cycles. The displayed examples only certify that equality is attained for several small periods.

Non-detection in the literature cannot exclude an equivalent formulation in an unindexed source.

## References
1. Paolo Leonetti and Florian Luca, “On the iterates of shifted Euler's function,” arXiv:2302.01783v1, first posted 3 February 2023; published as “On the iterates of the shifted Euler's function,” *Bulletin of the Australian Mathematical Society* 109 (2024), 206–214, DOI 10.1017/S0004972723000394. Primary MSC \(11B37\).
2. Tran Nguyen Thanh Danh, Hoang Tuan Dung, Pham Viet Hung, Nguyen Dinh Kien, Nguyen An Thinh, Khuc Dinh Toan, and Nguyen Xuan Tho, “An improvement to a theorem of Leonetti and Luca,” *Bulletin of the Australian Mathematical Society* 109 (2024), 437–442, DOI 10.1017/S0004972723000862.
3. OEIS A051953, “Cototient(n) := n - phi(n).”
