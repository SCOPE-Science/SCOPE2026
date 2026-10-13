# Exact PPT-mixture rigidity of a randomized single hyperedge
## Finding
The randomized-hypergraph model applies a multi-qubit phase gate to a chosen hyperedge with probability \(p\), or leaves the hyperedge unchanged with probability \(1-p\). For one hyperedge, this produces a rank-at-most-two density matrix. Even though the source literature studies the genuine multipartite entanglement of randomized hypergraphs with numerical PPT-mixture tests, the one-edge case has an exact all-size classification.

**Theorem.** Let \(n\ge2\). Choose a vertex set \(V=\{1,\ldots,n\}\), an edge \(E\subseteq V\) with \(|E|\ge2\), a probability \(p\in[0,1]\), and a phase \(\theta\in\mathbb R\). Put
\[
|a\rangle=|+\rangle^{\otimes n},\qquad
C_E(\theta)=I_E+(e^{i\theta}-1)|1\cdots1\rangle_E\langle1\cdots1|,
\]
\[
|\psi_{E,\theta}\rangle=(C_E(\theta)\otimes I_{E^c})|a\rangle,
\qquad
\rho_{E,p,\theta}=(1-p)|a\rangle\langle a|
+p|\psi_{E,\theta}\rangle\langle\psi_{E,\theta}|.
\]
A **PPT mixture** is a convex combination of density matrices each having positive partial transpose across at least one bipartition; the bipartition may vary from one component to another. A state is **genuinely multipartite entangled** (GME) if it is not a convex mixture of pure states product across various bipartitions.

Then
\[
\boxed{
\rho_{E,p,\theta}\text{ is a PPT mixture}
\quad\Longleftrightarrow\quad
E\ne V\ \text{or}\ p=0\ \text{or}\ e^{i\theta}=1.
}
\]
In the complementary regime
\[
E=V,\qquad p>0,\qquad e^{i\theta}\ne1,
\]
the state is not a PPT mixture and therefore is GME. Thus the exact random-gate success threshold for the single spanning edge is \(p_{\mathrm{crit}}=0\) (strictly positive \(p\) gives GME).

The complete answer admits a quantitative partial-transpose certificate. For every cut \(A|B\) with \(|A|=k\) and \(|B|=n-k\), the nonzero support of \(\rho_{V,p,\theta}^{T_B}\) lies inside an explicit local \(2\otimes2\) subspace. In an orthonormal basis of that subspace,
\[
\boxed{
\det\bigl((\rho_{V,p,\theta}^{T_B})_{4\times4}\bigr)
=-\frac{16p^3}{2^{2n}}\sin^4(\theta/2)
\bigl(1-2^{-k}\bigr)^2
\bigl(1-2^{-(n-k)}\bigr)^2<0.
}
\]
Consequently the state is NPT across every nontrivial cut. The determinant formula holds for \(p=0\) or a trivial phase as an equality with zero on the right; strict negativity requires the complementary regime above.

## Assumptions and scope
The quantum register consists of exactly \(n\) qubits, initially \(|+\rangle^{\otimes n}\). Each run either applies the ideal diagonal controlled-phase gate to the single chosen edge or leaves it unaltered. The classical success flag is discarded, giving the mixture above; conditioning on a retained success flag instead produces a different state.

The article's ordinary hypergraph gate has \(\theta=\pi\). The weighted-phase extension \(\theta\in\mathbb R\) is included because its ideal phase gate is defined in the same source formalism. The result requires only one edge and makes no claim about multiple simultaneously randomized gates, nonbinary coherent imperfections, imperfect single-qubit preparations, leakage, local depolarization, or correlated physical noise. The exact determinant is of the active \(4\times4\) matrix rather than the determinant of the full exponentially large partial transpose, which is zero whenever the latter has unused local dimensions.

## Proof
If \(E\subsetneq V\), both branches act identically on the complement:
\[
\rho_{E,p,\theta}
=\rho_{E,p,\theta}^{(E)}\otimes
|+\rangle\langle+|^{\otimes |V\setminus E|}.
\]
It is product across \(E|E^c\), hence biseparable and a PPT mixture. If \(p=0\) or \(e^{i\theta}=1\), the state equals \(|a\rangle\langle a|\) and is fully product. These cases exhaust the asserted non-GME side.

