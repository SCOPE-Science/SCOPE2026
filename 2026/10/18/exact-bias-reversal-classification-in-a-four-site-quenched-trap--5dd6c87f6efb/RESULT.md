# Exact bias-reversal classification in a four-site quenched-trap exclusion ring

## Finding

Consider the continuous-time asymmetric simple exclusion process on a four-site ring containing three particles and one vacancy, with positive site-dependent escape rates \(a,b,c,d\). A particle at site \(i\) jumps clockwise into an empty neighboring site at rate \(((1+\varepsilon)/2)w_i\) and anticlockwise at rate \(((1-\varepsilon)/2)w_i\), where \(w=(a,b,c,d)\) and \(|\varepsilon|<1\). Let \(J(\varepsilon)\) be the stationary clockwise particle current across a single specified bond.

Put
\[
U=a+c,\quad V=b+d,\quad x=a-c,\quad y=b-d,\quad \Delta=xy(U-V),
\]
\[
H=UV(U+V)-2(Vx^2+Uy^2),
\]
and
\[
P(\varepsilon)=UV(U+V)+\varepsilon^2H+\varepsilon(1-\varepsilon^2)\Delta.
\]
The exact steady current is
\[
\boxed{J(\varepsilon)=\frac{4abcd\,\varepsilon(1+\varepsilon^2)}{P(\varepsilon)}.}
\]
For all positive \(a,b,c,d\) and all \(|\varepsilon|<1\), the denominator is strictly positive. The **complete bias-reversal classification**, including non-reflection-symmetric environments, is
\[
\boxed{J(\varepsilon)=-J(-\varepsilon)\text{ for every }|\varepsilon|<1
\iff (a-c)(b-d)(a+c-b-d)=0.}
\]
If \(0<|\varepsilon|<1\) and \(\Delta\ne0\), then \(J(\varepsilon)+J(-\varepsilon)\) is nonzero and has sign \(-\operatorname{sgn}(\Delta)\), independently of the magnitude of \(\varepsilon\). In particular the current can be exactly odd even without spatial inversion symmetry: \((a,b,c,d)=(1,2,4,3)\) has \(a\ne c\), \(b\ne d\), equal opposite-site rate sums, and no reflection symmetry.

The exact first even response coefficient is
\[
\boxed{[\varepsilon^2]J(\varepsilon)=
-\frac{4abcd\,(a-c)(b-d)(a+c-b-d)}
{(a+c)^2(b+d)^2(a+b+c+d)^2}.}
\]
Thus vanishing of the quadratic response is equivalent, in this four-state system, to full oddness of the stationary current at **all** physical biases, rather than merely a perturbative cancellation.

## Assumptions and scope

Sites are \(0,1,2,3\) in clockwise order, with site escape rates \(w_0=a,w_1=b,w_2=c,w_3=d>0\). There are exactly three indistinguishable hard-core particles; hence exactly one hole. Hops into occupied sites are suppressed. The physical bias satisfies \(|\varepsilon|<1\); then every permitted rate is strictly positive, giving an irreducible continuous-time Markov chain with a unique stationary law. The current is the mean clockwise number of particles crossing bond \(0\to1\) per unit time, minus the anticlockwise number. Stationarity makes it the same at each bond. The theorem is for these four sites and three particles only; it does not infer a corresponding criterion for arbitrary particle counts or system sizes.

## Proof

Let \(h\in\{0,1,2,3\}\) be the hole position and set \(p=(1+\varepsilon)/2\), \(q=(1-\varepsilon)/2\). A hole at site \(h\) moves to \(h+1\pmod4\) at rate \(r_h=qw_{h+1}\), and to \(h-1\pmod4\) at rate \(\ell_h=pw_{h-1}\). These are precisely the particle-hop rates into the empty site. For each root \(h\), define
\[
\tau_h=r_{h+1}r_{h+2}r_{h+3}
+\ell_{h+1}r_{h+2}r_{h+3}
+\ell_{h+1}\ell_{h+2}r_{h+3}
+\ell_{h+1}\ell_{h+2}\ell_{h+3},
\]
with cyclic subscripts. Each term is a directed spanning tree of the four-cycle oriented toward the root \(h\), obtained by deleting one of the four undirected edges. Hence, by direct stationary balance (equivalently the finite Markov-chain tree formula), the stationary hole probability is \(\pi_h=\tau_h/Z\), where \(Z=\sum_{h=0}^3\tau_h>0\). Every summand is strictly positive when \(a,b,c,d>0\) and \(|\varepsilon|<1\).

Across bond \(0\to1\), a clockwise particle hop occurs precisely when the hole is at site \(1\), at rate \(pa\); the reverse occurs precisely when the hole is at site \(0\), at rate \(qb\). Thus
\[
J(\varepsilon)=\frac{pa\tau_1-qb\tau_0}{Z}.
\]
Expanding the four explicit tree weights and collecting terms gives the two **exact polynomial identities**
\[
pa\tau_1-qb\tau_0=\tfrac12 abcd\,\varepsilon(1+\varepsilon^2),
\qquad 8Z=P(\varepsilon).
\]
The expression for \(J\) follows immediately and \(P>0\) follows from \(P=8Z\). These identities are also symbolically rechecked by the accompanying standalone script, which constructs the tree weights independently from the asserted current formula.

