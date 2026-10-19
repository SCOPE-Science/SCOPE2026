# All exponential spectra of prime-square digit-lift graphs

## Finding
For every prime \(p\ge5\), let \(R=\mathbb Z/p^2\mathbb Z\) and let \(h:\mathbb F_p\to\mathbb F_p\) be arbitrary. Interpret each field element by its representative in \(\{0,\ldots,p-1\}\) and set
\[
S_h=\{(r+ps,\,r+ph(r)):0\le r,s<p\}\subset R^2.
\]
The \(p^p\) different sets \(S_h\) have identical Fourier-transform zero sets and identical collections of orthogonal exponential spectra.

Precisely, if
\[
F_h(u,v)=\sum_{(x,y)\in S_h}\exp\!\left(\frac{2\pi i(ux+vy)}{p^2}\right),
\]
then
\[
F_h(u,v)=0\quad\Longleftrightarrow\quad
\left(p\nmid u\right)\ \text{or}\quad
\left(u=pU,\ v=pV,\ U+V\not\equiv0\pmod p\right).
\]

Every orthogonal exponential basis is indexed *uniquely* by a function \(c:\mathbb F_p\to\mathbb F_p\) and a family of functions \(A_a:\mathbb F_p\to\mathbb F_p\), one for each \(a\in\mathbb F_p\):
\[
\Lambda_{c,A}=\bigcup_{a\in\mathbb F_p}
\bigl\{\bigl(a+pA_a(t),\ c(a)+p[t-A_a(t)]\bigr):t\in\mathbb F_p\bigr\}.
\]
Arithmetic inside brackets is modulo \(p\); both displayed frequency coordinates are elements of \(R\). Thus every \(S_h\) has exactly
\[
\boxed{p^{p^2+p}}
\]
distinct frequency spectra, of which precisely \(p^4-p^3\) are affine cosets of order-\(p^2\) subgroups. Nonaffine spectra occur for every \(p\ge5\).

The family contains the Frobenius graph \(\{(x,x^p):x\in R\}\), obtained with \(h(r)=(r^p-r)/p\pmod p\).

## Assumptions and scope
The prime \(p\) is any prime at least five. All arithmetic is in \(R\) except the index functions and digit differences, which are modulo \(p\). Fourier characters are unnormalized; multiplying the mask by a fixed nonzero normalization does not affect its zeros. A frequency spectrum means a subset of \(R^2\) of cardinality \(|S_h|=p^2\) whose restricted characters form an orthogonal basis of functions on \(S_h\), with counting inner product. Different translates of frequency sets count as different spectra. There are no assumptions on \(h\).

## Proof
**1. Cyclotomic zero criterion.** Put \(\zeta=\exp(2\pi i/p^2)\). For any integers \(n_j\), the sum \(\sum_{j=0}^{p^2-1}n_j\zeta^j\) vanishes if and only if, for every \(r\in\{0,\ldots,p-1\}\), the \(p\) coefficients \(n_{r},n_{r+p},\ldots,n_{r+(p-1)p}\) are equal. Indeed \(\Phi_{p^2}(z)=1+z^p+\cdots+z^{(p-1)p}\) is the irreducible polynomial of \(\zeta\), and any integer polynomial of degree less than \(p^2\) divisible by \(\Phi_{p^2}\) has quotient of degree less than \(p\). This proves the stated coefficient pattern in both directions.

**2. Fourier zero set.** Summing first over \(s\) yields
\[
F_h(u,v)=\left(\sum_{s=0}^{p-1}e^{2\pi ius/p}\right)
\left(\sum_{r=0}^{p-1}\zeta^{(u+v)r+pv h(r)}\right).
\]
If \(p\nmid u\), the first factor vanishes. If \(u=pU\) and \(v=pV\), the second factor is \(\sum_r e^{2\pi i(U+V)r/p}\), which vanishes precisely when \(U+V\not\equiv0\pmod p\). If \(u=pU\) but \(v\) is a unit, then the \(p\) exponents \((pU+v)r+pv h(r)\), reduced modulo \(p^2\), lie in pairwise different classes modulo \(p\), because their residues are \(vr\pmod p\). Thus the corresponding root-of-unity polynomial has exactly one coefficient equal to one in each residue class modulo \(p\), the other \(p-1\) coefficients being zero. By Step 1 it cannot vanish. The displayed complete zero characterization follows, and it is independent of \(h\).

