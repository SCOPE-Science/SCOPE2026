# A Pólya–Bessel zero-free strip for Fourier bipyramids

## Statement

For \(d\ge 3\), put
\[
\ell=d-1,\qquad \nu=\frac{\ell}{2}=\frac{d-1}{2},
\]
and define
\[
H_\nu(z):=(2\nu-1)J_{\nu-1}(z)-zJ_\nu(z).
\]
Let \(r_d\) be the least positive zero of \(H_\nu\). Such a zero exists: \(H_\nu\) is positive for sufficiently small positive \(z\), while at \(j_{\nu-1,1}\) it is negative by the standard interlacing
\(j_{\nu-1,1}<j_{\nu,1}\).

Consider the balanced bipyramid
\[
\Omega_{\alpha,d}:=\{(x,y)\in\mathbb R\times\mathbb R^{d-1}: |x|+\alpha |y|<1\}.
\]
Using the notation of Gómez-Serrano, Levitin, Platt and Polterovich,
\[
\widehat{\chi_{\Omega_{\alpha,d}}}(u,\eta)
=\alpha^{-\ell}F_\ell\!\left(u,\frac{|\eta|}{\alpha}\right),
\]
where
\[
F_\ell(u,s)
=2\int_0^1\cos(ux)(1-x)^\ell
B_\ell(s(1-x))\,dx,
\qquad
B_\ell(t)=(2\pi)^\nu\frac{J_\nu(t)}{t^\nu}.
\]

**Theorem.** For every \(d\ge3\),
\[
F_{d-1}(u,s)>0
\qquad
\text{for every }u\in\mathbb R,\quad 0\le s\le r_d.
\]
Consequently,
\[
\boxed{\ \kappa(\Omega_{\alpha,d})\ge \alpha r_d\ }.
\]

The equal-volume ball satisfies
\[
\kappa(\Omega_{\alpha,d}^*)
=
j_{d/2,1}
\left(\frac{d\omega_d}{2\omega_{d-1}}\right)^{1/d}
\alpha^{(d-1)/d}.
\]
Therefore the bipyramid is a rigorous counterexample to the equal-volume-ball inequality whenever
\[
\boxed{\ 
\alpha>A_d:=
\frac{d\omega_d}{2\omega_{d-1}}
\left(\frac{j_{d/2,1}}{r_d}\right)^d
\ }.
\]

In dimension \(3\),
\[
H_1(z)=J_0(z)-zJ_1(z),\qquad
r_3=1.2557837117945935\ldots,
\]
and
\[
A_3=91.6248852570052\ldots.
\]
The decimal values are not needed for the rigorous fixed-parameter conclusion below.

**Corollary.**
\[
\boxed{\ \kappa(\Omega_{100,3})>\kappa(\Omega_{100,3}^*)\ }.
\]
Thus the \((\alpha,d)=(100,3)\) numerical counterexample reported in the motivating paper admits a purely analytic certification, without two-variable interval arithmetic.

## Proof

### 1. Convexity of the one-dimensional kernel

For \(s>0\), define on \(0\le x\le1\)
\[
q_s(x):=(1-x)^\ell B_\ell(s(1-x)).
\]
Write \(t=1-x\) and
\[
g_s(t):=t^\ell B_\ell(st)
=(2\pi)^\nu s^{-\nu}t^\nu J_\nu(st).
\]
The Bessel identities
\[
\frac{d}{dz}(z^\nu J_\nu(z))=z^\nu J_{\nu-1}(z),
\qquad
J_{\nu-2}(z)+J_\nu(z)=\frac{2(\nu-1)}{z}J_{\nu-1}(z)
\]
give
\[
g_s''(t)
=(2\pi)^\nu s^{1-\nu}t^{\nu-1}
\bigl((2\nu-1)J_{\nu-1}(st)-stJ_\nu(st)\bigr)
\]
and hence
\[
g_s''(t)
=(2\pi)^\nu s^{1-\nu}t^{\nu-1}H_\nu(st).
\]

