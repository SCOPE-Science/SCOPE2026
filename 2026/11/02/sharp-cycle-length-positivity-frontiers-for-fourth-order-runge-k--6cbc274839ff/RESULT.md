# Sharp cycle-length positivity frontiers for fourth-order Runge–Kutta

## Finding

For each integer \(n\ge2\), let \(P_n\) be the cyclic permutation matrix \(P_ne_j=e_{j+1\pmod n}\), and let \(Q_n=P_n-I_n\) be the generator of the rate-one unidirectional continuous-time Markov cycle in column convention. For \(p\in\{1,2,3,4\}\), define the explicit exponential Taylor end-step
\[
T_{p,n}(h)=\sum_{k=0}^p\frac{h^kQ_n^k}{k!},\qquad h\ge0.
\]
For \(p=4\), this is exactly the end-step of the classical four-stage, fourth-order explicit Runge–Kutta method applied to this autonomous linear system. For \(p=1,2,3\), these are the standard truncated-exponential linear stability polynomials of the corresponding-order, same-stage explicit schemes.

**Theorem.** Each \(T_{p,n}(h)\) has unit column sums. It is entrywise nonnegative **if and only if** \(0\le h\le H_{p,n}\), with the complete sharp classification

| Order \(p\) | Cycle size \(n\) | Sharp positivity horizon \(H_{p,n}\) |
|---|---|---|
| \(1,2\) | every \(n\ge2\) | \(1\) |
| \(3\) | \(n=2\) | \(\rho_3=1.2563726633\ldots\) |
| \(3\) | \(n\ge3\) | \(1\) |
| \(4\) | \(n=2\) | \(\rho_{4,2}=1.3926467817\ldots\) |
| \(4\) | \(n=3\) | \(\rho_{4,3}=1.4933773767\ldots\) |
| \(4\) | \(n\ge4\) | \(1\) |

The three exceptional positive numbers are the **unique positive roots**, respectively, of
\[
2h^3-3h^2+3h-3=0,\qquad
h^3-2h^2+3h-3=0,\qquad
h^4-4h^2+8h-8=0.
\]
The largest admissible step for the three-state directed cycle thus exceeds that for the two-state cycle, while every cycle of length at least four has the forward-Euler positivity horizon.

**Minimal spectral/positivity separation.** For every two-state continuous-time Markov generator (not merely equal-rate cycles), the classical RK4 end-step is entrywise nonnegative if and only if its nonstationary eigenvalue lies in the closed unit disk. Yet, with \(n=3\) and \(h=3/2\),
\[
T_{4,3}(3/2)=-\frac1{128}I_3+\frac{39}{128}P_3+\frac{90}{128}P_3^2.
\]
This mass-preserving end-step has strictly negative diagonal entries even though both nonstationary eigenvalues have modulus exactly \(79/128<1\). Consequently three states are minimal for a spectrally contracting but non-positive classical RK4 Markov end-step.

## Assumptions and scope

The generator has unit departure rate and exactly one directed transition per state; for rate \(\lambda>0\) replace \(h\) by \(\lambda h\). All steps are exact-polynomial end-steps on autonomous linear systems, with no positivity correction or roundoff. The order-\(4\) conclusion refers to the final RK4 output, **not** positivity of intermediate RK stages. Spectral stability in the second statement means \(|\mu|\le1\) for eigenvalues on the nonstationary (zero-sum) subspace, not convergence of every possible initial distribution. These bounds are not claimed for arbitrary generators, nonlinear ODEs, or other Runge–Kutta tableaux.

## Proof

**1. Finite binomial-residue formula and mass conservation.** Expand \((P_n-I_n)^k\) by the binomial theorem, gather powers of \(P_n\), and set \(E_s(z)=\sum_{r=0}^s z^r/r!\). The end-step is
\[
T_{p,n}(h)=\sum_{r=0}^{n-1}c_{p,n,r}(h)P_n^r,\qquad
c_{p,n,r}(h)=\sum_{\substack{0\le j\le p\\j\equiv r\ (\mathrm{mod}\ n)}}
\frac{h^j}{j!}E_{p-j}(-h).
\tag{1}
\]
Each residue class labels disjoint positions of the cyclic matrix, so entrywise nonnegativity is **equivalent** to nonnegativity of every coefficient \(c_{p,n,r}(h)\). Since \(\mathbf1^\mathsf TQ_n=0\), the columns of every \(T_{p,n}(h)\) sum to one, at every real \(h\).

