# A weak staggered field changes the exact Kawasaki blocking entropy

## Finding
For every even ring length \(N=2m\ge4\), consider the ferromagnetic Ising Hamiltonian
\[
H(s)=-J\sum_{i=0}^{N-1}s_i s_{i+1}-h\sum_{i=0}^{N-1}(-1)^i s_i,
\qquad J>0,\quad 0<h<J,\quad s_i\in\{-1,+1\},
\]
with cyclic subscripts. At zero temperature, an antiparallel neighboring pair is exchanged whenever its exchange strictly lowers \(H\), and an equal-energy exchange would be permitted. In the stated open field interval no antiparallel exchange has zero energy change. Call a configuration *blocked* if no exchange is permitted. Let \(B_{2m}(z)\) count blocked configurations by their number of up-spins, with one monomial \(z^k\) for each configuration having exactly \(k\) up-spins.

Write \(u=1+z^2\), \(v=z+z^2+z^3\), and \(D(t,z)=1-u t-vt^2-z^5t^5\). The **complete finite-ring magnetization census** is
\[
\boxed{\sum_{m\ge2} B_{2m}(z)t^m
=\frac{ut+2vt^2+5z^5t^5}{D(t,z)}-ut.}
\]
In particular, the unweighted numbers \(a_m=B_{2m}(1)\) start
\[
(a_2,a_3,a_4,a_5,a_6)=(10,26,82,247,742)
\]
and obey \(a_m=2a_{m-1}+3a_{m-2}+a_{m-5}\) for every integer \(m\ge6\), with the auxiliary value \(a_1=2\).

Let \(\rho\) be the unique positive root of \(\rho^5-2\rho^4-3\rho^3-1=0\), so \(\rho\approx3.00915406482035\). The blocking entropy per physical spin is
\[
\boxed{\lim_{m\to\infty}\frac{\log B_{2m}(1)}{2m}
=\frac12\log\rho\approx0.550829498836637.}
\]
For the same Hamiltonian at **exactly zero** staggered field, with neutral Kawasaki moves still permitted, the entropy is instead \(\log((1+\sqrt5)/2)\approx0.481211825059603\). Thus the entropy of absorbing configurations has a strict upward jump when a positive staggered field is introduced, however small, while remaining below \(J\).

## Assumptions and scope
The ring is labeled, so translated configurations are counted separately. All magnetizations are included, and the polynomial above resolves their individual multiplicities. Temperature is zero in the standard positive-rate-on-energy-neutral convention; at positive field in the stated interval this convention agrees with the strict energy-decrease rule because neutral exchanges do not occur. Sites are labeled \(0,1,\dots,N-1\), the staggering is \((-1)^i\), and the initial spin configuration is arbitrary. The result is independent of positive choices of exchange rates on energy-decreasing moves. No field at or above \(J\), no positive-temperature law, and no distribution of dynamically selected blocked states are asserted.

## Proof
**1. Energy test and local classification.** Suppose \(s_i=b=-s_{i+1}\), and set \(a=s_{i-1}\), \(c=s_{i+1}\), \(d=s_{i+2}\). Direct subtraction of the Hamiltonians before and after exchanging positions \(i,i+1\) gives
\[
\Delta_i H=2Jb(a-d)+4h(-1)^i b.
\]
For \(0<h<J\), the sign is determined first by \(b(a-d)\in\{-2,0,2\}\). An antiparallel bond is therefore stable against an exchange precisely when
\[
\boxed{b(a-d)>0\quad\text{or}\quad
\bigl(a=d\ \text{and}\ (-1)^i b>0\bigr).}
\]
A parallel bond is always stable because no exchange is proposed. Equivalently, among four-spin words \((a,b,c,d)\) with the center at the bond \(i,i+1\), the four forbidden words for even \(i\) are \(\texttt{--+-},\texttt{-+-+},\texttt{+-+-},\texttt{+-++}\), and for odd \(i\) they are \(\texttt{-+--},\texttt{-+-+},\texttt{+-+-},\texttt{++-+}\). This gives an explicit if-and-only-if characterization for every ring length in scope. Every permitted exchange strictly lowers energy, so on a finite ring the zero-temperature chain eventually reaches a blocked state almost surely.

**2. Transfer graph.** Index the eight three-spin words \(q=(a,b,c)\in\{-1,+1\}^3\) in lexicographic order. For parity \(p\in\{0,1\}\), construct the \(8\times8\) matrix \(A_p(z)\) by placing \(z^{(1+b)/2}\) in row \((a,b,c)\), column \((b,c,d)\) whenever the local rule in step 1 permits the four-spin word at a bond of parity \(p\), and placing zero otherwise. The exponent is either zero or one. For \(N=2m\ge4\), closing a path of \(2m\) overlapping three-spin windows is equivalent to imposing cyclic consistency on exactly one length-\(2m\) spin configuration; the product assigns the weight of each site's spin exactly once. Consequently,
\[
B_{2m}(z)=\operatorname{tr}\bigl([A_0(z)A_1(z)]^m\bigr).
\]
This is a bijection, not an asymptotic or finite-enumeration heuristic. The two-step matrix encodes the alternating local energy rule without allowing any nonphysical transition.

