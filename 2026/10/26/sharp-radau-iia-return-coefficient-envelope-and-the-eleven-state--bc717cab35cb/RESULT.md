# Sharp Radau IIA return-coefficient envelope and the eleven-state boundary

## Finding
Let \(Q\) be the generator of a finite irreducible reversible continuous-time Markov chain with stationary probabilities \(\pi_i>0\), and let the completed two-stage, third-order Radau IIA step be
\[
T(h)=(6I+2hQ)(6I-4hQ+h^2Q^2)^{-1},\qquad h\ge0.
\]
Put \(m=(5-3\sqrt3)/2\). Every diagonal entry satisfies the **sharp universal bound**
\[
\boxed{T(h)_{ii}\ge\pi_i+(1-\pi_i)m.}
\]
For every prescribed strictly positive probability vector \(\pi\) and every \(h>0\), a reversible generator attains equality simultaneously at every state. Equality at a fixed state \(i\) holds precisely when, for \(c=(3+3\sqrt3)/h\), all outgoing rates from \(i\) satisfy \(q_{ij}=c\pi_j\) for \(j\ne i\) (the rates elsewhere may be arbitrary subject to irreducibility and reversibility). The sharp stationary-mass boundary for a nonnegative completed *diagonal* coefficient across every reversible generator is
\[
\boxed{\pi_i\ge(2-\sqrt3)/3.}
\]
More precisely, above this boundary every such coefficient is strictly positive for all \(h\ge0\); below it some reversible generator has a negative diagonal coefficient at a positive step.

For symmetric diffusion on an unweighted connected graph, \(\pi_i=1/n\). Hence **all diagonal coefficients stay strictly positive at every step on every connected graph of at most eleven vertices**, whereas for each \(n\ge12\) there is an unweighted connected graph with a negative diagonal coefficient. In fact, if a graph has \(n\ge12\) vertices and a vertex adjacent by unit-weight edges to every other vertex, then its hub diagonal is negative at the single fixed step \(h=3/4\), regardless of edges among the other vertices. A twelve-vertex star (or complete graph) gives the exact value \(T(3/4)_{ii}=-1/164\) at such a hub.

## Assumptions and scope
Use the *row-generator convention*: \(q_{ij}\ge0\) for distinct \(i,j\), \(\sum_jq_{ij}=0\), \(\pi_iq_{ij}=\pi_jq_{ji}\), and \(\sum_i\pi_i=1\). Irreducibility implies a simple zero eigenvalue. The generator acts on functions in the Hilbert space \(\ell^2(\pi)\). The theorem controls diagonal return coefficients, not the full matrix's entrywise positivity, nor internal Runge–Kutta stages. No restriction is imposed on positive edge rates or state count \(n\ge2\). In the graph corollary \(Q=-L\), with \(L\) the ordinary combinatorial Laplacian and uniform stationary probabilities.

## Proof
1. **Scalar minimum.** For a nonnegative scalar decay parameter \(x\), the stability factor is
\[
r(x)=\frac{6-2x}{x^2+4x+6},\qquad
r'(x)=\frac{2(x^2-6x-18)}{(x^2+4x+6)^2}.
\]
The denominator is strictly positive for \(x\ge0\). The unique positive critical point \(x_*=3+3\sqrt3\) is the global minimum, because the derivative changes from negative to positive and \(r(x)\to0\) from below. Direct substitution gives \(r(x_*)=m=(5-3\sqrt3)/2\). In particular \(-1<r(x)\le1\) for all \(x\ge0\), so the method is spectrally nonexpansive in \(\ell^2(\pi)\) at every step; spectral nonexpansiveness does *not* imply a nonnegative step matrix.

2. **Spectral mass at a state.** Reversibility makes \(Q\) self-adjoint in \(\ell^2(\pi)\). Write its orthogonal spectral projections as \(E_0=\mathbf1\pi^\mathsf T\) and \(E_{\lambda}\), where \(Q E_{\lambda}=-\lambda E_{\lambda}\) with \(\lambda>0\). Then
\[
T(h)_{ii}=\pi_i+\sum_{\lambda>0}r(h\lambda)(E_\lambda)_{ii}.
\]
Each \((E_\lambda)_{ii}\) is nonnegative: it equals \(\|E_\lambda e_i\|_\pi^2/\pi_i\). Their sum is \(1-\pi_i\), since \(E_0\) has diagonal \(\pi_i\). Therefore \(r(h\lambda)\ge m\) proves the claimed bound.

