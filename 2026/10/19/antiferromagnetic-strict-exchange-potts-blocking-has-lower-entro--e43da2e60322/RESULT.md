# Antiferromagnetic strict-exchange Potts blocking has lower entropy than ferromagnetic blocking at every alphabet size

## Finding
For every integer \(q\ge3\), consider all labelled periodic \(q\)-colour configurations of length \(N\ge4\), with only swaps of *unequal* adjacent colours that strictly reduce the nearest-neighbour Potts energy. In the antiferromagnet \(H_A=J\sum_i\mathbf1\{s_i=s_{i+1}\}\), write \(B^A_{N,q}\) for the number of blocked configurations. In the ferromagnet \(H_F=-J\sum_i\mathbf1\{s_i=s_{i+1}\}\), write \(B^F_{N,q}\) for the analogous count (\(J>0\)).

Both have exact triple-state transfer enumerations \(B^\bullet_{N,q}=\operatorname{tr}((T^\bullet_q)^N)\). Their entropy growth constants are respectively the Perron roots \(\lambda_A(q)\) and \(\lambda_F(q)\) of
\[
 p_A(t)=t^4-qt^3+(q-1)t^2-(q-1)t+(q-1)(q-2),
\]
\[
 p_F(t)=t^4-(q-1)t^3-t^2-(q-1)t+(q-1)(q-2).
\]
The central comparison is the strict all-alphabet inequality
\[
 0<\lambda_A(q)<\lambda_F(q)<q,\qquad
 \lim_{N\to\infty}N^{-1}\log B^\bullet_{N,q}=\log\lambda_\bullet(q).
\]
Moreover, \(B^\bullet_{N,q}=\lambda_\bullet(q)^N(1+o(1))\) for each fixed \(q\ge3\). Thus the antiferromagnetic blocked-state count is exponentially smaller than the ferromagnetic count despite the configurations blocked under the two energies being incomparable sets. For \(q=3\), \(\lambda_A(3)=2.359304085971775\ldots\) is the largest root of \(t^3-2t^2-2\), whereas \(\lambda_F(3)=2.573271963535197\ldots\).

## Assumptions and scope
Sites are indexed cyclically modulo \(N\); colours are labelled and all \(q^N\) words are considered, with no fixed colour-population constraint. A proposed exchange at neighbouring unequal sites is accepted if and only if it strictly decreases energy. Equal-colour swaps do nothing; energy-neutral swaps are not accepted. The results concern the *set* of blocked words, not their dynamical sampling weights. No randomness is needed to define this set. The coupling magnitude \(J>0\) does not affect it.

## Proof
Let \((a,b,c,d)\) be four consecutive colours and exchange the middle two if \(b\ne c\). All unaffected bonds cancel, and the antiferromagnetic energy change divided by \(J\) is exactly
\[
 \Delta_A(a,b,c,d)=[a=c]+[b=d]-[a=b]-[c=d].
\]
The ferromagnetic change is \(-J\Delta_A\). Hence the antiferromagnetic blocked local condition is \(\Delta_A\ge0\), while the ferromagnetic one is \(\Delta_A\le0\), whenever \(b\ne c\). Both conditions hold automatically for \(b=c\). Here \([P]\) is \(1\) if \(P\) holds, \(0\) otherwise.

Define \(T^A_q\) and \(T^F_q\) on all \(q^3\) ordered triples of colours. Set the entry from \((a,b,c)\) to \((b,c,d)\) to one precisely when the appropriate local condition above holds, and all other entries to zero. A closed length-\(N\) walk in this order-three de Bruijn graph specifies exactly one labelled cyclic word of length \(N\), with all four-site windows checked. Thus the stated exact trace formulas hold for every \(N\ge4\).

Identify triples by the equality patterns \(000,001,010,011,012\), where labels are assigned in order of first appearance. Colour-permutation symmetry makes these patterns an equitable partition. The five-state row-sum quotients, in that order, are
\[
Q_A=\begin{pmatrix}
1&q-1&0&0&0\\
0&0&1&0&0\\
0&0&1&1&q-2\\
1&q-1&0&0&0\\
0&0&1&0&q-2
\end{pmatrix},\qquad
Q_F=\begin{pmatrix}
1&q-1&0&0&0\\
0&0&1&1&q-2\\
0&0&0&1&0\\
1&q-1&0&0&0\\
0&0&0&1&q-2
\end{pmatrix}.
\]
Direct determinant expansion yields \(\det(tI-Q_A)=t p_A(t)\) and \(\det(tI-Q_F)=t p_F(t)\). Because each quotient Perron eigenvector lifts to a strictly positive eigenvector for the full transfer matrix, its Perron root equals that of the full matrix, once irreducibility has been established.

We now establish primitivity, including for the full (not merely quotient) matrices. From any triple \((a,b,c)\) with \(b\ne c\), in the antiferromagnet append \(d=b\), whose energy change is \(1+[a=c]-[a=b]\ge0\). This gives \((b,c,b)\); appending \(b\) again produces \((c,b,b)\) with energy change zero; appending another \(b\) gives the uniform triple \((b,b,b)\). In the ferromagnet, append \(d=c\) directly: the change is \([a=c]-[a=b]-1\le0\), giving \((b,c,c)\); appending \(c\) gives the uniform triple \((c,c,c)\). Triples with the last two colours already equal similarly reach a uniform triple immediately.

