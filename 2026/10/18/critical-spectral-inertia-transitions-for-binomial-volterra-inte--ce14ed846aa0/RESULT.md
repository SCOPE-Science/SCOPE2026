# Critical spectral-inertia transitions for binomial Volterra integration on the Bergman disk

## Finding

Let \(A^2(\mathbb D)\) be the analytic Bergman space for normalized planar area measure, and let \(1\le m<n\) be integers. For complex coefficients \(a,b\), not both zero, put \(g(z)=az^m+bz^n\) and
\[
(T_gf)(z)=\int_0^z f(w)g'(w)\,dw,\qquad H_g=T_g^*T_g-T_gT_g^*.
\]
Then \(H_g\) is a nonzero trace-class self-adjoint operator of trace zero. Its ordered singular values satisfy, for some positive constants depending on the parameters,
\[
 c j^{-3}\le s_j(H_g)\le Cj^{-3}\qquad(j\ge j_0).
\]
Consequently, for every \(p>0\), \(H_g\in\mathcal S_p\) if and only if \(p>1/3\). There are infinitely many strictly negative eigenvalues. When \(ab\ne0\), write \(r=|a|/|b|\). **There are infinitely many strictly positive eigenvalues precisely when**
\[
 \frac nm\le r<\left(\frac nm\right)^2.
\]
In every other case (including a vanishing coefficient) there are finitely many, but at least one, strictly positive eigenvalues. In particular the lower transition endpoint is included and the upper endpoint is excluded; neither conclusion follows from the leading asymptotic alone.

## Assumptions and scope

All Hilbert-space inner products and adjoints refer to the normalized unweighted complex Bergman space on the open unit disk. The basis is \(e_k(z)=\sqrt{k+1}\,z^k\), indexed by \(k\ge0\), with \(\langle e_k,e_\ell\rangle=\delta_{k\ell}\). The two exponents are distinct positive integers; the coefficients are arbitrary complex numbers except that both cannot vanish. The phrase “infinitely many positive eigenvalues” counts algebraic multiplicities of nonzero discrete eigenvalues, and likewise for negative eigenvalues. Schatten classes here include the quasi-Banach exponents \(0<p<1\).

## Proof

**1. A sparse exact matrix.** For any positive integer \(h\) define
\[
 w_{k,h}=\frac{h\sqrt{k+1}}{(k+h)\sqrt{k+h+1}}\quad(k\ge0),
 \qquad w_{k,h}=0\quad(k<0).
\]
Direct integration gives
\[
 T_ge_k=a w_{k,m}e_{k+m}+b w_{k,n}e_{k+n}.
\]
Write \(q=n-m\). The matrix of \(H_g\) has diagonal \(d_k\), a single upper diagonal \(c_k\) at displacement \(q\), and its conjugate lower diagonal:
\[
\begin{aligned}
 d_k={}&|a|^2(w_{k,m}^2-w_{k-m,m}^2)
       +|b|^2(w_{k,n}^2-w_{k-n,n}^2),\\
 c_k={}&a\overline b\bigl(w_{k,n}w_{k+q,m}-w_{k-m,m}w_{k-m,n}\bigr).
\end{aligned}
\]
The expression for \(c_k\) can equivalently be written, when \(k\ge m\), as
\[
\frac{a\overline b\,mn}{\sqrt{(k+1)(k+q+1)}}
\left[\frac{(k+1)(k+q+1)}{(k+n)^2(k+n+1)}-\frac{k-m+1}{k(k+q)}\right].
\]
In particular, all entries and asymptotics below are derived from explicit rational expressions and square roots, without assumptions about a normal operator.

