# First transition at order 17 in the power-abscissa colossally abundant hierarchy

## Finding

Consider Musin's hierarchy \(A_k(1,2)\) of higher-order colossally abundant numbers, whose coordinate abscissa is \(F(u)=\exp(u^2)\) and whose ordinate is \(-\rho(n)^k\). Let \(m_k=\min A_k(1,2)\). Its initial plateau has **exactly 16 levels**:
\[
m_1=m_2=\cdots=m_{16}=720720,\qquad m_{17}=6983776800.
\]
The new first contact is the fifteenth classical colossally abundant number, and
\[
\frac{m_{17}}{m_{16}}=9690=2\cdot3\cdot5\cdot17\cdot19.
\]
The first equality block through order \(16\) is independently known from Musin's Table 2; the new contribution identifies **order 17** as the exact first transition, including the globally optimal first contact at that order.

## Assumptions and scope

For integers \(n\ge3\), write \(\rho(n)=\sigma(n)/n\) and \(u(n)=\log\log n\). Set \(n_*=55440\), \(D=\{n:n\text{ is colossally abundant},\ n\ge55440\}\), and \(F(u)=\exp(u^2)\). Musin constructs the nested contact sets \(A_k(1,2)\) using the reference point at \(n_*\), the abscissa \(F(u(n))\), and the ordinate \(-\rho(n)^k\). The reference integer itself is excluded from the contact sets. His reference-secant lemma gives the exact characterization
\[
m_k=\min\operatorname*{arg\,max}_{n\in D\setminus\{n_*\}}J_k(n),\qquad
J_k(n)=\frac{\rho(n)^k-\rho(n_*)^k}{F(u(n))-F(u(n_*))}.
\]
Every maximum exists. The theorem establishes the initial plateau length and its first transition for this **particular** coordinate scheme, not all possible higher-order colossally abundant hierarchies.

## Proof

**Reduction to order 17.** Musin's Table 2 proves \(m_k=720720\) for every \(1\le k\le16\). It therefore remains to certify that the infinite optimization defining \(m_{17}\) has the unique maximizer \(6983776800\).

**Exhaustive finite classical contacts.** For each prime \(p\) and integer \(j\ge1\) define the Alaoglu–Erdős critical increment
\[
\varepsilon(p,j)=\frac{\log(1+1/(p+\cdots+p^j))}{\log p}.
\]
Classical colossally abundant integers are exactly the prime-exponent products obtained as the critical parameter decreases; at a tie, both neighboring products are retained. Every colossally abundant integer divisible by a prime at least \(167\) is divisible by the primorial through \(167\), and that primorial exceeds \(10^{65}\). Consequently, every colossally abundant integer below \(10^{65}\) has its prime increments among those with critical value above \(\varepsilon(167,1)\). Moreover, the product after all such strict increments already exceeds \(10^{65}\), so the tie at the cutoff cannot produce an omitted subthreshold candidate.

The packaged verifier enumerates **all 56** such increments using outward-rounded logarithmic intervals, proves that their values are strictly separated, and multiplies in descending critical order. Classical contact index \(9\) is \(55440\), index \(10\) is \(720720\), index \(15\) is \(6983776800\), index \(51\) is below \(10^{65}\), and index \(52\) is above it. This leaves exactly **42** integers in \(D\setminus\{55440\}\) below \(10^{65}\).

**Certified comparisons.** For each of these 42 candidates the verifier computes \(\rho(n)\) as an exact rational number and constructs outward-rounded intervals for \(\log n\), \(u(n)\), \(F(u(n))\), and \(J_{17}(n)\). All comparisons are strictly separated: the lower endpoint for the contact at index \(15\) exceeds the upper endpoint for every other candidate. In particular, its reference secant exceeds \(173600000\) and its margin over the best other finite candidate exceeds \(1.6\%\). Hence the unique maximizer below the cutoff is \(6983776800\).

