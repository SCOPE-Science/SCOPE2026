# Cubic overlap spectrum of minimal Reeve-prism lattice coverings

## Finding
For every integer \(m\ge2\), define the three-dimensional convex polytope
\[
K_m=\operatorname{conv}\{(0,0,0),(1,0,0),(0,1,0),(1,1,m)\}+[0,(0,0,1)].
\]
Its integer translates cover space, and the covering is inclusion-minimal (a previously established fact). On the unit fundamental cube \(F=[0,1)^3\), let
\[
N_m(u)=\#\{z\in\mathbb Z^3:u\in K_m+z\}.
\]
The distribution of the **entire integer-valued overlap multiplicity** is explicit. Write \(x_+=\max\{x,0\}\). For every integer \(k\ge2\),
\[
\Pr_{u\sim\mathrm{Unif}(F)}(N_m(u)\ge k)
=\frac m6\left[
\left(1-\frac{2(k-2)}m\right)_+^3-
\left(1-\frac{2(k-1)}m\right)_+^3
\right].\tag{1}
\]
Also \(\Pr(N_m\ge1)=1\); the individual level probabilities are differences of consecutive tails.

In particular, the essential/singly covered proportion of the fundamental domain is
\[
\boxed{\Pr(N_m=1)=\frac2m-\frac4{3m^2}.}\tag{2}
\]
The attainable positive-measure multiplicities are exactly \(1,2,\ldots,1+\lceil m/2\rceil\). Their mean and variance are
\[
\boxed{\mathbb E N_m=1+\frac m6,\qquad
\operatorname{Var}(N_m)=\frac{m^2}{72}+\frac16-
\frac{1-(-1)^m}{48m^2}.}\tag{3}
\]
Thus even and odd heights have an exact order-\(m^{-2}\) variance discrepancy. The subset of any one translate \(K_m+z\) whose interior is covered by no other lattice translate has volume \(2/m-4/(3m^2)\); its fraction of that translate's volume is exactly
\[
\boxed{\frac{4(3m-2)}{m^2(m+6)}\sim\frac{12}{m^2}.}\tag{4}
\]
Hence an inclusion-minimal lattice covering by eight-vertex convex polytopes can have unbounded covering density even as the essential fraction inside each translate tends to zero quadratically.

Moreover, under a coupling with a uniform \(u=(x,y,z)\in F\),
\[
\left|\frac{N_m(u)}m-\min\{x,1-x,y,1-y\}\right|\le\frac2m
\]
away from a measure-zero boundary set. Thus the normalized overlap multiplicity converges almost surely to a random variable whose survival function on \([0,1/2]\) is \((1-2t)^2\).

## Assumptions and scope
Lebesgue volumes are standard Euclidean volumes. The measure on \(F\) is normalized volume (\(\operatorname{vol}F=1\)); equalities about multiplicity and uniqueness are almost-everywhere statements, since boundary incidences can change counts. The parameter \(m\) is an integer at least two. The translated-body index is the full integer lattice \(\mathbb Z^3\), not a lattice optimized for covering density. In particular, inclusion-minimality is relative to this fixed lattice.

## Proof
**Fibers and reduction to one variable.** The horizontal projection of \(K_m\) is \([0,1]^2\). For \(0<x,y<1\), only the zero horizontal lattice translate can contain \((x,y,z)\), except for a null boundary set. The fiber over \((x,y)\) is the vertical interval
\[
[a,b+1],\quad a=m\max\{0,x+y-1\},\quad b=m\min\{x,y\}.
\]
This equality is established by barycentric coordinates and is also recorded in Lian--Xue, Section 4.2. The length equals
\[
L=1+mT,\qquad T=\min\{x,1-x,y,1-y\},
\]
by a four-case comparison (for \(x+y\le1\), \(T=\min(x,y)\); for \(x+y\ge1\), \(T=\min(1-x,1-y)\)). For an interval of length \(L\), the count of its integer translates containing a uniform height modulo one has values \(\lfloor L\rfloor\) and \(\lfloor L\rfloor+1\), with respective probabilities \(1-\{L\}\) and \(\{L\}\). This follows by moving the interval's left endpoint once around the circle \(\mathbb R/\mathbb Z\).

