# Sharp second minima of prime-power nonzero counts on Pascal-row blocks

## Finding

For any prime \(p\), integer \(\alpha\ge2\), and integer \(h\ge1\), put \(N=p^h\) and
\[
A_{p,\alpha}(n)=\#\bigl\{0\le k\le n:\ p^\alpha\nmid\binom nk\bigr\}.
\]
Over the complete block \(N\le n<pN\), the **unique** minimum of \(A_{p,\alpha}(n)\) occurs at \(n=N\), with value \(p^{\min(h,\alpha-1)}+1\). The second distinct minimum \(M_{p,\alpha,h}\), and its **entire equality set** \(E_{p,\alpha,h}\), are as follows:

| Conditions | \(M_{p,\alpha,h}\) | \(E_{p,\alpha,h}\) |
|---|---|---|
| \(h<\alpha\) | \(N+2\) | \(\{N+1\}\) |
| \(h=\alpha=2,\ p=2\) | \(6\) | \(\{N+1,N+2\}\) |
| \(h=\alpha\ge3,\ p=2\) | \(3\cdot2^{\alpha-2}+3\) | \(\{N+2\}\) |
| \(h=\alpha=2,\ p\ge3\) | \(2p+1\) | \(\{2N\}\) |
| \(h=\alpha=3,\ p\ge3\) | \(2p^2+1\) | \(\{N+p,2N\}\) |
| \(h=\alpha\ge4,\ p\ge3\) | \((2p-1)p^{\alpha-2}+p+1\) | \(\{N+p\}\) |
| \(h>\alpha=2,\ p=2\) | \(6\) | \(\{N+1,N+2^{h-1}\}\) |
| \(h>\alpha\ge3,\ p=2\) | \(2^\alpha+2\) | \(\{N+1\}\) |
| \(h>\alpha,\ p\ge3\) | \(2p^{\alpha-1}+1\) | \(\{2N\}\) |

In all cases, the second minimum is strictly larger than the first and the displayed equality set is complete. The boundary \(h=\alpha\) is a phase transition in which a low digit and the leading digit can give the same sharp value.

## Assumptions and scope

All counts are of **integer binomial coefficients nonzero modulo the prime power** \(p^\alpha\), not of their distinct residue values. There are exactly \((p-1)p^h\) row indices in the block. The theorem covers all primes and all integers \(\alpha\ge2\), \(h\ge1\); no unproved distributional assumption is used. It does not concern simultaneous minima over all row lengths, nor the frequency of a given count outside the indicated block.

## Proof

**1. Digital monotonicity and reduction to elementary perturbations.** Kummer's theorem identifies \(\nu_p\binom nk\) with the number of borrows in subtracting \(k\) from \(n\) in base \(p\). If the base-\(p\) digits of \(m\) are coordinatewise at least those of \(n\) (using equal padded length), then for each \(0\le k\le n\), the borrow count for \(m-k\) does not exceed that for \(n-k\). This follows by induction over digit positions from the rule \(b_{i+1}=\mathbf1_{k_i+b_i>n_i}\). Thus every \(k\) counted at \(n\) is counted at \(m\); since \(m>n\), \(k=m\) is a further counted endpoint, and \(A_{p,\alpha}(m)>A_{p,\alpha}(n)\). Every row in the block digitwise dominates \(N=p^h\), yielding the unique minimum at \(N\). Every other row digitwise dominates one of \(N+p^j\), \(0\le j<h\), or, for \(p\ge3\), \(2N\). Since strict dominance strictly increases the count, any second-minimum row must be **one of these elementary rows**.

**2. Exact borrow polynomials.** Define \(B_n(z)=\sum_{k=0}^n z^{\nu_p\binom nk}\) and \(U_r(z)=\sum_{e=1}^{r}(p-1)p^{e-1}z^e\), with \(U_0(z)=0\). The digit-by-digit subtraction rule has transition matrix
\[
T_d(z)=\begin{pmatrix}d+1&(p-1-d)z\\ d&(p-d)z\end{pmatrix},\quad 0\le d<p,
\]
where rows index the incoming borrow and columns the outgoing borrow; multiply the row vector \((1,0)\) by the matrices for the digits of \(n\), from least to most significant, and take its first component. Direct multiplication for the elementary digit patterns gives
\[
\begin{aligned}
 B_N(z)&=2+U_h(z),\\
 B_{2N}(z)&=3+2U_h(z)\quad(p\ge3),\\
 B_{N+1}(z)&=4+2U_{h-1}(z)+(p-2)p^{h-1}z^h.
\end{aligned}
\]
For \(1\le j<h\), write \(L=h-j-1\), \(U=U_j(z)\) and \(V=U_L(z)\). Then
\[
B_{N+p^j}(z)=4+2U+2V+UV+(p-2)p^Lz^{L+1}+(p-1)p^Lz^{L+1}U.
\]
Every displayed expression follows from the single digit transition, so no large-row enumeration is implicit. The required count is the sum of coefficients of \(z^0,\ldots,z^{\alpha-1}\). In particular, the minimum at \(N\) equals \(2+\sum_{e=1}^{\min(h,\alpha-1)}(p-1)p^{e-1}=p^{\min(h,\alpha-1)}+1\).