**2. A universal guaranteed interval and the long-cycle obstruction.** For \(0\le h\le1\), each alternating Taylor polynomial \(E_s(-h)\) is nonnegative. One proof groups successive terms: \(E_{2r+1}(-h)=\sum_{j=0}^r[h^{2j}/(2j)!-h^{2j+1}/(2j+1)!]\ge0\) because \(h\le1\), and \(E_{2r}(-h)=E_{2r-1}(-h)+h^{2r}/(2r)!\ge0\). Therefore (1) has nonnegative coefficients throughout \([0,1]\). For \(p\ge2\) and \(n\ge p\), the coefficient in residue \(p-1\) contains only the power \(j=p-1\), hence equals \(h^{p-1}(1-h)/(p-1)!\), which is strictly negative for **every** \(h>1\). For \(p=1\), the identity coefficient is \(1-h\). This proves all table entries with \(n\ge p\), including the long-cycle branches, and proves the universal \(p=1\) branch.

**3. Short-cycle exceptions.** There are precisely three cases not covered by Step 2:

For \((p,n)=(3,2)\), the even and odd residue coefficients are
\[
c_0=-\tfrac13(2h^3-3h^2+3h-3),\qquad
c_1=\tfrac h3(2h^2-3h+3).
\]
The second coefficient is positive for every \(h>0\), since its quadratic has negative discriminant and positive leading coefficient. The polynomial multiplying \(-1/3\) in \(c_0\) is strictly increasing on \([0,\infty)\), with derivative \(6h^2-6h+3>0\), starts negative, and tends to infinity. Thus it crosses zero once, at \(\rho_3\), and the positivity set is exactly the first interval in the table.

For \((p,n)=(4,2)\), the coefficients are
\[
c_1=-\tfrac h3(h^3-2h^2+3h-3),\qquad
c_0=\tfrac12[1+E_4(-2h)].
\]
The second coefficient is strictly positive for all \(h\ge0\): Taylor's theorem at degree four gives \(E_4(-z)=e^{-z}+z^5e^{-\xi}/5!>0\) for some \(\xi\in[0,z]\), whenever \(z>0\). The cubic multiplying \(-h/3\) in \(c_1\) has derivative \(3h^2-4h+3>0\), starts negative, and tends to infinity. Thus it has exactly one positive zero, \(\rho_{4,2}\), beyond which \(c_1<0\).

