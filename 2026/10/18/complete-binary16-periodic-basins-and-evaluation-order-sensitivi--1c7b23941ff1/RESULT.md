# Complete binary16 periodic basins and evaluation-order sensitivity of the quadratic logistic-like map

## Finding

For the quadratic chaotic map \(f(x)=2-x^2\), consider the complete set \(S\) of distinct finite IEEE-754 binary16 numerical values in \([-2,2]\), with positive and negative zero identified. Let \(R_{16}\) be correctly rounded binary16 round-to-nearest, ties-to-even, including gradual underflow. The two completely specified finite maps are
\[
F(x)=R_{16}(2-x^2),\qquad G(x)=R_{16}\bigl(2-R_{16}(x^2)\bigr).
\]
Every trajectory of either map is eventually periodic. Its exact cycle census, including **full basins** (each cycle plus every transient state ultimately entering it), is as follows. A cycle is identified by the hexadecimal binary16 word encoding its smallest numerical member.

| Map | Cycle minimum word | Least period | Full basin size |
| --- | --- | ---: | ---: |
| One final rounding \(F\) | `0xc000` | 1 | 20,785 |
| \(F\) | `0xbff8` | 94 | 11,706 |
| \(F\) | `0xbfa5` | 6 | 168 |
| \(F\) | `0xbebb` | 5 | 60 |
| \(F\) | `0xbe91` | 5 | 48 |
| \(F\) | `0x3c00` | 1 | 2 |
| Separate rounding \(G\) | `0xc000` | 1 | 20,341 |
| \(G\) | `0xbff0` | 44 | 12,156 |
| \(G\) | `0xbf76` | 4 | 62 |
| \(G\) | `0xbef8` | 8 | 208 |
| \(G\) | `0x3c00` | 1 | 2 |

These are **all** cycles and basins for all \(32{,}769\) numerical states. The two evaluation orders disagree on exactly \(1{,}842\) one-step transitions. For \(F\) there are \(2{,}049\) distinct successor values and maximal transient length \(59\); for \(G\) the corresponding figures are \(1{,}946\) and \(69\). Exactly two states attain each maximal transient length.

If the initial condition is uniformly sampled from the finite stored-state set \(S\), the exact expected infinite-time Cesàro mean is respectively
\[
\mathbb E_{x\sim\mathrm{Unif}(S)}\left[\lim_{N\to\infty}\frac1N\sum_{j=0}^{N-1}F^j(x)\right]
=-\frac{145830929641}{126168514560}
\]
and
\[
\mathbb E_{x\sim\mathrm{Unif}(S)}\left[\lim_{N\to\infty}\frac1N\sum_{j=0}^{N-1}G^j(x)\right]
=-\frac{861146119}{738220032}.
\]
For initial states drawn uniformly instead from the \(15{,}361\) stored binary16 values in \([0,1]\), these expectations are \(-217681579937/177430609920\) and \(-215011427/173026304\), respectively. In contrast, the invariant arcsine probability of the exact real map on \([-2,2]\) has mean zero, and the real-time average is zero for Lebesgue-almost every initial condition.

## Assumptions and scope

This is a precise **mathematical model of low-precision iteration**, not a claim that an actual analogue circuit uses binary16 arithmetic. The squaring and subtraction in \(F\) are evaluated over exact real arithmetic, followed by one final binary16 rounding. In \(G\), the nonnegative square is rounded first and subtraction from exactly representable \(2\) is rounded again. These protocols differ from a compiler-dependent fused operation, a rounded multiplication of two distinct operands, stochastic rounding, or a truncation scheme. Every binary16 subnormal is retained; the two signed-zero encodings represent one numerical state, consistently with ordinary arithmetic equality. The polynomial maps \([-2,2]\) into itself, so the finite graphs are closed. No floating-point overflow or invalid values occur.

The reported expectations use the **uniform finite-stored-state distribution**, not a uniform distribution in the continuum. For every state and either finite map, the ordinary time average exists because the orbit eventually reaches a finite cycle.

## Proof

**1. Exhaustive exact state representation.** Put \(U=2^{24}\). Every binary16 value within the domain is uniquely represented as \(k/U\), where \(k\) is an integer. A finite normalized binary16 magnitude with exponent field \(e\in\{1,\ldots,16\}\) and fraction field \(m\in\{0,\ldots,1023\}\) has \(k=(1024+m)2^{e-1}\); for a subnormal \(k=m\). Both signs are included except that the duplicated zero is merged. This produces all \(32{,}769\) domain values; the available nonnegative binary16 values through \(4\) number \(17{,}409\). The source `verify.py` independently enumerates every one of the \(2^{16}\) raw words to build these sets and asserts both cardinalities.