**3. Classification of bases.** Distinct restricted characters with frequencies \(\lambda,\mu\) are orthogonal exactly when \(F_h(\lambda-\mu)=0\). Partition any pairwise orthogonal frequency set by the first-coordinate residue \(a=u\pmod p\). Within such a group, all second-coordinate residues must agree: otherwise a pair difference has \(p\mid\Delta u\) and \(p\nmid\Delta v\), which Step 2 excludes. Call the common second residue \(c(a)\). Write the frequencies in this group as \((a+pU,c(a)+pV)\). Two distinct group members are orthogonal precisely when their \(U+V\pmod p\) values differ. Hence each group has at most \(p\) members. There are at most \(p\) groups, and a spectrum must contain \(p^2\) distinct characters, so all groups have size \(p\) and, in each, the values \(t=U+V\) run through all of \(\mathbb F_p\). For each \(a,t\), put \(A_a(t)=U\); necessarily \(V=t-A_a(t)\). This is the claimed parametrization, and it is forced uniquely by the set. Conversely, distinct groups have differences in their first coordinates that are units modulo \(p\), while within a group distinct values of \(t\) ensure the second alternative in Step 2. Hence every displayed \(\Lambda_{c,A}\) is orthogonal and, having \(p^2\) elements, is a basis.

**4. Enumeration and affine spectra.** There are \(p^p\) possible functions \(c\) and \(p^{p^2}\) possible independent choices of the \(p\) functions \(A_a\), giving \(p^{p^2+p}\) spectra with no double counting. An affine spectrum \(\lambda_0+H\) with \(|H|=p^2\) must have first coordinates meeting every residue class modulo \(p\). Thus \(H\) has an element whose first coordinate is a unit, so it is cyclic of order \(p^2\) and is the graph \(H=\{(t,mt):t\in R\}\) for one \(m\in R\). The basis condition is \(1+m\not\equiv0\pmod p\), because two parameters differing by a nonzero multiple of \(p\) must produce a Fourier zero. Every such affine spectrum is \(\{(t,mt+n):t\in R\}\). There are \(p^2-p\) allowed slopes and \(p^2\) distinct vertical intercepts, so the exact affine count is \(p^4-p^3\). The choice \(c(a)=0\), \(A_a(t)=t^2\) gives a nonaffine spectrum, because distinct \(t\) and \(-t\) can produce the same first coordinate but different second coordinates.

**5. Frobenius specialization.** For \(x=r+ps\), the binomial theorem gives \(x^p\equiv r^p\pmod{p^2}\). Since \(r^p\equiv r\pmod p\), choosing \(h(r)=(r^p-r)/p\pmod p\) gives \(S_h=\{(x,x^p):x\in R\}\). Finally \(S_h\ne S_{h'}\) whenever \(h\ne h'\), as the second coordinate of any point with first-coordinate residue \(r\) recovers \(h(r)\). This completes the proof.

## Verification
Run `python3 CHECK.py` with Python 3 and no third-party libraries. It tests the entire mask zero set for multiple deterministic graph lifts at \(p=2,3,5,7\), verifies generated spectra by exact root-of-unity coefficient arithmetic, and exhaustively enumerates all four-frequency bases for all four lifts at \(p=2\). Its recorded output is in `CHECK_OUTPUT.txt`. The proof, not the finite computations, establishes the assertion for every prime \(p\ge5\) and every \(h\).

## Relationship to prior work
Fallon–Kiss–Somlai, *Spectral sets and tiles in \(\mathbb Z_p^2\times\mathbb Z_q^2\)* (first public 2021-05-21), develop finite-group spectral/tiling methods for **distinct** primes, not the repeated-prime ring graph family or the enumeration here. Zhou, *On Tiling and Spectral Sets in \(\mathbb Z_{p^2}\times\mathbb Z_{p^2}\)* (first public December 2024), proves a general spectral/tiling equivalence and studies Fourier zero structure, but the inspected theorems do not give this common zero-set identity or exact spectrum census. Existing exact spectra classifications for the quadratic and cubic graphs concern different spatial subsets and do not imply the displayed parametrization for all digit-lift graphs. Qualitative spectrality alone does not imply the exact enumeration.

## Limitations
The theorem treats exactly the prime-square digit-lift diagonal graphs defined above, not arbitrary polynomial graphs or higher prime powers. It counts labeled frequency subsets, not spectra modulo translation or ambient affine automorphisms. Spectral indistinguishability here means identical zero sets and hence identical collections of orthogonal exponential bases; it does not mean identical Fourier magnitudes or Fourier transforms. Bibliographic novelty is qualified by the possibility of an uncatalogued equivalent p-adic spectral classification. Independent audit has not been performed.

## References
1. T. Fallon, G. Kiss, G. Somlai, *Spectral sets and tiles in \(\mathbb Z_p^2\times\mathbb Z_q^2\)*, arXiv:2105.10575, first submitted 2021-05-21. https://arxiv.org/abs/2105.10575
2. W. Zhou, *On Tiling and Spectral Sets in \(\mathbb Z_{p^2}\times\mathbb Z_{p^2}\)*, arXiv:2412.18132, first submitted 2024-12-24. https://arxiv.org/abs/2412.18132
