# Arithmetic safety for Gaussian-derivative Gabor frames

## Finding

Let
\[
\phi(t)=e^{-\pi t^2}
\]
and, for an integer \(m\ge0\), let
\[
g_m=\phi^{(m)}.
\]
For \(a,b>0\), put
\[
\delta=ab.
\]
Assume
\[
0<\delta<1.
\]

If \(\delta\) is irrational, then
\[
\mathcal G(g_m,a\mathbb Z\times b\mathbb Z)
\]
is a frame for \(L^2(\mathbb R)\).

If
\[
\delta=\frac pq
\]
in lowest terms and
\[
q-p>m,
\]
then
\[
\mathcal G(g_m,a\mathbb Z\times b\mathbb Z)
\]
is again a frame.

Equivalently, a subcritical failure of the frame property can occur only at a rational lattice product
\[
\delta=\frac pq
\]
whose denominator deficit satisfies
\[
q-p\le m.
\]

For \(m=0\), this recovers the familiar fact that the Gaussian generates a frame at every rectangular lattice with \(ab<1\). For \(m=1\), it recovers the arithmetic content of the exact first-Hermite frame-set theorem: the only possible subcritical failures have
\[
\delta=\frac{q-1}{q}.
\]

## Assumptions and scope

The Gabor system is
\[
\mathcal G(g,a\mathbb Z\times b\mathbb Z)
=
\{M_{kb}T_{na}g:k,n\in\mathbb Z\}.
\]
The theorem concerns derivatives of the Gaussian
\[
g_m=\frac{d^m}{dt^m}e^{-\pi t^2}.
\]
For \(m\ge2\), these windows are polynomial-times-Gaussian functions but are not, with this fixed Gaussian scale, the standard normalized Hermite functions appearing in the usual higher-Hermite frame-set problem.

The conclusion for \(m\ge2\) is sufficient rather than exact. It excludes every irrational subcritical product and every reduced rational product whose deficit \(q-p\) exceeds \(m\), but it does not decide all remaining rational products with \(q-p\le m\).

## Proof

The proof extends the Wronskian-amplification mechanism used for the first Hermite function.

First reduce a general rectangular lattice to frequency step one. Let
\[
(D_bf)(t)=b^{-1/2}f(t/b).
\]
Then
\[
D_bM_{kb}T_{na}
=
M_kT_{n\delta}D_b,
\qquad
\delta=ab.
\]
If
\[
\phi_\beta(t)=e^{-\pi t^2/\beta},
\qquad
\beta=b^2,
\]
then
\[
D_bg_m
=
b^{m-1/2}\phi_\beta^{(m)}.
\]
Multiplication of the window by a nonzero scalar does not affect the frame property, so it is enough to consider
\[
\mathcal G(\phi_\beta^{(m)},\delta\mathbb Z\times\mathbb Z).
\]

The window \(\phi_\beta^{(m)}\) belongs to the Wiener amalgam class used in the semi-regular Gabor criterion and has stable integer shifts. Indeed,
\[
\widehat{\phi_\beta^{(m)}}(\xi)
=
(2\pi i\xi)^m\sqrt{\beta}\,e^{-\pi\beta\xi^2},
\]
and the periodized square modulus
\[
\sum_{k\in\mathbb Z}
\left|
\widehat{\phi_\beta^{(m)}}(\xi+k)
\right|^2
\]
is continuous, one-periodic, and strictly positive. Hence it has a positive minimum.

Suppose now that the Gabor system is not a frame. The semi-regular Gabor characterization used in the source then yields a translate
\[
x_*+\delta\mathbb Z
\]
and a nonzero bounded coefficient sequence
\[
c=(c_k)_{k\in\mathbb Z}
\]
such that
\[
\sum_{k\in\mathbb Z}
c_k\phi_\beta^{(m)}(x_*+n\delta-k)
=
0
\qquad(n\in\mathbb Z).
\]
Define the Gaussian shift-invariant entire function
\[
F(z)
=
\sum_{k\in\mathbb Z}
c_ke^{-\pi(z-k)^2/\beta}.
\]
Then
\[
F^{(m)}(x_*+n\delta)=0
\qquad(n\in\mathbb Z).
\]

We need a higher-order version of the source's Wronskian multiplicity lemma.

Let \(N>m\), and let
\[
f_0,\ldots,f_{N-1}
\]
be holomorphic near a point \(\lambda\), with
\[
f_j^{(m)}(\lambda)=0
\qquad(0\le j<N).
\]
Let
\[
W=\det\bigl(f_j^{(r)}\bigr)_{0\le r,j<N}
\]
be their Wronskian. Then
\[
\operatorname{ord}_\lambda W\ge N-m
\]
unless \(W\equiv0\).

To prove this, differentiate the determinant \(s\) times. Every term in \(W^{(s)}(\lambda)\) is a generalized Wronskian determinant whose row orders are
\[
r_k=k+\alpha_k,
\qquad
\alpha_k\ge0,
\qquad
\sum_{k=0}^{N-1}\alpha_k=s.
\]
If two row orders coincide, that determinant vanishes. If they are distinct and none equals \(m\), then their sum is at least the sum of the \(N\) smallest nonnegative integers that avoid \(m\):
\[
0+\cdots+(m-1)+(m+1)+\cdots+N.
\]
This is
\[
\frac{N(N-1)}2+(N-m).
\]
But the actual row-order sum is
\[
\frac{N(N-1)}2+s.
\]
Therefore, if
\[
s<N-m,
\]
distinct row orders must include \(m\), and the corresponding row is zero at \(\lambda\). Hence
\[
W^{(s)}(\lambda)=0
\qquad(0\le s<N-m),
\]
which proves the multiplicity claim.

