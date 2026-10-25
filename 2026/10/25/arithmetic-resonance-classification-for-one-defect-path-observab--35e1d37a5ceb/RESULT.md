# Arithmetic resonance classification for one-defect path observability

## Finding

Let \(m\ge 2\) be an integer, and let \(w>0\). Give the path on vertices \(1,\ldots,2m\) unit conductance on all edges except the central edge \(\{m,m+1\}\), whose conductance is \(w\). Write \(L_{m,w}\) for its weighted combinatorial Laplacian. For a sensor at vertex \(j\), consider the continuous-time dynamics \(\dot z=-L_{m,w}z\) and scalar observation \(y=z_j\). By reflection it suffices to take \(1\le j\le m\).

Define \(q=2j-1\). For each \(1\le r<j\) put
\[
\theta_r=\frac{(2r-1)\pi}{q},\qquad
W_r(m,j)=\frac{\sin(\theta_r/2)\sin(m\theta_r)}{\cos((m-\tfrac12)\theta_r)}
\]
whenever the displayed denominator is nonzero. Let \(E_{m,j}\) be the set of **positive** values among these defined numbers.

**Theorem.** The pair \((-L_{m,w},e_j^{\mathsf T})\) is observable if and only if
\[
\boxed{\gcd(m,2j-1)=1\quad\text{and}\quad w\notin E_{m,j}.}
\]
For fixed \(j\), the set \(E_{m,j}\) and the complete observable/unobservable status at every fixed positive \(w\) depend only on the residue of \(m\) modulo \(2j-1\), provided \(m\ge j\). There are at most \(j-1\) exceptional positive conductances unless the gcd condition forces unobservability for **every** positive conductance.

In particular, for a sensor at the second vertex, the classification is an exact three-residue law:
\[
\boxed{\begin{array}{c|c}
m\pmod 3&\text{unobservable positive conductances}\hline
0&\text{all }w>0\\
1&\{\tfrac12\}\\
2&\varnothing
\end{array}}
\]
The unobservable subspace in either nonempty second-vertex case has dimension exactly one. Thus a single central-edge adjustment to \(w=1/2\) creates an unobservable mode for every path of length \(2m\) with \(m\equiv1\pmod3\), whereas for \(m\equiv2\pmod3\) no positive central-edge adjustment can do so.

## Assumptions and scope

All paths are finite, undirected, connected, and have strictly positive edge conductances. The matrix is the **combinatorial** weighted Laplacian, not the normalized Laplacian or weighted adjacency matrix. Full observability means recovery of every real initial state from the ideal noiseless trajectory \(t\mapsto y(t)\), equivalently the Kalman rank or PBH criterion. It says nothing about the condition number of a finite-horizon observability Gramian or robustness to noise. The theorem concerns a **single central defective edge**, not arbitrary edge-weight patterns. The same classification holds for single-vertex controllability of \((-L_{m,w},e_j)\) by symmetry.

## Proof

1. **Parity reduction and spectral simplicity.** Reflection across the central edge commutes with \(L_{m,w}\). Symmetric eigenvectors are obtained by duplicating a length-\(m\) vector; their reduced operator is the ordinary Neumann path Laplacian \(N_m\) with diagonals \(1,2,\ldots,2,1\) and nearest-neighbor entries \(-1\). Antisymmetric eigenvectors are obtained by duplicating with the opposite sign; their reduced operator is \(N_m+2we_me_m^{\mathsf T}\). Each is an irreducible symmetric Jacobi matrix with simple spectrum. Their spectra are disjoint for \(w>0\): if the two matrices shared \(\lambda\), the eigenvector recurrence with the first vertex normalized would make their eigenvectors coincide until the final equation, where subtraction forces \(2w v_m=0\). A nonzero irreducible-Jacobi eigenvector cannot vanish at its final coordinate, a contradiction. The full path operator therefore has simple spectrum. Its PBH observability test reduces to checking that no eigenvector has zero \(j\)-th component.

2. **Neumann sector.** An eigenvector in the symmetric sector has, up to a nonzero scalar, coordinates \(v_i=\cos((i-\tfrac12)\theta)\) with \(\theta=k\pi/m\) and \(0\le k<m\). For \(k=0\) it never vanishes. Otherwise \(v_j=0\) precisely when \((2j-1)k/m\) is odd. This happens for some \(1\le k<m\) exactly when \(\gcd(m,2j-1)>1\): necessity follows from the divisibility condition; for sufficiency put \(g=\gcd(m,2j-1)\) and \(k=m/g\), so that \((2j-1)/g\) is an odd positive integer. This zero mode exists independently of \(w\).

