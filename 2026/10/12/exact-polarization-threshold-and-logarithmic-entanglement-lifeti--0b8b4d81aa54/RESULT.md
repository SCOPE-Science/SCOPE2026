# Exact polarization threshold and logarithmic entanglement lifetime in anti-thermalizing qubit collisions

## Finding

For a reset-after-every-collision anti-exchange qubit model, the **joint state immediately following a coherent collision but before ancilla reset** is entangled exactly during a computable initial interval of collision indices. With polarization \(0\le m\le1\), \(0<\theta<\pi/2\), \(q=\cos^2\theta\), \(\eta=q(1-q)\), and \(h_k=q^{k-1}\), its negativity is
\[
\mathcal N_k=\frac14\left[m\sqrt{(2-h_k)^2+4\eta h_k^2}-1-m^2(1-h_k)\right]_+,
\quad [x]_+=\max(0,x).
\]
For \(0<m<1\), put \(v=\sqrt{1+4\eta}\) and
\[
h_*(m,q)=\frac{1-m^2}{m(v-m)}.
\]
Then \(\mathcal N_k>0\) precisely when \(q^{k-1}>h_*\). In particular, the system and its current ancilla are ever entangled exactly when \(m>1/v\). If \(1/v<m<1\), the exact number of entangling collisions is
\[
L(m,q)=\left\lceil\frac{\log h_*(m,q)}{\log q}\right\rceil.
\]
If \(m\le1/v\), it is zero. If \(m=1\), it is infinite, with strictly positive negativity at each finite collision, tending to zero with \(k\). Thus transient entanglement cannot first emerge late or revive after death in this model.

Among all interaction angles, entanglement occurs for at least one angle precisely when \(m>1/\sqrt2\), since \(v\le\sqrt2\), with equality at \(\theta=\pi/4\). At the first collision,
\[
\max_\theta\mathcal N_1=\tfrac14[\sqrt2m-1]_+.
\]
For fixed \(0<q<1\), the finite entanglement lifetime satisfies
\[
L(m,q)=\frac{\log[1/(1-m^2)]}{|\log q|}+O(1)\quad(m\uparrow1).
\]

## Assumptions and scope

Use ordered product basis \(\{|00\rangle,|01\rangle,|10\rangle,|11\rangle\}\), with the first bit belonging to system \(S\) and the second to ancilla \(A\). Start with \(\rho_S^{(0)}=I/2\). Each collision uses a fresh ancilla in the same state
\[
\tau_A=a|0\rangle\langle0|+b|1\rangle\langle1|,\quad a=(1+m)/2,\quad b=(1-m)/2.
\]
The coherent stroke is \(U_\theta=e^{-i\theta H_+}\) with \(H_+=|00\rangle\langle11|+|11\rangle\langle00|\); the output is \(\rho_{SA}^{(k)}=U_\theta(\rho_S^{(k-1)}\otimes\tau_A)U_\theta^\dagger\). Then discard \(A\) and reset it before the next stroke. Negativity means the sum of absolute negative eigenvalues of the partial transpose, \(\mathcal N(\rho)=(\|\rho^{T_A}\|_1-1)/2\). Every statement refers to this **pre-reset joint state**, not to a steady-state entangled pair. The angles \(\theta=0,\pi/2\) are non-entangling endpoints; polarization \(m=0\) likewise yields zero negativity.

For an ordinary positive-temperature qubit Gibbs ancilla with gap \(\varepsilon_A>0\), \(m=\tanh(\beta\varepsilon_A/2)\); hence an interaction angle producing entanglement exists precisely if \(\beta\varepsilon_A>\log(3+2\sqrt2)\). The basis convention merely fixes the sign of polarization; swapping both ancilla basis labels gives the same result for its absolute value.

## Proof

**Step 1: iterate the reduced state.** Write \(p_k=\langle1|\rho_S^{(k)}|1\rangle\). If the pre-collision excited population is \(p\), then the product input populations are \(d_{00}=a(1-p)\), \(d_{01}=b(1-p)\), \(d_{10}=ap\), and \(d_{11}=bp\). As the unitary acts only in the span of \(\{|00\rangle,|11\rangle\}\), direct partial trace gives \(p\mapsto qp+(1-q)a\). The initial value is \(p_0=1/2\), so induction gives
\[
p_{k-1}=a+(1/2-a)q^{k-1}=\frac{1+m(1-h_k)}2.
\]
This calculation also proves that the reduced state remains diagonal for all collisions.

**Step 2: diagonalize the partial transpose.** Only the \(00,11\) coherence appears after the stroke; it has modulus \(\sqrt{\eta}|p-a|\). Partial transpose moves this entry into the \(01,10\) block, whose diagonal entries are unchanged, \(d_{01}\) and \(d_{10}\). The two remaining diagonal eigenvalues are nonnegative. The possible negative eigenvalue is
\[
\lambda_- =\frac{d_{01}+d_{10}-\sqrt{(d_{01}-d_{10})^2+4\eta(p-a)^2}}2.
\]
Substitution of Step 1 yields \(d_{01}+d_{10}=[1+m^2(1-h_k)]/2\), \(d_{01}-d_{10}=-m(2-h_k)/2\), and \(p-a=-mh_k/2\). Thus \(\mathcal N_k=[-\lambda_-]_+\) is the displayed exact formula. In particular, positivity is equivalent to
\[
\eta m^2h_k^2/4>d_{01}d_{10}=abp_{k-1}(1-p_{k-1}),
\]
or, after clearing positive factors,
\[
4\eta m^2h_k^2>(1-m^2)\big[1-m^2(1-h_k)^2\big]. \tag{1}
\]

