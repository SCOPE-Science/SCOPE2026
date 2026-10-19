# Sharp discrete Wigner negativity on additive Sidon supports

## Finding
Let \(p\ge3\) be an odd prime, \(d\ge1\), \(G=\mathbb F_p^d\), \(N=p^d\), and \(\omega=\exp(2\pi i/p)\). For a unit vector \(\psi:G\to\mathbb C\), define its discrete Wigner distribution by
\[
W_\psi(q,\xi)=\frac1N\sum_{s\in G}\psi(q+s/2)\overline{\psi(q-s/2)}\,\omega^{-\langle\xi,s\rangle},\qquad(q,\xi)\in G^2.
\]
All vector arithmetic is over \(\mathbb F_p\), so division by two is unambiguous. Suppose the exact support \(S=\{u:\psi(u)\ne0\}\) has \(m\ge1\) elements and is **additive Sidon**, meaning every unordered pair \(\{u,v\}\), including repeated pairs \(\{u,u\}\), has a distinct sum \(u+v\). Put \(b_u=|\psi(u)|\) and
\[
\delta_{uv}=\min_{k\in\mathbb Z}\left|\arg\big(\psi(u)\overline{\psi(v)}\big)-\frac{k\pi}{p}\right|\in\left[0,\frac\pi{2p}\right],\qquad u\ne v,
\]
where a representative of the phase can be chosen arbitrarily. Then the following identity holds **exactly**:
\[
\boxed{\displaystyle
\sum_{(q,\xi)\in G^2}|W_\psi(q,\xi)|
=1+\frac{2}{p\sin(\pi/(2p))}\sum_{\{u,v\}\subset S}b_ub_v\cos\delta_{uv}.}
\]
In particular, the sharp support-conditional bound is
\[
\boxed{\displaystyle \|W_\psi\|_1\le 1+\frac{m-1}{p\sin(\pi/(2p))}.}
\]
Equality occurs precisely when \(b_u=1/\sqrt m\) for all \(u\in S\) and all relative phases lie in \((\pi/p)\mathbb Z\). Equivalently, the equality coefficients are \(\psi(u)=\lambda e^{\pi i k_u/p}/\sqrt m\) with a common \(|\lambda|=1\) and arbitrary integers \(k_u\).

More strongly, the **complete nonnegative deficit identity** is
\[
\boxed{\displaystyle
1+\frac{m-1}{p\sin(\pi/(2p))}-\|W_\psi\|_1
=\frac1{p\sin(\pi/(2p))}\sum_{\{u,v\}\subset S}
\Big[(b_u-b_v)^2+2b_ub_v(1-\cos\delta_{uv})\Big].}
\]
The summation runs over distinct unordered pairs; if \(m=1\), it is empty and the norm equals one.

For any \(r\ge1\), with \(F=\mathbb F_{p^r}\), the set \(S_r=\{(t,t^2):t\in F\}\subset F^2\) is additive Sidon, and its normalized uniform vector has
\[
\boxed{\displaystyle\|W_\psi\|_1=1+\frac{p^r-1}{p\sin(\pi/(2p))}.}
\]
Its ambient Hilbert dimension is \(N=p^{2r}\); its Wigner absolute mass divided by \(\sqrt N\) tends to \(1/(p\sin(\pi/(2p)))\) as \(r\to\infty\).

## Assumptions and scope
All dimensions are positive and \(p\) is an odd prime. The ambient phase space has \(N^2\) points and the norm is the **unweighted sum of absolute values**, not a probability-space average. The finite-dimensional vector has unit \(\ell^2(G)\) norm. The Sidon hypothesis includes the diagonal pair sums and cannot be replaced by an arbitrary sparse support. The subgroup in the quadratic-graph example is the underlying \(2r\)-dimensional vector space over \(\mathbb F_p\); the trace pairing may replace a chosen coordinate pairing without affecting the conclusions. The theorem does not claim global maximization among all pure states on the same Hilbert space.

## Proof
**1. Separating Wigner midpoints.** Substitute \(u=q+s/2\) and \(v=q-s/2\) in the definition. The pair-to-midpoint map is \(q=(u+v)/2\), \(s=u-v\). The Sidon condition implies that no two distinct unordered supported pairs have the same midpoint. At a diagonal midpoint \(q=u\in S\), only the pair \((u,u)\) contributes, and \(W_\psi(u,\xi)=b_u^2/N\) for all \(\xi\in G\). These points contribute exactly \(\sum_{u\in S}b_u^2=1\) to the absolute mass.

At the unique midpoint of a distinct supported pair \(\{u,v\}\), the two terms are conjugate, giving
\[
W_\psi((u+v)/2,\xi)
=\frac2N\operatorname{Re}\left(\psi(u)\overline{\psi(v)}\omega^{-\langle\xi,u-v\rangle}\right).
\]
This quantity is real. Since \(u-v\ne0\), its linear character takes every \(p\)-th root of unity exactly \(N/p\) times as \(\xi\) varies. Accordingly, this midpoint contributes
\[
\frac{2b_ub_v}{p}\sum_{j=0}^{p-1}\left|\cos\left(\arg(\psi(u)\overline{\psi(v)})+\frac{2\pi j}{p}\right)\right|.
\]
Every other midpoint contributes zero.

