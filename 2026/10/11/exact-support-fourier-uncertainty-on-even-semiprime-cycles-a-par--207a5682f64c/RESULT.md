# Exact-support Fourier uncertainty on even semiprime cycles: a parity law and sharp odd-support jumps

## Finding
Let \(p\ge3\) be an odd prime and \(G=\mathbb Z/(2p)\mathbb Z\). For each integer \(1\le k\le p\), define the **exact** uncertainty profile
\[
\Theta^{\mathrm{ex}}_{2p}(k):=\min\bigl\{|\operatorname{supp}\widehat f|:\ f:G\to\mathbb C,\ |\operatorname{supp}f|=k\bigr\}.
\]
The complete profile on this natural first-half range is
\[
\boxed{\Theta^{\mathrm{ex}}_{2p}(k)=
\begin{cases}
2(p-k+1),&k\text{ odd},\\
\min\{p-k/2+1,\,2(p-k+1)\},&k\text{ even}.
\end{cases}}
\]
Every displayed lower bound is attained by a function with **exactly** the prescribed time support. For even \(k=2r\), the paired-atom and single-parity-slice constructions exchange optimality when \(3r=p+1\); the single-parity-slice construction is optimal when \(3r\ge p+1\). An unexpected consequence is a strict upward jump at support size five: for every prime \(p\ge11\),
\[
\boxed{\Theta^{\mathrm{ex}}_{2p}(5)-\Theta^{\mathrm{ex}}_{2p}(4)=p-7>0.}
\]
Thus the exact-support profile need not be nonincreasing, even though the usual at-most-support uncertainty function is.

## Assumptions and scope
The cyclic group \(G\) has order twice an odd prime. The Fourier transform is \(\widehat f(t)=\sum_{x\in G}f(x)e^{-2\pi itx/(2p)}\); normalization does not affect zero sets. Every \(f\) is an arbitrary complex-valued function, not necessarily an indicator or positive. We require **exact** time support \(k\), in the range \(1\le k\le p\). We make no claim for larger support sizes or general semiprime orders with both factors odd.

## Proof
**1. Two prime Fourier channels.** The Chinese remainder theorem identifies \(G\) with \(\mathbb Z_2\times\mathbb Z_p\). Write \(f_0(x)=f(0,x)\) and \(f_1(x)=f(1,x)\), and define \(h_+(x)=f_0(x)+f_1(x)\) and \(h_-(x)=f_0(x)-f_1(x)\). The Fourier transforms on the two characters of \(\mathbb Z_2\) are exactly the \(p\)-point Fourier transforms \(\widehat h_+\) and \(\widehat h_-\), up to a harmless permutation of characters. Consequently
\[
|\operatorname{supp}\widehat f|=|\operatorname{supp}\widehat h_+|+|\operatorname{supp}\widehat h_-|.
\]

**2. Lower bounds.** The prime-order uncertainty theorem states that every nonzero \(h:\mathbb Z_p\to\mathbb C\) satisfies
\[
|\operatorname{supp}h|+|\operatorname{supp}\widehat h|\ge p+1.
\]
If both \(h_+\) and \(h_-\) are nonzero, their individual support sizes are at most \(k\), so the Fourier-support sum is at least \(2(p-k+1)\). If one channel is zero, then \(f_1=\pm f_0\), and every occupied \(p\)-coordinate supplies **two** nonzero entries of \(f\). Thus \(k=2r\) must be even, the nonzero channel has exactly \(r\) occupied coordinates, and its Fourier support is at least \(p-r+1=p-k/2+1\). For odd \(k\), the second case is impossible. These exhaust all possibilities and prove the stated lower bounds.

**3. Sharpness with exact support.** For each \(1\le s\le p\), a prime-length signal \(h_s\) with exactly \(s\) nonzero coefficients and exactly \(p-s+1\) nonzero Fourier coefficients exists. Here is a constructive proof: take a primitive \(p\)-th root \(\zeta\) and form
\[
P_s(X)=\prod_{j=0}^{s-2}(X-\zeta^j),
\]
where the empty product for \(s=1\) is \(1\). Regard the polynomial's coefficients as \(h_s(0),\ldots,h_s(s-1)\), and zero elsewhere in \(\mathbb Z_p\). Its Fourier transform evaluates \(P_s\) at all \(p\)-th roots, and precisely \(s-1\) such evaluations vanish. The prime uncertainty theorem prohibits any coefficient from vanishing, because that would leave at most \(s-1\) time coefficients together with \(s-1\) Fourier zeros and violate the bound. Hence the time support really has size \(s\).

