# A rare-center parity law for finite-field Heisenberg Lie gradings

## Finding
For each prime power \(q\) and integer \(m\geq1\), let \(H=H_{2m+1}(\mathbb F_q)\) be the Heisenberg Lie algebra with its one-dimensional center \(Z\). Count labeled \(\mathbb Z_2\)-gradings as ordered pairs of subspaces \((H_0,H_1)\) satisfying \(H=H_0\oplus H_1\) and \([H_i,H_j]\subseteq H_{i+j\pmod2}\); no identification under automorphisms is made.

Put \(S_m(q)=q^{m^2}\prod_{j=1}^m(q^{2j}-1)\), with \(S_0(q)=1\), and \(G_m(q)=\prod_{j=0}^{m-1}(q^m-q^j)\). The number with \(Z\subseteq H_0\) and \(\dim H_1=2r\) is, for every \(0\le r\le m\),
\[
 E_{m,r}(q)=q^{2r}\frac{S_m(q)}{S_r(q)S_{m-r}(q)}.
\]
The number with \(Z\subseteq H_1\) is
\[
 O_m(q)=q^m\frac{S_m(q)}{G_m(q)}=q^{m^2+2m}\prod_{j=1}^m(1+q^{-j}).
\]
These strata are disjoint and exhaustive. Under the automorphism group of \(H\), they form exactly \(m+2\) orbits: one for each \(r\), and one with \(Z\subseteq H_1\).

For fixed \(q\), define \(P_q=\prod_{j\ge1}(1-q^{-2j})\), \(C_q=\prod_{j\ge1}(1+q^{-j})\), and the convergent theta sums
\[
 \Theta_0(q)=\sum_{t\in\mathbb Z}q^{2t-4t^2},\qquad
 \Theta_1(q)=\sum_{t\in\mathbb Z+1/2}q^{2t-4t^2}.
\]
If \((H_0,H_1)\) is uniformly sampled among all gradings, then, as \(m\to\infty\) through either parity \(\epsilon=m\bmod2\),
\[
 \Pr(Z\subseteq H_0)=q^{-m}\frac{\Theta_\epsilon(q)}{P_q C_q}(1+o_q(1)).
\]
Conditioned on \(Z\subseteq H_0\), the law of \(R-m/2\), where \(R=\dim H_1/2\), converges in total variation to the discrete probability mass function proportional to \(q^{2t-4t^2}\) on \(\mathbb Z+\epsilon/2\). In particular, almost every grading in growing dimension puts the center in degree one. The formulas hold in characteristic two, where gradings cannot in general be identified with eigenspace decompositions of involutions.

## Assumptions and scope
The field is any finite field \(\mathbb F_q\), including characteristic two. The Heisenberg bracket is \([u+az,v+bz]=\omega(u,v)z\) for a nondegenerate alternating form on a \(2m\)-dimensional space \(V\), \(m\ge1\). A grading is a labeled ordered pair, not an isomorphism class; zero homogeneous subspaces are allowed. The central line lies in exactly one homogeneous component because a graded center is graded.

## Proof
Write \(\pi:H\to V=H/Z\). Let \(Z\subseteq H_0\). Then \(H_0=\pi^{-1}(V_0)\), and \(H_1\) is a graph of a linear functional \(V_1\to\mathbb F_q z\), where \(V=V_0\oplus V_1\). The condition \([H_0,H_1]\subseteq H_1\) makes \(\omega(V_0,V_1)=0\), since any such bracket belongs to \(Z\subseteq H_0\). Thus \(V_0\) and \(V_1\) are complementary nondegenerate symplectic spaces; \(\dim V_1=2r\). Conversely every such pair and every functional define a grading. The symplectic group acts transitively on the ordered orthogonal decompositions and the stabilizer is \(\operatorname{Sp}_{2r}(q)\times\operatorname{Sp}_{2(m-r)}(q)\). The \(q^{2r}\) graph choices give \(E_{m,r}(q)\).

