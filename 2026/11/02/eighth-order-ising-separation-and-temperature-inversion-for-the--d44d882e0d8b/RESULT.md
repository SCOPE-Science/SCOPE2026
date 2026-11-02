# Eighth-order Ising separation and temperature inversion for the two order-five Latin-square graphs

## Finding

Let \(G_{\mathrm C}\) be the Latin-square graph of the cyclic order-five square and \(G_{\mathrm N}\) that of the other order-five main class, each with \(25\) vertices and \(150\) edges. They have identical strongly regular parameters \((25,12,5,6)\) and adjacency eigenvalues \(12,2,-3\) of multiplicities \(1,12,12\), respectively. They are nonisomorphic.

For each real \(J\ne0\) and \(h\), and the finite classical Ising Hamiltonian
\[
H_G(\sigma)=J\sum_{\{u,v\}\in E(G)}\sigma_u\sigma_v-h\sum_{u\in V(G)}\sigma_u,\qquad \sigma_u\in\{-1,1\},
\]
write \(Z_G(\beta,J,h)=\sum_\sigma\exp(-\beta H_G(\sigma))\). As \(\beta\downarrow0\), for every fixed \(J\ne0\) and \(h\),
\[
\boxed{Z_{G_{\mathrm C}}(\beta,J,h)-Z_{G_{\mathrm N}}(\beta,J,h)
=-48\,2^{25}J^8\beta^8+O(\beta^9).}
\]
Thus all seven lower positive-order high-temperature coefficients agree, for **every** uniform longitudinal field, and the eighth coefficient separates the graphs independently of that field. Equivalently, the counts of Eulerian edge subsets with each of \(0,1,\ldots,7\) edges agree, whereas the cyclic graph has exactly \(48\) fewer Eulerian eight-edge subsets than the non-group graph.

For \(J>0\) and \(h=0\), the zero-temperature ground-state energy is \(-30J\) on both graphs, with multiplicities \(35260\) (cyclic) and \(35172\) (non-group). Therefore
\[
Z_{G_{\mathrm C}}-Z_{G_{\mathrm N}}\sim 88e^{30\beta J}
\qquad(\beta\to\infty),
\]
so the relative partition-function ordering reverses: **at least one finite positive inverse temperature has equal partition functions**. No uniqueness of the crossing is asserted.

## Assumptions and scope

The two Latin squares below use row and column labels \(\{0,1,2,3,4\}\), with entries the third coordinate (symbols):

```text
C:  0 1 2 3 4      N:  0 1 2 3 4
    1 2 3 4 0          1 0 3 4 2
    2 3 4 0 1          2 3 4 0 1
    3 4 0 1 2          3 4 1 2 0
    4 0 1 2 3          4 2 0 1 3
```

Vertices are cells \((r,c)\). Distinct cells are adjacent exactly when they share a row, a column, or a symbol. The result assumes uniform real coupling \(J\), uniform real field \(h\), finite volume, and no disorder. The high-temperature expansion concerns fixed \(J,h\) as \(\beta\to0\), not a field or coupling rescaled with temperature. The low-temperature reversal uses \(J>0,h=0\).

## Proof

For a subset \(S\) of negative-spin vertices define \(k=|S|\) and \(e_G(S)\) to be its induced-edge count. With \(150\) edges and vertex degree \(12\), the cut from \(S\) is \(12k-2e_G(S)\), whence
\[
H_G(S)=J(150-24k+4e_G(S))-h(25-2k).
\]
Define the finite integer polynomial
\[
P_G(y,z)=\sum_{S\subseteq V(G)}y^{|S|}z^{e_G(S)}.
\]
Then, identically,
\[
Z_G(\beta,J,h)=e^{-\beta(150J-25h)}
P_G(e^{\beta(24J-2h)},e^{-4\beta J}).
\]

Put \(\Delta=P_{G_{\mathrm C}}-P_{G_{\mathrm N}}\), and write \(\Delta(y,1+t)=\sum_{r\ge0}A_r(y)t^r\). Exact exhaustive integer counting gives
\[
A_r(y)=0\quad(0\le r\le5),\qquad
A_6(y)=-4y^4(y-1)^4(y+1)^{13},
\]
\[
A_7(y)=-24y^5(y-1)^2(y+1)^{11}
(17y^3-15y^2-3y+3),\qquad A_8(1)=-24576.
\]
These identities are certified by the complete standalone enumeration in `verify.cpp`, rather than by statistical sampling or truncated search. It constructs both adjacency graphs and checks their Latin-square and strongly regular properties. **Two structurally different enumerations each visit all \(2^{25}=33554432\) vertex subsets for each graph:** a Gray-code bitset traversal and a recursive five-row occupancy enumeration. They produce exactly identical integer histograms at every subset size and every induced-edge count. The checker computes \(A_r\) by integer binomial moments of the histogram difference and verifies the stated identities for all coefficients, together with direct energy moments at four integer choices of field. The two algorithmic routes check the same finite identity without relying on external result files or precomputed database tables.

