# An explicit smooth critical-heat witness for Fock Toeplitz Schatten classes

## Finding
On the Gaussian Fock space \(\mathcal F^2(\mathbb C)\) with probability measure \(d\mu(z)=(2\pi)^{-1}e^{-|z|^2/2}\,dA(z)\), there is a **deterministically specified, real-valued \(C^\infty\) symbol** \(g\) such that:

\[
 gk_a\in L^2(d\mu)\quad\text{for every }a\in\mathbb C,\qquad
 T_g\in\bigcap_{p>1}\mathcal S_p\setminus\mathcal S_1,
\]

and its critical heat transform \(Hg=g^{(1/4)}\), given by
\[
 Hg(a)=\frac1\pi\int_{\mathbb C}g(z)e^{-|z-a|^2}\,dA(z),
\]
obeys \(Hg(R_j)\ge 3j/2\) along an explicitly recursively selected increasing sequence of positive integers \(R_j\). The support of \(g\) is the disjoint union of narrow, concentric-annular supports centered at these integers. The construction needs no selection by a category or existence theorem.

The novelty claimed here is the *specified smooth real witness and constructive trace-norm blocks*, **not** the previously proved abstract existence of an admissible symbol with all \(p>1\) Schatten memberships and an unbounded critical heat transform.

## Assumptions and scope
Let \(e_n(z)=z^n/(2^{n/2}\sqrt{n!})\) for \(n\ge0\), and let \(P_n\) denote projection onto \(\mathbb Ce_n\). Let \(J e_n=(-1)^n e_n\). For a smooth compactly supported real radial symbol \(f(z)=F(|z|^2/2)\),
\[
 T_fe_n=\lambda_n(f)e_n,\qquad
 \lambda_n(f)=\frac1{n!}\int_0^\infty F(s)e^{-s}s^n\,ds.
\]

Define a single fixed nonnegative, nonzero smooth bump
\[
 b(u)=\begin{cases}
 \exp\!\left[-1/((u-1)(2-u))\right],&1<u<2,\\
 0,&\text{otherwise},
 \end{cases}
 \quad Z=\int_1^2b(u)\,du,
 \quad \rho_\varepsilon(s)=\frac{b(s/\varepsilon)}{\varepsilon Z}.
\]
Thus \(\int\rho_\varepsilon=1\) and \(\operatorname{supp}\rho_\varepsilon\subset[\varepsilon,2\varepsilon]\). For each integer \(j\ge1\), put
\[
 N_j=2^{j^2},\quad\varepsilon_j=N_j^{-3},\quad c_j=j/N_j,\quad
 B_j(z)=c_j e^{s}\sum_{m=0}^{N_j-1}\rho_{\varepsilon_j}^{(m)}(s),
 \quad s=|z|^2/2.
\]
All derivatives here are ordinary derivatives in \(s\), and every \(B_j\) is a completely specified real \(C_c^\infty(\mathbb C)\) function supported in \(|z|<1\).

Set the finite positive constants
\[
 L_j=(2\pi)^{-1/2}\|B_j\|_{L^2(dA)},\qquad
 M_j=\pi^{-1}\|B_j\|_{L^1(dA)}.
\]
Define \(R_0=0\). Inductively, \(R_j\) is the **least integer** \(R\ge R_{j-1}+4\) such that
\[
 L_j\exp\!\left(-\frac{(R-1)^2}{4}+\frac{j(R+1)}2\right)<2^{-j},
\]
and, for every \(1\le i<j\),
\[
 (M_i+M_j)\exp\!\left(-(R-R_i-1)^2\right)<2^{-i-j-4}.
\]
Each finite set of strict inequalities is eventually satisfied as \(R\to\infty\), so this defines unique finite integers with no arbitrary choices. The integrals and inequalities involve the fixed elementary smooth bump, so the recursion is constructive to any requested finite index. Finally set
\[
 g(z)=\sum_{j=1}^\infty B_j(z-R_j).
\]
The sum is locally finite because the supports have radius less than one and the centers differ by at least four.

