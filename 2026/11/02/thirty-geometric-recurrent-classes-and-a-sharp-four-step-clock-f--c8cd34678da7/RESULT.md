# Thirty geometric recurrent classes and a sharp four-step clock for majority dynamics on the four-cube

## Finding

For synchronous binary neighbor-majority dynamics on \(Q_n\), \(1\le n\le4\), with tie retention, the complete temporal recurrence census is:

| Dimension | Fixed configurations | Primitive two-cycle orbits | Sharp maximum entry time |
| ---: | ---: | ---: | ---: |
| 1 | 2 | 1 | 0 |
| 2 | 6 | 1 | 1 |
| 3 | 8 | 28 | 1 |
| 4 | **702** | **885** | **4** |

For the sixteen-vertex four-cube, there are **14** geometric equivalence classes of fixed configurations and **16** geometric equivalence classes of primitive two-cycles under the full spatial automorphism group. Every starting state is eventually fixed or two-periodic, and \(F^6=F^4\) holds identically. All trajectories ending in a primitive two-cycle enter it no later than update 2; entrance times 3 and 4 occur only in the basin of fixed points.

The exact joint distribution of first periodic entrance time \(T\) and final primitive period \(p\) on \(Q_4\) is:

| \(T\) | \(p=1\) | \(p=2\) | Total |
| ---: | ---: | ---: | ---: |
| 0 | 702 | 1770 | 2472 |
| 1 | 9336 | 8000 | 17336 |
| 2 | 25344 | 9600 | 34944 |
| 3 | 8864 | 0 | 8864 |
| 4 | 1920 | 0 | 1920 |
| Total | 46166 | 19370 | 65536 |

Equivalently, the finite dynamical zeta function for \(Q_4\) is \(\zeta_F(z)=(1-z)^{-702}(1-z^2)^{-885}\).

## Assumptions and scope

The Boolean \(n\)-cube \(Q_n\) has vertices \(V_n=\{0,1\}^n\), labelled numerically by binary integers \(v\in\{0,\ldots,2^n-1\}\). Vertices are adjacent precisely when their labels differ in one bit. A configuration is a subset of vertices, equivalently an integer bit mask \(x\in\{0,\ldots,2^{2^n}-1\}\). Let \(c_v(x)\) be the number of occupied neighbors of \(v\). At each simultaneous step,

\[
F_n(x)_v=\begin{cases}1,&2c_v(x)>n,\\0,&2c_v(x)<n,\\x_v,&2c_v(x)=n.\end{cases}
\]

A configuration is periodic if \(F_n^p(x)=x\) for some positive integer \(p\). Its primitive period is the smallest such \(p\). For arbitrary initial \(x\), its first periodic entrance time \(T(x)\) is the smallest nonnegative \(t\) such that \(F_n^t(x)\) is periodic. Temporal two-cycles are unordered pairs of successive states. Geometric classes further identify such orbits under automorphisms of the cube; temporal and geometric orbit counts are never conflated. The claim is restricted to dimensions 1 through 4, not to all hypercubes.

## Proof

**Exact finite transition.** In numeric vertex labels, the neighbor mask of vertex \(v\) is

\[
M_n(v)=\sum_{i=0}^{n-1}2^{v\oplus 2^i},\qquad c_v(x)=\operatorname{popcount}(x\mathbin{\&}M_n(v)).
\]

The displayed rule therefore computes \(F_n(x)\) by finite integer arithmetic, with no numerical approximation or unspecified tie choice. Both attached complete programs implement this rule independently: `verify_hypercube.cpp` checks each possible configuration directly, while `verify_independent.py` uses precomputed neighborhood masks, constructs the entire functional digraph, and removes all noncyclic vertices by indegree pruning. There are exactly \(2^{2^n}\) configurations in dimension \(n\); in dimension four this is exactly 65,536. The programs iterate **every** state, not a sample. The C++ computation tests periodicity by the defining equality \(F_n^2(y)=y\), and the Python graph decomposition separately confirms that its only cycles have length 1 or 2. Both compute the table of fixed points, two-cycles, entrance times, and basin populations displayed above; the full executable checks are part of the proof certificate.

**Geometric classes.** Every automorphism of the cube is a translation of \((\mathbb{Z}/2\mathbb{Z})^4\) followed by a coordinate permutation. Indeed, an automorphism sends the zero vertex to one of 16 choices, permutes its four neighbors in 24 ways, and is then forced on every other vertex by the incidence structure. Thus the full group is \((\mathbb{Z}/2\mathbb{Z})^4\rtimes S_4\), of size 384. Its action on configurations commutes with majority updating and hence descends to an action on unordered temporal two-cycles. The Python checker exhausts all 384 automorphisms, constructs spatial orbits from representatives, and checks that these orbits partition **all** recurrent configurations obtained from its full-state digraph.

