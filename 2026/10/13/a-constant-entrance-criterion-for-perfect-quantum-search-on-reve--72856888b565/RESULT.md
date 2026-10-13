# A constant-entrance criterion for perfect quantum search on reversible Markov chains

## Finding
For a finite irreducible reversible Markov chain, exactly successful continuous-time marked-state search driven by the reversible random-walk Laplacian is characterized by **constant probability of entering the marked state from any other state**. More precisely, for a marked state \(w\), such success is possible at some positive hopping coefficient and finite time if and only if
\[
P_{uw}=\frac{\pi_w(1-P_{ww})}{1-\pi_w}\quad\text{for every }u\ne w.
\]
When the condition holds, the unique successful hopping coefficient is
\[
\gamma_* = \frac{1-\pi_w}{1-P_{ww}}.
\]
At this coefficient, the entire success-probability curve is
\[
p(t)=\pi_w+(1-\pi_w)\sin^2\bigl(\sqrt{\pi_w}\,t\bigr),
\]
and every nonnegative perfect-search time is \(t_j=(j+\tfrac12)\pi/\sqrt{\pi_w}\), for integers \(j\ge0\). The result allows arbitrary reversible nonnegative transition weights, including self-loops.

## Assumptions and scope
Let \(V\) be any finite state set of size at least two. Let \(P=(P_{uv})\) be an irreducible, row-stochastic, reversible transition matrix with strictly positive stationary probability distribution \(\pi\). Thus \(\pi_uP_{uv}=\pi_vP_{vu}\) for all states. Work in the complex Hilbert space \(\mathcal H=\ell^2(V,\pi)\), with \(\langle f,g\rangle_\pi=\sum_u\pi_u\overline{f_u}g_u\). The constant initial state \(s\equiv1\) is normalized. For the designated marked state \(w\), the unit localized state is \(e=\mathbf1_{\{w\}}/\sqrt{\pi_w}\), and \(a=\sqrt{\pi_w}\in(0,1)\). Define the self-adjoint random-walk Laplacian \(\Delta=I-P\), hopping coefficient \(\gamma>0\), and rank-one marked-state Hamiltonian \(H_\gamma=\gamma\Delta-|e\rangle\langle e|\). Success is the exact equation \(\bigl|\langle e,e^{-itH_\gamma}s\rangle\bigr|^2=1\) at some finite \(t>0\).

The entrance condition is equivalently \(P_{wu}=\pi_u(1-P_{ww})/(1-\pi_w)\) for every \(u\ne w\), by detailed balance. Thus conditional on leaving \(w\), the chain chooses its next state according to the stationary distribution conditioned on the complement. In particular, every state has a strictly positive transition to \(w\).

## Proof
Write \(r=P_{ww}<1\), since irreducibility and at least two states prohibit the marked state being absorbing. Reversibility makes \(\Delta\) self-adjoint; stochasticity gives \(\Delta s=0\), and \(\langle s,e\rangle=a\). Hence \(H_\gamma s=-a e\).

Suppose perfect success occurs: \(e^{-itH_\gamma}s=z e\) with \(|z|=1\). The propagator commutes with \(H_\gamma\), so the moments of the two unit states agree. Their first moments are \(-a^2\) and \(\gamma(1-r)-1\), respectively. Equality forces
\[
\gamma=\frac{1-a^2}{1-r}.
\]
The second moments equal the squared norms of the corresponding Hamiltonian images. The initial-state value is \(a^2\), and the marked-state value is \(\gamma^2\|\Delta e\|^2-2\gamma(1-r)+1\). Inserting the forced hopping coefficient yields
\[
\|\Delta e\|^2=\frac{(1-r)^2}{1-a^2}.
\]
But \(\Delta e\perp s\), and \(\langle e-a s,\Delta e\rangle=\langle e,\Delta e\rangle=1-r\). Cauchy--Schwarz gives
\[
1-r\le\sqrt{1-a^2}\,\|\Delta e\|.
\]
The second-moment equality makes this inequality sharp. Its equality case therefore yields
\[
\Delta e=\kappa(e-a s),\qquad\kappa=\frac{1-r}{1-a^2}>0.
\]
For each \(u\ne w\), the \(u\)-coordinate of the left side is \(-P_{uw}/a\); the right side is \(-\kappa a\). Thus \(P_{uw}=\kappa\pi_w\), exactly the stated constant-entrance requirement. This establishes necessity, including uniqueness of the hopping coefficient.