Assume henceforth that \(E=V\) and that \(e^{i\theta}\ne1\). Write
\[
|v\rangle=|1\rangle^{\otimes n},\qquad
\gamma=2^{-n/2},\qquad
\kappa=(e^{i\theta}-1)\gamma.
\]
Since the spanning-edge gate changes only the all-ones computational-basis amplitude,
\[
|\psi_{V,\theta}\rangle=|a\rangle+\kappa|v\rangle.
\]
The vector on the right is normalized, because \(C_V(\theta)\) is unitary. As \(\kappa\ne0\) and \(|a\rangle,|v\rangle\) are independent, the state has support
\[
S=\operatorname{span}\{|a\rangle,|v\rangle\}
\]
when \(0<p<1\).

Fix any cut \(A|B\) with \(|A|=k\). Define
\[
\alpha=2^{-k/2},\quad \beta=2^{-(n-k)/2},\quad
u=\sqrt{1-\alpha^2},\quad w=\sqrt{1-\beta^2}.
\]
The local vectors \(|a_A\rangle=|+\rangle^{\otimes k}\) and \(|v_A\rangle=|1\rangle^{\otimes k}\) have overlap \(\alpha\), and similarly for \(B\). They are independent on both sides because \(1\le k<n\). Choose local orthonormal vectors
\[
|0_A\rangle=|a_A\rangle,\qquad
|1_A\rangle=\frac{|v_A\rangle-\alpha|a_A\rangle}{\nu},
\]
with analogous \(|0_B\rangle,|1_B\rangle\) using \(\beta,w\). In the induced \(2\otimes2\) basis, \(|a\rangle=|00\rangle\) and the coefficient matrix of \(|\psi_{V,\theta}\rangle\) is
\[
H=\begin{pmatrix}
1+\kappa\alpha\beta&\kappa\alpha w\\
\kappa\nu\beta&\kappa\nu w
\end{pmatrix}.
\]
A direct determinant calculation gives
\[
\det H=\kappa\nu w,
\qquad H_{11}=\kappa\nu w.
\]

For an arbitrary two-qubit pure vector \(|h\rangle\) with coefficient matrix \(H=(h_{ij})\), put \(Q=(|h\rangle\langle h|)^{T_B}\). The nonzero eigenvalues of \(Q\), expressed via the two Schmidt coefficients \(s_1,s_2\), are \(s_1^2,s_2^2,s_1s_2,-s_1s_2\). Therefore
\[
\det Q=-|\det H|^4.
\]
Direct expansion of the principal minor obtained by deleting the \(|00\rangle\) row and column gives the cofactor identity
\[
C_{00}(Q)=-|h_{11}|^2|\det H|^2.
\]
Because the classical gate-failure branch is \(|00\rangle\langle00|\) in this basis,
\[
(\rho_{V,p,\theta}^{T_B})_{4\times4}
=pQ+(1-p)|00\rangle\langle00|.
\]
The determinant is linear in the \((00,00)\) entry when all other entries are fixed, so
\[
\begin{aligned}
\det(\rho_{V,p,\theta}^{T_B})_{4\times4}
&=p^4\det Q+(1-p)p^3C_{00}(Q)\\
&=-p^3|\kappa|^4\nu^4w^4.
\end{aligned}
\]
The identity
\[
|\kappa|^4=16\,2^{-2n}\sin^4(\theta/2)
\]
yields precisely the formula displayed in the theorem. The determinant is strictly negative for \(p>0\) and nontrivial phase, proving NPT across every cut.

NPT across every cut does *not*, for general mixed multipartite states, by itself prove GME: mixtures of states separable across different cuts can be NPT across each individual cut. We therefore give a separate PPT-mixture exclusion proof.

For the same cut, consider any vector in \(S\):
\[
|z\rangle=s|a_A\rangle\otimes|a_B\rangle
+t|v_A\rangle\otimes|v_B\rangle.
\]
In the (nonorthogonal but independent) local bases \((a_A,v_A)\), \((a_B,v_B)\), its coefficient matrix is diagonal with entries \(s,t\). Hence \(|z\rangle\) is product across that cut if and only if \(st=0\). Thus **the only product rays in \(S\) for every bipartition are the rays of \(|a\rangle\) and \(|v\rangle\)**.