**Exact cubic tails.** For uniform independent \(x,y\in[0,1)\), the event \(T>t\) is the centered square \((t,1-t)^2\). Consequently
\[
\Pr(T>t)=(1-2t)^2,\quad 0\le t\le\frac12;
\qquad f_T(t)=4(1-2t).
\]
Conditional on \(T\), for \(k\ge2\) the probability of \(N_m\ge k\) is
\[
\min\{1,\max\{0,mT-(k-2)\}\}.
\]
The identity \(\min\{1,(s-a)_+\}=\int_a^{a+1}\mathbf 1\{s>v\}\,dv\) gives
\[
\Pr(N_m\ge k)=\int_{k-2}^{k-1}\Pr(mT>v)\,dv
=\int_{k-2}^{k-1}\left(1-\frac{2v}{m}\right)_+^2\,dv,
\]
which integrates exactly to (1). The support assertion follows by locating the last nonzero tail. For \(m\ge2\), setting \(k=2\) in (1) and subtracting from one proves (2).

**Mean, variance, and parity.** Conditional on \(T\), the count has mean \(1+mT\) and variance \(\{mT\}(1-\{mT\})\). Direct integration with the above triangular density gives \(\mathbb ET=1/6\) and \(\operatorname{Var}(T)=1/72\). Hence
\[
\operatorname{Var}(N_m)=\frac{m^2}{72}+\frac4m\int_0^{m/2}
\left(1-\frac{2s}m\right)\{s\}(1-\{s\})\,ds.
\]
If \(m=2q\), partitioning into \(q\) complete unit intervals gives the final integral contribution exactly \(1/6\). If \(m=2q+1\), partition into \(q\) complete intervals and the final half interval; on each complete interval \([j,j+1]\) the *unnormalized* integrand integrates to \((1-(2j+1)/m)/6\), while the final half interval contributes \(1/(32m)\). Multiplication by \(4/m\) gives \(1/6-1/(24m^2)\). This proves (3).

**Essential fraction and limit.** Lian--Xue establish that \(K_m\) is inclusion-minimal and has volume \(1+m/6\). Since every uniquely covered lattice orbit has exactly one covering translate, periodic integration yields
\[
\operatorname{vol}\{u\in K_m:N_m(u)=1\}=\int_F\mathbf1_{\{N_m=1\}}\,du.
\]
More explicitly, summing translates of the left integrand over \(F\) gives \(N_m(u)\mathbf1_{\{N_m(u)=1\}}\). Combining this equality with (2) and dividing by \(1+m/6\) proves (4). Finally, for almost every \(u\), the two-point rounding rule gives \(1+mT\le N_m+1\le mT+3\), and hence the stated uniform error bound \(|N_m/m-T|\le2/m\). The exact survival function of \(T\) yields the limiting law.

## Verification
The standalone standard-library checker `cover_profile_check.py` uses exact rational arithmetic. It compares (1) against independently summed even/odd level probabilities and verifies normalization and both moments for \(1\le m\le70\). It then independently enumerates vertical translate membership at 101,200 rational interior sample points for \(1\le m\le13\), excluding 2,800 boundary points; it checks the claimed local rounding law directly from the defining polytope's fiber inequalities. Successful execution prints `COVER_PROFILE_CHECK_OK`. These are finite independent diagnostic tests, not the source of the infinite-parameter proof.

## Relationship to prior work
Lian and Xue (2026) introduce the minimal covering family \(K_m\), prove its lattice covering and inclusion-minimality, and supply the explicit fiber endpoints and total volume. Those structural input facts are **not** new here. The present finding instead determines the full *multiplicity distribution* of lattice translates, the parity-sensitive variance, the measure of the essential region, and a quantitative almost-sure limiting profile. The fiber formula makes these further calculations possible, but those distributional conclusions are not stated in the cited treatment. Codenotti, Freyer, and Krivokuća (2026) develop a general unit-interval lift construction and prove minimality criteria; the inspected material does not analyze exact overlap multiplicity laws for the Reeve family. The possibility of earlier unindexed computations of this profile remains.

## Limitations
No result is claimed about the *optimal* covering lattice or about all minimal covering bodies. The constant in (4) is specific to these integral Reeve-prism bodies. The formula is a distributional analysis of an existing explicit construction, not a new construction of minimal coverings. Its originality depends on the absence of an earlier computation of the same multiplicity law; the underlying fiber description is already known. Boundary multiplicities may differ from the almost-everywhere profile. Finite tests do not independently certify the general proof.

## References
1. Y. Lian and F. Xue, *Minimal Covering Bodies and a Minkowski-Type Criterion for Lattice Coverings*, arXiv:2606.14584, first posted 2026-06-12, Section 4.2 (fiber formula, covering minimality, and volume), https://arxiv.org/html/2606.14584.
2. G. Codenotti, A. Freyer, and K. Krivokuća, *Minimal covering bodies and Brunn-Minkowski type inequalities for the covering radius*, arXiv:2606.14442, first posted 2026-06-12, Section 2.1 (unit-segment lift construction), https://arxiv.org/pdf/2606.14442.