If \(Z\subseteq H_1\), then \(H_1=\pi^{-1}(V_1)\), while \(H_0\) is a graph of a functional on a complement \(V_0\). Since \([H_0,H_0]\subseteq H_0\) and \([H_1,H_1]\subseteq H_0\), and both brackets are central, \(\omega(V_0,V_0)=\omega(V_1,V_1)=0\). Hence \(V_0,V_1\) are transverse Lagrangian subspaces of dimension \(m\). All ordered transverse Lagrangian pairs are one \(\operatorname{Sp}_{2m}(q)\)-orbit with stabilizer isomorphic to \(\operatorname{GL}_m(q)\). There are \(q^m\) graph choices for \(H_0\), proving \(O_m(q)\). These arguments also prove the converse for every field characteristic.

Every symplectic transformation of \(V\) lifts to a Lie automorphism fixing \(z\), and arbitrary center-valued linear shears of \(V\) lift as well. Thus the graph choices and symplectic decompositions within each stratum form a single automorphism orbit. No two strata coalesce, because the degree of the center and \(\dim H_1\) are invariant.

To obtain the asymptotic, let \(P_j=\prod_{i=1}^j(1-q^{-2i})\). Using \(S_j=q^{2j^2+j}P_j\), the term with \(r=m/2+t\) is exactly
\[
 E_{m,r}=q^{m^2+m}q^{2t-4t^2}\frac{P_m}{P_rP_{m-r}}.
\]
Here \(t\in\mathbb Z\) for even \(m\), and \(t\in\mathbb Z+1/2\) for odd \(m\). The Euler ratios are uniformly bounded above and below by positive constants depending only on \(q\). For fixed \(t\), they tend to \(1/P_q\); the discrete Gaussian weights \(q^{2t-4t^2}\) are summable. Dominated convergence yields
\[
 \sum_{r=0}^mE_{m,r}=q^{m^2+m}(\Theta_\epsilon(q)/P_q+o_q(1)).
\]
The exact odd-center count satisfies \(O_m=q^{m^2+2m}(C_q+o_q(1))\). Division proves the rare-center probability. Normalizing the same dominated-convergence weights yields convergence in total variation of the centered conditional law, as asserted. The proof does not rely on numerical extrapolation.

## Verification
The standalone \(check.py\) independently enumerates every subspace of the underlying vector space, then tests direct sums and all three homogeneous bracket inclusions. This checks dimensions three and five over \(\mathbb F_2\), and dimension three over \(\mathbb F_3\), without assuming the symplectic parameterization. Its verified stratum totals are \((1,4,12)\), \((1,9,36)\), and \((1,80,16,480)\), giving totals \(17\), \(46\), and \(577\), respectively. Run \(python check.py\) from the directory containing the checker. The finite tests do not prove the infinite formula.

## Relationship to prior work
Calderón Martín, Draper Fontanals, Martín González and Sánchez Delgado (arXiv:1405.4093, Theorem 1, Section 3) prove the homogeneous symplectic-basis structure of arbitrary group gradings of Heisenberg algebras and describe their automorphism groups. Their general structural theorem is explicitly prior and is not claimed as new here. Eick and Moede (arXiv:2205.03155, Sections 1–4) study computational \(\mathbb Z_2\)-gradings of simple finite-field Lie algebras, especially characteristic two. The current statement concerns the exact finite-field numbers for every Heisenberg dimension, and a fixed-field, growing-dimension parity rare-event and theta-fluctuation law. The source results motivate the question, but neither inspected text states those enumeration or asymptotic conclusions.

## Limitations
No claim of independent review or exhaustive priority is made. The underlying orbit structure can be deduced from the general homogeneous-basis theorem, and the novelty asserted is quantitative enumeration and the limiting probability law, not a new abstract classification mechanism. Previously unindexed finite-field grading enumerations might contain equivalent formulas. Automorphism orbits are counted only for the specified \(\mathbb Z_2\)-gradings; other grading groups and other two-step nilpotent Lie algebras are outside scope.

## References
1. A. J. Calderón Martín, C. Draper Fontanals, C. Martín González, J. M. Sánchez Delgado, *Gradings and Symmetries on Heisenberg type algebras*, arXiv:1405.4093, first public 2014-05-16; Theorem 1 and Section 3.
2. B. Eick and T. Moede, *Computing subalgebras and \(\mathbb Z_2\)-gradings of simple Lie algebras over finite fields*, arXiv:2205.03155, first public 2022-05-06; Sections 1–4.
