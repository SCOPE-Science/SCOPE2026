# A near-square-root rectangle bound from a linear-AND Gap-Hamming promise circuit

## Finding

For every integer \(k\ge 12\), put \(m=2^k\). There is a total Boolean communication function \(F_k\) on
\[
N_k=40k^2m^2-3km
\]
bits per party with public-coin bounded-error randomized communication \(R(F_k)=O(k\log k)\). Every monochromatic rectangle has density at most \(2^{-m/(8k)}\) under the uniform product distribution, so
\[
\operatorname{rect}(F_k)\le 2^{-\sqrt{N_k}/(51(\log_2 N_k)^2)},\qquad
P^{NP^{cc}}(F_k)=\Omega\!\left(\frac{\sqrt{N_k}}{(\log N_k)^2}\right),\qquad
P^{RP^{cc}}(F_k)=\Omega\!\left(\frac{\sqrt{N_k}}{(\log N_k)^3}\right).
\]
Here \(\operatorname{rect}\) denotes the maximum density of a monochromatic rectangle. The adaptive-query costs use Wang and Wu's conventions: an exact answer to a query is charged the nondeterministic or one-sided-error randomized communication cost of the queried function, respectively.

## Construction and scope

Use the Wang–Wu Gap-Hamming cheat sheet, retaining the address and table construction, but replacing their quadratic-AND circuit in Lemma 3.3. Their circuit computes **the complement of the promise indicator**, and the certificate checker tests for a **zero** final gate. The replacement computes this same complement.

Write the two base strings as \(x,y\in\{0,1\}^{km}\) and \(z=x\oplus y\), with \(k\) length-\(m\) blocks. Set \(B_i=1\) exactly when the weight \(w_i\) of block \(i\) is at most \(\lfloor m/3\rfloor\) or at least \(\lceil2m/3\rceil\). Then \(\mathrm{Ind}(z)=\bigwedge_i B_i\). The address on promised inputs is the \(k\)-bit vector of their low/high cases, identifying a cell \(h\in[m]\). The circuit output is \(1-\mathrm{Ind}(z)\), zero on the promise. XOR, NOT and constants are free in the AND-gate count.

### Circuit size

A full adder uses the sum \(a\oplus b\oplus c\) and the carry \((a\wedge b)\oplus(c\wedge(a\oplus b))\); the two carry terms cannot both be true. A ripple addition of two \(j+1\)-bit numbers therefore uses at most \(2(j+1)\) AND gates. The balanced binary tree that sums a block of \(m\) bits uses at most
\[
\sum_{j=0}^{k-1}\frac{m}{2^{j+1}}\,2(j+1)=4m-2k-4
\]
AND gates and gives a \(k+1\)-bit weight.

A comparison \(w>T\) against an \(L\)-bit constant uses at most \(2L\) AND gates. Scan the bits from most significant to least significant, starting with \((eq,gt)=(1,0)\), for equality and strict comparison of the prefixes. If the next constant bit is 0 and the word bit is \(b\), replace the states by \(eq\wedge\neg b\), \(gt\oplus(eq\wedge b)\). If the constant bit is 1, replace them by \(eq\wedge b\), \(gt\). This preserves the prefix meanings, since \(eq\) and \(gt\) cannot both be true. The low and high flags are obtained by negating the comparison against \(\lfloor m/3\rfloor\) and by comparing against \(\lceil2m/3\rceil-1\), respectively. Their OR costs at most one AND. Thus each \(B_i\) uses at most \(4m+2k+1\) AND gates.

Use \(k-1\) binary AND gates for \(\bigwedge_i B_i\), then apply a free NOT to form \(o=\neg(\bigwedge_i B_i)\), and reserve one final AND for \(o\wedge1\). The count is at most \(4km+2k^2+2k<5km\), because \(m>2k+2\). Insert enough unused \(0\wedge0\) gates **before** that final AND to give exactly \(d=5km\) AND gates ordered by evaluation, with gate \(d\) the complement-of-promise output.

### Certificate and randomized protocol

In the field \(K=\mathbb F_{2^{4k}}\), choose distinct points \(\tau_1,\ldots,\tau_d\). A certificate encodes a polynomial \(p\) of degree at most \(2d-2\) by its \(2d-1\) coefficients. The claimed output of gate \(v\) is \(p(\tau_v)\). Replacing preceding AND outputs by their claimed values leaves each gate's input pair affine over \(K\) in \(z\) and those claims, because only XOR, NOT and constants are used between AND gates. Let \(f,g\), each of degree at most \(d-1\), interpolate the two sequences of claimed inputs at the \(\tau_v\). The exact check of Wang and Wu (Section 3.3) accepts just when \(p\equiv fg\) and \(p(\tau_d)=0\).

