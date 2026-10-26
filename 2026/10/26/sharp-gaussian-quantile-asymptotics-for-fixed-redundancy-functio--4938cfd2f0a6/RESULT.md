# Sharp Gaussian-quantile asymptotics for fixed-redundancy function-correcting codes

## Finding

For every **fixed integer** \(s\geq1\), the universal redundancy-\(s\) threshold for binary nonsystematic two-valued function-correcting codes has the exact first-order law
\[
\lim_{t\to\infty}\frac{\kappa_s(t)}{t^2}
=\frac{4}{[\Phi^{-1}(1-2^{-s-1})]^2}.
\]
Here \(\Phi\) is the standard normal distribution function, and \(\kappa_s(t)\) is defined below. The limit is for fixed \(s\), not a claim uniform in \(s\). In particular, the one-redundant-bit threshold is asymptotic to \(8.79243735327093\ldots\,t^2\). The next constants, for \(s=2,3,4\), are \(3.02273772020389\ldots\), \(1.69957768221241\ldots\), and \(1.15281416018288\ldots\). Balanced two-valued functions already give the sharp asymptotic obstruction at every fixed redundancy.

## Assumptions and scope

Take integers \(t\geq1\) and \(1\leq s\leq 2t\). For each \(k\geq1\), a binary \((f,t)\)-function-correcting encoding of length \(n=k+s\) is an **injective** map \(E:\{0,1\}^k\to\{0,1\}^{n}\) such that \(d_H(E(u),E(v))\geq2t+1\) whenever \(f(u)\neq f(v)\). Here \(f:\{0,1\}^k\to\{0,1\}\) is any nonconstant Boolean function, and no systematicity or linearity condition is imposed. The threshold \(\kappa_s(t)\) is the least positive integer \(K\) such that for every \(k\geq K\) and every such \(f\), such an encoding exists at length \(k+s\).

Write \(B_j\) for the Hamming ball of radius \(j\) centered at zero in \(\{0,1\}^n\), and let \(V(n,j)=\sum_{i=0}^{j}\binom ni\), with \(V(n,j)=0\) for \(j<0\) and \(V(n,j)=2^n\) for \(j\geq n\). Let \(I_M\) be a simplicial-order initial segment of size \(M\); its radius-\(r\) neighborhood is \(N_r(I_M)\). Fix \(s\) and abbreviate \(p_s=2^{-s-1}\), \(z_s=\Phi^{-1}(1-p_s)>0\), and \(c_s=4/z_s^2\).

## Proof

**1. Exact finite feasibility criterion (prior result).** By the vertex-isoperimetric theorem of Harper and the two-class criterion of Rajput--Jagatti--Rajan (2026, Theorem 3), an encoding exists for a function whose smaller class contains \(M\) messages precisely when
\[
|N_{2t}(I_M)|-M\leq 2^n-2^k=2^n(1-2^{-s}),\qquad 1\leq M\leq2^{k-1}.
\tag{1}
\]
The same criterion applies to all nonconstant functions; only the size \(M\) matters. We use (1) without claiming it as new.

**2. Lower bound from balanced classes.** Choose a balanced Boolean function, so \(M=2^{k-1}=p_s2^n\), and let \(j\) be the smallest integer satisfying \(V(n,j)\geq M\). Then \(B_{j-1}\subseteq I_M\), hence \(B_{j-1+2t}\subseteq N_{2t}(I_M)\). Write \(X_n\sim\operatorname{Bin}(n,1/2)\). For any fixed \(0<c<c_s\), choose \(n=\lfloor ct^2\rfloor\) and \(k=n-s\). The binomial central limit theorem and the vanishing maximum atom imply the quantile convergence
\[
\frac{j-1-n/2}{\sqrt n/2}\longrightarrow \Phi^{-1}(p_s)=-z_s.
\]
Therefore
\[
2^{-n}|B_{j-1+2t}|\longrightarrow
\Phi\left(-z_s+\frac4{\sqrt c}\right)
>\Phi(z_s)=1-p_s.
\]
The right side of (1), after rearrangement to a bound on \(|N_{2t}(I_M)|\), is \(2^n-2^k+M=2^n(1-p_s)\). Thus (1) fails for these balanced functions for all sufficiently large \(t\). For every \(c<c_s\), this produces a failing length with \(k=ct^2+o(t^2)\), whence \(\liminf_{t\to\infty}\kappa_s(t)/t^2\geq c_s\).

