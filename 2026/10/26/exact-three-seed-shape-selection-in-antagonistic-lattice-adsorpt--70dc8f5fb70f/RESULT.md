# Exact three-seed shape selection in antagonistic lattice adsorption

## Finding

For every integer \(L\ge7\), consider the square \(L\times L\) periodic nearest-neighbor lattice. Choose uniformly one *unordered* three-site set \(S\), designate those three sites for one type-\(B\) arrival, and designate all other sites for one type-\(A\) arrival. Arrival times are independent with the same continuous distribution. A proposed particle adsorbs if its site is empty and none of its nearest neighbors already contains the opposite type. Let \(E\) mean that the chosen three sites induce a connected three-site subgraph and that all three designated \(B\) attempts adsorb.

There are precisely two connected shapes: a straight three-site segment \(I\) and a bent three-site segment \(L_3\). For any specified site triple of the respective shape, the *exact* probabilities of all three type-\(B\) attempts succeeding are
\[
\Pr(\text{all three }B\text{ adsorb}\mid S\cong I)=\frac1{48},
\qquad
\Pr(\text{all three }B\text{ adsorb}\mid S\cong L_3)=\frac2{63}.
\]
Thus the bent shape has \(32/21\) times the success probability of the straight shape. Among successful connected three-seed configurations,
\[
\boxed{\Pr(S\cong L_3\mid E)=\frac{64}{85},\qquad
\Pr(S\cong I\mid E)=\frac{21}{85}.}
\]
Unconditionally, with \(N=L^2\),
\[
\Pr(E)=\frac{85N}{504\binom{N}{3}}.
\]
In particular, the selected bent-shape fraction \(64/85\) is strictly greater than its undriven geometric frequency \(2/3\), by \(22/255\).

The proof also gives an exact finite-neighborhood formula for the all-success probability for *any fixed finite set* of designated type-\(B\) sites on an arbitrary finite simple graph. This is a one-arrival-per-site, three-designated-seed experiment; it is **not** claimed to be the order-three concentration coefficient of the unrestricted repeated-attempt deposition model.

## Assumptions and scope

The lattice has undirected nearest-neighbor edges and periodic boundary conditions. The condition \(L\ge7\) prevents small-torus coincidences among the three seeds and their nearest-neighbor boundary. On every site exactly one initial arrival is prescribed: type \(B\) on \(S\) and type \(A\) on the complement. Arrival priorities are exchangeable and almost surely distinct (iid continuous); equivalent independent unit-rate exponential clocks may be used. Particles remain adsorbed permanently. Like types do not repel, unlike types on neighboring sites exclude each other. Reattempts at a site following a rejected arrival are immaterial to the event that *all three designated type-\(B\) arrivals succeed*.

For the graph formula, let \(G=(V,E_G)\) be a finite simple graph, let \(S\subset V\) have cardinality \(k\ge1\), and let \(H=\{a\in V\setminus S:\exists b\in S,\{a,b\}\in E_G\}\) be the set of exterior nearest neighbors of the designated sites. Write \(N(a)=\{b:\{a,b\}\in E_G\}\). Only the clocks on \(S\cup H\) can affect the event that every designated \(B\) adsorbs.

## Proof

**1. Exact acceptance condition.** Assign independent exponential time \(T_v\) of rate one to each vertex. For each exterior neighbor \(a\in H\), put \(U_a=\min\{T_b:b\in S\cap N(a)\}\). The event that *every* type-\(B\) seed adsorbs is precisely
\[
\mathcal E_S=\bigcap_{a\in H}\{T_a>U_a\}.
\]
Indeed, if \(T_a<U_a\), then at that time no neighboring designated \(B\) has appeared; since no other vertices can receive \(B\), the type-\(A\) particle at \(a\) adsorbs and permanently blocks at least one seed. Conversely, suppose all inequalities hold. Process the designated \(B\) clocks chronologically. Before a seed \(b\) appears, any exterior neighbor \(a\) whose type-\(A\) arrival occurred already must have had an even earlier neighboring designated \(B\) arrival (since \(T_a>U_a\)); that earlier \(B\) has blocked the \(A\) attempt. Induction shows that every designated \(B\) adsorbs. Type-\(A\) particles outside \(H\) cannot affect the event.

**2. General finite-neighborhood formula.** Fix an arrival order \(\sigma=(b_1,\ldots,b_k)\) of the designated seeds, with times \(0<t_1<\cdots<t_k\). Assign each \(a\in H\) to the *first seed in this order* adjacent to it, and write \(u_j(\sigma)\) for the number assigned to \(b_j\). Conditional on the seed times, the acceptance inequalities have probability \(\exp[-\sum_{j=1}^k u_j t_j]\). Multiplying by the density \(\exp[-\sum_{j=1}^k t_j]\) of the independent seed clocks gives
\[
\Pr(\mathcal E_S)=\sum_{\sigma\in\mathfrak S_k}
\int_{0<t_1<\cdots<t_k}
\exp\!\left[-\sum_{j=1}^k(1+u_j(\sigma))t_j\right]
\,dt_1\cdots dt_k.
\]
With increments \(\delta_1=t_1\) and \(\delta_j=t_j-t_{j-1}\) for \(j\ge2\), the integral factorizes exactly:
\[
\boxed{\Pr(\mathcal E_S)=\sum_{\sigma\in\mathfrak S_k}
\prod_{j=1}^k
\frac{1}{k-j+1+\sum_{i=j}^k u_i(\sigma)}.}
\]
All denominators are strictly positive. This identity is valid for every finite simple graph and every prescribed seed set. The same probability may independently be counted by uniformly permuting the \(k+|H|\) relevant initial arrivals and requiring every type-\(A\) boundary vertex to occur after at least one adjacent designated type-\(B\) vertex.

