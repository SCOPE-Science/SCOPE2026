# Mass-resolved primitive two-cycle law for cyclic parallel chip-firing

## Finding
For every integer \(n\ge3\), let \(C_n\) be the simple cycle with distinguishable vertices \(0,\ldots,n-1\), and let \(F\) be ordinary synchronous degree-threshold chip-firing. Define the **orbit-mass polynomial**
\[
P_n(z)=\sum_{\mathcal O:\,|\mathcal O|=2}z^{M(\mathcal O)},
\]
where the sum is over distinct primitive temporal two-cycle orbits, counted once each, and \(M(\mathcal O)\) is the conserved total number of chips. With
\[
r_\pm(z)=\frac{1+z\pm\sqrt{1+6z+z^2}}2,
\]
the exact polynomial identity is
\[
\boxed{P_n(z)=\frac{z^n}{2}\left(r_+(z)^n+r_-(z)^n+(-1)^n(1+z^n)\right).}
\]
The square roots cancel in the sum. In particular,
\[
P_n(1)=\frac{(1+\sqrt2)^n+(1-\sqrt2)^n+2(-1)^n}{2},
\]
and \(P_n(z)=z^{3n}P_n(z^{-1})\). Its nonzero coefficients lie at masses between \(n\) and \(2n\), with mass \(n\) or \(2n\) attainable exactly when \(n\) is even, in which case each boundary coefficient is one.

Choose one primitive two-cycle orbit uniformly from the \(P_n(1)\) orbits, and let \(X_n\) denote its conserved mass. Then
\[
\mathbb E X_n=\frac{3n}{2},\qquad
\frac{X_n-3n/2}{\sqrt{n\sqrt2/8}}\ \xrightarrow[n\to\infty]{\mathrm{law}}\ \mathcal N(0,1).
\]
The exact central expectation follows from complement symmetry; the Gaussian normalization is asymptotic.

## Assumptions and scope
Vertices of \(C_n\) have nonnegative integer chip holdings \(c_i\). At each discrete update, vertex \(i\) fires if and only if \(c_i\ge2\) and then sends one chip to each of its two neighbors, all in parallel. There are no sinks, sources, stochastic steps or chip inputs. A primitive two-cycle consists of two different chip vectors mapped to one another by \(F\). The starting index and site labels are fixed: cyclic spatial rotations and reflections are **not** identified. An orbit of length two is counted once, not once per time phase. The result concerns configurations periodic from the initial update, not attraction basins or total eventually period-two trajectories.

## Proof
**1. Alternating firing is necessary.** Write \(a_i(t)\in\{0,1\}\) for whether site \(i\) fires at time \(t\). The update is
\[
c_i(t+1)=c_i(t)-2a_i(t)+a_{i-1}(t)+a_{i+1}(t).
\]
If \(c(t+2)=c(t)\), summing the two updates shows the graph Laplacian annihilates the vector \(a(0)+a(1)\). Since the cycle is connected, that vector is constant. The constant is \(0,1\) or \(2\). Constants \(0\) and \(2\) force everyone to remain respectively inactive or active and give a fixed point. Therefore a primitive two-cycle has \(a_i(1)=1-a_i(0)\) at *every* site.

**2. Exact local chip choices.** Write \(a_i=a_i(0)\), and let \(f_i=a_{i-1}+a_{i+1}\). If \(a_i=1\), the conditions that \(i\) fire at time zero and not at time one become \(2\le c_i\le3-f_i\). If \(a_i=0\), the reverse conditions become \(2-f_i\le c_i\le1\). Both intervals consist of nonnegative integers whenever nonempty. For a given binary phase word, independent choices from these intervals exactly construct all distinct primitive two-cycle states with that phase word: after the second update the chip counts return automatically, and the firing states complement at the intermediate step.

For a site with three consecutive phases \(a,b,c\), define its weight as the sum of \(z^{c_i}\) over the allowed chip counts. In the order \(00,01,10,11\) for successive phase pairs, the weighted de Bruijn transfer matrix is
\[
T(z)=\begin{pmatrix}
0&z&0&0\\
0&0&z^2+z^3&z^2\\
z&1+z&0&0\\
0&0&z^2&0
\end{pmatrix}.
\]
Because a cyclic length-\(n\) phase word corresponds to a unique closed length-\(n\) walk of pair states, \(\operatorname{tr}(T(z)^n)\) enumerates all time-oriented primitive two-cycle states, weighted by total chips. Each temporal orbit has precisely two such states and constant mass, so
\[
P_n(z)=\tfrac12\operatorname{tr}(T(z)^n).
\]
There are no fixed-state contributions, since a fixed configuration cannot have complementary firing phases.

