# A uniform all-temperature Lee–Yang root-locus transition between \(K_{2,3}\) and \(K_{2,4}\)

## Finding

Consider the antiferromagnetic Ising model on the complete bipartite graph \(K_{2,m}\), with two hubs, \(m\) common neighbors, uniform edge crossing weight \(q>1\), and complex uniform-field fugacity \(z\). The normalized partition polynomial is
\[
Z_{2,m}(z;q)=\sum_{S\subseteq V(K_{2,m})}z^{|S|}q^{|\delta(S)|}.
\]

**Theorem.** For every real \(q>1\), all five zeros of \(Z_{2,3}(\cdot;q)\) are simple and negative real, comprising \(-1\) and two reciprocal pairs. For the same entire range of couplings, the six zeros of \(Z_{2,4}(\cdot;q)\) are simple, comprising exactly four negative real zeros in two reciprocal pairs and exactly two nonreal zeros on the unit circle, which are complex conjugates. Thus adding the fourth common neighbor causes a nonreal circular Lee–Yang pair for every strictly antiferromagnetic coupling, not merely in a weak- or strong-coupling limit.

## Assumptions and scope

Here \(K_{2,m}\) is the simple unweighted complete bipartite graph with two vertices in one part and \(m\) in the other; each of its \(2m\) edges carries the same real crossing weight \(q>1\). The polynomial weights each spin subset \(S\) by \(z^{|S|}q^{|\delta(S)|}\), where \(\delta(S)\) denotes edges with exactly one endpoint in \(S\). For the conventional physical Hamiltonian with common exchange coupling \(J<0\), inverse temperature \(\beta>0\), and external field \(h\), these parameters are \(q=e^{-2\beta J}>1\) and \(z=e^{-2\beta h}\); the omitted Boltzmann prefactor is nonzero and has no effect on zeros. The result classifies precisely \(m=3,4\) at all \(q>1\); it makes no claim for arbitrary \(m\) or heterogeneous edge strengths.

## Proof

Fix the spin states of the two hubs. When both are outside \(S\), each neighbor separately contributes \(1+q^2z\). When both belong to \(S\), the hub fugacity contributes \(z^2\) and each neighbor contributes \(q^2+z\). In either mixed-hub state, each of the \(m\) neighbors creates exactly one crossing edge, giving \(q^m z(1+z)^m\). Consequently, for every positive integer \(m\),
\[
Z_{2,m}(z;q)=(1+q^2z)^m+2q^m z(1+z)^m+z^2(q^2+z)^m.
\]
This is a monic degree-\(m+2\) polynomial with constant term \(1\); spin complementation shows \(z^{m+2}Z_{2,m}(z^{-1};q)=Z_{2,m}(z;q)\). In particular, zero is not a root.

Write \(y=z+z^{-1}\). For \(m=3\), direct polynomial expansion and reciprocal pairing give
\[
Z_{2,3}(z;q)=(z+1)z^2F_3(y),\quad
F_3(y)=y^2+(2q^3+3q^2-1)y+q^6+3q^4+4q^3-3q^2-1.
\]
The exact evaluations are
\[
F_3(-2)=(q-1)^2(q+1)^2(q^2+5)>0,
\]
\[
F_3(-q^3-q^2)=-(q-1)^2(3q^3+5q^2+2q+1)<0.
\]
Since \(-q^3-q^2<-2\), continuity gives one real zero of \(F_3\) in \((-\infty,-q^3-q^2)\) and one in \((-q^3-q^2,-2)\). Degree two makes these all its zeros and ensures they are distinct. Each root \(y<-2\) yields two distinct negative real reciprocal solutions of \(z+z^{-1}=y\), neither equal to \(-1\). The additional factor \(z+1\) gives exactly one simple root at \(-1\), because \(F_3(-2)>0\). Thus all five zeros are simple and negative real.

