# Lucas–Fibonacci orbit census for synchronous majority dynamics on open ladders

## Finding

Let \(L_n=P_n\square K_2\) be the labelled open ladder with \(n\ge2\) rungs. In synchronous binary open-neighbour majority dynamics, a vertex adopts the strict majority of its neighbours and retains its current state in a tie. Let \(F_n\) denote this update, let \(Q_n=\#\operatorname{Fix}(F_n)\), and let \(P_n=\#\operatorname{Fix}(F_n^2)\). With the Fibonacci numbers \(f_0=0,f_1=1,f_{j+2}=f_{j+1}+f_j\) and Lucas numbers \(\ell_0=2,\ell_1=1,\ell_{j+2}=\ell_{j+1}+\ell_j\), the exact census is

\[
Q_n=2(f_{n+1}+1),\qquad
P_n=\ell_{2n}+1+3\mathbf1_{3\mid n}.
\]

Every orbit eventually has least period one or two, and the exact number \(N_n\) of **distinct primitive two-cycle orbits** (counting two alternating configurations as one orbit) is

\[
N_n=\frac{\ell_{2n}-2f_{n+1}-1+3\mathbf1_{3\mid n}}{2}.
\]

The first values of \((Q_n,P_n,N_n)\), for \(n=2,3,4,5,6,7,8\), are respectively \((6,8,1)\), \((8,22,7)\), \((12,48,18)\), \((18,124,53)\), \((28,326,149)\), \((44,844,400)\), and \((70,2208,1069)\). The term \(3\mathbf1_{3\mid n}\) is a genuine three-rung spatial resonance in the periodic-state census; no temporal period three is asserted. In particular, with \(\lambda=(3+\sqrt5)/2\),

\[
N_n\sim\tfrac12\lambda^n,
\qquad
\frac{P_n}{4^n}\sim\left(\frac{\lambda}{4}\right)^n,
\qquad
\frac{Q_n}{P_n}\longrightarrow0.
\]

## Assumptions and scope

The graph is simple, undirected, has the two labelled rows and \(n\) ordered rungs, and is *open*, not cyclic. At each of the four degree-two end vertices a tie is resolved by retaining that vertex's current bit. Equivalently, each endpoint updates by the majority of its own bit, its rung neighbour's bit, and its unique horizontal neighbour's bit. At every interior vertex, of degree three, the update uses its left, right, and rung neighbours. The counts concern labelled binary configurations, not row-exchange or spatial-reflection classes. A configuration belongs to \(\operatorname{Fix}(F_n^2)\) exactly when it is initially periodic of period dividing two; an eventually periodic but initially transient configuration is not counted in \(P_n\).

## Proof

**Transfer encoding.** Encode each rung of an ordered pair \((x,y)\) of consecutive configurations by the symbol \(a=(x_{\mathrm{top}},x_{\mathrm{bottom}},y_{\mathrm{top}},y_{\mathrm{bottom}})\in\{0,1\}^4\), giving sixteen symbols. Define \(\operatorname{maj}(a,b,c)=1\) when \(a+b+c\ge2\), and zero otherwise. For three adjacent rung-symbols \(a,b,c\), let \(H(a,b,c)\in\{0,1\}\) test the four equalities asserting that at the central rung \(F_n(x)=y\) **and** \(F_n(y)=x\). Concretely, writing \(a=(a_0,a_1,a_2,a_3)\), similarly for \(b,c\), these are

\[
\begin{aligned}
b_2&=\operatorname{maj}(a_0,b_1,c_0),&
 b_3&=\operatorname{maj}(a_1,b_0,c_1),\\
b_0&=\operatorname{maj}(a_2,b_3,c_2),&
 b_1&=\operatorname{maj}(a_3,b_2,c_3).
\end{aligned}
\]

Let \(S(a,b)\) test the analogous four equalities at the *first* rung, replacing the missing left neighbour by the central vertex's own bit; let \(E(a,b)\) test them at the *last* rung of a pair \((a,b)\), replacing the missing right neighbour by that vertex's own bit. Their explicit bitwise definitions are in `verify.py` and use only the preceding majority formula. Index a transfer state by an ordered pair \((a,b)\) of rung-symbols, yielding 256 states. Define the integer matrix and vectors

\[
T_{(a,b),(b',c)}=\mathbf1_{b=b'}H(a,b,c),\qquad
s_{(a,b)}=S(a,b),\qquad e_{(a,b)}=E(a,b).
\]

One-to-one correspondence between admissible paths in this transfer graph and paired configurations gives, for every \(n\ge2\),

\[
P_n=s^{\mathsf T}T^{n-2}e.
\]

For fixed configurations restrict the rung-symbols to the four satisfying \((a_0,a_1)=(a_2,a_3)\). Let \(T_f,s_f,e_f\) be the identically defined restricted transfer objects (or their zero-extended 256-state representatives). Then likewise

\[
Q_n=s_f^{\mathsf T}T_f^{n-2}e_f.
\]

**Finite exact identities.** A full enumeration of the sixteen symbols, 256 pair states, and 4096 possible symbol triples gives 36 nonzero entries in each boundary vector and 400 nonzero directed entries in \(T\). Direct integer evaluation on all 256 coordinates gives the **vector identities**

\[
(T^5-3T^4+T^3-T^2+3T-I)e=0,
\qquad
(T_f^3-2T_f^2+I)e_f=0.
\]

The eight-file package includes a standalone self-contained Python 3 implementation (`verify.py`) that enumerates **all** possible finite cases defining these operators, evaluates every coordinate of both residuals exactly as an integer, and asserts that all 512 residual coordinates vanish. These exhaustive finite identities are the exact certificate for an infinite-family recurrence, not a finite-length extrapolation. The same calculation gives

\[
(P_2,P_3,P_4,P_5,P_6)=(8,22,48,124,326),
\qquad (Q_2,Q_3,Q_4)=(6,8,12).
\]

The first annihilating polynomial factors as \((z^2-3z+1)(z^3-1)\), and the second as \((z-1)(z^2-z-1)\). The initial data therefore determine the solutions uniquely. The Lucas subsequence \(\ell_{2n}\) satisfies the first quadratic factor, the indicator \(\mathbf1_{3\mid n}\) satisfies the cubic factor, and \(f_{n+1}\) plus the constant term satisfies the second annihilator. Checking the displayed initial values proves the closed formulas for all \(n\ge2\).

**No higher temporal periods.** For completeness, encode binary states as spins \(\sigma_v\in\{-1,+1\}\). Let \(W\) be the symmetric adjacency matrix of \(L_n\), with an additional diagonal \(+1\) only at degree-two endpoint vertices. Then every coordinate of \(W\sigma\) is an *odd nonzero integer*, and the update reads \(\sigma_{t+1}=\operatorname{sgn}(W\sigma_t)\). For \(t\ge1\) put \(\mathcal E_t=-\sigma_t^{\mathsf T}W\sigma_{t-1}\). By symmetry of \(W\),

\[
\mathcal E_t-\mathcal E_{t+1}
=\sum_v[\sigma_{t+1}(v)-\sigma_{t-1}(v)](W\sigma_t)_v\ge0,
\]

and the inequality is strict whenever \(\sigma_{t+1}\ne\sigma_{t-1}\), since each nonzero summand equals \(2|(W\sigma_t)_v|\). Because the integer energy takes only finitely many values, \(\sigma_{t+1}=\sigma_{t-1}\) eventually. Thus every orbit ends in a fixed point or a primitive two-cycle, and each primitive two-cycle consists of exactly two members of \(\operatorname{Fix}(F_n^2)\setminus\operatorname{Fix}(F_n)\). Hence \(N_n=(P_n-Q_n)/2\).

**Growth.** The standard Binet formulas imply \(\ell_{2n}=\lambda^n+O(\lambda^{-n})\) and \(f_{n+1}=O(\varphi^n)\), with \(\varphi=(1+\sqrt5)/2<\lambda\). The asymptotic statements follow.

## Verification

`verify.py` requires only Python 3 standard-library features. Run `python3 verify.py` in the directory containing the script. It checks the two full transfer-vector polynomial identities, their exact initial values, and separately simulates **all 87,376 labelled initial configurations** on \(L_n\) for every \(2\le n\le8\), comparing each \(F_n\) and \(F_n^2\) fixed-set size with the formulas. `verification-output.txt` records the actual successful run. The finite simulations corroborate the independently sufficient transfer-vector identities but are not substitutes for them.

## Relationship to prior work

Goles and Olivos established the general eventual-period-at-most-two property for symmetric binary threshold networks; Benjamini, Chan, O'Donnell, Tamuz and Tan (2014) explicitly identify that theorem as background to their majority-dynamics results. Tamuz and Tessler (2013) study information retention and quantitative bounds under repeated majority, not exact periodic-state counts for ladder graphs. Nakar and Ron (2022) establish structural restrictions on periodic configurations for **one-row cyclic radius-\(r\)** majority automata, not the two-row open ladder with its rung interactions and degree-two boundary ties. The present claim is the exact, labelled, all-length two-row ladder census, including the modulo-three correction, growth rate and primitive-orbit normalization. Classical period-two theory, the transfer-matrix method, and Fibonacci/Lucas identities are not claimed as novel.

## Limitations

The result counts **initially recurrent** configurations and primitive two-cycle orbits, but does not provide the attraction-basin sizes, initial transient-depth distribution, or distribution of orbit selection under random starts. It concerns open ladders only and one specific tie-retaining rule. The integer-vector certificate is finite, exhaustive, and reproducible, but it is not a formally verified proof in an interactive theorem prover. An unindexed exact equivalent in historical cellular-automaton or Ising literature cannot be ruled out; no independent mathematical audit has been performed.

## References

1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics **30** (1980), 187–189. DOI: `10.1016/0012-365X(80)90121-1`.
2. O. Tamuz and R. J. Tessler, *Majority Dynamics and the Retention of Information*, arXiv:`1307.4035`, first posted 2013-07-15; see Sections 1.1–1.2 and 3.4.
3. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:`1405.2486`, first posted 2014-05-11; see Introduction and Theorem 1.1.
4. Y. Nakar and D. Ron, *The Structure of Configurations in One-Dimensional Majority Cellular Automata: From Cell Stability to Configuration Periodicity*, arXiv:`2205.08972`, first posted 2022-05-18; see Sections 1.1–1.6 and the related-work discussion.