**3. Closed spectral evaluation.** Direct determinant expansion yields
\[
\det(\lambda I-T(z))=(\lambda+z)(\lambda+z^2)
\bigl(\lambda^2-(z+z^2)\lambda-z^3\bigr).
\]
The quadratic roots are \(z r_+(z)\) and \(z r_-(z)\). The trace-of-powers identity, valid also when eigenvalues repeat, gives the boxed orbit-mass identity. The involution \(c_i\mapsto3-c_i\) on primitive two-cycle states conjugates the update and maps mass \(M\) to \(3n-M\); hence reciprocity and the exact mean. The coefficient of \(z^n\), obtained by taking \(z\to0\), is \((1+(-1)^n)/2\). The coefficient of \(z^{2n}\) is identical by reciprocity. The lower bound \(M\ge n\) and upper bound \(M\le2n\) follow from the spectral expression (or by pairing each alternating phase site's contributions along the cycle); the polynomial formula directly shows vanishing outside this interval.

**4. Gaussian mass law.** Set \(\Lambda(z)=z r_+(z)\). In a complex neighborhood of \(z=1\), the other three eigenvalues \(z r_-(z),-z,-z^2\) have strictly smaller modulus than \(\Lambda(z)\). Hence the moment generating function \(P_n(e^t)/P_n(1)\) has, uniformly for \(t\) in a sufficiently small complex disk, logarithm
\[
\log\frac{P_n(e^t)}{P_n(1)}
=n\bigl[\log\Lambda(e^t)-\log\Lambda(1)\bigr]+O(\rho^n)
\]
for some \(0<\rho<1\). Direct differentiation gives first logarithmic derivative \(3/2\) and second \(\sqrt2/8>0\) at \(t=0\). Substituting \(t=iu/\sqrt{n\sqrt2/8}\), centering and using the characteristic-function continuity theorem yields the stated Gaussian limit. The exact expectation follows independently from reciprocity.

## Verification
The independent `VERIFY.py` enumerates all \(4^n\) configurations with site holdings in \(\{0,1,2,3\}\) on cycles \(3\le n\le9\), filters for genuine primitive two-cycles by two direct updates, counts masses with each temporal orbit divided by two, and compares to the exact closed quadratic-root polynomial evaluated via an integer recurrence. Its output `VERIFY_OUTPUT.txt` records \(349{,}504\) configurations examined and the terminal `EXACT_RING_CHIPFIRE_MASS_VERIFY_OK`. The infinite-family claim is proved algebraically above, not inferred from these finite checks. The restriction to at most three chips per vertex is exhaustive **for primitive two-cycle states** by the intervals in proof step 2, though not for arbitrary transient states.

## Relationship to prior work
Dall'Asta's January 12, 2006 preprint gives the one-dimensional fixed-energy sandpile rule, periodicity regimes, spatial blocks for period-two states, and a separate recurrence-type enumeration of periodic configurations at the *critical boundary energies*. It already determines the existence of the period-two phase and in particular the unique alternating orbit at either energy boundary on an even ring. These facts are not claimed as new. The present finding instead provides an explicit **single closed generating polynomial resolving every conserved mass** and a normal limit law for masses among initially period-two orbits. The critical-boundary coefficients agree with Dall'Asta. Jiang's parallel chip-firing work provides general periodic-position structural lemmas and results about allowed periods for multipartite graphs, not this mass-refined cycle enumerator. Previously available path and open-ladder enumerations concern different underlying graphs and do not imply the cyclic mass polynomial by specialization, because closing an edge changes every local firing threshold at its endpoints.

## Limitations
The result counts initially primitive period-two **temporal orbits**, not all periodic states of different least periods and not the basin sizes of all orbits. It does not claim a distribution of transient lengths. The main 2006 source already provides a detailed symbolic description of two-cycle configurations; consequently the new statement should be regarded as a nontrivial explicit quantitative refinement of existing qualitative/block structure, not a new classification of dynamical modes. Originality could be affected by an uncatalogued mass-resolved enumeration or a readily equivalent earlier generating function. No independent external review has been undertaken.

## References
1. Luca Dall'Asta, *Exact Solution of the One-Dimensional Deterministic Fixed-Energy Sandpile*, arXiv:cond-mat/0601267v1, first publicly posted January 12, 2006; later Phys. Rev. Lett. **96**, 058003 (2006). https://arxiv.org/pdf/cond-mat/0601267
2. Tian-Yi Jiang, *On the Period Lengths of the Parallel Chip-Firing Game*, arXiv:1003.0943 (2010; later revision 2013). https://arxiv.org/pdf/1003.0943
3. Mario Casartelli, Luca Dall'Asta, Alessandro Vezzani, Pierpaolo Vivo, *Dynamical Invariants in the Deterministic Fixed-Energy Sandpile*, arXiv:cond-mat/0502208 (2005). https://arxiv.org/abs/cond-mat/0502208
