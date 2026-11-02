# Exact finite-size field staircase and parity-defect transition for the triangular-graph Ising antiferromagnet

## Finding
For every integer \(n\ge4\), every \(J>0\), and every real longitudinal field \(h\), the labelled classical zero-temperature ground states of the homogeneous antiferromagnetic Ising model on the triangular graph \(T_n=L(K_n)\) are classified exactly by the degree-profile criterion in the next section. The classification gives the ground energy, all ground-state magnetizations and an exact coefficient formula for every ground-state multiplicity, including all level crossings.

In the natural pre-saturation interval \(2J(n-4)<|h|<2J(n-2)\), the negatively oriented spin sites form the following complete families (take \(h>0\), and reverse spins for \(h<0\)):

* For even \(n\), a perfect matching in \(K_n\), with degeneracy \((n-1)!!\).
* For odd \(n\ge5\), when \(2J(n-4)<h<2J(n-3)\), a copy of the three-vertex path together with a perfect matching on the remaining \(n-3\) vertices, with degeneracy \(n\binom{n-1}{2}(n-4)!!\).
* For odd \(n\ge5\), when \(2J(n-3)<h<2J(n-2)\), one isolated vertex and a perfect matching on the other \(n-1\), with degeneracy \(n(n-2)!!\).
* At the odd-order crossing \(h=2J(n-3)\), both families coexist, giving \(n(n+1)(n-2)!!/2\) states and an exact two-unit jump in the ground magnetization as the field crosses this point.

At \(h=2J(n-2)\), for every \(n\ge4\), the negative spins form an arbitrary matching in \(K_n\). The ground-state multiplicity is the telephone number
\[
I_n=\sum_{k=0}^{\lfloor n/2\rfloor}\frac{n!}{2^k k!(n-2k)!}.
\]
At greater positive fields, only the all-positive state survives. The relation between saturation and matchings is a known general line-graph mechanism; the new assessed contribution is its exact finite-size field-and-parity classification, including the odd-order intermediate crossing.

## Assumptions and scope
Let \(K_n\) be the complete simple graph on labelled vertices \(1,\ldots,n\). Put one classical spin \(\sigma_{ij}\in\{-1,+1\}\) on each edge \(\{i,j\}\) of \(K_n\), equivalently on each vertex of \(T_n=L(K_n)\). Two spins interact once if their underlying edges have a common endpoint, with energy
\[
H(\sigma)=J\sum_{\{e,f\}\in E(T_n)}\sigma_e\sigma_f-h\sum_{e\in E(K_n)}\sigma_e,\qquad J>0.
\]
All states are labelled, no quotient by graph symmetry is taken, and \(T=0\). Define the signed incidence charges
\[
q_i=\sum_{j\ne i}\sigma_{ij}\in\mathcal D_n:=\{-(n-1),-(n-3),\ldots,n-1\},
\]
and let \(r_i=(n-1+q_i)/2\) be the degree of vertex \(i\) in the graph of positive-spin edges. In positive or zero field set \(t=h/J\), \(F_t(q)=(q^2-tq)/2\), and \(\mathcal Q_t=\arg\min_{q\in\mathcal D_n}F_t(q)\).

Here is the complete decision rule for \(h\ge0\):

1. If \(\mathcal Q_t=\{q,q+2\}\), let \(r=(n-1+q)/2\). The ground states are **precisely** those with all charges in \(\{q,q+2\}\); the number \(k\) of vertices of charge \(q+2\) must and may be any integer \(0\le k\le n\) satisfying \(nr+k\equiv0\pmod2\).
2. If \(\mathcal Q_t=\{q\}\) and \(nr\) is even, where \(r=(n-1+q)/2\), then every charge equals \(q\).
3. If \(\mathcal Q_t=\{q\}\) and \(nr\) is odd, exactly one charge is \(q+2\) or \(q-2\), whichever available choice minimizes \(F_t(q\pm2)\), and all other charges equal \(q\). If both costs tie, both classes occur. This case is possible only for odd \(n\) and odd \(r\).

