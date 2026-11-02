# A sharp first-collision bound for parallel binary carrying

## Finding

For every finite-support sequence \(c^{(0)}=(c_j^{(0)})_{j\geq0}\) of nonnegative integers with positive weighted value \(N=\sum_{j\geq0}2^j c_j^{(0)}\), use the simultaneous update
\[
c_j^{(t+1)}=(c_j^{(t)}\bmod 2)+\left\lfloor c_{j-1}^{(t)}/2\right\rfloor,
\qquad c_{-1}^{(t)}=0.
\]
Let \(T\) be the least number of rounds needed for every coefficient to belong to \(\{0,1\}\). If \(c^{(0)}\) already is binary, \(T=0\). Otherwise, if
\[
r=\min\{j\geq0:c_j^{(0)}\geq2\},
\]
then the **first-collision bound** is
\[
\boxed{T\leq \lfloor\log_2 N\rfloor-r.}
\]

For positive integers \(a,b\), let \(c^{(0)}\) be the binary pre-carry convolution and write \(L_{\mathrm{par}}(a,b)=T\). Then for all \(a,b\geq1\),
\[
\boxed{L_{\mathrm{par}}(a,b)\leq \max\{0,\lfloor\log_2(ab)\rfloor-1\}
\leq \lfloor\log_2 a\rfloor+\lfloor\log_2 b\rfloor.}
\]
In particular this proves the universal bound posed as Question 9.5.3 by Iizumi (2026). The stronger product-bit bound is attained infinitely often: for every odd integer \(k\geq3\), taking \(a=3\), \(b=(2^k+1)/3\) gives
\[
L_{\mathrm{par}}(a,b)=k-1=\lfloor\log_2(ab)\rfloor-1.
\]

## Assumptions and scope

All coefficients of the initial sequence are **nonnegative integers** and all but finitely many vanish. The update is simultaneous: the carry received at index \(j\) in round \(t+1\) depends on the coefficient at index \(j-1\) at time \(t\), not a partially updated value. We count complete parallel rounds, and regard a sequence already binary as depth zero. In multiplication, coefficients are the ordinary unsigned convolution of the binary digits of two strictly positive integers. No restriction to prime factors or proper factorizations is imposed. Only nonnegative integer arithmetic is involved.

## Proof

**1. Conservation.** For every round, the weighted value is unchanged:
\[
\begin{aligned}
\sum_{j\geq0}2^j c_j^{(t+1)}
&=\sum_{j\geq0}2^j(c_j^{(t)}\bmod2)
 +\sum_{j\geq0}2^{j+1}\lfloor c_j^{(t)}/2\rfloor\\
&=\sum_{j\geq0}2^jc_j^{(t)}=N.
\end{aligned}
\]
All sums are finite because each step increases the support's maximum possible index by at most one.

**2. Finite propagation of nonbinary coefficients.** The identity
\(c_j^{(t+1)}=(c_j^{(t)}\bmod2)+\lfloor c_{j-1}^{(t)}/2\rfloor\)
shows that \(c_j^{(t+1)}\geq2\) implies \(c_{j-1}^{(t)}\geq2\): if the latter is at most one, the incoming term vanishes while the residue is at most one. Since initially no coefficient below \(r\) is nonbinary, induction gives
\[
\{j:c_j^{(t)}\geq2\}\subseteq\{r+t,r+t+1,\ldots\}
\quad\text{for every }t\geq0.
\]
This is a lower bound on the location of any surviving collision, not an assumption that a particular carry follows a unique path.

**3. Bit-length barrier.** Let \(K=\lfloor\log_2 N\rfloor\). Since \(c_r^{(0)}\geq2\), we have \(K\geq r+1\). At time \(t=K-r\), the preceding inclusion would force any nonbinary coefficient to have index \(j\geq K\). Conservation and nonnegativity would then give
\[
N\geq2^jc_j^{(t)}\geq 2^{K+1}>N,
\]
a contradiction. Hence all coefficients are binary by round \(K-r\). This proves the first-collision bound, and also proves termination without relying on an experimental stopping criterion.

