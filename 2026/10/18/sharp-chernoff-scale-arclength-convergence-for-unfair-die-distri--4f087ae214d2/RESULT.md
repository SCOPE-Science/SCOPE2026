# Sharp Chernoff-scale arclength convergence for unfair-die distribution functions

## Finding

Let \(q\ge2\) be an integer and let \(p=(p_0,\ldots,p_{q-1})\) be a strictly positive, nonuniform probability vector. Independently draw infinitely many digits \(\xi_i\) with \(\Pr\{\xi_i=j\}=p_j\). Write \(F\) for the distribution function of
\[
X=\sum_{i=1}^{\infty}\xi_iq^{-i}.
\]
Let \(F_n\) be the polygonal interpolation of \(F\) at the mesh \(\{kq^{-n}:0\le k\le q^n\}\), and let \(L_n\) be the Euclidean length of its graph. Define
\[
\ell_j=\log(qp_j),\quad M(s)=\frac1q\sum_{j=0}^{q-1}e^{s\ell_j},\quad
s_* =\operatorname*{argmin}_{0\le s\le1}M(s),\quad \rho=M(s_*),
\]
\[
\pi_j=\frac{e^{s_*\ell_j}}{q\rho},\qquad
\sigma^2=\sum_{j=0}^{q-1}\pi_j\ell_j^2,\qquad
\phi(r)=1+r-\sqrt{1+r^2},\qquad
g(x)=e^{-s_*x}\phi(e^x).
\]
The minimizer is unique and interior, \(0<s_*<1\); moreover \(0<\rho<1\) and \(\sigma>0\). Set
\[
I=\frac{2^{s_*-1}}{s_*}B\left(\frac{s_*+1}{2},1-s_*\right),
\]
where \(B\) denotes Euler's beta function. **There are sharp asymptotics for both the remaining arclength deficit and the gain at the next refinement.**

If the finite set \(\{\ell_j\}\) is **nonarithmetic** (not contained in any translate of \(h\mathbb Z\) with \(h>0\)), then, as \(n\to\infty\),
\[
2-L_n=\frac{\rho^n}{\sqrt n}\left(\frac{I}{\sigma\sqrt{2\pi}}+o(1)\right),\qquad
L_{n+1}-L_n=\frac{\rho^n}{\sqrt n}\left(\frac{(1-\rho)I}{\sigma\sqrt{2\pi}}+o(1)\right).
\]

If \(\{\ell_j\}\) is **arithmetic**, let \(h>0\) be its maximal span, choose any \(a\in\{\ell_j\}\), and let \(\theta_n\) denote \(na\) modulo \(h\). Put
\[
\psi(x)=e^{-s_*x}\left[\phi(e^x)-\frac1q\sum_{j=0}^{q-1}\phi(e^{x+\ell_j})\right],
\]
\[
A(\theta)=\frac h{\sigma\sqrt{2\pi}}\sum_{k\in\mathbb Z}g(\theta+kh),\qquad
H(\theta)=\frac h{\sigma\sqrt{2\pi}}\sum_{k\in\mathbb Z}\psi(\theta+kh).
\]
Both sums converge absolutely and define continuous, strictly positive, \(h\)-periodic functions. In this case
\[
2-L_n=\frac{\rho^n}{\sqrt n}\bigl(A(\theta_n)+o(1)\bigr),\qquad
L_{n+1}-L_n=\frac{\rho^n}{\sqrt n}\bigl(H(\theta_n)+o(1)\bigr),
\]
with errors uniform in the phases; also \(H(\theta)=A(\theta)-\rho A(\theta+a)\). Consequently, **in every allowed case** both quantities are \(\Theta(\rho^n/\sqrt n)\). The same exponential rate \(-\log\rho\) is the Chernoff information separating one fair roll from one biased roll.

## Assumptions and scope

All digits are independent and identically distributed; all \(p_j\) are strictly positive and sum to one; the vector is not uniform; \(q\) is a fixed integer at least two. Limits refer to an increasing number \(n\) of base-\(q\) interpolation cells. Logarithms are natural. Arithmeticity concerns the real-valued log-likelihood increments \(\ell_j\), not the integer digit alphabet. The uniform distribution is outside the theorem: there \(L_n=\sqrt2\) for all \(n\). Vectors with one or more zero weights are deliberately excluded: their likelihood-tilting minimizer can lie on a boundary and require different asymptotics.