For \(m=4\), reciprocal reduction gives
\[
Z_{2,4}(z;q)=z^3F_4(y),
\]
\[
F_4(y)=y^3+(2q^4+4q^2)y^2+(q^8+14q^4-3)y+8q^6+8q^4-8q^2.
\]
Set \(y_*=-q^4-q^2<-2\). Exact evaluation yields
\[
F_4(y_*)=q^2(q-1)^3(q+1)^3(4q^2+5)>0,
\]
\[
F_4(-2)=-2(q-1)^4(q+1)^4<0,
\]
\[
F_4(2)=2(q^8+4q^6+22q^4+4q^2+1)>0.
\]
As a monic cubic, \(F_4(y)\to-\infty\) for \(y\to-\infty\). The displayed alternating signs therefore give one distinct root in each of \((-\infty,y_*)\), \((y_*,-2)\), and \((-2,2)\). Since the degree is three, these are all roots and all simple. Each of the first two roots yields a pair of distinct negative real reciprocal roots of \(Z_{2,4}\). For the remaining \(y\in(-2,2)\), solving \(z^2-yz+1=0\) produces a distinct nonreal conjugate pair with \(|z|=1\). All six zeros are simple and accounted for. This proves the theorem for every \(q>1\).

## Verification

The supplied `verify.py` enumerates every spin assignment for both graphs (\(2^5+2^6=96\) configurations), reconstructs the complete partition polynomials exactly, and checks both reciprocal reductions and the five crucial sign evaluations symbolically over rational polynomial coefficients. It additionally isolates the reduced real roots at four rational values of \(q\), using exact rational interval isolation. The symbolic identities corroborate the all-coupling proof; finite sampling by itself is not the justification of the universal quantifier. Run with `python3 verify.py` in an environment containing SymPy.

## Relationship to prior work

Sedik, Bhat, Dhar, and Shastry study antiferromagnetic Yang–Lee root curves and high-temperature expansions for square-lattice and mean-field systems (arXiv:2309.14562). Peters and Regts prove degree-uniform zero-free sectors and sharp union-of-graphs coverage (arXiv:1810.01699), rather than the exact zero multiset of either fixed complete bipartite graph. Bencs, Buys, Guerini, and Peters analyze Cayley trees and bounded-degree families (arXiv:1907.07479); neither graph here is a tree. Bencs, Csikvári, and Regts prove real-rootedness on line graphs (arXiv:2012.00806), which does not imply the \(K_{2,3}\) result: both graphs here have an induced claw, whereas line graphs are claw-free. Lebowitz, Ruelle, and Speer establish special real-negative-zero conditions for models whose site participation and interactions meet their structural hypotheses (arXiv:1204.0558); those specific conditions do not directly yield this pair of complete bipartite classifications. The new statement is the exact coupling-uniform root-locus distinction between these two neighboring graphs, not a claim to the general methods or earlier zero-free regions.

## Limitations

The threshold compares only the natural consecutive cases \(m=3\) and \(m=4\), with uniform strictly antiferromagnetic coupling; it does not determine the count of circular zeros for \(m\ge5\), prove monotonicity across the family, or apply to arbitrary inhomogeneous couplings. At the excluded endpoint \(q=1\), the polynomial is \((1+z)^{m+2}\), so the simplicity conclusion fails. The work has received self-review only; no independent audit or external proof verification has been performed. An equivalent treatment hidden within a more general exact root-locus theorem remains a literature risk.

## References

1. M. Sedik, J. M. Bhat, A. Dhar, and B. S. Shastry, *Yang-Lee Zeros of Certain Antiferromagnetic Models*, arXiv:2309.14562v1 (2023), https://arxiv.org/abs/2309.14562.
2. H. Peters and G. Regts, *Location of zeros for the partition function of the Ising model on bounded degree graphs*, arXiv:1810.01699v1 (2018), https://arxiv.org/abs/1810.01699.
3. F. Bencs, P. Buys, L. Guerini, and H. Peters, *Lee-Yang zeros of the antiferromagnetic Ising Model*, arXiv:1907.07479v1 (2019), https://arxiv.org/abs/1907.07479.
4. F. Bencs, P. Csikvári, and G. Regts, *Some applications of Wagner's weighted subgraph counting polynomial*, arXiv:2012.00806v1 (2020), https://arxiv.org/abs/2012.00806.
5. J. L. Lebowitz, D. Ruelle, and E. R. Speer, *Location of the Lee–Yang zeros and absence of phase transitions in some Ising spin systems*, arXiv:1204.0558v1 (2012), https://arxiv.org/abs/1204.0558.
