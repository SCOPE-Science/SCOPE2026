# Independent mathematical audit

## correctness

PASS

On the simple cubic prism, a recoloring changes the energy in units of J by the difference of two neighbor-color multiplicities. Checking the middle rung of a compatible pair transition tests exactly this condition. The trace fixes the column labels, checks each rung once and counts each transverse and horizontal edge once even for n=3. Independent sparse integer construction reproduced all three characteristic polynomials and nontrivial SCC sizes 48,3,3, and confirmed length-4 and length-5 returns in the 48-state SCC. The stated strict Rouché bounds check exactly, so the only root outside radius 3 is simple and real in (3,4); the smaller components cannot contain it (row sums at most 3). The proper-rung eigenvalues give the stated positive ground count. For strict proper colorings, at each rung the missing third color must appear in both rows among the two neighboring rungs. A swapped rung provides it in neither row; the two cyclically color-shifted rungs provide it in opposite rows. The neighbors must therefore be opposite cyclic shifts, forcing a constant shift around the ring and giving 6 times 2 solutions precisely when 3 divides n. Weighting each transition by z to its edge contribution gives the energy enumerator. The positive-energy edge in the primitive block makes the Perron derivative strictly positive; the simple eigenvalue and spectral separation control the remaining trace uniformly near t=0, yielding linear mean and O(n) variance, hence the claimed probability limit for the uniform ensemble, not a quench distribution. The independent calculation gave alpha 3.6730996940923, entropy per spin 0.65051795444237, energy/J per rung 0.21744173751868. Edge-based enumeration for n=3,4,5 gave weak counts 36,294,660 and summed weak energies 36,360,930; these are cross-checks, not the all-n proof.

## originality

PASS

The supported distinct claim is the exact weak-minima census and entropy, and the positive typical excess energy on the labeled ternary antiferromagnetic prism. The proper-coloring formula is already covered by the cyclic-ladder chromatic polynomial, and the strict proper constraint is the classical fall-coloring condition; neither is credited as the novel phenomenon. Closest indexed local-stability transfers and prior thermodynamic or dynamical results count different ensembles or graphs.

## value

PASS

This is an exact solvable local-optimality ensemble on a natural bounded-width graph, rather than a tabulation of tiny sizes. The entropy distinguishes it from the classical proper-coloring ensemble; the energy law proves an extensive excess even though the ground energy is zero. The energy statement is about uniformly weighted weak minima, not geometric frustration of the ground state or quench behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
