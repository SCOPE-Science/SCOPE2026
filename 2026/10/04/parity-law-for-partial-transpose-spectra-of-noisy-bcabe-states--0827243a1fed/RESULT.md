# Parity law for partial-transpose spectra of noisy BCABE states
## Finding
For every integer \(N\ge 1\), put \(n=2N+2\). Let \(R_1,\ldots,R_4\) denote the four orthogonal BCABE vertex states on \(n\) qubits and let
\[
\rho_p=\sum_{i=1}^4p_iR_i,\qquad p_i\ge0,\qquad \sum_{i=1}^4p_i=1,
\]
with \(w=\max_i p_i\). If \(T_S\) denotes partial transposition on a nonempty proper subset \(S\) of \(m\) qubits, then the complete spectrum of \(\rho_p^{T_S}\) depends only on the parity of \(m\).

For even \(m\),
\[
\rho_p^{T_S}=\rho_p,
\]
and the eigenvalues are
\[
\frac{p_1}{4^N},\ \frac{p_2}{4^N},\ \frac{p_3}{4^N},\ \frac{p_4}{4^N},
\]
each with multiplicity \(4^N\). For odd \(m\), the eigenvalues are
\[
\frac{1/2-p_1}{4^N},\ \frac{1/2-p_2}{4^N},\ \frac{1/2-p_3}{4^N},\ \frac{1/2-p_4}{4^N},
\]
each with multiplicity \(4^N\), up to permutation.

It follows that every even-size bipartition is PPT. Every odd-size bipartition has the same negativity
\[
\mathcal N(\rho_p)=\max\{0,w-1/2\}
\]
and logarithmic negativity
\[
E_{\mathcal N}(\rho_p)=\max\{0,\log_2(2w)\}.
\]
Thus the amount of NPT entanglement across every odd cut is independent of the number of qubits, even though each individual negative eigenvalue shrinks as \(4^{-N}\) and its multiplicity grows as \(4^N\).

## Assumptions and scope
The family is exactly the four-weight noisy BCABE family introduced by Bandyopadhyay, Chattopadhyay, Roychowdhury, and Sarkar. Their four vertices are mutually orthogonal normalized projectors, are related by a single local Pauli operation, and their noisy state uses the four weights \(x_+,x_-,y_+,y_-\); here \((p_1,p_2,p_3,p_4)\) is that four-tuple in an arbitrary fixed ordering.

The statement concerns the spectrum under partial transposition and the induced negativity measures. It does not assert that PPT across an arbitrary even-size cut implies separability. The source proves separability for every \(2:(2N)\) cut; the present result only asserts PPT for all even-size cuts.

## Proof
Let \(X,Y,Z\) be the Pauli matrices and write \(X_n=X^{\otimes n}\), \(Y_n=Y^{\otimes n}\), and \(Z_n=Z^{\otimes n}\). The generalized Smolin/BCABE four-vertex simplex has the Hilbert--Schmidt form
\[
R_i=2^{-n}\bigl(I+t_{i1}X_n+t_{i2}Y_n+t_{i3}Z_n\bigr),
\]
where the four sign vectors \(t_i\in\{-1,1\}^3\) form a regular tetrahedron:
\[
t_i\cdot t_i=3,\qquad t_i\cdot t_j=-1\quad(i\ne j).
\]
This follows from the Hilbert--Schmidt expression for generalized Smolin states together with the local-Pauli relation among the four BCABE vertices; the recursive BCABE construction and the Hilbert--Schmidt construction agree at the four-qubit Smolin state and obey the same Pauli-correlated recursion.

Because \(n\) is even, \(X_n,Y_n,Z_n\) commute. They have four joint eigenspaces, one for each allowed tetrahedral sign vector, and every joint eigenspace has dimension \(2^{n-2}=4^N\). For
\[
c=\sum_{i=1}^4p_it_i,
\]
we have
\[
\rho_p=2^{-n}\bigl(I+c_1X_n+c_2Y_n+c_3Z_n\bigr).
\]
On the joint eigenspace with sign vector \(t_i\),
\[
2^{-n}(1+c\cdot t_i)
=2^{-n}\left(1+3p_i-\sum_{j\ne i}p_j\right)
=\frac{p_i}{2^{n-2}}
=\frac{p_i}{4^N}.
\]
This proves the original spectrum and its degeneracy.

