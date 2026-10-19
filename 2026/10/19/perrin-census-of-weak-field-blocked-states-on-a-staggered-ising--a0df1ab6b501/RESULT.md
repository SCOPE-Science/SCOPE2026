# Perrin census of weak-field blocked states on a staggered Ising ring

## Finding

For every even \(n\ge4\), \(J>0\), and \(0<h<2J\), the one-spin blocked configurations of the staggered-field ferromagnetic Ising ring have an exact *staggered-magnetization-resolved* census. With \(k\) spins opposing their individual local fields, the number is

\[
B_{n,k}=\begin{cases}
\displaystyle\frac{n}{k}\binom{k}{n-2k},&\lceil n/3\rceil\le k\le\lfloor n/2\rfloor,\\
0,&\text{otherwise}.
\end{cases}
\]

The total is the Perrin integer \(P_n\), characterized by \(P_0=3\), \(P_1=0\), \(P_2=2\), and \(P_n=P_{n-2}+P_{n-3}\) for every \(n\ge3\). In particular, for consecutive even circumferences \(n=4,6,8,10,12,14,16,18\), the counts are \(2,5,10,17,29,51,90,158\). Its exponential growth rate is exactly

\[
\lim_{m\to\infty}\frac{1}{2m}\log P_{2m}=\log\rho,
\qquad \rho^3-\rho-1=0,\quad\rho>1.
\]

Here \(\rho\approx1.324717957\) is the plastic constant. The regime \(0<h<2J\) is open: the endpoint \(h=2J\) instead admits all nonadjacent defect sets and has the **already known** Lucas-number ground-state count. The result concerns single-spin blocked configurations, not probabilities of dynamically reaching them.

## Assumptions and scope

There are \(n\) labeled sites indexed modulo \(n\), with \(n\) even and \(n\ge4\), and spins \(s_i\in\{-1,1\}\). The energy is

\[
H(s)=-J\sum_{i=0}^{n-1}s_i s_{i+1}-h\sum_{i=0}^{n-1}(-1)^i s_i,
\qquad J>0,\quad 0<h<2J.
\]

Each undirected nearest-neighbor bond is counted once. An admissible elementary move flips precisely one spin. A configuration is **blocked** if every such flip has nonnegative energy change. At a zero energy change, the move is forbidden by the specified strict-descent dynamics. For \(0<h<2J\), no local flip actually has zero energy, but the endpoint convention matters when comparing other field regimes.

Define the field-aligned gauge spin \(t_i=(-1)^i s_i\) and the binary defect \(d_i=(1-t_i)/2\). The statistic \(k=\sum_i d_i\) counts sites opposing the staggered field; correspondingly \(\sum_i(-1)^i s_i=n-2k\). The count distinguishes sites (configurations related by a rotation are not identified).

## Proof

**Step 1: Exact local stability.** Even circumference ensures that the change of variables is compatible with the periodic edge. It gives \(H=J\sum_i t_i t_{i+1}-h\sum_i t_i\). If the spin at site \(i\) is flipped, direct cancellation of the two affected bonds and the field term yields

\[
\Delta_i H=2t_i\bigl(h-J(t_{i-1}+t_{i+1})\bigr).
\]

When \(t_i=-1\) (a defect), the inequality \(\Delta_iH\ge0\), combined with \(0<h<2J\), holds exactly when both neighbors are \(+1\). Thus two defects can never be adjacent: the cyclic binary word must avoid \(11\). When \(t_i=+1\), the inequality holds exactly when at least one neighbor is \(-1\): a length-three cyclic block \(000\) is forbidden. The two conditions are sufficient as well as necessary, because all possible neighbor sums are \(-2,0,2\).

**Step 2: Count at fixed defect number.** A cyclic word avoiding \(000\) must contain a defect; the prohibition of \(11\) separates consecutive defects by either one or two zeros. If there are \(k\) defects, let \(a\) gaps contain one zero and \(b\) gaps contain two zeros. Then \(a+b=k\) and \(2a+3b=n\), so \(b=n-2k\), \(a=3k-n\). Such gaps exist if and only if \(\lceil n/3\rceil\le k\le\lfloor n/2\rfloor\). Choose a distinguished defect site (\(n\) choices) and an ordered cyclic list of its \(k\) following gap lengths, with \(b\) long gaps (\(\binom{k}{b}\) choices). Every labeled binary word with \(k\) defects is represented exactly \(k\) times, once for each choice of the distinguished defect. Thus \(B_{n,k}=n\binom{k}{n-2k}/k\). For excluded \(k\), no compatible gap list exists, giving zero.

