# Integral spectrum and transversal profile of the 48 Fermat-quartic lines
## Finding
For the complex Fermat quartic
\[
X:\quad x_0^4+x_1^4+x_2^4+x_3^4=0,
\]
let \(\Gamma\) be the graph whose vertices are the 48 lines on \(X\), with two vertices adjacent when the corresponding lines meet. Then \(\Gamma\) is \(14\)-regular and
\[
\chi_\Gamma(t)=(t-14)(t-2)^{28}(t+2)^{12}(t+6)^6(t+10).
\]
There are \(792\) unordered skew pairs of Fermat lines. The number of Fermat lines meeting both members of such a pair is \(2,4,6,\) or \(10\), with respective pair counts
\[
96,\quad 192,\quad 480,\quad 24.
\]
Equivalently, the skew-pair common-transversal profile is
\[
2^{\times96},\ 4^{\times192},\ 6^{\times480},\ 10^{\times24}.
\]
If \(A\) denotes the adjacency matrix of \(\Gamma\), then the full line-intersection Gram matrix is \(G=A-2I\). Hence
\[
\operatorname{Spec}(G)=
12^1,\ 0^{28},\ (-4)^{12},\ (-8)^6,\ (-12)^1,
\]
so \(G\) has rank \(20\) and inertia \((1,19,28)\).

## Assumptions and scope
Work is over \(\mathbb C\). The 48 lines are the complete line set on the Fermat quartic. A “common transversal” here means another line among these 48 Fermat lines that meets both members of the given skew pair; no assertion is made about arbitrary lines in ambient projective space.

Choose \(\rho=e^{\pi i/4}\) and put \(r_j=\rho i^j\) for \(j\in\mathbb Z/4\mathbb Z\), so \(r_j^4=-1\). The 48 lines split into three 16-line families:
\[
A_{ab}:\ x_0=r_a x_1,\ x_2=r_b x_3,
\]
\[
B_{ab}:\ x_0=r_a x_2,\ x_1=r_b x_3,
\]
\[
C_{ab}:\ x_0=r_a x_3,\ x_1=r_b x_2,
\]
where \(a,b\in\mathbb Z/4\mathbb Z\).

## Proof
Each displayed line lies on \(X\), and the cited complete classification of the Fermat quartic's lines shows that these 48 lines exhaust the line set.

Solving the corresponding pairs of linear equations gives exact incidence rules. Distinct lines in the same family meet exactly when precisely one index agrees. For different families,
\[
A_{ab}\cap B_{cd}\neq\varnothing
\iff a+d\equiv b+c\pmod4,
\]
\[
A_{ab}\cap C_{cd}\neq\varnothing
\iff c\equiv a+b+d+1\pmod4,
\]
and
\[
B_{ab}\cap C_{cd}\neq\varnothing
\iff a+b\equiv c+d\pmod4.
\]
These congruences define the \(48\times48\) adjacency matrix \(A\) exactly. Direct enumeration gives row sum \(14\) for every row and \(336\) edges. Exact integer characteristic-polynomial computation yields
\[
\det(tI-A)=(t-14)(t-2)^{28}(t+2)^{12}(t+6)^6(t+10).
\]

For two distinct nonadjacent vertices \(\ell,m\), the entry \((A^2)_{\ell m}\) is exactly the number of Fermat lines adjacent to both, hence the number of Fermat-line common transversals. Exhausting all \(\binom{48}{2}-336=792\) skew pairs gives the stated profile.

Finally, on a smooth quartic K3 surface each line has self-intersection \(-2\), while two distinct lines have intersection number \(1\) when they meet and \(0\) otherwise. Thus \(G=A-2I\), so its spectrum is obtained by subtracting \(2\) from every adjacency eigenvalue. This gives rank \(20\) and inertia \((1,19,28)\).

## Verification
The accompanying checker reconstructs the 48 labeled vertices and the exact congruence incidence rules, verifies that all vertex degrees are \(14\), computes the characteristic polynomial over the integers, enumerates every skew pair through \(A^2\), and checks the shifted Gram-matrix rank. Its successful terminal line is
`VERIFY_OK lines=48 degree=14 edges=336 skew=792 profile=2:96,4:192,6:480,10:24 gram_rank=20 inertia=1,19,28`.

The finite enumeration is exhaustive for the complete 48-line set; it is not being used as evidence for an infinite classification.

## Relationship to prior work
Veniani treats Fano configurations and symmetries of smooth quartics with many lines and explicitly discusses the Fermat quartic \(X_{48}\). Shimada and Shioda give the complete 48-line configuration in explicit coordinates and compute a rank-20 Néron–Severi basis. Degtyarev and Rams place the Fermat configuration at the 48-line threshold in their classification of larger quartic line configurations.

The present statement refines those structural descriptions by giving the complete integral spectrum of the 48-vertex intersection graph and the common-transversal census for every skew pair. The previously known rank \(20\) does not determine either the characteristic polynomial or the skew-pair profile.

## Limitations
No claim is made that the graph is determined up to isomorphism by its spectrum, that the listed common-transversal numbers classify skew pairs under the full automorphism group, or that the 48 lines exhaust ambient projective transversals to a skew pair. A residual literature risk remains that an older classical incidence table encodes the same finite graph invariants without modern spectral terminology.

## References
1. D. C. Veniani, *Symmetries and equations of smooth quartic surfaces with many lines*, arXiv:1708.01219, first public version 2017-08-03.
2. I. Shimada and T. Shioda, *On a smooth quartic surface containing 56 lines which is isomorphic as a K3 surface to the Fermat quartic*, arXiv:1604.06265.
3. A. Degtyarev and S. Rams, *Lines on K3-quartics via triangular sets*, arXiv:2301.04127.
