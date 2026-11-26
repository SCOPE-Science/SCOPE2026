# Sharp uniform Bernoulli approximation for the nilpotency-index defect of restricted-range maps

## Finding

Fix a prime power \(q\). Let \(V\) be a \((k+c)\)-dimensional vector space over \(\mathbb F_q\) with a fixed \(k\)-dimensional subspace \(W\), where \(k,c\ge1\). Choose \(X\) uniformly among the nilpotent linear maps \(V\to V\) whose images lie in \(W\). Write \(\nu(X)=\min\{j\ge1:X^j=0\}\) and \(D_{k,c}=k+1-\nu(X)\), the defect from the maximum possible index. Set
\[
\varphi_s(q)=\prod_{i=1}^s(1-q^{-i}),\qquad K_q=\prod_{i=2}^{\infty}(1-q^{-i}),\qquad \varphi_0(q)=1.
\]
Let \(S_q\) and \(E_c\) be independent, with
\[
\Pr(S_q=s)=K_q\frac{q^{-2s}}{\varphi_s(q)}\quad(s\ge0),\qquad
\Pr(E_c=1)=q^{-c},\quad\Pr(E_c=0)=1-q^{-c}.
\]
Using total variation distance \(d_{\rm TV}(P,Q)=\sup_A|P(A)-Q(A)|\), for every \(k,c\ge1\) one has
\[
\frac{K_q(1-q^{-1})}{q}\,q^{-k}
\;\le\;d_{\rm TV}\!\left(\mathcal L(D_{k,c}),\mathcal L(S_q+E_c)\right)
\;\le\;\frac{q^2}{(1-q^{-1})(1-q^{-2})}\,q^{-k}.
\]
Thus the approximation error has exact order \(q^{-k}\) at fixed field size, uniformly in all positive codimensions. In particular, fixed \(c\) gives the indicated Bernoulli-shifted limit, and if \(c=c(k)\to\infty\), the unshifted law \(S_q\) approximates \(D_{k,c(k)}\) with error at most the displayed upper bound plus \(q^{-c(k)}\).

## Assumptions and scope

All dimensions, matrices and ranks are over \(\mathbb F_q\), with every characteristic permitted. The sampling is uniform on the nilpotent subset of the entire restricted-range semigroup, with no regularity restriction. The theorem concerns only the nilpotency index, with \(\nu(0)=1\). The target law is allowed to vary with \(c\); the error estimate does not assume that \(c\) is fixed or tends to infinity. The rate constants depend on \(q\); the theorem does not assert a leading asymptotic constant for the error.

## Proof

**Block restriction and fibres.** Choose a complement to \(W\). Then \(X=\begin{pmatrix}A&B\\0&0\end{pmatrix}\) with \(A\) of size \(k\) and \(B\) of size \(k\times c\). For \(j\ge1\), the two upper blocks of \(X^j\) are \(A^j\) and \(A^{j-1}B\). Thus \(X\) is nilpotent exactly when \(A\) is, and in the uniform nilpotent ensemble \(A\) is uniform nilpotent and \(B\) is independent and uniform. If the largest Jordan block of \(A\) has size \(d\) and multiplicity \(r\), then \(A^{d-1}\) has rank \(r\), even for \(A=0\), where \(d=1\) and \(r=k\). The index of \(X\) is \(d\) with probability \(q^{-rc}\), since the columns of \(B\) must all lie in \(\ker(A^{d-1})\), and is otherwise \(d+1\). In particular the maximum is \(k+1\), attained by taking a single block in \(A\) and a column not killed by \(A^{k-1}\).

