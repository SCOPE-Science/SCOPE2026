# An irrational period-two density for the dyadic arithmetic partial derivative

## Finding

For a nonzero integer \(x\), write \(\nu_2(x)\) for its \(2\)-adic valuation, and set
\[
D_2(x)=\frac{x\nu_2(x)}2,\qquad D_2(0)=0.
\]
For each integer \(m\ge2\), consider the valuation trajectory
\[
v_j(m)=\nu_2\bigl(D_2^{\,j}(2^m)\bigr)\qquad(j\ge0).
\]
It is eventually periodic, with least eventual period either \(1\) or \(2\). Let \(E\) consist of the exponents \(m\ge2\) for which the least eventual period is \(2\).

Define \(T(r)=1+\nu_2(\lfloor(r-1)/2\rfloor)\) for integers \(r\ge3\), and define \(F:\mathbb Z_{\ge1}\to\{1,2\}\) recursively by \(F(1)=1\), \(F(2)=2\), and \(F(r)=F(T(r))\) for \(r\ge3\). This terminates because \(1\le T(r)<r\). Set \(A=\{r\ge1:F(r)=2\}\). Then:

1. \(m\in E\) if and only if \(m+1\in A\).
2. \(A\) has the exact, disjoint self-similar description
   \[
   A=\{2\}\ \sqcup\!
   \bigsqcup_{\substack{t\in A\\h\ge0}}
   \bigl\{2^t(2h+1)+1,\ 2^t(2h+1)+2\bigr\}.
   \]
3. The natural density of \(E\), taken over the **exponents** \(m\), is the number
   \[
   \alpha=\sum_{r\in A}2^{-r}
   =0.297058823704034\ldots .
   \]
   More precisely, for every integer \(N\ge2\),
   \[
   \#\{m\in E:2\le m\le N\}=\alpha N+O(\log(N+2)).
   \]
4. \(\alpha\) is irrational. Its binary fractional digits are exactly \(\mathbf 1_A(1),\mathbf 1_A(2),\ldots\), and this binary sequence is not eventually periodic.

## Assumptions and scope

The only input is a nonnegative integer exponent \(m\ge2\) and the ordinary arithmetic partial derivative with respect to the prime \(2\). The density counts **exponent values**, not all positive integers, not general \(2\)-adic starting values, and not weighted integer samples. The valuation of zero is not needed because these trajectories never reach zero. A period is the least positive integer that repeats the valuation sequence after some finite transient; it is not the period of the rapidly growing integer trajectory itself.

## Proof

**1. Direct valuation dynamics and exact period labels.** For every integer \(x\ne0\) with \(v=\nu_2(x)\ge2\),
\[
\nu_2(D_2(x))=v+\nu_2(v)-1.
\]
Thus all valuations remain at least \(2\), and the valuation trajectory depends only on its initial exponent. If \(v\ge3\) is odd, its next value is \(v-1\), which is even. We analyze the dynamics at even valuations \(v\), writing \(k=\nu_2(v)\ge1\).

If \(k=1\), then \(v\) is fixed. If \(k=2\), then the orbit alternates \(v,v+1,v\), with exact period \(2\). If \(k\ge3\) is odd, the next value is the even integer \(v+k-1\), whose valuation is \(\nu_2(k-1)=T(k)\), since \(0<k-1<2^k\). If \(k\ge4\) is even, the next two values are \(v+k-1\) (odd) and \(v+k-2\) (even); the latter has valuation \(\nu_2(k-2)=T(k)\), again because \(0<k-2<2^k\). In either case \(1\le T(k)<k\). Repeating these finite blocks reaches \(k=1\) or \(k=2\), yielding the exact least eventual valuation period \(F(k)\).

For an initial exponent \(m\ge2\), after at most one step the even valuation is \(2\lfloor m/2\rfloor\). Its \(2\)-adic order is
\[
1+\nu_2(\lfloor m/2\rfloor)=T(m+1).
\]
The preceding block argument shows that the eventual period is \(F(T(m+1))=F(m+1)\). This proves assertion 1, including exact least periods and all boundary exponents.

**2. Recursive structure.** For \(r\ge3\), the equality \(T(r)=t\) holds exactly when \(\lfloor(r-1)/2\rfloor=2^{t-1}(2h+1)\) for some \(h\ge0\), that is, when \(r\) equals one of \(2^t(2h+1)+1\) and \(2^t(2h+1)+2\). Their labels satisfy \(F(r)=F(t)\). Because \(t\) and \(h\) are uniquely determined, and \(F(1)=1,F(2)=2\), this proves the disjoint decomposition in assertion 2.

