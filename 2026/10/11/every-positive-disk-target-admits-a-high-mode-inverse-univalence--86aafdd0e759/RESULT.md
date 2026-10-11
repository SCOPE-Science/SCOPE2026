# Every positive disk target admits a high-mode inverse-univalence counterexample

## Finding

Fix
\[
\lambda,\mu>0
\]
and
\[
0<\delta\le1.
\]
For
\[
\Omega_n
=
\frac{(n-1)^{\lambda/2}}
{1+(n-1)^{\lambda+\mu}},
\qquad
n\ge2,
\]
consider the Hadamard multiplier
\[
\mathfrak M_{\lambda,\mu}f(z)
=
z+\sum_{n\ge2}\Omega_n a_nz^n.
\]
The associated operator-preimage class is defined by
\[
\left|
\frac{z(\mathfrak M_{\lambda,\mu}f)'(z)}
{\mathfrak M_{\lambda,\mu}f(z)}
-1
\right|
<
\delta
\qquad
(z\in\mathbb D).
\]

For every integer
\[
n\ge2,
\]
the single-mode family
\[
f_{a,n}(z)=z+az^n
\]
belongs to this class exactly when
\[
|a|
\le
A_n(\delta)
:=
\frac{\delta}
{\Omega_n(n-1+\delta)}.
\]

The original function
\[
f_{a,n}
\]
is starlike, and therefore univalent and locally univalent, exactly when
\[
|a|\le\frac1n.
\]
Hence the complete \(n\)-th monomial slice is inverse-safe exactly for
\[
0<\delta
\le
\delta_n(\lambda,\mu)
:=
\frac{\Omega_n(n-1)}
{n-\Omega_n}.
\]

If
\[
\delta>\delta_n(\lambda,\mu),
\]
then every choice satisfying
\[
\frac1n
<
|a|
\le
\frac{\delta}
{\Omega_n(n-1+\delta)}
\]
produces a member of the operator-preimage disk-starlike class whose original function is not even locally univalent.

Finally,
\[
\delta_n(\lambda,\mu)
\sim
\Omega_n
\sim
(n-1)^{-(\lambda/2+\mu)}
\longrightarrow0.
\]
Thus no fixed positive target radius can guarantee inverse preservation of local univalence, univalence, or starlikeness on the full normalized analytic class.

## Assumptions and scope

The domain is the unit disk
\[
\mathbb D
=
\{z\in\mathbb C:|z|<1\}.
\]
The parameters satisfy
\[
\lambda,\mu>0
\]
and
\[
0<\delta\le1.
\]

The conclusion concerns the specific algebraically damped Hadamard multiplier above and the disk target
\[
\Phi_\delta(z)=1+\delta z.
\]
It is an inverse-preservation statement: the transformed function obeys a disk-starlikeness condition, while the question is whether that forces the original preimage function to retain local univalence, univalence, or starlikeness.

The theorem proves a negative answer on the full normalized analytic class and gives an exact positive threshold on every individual monomial slice. It does not rule out inverse-preservation theorems under additional coefficient, sign, sparsity, or regularity hypotheses.

## Proof

Fix
\[
n\ge2
\]
and write
\[
f_{a,n}(z)=z+az^n.
\]
Its transformed function is
\[
F(z)
=
\mathfrak M_{\lambda,\mu}f_{a,n}(z)
=
z+cz^n,
\qquad
c=\Omega_n a.
\]
A direct calculation gives
\[
\frac{zF'(z)}{F(z)}-1
=
\frac{(n-1)cz^{n-1}}
{1+cz^{n-1}}.
\]

Put
\[
t=|c|.
\]
For
\[
|z|<1,
\]
the variable
\[
w=cz^{n-1}
\]
ranges over the disk
\[
|w|<t.
\]
If
\[
t>1,
\]
then \(1+cz^{n-1}\) vanishes at an interior point, while for
\[
t=1
\]
the displayed logarithmic-derivative modulus is unbounded as that boundary zero is approached. Hence class membership already fails whenever
\[
t\ge1.
\]
It remains to consider
\[
t<1.
\]
In that case one has
\[
\sup_{|w|<t}
\left|
\frac{(n-1)w}{1+w}
\right|
=
\frac{(n-1)t}{1-t}.
\]
Indeed,
\[
|1+w|\ge1-|w|,
\]
so the displayed expression is at most
\[
(n-1)t/(1-t),
\]
and values arbitrarily close to this bound are obtained as
\[
w
\]
approaches
\[
-t
\]
from inside the disk.

Therefore the strict disk condition at every interior point is equivalent to
\[
\frac{(n-1)t}{1-t}
\le
\delta.
\]
Equality is allowed in this boundary supremum because
\[
|z|<1
\]
forces
\[
|w|<t.
\]
Solving gives
\[
t
\le
\frac{\delta}{n-1+\delta}.
\]
Since
\[
t=\Omega_n|a|,
\]
we obtain the exact membership criterion
\[
|a|
\le
\frac{\delta}
{\Omega_n(n-1+\delta)}.
\]

Now examine the original function. Its derivative is
\[
f'_{a,n}(z)
=
1+naz^{n-1}.
\]
A critical point lies in
\[
\mathbb D
\]
exactly when
\[
|a|>\frac1n.
\]
Thus local univalence holds exactly when
\[
|a|\le\frac1n.
\]

The same threshold is also exactly the starlikeness threshold. With
\[
u=az^{n-1},
\]
one has
\[
\frac{zf'_{a,n}(z)}
{f_{a,n}(z)}
=
\frac{1+nu}{1+u}.
\]
Its real part is
\[
\operatorname{Re}
\frac{1+nu}{1+u}
=
\frac{
1+n|u|^2+(n+1)\operatorname{Re}u
}{
|1+u|^2
}.
\]
On
\[
|u|<|a|,
\]
the numerator is positive for every interior point whenever
\[
|a|\le\frac1n,
\]
because its boundary minimum occurs at a negative real value and factors as
\[
1+n|a|^2-(n+1)|a|
=
(1-|a|)(1-n|a|).
\]
If
\[
|a|>\frac1n,
\]
the interior critical point already rules out starlikeness. Hence
\[
f_{a,n}
\]
is starlike exactly when
\[
|a|\le1/n.
\]

Every class member in the \(n\)-th monomial slice is therefore starlike exactly when
\[
\frac{\delta}
{\Omega_n(n-1+\delta)}
\le
\frac1n.
\]
This is equivalent to
\[
\delta
\le
\frac{\Omega_n(n-1)}
{n-\Omega_n}
=
\delta_n(\lambda,\mu).
\]

Finally,
\[
\frac{\delta_n(\lambda,\mu)}
{\Omega_n}
=
\frac{n-1}{n-\Omega_n}
\longrightarrow1.
\]
The defining multiplier satisfies
\[
\Omega_n
\sim
(n-1)^{-(\lambda/2+\mu)},
\]
so
\[
\delta_n(\lambda,\mu)\to0.
\]
For every fixed
\[
\delta>0,
\]
some sufficiently large
\[
n
\]
therefore satisfies
\[
\delta>\delta_n(\lambda,\mu).
\]
Choosing
\[
a
\]
in the nonempty interval
\[
\frac1n<|a|\le A_n(\delta)
\]
gives the claimed high-mode counterexample.

## Verification

The proof uses exact one-variable inequalities only.

The transformed logarithmic derivative identity was recomputed directly:
\[
F(z)=z+cz^n
\]
implies
\[
zF'(z)-F(z)
=
(n-1)cz^n,
\]
and division by
\[
F(z)=z(1+cz^{n-1})
\]
gives the stated fraction.

The supremum over
\[
|w|<t
\]
is exact because the denominator obeys
\[
|1+w|\ge1-|w|,
\]
with sharp boundary approach along the negative real ray.

The original-function threshold is independently checked from both
\[
f'_{a,n}(z)=1+naz^{n-1}
\]
and the exact real-part formula for
\[
zf'_{a,n}(z)/f_{a,n}(z).
\]

No numerical sampling, finite enumeration, or asymptotic approximation is used to establish the continuum statement. The asymptotic conclusion uses only the explicit multiplier formula and
\[
(n-1)/(n-\Omega_n)\to1.
\]

## Relationship to prior work

The 2026 source introduces the algebraically damped Hadamard operator and its disk-starlike preimage class. It explicitly emphasizes that the geometric conclusion applies to the transformed function and does not automatically imply starlikeness or univalence of the original preimage.

That source gives an exact calculation for the quadratic family
\[
z+az^2:
\]
membership is equivalent to
\[
|a|
\le
\frac{2\delta}{1+\delta}.
\]
The present result extends the exact calculation to every single Taylor mode and then uses the algebraic decay
\[
\Omega_n\to0
\]
to obtain a global impossibility theorem for inverse preservation at every fixed positive disk radius.

Classical convolution literature contains many forward property-preservation results under additional hypotheses on the convolving functions or multiplier kernels. Those results do not contradict the present statement: the operator here damps high modes to zero, so inversion amplifies them, and the explicit monomial calculation shows that no full-class inverse-preservation theorem can hold at any fixed positive
\[
\delta.
\]

## Limitations

The counterexamples are deliberately sparse: each uses only one nonlinear Taylor coefficient. The theorem does not classify which additional restrictions on the original coefficient sequence can restore inverse preservation.

The exact thresholds
\[
\delta_n(\lambda,\mu)
\]
describe monomial slices. They are not claimed to be optimal thresholds for arbitrary finite-dimensional coefficient subspaces with several interacting modes.

The literature comparison was targeted to the named operator, its aliases, inverse preservation, monomial slices, and broader Hadamard property-preserving results. Older results under different multiplier conventions may use related terminology; the explicit counterexample nevertheless excludes any such theorem from applying to this full preimage class without additional hypotheses.

## References

1. A. Alameer, *Sharp Coefficient Bounds for a Disk-Starlike Preimage Class Defined by an Algebraically Damped Hadamard Operator*, Mathematics 14 (2026), 3066, DOI: 10.3390/math14173066. Published 26 August 2026.
2. K. Piejko and J. Sokół, *Hadamard product of analytic functions and some special regions and curves*, Journal of Inequalities and Applications 2013 (2013), 420, DOI: 10.1186/1029-242X-2013-420.
