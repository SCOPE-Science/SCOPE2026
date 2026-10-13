# An explicit leading constant for the reciprocal iterated-divisor sum

## Finding

Let \(\tau(n)=\sum_{d\mid n}1\) be the divisor-count function, with \(\tau(1)=1\). Let \(\omega(n)\) count distinct prime factors. A positive integer \(b\) is **powerful** if each prime dividing it occurs to exponent at least two; by convention \(1\) is powerful. For each powerful \(b\), write
\[
\tau(b)=2^{u_b}v_b,\qquad u_b=\nu_2(\tau(b)),\qquad 2\nmid v_b.
\]
Then the positive, absolutely convergent series
\[
C=\frac{1}{\zeta(2)}\sum_{\substack{b\ge1\\b\text{ powerful}}}
\frac{1}{b\,\tau(v_b)}\prod_{p\mid b}\frac{p}{p+1}
\]
is the exact leading constant in
\[
\boxed{\sum_{n\le x}\frac{1}{\tau(\tau(n))}\sim C\frac{x}{\log\log x}}\qquad(x\to\infty).
\]
Moreover,
\[
\frac1{\zeta(2)}<C<\frac{\zeta(3)}{\zeta(6)}.
\]
This establishes the constant-asymptotic conjecture stated as Equation (8) in Campbell's 2026 study of the reciprocal iterated-divisor sum.

## Assumptions and scope

All variables \(n,b,a\) are positive integers and \(x\) tends to infinity through real values. Every \(n\) has a unique factorization \(n=ab\), where \(a\) consists of exactly the primes occurring to exponent one in \(n\), while \(b\) consists of the remaining prime-power factors. Thus \(a\) is squarefree, \(b\) is powerful, and \(\gcd(a,b)=1\). The empty products for \(a=1\) or \(b=1\) have their usual values. No unproved distributional conjecture is used.

## Proof

**1. Exact decomposition.** For the unique \(n=ab\) described above, multiplicativity of \(\tau\) gives
\[
\tau(n)=2^{\omega(a)}\tau(b)=2^{\omega(a)+u_b}v_b.
\]
Because \(v_b\) is odd, multiplicativity again gives the exact identity
\[
\frac1{\tau(\tau(n))}=
\frac1{(\omega(a)+u_b+1)\tau(v_b)}.\tag{1}
\]
In particular, for every fixed powerful \(b\), the contribution of integers with powerful part exactly \(b\) is
\[
\frac1{\tau(v_b)}
\sum_{\substack{a\le x/b\\\mu^2(a)=1\\(a,b)=1}}
\frac1{\omega(a)+u_b+1}.\tag{2}
\]

**2. A fourth-moment concentration estimate.** Put \(L_y=\log\log y\) for large \(y\). We use the elementary estimate
\[
\sum_{m\le y}\bigl(\omega(m)-L_y\bigr)^4\ll yL_y^2.\tag{3}
\]
Here is a proof of the estimate, rather than an assumption about the tails of the normal-order theorem. Let \(Y=y^{1/10}\), and set
\[
S(m)=\sum_{p\le Y}\bigl(\mathbf1_{p\mid m}-1/p\bigr).
\]
Every \(m\le y\) has at most nine distinct prime divisors exceeding \(Y\). Mertens' estimate gives \(\sum_{p\le Y}1/p=L_y+O(1)\), so
\[
\omega(m)-L_y=S(m)+O(1)
\]
uniformly. Expand the fourth power of \(S(m)\). For any set of at most four distinct primes, the average over \(m\le y\) of their joint divisibility indicator differs by at most \(O(1/y)\) from the corresponding product of the probabilities \(1/p\). There are at most \(O(\pi(Y)^4)\) terms, so the total averaged discrepancy is \(O(Y^4/y)=O(y^{-3/5})\). In the independent Bernoulli model, the fourth centered moment is at most a constant times
\[
\sum_{p\le Y}\frac1p+\left(\sum_{p\le Y}\frac1p\right)^2\ll L_y^2.
\]
This proves (3). In particular, for every fixed \(\varepsilon>0\),
\[
\#\{m\le y:|\omega(m)-L_y|>\varepsilon L_y\}
\ll_\varepsilon \frac{y}{L_y^2}.\tag{4}
\]
The fourth moment, rather than a variance bound alone, is important: after multiplication by \(L_y\), the exceptional contribution to a reciprocal average still tends to zero.

**3. A fixed powerful part.** For fixed \(b\), squarefree inclusion--exclusion with the coprimality constraint gives
\[
\#\{a\le y:\mu^2(a)=1,\ (a,b)=1\}
=\delta_b y+O_b(\sqrt y),\qquad
\delta_b=\frac1{\zeta(2)}\prod_{p\mid b}\frac p{p+1}.\tag{5}
\]
By (4), the exceptional values \(|\omega(a)-L_y|>\varepsilon L_y\) contribute at most
\[
O_\varepsilon(y/L_y^2)
\]
to the reciprocal sum in (2), since every summand is at most one. On the remaining integers,
\[
\frac{L_y}{\omega(a)+u_b+1}
\in\left[\frac1{1+\varepsilon+o(1)},
\frac1{1-\varepsilon+o(1)}\right]
\]
for fixed \(b\). Equation (5), followed by \(\varepsilon\downarrow0\), therefore gives
\[
\sum_{\substack{a\le y\\\mu^2(a)=1\\(a,b)=1}}
\frac1{\omega(a)+u_b+1}
\sim\delta_b\frac{y}{\log\log y}.\tag{6}
\]
Taking \(y=x/b\), the normalized contribution from this fixed \(b\) tends to \(\delta_b/[b\tau(v_b)]\).

