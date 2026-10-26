# Exact dyadic two-adic valuations in Farhi's integer sequence

## Finding
Let \(a_0=0\), and let the rational recurrence \(a_n=(n/2)a_{n-1}+(n-1)!\) hold for every integer \(n\ge1\). For \(n\ge1\), set \(S_n=\sum_{j=1}^{n}2^j/j\). Then \(a_n=n!S_n/2^n\). **For every integer \(m\ge4\)**, the following valuations are exact:
\[
\nu_2(S_{2^m})=2^m+2m-2,\qquad
\nu_2(a_{2^m})=2^m+2m-3.
\]
Here \(\nu_2\) is the usual two-adic valuation on nonzero rational numbers. Both identities concern infinitely many explicitly specified indices, and the values for \(m=2\) and \(m=3\) need not follow the same formula.

## Assumptions and scope
All finite sums lie in \(\mathbb Q\); auxiliary infinite sums are taken in the complete field \(\mathbb Q_2\). All denominators in those series are nonzero positive integers. The series \(L_r=\sum_{j\ge1}2^j/j^r\), with \(r\in\{1,2,3\}\), converge two-adically because \(j-r\nu_2(j)\to+\infty\). The usual formal logarithm and dilogarithm identities apply after evaluation at the two-adically small argument \(2\).

## Proof
**1. The first two polylogarithm values vanish.** Define \(L_r=\sum_{j\ge1}2^j/j^r\). The convergent two-adic logarithm is \(\log(1-z)=-\sum_{j\ge1}z^j/j\). Its multiplicative identity holds on \(1+2\mathbb Z_2\); since \((-1)^2=1\), it gives \(2\log(-1)=\log(1)=0\), hence \(\log(-1)=0\). Evaluating the power series at \(z=2\) gives \(L_1=-\log(-1)=0\).

