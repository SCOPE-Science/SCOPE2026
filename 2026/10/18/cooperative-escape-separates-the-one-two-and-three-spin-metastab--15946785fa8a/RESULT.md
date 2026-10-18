# Cooperative escape separates the one-, two-, and three-spin metastable entropies of the triangular plaquette model

## Finding
For the Newman–Moore triangular three-spin Ising plaquette Hamiltonian on the periodic \(L\times L\) square-coordinate torus with \(L=2^k\ge8\), let \(A_L^{(r)}\) be the number of spin configurations for which no simultaneous flip of between one and \(r\) distinct spins reduces the energy. Let \(P_L(z)\) be the independence polynomial of the triangular-neighbor graph on the same torus. Then
\[
 A_L^{(1)}=A_L^{(2)}=P_L(1),\qquad
 \frac{A_L^{(3)}}{A_L^{(1)}}\le \exp\!\left(-\frac{L^2}{100\cdot 2^{25}}\right).
\]
Indeed, the complete one-spin-stable energy-counting polynomial is \(P_L(z)\): the weight \(z\) records the number of frustrated plaquettes. Thus the first cooperative move size at which a positive metastable-complexity deficit can be forced is three, and the deficit is *extensive*, not just a finite exceptional set. In particular, along dyadic lengths, the limsup of the three-spin-stable entropy per site lies at least \(1/(100\cdot2^{25})\) below the usual hard-hexagon entropy \(\log\kappa_{\rm HH}(1)\).

## Assumptions and scope
Use vertices \(v=(i,j)\) in \((\mathbb Z/L\mathbb Z)^2\). Spins \(s_v\in\mathbf F_2\) define plaquette defects
\[
 d_{i,j}=s_{i,j}+s_{i-1,j}+s_{i,j-1}\pmod2,
 \qquad H(s)=J\sum_{i,j}d_{i,j},\quad J>0.
\]
This convention is a coordinate reversal of common triangular-plaquette conventions; physically each spin belongs to three upward-oriented triangles. An \(r\)-spin-stable configuration is stable for **every** nonempty subset of at most \(r\) distinct vertices, flipped simultaneously (not successive relaxation). Neutral moves are allowed; a move is destabilizing only when \(\Delta H<0\). For \(r=1\), energy changes are odd multiples of \(J\), so neutral single flips never arise. Let \(G_L\) be the six-neighbor triangular graph whose adjacency differences are \(\pm(1,0),\pm(0,1),\pm(1,-1)\), and let \(P_L(z)=\sum_{D\subseteq V(G_L),\,D\text{ independent}}z^{|D|}\). We use dyadic sizes to ensure an exact spin–defect bijection; claims about nondyadic tori are not made.

## Proof
**1. The defect coordinates are globally independent.** Let \(X\) and \(Y\) be the two commuting cyclic coordinate shifts over \(\mathbf F_2\). The spin-to-defect operator is \(T=I+X+Y\). In characteristic two and for \(L=2^k\), Frobenius gives
\[
 T^L=I+X^L+Y^L=I+I+I=I.
\]
Thus \(T\) is invertible with inverse \(T^{L-1}\); every binary defect pattern corresponds to exactly one spin configuration. A spin flip at \(v=(i,j)\) toggles the three sites \(T_v=\{v,v+(1,0),v+(0,1)\}\). The change in energy is \(\Delta H=J(3-2|D\cap T_v|)\), where \(D\) is the defect set. Nonnegative changes for all \(v\) are equivalent to \(|D\cap T_v|\le1\) for all \(v\). Every triangular-neighbor edge is contained in some such three-site triangle, and every pair within one triangle is an edge. Hence one-spin-stable defect sets are precisely independent sets of \(G_L\). This proves the polynomial identity and \(A_L^{(1)}=P_L(1)\).

**2. Two-spin flips cannot lower energy from such a state.** For two distinct spins, their toggled triangles intersect in either zero or one vertex (since \(L\ge4\)). With no intersection, the symmetric-difference support has size six and an independent defect set occupies at most one site from each triangle: \(\Delta H\ge J(6-2\cdot2)=2J\). With one common vertex, the four sites in the symmetric difference are the two nonshared sites of each original triangle. Each of those two pairs is adjacent in \(G_L\), so at most two of the four sites can be defects. Consequently \(\Delta H\ge J(4-2\cdot2)=0\). Every one-spin-stable configuration is therefore two-spin-stable, establishing equality of their counts.

**3. An interior five-by-five witness admits a lowering three-spin flip.** Inside a \(5\times5\) coordinate block, assign defects at \((1,2)\) and \((3,2)\) and nowhere else in that block. These defects are nonadjacent. Each of their six triangular neighbors lies within the block, so this prescription is a valid independent-set completion for **any** independent defect pattern outside the block. The three spins \((1,2),(2,2),(1,3)\) have toggling symmetric difference exactly
\[
 \{(1,2),(3,2),(1,4)\}.
\]
Exactly two of these three sites are defects. Flipping these spins simultaneously decreases energy by \(J\). Thus every global independent-set pattern realizing the block prescription fails three-spin stability. This witness can be translated to any nonoverlapping coordinate \(5\times5\) block.

