# Arithmetic parity jumps in Möbius-ladder quantum average mixing

## Finding
For every integer \(n\ge3\), the infinite-time average-mixing matrix of the unweighted Möbius ladder has rank
\[
\operatorname{rank}\widehat M_n
=n+3\mathbf1_{\{n\equiv3\pmod6\}}+2\mathbf1_{\{n\equiv2\pmod4\}}.
\]
This has a universal baseline of \(n\), with a jump of three exactly when \(n\) is an odd multiple of three and a jump of two exactly when \(n\equiv2\pmod4\). All ranks and Fourier nullspaces are determined analytically, without restricting the order of the ladder beyond \(n\ge3\).

## Assumptions and scope
Let \(N=2n\). The graph \(L_n\) has vertices \(\mathbb Z/N\mathbb Z\) and the undirected edges \(j\sim j\pm1\) and \(j\sim j+n\). Because \(n\ge3\), these are three distinct neighbors, so this is a finite connected simple cubic graph. Write \(S\) for cyclic translation by one position and use the real symmetric adjacency Hamiltonian
\[
H_n=S+S^{-1}+S^n.
\]
For \(U(t)=\exp(itH_n)\), define the instantaneous transition-probability matrix \(M(t)_{uv}=|U(t)_{uv}|^2\) and the Cesàro average \(\widehat M_n=\lim_{T\to\infty}T^{-1}\int_0^T M(t)\,dt\). The limit exists since the spectrum is finite. Throughout, rank means rank over \(\mathbb R\) (equivalently over \(\mathbb C\) for this real matrix); Fourier indices are taken modulo \(N\).

For \(\chi_q(j)=\exp(2\pi i qj/N)\), the **complete** set of positive-eigenvalue Fourier modes is
\[
\mathcal F_n=\{0,2,4,\ldots,2n-2\}\cup
\begin{cases}
\{n/3,n,5n/3\},&n\equiv3\pmod6,\\
\{n/2,3n/2\},&n\equiv2\pmod4,\\
\varnothing,&\text{otherwise}.
\end{cases}
\]
Thus \(\ker\widehat M_n=\operatorname{span}\{\chi_q:q\notin\mathcal F_n\}\); conjugate pairs give the corresponding real cosine/sine description. This formula treats the smallest permissible ladder \(n=3\) and every larger size.

