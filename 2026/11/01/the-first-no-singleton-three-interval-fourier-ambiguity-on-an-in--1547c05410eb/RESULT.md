# The first no-singleton three-interval Fourier ambiguity on an integer grid

## Finding

Let \(\mathcal T_N\) comprise the indicator functions of exactly three disjoint nonempty unions of consecutive unit cells on the integer grid, each occupied component containing **at least two consecutive unit cells**, and both intercomponent gaps containing at least one unit cell. Normalize each support to begin at \(0\) and end at \(N\); equivalently, each mask starts and ends with an occupied cell. The smallest \(N\) for which there exist inequivalent \(f,g\in\mathcal T_N\) with identical continuous Fourier magnitudes is **\(N=19\)**. At this length there is exactly one unordered ambiguous pair modulo translation and reflection; every mask in \(\mathcal T_N\) for \(8\le N\le18\) is uniquely retrievable **within this same constrained class**.

The unique first ambiguous pair is represented by the unit-cell strings

```
1110001111111111011
1111111101111100011
```

or by the interval unions \([0,3)\cup[6,16)\cup[17,19)\) and \([0,8)\cup[9,14)\cup[17,19)\). Their aperiodic autocorrelation vectors coincide and equal

\[
(15,12,10,9,9,9,9,8,7,6,5,5,4,3,2,2,2,2,1).
\]

Here the precise assertion concerns continuous Fourier magnitudes at **all real frequencies**, not just a fixed finite sampling grid. The sharpness and uniqueness assertions are established by complete reproducible finite enumeration, together with an exact algebraic witness.

## Assumptions and scope

Fix an integer \(N\ge8\). For integers \(a,b,c\ge2\), \(u,v\ge1\) with \(a+u+b+v+c=N\), define the binary cell vector

\[
\mathbf x_{a,u,b,v,c}=1^a0^u1^b0^v1^c
\]

and the measurable indicator

\[
f_{\mathbf x}(t)=\sum_{j=0}^{N-1}x_j\,\mathbf 1_{[j,j+1)}(t).
\]

The Fourier transform uses \(\widehat f(\xi)=\int_{\mathbb R}f(t)e^{-2\pi i\xi t}\,dt\). Equality is tested between two functions in the union of these admissible classes; recovery is only **within this model**. Two functions are considered equivalent if one is a translate or a reflected translate of the other. Half-open endpoints have no effect on Fourier transforms.

## Proof

**Fourier reduction.** Put \(P_{\mathbf x}(z)=\sum_{j=0}^{N-1}x_jz^j\). Direct integration gives

\[
\widehat{f_{\mathbf x}}(\xi)=e^{-\pi i\xi}\frac{\sin(\pi\xi)}{\pi\xi}P_{\mathbf x}(e^{-2\pi i\xi}),
\]

with the continuous extension at \(\xi=0\). For integer \(0\le k<N\) set

\[
C_{\mathbf x}(k)=\sum_{j=0}^{N-1-k}x_jx_{j+k}.
\]

The coefficients of the Laurent polynomial \(P_{\mathbf x}(z)P_{\mathbf x}(z^{-1})\) are exactly these correlations and their reflections. Hence identical correlations imply identical Fourier magnitudes. Conversely, equal continuous Fourier magnitudes imply equality of the Laurent polynomials: cancel the common sinc factor on a nonempty open interval and use polynomial identity on the unit circle. Every admissible mask has \(x_0=x_{N-1}=1\), so \(C_{\mathbf x}(N-1)=1\) and every higher correlation vanishes. The data therefore also determine \(N\), excluding cross-length ambiguities.

**Exhaustive no-collision certificate below \(19\).** Any admissible \(N\)-cell mask has unique integer breakpoints \(1\le e_1<e_2<e_3<e_4<N\), yielding

\[
(a,u,b,v,c)=(e_1,e_2-e_1,e_3-e_2,e_4-e_3,N-e_4).
\]

Reversal sends this tuple to \((c,v,b,u,a)\). Keep exactly the lexicographically smaller representative of each reversal orbit. `CHECK.py` exhaustively iterates every four-element subset of \(\{1,\dots,N-1\}\) and retains only tuples with three occupied lengths at least two, using Python integer arithmetic and no random choices. It independently iterates all admissible integer compositions, verifies that both methods return the same correlation fibers, and independently evaluates each correlation by both dot products and integer bit shifts.

