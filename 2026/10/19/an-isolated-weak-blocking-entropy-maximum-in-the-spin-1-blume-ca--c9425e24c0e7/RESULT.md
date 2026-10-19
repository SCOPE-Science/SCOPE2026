# An isolated weak-blocking entropy maximum in the spin-1 Blume–Capel ring

## Finding
For every integer \(n\ge3\), every \(J>0\), and every crystal-field ratio \(\delta=D/J>0\), consider spins \(s_i\in\{-1,0,1\}\) on a labelled cycle of length \(n\), with periodic indices and energy
\[
H(s)=-J\sum_{i=0}^{n-1}s_i s_{i+1}+D\sum_{i=0}^{n-1}s_i^2.
\]
A configuration is **weakly blocked** if changing any one spin to either of the other two spin values never strictly lowers \(H\). Energy-neutral changes are allowed by this definition. Let \(B_n(\delta)\) be the number of such configurations, and let \(h(\delta)=\lim_{n\to\infty}n^{-1}\log B_n(\delta)\).

The limit exists, and its exact complete positive-crystal-field classification is
\[
 h(\delta)=
 \begin{cases}
 \log\lambda_{<}, &0<\delta<1,\\
 \log\lambda_{*}, &\delta=1,\\
 0, &\delta>1,
 \end{cases}
\]
where \(\lambda_{<}=1.465571231876768\ldots\) is the unique real root larger than one of \(t^3-t^2-1=0\), and \(\lambda_{*}=1.897179401065394\ldots\) is the largest positive root of \(t^4-2t^3+t^2-t-1=0\). More precisely, \(B_n(\delta)\sim\lambda_{<}^{n}\) when \(0<\delta<1\), and \(B_n(1)\sim\lambda_{*}^{n}\). For \(1<\delta\le2\), \(B_n(\delta)=3\) exactly; for \(\delta>2\), \(B_n(\delta)=1\) exactly. Therefore \(\delta=1\) is an **isolated strict global maximum of weak-blocking entropy** throughout the positive crystal-field axis.

At this same coupling, the Hamiltonian is a sum of squares,
\[
H(s)/J=\frac12\sum_i(s_i-s_{i+1})^2,
\]
so **there are exactly three true ground states**, the constant configurations, even though there are \(\lambda_{*}^{n}(1+o(1))\) one-site-stable configurations. The ground-state entropy density is zero for every positive \(\delta\), in contrast with the singular weak-blocking entropy.

## Assumptions and scope
Spins are labelled at sites; global reversal and cyclic rotation are **not** quotiented out. Adjacent sites are the two distinct cyclic neighbours, including at \(n=3\). One attempted move replaces one existing spin by either alternative member of \(\{-1,0,1\}\). Zero energy difference is allowed in the definition of stability, but this does not assert absorbing behaviour for dynamics that execute neutral moves. No external magnetic field, disorder, or multiparticle move is present. Positive \(J,D\) are arbitrary real numbers; only their ratio enters the count.

## Proof
**1. Exact local test.** If the two neighbours of site \(i\) have values \(a,c\), replacing its spin with \(u\) changes only the local objective \(f_{a,c}(u)=\delta u^2-(a+c)u\). For the five possible sums \(a+c\in\{-2,-1,0,1,2\}\), direct comparison of \(u=-1,0,1\) gives these precise conditions:

* For \(0<\delta<1\), at neighbour-sum zero only spin zero minimizes, and at nonzero neighbour-sum only its sign minimizes.
* At \(\delta=1\), at neighbour-sum zero only zero minimizes; at absolute neighbour-sum one, both zero and its sign minimize; at absolute neighbour-sum two, only its sign minimizes.
* For \(1<\delta<2\), only zero minimizes when the absolute neighbour-sum is at most one; for absolute neighbour-sum two only the matching nonzero sign minimizes.
* At \(\delta=2\), zero and the matching sign both minimize at absolute neighbour-sum two, while zero alone minimizes otherwise.
* For \(\delta>2\), only zero minimizes for every neighbour-sum.

If \(\delta>1\) and a site is nonzero in a blocked configuration, both its neighbours must equal that same nonzero spin. Connectivity of the cycle forces the entire configuration to be constant. Conversely, the two nonzero constant configurations are blocked exactly up to \(\delta=2\), and the zero configuration is always blocked. This proves the stated exact counts for \(\delta>1\).