3. **Antisymmetric sector.** Fix any eigenvector of \(N_m+2we_me_m^{\mathsf T}\). The equations at vertices \(1,\ldots,m-1\) are unchanged. The nonzero first coordinate and the recurrence imply \(v_i=c\cos((i-\tfrac12)\theta)\), where \(\lambda=2-2\cos\theta\) whenever a coordinate \(v_j\) with \(j\ge2\) vanishes. Indeed, such a zero forces \(\lambda\) to be an eigenvalue of the left \((j-1)\)-vertex Neumann-Dirichlet submatrix, which has exactly the parameters \(\theta=\theta_r\), \(1\le r<j\), all strictly between zero and \(\pi\). The final reduced eigenvalue equation is
\[
-v_{m-1}+(1+2w)v_m=\lambda v_m.
\]
If \(v_m=0\), this equation forces \(v_{m-1}=0\) and hence all entries zero, impossible. Thus \(\cos((m-\tfrac12)\theta_r)\ne0\), and substitution gives
\[
2w=\lambda-1+\frac{\cos((m-\tfrac32)\theta_r)}{\cos((m-\tfrac12)\theta_r)}
=\frac{2\sin(\theta_r/2)\sin(m\theta_r)}{\cos((m-\tfrac12)\theta_r)}.
\]
This proves that a zero in the antisymmetric sector requires \(w=W_r(m,j)>0\). Conversely, whenever the denominator is nonzero and this value is positive, the displayed cosine sequence solves every reduced eigenvalue equation, is nonzero, and vanishes at \(j\). It therefore supplies an unobservable eigenvector. For \(j=1\) there is no candidate; for \(j=m\), every candidate has a zero denominator, consistent with unconditional central-vertex observability.

4. **Periodicity.** With \(q=2j-1\), increasing \(m\) by \(q\) changes each \(m\theta_r\) and \((m-\tfrac12)\theta_r\) by the odd multiple \((2r-1)\pi\). Their sine and cosine consequently change sign together. A zero denominator remains zero and every defined \(W_r\) is unchanged. Since the gcd condition also depends only on \(m\pmod q\), the entire classification is periodic as asserted.

5. **Second-vertex law and dimension.** For \(j=2\), there is only \(\theta_1=\pi/3\). If \(3\mid m\), the Neumann sector has precisely one zero eigenvector at this sensor (\(k=m/3\)) and the antisymmetric candidate would require \(w=0\), excluded. If \(m\equiv1\pmod3\), the Neumann sector is observable and the antisymmetric boundary expression equals \(1/2\). If \(m\equiv2\pmod3\), its denominator is zero, so no antisymmetric zero is possible. Simplicity of both reduced spectra and their disjointness give unobservable dimension one in the two nonempty cases.

## Verification

The accompanying standalone file `verify.py` constructs exact tridiagonal characteristic polynomials and determines observability by their polynomial greatest common divisors after deletion of the sensor vertex. It checks 462 combinations with \(2\le m\le12\), all \(1\le j\le m\), and six positive rational conductances, comparing them with the trigonometric criterion. It separately checks 22 second-vertex cases at conductances \(1/2\) and \(1\). All comparisons pass, as recorded in `verify_output.txt`. These finite checks are neither exhaustive for all sizes nor substitutes for the preceding proof.

## Relationship to prior work

Parlangeli and Notarstefano (2011) characterize observability for **uniform unweighted** paths and cycles using number-theoretic criteria. Their results imply the present answer at \(w=1\), but do not characterize positive perturbations of a singled-out central edge. Monshizadeh, Zhang and Camlibel (2014) characterize strong structural controllability by zero forcing; they explain why path endpoints are privileged for all weights, but this qualitative guarantee does not determine which **interior** sensors succeed at individual weight values. Bianchin and colleagues (2016, expanded preprint 2016) study the observability radius for weighted-adjacency networks and an endpoint-observed line model; those results do not imply the present complete weighted-**Laplacian**, interior-sensor resonance formula. Earlier classifications for one-weight **cycles** also do not imply the central-edge path classification; the boundary recurrences and exceptional sets differ.

## Limitations

The conclusion is an exact binary observability classification, not a bound on estimation accuracy, Gramian conditioning, or resilience to general multiedge perturbations. A published-equivalence comparison can miss specialized accounts of boundary-perturbed Jacobi matrices; the derivation uses classical recurrence and PBH ingredients, so mathematical originality beyond those ingredients must be assessed in that context. The arithmetic exceptional sets may contain duplicates, and their presentation is as a set rather than as a count of distinct eigenmodes. No independent audit has been performed.

## References

- G. Parlangeli and G. Notarstefano, *On the reachability and observability of path and cycle graphs*, arXiv:1109.3556, first posted 16 September 2011; IEEE Transactions on Automatic Control 57 (2012), 743–748.
- N. Monshizadeh, S. Zhang, and M. K. Camlibel, *Zero forcing sets and controllability of dynamical systems defined on graphs*, arXiv:1403.4868, first posted 19 March 2014; IEEE Transactions on Automatic Control 59 (2014), 2562–2567.
- G. Bianchin, P. Frasca, A. Gasparri, and F. Pasqualetti, *The observability radius of network systems*, American Control Conference, 6–8 July 2016, DOI:10.1109/ACC.2016.7524913; expanded treatment *The Observability Radius of Networks*, arXiv:1612.06120, first posted 19 December 2016.
