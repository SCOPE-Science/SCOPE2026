# One-block contractivity and sharp binary amplification of two-block Lorentz averages

## Finding
For every \(1<p<\infty\) and \(0<q<1\), let \(X_{p,q}\) be the real or complex Lorentz sequence space with its **power-normalized gauge**
\[
\|x\|_{p,q}=\left[\sum_{k\ge1}\big(k^{q/p}-(k-1)^{q/p}\big)(x_k^*)^q\right]^{1/q},
\]
where \((x_k^*)\) is the nonincreasing rearrangement of \((|x_k|)\). In particular, an indicator of any \(m\) coordinates has norm exactly \(m^{1/p}\).

Let \(V_B\) replace the coordinates on a nonempty finite set \(B\) by their arithmetic average and set all other coordinates to zero. Let \(B,C\) be disjoint sets of cardinality \(n\), and put \(P_n=V_B+V_C\).

**Theorem.** (i) Every \(V_B\) has exact operator quasi-norm \(\|V_B\|=1\). (ii) Define \(M_n^{\mathrm{bin}}\) as the maximum of \(\|P_nx\|_{p,q}/\|x\|_{p,q}\) over nonzero binary vectors supported on \(B\cup C\). Set \(A_{p,q}=2^{q/p}-1\). Then
\[
\lim_{n\to\infty}M_n^{\mathrm{bin}}=R_{p,q}:=\max_{0\le t\le1}\frac{(1+A_{p,q}t^q)^{1/q}}{(1+t)^{1/p}}>1.
\]
There is a unique maximizer \(t_{p,q}\in(0,1)\), the first positive root of
\[
A_{p,q}t^{q-1}\big[p+(p-1)t\big]=1.
\]
Consequently \(\liminf_{n\to\infty}\|P_n\|\ge R_{p,q}>1\). Thus one averaging block never expands this gauge, but two equal-sized blocks expand it for all sufficiently large block sizes.

(iii) The binary amplification has sharp singular endpoint laws
\[
\lim_{q\downarrow0}R_{p,q}=2^{1/p},
\]
and, as \(q\uparrow1\) with \(p>1\) fixed, writing
\[
B_p=p(2^{1/p}-1)\in(0,1),\qquad
\kappa_p=\frac{\log2}{p}\frac{2^{1/p}}{2^{1/p}-1},
\]
we have
\[
t_{p,q}\sim e^{-\kappa_p}B_p^{1/(1-q)},\qquad
R_{p,q}-1\sim \frac{1-q}{p}\,e^{-\kappa_p}B_p^{1/(1-q)}.
\]
These are statements about binary inputs; no equality between \(R_{p,q}\) and the unrestricted two-block operator norm is asserted.

## Assumptions and scope
The parameters satisfy \(p\in(1,\infty)\), \(q\in(0,1)\), and all coordinate sets are finite. The scalar field is real or complex. The gauge above has decreasing positive weights and fundamental function exactly \(m^{1/p}\). It is a standard equivalent **normalization** of the classical Lorentz space \(\ell_{p,q}\), not the only possible Lorentz quasi-norm. Exact contractivity is gauge-dependent and is asserted only in this displayed normalization. The projection \(V_B\) is supported on \(B\); it does not preserve coordinates outside \(B\). The two-block projection has support \(B\cup C\) and is defined for each \(n\) separately. In the binary optimization the entries are exactly zero or one, not arbitrary real or complex amplitudes.

