# An exact ordered-cascade entanglement-breaking threshold for amplitude-damped qubits

## Finding
Let \(\mathcal A_q\) denote the zero-temperature qubit amplitude-damping channel with excited-state survival probability \(q\), and let \(0<a,b<1\). For every qubit unitary \(U\), define the ordered two-stage channel
\[
\Phi_{a,b,U}=\mathcal A_a\circ\operatorname{Ad}_U\circ\mathcal A_b,
\qquad t=|\langle1|U|0\rangle|^2\in[0,1].
\]
Then the **exact necessary-and-sufficient criterion** for this channel to be entanglement breaking is
\[
\boxed{\Phi_{a,b,U}\ \text{is entanglement breaking}
\quad\Longleftrightarrow\quad (1-a)(1-b)t^2\ge b.}
\]
In particular, an entanglement-breaking intermediate unitary exists precisely when
\[
\boxed{b\le\frac{1-a}{2-a};}
\]
when it exists, **all** successful unitaries are characterized by \(t\ge\sqrt{b/((1-a)(1-b))}\). The optimal attainable value is \(t=1\), achieved exactly by population-interchanging unitaries up to diagonal phases. There is no such effect without a population interchange: \(\mathcal A_a\circ\mathcal A_b=\mathcal A_{ab}\) is not entanglement breaking for \(a,b>0\).

The condition distinguishes the **order** of the two noise stages. At \(a=1/2\) and \(b=1/9\), the channel \(\mathcal A_{1/2}\circ\operatorname{Ad}_U\circ\mathcal A_{1/9}\) is entanglement breaking exactly for \(t\ge1/2\), while the reverse ordering \(\mathcal A_{1/9}\circ\operatorname{Ad}_U\circ\mathcal A_{1/2}\) is never entanglement breaking for any intermediate unitary.

For equal damping strengths \(a=b=q\), a population-interchanging unitary can make the cascade entanglement breaking exactly on the sharp interval
\[
\boxed{0<q\le\frac{3-\sqrt5}{2}.}
\]

## Assumptions and scope
The local Hilbert space is \(\mathbb C^2\), with ordered energy basis \(|0\rangle,|1\rangle\). The amplitude-damping Kraus operators are
\[
E_0(q)=\begin{pmatrix}1&0\\0&\sqrt q\end{pmatrix},\qquad
E_1(q)=\sqrt{1-q}\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
\mathcal A_q(X)=\sum_{j=0}^1 E_j(q)X E_j(q)^\dagger.
\]
The unitary \(U\) is arbitrary in \(U(2)\), and composition is read right to left, so \(b\) is the first (input) survival parameter, while \(a\) is the second (output) parameter. Entanglement breaking means that acting with the channel on half of **every** bipartite input state gives a separable output; the criterion uses the equivalent separability of its normalized Choi state. No small-noise approximation, thermal equilibrium assumption or restriction to real unitary controls is made.

## Proof
**Phase reduction.** A qubit unitary has an Euler factorization \(U=D_1 R D_2\) up to a global phase, where \(D_1,D_2\) are diagonal and
\[
R=\begin{pmatrix}c&-s\\s&c\end{pmatrix},\qquad c^2+s^2=1,\qquad s^2=t.
\]
Diagonal conjugations commute with each \(\mathcal A_q\) as channels. The diagonal factors therefore become unitary input/output conjugations of the cascade, which do not change whether it is entanglement breaking. We may take \(U=R\) with real \(c,s\).

**Exact Choi calculation.** Write \(h=\sqrt a\), \(g=\sqrt b\), \(k=\sqrt{1-a}\), \(\ell=\sqrt{1-b}\). The four Kraus operators for the cascade are \(K_{ij}=E_i(a)R E_j(b)\). Form its normalized Choi state
\[
J=(\mathrm{id}\otimes\Phi_{a,b,R})(|\Omega\rangle\langle\Omega|),\quad
|\Omega\rangle=(|00\rangle+|11\rangle)/\sqrt2.
\]
For partial transpose \(T=J^{\Gamma}\) on the output qubit, direct multiplication gives the identity
\[
\begin{aligned}
16\det T
&=h^4\bigl(k^4\ell^4s^8-g^4\bigr)\\
&=a^2\left((1-a)^2(1-b)^2t^4-b^2\right).
\end{aligned}
\]
This calculation is reproduced symbolically from the Kraus matrices by the accompanying verifier; it does not assume the desired criterion.

**Why the determinant detects separability.** For every positive two-qubit operator \(J\), its partial transpose has at most one strictly negative eigenvalue. Indeed, if it had two, their complex span would be a two-dimensional subspace on which the partial transpose is strictly negative. Every complex two-dimensional subspace of \(\mathbb C^2\otimes\mathbb C^2\) contains a nonzero product vector: reshape a spanning pair as \(2\times2\) matrices and solve the homogeneous quadratic determinant equation for their linear combination over \(\mathbb C\). But for a product vector \(x\otimes y\),
\[
\langle x\otimes y|J^{\Gamma}|x\otimes y\rangle
=\langle x\otimes\overline y|J|x\otimes\overline y\rangle\ge0,
\]
a contradiction. Thus, where \(\det T\ne0\), \(\det T>0\) is equivalent to \(T\ge0\), and \(\det T<0\) to \(T\not\ge0\). On the zero-determinant boundary with \(0<a,b<1\), positivity follows by continuity from strictly positive-determinant parameter choices, obtained by slightly decreasing \(b\). By the Peres–Horodecki criterion for two qubits, \(J\) is separable exactly when \(T\ge0\), which is exactly when \(\Phi_{a,b,U}\) is entanglement breaking.

