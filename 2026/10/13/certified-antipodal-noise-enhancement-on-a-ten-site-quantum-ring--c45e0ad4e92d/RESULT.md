# Certified antipodal noise enhancement on a ten-site quantum ring

## Finding

Consider the ten-site cycle with vertices \(\mathbb Z/10\mathbb Z\), uniform coherent hopping of amplitude \(1\), an irreversible trap at vertex \(0\), and an initially localized excitation at its antipode, vertex \(5\). Take the uniform recombination parameter \(\mu=1/1000\) and trap parameter \(\kappa=30\), in the attenuation convention of Kassal and Aspuru-Guzik (2012). When the site-dephasing parameter increases from \(\gamma=0\) to \(\gamma=1/5\), the total eventual trapping probability strictly increases:

\[
\eta_{1/5}-\eta_0\;\ge\;\frac{1385039389500}{100000000000000}
=0.013850393895>0.
\]

In fact, the rigorous certificate gives \(0.8581335587454\le\eta_0\le0.8581337052390\) and \(0.8719840991340\le\eta_{1/5}\le0.8719842115788\). This supplies a concrete counterexample to the assertion in Section 3, Eq. (13), of Kassal and Aspuru-Guzik (2012) that the maximum environment-assisted transfer enhancement is zero whenever source and trap are opposite vertices of an ordered cycle. By continuity, the enhancement is also positive on a nonempty open neighborhood of the given strictly positive rates. No assertion about other ring lengths or global optimization is required.

## Assumptions and scope

Write \(|j\rangle\) for the vertex basis and
\[
H=\sum_{j=0}^{9}\bigl(|j\rangle\langle j+1|+|j+1\rangle\langle j|\bigr),
\qquad P=|0\rangle\langle0|,
\]
with indices modulo \(10\). The unnormalized network density matrix starts at \(\rho(0)=|5\rangle\langle5|\), and evolves by
\[
\dot\rho=-i[H,\rho]-2\mu\rho-\kappa\{P,\rho\}
-2\gamma\bigl(\rho-\operatorname{diag}(\rho)\bigr).
\]
This is the single-excitation attenuation/dephasing convention of the cited 2012 work: the trap population receives the non-Hermitian amplitude term \(-i\kappa P\), each vertex receives \(-i\mu\), and each off-diagonal density entry experiences the additional decay \(2\gamma\). The eventual useful trapping probability, not the total loss probability, is
\[
\eta_\gamma=2\kappa\int_0^\infty\langle0|\rho(t)|0\rangle\,dt.
\]
Only the specified ten-site counterexample and its open parameter neighborhood are claimed. Recombination is strictly positive, so the integral is finite.

## Proof

Let \(D(X)=X-\operatorname{diag}(X)\) and define the linear map
\[
\mathcal M_\gamma(X)=i[H,X]+2\mu X+\kappa\{P,X\}+2\gamma D(X).
\]
For the Hilbert-Schmidt inner product, its Hermitian part obeys, for every complex matrix \(X\),
\[
\operatorname{Re}\langle X,\mathcal M_\gamma X\rangle
=2\mu\|X\|_2^2+\kappa\bigl(\|PX\|_2^2+\|XP\|_2^2\bigr)
+2\gamma\sum_{i\ne j}|X_{ij}|^2
\ge2\mu\|X\|_2^2.
\]
Thus \(\mathcal M_\gamma\) is invertible and \(\|\mathcal M_\gamma^{-1}\|_{2\to2}\le(2\mu)^{-1}\). Indeed, the strictly positive uniform recombination implies decay of the density-matrix trace at least at rate \(2\mu\), so its time integral \(X_\gamma=\int_0^\infty\rho(t)\,dt\) is the unique solution of
\[
\mathcal M_\gamma(X_\gamma)=|5\rangle\langle5|,
\qquad \eta_\gamma=60(X_\gamma)_{00}.
\]