Every degree pattern described above occurs on an actual simple labelled graph; the rule imposes no hidden graphability conditions. At \(h=0\), it covers both \(\mathcal Q_0=\{-1,1\}\) for even \(n\) and \(\mathcal Q_0=\{0\}\) for odd \(n\). For \(h<0\), globally reverse all spins in the positive-field classification with field \(|h|\).

For any admissible charge vector \(\mathbf q\), its energy and magnetization are exactly
\[
E(\mathbf q)=J\left(\sum_{i=1}^n F_t(q_i)-\frac{n(n-1)}2\right),\qquad M(\mathbf q)=\frac12\sum_iq_i.
\]
The exact labelled multiplicity of a fixed degree vector \(\mathbf r\) is
\[
\Phi_n(\mathbf r)=[z_1^{r_1}\cdots z_n^{r_n}]\prod_{1\le i<j\le n}(1+z_iz_j).
\]
Consequently the degeneracy at any field is exactly \(g_n(h)=\sum_{\mathbf q\in\mathcal G_n(h)}\Phi_n((n-1+\mathbf q)/2)\), where \(\mathcal G_n(h)\) is the set of charge vectors described by the three-case rule. This finite coefficient expression, together with the explicit rule, is a complete reproducible multiplicity formula, not a claimed simple closed form for counts of arbitrary regular labelled graphs.

## Proof
**Incidence-square identity.** Since the \(n-1\) spins touching vertex \(i\) form a clique of interacting sites in \(T_n\), their pair contribution is \((q_i^2-(n-1))/2\). Each interacting pair belongs to exactly one such clique. Moreover \(\sum_iq_i=2\sum_e\sigma_e\). Therefore
\[
H=\frac J2\sum_iq_i^2-\frac{Jn(n-1)}2-\frac h2\sum_iq_i
=J\left(\sum_iF_t(q_i)-\frac{n(n-1)}2\right).
\]
Writing \(r_i=(n-1+q_i)/2\) identifies positive spins with the edges of an ordinary simple graph on \(n\) labelled vertices; the handshake identity demands \(\sum_i r_i\) even.

**Near-regular graphical lemma (proved here).** For integers \(0\le r\le n-1\) and \(0\le k\le n\) such that \(r+1\le n-1\) whenever \(k>0\), any prescribed multiset consisting of \(n-k\) degrees \(r\) and \(k\) degrees \(r+1\) is graphical if and only if \(nr+k\) is even. Necessity is the handshake lemma. For sufficiency choose a simple graph on \(n\) vertices with exactly \((nr+k)/2\) edges minimizing the sum of squared vertex degrees; existence is automatic since that edge number lies between \(0\) and \(\binom n2\). If vertices \(u,v\) satisfy \(\deg u\ge\deg v+2\), there is a neighbor \(w\ne v\) of \(u\) that is not adjacent to \(v\). Replace the edge \(uw\) by \(vw\): simplicity and the edge count are preserved, while the degree-square sum drops by \(2(\deg u-\deg v-1)>0\), a contradiction. Thus all degrees differ by at most one. Their sum forces exactly the prescribed multiset; relabelling realizes every prescribed placement.

**Exact optimization.** Each \(F_t\) is strictly convex on the arithmetic progression \(\mathcal D_n\), so its local minimizers form one point or two adjacent points. If two points \(q,q+2\) tie, every vector using only them has absolute minimal possible local energy. The handshake condition is precisely \(nr+k\) even, and the near-regular lemma realizes every such degree multiset. Any other charge incurs positive excess energy and cannot minimize. If the local optimum is unique and \(nr\) is even, the regular degree vector is graphical by the lemma and attains all local minima. Otherwise \(n,r\) are odd and the handshake parity excludes the uniform vector. Every admissible state must pay at least the least strictly positive local excess \(\min\{F_t(q-2)-F_t(q),F_t(q+2)-F_t(q)\}\), ignoring unavailable charges. One exceptional charge \(q\pm2\) changes one positive degree by \(\pm1\), gives even total degree, and is graphical by the lemma. Hence precisely the stated one-exception families attain the global minimum. Convexity excludes any more distant charge from having smaller excess. At a tie between the two defects both families minimize. Global spin reversal proves negative-field symmetry.

