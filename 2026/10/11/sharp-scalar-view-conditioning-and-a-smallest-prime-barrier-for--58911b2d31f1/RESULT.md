# Sharp scalar-view conditioning and a smallest-prime barrier for projective cyclic Radon transforms

## Finding

Consider the complete line-sum transform on a square cyclic grid with **one positive scalar acquisition weight per projective direction**, shared by all its parallel lines. For every integer \(N\ge2\), its smallest and largest nonconstant squared singular values admit exact closed formulas in terms of reduction of directions modulo primes. The optimum conditioning within this natural scalar-weight class is attained by, and **only by**, uniform direction weights:

\[
\inf_{w_d>0}\kappa_0(T_w)^2
=\frac{N\prod_{p\mid N}(1+p^{-1})}{p_*+1},
\qquad p_*:=\min\{p:p\mid N\}.
\]

This yields a sharp arithmetic obstruction to a tight transform on mean-zero images: its squared condition number equals one exactly for prime grid sizes. The finding additionally gives every normal-operator eigenvalue and multiplicity under uniform weights.

## Assumptions and scope

Let \(R=\mathbb Z/N\mathbb Z\), \(G=R^2\), and \(\mathcal D=\mathbb P^1(R)\). Here \(\mathcal D\) means the set of pairs \(d=(a,b)\in R^2\) satisfying \(\gcd(a,b,N)=1\), identified under multiplication by units of \(R\). Let \(U_d=\{td:t\in R\}\), a subgroup of cardinality \(N\); each quotient \(G/U_d\) has exactly \(N\) affine lines. The number of directions is

\[
D_N=|\mathcal D|=\prod_{p^k\parallel N}p^{k-1}(p+1)
=N\prod_{p\mid N}(1+p^{-1}).
\]

Choose arbitrary real weights \(w_d>0\), with no normalization condition. Define the Hilbert-space operator from counting-measure \(\ell^2(G)\) to the counting-measure orthogonal sum of quotient spaces by

\[
(T_wf)(d,L)=\sqrt{\frac{w_d}{N}}\sum_{x\in L}f(x),\quad d\in\mathcal D,\quad L\in G/U_d.
\]

Write \(\ell^2_0(G)=\{f:\sum_{x\in G}f(x)=0\}\). The condition number \(\kappa_0(T_w)\) is the ratio of the largest to the smallest nonzero singular value of the restriction to this mean-zero subspace; no image-frequency preconditioner and no frequency-dependent filtering are allowed. For each prime \(p\mid N\), reduce each projective direction modulo \(p\) and denote by

\[
W_{p,\ell}=\sum_{\substack{d\in\mathcal D\\\operatorname{red}_p(d)=\ell}}w_d,
\qquad \ell\in\mathbb P^1(\mathbb F_p),
\]

the aggregate weight of the residue fiber. All these fibers have the same cardinality \(D_N/(p+1)\).

## Proof

**Diagonalization and exact endpoints.** Characters \(\phi_\xi(x)=N^{-1}\exp(2\pi i\langle\xi,x\rangle/N)\), indexed by \(\xi\in G\), form an orthonormal basis. For each \(d\), the component \(T_d f(L)=N^{-1/2}\sum_{x\in L}f(x)\) has normal operator equal to the orthogonal projection onto characters trivial on \(U_d\). To check normalization directly: on such a character the \(N\) line sums each have modulus one, so the weighted output has squared norm \(w_d\); on all other characters each line sum vanishes. Consequently

\[
T_w^*T_w\phi_\xi=\lambda_\xi\phi_\xi,
\qquad\lambda_\xi=\sum_{\substack{d\in\mathcal D\\\langle\xi,d\rangle\equiv0\pmod N}}w_d.
\tag{1}
\]

For each primitive frequency \(\xi\) (its two entries, together with \(N\), have gcd one), the equation in (1) has exactly one projective direction, represented by \((-\xi_2,\xi_1)\). Conversely every projective direction arises as the perpendicular of some primitive frequency. Every nonzero frequency has at least one perpendicular projective direction by the Chinese remainder theorem, and all weights are positive. Thus the smallest eigenvalue among nonconstant characters is exactly

\[
\lambda_{\min}=\min_{d\in\mathcal D}w_d.
\tag{2}
\]

Take any nonzero frequency \(\xi\). For at least one prime power \(p^k\parallel N\), its local component is nonzero. Dividing that component by its common power \(p^v\), with \(v<k\), gives a primitive pair modulo \(p^{k-v}\). Any direction orthogonal to \(\xi\) must therefore reduce to the **unique** direction perpendicular to this pair modulo \(p\). Positivity implies \(\lambda_\xi\le W_{p,\ell}\) for that residue direction. Conversely, fix any \(p\mid N\) and any residue direction \(\ell\). By the Chinese remainder theorem choose a frequency whose local component at \(p^k\) is \(p^{k-1}\) times a primitive vector perpendicular to \(\ell\), and whose components at every other prime power are zero. The directions compatible with this frequency are *exactly* the fiber above \(\ell\), so \(\lambda_\xi=W_{p,\ell}\). Therefore

\[
\lambda_{\max}(T_w^*T_w|_{\ell^2_0})
=\max_{p\mid N}\max_{\ell\in\mathbb P^1(\mathbb F_p)}W_{p,\ell}.
\tag{3}
\]