Since \(e^{-4\beta J}-1=-4\beta J+O(\beta^2)\) and \(e^{\beta(24J-2h)}-1=O(\beta)\), the \(A_6\) and \(A_7\) terms enter only at orders at least \(\beta^{10}\) and \(\beta^9\), respectively. The \(A_8\) term contributes \(-24576(4J)^8\beta^8=-48\,2^{25}J^8\beta^8\), proving the asserted leading term for **arbitrary fixed real** \(h\).

For the equivalent even-subgraph statement, the standard zero-field expansion is
\[
Z_G(\beta,J,0)=2^{25}(\cosh\beta J)^{150}
\sum_{F\subseteq E(G):\,\deg_F(v)\ \mathrm{even}\ \forall v}
(-\tanh\beta J)^{|F|}.
\]
Both graphs have the same edge count, so the first nonzero high-temperature difference at order \(\beta^8\) is precisely the difference of eight-edge Eulerian-subset counts multiplied by \(2^{25}J^8\). It is \(-48\), and all lower counts coincide. This count concerns **edge subsets**, not only simple cycles.

For the antiferromagnetic low-temperature statement, if \(k=5q+r\) with \(0\le r<5\), each of the three clique partitions into rows, columns and symbols forces at least \(5\binom q2+qr\) induced edges. Therefore
\[
e_G(S)\ge 3\left(5\binom q2+qr\right).
\]
The included verifier independently checks an attaining subset for every \(0\le k\le12\), and complements provide all other sizes. The exact optimum cut is \(90\), attained only for \(10\le k\le15\). Counting the corresponding optimal subsets by both exhaustive methods gives the zero-field degeneracies \(35260\) and \(35172\). Hence the partition-function difference is positive for all sufficiently large \(\beta\); it is negative for all sufficiently small positive \(\beta\), so continuity forces at least one positive-temperature crossing.

The checker also counts \(K_4\) subgraphs (\(75\) cyclic versus \(79\) non-group), independently confirming nonisomorphism, and verifies their shared strongly regular parameters.

## Verification

The portable C++17 source `verify.cpp` is a complete self-contained checker; no network, proprietary library, random seed or external data file is needed. From the directory containing that file run:

```sh
c++ -std=c++17 -O3 verify.cpp -o verify
./verify
```

Expected final status: `VERIFY_OK graph_classes=2 methods=2 subsets_each=33554432 sector_sizes=26 hist_cells=7852`. The source additionally checks all binomial-moment equalities and the two low-temperature sector multiplicities, and prints `MOMENTS_OK`. Arithmetic for moment identities uses signed 128-bit integers; the maximum possible intermediate values are far below that integer type's range. No finite sample is presented as an infinite-family proof: this is a fully exhausted **finite pair** of 25-site systems, and the all-real-field conclusion follows from exact polynomial identities.

## Relationship to prior work

The two order-five Latin-square species, their 1-plex and 2-plex counts (\(15\) versus \(3\), and \(130\) versus \(30\)) were already reported by Egan and Wanless; **these counts are not claimed as new**. The catalogue of Paulus–Rozenfeld strongly regular graphs identifies the relevant nonisomorphic graphs as P25.15 (Paley) and P25.12 (non-group). Besharati and collaborators established their distinct chromatic numbers. Vinci and collaborators developed the bivariate Ising-polynomial framework. The present narrow contribution is the precise eighth-order, uniform-field high-temperature separation and the demonstrated finite-temperature reversal for this particular pair; neither the underlying Ising-polynomial construction nor the published Latin-square invariants are claimed as discoveries.

## Limitations

Historical priority remains provisional: a specialized Ising/Tutte-polynomial table, an earlier enumeration of Eulerian eight-edge subsets, or an equivalence of previously published finite-graph invariants could cover the result. The claim is not about arbitrary strongly regular graphs, more Latin-square orders, the smallest crossing temperature, uniqueness of the crossing, a thermodynamic phase transition, quantum Ising dynamics or nonuniform interactions. The verification establishes exactness of the specified finite pair only; independent scientific auditing has not been performed.

## References

1. Judith Egan and Ian M. Wanless, *Indivisible partitions of latin squares*, Journal of Statistical Planning and Inference 141 (2011), 402–417, publicly online 2010-06-22, https://users.monash.edu.au/~iwanless/papers/DataIndivJSPI.pdf, especially Table 2.
2. Walter Vinci et al., *Hearing the Shape of the Ising Model*, arXiv:1307.1114 (2013), https://arxiv.org/abs/1307.1114.
3. Besharati et al., *On the chromatic number of Latin square graphs*, arXiv:1510.02521 (2015), https://arxiv.org/abs/1510.02521.
4. A. E. Brouwer, *Paulus–Rozenfeld graphs*, https://aeb.win.tue.nl/graphs/Paulus.html, recording P25.12 and P25.15 and earlier classifications (1973).