**4. Multiplication corollary.** For positive integers \(a,b\), write the binary digits \(a_i,b_j\in\{0,1\}\) and set \(c_h^{(0)}=\sum_{i+j=h}a_ib_j\). Then
\(\sum_h2^hc_h^{(0)}=ab\). Crucially \(c_0^{(0)}=a_0b_0\leq1\), so if a collision occurs, its least index satisfies \(r\geq1\), giving \(T\leq\lfloor\log_2(ab)\rfloor-1\). If no collision occurs, \(T=0\). Thus the first boxed multiplication inequality holds universally. Moreover,
\[
\lfloor\log_2(ab)\rfloor
\leq \lfloor\log_2 a\rfloor+\lfloor\log_2 b\rfloor+1,
\]
so the conjectured bound follows (also trivially in the no-collision case).

**5. Infinite sharpness.** For odd \(k\geq3\), the integer
\(b=(2^k+1)/3\) has binary ones exactly at positions \(0,1,3,5,\ldots,k-2\). As \(3=1+2\), its convolution coefficients with \(3\) are
\[
c_0^{(0)}=1,\quad c_1^{(0)}=2,\quad
c_j^{(0)}=1\ (2\leq j\leq k-1),\quad
c_j^{(0)}=0\ (j\geq k).
\]
At round \(t\) with \(0\leq t\leq k-2\), there is exactly one nonbinary coefficient, a \(2\) at index \(1+t\), and all the later occupied positions through \(k-1\) carry coefficient \(1\). The simultaneous update replaces that \(2\) by zero and adds one to the next position, where the existing \(1\) creates another \(2\), until round \(k-1\), when the last carry enters the previously vacant position \(k\) and the sequence is binary. Therefore \(T=k-1\). Here \(ab=2^k+1\), so \(\lfloor\log_2(ab)\rfloor=k\); the stronger bound is sharp for infinitely many inputs. This family and its depth already appeared in Iizumi's Proposition 1; the contribution here is the new universal upper bound.

## Verification

The standalone standard-library program `VERIFY.py` checks the simultaneous update by two implementations, verifies conservation, and exhaustively checks the first-collision theorem over all nonzero coefficient vectors of lengths one through five with entries in \(\{0,1,2,3\}\), 1,359 sequences. It separately tests all 65,025 ordered pairs \((a,b)\) with \(1\leq a,b\leq255\) and 25 exact sharpness-family examples with odd \(3\leq k\leq51\). The recorded result is `VERIFY_OK general_sequences=1359 multiplier_pairs=65025 sharp_families=25`.

These exhaustive finite computations corroborate, but do not substitute for, the induction and conservation argument for arbitrary inputs.

## Relationship to prior work

Iizumi, *Binary convolution height: Structural invariants of integer factorisations* (published online 11 September 2026), Definition 4 specifies the same parallel update; Lemma 1 proves qualitative termination; Remark 6 describes the bound
\(L_{\mathrm{par}}(a,b)\leq\lfloor\log_2 a\rfloor+\lfloor\log_2 b\rfloor\)
as empirical; Question 9.5.3 explicitly asks whether it can be proved; and Proposition 1 provides the sharpness family used above. The present first-collision invariant yields both a proof of that question and the stronger, universally sharp product-bit estimate.

Izsak and Pippenger, *Carry Propagation in Multiplication by Constants* (2011), analyze a probabilistic carry-chain distribution for random multiplicands with carry-save followed by carry-propagate addition, not this deterministic simultaneous coefficient-normalization depth. Public research-index searches and comparison with accessible related records did not identify a covering theorem; indexing gaps and independently rediscovered elementary bounds remain priority risks.

## Limitations

The first-collision inequality assumes finite nonnegative coefficient vectors; it is not asserted for signed-digit encodings, arbitrary carry radices, or different schedules. The sharp family proves optimality of the uniform product-bit estimate, not uniqueness of extremizers. The remaining separate inequality involving convolution height in Iizumi's Question 9.5.3 is not resolved. The direct publisher-page fetch was unavailable, so the comparison of the primary source used its richly indexed full-article text, including the exact theorem, definitions, remarks, and open-question sections; an earlier implicit proof outside the inspected material cannot be absolutely excluded.

## References

1. Masamichi Iizumi, *Binary convolution height: Structural invariants of integer factorisations*, **Research in Mathematics** (2026), article 2727395, published online 2026-09-11. DOI: 10.1080/27684830.2026.2727395. Definitions 1 and 4, Lemma 1, Proposition 1, Remark 6, Question 9.5.3.
2. Alexander Izsak and Nicholas Pippenger, *Carry Propagation in Multiplication by Constants*, **ACM Transactions on Algorithms** 7 (2011), article 54. DOI: 10.1145/2000807.2000822; arXiv:0801.4040.
