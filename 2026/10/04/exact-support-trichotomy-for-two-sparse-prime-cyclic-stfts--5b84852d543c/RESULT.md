# Exact support trichotomy for two-sparse prime cyclic STFTs
## Finding
Let \(p\ge5\) be prime and let \(f,g:\mathbb Z_p\to\mathbb C\) each have exactly two nonzero entries. Put
\[
A=\operatorname{supp}f=\{a_0,a_1\},\qquad
B=\operatorname{supp}g=\{b_0,b_1\},
\]
and define the unoriented difference sets
\[
\Delta(A)=\{\pm(a_1-a_0)\},\qquad
\Delta(B)=\{\pm(b_1-b_0)\}.
\]
For the short-time Fourier transform
\[
V_gf(x,\xi)=\sum_{y\in\mathbb Z_p} f(y)\overline{g(y-x)}e^{-2\pi i\xi y/p},
\]
there is an exact trichotomy.

If \(\Delta(A)\ne\Delta(B)\), then
\[
|\operatorname{supp}V_gf|=4p.
\]

If \(\Delta(A)=\Delta(B)\), label the two supports so that
\[
a_1-a_0=b_1-b_0=:d\ne0.
\]
Set
\[
R=-\frac{f(a_0)\overline{g(b_0)}}{f(a_1)\overline{g(b_1)}}.
\]
Then
\[
|\operatorname{supp}V_gf|=
\begin{cases}
3p-1,&R^p=1,\\
3p,&R^p\ne1.
\end{cases}
\]
All three values occur for every prime \(p\ge5\).

In particular, the Krahmer--Pfander--Rashkov two-sparse lower bound
\[
|\operatorname{supp}V_gf|\ge3p-1
\]
is sharp, and equality is characterized exactly by aligned support differences together with the displayed root-of-unity phase condition.

## Assumptions and scope
The group is the prime cyclic group \(\mathbb Z_p\), with \(p\ge5\). Both functions have support cardinality exactly two and all four support values are nonzero. The STFT normalization is irrelevant for support size; the displayed unnormalized convention is used throughout. The result does not classify higher sparse strata or composite cyclic groups.

## Proof
For each translation \(x\in\mathbb Z_p\), define
\[
h_x(y)=f(y)\overline{g(y-x)}.
\]
The row \(V_gf(x,\cdot)\) is the Fourier transform of \(h_x\). Its spatial support is
\[
\operatorname{supp}h_x=A\cap(x+B).
\]
Thus a row is nonzero exactly when \(x\in A-B\).

Suppose first that \(\Delta(A)\ne\Delta(B)\). The four differences \(a_i-b_j\), with \(i,j\in\{0,1\}\), are then distinct. Indeed, a collision between two differences using different indices on both sides would imply
\[
\pm(a_1-a_0)=\pm(b_1-b_0),
\]
contrary to the hypothesis. Hence \(|A-B|=4\), and every nonzero \(h_x\) is supported at a single point. The Fourier transform of a nonzero point mass is nonzero at all \(p\) frequencies, so four rows each contribute \(p\) support points. This gives
\[
|\operatorname{supp}V_gf|=4p.
\]

Now suppose \(\Delta(A)=\Delta(B)\), and relabel so that \(a_1-a_0=b_1-b_0=d\). Then
\[
A-B=\{a_0-b_1,\ a_0-b_0,\ a_1-b_0\},
\]
which has three distinct elements because \(p\) is odd and \(d\ne0\). At the two outer translations the intersection \(A\cap(x+B)\) has one point, so those two Fourier rows each have all \(p\) frequencies nonzero.

At the middle translation \(x_0=a_0-b_0=a_1-b_1\), one has
\[
h_{x_0}=c_0\,1_{\{a_0\}}+c_1\,1_{\{a_1\}},
\qquad
c_j=f(a_j)\overline{g(b_j)}\ne0.
\]
Writing \(\omega=e^{-2\pi i/p}\), its Fourier transform is
\[
\widehat h_{x_0}(\xi)=\omega^{\xi a_0}\bigl(c_0+c_1\omega^{\xi d}\bigr).
\]
Since \(d\ne0\) and \(p\) is prime, the map \(\xi\mapsto\omega^{\xi d}\) runs bijectively through all \(p\)-th roots of unity. Therefore the middle row has a zero if and only if
\[
-\frac{c_0}{c_1}=R
\]
is a \(p\)-th root of unity. If such a zero exists it is unique, again by bijectivity. Hence the middle row has support \(p-1\) when \(R^p=1\), and support \(p\) otherwise. Adding the two full outer rows yields the stated values \(3p-1\) and \(3p\).

All three values occur. Take aligned supports \(A=B=\{0,1\}\). With \(f(0)=f(1)=1\), \(g(0)=-1\), and \(g(1)=1\), one has \(R=1\), giving \(3p-1\). With all four values equal to \(1\), one has \(R=-1\), which is not a \(p\)-th root of unity for odd \(p\), giving \(3p\). Finally, for \(p\ge5\), the supports \(A=\{0,1\}\) and \(B=\{0,2\}\) have unequal unoriented differences, giving \(4p\).

## Verification
The accompanying `verify.py` independently constructs the STFT and checks the trichotomy for every pair of two-point supports for primes \(5,7,11,13\). It tests both the aligned generic-phase case and the aligned cancellation case, and it verifies the explicit witnesses for all three values. The script prints `VERIFY_OK`.

These finite computations are consistency checks only. The universal statement follows from the row-support argument and the elementary two-point Fourier calculation above.

## Relationship to prior work
Krahmer, Pfander, and Rashkov proved a general prime-cyclic STFT support lower bound. Specializing their Proposition 4.3 to two-sparse \(f\) and \(g\) gives
\[
|\operatorname{supp}V_gf|\ge3p-1.
\]
Their proof already decomposes the STFT by translation rows and invokes Cauchy--Davenport, but it does not classify equality in the two-sparse stratum or give the exact three-valued support spectrum for arbitrary primes. Their extended 2007 technical report displays finite support data for \(\mathbb Z_5\) and treats \(\mathbb Z_3\) separately, rather than stating the present all-prime classification.

Nicola later completely classified the global extremizers for the universal bound \(|\operatorname{supp}V_gf|\ge p\). That result concerns the bottom support level and does not imply the present classification at the two-sparse level, whose minimum is \(3p-1\).

Targeted searches for the exact values \(3p-1\), \(3p\), and \(4p\) in the two-sparse prime-cyclic STFT setting, and for equality cases of the Krahmer--Pfander--Rashkov bound, found no covering theorem.

## Limitations
The classification is restricted to two-sparse pairs on prime cyclic groups. No claim is made for support sizes larger than two, for composite cyclic groups, or for quantitative stability near the three support levels. Literature searches cannot exclude an unindexed equivalent formulation.

## References
1. F. Nicola, "The uncertainty principle for the short-time Fourier transform on finite cyclic groups: cases of equality," arXiv:2204.14176, first posted 29 April 2022; Journal of Functional Analysis 284 (2023), 109924.
2. F. Krahmer, G. E. Pfander, and P. Rashkov, "Uncertainty in time-frequency representations on finite Abelian groups and applications," arXiv:math/0611493; Applied and Computational Harmonic Analysis 25 (2008), 209--225.
3. F. Krahmer, G. E. Pfander, and P. Rashkov, "Support size conditions for time-frequency representations on finite Abelian groups," Technical Report 13, Jacobs University Bremen, 2007.