For the actual gate input values, the product of their two interpolants gives a certificate satisfying the polynomial identity: at each point its value is the actual gate output, so it induces those same interpolants. Conversely, the identity forces every claimed gate output in evaluation order; once these values are fixed, the two interpolants are fixed and the identity determines the entire polynomial. The output condition is therefore satisfied by exactly one certificate when \(\mathrm{Ind}(z)=1\), and by none when \(\mathrm{Ind}(z)=0\). The padding merely contributes forced zeros to this induction.

Each party has a table with \(m\) cells, each a string of \(4k(2d-1)\) bits. On a promised base input \(F_k\) is the exact check on the XOR of the two cells at the address; on an unpromised input it is 0. For the randomized protocol, estimate the address by sampling \(O(\log k)\) public coordinates per block. On promised input this errs with probability at most \(1/6\) by independent-sample concentration and the union bound. For the chosen certificate, a uniform \(T\in K\) tests \(p(T)=f(T)g(T)\), together with the exact check at \(\tau_d\). Four field elements suffice via linear shares, accounting for the known affine constants. The field has \(d<|K|\), and the nonzero polynomial root bound gives error at most \((2d-2)/|K|<1/6\) for \(k\ge12\). Sampling \(T\) independently of the address estimate preserves this bound for each chosen address. On unpromised input the exact check rejects every cell choice. Hence the total protocol has error at most \(1/3\) and uses \(O(k\log k)\) bits.

### Rectangle bound and input length

In Wang and Wu's proof of Theorem 5.1, the 0-rectangle argument uses density of table projections, not the architecture or size of the promise circuit. For a candidate 0-rectangle of density at least \(2^{-m/(8k)}\), it selects a cell \(h\) and sets of base strings such that the projected table sets at \(h\) each have more than half the possible entries for each selected base string. Its Gap-Hamming argument then selects a promised pair from those sets of base strings with address \(h\). The exact accepted certificate exists, so translating the second cell projection by this certificate makes it intersect the first cell projection. This forces a 1-input in the candidate rectangle. This transfer uses the same number of cells, address rule, uniform product measures, and existence on promised inputs, all retained here. For 1-rectangles, condition on a base pair. On promised input there is exactly one accepting certificate, so the probability over uniform independent tables is \(2^{-4k(2d-1)}\); on unpromised input it is zero. The same expression thus bounds all 1-rectangle densities, and \(4k(2d-1)>m/(8k)\) for \(d=5km\). Both rectangle bounds follow.

The per-party input length is
\[
N_k=km+4km(2d-1)=40k^2m^2-3km.
\]
Using \(N_k<40k^2m^2\), \(k\le\log_2N_k\) and \(8\sqrt{40}<51\) gives
\[
\frac{m}{8k}>\frac{\sqrt{N_k}}{8\sqrt{40}\,k^2}\ge\frac{\sqrt{N_k}}{51(\log_2N_k)^2}.
\]
The product-method bound for the uniform product measure (Wang–Wu, Fact 2.1) gives \(P^{NP^{cc}}(F_k)=\Omega(\log(1/\operatorname{rect}(F_k)))\). Their simulation \(P^{NP^{cc}}(F_k)\le O(\log N_k)P^{RP^{cc}}(F_k)\) gives the last lower bound in the finding.

## Prior work and limitations

The qualitative separation, the fully linear PCP approach, the address protocol and the rectangle method are prior work. Binary adders and constant comparators are standard. Wang and Wu's circuit has \(d=k(m(m+3)+1)\) AND gates; their density bound as a function of \(k,m\) is unchanged here. The improvement is in the certificate-dependent input length, from \(\Theta(k^2m^3)\) to \(\Theta(k^2m^2)\), converting the same exponent \(m/(8k)\) into a near-square-root exponent in the actual input length. This does not assert an optimal exponent, exact rectangle density, or a new qualitative separation.

The supplied `artifacts/verify_parameters.py` checks component truth tables and representative parameter inequalities. It does not check whether the full circuit has the proper output polarity or prove the asymptotic results; the output and checker compatibility are verified above.

## References

1. H. Wang and P. Wu, *Efficient Randomized Communication Without Large Monochromatic Rectangles*, arXiv:2609.20763v1, 2026; ECCC TR26-190.
2. D. Boneh, E. Boyle, H. Corrigan-Gibbs, N. Gilboa, and Y. Ishai, *Zero-Knowledge Proofs on Secret-Shared Data via Fully Linear PCPs*, CRYPTO 2019, IACR ePrint 2019/188.