Equations (2) and (3) give the exact weighted endpoint formula, as well as injectivity (all eigenvalues are positive).

**Sharp scalar-weight minimax.** Denote the total weight by \(S=\sum_{d\in\mathcal D}w_d\), and let \(p_*\) be the least prime dividing \(N\). The \(p_*+1\) residue fibers partition the directions, so

\[
\max_{\ell}W_{p_*,\ell}\ge\frac{S}{p_*+1},
\qquad \min_d w_d\le\frac{S}{D_N}.
\]

Combining with (2) and (3) yields \(\kappa_0(T_w)^2\ge D_N/(p_*+1)\). Equality implies the second inequality is equality, hence **every** positive weight equals their common average. Conversely, if \(w_d\) is constant, each fiber has \(D_N/(p+1)\) directions and the largest is attained at the smallest prime; equality follows. This proves optimality and its complete equality classification.

**Complete uniform singular spectrum.** Factor \(N=\prod_{p^k\parallel N}p^k\), and use the Chinese remainder theorem for positions, frequencies, and projective directions. A zero local frequency at \(p^k\) is orthogonal to all \(p^{k-1}(p+1)\) local directions. A nonzero local frequency with common valuation \(v<k\) is orthogonal to exactly \(p^v\) projective directions: there is one perpendicular projective class modulo \(p^{k-v}\), having \(p^v\) lifts modulo \(p^k\). Thus for \(w_d=1\), each eigenvalue \(\lambda_\xi\) is a product of the local factors

\[
\Lambda_{p,k}(\xi_p)=
\begin{cases}
p^{k-1}(p+1),&\xi_p=0,\\
p^v,&\xi_p\ne0\text{ and }v=\min\{\nu_p(\xi_{p,1}),\nu_p(\xi_{p,2})\}.
\end{cases}
\]

The zero local frequency has multiplicity one; valuation \(v\) occurs for exactly \(p^{2(k-v)}-p^{2(k-v-1)}\) local frequencies. Multiply independent local multiplicities, and add them when numerical eigenvalue products coincide. The singular values are the positive square roots; the constant-frequency (DC) eigenvalue is \(D_N\). These descriptions exhaust exactly \(N^2\) right singular vectors and prove the claimed complete spectrum.

## Verification

The supplementary Python 3 standard-library checker `CHECK.py` independently generates all projective directions and reductions for each \(2\le N\le30\), checks exact weighted endpoint identities with nonuniform positive integer weights, verifies the prime-power product eigenvalue multiplicities, and compares Fourier-mode energies against the direct weighted Gram operator for small moduli. Running `python3 CHECK.py` yields:

`VERIFY_OK moduli=29 weighted_endpoints=PASS CRT_multiplicities=PASS direct_Gram_Fourier=PASS flat_optimum=PASS`

This is finite corroboration, not a substitute for the proof above, and tests neither arbitrary large moduli nor arbitrary real weights exhaustively.

## Relationship to prior work

The line-sum model, discrete Fourier-slice principle, and composite-modulus redundancy are classical. Beylkin (1987) studied invertible periodic discrete Radon transforms and Fourier-block inversion. Kingston and Svalbe (2005) introduced the projective modulo-\(N\) transform and composite-modulus redundancy. Kingston (2006) developed orthogonalized prime-power projection bases; Kingston and Svalbe (2007) described correction with an angle-invariant **one-dimensional filter**. These are essential background, not originality claims. The present claim singles out the constrained acquisition-design problem in which each projective direction receives only one positive scalar shared across its lines: exact weighted nonconstant spectral endpoints, a sharp minimax bound determined by the least prime factor, rigidity of its optimizer, and an explicit full unweighted singular spectrum. Altering basis vectors or using filters that vary across Fourier frequencies is not covered by this minimax assertion. Some closely related publisher full texts could not be inspected; priority risk remains.

## Limitations

The theorem does not claim that uniform view scalars are optimal among arbitrary frequency-dependent filters, coordinate-dependent weights, subsets of measured lines, or other projection families. It assumes strictly positive real direction weights and a complete family of projective cyclic directions. The exact conditioning assertion applies to mean-zero images; the constant mode is accounted for in the full spectrum but excluded from that optimization. All statements concern finite cyclic product grids. The mathematical proof is internal and finite checks are supplementary; independent validation and an exhaustive literature-priority determination have not been performed.

## References

1. G. Beylkin, "Discrete Radon Transform," *IEEE Transactions on Acoustics, Speech, and Signal Processing* **35** (1987), 162–172. Open full text: https://amath.colorado.edu/faculty/beylkin/papers/BEYLKI-1987.pdf.
2. A. Kingston and I. Svalbe, "A Discrete Modulo N Projective Radon Transform for N × N Images," *Lecture Notes in Computer Science* **3429** (2005), 136–147; https://doi.org/10.1007/978-3-540-31965-8_13. Publisher catalogue reports public release September 14, 2005.
3. A. Kingston, "Orthogonal discrete Radon transform over prime-power images," *Signal Processing* **86** (2006), 2040–2050; https://doi.org/10.1016/j.sigpro.2005.09.024.
4. A. Kingston and I. Svalbe, "Generalised finite Radon transform for N × N images," *Image and Vision Computing* **25** (2007), 1620–1630; https://doi.org/10.1016/j.imavis.2006.03.002.
