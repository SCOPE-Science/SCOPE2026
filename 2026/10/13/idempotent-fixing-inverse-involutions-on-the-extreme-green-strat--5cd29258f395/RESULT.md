# Idempotent-fixing inverse involutions on the extreme Green strata of isotone monoids

## Finding
For every integer \(n\ge4\), let \(\mathcal O_n\) be the transformation monoid of nondecreasing maps on the chain \([n]=\{1,\ldots,n\}\). Let \(D_r\subset\mathcal O_n\) consist of the transformations of rank \(r\). The two natural nontrivial extreme strata, \(D_2\) and \(D_{n-1}\), each admit an **explicit involution** \(\tau_r:D_r\to D_r\) satisfying
\[
 f\tau_r(f)f=f,\qquad \tau_r(f)f\tau_r(f)=\tau_r(f),\qquad
 \tau_r^2(f)=f.
\]
The fixed points of \(\tau_r\) are **exactly all idempotents** in that stratum. In particular the fixed-point counts and two-cycle counts are
\[
\begin{array}{c|cc}
 & \#\operatorname{Fix}(\tau_r)&\#\text{two-cycles}\\\hline
r=2&\binom{n+1}{3}&\binom n3\\
r=n-1&2(n-1)&\binom{n-1}{2}.
\end{array}
\]
The fixed-point counts are maximal among all involutive inverse matchings on these strata, since a fixed point of any inverse matching of order-preserving transformations must be idempotent.

## Assumptions and scope
A *mutual inverse* of a semigroup element \(f\) is an element \(g\) with \(fgf=f\) and \(gfg=g\). An *involutive inverse matching* on \(D_r\) is a permutation \(\tau_r\) of order at most two assigning each element a mutual inverse in the same stratum. Products of transformations are composition; the two inverse equations are independent of composition orientation.

**Rank two.** Every \(f\in D_2\) has a unique triple \((a;b,c)\), where \(1\le a<n\) and \(1\le b<c\le n\), meaning \(f(i)=b\) for \(i\le a\) and \(f(i)=c\) for \(i>a\). Define
\[
\tau_2(a;b,c)=
\begin{cases}
(c-1;a,b),&a<b,\\
(a;b,c),&b\le a<c,\\
(b;c,a+1),&c\le a.
\end{cases}
\]

**Corank one.** Every \(f\in D_{n-1}\) has unique parameters \((d,m)\), where its one nonsingleton kernel class is \(\{d,d+1\}\), \(1\le d<n\), and the missing value in its image is \(m\in[n]\). Write the unique isotone transformation specified by these parameters as \([d;m]\). Define
\[
\tau_{n-1}[d;m]=
\begin{cases}
[m;d+1],&m<d,\\
[d;m],&m\in\{d,d+1\},\\
[m-1;d],&m>d+1.
\end{cases}
\]
These definitions require no parity restriction on \(n\).

## Proof
**Mutual inverse criterion.** Let \(f,g\in D_r\). Write \(A_1<\cdots<A_r\) for the consecutive interval kernel classes of \(f\), and \(v_1<\cdots<v_r\) for its image points; let \(B_i\) and \(w_i\) be the corresponding data for \(g\). Then \(fgf=f\) and \(gfg=g\) if and only if \(w_i\in A_i\) and \(v_i\in B_i\) for every \(i\). Indeed, the inverse equations force \(g\) to restrict to a bijection from \(\operatorname{im}(f)\) to a transversal of \(f\)'s kernel, and vice versa. Both restrictions are increasing and hence match increasing positions, proving necessity; conversely, substituting the two transversal conditions into the composite proves the identities.

For rank two, a candidate inverse \((d;e,h)\) satisfies the criterion precisely when
\[
 e\le a<h,\qquad b\le d<c.
\]
If \(a<b\), the first displayed formula gives \((d;e,h)=(c-1;a,b)\): indeed \(a\le a<b\) and \(b\le c-1<c\). Applying the formula again uses the branch \(h\le d\) and returns \((a;b,c)\). If \(c\le a\), the formula gives \((b;c,a+1)\), again satisfying the two inequalities; this time the reverse application uses \(d<e\) and returns the initial triple. In the remaining case \(b\le a<c\), the original map is idempotent, and is fixed. These branches exhaust the admissible triples, so \(\tau_2\) is an involutive inverse matching. The idempotent condition is exactly \(b\le a<c\).