**Near-saturation and counting.** Put \(S=\{e:\sigma_e=-1\}\) and let \(a_i\) be its degree in \(K_n\). Then \(q_i=n-1-2a_i\), and relative to all-positive spins the exact energy is
\[
H(S)-H(\varnothing)=2(h-2J(n-2))|S|+4J\sum_i\binom{a_i}{2}.
\]
The just-proved charge classification in \(2J(n-4)<h<2J(n-2)\) gives negative degrees all \(1\) for even \(n\); for odd \(n\), all \(1\) except exactly one \(2\) on the lower half or exactly one \(0\) on the upper half. These are respectively a perfect matching, a single path \(P_3\) plus a matching, and an isolated vertex plus a matching. In the odd case the energy difference of the two families is \(2(h-2J(n-3))\), giving the unique internal crossing and the magnetization jump of two. Choosing the exceptional vertex, path endpoints and remaining pairing gives the three stated multiplicities. At \(h=2J(n-2)\), the linear term vanishes and the positive collision term vanishes exactly for matchings; counting matchings yields \(I_n\). Above that field the empty negative-edge set uniquely minimizes the energy. These statements use no thermodynamic-limit or asymptotic assumption.

## Verification
The standalone standard-library program `verify.py` traverses **every** spin assignment on \(T_4,T_5,T_6,T_7\) via a Gray code, updating the exact integer incidence charges, energy and magnetization. For every half-integer \(h/J\) between \(0\) and \(2(n-2)+1\), it compares all minimizing charge profiles with the three-case analytical rule, and compares their full labelled counts. The replayed output is `verification_output.txt`.

Specific near-saturation data: for \(n=5\), the lower, crossing and upper degeneracies are \(30,45,15\), with \(26\) states at saturation; for \(n=7\) they are \(315,420,105\), with \(232\) states at saturation. For even \(n=4,6\), the open pre-saturation counts are \(3,15\), and saturation counts are \(10,76\), respectively. The finite check tests small sizes only; the arbitrary-\(n\) conclusion follows from the exact optimization and graphability proof.

## Relationship to prior work
The general two-star/edge-count graph Hamiltonian and its degree-square formulation are known from Park and Newman (2004) and Annibale and Courtney (2015). The latter also discusses regularity minimizing two-star density at fixed mean degree. The antiferromagnetic Ising model on line graphs in arbitrary field is considered by Dyer, Heinrich, Jerrum and Müller (2020), who give polynomial-time *approximate* partition-function algorithms for general line graphs, not an exact finite-size zero-temperature classification for \(L(K_n)\). The matching description at saturation is an elementary general consequence of hard-core negative-spin defects on a line graph and is not claimed independently as a new principle.

The specific assessed result here is the complete graphical-parity refinement for the finite \(L(K_n)\) family, including all positive/negative field crossings and the exact odd-order pre-saturation \(P_3\)-versus-isolated-vertex switch. This is neither the source's large-\(n\) cooperative mean-field phase diagram nor a general algorithm for approximating the finite-temperature partition function. Specialized unpublished or less searchable exact magnetic-census literature could still imply the result; independent historical-priority verification has not been performed.

## Limitations
The result assumes classical two-state spins, uniform antiferromagnetic pair interactions and one uniform longitudinal field, on complete-graph line graphs only, at exactly zero temperature. The degree enumerator is exact but not generally a short closed formula for the number of regular labelled graphs. Finite-size magnetization steps, including the two-unit odd-order step, do not establish a bulk thermodynamic phase transition; no quantum, kinetic or positive-temperature assertion is made.

## References
- J. Park and M. E. J. Newman, “Solution of the 2-star model of a network,” first arXiv public version May 19, 2004, https://arxiv.org/abs/cond-mat/0405457 .
- A. Annibale and O. T. Courtney, “The two-star model: exact solution in the sparse regime and condensation transition,” first arXiv public version April 24, 2015, https://arxiv.org/abs/1504.06458 .
- M. Dyer, M. Heinrich, M. Jerrum and H. Müller, “Polynomial-time approximation algorithms for the antiferromagnetic Ising model on line graphs,” first arXiv public version May 16, 2020, https://arxiv.org/abs/2005.07944 .
