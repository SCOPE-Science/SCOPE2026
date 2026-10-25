# Unbounded entropy under finite periodic-orbit agreement near the full tent map

## Finding
Let \(T:[0,1]\to[0,1]\) be the full tent map, \(T(x)=2\min\{x,1-x\}\). Given any integer \(H\ge1\), any \(\varepsilon>0\), and any \(R>0\), there is a continuous surjective topologically exact piecewise-linear map \(F:[0,1]\to[0,1]\), uniformly expanding on each of finitely many monotonicity intervals, for which
\[
\|F-T\|_\infty<\varepsilon,\qquad h_{\mathrm{top}}(F)>R.
\]
For every \(1\le n\le H\), the collections of least-period-\(n\) orbits of \(F\) and \(T\), considered as unlabelled subsets of \([0,1]\), coincide **exactly**. In fact, their maps agree at every point belonging to one of these orbits. This is stronger than agreement of periodic-point counts or period lengths.

## Assumptions and scope
Choose an integer \(P\ge H+1\) so large that \(2^{1-2P}<\varepsilon\). Write \(Q=2^P\) and put
\[
a=\frac{2Q-2}{Q^2},\qquad b=\frac{2Q-1}{Q^2},\qquad I=[a,b],\qquad \ell=b-a=Q^{-2}.
\]
Choose an odd integer \(M\ge3\) with \(\log M>PR\). Let \(I_j=[a+j\ell/M,a+(j+1)\ell/M]\) for \(0\le j<M\). Set \(F=T\) outside \(I\), and define \(F\) on \(I\) by linear interpolation of the values
\[
F(a+j\ell/M)=\begin{cases}T(a),&j\text{ even},\\T(b),&j\text{ odd},\end{cases}\qquad 0\le j\le M.
\]
The oddness of \(M\) gives \(F(b)=T(b)\), so the definition is continuous at both endpoints. All subdivisions and breakpoint values are rational, and the formula makes \(F\) unambiguous. As \(I\subset(0,1/2)\), each modified lap has slope of magnitude \(2M\); all other slopes have magnitude \(2\). In particular \(F\) is uniformly piecewise expanding.

## Proof
**1. Return-free surgery region.** The tent map acts as doubling on the first \(P-2\) subsequent images of \(I\), and on the next image its right branch applies. Direct substitution gives
\[
T^j(I)=[2^ja,2^jb]\quad(1\le j\le P-1),\qquad T^P(I)=[1/Q,2/Q].
\]
Here \(T^{P-1}(I)=[1-1/Q,1-1/(2Q)]\subset[1/2,1]\). Since \(2a>b\), every \(T^j(I)\), \(1\le j<P\), lies strictly to the right of \(I\). Moreover \(1/Q<a<b<2/Q\), so the first return image \(T^P(I)\) strictly contains \(I\).

By construction \(F(I)=T(I)\); since all intermediate images avoid the modified interval, induction gives \(F^j(I)=T^j(I)\) for \(1\le j\le P\). Therefore \(F^n(x)\ne x\) and \(T^n(x)\ne x\) whenever \(x\in I\) and \(1\le n<P\).

**2. Complete agreement of all short periodic orbits.** A periodic orbit of either map with least period below \(P\) cannot intersect \(I\), by the preceding disjointness. Every point on such an orbit is therefore outside \(I\), where \(F=T\), so the other map has precisely the same pointwise orbit. This proves equality of the collections of embedded, unlabelled periodic orbits for all periods at most \(H\). No labeling or orbit-counting reduction is needed.

**3. Explicit high-entropy horseshoe.** Each \(I_j\) maps homeomorphically under \(F\) onto \(T(I)\). The next \(P-1\) iterates follow the original tent map and are monotone on \(T(I)\), whence \(F^P\) maps each \(I_j\) homeomorphically onto \([1/Q,2/Q]\). Because that interval strictly contains \(I\), there is a compact subinterval \(K_j\) strictly inside \(I_j\) with \(F^P(K_j)=I\). The intervals \(K_0,\ldots,K_{M-1}\) are pairwise disjoint. The standard full-branch horseshoe argument gives an invariant Cantor set for \(F^P\) with a full \(M\)-symbol shift factor (indeed, a conjugacy from inverse branches). Therefore
\[
h_{\mathrm{top}}(F)\ge\frac{\log M}{P}>R.
\]

