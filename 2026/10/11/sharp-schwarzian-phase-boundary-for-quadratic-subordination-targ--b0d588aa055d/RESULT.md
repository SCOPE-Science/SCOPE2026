# Sharp Schwarzian phase boundary for quadratic subordination targets

## Finding

For every real parameter \(c\) with \(-1/2\le c\le1/2\), put
\[
\varphi_c(z)=1+z+cz^2
\]
and let \(\mathcal F_c\) consist of normalized holomorphic functions \(f\) on the unit disk \(\mathbb D\) satisfying
\[
f(0)=0,\quad f'(0)=1,\quad
1+\frac{zf''(z)}{f'(z)}\prec\varphi_c(z).
\]
The quotient is interpreted holomorphically, so the derivatives do not vanish. Define the hyperbolic Schwarzian norm by
\[
S_f=\left(\frac{f''}{f'}\right)'-\frac12\left(\frac{f''}{f'}\right)^2,
\qquad \|S_f\|=\sup_{z\in\mathbb D}(1-|z|^2)^2|S_f(z)|.
\]
Then the exact parameter interval for a universal *unit Schwarzian bound* is
\[
\boxed{\ \sup_{f\in\mathcal F_c}\|S_f\|=1\quad\Longleftrightarrow\quad
\frac{1-\sqrt3}{2}\le c\le\frac12\ },
\]
where the equivalence is understood inside the complete interval \(-1/2\le c\le1/2\). For every \(-1/2\le c<(1-\sqrt3)/2\), the strict reverse inequality
\[
\sup_{f\in\mathcal F_c}\|S_f\|>1
\]
holds, witnessed by explicit degree-one disk-automorphism data.

Moreover, throughout the unit-norm interval, equality \(\|S_f\|=1\) occurs **precisely** for the one-parameter rotation family
\[
f_\theta(z)=\int_0^z
\exp\!\left(\frac{e^{i\theta}\zeta^2}{2}+
\frac{c e^{2i\theta}\zeta^4}{4}\right)\,d\zeta,
\qquad \theta\in\mathbb R.
\]
Consequently, every \(f\in\mathcal F_c\) in that interval has a quasiconformal extension to the sphere with maximal dilatation **at most \(3\)**, by Ahlfors--Weill. The value \(3\) is a guaranteed extension bound, *not* asserted to be the optimal extension dilatation.

The critical point \((1-\sqrt3)/2\approx-0.3660254037844386\) lies strictly inside the natural negative half of the polynomial target's univalence range. The original positive-parameter Ma--Minda convex family is therefore contained in a larger, sharply delimited Schwarzian-controlled family, even though negative parameters no longer impose the original convexity condition.

## Assumptions and scope

The subordination \(h\prec\varphi_c\) means that there is a holomorphic self-map \(\omega:\mathbb D\to\mathbb D\), with \(\omega(0)=0\), for which \(h=\varphi_c\circ\omega\). The polynomial \(\varphi_c\) is univalent throughout \(|c|\le1/2\): if \(\varphi_c(z_1)=\varphi_c(z_2)\), then either \(z_1=z_2\) or \(1+c(z_1+z_2)=0\), the latter being impossible for distinct points of \(\mathbb D\) when \(|c|\le1/2\).

Allu and Kumar introduced the case \(c=m/n\), where \(m,n\) are positive integers and \(2m\le n\), as a Ma--Minda **convex** class and solved related Hankel determinant problems. The present statement allows continuous real \(c\in[-1/2,1/2]\). For negative \(c\), the polynomial may have negative real part at disk points; the class is then only a *quadratic-target subordination class*, not automatically a Ma--Minda convex class. The theorem itself gives its univalence and extension conclusion on the stated subinterval.

## Proof

**1. Schwarz representation.** Write \(\omega(z)=zv(z)\) by Schwarz's lemma. Either \(v\) is a disk self-map or a unimodular constant; both satisfy the derivative inequality
\[
|v'(z)|\le\frac{1-|v(z)|^2}{1-|z|^2}.
\]
The subordination relation implies
\[
P(z):=\frac{f''(z)}{f'(z)}=v(z)+czv(z)^2.
\]
Differentiation gives the exact identity
\[
\boxed{\quad
S_f(z)=(1+2czv)v'+(c-\tfrac12)v^2-czv^3-\tfrac12c^2z^2v^4.
\quad}
\]
Put \(r=|z|\), \(s=|v(z)|\), and \(u=1-r^2\). Here \(0\le r<1\) and \(0\le s\le1\).

**2. Nonnegative parameters.** For \(0\le c\le1/2\), the triangle inequality and Schwarz--Pick yield
\[
u^2|S_f(z)|\le
F_+(c,r,s):=u(1-s^2)(1+2crs)+u^2s^2\left(\tfrac12-c+crs+\tfrac12c^2r^2s^2\right).
\]
At fixed \(r,s\), this is a convex quadratic function of \(c\); hence it is no larger than the maximum of its values at \(c=0\) and \(c=1/2\). Direct expansion gives
\[
1-F_+(0,r,s)=r^2+us^2(1-u/2)
\]
and
\[
\begin{aligned}
1-F_+(\tfrac12,r,s)
={}&r^2(1-u/4)+u(s-r/2)^2\\
&+rus^3\left((1+r^2)/2-rus/8\right).
\end{aligned}
\]
Every summand is nonnegative because \(0\le r,s,u\le1\); the displayed last parenthesis is at least \(3/8\). Equality in either endpoint bound is possible only when \(r=s=0\). Consequently
\[
u^2|S_f(z)|\le1
\]
for all \(0\le c\le1/2\), with equality in this pointwise bound only at \(r=s=0\).

**3. Negative parameters: an exact sum-of-squares certificate.** Write \(c=-d\), \(0\le d\le1/2\). From the same Schwarzian identity,
\[
u^2|S_f(z)|\le
F_-(d,r,s):=u(1-s^2)(1+2drs)+u^2s^2\left(\tfrac12+d+drs+\tfrac12d^2r^2s^2\right).
\]
An exact polynomial identity is
\[
\begin{aligned}
1-F_-(d,r,s)
={}&(r-dus)^2\\
&+us^2(\tfrac12-d-d^2)\\
&+ur^2s^2(d^2+d+\tfrac12)\\
&+drus^3\left(1+r^2-\tfrac12drus\right).
\end{aligned}
\]
Every term on the right is nonnegative if
\[
d^2+d\le\tfrac12,
\]
namely if \(0\le d\le d_*=(\sqrt3-1)/2\). Indeed, \(1+r^2-\tfrac12drus\ge3/4\). For each such \(d\), equality requires \(r=s=0\). This proves the unit Schwarzian bound down to \(c=-d_*\).

**4. Rigidity of norm extremizers.** For each admissible parameter in the interval established above, the pointwise gaps in steps 2--3 are positive whenever \((r,s)\ne(0,0)\). In addition, the gaps are uniformly positive for \(r\ge\varepsilon\) for each fixed \(\varepsilon>0\), because their displayed expressions extend continuously to \(r=1\) and equal \(1\) there.

Suppose \(\|S_f\|=1\), and choose a sequence \(z_j\) approaching its supremum. The uniform gap away from \(r=0\) forces \(z_j\to0\). At \(r=0\), the upper bound equals
\[
F_+(c,0,s)=1-(\tfrac12+c)s^2
\]
for \(c\ge0\), and
\[
F_-(d,0,s)=1-(\tfrac12-d)s^2
\]
for \(c=-d\); both coefficients are strictly positive on the permitted parameter interval. Thus \(v(z_j)\to0\), and continuity gives \(v(0)=0\). By continuity of \(S_f\),
\[
|S_f(0)|=1,
\]
and the Schwarzian identity reduces this to \(|v'(0)|=1\). The equality case of Schwarz's lemma forces
\[
v(z)=e^{i\theta}z.
\]
Integrating \(f''/f'=v+czv^2\) with the normalization determines exactly the stated \(f_\theta\) family. Conversely each such function belongs to \(\mathcal F_c\), since its Schwarz function is \(\omega(z)=e^{i\theta}z^2\); it satisfies \(|S_{f_\theta}(0)|=1\). Therefore the norm bound is sharp and these are *all* extremizers.

**5. Failure below the critical parameter.** Fix \(d_*<d\le1/2\), and choose a small real \(s>0\). Set \(r=ds\), \(u=1-r^2\), and
\[
a=\frac{r-s}{1-rs},\qquad
v_{r,s}(z)=\frac{a-z}{1-az}.
\]
Since \(0<r,s<1\), this is a disk automorphism satisfying
\[
v_{r,s}(r)=-s,
\qquad
v_{r,s}'(r)=-\frac{1-s^2}{1-r^2}.
\]
Let \(f\) be the uniquely normalized holomorphic solution of
\[
\frac{f''(z)}{f'(z)}=v_{r,s}(z)-dzv_{r,s}(z)^2.
\]
Such a solution exists by integrating the holomorphic right-hand side twice and has nonvanishing derivative. Its subordinate Schwarz function is \(\omega(z)=zv_{r,s}(z)\), so \(f\in\mathcal F_{-d}\). At the real point \(z=r\), **all four terms** of the Schwarzian expression are negative real numbers; therefore the Schwarz--Pick/triangle estimate is an equality:
\[
(1-r^2)^2|S_f(r)|=F_-(d,r,s).
\]
The expansion under \(r=ds\) is
\[
F_-(d,ds,s)=1+(d^2+d-\tfrac12)s^2+O_d(s^4).
\]
Because \(d>d_*\), the quadratic coefficient is strictly positive, so \(F_->1\) for all sufficiently small \(s\). This completes the if-and-only-if classification.

**6. Quasiconformal extension.** The Ahlfors--Weill theorem says that a holomorphic map on \(\mathbb D\) with \(\|S_f\|\le2k<2\) extends quasiconformally over the sphere with Beltrami coefficient bounded by \(k\). Taking \(k=1/2\) yields maximal dilatation at most \((1+k)/(1-k)=3\) throughout the unit-Schwarzian interval.

## Verification

The standalone script `verify.py` re-expands both positive-parameter endpoint defects, the negative-parameter sum-of-squares identity, the Schwarzian identity, the disk-automorphism derivative, and the small-parameter expansion. It also checks the concrete witness \(d=2/5\), \(s=1/10\), \(r=1/25\), for which
\[
F_-(2/5,1/25,1/10)-1
=\frac{2159560547}{3814697265625}>0.
\]
The proof itself supplies all sign arguments and quantifiers; symbolic checks do not replace an infinite-domain proof.

## Relationship to prior work

Allu and Kumar (2026) introduced the positive quadratic target \(1+z+(m/n)z^2\), verified its Ma--Minda admissibility and calculated sharp second and third Hankel determinants. They did not discuss Schwarzian norms, quasiconformal extensions, or continuation to negative parameters.

Kanas and Sugawa (2011), Theorem 2.1, is the most relevant general result: it provides a **sharp variational formula** for the Schwarzian norm of *every* Ma--Minda-type subordinate class, including arbitrary analytic targets with value \(1\) at the origin. This general reduction contains the ingredients needed to pose the present optimization; it does not evaluate the complete signed quadratic-target interval, identify the radical phase boundary, classify all equality cases in that family, or give the sum-of-squares threshold certificate. The present result is an explicit parameter-phase solution and extremizer classification of that nontrivial specialization, rather than a claim that no general Schwarzian reduction previously existed.

Work on Janowski-convex Schwarzian norms concerns rational targets; work on pre-Schwarzian norms for other quadratic Ma--Minda functions treats a different invariant and normalization. Searches for the signed quadratic target, its radical threshold, the Schwarzian norm-one phase, and rotational extremizer rigidity found no exact equivalent statement.

## Limitations

The sharp claim is the **unit-Schwarzian norm threshold** inside the full real target-univalence range \(|c|\le1/2\); it is not the exact value of \(\sup_f\|S_f\|\) for subcritical \(c\). In particular, \(\|S_f\|>1\) below the threshold does **not** show the failure of any particular quasiconformal extension constant: Ahlfors--Weill is sufficient, not necessary.

The universal extension bound \(K\le3\) is not claimed to be the smallest possible quasiconformal dilatation for the family. For negative \(c\), the target need not have positive real part; no convexity assertion is made there. No claims are made for complex \(c\) or for \(|c|>1/2\).

## References

1. V. Allu and S. Kumar, *Sharp Estimates of Hankel Determinants for certain classes of convex univalent functions*, arXiv:2604.16833v1, first posted 18 April 2026.
2. S. Kanas and T. Sugawa, *Sharp norm estimate of Schwarzian derivative for a class of convex functions*, Annales Polonici Mathematici **101** (2011), 75--86, DOI:10.4064/ap101-1-8.
3. M. F. Ali and S. Pal, *The Schwarzian norm estimates for Janowski convex functions*, Proceedings of the Edinburgh Mathematical Society (2024).
4. R. Biswas, *Pre-Schwarzian norm estimation for functions in the Ma-Minda-type starlike and convex classes*, arXiv:2505.01910v1, first posted 3 May 2025.
