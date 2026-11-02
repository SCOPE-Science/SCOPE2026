# Optimal Schatten commutator cost for square-zero operators

## Finding

Let \(H\) be a complex separable Hilbert space, let \(1\le p<\infty\), and let \(N\in S_p(H)\) satisfy \(N^2=0\). With \([X,Y]=XY-YX\), define the unconstrained two-factor Schatten cost
\[
\mathfrak c_p(N)=\inf\{\|X\|_{S_{2p}}\|Y\|_{S_{2p}}:\ X,Y\in S_{2p}(H),\ [X,Y]=N\}.
\]
Then the infimum is attained and its exact value is
\[
\boxed{\mathfrak c_p(N)=2^{1/(2p)-1}\|N\|_{S_p}.}
\]
This includes arbitrary finite or infinite rank, all singular-value profiles, and the trace-class endpoint \(p=1\). It is the cost over **all** possible factors, not just the explicit construction below.

## Assumptions and scope

The Schatten class \(S_r(H)\) has norm \(\|T\|_{S_r}=(\operatorname{Tr}|T|^r)^{1/r}\) for \(r<\infty\); \(S_\infty\) denotes bounded operators with the operator norm. The infimum permits any factors in \(S_{2p}(H)\); the ambient dimension is arbitrary and the Hilbert space is complex. The formula gives zero when \(N=0\), attained by zero factors. The nonzero case is proved below. The exponent range does not claim the formula for quasi-Schatten exponents below one or for targets with nilpotency order exceeding two.

## Proof

**1. Explicit attainment.** Write the polar decomposition \(N=U|N|\). Let \(Q=U^*U\) be the source projection and \(P=UU^*\) the final projection. The equation \(N^2=0\) implies \(\overline{\operatorname{ran}N}\perp\overline{\operatorname{ran}N^*}\), hence \(PQ=0\). In particular \(|N|\) is supported on \(Q\) and \(|N^*|=U|N|U^*\) is supported on \(P\). Put
\[
X_0=\tfrac12\bigl(|N^*|^{1/2}-|N|^{1/2}\bigr),
\qquad Y_0=U|N|^{1/2}.
\]
Because \(|N^*|^{1/2}U=U|N|^{1/2}\), and because the two positive square roots have orthogonal supports, direct multiplication gives
\[
X_0Y_0=\tfrac12N,\qquad Y_0X_0=-\tfrac12N,
\qquad [X_0,Y_0]=N.
\]
The nonzero singular values of \(Y_0\) are the square roots of those of \(N\). Those of \(X_0\) are half the same square roots, each occurring **twice**; the orthogonality of \(P,Q\) is essential here. Thus
\[
\|Y_0\|_{S_{2p}}=\|N\|_{S_p}^{1/2},\qquad
\|X_0\|_{S_{2p}}=2^{1/(2p)-1}\|N\|_{S_p}^{1/2},
\]
which proves the upper bound and exhibits an actual minimizer if the lower bound holds.

