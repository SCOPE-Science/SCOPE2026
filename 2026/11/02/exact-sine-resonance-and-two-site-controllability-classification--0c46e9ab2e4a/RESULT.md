# Exact sine-resonance and two-site controllability classification for coprime directed tori

## Finding

For every pair of coprime integers \(m,n\ge3\), a two-dimensional Cartesian product of uniformly directed cycles with strictly positive direction rates \(a,b\) has an entirely explicit node-controllability classification. Write \(q=b/a\) and define the finite set

\[
\mathcal R_{m,n}=\left\{\frac{\sin(2\pi r/m)}{\sin(2\pi s/n)}:\ 1\le r<m/2,\ 1\le s<n/2,\ r,s\in\mathbb Z\right\}.
\]

Every eigenvalue of its directed Laplacian has multiplicity at most two. Its spectrum is simple precisely when \(q\notin\mathcal R_{m,n}\). At a resonant value, each repeated eigenvalue is real and has exactly the two Fourier indices \((r,n-s)\) and \((m-r,s)\) for one pair \((r,s)\) realizing that ratio; distinct realizing pairs give distinct eigenvalues.

A separate scalar control at any one vertex renders the system Kalman-controllable exactly when \(q\notin\mathcal R_{m,n}\). At resonance, one such input is insufficient, whereas any two vertices adjacent along either coordinate direction suffice. More generally, two independent node inputs at distinct vertices with cyclic displacement \((u,v)\) render the system controllable precisely when

\[
\forall(r,s)\text{ with }\frac{\sin(2\pi r/m)}{\sin(2\pi s/n)}=q:\quad
(m\nmid 2ru)\ \text{or}\ (n\nmid 2sv).
\]

Thus the exact minimum number of independent node actuators is one outside the finite resonance set and two on it. In particular, when \(a=b\), one input at any vertex always suffices for coprime \(m,n\ge3\). If both lengths are odd primes, every two distinct vertices suffice even at resonance. These statements hold for every real positive rate pair, not merely generic choices.

## Assumptions and scope

The state space has one real scalar state per vertex in \(\mathbb Z_m\times\mathbb Z_n\). Let \(P_d\) be the permutation matrix shifting coordinates once clockwise on \(\mathbb Z_d\), and put

\[
L=a(I_m-P_m)\otimes I_n+bI_m\otimes(I_n-P_n),\qquad a,b>0.
\]

Dynamics are \(\dot x=-Lx+B_Uu\), with each column of \(B_U\) a distinct standard basis vector at an independently actuated vertex. Controllability means full Kalman rank over \(\mathbb R\), equivalently the complex Popov–Belevitch–Hautus test. The two cycle lengths must be coprime and both at least three. There are no additional edges, and rates within each coordinate direction are uniform. The directed Laplacian is normal but, in general, not symmetric.

## Proof

**Fourier diagonalization.** Put \(\zeta_d=\exp(2\pi i/d)\). A unitary Fourier basis consists of vectors with entries proportional to \(\zeta_m^{jx}\zeta_n^{ky}\), where \((j,k)\in\mathbb Z_m\times\mathbb Z_n\). Depending on whether the shift convention acts forward or backward, indices may be simultaneously negated; this has no effect on the conclusions. Fix the convention in which the corresponding Laplacian eigenvalue is

\[
\lambda_{j,k}=a(1-\zeta_m^j)+b(1-\zeta_n^k).
\]

**Complete collision classification.** Suppose \(\lambda_{j,k}=\lambda_{j',k'}\) for distinct index pairs. Since roots of unity in either factor are distinct, necessarily \(j\ne j'\) and \(k\ne k'\). Rearrangement gives

\[
a(\zeta_m^j-\zeta_m^{j'})=-b(\zeta_n^k-\zeta_n^{k'}).
\]

The chord-difference identity

\[
\zeta_d^h-\zeta_d^\ell=2i\exp(\pi i(h+\ell)/d)\sin(\pi(h-\ell)/d)
\]

has a nonzero real sine factor here. Therefore the two chord directions are parallel, so \((j+j')/m-(k+k')/n\in\mathbb Z\). Multiplying by \(mn\), reducing modulo each of the coprime lengths, and using \(1\le j+j'\le2m-3\) and \(1\le k+k'\le2n-3\) yields

\[
j+j'=m,\qquad k+k'=n.
\]

Consequently the two indices must be opposite nontrivial conjugates within *both* cycles. Write their unique representatives as \((r,n-s)\), \((m-r,s)\), with \(1\le r<m/2\), \(1\le s<n/2\). Equality of their imaginary parts is exactly \(a\sin(2\pi r/m)=b\sin(2\pi s/n)\), or \(q\in\mathcal R_{m,n}\) at the indicated pair. Conversely this equality causes the claimed collision. The common eigenvalue is real. Each index is paired with only its unique conjugate, so a third coincident Fourier mode is impossible; multiple pairs realizing the same price ratio yield distinct repeated eigenvalues. This proves simplicity off resonance, multiplicity exactly two at resonance, and the first assertion.

**One- and two-site PBH test.** Since \(L\) is normal, the PBH condition is full row rank of the Fourier eigenvector evaluations on the chosen input vertices within each eigenspace. Each Fourier vector has nonzero amplitude at every vertex. Thus every single input works for simple spectrum, while no single input can span the evaluation space of a repeated eigenvalue.

Translate the first input to \((0,0)\), and write the other as \((u,v)\). For the repeated modes \((r,n-s)\), \((m-r,s)\), their two-by-two evaluation matrix, up to harmless complex conjugation of all entries, has rows proportional to