To attain \(2(p-k+1)\), put \(h_k\) entirely in the \(0\)-slice of \(\mathbb Z_2\times\mathbb Z_p\), with the \(1\)-slice zero. Both Fourier channels then equal \(\widehat h_k\), giving precisely twice its support. For even \(k=2r\), to attain \(p-r+1\), put \(h_r\) on **both** slices with equal coefficients. One Fourier channel vanishes identically and the other is \(2\widehat h_r\). The time support is exactly \(2r\). Taking the smaller of the two attainable bounds proves the entire formula.

**4. Structural crossover and nonmonotonicity.** At even \(k=2r\), the two sharp expressions agree iff \(p-r+1=2(p-2r+1)\), equivalently \(3r=p+1\). For every odd prime \(p\ge11\), the formula yields \(\Theta^{\mathrm{ex}}_{2p}(4)=p-1\) and \(\Theta^{\mathrm{ex}}_{2p}(5)=2p-8\), so the upward jump is \(p-7\), strictly positive and unbounded as \(p\) grows. This is a statement about exact supports, not the monotone at-most-support minimum.

## Verification
The companion standalone Python script `verify_exact_semiprime_profile.py` carries out exact cyclotomic integer arithmetic for the explicit polynomials \(P_s\), for all \(1\le s\le p\) and primes \(p\in\{3,5,7,11,13,17,19\}\). It checks that every coefficient is nonzero, the Fourier zero set has size \(s-1\), and the two candidate sharp formulas agree with the claimed first-half profile. It reports `VERIFY_OK` for 75 support sizes. This finite certificate supplements but does not replace the prime-order analytic uncertainty proof, which establishes the theorem for all odd primes.

## Relationship to prior work
The prime-order uncertainty theorem and full-minor property of the \(p\)-point Fourier matrix (Chebotarev and Tao) supply the critical underlying inequality and the support-sharp signal existence. Loukaki's recent theorem gives parity-balanced nonvanishing minors and a **stratified** uncertainty principle on \(\mathbb Z_2\times\mathbb Z_p\); it does not explicitly provide the exact-support \(k\)-profile, its even-\(k\) crossover, or the strict \(4\)-to-\(5\) jump. Bonami and Ghobber determine the at-most-\(k\) Meshulam function's equality cases for broad product-group ranges, which is a different invariant: allowing fewer than \(k\) nonzero coefficients erases the upward jumps central to this theorem. Existing exact-support computations for fixed small composite groups and previous three- and four-point special results do not provide the full formula for all \(k\le p\) and all odd primes.

## Limitations
This is an exact-support **cardinality** theorem, not a classification of every extremizing coefficient vector or every support shape. The proof builds on the well-known prime Chebotarev/Tao theorem; it does not independently reprove that underlying result. The new step is a complete exact-sparsity parity analysis and optimization across two competing mechanisms for an infinite composite-order family. An undiscovered equivalent full exact-support profile in earlier literature remains a novelty risk. No independent audit has been performed.

## References
1. M. Loukaki, “Chebotarev's theorem for roots of unity of square free order,” arXiv:2412.08600v1, first posted 2024-12-11; journal version: “Chebotarev's theorem for cyclic groups of order pq and an uncertainty principle,” Bulletin of the London Mathematical Society 57 (2025), 3841–3856, DOI 10.1112/blms.70192.
2. A. Bonami and S. Ghobber, “Equality cases for the uncertainty principle in finite Abelian groups,” arXiv:1003.5060v1, first posted 2010-03-26; Acta Scientiarum Mathematicarum 79 (2013), 507–528.
3. T. Tao, “An uncertainty principle for cyclic groups of prime order,” arXiv:math/0308286v1, first posted 2003-08-29; Mathematical Research Letters 12 (2005), 121–127.
