# Sharp Schatten thresholds and a weak endpoint for palindromic language Hankel operators

## Finding
Let \(\Sigma\) be an alphabet with \(q\ge2\) letters, \(W=\Sigma^*\), and \(\varepsilon\) the empty word. Write \(\operatorname{rev}(w)\) for reversal of a word. Define a matrix for each real \(r>0\) by
\[
(H_r)_{u,v}=r^{|u|+|v|}\mathbf{1}_{\{uv=\operatorname{rev}(uv)\}},\qquad u,v\in W.
\]
Consider it initially as an operator from finitely supported inputs, whenever the resulting output belongs to \(\ell^2(W)\). It extends boundedly to \(\ell^2(W)\) exactly for \(r<q^{-1/4}\). In this entire range it is Hilbert--Schmidt, hence compact, and its exact Hilbert--Schmidt norm is
\[
\|H_r\|_{\mathcal{S}_2}^2=\frac{1+2qr^2+qr^4}{(1-qr^4)^2}.
\]
For every \(1\le p<\infty\), its sharp Schatten-class criterion is
\[
H_r\in\mathcal{S}_p\quad\Longleftrightarrow\quad
0<r<\min(q^{-1/4},q^{-1/(2p)}).
\]
At the ideal-critical boundary \(1<p<2\) with \(r=q^{-1/(2p)}\), \(H_r\) remains compact and lies in the weak Schatten class \(\mathcal{S}_{p,\infty}\), but not in \(\mathcal{S}_p\). Here weak membership means \(\sup_{k\ge1}k^{1/p}s_k(H_r)<\infty\), where \(s_k\) are singular values in nonincreasing order. At the boundedness endpoint \(r=q^{-1/4}\), the operator is not bounded; no weak claim is made there or at the trace-class endpoint \(p=1\).

## Assumptions and scope
All Hilbert spaces are complex. The alphabet is finite and has cardinality at least two. A word of length zero is included. \(P_n\) denotes the orthogonal projection from \(\ell^2(W)\) onto the span of words of length \(n\), a space of dimension \(q^n\). The usual Schatten ideals \(\mathcal{S}_p\) are the compact operators whose singular values have summable \(p\)-th powers. The normalization is exactly the one in the displayed matrix, with one factor \(r\) per concatenated letter; changing this factor changes both thresholds.

## Proof
**1. Word-length block singular values.** Fix \(m,n\ge0\) and set \(B_{mn}=P_mH_rP_n\), a rectangular finite matrix. Suppose \(m\ge n\) and write \(d=m-n\). The concatenation \(uv\) of lengths \(m,n\) is a palindrome precisely when \(u=\operatorname{rev}(v)t\) for some palindromic word \(t\) of length \(d\). There are exactly \(q^{\lceil d/2\rceil}\) possibilities for \(t\). For distinct length-\(n\) words \(v\), these length-\(m\) output supports are disjoint. Thus the columns of \(B_{mn}\) are mutually orthogonal, each of Euclidean norm \(r^{m+n}q^{\lceil d/2\rceil/2}\), and all \(q^n\) columns are nonzero. If \(n>m\), the same argument applied to rows gives \(q^m\) nonzero singular values of that size. Consequently, for every \(1\le p<\infty\),
\[
\|B_{mn}\|_{\mathcal{S}_p}
=q^{\min(m,n)/p}r^{m+n}q^{\lceil|m-n|/2\rceil/2}.
\tag{1}
\]
This block identity is exact for all finite \(m,n\), not an asymptotic statement.

**2. Boundedness and the exact Hilbert--Schmidt formula.** The column indexed by \(\varepsilon\) contains \(r^{|u|}\) precisely on palindrome rows. There are \(q^{\lceil j/2\rceil}\) palindromes of length \(j\). Hence its squared output norm equals \(\sum_{j\ge0}q^{\lceil j/2\rceil}r^{2j}\), which diverges exactly when \(qr^4\ge1\). In that case no bounded extension is possible. Conversely, if \(qr^4<1\), each palindrome of total length \(j\) contributes exactly \(j+1\) matrix entries, one per prefix/suffix split, so Tonelli's theorem yields
\[
\begin{aligned}
\|H_r\|_{\mathcal{S}_2}^2
&=\sum_{j=0}^\infty(j+1)q^{\lceil j/2\rceil}r^{2j}\\
&=\frac{1+qr^4}{(1-qr^4)^2}+\frac{2qr^2}{(1-qr^4)^2}\\
&=\frac{1+2qr^2+qr^4}{(1-qr^4)^2}.
\end{aligned}
\]
The square-summable matrix defines a unique Hilbert--Schmidt extension, which is bounded and compact. This proves the sharp boundedness characterization.

**3. Necessary Schatten condition.** If \(H_r\in\mathcal{S}_p\), averaging conjugations by the length-gauge unitaries \(U_\theta|_{P_n\ell^2(W)}=e^{in\theta}I\) projects contractively in \(\mathcal{S}_p\) onto the direct sum \(D=\bigoplus_{n\ge0}B_{nn}\). Since \(uv\) for equal lengths is palindromic exactly when \(u=\operatorname{rev}(v)\), each \(B_{nn}\) is \(r^{2n}\) times a permutation matrix, with \(q^n\) singular values. Thus
\[
\|D\|_{\mathcal{S}_p}^p=\sum_{n\ge0}q^n r^{2pn},
\]
so \(qr^{2p}<1\) is necessary in addition to the boundedness condition from step 2.

