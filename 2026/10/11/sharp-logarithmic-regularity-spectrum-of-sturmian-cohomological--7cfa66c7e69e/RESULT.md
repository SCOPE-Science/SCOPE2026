# Sharp logarithmic regularity spectrum of Sturmian cohomological transfers

## Finding

Let \(\alpha\in(0,1)\) be irrational and \(\theta\in(0,1)\). On the one-sided Sturmian subshift \(X_\alpha\), use the symbolic metric \(d_\theta(x,y)=\theta^{\ell(x,y)}\), where \(\ell(x,y)\) is the first disagreement index. Let \(\sigma\) be the left shift, \(\mu_\alpha\) its invariant measure, and \(\Phi(x)=x_0\). For a real Lipschitz observable \(f\) satisfying \(\int f\,d\mu_\alpha=0\), let \(c_f\) be the uniquely determined scalar in the Lipschitz cohomological decomposition of Huang--Jenkinson--Xu--Zhang [1]. Every continuous solution to \(f=w\circ\sigma-w\) is unique up to a constant.

For \(n\geq1\), let \(\Omega_n(w)\) be the largest oscillation of \(w\) on a length-\(n\) cylinder, and let \(G_n(\alpha)\) be the longest gap cut from the unit circle by \(\{0,-\alpha,\ldots,-n\alpha\}\pmod 1\). Then a Lipschitz function \(u_f\) can be chosen with \(w=u_f-c_f\tau\), where \(\tau\) is the canonical transfer in [1], and

\[
\left|\Omega_n(w)-|c_f|G_n(\alpha)\right|
\leq \operatorname{Lip}_{d_\theta}(u_f)\,\theta^n
\qquad(n\geq1).
\]

In particular, if \(c_f\neq0\), then \(\Omega_n(w)/G_n(\alpha)\to|c_f|\). Let \(p_k/q_k\) be the regular continued-fraction convergents of \(\alpha\), with \(q_0=1\). For every \(s\in(0,1]\), the following are equivalent:

\[
\sup_{n\geq1}n^s\Omega_n(w)<\infty
\quad\Longleftrightarrow\quad
\sup_{k\geq0}\frac{q_{k+1}^{s}}{q_k}<\infty,
\qquad(c_f\neq0).
\]

Consequently, writing \(\mu_{\mathrm{irr}}(\alpha)\in[2,\infty]\) for the usual irrationality exponent and interpreting \(1/\infty=0\),

\[
\sup\left\{s>0:\sup_{n\geq1}n^s\Omega_n(w)<\infty\right\}
=\frac{1}{\mu_{\mathrm{irr}}(\alpha)-1}.
\]

The supremum of an empty set is taken as zero. At the critical exponent, membership is decided by the stated continued-fraction supremum; the exponent alone does not decide endpoint membership. In particular, the endpoint \(s=1\) holds exactly when \(\alpha\) has bounded partial quotients. If \(c_f=0\), all continuous transfers are Lipschitz instead. For instance, a bounded-type slope and the slope \(\alpha=[0;1,2,3,\ldots]\) both have irrationality exponent two, but only the bounded-type slope attains the \(s=1\) endpoint for nonzero \(c_f\).

## Assumptions and scope

The shift and metric are the **one-sided** Sturmian model in [1], not the two-sided symbolic metric. A length-\(n\) cylinder is the set of sequences with a specified prefix in coordinates \(0,\ldots,n-1\). Its oscillation is \(\sup\{|w(x)-w(y)|:x,y\text{ in the cylinder}\}\). We define \(\Omega_n\) as the maximum over the \(n+1\) nonempty cylinders. The number \(G_n\) is the maximum of the \(n+1\) cyclic consecutive gaps formed by the points \(\{j\alpha\}\) with \(0\leq j\leq n\), equivalently by their negatives.

The theorem assumes only irrationality of \(\alpha\), Lipschitz regularity of the centered observable \(f\) in \(d_\theta\), and a **continuous** transfer \(w\). The latter exists for all such \(f\) by [1, Theorem D and Corollary 6.4]. We do not assume bounded partial quotients or a finite irrationality exponent. The irrationality exponent means \(\sup\{v:|\alpha-p/q|<q^{-v}\text{ for infinitely many coprime }p,q\}\).

