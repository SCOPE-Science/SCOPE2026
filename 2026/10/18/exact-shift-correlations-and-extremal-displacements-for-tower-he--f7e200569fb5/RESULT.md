# Exact shift correlations and extremal displacements for tower-height levels

## Finding

Let \(h(1)=0\), and, for \(n>1\) with canonical factorization \(n=\prod_{p^a\parallel n}p^a\), let
\[
h(n)=1+\max_{p^a\parallel n}h(a).
\]
For each fixed integer \(k\ge 2\), define \(\mathcal C_k=\{n\ge1:h(n)\le k\}\), \(\mathcal A_k=\{a\ge1:h(a)\ge k\}\), and \(T_1=2\), \(T_{j+1}=2^{T_j}\). For every nonzero integer displacement \(t\), the joint natural density
\[
Q_k(t)=\lim_{X\to\infty}\frac1X\#\{1\le n\le X:n,n+t\in\mathcal C_k\}
\]
exists (ignore the finitely many \(n\) for which \(n+t\le0\)). Define, for each prime \(p\) and \(a\ge1\),
\[
w_p(a)=(p-1)p^{-a-1},\qquad
\beta_{p,k}=\sum_{a\in\mathcal A_k}w_p(a),
\]
and, for each nonnegative integer \(r\),
\[
\gamma_{p,k}(r)=\sum_{\substack{a\in\mathcal A_k\\a<r}}w_p(a)
+\mathbf1_{r\in\mathcal A_k}\left(\frac{p-2}{p-1}w_p(r)+2\sum_{\substack{a\in\mathcal A_k\\a>r}}w_p(a)\right).
\]
Then
\[
\boxed{Q_k(t)=\prod_p\bigl(1-2\beta_{p,k}+\gamma_{p,k}(v_p(|t|))\bigr).}
\]
Writing \(c_k=\prod_p(1-\beta_{p,k})\), the exact lower and upper extremal laws are
\[
\boxed{Q_k(1)\le Q_k(t)<c_k,\quad
Q_k(t)=Q_k(1)\iff |t|\text{ is }T_k\text{-free},\quad
\sup_{t\ne0}Q_k(t)=c_k.}
\]
Here \(T_k\)-free means that \(p^{T_k}\nmid |t|\) for every prime \(p\). The supremum is not attained; rather \(Q_k(j!)\to c_k\) as \(j\to\infty\). In particular, minimizing positive displacements have natural density \(1/\zeta(T_k)\).

The height-level indicators have both signs of shifted covariance: \(Q_k(1)<c_k^2\), whereas \(Q_k(j!)>c_k^2\) for all sufficiently large \(j\).

## Assumptions and scope

The level \(k\ge2\) and displacement \(t\ne0\) are fixed before \(X\to\infty\). All prime products and sums are ordinary convergent real series; \(v_p(t)\) is the usual prime-adic valuation of a nonzero integer. The theorem concerns joint natural densities of integers, not independence of prime valuations at finite \(X\), and does not assert a uniform error term in either \(k\) or \(t\). The previously known squarefree case \(k=1\) is included only in the verifier as a boundary check, not in the new classification's originality claim.

## Proof

**1. Minimal prohibited exponent.** For \(k\ge1\), the least positive integer of height at least \(k\) equals \(T_k\). This is induction: it is \(2\) at level one; to have height at least \(k+1\), some prime-power exponent \(a\) must have height at least \(k\), so the integer is at least \(2^{T_k}=T_{k+1}\). This bound is attained by \(2^{T_k}\). Thus \(\min\mathcal A_k=T_k\ge4\) for \(k\ge2\), and \(\mathcal A_k\) is unbounded: for \(k\ge2\), all odd multiples of \(T_k\) have height at least \(k\), because their exponent of \(2\) is \(T_{k-1}\).

**2. One-prime valuation geometry.** Fix a prime \(p\) and \(r=v_p(t)\). In the uniform \(p\)-adic residue model, \(\Pr(v_p(n)=a)=w_p(a)\) for \(a\ge1\). If \(a<r\), then \(v_p(n+t)=a\); if \(a>r\), then \(v_p(n+t)=r\). Conditional on \(v_p(n)=r\), one has \(v_p(n+t)=r\) with probability \((p-2)/(p-1)\). For each \(b>r\), the joint event \(v_p(n)=r,\ v_p(n+t)=b\) has probability \(w_p(b)\), as does its transpose. These disjoint cases give exactly \(\gamma_{p,k}(r)\), the probability that both prime exponents belong to \(\mathcal A_k\). The probability that neither exponent is forbidden is therefore \(1-2\beta_{p,k}+\gamma_{p,k}(r)\).