**2. The tail coefficients and their exact critical signs.** Set
\[
 Q=m^3|a|^2+n^3|b|^2,\quad
 P=m^4|a|^2+n^4|b|^2,\quad
 B=mn(m+n)|ab|.
\]
Expansion of the expressions in step 1 (with \(m,n\) fixed) yields
\[
\begin{aligned}
 d_k&=-\frac{2Q}{k^3}+\frac{6P}{k^4}+O(k^{-5}),\\
 c_k&=a\overline b\,mn\left[-\frac{m+n}{k^3}
  +\frac{-m^2+8mn+5n^2}{2k^4}+O(k^{-5})\right].
\end{aligned}
\]
For \(ab\ne0\) the entries \(c_k\) have, past a fixed index, a common phase. Each residue-class chain modulo \(q\) can be conjugated by a diagonal unitary to give positive upper entries \(\beta_k=|c_k|\) on its tail. Define \(V_k=d_k+\beta_{k-q}+\beta_k\). The above expansion gives
\[
 V_k=\frac{2(B-Q)}{k^3}+\frac{W}{k^4}+O(k^{-5}),
 \qquad W=2\bigl[3P-mn|ab|(m^2+4mn+n^2)\bigr].
\]
If \(b\ne0\) and \(r=|a|/|b|\), exact factorization gives
\[
 Q-B=m^3|b|^2\left(r-\frac nm\right)
 \left(r-\left(\frac nm\right)^2\right).
\]
At the two zeros of \(B-Q\), direct substitution into the next coefficient gives, respectively,
\[
 W\big|_{r=n/m}=4n^2(n-m)^2|b|^2>0,
 \qquad
 W\big|_{r=(n/m)^2}=-\frac{2n^3(n-m)^2}{m}|b|^2<0.
\]
These nonzero fourth-order terms decide the two opposite endpoint conventions. Their formulas follow by elementary expansion of the exact entries (or symbolic polynomial multiplication after clearing the strictly positive denominators); no numerical extrapolation is involved.

**3. Tail quadratic-form identity and inertia.** For finitely supported coordinates \(x_k\) in a sufficiently remote residue-class tail, extend them by zero outside their support. After the above unitary gauge,
\[
 \langle H_gx,x\rangle=\sum_k V_k|x_k|^2
 -\sum_k\beta_k|x_{k+q}-x_k|^2.
\]
For \(B<Q\), or for the upper critical equality where \(W<0\), there is a tail on which every \(V_k<0\). The identity makes the compression to that tail negative definite. The orthogonal complement is finite dimensional, so the min–max principle bounds the number of positive eigenvalues by a finite number. A vanishing coefficient gives \(\beta_k=0\) and \(d_k<0\) eventually, yielding the same conclusion.

For \(B>Q\) the potential is eventually positive of order \(k^{-3}\). On a distant, fixed-length consecutive segment in one residue chain, choose a real tent function vanishing at both endpoints. The Dirichlet-cost-to-mass ratio is \(O(L^{-2}k^{-3})\), while the positive-potential-to-mass ratio is comparable to \(k^{-3}\); choose the integer segment length \(L\) large enough first, then move it arbitrarily far out. Infinitely many pairwise separated positive test vectors result. They span positive-definite subspaces of arbitrarily large dimension, so the positive spectral subspace is infinite dimensional.

At the **lower critical equality**, \(V_k\ge c k^{-4}\) eventually, while \(\beta_k\le Ck^{-3}\). Use a tent function on a residue-chain segment of length \(L=\lfloor K^{3/4}\rfloor\), starting near \(K\). Since \(qL=o(K)\), every index of the segment is asymptotic to \(K\). The positive contribution is at least \(c'K^{-4}\|x\|_2^2\), whereas the Dirichlet cost is at most \(C'K^{-3}L^{-2}\|x\|_2^2=o(K^{-4})\|x\|_2^2\). Separated such segments yield arbitrarily many independent positive directions. This proves inclusion of the lower endpoint. In every regime, \(d_k\sim-2Qk^{-3}<0\); arbitrarily many mutually nonadjacent distant basis coordinates therefore give negative-definite subspaces and infinitely many negative eigenvalues.

**4. Singular-value exponent and trace.** Because \(w_{k,h}=O((k+1)^{-1})\), the two-shift formula makes \(T_g\) Hilbert–Schmidt. Thus \(T_g^*T_g\) and \(T_gT_g^*\) are trace class with equal traces, proving \(H_g\in\mathcal S_1\) and \(\operatorname{tr}H_g=0\). The already-proved negative eigenvalues imply \(H_g\ne0\); since the trace is zero, there must also be at least one positive eigenvalue.

