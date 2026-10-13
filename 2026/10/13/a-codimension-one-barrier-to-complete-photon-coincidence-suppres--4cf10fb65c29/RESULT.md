# A codimension-one barrier to complete photon-coincidence suppression

## Finding

**Theorem (full coincidence with at most one missing internal dimension).** Fix an integer \(N\geq3\). Prepare exactly one photon in each of \(N\) distinct input spatial modes, with normalized, nonzero, pure internal states \(\phi_1,\ldots,\phi_N\) in a complex Hilbert space \(\mathcal H\). An arbitrary \(N\)-mode lossless interferometer \(U\in\mathrm U(N)\) acts only on spatial modes. Ideal number-resolving detectors, insensitive to internal states, measure the event \(\mathsf C\) of exactly one photon in **every** output spatial mode. Write \(P_U=\Pr(\mathsf C)\) and \(r=\dim\operatorname{span}\{\phi_1,\ldots,\phi_N\}\).

If \(r=N\), then \(P_U>0\) for every \(U\). If \(r=N-1\), then the following statements are equivalent:

1. \(P_U>0\) for **every** \(U\in\mathrm U(N)\).
2. No two internal states are proportional (that is, \(\phi_i\notin\mathbb C\phi_j\) for \(i\ne j\)).

If a proportional pair exists, some interferometer has \(P_U=0\): a balanced beamsplitter embedded on that pair's spatial modes suffices. Thus the assertion is about existence versus universal impossibility of suppression; it is *not* an assertion that all interferometers suppress a proportional pair.

There is also a uniform quantitative statement. Suppose \(r=N-1\) and **each** \(N-1\) of the internal states are linearly independent (the unique dependence has full support). Let \(S_N\) be the permutation group and \(P_\sigma\) the tensor-factor permutation operators on \(\mathcal H^{\otimes N}\). Put
\[
V=\phi_1\otimes\cdots\otimes\phi_N,\qquad
J_{\sigma,\pi}=\langle P_\sigma V,P_\pi V\rangle.
\]
The positive-semidefinite \(N!\)-by-\(N!\) Gram matrix \(J\) has precisely a one-dimensional kernel, spanned by \((\operatorname{sgn}\sigma)_{\sigma\in S_N}\). Let \(\lambda_*(J)>0\) be its smallest positive eigenvalue. For every \(U\in\mathrm U(N)\),
\[
\boxed{
P_U\geq\lambda_*(J)\left[\operatorname{per}(|U|^2)-\frac1{N!}\right]
\geq\lambda_*(J)\left(\frac{N!}{N^N}-\frac1{N!}\right)>0.
}
\]
Here \(\operatorname{per}\) is the matrix permanent and \(|U|^2\) denotes entrywise squared moduli. The last bound depends only on the photons' internal Gram matrix, not on the interferometer.

## Assumptions and scope

All photons enter in different spatial modes and have an **independent product of pure internal states**; no initial inter-source internal entanglement or coherence between alternative multiphoton input components is allowed. The internal space may be finite- or infinite-dimensional: the argument uses only the finite-dimensional span of the specified states. The interferometer is an exactly unitary square \(N\)-port and is internal-mode independent. Every output is monitored by an ideal non-internal-resolving number-resolving detector. Loss, postselection on fewer photons, inaccessible output ports, nonideal spectral filters, mixed initial internal states and output patterns with collisions fall outside the claim. The theorem imposes \(r\ge N-1\); it does not settle rank \(r\le N-2\).

The **quantitative** lower bound requires the stronger full-support dependence condition. The qualitative equivalence does **not** require full support: it covers a unique dependence involving only three or more of the \(N\) states.

## Proof

**1. Coincidence amplitude and determinant.** Choose the spatial convention \(a_j^\dagger(\phi)=\sum_{k=1}^N U_{k,j}b_k^\dagger(\phi)\). Expand the product of all input creation operators and restrict it to one photon in each output. For \(\sigma\in S_N\), put
\[
a_\sigma=\prod_{j=1}^N U_{\sigma(j),j},\qquad
\Psi_U=\sum_{\sigma\in S_N} a_\sigma P_\sigma V.
\]
The ordered output tensor \(P_\sigma V\) places internal state \(\phi_j\) in output slot \(\sigma(j)\). Distinct output slots are distinguishable and have occupation one, so bosonic creation-operator normalization contributes no additional factorial. Consequently
\[
P_U=\|\Psi_U\|^2=a^*Ja,
\quad \sum_{\sigma\in S_N}\operatorname{sgn}(\sigma)a_\sigma=\det U\ne0.
\]
In particular, not all path amplitudes vanish.

