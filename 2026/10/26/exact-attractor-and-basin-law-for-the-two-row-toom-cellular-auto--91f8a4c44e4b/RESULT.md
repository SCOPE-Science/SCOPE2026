# Exact attractor and basin law for the two-row Toom cellular automaton

## Finding

For each integer \(n\ge2\), put a binary spin at each site of the periodic strip \(\mathbb Z/2\mathbb Z\times\mathbb Z/n\mathbb Z\), and simultaneously replace each spin by the majority of itself, its north neighbour, and its east neighbour (the deterministic North–East–Center, or NEC, Toom rule). Let \(F_n\) be the resulting map on \(4^n\) labelled configurations. The following statements together give the complete finite-state attractor, basin and first-periodic-entry census.

**Periodic configurations and primitive periods.** Exactly \(2^{n+1}\) configurations are recurrent: \(2^n\) column-uniform fixed points and \(2^n\) entirely column-discordant states on which \(F_n\) acts as the cyclic one-step shift. Hence
\[
\#\operatorname{Fix}(F_n^k)=2^n+2^{\gcd(n,k)}\quad(k\ge1),
\]
including \(2^n+2\) fixed states. Every primitive period divides \(n\), and every positive divisor of \(n\) is attained. For \(d\mid n\), the number of distinct primitive \(d\)-cycles is
\[
N_d(n)=\frac1d\sum_{e\mid d}\mu(d/e)2^e+\mathbf1_{\{d=1\}}2^n.
\]

**Complete fixed-point basins.** A fixed configuration has identical spins in its two rows, so identify it with a cyclic binary word \(y=(y_0,\ldots,y_{n-1})\). Let
\[
b(y)=\#\{i\in\mathbb Z/n\mathbb Z:y_i\ne y_{i+1}\}.
\]
Its exact attraction-basin cardinality, including the fixed point itself, is
\[
\boxed{B_n(y)=\begin{cases}3^n-2^n,&b(y)=0,\\3^{n-b(y)},&b(y)>0.\end{cases}}
\]
Thus two consensus fixed points each have basin \(3^n-2^n\). The number of nonconstant fixed points with boundary count \(b\) is \(2\binom nb\) for even \(2\le b\le n\), and zero for odd \(b\). No transient enters the travelling subsystem; the attraction basin of each primitive travelling orbit of period \(d\) has size exactly \(d\), consisting of the orbit itself.

**Sharp transients and exact distribution.** For an initial configuration \(x\) write \(m_i=1\) when the two spins in column \(i\) disagree, and \(m_i=0\) otherwise. When the mask has both symbols, the first-periodic-entry time \(\tau(x)\) equals the longest cyclic run of ones in \(m\). For the constant masks \(0^n\) and \(1^n\), \(\tau(x)=0\). Consequently \(\max_x\tau(x)=n-1\), attained by a mask with precisely one zero, and
\[
F_n^{2n-1}=F_n^{n-1}.
\]
For integer \(0\le t\le n-1\), the *exact* number of initial configurations entering a periodic orbit by time \(t\) is
\[
E_n(t)=2^n\left[1+\sum_{k=1}^{n}\frac nk[u^{n-k}](1+u+\cdots+u^t)^k\right].
\]
The number entering at time exactly \(t\ge1\) is \(E_n(t)-E_n(t-1)\), and \(E_n(0)=2^{n+1}\).

**Typical time and basin contrast.** Under uniform independent initial spins, \(\tau(x)/\log_2 n\to1\) in probability as \(n\to\infty\), despite the sharp worst-case time \(n-1\). The probability of eventual consensus is exactly \(2(3^n-2^n)/4^n\), tending exponentially to zero; the probability of ever reaching a nonfixed travelling cycle is exactly \(2^{-n}-2^{1-2n}\), because the travelling subsystem has no outside predecessors.

## Assumptions and scope

The domain is the finite quotient of the square lattice with **two distinct rows** and \(n\ge2\) columns, with periodic boundary conditions in both directions. The north neighbour switches row without changing column; the east neighbour advances the column index modulo \(n\). An individual update uses the three separately defined sites (center, north, east) and has no stochastic errors. Configurations are labelled by column, so rotations are not identified. A *basin* is the set of labelled initial states eventually reaching the specified periodic orbit; for fixed states it is the set eventually equal to the indicated fixed point. The first-periodic-entry time is the smallest nonnegative \(t\) such that \(F_n^t(x)\) belongs to a periodic orbit. A recurrent configuration means a periodic point of the finite map \(F_n\).