Conversely, assume the constant-entrance condition. Comparing coordinates at \(u\ne w\) gives \((\Delta e)_u=-\kappa a\), and at \(w\) gives \((\Delta e)_w=(1-r)/a=\kappa(1-a^2)/a\). Therefore \(\Delta e=\kappa(e-a s)\). At \(\gamma_*=1/\kappa\) one has
\[
H_{\gamma_*}s=-a e,\qquad H_{\gamma_*}e=-a s.
\]
The span of \(s,e\) is invariant and \(H_{\gamma_*}^2s=a^2s\). Consequently
\[
e^{-itH_{\gamma_*}}s=\cos(at)s+i\sin(at)e,
\]
so \(\langle e,e^{-itH_{\gamma_*}}s\rangle=a\cos(at)+i\sin(at)\). The squared magnitude equals \(a^2+(1-a^2)\sin^2(at)\) and is one precisely when \(at=(j+\tfrac12)\pi\) for some integer \(j\ge0\). This proves sufficiency and the complete set of times.

## Verification
A standalone Python 3 standard-library checker in `verify.py` uses exact rational arithmetic on connected conductance networks with two to four states, including loops. It independently checks the equality of first/second Hamiltonian moments against the constant-entrance criterion and, whenever the condition is true, all coordinates of the invariant-subspace identity. It also checks two explicit weighted examples. Invocation: `python3 verify.py`. The expected output is `VERIFY_OK exact_markov_moments_checks=41592 condition_true=870 weighted_cone=true triangle_balance=true`. This finite reproducibility check is not used as proof of the unrestricted theorem; the analytic moment argument above is the proof.

A concrete weighted example demonstrates the new freedom beyond unweighted graphs. Consider the symmetric nonnegative conductance matrix
\[
C=\begin{pmatrix}0&1&2&1\\1&0&1&0\\2&1&0&1\\1&0&1&0\end{pmatrix},\qquad P_{uv}=\frac{C_{uv}}{\sum_xC_{ux}},\qquad w=0.
\]
The graph is a cone over a three-vertex path, so its unweighted base is not regular. Nevertheless \(\pi_w=1/3\) and all three outside entrance probabilities are exactly \(1/2\). Thus weighted perfect search occurs at \(\gamma_*=2/3\) and first success time \(\pi\sqrt3/2\). Conversely, unequal marked-edge conductances can prevent perfect search even on a triangular graph.

## Relationship to prior work
Mograby, Balu, Okoudjou and Teplyaev (2022) formulate quantitative Grover/continuous-time search using weighted reversible graph Laplacians and derive exact information for the complete graph. Their paper supplies the operator setting but not the constant-entrance necessary-and-sufficient classification for arbitrary reversible chains.

Ide and Narimatsu (2022) study continuous-time quantum search through equitable quotient graphs and perfect state transfer, with different initial-state and adjacency-operator assumptions; those sufficiency conditions do not imply this all-weighted-chain criterion. Chakraborty, Novo and Roland (2020) give general asymptotic conditions for optimal spatial search, not an exact finite-time probability-one classification. Results for unweighted cones with regular complements form a proper special case of the present theorem: the weighted path-base example above attains perfect search despite the nonregular complement.

## Limitations
The result is for a single marked state, a finite irreducible reversible chain, the specified rank-one oracle and stationary initial vector. It does not apply without modification to irreversible walks, nonstationary initial states, multiple marked states, other Hamiltonian normalizations, or approximate/asymptotic search. It identifies exact attainment, not a stability or near-perfect bound. Any earlier equivalent theorem under alternate language for reversible chains remains a literature-indexing risk. No independent validation is asserted.

## References
1. D. Mograby, R. Balu, K. A. Okoudjou and A. Teplyaev, *Quantitative approach to Grover's quantum walk on graphs* (first publicly posted 2022-07-04), arXiv:2207.01686v1; especially weighted-chain definitions, complete-graph example and applications.
2. Y. Ide and T. Narimatsu, *A Note on Quantum Search Algorithms on Graphs with Equitable Partitions* (2022), arXiv:2209.07688v1; especially Theorem 3.1.
3. S. Chakraborty, L. Novo and J. Roland, *Optimality of spatial search via continuous-time quantum walks* (2020), arXiv:2004.12686v1; asymptotic spectral approach.
4. S. Chakraborty, L. Novo, A. Ambainis and Y. Omar, *Spatial search by quantum walk is optimal for almost all graphs* (2018), arXiv:1807.05957; comparison with modified search settings.