**2. Independent internal states.** If \(r=N\), the vectors \(\phi_j\) are linearly independent. Tensor products of these vectors in any ordered positions form a linearly independent set, so the \(N!\) orbit tensors \(P_\sigma V\) are independent. Thus \(\Psi_U=0\) would force every \(a_\sigma=0\), contradicting \(\det U\ne0\). Hence \(P_U>0\).

**3. Exactly one linear relation.** Now suppose \(r=N-1\). Relabel so \(\phi_1,\ldots,\phi_{N-1}\) are independent and
\[
\phi_N=\sum_{i\in T}c_i\phi_i,
\qquad T\subseteq\{1,\ldots,N-1\},\quad c_i\ne0.
\]
For each \(i\in T\), let
\[
w_i=\phi_1\otimes\cdots\otimes\phi_{N-1}\otimes\phi_i.
\]
The orbit tensors of \(w_i\) have one repeated label \(i\), and its other \(N-2\) labels occur once. Orbits for distinct \(i\) have distinct multisets of labels. Since \(\phi_1,\ldots,\phi_{N-1}\) are a basis of their span, the resulting tensor-basis weight spaces are independent. Therefore
\[
\Psi_U=0\quad\Longleftrightarrow\quad
\sum_{\sigma\in S_N}a_\sigma P_\sigma w_i=0
\quad\text{for every }i\in T.
\]
The tensor \(P_\sigma w_i\) equals \(P_{\sigma(i\ N)}w_i\), where \((i\ N)\) transposes the identical input labels; different two-element cosets correspond to different tensor-basis words. Hence the last equality is equivalent to
\[
a_{\sigma(i\ N)}=-a_\sigma
\qquad\text{for every }\sigma\in S_N\text{ and }i\in T. \tag{1}
\]
If \(|T|\ge2\), choose distinct \(i,k\in T\). The star transpositions \((i\ N)\) and \((k\ N)\) generate the full permutation group on those three input positions. By the determinant identity there is a \(\sigma_0\) with \(a_{\sigma_0}\ne0\); (1) then forces all six path amplitudes \(a_{\sigma_0 h}\), for \(h\) permuting \(i,k,N\), to be nonzero and equal to \(\operatorname{sgn}(h)a_{\sigma_0}\). All other input-column/output-row assignments are fixed by \(\sigma_0\), so their nonzero product cancels from these equalities. We obtain a \(3\)-by-\(3\) submatrix \(B\) of \(U\), with no zero entries, whose six permutation monomials have equal magnitudes and the permutation signs.

Fix any two of those columns, called \(p,q\), and the three output rows \(x,y,z\). Comparing a permutation with the permutation that swaps assignments of columns \(p,q\) to rows \(x,y\), with the third column assigned to row \(z\), gives
\[
B_{x,p}B_{y,q}=-B_{x,q}B_{y,p}.
\]
The same comparison for each of the three unordered pairs of rows gives, with \(r_t=B_{t,p}/B_{t,q}\ne0\), the impossible conditions \(r_x=-r_y\), \(r_y=-r_z\), and \(r_x=-r_z\). Therefore \(\Psi_U\ne0\) whenever \(|T|\ge2\). Since \(\phi_N\) is proportional to one of the other states exactly when \(|T|=1\), this proves universal positivity if no pair is proportional.

Conversely, if \(\phi_i\) and \(\phi_j\) are proportional, choose the spatial unitary equal to the identity outside their two ports and a balanced beamsplitter
\[
\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}
\]
on those ports. The two distinguishable spatial paths to one photon per selected output have opposite amplitudes and equal internal tensors; the pair therefore never exits one photon per port (Hong--Ou--Mandel cancellation). Consequently the full \(N\)-port collision-free event has probability zero. This finishes the qualitative equivalence.