## Proof

**1. Exact four-symbol reduction.** Write column \(i\) as the ordered pair \(c_i=(a_i,b_i)\in\{00,11,01,10\}\). Because the other spin in the column is the north neighbour, if \(a_i=b_i\) then both have a majority of two equal votes and the column remains unchanged. If \(a_i\ne b_i\), the center and north votes cancel, and the east vote decides independently in each row. Thus, *exactly*:
\[
(F_nc)_i=\begin{cases}c_i,&c_i\in\{00,11\},\\c_{i+1},&c_i\in\{01,10\}.
\end{cases}\tag{1}
\]
This reduction holds on the full \(4^n\)-state space without approximations.

**2. Recurrent states and periods.** Each column-uniform symbol \(00\) or \(11\) is permanent under (1). If any such anchor is present, every adjacent run of discordant symbols \(01\) or \(10\) is replaced from right to left by that run's next uniform anchor. At least one more symbol becomes uniform on every step until none is discordant. A periodic state containing an anchor therefore must consist solely of uniform columns, hence is fixed. If there is no anchor, (1) cyclically shifts the length-\(n\) binary word over the two discordant symbols, bijectively. This gives all \(2^n+2^n\) periodic states and their allowable periods. A word is fixed by shift to the power \(k\) iff it is constant on each of the \(\gcd(n,k)\) cycles of the corresponding index permutation, giving \(2^{\gcd(n,k)}\). Möbius inversion on divisors counts primitive words, and division by their period counts orbits. The \(2^n\) fixed uniform states supply the separate \(d=1\) term.

**3. Basin formula, including the cyclic boundary.** Suppose the target uniform fixed state is the binary word \(y\). A starting configuration reaching \(y\) must have at least one uniform column (all-discordant states stay all-discordant). Let \(S\) be its nonempty set of initially uniform columns. These anchors never move. Every initial discordant column eventually copies the value of the first uniform column strictly to its right, traversing the cyclic index. Hence the limit equals \(y\) precisely when every outgoing color-change index \(i\), with \(y_i\ne y_{i+1}\), is an anchor in \(S\), and the uniform columns initially carry the values prescribed by \(y\). Necessity follows because a nonanchor at such an index would converge to the same color as column \(i+1\). Sufficiency follows because all intervals between successive required anchors have constant target color. If \(b(y)>0\), the \(b(y)\) required anchor sites each have exactly one initial choice; each of the other \(n-b(y)\) sites independently is either the prescribed uniform pair (one choice) or one of the two discordant pairs (two choices). This yields \(3^{n-b(y)}\). If \(b(y)=0\), the same \(3^n\) choices are available but the all-discordant set of \(2^n\) states must be removed. The cyclic boundary-count multiplicities follow from choosing an even number of changes among \(n\) edges and choosing the first bit in two ways. Any orbit in the all-discordant set has no outside predecessors because the presence of a uniform column is permanent. Its attraction basin is exactly the states of that orbit (not a singleton when its period exceeds one).

**4. Sharp entrance time.** In a mixed anchor/discordant mask, each maximal cyclic discordant run loses exactly its rightmost discordant column per update. Its length decreases by one until it disappears; no new discordant symbols form. Thus \(\tau\) equals the maximum initial run length. In the two constant-mask cases the starting state is already recurrent. With at least one anchor, the longest possible run has length \(n-1\); this is attained by a unique-anchor mask. After \(n-1\) updates all configurations lie in the recurrent subset, on which the \(n\)-step map is the identity. This proves the stated functional identity.

**5. Distribution by bounded cyclic compositions.** Fix the binary anchor mask and let \(k\) be the number of uniform columns, \(1\le k\le n\). Mark one of the \(k\) anchors, select its labelled position in \(n\) ways, and list the \(k\) subsequent discordant run lengths. They form a weak composition of \(n-k\) with every part at most \(t\) exactly when \(\tau\le t\). The bounded-composition count is \([u^{n-k}](1+u+\cdots+u^t)^k\). Because each labelled mask is counted \(k\) times (one per marked anchor), divide by \(k\). Add the one all-discordant mask, which is recurrent at time zero. Each binary mask admits exactly \(2^n\) independent refinements into the original four column symbols. This gives \(E_n(t)\).

