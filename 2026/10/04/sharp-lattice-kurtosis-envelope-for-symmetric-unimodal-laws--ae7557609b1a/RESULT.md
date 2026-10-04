# Sharp lattice kurtosis envelope for symmetric unimodal laws

## Finding

Let \(X\) be a nondegenerate integer-valued random variable with a symmetric
unimodal probability mass function:
\[
\Pr(X=j)=\Pr(X=-j)=p_j,
\qquad
p_0\ge p_1\ge p_2\ge\cdots .
\]
Write
\[
v=\mathbb E X^2>0.
\]

For \(m\ge0\), define
\[
v_m=\frac{m(m+1)}3
\]
and
\[
q_m=
\frac{m(m+1)(3m^2+3m-1)}{15}.
\]
Choose the unique \(m\) for which
\[
v_m\le v\le v_{m+1}.
\]

Then the exact minimum fourth moment is the chord joining the two adjacent
centered discrete-uniform moment points:
\[
\boxed{
\mathbb E X^4
\ge
\frac{v_{m+1}-v}{v_{m+1}-v_m}\,q_m
+
\frac{v-v_m}{v_{m+1}-v_m}\,q_{m+1}.
}
\]

Equivalently, writing
\[
\kappa(X)=\frac{\mathbb E X^4}{v^2},
\]
the exact kurtosis lower envelope is
\[
\boxed{
\kappa(X)
\ge
\frac95-\frac1{5v}
+
\frac9{5v^2}(v-v_m)(v_{m+1}-v).
}
\tag{1}
\]

Equality holds exactly for the unique variance-matching mixture of the two
centered discrete uniform laws
\[
U_m\sim {\rm Unif}\{-m,\ldots,m\},
\qquad
U_{m+1}\sim {\rm Unif}\{-(m+1),\ldots,m+1\}.
\]
At a grid variance \(v=v_m\), the mixture collapses to \(U_m\).

The continuous symmetric-unimodal lower kurtosis value \(9/5\) survives only
as the leading large-variance term. The lattice correction has a genuine
phase. Put
\[
\theta=
\frac{v-v_m}{v_{m+1}-v_m}.
\]
If \(v\to\infty\) along a sequence for which \(\theta\to\tau\in[0,1]\), then
\[
\boxed{
v\left(\kappa_{\min}(v)-\frac95\right)
\longrightarrow
-\frac15+\frac{12}{5}\tau(1-\tau).
}
\tag{2}
\]
Hence the full cluster interval of the scaled correction is
\[
\boxed{\left[-\frac15,\frac25\right]}.
\]

In particular, at the discrete-uniform grid points the sharp kurtosis lies
below \(9/5\):
\[
\kappa(U_m)=\frac95-\frac1{5v_m},
\]
while phases near the middle of a variance cell eventually lie above \(9/5\).

## Assumptions and scope

Symmetry means equality of the masses at \(j\) and \(-j\). Unimodality is the
standard lattice condition that those masses are nonincreasing as
\(|j|\) increases.

No finite-support assumption is imposed. Finite variance alone is enough for
the mixture representation used in the proof, and the theorem is meaningful
when the fourth moment is finite; if the fourth moment is infinite, the lower
bound is automatic.

The lattice spacing is normalized to one. A rescaled lattice follows by the
obvious change of scale.

## Proof

For \(m\ge0\), let \(U_m\) denote the centered discrete uniform law on
\[
\{-m,-m+1,\ldots,m\}.
\]
Define
\[
\lambda_m=(2m+1)(p_m-p_{m+1}),
\]
where \(p_m\to0\). By unimodality,
\[
\lambda_m\ge0.
\]
Summation by parts gives
\[
\sum_{m\ge0}\lambda_m
=
p_0+2\sum_{m\ge1}p_m
=
1.
\]
Moreover, for every \(j\ge0\),
\[
\sum_{m\ge j}\frac{\lambda_m}{2m+1}
=
\sum_{m\ge j}(p_m-p_{m+1})
=
p_j.
\]
Thus
\[
X\ \stackrel{d}{=}\ U_M
\]
for a mixing index \(M\) with
\[
\Pr(M=m)=\lambda_m.
\tag{3}
\]

The centered discrete uniform moments are
\[
\mathbb E U_m^2
=
\frac{m(m+1)}3
=
v_m
\]
and
\[
\mathbb E U_m^4
=
\frac{m(m+1)(3m^2+3m-1)}{15}
=
q_m.
\tag{4}
\]
Since
\[
q_m=\phi(v_m),
\qquad
\phi(t)=\frac{9t^2-t}{5},
\tag{5}
\]
the moment points lie exactly on a strictly convex parabola.

By (3) and (4),
\[
v=\sum_{r\ge0}\lambda_r v_r,
\qquad
\mathbb E X^4=\sum_{r\ge0}\lambda_r q_r.
\tag{6}
\]