**4. The rarity bound requires no independence approximation.** Partition a coordinate square into \(q=\lfloor L/5\rfloor^2\) pairwise disjoint nonwrapping \(5\times5\) blocks, leaving any unused strips unrestricted. Sample an independent set \(D\) uniformly from all \(P_L(1)\) choices. For each block, **conditionally on any prescribed independent pattern outside that block**, the witness completion from step 3 is admissible. At most \(2^{25}\) block assignments can be admissible, so the conditional chance of the exact witness prescription is at least \(2^{-25}\). This remains true when also conditioning on nonoccurrence of witnesses in earlier blocks: that event depends on coordinates outside the current block, so the estimate holds pointwise for each allowable exterior and survives averaging. Iterating,
\[
 \Pr(\text{no witness in any selected block})
 \le(1-2^{-25})^q\le e^{-q/2^{25}}.
\]
For dyadic \(L\ge8\), \(\lfloor L/5\rfloor\ge L/10\), hence \(q\ge L^2/100\). A three-spin-stable state has no witnesses, and the probability above equals the ratio of its count to the total number of one-spin minima, proving the advertised bound. Baxter's hard-hexagon result establishes the existence of the triangular hard-core thermodynamic pressure, yielding the stated entropy-limsup consequence by taking logarithms and dividing by \(L^2\).

## Verification
A standalone `verify.py` (Python 3 standard library) exhaustively enumerates all \(2^{16}=65,536\) spins on the \(4\times4\) torus, applies **physical** spin-flip energy tests, constructs the independent-set graph separately, and confirms the exact polynomial
\[
 P_4(z)=1+16z+72z^2+96z^3+16z^4,
 \qquad A_4^{(1)}=A_4^{(2)}=201.
\]
It checks the explicit lowering three-flip witness for \(L=4,8\), geometric conditions in the \(5\times5\) block for \(L=8,16\), and \(120\) seeded spin-to-defect Frobenius tests for dyadic sizes \(4,8,16\). Run `python3 verify.py`. The finite enumeration is not a proof for all sizes: steps 1–4 provide that proof and the exponential bound.

## Relationship to prior work
Newman and Moore introduced the triangular plaquette model and its dyadic spin–defect correspondence, and discussed glassy low-temperature dynamics and isolated-defect metastability. The defect bijection and single-flip local rule are therefore **prior knowledge**, not claimed as discoveries here. Franz, Gradenigo and Spigler likewise discuss the basic three-plaquette flip rule. Baxter solved the hard-hexagon model and its thermodynamic pressure; that exact solution is used only as background to identify the one-spin entropy. Turner, Jack and Garrahan examine coupled-plaquette and activity-biased glass transitions. The claim being advanced here is instead the **exact two-flip robustness together with a uniform exponential deficit after allowing simultaneous three-spin flips**, proved by the compatible local witness and conditional counting. None of the inspected material established this specific implication. Overlap with specialized unindexed results cannot be ruled out.

## Limitations
This is an exact finite-size theorem for positive coupling and dyadic tori, not a dynamical distribution of trapped states under a chosen quench. Three-spin stability allows neutral flips and may exclude more configurations than our bound detects. The exponential deficit constant is intentionally coarse and is **not** a measured entropy difference, a sharp exponent, or an exact three-spin pressure; existence of the three-spin entropy limit is not asserted. The original 1980 hard-hexagon paper was not fully accessible in the consulted sources; its established pressure is standard prior mathematics. Independent external validation has not been performed.

## References
1. M. E. J. Newman and C. Moore, “Glassy dynamics and aging in an exactly solvable spin model,” arXiv:cond-mat/9707273 (first posted 1997-07-25), https://arxiv.org/abs/cond-mat/9707273 .
2. R. J. Baxter, “Hard hexagons: exact solution,” *J. Phys. A* **13** (1980), L61–L70, https://doi.org/10.1088/0305-4470/13/3/007 .
3. M. C. Turner, R. L. Jack, and J. P. Garrahan, “Overlap and activity glass transitions in plaquette spin models with hierarchical dynamics,” arXiv:1504.05076, https://arxiv.org/abs/1504.05076 .
4. S. Franz, G. Gradenigo, and L. Spigler, “The Random-Diluted Triangular Plaquette Model,” arXiv:1507.05072, https://arxiv.org/abs/1507.05072 .
5. K. Sfairopoulos et al., “Boundary conditions dependence of the phase transition in the quantum Newman–Moore model,” arXiv:2301.02826, https://arxiv.org/abs/2301.02826 .
