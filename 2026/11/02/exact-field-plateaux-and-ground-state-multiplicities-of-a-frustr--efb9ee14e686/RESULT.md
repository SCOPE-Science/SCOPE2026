# Exact field plateaux and ground-state multiplicities of a frustrated three-leg Ising tube

## Finding

For the classical antiferromagnetic three-leg Ising tube with triangular rungs and periodic legs, both the exact ground-state energy and the number of distinct labelled-spin minimizers admit closed formulas for every tube length and every longitudinal magnetic field. In particular, the one-third-magnetization interval has exponentially many ground states; the two transition fields have different algebraic exponential degeneracies; and the low-field multiplicity differs dramatically for odd and even circumferences.

Put \(r=|h|/J\), where \(J>0\). Write \(E_0\) for the lowest energy and \(g\) for its multiplicity. For each integer \(n\ge3\), define
\[
 a_n=(1+\sqrt2)^n+(1-\sqrt2)^n,\qquad
 b_n=\left(\frac{-1+\sqrt5}{2}\right)^n+\left(\frac{-1-\sqrt5}{2}\right)^n,
\]
\[
 c_n=\left(\frac{3+\sqrt{13}}2\right)^n+\left(\frac{3-\sqrt{13}}2\right)^n.
\]
These expressions are integers. The complete classification is

| Field | Ground energy \(E_0/J\) | Multiplicity \(g\) |
|---|---|---|
| \(r=0\), even \(n\) | \(-4n\) | \(6\) |
| \(r=0\), odd \(n\) | \(-4n+6\) | \(2n(n^2+3n-1)\) |
| \(0<r<2\), even \(n\) | \(-4n\) | \(6\) |
| \(0<r<2\), odd \(n\) | \(-4n+6-3r\) | \(n(n^2-1)/4\) |
| \(r=2\) | \(-4n\) | \(a_n+2b_n\) |
| \(2<r<4\) | \(-(2+r)n\) | \(2^n+2(-1)^n\) |
| \(r=4\) | \(-6n\) | \(c_n+2(-1)^n\) |
| \(r>4\) | \((6-3r)n\) | \(1\) |

For \(h>0\), every ground state in \(0<h/J<2\) has total magnetization \(0\) for even \(n\) and \(3\) for odd \(n\). Every ground state in \(2<h/J<4\) has magnetization \(n\) (one-third of full saturation), and for \(h/J>4\) it has magnetization \(3n\). Negative field reverses every spin, preserving energy and multiplicity and reversing the magnetization. On the transition fields, multiple magnetizations coexist.

## Assumptions and scope

Vertices are \((i,t)\in \mathbb Z/3\mathbb Z\times \mathbb Z/n\mathbb Z\), where \(n\ge3\). Edges join \((i,t)\) to \((i+1,t)\) and to \((i,t+1)\); each undirected edge is counted once. Every spin \(\sigma_{i,t}\) equals \(+1\) or \(-1\). The *classical*, spatially homogeneous Hamiltonian is
\[
 H(\sigma)=J\sum_{\{u,v\}\in E}\sigma_u\sigma_v-h\sum_{v}\sigma_v,
 \qquad J>0,\quad h\in\mathbb R.
\]
There are \(3n\) vertices and \(6n\) edges. All site-labelled spin assignments are distinct; no quotient by rotations or global spin reversal is taken. The result is strictly zero-temperature and concerns unrestricted spin configurations.

## Proof

By spin inversion it suffices to consider \(h\ge0\). Let \(S\) be the set of down spins, \(q=|S|\), and \(e(S)\) its number of internally adjacent vertex pairs. Let \(U\) denote the number of bonds with equal endpoint spins. Direct edge counting gives
\[
 M=3n-2q,\qquad U=6n-4q+2e(S),
\]
\[
 E/J=2U-6n-rM.
\]
For each triangular rung containing \(k\) down spins, the quantity \(k-e_{\mathrm{rung}}\) is \(1\) for \(k=1,2\) and \(0\) for \(k=0,3\). Leg edges within \(S\) can only decrease \(q-e(S)\). Therefore \(q-e(S)\le n\), equivalently
\[
 U\ge n+M,\qquad E/J\ge -4n+(2-r)M.
\]
Equality holds precisely when every rung has one or two down spins and no two down spins in neighboring rungs occupy the same leg.

Encode a one-down rung by \(S_i\), where \(i\) is its down-spin leg, and a two-down rung by \(D_i\), where \(i\) is its sole up-spin leg. The allowed neighboring equality-state pairs are \(S_iS_j\) when \(i\ne j\), and \(S_iD_i\) or \(D_iS_i\). There are no \(D_iD_j\) pairs. Thus the symmetric six-state compatibility matrix is
\[
 B=\begin{pmatrix}\mathbf 1\mathbf 1^{\mathsf T}-I_3&I_3\\I_3&0\end{pmatrix}.
\]
At \(r=2\), equality configurations are exactly the minimizers, with \(E_0/J=-4n\) and \(g=\operatorname{tr}(B^n)\). The uniform colour vector yields eigenvalues solving \(\lambda^2-2\lambda-1=0\), once each; the orthogonal two-dimensional colour sector yields roots of \(\lambda^2+\lambda-1=0\), each twice. This gives \(a_n+2b_n\).