**3. Quantitative density.** For a fixed \(t\), the two residue classes above occupy exactly two residue classes modulo \(2^{t+1}\). Their contribution to the number of elements of \(A\) in \([1,N]\) is \(N/2^t+O(2)\). Only \(t\le\lfloor\log_2 N\rfloor\) can contribute below \(N\). Their omitted density is bounded by \(\sum_{t>\lfloor\log_2N\rfloor}2^{-t}\), so its contribution after multiplication by \(N\) is at most \(2\). Including the singleton \(\{2\}\), we obtain
\[
\#(A\cap[1,N])=N\sum_{t\in A}2^{-t}+O(\log(N+2)).
\]
The right-hand series converges absolutely to a real \(\alpha\in(0,1)\). Since \(m\in E\) exactly when \(m+1\in A\), shifting by one preserves the density and the logarithmic discrepancy. This proves assertion 3.

**4. Irrationality.** We first prove that the indicator sequence of \(A\) cannot be eventually periodic. Let \(u_0=2\), \(u_{j+1}=2^{u_j}+1\). We have \(T(u_{j+1})=u_j\), so \(F(u_j)=2\) for all \(j\), and \(u_j\to\infty\). In contrast, \(F(2^K+3)=1\) for every integer \(K\ge2\), since \(T(2^K+3)=1\). Hence \(F\) takes both values arbitrarily far out.

Suppose the indicator were eventually periodic with period \(q\ge2\), and put \(h=\lfloor q/2\rfloor\ge1\). For arbitrarily large \(K\), take \(r=2^K+1\). Then \(T(r)=K\), whereas, whenever \(K-1>\nu_2(h)\),
\[
T(r+q)=1+\nu_2(2^{K-1}+h)=1+\nu_2(h).
\]
Thus \(F(r)=F(K)\) can take both values for arbitrarily large \(K\), while \(F(r+q)=F(1+\nu_2(h))\) is fixed, a contradiction. If \(q=1\), take \(r=2^K+2\) with arbitrarily large \(K\in A\). Then \(T(r)=K\) and \(T(r+1)=1\), so \(F(r)=2\ne1=F(r+1)\), again contradicting eventual periodicity.

Consequently \(\mathbf 1_A\) is not eventually periodic. The absolutely convergent sum \(\alpha=\sum_{r\in A}2^{-r}\) is a genuine infinite binary expansion with infinitely many zeros and ones. Since a real number has an eventually periodic binary expansion precisely when it is rational, \(\alpha\) is irrational. This completes the proof.

## Verification

Execute `python3 verifier.py` with the supplied Python 3 program. It independently checks the exact valuation recurrence, by direct cycle detection, against the recursive label for **every** exponent from \(2\) through \(100000\); it also checks the recursive membership law up to \(100000\), and calculates an exact dyadic interval of width \(2^{-120}\) for \(\alpha\). It finds \(29705\) period-two exponents between \(2\) and \(100000\) inclusive. These finite computations check implementation and boundary cases; the proof above, not extrapolation, establishes the infinite claims. The tail bound follows immediately because the omitted terms in \(\alpha\) total less than \(2^{-120}\).

## Relationship to prior work

Emmons and Xiao, *The Arithmetic Partial Derivative* (first arXiv posting January 28, 2022), prove eventual periodicity of all prime-adic valuation trajectories and describe their periods (Theorems 8 and 9). Their theorem provides a natural starting point but does not evaluate the density of exponent classes or establish an irrational invariant. Their later paper *A Generalization of Arithmetic Derivative to \(p\)-adic Fields and Number Fields* (arXiv July 10, 2023) extends the valuation dynamics to local fields (Theorem 2.8). It does not state or prove this exponent-density law. The present contribution is the self-similar arithmetic description, logarithmic counting discrepancy, and irrationality theorem, not the previously known fact that individual valuation sequences become periodic.

## Limitations

The theorem concerns only the dyadic partial derivative and uniform sampling of initial exponents. It makes no statement about all prime-adic derivatives, the arithmetic derivative involving all primes, or natural densities among all positive integer starting values. The irrational constant is specified by a convergent binary series rather than a known closed form in standard constants. Finite calculations do not prove irrationality; that conclusion relies on the nonperiodicity proof. An unindexed earlier derivation remains a publication-priority risk; independent audit has not been performed.

## References

1. Brad Emmons and Xiao Xiao, *The Arithmetic Partial Derivative*, arXiv:2201.12453, submitted January 28, 2022; *Journal of Integer Sequences* 25 (2022), Article 22.6.3. https://arxiv.org/abs/2201.12453 ; https://cs.uwaterloo.ca/journals/JIS/VOL25/Xiao/xiao3.html .
2. Brad Emmons and Xiao Xiao, *A Generalization of Arithmetic Derivative to \(p\)-adic Fields and Number Fields*, arXiv:2307.04912, submitted July 10, 2023. https://arxiv.org/abs/2307.04912 .