**2. Finite-size exact transfer formula.** Order the nine pairs \((a,b)\in\{-1,0,1\}^2\) lexicographically. Define the explicit integer matrix \(T_{\delta}\) by
\[
 (T_{\delta})_{(a,b),(b',c)}=
 \mathbf 1_{\{b=b'\}}\,\mathbf 1_{\{f_{a,c}(b)\le f_{a,c}(u)\ \forall u\in\{-1,0,1\}\}}.
\]
A cyclic closed walk of length \(n\) through overlapping pairs specifies precisely one labelled cyclic spin word; the successive edge tests check all its sites. Consequently, for every \(n\ge3\),
\[
B_n(\delta)=\operatorname{tr}(T_{\delta}^{n}).
\]
Exact integer determinant evaluation yields
\[
\begin{aligned}
\det(tI-T_{\delta})
&=t^2(t-1)(t^3-t^2-1)(t^3-t^2+1),&&0<\delta<1,\\
&=t^2(t^3-t^2+1)(t^4-2t^3+t^2-t-1),&&\delta=1,\\
&=t^6(t-1)^3,&&1<\delta\le2,\\
&=t^8(t-1),&&\delta>2.
\end{aligned}
\]
These formulae are reproducible from the nine entry definitions by `verify.py`, which checks all characteristic polynomials symbolically. They also provide exact finite-ring counts without root approximations.

**3. Structural derivation of the dominant roots.** For \(0<\delta<1\), every blocked configuration except the three constant words consists of nonzero monochromatic domains of length at least two, alternating in sign, with exactly one zero separating successive domains. Conversely every such cyclic composition is blocked. Let \(z\in(0,1)\) mark each site. The weight of one nonzero run is \(A(z)=z^2/(1-z)\). The two-sign renewal transfer between successive runs has off-diagonal weight \(A(z)z=z^3/(1-z)\) and diagonal zero. Its Perron eigenvalue first reaches one at \(z=1/\lambda_{<}\), where \(\lambda_{<}^3-\lambda_{<}^2-1=0\).

At \(\delta=1\), nonzero runs still have length at least two and opposite signs cannot be adjacent. A zero run of length one may separate only **opposite** nonzero signs, whereas a zero run of length at least two can separate arbitrary nonzero signs. The sign-renewal transfer therefore has diagonal entry \(A(z)z^2/(1-z)\), and off-diagonal entry \(A(z)[z+z^2/(1-z)]\). Its positive-row-sum Perron eigenvalue is \(z^3(1+z)/(1-z)^2\). The value one is reached at \(z=1/\lambda_{*}\), giving \(\lambda_{*}^4-2\lambda_{*}^3+\lambda_{*}^2-\lambda_{*}-1=0\). Both nontrivial cyclic-word systems possess a self-loop and a strongly connected dominant component, so their positive dominant transfer eigenvalue is algebraically simple and strictly dominates the remaining eigenvalues. The exact characteristic factorizations above give the same conclusion independently. Hence the trace asymptotics have coefficient one.

For the strict comparison, the low-coupling equation gives \(\lambda_{<}\in(1,2)\) and substitution into the critical polynomial gives \(\lambda_{<}^4-2\lambda_{<}^3+\lambda_{<}^2-\lambda_{<}-1=-2\). The critical renewal Perron function is strictly decreasing in \(\lambda=1/z>1\), equals more than one at \(\lambda_{<}\), and equals one at \(\lambda_{*}\). Thus \(\lambda_{*}>\lambda_{<}>1\).

**4. Ground-state contrast.** For every \(\delta>0\), rewrite
\[
H(s)/J=\frac12\sum_i(s_i-s_{i+1})^2+(\delta-1)\sum_i s_i^2.
\]
If \(0<\delta<1\), this expression is at least \((\delta-1)n\), with equality only for the two constant nonzero words. At \(\delta=1\), it vanishes precisely for the three constant words. Above one, it is minimized uniquely by the all-zero configuration. Thus the ground-state count never grows exponentially.

## Verification
The standalone script `verify.py` independently recomputes the Hamiltonian before and after every one-site recolouring for all \(3^n\) labelled words at each \(n=3,\ldots,8\), for five rational field ratios representing the two open intervals and both transition points. It compares the counts with the exact transfer traces (30 independent count comparisons), checks five integer characteristic polynomials, and checks the polynomial-remainder identity establishing the root separation. The independently calculated counts at length eight, for \(\delta=1/2,1,3/2,2,5/2\), are \(27,171,3,3,1\), respectively. Executing `python verify.py` requires Python 3 and SymPy. Enumeration is finite corroboration only; the all-length statements follow from the proof above.

## Relationship to prior work
Blume's foundational three-state magnetic model (1966) provides the physical Hamiltonian. Fiig, Gorman, Rikvold, and Novotny (1994) study competing metastable free-energy branches in a **weak, long-range** Blume–Capel regime. Waclaw and Burda (2008) study one-spin-stable configurations for **binary** Ising spin glasses with random bonds. Yamamoto and Park (2013) investigate nucleation lifetimes in a **two-dimensional** spin-1 system under two dynamics; the distinction between neutral and energetically reducing moves motivates specifying weak blocking precisely. Chen and Shen (2015) study nucleation pathways on heterogeneous networks. None of the inspected portions provides the exact finite-ring one-step minima count and singular positive-crystal-field entropy derived here. Such a noncoverage assessment is restricted to materials actually inspected; the 1994 full article was not accessible for complete checking.

## Limitations
The result counts one-site weak energy minima, not dynamically absorbing states for rates that admit neutral moves and not configurations stable under multi-site changes. It gives no relaxation-time law, nucleation probability, fixed-magnetization count, disorder extension, or finite-temperature singularity. The novelty comparison remains subject to equivalent formulae in differently indexed older literature; the 1994 long-range article could not be fully inspected.

## References
Blume, M., *Theory of the First-Order Magnetic Phase Change in UO2*, Physical Review **141**, 517–524 (1966), DOI:10.1103/PhysRev.141.517 (public 1966-01-14).

Fiig, T., Gorman, B. M., Rikvold, P. A., and Novotny, M. A., *Numerical transfer-matrix study of a model with competing metastable states*, Physical Review E **50**, 1930–1947 (1994), DOI:10.1103/PhysRevE.50.1930.

Waclaw, B., and Burda, Z., *Counting metastable states of Ising spin glasses on arbitrary graphs*, Physical Review E **77**, 041114 (2008), arXiv:0801.1224 (public 2008-01-08).

Yamamoto, Y., and Park, K., *Metastability for the Blume-Capel model with distribution of magnetic anisotropy using different dynamics*, Physical Review E **88**, 012110 (2013), DOI:10.1103/PhysRevE.88.012110.

Chen, H., and Shen, C., *Nucleation of a three-state spin model on complex networks*, arXiv:1501.00347 (first public 2015-01-02).