**Step 3: factor the sharp boundary.** Let \(v=\sqrt{1+4\eta}\). The difference between the two sides of (1) factors exactly as
\[
m^2(v^2-m^2)\left(h_k-\frac{1-m^2}{m(v-m)}\right)
\left(h_k+\frac{1-m^2}{m(v+m)}\right).
\]
For \(0<m<1\) and \(0<q<1\) all factors except the first parenthesis are strictly positive at \(h_k>0\). This proves \(\mathcal N_k>0\iff h_k>h_*\). Because \(h_k\) strictly decreases from \(1\) to \(0\), the crossing is unique and later revival is impossible. One has \(h_*<1\) exactly when \(m>1/v\) (subtracting the equal quadratic terms in the positive-denominator inequality). The strict inequality \(q^{k-1}>h_*\) is equivalent to \(k-1<\log h_*/\log q\). Its exact count is the ceiling displayed above, including when the ratio is an integer. For \(m=1\) the right side of (1) vanishes and the left side is positive for every finite \(k\); directly expanding the negativity gives \(\mathcal N_k\sim\eta q^{2(k-1)}/4\). At \(m=0\), or \(q=0,1\), the coherence vanishes and so does negativity.

**Step 4: optimize and take the limit.** The maximum of \(\eta=q(1-q)\) on \([0,1]\) is \(1/4\), giving \(v\le\sqrt2\) and the universal critical polarization. In the first collision \(h_1=1\), yielding \(\mathcal N_1=[mv-1]_+/4\). Finally, as \(m\uparrow1\), \(h_*=(1-m^2)/[m(v-m)]\); its denominator approaches \(v-1>0\), so \(\log h_* =\log(1-m^2)+O(1)\). Taking the ceiling proves the asserted logarithmic lifetime. This is a finite-dimensional analytic argument for every \(k\), not an inference from finite enumeration.

## Verification

The standalone `verify.py` reconstructs the four-by-four unitary and density matrix at every stroke, partially transposes the fresh ancilla, directly computes eigenvalues, and independently obtains the next system state by partial trace. It checks the exact formula against 12,600 matrix evaluations (1,800 deterministic parameter draws, seven collisions each), confirms polynomial factorization symbolically, and tests special polarizations. With Python, NumPy, and SymPy installed, run `python verify.py`. Its successful output is `VERIFY_OK 12600 matrix comparisons; symbolic identities passed`. These finite computational tests are supplementary; the proof above covers all admissible angles, polarizations, and finite collision indices.

For instance, at \(m=0.9\), \(q=1/2\), the threshold is \(h_*\approx0.4108\) and exactly the first two collisions are entangling.

## Relationship to prior work

Pal et al. [1] specify the partial bit-flipped swap (anti-thermalization) collision protocol, derive its geometric population relaxation, and show numerically that the negativity is appreciable in early collisions; their main text and supplemental sections do not present the exact all-index negativity boundary, its no-revival criterion, or its closed lifetime count. Scarani et al. [2] earlier characterized partial-swap thermalizing machines, their geometric relaxation and entanglement-generating capabilities; the present anti-swap model is locally bit-flip equivalent. This theorem therefore does **not** claim discovery of repeated qubit collisions, their population recursion, or a novel general PPT principle. De Oliveira Junior et al. [3] give substantially more general thermodynamic entangleability criteria for two-qubit inputs, but do not classify this fixed-angle reset sequence and its finite entangling-collision count. The present all-stroke arithmetic classification is obtained by combining known ingredients with an exact specialization and strict-boundary analysis; an earlier implicit equivalent derivation cannot be excluded.

## Limitations

The coherent unitary is ideal, the ancilla is refreshed without memory between strokes, and the system begins maximally mixed. This is not a statement for noisy control, correlated reservoirs, general starting coherences, or arbitrary ancilla Hamiltonians. Joint pre-reset entanglement is erased by the next reset; no persistent system--ancilla entangled steady state is asserted. The threshold and duration apply to negativity in this qubit model, not to a macroscopic thermodynamic phase transition. The maximal first-collision result does not optimize the entanglement lifetime over angles.

## References

[1] S. Pal, K. Hovhannisyan, O. Porat, S. Dutta, J. Anders, and H. Knowles, *Ancilla mediated steady-state engineering in open quantum systems*, arXiv:2609.04905v1 (submitted 2026-09-04), esp. Eqs. (1), (3), (6)--(8), Fig. 3(d), and supplemental methods. https://arxiv.org/abs/2609.04905

[2] V. Scarani, M. Ziman, P. Štelmachovič, N. Gisin, and V. Bužek, *Thermalizing quantum machines: Dissipation and entanglement*, arXiv:quant-ph/0110088v2 (2002), esp. Eqs. (3), (6)--(9) and the entangling-power discussion. https://arxiv.org/abs/quant-ph/0110088

[3] A. de Oliveira Junior, J. Son, J. Czartowski, and N. H. Y. Ng, *Entanglement generation from athermality*, Physical Review Research **6**, 033236 (2024), esp. Sec. V and appendices. https://doi.org/10.1103/PhysRevResearch.6.033236