For \(0<r<2\) one may choose positive magnetization by global reversal. If \(n\) is even, the lower bound is attained at \(M=0\): each rung alternates between an \(S_i\) and \(D_i\), with three choices of \(i\) and two parities, giving six ground states. For odd \(n\), \(M\) is odd and \(M=1\) cannot satisfy the equality conditions: the necessary number of \(D\) rungs leaves exactly one \(S\)-to-\(S\) colour change around the cycle, which cannot close. The difference \(U-(n+M)\) is even, hence at \(M=1\) the energy exceeds its nominal lower bound by at least four. The \(M=3\) equality states are thus optimal for every \(0<r<2\): compare their energy \(-4n+3(2-r)\) with the \(M=1\) lower bound \(-4n+4+(2-r)\), and use the increasing bound for \(M\ge3\). Such configurations have \((n-3)/2\) nonadjacent \(D\) rungs. There are \(n(n^2-1)/24\) choices of their locations. Contracting each \(D\) rung into the forced adjoining \(S\)-colour leaves a three-edge colour cycle with six proper colour assignments. Consequently their total is \(n(n^2-1)/4\).

For the high-field phases, the down-spin expression is
\[
 E/J=6n-3rn+(2r-8)q+4e(S).
\]
For \(r>2\), any down vertex with a down-spin neighbour can be removed from \(S\), decreasing the energy by at least \(2r-4>0\). Thus every minimizer has \(e(S)=0\). For \(2<r<4\), maximizing \(q\) subject to independence forces exactly one down spin per triangular rung; adjacent rungs cannot use the same leg. Hence the minimizers are proper three-colourings of a length-\(n\) cycle, of which there are \(2^n+2(-1)^n\). This yields \(M=n\) and energy \(-(2+r)n\). For \(r=4\), every independent set minimizes. A four-state transfer matrix indexed by the empty rung and three one-down rungs is
\[
 T=\begin{pmatrix}1&\mathbf1^{\mathsf T}\\\mathbf1&\mathbf1\mathbf1^{\mathsf T}-I_3\end{pmatrix}.
\]
Its eigenvalues are the two roots of \(\lambda^2-3\lambda-1=0\) and \(-1\) with multiplicity two. Thus \(g=\operatorname{tr}(T^n)=c_n+2(-1)^n\). When \(r>4\), all spins point up uniquely.

Finally, at \(r=0\) each triangle costs at least one equal-spin bond. If \(n\) is odd, each leg cycle also requires at least one equal-spin bond; hence \(U\ge n+3\), attained exactly by assigning one kink on each leg and keeping every triangular rung nonuniform. If \(n\) is even, all legs can alternate and the six initial nonuniform rung patterns give all minimizers. For odd \(n\), select the locations of the three labelled leg kinks. If they occupy respectively \(k=1,2,3\) distinct rungs, there are exactly \(8-2k\) admissible choices of initial three-spin signs: the \(k\) distinct partial parity flips forbid \(k\) opposite pairs of the eight possible sign triples. The counts of kink-location triples by distinct positions are \(n\), \(3n(n-1)\) and \(n(n-1)(n-2)\). Therefore
\[
 g=6n+12n(n-1)+2n(n-1)(n-2)=2n(n^2+3n-1).
\]
This exhausts all fields and lengths.

## Verification

The standalone `checker.py` uses both direct enumeration of all \(2^{3n}\) configurations for \(3\le n\le6\) and an independently implemented eight-rung-state exact min-plus transfer calculation for \(3\le n\le30\). For integer sample fields \(r\in\{0,1,2,3,4,5\}\), all 24 full enumerations and all 168 transfer comparisons match the theorem's energies and multiplicities. Execute `python3 checker.py`; its expected output is supplied in `CHECK_LOG.txt`. The infinite-family proof is algebraic and combinatorial; finite checks alone would not establish it.

## Relationship to prior work

Three-leg spin tubes, magnetization plateaux and frustration are established physical topics. Kawano and Takahashi (1997) treat a quantum Heisenberg ladder rather than this classical nearest-neighbour Ising Hamiltonian. Lajkó, Sindzingre and Penc (2011) study a Heisenberg model with plaquette projector/ring exchange; their exact states do not imply these finite Ising counts. Strečka and collaborators (2015) analyze Heisenberg triangles coupled by Ising interactions in *zero* field, with different local interactions. Jurčišinová and Jurčišin (2014) analyze an infinite *zigzag ladder* with multisite couplings, not the present three-leg triangular-rung torus. The general transfer-matrix principle is standard; the specific all-field formulas, odd-length cubic count and the two distinct transition spectra are the assessed results.

## Limitations

The theorem assumes exactly equal rung and leg antiferromagnetic couplings, classical Ising spins, uniform longitudinal field, periodicity in both directions and \(n\ge3\). It does not describe excitation gaps, finite-temperature observables, unequal couplings, diagonal leg bonds, quantum dynamics or open leg boundaries. Historical novelty has not been independently certified; specialized classical ladder studies may supply broader coverage not located in the inspected sources.

## References

- H. Kawano and M. Takahashi, *Three-leg antiferromagnetic Heisenberg ladder*, arXiv:cond-mat/9709271v1 (1997-09-25). https://arxiv.org/abs/cond-mat/9709271
- M. Lajkó, P. Sindzingre and K. Penc, *Exact ground states with deconfined gapless excitations for the three-leg spin-1/2 tube*, arXiv:1107.5501v1 (2011-07-27). https://arxiv.org/abs/1107.5501
- E. Jurčišinová and M. Jurčišin, *Solution of the antiferromagnetic Ising model with multisite interaction on a zigzag ladder*, Physical Review E 90, 032108 (2014). https://doi.org/10.1103/PhysRevE.90.032108
- J. Strečka, R. C. Alécio, M. L. Lyra and O. Rojas, *Spin frustration of a spin-1/2 Ising-Heisenberg three-leg tube as an indispensable ground for thermal entanglement*, arXiv:1512.03231v1 (2015-12-10). https://arxiv.org/abs/1512.03231
