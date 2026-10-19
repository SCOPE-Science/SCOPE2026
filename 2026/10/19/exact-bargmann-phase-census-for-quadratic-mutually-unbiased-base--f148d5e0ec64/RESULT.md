# Exact Bargmann phase census for quadratic mutually unbiased bases over odd finite fields

## Finding
For any odd prime \(p\), positive integer \(r\), and \(q=p^r\), consider the standard quadratic construction of \(q+1\) mutually unbiased bases (MUBs) in \(\mathbb C^q\). For every ordered triple \((u,v,w)\) of unit vectors drawn from **three distinct bases**, define its normalized Bargmann phase
\[
\Omega(u,v,w)=q^{3/2}\langle u,v\rangle\langle v,w\rangle\langle w,u\rangle.
\]
The complex phases and their exact global multiplicities are determined below. In particular, exactly \(p+1\) different phases occur when \(r=1\), while exactly \(2p\) occur for every \(r\ge2\). This jump is not a statement about arbitrary MUB systems: it concerns precisely the specified quadratic finite-field construction.

Write \(\zeta_p=\exp(2\pi i/p)\), and let \(\chi_q\) be the quadratic character of \(\mathbb F_q\), extended by \(\chi_q(0)=0\). Define
\[
\gamma_p=\begin{cases}1,&p\equiv1\pmod4,\\ i,&p\equiv3\pmod4,\end{cases}\qquad
\gamma_q=(-1)^{r-1}\gamma_p^r,\qquad B_q=q(q-1)(q+1).
\]
For \(s\in\{-1,1\}\) and \(t\in\mathbb F_p\), let
\[
\omega_{s,t}=\gamma_q^3s\zeta_p^t,
\quad H(t)=p^{r-1}-\mathbf1_{t=0},\quad
S(t)=\sum_{\substack{z\in\mathbb F_q\\\operatorname{Tr}(z)=t}}\chi_q(z).
\]
The explicit integer-valued trace sums are
\[
S(t)=\begin{cases}
\gamma_q(p-1)p^{r/2-1},&r\text{ even},\ t=0,\\
-\gamma_qp^{r/2-1},&r\text{ even},\ t\ne0,\\
0,&r\text{ odd},\ t=0,\\
\gamma_q\gamma_p\chi_p(-t)p^{(r-1)/2},&r\text{ odd},\ t\ne0.
\end{cases}
\]
All \(2p\) possible \(\omega_{s,t}\) are pairwise distinct; some have zero multiplicity for \(r=1\). The **exact number of ordered triples of vectors drawn from three distinct bases** with phase \(\omega_{s,t}\) is
\[
\boxed{\mathcal N_q(s,t)=\frac{B_qq^2}{2}\bigl(H(t)+sS(t)+\mathbf1_{t=0}\bigr).}
\tag{1}
\]
In particular, \(\sum_{s,t}\mathcal N_q(s,t)=B_qq^3\). Formula (1) determines the entire spectrum of any three-vector Gram matrix via
\[
\det(\lambda I-G)=\lambda^3-3\lambda^2+3(1-q^{-1})\lambda
-\bigl(1-3q^{-1}+2q^{-3/2}\operatorname{Re}\Omega\bigr).
\tag{2}
\]
For \(q=3\), exactly \(216\) ordered triples (equivalently \(36\) unordered triples) from distinct bases are linearly dependent, and each such Gram matrix has eigenvalues \(\{0,1,2\}\). For every odd \(q\ge5\), all these three-vector families are independent.

## Assumptions and scope
Set \(F=\mathbb F_q\), let \(\operatorname{Tr}:F\to\mathbb F_p\) be the absolute trace, and \(\psi(z)=\zeta_p^{\operatorname{Tr}(z)}\). All inner products are conjugate-linear in their first coordinate. A finite-indexed basis \(\mathcal B_a\), with \(a\in F\), has vectors
\[
\phi_{a,b}(x)=q^{-1/2}\psi(ax^2+bx),\qquad b,x\in F.
\]
The remaining basis \(\mathcal B_{\infty}\) has vectors \(\phi_{\infty,b}=\mathbf1_{x=b}\). Triple means an *ordered* choice of distinct basis indices and an ordered choice of one vector from each; bases and labels are part of the sample, not identified under symmetry. There are \(B_q=(q+1)q(q-1)\) ordered basis triples and \(q^3\) vector triples above each. A change of scalar phases for individual vectors does not affect \(\Omega\).

## Proof
**1. Gauss sums and all individual triple phases.** The classical finite-field quadratic Gauss sum gives, for every \(A\in F^\times\) and \(t\in F\),
\[
\sum_{x\in F}\psi(Ax^2+tx)=\sqrt q\,\gamma_q\chi_q(A)\psi\bigl(-t^2/(4A)\bigr).
\tag{3}
\]
The evaluation \(\gamma_q=(-1)^{r-1}\gamma_p^r\) is the quadratic Hasse–Davenport lifting formula (with the positive square-root convention); in particular \(\gamma_q^2=\chi_q(-1)\) and \(\gamma_q^4=1\).

