# Normalized weak tiling already forces tiling in \(\mathbb F_2^4\)
## Finding
Let \(G=\mathbb F_2^4\). Suppose \(A\subset G\) is nonempty and there exists a function
\[
h:G\to\mathbb R_{\ge0}
\]
such that
\[
h(0)=1,\qquad 1_A*h=1_G.
\]
Then \(A\) tiles \(G\) by translations.

This is stronger than pd-flatness: no Fourier-positivity assumption on \(h\) is needed. Consequently \(\mathbb F_2^4\) is pd-flat.

The exact census of normalized sets \(0\in A\) gives \(32768\) subsets, split into \(46\) linear-equivalence classes. Exactly \(9\) classes tile and \(37\) do not. The normalized tiling sets occur only in sizes \(1,2,4,8,16\), with counts
\[
1,\ 15,\ 455,\ 1395,\ 1,
\]
respectively.

## Assumptions and scope
The group law on \(\mathbb F_2^4\) is written additively. A translational tiling \(A\oplus B=G\) means every element of \(G\) has a unique representation \(a+b\).

The weak complement here is normalized and nonnegative: \(h(0)=1\), \(h\ge0\), and \(1_A*h=1_G\). This is strictly weaker than the pd-tiling condition of Kiss--Matolcsi--Matolcsi--Somlai because no condition on \(\widehat h\) is assumed.

## Proof
Translate \(A\) so that \(0\in A\). Translation preserves both tiling and the existence of a normalized nonnegative weak complement.

If \(d=a-a'\ne0\) with \(a,a'\in A\), then nonnegativity and the convolution identity at \(a\) imply
\[
1=(1_A*h)(a)\ge h(0)+h(d)=1+h(d),
\]
so
\[
h(d)=0.
\]
Therefore every normalized nonnegative weak complement must solve the finite linear system
\[
h(0)=1,\qquad
\sum_{a\in A}h(x-a)=1\quad(x\in G),\qquad
h(d)=0\quad(d\in(A-A)\setminus\{0\}).
\]
All coefficients of this system are integers.

Now act on normalized subsets by \(\mathrm{GL}(4,2)\). Three elementary linear generators used in the checker generate a group of order
\[
(16-1)(16-2)(16-4)(16-8)=20160,
\]
hence all of \(\mathrm{GL}(4,2)\). Their action partitions the \(2^{15}=32768\) subsets containing \(0\) into exactly \(46\) orbits.

For each orbit representative, tiling is checked exactly by the standard difference-set criterion: \(A\oplus B=G\) is equivalent to
\[
|A||B|=16,\qquad (A-A)\cap(B-B)=\{0\}.
\]
There are \(9\) tiling orbits and \(37\) non-tiling orbits.

For each of the \(37\) non-tiling representatives, exact rational Gaussian elimination applied to the displayed weak-tiling system gives
\[
\operatorname{rank}(M_A\mid b_A)=\operatorname{rank}(M_A)+1.
\]
Thus the system has no real solution at all, hence no nonnegative solution. Linear automorphisms preserve the system, so no set in any non-tiling orbit can admit a normalized nonnegative weak complement.

Therefore every normalized nonnegative weak tile in \(\mathbb F_2^4\) is a translational tile.

## Verification
The accompanying `verify.py` uses only exact integer and rational arithmetic. It independently:
- generates \(\mathrm{GL}(4,2)\) from three elementary transformations and checks its order is \(20160\);
- partitions all \(32768\) normalized subsets into \(46\) orbits;
- finds exact tiling complements for every tiling orbit by the difference-set criterion;
- verifies that every non-tiling orbit representative has augmented rank exactly one larger than coefficient rank in the necessary weak-tiling system;
- recovers the normalized tiling counts \(1,15,455,1395,1\) at sizes \(1,2,4,8,16\).

It prints `VERIFY_OK`. The computation is exhaustive and exact; no floating-point feasibility decision is used.

## Relationship to prior work
Kiss, Matolcsi, Matolcsi and Somlai introduced pd-tiling for finite abelian groups and proved pd-flatness in dimensions \(1\) and \(2\), with partial structural results in dimension \(3\). Their higher-dimensional non-pd-flat discussion is based on known spectral non-tiles over odd prime fields. The binary four-dimensional case is not settled by those arguments.

The present result treats \(p=2,d=4\) and is stronger than pd-flatness because Fourier positivity of the weak complement is unnecessary.

Later work on weak tiling gives counterexamples in other settings and later binary spectral/tiling counterexamples occur in substantially higher dimensions; these do not imply a normalized weak non-tile in \(\mathbb F_2^4\).

## Limitations
The argument is a complete finite classification specific to \(\mathbb F_2^4\). It does not prove an analogous theorem for \(\mathbb F_2^d\) with \(d\ge5\), and it does not classify arbitrary unnormalized weak tilings. Literature non-detection is not a proof of absolute novelty.

## References
1. G. Kiss, D. Matolcsi, M. Matolcsi and G. Somlai, "Tiling and weak tiling in \((\mathbb Z_p)^d\)," arXiv:2212.05513, first posted 11 December 2022; later published in *Sampling Theory, Signal Processing, and Data Analysis* 22 (2024), Article 1.
2. G. Kiss, I. Londner, M. Matolcsi and G. Somlai, "A lonely weak tile," arXiv:2410.04948, first posted 7 October 2024.
