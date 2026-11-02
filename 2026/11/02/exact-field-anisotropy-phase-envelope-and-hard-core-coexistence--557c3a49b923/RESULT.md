# Exact field–anisotropy phase envelope and hard-core coexistence on the Petersen spin-one antiferromagnet

## Finding
Let \(P=KG(5,2)\) be the Petersen graph: its ten vertices are the two-element subsets of a five-element set, with edges joining disjoint subsets. Give each vertex a classical spin \(s_v\in\{-1,0,1\}\), and define
\[
\mathcal H(s)=J\sum_{\{v,w\}\in E(P)}s_vs_w+D\sum_vs_v^2-h\sum_vs_v,
\qquad J>0,\quad D\in\mathbb R,\quad h\ge0.
\]
Write \(r=D/J\) and \(u=h/J\). The exact zero-temperature energy for **every** real \(r\) and every \(u\ge0\) is
\[
\boxed{\frac{E_0(D,h)}J=\min\{-9+10r-2u,\;-6+6r,\;-3+4r-2u,\;4r-4u,\;3+6r-6u,\;15+10r-10u,\;0\}.}
\]
The seven branches are denoted \(A,B,C,D_*,E,F,Z\), respectively. In any open parameter region where precisely one branch is minimal, the exact ground-state data (bond energy \(b\), number of occupied sites \(k\), total magnetization \(m\), and number of labeled ground states) are:

| Branch | \((b,k,m)\) | Ground-state count |
|---|---|---:|
| \(A\) | \((-9,10,2)\) | 5 |
| \(B\) | \((-6,6,0)\) | 20 |
| \(C\) | \((-3,4,2)\) | 10 |
| \(D_*\) | \((0,4,4)\) | 5 |
| \(E\) | \((3,6,6)\) | 5 |
| \(F\) | \((15,10,10)\) | 1 |
| \(Z\) | \((0,0,0)\) | 1 |

Thus the generic magnetizations contain the exact plateaus \(m/10\in\{0,1/5,2/5,3/5,1\}\); the two distinct branches \(A\) and \(C\) have the same magnetization but different occupied-site counts. All seven branches are genuinely attained on open parameter regions (with \(h>0\) where appropriate).

A particularly sharp coexistence law holds at the saturation boundary. Define the Petersen independence polynomial
\[
I_P(z)=1+10z+30z^2+30z^3+5z^4.
\]
For any \(r<0\), at \(u=3\) the ground states are precisely the configurations obtained by choosing an independent vertex set and placing spin \(-1\) on it, with \(+1\) elsewhere; there are \(I_P(1)=76\) such states. For any \(r>0\), at \(u=3+r\), an independent vertex set may instead carry spin \(0\), with \(+1\) elsewhere; there are again 76 states. At their junction \((r,u)=(0,3)\), each vertex of an independent set may independently carry \(0\) or \(-1\); this gives the **exact 461-fold degeneracy**
\[
\#\mathrm{GS}(0,3J)=I_P(2)=461.
\]
There is no claim of a thermodynamic-limit phase transition.

## Assumptions and scope
The graph is the simple, undirected Petersen graph with all 15 edges present, one exchange strength \(J>0\), an arbitrary real single-ion coefficient \(D\), and a uniform nonnegative field \(h\). Spins are three-valued and **classical**, with the sign convention that positive \(D\) penalizes occupied sites. Ground states are all ten-site assignments minimizing \(\mathcal H\). Every count refers to labeled configurations on these ten fixed sites. A negative field is obtained by simultaneous field and spin reversal, but is not required for the stated theorem.

## Proof
**1. Reduction to a finite exact bond–occupancy–magnetization table.** Let \(b(s)=\sum_{\{v,w\}\in E(P)}s_vs_w\), \(k(s)=\sum_vs_v^2\), and \(m(s)=\sum_vs_v\). Then \(\mathcal H/J=b+rk-um\). Because \(u\ge0\), global spin reversal ensures it suffices to minimize over \(m\ge0\). Necessarily \(0\le m\le k\le10\) and \(k\equiv m\pmod2\), hence there are exactly 36 possible \((k,m)\) sectors. The exact minimum bond energies \(b_{\min}(k,m)\) in these sectors are recorded in the companion `convex_certificate.json`. They follow by exhaustive evaluation of the \(3^{10}=59049\) assignments on the **explicit** Kneser adjacency relation; `checker.py` independently regenerates the full 318-class \((b,k,m)\) histogram in two representations, one by Cartesian spin assignment and one by disjoint positive- and negative-spin subsets. This is exhaustive finite mathematics, not a statistical sample or a numerical optimization oracle.

