# Sharp quadratic waiting-time law for antipodal quantum transport on the icosahedron

## Finding
Let \(A\) be the ordinary unweighted adjacency matrix of the 12-vertex icosahedral graph, \(J>0\), and \(u,v\) its antipodal (distance-three) vertices. Define \(U(t)=e^{-iJtA}\), \(F(t)=|\langle v,U(t)u\rangle|^2\), and the optimal fidelity up to time \(T\) by \(F_*(T)=\max_{0\le t\le T}F(t)\). Then there is no finite-time perfect transfer, but for every \(T\ge\pi/J\),
\[
\frac{1}{324(1+JT)^2}\le1-F_*(T)\le\frac{5\pi^4}{2(JT)^2}.
\]
In particular the best achievable infidelity is \(\Theta((JT)^{-2})\), not merely tending to zero. Explicit high-fidelity times are \(t_k=\pi p_k/J\), where positive integers \(n_k,p_k\) satisfy \(n_k+p_k\sqrt5=(2+\sqrt5)^k\). At these times
\[
F(t_k)=\cos^4\!\left(\frac{\pi}{2(n_k+\sqrt5p_k)}\right),\qquad
\lim_{k\to\infty}(Jt_k)^2[1-F(t_k)]=\frac{\pi^4}{40}.
\]
The result applies simultaneously to all six antipodal pairs by graph symmetry. The Pell times are explicit witnesses but are not claimed to be the globally earliest or optimal transfer times at fixed fidelity.

## Assumptions and scope
The graph is the ordinary simple icosahedral graph with 12 vertices and 30 edges. The dynamics is one excitation with Hermitian nearest-neighbor hopping of the same strictly positive strength \(J\) on every edge; there is no on-site potential, longer-range hopping, dephasing, or loss. Time \(t\ge0\) is continuous. We use probability fidelity, not amplitude fidelity. The graph's antipodal map \(P\) sends each vertex to its unique vertex at distance three. No thermodynamic-limit or noisy-channel conclusion is asserted.

## Proof
**Spectral reduction.** Distance-regularity gives intersection array \(\{5,2,1;1,2,5\}\). Let \(A_2\) be the distance-two matrix. Exact path counting yields
\[
A^2=5I+2A+2A_2,\qquad
10P=A^3-4A^2-5A+10I,
\]
with \(P^2=I\) and \(PA=A_2\). The adjacency eigenvalues \(5,-1,\sqrt5,-\sqrt5\) have respective multiplicities \(1,5,3,3\); by the displayed polynomial, \(P\) is \(+1\) on the first two eigenspaces and \(-1\) on the last two. Vertex-transitivity makes the diagonal spectral projector weights equal to multiplicity divided by twelve. Consequently, with \(x=Jt\),
\[
a(x):=\langle v|e^{-ixA}|u\rangle=\frac{e^{-5ix}+5e^{ix}-6\cos(\sqrt5x)}{12}.
\]
This is an *exact* amplitude for all nonnegative real times.

**No perfect transfer and the lower fidelity bound.** Express the amplitude as a convex combination of unit phases
\[
c_1=e^{-5ix},\quad c_2=e^{ix},\quad c_3=-e^{-i\sqrt5x},\quad c_4=-e^{i\sqrt5x}
\]
with weights \(w_1=1/12,w_2=5/12,w_3=w_4=1/4\). The weighted variance identity is
\[
\varepsilon(x):=1-|a(x)|^2=\sum_{j<k}w_jw_k|c_j-c_k|^2.
\]
Equality \(\varepsilon=0\) would force the four phases equal. The pair \(c_3,c_4\) then forces \(\sqrt5x=\pi n\), \(n\in\mathbb Z\), and \(c_2=c_3\) forces \(e^{ix}=(-1)^{n+1}\), hence \(x=\pi p\), \(p\in\mathbb Z\). The irrationality of \(\sqrt5\) forces \(n=p=0\), at which \(c_2\ne c_3\). Thus \(\varepsilon(x)>0\) for all finite \(x\ge0\).