**Entire infinite tail.** Musin cites Robin's unconditional bound
\[
\rho(n)\le e^{\gamma}u(n)+\frac{0.6483}{u(n)}\qquad(n\ge3),
\]
where \(e^{\gamma}<1.8\). For \(n\ge10^{65}\), one has \(u(n)>5\). Therefore every positive \(J_{17}(n)\) in this tail is at most
\[
B(u)=\frac{(1.8u+0.6483/u)^{17}}{\exp(u^2)-\exp(u(n_*)^2)}.
\]
For \(u\ge5\), the logarithmic derivative of the numerator is less than \(17/u\), whereas the logarithmic derivative of the denominator is greater than \(2u\); since \(17/u<2u\), the function \(B(u)\) is strictly decreasing. Exact outward-rounded evaluation gives \(B(5)<300000\), much smaller than the selected finite secant. Nonpositive secants cannot be maximizers. Thus no colossally abundant number beyond the cutoff can tie or exceed the contact at index \(15\).

Musin's reference-secant lemma now identifies \(m_{17}=6983776800\). Together with the published \(1\)-through-\(16\) plateau, this proves the exact first transition. The integer quotient and its factorization follow directly.

## Verification

Run `python3 artifacts/verify.py` using Python's standard library. Its actual output appears in `artifacts/replay.txt`. The checker uses 110-significant-digit `decimal.Decimal` logarithms and exponentials, with conservative outward padding and explicitly directed arithmetic for all interval operations. It verifies strict separation of every critical increment; every candidate secant inequality; the full tail bound; the known order-\(16\) winner; and, as an ancillary normalization check, the published finite-horizon order-\(32\) winner at classical index \(27\).

The proof does not infer an infinite statement from a finite sample: the primorial and critical-increment argument closes the finite search, while Robin's unconditional inequality eliminates the entire unbounded remainder. The executable verification is a reproducible arithmetic certificate for the strict finite inequalities.

## Relationship to prior work

Musin's Table 2 certifies first contacts for this coordinate scheme at orders \(1\)–\(16\), \(32\), \(64\), \(128\), and \(200\), without a value at order \(17\). His reference-secant lemma and prime-increment framework supply the definitions and reduction, but neither the tabulated values nor the large-order asymptotics determine the first transition immediately after the plateau. The distinction matters: the same number \(6983776800\) is already listed as the order-\(3\) first contact for the **different** abscissa \(F(u)=\exp(u)\); that statement does not imply an order-\(17\) first contact when \(F(u)=\exp(u^2)\).

A prior published prime-support bootstrap for the same manuscript forces a primorial divisor of contacts at order \(8\); it does not determine the order-\(17\) first-contact optimizer or the plateau endpoint. Existing classical lists of colossally abundant integers identify index \(15\), but not the maximizing reference secant in this hierarchy.

## Limitations

The result addresses only the first transition in \(A_k(1,2)\). It does not classify the next transition or arbitrary contacts at fixed order, and it does not strengthen the source's asymptotic results. The source mentions ancillary interval tables/scripts; those supplementary files were not independently read. The inspected full-text paper presents the specific finite first-contact values in Table 2, which skips order \(17\). The present verifier independently establishes that previously unstated value from the printed definitions and bounds.

## References

1. Oleg R. Musin, *Higher-order colossally abundant numbers*, arXiv:2609.33794v1 (first publicly available 2026-09-27), Introduction, Section 2.1, Corollary 3.5, Lemma 3.6, Section 5.1 and Table 2.
2. L. Alaoglu and P. Erdős, *On highly composite and similar numbers*, Transactions of the American Mathematical Society 56 (1944), 448–469.
3. G. Robin, *Grandes valeurs de la fonction somme des diviseurs et hypothèse de Riemann*, Journal de Mathématiques Pures et Appliquées 63 (1984), 187–213.
4. OEIS A004490, classical colossally abundant numbers, used solely as an independent index/factorization reference.
