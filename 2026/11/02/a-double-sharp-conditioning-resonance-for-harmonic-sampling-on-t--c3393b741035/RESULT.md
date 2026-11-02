# A double sharp conditioning resonance for harmonic sampling on the \(A_4\) roots

## Finding
Let \(W=\{x\in\mathbb R^5:\sum_{i=1}^{5}x_i=0\}\), and let \(X=\{(e_i-e_j)/\sqrt2:i\ne j\}\subset S(W)\cong S^3\), the twenty unit roots of \(A_4\). For \(k\ge0\), let \(E_k\) evaluate all real spherical harmonics of exactly degree \(k\) at \(X\). Its rank for \(k=0,1,2\) is respectively \(1,4,9\), and its rank is exactly \(10\) for **every** \(k\ge3\). The rank cap of ten is the antipodal parity obstruction.

For the ten representatives \(r_{ij}=(e_i-e_j)/\sqrt2\) with \(1\le i<j\le5\), form the normalized Gegenbauer sampling Gram matrix
\[
 G_k=\left[\frac{U_k(\langle r_{ij},r_{pq}\rangle)}{k+1}\right]_{ij,pq},
\]
where \(U_k(\cos\theta)=\sin((k+1)\theta)/\sin\theta\), continuously interpreted at endpoints. At every degree \(k\ge3\), the following **sharp, simultaneous, all-degree** bounds hold:
\[
 \frac2{11}\,I_{10}\preceq G_k\preceq\frac{22}{13}\,I_{10},\qquad
 \kappa_2(G_k)\le6.
\]
The lower spectral bound is achieved **only in degree ten**, the upper bound **only in degree twelve**, and the sharp condition number \(6\) is achieved **exactly at degrees three and ten**. Conversely \(G_k=I_{10}\) (perfectly conditioned sampling) holds exactly for \(k\equiv5\pmod6\), giving infinitely many separated tight degrees.

Consequently, for all \(k\ge3\), the two neighboring exact-degree spaces \(\mathcal H_k(S^3)\oplus\mathcal H_{k+1}(S^3)\) interpolate arbitrary real data on all twenty roots, and \(k=3\) is the sharp starting-degree threshold.

## Assumptions and scope
All vectors are Euclidean unit vectors in the four-dimensional real inner-product space \(W\). The degree \(k\) is any nonnegative integer. The spherical harmonics are restrictions of homogeneous, real-valued harmonic polynomials on \(W\) of degree \(k\). The matrix \(G_k\) is the **ten-by-ten** normalized evaluation Gram matrix on one oriented representative of each antipodal pair; it is not the unnormalized twenty-by-twenty Gram matrix. The latter has the same positive spectral condition number, its nonzero eigenvalues being exactly twice those of \(G_k\). The normalized zonal kernel has diagonal entries one; no normalization of harmonic basis is assumed beyond the standard addition theorem.

## Proof
**Step 1: exact two- and three-sector spectra.** The normalized addition theorem on \(S^3\) identifies \(P_k(t)=U_k(t)/(k+1)\) as the positive-semidefinite exact-degree reproducing kernel with \(P_k(1)=1\). Any two distinct representatives have inner product \(0\) when their underlying pairs are disjoint, and \(\pm\tfrac12\) when they meet in one vertex. Write \(a_k=P_k(\tfrac12)\) and \(b_k=P_k(0)\).

For odd \(k\), let \(B\) be the \(5\)-by-\(10\) signed vertex-edge incidence matrix of the complete graph on five vertices, with column \(e_i-e_j\) for \(i<j\). The Gram is \(G_k=(1-2a_k)I+a_kB^\top B\). Since \(BB^\top=5I_5-J_5\), the spectrum is
\[
 1+3a_k\quad(\text{multiplicity }4),\qquad
 1-2a_k\quad(\text{multiplicity }6).
\]
For even \(k\), let \(A\) be adjacency of the triangular graph \(J(5,2)\) on the ten unordered pairs. Since \(A\) has eigenvalues \(6,1,-2\) with multiplicities \(1,4,5\), respectively, and \(G_k=I+a_kA+b_k(J-I-A)\), its spectrum is
\[
 \begin{aligned}
 1+6a_k+3b_k&\quad(\text{multiplicity }1),\\
 1+a_k-2b_k&\quad(\text{multiplicity }4),\\
 1-2a_k+b_k&\quad(\text{multiplicity }5).
 \end{aligned}
\]
The Johnson eigenvalues follow directly from the unsigned vertex-edge incidence matrix \(C\): \(CC^\top=3I_5+J_5\), so \(C^\top C-2I=A\). Thus its eigenvalues are \(6,1,-2\) as asserted.

