# A near-square-root rectangle bound from a linear-AND Gap-Hamming promise circuit

## Result

For every integer \(k\ge 12\), let \(m=2^k\). There is a total Boolean function \(F_k\) on \(N_k\) bits per party, with
\[
N_k=40k^2m^2-3km,
\]
such that
\[
R(F_k)=O(k\log k)
\]
and every monochromatic rectangle has density at most
\[
\operatorname{rect}(F_k)\le 2^{-m/(8k)}.
\]
Consequently,
\[
\operatorname{rect}(F_k)
\le
2^{-\sqrt{N_k}/(51(\log_2 N_k)^2)},
\]
and therefore
\[
P^{NP^{cc}}(F_k)=\Omega\!\left(\frac{\sqrt{N_k}}{(\log N_k)^2}\right).
\]
Using the standard relation \(P^{NP^{cc}}(F)\le O(\log N)P^{RP^{cc}}(F)\), the same family also satisfies
\[
P^{RP^{cc}}(F_k)=\Omega\!\left(\frac{\sqrt{N_k}}{(\log N_k)^3}\right).
\]

The construction is the Wang--Wu Gap-Hamming cheat-sheet function, with only its Boolean promise-checking circuit replaced. Their exact-prefix-weight dynamic program uses \(\Theta(km^2)\) AND gates. A balanced binary counter and constant-threshold comparators reduce this to fewer than \(5km\) AND gates, while preserving the fully linear PCP, randomized protocol, and monochromatic-rectangle argument.

## Context

Wang and Wu construct a total Boolean function from a \(k\)-block Gap-Hamming promise problem and a fully linear PCP. Their Boolean circuit for the promise indicator computes every exact prefix Hamming weight by dynamic programming, using
\[
d=k\bigl(m(m+3)+1\bigr)=\Theta(km^2)
\]
AND gates. After arithmetization over \(\mathbb F_{2^{4k}}\), the certificate part of each input has length proportional to \(km(2d-1)\). Their rectangle theorem itself gives density at most \(2^{-m/(8k)}\); the quadratic factor in \(d\) therefore enters through the conversion from \((k,m)\) to the total input length.

The observation below supplies a smaller promise circuit satisfying the same circuit interface: XOR, NOT, constants, and AND gates labeled in evaluation order, with the final output produced by the last AND gate.

## A linear-AND promise circuit

### Full adders

For Boolean inputs \(a,b,c\), a full adder can be written as
\[
s=a\oplus b\oplus c,
\qquad
r=(a\wedge b)\oplus\bigl(c\wedge(a\oplus b)\bigr).
\]
The two product terms in the carry expression are disjoint on Boolean inputs, so the XOR is exactly the carry bit. Thus a full adder costs two AND gates; XOR and NOT gates are free in the relevant gate count.

### Balanced Hamming-weight computation

Sum the \(m=2^k\) input bits in a balanced binary tree. At level \(j\), there are \(m/2^{j+1}\) additions of \((j+1)\)-bit integers. A ripple addition of two such integers uses at most \(2(j+1)\) AND gates. Hence the total number of AND gates for one block is
\[
\sum_{j=0}^{k-1}\frac{m}{2^{j+1}}\,2(j+1)
=
4m-2k-4
<4m.
\]
The resulting Hamming weight has \(k+1\) bits.

### Comparing with fixed thresholds