**3. Exact determinant and generating series.** Direct multiplication of the explicitly defined eight-state matrices, followed by an ordinary determinant calculation, gives
\[
\det\bigl(xI-A_0(z)A_1(z)\bigr)
=x^3\bigl[x^5-(1+z^2)x^4-(z+z^2+z^3)x^3-z^5\bigr].
\]
Therefore \(\det(I-tA_0(z)A_1(z))=D(t,z)\). For an arbitrary finite square matrix \(T\), the formal identity
\[
\sum_{m\ge1}\operatorname{tr}(T^m)t^m
=-t\frac{d}{dt}\log\det(I-tT)
\]
follows either by the matrix geometric series or Newton's identities. Applying it to \(T=A_0(z)A_1(z)\) yields \((ut+2vt^2+5z^5t^5)/D(t,z)\). Its \(m=1\) coefficient is the formal transfer-graph trace \(u\); because physical two-site rings are outside the statement, subtracting \(ut\) gives exactly the displayed series starting at \(m=2\). For \(z=1\), the characteristic polynomial reduces to \(x^3(x^5-2x^4-3x^3-1)\), giving the coefficients and recurrence stated in the finding.

**4. Entropy and singular weak-field limit.** The polynomial \(f(x)=x^5-2x^4-3x^3-1\) has exactly one positive root by Descartes' rule of signs, and that root lies strictly above \(3\) since \(f(3)=-1\). If \(w\) is any root then \(|w|^5\le2|w|^4+3|w|^3+1\), which forces \(|w|\le\rho\); equality would require the phases of \(w^4\), \(w^3\), and \(1\) to coincide, hence \(w=\rho\). Thus \(\rho\) is the unique simple strictly dominant eigenvalue of the two-step matrix. Its power sum yields \(a_m=\rho^m(1+o(1))\), proving the entropy formula.

At exactly \(h=0\), an equal-energy swap is permitted. The absorbing configurations are then precisely those with no isolated spin, equivalently no cyclic occurrence of \(\texttt{+-+}\) or \(\texttt{-+-}\). Their two-spin-window transfer matrix has characteristic polynomial \((x^2-x-1)(x^2-x+1)\), with dominant root \((1+\sqrt5)/2\). Hence their asymptotic entropy is the smaller value claimed. The difference is strict because \(\rho>3\), so \(\sqrt\rho>\sqrt3>(1+\sqrt5)/2\). The comparison uses the same neutral-exchange convention at both field values.

## Verification
Run `python3 verify.py` with Python 3 and SymPy. The script constructs the two parity transfer matrices from the local rule, verifies the characteristic polynomial and determinant symbolically, independently enumerates physical Hamiltonian energy-decrease moves at \(h/J=1/7\) and \(h/J=9/10\), and checks the full up-spin polynomial for ring lengths \(4,6,8,10,12\). It also checks the rational generating series through eight transfer powers. All assertions passed. The finite enumeration is only a diagnostic; the proof for all even lengths rests on the local bijection, determinant identity, and root argument.

## Relationship to prior work
De Smedt, Godrèche, and Luck studied the zero-field ferromagnetic Kawasaki chain and determined both the freely diffusing zero-energy-move regime and the fully constrained regime. Their full text identifies the respective forbidden local patterns and the golden-mean entropy for the former; a parity-dependent weak staggered field and its quintic magnetization-resolved census are not treated there. Gómez Albarracín, Rosales, and Grynberg analyzed Kawasaki metastability from first- and second-neighbor couplings; their proliferation table and Appendix A treat spatially uniform coupling classes and do not imply this alternating on-site-field constraint. The present result does not claim priority for the general transfer-matrix technique, the zero-field golden-mean law, or those previously studied coupling classes.

## Limitations
The field interval is open and exact: at \(h=0\) neutral moves return, and at \(h=J\) additional degeneracies enter. The theorem enumerates dynamically absorbing states, not their hitting probabilities or the Edwards measure sampled after a quench. Numerical verification is finite; no infinite-family fact is inferred solely from checked lengths. An earlier source studying precisely parity-dependent exchange kinetics under an alternative lattice-gas description could exist despite the targeted literature comparison. Independent scientific validation has not been performed.

## References
1. G. De Smedt, C. Godrèche, and J. M. Luck, *Metastable states of the Ising chain with Kawasaki dynamics*, arXiv:cond-mat/0210477, first public version 2002-10-22; https://arxiv.org/html/cond-mat/0210477v1.
2. F. A. Gómez Albarracín, H. D. Rosales, and M. D. Grynberg, *Metastable and scaling regimes of a one-dimensional Kawasaki dynamics*, arXiv:1601.04375, first public version 2016-01-18; https://arxiv.org/html/1601.04375v2.
3. K. Kawasaki, *Diffusion constants near the critical point for time-dependent Ising models. I*, Physical Review 145 (1966), 224–230, doi:10.1103/PhysRev.145.224 (background on magnetization-conserving spin exchange).
