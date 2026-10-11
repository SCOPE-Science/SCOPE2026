# Exact radial Schwarzian profile of the Lehtinen witness family

## Finding

For
\[
\alpha>1,
\]
consider the harmonic mapping
\[
f_\alpha=h_\alpha+\overline{g_\alpha},
\]
where
\[
h_\alpha(z)
=
\frac{1-(1-z)^\alpha}{\alpha}
\]
and
\[
g_\alpha(z)
=
\frac{1-(1+\alpha z)(1-z)^\alpha}
{\alpha(1+\alpha)}.
\]
This is the non-injective family used in the recent harmonic analogue of Lehtinen's theorem.

For
\[
0\le r<1,
\]
define its radial Schwarzian profile by
\[
M_\alpha(r)
=
\max_{|z|=r}
(1-r^2)^2
|S_{f_\alpha}(z)|.
\]
Then
\[
M_\alpha(r)
=
\frac{\alpha^2-1}{2}(1+r)^2
+
(\alpha-1)r(1+r)
+
\frac32r^2.
\]
For every
\[
r>0,
\]
the maximizing point on the circle
\[
|z|=r
\]
is uniquely
\[
z=r.
\]

Consequently the harmonic Schwarzian norm is exactly
\[
\|S_{f_\alpha}\|_{\mathbb D}
=
2(\alpha^2-1)
+
2(\alpha-1)
+
\frac32
=
2\alpha^2+2\alpha-\frac52.
\]
The source states the right-hand side as an upper bound; the equality above shows that there is no slack in that estimate.

The norm is not attained inside the disk. Every sequence
\[
z_j\in\mathbb D
\]
with
\[
(1-|z_j|^2)^2
|S_{f_\alpha}(z_j)|
\longrightarrow
\|S_{f_\alpha}\|_{\mathbb D}
\]
must converge to the single boundary point
\[
1.
\]

The radial deficit is also exact:
\[
\|S_{f_\alpha}\|_{\mathbb D}
-
M_\alpha(r)
=
(1-r)
\left[
\frac{\alpha^2-1}{2}(3+r)
+
(\alpha-1)(2+r)
+
\frac32(1+r)
\right].
\]
Thus the norm approaches its boundary value linearly along the unique maximizing radius.

Writing
\[
\varepsilon=\alpha-1,
\]
the exact norm becomes
\[
\|S_{f_{1+\varepsilon}}\|_{\mathbb D}
=
\frac32+6\varepsilon+2\varepsilon^2.
\]
Hence the non-injective witness family approaches the conjectured harmonic inner-radius threshold from above with an exact first-order slope equal to
\[
6.
\]

## Assumptions and scope

The Schwarzian derivative used here is the planar harmonic Schwarzian
\[
S_f
=
(P_f)_z-\frac12P_f^2,
\]
with
\[
P_f=(\log J_f)_z.
\]
On the unit disk its norm is
\[
\|S_f\|_{\mathbb D}
=
\sup_{z\in\mathbb D}
(1-|z|^2)^2|S_f(z)|.
\]

For the family above, the cited 2026 source computes
\[
S_{f_\alpha}(z)
=
\frac{1-\alpha^2}{2(1-z)^2}
+
\frac{(1-\alpha)\overline z}
{(1-|z|^2)(1-z)}
-
\frac{3\overline z^2}
{2(1-|z|^2)^2}.
\]
It uses this formula to obtain
\[
\|S_{f_\alpha}\|_{\mathbb D}
\le
2(\alpha^2-1)+2(\alpha-1)+\frac32.
\]

The present result concerns precisely this source family and this harmonic Schwarzian norm. It does not prove the conjecture
\[
\sigma_H(\mathbb D)=\frac32,
\]
nor does it characterize all non-injective harmonic mappings whose Schwarzian norms approach the threshold.

The parameter range
\[
\alpha>1
\]
is the non-injective range used in the source argument. The endpoint
\[
\alpha=1
\]
has norm
\[
3/2
\]
as well, but its boundary extremizing set is no longer concentrated at one point because the first two terms of the displayed Schwarzian vanish.

## Proof

Set
\[
A=\frac{\alpha^2-1}{2}
\]
and
\[
b=\alpha-1.
\]
Both are positive for
\[
\alpha>1.
\]
For
\[
z\in\mathbb D,
\]
write
\[
r=|z|
\]
and
\[
w(z)=\frac{1-r^2}{1-z}.
\]
Multiplying the source formula for the Schwarzian by
\[
(1-r^2)^2
\]
gives
\[
(1-r^2)^2S_{f_\alpha}(z)
=
-
\left[
Aw(z)^2
+
b\overline z\,w(z)
+
\frac32\overline z^2
\right].
\]
Therefore
\[
(1-r^2)^2|S_{f_\alpha}(z)|
\le
A|w(z)|^2
+
br|w(z)|
+
\frac32r^2.
\]

Now
\[
|w(z)|
=
\frac{1-r^2}{|1-z|}
\le
\frac{1-r^2}{1-r}
=
1+r.
\]
Hence
\[
(1-r^2)^2|S_{f_\alpha}(z)|
\le
A(1+r)^2
+
br(1+r)
+
\frac32r^2.
\]

At the positive real point
\[
z=r,
\]
one has
\[
w(r)=1+r.
\]
All three terms inside the bracket then have the same positive real phase before the common minus sign. Thus equality holds and
\[
M_\alpha(r)
=
A(1+r)^2
+
br(1+r)
+
\frac32r^2.
\]

For
\[
r>0,
\]
equality in
\[
|1-z|\ge1-r
\]
holds only when
\[
z=r.
\]
Since
\[
A>0,
\]
this proves uniqueness of the maximizing point on every nonzero circle.