3. **Sharpness and equality cases.** Fix \(h>0\) and set \(c=x_*/h\). The reset generator \(Q=c(\mathbf1\pi^\mathsf T-I)\) has off-diagonal rates \(q_{ij}=c\pi_j>0\), stationary distribution \(\pi\), and spectrum \(\{0,-c\}\). It satisfies
\[
T(h)=\mathbf1\pi^\mathsf T+m(I-\mathbf1\pi^\mathsf T),
\]
so every diagonal entry attains the lower bound. Conversely, scalar strictness away from \(x_*\) means equality at \(i\) requires \(e_i-\pi_i\mathbf1\) to lie entirely in the \(-c\) eigenspace. For any \(j\ne i\), its \(j\)th coordinate in \(Q(e_i-\pi_i\mathbf1)=-c(e_i-\pi_i\mathbf1)\) gives \(q_{ji}=c\pi_i\); detailed balance yields \(q_{ij}=c\pi_j\). The \(i\)th coordinate then follows from the zero row sum. This condition is also sufficient. Rates not incident to \(i\) need not be equal.

4. **Sharp mass and graph-size boundaries.** The lower bound is nonnegative exactly when
\[
\pi_i\ge\frac{-m}{1-m}=\frac{2-\sqrt3}{3}.
\]
When the inequality fails, the reset generator gives a strictly negative entry at \(h=x_*/c\). For an unweighted connected graph, \(\pi_i=1/n\), and \(3/(2-\sqrt3)=6+3\sqrt3\) lies strictly between \(11\) and \(12\). Thus all diagonal coefficients are positive for \(n\le11\), and the result is sharp at \(n=12\).

5. **A topology-independent cone witness.** For any simple unweighted graph having a universal vertex \(i\), one has \(Q(e_i-\mathbf1/n)=-n(e_i-\mathbf1/n)\) whether or not other vertices are joined. Therefore
\[
T(h)_{ii}=\frac{1+(n-1)r(nh)}n
=\frac{(nh)^2+(6-2n)nh+6n}{n((nh)^2+4nh+6)}.
\]
For each \(n\ge12\), the diagonal is negative precisely when \(nh\) lies strictly between the two positive roots
\[
n-3-\sqrt{n^2-12n+9},\qquad n-3+\sqrt{n^2-12n+9}.
\]
At \(h=3/4\), its numerator is \(n(168-15n)/16<0\) for every integer \(n\ge12\). For \(n=12\) the exact diagonal is \(-1/164\). This proves all claimed sharpness statements.

## Verification
The accompanying standalone `verify.py` checks the scalar derivative, exact minimum, mass threshold, discriminants, cone roots, and finite-dimensional rational matrix identities. It constructs exact reversible generators with nonuniform stationary distributions; it independently evaluates their completed Radau step by a rational matrix inverse, verifies detailed balance and row sums, tests the diagonal bound, and replays four twelve-vertex cone matrices including the star and complete graph. Run `python verify.py` with SymPy available. The analytical spectral argument, not these finite examples, proves the statements for arbitrary dimension and arbitrary positive real rates.

## Relationship to prior work
The foundational study by Gottlieb, Shu and Tadmor (2001) analyzes the strong-stability-preserving limitations of high-order time stepping; it does not provide a stationary-mass-dependent sharp *diagonal* envelope for the Radau IIA map or an eleven-state threshold. Blanes, Iserles and Macnamara (2022) study positive graph-Laplacian flows and construct specialized positivity-preserving integrators; they do not give this return-coefficient extremal characterization. Specialized graph-family studies of the same Radau stability function exhibit negative off-diagonal or diagonal entries but do not yield the universal envelope, equality conditions or minimal vertex count. In particular, earlier off-diagonal distance-five sign losses do not imply a failure of a diagonal coefficient.

## Limitations
The theorem says nothing about nonnegative off-diagonal entries: a step may have positive diagonals and negative entries elsewhere. The exact stationary-mass criterion concerns robustness over *all* reversible generators with the prescribed stationary vector, not unconditional diagonal positivity for each individual generator below the boundary. Reversibility is essential to the orthogonal spectral-measure proof. Claims about nonreversible chains, intermediate Runge–Kutta stages, nonlinear problems, or multiple-step compositions are not made. Independent mathematical validation has not been performed.

## References
1. S. Gottlieb, C.-W. Shu and E. Tadmor, *Strong Stability-Preserving High-Order Time Discretization Methods*, SIAM Review **43** (2001), 89–112. DOI: `10.1137/S003614450036757X`. Author-hosted text: `https://math.umd.edu/~tadmor/pub/linear-stability/Gottlieb-Shu-Tadmor.SIREV-01.pdf` (paper states electronic publication 2001-02-02).
2. S. Blanes, A. Iserles and S. Macnamara, *Positivity-preserving methods for ordinary differential equations*, ESAIM: M2AN **56** (2022), 1843–1870. DOI: `10.1051/m2an/2022042`. Author-hosted PDF: `https://personales.upv.es/serblaza/2022_M2AN.pdf`.
