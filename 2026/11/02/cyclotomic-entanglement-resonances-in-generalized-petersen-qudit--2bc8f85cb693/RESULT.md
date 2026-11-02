# Cyclotomic entanglement resonances in generalized Petersen qudit graph states

## Finding

For every prime \(p\), integer \(m\ge2\), and integer \(1\le k<m\), form the generalized Petersen graph \(GP(2m,k)\) with vertices \(u_i,v_i\), indexed by \(i\in\mathbb Z/(2m)\), and edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+k}\). Prepare its pure unit-weight \(p\)-dimensional qudit graph state and cut it into
\[
 A=\{u_{2j},v_{2j+1}:j\in\mathbb Z/m\},\qquad
 B=\{u_{2j+1},v_{2j}:j\in\mathbb Z/m\}.
\]
Each side has \(2m\) qudits. For \(k\) even the reduced state has rank \(p^{2m}\): the cut is maximally entangled. For \(k\) odd, put
\[
 f_{p,k}(X)=X^{k+1}+X^k+X+1-X^{(k+1)/2}\in\mathbb F_p[X],
 \qquad \delta_{p}(m,k)=\deg\gcd\bigl(X^m-1,f_{p,k}(X)\bigr).
\]
Then the reduced state has exactly \(p^{2m-\delta_p(m,k)}\) nonzero eigenvalues, each \(p^{-(2m-\delta_p(m,k))}\). Hence **all positive-order Rényi entropies and the von Neumann entropy in base-\(p\) units** are exactly
\[
 S_p(m,k)=\begin{cases}2m,&k\text{ even},\\2m-\delta_p(m,k),&k\text{ odd}.\end{cases}
\]
No squarefreeness assumption on \(X^m-1\) is made; repeated roots are essential.

For every fixed odd \(k\), \(p=3\) gives \(\delta_3(m,k)\ge1\) at **every** admissible circumference, whereas for every prime \(p\ne3\) there are infinitely many admissible \(m\) with \(\delta_p(m,k)=0\) and infinitely many with \(\delta_p(m,k)>0\). For the natural five-step family \(k=5\), \(m\ge6\), the exact defects are
\[
 \delta_2(m,5)=\begin{cases}
 0,&3\nmid m,\\2\min\{3,2^{v_2(m)}\},&3\mid m,
 \end{cases}
 \qquad
 \delta_3(m,5)=\min\{2,3^{v_3(m)}\}\bigl(1+2\mathbf1_{4\mid m}\bigr).
\]
For the 24-qudit Nauru network \(GP(12,5)\), the corresponding entropies are \(8\) base-two units and \(10\) base-three units. For \(GP(16,5)\), the qubit cut is maximally entangled (\(16\) bits) while the qutrit cut has \(13\) base-three units.

## Assumptions and scope

All graphs are finite and simple, all controlled-phase edge weights are \(1\), and every local dimension \(p\) is prime. The edge \(\{x,y\}\) applies \(\mathrm{CZ}_p\lvert a,b\rangle=\omega^{ab}\lvert a,b\rangle\), where \(\omega=\exp(2\pi i/p)\), to \(\lvert+\rangle^{\otimes4m}\). Graph indices are modulo \(2m\). The cut is precisely the alternating outer/inner cut stated above. The entropy logarithm is base \(p\); multiply by \(\log_2p\) to obtain bits. By construction, the model has \(4m\) quantum sites and a balanced cut with \(2m\) sites per side.

## Proof

**1. Reduction to a finite-field rank.** Let \(D\) be the \((2m)\times(2m)\) adjacency block from \(A\) to \(B\), over \(\mathbb F_p\), and write \(r=\operatorname{rank}_{\mathbb F_p}D\). Gates internal to \(A\) or \(B\) act as local diagonal unitaries and do not change the cut spectrum. After removing their phases the coefficient matrix is \(M_{x,y}=p^{-2m}\omega^{x^{\mathsf T}Dy}\), for \(x,y\in\mathbb F_p^{2m}\). Orthogonality of additive characters gives
\[
 (MM^\dagger)_{x,x'}=p^{-2m}\mathbf1_{D^{\mathsf T}(x-x')=0}.
\]
The \(p^r\) cosets of \(\ker D^{\mathsf T}\) give \(p^r\) rank-one blocks, each with the single eigenvalue \(p^{-r}\). This establishes the entire flat nonzero spectrum, not merely its rank.

**2. Cross-cut matrix and Schur complement.** Index rows of \(D\) by \(u_{2j},v_{2j+1}\), columns by \(u_{2j+1},v_{2j}\). Let \(P\) be the cyclic shift of \(\mathbb F_p^m\) defined by \((Pz)_j=z_{j-1}\). The outer-cycle contribution is \(O=I+P\); each spoke contributes an identity block. If \(k\) is even, inner edges remain within the two sides and
\[
 D=\begin{pmatrix}O&I\\I&0\end{pmatrix}.
\]
The equation \(D(z,w)=0\) forces \(z=w=0\), so \(r=2m\). If \(k=2a+1\) is odd, inner edges cross and
\[
 D=\begin{pmatrix}O&I\\I&Q\end{pmatrix},\qquad
 Q=P^a+P^{-(a+1)}.
\]
The first row of \(D(z,w)=0\) gives \(w=-Oz\), and the second gives \((I-QO)z=0\). Multiply \(I-QO\) by the invertible scalar-shift \(-P^{a+1}\): the result is precisely
\[
 P^{k+1}+P^k+P+I-P^{a+1}=f_{p,k}(P).
\]
Thus the nullity of \(D\) equals the nullity of \(f_{p,k}(P)\).