The function
\[
M_\alpha(r)
\]
is strictly increasing because
\[
M_\alpha'(r)
=
2A(1+r)
+
b(1+2r)
+
3r
>
0.
\]
Therefore
\[
\|S_{f_\alpha}\|_{\mathbb D}
=
\lim_{r\uparrow1}M_\alpha(r)
=
4A+2b+\frac32.
\]
Substituting the definitions of
\[
A
\]
and
\[
b
\]
gives the stated exact norm.

The deficit factors directly:
\[
4A+2b+\frac32
-
\left[
A(1+r)^2
+
br(1+r)
+
\frac32r^2
\right]
\]
equals
\[
(1-r)
\left[
A(3+r)
+
b(2+r)
+
\frac32(1+r)
\right].
\]

It remains to locate arbitrary extremizing sequences. Suppose
\[
z_j\in\mathbb D
\]
is such that the weighted Schwarzian tends to its norm. Put
\[
r_j=|z_j|
\]
and
\[
w_j=w(z_j).
\]
The preceding bounds imply
\[
(1-r_j^2)^2|S_{f_\alpha}(z_j)|
\le
M_\alpha(r_j)
<
\|S_{f_\alpha}\|_{\mathbb D}.
\]
Since
\[
M_\alpha
\]
is strictly increasing and continuous,
\[
r_j\to1.
\]
Moreover, because
\[
A>0,
\]
the same chain of inequalities forces
\[
|w_j|\to2.
\]
But
\[
\frac{|w_j|}{1+r_j}
=
\frac{1-r_j}{|1-z_j|}
\le1.
\]
Hence
\[
\frac{1-r_j}{|1-z_j|}
\to1.
\]
Writing
\[
z_j=r_je^{i\theta_j},
\]
the identity
\[
|1-z_j|^2
=
(1-r_j)^2
+
2r_j(1-\cos\theta_j)
\]
then gives
\[
\theta_j\to0.
\]
Thus
\[
z_j\to1.
\]

Finally,
\[
2\alpha^2+2\alpha-\frac52
\]
at
\[
\alpha=1+\varepsilon
\]
is exactly
\[
\frac32+6\varepsilon+2\varepsilon^2.
\]

## Verification

The source formula for
\[
S_{f_\alpha}
\]
was substituted directly before any estimate was made.

The key geometric inequality
\[
\frac{1-r^2}{|1-z|}
\le1+r
\]
is simply the reverse triangle inequality
\[
|1-z|\ge1-|z|.
\]
Its equality condition on
\[
|z|=r
\]
is exactly
\[
z=r.
\]

The exact circle maximum was independently replayed numerically for several values of
\[
\alpha
\]
and
\[
r.
\]
Those computations agree with the symbolic formula but are not used as proof.

The global norm follows from a monotone one-variable profile, so no finite search over the disk is used to infer a supremum.

The extremizing-sequence statement uses both necessary limiting conditions
\[
|z_j|\to1
\]
and
\[
\frac{1-|z_j|}{|1-z_j|}\to1.
\]
The latter rules out approach to any boundary point other than
\[
1.
\]

## Relationship to prior work

Efraimidis and Hernández introduce the harmonic inner-radius problem and prove
\[
\sigma_H(\mathbb D)\le\frac32
\]
using the non-injective family
\[
f_\alpha.
\]
They compute its harmonic Schwarzian explicitly and state the estimate
\[
\|S_{f_\alpha}\|_{\mathbb D}
\le
2(\alpha^2-1)+2(\alpha-1)+\frac32.
\]
Their proof only needs the estimate and its limit as
\[
\alpha\downarrow1.
\]
The inspected full text does not state equality, an exact circle-by-circle profile, or a uniqueness statement for norm-extremizing boundary approach.

Wang, Liu, Rasila, and Sun constructed the underlying non-injective harmonic family in earlier work to answer a univalence problem. That paper predates the 2026 use of the harmonic Schwarzian norm for this family and does not supply the present exact norm profile.

The general harmonic Schwarzian theory of Hernández and Martín provides the derivative formalism used by the 2026 source, but it does not specialize to this later witness family.

Targeted searches for the exact family, its harmonic Schwarzian norm, the polynomial value
\[
2\alpha^2+2\alpha-\frac52,
\]
and boundary concentration at
\[
1
\]
did not locate a published statement implying the theorem above.

## Limitations

The result exactly calibrates the witness family used for the upper bound on
\[
\sigma_H(\mathbb D).
\]
It does not provide the missing lower bound needed to settle the conjectured equality
\[
\sigma_H(\mathbb D)=3/2.
\]

The uniqueness statement concerns the location of sequences that extremize the Schwarzian norm of this explicit family. It is not a classification of extremal harmonic mappings for the harmonic inner-radius problem.

For
\[
\alpha=1,
\]
the norm remains
\[
3/2,
\]
but the angular concentration statement changes because the terms depending on
\[
\alpha-1
\]
vanish.

## References

1. I. Efraimidis and R. Hernández, *Harmonic mappings, univalence criteria and a theorem of Lehtinen*, arXiv:2604.00269v1, first posted 31 March 2026; The Journal of Analysis (2026), DOI: 10.1007/s41478-026-01157-y.
2. Z.-G. Wang, Z.-H. Liu, A. Rasila, and Y. Sun, *On a problem of Bharanedhar and Ponnusamy involving planar harmonic mappings*, arXiv:1703.09478; Rocky Mountain Journal of Mathematics 48 (2018), 1345--1358, DOI: 10.1216/RMJ-2018-48-4-1345.
3. R. Hernández and M. J. Martín, *Pre-Schwarzian and Schwarzian derivatives of harmonic mappings*, The Journal of Geometric Analysis 25 (2015), 64--91.
