# Complete-monotonicity classification for consecutive exponential-derivative ratios

## Statement

For \(t>0\) and \(i\in\{0,1,2,\ldots\}\), define
\[
 f_i(t)=(-1)^i\frac{d^i}{dt^i}\frac1{e^t-1},
 \qquad
 g_i(t)=(-1)^i\frac{d^i}{dt^i}\frac1{1-e^{-t}},
\]
and the consecutive ratios
\[
 \mathcal F_i(t)=\frac{f_{i+1}(t)}{f_i(t)},
 \qquad
 \mathcal G_i(t)=\frac{g_{i+1}(t)}{g_i(t)}.
\]

Wei and Guo (2014) proved that every \(\mathcal F_i,\mathcal G_i\) is decreasing on
\((0,\infty)\), verified complete monotonicity in the first cases, and posed
Conjecture 12 asserting complete monotonicity for every index.

The conjecture has the following exact classification:
\[
\boxed{\;
\mathcal F_i \text{ and }\mathcal G_i \text{ are completely monotone on }(0,\infty)
\iff i\in\{0,1,2\}.
\;}
\]

In particular, the first previously untreated positive case \(i=2\) does satisfy
the conjecture, while every \(i\ge3\) fails it.

There is also a sharp logarithmic-complete-monotonicity boundary:
\[
\boxed{\;
\mathcal F_i \text{ and }\mathcal G_i \text{ are logarithmically completely monotone}
\iff i\in\{0,1\}.
\;}
\]

## Proof

Put \(z=e^{-t}\in(0,1)\). For \(i\ge1\),
\[
 f_i(t)=g_i(t)=\sum_{m=1}^{\infty}m^i z^m
 =\operatorname{Li}_{-i}(z),
\]
while \(f_0=z/(1-z)\) and \(g_0=1/(1-z)\). Hence
\[
 \mathcal G_i=\mathcal F_i\qquad(i\ge1).
\]

Let
\[
 A_n(z)=\sum_{k=0}^{n-1}\left\langle{n\atop k}\right\rangle z^k
\]
be the \(n\)-th Eulerian polynomial. The standard negative-integer
polylogarithm identity gives, for \(n\ge1\),
\[
 \operatorname{Li}_{-n}(z)=\frac{zA_n(z)}{(1-z)^{n+1}}.
\]
Therefore
\[
 \mathcal F_i(t)
 =\frac{A_{i+1}(z)}{(1-z)A_i(z)},\qquad i\ge1. \tag{1}
\]

### The three completely monotone cases

Directly,
\[
 \mathcal F_0(t)=\frac1{1-z}
 =1+\sum_{m\ge1}e^{-mt},
 \qquad
 \mathcal G_0(t)=\frac{z}{1-z}
 =\sum_{m\ge1}e^{-mt},
\]
and
\[
 \mathcal F_1(t)=\mathcal G_1(t)
 =\frac{1+z}{1-z}
 =1+2\sum_{m\ge1}e^{-mt}.
\]
These are Laplace transforms of positive discrete measures.

For \(i=2\),
\[
 \mathcal F_2(t)=\mathcal G_2(t)
 =\frac{1+4z+z^2}{1-z^2}
 =1+4\sum_{k\ge0}e^{-(2k+1)t}
   +2\sum_{k\ge1}e^{-2kt}. \tag{2}
\]
Thus \(i=2\) is also completely monotone.

### A right-half-plane pole for every \(i\ge3\)

Two classical facts about the Eulerian polynomials are used:

1. \(A_i\) has \(i-1\) simple zeros, all in \(( -\infty,0)\).
2. Eulerian-number symmetry gives
   \[
   A_i(z)=z^{i-1}A_i(1/z).
   \]

For every \(i\ge3\), these facts imply that \(A_i\) has a zero
\[
 \rho_i\in(-1,0).
\]
Indeed, reciprocal symmetry pairs every zero \(r\ne-1\) with \(1/r\). If the
degree \(i-1\) is even, the roots split into reciprocal pairs. If the degree is
odd, \(-1\) is the single unpaired root and the remaining roots split into
reciprocal pairs. Since \(i-1\ge2\), at least one pair exists, with one member
in \((-1,0)\).

There is no cancellation in (1). The Eulerian recurrence
\[
 A_{i+1}(z)=(1+iz)A_i(z)+z(1-z)A_i'(z)
\]
gives at a simple zero \(\rho_i\)
\[
 A_{i+1}(\rho_i)=\rho_i(1-\rho_i)A_i'(\rho_i)\ne0.
\]
Consequently (1), regarded as a meromorphic function of complex \(t\), has a
genuine pole at
\[
 t_i=-\log|\rho_i|+i\pi,
 \qquad \Re t_i=-\log|\rho_i|>0, \tag{3}
\]
because \(e^{-t_i}=\rho_i\).

Now recall the Hausdorff--Bernstein--Widder theorem. If \(h\) is completely
monotone on \((0,\infty)\), then
\[
 h(t)=\int_0^\infty e^{-ts}\,d\mu(s)
\]
for a nonnegative measure \(\mu\). Since the integral is finite at every
positive real \(t\), the same integral defines a holomorphic function on the
entire half-plane \(\Re t>0\): on a compact subset with
\(\Re t\ge\sigma>0\), it is dominated by \(e^{-\sigma s}\), whose
\(\mu\)-integral is finite.

