# Three exact square-window GCD laws for balancing companions

## Finding

Let the balancing, Lucas-balancing, and Lucas-cobalancing sequences be defined, respectively, by
\[
B_0=0,\quad B_1=1;\qquad C_0=1,\quad C_1=3;\qquad c_0=-1,\quad c_1=1,
\]
with \(X_{n+2}=6X_{n+1}-X_n\) for each sequence and every \(n\ge0\). For \(k\ge1\) and \(X\in\{B,C,c\}\), define
\[
D_X(k)=\gcd\left\{\sum_{i=1}^k X_{n+i}^{\,2}:n\ge0\right\},\qquad
h(k)=\gcd(k,B_k).
\]
The infinite GCDs are positive because all the window sums are positive. The exact values, for **every** positive integer \(k\), are
\[
\boxed{D_C(k)=h(k),}
\]
\[
\boxed{D_B(k)=
\begin{cases}h(k)/2,&2\mid k,\\h(k),&2\nmid k,\end{cases}}
\]
and
\[
\boxed{D_c(k)=
\begin{cases}3h(k),&k\equiv3\pmod6,\\h(k),&k\not\equiv3\pmod6.\end{cases}}
\]
Thus three square-window GCD families are determined by a single finite index GCD. In particular, the two relationships stated as experimental observations in Question 30 of Mbirika--Schrader--Spilker (2023) follow as theorems. Their fourth family, involving cobalancing squares, is outside the claim.

## Assumptions and scope

All indices \(k\) are positive integers and window starting indices \(n\) are arbitrary nonnegative integers. The symbol \(\gcd\) means the nonnegative greatest common divisor of integers. No restriction to a finite initial collection of windows is made. The formula \(h(k)=\gcd(k,B_k)\) is exact, but is not asserted to be a prime-factorization-free closed form for the separate index-divisibility problem.

## Proof

**1. Identities and the GCD of window differences.** The recurrences give
\[
C_n^2=8B_n^2+1,\quad C_{2n}=2C_n^2-1,\quad
c_n^2=(C_{2n-1}-1)/2\quad(n\ge1).
\]
Standard companion-sequence addition identities, or induction, yield
\[
\sum_{i=1}^k C_{2i}=B_kC_{k+1},\qquad
\sum_{i=1}^k C_{2i-1}=B_kC_k.
\]
Consequently, if \(T_X(n)=\sum_{i=1}^kX_{n+i}^2\), then
\[
T_B(0)=\frac{B_kC_{k+1}-k}{16},\quad
T_C(0)=\frac{B_kC_{k+1}+k}{2},\quad
T_c(0)=\frac{B_kC_k-k}{2}.
\]
The identities \(B_u^2-B_v^2=B_{u-v}B_{u+v}\) and \(C_u-C_v=16B_{(u+v)/2}B_{(u-v)/2}\) (for \(u,v\) of the same parity) imply
\[
\begin{aligned}
T_B(n+1)-T_B(n)&=B_kB_{2n+k+2},\\
T_C(n+1)-T_C(n)&=8B_kB_{2n+k+2},\\
T_c(n+1)-T_c(n)&=8B_kB_{2n+k+1}.
\end{aligned}
\]
The recurrence \(B_{m+n}=B_mB_{n+1}-B_{m-1}B_n\), together with \(\gcd(B_m,B_{m-1})=1\), proves by Euclid's algorithm that \(\gcd(B_a,B_b)=B_{\gcd(a,b)}\) for positive indices. In particular,
\[
\gcd_{n\ge0}B_{k+2+2n}=
\begin{cases}6,&k\text{ even},\\1,&k\text{ odd},\end{cases}
\]
and
\[
\gcd_{n\ge0}B_{k+1+2n}=
\begin{cases}6,&k\text{ odd},\\1,&k\text{ even}.\end{cases}
\]
For any integral sequence, \(\gcd_{n\ge0}T(n)=\gcd(T(0),\{T(n+1)-T(n)\}_{n\ge0})\). It follows that
\[
\begin{aligned}
D_B(k)&=\gcd\left(\frac{B_kC_{k+1}-k}{16},\,\lambda_k B_k\right),\\
D_C(k)&=\gcd\left(\frac{B_kC_{k+1}+k}{2},\,8\lambda_k B_k\right),\\
D_c(k)&=\gcd\left(\frac{B_kC_k-k}{2},\,8\mu_k B_k\right),
\end{aligned}
\]
where \(\lambda_k=6\) for even \(k\) and \(1\) otherwise, whereas \(\mu_k=6\) for odd \(k\) and \(1\) otherwise. These are **exact** reductions of the infinite GCDs.