**2. Exact transition construction.** For integer-scaled state \(k\), compute the exact numerator \(2U^2-k^2\) over denominator \(U\) to represent \(U f(k/U)\). Find the two adjacent eligible integer-scaled half values by binary search and compare exact integer distances to that rational. On a tie, the neighboring value with even least significant significand bit is selected. For \(G\), similarly round the numerator \(k^2\) over denominator \(U\) into the set of nonnegative half values through \(4\), and then round the exact difference from \(2U\) again. Some such differences are not themselves binary16 values. Thus no floating-point calculation enters the authoritative transition construction. The resulting successor indices are completely determined at each of the \(32{,}769\) states.

**3. Exhaustive functional-graph certificate.** In a finite directed graph with one outgoing edge from every vertex, repeatedly remove vertices of indegree zero. The remaining vertices are exactly the disjoint directed cycles. Give each such cycle a distinct label, then process removed vertices in reverse order to assign the same label as their successors and add one to successor depth. This proves both completeness of the cycle census and the full-basin counts. The supplied checker implements these steps, checks \(\sum\text{basin-size}=32769\), verifies that every state after its assigned depth is on the asserted cycle, and recomputes cycle averages as exact rational numbers. It also recomputes each transition independently using the standard library's binary16 packing and unpacking and checks agreement on every input for each evaluation protocol. The finite exhaustive computation yields precisely the tables and counts above.

**4. Time averages and real-map comparison.** A trajectory with transient prefix and a cycle of least period \(p\) has time average equal to the sum of the cycle's states divided by \(p\). Weighting these exact rational averages by the computed basin sizes and dividing by \(32769\) gives the two displayed fractions; restricting initial states to \([0,1]\) and weighting the labels of just those starts gives the other two. Finally, the affine change of variable \(u=(x+2)/4\) conjugates the exact real quadratic map to \(u\mapsto4u(1-u)\). Its absolutely continuous invariant arcsine density is symmetric about \(u=1/2\), so the induced invariant law in the \(x\)-coordinate is symmetric about zero. Ergodicity of the full logistic map under the arcsine law and its equivalence to Lebesgue measure on the interior yield a zero real-time mean for Lebesgue-almost every \(x\in[-2,2]\). The map between real coordinates does not commute with rounding, so this argument does **not** transfer the finite census from an independently rounded logistic map.

## Verification

Run `python3 verify.py` with Python 3 and no third-party dependencies. The script enumerates the full binary16 alphabet by raw-bit decoding; constructs the two maps with integer numerators, denominators and ties-even comparisons; exhaustively peels and labels both graphs; checks every initial state's assigned entry depth; performs an independent `struct`-based binary16 rounding comparison on all \(65{,}538\) protocol/input pairs; and asserts every cycle, basin, transient maximum, exact fraction, distinct-image count and the \(1{,}842\) transition discrepancy. This was successfully executed on the packaged code. The graph census is a **complete finite proof by enumeration**, not an extrapolation from sampled simulations. The real-map almost-sure statement relies on the separate analytical conjugacy argument, not finite computation.

## Relationship to prior work

Wu, Fu, He and Wang introduced and implemented the analogue quadratic logistic-like family \(x\mapsto b-ax^2\) and identified chaotic dynamics at \(a=1,b=2\) [1]. Their inspected mathematical and implementation sections do not give an exact binary16 functional-graph classification under either rounding protocol. Sayed and coauthors investigated finite-precision logistic-map behavior and roundoff effects under different fixed-point choices [2]; these do not determine the present two half-precision quadratic graph counts. Klöwer and coauthors examined low-precision chaotic simulations, including their finite periodic orbits [3], but not the full exact binary16 census here. The exact real affine conjugacy to logistic dynamics does not transfer a binary16 basin or cycle census because the affine change of variables fails to preserve its discrete grid and rounding protocol. An equivalent finite-state computation elsewhere cannot be excluded.

## Limitations

The numerical counts apply exclusively to IEEE-754 binary16, gradual underflow, nearest ties-even, the complete stated stored-state range and the two specified evaluation orders. Compiler arithmetic and hardware circuits may implement different sequences of operations. The displayed expected means average over uniformly chosen stored states (or the explicitly stated \([0,1]\) subset); they are not expectations over uniformly chosen real states, nor do they imply every stored trajectory has the same average. No result on stochastic rounding, higher precision or actual physical noise follows. Exhaustive verification covers this finite format but not a uniform theorem across floating-point formats. Priority searches cannot exclude unindexed or differently described antecedents.

## References

[1] X. Wu, L. Fu, S. He and H. Wang, “Analogue circuit implementation of a new logistic-like map,” *Electronics Letters* **58** (2022), 533–535. First online 31 May 2022. DOI: 10.1049/ell2.12529.

[2] W. Sayed et al., “Finite Precision Logistic Map between Computational Efficiency and Accuracy with Encryption Applications,” *Complexity* (2017), article 8692046. DOI: 10.1155/2017/8692046.

[3] M. Klöwer, P. V. Coveney, C. Paxton and T. N. Palmer, “Periodic orbits in chaotic systems simulated at low precision,” *Scientific Reports* **13** (2023). DOI: 10.1038/s41598-023-37004-4.