A comparison of an \(L\)-bit word \(w\) with a fixed \(L\)-bit constant can be performed with at most \(2L\) AND gates. Scan bits from most significant to least significant while maintaining two Boolean states: \(eq\), saying that the processed prefixes are equal, and \(gt\), saying that the word is already larger. If the next constant bit is \(0\), use
\[
gt' = gt\oplus(eq\wedge w),
\qquad
eq'=eq\wedge\neg w;
\]
if the constant bit is \(1\), use
\[
gt'=gt,
\qquad
eq'=eq\wedge w.
\]
The terms in the XOR for \(gt'\) are disjoint, so this is a Boolean comparator with at most two ANDs per bit.

Use two such comparisons to test whether a block has Hamming weight at most \(\lfloor m/3\rfloor\) or at least \(\lceil 2m/3\rceil\). Combining the two disjoint cases costs at most one further AND. Therefore one block requires at most
\[
(4m-2k-4)+4(k+1)+1
=4m+2k+1
\]
AND gates.

For all \(k\) blocks, include at most \(k-1\) further AND gates to combine their valid-promise indicators and one final output AND. The total is
\[
d_0\le 4km+2k^2+2k<5km
\]
for \(k\ge12\), since \(m=2^k>2k+2\).

Pad with unused gates of the form \(0\wedge0\), and realize the output as a final gate \(o\wedge1\), to obtain exactly
\[
\boxed{d=5km}
\]
AND gates while retaining the required evaluation ordering and final-gate convention.

## Compatibility with the fully linear PCP

The Wang--Wu arithmetization only needs the preceding circuit form. Once the outputs of earlier AND gates are fixed, every subsequent wire entering an AND gate is affine over the original Boolean inputs and those previously claimed AND outputs. The same polynomial consistency test therefore applies unchanged.

Keeping their field \(\mathbb F_{2^{4k}}\) is more than sufficient. For \(d=5k2^k\) and \(k\ge12\),
\[
d<2^{4k},
\qquad
\frac{2d-2}{2^{4k}}<\frac16.
\]
Thus the same four-query fully linear PCP has the required soundness. Padding gates do not change the computed Boolean function; they merely add forced zero multiplication constraints.

The certificate uniqueness property used in the monochromatic-rectangle proof is likewise unaffected: induction through the ordered AND gates forces every claimed multiplication output to equal the true circuit value. The rectangle argument consequently applies with the new value of \(d\).

## Parameters and communication consequences

With \(d=5km\), the Wang--Wu encoding gives per-party input length
\[
N_k
=km+4km(2d-1)
=40k^2m^2-3km.
\]
Their public-coin randomized protocol still costs \(O(k\log k)\), so
\[
R(F_k)=O(k\log k)=O(\log N_k\log\log N_k).
\]
Their rectangle argument still gives
\[
\operatorname{rect}(F_k)\le2^{-m/(8k)}.
\]
Since \(N_k<40k^2m^2\),
\[
m>\frac{\sqrt{N_k}}{\sqrt{40}\,k}.
\]
Also \(k\le\log_2N_k\). Hence
\[
\frac{m}{8k}
>
\frac{\sqrt{N_k}}{8\sqrt{40}\,k^2}
\ge
\frac{\sqrt{N_k}}{51(\log_2N_k)^2},
\]
which proves the stated explicit rectangle-density bound.

By the product-method lower bound used by Wang--Wu,
\[
P^{NP^{cc}}(F_k)
=\Omega\!\left(\log\frac1{\operatorname{rect}(F_k)}\right)
=\Omega\!\left(\frac{\sqrt{N_k}}{(\log N_k)^2}\right).
\]
Combining this with \(P^{NP^{cc}}(F)\le O(\log N)P^{RP^{cc}}(F)\) gives the stated \(P^{RP^{cc}}\) lower bound.

## Novelty boundary

The qualitative separation between efficient randomized communication and the absence of large monochromatic rectangles is due to Wang and Wu. Fully linear PCPs are also prior work, and balanced binary adders and constant comparators are standard Boolean-circuit devices. The claim here is the quantitative consequence of replacing the particular quadratic-AND promise circuit in the Wang--Wu construction by the linear-AND circuit above: the certificate-driven input scaling drops from \(\Theta(k^2m^3)\) to \(\Theta(k^2m^2)\), yielding the explicit near-square-root rectangle exponent and the corresponding stronger \(P^{NP^{cc}}\) and \(P^{RP^{cc}}\) lower bounds.

## Limitations

The argument concerns this construction and proof template; it does not claim that the exponent \(1/2\) is optimal, nor that the exact monochromatic-rectangle density of these functions matches the stated upper bound. Originality is to the best of our knowledge. The motivating preprint is extremely recent, so a near-simultaneous observation or subsequent revision may not yet be indexed. No independent validation is asserted.

## Reproducibility

`artifacts/verify_parameters.py` checks the full-adder and fixed-threshold comparator truth tables, the gate-count inequalities, the field/soundness inequalities, and the explicit conversion from \((k,m)\) to \(N_k\). `artifacts/verification.txt` records representative exact checks.

## References

1. H. Wang and P. Wu, *Efficient Randomized Communication Without Large Monochromatic Rectangles*, arXiv:2609.20763, 2026; ECCC TR26-190.
2. D. Boneh, E. Boyle, H. Corrigan-Gibbs, N. Gilboa, and Y. Ishai, *Zero-Knowledge Proofs on Secret-Shared Data via Fully Linear PCPs*, CRYPTO 2019, IACR ePrint 2019/188.