**Step 3: Total and characteristic polynomial.** The three-state successor automaton for a defect \(1\), a first following zero, and an optional second following zero has adjacency matrix

\[
Q=\begin{pmatrix}0&1&0\\1&0&1\\1&0&0\end{pmatrix}.
\]

Its edges encode precisely the allowed excursions from one defect to the next, of total length two or three. Because every valid cyclic word has at least one defect, its state labeling is unique, and the number of length-\(n\) closed paths is the number of labeled cyclic binary words: \(P_n=\operatorname{tr}(Q^n)\) for all even \(n\ge4\). Direct determinant expansion gives \(\det(xI-Q)=x^3-x-1\), whence Cayley–Hamilton implies \(Q^3=Q+I\). Taking traces after multiplying by powers of \(Q\) gives the Perrin recurrence and initial traces \(3,0,2\).

**Step 4: Exponential rate.** The polynomial \(x^3-x-1\) has exactly one positive real root \(\rho>1\). Its two other roots are conjugate, and their common modulus is \(\rho^{-1/2}<1\) because the product of all three roots is one. Therefore \(P_n=\rho^n+O(\rho^{-n/2})\), and the announced positive entropy \(\log\rho\) follows through even \(n\).

## Verification

The accompanying script `verify_staggered.py` uses a direct enumeration of \(2^n\) physical-spin configurations and, separately, a four-state spin-pair transfer matrix. For even \(n=4,6,\ldots,18\), these independent calculations agree with the Perrin total in the entire weak-field regime sampled and with the field-resolved binomial census. For even \(n\le14\), an exhaustive configuration-by-configuration comparison checks the equivalence between physical energy-change inequalities and the forbidden-word condition. Symbolic matrix characteristic polynomials and exact integer recurrences are checked as well. These finite calculations support, but do not replace, the preceding all-size proof. Run with `python verify_staggered.py` using Python 3 and SymPy.

## Relationship to prior work

De Smedt, Godrèche and Luck (2002) count blocked states of several one-dimensional *kinetically constrained* chains, including a ferromagnetic constrained-Glauber and a Kawasaki system. Their explicit Fibonacci and higher-order growth constants arise from different forbidden words and dynamics. Their accessible full text does not state the present staggered-field, weak-field, magnetization-resolved Perrin law. Yi and Baek (2015) investigate a **spatially homogeneous field oscillating in time**, with zero-energy flips allowed at half rate; this is not the stationary staggered landscape studied here.

The staggered gauge transformation also relates this Hamiltonian to an antiferromagnetic ring with a spatially uniform longitudinal field. Castorene, Peña, Groves and Vargas (2025 preprint, 2026 revision) prove a **critical-field** Lucas-number ground-state degeneracy at \(h/J=2\). That important result is not claimed as new here. The weak-field metastable configurations counted in the theorem are local minima, not generally ground states. The 1989 paper by Masui, Southern and Jacobs treats spin-glass/random-ferromagnet local minima with a field using recursive methods; the publicly accessible abstract does not identify the exact period-two weak-field census. The complete source was not accessible in this review, so stronger overlap with it remains a real bibliographic uncertainty.

## Limitations

No dynamical basin sizes, hitting probabilities, finite-temperature lifetimes, odd-circumference staggered boundary twists, or arbitrary inhomogeneous fields are established. At \(h=0\) and \(h=2J\), local stability inequalities change and the weak-field formula does not apply. The proof is purely classical and uses strict energy-lowering moves. The absence of an identical result in the searches performed does not establish absolute priority; a full comparison to every general recursion for one-dimensional Ising metastability remains open.

## References

1. G. De Smedt, C. Godrèche and J. M. Luck, *Jamming, freezing and metastability in one-dimensional spin systems* (2002), arXiv:cond-mat/0202465, https://arxiv.org/pdf/cond-mat/0202465 .
2. S. D. Yi and S. K. Baek, *Interrupted coarsening in the zero-temperature kinetic Ising chain driven by a periodic external field* (2015), arXiv:1506.01098, https://arxiv.org/pdf/1506.01098 .
3. B. Castorene, F. J. Peña, M. H. E. Groves and P. Vargas, *Exact Combinatorial Density of States for the Critical 1D Ising Model* (arXiv:2511.01646, initial 2025 version, revised 2026), https://arxiv.org/pdf/2511.01646 .
4. S. Masui, B. W. Southern and A. E. Jacobs, *Metastable states of Ising spin glasses and random ferromagnets* (1989), Phys. Rev. B 39, 6925; DOI:10.1103/PhysRevB.39.6925 .
5. MSC2020, code 82C20, *Dynamic lattice systems (kinetic Ising, etc.) and systems on graphs*, https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=82C20 .