Apply this lemma to the translates
\[
F_j(z)=F(z-j\delta),
\qquad
0\le j<N.
\]
At every point \(x_*+n\delta\), all \(F_j^{(m)}\) vanish. If the characters
\[
e^{2\pi i j\delta},
\qquad
0\le j<N,
\]
are pairwise distinct, the source's translate-independence argument shows that the Wronskian is nonzero.

The automorphy calculation in the source is independent of the derivative order. After the same rescaling, this nonzero Wronskian is again a Gaussian shift-invariant entire function with bounded coefficients. Its real zero lattice has spacing \(N\delta\), and every such zero has multiplicity at least \(N-m\). The sharp Gaussian zero-density theorem therefore gives
\[
\frac{N-m}{N\delta}\le1.
\]
Equivalently,
\[
\delta\ge1-\frac mN.
\]

If \(\delta\) is irrational, the characters are pairwise distinct for every \(N>m\). Letting \(N\to\infty\) gives
\[
\delta\ge1,
\]
contrary to the subcritical assumption. Thus every irrational \(\delta<1\) gives a frame.

Now let
\[
\delta=\frac pq
\]
in lowest terms. If \(q\le m\), then automatically
\[
q-p\le q-1<m.
\]
If \(q>m\), choose \(N=q\). The \(q\) characters are pairwise distinct, and the density inequality gives
\[
\frac{q-m}{p}\le1.
\]
Hence
\[
p\ge q-m,
\]
or
\[
q-p\le m.
\]
Therefore non-frame behavior can occur only at the rational products stated in the finding.

## Verification

The argument is analytic.

The critical new combinatorial step is the exact multiplicity count for the higher-order Wronskian. The baseline row orders are
\[
0,1,\ldots,N-1,
\]
whose sum is
\[
N(N-1)/2.
\]
Among \(N\) distinct nonnegative row orders avoiding \(m<N\), the minimal possible set is
\[
\{0,1,\ldots,N\}\setminus\{m\},
\]
whose sum exceeds the baseline by exactly
\[
N-m.
\]
This is why common \(m\)-th derivative zeros produce Wronskian zeros of multiplicity \(N-m\).

All remaining ingredients are used in the same logical direction as in the primary source: non-frame behavior produces a bounded-coefficient Gaussian shift-invariant function with prescribed derivative zeros; distinct translation characters imply a nonzero Wronskian; automorphy keeps the rescaled Wronskian in the Gaussian shift-invariant class; and the sharp zero-density theorem bounds its weighted real-zero density.

The stable-shift condition for \(\phi_\beta^{(m)}\) is verified directly from its Fourier transform. The periodized squared modulus cannot vanish because, for any real \(\xi\), at least one integer translate \(\xi+k\) is nonzero.

No finite experiment, numerical fit, or truncated computation is used to prove the theorem.

## Relationship to prior work

Faulhuber and Petersen determine the complete rectangular frame set of the first Hermite function. Their proof turns non-frame behavior into the existence of a bounded-coefficient Gaussian shift-invariant entire function whose first derivative vanishes on a lattice, and then amplifies those common critical points with Wronskians. The result here changes the window from the first derivative of the Gaussian to an arbitrary fixed derivative and proves the corresponding higher-order multiplicity law
\[
N-1\longrightarrow N-m.
\]
That produces the new denominator-deficit condition
\[
q-p\le m.
\]

Gröchenig, Romero, and Stöckler prove sharp density theorems for sampling a full derivative jet in Gaussian-type shift-invariant spaces and derive multi-window Gabor results for a basis of polynomial differential operators. Those theorems concern simultaneous access to several derivatives or several windows. They do not state the single-window arithmetic conclusion for the lone window \(\phi^{(m)}\).

The standard higher-Hermite frame-set literature concerns
\[
h_n(t)
=
c_n(-1)^ne^{\pi t^2}
\frac{d^n}{dt^n}e^{-2\pi t^2}.
\]
For \(n\ge2\), this is not a scalar multiple of
\[
\frac{d^n}{dt^n}e^{-\pi t^2}.
\]
Accordingly, known higher-Hermite obstructions do not imply the present Gaussian-derivative statement.

Searches using the aliases “Gaussian derivative”, “derivative of Gaussian”, “Hermitian wavelet”, “Wronskian deficit”, “single derivative sampling”, and rational Gabor density did not locate a theorem giving the irrational safety statement or the condition \(q-p\le m\).

## Limitations

For \(m\ge2\), the theorem does not determine the full frame set. The remaining rational products satisfying
\[
q-p\le m
\]
may contain both frame and non-frame points; no converse is claimed.

The argument is specific to rectangular lattices and to derivatives of a Gaussian. It does not establish an analogous arithmetic classification for arbitrary polynomial-times-Gaussian windows.

The proof uses the sharp real-zero density theorem for Gaussian shift-invariant entire functions. Extending the method to generators without a comparable zero-density theorem requires additional ideas.

## References

1. M. Faulhuber and P. Petersen, *The frame set of the first Hermite function*, arXiv:2609.02610, first public 2026.
2. K. Gröchenig, J. L. Romero, and J. Stöckler, *Sharp Results on Sampling with Derivatives in Shift-Invariant Spaces and Multi-Window Gabor Frames*, Constructive Approximation 51 (2020), 1--25.
3. M. Faulhuber, I. Shafkulovska, and I. Zlotnikov, *On the Frame Property of Hermite Functions and Exploration of their Frame Sets*, Journal of Fourier Analysis and Applications 31 (2025), Article 21.