The formal identity
\[
\operatorname{Li}_2(z)+\operatorname{Li}_2\!\left(\frac{z}{z-1}\right)
=-\tfrac12\log^2(1-z)
\]
can be checked without analytic continuation: differentiate both sides as formal rational power series around \(z=0\), use \(\operatorname{Li}_2'(z)=-\log(1-z)/z\), and note that both constants vanish. At \(z=2\), the two arguments of \(\operatorname{Li}_2\) are both \(2\), whereas \(\log(1-2)=0\). All three series converge in \(\mathbb Q_2\). Therefore \(2L_2=0\), so \(L_2=0\).

**2. The third value has valuation exactly minus two.** The \(j\)-th term of \(L_3\) has valuation \(j-3\nu_2(j)\). For \(j=4\) this equals \(-2\). This is the unique smallest term valuation: if \(t=\nu_2(j)\) then \(j\ge2^t\); the minima of \(2^t-3t\) are \(1\) at \(t=0\), \(-1\) at \(t=1\), \(-2\) at \(t=2\), \(-1\) at \(t=3\), and at least \(4\) for \(t\ge4\). At \(t=2\), only \(j=4\) attains \(-2\). By the ultrametric inequality for convergent sums,
\[\nu_2(L_3)=-2.\]

**3. Expand the tail at a dyadic index.** Fix an arbitrary integer \(m\ge4\) and set \(N=2^m\). Because \(L_1=0\),
\[
S_N=-\sum_{j\ge1}\frac{2^{N+j}}{N+j}=-2^N R_N,
\qquad R_N=\sum_{j\ge1}\frac{2^j}{N+j}.
\]
For every positive integer \(j\), exact rational division yields
\[
\frac1{N+j}=\frac1j-\frac N{j^2}+\frac{N^2}{j^3}
-\frac{N^3}{j^3(N+j)}.
\]
Summing and using \(L_1=L_2=0\) gives
\[
R_N=N^2(L_3-NT_N),\qquad
T_N=\sum_{j\ge1}\frac{2^j}{j^3(N+j)}.
\]
We show \(\nu_2(T_N)\ge-4\), interpreting this inequality as membership in \(2^{-4}\mathbb Z_2\). When \(j<N\), let \(t=\nu_2(j)<m\). Then \(\nu_2(N+j)=t\), so the \(j\)-th summand has valuation \(j-4t\ge2^t-4t\ge-4\); the last inequality follows by direct inspection for \(t=0,1,2,3,4\) and monotonicity thereafter. When \(j\ge N\ge16\), the estimates \(\nu_2(j)\le\log_2 j\) and \(\nu_2(N+j)\le\log_2(2j)\) imply that its valuation is at least \(j-4\log_2j-1\ge-1\), since the latter function is increasing on \([16,\infty)\) and equals \(-1\) at \(16\). Thus every summand belongs to \(2^{-4}\mathbb Z_2\); convergence yields \(T_N\in2^{-4}\mathbb Z_2\).

It follows that \(\nu_2(NT_N)\ge m-4\ge0\), strictly greater than \(\nu_2(L_3)=-2\). Hence
\[
\nu_2(R_N)=2m-2,\qquad
\nu_2(S_N)=N+2m-2.
\]
Finally, the recurrence (or direct telescoping after multiplication by \(2^n/n!\)) gives \(a_n=n!S_n/2^n\). Legendre's identity \(\nu_2(N!)=N-1\) for the power \(N=2^m\) yields
\[
\nu_2(a_N)=(N-1)-N+(N+2m-2)=N+2m-3.
\]
This completes both assertions for every \(m\ge4\).

## Verification
The accompanying standalone Python file `verifier.py` uses only the standard library. It independently computes the original rational recurrence with exact integer arithmetic and checks the asserted valuation for \(m=4,\ldots,11\), checks the elementary extremal valuation bounds, and evaluates sufficiently long two-adic power-series truncations modulo a high power of two. These checks are finite consistency tests; the universal claims rest on the foregoing algebra and valuation inequalities.

## Relationship to prior work
Farhi's 2022 preprint introduces the integer recurrence and relates it to Genocchi and Stirling numbers. The companion 2022 paper proves a general, nonexact lower bound on \(\nu_2(S_n)\). Dubickas's 2024 Theorem 1 establishes \(\nu_2(S_n)\ge n+1-\log_2(n+1)\), with equality precisely at indices one below a power of two, and his equation (2.4) determines those latter indices exactly. The present theorem determines the complementary, structurally different family of **power-of-two indices** and obtains a substantially larger exact valuation there. Farhi's 2023 dilogarithm paper obtains bounds for a different harmonic-weighted sum, and does not state these exact valuations. OEIS A003149 tabulates the factorial convolution, but the inspected record does not contain the present dyadic valuation identity. A previously implicit derivation from broader techniques is possible; no independent publication-priority claim is made.

## Limitations
No formula is asserted for arbitrary \(n\), and the proof does not settle an unrestricted classification of the exact values of \(\nu_2(S_n)\). The lower indices \(m=2,3\) are excluded. The novelty assessment is limited to the inspected sources and searches; no external independent mathematical audit has been performed.

## References
1. B. Farhi, *On a curious integer sequence*, arXiv:2204.10136 (first publicly posted 2022-04-21), https://arxiv.org/abs/2204.10136 .
2. B. Farhi, *The integrality of the Genocchi numbers obtained through a new identity and other results*, Notes on Number Theory and Discrete Mathematics 28 (2022), 749–757, https://nntdm.net/papers/nntdm-28/NNTDM-28-4-749-757.pdf .
3. A. Dubickas, *On a sequence of rational numbers with unusual divisibility by a power of 2*, Miskolc Mathematical Notes 25 (2024), 203–208, https://epublications.vu.lt/object/elaba:201585470/201585470.pdf .
4. B. Farhi, *Nontrivial lower bounds for the p-adic valuations of some type of rational numbers and an application for establishing the integrality of some rational sequences*, Notes on Number Theory and Discrete Mathematics 29 (2023), 820–826, https://nntdm.net/papers/nntdm-29/NNTDM-29-4-820-826.pdf .
5. OEIS Foundation, *A003149: factorial convolution*, https://oeis.org/A003149 .
