# Infinite repelling two-cycles and their sharp density in a cosine-memory logistic map

## Finding

Consider the real-plane autonomous map
\[
F_{a,k,q}(x,w)=\bigl(a x[1-x^2\cos(q+kw)],\;w+x\bigr),\qquad a>0,\quad k>0,\quad q\in\mathbb R.
\]
This is the full-state extension of the cosine-memristor logistic recurrence in Li, Zhong, Xu and Xu (2022), equation (11). Translation by \(2\pi/k\) in the accumulator coordinate commutes with the map. Identify two geometric primitive two-cycles only when one is the translate of the other by such a translation. For \(R>0\), let \(N_2(R)\) count the resulting two-cycle classes with positive first-coordinate amplitude \(u\le R\).

**Theorem.** Put \(C=1+1/a\). For every \(a,k>0\) and \(q\in\mathbb R\), all nontrivial primitive two-cycles are precisely the following two families. Their representatives have the form
\[
(u,w)\longleftrightarrow(-u,w+u),\quad u\ge\sqrt C,\quad\theta=q+kw\pmod{2\pi}.
\]

* **Commensurate-memory family A:** \(u=2\pi m/k\) for an integer \(m\ge1\) with \(u\ge\sqrt C\), and \(\theta=\pm\arccos(C/u^2)\). The two phases coincide when \(u=\sqrt C\).
* **Reflected-phase family B:** \(u\ge\sqrt C\) solves \(|\cos(ku/2)|=C/u^2\), and \(\theta=-ku/2+j\pi\), with the unique \(j\in\{0,1\}\) for which \((-1)^j\cos(ku/2)=C/u^2\). Families A and B intersect only in the exceptional event \(u=\sqrt C=2\pi m/k\).

Let \(z_n=(2n+1)\pi/k\). Every sufficiently large \(n\) contributes **exactly two** B-cycles, with amplitudes
\[
u_{n,\pm}=z_n\pm\frac{2C}{kz_n^2}+O_{a,k}(z_n^{-5}).\]
Consequently,
\[
\boxed{N_2(R)=\frac{2k}{\pi}R+O_{a,k}(1)\qquad(R\to\infty).}
\]
All but finitely many of these cycles are hyperbolically repelling, and each of their two return-map eigenvalues \(\Lambda\) has
\[
\boxed{|\Lambda|\sim a k u^3\qquad(u\to\infty).}
\]
For sufficiently large amplitudes, the A-family return maps reverse orientation, whereas the B-family return maps preserve orientation. Each family contributes \((k/\pi)R+O_{a,k}(1)\) repelling cycles through amplitude \(R\).

There is a complementary global trapping statement. If \(0<a<1\), the open strip \(|x|<\rho_a\), where
\[\rho_a=\sqrt{a^{-1}-1},\]
is forward invariant, and every orbit starting in it converges to a point on the fixed line \(x=0\), at a geometric rate depending on the initial amplitude. The radius \(\rho_a\) is optimal for a uniform one-step contraction assertion across all memory phases. Every nontrivial two-cycle lies outside this strip, with \(u^2-\rho_a^2\ge2\). Hence a globally defined attracting strip coexists with infinitely many remote repelling two-cycles for every \(0<a<1\) and \(k>0\).

## Assumptions and scope

All variables and parameters are real, \(a>0\), \(k>0\), and \(q\) is arbitrary. The periodicity is **literal in the full real-plane state**: \(F^2(x,w)=(x,w)\). Counting modulo accumulator translations avoids artificial copies of the same orbit caused by the cosine period. No quotient-periodic orbit with nonzero accumulator winding is counted. The published numerical setting takes initial accumulator \(w_0=0\); the theorem concerns all states of its autonomous two-dimensional recurrence, not solely that prescribed initial slice. The arbitrary phase \(q\) may equivalently absorb a change in accumulator origin.

## Proof