For reference, the classical multiplicity of a nilpotent Jordan type \(\lambda\vdash k\) is \(N_\lambda=|\operatorname{GL}_k(\mathbb F_q)|/C_\lambda\), with
\[
C_\lambda=q^{\sum_i(\lambda'_i)^2}\prod_j\varphi_{m_j(\lambda)}(q),
\]
where \(\lambda'\) is the conjugate partition and \(m_j\) is the multiplicity of part \(j\). The block argument consequently gives the finite count by summing \(N_\lambda q^{kc-rc}\) at index \(d\) and \(N_\lambda(q^{kc}-q^{kc-rc})\) at index \(d+1\). These finite counts are used as inputs to the asymptotic comparison, not claimed as a new enumerative theorem.

**Exact masses near the maximum.** Write \(K_{q,k}=\prod_{i=2}^k(1-q^{-i})\). When \(0\le 2s<k\), a partition with largest part \(k-s\) is uniquely \(\lambda=(k-s,\mu)\) with \(\mu\vdash s\), and that largest part is unique. Squaring the conjugate column lengths gives
\[
\sum_i(\lambda'_i)^2=k+s+\sum_i(\mu'_i)^2,\qquad C_\lambda=q^{k+s}(1-q^{-1})C_\mu.
\]
The classical nilpotent-matrix counts in dimensions \(j\) are \(q^{j^2-j}\), so \(\sum_{\mu\vdash s}C_\mu^{-1}=q^{-s}/\varphi_s(q)\) by orbit-stabilizer. This includes the empty partition in dimension zero. Using \(|\operatorname{GL}_k|=q^{k^2}\varphi_k(q)\) and dividing by \(q^{k^2-k}\) for the uniform nilpotent \(A\) gives
\[
\Pr(k-\nu(A)=s)=K_{q,k}q^{-2s}/\varphi_s(q)\qquad(2s<k).
\]
For \(D_{k,c}=s\) either the largest-block defect of \(A\) is \(s\) and the index is extended by one, or its defect is \(s-1\) and the index remains unchanged. In either case the largest block is unique in the stated range, so the probability of no extension is \(q^{-c}\), regardless of the smaller blocks. The exact near-maximum masses are therefore
\[
\Pr(D_{k,c}=s)=K_{q,k}\left((1-q^{-c})\frac{q^{-2s}}{\varphi_s(q)}+
\mathbf1_{s\ge1}q^{-c}\frac{q^{-2(s-1)}}{\varphi_{s-1}(q)}\right),\qquad 2s<k.
\]

**Uniform total variation and sharpness.** The law of \(S_q\) is normalized by the power series \(G(z)=\sum_{s\ge0}z^s/\varphi_s(q)\), which obeys \((1-z)G(z)=G(z/q)\) by comparing coefficients. For \(|z|<1\), iteration gives \(G(z)=\prod_{j\ge0}(1-zq^{-j})^{-1}\). Taking \(z=q^{-2}\) gives \(G(z)=K_q^{-1}\), and \(K_q>0\) since the sum of the omitted factors' deficits is finite.

Put \(h=\lfloor(k-1)/2\rfloor\) and \(P=\mathcal L(D_{k,c})\), \(Q=\mathcal L(S_q+E_c)\). At every integer \(0\le s\le h\), the finite mass formula gives \(P(s)=(K_{q,k}/K_q)Q(s)\ge Q(s)\). The identity \(d_{\rm TV}(P,Q)=1-\sum_s\min(P(s),Q(s))\) then yields
\[
d_{\rm TV}(P,Q)\le Q\{s>h\}\le \Pr(S_q\ge h)\le \frac{q^{-2h}}{(1-q^{-1})(1-q^{-2})}.
\]
The second inequality uses \(E_c\le1\). The third uses \(\varphi_s(q)\ge(1-q^{-1})K_q\) and a geometric sum. Since \(2h\ge k-2\), this gives the claimed upper bound even for \(k=1\).

For a matching lower order uniformly in \(c\), use the event \(D_{k,c}=0\). Its excess probability over \(Q(0)\) is \((K_{q,k}-K_q)(1-q^{-c})\). The product identity \(K_{q,k}/K_q=\prod_{i>k}(1-q^{-i})^{-1}\ge (1-q^{-(k+1)})^{-1}\) and \(1-q^{-c}\ge1-q^{-1}\) give the stated lower bound. Finally \(S_q+E_c\) and \(S_q\) can be coupled by using the same \(S_q\); they disagree with probability \(q^{-c}\), yielding the claim for growing codimension.

## Verification and limitations

The accompanying `verify.py` compares the finite index counts with direct matrix powers over small fields of orders 2, 3, 4 and 5, including the zero map. Run with standard Python 3. These checks address the finite block-counting input. They do not test the infinite product approximation or establish its sharp rate. The upper rate follows from the exact-mass prefix and its complementary tail; the lower rate already follows from the single maximum-index event. No ambient Jordan classification or asymptotic leading constant in total variation is claimed.

## Relationship to prior work

The finite Jordan-type counts for this restricted-range family are a consequence of classical Hall-polynomial counts, including in arbitrary codimension. For a nilpotent Jordan type \(\eta\) on \(V\), the condition \(X(V)\subseteq W\) says that \(W\) is a submodule with quotient of type \((1^c)\). For each restriction type \(\lambda\) on \(W\), the Hall number \(g_{(1^c),\lambda}^{\eta}(q)\) counts these submodules for one operator of type \(\eta\). Multiplying by the unrestricted count of operators of that type and dividing by the number of \(k\)-planes gives the count for fixed \(W\), by transitivity on the Grassmannian. The largest part \(\eta_1\) is the index. For \(c=1\) there is also the affine cycle-index route: swapping the two blocks and transposing \(I+X\) gives a unipotent matrix in the point-stabilizer realization of the finite affine group. Neither the existence of finite counts nor the one-column case is claimed as new. The assertion here is instead a uniform stochastic approximation with sharp exponential order in \(k\). The proof identifies the Bernoulli contribution in the unique-longest-block range and uses the resulting mass comparison to bound total variation from above and below. Related calculations for lifts over finite dual-number rings concern an index that can double, with a different perturbation mechanism.

## References

1. I. G. Macdonald, *Symmetric Functions and Hall Polynomials*, 2nd ed., Oxford University Press, 1995, Chapter II §§2, 4, especially (4.3) and (4.6).
2. J. Fulman, *Finite Affine Groups: Cycle Indices, Hall–Littlewood Polynomials, and Probabilistic Algorithms*, arXiv:math/0009182, Theorem 2 and Corollary 1. https://arxiv.org/abs/math/0009182
3. J. Fulman and R. Guralnick, *Cohen Lenstra Partitions and Mutually Annihilating Matrices over a Finite Field*, arXiv:2111.09433, §3, for classical Jordan counts. https://arxiv.org/abs/2111.09433