The complete fixed-configuration representatives (decimal masks), with their geometric orbit sizes, are:

| Representative | Class size |
| ---: | ---: |
| `0` | 1 |
| `15` | 24 |
| `63` | 96 |
| `255` | 8 |
| `831` | 32 |
| `855` | 48 |
| `863` | 192 |
| `975` | 96 |
| `1023` | 96 |
| `1911` | 48 |
| `4080` | 12 |
| `4095` | 24 |
| `7128` | 24 |
| `65535` | 1 |

The complete primitive two-cycle representatives, displayed as \((x,F_4(x))\), and their geometric class sizes are:

| First state | Next state | Class size |
| ---: | ---: | ---: |
| `879` | `927` | 192 |
| `1659` | `2487` | 192 |
| `875` | `919` | 96 |
| `1915` | `2999` | 96 |
| `111` | `159` | 48 |
| `1785` | `2550` | 48 |
| `1791` | `2559` | 48 |
| `7140` | `10200` | 48 |
| `1641` | `2454` | 24 |
| `1647` | `2463` | 24 |
| `1695` | `2415` | 24 |
| `27039` | `38511` | 24 |
| `105` | `150` | 8 |
| `27135` | `38655` | 8 |
| `15555` | `49980` | 4 |
| `27030` | `38505` | 1 |

The first class sizes sum to 702. The second class sizes sum to 885 **temporal** two-cycles. These lists also appear in `orbit_classes.csv`, generated reproducibly by the independent graph-decomposition code. No class duplicates another, because each class is removed in its entirety before the next representative is selected.

**Sharp entry clock.** The complete digraph gives no state of entrance time greater than 4, which proves \(F_4^6=F_4^4\). Sharpness is witnessed by the state-mask trajectory \(1972\to1377\to276\to1\to0\to0\), whose first periodic state occurs at time 4. The same exhaustive check establishes the two-period basin cutoff at time 2 and the strict dimensional transition between \(Q_3\) and \(Q_4\).

## Verification

From the directory containing the standalone artifacts, run:

```sh
g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_hypercube.cpp -o verify_hypercube
./verify_hypercube > cert_full.txt
python3 verify_independent.py > independent_output.txt
```

The first program enumerates all \(4+16+256+65536=65812\) labelled initial configurations over the four cube dimensions and writes the complete \(Q_4\) list of 885 temporal two-cycle representatives. The second program uses a distinct transition implementation and functional-digraph pruning, checks all 65,536 four-cube configurations, and constructs the 30 spatial classes from all 384 group elements. The included `cert_full.txt`, `independent_output.txt`, and `orbit_classes.csv` are the actual outputs from these programs. No probabilistic experiment or extrapolation is used.

## Relationship to prior work

Goles and Olivos proved the **general** eventual period-at-most-two theorem for symmetric threshold systems; that theorem does not enumerate recurrent states, graph-automorphism types, or exact transient layers of the four-cube. Benjamini, Chan, O'Donnell, Tamuz, and Tan (first public preprint 2014-05-11) study majority dynamics on unimodular and random graphs and establish qualitative and probabilistic results. Kaaser, Mallmann-Trenn, and Natale (2016) develop general voting-time bounds and a complexity theorem. The present classification is specific to the four-cube and supplies exact finite values not implied by those general statements. Work on majority dynamics on simple cycles counts stable configurations for a different underlying graph. No claim is made to rediscover the general period-two theorem or to settle dynamics of higher-dimensional cubes.

## Limitations

The 30-class recurrent census and the exact basin numbers are confined to the finite, labelled sixteen-vertex cube with synchronous updates and tie retention. They are rigorous exhaustive finite counts, but do not establish formulae for dimensions at least five or stochastic/asynchronous updates. Search of indexed literature did not uncover the exact same 30-class computation; an earlier unindexed enumeration could still exist. The attached code and output are finite computation certificates, not independently audited mathematical proofs by an outside reviewer.

## References

1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, DOI: 10.1016/0012-365X(80)90121-1.
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, first arXiv version 2014-05-11, arXiv:1405.2486.
3. D. Kaaser, F. Mallmann-Trenn, and E. Natale, *On the Voting Time of the Deterministic Majority Process*, MFCS 2016, DOI: 10.4230/LIPIcs.MFCS.2016.55.
4. A. N. Zehmakan, *Majority opinion diffusion: when tie-breaking rule matters*, Autonomous Agents and Multi-Agent Systems (2024), DOI: 10.1007/s10458-024-09651-y.