## Proof

**1. The exact dynamical oscillation profile.** By [1, Theorem D], there are a unique scalar \(c_f\) and a Lipschitz function \(u_f\) such that \(f=c_f(\Phi-\alpha)+u_f\circ\sigma-u_f\). Proposition 6.1(ii) of [1] gives \(\Phi-\alpha=\tau-\tau\circ\sigma\), hence \(w=u_f-c_f\tau\) solves \(f=w\circ\sigma-w\). Minimality of \(X_\alpha\) makes any two continuous solutions differ by a constant.

By [1, Proposition 6.1(iii)], the image of each length-\(n\) cylinder under \(\tau\) is a closed interval whose length is the measure of that cylinder. By [1, Lemma 3.5(ii)], those cylinder measures are precisely the consecutive rotation gaps cut by \(\{0,-\alpha,\ldots,-n\alpha\}\). Therefore \(\Omega_n(\tau)=G_n\). On each cylinder, the oscillation of \(u_f\) is at most \(L\theta^n\), where \(L=\operatorname{Lip}_{d_\theta}(u_f)\). The elementary inequality

\[
\left|\operatorname{osc}_{C}(g+h)-\operatorname{osc}_{C}(g)\right|
\leq\operatorname{osc}_{C}(h)
\]

and the inequality \(\left|\max_i a_i-\max_i b_i\right|\leq\max_i|a_i-b_i|\) give \(\left|\Omega_n(w)-|c_f|G_n\right|\leq L\theta^n\). Since the gaps sum to one, \(G_n\geq(n+1)^{-1}\). Hence if \(c_f\neq0\), the additive error divided by \(G_n\) tends to zero and the profile ratio tends to \(|c_f|\). If \(c_f=0\), \(w=u_f\) is Lipschitz.

**2. Upper rotation-gap estimate.** The convergents satisfy \(\left|\alpha-p_k/q_k\right|<1/(q_kq_{k+1})\). For \(q_k\leq n+1<q_{k+1}\), consider the first \(q_k\) rotation points. For \(0\leq j<q_k\), the circular distance from \(\{j\alpha\}\) to \(\{jp_k/q_k\}\) is less than \(1/q_{k+1}\leq1/q_k\). Since multiplication by \(p_k\) permutes the residues modulo \(q_k\), the latter set is the uniform \(q_k\)-grid. Perturbing that grid by at most \(1/q_k\) can leave no gap longer than \(3/q_k\). Adding the remaining rotation points can only shorten gaps. Thus

\[
G_n\leq\frac{3}{q_k}\quad\text{whenever}\quad q_k\leq n+1<q_{k+1}.
\]

A harmless finite-index convention covers the initial repeated denominator \(q_0=q_1=1\), when present.

**3. Lower rotation-gap estimate at large partial quotients.** Fix \(k\) with \(q_{k+1}\geq8q_k\), and put \(N_k=\lfloor q_{k+1}/4\rfloor\). Each of the \(N_k+1\) points \(\{j\alpha\}\), \(0\leq j\leq N_k\), is within \(1/(4q_k)\) in circular distance of the \(q_k\)-grid, since \(j|\alpha-p_k/q_k|\leq1/(4q_k)\). The complement of the union of the \(q_k\) closed arcs of radius \(1/(4q_k)\) around the grid includes an empty arc of length \(1/(2q_k)\). Consequently,

\[
G_{N_k}\geq\frac{1}{2q_k},
\qquad N_k\geq\frac18 q_{k+1}.
\]

**4. Necessary and sufficient logarithmic power condition.** For \(0<s\leq1\), if \(B_s:=\sup_k q_{k+1}^s/q_k<\infty\), the upper estimate yields \(n^s G_n\leq3B_s\), apart from finitely many initial indices. Conversely, if \(\sup_n n^sG_n<\infty\), the lower estimate bounds \(q_{k+1}^s/q_k\) uniformly on indices with \(q_{k+1}\geq8q_k\). On every other index, \(q_{k+1}^s/q_k<8^s q_k^{s-1}\leq8^s\). This proves the equivalence for \(G_n\). The exponentially small additive error in Step 1 leaves the boundedness of \(n^s\Omega_n(w)\) unchanged when \(c_f\neq0\), proving the principal equivalence.