## Proof

**1. Exact finite-length and likelihood formula.** For every word \(w=(w_1,\ldots,w_n)\), its cell has horizontal length \(u_w=q^{-n}\) and vertical increment \(v_w=\prod_{i=1}^np_{w_i}\). Hence
\[
L_n=\sum_w\sqrt{u_w^2+v_w^2},\qquad
D_n:=2-L_n=\sum_w u_w\phi(v_w/u_w).
\]
The second identity uses \(\sum_wu_w=\sum_wv_w=1\). Let \(\ell(w)=\sum_{i=1}^n\ell_{w_i}\); then \(v_w/u_w=e^{\ell(w)}\). The derivatives of \(M\) satisfy
\[
M'(0)=-D(U\Vert P)<0,\qquad M'(1)=D(P\Vert U)>0,\qquad M''(s)>0,
\]
with \(U\) the uniform digit law. Strict signs follow from nonuniformity and full support. Thus \(s_*\in(0,1)\), \(\rho=M(s_*)<M(0)=M(1)=1\), and \(\pi\) is a positive probability vector with \(\sum_j\pi_j\ell_j=0\). Since not all \(\ell_j\) vanish, \(\sigma^2>0\).

**2. Exponential change of measure.** For each word, \(\prod_i\pi_{w_i}=\rho^{-n}u_we^{s_*\ell(w)}\). If \(S_n\) is the sum of \(n\) independent increments taking value \(\ell_j\) with probability \(\pi_j\), the exact identity is
\[
D_n=\rho^n\mathbb E_\pi[g(S_n)].
\]
Furthermore, subdividing every interval into \(q\) descendants gives
\[
D_n-D_{n+1}=\rho^n\mathbb E_\pi[\psi(S_n)].
\]
Here \(\phi''(r)=-(1+r^2)^{-3/2}<0\) and \(q^{-1}\sum_j e^{\ell_j}=1\). Strict Jensen concavity shows \(\psi(x)>0\) for every real \(x\); hence \(L_{n+1}>L_n\). Both \(g\) and \(\psi\) are continuous and exponentially decaying at either end, since \(0<s_*<1\) and \(0<\phi(r)<\min\{1,r\}\). In particular they are directly Riemann integrable.

**3. Apply the appropriate local limit theorem.** The finite-support tilted increments are centered with variance \(\sigma^2>0\). The nonarithmetic (Stone) local limit theorem for a directly Riemann integrable test function \(f\) gives
\[
\sqrt n\,\mathbb E_\pi[f(S_n)]\longrightarrow \frac{1}{\sigma\sqrt{2\pi}}\int_{\mathbb R} f(x)\,dx.
\]
For arithmetic increments on a maximal lattice \(a+h\mathbb Z\), the lattice local limit theorem and the exponential tails of \(f\) give
\[
\sqrt n\,\mathbb E_\pi[f(S_n)]
=\frac h{\sigma\sqrt{2\pi}}\sum_{k\in\mathbb Z} f(na+kh)+o(1),
\]
where the error is uniform in the residue class of \(na\) modulo \(h\). To justify the infinite sum, first restrict to \(|x|\le R\), use the local theorem uniformly there, then bound the complement by exponential decay and the standard \(O(n^{-1/2})\) concentration bound for every fixed-width interval (itself a consequence of the same local theorem). Apply these formulas to \(f=g\) and \(f=\psi\). The lattice sums are continuous and strictly positive: for \(g\) this is immediate; for \(\psi\) it follows from strict Jensen concavity, and compactness of a period supplies uniform positive lower bounds.