## Proof
**1. Exact finite-rank approximants.** For every \(m\ge0\) and \(\varepsilon>0\) define
\[
 G_{m,\varepsilon}(z)=(-1)^m e^s\rho_\varepsilon^{(m)}(s),\qquad s=|z|^2/2.
\]
Repeated integration by parts (all boundary terms vanish) gives, for every integer \(n\ge0\),
\[
 \lambda_n(G_{m,\varepsilon})=
 \begin{cases}
 0,&n<m,\\
 \displaystyle\frac1{(n-m)!}\int\rho_\varepsilon(s)s^{n-m}\,ds,&n\ge m.
 \end{cases}
\]
In particular, \(\lambda_m=1\). All other eigenvalues are nonnegative, and their sum is at most \(e^{2\varepsilon}-1\). Hence the exact trace-norm estimate is
\[
 \|T_{G_{m,\varepsilon}}-P_m\|_{\mathcal S_1}
 =\int\rho_\varepsilon(s)(e^s-1)\,ds\le e^{2\varepsilon}-1.
\]
This explicitly approximates *any selected monomial projection in trace norm* by a smooth, compactly supported radial Toeplitz symbol.

**2. Alternating blocks and Schatten bounds.** Because \(B_j=c_j\sum_{m=0}^{N_j-1}(-1)^mG_{m,\varepsilon_j}\), the triangle inequality gives
\[
 \left\|T_{B_j}-c_jJP_{<N_j}\right\|_{\mathcal S_1}
 \le c_jN_j(e^{2\varepsilon_j}-1)=j(e^{2\varepsilon_j}-1),
\]
where \(P_{<N}=\sum_{m=0}^{N-1}P_m\). Consequently, for every \(p\ge1\),
\[
 \|T_{B_j}\|_{\mathcal S_p}
 \le j N_j^{1/p-1}+j(e^{2N_j^{-3}}-1).
\]
For fixed \(p>1\), both series over \(j\) converge since \(N_j=2^{j^2}\). Weyl covariance of Fock Toeplitz operators gives
\(\|T_{B_j(\cdot-R_j)}\|_{\mathcal S_p}=\|T_{B_j}\|_{\mathcal S_p}\).

**3. Smoothness, admissibility, and operator identification.** Define
\[
 q_m(f)^2=(2\pi)^{-1}\int_{\mathbb C}|f(z)|^2e^{-|z|^2/2+m|z|}\,dA(z)
\quad(m\ge0).
\]
For \(R>1\), support of \(B_j(\cdot-R)\) lies in \(|z-R|<1\), whence
\[
 q_m(B_j(\cdot-R))\le L_j
 \exp\!\left[-(R-1)^2/4+m(R+1)/2\right].
\]
For \(j\ge m\), the defining inequality yields \(q_m(B_j(\cdot-R_j))<2^{-j}\). The finite earlier terms have finite seminorms. Thus \(q_m(g)<\infty\) for every \(m\), and \(g\) is a smooth admissible symbol: \(gk_a\in L^2(d\mu)\) for every normalized Fock kernel \(k_a\). In fact partial sums converge in every \(q_m\), hence after multiplication by each \(k_a\) in \(L^2(d\mu)\). Applying the Fock projection identifies \(T_g\) on coherent kernels with the norm-convergent operator sum \(\sum_jT_{B_j(\cdot-R_j)}\). By Step 2 the latter sum converges in every \(\mathcal S_p\) with \(p>1\).

**4. Exact heat peaks.** In one complex dimension the critical heat transform of a radial compact symbol is
\(HB_j(0)=2\int_0^\infty B_j(s)e^{-2s}\,ds\). Integrating each derivative by parts against \(e^{-s}\) gives the *exact* identity
\[
 HB_j(0)=2c_jN_j\int_0^\infty\rho_{\varepsilon_j}(s)e^{-s}\,ds
 =2j\int\rho_{\varepsilon_j}(s)e^{-s}\,ds
 \ge2j e^{-2\varepsilon_j}.
\]
If \(|a|>1\), the support bound implies
\[
 |HB_j(a)|\le M_j\exp[-(|a|-1)^2].
\]
Using the defining pairwise distance inequalities, the sum of all contributions at \(R_j\) from blocks of index other than \(j\) is strictly smaller than \(2^{-j-4}\). Therefore
\[
 Hg(R_j)\ge 2j e^{-2\varepsilon_j}-2^{-j-4}
 \ge 2j e^{-1/4}-2^{-j-4}>\frac32j.
\]
The equality \(Hg=\sum_jH(B_j(\cdot-R_j))\) at every point follows from the \(q_m\)-convergence and Cauchy–Schwarz for the Gaussian heat integral.