**2. Exact odd-grid cosine identity.** Define \(A_p(t)=\sum_{j=0}^{p-1}|\cos(t+2\pi j/p)|\). Because \(p\) is odd, a shift by \(\pi/p\) permutes these absolute values; reflection also preserves them. Therefore it suffices to take \(|t|\le\pi/(2p)\). In this interval the summand signs agree with those at zero except possibly vanishing endpoints. Reflection pairs the sine contributions, so \(A_p(t)=A_p(0)\cos t\). Writing \(p=2h+1\), elementary geometric summation yields
\[
A_p(0)=1+2\sum_{j=1}^h\cos\frac{\pi j}{p}
=\frac{\sin((h+1/2)\pi/p)}{\sin(\pi/(2p))}
=\frac1{\sin(\pi/(2p))}.
\]
Consequently, for any real \(t\), \(A_p(t)=\cos(\operatorname{dist}(t,(\pi/p)\mathbb Z))/\sin(\pi/(2p))\). Combining this with Step 1 gives the stated exact Wigner mass identity.

**3. Sharp bound and all equality cases.** Write \(c_p=1/[p\sin(\pi/(2p))]\). Using \(\sum b_u^2=1\),
\[
(m-1)-2\sum_{\{u,v\}}b_ub_v\cos\delta_{uv}
=\sum_{\{u,v\}}(b_u-b_v)^2
 +2\sum_{\{u,v\}}b_ub_v(1-\cos\delta_{uv}).
\]
Each term on the right is nonnegative because \(b_u>0\) and \(0\le\delta_{uv}\le\pi/(2p)\). Thus \(\|W_\psi\|_1\le1+(m-1)c_p\), with the displayed exact deficit. If \(m\ge2\), vanishing of the deficit forces all moduli equal and every \(\delta_{uv}=0\). This means all coefficient phases belong to one coset of \((\pi/p)\mathbb Z\), exactly the asserted family. Conversely every such coefficient vector saturates the expression. For \(m=1\) the statement reduces to a normalized delta function and is automatic.

**4. Quadratic Sidon graphs and the high-negativity family.** For \(F=\mathbb F_{p^r}\), if two unordered pairs of graph points have equal sums, then their first coordinate sums \(s=t+u\) agree, and their second coordinate sums \(q=t^2+u^2\) agree. Because two is invertible, both pairs have the same product \(tu=(s^2-q)/2\). The two elements of each pair are exactly the roots, with multiplicities, of \(X^2-sX+tu\), so the unordered pairs coincide. Hence \(S_r\) is Sidon. Taking positive uniform coefficients meets the sharp equality conditions. Since \(m=p^r\) and \(N=p^{2r}\), the asserted formula follows. Finally, the Fourier-Plancherel identity gives \(\sum_{q,\xi}|W_\psi(q,\xi)|^2=1/N\). Cauchy--Schwarz over \(N^2\) phase-space sites yields \(\|W_\psi\|_1\le\sqrt N\), justifying the comparison. No assertion of optimality in the unrestricted class is used.

## Verification
The accompanying standalone `check_wigner_sidon.py` evaluates the original Wigner sum directly and compares it with the closed formula. It tests four distinct Sidon supports in dimensions one and two, each with a phase-quantized equality vector and five reproducibly seeded arbitrary complex vectors. All comparisons and sharp inequalities passed with absolute error below \(10^{-9}\). These finite floating-point tests are corroboration only; Steps 1--4 prove the stated theorem for all permitted parameters. The script uses only the Python standard library and can be run with `python3 check_wigner_sidon.py`.

## Relationship to prior work
Gross established the standard odd-dimensional discrete Wigner phase-space formalism and the classification of nonnegative pure-state Wigner distributions. Veitch, Ferrie, Gross, and Emerson explained why Wigner negativity is a resource measure. Neither inspected account gives the Sidon-support phase-resolved absolute-mass formula, its sharp equality family and deficit, or the quadratic-Sidon family attaining a dimension-independent fraction of the universal bound. These conclusions do not follow from the classical positive-Wigner/nonnegative-state dichotomy: the present values quantify the strictly negative regime and all phase-dependent variations. The quadratic-graph Sidon fact is elementary and is used as a concrete extremal support, not presented as new in isolation.

## Limitations
The claim is conditional on exact additive Sidon support and on odd prime local order. It does not optimize over all supports or all pure states; the \(\sqrt N\) comparison is an upper benchmark, not an attained global optimum. The exact deficit controls coefficient imbalance and grid-phase deviation **within** a fixed Sidon support; it is not a global distance-to-stabilizer theorem. Prior classifications of negative Wigner resources, Sidon sets, and special finite-state examples may hide an equivalent statement. An independent priority check has not been performed.

## References
- D. Gross, *Hudson's Theorem for finite-dimensional quantum systems*, arXiv:quant-ph/0602001, first public preprint 2006-02-01; Journal of Mathematical Physics **47**, 122107 (2006). https://arxiv.org/abs/quant-ph/0602001
- V. Veitch, C. Ferrie, D. Gross, and J. Emerson, *Negative Quasi-Probability as a Resource for Quantum Computation*, arXiv:1201.1256, first public preprint 2012-01-05; New Journal of Physics **14**, 113011 (2012). https://arxiv.org/abs/1201.1256