**4. Uniform domination of the powerful tail.** From (3), the integers \(m\le y\) with \(\omega(m)<L_y/2\) number \(O(y/L_y^2)\). Splitting at that threshold proves the uniform bound
\[
\sum_{m\le y}\frac1{\omega(m)+1}\ll\frac{y}{\log\log y}\qquad(y\text{ sufficiently large}).\tag{7}
\]
Every powerful \(b\) has a unique representation \(b=r^2s^3\), with \(s\) squarefree. Consequently
\[
\#\{b\le t:b\text{ powerful}\}
\le\sum_{s\le t^{1/3}}\left\lfloor\sqrt{t/s^3}\right\rfloor
\ll\sqrt t,
\]
and partial summation yields
\[
\sum_{\substack{b>B\\b\text{ powerful}}}\frac1b\ll B^{-1/2}.\tag{8}
\]
For \(B<b\le\sqrt x\), using (7) with \(y=x/b\) and \(u_b\ge0\) bounds their combined contribution by
\[
\ll\frac{x}{\log\log x}
\sum_{\substack{b>B\\b\text{ powerful}}}\frac1b
\ll\frac{x}{\sqrt B\log\log x}.
\]
For \(b>\sqrt x\), bounding every summand by one gives at most
\[
x\sum_{\substack{b>\sqrt x\\b\text{ powerful}}}\frac1b
\ll x^{3/4}=o\left(\frac{x}{\log\log x}\right).
\]
Thus the normalized tail contributes \(O(B^{-1/2})+o(1)\), uniformly as \(x\to\infty\). First use (6) on a finite collection of powerful \(b\), then let \(B\to\infty\). The positive series defining \(C\) converges absolutely by (8), and the claimed asymptotic follows.

**5. Positive finite constant.** The \(b=1\) term is \(1/\zeta(2)\); the \(b=4\) term adds \(1/(12\zeta(2))\), so the lower inequality is strict. Also \(\delta_b\le1/\zeta(2)\) and \(\tau(v_b)\ge1\). Since
\[
\sum_{\substack{b\ge1\\b\text{ powerful}}}\frac1b
=\frac{\zeta(2)\zeta(3)}{\zeta(6)},
\]
we obtain \(C<\zeta(3)/\zeta(6)\), completing the proof.

## Verification

`artifacts/verify.py` is a standalone standard-library Python program. It constructs \(\tau(n)\) with a least-prime-factor sieve, compares the result against independent direct divisor counts, and verifies identity (1) for every \(1\le n\le200000\). It also enumerates powerful integers through \(100000\) both from their factorizations and from the unique \(r^2s^3\) representation, and evaluates a **partial** sum of the constant series. `artifacts/replay.txt` records the program's output.

The finite checks are not substituted for the fourth-moment proof, the fixed-\(b\) limiting argument, or the uniform powerful-tail bound.

## Relationship to prior work

John M. Campbell, *On divisor sums due to Erdős and Ramanujan* (arXiv:2605.00695v1, May 1, 2026), establishes only the order of magnitude
\[
\sum_{n\le x}\frac1{\tau(\tau(n))}\asymp\frac{x}{\log\log x}
\]
and explicitly conjectures an asymptotic equivalent with a positive constant in his Equation (8). The paper already introduces the squarefree/powerful decomposition, but its exceptional-set estimates leave errors on the main-term scale. The present proof upgrades those estimates using a fourth moment, isolates a fixed powerful part, and controls the infinite remaining sum uniformly. The exact constant is new relative to the inspected source.

The historical Erdős asymptotic for \(\sum_{n\le x}\tau(\tau(n))\) concerns a different, non-reciprocal sum and does not imply this result. Searches for equivalent reciprocal-iteration formulations and stronger published coverage found no theorem resolving Campbell's Equation (8).

## Limitations

The theorem proves a first-order asymptotic but no effective secondary term or rate of convergence. The standalone finite calculations check identities and series truncations only; they do not certify the infinite limit. Undiscovered or unindexed equivalent work remains a bibliographic possibility.

## References

1. John M. Campbell, *On divisor sums due to Erdős and Ramanujan*, arXiv:2605.00695v1 (submitted 2026-05-01), especially Section 1.2, Equation (8), Sections 2–3 and the conclusion.
2. P. Erdős, *On the sum of \(\sum_{n\le x}\tau(\tau(n))\)*, Math. Student 36 (1968), 227–229 (non-reciprocal comparison, as cited in Campbell).
3. S. W. Golomb, *Powerful numbers*, Amer. Math. Monthly 77 (1970), 848–855 (background; the needed bound is independently derived above).