The resulting count of normalized reversal classes and distinct correlation vectors is

| \(N\) | Masks modulo reversal | Distinct correlations |
|---:|---:|---:|
| 8 | 1 | 1 |
| 9 | 3 | 3 |
| 10 | 9 | 9 |
| 11 | 19 | 19 |
| 12 | 38 | 38 |
| 13 | 66 | 66 |
| 14 | 110 | 110 |
| 15 | 170 | 170 |
| 16 | 255 | 255 |
| 17 | 365 | 365 |
| 18 | 511 | 511 |
| 19 | 693 | 692 |

Thus every correlation fiber is a singleton through \(18\); at \(19\) exactly one fiber has two elements, and every other fiber has one element. The two canonical five-tuples in that exceptional fiber are

\[
(2,1,10,3,3),\qquad(2,3,5,1,8).
\]

This proves the sharp threshold and complete classification, conditional on the finite enumeration whose full source accompanies the claim.

**Independent algebraic witness.** Define

\[
Q(z)=1+z+z^2+z^6+z^7,\quad A(z)=1+z^8+z^{11},\quad B(z)=1+z^3+z^{11}.
\]

The coefficients of \(Q(z)A(z)\) and \(Q(z)B(z)\) are precisely the two displayed binary strings; there are no overlapping nonzero product terms. Since

\[
B(z)=z^{11}A(z^{-1}),
\]

it follows identically that

\[
(QA)(z)(QA)(z^{-1})=(QB)(z)(QB)(z^{-1}).
\]

The two runs tuples are not equal up to reversal, so the masks are genuinely inequivalent. This provides an exact symbolic identity independent of the exhaustive collision certificate.

## Verification

Run `python3 CHECK.py` with Python \(\ge3.8\), standard library only. It checks two independent complete parametrizations, two independent integer autocorrelation evaluations, every fiber count above, the unique exceptional fiber, and the entire stated autocorrelation vector. An observed successful run ended:

```
CHECK_OK lengths=8..19 normalized_masks=2240 ambiguity_classes_at_19=1
```

The computations are a **finite exhaustive proof component** for the restricted \(N\le19\) universe, not an extrapolation to unbounded lengths. The Fourier reduction and exact witness are separate analytical identities.

## Relationship to prior work

Xia and Xu (2026, arXiv:2606.19855v1), §§4–6, prove general structural statements about phase retrieval of finite unions of intervals, including nonuniqueness for every number of components at least three and a factorization criterion for integer endpoints. Their exhibited three-interval ambiguous pair has an isolated unit cell and does not satisfy the present minimum-width restriction. Their general factorization criterion is acknowledged as prior coverage of the *type* of phase-retrieval ambiguity; the additional claim here is the explicit sharp finite resolution threshold and the complete first ambiguous fiber when each occupied interval is at least two units wide. The sufficient wide-separation hypothesis in their Theorem 6.2 is not imposed here. General run-structure identities for binary autocorrelations, such as those discussed by Willms (2013), do not by themselves provide the particular enumerated threshold.

## Limitations

The minimum width of two cells, unit integer-grid endpoints, exactly three occupied components, and positive gaps are essential scope restrictions. This result does **not** imply uniqueness against competitors with arbitrary real endpoints, shorter components, more components, or coefficients other than zero and one. It proves a first finite ambiguity threshold in this constrained class, not a general stability estimate, asymptotic theorem, or a classification of all later ambiguities. The finite threshold depends on a complete auditable computation; its independent mathematical audit remains unperformed. Earlier unindexed equivalent enumeration is a residual originality risk.

## References

1. Yu Xia and Zhiqiang Xu, *Fourier Phase Retrieval for Finite Unions of Intervals*, arXiv:2606.19855v1 (first public version June 18, 2026), https://arxiv.org/abs/2606.19855.
2. Jürgen Willms, *Autocorrelations of Binary Sequences and Run Structure*, IEEE Transactions on Information Theory **59** (2013), 4985–4993, DOI:10.1109/TIT.2013.2259293.