## Proof
**1. Spectral Fourier reduction.** Since \(S\chi_k=\exp(2\pi ik/N)\chi_k\), the adjacency eigenvalues are
\[
\lambda_k=2\cos(\pi k/n)+(-1)^k,\qquad 0\le k<N.
\]
Let \(E_\lambda\) be the orthogonal projector onto the eigenspace associated with a distinct eigenvalue \(\lambda\). Time averaging eliminates different-frequency cross terms, giving
\[\widehat M_n=\sum_\lambda E_\lambda\circ E_\lambda.\]
For an offset \(r=u-v\) modulo \(N\), the projector entries are
\[
E_\lambda(r)=\frac1N\sum_{k:\lambda_k=\lambda}\exp(2\pi ikr/N).
\]
The energy sets are closed under \(k\mapsto-k\), so \(E_\lambda(r)\) is real and even in \(r\). Consequently, the circulant kernel of \(\widehat M_n\) has the nonnegative Fourier coefficients
\[
\boxed{\mu_q=\frac1N\#\big\{(k,\ell):\lambda_k=\lambda_\ell,\ k+\ell\equiv q\pmod N\big\}.}
\]
Indeed, expand \(\sum_\lambda |E_\lambda(r)|^2\), use \(\lambda_{-\ell}=\lambda_\ell\), and apply Fourier orthogonality. In particular, \(\mu_q>0\) precisely when at least one such ordered pair exists. The pairs \((k,k)\) ensure that every even \(q\) occurs, and there are exactly \(n\) even modes.

**2. Same-parity pairs yield no additional modes.** If \(k\) and \(\ell\) have the same parity and \(\lambda_k=\lambda_\ell\), then
\(\cos(\pi k/n)=\cos(\pi\ell/n)\), hence \(\ell\equiv k\) or \(\ell\equiv-k\pmod N\). In either case \(k+\ell\) is even. Thus every possible additional positive Fourier coefficient must arise from an equal-energy pair of opposite parity.

**3. Cyclotomic rigidity lemma.** Suppose rational multiples \(\alpha,\beta\) of \(\pi\) satisfy \(\cos\alpha-\cos\beta=1\). Then
\[
(\cos\alpha,\cos\beta)\in\{(0,-1),(1/2,-1/2),(1,0)\}.
\]
To prove this, work in a cyclotomic field containing \(a=2\cos\alpha\) and \(b=2\cos\beta=a-2\). Both are algebraic integers. Under every complex field embedding into \(\mathbb C\), they remain real numbers in \([-2,2]\) because every conjugate of a sum \(\zeta+\zeta^{-1}\) of roots of unity is of the same form. The embedded relation \(a-b=2\) therefore forces every conjugate of \(a\) into \([0,2]\). All conjugates of the algebraic integer \(c=a-1\) lie in \([-1,1]\). If \(c\ne0\), its algebraic norm is a nonzero integer, while its absolute value is a product of factors at most one. Hence each conjugate has absolute value one. In particular \(c=\pm1\), and if \(c=0\) the conclusion is immediate. Thus \(a\in\{0,1,2\}\), yielding the three displayed pairs. No finite-enumeration assumption enters this lemma.

**4. Exhaust all opposite-parity collisions.** Choose an odd Fourier index \(o\) and an even Fourier index \(e\) with the same eigenvalue. Because \(\lambda_k=\lambda_{N-k}\), each can be represented in \([0,n]\), preserving its parity. Equality is precisely
\[\cos(\pi o/n)-\cos(\pi e/n)=1.\]
The rigidity lemma leaves three cases. The pair \((1,0)\) is impossible because \(\cos(\pi o/n)=1\) within \([0,n]\) would require \(o=0\), not odd.

For \((0,-1)\), the only possible representatives are \(o=n/2\) and \(e=n\). Their required parities hold exactly when \(n\equiv2\pmod4\). The full associated cross-parity energy class is \(\{n/2,n,3n/2\}\). Its mixed-parity sums supply exactly the two additional Fourier indices \(n/2\) and \(3n/2\).

For \((1/2,-1/2)\), the representatives are \(o=n/3\) and \(e=2n/3\). Their required parities hold exactly when \(n\equiv3\pmod6\). The full cross-parity energy class is \(\{n/3,2n/3,4n/3,5n/3\}\). Its mixed-parity sums supply precisely \(n/3\), \(n\), and \(5n/3\).

No other cross-parity collisions exist. Every additional index just listed is odd and therefore was not among the baseline even modes. The two exceptional congruence classes are disjoint. Counting all positive Fourier eigenvalues proves the rank formula and the stated kernel classification. \(\square\)

## Verification
The accompanying standalone `verify.py` uses integer polynomial arithmetic only. It constructs the exact cyclotomic polynomial for each order, represents each adjacency eigenvalue as an element of a cyclotomic quotient, groups exactly equal energies, and checks the predicted positive Fourier support and rank for each \(3\le n\le120\) (graph sizes six through 240). It also checks the predicted structure of every cross-parity collision. Run with `python3 verify.py` from the directory containing the extracted file. The actual check returns `VERIFY_OK exact_cyclotomic_orders=118 graph_vertices=6..240 exceptional_orders= 49`.

These 118 exact finite checks corroborate, but do not replace, the all-order proof. No numerical tolerance, root-finding or presumed spectral separation is used by the verifier.

## Relationship to prior work
Godsil's general theory [1] supplies the average-mixing projector decomposition. Coutinho and collaborators [2] develop exact methods for average mixing with irrational quantum-walk eigenvalues; neither inspected source establishes the Möbius-ladder Fourier support or the two arithmetic exceptional families in this theorem. Zhao and collaborators [3] analyze spinless-particle hopping on a Möbius ladder and its topological spectral and transport effects, making this a same-object comparison. Their inspected spectral/optical/decoherence analysis does not give the long-time average-mixing rank and nullspace formula. Ordinary prisms \(C_n\square K_2\) have different adjacency spectra and do not automatically determine the Möbius-ladder average-mixing matrix.

## Limitations
The statement is for the unweighted, zero-diagonal adjacency walk on the simple Möbius ladder, with all edge couplings equal to one. It does not classify arbitrary magnetic phases, nonuniform rung weights, finite-time mixing, vertex-dependent potentials, or unrelated graph families. The method supplies a family theorem, not a general formula beyond this graph class. The originality comparison is based on inspected literature and database searching; it does not constitute exhaustive priority certification, and an unlocated broader circulant spectral theorem remains a residual possibility. Independent assessment has not been performed.

## References
[1] C. Godsil, *Average mixing of continuous quantum walks*, arXiv:1103.2578, https://arxiv.org/abs/1103.2578.

[2] G. Coutinho, P. F. Baptista, C. Godsil, T. J. Spier, and R. Werner, *Irrational quantum walks*, arXiv:2208.08971 (first publicly submitted 2022-08-18), https://arxiv.org/abs/2208.08971; SIAM Journal on Applied Algebra and Geometry **7** (2023), 567–584, DOI:10.1137/22M1521262.

[3] N. Zhao, H. Dong, S. Yang, and C. P. Sun, *Observable topological effects in molecular devices with Möbius topology*, Physical Review B **79** (2009), 125440, arXiv:0809.0731, https://arxiv.org/abs/0809.0731; DOI:10.1103/PhysRevB.79.125440.

[4] G. Coutinho, C. Godsil, K. Guo and H. Zhan, *A New Perspective on the Average Mixing Matrix*, arXiv:1709.03591, https://arxiv.org/abs/1709.03591.