**4. Full-support dependence and a positive uniform gap.** If \(T=\{1,\ldots,N-1\}\), (1) shows that every vector \(a\in\ker J\) must flip sign under right multiplication by every star transposition \((i\ N)\). These transpositions generate \(S_N\), so such a vector is a scalar multiple of the alternating sign vector \(s=(\operatorname{sgn}\sigma)_\sigma\). Conversely \(\sum_\sigma s_\sigma P_\sigma V=0\), since each repeated-label tensor orbit cancels pairwise, so \(\ker J=\operatorname{span}\{s\}\). Thus \(\lambda_*(J)>0\), and orthogonal projection away from the sign direction gives
\[
P_U=a^*Ja\ge\lambda_*(J)\left(\|a\|_2^2-
\frac{|\langle s,a\rangle|^2}{\|s\|_2^2}\right).
\]
Now \(\|a\|_2^2=\operatorname{per}(|U|^2)\), \(\langle s,a\rangle=\det U\), \(|\det U|=1\), and \(\|s\|_2^2=N!\), giving the first bound. The nonnegative matrix \(|U|^2\) is doubly stochastic. The Egorychev--Falikman (van der Waerden) permanent lower bound yields \(\operatorname{per}(|U|^2)\ge N!/N^N\). Finally
\[
(N!)^2=\prod_{k=1}^{N}k(N+1-k)>N^N\quad(N\ge3),
\]
since \(k(N+1-k)-N=(k-1)(N-k)\ge0\), with a strict inequality for an interior \(k\). This proves the claimed strict, interferometer-uniform bound.

## Verification

The standalone script `verify_photon.py` (Python 3, NumPy) independently calculates the full ordered output internal tensor and the permutation-Gram quadratic form for \(N=3,4,5\) with several lossless interferometers. It tests the exact balanced-beamsplitter cancellation when a proportional pair is inserted; checks the one-dimensional alternating Gram kernel and positive eigenvalue quotient for a full-support three-state dependence; checks its numerical lower bound; and checks the strict elementary factorial inequality for a finite range. The measured output is `VERIFY_OK direct_tensor_gram=12 HOM_boundary=3 positive_orbit_quotient=passed finite_factorial_gap=passed`. These finite tests are diagnostic only: steps 1–4 above prove the assertions for every allowed \(N\).

## Relationship to prior work

Shchesnovich, *Partial indistinguishability theory for multi-photon experiments in multiport devices* (arXiv:1410.1506), supplies the general photon-counting and permutation-Gram framework. Its Section III.C analyzes the corresponding linearly dependent three-photon case, proves absence of exact zero for a pairwise partially distinguishable triple, and explicitly frames the many-photon zero-probability question as a conjecture. The present theorem proves an all-photon-number codimension-one **product-input, collision-free** case and adds a photon-Gram-dependent uniform positive lower bound. It does not purport to settle that conjecture for arbitrary multiphoton entangled inputs, other output occupations, or detectors.

Shchesnovich, *Partial distinguishability and photon counting probabilities in linear multiport devices* (arXiv:1712.03191), develops broader generating functions for independent sources; no explicit codimension-one zero-impossibility classification or the quantified all-unitary positive gap is stated in its inspected introductory, main-formula and concluding sections. Crespi, *Suppression laws for multi-particle interference in Sylvester interferometers* (arXiv:1502.06372), concerns symmetry-induced zeros for special networks and input symmetries, and does not subsume the present all-interferometer positivity result. The permanent inequality employed in step 4 is classical; see Gurvits, arXiv:math/0504397, for an independent proof encompassing the Egorychev--Falikman bound.

## Limitations

The result does not classify exact zeros when the internal-state span has dimension at most \(N-2\), does not assert a positivity bound uniform over **varying** internal state families, and does not address loss, mixed states, nonideal or internal-resolving detectors, other output patterns, or internally entangled preparations. A conceivable equivalent treatment in less easily indexed optical-interference literature remains a priority risk; the literature search is not a mathematical proof of novelty. The quantitative bound is not generally asserted to be optimal. The verification program does not certify infinite parameter ranges or independently audit the proof.

## References

1. V. S. Shchesnovich, *Partial indistinguishability theory for multi-photon experiments in multiport devices*, arXiv:1410.1506 (initial public posting 2014-10-06), especially Section III.C and equations (80)–(83). https://arxiv.org/abs/1410.1506
2. V. S. Shchesnovich, *Partial distinguishability and photon counting probabilities in linear multiport devices*, arXiv:1712.03191. https://arxiv.org/abs/1712.03191
3. A. Crespi, *Suppression laws for multi-particle interference in Sylvester interferometers*, arXiv:1502.06372. https://arxiv.org/abs/1502.06372
4. L. Gurvits, *A proof of hyperbolic van der Waerden conjecture: the right generalization is the ultimate simplification*, arXiv:math/0504397. https://arxiv.org/abs/math/0504397