**3. The range \(h<\alpha\).** Any row in the block has at most \(h\) subtraction borrows, so all its binomial coefficients are nonzero modulo \(p^\alpha\). Thus \(A_{p,\alpha}(n)=n+1\) and the next row \(N+1\) uniquely attains the second value \(N+2\).

**4. The boundary \(h=\alpha\).** The formulas above give
\[
\begin{aligned}
 A_{p,\alpha}(N+1)&=2p^{\alpha-1}+2,\\
 A_{p,\alpha}(2N)&=2p^{\alpha-1}+1\quad(p\ge3),\\
 A_{p,\alpha}(N+p^j)&=(2p-1)p^{\alpha-2}+p^j+1\quad(1\le j<\alpha).
\end{aligned}
\]
For the last identity, the only omitted \(z^\alpha\) contribution to the full coefficient sum \(p^\alpha+p^j+1\) is \((p-1)^2p^{\alpha-2}\). The final expression is strictly increasing in \(j\), so its smallest case is \(j=1\). Comparing the three displayed candidates (omitting \(2N\) when \(p=2\)) gives precisely the five boundary cases in the table, including both ties.

**5. The range \(h>\alpha\).** Put \(s=\alpha-1\), so \(h\ge s+2\). The low-digit candidate and, when available, the leading candidate are
\[
A_{p,\alpha}(N+1)=2p^s+2,\qquad A_{p,\alpha}(2N)=2p^s+1\quad(p\ge3).
\]
For each \(j\ge1\), put \(L=h-j-1\). Truncating the formula in step 2 shows that \(A_{p,\alpha}(N+p^j)>2p^s+2\), except for the equality case \(p=2,s=1,L=0\). For completeness, the strict comparison splits into three exhaustive ranges. If \(L\ge s\), the term \(2V\) alone contributes the entire baseline \(2(p^s-1)\), and \(2U\) gives a positive additional contribution. If \(j\ge s\) and \(L<s\), the \(2U\) term supplies the baseline and the term \(2V\), or when \(L=0\) the remaining positive transition terms, supplies a strict excess; at \(p=2,s=1,L=0\) the excess vanishes. Finally, if \(1\le j<s\) and \(1\le L<s\), then \(j+L=h-1\ge s+1\), and the coefficient sum simplifies exactly to
\[
A_{p,\alpha}(N+p^j)-A_{p,\alpha}(N+1)=p^j-1+\big((p-1)(h-\alpha)-1\big)p^{s-1}>0.
\]
The final strictness follows from \(h-\alpha\ge1\), \(p\ge2\), and \(j\ge1\). Therefore the best elementary row is \(2N\) for odd \(p\), and \(N+1\) for \(p=2\), with exactly the exceptional tie \(p=2,\alpha=2\) at \(N+2^{h-1}\). Step 1 excludes all other rows from equality. This completes the proof.

## Verification

The accompanying `verify_pascal_second_min.py` computes each row count by independently tracking borrow states and verifies the theorem by exhaustive intervals for \(p\in\{2,3,5,7\}\), \(2\le\alpha\le5\), and \(1\le h\le6\) whenever the upper endpoint is at most \(40000\). It also directly compares the digit recurrence against exact integer binomial coefficients for all \(n<230\). On replay, the program reports `CHECK_OK full_intervals=84 counted_rows=138920 direct_binomial_checks=3680`. These finite tests corroborate but do not replace the all-parameter proof.

## Relationship to prior work

Kummer's theorem (1852) supplies the borrow interpretation. Everett (arXiv:0710.1468, 2007), Rowland (arXiv:1001.1783, 2010), and Spiegelhofer–Wallner (arXiv:1604.07089, 2016) derive general pointwise formulas for counts of binomial coefficients with prescribed prime-power divisibility. Their results enable the evaluation of an individual row and therefore **implicitly determine the entries in any finite interval**, but the inspected primary texts do not formulate or prove the uniform second-minimum and complete-equality-set optimization here. Davis–Webb's analysis of Pascal's triangle modulo four treats a special modulus; the present result includes it without claiming to rediscover its counting formulas. The new assertion is a sharp, uniform, structural extremal theorem derived from these classical counting principles.

## Limitations

Originality is relative to inspected references, not a guarantee of uniqueness in all literature. The digital-counting technology is classical; the asserted new contribution is the cross-parameter **second-order extremal classification**, not a new formula for individual row counts. Higher ordered minima and density/multiplicity profiles over larger ranges remain untreated. External independent mathematical review has not been conducted.

## References

1. E. Rowland, *The number of nonzero binomial coefficients modulo \(p^\alpha\)*, arXiv:1001.1783 (initial public version 2010-01-12), https://arxiv.org/abs/1001.1783.
2. W. B. Everett, *Number of binomial coefficients divided by a fixed power of a prime*, arXiv:0710.1468 (initial public version 2007-10-08), https://arxiv.org/abs/0710.1468.
3. L. Spiegelhofer and M. Wallner, *An explicit generating function arising in counting binomial coefficients divisible by powers of primes*, arXiv:1604.07089 (initial public version 2016-04-24), https://arxiv.org/abs/1604.07089.
4. K. Davis and W. Webb, *Pascal's triangle modulo 4*, Fibonacci Quarterly **29** (1991), 79–83.
5. E. E. Kummer, *Über die Ergänzungssätze zu den allgemeinen Reciprocitätsgesetzen* (1852), borrow interpretation of prime valuations of binomial coefficients.