**4. Surjectivity and topological exactness.** Use the dyadic Markov partition of \(T\) into the \(Q^2\) intervals \(J_t=[t/Q^2,(t+1)/Q^2]\). Every image of a partition cell is a union of full cells. On each cell, \(T^{2P}\) maps homeomorphically onto \([0,1]\), so its finite Markov adjacency matrix \(A\) has \(A^{2P}\) strictly positive. The surgery replaces exactly the cell \(J_{2Q-2}=I\) by the \(M\) cells \(I_j\). Each new cell has image \(T(I)\), while every unmodified cell retains its original image. Thus the new adjacency matrix \(B\) is obtained by cloning the state corresponding to \(I\): if \(\pi\) sends each new state to its parent old state, then \(B_{uv}=A_{\pi(u),\pi(v)}\). Consequently every directed path in the old graph lifts between *any* prescribed new states, and \(B^{2P}\) is strictly positive.

On each monotone Markov branch \(|F'|\ge2\); every iterated Markov cylinder of depth \(r\) has length at most \(2^{-r}\). Any nonempty open interval contains an entire sufficiently deep cylinder, whose image is one whole partition cell. After a further \(2P\) iterates its image is all of \([0,1]\), since \(B^{2P}>0\). Therefore \(F\) is topologically exact, in particular mixing and surjective.

**5. Uniform proximity.** Outside \(I\) the maps agree. On \(I\), both \(F(x)\) and \(T(x)\) lie in \(T(I)\), an interval of length \(2\ell\). Hence
\[
\|F-T\|_\infty\le2\ell=2^{1-2P}<\varepsilon.
\]
All required quantifiers hold independently: increasing \(P\) makes the perturbation arbitrarily small and preserves the observed horizon, while increasing odd \(M\) makes the entropy arbitrarily large. This completes the proof.

## Verification
The accompanying Python checker uses exact rational arithmetic to verify the return-free geometry, preservation of every period up to \(P-1\) among tent-map periodic points, the precise cloned Markov adjacency, and strict positivity of the \(2P\)-step adjacency matrix for \(H\in\{1,2,3,4\}\) and \(M\in\{3,5,9\}\), all twelve pairs. Its terminal result is `CHECKS_PASS`. These finite calculations supplement the uniform argument above; they are not an enumeration of all parameters or a substitute for the infinite proof. Run `python period_spectrum_checker.py` with Python 3.

## Relationship to prior work
Fuhrmann, Gröger and Passeggi (2026), Theorems A–C and Corollary 4.13, prove that the **complete** collection of embedded periodic orbits determines mixing interval maps and, for general compact intervals, equal complete collections force equal entropy. Their Section 5 supplies nonmixing examples with matching complete spectra. The present theorem treats the different finite-horizon problem: it shows no finite prefix of that same *spatial orbit data* bounds entropy, even inside topologically exact expanding maps arbitrarily close to one fixed map. No contradiction arises because the added horseshoes necessarily introduce longer orbits.

Ruette (2019), especially Section 3, realizes a wide range of entropies in mixing interval maps having fixed Sharkovskii period type. Period type records possible *period lengths* rather than the actual positions of **every** orbit of each prescribed short period. The above simultaneous equality of short embedded orbit sets and uniform-distance bound are not consequences of fixed type alone.

## Limitations
The expanding slopes and number of laps are not bounded uniformly as \(R\to\infty\); no uniform Lipschitz bound, bounded-lap theorem, or smooth fixed-criticality extension is asserted. The explicit lower entropy bound need not be an equality. This establishes non-identifiability from **finite** periodic-orbit data, not failure of the full-spectrum rigidity theorem. No independent mathematical audit or exhaustive priority certification has been carried out.

## References
Fuhrmann, Gabriel; Gröger, Maik; Passeggi, Alejandro. *Period spectrum and rigidity of interval maps*, arXiv:2610.07435v1 (first publicly posted October 5, 2026). https://arxiv.org/abs/2610.07435

Ruette, Sylvie. *Interval maps of given topological entropy and Sharkovskii's type*, arXiv:1906.03649v1 (2019). https://arxiv.org/html/1906.03649v1
