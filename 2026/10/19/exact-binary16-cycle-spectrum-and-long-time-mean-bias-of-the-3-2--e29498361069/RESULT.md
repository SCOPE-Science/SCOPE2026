# Exact binary16 cycle spectrum and long-time mean bias of the \(3/2\)-beta map

## Finding

Let \(F\) be the map obtained by evaluating the generalized Bernoulli transformation \(x\mapsto (3x/2)\bmod 1\) in IEEE 754 binary16, rounding each multiplication to nearest with ties to even and then subtracting \(1\) when the rounded product is at least \(1\). Subnormals are retained. The closed domain of all nonnegative binary16 states strictly below \(1\) has exactly \(15360\) members. Its complete functional graph has exactly **five periodic cycles**. The following table gives their least period, total basin cardinality (including the cycle), smallest cycle bit pattern interpreted as an unsigned integer, and maximum first-entry time to that cycle:

| Least period | Basin cardinality | Minimum cycle encoding | Maximum first-entry time |
|---:|---:|---:|---:|
| \(1\) | \(5705\) | \(0\) | \(155\) |
| \(3\) | \(26\) | \(14012\) | \(15\) |
| \(4\) | \(3138\) | \(13280\) | \(133\) |
| \(24\) | \(2013\) | \(9472\) | \(77\) |
| \(41\) | \(4478\) | \(10944\) | \(67\) |

For a uniformly sampled **stored** state, the expectation of the orbitwise Cesàro long-time average of the observable \(x\) is exactly
\[
 M_{\mathrm{stored}}=\frac{825722879}{2751463424}=0.3001031639\ldots.
\]
For a Lebesgue-uniform initial real \(x\in[0,1]\) independently rounded once to nearest binary16 (including the positive-measure cell rounding to \(1\)), the five basin probabilities have the common denominator \(2^{25}=33554432\) and numerators \(12777057,68656,7273607,4398294,9036818\), respectively. In this natural initial-ensemble model, the expectation of the orbitwise Cesàro time average is exactly
\[
 M_{\mathrm{rounded}}=\frac{13332128797227}{45079976738816}=0.2957439147\ldots.
\]
The absolutely continuous invariant probability of the real \(3/2\)-beta transformation has mean \(M_{\mathrm{real}}=0.3988940412502474\ldots\). Consequently,
\[
 0.103<M_{\mathrm{real}}-M_{\mathrm{rounded}}<0.104.
\]
This is an exact initial-ensemble calculation for the specified finite-precision model, not an asymptotic extrapolation in precision.

## Assumptions and scope

IEEE 754 binary16 is used with a one-bit sign, five exponent bits, and ten fraction bits, roundTiesToEven for multiplication and subtraction, and gradual underflow (no flushing of subnormals). The multiplier \(3/2\) is exactly representable. For \(x\ge0\), form \(p=\operatorname{RN}_{16}((3/2)x)\) and let \(F(x)=p\) if \(p<1\), otherwise \(F(x)=\operatorname{RN}_{16}(p-1)\). There is no fused operation or extra-precision intermediate. Every one of the \(15360=15\cdot1024\) nonnegative binary16 encodings from \(0\) through \(0x3bff\) is included, with the single zero encoding; \(1\) is excluded from the recurrent-state domain but included as a possible initial rounding endpoint. An orbitwise long-time average means \(\lim_{N\to\infty}N^{-1}\sum_{n=0}^{N-1}F^n(x)\), which exists on every finite functional graph.

## Proof

**Exact arithmetic reduction.** Index the encodings by integers \(h=0,\ldots,15360\) (including the encoding of \(1\)). Write the exact represented real as \(V_h/2^{24}\), with
\[
 V_h=\begin{cases}f,&e=0,\\ (1024+f)2^{e-1},&e\ge1,\end{cases}\qquad
 e=\lfloor h/1024\rfloor,\quad f=h\bmod1024.
\]
Thus the rounded product is determined by comparing the exact integer \(3V_h\) with two times the adjacent values in the strictly increasing table \((V_j)\). If the distances tie, the even-significand encoding is selected. Because a rounded product at least \(1\) lies below \(3/2\) and has an integral multiple of \(2^{-10}\), subtracting \(1\) is exactly representable in binary16. Therefore the integer-only routine in `CHECKER.py` implements the stated IEEE operations without any floating-point rounding ambiguity.

**Complete graph certificate.** For each of the \(15360\) encodings, construct its unique successor by that exact integer routine. Compute indegrees, iteratively delete vertices of indegree zero, and then follow all remaining vertices. In every finite functional digraph, the vertices surviving deletion are precisely the disjoint directed cycles. Assign each deleted vertex to its successor's cycle in reverse deletion order, increasing its first-entry depth by one. These finite, exhaustive operations produce exactly the five cycle and basin records in the table. Their basin sizes sum to \(15360\). The maximum depth is \(155\). The little-endian 16-bit successor table has SHA-256 `5b2f33943cdf5fa52dafdaaa48c8b354e29542389d30954404fe1842cfe245e6`.