For \((p,n)=(4,3)\), the three residue coefficients simplify to
\[
\begin{aligned}
c_0&=1-h+\frac{h^2}{2}-\frac{h^4}{8},\\
c_1&=\frac{h(2-h)(h^2-2h+4)}8,\\
c_2&=\frac{h^2(h^2-2h+2)}4.
\end{aligned}
\]
Here \(c_2>0\) for \(h>0\), and \(c_1\ge0\) on \([0,2]\). Moreover \(c_0'(h)=-1+h-h^3/2<0\) on \([0,\infty)\): the maximum of \(h-h^3/2\) is \((2/3)\sqrt{2/3}<1\). As \(c_0(0)=1\) and \(c_0(2)=-1\), it has one zero \(\rho_{4,3}\in(0,2)\), and is negative for every larger step. This completes the sharp classification, including its endpoints and exclusion of later reentrant windows.

**4. The universal two-state spectral implication.** Every two-state column Markov generator has the form
\[
Q=\begin{pmatrix}-a&b\\a&-b\end{pmatrix},\qquad a,b\ge0.
\]
If \(a+b=0\), its RK4 step is the identity. Otherwise let \(\lambda=a+b\) and \(\Pi=\lambda^{-1}\begin{pmatrix}b&b\\a&a\end{pmatrix}\), a nonnegative rank-one stochastic projection. Since \(Q=-\lambda(I-\Pi)\), the end-step equals
\[
T_4(h;Q)=\Pi+E_4(-\lambda h)(I-\Pi).
\]
By the positive Taylor-remainder argument above, \(E_4(-\lambda h)>0\). Its off-diagonal entries are \((1-E_4(-\lambda h))\Pi_{ij}\), while its diagonal entries are \(\Pi_{ii}+E_4(-\lambda h)(1-\Pi_{ii})>0\). Hence the matrix is entrywise nonnegative exactly when \(E_4(-\lambda h)\le1\), which is exactly the spectral unit-disk condition on the one-dimensional nonstationary subspace.

**5. Sharp three-state obstruction.** Substituting \(h=3/2\) into (1) gives the rational circulant stated above. Its diagonal coefficient is negative. Let \(\omega=e^{2\pi i/3}\). The two nonstationary eigenvalues are \(\mu_\pm=(-1+39\omega^{\pm1}+90\omega^{\mp1})/128\). The identity \(\omega^2+\omega+1=0\) yields \(\lvert\mu_\pm\rvert^2=6241/16384=(79/128)^2<1\). Therefore spectral contraction does not entail positivity in dimension three, whereas Step 4 rules such a separation out in dimension two.

## Verification

The accompanying standalone `verify.py` uses only the Python standard library and rational arithmetic. Execute `python verify.py` from the same directory. It recomputes every matrix polynomial directly and independently compares it with the residue formula on \(11\) cycle sizes, four polynomial orders, and \(41\) rational steps; checks the sign table; checks \(1{,}260\) distinct two-state rate/step combinations; verifies the rational three-state eigenvalue certificate; and brackets all three algebraic endpoints by rational decimal intervals. The reference run printed `ALL_CHECKS_PASSED 4070`.

The infinite quantification over all cycle lengths, all nonnegative step sizes, and all two-state generators is established by the analytical proof, **not** by this finite verifier. The check is complementary evidence against algebraic and transcription mistakes.

## Relationship to prior work

The graph-Laplacian/Markov positivity setting and the limitations of standard high-order integrators are established in the February 16, 2021 preprint by Blanes, Iserles and Macnamara [1], which uses classical RK4 as a comparison solver. Earlier SSP theory and its refinements by Gottlieb, Grant and Higgs [2] and Higueras, Ketcheson and Kocsis [3] study general convex monotonicity guarantees and their improvement by method design or perturbation. Those sources do not state the finite-cycle-dependent exact RK4 end-step boundaries or the all-two-state versus three-state spectral/positivity separation above. The general facts that SSP radii can vanish for RK4, that spectral stability differs from positivity, and that the scalar RK4 negative-real-axis stability endpoint is known are **not** claimed to be new. The investigated claim is the complete sharp directed-cycle classification, including the exact algebraic three-cycle threshold and the minimal-dimension spectral counterexample.

## Limitations

The table is specific to unit-rate unidirectional cycles and first through fourth Taylor end-step polynomials. In particular the sharp horizon for general Markov generators need not depend on state count alone. The two-state spectral equivalence is specific to the RK4 polynomial, whose values on the negative real axis stay positive. Intermediate RK stages can fail positivity even if the final end-step is nonnegative. Search-based originality assessment is provisional: a specialized Markov-semigroup, circulant, or stochastic-matrix literature result may already entail this classification. No independent scientific audit has been performed.

## References

[1] Sergio Blanes, Arieh Iserles, Shev Macnamara, *Positivity-preserving methods for population models*, arXiv:2102.08242, first posted 2021-02-16, https://arxiv.org/abs/2102.08242 . The revised article is *Positivity-preserving methods for ordinary differential equations*, DOI:10.1051/m2an/2022042.

[2] Sigal Gottlieb, Zachary J. Grant, Daniel Higgs, *Optimal Explicit Strong Stability Preserving Runge–Kutta Methods with High Linear Order and Optimal Nonlinear Order*, arXiv:1403.6519, first posted 2014-03-25, https://arxiv.org/abs/1403.6519 .

[3] Inmaculada Higueras, David I. Ketcheson, Tihamér A. Kocsis, *Optimal monotonicity-preserving perturbations of a given Runge–Kutta method*, arXiv:1505.04024, first posted 2015-05-15, https://arxiv.org/abs/1505.04024 .
