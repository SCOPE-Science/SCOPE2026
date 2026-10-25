# Centralizer profiles and a quadratic limit law for idempotent finite-chain contractions

## Finding
Let \([n]=\{1,\ldots,n\}\). Denote by \(\mathcal C_n\) the transformation monoid of all nondecreasing \(1\)-Lipschitz maps \([n]\to[n]\), with composition. For an idempotent \(e\) let \(\operatorname{Cent}_{\mathcal C_n}(e)=\{f\in\mathcal C_n:fe=ef\}\).

For integers \(n\geq1\) and \(1\leq a\leq b\leq n\) set
\[
e_{a,b}(i)=\min(b,\max(a,i)),\qquad u=a-1,\quad k=b-a,\quad v=n-b.
\]
Every idempotent is uniquely of this form, so the parameters range over all nonnegative triples satisfying \(u+k+v=n-1\). Their centralizer cardinalities are
\[
\boxed{\lvert\operatorname{Cent}_{\mathcal C_n}(e_{a,b})\rvert =
\begin{cases}
2^{n-1},&k=0,\\[2pt]
(k+2)2^{k-1}+(2^u+2^v-2)2^k+(2^u-1)(2^v-1),&k\geq1.
\end{cases}}
\]
In particular, the exact polynomial \(H_n(T)=\sum_{u+k+v=n-1}T^{C_n(u,k,v)}\) encodes the complete centralizer-size multiset among idempotents. For fixed \(k\geq1\), a balanced placement \(\lvert u-v\rvert\leq1\) minimizes this cardinality, and an end-anchored placement \(uv=0\) maximizes it. The minimizer is unique when \(n-k-1\) is even and consists of two reflected placements otherwise; the maximizers are the two ends unless they coincide.

If an idempotent \(E_n\) is drawn uniformly from the \(n(n+1)/2\) idempotents and
\[W_n=\frac1n\log_2\lvert\operatorname{Cent}_{\mathcal C_n}(E_n)\rvert,\]
then \(W_n\Rightarrow W\), with cumulative distribution function
\[
F_W(t)=\begin{cases}
0,&t<2/3,\\
(3t-2)^2,&2/3\leq t\leq1,\\
1,&t>1.
\end{cases}
\]
Furthermore \(\mathbb E[W_n]\to8/9\). This is a nondegenerate limit law on a natural intrinsic semigroup invariant, not a statement about uniformly sampling arbitrary monoid elements.

## Assumptions and scope
All maps here are *full*, weakly order-preserving, and contractions for the usual distance on the discrete chain. Equivalently, each adjacent increment \(f(i+1)-f(i)\) belongs to \(\{0,1\}\). The centralizer is computed **inside** \(\mathcal C_n\), not inside the full transformation monoid. Every assertion holds for every positive integer \(n\). The singleton-chain and constant-idempotent boundaries are included.

## Proof
**1. Idempotent classification.** The image of a nondecreasing \(1\)-Lipschitz map is an interval \([a,b]\cap\mathbb Z\), because adjacent values change by zero or one. A transformation is idempotent precisely when it fixes its image pointwise. Thus \(f(i)=i\) for \(a\leq i\leq b\). For \(i<a\), monotonicity gives \(f(i)\leq a\), whereas the Lipschitz inequality from \(a\) gives \(f(i)\geq a-(a-i)=i\). Because the image is contained in \([a,b]\), \(f(i)=a\); similarly \(f(i)=b\) for \(i>b\). Hence \(f=e_{a,b}\). Conversely every clamp is an idempotent. There are exactly \(\sum_{a=1}^n(n-a+1)=n(n+1)/2\) of them.

**2. Necessary and sufficient commutation constraints.** Write \(e=e_{a,b}\), and let \(f\in\mathcal C_n\). For each interior \(a\leq i\leq b\), the relation \(ef(i)=fe(i)=f(i)\) forces \(f(i)\in[a,b]\). Denote \(x=f(a)\), \(y=f(b)\), where \(a\leq x\leq y\leq b\). For \(i<a\), the equality \(e(f(i))=f(a)=x\) forces every value \(f(i)\) to equal \(x\) when \(x>a\). If \(x=a\), it instead places no restriction beyond the original adjacent-step condition, and there are exactly \(2^{a-1}=2^u\) left-hand binary-step words, all valid because their final value is \(a\). Symmetrically, the right-hand word has \(2^v\) possibilities when \(y=b\) and one when \(y<b\). Together with the interior condition, these are both necessary and sufficient for \(ef=fe\).

**3. Exact enumeration.** Fix \(x,y\) as above. On the \(k=b-a\) interior edges, exactly \(y-x\) increments must equal one. Thus there are \(\binom{k}{y-x}\) internal walks. Put \(L_x=2^u\) if \(x=a\) and \(L_x=1\) otherwise, and \(R_y=2^v\) if \(y=b\) and \(R_y=1\) otherwise. It follows that
\[
C_n(u,k,v)=\sum_{a\leq x\leq y\leq b}\binom{k}{y-x}L_xR_y.
\]
For \(k=0\), the endpoints coincide, so this sum is \(2^u2^v=2^{n-1}\). For \(k\geq1\), first set both endpoint weights to one. This contributes
\[
\sum_{j=0}^{k}(k+1-j)\binom{k}{j}
=(k+2)2^{k-1}.
\]
The correction at \(x=a\) is \((2^u-1)\sum_{y=a}^b\binom{k}{y-a}=(2^u-1)2^k\). The correction at \(y=b\) similarly contributes \((2^v-1)2^k\), and the simultaneous correction at \((x,y)=(a,b)\) contributes \((2^u-1)(2^v-1)\binom{k}{k}\). This proves the stated cardinality.