If \(\mathcal F_i\) were completely monotone for some \(i\ge3\), its Laplace
representation would therefore give a holomorphic function on \(\Re t>0\).
On the positive real axis this function agrees with (1), so analytic
continuation forces agreement throughout the punctured right half-plane.
The pole (3) is impossible. Hence no \(i\ge3\) is completely monotone.
Since \(\mathcal G_i=\mathcal F_i\) for \(i\ge1\), this proves the stated
classification for both ratio families.

For the first failed index the obstruction is explicit:
\[
 A_3(z)=1+4z+z^2,\qquad
 \rho_3=-2+\sqrt3,
\]
so \(\mathcal F_3=\mathcal G_3\) has a pole at
\[
 t=\log(2+\sqrt3)+i\pi.
\]
A purely real-axis check is also available: exact symbolic differentiation
gives
\[
 \mathcal F_3^{(10)}(\log 500)<0,
\]
which directly violates complete monotonicity. The accompanying verification
script checks this exact rational sign.

### Logarithmic complete monotonicity

For \(i=0\), the two ratio functions are the two elementary functions
\(1/(1-e^{-t})\) and \(1/(e^t-1)\), whose logarithmic complete monotonicity is
standard and is also established in the 2014 source.

For \(i=1\),
\[
 -\frac{d}{dt}\log\mathcal F_1(t)
 =\frac{2e^{-t}}{1-e^{-2t}}
 =2\sum_{k\ge0}e^{-(2k+1)t},
\]
which is completely monotone; hence \(\mathcal F_1=\mathcal G_1\) is
logarithmically completely monotone.

For \(i=2\), the function
\[
 -(\log\mathcal F_2)'(t)
\]
has a genuine right-half-plane pole above the zero
\(\rho_3=-2+\sqrt3\) of the numerator \(A_3(e^{-t})\). If it were completely
monotone, the same Laplace-transform holomorphy argument would prohibit that
pole. Thus \(\mathcal F_2=\mathcal G_2\) is not logarithmically completely
monotone. For \(i\ge3\), failure of complete monotonicity already excludes
logarithmic complete monotonicity.

## Relation to the 2014 conjecture

Wei and Guo's Conjecture 12 asked for complete monotonicity of all the
consecutive derivative ratios. Their paper explicitly verifies only the
initial ratio cases before posing the conjecture. Formula (2) supplies the
next positive case, while the Eulerian-zero obstruction above shows that
\(i=3\) is the exact point where the conjecture begins to fail and that the
failure persists for every larger index.

The mechanism is structural rather than a single counterexample: the
reciprocal real-root geometry of Eulerian polynomials places a denominator
zero inside the unit disk, which becomes a forbidden singularity of a
putative Laplace transform in the right half-plane.

## Reproducibility

`artifacts/verify_eulerian_ratio.py` checks:

- the Eulerian-polynomial recurrence and the rational forms for \(i=1,2,3\);
- the positive discrete expansion for \(i=2\);
- the first forbidden pole \(\rho_3=-2+\sqrt3\);
- the exact inequality \(\mathcal F_3^{(10)}(\log 500)<0\);
- representative reciprocal negative roots of \(A_i\) for \(3\le i\le10\).

The symbolic checks are supplementary; the general proof is analytic.

## Originality status and limitations

To the best of our knowledge, the complete classification above and the
Eulerian-pole obstruction have not previously been stated for the Wei--Guo
ratio families. Searches included the exact 2014 title and DOI, Conjecture 12,
consecutive derivative-ratio terminology, the equivalent negative-integer
polylogarithm ratios, and Eulerian-polynomial formulations. Later literature
located in the search continues to cite or use the 2014 derivative-ratio
monotonicity, but no source located in this review resolves Conjecture 12.

The main residual originality risk is that the same classification may exist
under a different notation for ratios of negative-integer polylogarithms or
Eulerian rational functions. Classical ingredients used here--the
Hausdorff--Bernstein--Widder theorem, the negative-integer polylogarithm
formula, Eulerian-number reciprocity, and real-rootedness of Eulerian
polynomials--are not claimed as new.

## References

1. C.-F. Wei and B.-N. Guo, *Complete Monotonicity of Functions Connected
   with the Exponential Function and Derivatives*, Abstract and Applied
   Analysis 2014, Article ID 851213.
   https://doi.org/10.1155/2014/851213
2. NIST Digital Library of Mathematical Functions, §25.12, *Polylogarithms*.
   https://dlmf.nist.gov/25.12
3. NIST Digital Library of Mathematical Functions, §26.14, *Permutations:
   Order Notation* (Eulerian numbers and their symmetry).
   https://dlmf.nist.gov/26.14
4. C.-O. Chow, *New proofs of interlacing of zeros of Eulerian polynomials*,
   Journal of Mathematical Analysis and Applications 510 (2022), 126019.
   https://doi.org/10.1016/j.jmaa.2022.126019
5. D. V. Widder, *The Laplace Transform*, Princeton University Press, 1946.