Transposition fixes \(X\) and \(Z\) and sends \(Y\) to \(-Y\). Therefore partial transposition on \(m\) qubits sends
\[
(c_1,c_2,c_3)\longmapsto(c_1,(-1)^m c_2,c_3).
\]
If \(m\) is even, the state is unchanged. If \(m\) is odd, this is reflection of the tetrahedron in one coordinate. That reflection sends each tetrahedral vertex to the antipode of another vertex. Hence, after a permutation \(\pi\) of the four labels,
\[
1+(Rc)\cdot t_i
=1+\sum_jp_j(Rt_j)\cdot t_i
=1+(1-p_{\pi(i)})-3p_{\pi(i)}
=4\left(\frac12-p_{\pi(i)}\right).
\]
Division by \(2^n\) gives the odd-parity spectrum.

Since the four probabilities sum to one, at most one exceeds \(1/2\). If \(w>1/2\), exactly \(4^N\) eigenvalues are negative and each equals \((1/2-w)/4^N\). Their absolute sum is therefore \(w-1/2\). If \(w\le1/2\), no eigenvalue is negative. Finally,
\[
\lVert\rho_p^{T_S}\rVert_1=1+2\mathcal N(\rho_p),
\]
which gives \(E_{\mathcal N}=\log_2\lVert\rho_p^{T_S}\rVert_1=\max\{0,\log_2(2w)\}\).

## Verification
The bundled `verify.py` independently constructs the Pauli-simplex matrices for \(N=1,2,3\), checks the orthogonal-projector scaling, explicitly partially transposes representatives of every nontrivial subset size, and compares numerical spectra and negativities with the closed forms for four distinct probability vectors. Its recorded output is:

`VERIFY_OK parity_spectra=60 levels=3 test_weights=4`

The finite matrix checks are supplementary. The proof above establishes the formula for every \(N\ge1\) and every admissible probability vector.

## Relationship to prior work
Bandyopadhyay et al. introduced the noisy four-weight BCABE family, rewrote it using Bell-diagonal two-qubit blocks, and proved the activation threshold \(w>1/2\). They did not state the complete partial-transpose spectrum or a negativity formula for all bipartitions.

Augusiak and Horodecki gave the Hilbert--Schmidt Pauli representation of generalized Smolin states, supplying the algebraic representation used above. Their inspected text develops Bell inequalities and information-concentration properties; it does not state negativity or partial-transpose spectral formulas for the four-weight noisy simplex.

Hiesmayr et al. subsequently described the same even-qubit Pauli tetrahedron, observed that partial transposition of an odd number of qubits flips the \(Y^{\otimes n}\) coefficient while an even number returns the positivity condition, and derived a multipartite concurrence-type measure. This gives the closest prior geometric coverage. The present result is the stronger spectral statement: it identifies all four partial-transpose eigenvalues, their exact degeneracy, the parity-uniform negativity, and the logarithmic negativity in the original noisy-BCABE barycentric weights.

As an external relevance check, recent experimental work on the four-qubit Smolin state studies one-versus-three negativity under white noise and reports the familiar \(2/3\) white-noise threshold. The present formula reproduces that special case immediately: for \(\rho(q)=(1-q)R_1+qI/16\), one has \(w=1-3q/4\), so \(\mathcal N=\max\{0,1/2-3q/4\}\).

## Limitations
The result is restricted to the four-vertex BCABE/generalized-Smolin simplex. It does not quantify entanglement outside this simplex, does not turn PPT on even cuts into a separability theorem, and does not equate negativity with distillable entanglement. The literature comparison cannot rule out an unindexed source that independently writes the same spectrum; the closest inspected sources provide the threshold and parity geometry but not the stated spectral/negativity formulas.

## References
1. S. Bandyopadhyay, I. Chattopadhyay, V. Roychowdhury, and D. Sarkar, “Bell-Correlated Activable Bound Entanglement in Multiqubit Systems,” arXiv:quant-ph/0411082v1 (2004); Phys. Rev. A 71, 062317 (2005), DOI: 10.1103/PhysRevA.71.062317.
2. R. Augusiak and P. Horodecki, “Generalized Smolin states and their properties,” Phys. Rev. A 73, 012318 (2006), DOI: 10.1103/PhysRevA.73.012318.
3. B. C. Hiesmayr, F. Hipp, M. Huber, P. Krammer, and Ch. Spengler, “A simplex of bound entangled multipartite qubit states,” arXiv:0807.4842v2; Phys. Rev. A 78, 042327 (2008), DOI: 10.1103/PhysRevA.78.042327.
4. “Multiparticle entanglement of nuclear spins in silicon,” Nature Communications (2026), article s41467-026-74491-1.