**2. A rational certificate valid for a continuum of parameters.** The companion certificate records, for each of the 36 sectors, nonnegative rational weights \(\lambda_i\) on the seven reference triples \((b_i,k_i,m_i)\), satisfying
\[
\sum_i\lambda_i=1,\qquad \sum_i\lambda_i k_i=k,\qquad
\sum_i\lambda_i m_i\ge m,\qquad \sum_i\lambda_i b_i\le b_{\min}(k,m).
\]
For any real \(r\) and any \(u\ge0\), these identities give
\[
b_{\min}(k,m)+rk-um
\;\ge\;\sum_i\lambda_i(b_i+rk_i-um_i)
\;\ge\;\min_i(b_i+rk_i-um_i).
\]
Every one of the seven reference triples is realized by an actual spin assignment, so the resulting lower bound is attained. This proves the displayed seven-branch formula **simultaneously for all allowed continuous parameters**. Exact enumeration identifies the stated labeled counts when a branch is uniquely minimal. `checker.py` verifies that every branch has a strict minimizing witness, so none is a redundant formula entry.

**3. Hard-core coexistence.** Set \(x_v=1-s_v\in\{0,1,2\}\). Since \(P\) is cubic, expansion about the all-positive state gives the identity
\[
\frac{\mathcal H(s)}J=15+10r-10u+
\sum_{\{v,w\}\in E(P)}x_vx_w+
\sum_v\bigl[r x_v^2+(u-3-2r)x_v\bigr].
\]
When \(r<0,u=3\), the on-site term is \(r x_v(x_v-2)\), which is zero exactly for \(x_v\in\{0,2\}\) and positive for \(x_v=1\). When \(r>0,u=3+r\), the on-site term is \(r x_v(x_v-1)\), which vanishes exactly for \(x_v\in\{0,1\}\). At \(r=0,u=3\), it vanishes for all three spin values. In all cases the remaining edge sum is nonnegative, and it vanishes precisely when vertices carrying nonzero \(x_v\) form an independent set. The five-term independence polynomial is obtained by exactly counting Petersen independent sets of each size, or by the separate bit-mask check in `checker.py`; the resulting totals are 76, 76, and 461.

## Verification
Run `python3 checker.py` with `convex_certificate.json` in the same directory, using Python 3 with only its standard library. It checks all 59049 ternary states in each of two independent enumeration representations, all 318 distinct energy-statistic triples, each of the 36 exact rational dominance certificates, strict witnesses and multiplicities for all seven phases, and the independent-set polynomial. It also checks the following critical point multiplicities exactly:

| \((r,u)\) | Labeled ground states |
|---|---:|
| \((0,3)\) | 461 |
| \((3/4,0)\) | 30 |
| \((3/4,9/4)\) | 85 |
| \((1,0)\) | 21 |
| \((1,1/2)\) | 36 |
| \((1,3/2)\) | 20 |
| \((3/2,3/2)\) | 86 |

The certificate has only exact integers and fractions. Boundary degeneracies elsewhere can be obtained from the same complete \((b,k,m)\) histogram; the seven interior counts above are **not** asserted to sum to the ground-state degeneracy on every coexistence line.

## Relationship to prior work
Žukovič and Bobák (2013, arXiv:1309.3593) analyzed the frustrated spin-one Blume–Capel antiferromagnet on the **triangular lattice**, including a seven-phase field–anisotropy diagram. The existence of several magnetization plateaus, or the number of generic branches alone, is therefore not a novelty claim here. Mohylna and Žukovič (2020, arXiv:2010.16287; *Magnetochemistry* 6, 56) used exact enumeration for a three-site triangle and two corner-sharing tetrahedra (seven sites), not the Petersen connectivity. The Petersen graph itself is a canonical cubic cage and strongly regular graph, with well-known independence structure; its graph invariants are not claimed as discoveries. The specific new claim is the **exact 10-site Petersen Hamiltonian envelope, branch multiplicities, and its 461-state joint hard-core coexistence law**. The lack of an identified equivalent result is subject to historical-priority review.

## Limitations
No quantum-spin dynamics, continuous spins, disorder, spatially nonuniform exchange, positive-temperature singularities, material realization, or infinite-lattice behavior is established. The model is a finite mathematical benchmark; its physical relevance does not imply an experimentally observed Petersen molecular magnet. The independent-set mapping at saturation extends to regular graphs and is a standard type of hard-core reduction; the claimed contribution lies in its exact integration with this Petersen phase classification. Search-based originality is not proof of worldwide uniqueness and independent review has not been performed.

## References
1. M. Žukovič and A. Bobák, *Magnetocaloric properties of a frustrated Blume-Capel antiferromagnet* (first public 2013-09-13), https://arxiv.org/abs/1309.3593 .
2. M. Mohylna and M. Žukovič, *Effect of Single-Ion Anisotropy on Magnetocaloric Properties of Frustrated Spin-s Ising Nanoclusters* (2020), https://arxiv.org/abs/2010.16287 ; https://doi.org/10.3390/magnetochemistry6040056 .
3. A. E. Brouwer, *The Petersen graph*, https://aeb.win.tue.nl/graphs/Petersen.html (Kneser graph, independent sets and automorphism group).
4. C. Ekiz and H. Yaraneri, *The magnetization plateaus of general Ising system with single-ion anisotropy*, *J. Magn. Magn. Mater.* 318 (2007), 49–57, https://doi.org/10.1016/j.jmmm.2007.04.022 (Bethe-lattice comparison).