Suppose \(0<p<1\) and \(\rho\) were a PPT mixture. Write it as a finite sum of positive semidefinite operators, each PPT across a chosen cut. Because their sum has support \(S\), positivity forces each summand to have support contained in \(S\). In the chosen cut, \(S\) is contained in the local \(2\otimes2\) subspace constructed above. The two-qubit Peres--Horodecki theorem says that a PPT operator on \(2\otimes2\) is separable across that cut. Every product vector occurring in a separable decomposition of such a summand also lies in \(S\); by the rank argument, it must be proportional to \(|a\rangle\) or \(|v\rangle\). Hence the entire PPT mixture would have to be of the form
\[
q_a|a\rangle\langle a|+q_v|v\rangle\langle v|
\qquad(q_a,q_v\ge0).
\]
But the actual expansion is
\[
\rho_{V,p,\theta}
=|a\rangle\langle a|
+p\kappa|v\rangle\langle a|
+p\overline\kappa|a\rangle\langle v|
+p|\kappa|^2|v\rangle\langle v|.
\]
The four operators \(|a\rangle\langle a|\), \(|a\rangle\langle v|\), \(|v\rangle\langle a|\), and \(|v\rangle\langle v|\) are linearly independent because \(|a\rangle,|v\rangle\) are independent. The nonzero coefficient \(p\kappa\) makes the asserted diagonal decomposition impossible.

Finally, when \(p=1\), the state is the pure projector onto \(|\psi_{V,\theta}\rangle\). Its coefficient matrix has nonzero determinant in *every* cut. Therefore it is entangled across every cut and cannot be a PPT mixture. Together these cases prove the theorem.

## Verification
The theorem for all integer \(n\ge2\) and all real phases is analytic. The supporting file `artifacts/verify.py` checks the two-qubit cofactor identity for diverse complex coefficient matrices; numerically compares the exact active-block determinant with its closed expression for \(2\le n\le8\), every cut and multiple phases and probabilities; and separately checks the active block against direct full computational-basis partial transposes for \(2\le n\le5\). The finite computations are transcription checks, not a substitute for the universal proof.

## Relationship to prior work
Salem, Silva and Andrade define randomized hypergraph states by probabilistic application of perfect controlled-phase hyperedges and analyze bipartite negativity and genuine multipartite entanglement largely numerically for three- and four-qubit systems. Their article includes a single spanning four-body hyperedge as a pure-state example, but does not determine the all-size, all-probability PPT-mixture boundary for a single randomized spanning hyperedge. Its discussion of randomized states formed from multiple edges does not imply the present rank-two classification.

The earlier Salem--Silva--Andrade paper examines entanglement sudden death and birth when different hyperedge orders compete; it does not provide this one-edge exact classification.

Chen and Đoković already prove, in particular, that mixing a product projector with an entangled pure-state projector yields a bipartite NPT state (Lemma 12 of arXiv:1301.2372). **Consequently, qualitative NPT across each cut is not claimed as the original contribution**: it also follows by applying their lemma to the present pure spanning-edge branch. Their general rank-two PPT separability results and the classical \(2\otimes2\) PPT criterion also support the reasoning. The source-specific contributions here are the explicit determinant at every cut, the necessary-and-sufficient all-parameter classification of **PPT mixtures** (a strictly stronger obstruction than NPT on each cut), and the extension to arbitrary controlled phases.

Jungnitsch, Moroder and Gühne introduced the PPT-mixture relaxation to certify GME. That general methodology and its definitions are prior work; the theorem computes the relaxation exactly for this architecture without an SDP and for arbitrary qubit number.

## Limitations
No numerical value is claimed for a GME monotone or the optimization objective of a PPT-mixture SDP. Strict nonmembership does not provide an experimental detection threshold under finite measurement precision. The determinant can be very small for large \(n\), small \(p\), or near-trivial phases. The model includes exactly one ideal-or-absent gate, not realistic coherent or incoherent gate noise and not networks containing multiple random hyperedges.

## References
1. V. Salem, A. A. Silva, and F. M. Andrade, *Randomized hypergraph states and their entanglement properties*, arXiv:2506.20075v1 (2025; first public June 25, 2025), DOI 10.1002/andp.202500622.
2. V. Salem, A. A. Silva, and F. M. Andrade, *Multipartite entanglement sudden death and birth in randomized hypergraph states*, arXiv:2310.20418v2, Physical Review A 109, 012416 (2024).
3. L. Chen and D. Ž. Đoković, *Separability problem for multipartite states of rank at most four*, arXiv:1301.2372v1, Journal of Physics A 46, 275304 (2013).
4. M. Horodecki, P. Horodecki, and R. Horodecki, *Separability of mixed states: necessary and sufficient conditions*, Physics Letters A 223, 1 (1996), DOI 10.1016/S0375-9601(96)00706-2.
5. B. Jungnitsch, T. Moroder, and O. Gühne, *Taming multiparticle entanglement*, Physical Review Letters 106, 190502 (2011), DOI 10.1103/PhysRevLett.106.190502.