All uniform triples communicate. For either sign, from \((r,r,r)\) append a different colour \(z\). In the ferromagnet append \(z,z\) again, yielding \((z,z,z)\). In the antiferromagnet append \(r,z,z,z\) in that order, yielding \((z,z,z)\) through changes \(0,+2,0\), followed by an equal-middle step. The four-site swap condition is invariant under reversing the four colours. Thus reversal maps every directed transition to another directed transition in reverse order, with the triple coordinates reversed. Since every triple can reach some uniform triple and all uniform triples communicate, reversal shows that any fixed uniform triple can reach every triple. The graph is therefore strongly connected. A uniform triple also has a self-loop, so each transfer matrix is primitive.

Perron--Frobenius theory now gives \(\operatorname{tr}((T_q^\bullet)^N)=\lambda_\bullet^N(1+o(1))\), because the leading eigenvalue is simple and all other eigenvalues have strictly smaller modulus. Each \(Q_\bullet\) has row sums at most \(q\), with at least one strictly smaller than \(q\); irreducibility and the strict Collatz--Wielandt comparison imply \(\lambda_A<q\) and \(\lambda_F<q\).

The decisive polynomial identity is
\[
 p_A(t)-p_F(t)=t^2(q-t).
\]
At \(t=\lambda_A\), we have \(p_A(t)=0\), so \(p_F(\lambda_A)=-\lambda_A^2(q-\lambda_A)<0\). Since \(p_F(t)\to+\infty\) as \(t\to+\infty\), it has a real root \(r>\lambda_A\). This root is an eigenvalue of \(Q_F\), so its Perron root satisfies \(\lambda_F\ge r>\lambda_A\). This completes the proof of the strict entropy comparison.

For \(q=3\), the factorization \(p_A(t)=(t-1)(t^3-2t^2-2)\) identifies the indicated positive root. An independent finite-size refinement follows from factoring the full \(27\)-state transfer characteristic polynomial:
\[
\det(tI-T^A_3)=t^{13}(t-1)(t^3-2t^2-2)(t^5-t^3-2t^2-t-3)^2.
\]
For every positive integer \(N\), the exact trace is \(1+\sum_{t^3-2t^2-2=0}\alpha^N+2\sum_{t^5-t^3-2t^2-t-3=0}\beta^N\), where the sums run over complex roots with multiplicity and \(\alpha\) and \(\beta\) denote the respective roots. For the physically relevant rings \(N\ge4\), this is the exact antiferromagnetic blocked count.

## Verification
The standalone `verify.py` independently enumerates spin words, computes energy changes by explicitly swapping positions in complete cyclic words, builds the triple-state graph, checks pattern lumpability, verifies the two all-\(q\) symbolic characteristic polynomials and their identity, checks connectivity for \(3\le q\le7\), and computes the full \(q=3\) characteristic polynomial. Its finite-volume antiferromagnetic counts for \(N=4,5,6,7,8,9,10,11,12\) are \(45,123,213,507,1149,2529,5919,13467,31329\). Direct exhaustive comparisons with transfer-matrix traces are made for \(q=3, N\le9\), \(q=4, N\le7\), and \(q=5, N\le6\), including both energy signs. These finite checks are corroborative; the proof of the all-\(q\), all-\(N\) statements is analytic. Run `python verify.py` after installing SymPy from `requirements.txt`.

## Relationship to prior work
De Smedt, Godrèche, and Luck (2002) developed blocked-state statistics for constrained ferromagnetic Ising chains, including constrained Kawasaki dynamics. Gómez Albarracín, Rosales, and Grynberg (2016) studied metastable one-dimensional Kawasaki dynamics with Ising spins and competing couplings. These works motivate the blocked-state observable and its local move rule but treat different spin alphabets/interactions from the general \(q\)-colour antiferromagnetic comparison proved here. Ferromagnetic Potts blocked-state enumeration is the natural sign-reversed comparator, not a proof of the antiferromagnetic claim: the accepted local inequalities reverse, and for example the cyclic word \(0101\) is antiferromagnetically blocked but not ferromagnetically blocked, whereas \(0011\) has the reverse property. The comparison theorem quantifies the resulting exponential asymmetry.

## Limitations
The statement is restricted to one-dimensional periodic nearest-neighbour chains, integer \(q\ge3\), length \(N\ge4\), and strictly decreasing unequal-neighbour swaps. It counts all colour populations jointly and does not determine blocked counts at a fixed population vector. Energy-neutral exchanges, if permitted dynamically, alter absorption. No claim is made for dynamical sampling probabilities, rates of approach to jammed states, arbitrary graph interactions, or independent certification. Unindexed or differently formulated equivalent results may exist.

## References
1. G. De Smedt, C. Godrèche, J. M. Luck, *Jamming, freezing and metastability in one-dimensional spin systems* (2002), arXiv:cond-mat/0202465, https://arxiv.org/abs/cond-mat/0202465.
2. F. A. Gómez Albarracín, H. D. Rosales, M. D. Grynberg, *Metastable and scaling regimes of a one-dimensional Kawasaki dynamics* (2016), arXiv:1601.04375, https://arxiv.org/abs/1601.04375.
