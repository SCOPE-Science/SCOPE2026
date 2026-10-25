# The anticanonical curve-degree spectrum of the twelve-dimensional dyadic Richardson variety

## Finding

Let \(v=(1,5,3,7,2,6,4,8)\) and \(w=(8,4,6,2,7,3,5,1)\), in one-line notation, and let \(X=\overline{R}_{v,w}\subset\operatorname{Fl}(\mathbb C^8)\) be the closed Richardson variety. The associated Bruhat interval is the twelve-dimensional dyadic hypercube. The variety \(X\) is a smooth projective toric twelvefold. The **complete spectrum of anticanonical degrees** of its torus-invariant irreducible curves is

\[
\begin{array}{c|rrrrr}
(-K_X\cdot C)&-2&0&2&4&6\\
\hline
\#\{C\}&512&4096&15360&4096&512.
\end{array}
\]

Consequently, \(-K_X\) is **not nef**, and the minimum anticanonical degree of a torus-invariant curve is precisely \(-2\). There are \(12\cdot 2^{11}=24{,}576\) torus-invariant irreducible curves in total. This is the next dyadic example after the four-dimensional case; it locates the first failure of anticanonical nefness among the first three members of this natural sequence.

## Assumptions and scope

All varieties and intersection numbers are over \(\mathbb C\). Write \(s_i=(i,i+1)\) for the simple transpositions in \(S_8\), indexed from \(1\) through \(7\). A torus-invariant curve is a one-dimensional orbit closure of the **intrinsic twelve-dimensional dense torus** of \(X\). This is not the seven-dimensional maximal diagonal torus of \(\operatorname{SL}_8\), although the latter acts and can be used to compute weights.

The smoothness, existence of an intrinsic toric structure, and identification with a skew-sub-Bott–Samelson tower are established in the cited literature. The claim is the evaluated numerical curve-degree spectrum and its nefness consequence; it does not classify all effective curves individually or any higher dyadic member.

## Proof

**1. The magic word and fixed points.** The 2026 magic-word construction supplies the reduced word

\[
Q=(s_1,s_3,s_2,s_1,s_3,s_5,s_7,s_6,s_5,s_7,
 s_4,s_3,s_5,s_2,s_4,s_6,s_1,s_3,s_5,s_7)
\]

for \(w\). Its unique subword with product \(v\) uses positions \(3,8,11,12,13,14,15,16\) (one-based indexing). The complementary \(12\) free positions, in increasing order, are

\[
F=(1,2,4,5,6,7,9,10,17,18,19,20).
\]

The skew-sub-Bott–Samelson description sets the coordinates indexed by the mandatory positions to zero in every standard chart and leaves the free coordinates as successive \(\mathbb P^1\)-bundle coordinates. Hence the fixed points are indexed by \(b\in\{0,1\}^{12}\); a chosen simple reflection is used at mandatory positions and at free positions where its bit is one. The toric moment polytope has the combinatorics of a twelve-cube, so each pair of vertices differing in exactly one free bit corresponds to one torus-invariant irreducible curve. There are exactly \(12\cdot2^{11}\) such curves.

**2. Tangent-weight formula.** Let \(r_j\) be the reflection or identity selected at word position \(j\), let \(i_j\) be the simple-root index of \(Q_j\), and write \(\alpha_i=e_i-e_{i+1}\) in the character lattice of the diagonal torus. In a Bott–Samelson chart, the tangent weight for a free position \(j\) at the corresponding fixed point is

\[
\chi_j(b)=-r_1r_2\cdots r_j(\alpha_{i_j}).
\]

Indeed, the coordinate at position \(j\) is a root-group parameter with character \(-r_j\alpha_{i_j}\), conjugated by the preceding chosen Weyl representatives. This also follows directly from the displayed Bott–Samelson chart parametrization in the source. The coordinates forced to vanish have no tangent directions in \(X\). Therefore the equivariant restriction of \(c_1(T_X)=-K_X\) at \(b\) is \(S(b)=\sum_{j\in F}\chi_j(b)\).

**3. Curve degrees from the two endpoints.** If \(b_k=0\) and \(b'=b\oplus 2^{k-1}\) (with free coordinates numbered \(1,\ldots,12\)), then the invariant curve \(C_{b,k}\) joins \(b\) to \(b'\). Its tangent character at \(b\) is \(\chi_{F_k}(b)\), and the standard equivariant degree formula on \(\mathbb P^1\) gives