Because \(a,b\) and \(1-a,1-b\) are strictly positive, factoring the displayed determinant yields
\[
\det T\ge0\quad\Longleftrightarrow\quad
(1-a)(1-b)t^2\ge b.
\]
The admissible range \(0\le t\le1\) yields the unitary-existence threshold \(b(2-a)\le1-a\), or \(b\le(1-a)/(2-a)\). Swapping \(a\) and \(b\) changes that criterion. For \(a=b=q\), it becomes \((1-q)^2\ge q\), whose solution inside \((0,1)\) is \(q\le(3-\sqrt5)/2\).

**Boundaries.** The theorem assumes strictly positive survival probabilities strictly below one. If \(a=0\) or \(b=0\), the cascade is entanglement breaking because one stage is a constant-output channel; the determinant test degenerates and should not be extended by a strict-sign argument. If \(a=1\) or \(b=1\), the remaining positive-survival amplitude damping with a unitary pre/post transformation is not entanglement breaking. These endpoint facts follow directly from the channel definition.

## Verification
The standalone `verify.py` reconstructs all four composite Kraus operators, forms the normalized \(4\times4\) Choi partial transpose, factors its determinant in independent symbolic amplitude variables, and confirms the normalization identity. It also builds the Choi state numerically from separate Kronecker operations and checks eight interior/boundary/order-reversed parameter cases against the analytic determinant and PPT sign. Its successful output is `VERIFY_OK symbolic_Choi_determinant=passed Kraus_trace=passed numerical_cases=8 order_boundary=passed`. Symbolic algebra checks the determinant identity; the universal implication uses the analytic two-qubit argument above rather than finite sampling. Python 3 with SymPy and NumPy is sufficient to rerun the checks.

## Relationship to prior work
Lami and Giovannetti, *Entanglement-Breaking Indices* (first public preprint arXiv:1411.2517v1, 2014-11-10), establish the basic entanglement-breaking index/filter framework and the exact entanglement-breaking condition for generalized amplitude-damping channels (Sec. III, Example 1). Their direct unfiltered-composition formula explains why pure zero-temperature amplitude damping never becomes entanglement breaking at a finite number of positive-survival steps. The bit-flip-only endpoint here can also be recovered using their generalized-damping PPT criterion after an output basis swap. The additional result is the full **all-unitary, two-unequal-stage** sharp classification, including the order-sensitive phase boundary, not the known generalized-damping test itself.

Cuevas et al., *Amending entanglement-breaking channels via intermediate unitary operations* (arXiv:1707.00161v1, 2017), study rotated amplitude damping experimentally; their five-page text (Sec. II–IV and Figs. 2–4) illustrates an entanglement-breaking cascade and unitary rescue for selected parameters. These examples overlap the physical mechanism, but the inspected text does not give the arbitrary unequal-damping criterion, the entire unitary rotation threshold or the order asymmetry. Filippov, Rybár and Ziman (2012) address entanglement annihilation by local two-qubit channels, a different quantified property. An equivalent parametrization in the wider literature remains a residual priority risk.

## Limitations
The statement is confined to serial two-stage zero-temperature qubit amplitude damping and **unitary** controls. It does not characterize nonunitary intermediate filters, more stages, finite-temperature generalized damping, qudit noise, entanglement-breaking times of arbitrary dynamics, or quantitative channel capacities. The result's relation to the prior generalized-damping formula is acknowledged; the closed all-unitary boundary is the new claim. Literature search cannot certify absolute priority, and independent validation has not been performed.

## References
1. L. Lami and V. Giovannetti, *Entanglement-Breaking Indices*, arXiv:1411.2517v1 (2014), subsequently Journal of Mathematical Physics 56, 092201 (2015). https://arxiv.org/abs/1411.2517
2. Á. Cuevas et al., *Amending entanglement-breaking channels via intermediate unitary operations*, arXiv:1707.00161v1 (2017), Physical Review A 96, 022322. Author-accepted open-access PDF: https://ricerca.sns.it/retrieve/db0ea4be-1cd0-448c-bb2b-ab671f299d1b/1707.00161v1.pdf
3. S. N. Filippov, T. Rybár and M. Ziman, *Local two-qubit entanglement-annihilating channels*, Physical Review A 85, 012303 (2012). https://doi.org/10.1103/PhysRevA.85.012303
4. A. Peres, *Separability Criterion for Density Matrices*, Physical Review Letters 77, 1413 (1996). https://doi.org/10.1103/PhysRevLett.77.1413
5. M. Horodecki, P. Horodecki and R. Horodecki, *Separability of mixed states: necessary and sufficient conditions*, Physics Letters A 223, 1–8 (1996). https://doi.org/10.1016/S0375-9601(96)00706-2