**Exact long-time means.** On every basin the Cesàro limit equals the arithmetic mean of its unique eventual periodic cycle. Weighting these cycle means by the basin cardinalities over \(15360\) yields \(M_{\mathrm{stored}}\). For a real-valued uniform initial condition, the nearest-binary16 Voronoi cell of an interior encoding \(h\) has length \((V_{h+1}-V_{h-1})/(2\cdot2^{24})\); the cells at \(0\) and \(1\) are clipped to \([0,1]\). The cell rounding to \(1\) is assigned to the cycle reached after one additional step (namely the successor of \(1\), which is \(1/2\)). Summing exactly these integer cell lengths over the five basins proves the stated probability numerators and hence \(M_{\mathrm{rounded}}\).

**Rigorous comparison with the real map.** For \(T(x)=(3x/2)\bmod1\), set \(a_0=1\) and \(a_{j+1}=T(a_j)\), taking the right-sided value at the endpoint. The Parry/Hofbauer invariant density is proportional to \(\sum_{j\ge0}(2/3)^j\mathbf{1}_{[0,a_j]}(x)\); hence its first moment is
\[
 M_{\mathrm{real}}=\frac{\frac12\sum_{j\ge0}(2/3)^j a_j^2}{\sum_{j\ge0}(2/3)^j a_j}.
\]
All \(a_j\) are exact rationals in \([0,1]\). After \(120\) terms, let \(S_1\) and \(S_2\) denote the respective truncated denominator and numerator, and \(R=3(2/3)^{120}\). Since the omitted denominator lies in \([0,R]\) and numerator in \([0,R/2]\),
\[
 \frac{S_2}{S_1+R}\le M_{\mathrm{real}}\le\frac{S_2+R/2}{S_1}.
\]
Both endpoints are explicit exact rational numbers, with separation below \(1.04\cdot10^{-21}\). Exact rational comparison with \(M_{\mathrm{rounded}}\) establishes the strict claimed gap bounds.

## Verification

Run `python3 CHECKER.py` using only Python's standard library. It enumerates every possible successor, compares the complete graph to all five records, computes integer Voronoi-cell basin weights and both exact finite-state means, and computes the \(120\)-term rational enclosure for the real invariant mean. Its assertions include the complete successor-table checksum, the exact rational means, and the absolute-gap enclosure. The operations are exhaustive over all \(15360\) states, not a finite sample from a larger unverified space.

As a separate implementation comparison, all \(15360\) successors were also evaluated using NumPy's binary16 arithmetic for native multiplication and subtraction; there were zero mismatched transitions. The standalone published checker does not require NumPy.

## Relationship to prior work

Boghosian, Coveney and Wang (2019) show that generalized Bernoulli maps can display severe floating-point invariant-measure bias and enumerate cycles for **single precision** at the same \(3/2\) parameter; their reported Float32 cycle information does not determine the binary16 functional graph. Klöwer, Coveney, Paxton and Palmer (2022 preprint; 2023 publication) systematically examine half-precision and other formats, with sampled orbit and invariant-measure comparisons, but their inspected article and accompanying open research description do not present the exact **all-state** binary16 five-cycle/basin classification or the exact uniform-initialization Cesàro mean. The present calculation is an exhaustive and reproducible finite-resolution specification of that natural benchmark; an equivalent unpublished or separately tabulated enumeration cannot be excluded.

## Limitations

Every claim is restricted to the stated binary16 arithmetic semantics, \(3/2\) multiplier, and initial ensembles. Changing the rounding rule, operation order, treatment of subnormals, compiler contraction, or multiplier can change the functional graph. The continuum comparison uses the absolutely continuous invariant probability of the real beta map; it does not say that arbitrary real initial conditions or stochastic-rounding orbits share a single deterministic limit. Exact finite-state enumeration is not a general classification for all precisions or parameters. The cited literature comparisons reduce but do not eliminate priority risk.

## References

1. B. M. Boghosian, P. V. Coveney and H. Wang, *A New Pathology in the Simulation of Chaotic Dynamical Systems on Digital Computers*, Advanced Theory and Simulations **2** (2019), 1900125, DOI: 10.1002/adts.201900125. First publicly published September 23, 2019.
2. M. Klöwer, P. V. Coveney, E. A. Paxton and T. N. Palmer, *Periodic orbits in chaotic systems simulated at low precision*, Research Square preprint (November 8, 2022), DOI: 10.21203/rs.3.rs-2223046/v1; Scientific Reports **13** (2023), 11410, DOI: 10.1038/s41598-023-37004-4.
3. W. Parry, *On the \(\beta\)-expansions of real numbers*, Acta Mathematica Academiae Scientiarum Hungaricae **11** (1960), 401–416. The beta-map invariant density formula also appears in the references and exposition of the papers above.