**4. Evaluate the universal constants.** The integral \(\int_{\mathbb R}g(x)\,dx\), after substituting \(r=e^x\), is
\[
\int_0^\infty r^{-s_*-1}\bigl(1+r-\sqrt{1+r^2}\bigr)\,dr.
\]
Integration by parts, followed by \(r=\sinh t\) and \(u=e^{-2t}\), gives
\[
\frac1{s_*}\int_0^\infty e^{-t}(\sinh t)^{-s_*}\,dt
=\frac{2^{s_*-1}}{s_*}B\left(\frac{s_*+1}{2},1-s_*\right)=I.
\]
The boundary terms vanish because \(0<s_*<1\). For every \(j\), shifting the integration variable by \(\ell_j\) gives
\[
\int_{\mathbb R} e^{-s_*x}\phi(e^{x+\ell_j})\,dx=e^{s_*\ell_j}I.
\]
Therefore \(\int\psi=\bigl(1-M(s_*)\bigr)I=(1-\rho)I\). This proves both nonarithmetic coefficients. In the arithmetic case the same lattice shift, using \(\ell_j\equiv a\pmod h\), gives \(H(\theta)=A(\theta)-\rho A(\theta+a)\). Together with Step 3 this proves the claimed formulas and the common order \(\Theta(\rho^n/\sqrt n)\).

## Verification

The accompanying standalone `CHECK.py` uses a word-by-word enumeration and an independent multinomial count formula to check the exact finite arclength identity for rational biased dice. It checks strict increase, the stable positive formula for the deficit, the unique Chernoff tilt numerically, and the beta-integral constant by independent quadrature. The checks concern finitely many levels and do **not** substitute for the local-limit proof. An example with \(q=3\), \(p=(1/6,1/3,1/2)\), is nonarithmetic because the increments are \(-\log2,0,\log(3/2)\) and their differences generate an additive group with irrational ratio \(\log3/\log2\). For \(q=2\) and \(p=(1/4,3/4)\), the increments are arithmetic, and the checker evaluates the phase-dependent prefactor.

Run from a directory containing the standalone file with `python3 CHECK.py`; no nonstandard Python dependencies are needed.

## Relationship to prior work

Pfeffer, Smith and Severa (arXiv:2309.07366, originally posted September 14, 2023) prove the finite arclength sum in their Theorem 4.2 and the limiting arclength \(2\) for an unfair die. Their Section 5.1 asks for a **direct quantitative account of the additional arclength at each iteration**; it does not give the sharp exponential rate, the \(n^{-1/2}\) correction, the beta prefactor, or the lattice-phase profile. The present finding derives these from a centered exponential likelihood tilt. Stone's classical local limit theorem supplies the standard probabilistic asymptotic input but does not identify the arclength observable or its special beta-function coefficient. General integral-representation methods for information divergences, as in Sason (2018), provide context for likelihood-based comparisons but do not state these geometric formulas. Classical Chernoff theory identifies the testing exponent \(-\log\rho\), not the arclength-specific exact prefactors; the problem-specific bridge and its lattice correction are essential here.

## Limitations

The result is for fixed, independent, identically distributed, strictly positive biased dice. It does not give a uniform estimate as the die approaches the uniform law; the \(n\to\infty\) asymptotics need not interchange with \(p\to U\). It does not cover missing digit outcomes, changing biases over time, or quantitative error terms beyond \(o(1)\) in the leading coefficients. Nonarithmeticity is necessary for a single constant prefactor: lattice inputs can have varying phase-dependent leading factors. The local-limit theorems used are classical external mathematical results, not reproved from first principles. Originality is assessed against accessible sources; unindexed asymptotic work remains a possible overlap risk.

## References

1. D. T. Pfeffer, J. D. Smith, W. Severa, *Induced Distributions from Generalized Unfair Dice*, arXiv:2309.07366v2 (2023), especially Theorem 4.2, Corollary 4.1 and Section 5.1. https://arxiv.org/html/2309.07366v2
2. C. J. Stone, *A Local Limit Theorem for Nonlattice Multi-Dimensional Distribution Functions*, Annals of Mathematical Statistics 36 (1965), 546–551. https://doi.org/10.1214/aoms/1177700165
3. I. Sason, *On f-Divergences: Integral Representations, Local Behavior, and Inequalities*, Entropy 20 (2018), 383; arXiv:1804.06334v3. https://arxiv.org/html/1804.06334v3