**6. Typical logarithmic time.** For independent fair initial spins, each column is discordant independently with probability \(1/2\). Let \(L\) be the longest cyclic run of discordant columns, except set \(L=0\) on the all-discordant mask. For any fixed \(0<\varepsilon<1\), set \(s=\lceil(1+\varepsilon)\log_2n\rceil\). A union bound over \(n\) possible cyclic starts gives \(\mathbb P(L\ge s)\le n2^{-s}\to0\). For \(r=\lfloor(1-\varepsilon)\log_2n\rfloor\), take \(\lfloor n/r\rfloor\) pairwise disjoint runs of length \(r\). Except for the all-discordant mask (probability \(2^{-n}\)), if any such run is all discordant, then \(L\ge r\). Therefore
\[
\mathbb P(L<r)\le (1-2^{-r})^{\lfloor n/r\rfloor}+2^{-n}\to0.
\]
Together these bounds prove \(L/\log_2n\to1\) in probability. The consensus-basin fraction follows by dividing the two consensus basin counts by \(4^n\). The nonfixed travelling states consist of \(2^n-2\) discordant words of primitive period at least two, with no external predecessors, giving \((2^n-2)/4^n\).

## Verification

The standalone stdlib script `verify.py` enumerates all \(4^n\) configurations for each integer \(2\le n\le8\) (\(87{,}376\) labelled configurations in total). It separately implements the original two-row majority rule and the four-symbol reduction, then compares one-step images and explicit trajectories. It checks recurrence counts, primitive-period spectra, individual fixed-state basin sizes, sharp entrance times and every cumulative bounded-composition count \(E_n(t)\). The recorded output `VERIFY_OUTPUT.txt` ends with `VERIFY_OK`. These finite checks corroborate—but do not replace—the all-size proof above.

## Relationship to prior work

Toom's North–East–Center majority rule and its erosion geometry are classical. Gács (arXiv:math-ph/0102009, first posted 8 February 2001) analyzes planar and toroidal erosion and winding components but does not give the two-row labelled basin spectrum or the exact first-entrance distribution above. Makowiec (1997) examines stationary configurations for NEC dynamics with periodic boundaries, predominantly numerically; the consulted abstract does not establish these exact thin-torus basin formulas. Jen (1988) develops general finite-cylinder attractor techniques and discusses shifts, which are compatible with the travelling part here; a generic procedure to compute attractors does not by itself supply the explicit two-row Toom basin law. Ayyer (arXiv:1503.00086, first posted 28 February 2015) studies a *different* finite stochastic one-dimensional interface/exclusion variant and supplies no result on this deterministic two-row torus. The claim is an explicit structural and quantitative classification for the specified Toom quotient, not a general assertion about all NEC tori.

## Limitations

The results assume exactly two rows, periodicity in both directions and the noiseless NEC vote. No formula is asserted for taller tori, noisy dynamics, other update schemes, or nonperiodic boundaries. The logarithmic typical-entry statement assumes independent unbiased initial spins. The generic 1988 cylinder paper and a 1997 toroidal Toom paper could not be inspected beyond accessible abstracts, so a historical equivalent not indexed by the searches remains a residual originality risk. Mathematical correctness has been reviewed here but independently validated results have not been supplied.

## References

1. P. Gács, *A Toom rule that increases the thickness of sets*, arXiv:math-ph/0102009, first version 8 February 2001. https://arxiv.org/abs/math-ph/0102009.
2. D. Makowiec, *Ground-state configurations for Toom cellular automata: Experimental hints*, Physical Review E 56, 5195 (1997), published 1 November 1997, DOI:10.1103/PhysRevE.56.5195. https://doi.org/10.1103/PhysRevE.56.5195.
3. E. Jen, *Cylindrical cellular automata*, Communications in Mathematical Physics 118, 569–590 (1988), DOI:10.1007/BF01221109. https://doi.org/10.1007/BF01221109.
4. A. Ayyer, *A finite variant of the Toom Model*, arXiv:1503.00086, first version 28 February 2015. https://arxiv.org/abs/1503.00086.