The supplied `certificate.json` gives two explicit rational approximate solutions \(Y_\gamma\), represented by real and imaginary integer matrices divided by \(T=10^{14}\), for \(\gamma=0,1/5\). Define
\[
S_\gamma=\sum_{i,j=0}^9\left(
\left|\operatorname{Re}\bigl(1000T(\mathcal M_\gamma Y_\gamma-E_{55})_{ij}\bigr)\right|
+\left|\operatorname{Im}\bigl(1000T(\mathcal M_\gamma Y_\gamma-E_{55})_{ij}\bigr)\right|
\right).
\]
Here \(E_{55}=|5\rangle\langle5|\). All summands are integers: the factors \(1000T\) clear every denominator. Direct exact-integer substitution, implemented in `verify.py`, gives
\[
S_0=244156,\qquad S_{1/5}=187408,
\]
and the real numerators of the respective \((0,0)\) entries are \(1430222719987\) and \(1453306925594\). The inverse bound and the elementary inequality \(\|R\|_2\le\sum_{ij}(|\operatorname{Re}R_{ij}|+|\operatorname{Im}R_{ij}|)\) imply
\[
|\eta_\gamma-60\operatorname{Re}(Y_\gamma)_{00}|
\le 2\kappa(2\mu)^{-1}\,\|\mathcal M_\gamma Y_\gamma-E_{55}\|_2
\le\frac{30 S_\gamma}{T}.
\]
Subtracting the upper bound for \(\eta_0\) from the lower bound for \(\eta_{1/5}\) yields the claimed strictly positive rational gap:
\[
\eta_{1/5}-\eta_0\ge
\frac{60(1453306925594-1430222719987)-30(244156+187408)}{10^{14}}
=\frac{1385039389500}{10^{14}}.
\]
The map \(\mathcal M_\gamma\) and its inverse vary continuously with the strictly positive parameters, proving persistence on an open neighborhood.

## Verification

Run `python3 verify.py` from the directory containing `certificate.json` and `verify.py`. Python's standard library suffices. The verifier validates both integer matrices, reconstructs all one hundred complex residual entries for each dephasing rate using the ten-cycle adjacency, and checks the exact residual totals, projected capture numerators, and strict rational gap. The stated inequality follows from the analytical Hilbert-Schmidt coercivity bound, not from a floating-point time evolution, a grid search, or an unsupported numerical assertion. The integer matrices are reusable finite witnesses; their numerical generation method is not part of the proof.

## Relationship to prior work

Kassal and Aspuru-Guzik (2012), arXiv:1201.5202, develop precisely the ordered-cycle model, including uniform recombination, a site trap, independent dephasing, and eventual trapping efficiency; their Section 3, Eq. (13), gives zero maximal enhancement for antipodal source/trap placements. The finite certified positive gap above contradicts that universal antipodal conclusion for one ten-cycle parameter choice. It does not contradict their weak-attenuation approximations, the possibility of no enhancement in other parameter regions, or their other transport examples. Plenio and Huelga (2008), arXiv:0807.4902, study noise-assisted transfer and the special absence of enhancement for end-to-end open uniform chains; that different graph does not imply the cyclic exclusion. Forgy and Mazziotti (2014), DOI:10.1063/1.4902883, analyze optimal environmental noise in one- and two-dimensional networks rather than an exact exclusion at antipodes of this cyclic model.

## Limitations

This is a counterexample to a stated global exclusion, not a complete classification of all ordered rings, all noise distributions, or optimum dephasing values. The model is Markovian, single-excitation, and exactly homogeneous in hopping, with one designated trap and strictly positive uniform recombination. The rational verification certifies the stationary infinite-time probabilities; finite-time enhancement, robustness to disorder, and optimized device performance are not established. Publication priority beyond the inspected literature has not been independently established.

## References

1. I. Kassal and A. Aspuru-Guzik, *Environment-assisted quantum transport in ordered systems*, New Journal of Physics **14**, 053041 (2012), arXiv:1201.5202, DOI:10.1088/1367-2630/14/5/053041. Original public submission: 2012-01-25 UTC. https://arxiv.org/html/1201.5202v2
2. M. B. Plenio and S. F. Huelga, *Dephasing assisted transport: Quantum networks and biomolecules*, New Journal of Physics **10**, 113019 (2008), arXiv:0807.4902. Original public submission: 2008-07-30 UTC. https://arxiv.org/html/0807.4902v1
3. C. C. Forgy and D. A. Mazziotti, *Relations between environmental noise and electronic coupling for optimal exciton transfer in one- and two-dimensional homogeneous and inhomogeneous quantum systems*, Journal of Chemical Physics **141**, 224111 (2014), DOI:10.1063/1.4902883.