**3. Uniform upper bound for every class size.** Fix \(\varepsilon>0\). Let \(n=k+s\geq(c_s+\varepsilon)t^2\), and let \(M\) range over **every** integer from \(1\) to \(2^{k-1}\). Define \(j\) minimally by \(V(n,j)\geq M\). Since \(B_{j-1}\subset I_M\subseteq B_j\),
\[
|N_{2t}(I_M)|-M
<\sum_{i=j}^{j+2t}\binom ni.
\tag{2}
\]
Terms outside the interval from \(0\) to \(n\) are zero. Standardize \(X_n\) with mean \(n/2\) and standard deviation \(\sigma_n=\sqrt n/2\), and put \(x=(j-1-n/2)/\sigma_n\) and \(a=(2t+1)/\sigma_n\). Since \(V(n,j-1)<M\leq p_s2^n\), the uniform Berry--Esseen estimate gives
\[
x\leq -z_s+O_s(n^{-1/2}).
\]
The normalized sum in (2) differs from \(\Phi(x+a)-\Phi(x)\) by at most \(O(n^{-1/2})\), uniformly in \(j\). Moreover, uniformly for all the allowed \(n\),
\[
a\leq \frac4{\sqrt{c_s+\varepsilon}}+O(t^{-1})<2z_s
\]
for sufficiently large \(t\). For \(0<a<2z_s\), the map \(x\mapsto\Phi(x+a)-\Phi(x)\) increases for \(x<-a/2\), so its maximum on \(x\leq-z_s+o(1)\) is attained at the right endpoint up to \(o(1)\). Consequently the normalized right side of (2) is at most
\[
\Phi\left(-z_s+\frac4{\sqrt{c_s+\varepsilon}}\right)-\Phi(-z_s)+o(1)
<\Phi(z_s)-\Phi(-z_s)=1-2^{-s}.
\]
The strict gap is independent of \(k\) and \(M\); the error bound is uniform over \(n\geq(c_s+\varepsilon)t^2\). Thus (1) holds for all \(M\) and all \(k\) in this range once \(t\) is large. Hence \(\limsup_{t\to\infty}\kappa_s(t)/t^2\leq c_s\). Combining with Step 2 proves the claimed limit for each fixed \(s\).

## Verification

The included `verify_threshold.py` checks the elementary neighborhood enclosures by direct enumeration on short binary cubes, and uses exact integer binomial coefficients to produce both failure certificates (balanced-class ball lower bounds) and universal success certificates (all-class interval upper bounds). For each \(s\in\{1,2,3,4\}\) and \(t\in\{5,10,20\}\), certificates work at lengths equal to approximately \(0.75c_st^2\) and \(1.25c_st^2\), respectively. `verification_output.txt` records the actual execution. These finite computations are corroboration, not a proof of the \(t\to\infty\) limit; the proof uses isoperimetry and the uniform binomial normal approximation.

## Relationship to prior work

Rajput, Jagatti and Rajan (arXiv:2610.09011, publicly posted 2026-10-06) give the exact finite neighborhood criterion (their Theorem 3) and bounds \(\kappa_s(t)\leq\lceil2(2t+1)^2/[3(1-2^{-s})^2]\rceil-s\). They explicitly leave the growth order of \(\kappa_1(t)\) and lower bounds for \(s\geq2\) open. This finding **uses** their finite criterion and determines a previously unreported exact quadratic asymptotic constant for every fixed \(s\). Harper's classical vertex-isoperimetric theorem, treated in Räty's work, is credited as a prerequisite rather than a new result. Earlier work on linear/systematic function-correcting codes concerns a different encoding class.

## Limitations

The result applies only to binary Hamming-metric codes, two-valued functions, arbitrary injective nonsystematic encoders, and fixed redundancy \(s\) as \(t\to\infty\). It gives a first-order asymptotic, not exact finite thresholds, a bounded second-order error, or a uniform theorem for \(s\) growing with \(t\). It does not protect the full message against errors. Novelty is assessed against the inspected accessible literature, not independently certified; an older equivalent Gaussian-isoperimetric formulation may exist.

## References

1. C. Rajput, K. L. Jagatti, B. S. Rajan, *On Optimal Encodings and Systematicity in Function-Correcting Codes*, arXiv:2610.09011v1 (first public posting 2026-10-06), https://arxiv.org/abs/2610.09011 .
2. E. Räty, *Uniqueness in Harper's vertex-isoperimetric theorem*, arXiv:1806.11061, Discrete Mathematics 343 (2020), 111696, https://arxiv.org/abs/1806.11061 .
3. L. H. Harper, *Optimal numberings and isoperimetric problems on graphs*, Journal of Combinatorial Theory 1 (1966), 385--393.
4. Classical de Moivre--Laplace central limit theorem and uniform Berry--Esseen normal approximation for binomial sums.
