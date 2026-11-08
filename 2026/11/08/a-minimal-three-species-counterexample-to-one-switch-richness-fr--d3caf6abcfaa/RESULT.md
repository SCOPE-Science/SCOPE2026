# A minimal three-species counterexample to one-switch richness–frequency covariance

## Finding
Let \(K\) denote observed richness and \(F_r\) the number of species represented exactly \(r\) times in a sample of 16 independent categorical draws with probabilities \((7/10,1/5,1/10)\). Then
\[
\operatorname{sgn}\operatorname{Cov}(K,F_r)=
\begin{cases}
+1,&1\le r\le5,\\
-1,&r=6,\\
+1,&7\le r\le12,\\
-1,&13\le r\le16.
\end{cases}
\]
Consequently the covariance has **three sign reversals**, whereas two positive-probability species admit only one. This establishes that the one-switch behavior for equal-probability occupancy need not survive unequal sampling weights, already at the smallest possible alphabet size.

## Assumptions and scope
For integers \(m\ge2\), \(n\ge2\), and \(1\le r\le n\), let \(Y_1,\ldots,Y_n\) be independent categorical variables with probability vector \((p_1,\ldots,p_m)\), each \(p_i>0\), \(\sum_i p_i=1\). Let \(N_i=\sum_{t=1}^n\mathbf{1}\{Y_t=i\}\), \(K=\sum_i\mathbf{1}\{N_i>0\}\), and \(F_r=\sum_i\mathbf{1}\{N_i=r\}\). The three-reversal statement specializes to \(m=3\), \(n=16\), and \((p_1,p_2,p_3)=(7/10,1/5,1/10)\). All covariance statements are for fixed-size, not Poissonized, samples.

## Proof
**Exact covariance identity.** Write \(I_i=\mathbf{1}\{N_i>0\}\), \(J_j=\mathbf{1}\{N_j=r\}\). For \(i=j\) and \(r\ge1\),
\[\operatorname{Cov}(I_j,J_j)=\Pr(N_j=r)\Pr(N_j=0).\]
For distinct \(i,j\), inclusion-exclusion gives
\[
\operatorname{Cov}(I_i,J_j)=\Pr(N_i=0)\Pr(N_j=r)-\Pr(N_i=0,N_j=r).
\]
Here \(\Pr(N_j=r)=\binom nr p_j^r(1-p_j)^{n-r}\) and \(\Pr(N_i=0,N_j=r)=\binom nr p_j^r(1-p_i-p_j)^{n-r}\). Summing these equations over all \(i,j\) proves the universal identity
\[\operatorname{Cov}(K,F_r)=\binom nr\sum_{j=1}^{m}p_j^r\left[(1-p_j)^{n-r}\sum_{i=1}^{m}(1-p_i)^n-\sum_{i\ne j}(1-p_i-p_j)^{n-r}\right].\]
For \(m=3\), substituting the stated rational probabilities and \(n=16\) gives the 16 exact signs in the finding. The standalone verifier calculates all entries in rational arithmetic by two independent methods. Five boundary values, displayed without rounding, are
\[
\begin{aligned}
\operatorname{Cov}(K,F_5)&=\frac{491477014571896186404867387}{1562500000000000000000000000000}>0,\\
\operatorname{Cov}(K,F_6)&=-\frac{3969577919885613399780795379}{3125000000000000000000000000000}<0,\\
\operatorname{Cov}(K,F_7)&=\frac{565425373537234919456753577}{312500000000000000000000000000}>0,\\
\operatorname{Cov}(K,F_{12})&=\frac{909901009394535995895709651}{1250000000000000000000000000000}>0,\\
\operatorname{Cov}(K,F_{13})&=-\frac{5488321470389007696069451107}{312500000000000000000000000000}<0.
\end{aligned}
\]
The signs at all remaining indices are checked by exact fractions, with no numerical tolerance.

**Minimal support.** In any strictly positive two-category model, \(K\in\{1,2\}\), and \(\Pr(K=1)=p_1^n+p_2^n\) lies strictly between zero and one. For \(1\le r<n\), \(F_r=0\) whenever \(K=1\), hence \(KF_r=2F_r\) pointwise and
\[\operatorname{Cov}(K,F_r)=\Pr(K=1)\,\mathbb EF_r>0.\]
For \(r=n\), \(F_n=\mathbf{1}\{K=1\}\), hence
\[\operatorname{Cov}(K,F_n)=-\Pr(K=1)\Pr(K=2)<0.\]
Thus no two-category law can have three (or even two) sign reversals. The explicit three-category sample attains three.

## Verification
Run `python3 verify.py`. The verifier independently enumerates all \(\binom{18}{2}=153\) nonnegative count vectors adding to 16, weights each with its multinomial probability as an exact fraction, evaluates \(\mathbb EK\), \(\mathbb EF_r\), and \(\mathbb E[KF_r]\), and compares all 16 covariances with the closed identity. It also checks the complete sign sequence and the five displayed exact boundary fractions. It requires only the Python standard library and no external data.

## Relationship to prior work
Barbour and Gnedin, *Small counts in the infinite occupancy scheme* (arXiv:0809.4387, first public version 25 September 2008), study asymptotic distributions and covariance behavior of occupancy frequency counts with a countably infinite positive frequency sequence; their main asymptotic normal approximation hypotheses do not apply to a fixed three-species alphabet. A publicly accessible note titled *A one-switch covariance law for occupancy richness and frequency counts* establishes the single transition for **uniform** box probabilities, but its homogeneous assumption does not imply the same conclusion for the unequal probabilities above. The present result is a counterexample to extending that one-switch behavior, not a claim to a new formula for the multinomial law itself.

## Limitations
The example does not assert that three is the maximum possible number of reversals for larger alphabets, nor that 16 is the minimum sample size among all three-category probability vectors. The universal identity is elementary; the mathematical contribution is the exact three-reversal pattern and the proof that three species are necessary. Although relevant literature and mathematical finding records were compared, an exhaustive historical-priority determination and independent audit have not been performed.

## References
1. A. D. Barbour and A. V. Gnedin, *Small counts in the infinite occupancy scheme*, arXiv:0809.4387v1 (25 September 2008), https://arxiv.org/abs/0809.4387.
2. *A one-switch covariance law for occupancy richness and frequency counts*, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-one-switch-covariance-law-for-occupancy-richness-and-frequency--93dddb2be813.