By definition of \(r_d\), \(H_\nu(z)>0\) for \(0<z<r_d\) and
\(H_\nu(r_d)=0\). Hence, for \(0<s\le r_d\), \(q_s''(x)\ge0\) on
\([0,1]\), with strict positivity in the interior except possibly at an endpoint.
Moreover, since \(\ell\ge2\),
\[
q_s(1)=q_s'(1)=0.
\]
Extending \(q_s\) by zero for \(x\ge1\) therefore gives a nonnegative convex \(C^1\) function on \([0,\infty)\).

For \(s=0\),
\[
q_0(x)=\omega_\ell(1-x)^\ell\quad(0\le x\le1),
\]
again extended by zero, and the same convexity and endpoint properties hold.

### 2. Strict positivity of the cosine transform

Set
\[
w_s(x):=-q_s'(x).
\]
Convexity and the endpoint conditions imply that \(w_s\ge0\), that \(w_s\) is nonincreasing, and that it is strictly decreasing on the nonzero part of its support. For \(u>0\), integration by parts gives
\[
\int_0^\infty q_s(x)\cos(ux)\,dx
=
\frac1u\int_0^\infty w_s(x)\sin(ux)\,dx.
\]
Put \(\delta=\pi/u\). Pairing consecutive positive and negative half-waves yields
\[
\int_0^\infty w_s(x)\sin(ux)\,dx
=
\sum_{k\ge0}
\int_{2k\delta}^{(2k+1)\delta}
\bigl(w_s(x)-w_s(x+\delta)\bigr)\sin(ux)\,dx.
\]
Every term is nonnegative, and the first is strictly positive because \(w_s\) is not constant on its support. Therefore
\[
\int_0^\infty q_s(x)\cos(ux)\,dx>0.
\]
The case \(u<0\) follows by evenness, and \(u=0\) is immediate from \(q_s\not\equiv0\). Since \(q_s\) is supported on \([0,1]\),
\[
F_\ell(u,s)=2\int_0^\infty q_s(x)\cos(ux)\,dx>0.
\]
This proves the zero-free strip.

This positivity mechanism is the classical convex-kernel criterion for cosine transforms (often associated with Pólya); the argument above is included to make the application self-contained.

### 3. From the strip to a bipyramid threshold

Every real Fourier zero of \(\Omega_{\alpha,d}\) corresponds to a zero
\(F_{d-1}(u,|\eta|/\alpha)=0\). The theorem therefore forces
\[
|\eta|/\alpha>r_d.
\]
In particular every zero has Euclidean norm at least \(\alpha r_d\), so
\[
\kappa(\Omega_{\alpha,d})\ge\alpha r_d.
\]

The bipyramid volume is
\[
|\Omega_{\alpha,d}|=\frac{2\omega_{d-1}}{d}\alpha^{-(d-1)}.
\]
Thus the equal-volume ball has radius
\[
R_{\alpha,d}
=
\left(\frac{2\omega_{d-1}}{d\omega_d}\right)^{1/d}
\alpha^{-(d-1)/d},
\]
and its first Fourier zero has radius
\[
\kappa(\Omega_{\alpha,d}^*)
=
\frac{j_{d/2,1}}{R_{\alpha,d}}.
\]
Comparing with \(\alpha r_d\) gives the stated sufficient threshold \(A_d\).

### 4. A fully elementary certification at \((\alpha,d)=(100,3)\)

For \(d=3\),
\[
H_1(z)=J_0(z)-zJ_1(z).
\]
On \(0\le z\le5/4\), the alternating series imply
\[
J_0(z)>1-\frac{z^2}{4}>0,\qquad
J_1(z)>\frac z2-\frac{z^3}{16}>0.
\]
Since
\[
H_1'(z)=-J_1(z)-zJ_0(z)<0,
\]
it is enough to check \(H_1(5/4)>0\). The exact alternating expansion
\[
H_1(z)=
\sum_{m=0}^\infty
(-1)^m\frac{2m+1}{(m!)^2}
\left(\frac{z^2}{4}\right)^m
\]
has decreasing term magnitudes from \(m=1\) onward at \(z=5/4\). Truncating after \(m=3\) gives the rigorous lower bound
\[
H_1(5/4)>
1-\frac{75}{64}
+\frac{3125}{16384}
-\frac{109375}{9437184}
=
\frac{68609}{9437184}>0.
\]
Hence
\[
r_3>\frac54.
\]