Fix \(m\) such that \(v_m\le v\le v_{m+1}\), and let \(L_m(t)\) be the affine
line through
\[
(v_m,q_m)
\quad\text{and}\quad
(v_{m+1},q_{m+1}).
\]
Because \(\phi\) is strictly convex and there is no variance grid point
strictly between \(v_m\) and \(v_{m+1}\),
\[
q_r=\phi(v_r)\ge L_m(v_r)
\]
for every integer \(r\ge0\), with equality only for \(r=m\) or \(r=m+1\).
Taking the mixture average in (6),
\[
\mathbb E X^4
\ge
\sum_r\lambda_r L_m(v_r)
=
L_m\!\left(\sum_r\lambda_r v_r\right)
=
L_m(v).
\]
This is the first displayed bound.

Since \(\phi\) is quadratic,
\[
L_m(v)
=
\phi(v)
+
\frac95(v-v_m)(v_{m+1}-v),
\]
which yields (1).

Strict convexity also gives the equality statement. Equality in the chord
bound forces
\[
\lambda_r=0
\]
outside \(\{m,m+1\}\). The variance constraint then fixes the weights:
\[
\Pr(M=m)
=
\frac{v_{m+1}-v}{v_{m+1}-v_m},
\qquad
\Pr(M=m+1)
=
\frac{v-v_m}{v_{m+1}-v_m}.
\]

For the phase limit, note that
\[
v_{m+1}-v_m=\frac{2(m+1)}3.
\]
If
\[
\theta=
\frac{v-v_m}{v_{m+1}-v_m},
\]
then (1) gives the exact identity
\[
v\left(\kappa_{\min}(v)-\frac95\right)
=
-\frac15
+
\frac9{5v}\,
\theta(1-\theta)(v_{m+1}-v_m)^2.
\tag{7}
\]
As \(v\to\infty\),
\[
\frac{(v_{m+1}-v_m)^2}{v}\longrightarrow\frac43.
\]
Substituting into (7) proves (2). Since
\[
-\frac15+\frac{12}{5}\tau(1-\tau)
\]
ranges exactly over
\[
\left[-\frac15,\frac25\right],
\]
every value in the claimed cluster interval is realized by choosing a variance
phase approaching an appropriate \(\tau\).

## Verification

The accompanying exact-rational checker verifies the discrete-uniform moment
formulas, the parabola identity, every chord inequality on a large finite
range of grid indices, exact attainment by the adjacent-uniform mixture, and
the phase-scaled formula.

It also generates random rational convex mixtures of centered discrete
uniforms and confirms that their fourth moments stay above the stated sharp
envelope.

Finite computation is not used to infer the universal result.

## Relationship to prior work

Navard, Seaman, and Young give a convexity-based characterization of discrete
unimodality and derive variance bounds for discrete unimodal distributions.
Their full 1993 paper explicitly develops the lattice unimodality framework
and its connection to convex analysis. The inspected paper does not optimize
fourth moments at fixed variance and does not state the adjacent-uniform
kurtosis envelope above.

Classical continuous unimodality theory gives the sharp symmetric-unimodal
kurtosis bound
\[
\kappa\ge\frac95,
\]
with equality only for a continuous uniform law. Recent full-text treatments
of the skewness-kurtosis set restate that sharp continuous result. The lattice
theorem above is not a direct specialization: discrete uniform laws already
satisfy
\[
\kappa(U_m)<\frac95,
\]
and the exact discrete lower envelope oscillates around \(9/5\) at order
\(1/v\).

A previously obtained sharp lattice Gauss tail envelope for the same class of
symmetric unimodal integer laws optimizes tail probability at a prescribed
threshold. Pointwise tail maxima use threshold-dependent extremizers and do
not imply the present minimum-fourth-moment chord problem. The present theorem
instead identifies a single adjacent-uniform mixture from the variance alone.

Targeted searches using discrete-unimodality, fourth-moment, kurtosis,
centered-uniform-mixture, and lattice-correction terminology did not locate
the formula (1), its equality classification, or the phase law (2).

## Limitations

The theorem is for symmetric unimodal integer laws. Without symmetry, the
fourth-moment problem has additional skewness degrees of freedom.

The result fixes variance but no support radius. Consequently there is no
finite upper bound on the fourth moment in this class.

The originality assessment is based on targeted searches and inspection of
the closest full texts. An equivalent moment-envelope statement could exist
in older discrete-unimodality literature under terminology not captured by
those searches.

## References

1. S. E. Navard, J. W. Seaman Jr., and D. M. Young, “A characterization of
   discrete unimodality with applications to variance upper bounds,”
   *Annals of the Institute of Statistical Mathematics* 45 (1993), 603–614,
   DOI 10.1007/BF00774775.
2. C. A. J. Klaassen, P. J. Mokveld, and B. van Es, “Squared skewness minus
   kurtosis bounded by 186/125 for unimodal distributions,”
   *Statistics & Probability Letters* 50 (2000), 131–135,
   DOI 10.1016/S0167-7152(00)00090-0.
3. S. Dharmadhikari and K. Joag-Dev, *Unimodality, Convexity, and
   Applications*, Academic Press, 1988.