**5. The trace-class endpoint is excluded.** The trace-class endpoint theorem of Virtanen (arXiv:2609.11853, Theorem 1.1(i)) states that every admissible Fock symbol whose Toeplitz operator is trace class has bounded critical heat transform, quantitatively \(\|Hg\|_\infty\le2\|T_g\|_{\mathcal S_1}\) in one complex dimension. Step 4 contradicts boundedness; therefore \(T_g\notin\mathcal S_1\). This finishes the single stated result.

## Verification
The supplied Python program `verify.py` checks 186 finite exact rational moment, eigenvalue, trace-pairing, and numerical majorant assertions. It uses the uniform probability law on a rational annulus as an independent computational surrogate; the proof above covers the actually specified smooth bump using integration by parts and positivity, without relying on that surrogate's regularity. The program does **not** certify infinitely many derivatives, infinitely many indices, or all real Schatten exponents. These are established by the preceding analytic bounds. The distance recursion is guaranteed to terminate by Gaussian decay; executing astronomically large instances is not required for the logical construction.

## Relationship to prior work
Virtanen, *The critical Schatten exponent for the Berger–Coburn endpoint problem*, arXiv:2609.11853v2, Theorem 1.1(ii), already proves the existence of **some** admissible symbol with \(T_g\in\mathcal S_p\) for all \(p>1\) and unbounded critical heat transform. That proof uses Baire category and explicitly notes it supplies no formula. The present result is a constructive strengthening with a fixed real smooth formula, a deterministic selection of separated supports, and explicit error and heat-growth bounds; it does not reassert the pre-existing existential implication as novel.

Looi, *A counterexample to the Berger–Coburn conjecture*, arXiv:2601.20859v1, constructs an explicit summation of translated Weyl-based building blocks giving a bounded Toeplitz operator with unbounded critical heat transform. Its displayed estimates control operator norm rather than all Schatten exponents \(p>1\), and its blocks differ from the trace-norm mollified monomial projections used here.

García and Maximenko, *Constructive approximation of convergent sequences by eigenvalue sequences of radial Toeplitz–Fock operators*, arXiv:2503.23276v1, provide constructive **uniform** approximation with bounded radial symbols. That is distinct from the present explicit **trace-norm** monomial-block estimates and critical heat application. No priority claim is made for integration by parts or Toeplitz covariance as isolated standard tools.

## Limitations
The formula is explicit in a recursive, finite-computation-per-index sense rather than a short closed expression for its translation centers. The resulting smooth symbol is unbounded and its annular amplitudes can be enormous; the statement does **not** extend to bounded symbols. The construction is on \(\mathbb C\) with the specified Gaussian normalization, and makes no claims about optimal growth rate, derivative regularity at infinity, or direct finite-time numerical evaluation of very high-order derivatives. The existence of a nonconstructive all-\(p>1\) example was already known. Older distributional Toeplitz approximation results could contain equivalent constructive machinery; independent literature-priority review remains outstanding.

## References
1. J. A. Virtanen, *The critical Schatten exponent for the Berger–Coburn endpoint problem*, arXiv:2609.11853v2 (first posted 2026-09-10), especially Theorem 1.1 and Lemmas 2.1–2.2.
2. S. Looi, *A counterexample to the Berger–Coburn conjecture*, arXiv:2601.20859v1 (2026), especially Sections 4–6.
3. K. E. García and E. A. Maximenko, *Constructive approximation of convergent sequences by eigenvalue sequences of radial Toeplitz–Fock operators*, arXiv:2503.23276v1 (2025), especially the radial moment formula and constructive approximation discussion.
4. C. A. Berger and L. A. Coburn, *Heat flow and Berezin–Toeplitz estimates*, American Journal of Mathematics 116 (1994), 563–590, for the original endpoint setting and covariance framework.