**3. Cyclic module, including inseparable cases.** Identify \(\mathbb F_p^m\) with \(\mathbb F_p[X]/(X^m-1)\), so that \(P\) acts by multiplication by \(X\). For any \(g\), the nullity of multiplication by \(g\) in this quotient is \(\deg\gcd(g,X^m-1)\): writing \(h=\gcd(g,X^m-1)\) and \(X^m-1=hw\), the kernel consists exactly of the residue classes divisible by \(w\), giving \(\deg h\) dimensions. This argument works when \(p\mid m\), when \(X^m-1\) has repeated roots. It proves the general formula.

**4. Prime-characteristic dichotomy.** If \(k\) is odd then \(f_{p,k}(0)=1\) and \(f_{p,k}(1)=3\). At \(p=3\), \(X-1\) divides \(f_{3,k}\) and every \(X^m-1\), proving persistent positive nullity. At any prime \(p\ne3\), no root of \(f_{p,k}\) is \(0\) or \(1\). All its roots lie in a finite extension of \(\mathbb F_p\) and have finite multiplicative orders greater than one. Let \(L\) be the least common multiple of those orders. For arbitrarily large \(m\equiv1\pmod L\), no root also solves \(X^m=1\), hence the gcd is \(1\); for arbitrarily large multiples of \(L\), at least one root is common. This proves both infinite families without requiring any roots to be simple.

**5. Two different valuation staircases.** At \(k=5\), direct polynomial identities give
\[
 f_{2,5}(X)=(X^2+X+1)^3,\qquad
 f_{3,5}(X)=(X-1)^2(X^2+1)^2.
\]
The factor \(X^2+X+1\) consists of primitive third roots in characteristic two; it divides \(X^m-1\) iff \(3\mid m\), with common multiplicity \(\min\{3,2^{v_2(m)}\}\). Over \(\mathbb F_3\), the factor \(X-1\) always occurs, while the two primitive fourth roots from \(X^2+1\) occur iff \(4\mid m\). Their common multiplicity is \(\min\{2,3^{v_3(m)}\}\). Taking degrees establishes both closed formulas and examples.

## Verification

The standalone script `verify.py` constructs all generalized Petersen edges directly, forms the stated cut, and row-reduces its matrix over \(\mathbb F_p\). Separately, it performs polynomial Euclidean gcd arithmetic modulo \(p\), comparing the predicted rank without using the block-matrix formula in the graph construction. It passed \(1740\) direct graph-rank/gcd comparisons for primes \(2,3,5,7\), \(2\le m\le30\), and every \(1\le k<m\). It also checked both \(k=5\) valuation formulas for \(6\le m<300\). Optional direct state-coefficient singular-value tests at five small instances passed, with largest absolute spectral error \(5.56\times10^{-17}\). Run `python verify.py --spectra` after installing the single listed dependency in `requirements.txt`. Finite checks are corroboration; the preceding argument is the proof for all allowed parameters.

## Relationship to prior work

Hein, Eisert and Briegel's general graph-state theorem reduces bipartite entanglement to finite-field adjacency rank for qubits [1]. Looi, Yu, Gheorghiu and Griffiths give the prime-dimensional controlled-phase graph-state construction [2]. Gera and Stănică derive the ordinary complex adjacency spectrum of generalized Petersen graphs using circulant blocks [3]. Wu, Kampermann and Bruß provide a distinct graph-state Schmidt-decomposition method via X-chains [4]. These methods motivate the exact problem but do not evaluate this alternating-layer cut over arbitrary prime characteristics, account for repeated cyclic roots, or identify the two valuation-dependent \(k=5\) spectra. The complex adjacency eigenvalues in [3] alone do not determine the rank of the cut block over fields whose characteristic divides the circumference. General block-rank methods are acknowledged; the specific all-parameter prime-dependent evaluation is the assessed contribution.

## Limitations

The theorem covers only the stated balanced cut, unit-weight interactions, pure states and prime local dimensions. It does not classify arbitrary bipartitions, composite qudits, nonuniform edge weights or noisy operations. Although the rank drops are exact and motivate finite-size entanglement resource comparisons, no claim is made about preparation complexity, quantum advantage or experimental robustness. The historical novelty assessment remains subject to specialized modular-circulant and quantum-network literature beyond the inspected works.

## References

[1] M. Hein, J. Eisert, H. J. Briegel, *Multi-party entanglement in graph states*, arXiv:quant-ph/0307130 (first publicly submitted 2003-07-18), https://arxiv.org/abs/quant-ph/0307130.

[2] S. Y. Looi, L. Yu, V. Gheorghiu, R. B. Griffiths, *Quantum Error Correcting Codes Using Qudit Graph States*, arXiv:0712.1979 (first publicly submitted 2007-12-12), https://arxiv.org/abs/0712.1979.

[3] R. Gera and P. Stănică, *The spectrum of generalized Petersen graphs*, Australasian Journal of Combinatorics 49 (2011), 39–45, https://ajc.maths.uq.edu.au/pdf/49/ajc_v49_p039.pdf.

[4] J.-Y. Wu, H. Kampermann, D. Bruß, *Group structures and representations of graph states*, arXiv:1504.03302 (2015), https://arxiv.org/abs/1504.03302.