**4. Sufficient Schatten condition.** If \(r<\min(q^{-1/4},q^{-1/(2p)})\), then (1) gives the uniform estimate
\[
\|B_{mn}\|_{\mathcal{S}_p}
\le q^{1/4}(q^{1/p}r^2)^{\min(m,n)}(rq^{1/4})^{|m-n|},
\]
because \(q^{\lceil d/2\rceil/2}\le q^{1/4}q^{d/4}\). Both geometric bases are strictly below one, so \(\sum_{m,n\ge0}\|B_{mn}\|_{\mathcal{S}_p}<\infty\). The double block series therefore converges in the Banach ideal \(\mathcal{S}_p\), as \(p\ge1\). On finitely supported vectors the sum agrees with the defining matrix, proving sufficiency.

**5. Nontrivial weak endpoint.** Fix \(1<p<2\), let \(r=q^{-1/(2p)}\), and decompose \(H_r=\sum_{d\in\mathbb Z}H_{r,d}\) by the signed length difference \(d=m-n\). For a fixed \(d\), the blocks occupy mutually orthogonal input and output length spaces. By step 1, the singular values of \(H_{r,d}\) are precisely
\[
b_d q^{-k/p}\quad\text{with multiplicity }q^k,
\qquad k=0,1,\ldots,
\qquad b_d=r^{|d|}q^{\lceil|d|/2\rceil/2}.
\]
Indeed, at this parameter \(q^{1/p}r^2=1\), and the corresponding block is based at minimum word length \(k\). Since \(\sum_{j=0}^k q^j\le q^{k+1}/(q-1)\), the weak singular-value estimate is
\[
\sup_{N\ge1}N^{1/p}s_N(H_{r,d})
\le\bigl(q/(q-1)\bigr)^{1/p} b_d.
\tag{2}
\]
For \(1<p<\infty\), the Ky Fan functional \(\|T\|_{(p,\infty)}=\sup_{N\ge1}N^{1/p-1}\sum_{j=1}^Ns_j(T)\) obeys the triangle inequality, and is at most \(p/(p-1)\) times the left side of (2). Since \(rq^{1/4}=q^{1/4-1/(2p)}<1\), we have \(\sum_{d\in\mathbb Z}b_d<\infty\). Thus finite sums of \(H_{r,d}\) possess a uniformly bounded \(\|\cdot\|_{(p,\infty)}\). Because \(H_r\in\mathcal{S}_2\) and the different length bands have disjoint entries, these finite sums converge in Hilbert--Schmidt norm, hence in operator norm. Pointwise continuity of singular values under norm convergence passes the Ky Fan bound to \(H_r\), proving weak \(\mathcal{S}_p\) membership. But step 3 gives \(\sum_n q^n r^{2pn}=\sum_n1=\infty\); therefore \(H_r\notin\mathcal{S}_p\).

## Verification
A standalone finite checker `palindrome_schatten_check.py` enumerates word-length blocks and independently computes their singular values with numerical linear algebra; it also checks finite Hilbert--Schmidt sums against the exact infinite rational expression. It passes for alphabet sizes \(q=2\), \(q=3\) and the stated finite cutoffs. These computations corroborate but do not replace the five analytic steps above. The sharpness at every infinite-dimensional endpoint comes from the explicit divergent column or diagonal-pinch series, not from finite experiments.

## Relationship to prior work
Hristov, Ilchev, Nedelcheva and Zlatanov (2026), Section 8, consider the **unweighted** Boolean Hankel matrix of any formal language as an operator from \(\ell^1(W)\) into \(\ell^\infty(W)\); they establish a regularity/compactness dichotomy and approximation-number bounds. This is the source of the natural language-Hankel setup, but their operator, its norms and conclusions differ. The present theorem fixes a nonregular palindrome language and studies a **length-weighted Hilbert-space realization**, where compactness is restored and ideal membership changes sharply with \(q\), \(r\), and \(p\). Abusaksaka and Partington (2017) analyze weighted Hankel *integral* operators associated with diffusive systems on a continuous half-line; those conditions neither include free-monoid word reversal nor establish these exact block multiplicities or thresholds. A check of indexed nearby operator-ideal results found no statement known to imply this combined sharp classification. This is not a proof of historical priority.

## Limitations
The statements concern this one canonical palindrome language on finite alphabets; they do not classify all context-free languages. No exact individual singular-value asymptotics for the full operator are claimed, nor a weak \(\mathcal{S}_1\) endpoint. The matrix may be non-selfadjoint. Classification depends on the precise length-weighted normalization. An unindexed result about weighted Hankel matrices on free monoids could potentially cover part of the theorem. Independent validation has not been performed.

## References
1. M. Hristov, A. Ilchev, D. Nedelcheva, B. Zlatanov, *Banach Spaces Generated by Finite-Valued Functions: Superreflexive Rigidity, Hankel Operators, and Universality*, arXiv:2608.15185v1 (first posted 2026-08-15), especially Section 8.
2. A. B. Abusaksaka, J. R. Partington, *Diffusive Systems and Weighted Hankel Operators*, arXiv:1704.00518v1 (2017), especially the treatment of integral Hankel ideals.
