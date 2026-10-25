# Odd-length cubic Fibonacci and Lucas window GCDs

## Finding
Let \(F_0=0\), \(F_1=1\), \(L_0=2\), \(L_1=1\), and \(X_{n+2}=X_{n+1}+X_n\) for either \(X=F\) or \(X=L\). For every positive **odd** integer \(k\), put
\[
G_X(k)=\gcd_{n\ge0}\left(\sum_{j=1}^{k}X_{n+j}^{3}\right).
\]
Then, for both the Fibonacci and Lucas sequences,
\[
\boxed{G_F(k)=G_L(k)=\begin{cases}2,& k\equiv3\pmod6,\\1,&k\equiv1,5\pmod6.\end{cases}}
\]
In particular every odd-window cubic GCD is at most two; the entire two-family classification is independent of the size of the odd window.

## Assumptions and scope
Indices \(n\) are nonnegative and window lengths \(k\) are positive odd integers. Both sequences are specified by the above initial values. The GCD of an infinite nonzero set of integers denotes its positive common divisor. No assertion about an arbitrary generalized-Fibonacci initial pair or even window lengths is part of this finding.

## Proof
**1. An invertible recurrence for cubes.** For \(X=F\) or \(L\), write \(u_n=X_n^3\). The roots of the Fibonacci characteristic polynomial \(z^2-z-1\) are \(\alpha,\beta\), with \(\alpha\beta=-1\). The four possible exponential bases in \(u_n\) are \(\alpha^3,\beta^3,-\alpha,-\beta\); their monic characteristic polynomial is
\[
(z^2-4z-1)(z^2+z-1)=z^4-3z^3-6z^2+3z+1.
\]
Thus, over the integers and after reduction modulo any positive modulus,
\[
u_{n+4}-3u_{n+3}-6u_{n+2}+3u_{n+1}+u_n=0.\tag{1}\]
In particular the coefficient of \(u_n\) is a unit. Fix \(k\). If \(u_{t+k}-u_t\equiv0\pmod p\) for every \(t\ge1\), then (1), applied to the difference sequence at \(t=0\), also forces the identity at \(t=0\).

**2. No odd prime divides the window GCD.** Suppose an odd prime \(p\) divides \(G_X(k)\), where \(k\) is odd. Consecutive window subtraction gives
\[
\sum_{j=1}^{k}X_{n+1+j}^3-\sum_{j=1}^{k}X_{n+j}^3
=X_{n+k+1}^3-X_{n+1}^3.
\]
Hence \(X_{t+k}^3\equiv X_t^3\pmod p\) for every \(t\ge1\), and by step 1 also for \(t=0\).

For \(X=F\), the cases \(t=0,1\) give \(F_k\equiv0\) and \(F_{k+1}^3\equiv1\pmod p\). Cassini's identity
\[
F_{k+1}^2-F_kF_{k+2}=(-1)^k=-1
\]
gives \(F_{k+1}^2\equiv-1\pmod p\). Cubing the last congruence yields \(F_{k+1}^6\equiv-1\), but squaring the earlier cube identity yields \(F_{k+1}^6\equiv1\), so \(p=2\), a contradiction.

For \(X=L\), set \(a=L_k\pmod p\) and \(b=L_{k+1}\pmod p\). Using \(t=0,1,2,3\), recurrence and \((L_0,L_1,L_2,L_3)=(2,1,3,4)\), we have
\[
a^3=8,\qquad b^3=1,\qquad(a+b)^3=27,\qquad(a+2b)^3=64\pmod p.
\]
The class \(b\) is invertible. Set \(x=a/b\). Subtraction of adjacent cube equations gives \(3(x+3)(x-2)=3(x+5)(x-2)=0\). Their difference is \(6(x-2)=0\). If \(p\ne3\), then \(x=2\). If \(p=3\), \(x^3=8\) also forces \(x=2\). Hence \(a=2b\) for every odd \(p\). The Lucas Cassini identity \(L_kL_{k+2}-L_{k+1}^2=5(-1)^k=-5\) becomes \(5b^2=-5\pmod p\). If \(p\ne5\), then \(b^2=-1\), contradicting \(b^3=1\) as in the Fibonacci case. If \(p=5\), cubing is a permutation of \(\mathbf F_5\), so \(b=1\), \(a=2\). But the Lucas sequence modulo five repeats \((2,1,3,4)\) with minimal period four. Thus \((L_k,L_{k+1})\equiv(2,1)\pmod5\) forces \(4\mid k\), impossible for odd \(k\). Therefore no odd prime divides either GCD.

**3. Exact power of two.** In each of the Fibonacci and Lucas sequences, the residues modulo two repeat with period three and contain precisely two ones per period. Cubing preserves parity. For odd \(k\equiv3\pmod6\), every window contains an integral number of three-term parity periods, so every cubic window sum is even. But the sequences modulo four each have period six and satisfy \(X_1\equiv1\), \(X_4\equiv3\pmod4\). Therefore, when \(k\equiv3\pmod6\),
\[
X_{k+1}^3-X_1^3\equiv3^3-1^3\equiv2\pmod4.
\]
A difference of two window sums is not divisible by four. Accordingly their GCD is exactly two. If \(k\equiv1,5\pmod6\), shifting a window changes its parity at some starting index: for \(k\equiv1\pmod6\), take \(t=2\) in \(X_{t+k}^3-X_t^3\), and for \(k\equiv5\pmod6\), take \(t=1\). Those differences are odd because the indices hit distinct parity classes modulo three. Hence the GCD is odd and, by step 2, equals one. This proves the theorem.

## Verification
The included `verify.py` performs exact integer checks of recurrence (1), the GCD of twenty translated sums for every odd \(1\le k\le201\) in both families, and the difference-GCD over eleven shifts. It also checks modular witnesses for ten odd primes and all odd \(1\le k\le79\). Every assertion passed when executed. These bounded checks independently corroborate the fully quantified proof; they are not extrapolated to untested integers.

## Relationship to prior work
Mbirika and Spilker (arXiv:2204.12626, 2022) establish analogous complete GCD formulas for **squares** and pose a higher-power question in Section 6.1, concentrating explicitly on even windows. Separate earlier work gives the even-window cubic GCDs. The present theorem addresses the complementary positive odd window lengths without assuming any even-window formula. Adegoke (arXiv:1706.08469, 2017) proves factorizations for sums over **even-indexed subsequences**; these are not GCDs over all translations of consecutive odd-length cubic windows. A direct published antecedent has not been identified in the literature inspected.

## Limitations
There is no claim for arbitrary initial conditions, higher powers, or even-length windows. The originality comparison is necessarily bounded by available indexed literature and may miss an implicit earlier consequence of a general cube-sum theorem. The arithmetic argument is elementary, so independent publication-priority confirmation would be useful.

## References
- aBa Mbirika and Jürgen Spilker, *GCD of sums of \(k\) consecutive squares of generalized Fibonacci numbers*, arXiv:2204.12626 (first submitted 2022-04-26), especially Section 6.1, https://arxiv.org/abs/2204.12626.
- Kunle Adegoke, *Factored closed-form expressions for the sums of cubes of Fibonacci and Lucas numbers*, arXiv:1706.08469 (2017), https://arxiv.org/abs/1706.08469.