\[
S(b)-S(b')=(-K_X\cdot C_{b,k})\,\chi_{F_k}(b).
\]

This is an equality of eight-coordinate character vectors modulo the diagonal character, not a numerical interpolation at a single torus element. The attached program computes these characters as integer vectors, verifies this equality componentwise for **every** edge, and obtains the complete table below. The table groups free positions with identical degree distributions; each position has \(2^{11}=2048\) edges.

| Free-coordinate positions (in order within \(F\)) | Degree \(-2\) | Degree \(0\) | Degree \(2\) | Degree \(4\) | Degree \(6\) |
|---|---:|---:|---:|---:|---:|
| \(1,2,5,6\) (each) | 128 | 512 | 768 | 512 | 128 |
| \(3,4,7,8\) (each) | 0 | 512 | 1024 | 512 | 0 |
| \(9,10,11,12\) (each) | 0 | 0 | 2048 | 0 | 0 |
| **Total** | **512** | **4096** | **15360** | **4096** | **512** |

For a direct negative witness, use the free-bit mask \(b=516\) (bits numbered from zero), toggle its first free bit, and obtain \(b'=517\). The endpoint permutations, in one-line notation, are \((3,5,7,1,2,6,4,8)\) and \((3,5,7,2,1,6,4,8)\). The character difference is exactly \(S(b)-S(b')=-2\chi_{F_1}(b)\), proving \((-K_X\cdot C_{b,1})=-2\) without relying on a counting estimate. Since a nef divisor has nonnegative intersection with every irreducible curve, \(-K_X\) cannot be nef.

## Verification

Execute `python3 verify_dyadic_richardson.py` using Python 3 and its standard library; the expected terminal line is `VERIFY_OK`. The program enumerates all \(\binom{20}{8}\) eight-position candidate subwords and identifies the unique mandatory subword, then computes the character vectors of the \(4096\) fixed points and all \(24576\) edges. For each edge it verifies equality of the two tangent-edge characters up to sign and componentwise equality of the equivariant Chern difference with an integer multiple of the tangent weight. It verifies each row of the table, the totals, and the explicit negative witness. No finite sample is extrapolated: these are all fixed points and all invariant edges of this specified twelve-dimensional cube.

## Relationship to prior work

Ellenberg, Libedinsky, Plaza, Simental, and Williamson introduced the dyadic hypercube intervals. Gorsky, Kim, and Sherman-Bennett established the toric Richardson structure and supplied explicit moment-polytope descriptions, including the twelve-dimensional example. Elek's magic-word construction provides a convenient Bott–Samelson tower and explicit word for this example. These are essential premises, not new results claimed here. The computed anticanonical degree histogram, including the negative tail and its exact multiplicity, is not stated in those inspected sources. A moment-polytope description determines the answer in principle, but extracting this evaluated intersection-theoretic invariant is a separate calculation. Earlier records describing the four-dimensional member's weak-Fano property do not imply the twelve-dimensional member's non-nefness or its complete degree spectrum.

## Limitations

The calculation treats exactly the dyadic twelvefold in \(\operatorname{Fl}(\mathbb C^8)\); it makes no claim that all higher dyadic Richardsons fail to have nef anticanonical class. The spectrum describes invariant curves of the intrinsic torus, rather than a classification of all irreducible curves. A negative invariant curve suffices to refute nefness. Although the inspected sources do not state the evaluated spectrum, their explicit toric data could permit an equivalent derivation elsewhere; undiscovered prior coverage remains a literature-priority risk. Independent mathematical verification has not been performed.

## References

1. J. Ellenberg, N. Libedinsky, D. Plaza, J. Simental, and G. Williamson, *Bruhat intervals that are large hypercubes*, arXiv:2601.01235v1 (first public version, 2026-01-03).
2. E. Gorsky, S. Kim, and M. Sherman-Bennett, *Unexpected toric Richardson varieties*, arXiv:2603.29260v1 (2026-03-31), especially Theorems 1.2 and 1.3 and Example 5.25.
3. B. Elek, *Hypercube Richardson varieties from magic words*, arXiv:2610.22730v1 (2026-10-15), especially Theorem 2.19, Theorem 4.1 and Example 4.2.