**Step 2: exact arithmetic and low degrees.** The Chebyshev identity gives
\[
 a_k=\frac{\sin((k+1)\pi/3)}{(k+1)\sin(\pi/3)}\in\left\{0,\pm\frac1{k+1}\right\},\qquad
 b_k=\frac{\sin((k+1)\pi/2)}{k+1},
\]
with \(b_k=0\) for odd \(k\) and \(b_k=(-1)^{k/2}/(k+1)\) for even \(k\). Direct substitution for \(k=0,1,2\) gives nonzero-rank counts \(1,4,9\). For degrees \(3,4,6,8,10,12\), the respective complete nonzero spectral lists, with multiplicities as in Step 1, are
\[
 \begin{array}{c|c}
 k&\text{spectral values (including repetitions by sectors)}\\\hline
 3&(\tfrac14,\tfrac32)\\
 4&(\tfrac25,\tfrac25,\tfrac85)\\
 6&(\tfrac{10}7,\tfrac{10}7,\tfrac47)\\
 8&(\tfrac43,\tfrac79,\tfrac{10}9)\\
 10&(\tfrac2{11},\tfrac{12}{11},\tfrac{12}{11})\\
 12&(\tfrac{22}{13},\tfrac{12}{13},\tfrac{12}{13}).
 \end{array}
\]
Every odd \(k\equiv5\pmod6\) has \(a_k=b_k=0\), hence \(G_k=I\).

**Step 3: infinite-degree bounds and sharpness.** For odd \(k\ge5\), \(|a_k|\le1/(k+1)\). Both eigenvalues therefore lie in \([1-3/(k+1),1+3/(k+1)]\subset[\tfrac12,\tfrac32]\), and their condition number is at most \(3\). At \(k=3\), the eigenvalues are \(\tfrac14,\tfrac32\), giving condition number \(6\).

For every even \(k\ge12\), \(|a_k|,|b_k|\le1/(k+1)\), hence every eigenvalue lies in \([1-9/(k+1),1+9/(k+1)]\). This interval is positive. The condition number is at most \((k+10)/(k-8)\le\tfrac{11}2<6\). At \(k\ge14\), the same interval is included in \([\tfrac25,\tfrac85]\), strictly inside \([\tfrac2{11},\tfrac{22}{13}]\); degree twelve gives the exact upper endpoint. Comparing the finite values at even degrees \(4,6,8,10\) and odd degree three proves both uniform frame endpoints, their unique degrees of attainment, and the two and only two degrees with condition number \(6\). It also proves positivity and rank ten at all \(k\ge3\).

**Step 4: tightness and twenty-point interpolation.** For odd degrees, \(b_k=0\), and \(G_k=I\) iff \(a_k=0\), namely \(k\equiv5\pmod6\); for even degrees \(b_k\ne0\) and the off-diagonal entries prevent \(G_k=I\). The full root configuration consists of ten antipodal pairs, so exact-degree data must satisfy \(f(-x)=(-1)^k f(x)\). Positive rank ten of \(G_k\) is precisely the ability to realize every such parity-compatible datum. Combining two consecutive degrees with opposite parity realizes arbitrary twenty-point data for \(k\ge3\). Degrees zero through two have ranks \(1,4,9\), so earlier consecutive pairs cannot be surjective.

## Verification
The standalone pure-Python checker `check_a4.py` constructs all ten oriented root representatives, evaluates the normalized Chebyshev kernel by integer recurrence using exact rational arithmetic, independently constructs signed/unsigned incidence projectors, and checks the exact \(10\)-by-\(10\) matrix decomposition for every \(0\le k\le300\). It also checks sector ranks, exceptional eigenvalues, frame bounds and condition-number equality cases over that finite range. Run with `python3 check_a4.py`; successful execution prints `A4_HARMONIC_EXACT_CHECK_OK`. The infinite-degree assertions follow from Steps 1–4, **not** from the finite check.

## Relationship to prior work
Bannai, Okuda and Tagami (2013, arXiv:1308.5101) introduce harmonic-index designs and the zonal Gegenbauer/reproducing-kernel framework. That framework yields the positive semidefiniteness used here but does not itself provide the explicit \(A_4\) evaluation spectrum, all-degree tightness congruence, or the sharp degree-uniform spectral bounds. The triangular graph \(J(5,2)\) and its three adjacency eigenspaces are classical; their explicit coupling to the odd signed-incidence sectors and the trigonometric degree dependence yields the present classification. This is a new statement conditional on the bounded comparison below, not a claim that Johnson-scheme or addition-theorem machinery is new.

## Limitations
The result is specific to the twenty normalized \(A_4\) roots in four ambient dimensions, with exact-degree harmonics and the stated normalization. It does not assert the corresponding sharp constants for other \(A_n\) root systems, perturbations, or arbitrary sample sets. Source comparison is bounded and not an independent literature audit; an equivalent all-degree frame calculation may exist in older association-scheme, root-system, or cubature sources. Exact computation through degree three hundred is supplementary; independent mathematical audit has not been performed.

## References
1. E. Bannai, T. Okuda, M. Tagami, *Spherical designs of harmonic index \(t\)*, arXiv:1308.5101, first posted 2013-08-23. https://arxiv.org/abs/1308.5101
2. P. Delsarte, J. M. Goethals, J. J. Seidel, *Spherical codes and designs*, Geometriae Dedicata 6 (1977), 363–388, DOI:10.1007/BF03187604 (classical background; not independently compared in full text).
3. Classical eigenvalue formulas for the triangular Johnson graph \(J(5,2)\); the needed formulas are also derived directly in the proof.