Take three finite slopes \(a,c,e\in F\), all distinct, and corresponding vector labels \(i,j,k\). Put \(A=c-a\), \(B=e-c\), \(K=AB(A+B)\), and \(T=B(j-i)-A(k-j)\). Each of \(A,B,A+B,K\) is nonzero. Applying (3) to the three pairwise inner products and completing the square yields
\[
\Omega(\phi_{a,i},\phi_{c,j},\phi_{e,k})
=\gamma_q\chi_q(K)\psi\bigl(-T^2/(4K)\bigr).
\tag{4}
\]
Indeed the product of the three quadratic-character factors equals \(\chi_q(-K)=\gamma_q^2\chi_q(K)\), and the three additive phases combine to \(-[B(j-i)-A(k-j)]^2/(4K)\).

If one basis is computational, cyclically rotate the ordered triple so that it is first (a cyclic rotation preserves \(\Omega\)). For finite slopes \(a,c\), distinct, let \(A=c-a\) and define \(s=h+(k-j)/(2A)\). Direct multiplication using (3) gives
\[
\Omega(\phi_{\infty,h},\phi_{a,j},\phi_{c,k})
=\gamma_q\chi_q(A)\psi(-As^2).
\tag{5}
\]
For every fixed ordered basis triple, the map \((i,j,k)\mapsto T\), or \((h,j,k)\mapsto s\), is a surjective \(F\)-linear map \(F^3\to F\): in (4) the coefficient of \(i\) is \(-B\ne0\); in (5) that of \(h\) is \(1\). Thus each field value has precisely \(q^2\) preimages.

At \(T=0\) or \(s=0\) the phase is \(\pm\gamma_q\). At a nonzero parameter put \(z=-T^2/(4K)\) or \(z=-As^2\). Equation (4) or (5), together with \(\gamma_q^2=\chi_q(-1)\), simplifies uniformly to
\[
\Omega=\gamma_q^3\chi_q(z)\psi(z),\qquad z\in F^\times.
\tag{6}
\]
For each fixed ordered basis triple, nonzero \(z\) has exactly \(2q^2\) preimages if its quadratic character agrees with the fixed quadratic class of the coefficient of the square, and none otherwise. The square coefficient's class is \(\chi_q(-K)\) for (4), respectively \(\chi_q(-A)\) for (5).

**2. Averaging over ordered basis triples.** Multiplying all finite slopes by any fixed nonsquare \(\rho\in F^\times\), while fixing the computational slope \(\infty\), permutes the ordered distinct-slope triples. In (4), \(K\) becomes \(\rho^3K\); in (5), \(A\) becomes \(\rho A\). Hence \(\chi_q(K)\) and \(\chi_q(A)\) each change sign, pairing precisely half the \(B_q\) ordered basis triples in each of the two quadratic classes. Consequently, the zero-parameter value \(+\gamma_q\) occurs \(B_qq^2/2\) times and \(-\gamma_q\) equally often. For each fixed \(z\ne0\), exactly \(B_q/2\) base triples admit \(z\), with \(2q^2\) label triples each. Thus \(\gamma_q^3\chi_q(z)\psi(z)\) occurs \(B_qq^2\) times for each fixed nonzero \(z\). This establishes the stronger **field-element-indexed** phase census before collapsing equal traces.

**3. Trace fibers and phase multiplicities.** A nonzero \(z\) contributes phase \(\omega_{s,t}\) precisely when \(\chi_q(z)=s\) and \(\operatorname{Tr}(z)=t\). The number of such \(z\) is \((H(t)+sS(t))/2\). Add \(B_qq^2/2\) for the zero-parameter contribution in each of the \(t=0\) phases: since \(\gamma_q^3\gamma_q^{-1}=\gamma_q^2=\pm1\), the two phases \(\pm\gamma_q\) are the same unordered pair as \(\omega_{\pm1,0}\). This proves (1).

For completeness, use the additive-character formula for the trace indicator and the quadratic Gauss sum \(G_q=\gamma_q\sqrt q\):
\[
S(t)=\frac{G_q}{p}\sum_{u\in\mathbb F_p^\times}\chi_q(u)\zeta_p^{-ut}.
\tag{7}
\]
The restriction of \(\chi_q\) to \(\mathbb F_p^\times\) is trivial if \(r\) is even and is \(\chi_p\) if \(r\) is odd. The first case yields \(p-1\) or \(-1\), according as \(t=0\) or not. In the second case the sum vanishes for \(t=0\), and for nonzero \(t\) equals \(\chi_p(-t)\gamma_p\sqrt p\). This proves the displayed evaluation of \(S(t)\), with all signs and powers of \(p\).