Write \(E(\varepsilon)=UV(U+V)+\varepsilon^2H\) and \(S(\varepsilon)=\varepsilon(1-\varepsilon^2)\Delta\). Then \(P(\varepsilon)=E(\varepsilon)+S(\varepsilon)\) and \(P(-\varepsilon)=E(\varepsilon)-S(\varepsilon)\). Straight algebra therefore yields
\[
J(\varepsilon)+J(-\varepsilon)
=-\frac{8abcd\,\varepsilon^2(1+\varepsilon^2)(1-\varepsilon^2)\Delta}
{P(\varepsilon)P(-\varepsilon)}.
\]
The denominator is positive. For any fixed \(0<|\varepsilon|<1\), all displayed factors other than \(\Delta\) are positive, establishing both the stated global criterion and the strict sign classification. Taylor expansion at \(\varepsilon=0\), justified by the positive denominator, gives
\[
J(\varepsilon)=\frac{4abcd}{UV(U+V)}\varepsilon
-\frac{4abcd\Delta}{U^2V^2(U+V)^2}\varepsilon^2+O(\varepsilon^3),
\]
proving the quadratic coefficient and its equivalence with global oddness. This completes the four-site proof.

For completeness, the smaller nondegenerate three-site ring cannot exhibit this rectification. With two occupied sites and site rates \(a,b,c\), the analogous three rooted-tree sums give
\[
J_3(\varepsilon)=\frac{abc\,\varepsilon(3+\varepsilon^2)}
{(a+b+c)^2-\varepsilon^2[(a+b+c)^2-4(ab+bc+ca)]},
\]
which is odd for arbitrary positive rates. With one occupied site its stationary current is \(J_1(\varepsilon)=\varepsilon/(1/a+1/b+1/c)\), also odd. Thus four is the smallest nondegenerate ring on which the quenched-trap model can display a nonzero even-in-bias current. Both three-site identities follow by the same finite generator/tree calculation; no larger-ring conclusion follows.

## Verification

Run `python verify.py` with NumPy and SymPy installed. It constructs the four directed tree weights and checks **as polynomial identities**, for symbolic arbitrary \(a,b,c,d,\varepsilon\), that the tree-current ratio equals the rational formula, that the stated first two response coefficients agree with Taylor limits, and that the exact even-current formula holds. It separately constructs the continuous-time Markov generator, solves the stationary linear equations numerically for six heterogeneous rate quadruples and eight bias values (48 independent linear solves), and checks the parity and sign tests. A further nine three-site checks support, but are not needed for, the main theorem. The check is deterministic and was executed successfully. The proof above is finite exact algebra; the numerical calculations are cross-checks and make no infinite-size inference.

## Relationship to prior work

Sakai and Akimoto's *Symmetry Breaking of Current Response in Disordered Exclusion Processes*, arXiv:2512.03316 (first submitted 2025-12-03), introduces the same trap-type periodic exclusion rates, identifies a sufficient uniform-bond-bias condition, gives an inversion-correspondence mechanism, and studies symmetry breaking using mean-field perturbation and numerical simulations. Its single-particle exact current is also known. It does not state the all-bias four-site, three-particle current rational function, the necessary-and-sufficient polynomial cancellation locus at that fixed density, or the balanced-opposite-sublattice non-reflection family. The source's conditions address more global symmetry mechanisms; a specific-density accidental equality is not ruled out by their general symmetry discussion.

Sakai and Akimoto's *Sample-specific rectification-like response in a boundary-driven exclusion process*, arXiv:2609.03560, concerns a different geometry (two reservoirs, open boundaries) and density-contrast driving, rather than a periodic four-site fixed-particle ring. Kanai, Nishinari and Tokihiro's *Exact solution and asymptotic behaviour of the asymmetric simple exclusion process on a ring* concerns a different, homogeneous-rate formulation. None of these comparisons excludes possible implicit coverage by a more general formula for disordered finite Markov chains; the contribution claimed is the explicit physical classification, not a new stationary-state algorithm.

## Limitations

The theorem concerns precisely three particles and one vacancy on four periodic sites. It does not classify higher-density, longer-ring or random-disorder averaged systems; it makes no thermodynamic-limit claim. The balancing condition is one exact exceptional surface of escape rates and need not be robust under arbitrary rate perturbations. The published literature search may miss an earlier derivation hidden in general exact finite-state formulas. Independent external audit has not been performed.

## References

1. I. Sakai and T. Akimoto, *Symmetry Breaking of Current Response in Disordered Exclusion Processes*, arXiv:2512.03316, first posted 2025-12-03, https://arxiv.org/abs/2512.03316, Phys. Rev. E 113, 044123 (2026), DOI 10.1103/21vm-n8gp.
2. I. Sakai and T. Akimoto, *Sample-specific rectification-like response in a boundary-driven exclusion process*, arXiv:2609.03560, first posted 2026-09-03, https://arxiv.org/abs/2609.03560.
3. M. Kanai, K. Nishinari and T. Tokihiro, *Exact solution and asymptotic behaviour of the asymmetric simple exclusion process on a ring*, J. Phys. A 39, 9071 (2006), DOI 10.1088/0305-4470/39/29/004.