For rank \(n-1\), the image \([n]\setminus\{m\}\) is a transversal of the kernel with double block \(\{d,d+1\}\) if and only if \(m\in\{d,d+1\}\). Consequently, \([e;k]\) is a mutual inverse of \([d;m]\) precisely when
\[
 k\in\{d,d+1\},\qquad m\in\{e,e+1\}.
\]
The displayed cases for \(\tau_{n-1}\) meet these two conditions. The two strict branches exchange: \(m<d\) gives \([m;d+1]\), whose new missing value exceeds its new doubled position by at least two, and the reverse branch sends it back to \([d;m]\); similarly for the opposite branch. The central branch consists exactly of idempotents. Hence \(\tau_{n-1}\) is an involutive inverse matching with precisely the asserted fixed points.

**Enumeration.** At rank two, the \(a\)-th kernel cut contributes \(a(n-a)\) idempotents (choose \(b\le a\) and \(c>a\)), so
\[
 \#\operatorname{Fix}(\tau_2)=\sum_{a=1}^{n-1}a(n-a)=\binom{n+1}{3}.
\]
Non-idempotent triples in the branch \(a<b<c\) correspond bijectively to three-element subsets of \([n]\), and each forms one transposition with its partner in the opposite branch. Thus there are \(\binom n3\) two-cycles. At rank \(n-1\), there are two idempotents for each \(d\), giving \(2(n-1)\) fixed points; the branch \(m<d\) has \(\sum_{d=1}^{n-1}(d-1)=\binom{n-1}{2}\) elements, one per two-cycle.

**Optimality.** If \(f\) is its own mutual inverse, then \(f^3=f\). On the finite chain \(Y=\operatorname{im}(f)\), this implies that the restriction of \(f\) to \(Y\) is an increasing involutive permutation. An increasing permutation of a finite chain is the identity. Therefore \(f^2=f\). Thus any inverse matching can fix only idempotents, and our matchings fix every one, attaining the greatest possible number of fixed points.

## Verification
Run the self-contained `verify.py` with Python 3. It enumerates all elements in \(D_2\) and \(D_{n-1}\) for \(3\le n\le12\), independently constructs their full image tuples, checks both mutual-inverse equations, involutivity, the equivalence of fixed points and idempotency, and the two exact orbit-count formulas. Execution completed with `EXHAUSTIVE_INVERSE_IDENTITIES_AND_FIXED_POINT_COUNTS_OK` and `VERIFY_OK`. Exhaustive finite tests do not prove the universal quantifier; the proof above does.

## Relationship to prior work
Higgins (2026, arXiv:2610.01912v1) proves existence of a *permutation* matching of the entire order-preserving transformation monoid using balanced weightings, not the explicit idempotent-fixing involutive formulas above. Higgins (2024, DOI:10.1007/s00233-024-10430-0) includes a sufficient numerical criterion for involutive matchings of rectangular incidence classes; for rank two its integer-ratio case already yields **existence** for even \(n\), which is not claimed as new here. The present statements specify a canonical piecewise matching for **all** \(n\), identify **all** fixed points and count the cycles. Higgins (2019, arXiv:1811.04472) constructs inverse involutions in the larger orientation-preserving transformation semigroup; these involutions need not preserve the submonoid of order-preserving chain maps. Catarino, Higgins and Levi (2015) study inverse *subsemigroups*, a different condition from a set-theoretic matching. These distinctions do not certify absence of an older equivalent formula.

## Limitations
The construction does **not** provide an idempotent-fixing inverse involution on arbitrary intermediate Green strata. There is a genuine obstruction: in \(\mathcal O_5\), rank three has \(60\) elements but just \(21\) idempotents; the remaining odd number \(39\) cannot all be paired by a fixed-point-free involution, while no non-idempotent can be fixed in any inverse matching. No claim is made about an involution of the *entire* monoid, or about other types of semigroup inverse. Earlier equivalent work using other matching terminology may exist.

## References
1. P. M. Higgins, *Balanced weightings and permutation matchings applied to the monoid of order-preserving mappings*, arXiv:2610.01912v1, first submitted 2026-10-01, https://arxiv.org/abs/2610.01912.
2. P. M. Higgins, *Finite regular semigroups with permutations that map elements to inverses*, Semigroup Forum (2024), DOI:10.1007/s00233-024-10430-0.
3. P. M. Higgins, *Involution matchings, the semigroup of orientation-preserving and orientation-reversing mappings, and inverse covers of the full transformation semigroup*, Semigroup Forum 98 (2019), 669–689; arXiv:1811.04472.
4. P. Catarino, P. M. Higgins and I. Levi, *On inverse subsemigroups of the semigroup of orientation-preserving or orientation-reversing transformations*, Algebra and Discrete Mathematics 19 (2015), 162–171.