As \(p\) is odd, the values \(s\zeta_p^t\) for \(s\in\{\pm1\}\), \(t\in\mathbb F_p\), are distinct. For \(r=1\), trace is the identity, so exactly one quadratic sign occurs for each \(t\ne0\), whereas both signs occur for \(t=0\) through the zero-parameter contributions. Hence exactly \(p+1\) values occur. For \(r\ge2\), all trace-sign fibers for \(t\ne0\) are nonempty: for even \(r\), \(p^{r-1}>p^{r/2-1}\); for odd \(r\ge3\), \(p^{r-1}>p^{(r-1)/2}\). For \(t=0\), both phases occur even when one nonzero-character fiber vanishes, because the zero-parameter term remains positive. Thus all \(2p\) phases occur.

**4. Gram spectra and rank boundary.** The three unit vectors have off-diagonal Gram entries of common modulus \(q^{-1/2}\). Expanding the determinant of their Hermitian Gram matrix gives \(\det G=1-3q^{-1}+2q^{-3/2}\operatorname{Re}\Omega\); the sum of its principal two-minors is \(3(1-q^{-1})\). This proves (2). At \(q=3\), the phases from zero parameters are \(\pm i\) and give determinant zero. The two other phases have real part \(\sqrt3/2\) and give determinant \(1/3\); there are exactly \(B_qq^2=216\) ordered singular triples. Dividing by the six orderings gives \(36\) distinct unordered singular triples, with Gram eigenvalues \(0,1,2\). For \(q\ge5\), Gershgorin's theorem gives \(\lambda_{\min}(G)\ge1-2/\sqrt q>0\). The full claim follows.

## Verification
The self-contained Python programs `verify_mub.py` and `verify_extensions.py` require only the standard library. Run `python verify_mub.py` and `python verify_extensions.py` from a directory containing both files. The first constructs every vector in the quadratic MUBs over \(\mathbb F_3\), \(\mathbb F_5\), and \(\mathbb F_7\), and directly computes all normalized triple overlaps, comparing every one to the Gauss-sum phase formula and every phase count to the theorem. It checked respectively \(648\), \(15{,}000\), and \(115{,}248\) ordered triple overlaps, including all \(216\) dependent ordered triples at \(q=3\). The second independently constructs \(\mathbb F_9=\mathbb F_3[u]/(u^2+1)\), exhaustively checks all \(524{,}880\) ordered triples, verifies six phase multiplicities and the quadratic-character trace sums. Both programs printed `VERIFY_OK`. Their finite computations are corroboration, not proof for arbitrary \(q\); arbitrary \(q\) is covered by the algebraic argument above.

## Relationship to prior work
Klappenecker and Rötteler [1, Construction I] explicitly state the odd-prime-power Wootters–Fields MUB construction used here and prove projective \(2\)-design properties. Mutual unbiasedness fixes pairwise magnitudes, not the third-order gauge-invariant distribution in (1). Wootters and Fields [2] originated the construction; its complete original text was not available for direct comparison. Matolcsi–Matszangosz–Varga–Weiner [3, §3] introduce and study normalized Bargmann phase arrays (“Hadamard cubes”) for general MUB triplets, giving a precise alias for (1). Their general slice and reconstruction theorems, and their dimension-six study, do not state the explicit odd-field trace-sign census, the prime-versus-extension jump, or the exceptional rank-three boundary computed here. The classical quadratic Gauss evaluation (3) and the lifting formula are inputs, not claimed discoveries. The novelty claim is restricted to the complete global multiplicity formula (1), its support dichotomy, and the rank/spectral consequences (2).

## Limitations
The result is for the fixed canonical odd-characteristic quadratic MUB construction, not every unitarily inequivalent maximal MUB family, and not characteristic two. It counts ordered distinct-basis vector triples rather than unordered basis triples; all multiplicities depend on this explicit convention. Numerical tests cover four finite fields only; the unrestricted assertion rests on (3)–(7). The q=3 dependence statement does not extend to triples containing two vectors from a common basis. A historical equivalence in an inaccessible source cannot be excluded, and no independent mathematical audit or priority certification has been performed.

## References
[1] A. Klappenecker and M. Rötteler, *Mutually Unbiased Bases are Complex Projective 2-Designs*, first public arXiv version 2005-02-04, arXiv:quant-ph/0502031v1; https://arxiv.org/abs/quant-ph/0502031 (Construction I and §III).

[2] W. K. Wootters and B. D. Fields, *Optimal state-determination by mutually unbiased measurements*, Annals of Physics **191** (1989), 363–381; DOI:10.1016/0003-4916(89)90322-9. Abstract and metadata consulted; original complete article not inspected.

[3] M. Matolcsi, Á. K. Matszangosz, D. Varga and M. Weiner, *Triplets of mutually unbiased bases*, Journal of Algebraic Combinatorics **63** (2026), article 26, https://doi.org/10.1007/s10801-026-01506-x, §3 and §4, openly accessible full article.

[4] Classical quadratic Gauss-sum evaluation and Hasse–Davenport lifting identity; see e.g. R. Lidl and H. Niederreiter, *Finite Fields*, Cambridge University Press, 1997, chapters on additive and multiplicative character sums.