## Proof
**One-block contractivity.** Let \(m=|B|\), let \(a_1\ge\dots\ge a_m\ge0\) list \((|x_i|)_{i\in B}\), and put \(S=\sum_i a_i\). If \(S=0\), the claim is trivial. Write \(a_{m+1}=0\). The ordered vector \((a_i)\) is a convex combination of the \(m\) ordered vectors \((S/j)\mathbf1_{\{1,\dots,j\}}\), with coefficients \(\lambda_j=j(a_j-a_{j+1})/S\). They are nonnegative and sum to one. The function \(F(a)=\sum_{i=1}^m w_i a_i^q\), where \(w_i=i^{q/p}-(i-1)^{q/p}>0\), is concave on the nonnegative orthant because \(0<q<1\). Hence
\[
\sum_{i=1}^m w_i a_i^q\ge\min_{1\le j\le m}S^qj^{q/p-q}=S^qm^{q/p-q}.
\]
The full-vector rearrangement can only raise the Lorentz gauge relative to the selected coordinates. On the other hand, \(V_Bx\) has \(m\) entries equal in modulus to at most \(S/m\), so
\[
\|V_Bx\|_{p,q}\le(S/m)m^{1/p}\le\|x\|_{p,q}.
\]
Taking \(x=\mathbf1_B\) gives equality and \(\|V_B\|=1\).

**Exact binary restriction.** Let the input have \(k\) ones on \(B\) and \(j\) ones on \(C\). By symmetry interchange the blocks so that \(0\le j\le k\le n\); the zero input is excluded. The input norm is \((k+j)^{1/p}\). The output has \(n\) entries \(k/n\) and \(n\) entries \(j/n\). Telescoping the weights at ranks \(n\) and \(2n\) gives
\[
\frac{\|P_nx\|_{p,q}}{\|x\|_{p,q}}
=\left(\frac{k}{n}\right)^{1-1/p}
\frac{\big(1+(2^{q/p}-1)(j/k)^q\big)^{1/q}}{(1+j/k)^{1/p}}.
\]
The prefactor is at most one, proving \(M_n^{\mathrm{bin}}\le R_{p,q}\). Conversely take \(k=n\) and \(j/n\) converging to an arbitrary \(t\in[0,1]\). Continuity gives the matching lower limit and the exact formula for \(\lim M_n^{\mathrm{bin}}\). Since the ordinary operator norm dominates its restriction to binary inputs, the bound on \(\liminf\|P_n\|\) follows.

**Strict expansion and uniqueness.** Put \(\rho(t)=(1+A_{p,q}t^q)^{1/q}/(1+t)^{1/p}\). Then \(\rho(0)=\rho(1)=1\), while
\[
\log\rho(t)=\frac{A_{p,q}}q t^q-\frac tp+o(t^q)>0
\quad(t\downarrow0).
\]
For \(0<t<1\), the sign of \(d\log\rho(t)/dt\) is the sign of
\[
H(t)=A_{p,q}t^{q-1}\big[p+(p-1)t\big]-1.
\]
The derivative of \(H\) has the sign of \(p(q-1)+q(p-1)t\), which changes at most once, from negative to positive. Thus \(H\) first decreases and can subsequently increase; there are at most two roots, and the first is a local maximum of \(\rho\). Since \(\rho\) exceeds one near zero but equals one at both endpoints, the first root exists and gives the **unique global maximum**. A possible second root is a minimum; it cannot give a competing maximum. Taking a sufficiently fine integer grid \(j/n\) yields a strict two-block expansion for all sufficiently large \(n\).

**Small-\(q\) limit.** Since \(t\le1\), we have \(\rho(t)\le(1+A_{p,q})^{1/q}=2^{1/p}\). For the test \(t=q\), \(q^q\to1\), \((1+A_{p,q}q^q)^{1/q}\to2^{1/p}\), and \((1+q)^{1/p}\to1\). This matches the upper bound.

