# The joint rational-point and bitangent spectrum of smooth plane quartics over \(\mathbf F_2\)

## Finding

Let \(V=\mathbf F_2[X,Y,Z]_4\). For each nonzero form \(F\in V\), let \(C_F\subset\mathbf P^2_{\mathbf F_2}\) be its zero curve. Say that a rational line \(L\) is an *even-contact line* (a bitangent, including the hyperflex degeneration) when its degree-four intersection divisor with \(C_F\) is twice an effective divisor of degree two over the algebraic closure; equivalently \(F|_L\) is a square of a binary quadratic. This convention explicitly includes contact of order four at a single point. Write \(r(F)=\#C_F(\mathbf F_2)\) and \(b(F)\) for the number of rational even-contact lines. Count equations in fixed coordinates, not only abstract isomorphism classes. Each equation is unique up to scalar because \(\mathbf F_2^\times=\{1\}\).

**Theorem.** Exactly \(10,920\) of the \(32,767\) nonzero binary plane-quartic equations define geometrically smooth curves. Their exact joint distribution \(N_{r,b}=\#\{F:C_F\text{ geometrically smooth},\ r(F)=r,\ b(F)=b\}\) is

| \(r\) | \(b=0\) | \(b=1\) | \(b=2\) | \(b=3\) | \(b=4\) | \(b=7\) | Row total |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 24 | 56 | 84 | 0 | 0 | 1 | 165 |
| 1 | 168 | 588 | 168 | 0 | 84 | 0 | 1,008 |
| 2 | 504 | 1,218 | 840 | 84 | 0 | 0 | 2,646 |
| 3 | 840 | 1,736 | 756 | 0 | 28 | 0 | 3,360 |
| 4 | 840 | 1,260 | 420 | 21 | 0 | 0 | 2,541 |
| 5 | 504 | 420 | 84 | 0 | 0 | 0 | 1,008 |
| 6 | 168 | 0 | 0 | 0 | 0 | 0 | 168 |
| 7 | 24 | 0 | 0 | 0 | 0 | 0 | 24 |
| **Total** | **3,072** | **5,278** | **2,352** | **105** | **112** | **1** | **10,920** |

In particular, \(b\in\{0,1,2,3,4,7\}\), never five or six. Precisely \(105\) quartics have three rational bitangents, with \(r\in\{2,4\}\); precisely \(112\) have four, with \(r\in\{1,3\}\). Their rational bitangents have rigid incidence patterns in the seven-line dual Fano plane: in the three-line case they are concurrent, with exactly \(15\) smooth quartics realizing each of the seven concurrent triples; in the four-line case they contain a concurrent triple, with exactly four quartics realizing each of the 28 such four-line sets. The unique quartic with seven rational bitangents has no rational points. The number of quartics possessing at least three rational bitangents is \(218\), a proportion \(109/5460\) of the smooth equations.

## Assumptions and scope

The ground field is exactly \(\mathbf F_2\), and *geometrically smooth* means smooth after base change to an algebraic closure. Every such plane quartic is geometrically integral and of genus three. A bitangent here means an even intersection divisor, with hyperflexes included. The count is for nonzero homogeneous equations in fixed projective coordinates, not unweighted projective-isomorphism classes. The classification does not assert a formula over all even finite fields, or count lines whose geometric contact divisor is not even.

## Proof

There are \(\binom{6}{2}=15\) monomials of total degree four, so exactly \(2^{15}-1\) nonzero forms. Let \(S=\mathbf F_2[X,Y,Z]\), and \(S_d\) its degree-\(d\) forms. For each \(F\), form the homogeneous ideal \(I_F=(F,F_X,F_Y,F_Z)\). The curve is geometrically smooth exactly when \(I_F\) has no projective zero over the algebraic closure.

**Exact geometric smoothness criterion.** Consider the linear map
\[
\Phi_F:S_6\oplus S_7^{\oplus3}\longrightarrow S_{10},\qquad (A,B,C,D)\longmapsto AF+BF_X+CF_Y+DF_Z.
\]
Then \(C_F\) is geometrically smooth if and only if \(\operatorname{rank}\Phi_F=\dim S_{10}=66\). If the curve is singular, evaluation at a geometric singular point annihilates every element of \(I_F\), including its degree-ten subspace, so the rank is below 66. Conversely, assume smoothness. The degree-four part of \(I_F\), spanned by \(F\) and linear multiples of its cubic partial derivatives, has no common projective zero. Over the infinite algebraic closure, three sufficiently general degree-four members of this base-point-free linear system have no common projective zero: two intersect in finitely many points, and a third can avoid them. These three homogeneous forms generate an Artinian complete intersection of three quartics in three variables. Its quotient has Hilbert-series numerator \((1-t^4)^3\) over denominator \((1-t)^3\) and last nonzero graded degree \(3(4-1)=9\). Therefore its entire degree-ten part vanishes. The larger ideal \(I_F\) also contains all of \(S_{10}\), proving rank 66. The same conclusion holds after descent to \(\mathbf F_2\), since matrix rank is unchanged by scalar extension.

**Exact rational-bitangent criterion.** For any of the seven rational lines \(L\), choose two linearly independent rational vectors \(u,v\) spanning it. Write
\[
F(su+tv)=a_0s^4+a_1s^3t+a_2s^2t^2+a_3st^3+a_4t^4.
\]
In characteristic two, this binary quartic is the square of a quadratic over \(\overline{\mathbf F}_2\) if and only if \(a_1=a_3=0\); over \(\mathbf F_2\), the same characterization holds with rational square root. Thus each rational line contributes two independent-or-dependent *linear coefficient tests* on the 15 bits specifying \(F\). Separately, the seven rational point evaluations compute \(r(F)\) with seven further linear tests.

The first provided program enumerates every nonzero coefficient vector and applies the 66-row exact rank criterion. It enumerates all seven lines and all seven rational points by binary arithmetic, computing the full \((r,b)\)-table. For every specified rational-line subset it also records the number of quartics realizing that precise set. The output gives 10,920 smooth quartics and the table and incidence counts above. This finite enumeration is exhaustive, not a sample; the preceding lemmas justify the exhaustive tests over the algebraic closure.

Independently, the second program generates projective-coordinate orbits under a three-cycle of variables and an elementary transvection. These transformations generate the full 168-element group \(\operatorname{PGL}_3(\mathbf F_2)\). It obtains 279 orbits of nonzero quartic forms. For each representative it tests geometric smoothness using Gröbner bases of the quartic and its three derivatives on each of the three affine projective charts, instead of the rank-66 criterion. It finds exactly 78 smooth orbits, with weighted size 10,920. It then calculates rational points and even-contact lines by independent symbolic evaluations; the orbit-size-weighted joint distribution and concurrency incidences agree exactly with the table. Because both methods exhaust the same finite parameter set using independent smoothness tests, this supplies an independent check on each enumerative step without substituting experiments for the algebraic criterion.

## Verification

Two standalone files accompany this result: `bitangent_census.cpp` (C++17, no nonstandard libraries) and `bitangent_orbits.py` (Python 3 with SymPy). For example, compile and run the first with `g++ -std=c++17 -O2 bitangent_census.cpp -o bitangent_census && ./bitangent_census`, and run the second using `python3 bitangent_orbits.py`. The first prints the table, distribution, individual bitangent subsets, and witnesses; the second asserts the complete joint table, orbit totals, and concurrence conclusions. Both were run successfully with the reported data. All tests use exact finite-field algebra; no randomized, floating-point, or bounded-extension smoothness tests are used. The 78 projective orbit representatives are generated, not imported from an external table.

## Relationship to prior work

Markwig, Payne, and Shaw [1], first publicly available July 4, 2022, investigate arithmetic rationality of plane-quartic bitangents by tropical methods but work over Henselian valued fields whose residue characteristic is not two. The characteristic-two case here does not follow from their lifting theorems. Asgarli, Ghioca, and Yip [2] study rational point configurations on plane curves over finite fields, including low-degree quartics, but do not relate those configurations to the rational bitangent spectrum.

The strongest directly relevant foundational source is Nart and Ritzenthaler [3]. It gives a complete classification of smooth genus-three nonhyperelliptic curves over finite fields of characteristic two, explicitly relates geometric bitangents to 2-rank, and describes the Fano-plane configuration and descent data. Its results cover classification of abstract curve isomorphism classes and the possible geometric bitangent counts; these are **not** claimed here as new. Its Theorem 3.4 counts rational **points of the moduli strata**, not the \(\mathbf F_2\)-points on each individual curve. The weighted joint distribution of rational points *on curves* and individually rational even-contact lines, including the exact support exclusions and per-line-configuration multiplicities, does not appear in its stated results. Deriving the table from its normal models would require additional point and line calculations and orbit weights. Müller and Ritzenthaler [4] develop the invariant theory of ordinary quartics, not this joint distribution. Earlier global classifications enable alternative computations in principle and present a residual priority risk; the present claim is only the computed, fully explicit joint arithmetic incidence spectrum.

## Limitations

The proof concerns \(\mathbf F_2\) alone, and the frequencies are coordinate-equation counts; no asymptotic distribution over extension fields is claimed. An alternative derivation via existing complete normal-form classifications may exist, so the absence of an identical previously published table is not a proof of absolute novelty. The proof uses an exact exhaustive computation of 32,767 forms plus the algebraic smoothness and bitangency criteria; the code is part of the reproducibility evidence. No independent external audit or formal verification is asserted.

## References

[1] H. Markwig, S. Payne, K. Shaw, *Bitangents to plane quartics via tropical geometry: rationality, A1-enumeration, and real signed count*, arXiv:2207.01305 (first posted 2022-07-04). https://arxiv.org/abs/2207.01305

[2] S. Asgarli, D. Ghioca, C. H. Yip, *Plane curves giving rise to blocking sets over finite fields*, arXiv:2208.13299 (first posted 2022-08-28). https://arxiv.org/abs/2208.13299

[3] E. Nart, C. Ritzenthaler, *Non hyperelliptic curves of genus three over finite fields of characteristic two*, arXiv:math/0312366 (first posted 2003-12-18). https://arxiv.org/abs/math/0312366

[4] P. Müller, C. Ritzenthaler, *On the ring of invariants of ordinary quartics in characteristic 2*, arXiv:math/0405052 (first posted 2004). https://arxiv.org/abs/math/0405052