The matrix of \(H_g\) has bandwidth \(q\) and entries \(O((k+1)^{-3})\) outside its fixed initial rows. Truncating to the first \(N\) coordinate rows and columns leaves an operator of norm \(O(N^{-3})\), hence the approximation-number characterization gives \(s_j(H_g)\le Cj^{-3}\) for sufficiently large \(j\). Conversely, choose \(j\) large, mutually nonadjacent basis vectors with indices in \([j,C_qj]\). Their compressed matrix is diagonal, all entries at most \(-c_qj^{-3}\). The min–max principle gives at least \(j\) negative eigenvalues of magnitude \(\ge c_qj^{-3}\), hence \(s_j(H_g)\ge cj^{-3}\) after adjusting the constants. Consequently \(\sum_js_j(H_g)^p<\infty\) precisely for \(3p>1\).

## Verification

The standalone standard-library program `verify.py` recomputes the displayed matrix independently from finite shift matrices, checks rational diagonal and squared off-diagonal formulas, and compares scaled asymptotic coefficients for numerous exponents and coefficient choices. It also checks positive remote blocks in the strict interval and, at both critical ratios, the sign of the next-order potential by 65-digit Decimal arithmetic. At the lower endpoint it exhibits additional explicit positive remote tent vectors. Run `python3 verify.py` from a directory containing this file; expected successful output is `VERIFICATION_OK 5485`. These finite calculations are reproducibility tests, not a proof of the infinitely many eigenvalues or the sharp infinite-rank exponent. Those conclusions follow from the preceding min–max and asymptotic arguments.

## Relationship to prior work

Aleman and Siskakis (1997) established foundational boundedness and Schatten-membership criteria for the integration operator \(T_g\) on Bergman spaces; their Section 5 explicitly studies \(T_g^*T_g\) but does not provide the signed spectral inertia or the \(\mathcal S_p\) boundary of the **difference** \(T_g^*T_g-T_gT_g^*\). Pau and Peláez (2013 preprint) present analogous Schatten classifications for \(T_g\) on Dirichlet-type spaces and recover the classical Bergman case. Related investigations of hyponormal Toeplitz operators on Bergman spaces concern Toeplitz operators, not this Volterra integration commutator. The present assertion is the combined signed-inertia boundary and sharp singular-value order for binomial analytic Volterra symbols. No novelty is claimed for the basic shift matrix, the Hilbert–Schmidt criterion for \(T_g\), or the min–max principle. The published literature comparison and its residual search limitations are recorded separately in `AUDIT.json`.

## Limitations

The result assumes the **unweighted** Bergman space, two positive monomial exponents, and a polynomial with at most two nonzero monomials. It does not classify the exact *finite* number of positive eigenvalues outside the infinite-inertia interval, compute each nonzero eigenvalue, or establish sharp leading constants in \(s_j(H_g)\asymp j^{-3}\). The eigenvalue assertion is mathematical, not an independently certified bibliographic priority claim; other historical or unindexed literature may overlap.

## References

1. A. Aleman and A. G. Siskakis, “Integration operators on Bergman spaces,” *Indiana University Mathematics Journal* **46** (1997), 337–356. DOI: 10.1512/iumj.1997.46.1373. Relevant material: §5, Schatten criteria for \(T_g\); accessible full text at https://www.researchgate.net/publication/243105024_Integration_operators_on_Bergman_spaces.
2. J. Pau and J. A. Peláez, “Schatten classes of integration operators on Dirichlet spaces,” arXiv:1302.2417v1, publicly posted 2013-02-11, https://arxiv.org/abs/1302.2417. Relevant material: Introduction and relationship to Bergman spaces.
3. Ž. Čučković and R. E. Curto, “A new necessary condition for the hyponormality of Toeplitz operators on the Bergman space,” *Journal of Operator Theory* **79** (2018), 287–300. DOI: 10.7900/jot.2017feb15.2152. Distinct Toeplitz, not Volterra, objects.