**2. Two-adic valuations.** Induction in the recurrences shows
\[
C_j\equiv\begin{cases}1,&j\text{ even},\\3,&j\text{ odd},\end{cases}\pmod{16},\qquad
B_j\equiv\begin{cases}3j,&j\text{ even},\\j,&j\text{ odd}\end{cases}\pmod{16}.
\]
Also \(B_{2j}=2B_jC_j\). For an even index \(k=2^st\), where \(s\ge1\) and \(t\) is odd, iteration gives
\[
B_k/2^s=B_t\prod_{j=0}^{s-1}C_{2^jt}\equiv3t\pmod{16}.
\]
In particular \(\nu_2(B_k)=s=\nu_2(k)\). Because \(C_{k+1}\equiv3\) and \(C_k\equiv1\pmod{16}\), the normalized numerators satisfy
\[
\frac{B_kC_{k+1}+k}{2^s}\equiv10t,\quad
\frac{B_kC_{k+1}-k}{2^s}\equiv8t,\quad
\frac{B_kC_k-k}{2^s}\equiv2t\pmod{16}.
\]
Their exact two-adic valuations are respectively \(s+1,s+3,s+1\). After the displayed denominators, \(\nu_2(T_C(0))=s\), \(\nu_2(T_B(0))=s-1\), and \(\nu_2(T_c(0))=s\). The other GCD arguments carry at least these valuations, so these are precisely the two-adic valuations of \(D_C(k),D_B(k),D_c(k)\) for even \(k\).

For odd \(k\), the congruences instead give \(B_k\equiv k\), \(C_{k+1}\equiv1\), and \(C_k\equiv3\pmod{16}\). Therefore \(T_C(0)\) and \(T_c(0)\) are odd, while the second GCD argument for \(D_B(k)\) is \(B_k\), also odd. All three GCDs are odd, matching the oddness of \(h(k)\).

**3. The prime three.** Reducing the \(B\)-recurrence modulo \(3\) gives \(3\nmid B_j\) when \(j\) is odd. For even \(k=2m\), write \(B_{2m}=6R_m\). Here \(R_0=0,R_1=1\) and \(R_{m+2}=34R_{m+1}-R_m\). Modulo \(3\), \(R_m\equiv0\) if and only if \(3\mid m\). The triplication identity
\[
R_{3m}=R_m(4C_{2m}^{\,2}-1)=R_m(3+32B_{2m}^{\,2})
\]
shows that the multiplying factor has exact \(3\)-adic valuation \(1\), because \(3\mid B_{2m}\). Repeatedly removing factors of three proves
\[
\nu_3(B_k)=\nu_3(k)+1\qquad(k\text{ even}).
\]
For even \(k\), this strict inequality makes the \(3\)-adic valuation of each base numerator \(B_kC_{k+1}\pm k\) (or \(B_kC_k-k\)) equal to \(\nu_3(k)\). The extra factor \(3\) from \(\lambda_k=6\) therefore introduces no extra power of three into \(D_B\) or \(D_C\).