We now prove the quantitative estimate. From the two pairs \((c_3,c_4)\) and \((c_2,c_3)\),
\[
\varepsilon\ge\frac14\sin^2(\sqrt5x),\qquad
\varepsilon\ge\frac5{48}|e^{ix}+e^{-i\sqrt5x}|^2.
\]
If \(\varepsilon\le1/256\), choose \(n\ge0\) with \(|\sqrt5x-\pi n|\le\pi\sqrt\varepsilon\): indeed the first inequality bounds the sine by \(2\sqrt\varepsilon\), and \(\arcsin(2\sqrt\varepsilon)\le\pi\sqrt\varepsilon\). Set \(L=\pi+\sqrt{48/5}<6.25\). The second inequality and triangle inequality show
\[
|e^{ix}-(-1)^{n+1}|\le L\sqrt\varepsilon.
\]
The nearest angle of the appropriate parity supplies a nonnegative integer \(p\), opposite in parity to \(n\), with \(|x-\pi p|\le(\pi L/2)\sqrt\varepsilon\), using the elementary chord bound \(|\theta|\le(\pi/2)|e^{i\theta}-1|\) for \(|\theta|\le\pi\). Thus, writing \(K=1+\sqrt5L/2<9\),
\[
|\sqrt5p-n|\le K\sqrt\varepsilon<9\sqrt\varepsilon,
\quad \sqrt5p+n\le(2\sqrt5/\pi)x+K\sqrt\varepsilon\le2(1+x).
\]
Since \(p,n\) have opposite parity, \(n^2-5p^2\) is a nonzero integer. Therefore
\[
9\sqrt\varepsilon> |\sqrt5p-n|=\frac{|5p^2-n^2|}{\sqrt5p+n}\ge\frac1{2(1+x)},
\]
and hence \(\varepsilon(x)\ge1/[324(1+x)^2]\). If \(\varepsilon>1/256\), the same lower estimate is automatic since \(1/256>1/324\). The inequality holds pointwise for all \(x\ge0\), so also for the optimal fidelity over \(0\le t\le T\).

**Explicit Pell times and upper bound.** Expanding \((2+\sqrt5)^k\) gives positive integers \(n_k,p_k\) satisfying \(n_k^2-5p_k^2=(-1)^k\) and opposite parity. At \(x_k=\pi p_k\), the exact amplitude above simplifies to
\[
F(t_k)=\cos^4\!\left(\frac{\pi}{2(n_k+\sqrt5p_k)}\right),
\]
using \(|\sqrt5p_k-n_k|=1/(n_k+\sqrt5p_k)\). The elementary bound \(1-\cos^4 y\le2y^2\) implies
\[
1-F(t_k)\le\frac{\pi^2}{10p_k^2}.
\]
Moreover \(p_1=1\) and \(p_{k+1}=n_k+2p_k<5p_k\). For any \(X=JT\ge\pi\), choose the largest \(k\) with \(\pi p_k\le X\). Then \(p_k>X/(5\pi)\), giving \(1-F_*(T)\le1-F(t_k)\le5\pi^4/(2X^2)\). Finally \(n_k/p_k\to\sqrt5\) and \(1-\cos^4 y\sim2y^2\), which gives the stated \(\pi^4/40\) asymptotic coefficient along these times.

## Verification
The standalone `checker.py` constructs the icosahedral graph, verifies the distance-algebra identities by exact integer matrix arithmetic, and numerically compares the displayed amplitude with a separately implemented matrix exponential at seven times. It checks seven Pell pairs and 20,001 sampled lower-bound times, with further horizon comparisons. Run `python3 checker.py` using Python 3 and its standard library. All checks passed; the universal inequalities and asymptotic conclusion follow from the written exact proof, not the finite samples. The checker output is preserved in `checker_output.txt`.

## Relationship to prior work
Jafarizadeh and Sufiani (2007), Appendix, explicitly analyze the icosahedron's distance-regular spectrum and construct **perfect transfer with engineered couplings in several distance shells**, including a nonzero antipodal coupling. This result uses **only the ordinary nearest-neighbor adjacency Hamiltonian**; it makes no novelty claim for the graph spectrum or the general distance-regular framework. Godsil, Kirkland, Severini and Smith (2012) classify pretty-good transfer for unmodulated paths; the spectrum's number-theoretic role is known. Vinet and Zhedanov (2012) study almost-perfect transfer in mirror-symmetric chains. The contribution assessed here is a graph-specific constructive Pell protocol together with a two-sided, all-continuous-time, sharp-exponent fidelity-versus-waiting-time law. Searches of related primary literature and mathematical research records did not identify its exact statement, but absence from search is not proof of priority.

## Limitations
The upper and lower constants are not matched; hence a sharp asymptotic constant for the **globally optimized** fidelity is not claimed. Pell times are not proven to be individually optimal. Some relevant quantum-transfer papers were accessible only in abstract form; historical priority requires further independent examination. The theorem does not address noise, energy disorder, interactions, multi-excitation transfer, readout constraints or finite-temperature physics. Independent scientific validation has not been performed.

## References
- M. A. Jafarizadeh and R. Sufiani, *Perfect state transfer over distance-regular spin networks* (first publicly posted 2007-09-05), https://arxiv.org/abs/0709.0755 (especially the icosahedron appendix).
- C. Godsil, S. Kirkland, S. Severini and J. Smith, *Number-Theoretic Nature of Communication in Quantum Spin Systems* (first publicly posted 2012-01-23), https://arxiv.org/abs/1201.4822.
- L. Vinet and A. Zhedanov, *Almost perfect state transfer in quantum spin chains* (first publicly posted 2012-05-21), https://arxiv.org/abs/1205.4680.