For \(k\geq1\), the same formula is equivalently
\[
C_n(u,k,v)=2^{u+v}+(2^k-1)(2^u+2^v)+(k-2)2^{k-1}+1.
\]
At fixed \(k\) and fixed \(u+v=n-k-1\), only the factor \(2^u+2^v\) varies. Its discrete strict convexity proves the balanced minima and end-anchored maxima, including the symmetry and boundary cases described above.

**4. A uniform logarithmic approximation.** Write
\[
M_n(u,k,v)=\max\{u+v,k+u,k+v\}=n-1-\min\{u,k,v\}.
\]
For \(k=0\), \(C_n=2^{M_n}\) exactly. For \(k\geq1\), the positive summands in the original enumeration give
\[
2^{M_n-1}\leq C_n(u,k,v)\leq 4(n+1)2^{M_n}.
\]
Indeed the \((u,v)\)-joint term, two endpoint-weight terms and the baseline each have exponential order at most \(2^{M_n}\), with at most a linear factor \(k+2\); for the lower bound, the joint term contributes \(2^{u+v}\), and endpoint corrections together with the baseline give at least half of \(2^{k+u}\) and \(2^{k+v}\). Consequently, uniformly in all idempotents,
\[
\bigl|\log_2 C_n(u,k,v)-M_n(u,k,v)\bigr|\leq2+\log_2(4(n+1))=O(\log n).
\]

**5. Exact minimum-gap law and limit.** Under uniform choice of idempotent, \((u,k,v)\) is uniform over the \(\binom{n+1}{2}\) nonnegative compositions of \(n-1\). For every integer \(m\) with \(0\leq3m\leq n-1\), shifting all three coordinates down by \(m\) gives exactly \(\binom{n+1-3m}{2}\) compositions. Therefore
\[
\Pr(\min(u,k,v)\geq m)=\frac{\binom{n+1-3m}{2}}{\binom{n+1}{2}}.
\]
It follows that \(\min(u,k,v)/n\Rightarrow Z\), with \(\Pr(Z\geq t)=(1-3t)^2\) for \(0\leq t\leq1/3\), and \(Z\in[0,1/3]\). Since \(M_n/n=(n-1)/n-\min(u,k,v)/n\), the uniform logarithmic estimate yields \(W_n\Rightarrow 1-Z\), whose CDF is the stated piecewise quadratic expression. Finally \(0\leq W_n\leq1+O(\log n/n)\) uniformly, so convergence of expectations holds, with
\[
\mathbb E(1-Z)=1-\int_0^{1/3}(1-3t)^2\,dt=\frac89.
\]
This proves all claims.

## Verification
The standalone script `check_clamp_centralizers.py` enumerates every weakly increasing binary-increment map for \(1\leq n\leq10\), tests idempotence directly, tests commutation by composition at each chain point, and compares every centralizer size with the displayed formula. It checks all \(220\) idempotents in these sizes and \(243714\) map-idempotent commuting comparisons. It additionally checks the exact minimum-gap counts and a logarithmic comparison bound for \(2\leq n\leq100\). Invoke `python3 check_clamp_centralizers.py` in a directory containing that file. The script reports `ALL_CLAMP_CENTRALIZER_TESTS_PASSED`. These finite checks corroborate the proof but cannot establish its infinite-\(n\) conclusions.

## Relationship to prior work
The 2022 preprint by Zubairu, Umar and Aliyu studies cardinalities and generation ranks of regular and idempotent contraction subsemigroups, including the classical count of interval-clamp idempotents (arXiv:2205.00438v1). Umar and Zubairu's 2021 paper proves structural properties, Green relations and abundance for full contraction monoids (DOI 10.12958/adm1816). Adeshola and Umar give counts by transformation equivalence classes and total orders (arXiv:1303.7428). Zubairu and Lawan determine sizes of monoids fixing a prescribed set (DOI 10.4236/ojdm.2025.153004). These are related but differ in the commutation constraint: \(fe=ef\) does not mean that \(f\) fixes the interior interval pointwise. The claimed new invariants are the exact centralizer-size profile of *every idempotent in the full contraction monoid* and its nondegenerate random-idempotent logarithmic limit distribution. No claim is made that idempotent classification or overall monoid cardinality is new.

## Limitations
The result concerns centralizers of idempotents inside the order-preserving **full** contraction monoid; it does not count centralizers of nonidempotents, or commuting pairs over the entire monoid. The limiting distribution samples idempotents uniformly, rather than general elements uniformly. The literature comparison does not establish historical uniqueness: an equivalent count could exist in older transformation-semigroup work or as a non-explicit consequence of a more general centralizer theorem. No independent mathematical audit has been conducted.

## References
- M. M. Zubairu, A. Umar, and M. J. Aliyu, *On the combinatorial and rank properties of certain subsemigroups of full contractions of a finite chain*, arXiv:2205.00438v1, publicly posted 2022-05-01.
- A. Umar and M. M. Zubairu, *On certain semigroups of contraction mappings of a finite chain*, Algebra and Discrete Mathematics 32 (2021), 299–320, DOI:10.12958/adm1816.
- A. D. Adeshola and A. Umar, *Combinatorial results for certain semigroups of order-preserving full contraction mappings of a finite chain*, arXiv:1303.7428.
- M. M. Zubairu and Z. D. Lawan, *On the monoid of all order preserving full contractions with a fixed set*, Open Journal of Discrete Mathematics 15 (2025), 55–71, DOI:10.4236/ojdm.2025.153004.