**5. Critical exponent and endpoint.** The standard convergent inequalities and best-approximation criterion yield

\[
\mu_{\mathrm{irr}}(\alpha)
=1+\limsup_{k\to\infty}\frac{\log q_{k+1}}{\log q_k}.
\]

Thus the supremal \(s\in(0,1]\) for which \(q_{k+1}^s/q_k\) is bounded is the reciprocal of the limsup on the right. The borderline value may or may not be attained; precisely the stated supremum test decides it. For \(s=1\), boundedness of \(q_{k+1}/q_k\) is equivalent, by \(q_{k+1}=a_{k+1}q_k+q_{k-1}\), to boundedness of the partial quotients. No exponent greater than one is possible for \(c_f\neq0\), since \(\Omega_n(w)\geq |c_f|/(2(n+1))\) for all large \(n\).

## Verification

The self-contained `verify.py` performs exact `fractions.Fraction` arithmetic for three long finite continued-fraction approximants. It enumerates circular gaps directly and checks the average-gap lower bound, the \(3/q_k\) upper estimate, and the \(1/(2q_k)\) lower estimate at eligible large-ratio convergents. Running `python verify.py` from the directory containing the script produced `PASS: 1564 exact rational finite gap assertions across 3 continued fractions`. These finite tests detect normalization or indexing errors but do not prove irrational-limit claims or the transfer decomposition. The proof above supplies those infinite steps using the cited source theorem and elementary rational approximation.

## Relationship to prior work

Huang, Jenkinson, Xu and Zhang [1] proved the Lipschitz cohomological decomposition and the exact interval image of the canonical transfer. Their Corollary 6.4 distinguishes Lipschitz transfers from continuous non-Hölder transfers, but does not determine the full logarithmic regularity spectrum, critical irrationality exponent, or the exponentially accurate oscillation profile for every transfer. Those are the results established here.

The three-gap/factor-frequency formulas themselves are **not new**: Berthé [2, Theorem 1], Alessandri--Berthé [3, Sections 1--3], and Julien--Putnam [4, Theorem 2.11] determine rotation-cylinder frequencies by continued fractions. In particular, the bounded-type versus unbounded-type distinction for \(nG_n\) is classical (see [3, Theorem 1]). The contribution is the stated precise all-observable cohomological oscillation law and sharp classification at **every** logarithmic power, including endpoint and Liouville behavior. It combines these established ingredients with the upper/lower large-convergent-scale argument above; it does not claim discovery of the three-gap theorem.

## Limitations

The conclusion concerns one-sided Sturmian subshifts and centered Lipschitz observables; no corresponding theorem is established here for general substitutions, multi-interval exchanges, arbitrary beta-shifts, or Hölder transfer functions on unrelated systems. The critical exponent is a supremum and does not assert endpoint attainment; the exact denominator-ratio condition supplies the endpoint test. Constants may depend on \(\alpha,\theta,f\). A finite rational experiment cannot certify the irrationality exponent, an infinite logarithmic modulus, or mathematical novelty. Related older formulations of cohomological moduli could affect priority; no independent validation is claimed.

## References

[1] W. Huang, O. Jenkinson, L. Xu, Y. Zhang, *Sturmian beta-shifts do not have typical periodic optimization*, arXiv:2610.03619v1 (first public 2026-10-02), Theorem D, Proposition 6.1, Corollary 6.4, https://arxiv.org/html/2610.03619v1.

[2] V. Berthé, *Fréquences des facteurs des suites sturmiennes*, Theoretical Computer Science **165** (1996), 295--309, Theorem 1; lawful author-hosted full text https://www.irif.fr/~berthe/Articles/st.pdf.

[3] P. Alessandri, V. Berthé, *Three distance theorems and combinatorics on words*, L'Enseignement Mathématique **44** (1998), 103--132; lawful author-hosted full text https://www.irif.fr/~berthe/Articles/3d.pdf.

[4] A. Julien, I. F. Putnam, *Spectral triples for subshifts*, Journal of Functional Analysis **270** (2016), 1031--1063, Theorem 2.11 and Section 5.4; arXiv:1411.6800v2, https://arxiv.org/pdf/1411.6800.