**2. A sharp square-zero-corner commutator inequality.** Let \(P,Q\) be arbitrary orthogonal projections with \(PQ=0\), and suppose \(W=PWQ\). For \(1\le p<\infty\), write \(p'=p/(p-1)\), taking \(p'=\infty\) at \(p=1\), and let \(q=2p/(2p-1)\). We claim
\[
\tag{1}
\|[W,X]\|_{S_q}\le
2^{1-1/(2p)}\|W\|_{S_{p'}}\|X\|_{S_{2p}}
\]
for \(X\in S_{2p}(H)\) (when \(p=1\), \(W\) may be bounded and need not be compact).

First consider the endpoint \(W\in P\mathcal B(H)Q\), \(X\in S_2\). Relative to \(PH\oplus QH\oplus (P+Q)^\perp H\), the only possibly nonzero blocks of \([W,X]\) are
\[
\begin{array}{lll}
(P,P):WX_{QP},&(P,Q):WX_{QQ}-X_{PP}W,&(P,R):WX_{QR},\\
(Q,Q):-X_{QP}W,&(R,Q):-X_{RP}W.&
\end{array}
\]
With \(a=\|W\|\), the two blocks involving \(X_{QP}\) contribute at most \(2a^2\|X_{QP}\|_2^2\) to the squared Hilbert–Schmidt norm, and the \((P,Q)\) block contributes at most \(2a^2(\|X_{QQ}\|_2^2+\|X_{PP}\|_2^2)\). The other two blocks contribute at most \(a^2\|X_{QR}\|_2^2\) and \(a^2\|X_{RP}\|_2^2\). Summing the orthogonal block energies yields
\[
\tag{2}\|[W,X]\|_{S_2}\le\sqrt2\,\|W\|\,\|X\|_{S_2}.
\]
At the other endpoint, Schatten Hölder and the triangle inequality give
\[
\tag{3}\|[W,X]\|_{S_1}\le2\|W\|_{S_1}\|X\|.
\]
For completeness, here is a direct three-lines interpolation argument for \(1<p<\infty\), first for finite-rank \(W=PWQ\), \(X\), and an arbitrary finite-rank dual test operator \(Z\). Normalize \(\|W\|_{S_{p'}}=\|X\|_{S_{2p}}=\|Z\|_{S_{2p}}=1\) and write their polar decompositions \(W=V_W|W|\), \(X=V_X|X|\), and \(Z=V_Z|Z|\). In the strip \(0\le\operatorname{Re}z\le1\), define
\[
W(z)=V_W|W|^{p'z},\qquad
X(z)=V_X|X|^{p(1-z)},\qquad
Z(z)=V_Z|Z|^{p(1-z)},
\]
with powers defined on the positive singular-value supports and zero on the kernels. These are bounded analytic finite-rank families on the closed strip, and every \(W(z)\) remains in the same corner \(P\mathcal B(H)Q\). At \(\operatorname{Re}z=0\), their norms satisfy
\[\|W(z)\|=\|X(z)\|_{S_2}=\|Z(z)\|_{S_2}=1;\]
at \(\operatorname{Re}z=1\), they satisfy
\[\|W(z)\|_{S_1}=\|X(z)\|=\|Z(z)\|=1.\]
The analytic scalar function \(f(z)=\operatorname{Tr}(Z(z)[W(z),X(z)])\) is bounded by \(\sqrt2\) on the first edge by (2), and by \(2\) on the second edge by (3). The three-lines theorem at \(\theta=1-1/p\), where all three analytic families agree with the original inputs, gives
\[
|\operatorname{Tr}(Z[W,X])|\le (\sqrt2)^{1-\theta}2^\theta
=2^{1-1/(2p)}.
\]
Schatten duality, scaling, and finite-rank approximation in \(S_{p'}\) and \(S_{2p}\) establish (1). For \(p=1\), (1) is exactly (2). The argument remains valid on infinite-dimensional separable Hilbert spaces.

**3. Optimality over arbitrary factors.** Suppose now that \(N\ne0\) and \([X,Y]=N\) for arbitrary \(X,Y\in S_{2p}\). Write \(N=U|N|\) as above and set
\[
W=|N|^{p-1}U^*\quad(p>1),\qquad W=U^*\quad(p=1).
\]
In either case \(W\) maps \(PH\) into \(QH\), so \(W=QWP\) is a square-zero corner operator and inequality (1), with the two projections interchanged, applies. Polar duality gives
\[
\operatorname{Tr}(WN)=\|N\|_{S_p}^p,
\qquad \|W\|_{S_{p'}}=\|N\|_{S_p}^{p-1},
\]
where at \(p=1\) the latter identity means \(\|W\|=1\). The products are trace class by Schatten Hölder, so cyclicity is legitimate and
\[
\begin{aligned}
\|N\|_{S_p}^p
 &=|\operatorname{Tr}(W[X,Y])|
  =|\operatorname{Tr}([W,X]Y)|\\
 &\le\|[W,X]\|_{S_q}\|Y\|_{S_{2p}}\\
 &\le2^{1-1/(2p)}\|N\|_{S_p}^{p-1}
 \|X\|_{S_{2p}}\|Y\|_{S_{2p}}.
\end{aligned}
\]
Dividing by the nonzero power of \(\|N\|_{S_p}\) proves
\[
\|X\|_{S_{2p}}\|Y\|_{S_{2p}}
\ge2^{1/(2p)-1}\|N\|_{S_p}.
\]
This holds for every representation, hence for its infimum; equality is furnished by \(X_0,Y_0\) in step 1. The proof is complete.

## Verification

The included standalone `verify.py` uses only Python's standard library and tests explicit square-zero matrix representatives with multiple independent singular values, seven exponents \(p\) from \(1\) to \(12\), the primal and dual trace identities, the exact cost, and randomly sampled instances of the corner Hilbert–Schmidt estimate (2). Command: `python verify.py`. Its observed result was `PASS 390 finite assertions (factorizations, cost, dual identities, endpoints)`. These checks are finite consistency tests, **not** the proof of (1) in infinite dimensions. The infinite-dimensional argument is the three-lines proof plus Schatten duality and density above.

## Relationship to prior work

Liu and Yang (arXiv:2610.27024v1, first public 2026-10-19) prove a general existence and product bound \(16\zeta(p-1)^{1/p}\|T\|_{S_p}\) for arbitrary \(T\in S_p\) when \(p>2\). Their Theorem 1.1 and Lemma 2.6 do not determine a sharp factor cost, and their general existence range does not include \(p\le2\). This finding determines the **unrestricted sharp infimum** on all square-zero targets and all \(1\le p<\infty\); it makes no claim about arbitrary nonnilpotent targets at \(p\le2\).

Dykema and Krishnaswamy-Usha (arXiv:1706.03465, Proposition 3.1 and Theorem 3.2) treat single-commutator existence and factor-ideal membership for nilpotents, but do not give the exact Schatten factor-product minimum. Marcoux, Radjavi, and Zhang (arXiv:2402.15676) study commutators **of two square-zero factors** and their norm closures, not the minimum Schatten factor cost when the *target* is square-zero. The classical Böttcher–Wenzel Hilbert–Schmidt commutator estimate supplies related sharp two-matrix inequalities and includes a rank-one endpoint comparison, but is not an exact trace-norm factor-cost result for arbitrary-rank targets. The lower estimate here uses a corner-specific Hilbert–Schmidt-to-trace interpolation mechanism.

## Limitations

The theorem assumes \(N^2=0\), is specific to complex Hilbert Schatten classes with \(p\ge1\), and does not characterize all minimizing pairs or mixed-exponent products. Its originality assessment is based on inspected relevant primary texts and mathematical-record searches; a differently phrased prior exact factor-cost formula remains possible. No independent external validation or publication-priority determination has been performed.

## References

1. Z. Liu and S. Yang, *Single commutators in Schatten ideals*, arXiv:2610.27024v1 (2026), https://arxiv.org/html/2610.27024v1, especially Theorem 1.1 and Lemma 2.6.
2. K. Dykema and A. Krishnaswamy-Usha, *Nilpotent elements of operator ideals as single commutators*, arXiv:1706.03465 (2017), https://arxiv.org/abs/1706.03465, Proposition 3.1 and Theorem 3.2.
3. L. W. Marcoux, H. Radjavi and Y. Zhang, *On commutators of square-zero Hilbert space operators*, arXiv:2402.15676 (2024), https://arxiv.org/abs/2402.15676, Introduction and Section 2.
4. D. Chruściński, G. Kimura, H. Ohno and T. Singal, *Bounding the Frobenius norm of a q-deformed commutator*, arXiv:2202.11520 (2022), https://arxiv.org/abs/2202.11520, for background on Hilbert–Schmidt commutator bounds.