\[
\begin{pmatrix}
1&\zeta_m^{ru}\zeta_n^{-sv}\\
1&\zeta_m^{-ru}\zeta_n^{sv}
\end{pmatrix}.
\]

Its determinant vanishes exactly when \(2ru/m-2sv/n\in\mathbb Z\). Coprimality makes this equivalent to the simultaneous divisibilities \(m\mid 2ru\) and \(n\mid2sv\). Requiring nonsingularity for every resonant pair is therefore necessary and sufficient for controllability. When \((u,v)=(1,0)\), \(0<2r<m\) prevents the first divisibility; similarly \((0,1)\) works. This proves the two-site classification and the exact minimum number of sites.

**Uniform-rate and prime-length consequences.** If \(q=1\) belonged to \(\mathcal R_{m,n}\), equality of two sines with angles in \((0,\pi)\) would imply either \(r/m=s/n\) or \(r/m+s/n=1/2\). The former contradicts coprimality and \(0<r<m\). The latter gives \(2nr+2ms=mn\), and hence \(m\mid2r\), contrary to \(0<2r<m\). Therefore \(1\notin\mathcal R_{m,n}\). If both cycle lengths are odd primes, the divisibilities \(m\mid2ru\) and \(n\mid2sv\) imply \(u=0\) and \(v=0\), respectively, so every pair of distinct vertices is controllable at resonance. The placement restriction is substantive for composite orders: with \(m=9\), \(n=5\) and \(q=\sin(2\pi/3)/\sin(2\pi/5)\), the two distinct vertices \((0,0)\) and \((3,0)\) fail the divisibility test, whereas \((0,0)\) and \((1,0)\) pass.

## Verification

The included `check_directed_tori.py` is a standalone supplementary checker requiring Python 3 and `mpmath`. Run `python check_directed_tori.py` in the extracted package directory. It verifies the coprime chord-direction modular lemma for all coprime orders from three through twenty-five; computes the complete eigenvalue collisions for 89 exact-formula resonance parameter instances; checks Fourier-eigenspace multiplicities, realness and the two-node arithmetic determinant criterion at all cyclic offsets in those instances; and checks the absence of equal-rate collisions. With 82-digit arithmetic it produces `PASS 4248701 deterministic checks across 89 resonant parameter samples and all coprime pairs through 25`. Finite numerical sampling is a consistency test, not a proof of the universal theorem; the preceding exact argument supplies that proof.

## Relationship to prior work

Notarstefano and Parlangeli (first public arXiv version 2012-03-01) analyze controllability of *undirected* Cartesian-product grid Laplacians and furnish the graph-product spectral framework, but their hypotheses and formulas are not this directed, two-rate coprime-torus classification. Chapman, Nabi-Abdolyousefi and Mesbahi (2014) establish general controllability criteria for Cartesian products and emphasize collisions of factor eigenvalue sums. Their general PBH method is prior and is used here; it does not, in the material inspected, list the precise sine-ratio resonance set or the all-pairs divisibility criterion. Nabi-Abdolyousefi and Mesbahi (2013) provide a broader circulant-network controllability theorem based on maximum eigenvalue multiplicity: the abstract already implies that the generic actuator-count principle is not novel. Here the specific spectral multiplicities are derived, and all two-site placements on the coprime two-generator family are classified. The complete 2013 text was not accessible, leaving an explicit priority risk as to whether it contains these formulas. Xiang and collaborators (2013) cover general weighted directed controllability; Liu and collaborators (2024) provide more recent general Cartesian-product conditions. No inspected applicable statement implied the exact arithmetic classification.

## Limitations

This theorem is restricted to two factors with coprime orders, uniform positive rates within each directed factor, and independent point inputs. No conclusion is asserted for noncoprime orders, nonuniform edge weights, three or more factors, or energy-optimal control. The 2013 specialist circulant full text and 2014 book-chapter coverage were not available for complete inspection, and overlap cannot be ruled out by search alone. The work has self-review only; independent audit and external priority verification have not been performed.

## References

1. G. Notarstefano and G. Parlangeli, *Controllability and Observability of Grid Graphs via Reduction and Symmetries*, arXiv:1203.0129 (first posted 2012-03-01). https://arxiv.org/abs/1203.0129
2. A. Chapman, M. Nabi-Abdolyousefi and M. Mesbahi, *Controllability and Observability of Network-of-Networks via Cartesian Products*, IEEE Transactions on Automatic Control 59 (2014), 2668–2679. DOI:10.1109/TAC.2014.2328757. https://www.researchgate.net/publication/265856026_Controllability_and_Observability_of_Network-of-Networks_via_Cartesian_Products
3. M. Nabi-Abdolyousefi and M. Mesbahi, *On the Controllability Properties of Circulant Networks*, IEEE Transactions on Automatic Control 58 (2013), 3179–3184. DOI:10.1109/TAC.2013.2259992. https://www.researchgate.net/publication/260662084_On_the_Controllability_Properties_of_Circulant_Networks
4. L. Xiang et al., *Controllability of Weighted and Directed Networks with Nonidentical Node Dynamics*, Mathematical Problems in Engineering (2013), article 405034. DOI:10.1155/2013/405034. https://doi.org/10.1155/2013/405034
5. B. Liu et al., *Discrete-Time Controllability of Cartesian Product Networks*, IEEE Transactions on Signal and Information Processing over Networks 10 (2024), 868–880. DOI:10.1109/TSIPN.2024.3487411. https://strathprints.strath.ac.uk/91217/