For odd \(k\), \(3\nmid B_k\) and \(C_k\equiv0\pmod3\). Hence \(T_c(0)=(B_kC_k-k)/2\) is divisible by \(3\) exactly when \(3\mid k\). Since \(8\mu_kB_k=48B_k\) has exactly one factor of \(3\), this contributes precisely \(3^{\mathbf1_{3\mid k}}\) to \(D_c(k)\).

**4. Remaining odd primes and conclusion.** For any odd prime \(\ell\), division by \(2\) or \(16\) is invertible modulo its powers. At every odd prime, the GCD of \(B_k\) with a base value of the form \((B_kC_j\pm k)/2\) or \((B_kC_j-k)/16\) therefore has the same valuation as \(\gcd(B_k,k)\). The only possible discrepancy caused by multiplying the second GCD argument by \(6\) is at prime \(3\), handled in Step 3. Step 2 supplies the exact powers of \(2\). Combining all valuations gives the three asserted identities.

## Verification

The standalone Python 3 script `balancing_square_gcd_checker.py` tests all window lengths \(1\le k\le300\) for each of the three sequences, independently computing each window GCD using \(25\) consecutive windows with exact integers. It also checks the three initial-sum identities, the exact GCD of two successive window differences, and the recurrence congruences used in the proof. The run printed `PASS: 300 lengths x 3 sequences x 25 windows; sum identities and difference-gcd reductions confirmed.`

The symbolic valuation proof, not the finite checks, establishes the infinite-index result. No general formula for square-window GCDs of the nonhomogeneous cobalancing sequence is claimed.

## Relationship to prior work

Mbirika, Schrader, and Spilker (2023), Question 30, ask for formulas for four square-window GCD families. Their paper **already states** the two proportionality patterns between the balancing, Lucas-balancing, and Lucas-cobalancing cases as computational observations, without a proof or an explicit formula for the Lucas-balancing square-window invariant. The new contribution claimed here is the exact common index-GCD formula \(D_C(k)=\gcd(k,B_k)\) and rigorous proofs of both proposed patterns. This is a partial answer (three of four families), not a claim that the two observed patterns were first discovered here.

Mbirika and Spilker (2022) solve a related square-window problem for sequences satisfying the Fibonacci recurrence, with coefficient \(1\) rather than the balancing recurrence coefficient \(6\) and no Lucas-cobalancing initial data. Fiebig, Mbirika, and Spilker (2024) develop Lucas sequence modular periods, entry points, and order, rather than these square-window GCDs. General recurrence and strong-divisibility identities are used as established tools, not claimed as new.

## Limitations

The formulas reduce three infinite GCDs to \(\gcd(k,B_k)\); no fully factored formula for that separate index GCD is established. The fourth square-window GCD of cobalancing numbers is unresolved. The 2023 paper's authors have referred to work in preparation on GCDs of sums of consecutive squares; a publicly verifiable full text of that prospective follow-up was not identified in the present examination. There is therefore a concrete overlap risk, and the work has not undergone independent validation.

## References

1. aBa Mbirika, Janee Schrader, and Jürgen Spilker, *Pell and associated Pell braid sequences as GCDs of sums of k consecutive Pell, balancing, and related numbers*, Journal of Integer Sequences 26 (2023), Article 23.6.4, arXiv:2301.05758 (first posted January 13, 2023), especially Definitions 6–7 and Question 30. https://arxiv.org/abs/2301.05758
2. aBa Mbirika and Jürgen Spilker, *GCD of sums of k consecutive squares of generalized Fibonacci numbers*, Fibonacci Quarterly 60 (2022), 255–269, arXiv:2204.12626 (first posted April 26, 2022). https://arxiv.org/abs/2204.12626
3. Morgan Fiebig, aBa Mbirika, and Jürgen Spilker, *Period patterns, entry points, and orders in the Lucas sequences: theory and applications*, arXiv:2408.14632 (first posted August 26, 2024). https://arxiv.org/abs/2408.14632