Also
\[
J_{3/2}(z)
=
\sqrt{\frac{2}{\pi z}}
\left(\frac{\sin z}{z}-\cos z\right),
\]
so its first positive zero \(j_{3/2,1}\) is the unique root of \(\tan z=z\)
in \((\pi,3\pi/2)\). At \(z_0=23/5\), write
\[
y=\frac{3\pi}{2}-z_0.
\]
Using the elementary bounds \(3.14<\pi<22/7\) gives
\(0<y<4/35\). Since
\[
\tan y<\frac{y}{1-y^2/2}
<
\frac{140}{1217}<\frac5{23},
\]
we have \(z_0\tan y<1\), equivalently
\[
\sin z_0-z_0\cos z_0<0.
\]
The same expression is positive at \(z=\pi\), hence
\[
j_{3/2,1}<\frac{23}{5}.
\]

Finally, in dimension \(3\),
\[
\frac{3\omega_3}{2\omega_2}=2,
\]
so
\[
A_3=2\left(\frac{j_{3/2,1}}{r_3}\right)^3
<
2\left(\frac{23/5}{5/4}\right)^3
=
\frac{1557376}{15625}
=
99.672064<100.
\]
Therefore \(\alpha=100>A_3\), proving the corollary.

## Context and comparison with prior work

Gómez-Serrano, Levitin, Platt and Polterovich prove that for every \(d\ge3\) there exists some \(\sigma_d>0\) such that
\[
F_{d-1}(u,s)>0\qquad(u\in\mathbb R,\ 0\le s\le\sigma_d),
\]
which yields sufficiently elongated bipyramid counterexamples. They explicitly note that quantitative constants can in principle be extracted from their proof but do not record them. They also report non-rigorous values at \(\alpha=100\) and leave rigorous certification for a prescribed pair \((\alpha,d)\) to future work via uniform interval bounds over a two-dimensional region.

The theorem above supplies a different, one-dimensional structural certificate:
the strip width is the first positive zero of an explicit Bessel combination.
In particular it rigorously certifies the paper's \((100,3)\) example analytically.

The general cosine-transform positivity principle for convex kernels is classical; see Tuck (2006). The new point here is the Bessel derivative identity for the bipyramid slice kernel, which converts the current Fourier-zero problem into the sign of \(H_\nu\).

## Limitations

- The bound \(\kappa(\Omega_{\alpha,d})\ge\alpha r_d\) is a lower bound; it does not determine the actual nearest Fourier zero.
- The threshold \(A_d\) is sufficient, not claimed optimal.
- Loss of convexity of the slice kernel beyond \(r_d\) does not imply the appearance of a Fourier zero there.
- The elementary fixed-parameter certification above is given for \((\alpha,d)=(100,3)\); the general theorem nevertheless gives an explicit sufficient threshold in every \(d\ge3\).
- The motivating preprint is very recent, so unindexed or unpublished parallel work remains a residual originality risk.

## References

1. J. Gómez-Serrano, M. Levitin, D. Platt, I. Polterovich, *An isoperimetric problem for Fourier zeros of centrally symmetric convex bodies*, arXiv:2609.10517 (2026). https://arxiv.org/abs/2609.10517
2. E. O. Tuck, *On Positivity of Fourier Transforms*, Bull. Aust. Math. Soc. 74 (2006), 133–138. https://doi.org/10.1017/S0004972700047511
3. NIST Digital Library of Mathematical Functions, §§10.6 and 10.21 (Bessel recurrences, derivatives, and zero interlacing). https://dlmf.nist.gov/10.6 and https://dlmf.nist.gov/10.21