**Near-convex limit.** Set \(\eta=1-q\). Strict concavity of the power function gives \(0<B_p<1\). Since \(H(t)\) at \(q=1\) is negative for all sufficiently small *fixed* positive \(t\), the first zero \(t_{p,q}\) tends to zero as \(q\uparrow1\). Its equation is
\[
t_{p,q}^{\eta}=pA_{p,q}\left[1+\frac{p-1}{p}t_{p,q}\right].
\]
Here \(\log(pA_{p,q})=\log B_p-\eta\kappa_p+O(\eta^2)\). The equation first bounds \(t_{p,q}\) exponentially, so \(t_{p,q}=o(\eta)\). Taking logs then gives
\[
\log t_{p,q}=\frac{\log B_p}{\eta}-\kappa_p+o(1).
\]
At this critical point, \(A_{p,q}t_{p,q}^q=t_{p,q}/[p+(p-1)t_{p,q}]\). Thus Taylor expansion, using \(t_{p,q}=o(\eta)\), gives
\[
\log R_{p,q}=\frac{\eta}{pq}t_{p,q}+O(t_{p,q}^2)
\sim\frac\eta p t_{p,q}.
\]
Exponentiating yields the claimed second asymptotic law.

## Verification
The included stand-alone Python file `CHECK.py` computes the displayed Lorentz gauge and the binary ratio independently, verifies the single-block inequality on finite random samples, checks the exact binary formula over finite counts and several parameter pairs, and tests stationary points and endpoint consistency. Executing `python3 CHECK.py` with the standard library produces the recorded `PASS finite checks: 42704`. This is finite numerical evidence only. The proof above establishes the infinite-dimensional and all-parameter claims analytically; the checker does not certify infinite ranges or originality.

## Relationship to prior work
Albiac–Ansorena–Berasategui, arXiv:2605.11295v1 (public May 11, 2026), establish uniform boundedness of **all** disjoint-block averaging projections on nonlocally convex \(\ell_{p,q}\), including the stated parameter range; see their Theorem 3.13. Their §3 permits the weighted Lorentz gauge with power-difference weights used here. This result instead isolates the exact one-block contractivity threshold, the sharp *binary-input* amplification for two equal blocks, and its endpoint phase scales. Mere boundedness of the general family neither states nor implies the coefficient-one versus coefficient-greater-than-one distinction in a given equivalent gauge. Classical conditional-expectation contractivity results in locally convex \(L^p\) and Banach rearrangement-invariant spaces use distinct hypotheses and do not give the nonlocally convex two-block binary profile. Published records concerning norms of other kinds of coordinate projections and mixing of \(L^p\) conditional expectations do not yield the result by specialization.

## Limitations
The sharp quantity \(R_{p,q}\) is the limit of an **input-restricted** maximum. The unrestricted operator norms \(\|P_n\|\) may be larger, and their sharp supremum or limit is not determined. The theorem is sensitive to Lorentz quasi-norm normalization and does not assert coefficient-one contractivity for every equivalent Lorentz gauge. It covers only the classical power-fundamental scale with \(1<p<\infty\), \(0<q<1\); other weights, multiple-block optimum, and quantitative rates in \(n\) are open here. Published-priority assessment remains provisional; a more general rearrangement-invariant projection theorem with hidden exact constants is a residual risk. No independent audit has been performed.

## References
1. F. Albiac, J. L. Ansorena, and M. Berasategui, *Boundedness of the averaging projections in nonlocally convex Lorentz sequence spaces and applications to basis theory*, arXiv:2605.11295v1, publicly submitted May 11, 2026. https://arxiv.org/html/2605.11295 ; https://arxiv.org/abs/2605.11295 . Theorem 3.13, equations (3.1) and (3.4), and §3.2.
2. E. Shargorodsky and T. Sharia, *Sharp estimates for conditionally centered moments and for compact operators on \(L^p\) spaces*, *Mathematische Nachrichten* 296 (2023), 368–381, DOI 10.1002/mana.202100217, open access https://onlinelibrary.wiley.com/doi/full/10.1002/mana.202100217 . Section 2 describes conditional-expectation contraction in Banach function spaces.
3. T. Ando, *Contractive projections in \(L^p\) spaces*, *Pacific Journal of Mathematics* 17 (1966), 391–405, DOI 10.2140/pjm.1966.17.391 (bibliographic comparison only).