**3. Straight trimer.** Take \(S_I=\{(0,0),(1,0),(2,0)\}\). It has eight exterior neighbors, so the first factor is always \(1/11\). The six seed orders comprise three symmetry pairs. Their successive exterior assignment vectors \((u_1,u_2,u_3)\) are \((3,2,3)\), \((3,3,2)\), and \((2,3,3)\), each occurring twice. The general formula gives
\[
\Pr(\mathcal E_{S_I})
=2\left(\frac{1}{11\cdot7\cdot4}
+\frac{1}{11\cdot7\cdot3}
+\frac{1}{11\cdot8\cdot4}\right)
=\frac1{48}.
\]

**4. Bent trimer.** Take \(S_L=\{(0,0),(1,0),(0,1)\}\). Its exterior boundary contains seven sites. If the elbow arrives first, the vectors are \((2,3,2)\), with two permutations; if an arm arrives first, they are \((3,2,2)\), with four permutations. Hence
\[
\Pr(\mathcal E_{S_L})
=\frac{2}{10\cdot7\cdot3}+
\frac{4}{10\cdot6\cdot3}=\frac2{63}.
\]
This completes an exhaustive classification of the two connected three-site shapes of the square lattice.

**5. Exact shape law.** On the \(L\times L\) torus with \(L\ge7\), there are \(2N\) unordered straight trimers (two orientations per start) and \(4N\) unordered bent trimers (four distinct three-corner subsets per elementary square). A uniform unordered triple of sites has probability \(\binom N3^{-1}\) to equal any particular trimer. Weighting each shape by its success probability produces masses proportional to \(2N/48=N/24\) and \(4N(2/63)=8N/63\), respectively. Their sum is \(85N/504\), and their ratio yields the claimed conditional probabilities \(21/85\) and \(64/85\), as well as the unconditional event probability. \(\square\)

## Verification

The standalone dependency-free script `verify_triads.py` implements two different exact methods: integration over all \(k!\) seed-clock orders with rational arithmetic, and an integer dynamic program counting permissible permutations of all seed and neighboring type-\(A\) arrival sites. The two calculations agree on both triomino shapes, on the published nearest-neighbor two-seed benchmark \(1/16\), on the symmetries/translations tested, and on eight further nontrivial seed configurations. Its 171 exact assertions pass under Python 3 using only the standard library.

The integer permutation counts are \(831600\) out of \(11!=39916800\) for the straight trimer and \(115200\) out of \(10!=3628800\) for the bent trimer. These independently give the same rational values. The infinite family in the lattice circumference is proved by finite-neighborhood locality, not by extrapolating a set of computed sizes.

## Relationship to prior work

Martins, Dickman and Ziff (2022 preprint; 2023 journal publication) introduced and studied the two-species antagonistic square-lattice deposition setting and investigated how minority species cluster and affect percolation. Their Section III.2 explicitly reports exact or high-precision two-designated-type-\(B\)-arrival probabilities for several pair separations, including \(1/16\) for neighboring designated sites. The present result uses that model of designated attempts but determines the first connected cluster size with two inequivalent geometries, namely three sites. The cited paper discusses possible higher-order calculations without specifying the two three-seed probabilities or their exact shape-selection ratio. The general order-statistic formulation and the \(64/85\) selection law are the assessed contribution, not the two-seed data or the basic antagonistic exclusion rule.

## Limitations

The model fixes exactly three designated type-\(B\) trial locations among type-\(A\) locations. It must not be confused with the original unrestricted random-color stream, in which rejected proposals may be followed by different-color proposals and extra type-\(B\) arrivals can change higher-order coefficients. No claim is made for the third coefficient of unrestricted minority coverage, for continuous-space deposition, for site-dependent clocks, or for the thermodynamic percolation threshold. A much broader general order-statistics result may subsume the finite graph identity; comparison with such results remains a scholarly priority risk. The shape probability is exact under the stated conditional experiment but is not presented as an unconditional spontaneous-cluster frequency in the unrestricted model.

## References

1. P. H. L. Martins, R. Dickman, and R. M. Ziff, *Percolation in two-species antagonistic random sequential adsorption in two dimensions*, arXiv:2211.04622 (first submitted 2022-11-09), Phys. Rev. E **107**, 024104 (2023), https://arxiv.org/abs/2211.04622 and https://doi.org/10.1103/PhysRevE.107.024104.
2. J. W. Evans, *Random and cooperative sequential adsorption*, Rev. Mod. Phys. **65**, 1281–1329 (1993), https://doi.org/10.1103/RevModPhys.65.1281 (general background only).