**3. Natural-density limit.** At any finite set of primes, truncating valuations to a fixed power gives periodic residue conditions, whose natural density equals the product of the local good probabilities by the Chinese remainder theorem. Truncation at exponent \(L\) changes each local probability by at most \(2p^{-L}\). Let \(m=T_k\). An integer of height exceeding \(k\) has some exponent in \(\mathcal A_k\), hence is divisible by \(p^m\) for a prime \(p\). For primes \(p>Y\), the upper natural density of the union of the events \(p^m\mid n\) or \(p^m\mid n+t\) is at most \(2\sum_{p>Y}p^{-m}\): for \(n\le X\), count multiples by \(X/p^m+O(1)\), and the total \(O(1)\) terms over \(p\le (X+|t|)^{1/m}\) are \(O((X+|t|)^{1/m})=o(X)\). The prime tail tends to zero because \(m\ge4\). Passing first through finite residue conditions and then \(Y\to\infty\) proves the product formula and its convergence. Positivity follows because \(\beta_{p,k}\le p^{-m}\), whence every local factor is at least \(1-2p^{-m}>0\) and the deviations are summable.

**4. Sharp displacement classification.** Every \(\gamma_{p,k}(r)\ge0\), and it vanishes precisely for \(r<m\). Indeed, for \(r<m\), all three sums are empty. For \(r\ge m\) outside \(\mathcal A_k\), its first sum contains \(w_p(m)>0\); for \(r\in\mathcal A_k\), its strictly positive tail \(2\sum_{a\in\mathcal A_k,a>r}w_p(a)\) is present, using unboundedness. Hence the prime-factor product is minimized exactly when \(v_p(t)<m\) for every prime, and equals \(Q_k(1)=\prod_p(1-2\beta_{p,k})\). The minimizer set is exactly the set of \(m\)-free positive integers, whose density is \(\prod_p(1-p^{-m})=1/\zeta(m)\), by the same CRT and tail argument.

Since the local simultaneous-good event is contained in the single-good event, \(1-2\beta_{p,k}+\gamma_{p,k}(r)\le1-\beta_{p,k}\). For each finite nonzero \(t\), choose any prime \(p\nmid t\): its local factor equals \(1-2\beta_{p,k}<1-\beta_{p,k}\). Since the infinite products are positive, \(Q_k(t)<c_k\). On the other hand, \(v_p(j!)\to\infty\) for each fixed prime, and \(\gamma_{p,k}(r)\to\beta_{p,k}\) as \(r\to\infty\). The summable bound by \(2\beta_{p,k}\) permits passage through the products, proving \(Q_k(j!)\to c_k\).

**5. Covariance sign change.** For each prime, \(1-2\beta_{p,k}<(1-\beta_{p,k})^2\), because \(\beta_{p,k}>0\); therefore \(Q_k(1)<c_k^2\). Finally \(0<c_k<1\), so \(\lim_{j\to\infty}Q_k(j!)=c_k>c_k^2\). Thus factorial displacements eventually have positive covariance, completing the proof.

## Verification

Running `python3 verify.py` with Python 3 and no external dependencies performs exact modular-enumeration comparisons for 24 one-prime cases, 14 full-range empirical correlations for the first two height levels, and three checks of minimal prohibited exponents. On the checked package, it prints `MINIMUM_FORBIDDEN_EXPONENT_CHECKS=3`, `LOCAL_EXACT_CHECKS=24`, `FINITE_PAIR_COMPARISONS=14`, and `VERIFY_OK`. Finite numerical agreement verifies the implementation on the tested ranges, but the proof above is the evidence for all levels and all integer shifts.

## Relationship to prior work

De Koninck and Verreault establish the tower-height recursion and one-point densities \(c_k\), together with the existence of arbitrarily long high-height runs. Devlin and Gnang study the presence of fixed primes within tower factorizations. Srichan, Rungtanapirom, and Wananiyakul prove a general consecutive \(M\)-free two-point density for \(n,n+1\), which already determines \(Q_k(1)\) by taking \(M=\mathcal A_k\); that special case is **not** claimed as new here. Their theorem does not state an arbitrary-displacement formula or identify all minimizing shifts, the unattained supremum, and both covariance signs. The older Mirsky shift formula for ordinary \(m\)-free integers pertains to the forbidden exponent set \(\{m,m+1,\ldots\}\). At \(k\ge2\), the present forbidden set \(\mathcal A_k\) has genuine gaps, so it is not that case. The contribution is the complete displacement-dependent local correlation law and its sharp extremal classification.

## Limitations

The result does not estimate convergence rates for arbitrary shifts, optimize finite-range error terms, or determine the sign of covariance for every individual displacement. Literature comparisons are limited to the inspected papers, their pertinent statements and proofs, and targeted searches; unindexed equivalent work may exist. The original 2026 consecutive \(M\)-free result already covers the displacement-one formula, and the squarefree height-one specialization follows classical work. No independent mathematical audit has been performed.

## References

1. J.-M. De Koninck and W. Verreault, *On the tower factorization of integers*, arXiv:2308.09149v1 (first public 2023-08-17); *American Mathematical Monthly* 131 (2024), 511–518, DOI: 10.1080/00029890.2024.2322912.
2. P. Devlin and E. K. Gnang, *Primes Appearing in the Tower Factorization of Integers*, arXiv:1204.5251 (2012; revised 2014).
3. T. Srichan, N. Rungtanapirom, and S. Wananiyakul, *On the distribution of consecutive M-free integers*, RAIRO-Theoretical Informatics and Applications 60 (2026), article 22, DOI: 10.1051/ita/2026022.
4. L. Mirsky, *On the frequency of pairs of square-free numbers with a given difference*, Bulletin of the American Mathematical Society 55 (1949), 936–939.
