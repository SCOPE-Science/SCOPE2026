# Exact central-binomial Cusick bias for uniformly separated one-bits

## Finding
For each integer \(h\ge3\), let \(e_1<\cdots<e_h\) be nonnegative integers with gaps \(e_{j+1}-e_j\ge h+1\), and put \(t=\sum_{j=1}^h2^{e_j}\). The density
\[
c_t=\lim_{X\to\infty}\frac1X\#\{0\le n<X:s_2(n+t)\ge s_2(n)\}
\]
exists and takes the position-independent value
\[
\boxed{c_t=\frac12+\frac{1}{2\cdot4^h}\binom{2h}{h}.}
\]
The associated bias is \(c_t-1/2\sim(2\sqrt{\pi h})^{-1}\). The same equality is true for \(h=1,2\), but the claimed uniform structural family concerns \(h\ge3\).

## Assumptions and scope
The sum \(s_2(n)\) is the number of ones in the ordinary base-two representation of \(n\ge0\). A binary carry at digit \(j\) is the outgoing carry from position \(j\) to \(j+1\) when adding \(n\) and \(t\). The support positions \(e_j\) may depend arbitrarily on \(h\), provided adjacent distances are at least \(h+1\); the density is taken with \(h,t\) fixed and \(X\to\infty\). The eventual probabilistic computations use independent fair binary digits, the limiting distribution of any fixed prefix of the nonnegative integers.

## Proof
For a nonnegative integer \(n\), let \(K(n,t)\) be the total number of outgoing binary carries in the addition of \(n\) and \(t\). Summing the bitwise identities gives the exact integer relation
\[
s_2(n+t)=s_2(n)+s_2(t)-K(n,t)=s_2(n)+h-K(n,t).
\]
Consequently the defining event is \(K(n,t)\le h\). For fixed \(t\), the tail after the highest nonzero bit of \(t\) is a geometrically decaying carry process under independent fair random bits, so the limiting probability of the event exists. Equivalently, for every \(r\) the bit-prefix distributions are uniform for integer intervals of length \(2^r\), and the probability that a carry survives beyond \(r\) goes to zero.

For each injection position \(e_j\), imagine adding the isolated bit \(2^{e_j}\) to the same infinite fair binary word. The outgoing carry-chain length \(L_j\) has law
\[
\Pr(L_j=\ell)=2^{-\ell-1}\qquad(\ell=0,1,\ldots),
\]
because a length \(\ell\) chain encounters exactly \(\ell\) initial ones and then a zero. Define its truncated length \(T_j=\min(L_j,h+1)\). The event \(\sum_jT_j\le h\) depends only on bits at positions \(e_j,\ldots,e_j+h\). These windows are disjoint by the gap hypothesis, hence the \(T_j\) are independent and distributed as independently truncated copies of \(L\).

We claim the original carry event agrees exactly (up to the measure-zero infinite-tail event) with this truncated independent event:
\[
\{K(n,t)\le h\}=\left\{\sum_{j=1}^hT_j\le h\right\}.
\]
If an actual carry launched at one occupied position reaches the next occupied position, its length up to that point is at least \(h+1\), and the total carries exceed \(h\). Therefore every configuration with at most \(h\) actual carries consists of separate isolated-bit carry chains, and their lengths add. Conversely, if the sum of truncated isolated-chain lengths is at most \(h\), then each chain ends before the next occupied position, so the actual carries are exactly these isolated chains. In either direction, a chain that continues beyond \(h\) contributes at least \(h+1\) carries and cannot be in the accepted event. This proves the identity.

For independent geometric \(L_1,\ldots,L_h\) with \(\Pr(L=\ell)=2^{-\ell-1}\), the distribution of the sum is negative binomial:
\[
\Pr\left(\sum_{j=1}^hL_j=m\right)=\binom{h+m-1}{m}2^{-(h+m)}.
\]
The event \(\sum L_j\le h\) is equivalent to obtaining the \(h\)-th success in \(2h\) independent fair coin tosses. By the symmetry of \(\operatorname{Bin}(2h,1/2)\), its probability equals
\[
\Pr(\operatorname{Bin}(2h,1/2)\ge h)=\frac12+\frac{1}{2\cdot4^h}\binom{2h}{h}.
\]
This is \(c_t\). Finally the central binomial asymptotic \(\binom{2h}{h}\sim4^h/\sqrt{\pi h}\) gives the announced bias scale.

## Verification
The standalone exact-rational program `verify.py` evaluates the finite carry automaton and compares its result with the central-binomial formula for every weight \(1\le h\le6\) at three permitted gaps each, with no floating-point arithmetic. For \(h=2,3,4,5,6\), it also calculates the adjacent smaller-gap examples, which do not have the same value in these tests. The verifier is a finite consistency check; the independent-window coupling and binomial symmetry above prove the infinite assertion.

## Relationship to prior work
Bésineau established existence of fixed-shift digit-sum correlation measures. Sobolewski and Spiegelhofer (arXiv:2411.07779, initially public 2024-11-12) developed general measure decompositions and studied in detail shifts with at most two blocks of ones. Cheng's 2026 proof of Cusick's conjecture (arXiv:2606.23398, initially public 2026-06-22) proves strict positivity and a bound uniform in all shifts, while Cheng's arXiv:2608.25899 analyzes minimum bias at large fixed weight. The claim here isolates a different exact phenomenon: a uniform **finite separation threshold** makes the half-line mass independent of all support positions at *every* Hamming weight \(h\ge3\), with the explicit central-binomial constant. The inspected main theorems and relevant isolated-block sections did not state this exact finite-gap stabilization. General recurrence-based evaluations of individual shifts are acknowledged and are not claimed as new.

## Limitations
The gap condition is sufficient, not a full characterization of all shifts producing the same density. The theorem addresses a fixed binary shift and its natural density, not a uniform error term in \(X\) when the shift grows with \(X\). Its discovery/priority relative to all possible published special-case formulas has not been independently certified. For \(h=2\) a smaller gap can change the value, as \(c_5=5/8\) versus \(c_9=11/16\). The main new claim starts at \(h=3\).

## References
- K. Cheng, *A first-exit proof of Cusick's sum-of-digits conjecture*, arXiv:2606.23398 (2026), https://arxiv.org/abs/2606.23398.
- K. Cheng, *Sharp extremal asymptotics for Cusick's sum-of-digits bias at fixed Hamming weight*, arXiv:2608.25899 (2026), https://arxiv.org/abs/2608.25899.
- B. Sobolewski and L. Spiegelhofer, *Decomposing the sum-of-digits correlation measure*, arXiv:2411.07779 (2024), https://arxiv.org/abs/2411.07779.
- M. Drmota, M. Kauers, and L. Spiegelhofer, *On a conjecture of Cusick concerning the sum of digits of n and n+t* (2016), as cited in the above primary papers.