**Reduction and exhaustion.** If \((x,w)\) is a real-plane period-two point, its second coordinate after two steps is \(w+x+x'\), where \(x'\) is its next first coordinate. Therefore \(x'=-x\). The case \(x=0\) is fixed, not primitive; every other orbit has a unique positive first-coordinate point \((u,w)\). Its two first-coordinate equations reduce to
\[
\cos\theta=\cos(\theta+ku)=\frac{1+1/a}{u^2}=\frac C{u^2}.
\]
In particular \(u\ge\sqrt C\). Using
\[
\cos\theta-\cos(\theta+ku)=2\sin(ku/2)\sin(\theta+ku/2),
\]
we obtain either \(ku=2\pi m\) (family A) or \(\theta+ku/2=j\pi\) (family B). The stated phases follow from \(\cos\theta=C/u^2>0\). Conversely each listed representative obeys both full-state return equations. At the intersection, \(\cos\theta=1\), so \(u=\sqrt C\), and also \(ku=2\pi m\); these finite resonant coincidences are counted only once.

**Two roots per remote cosine zero.** For \(n\ge0\) let \(z_n=(2n+1)\pi/k\) and \(I_n=[z_n-\pi/(3k),z_n+\pi/(3k)]\). Beyond a parameter-dependent finite amplitude threshold, \(C/u^2<1/2\), so every B root is in exactly one such interval. On each half of \(I_n\), the function \(|\cos(ku/2)|\) rises strictly from zero to \(1/2\), with derivative magnitude at least \(k\sqrt3/4\). The derivative magnitude of \(C/u^2\) is only \(2C/u^3\). Hence their difference is strictly monotone on each half for sufficiently large \(n\), negative at \(z_n\) and positive at each endpoint: precisely one root occurs on each side. Writing \(u=z_n+\delta\), the defining equation becomes \(\sin(k|\delta|/2)=C/(z_n+\delta)^2\), giving
\[
\delta=\pm\frac{2C}{kz_n^2}+O_{a,k}(z_n^{-5})
\]
by Taylor expansion (\(\delta=O(z_n^{-2})\)). Family A contributes two phases for each sufficiently large positive integer \(m\), namely \((k/\pi)R+O(1)\) cycles through amplitude \(R\). The zeros \(z_n\) have the same asymptotic spacing \(2\pi/k\) and each contributes two B cycles. Adding them, and ignoring only finitely many exceptional amplitudes, proves the density formula.

**Return spectra and orientation.** At any point of a two-cycle the one-step Jacobian is
\[
J(x,\theta)=\begin{pmatrix}a(1-3x^2\cos\theta)&akx^3\sin\theta\\1&1\end{pmatrix}.
\]
Define \(d=-2a-3\) and \(b=aku^3\sin\theta\). On every two-cycle, \(u^2\cos\theta=C\), so its first Jacobian is \(J_+=\begin{pmatrix}d&b\\1&1\end{pmatrix}\) and \(|b|=aku^3\sqrt{1-C^2/u^4}\sim aku^3\). On an A-cycle the second Jacobian is \(J_-=\begin{pmatrix}d&-b\\1&1\end{pmatrix}\). Thus the return matrix \(M_A=J_-J_+\) has
\[
\operatorname{tr}M_A=d^2+1,\qquad\det M_A=d^2-b^2,
\]
and eigenvalues
\[
\Lambda_{A,\pm}=\frac{d^2+1\pm\sqrt{(d^2-1)^2+4b^2}}2.
\]
For sufficiently large \(u\), one is greater than \(1\) and the other less than \(-1\), both with modulus asymptotic to \(aku^3\); the determinant is negative.

For a B-cycle, \(\theta+ku=-\theta\pmod{2\pi}\). Since simultaneously \(x\) changes from \(u\) to \(-u\), the second Jacobian equals \(J_+\), so \(M_B=J_+^2\). Now \(\operatorname{tr}J_+=d+1=-2(a+1)\) is constant while \(\det J_+=d-b\) has magnitude asymptotic to \(aku^3\). Its two eigenvalues both have modulus asymptotic to \(\sqrt{aku^3}\), so the eigenvalues of \(M_B\) both have modulus asymptotic to \(aku^3\). This also proves hyperbolic repulsion and \(\det M_B=(d-b)^2>0\) for sufficiently large \(u\). Every omitted non-repelling cycle has bounded amplitude and there are only finitely many cycles of bounded amplitude by the preceding classification (zeros are discrete and the defining analytic functions have only finitely many roots in a compact interval).

**Attracting inner strip.** If \(0<a<1\) and \(|x_0|<\rho_a\), let \(\gamma=a(1+|x_0|^2)<1\). The first-coordinate recurrence yields \(|x_{n+1}|\le a|x_n|(1+|x_n|^2)\le\gamma|x_n|\), so \(|x_n|\le\gamma^n|x_0|\). The memory sums converge absolutely and \(w_n\to w_0+\sum_{n\ge0}x_n\). The limit is a fixed point on \(x=0\). If any putative uniform one-step contraction radius exceeded \(\rho_a\), choose an amplitude just above \(\rho_a\) and a phase with \(\cos(q+kw)=-1\); the next absolute amplitude would increase because \(a(1+x^2)>1\). The two-cycle amplitude bound gives \(u^2-\rho_a^2\ge(1+1/a)-(1/a-1)=2\).

## Verification

Run `python3 verify_cycles.py` with Python 3.10 or newer. The checker uses only the standard library. It independently evaluates representatives under the original two-dimensional recurrence, checks their full two-step return, reconstructs and multiplies both Jacobians, compares exact family-specific trace and determinant formulas, tests the predicted orientation and asymptotic modulus on remote cycles, and checks strict contraction along inner-strip orbits. The supplied code tested three parameter triples and the two sides of six high-index B phase zeros per triple. These finite checks are reproducibility witnesses; the universal enumeration and asymptotics follow from the preceding analytic argument.

## Relationship to prior work

Li, Zhong, Xu and Xu introduced equation (11), emphasizing trajectory, Lyapunov, bifurcation, and entropy plots. Their complete article was inspected, particularly sections 3.1–3.4 and 5; it does not give a literal two-cycle classification modulo memory translations, a two-branch density, or remote return spectra. Chunlai Li and collaborators (2022) constructed a distinct memristor logistic map with **affine** accumulator dependence, \(x'=\mu x[1-(A+By)x]\), \(y'=y+cx\). Their full text was examined, including equation (20) and section 3; that model's fixed line and numerical multistability do not imply the present cosine-phase resonance law. Bao and collaborators (2020) analyze another cosine-memristive two-dimensional map with a different update rule and numerical period doubling. Related exact two-cycle classifications of other planar maps lack the present oscillatory accumulator coupling and do not imply the asymptotic count. Targeted searches of published mathematical records and bibliographic indexes revealed no equivalent or dominating statement; absence in a search is not a proof of priority.

## Limitations

The theorem counts literal full-plane two-cycles modulo only the **exact** accumulator translation symmetry; it does not classify higher periods, global basins, or finite-amplitude two-cycle bifurcations. The author's numerical convention \(w_0=0\) is an initial-data restriction; no claim is made that each periodic orbit intersects that slice for a fixed external phase. The theorem's orientation conclusion concerns the return derivative at large-amplitude cycles only. Independent validation has not been performed. A presently unindexed source with the same full-plane map and a stronger orbit census could still supersede the novelty claim.

## References

1. G. Li, H. Zhong, W. Xu, X. Xu, *Two Modified Chaotic Maps Based on Discrete Memristor Model*, **Symmetry** 14 (2022), 800, published 12 April 2022. DOI: https://doi.org/10.3390/sym14040800. Full-text inspection: https://www.researchgate.net/publication/367737385_Two_Modified_Chaotic_Maps_Based_on_Discrete_Memristor_Model.
2. C. Li, Y. Yang, X. Yang, Y. Lu, *Application of discrete memristors in logistic map and Hindmarsh–Rose neuron*, **European Physical Journal Special Topics** 231 (2022), 3209–3224. DOI: https://doi.org/10.1140/epjs/s11734-022-00645-z. Full-text inspection: https://www.researchgate.net/publication/362703606_Application_of_discrete_memristors_in_logistic_map_and_Hindmarsh-Rose_neuron.
3. H. Bao et al., *Hyperchaos in a second-order discrete memristor-based map model*, **Electronics Letters** (2020), DOI: https://doi.org/10.1049/el.2020.1172.
