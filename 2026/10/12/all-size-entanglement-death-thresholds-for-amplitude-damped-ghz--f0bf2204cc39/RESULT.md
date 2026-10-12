# All-size entanglement-death thresholds for amplitude-damped GHZ states with intermediate partial NOT gates

## Finding
For any integer \(n\ge2\), any \(1\le m\le n-1\), any nonzero GHZ amplitudes, and two stages of identical, independent amplitude damping, the genuine multipartite concurrence of the state after an intermediate local NOT gate on exactly \(m\) qubits is given by one explicit binomial sum. The expression produces a strictly monotone *normalized concurrence deficit*, implying a unique sudden-death time whenever finite-time death occurs. It also yields, for each fixed \(n,m\) and amplitude ratio, a unique critical **first-stage damping probability** separating survival throughout every incomplete second damping stage from finite-stage sudden death.

Write \(a=|\alpha|>0\), \(b=|\beta|>0\), \(a^2+b^2=1\), \(0<p<1\), \(q=1-p\), and \(r=1-p'\in(0,1]\), where \(p'\) is second-stage damping probability. Set
\[
A(r)=(1-pr)^m(1-qr)^{n-m},\qquad
B_k(r)=(1-pr)^k(1-r)^{m-k}\quad (0\le k<m),
\]
\[
R_{n,m}(p,r)=\frac ba\left(\frac pq\right)^{m/2}
\left[(2^{n-1}-2^m)\sqrt{A(r)}+
\sum_{k=0}^{m-1}\binom mk
\sqrt{A(r)+\frac{a^2}{b^2p^k}B_k(r)}\right].
\]
Then the exact genuine multipartite concurrence is
\[
\boxed{C_{n,m}(p,p')=2ab(qr)^{n/2}\max\{0,1-R_{n,m}(p,r)\}.}
\]
The function \(r\mapsto R_{n,m}(p,r)\) is strictly decreasing on \([0,1]\), with endpoints
\[
R_{n,m}(p,1)=(2^{n-1}-1)\frac ba p^{n/2},
\]
\[
R_{n,m}(p,0)=\frac1{q^{m/2}}\left[
\frac ba(2^{n-1}-2^m)p^{m/2}+
\sum_{k=0}^{m-1}\binom mk p^{(m-k)/2}
\sqrt{1+\frac{b^2}{a^2}p^k}\right]=:F_{n,m}(p).
\]
For fixed \(n,m,a,b\), \(F_{n,m}\) increases strictly and continuously from zero to infinity as \(p\) goes from zero to one. Therefore exactly one \(p_c\in(0,1)\) satisfies \(F_{n,m}(p_c)=1\). For \(0<p\le p_c\), concurrence remains positive for every \(0\le p'<1\). For \(p>p_c\) and \(R_{n,m}(p,1)<1\), exactly one finite \(p'_c\in(0,1)\) makes concurrence vanish; after that it remains zero. If \(R_{n,m}(p,1)\ge1\), concurrence has already vanished before the second stage begins. Equality \(F_{n,m}(p)=1\) means death only in the complete-damping limit \(p'\uparrow1\), never at finite \(p'<1\).

For every fixed \(m\ge1\), fixed positive amplitudes, and \(n\to\infty\) through \(n\ge m+1\), the critical first-stage probability has the sharp scaling
\[
\boxed{p_c(n,m,a,b)\sim\left(\frac ab\right)^{2/m}2^{-2(n-1)/m}.}
\]
In particular the leading rare-initial-loss budget is exponentially sensitive to the number of sites receiving intermediate NOT operations.

## Assumptions and scope
Start with the pure \(n\)-qubit state \(\alpha|0\rangle^{\otimes n}+\beta|1\rangle^{\otimes n}\). Every qubit first undergoes independent amplitude damping with Kraus operators \(K_0=\operatorname{diag}(1,\sqrt q)\) and \(K_1=\sqrt p\,|0\rangle\langle1|\). A fixed subset \(S\) of \(m\) sites receives \(X\) gates, after which every site independently undergoes amplitude damping with excited-state survival probability \(r\). The same \(X\) gates may be applied afterward to restore the original basis; being local unitary, this does not change concurrence. Both stages are Markovian, gates are ideal and instantaneous, and channels act independently across sites. The state has exactly one complement-pair coherence and hence lies in the \(n\)-qubit X family. We use the convex-roof genuine multipartite concurrence whose exact X-state formula was proved by Hashemi Rafsanjani et al. The permutation-symmetric channel implies dependence only on \(m=|S|\), not the locations of the flips.

## Proof
**Step 1: exact populations and coherence.** Work just before the optional final \(X\) restoration. If a bit string \(x\) has \(k\) ones on \(S\) and \(\ell\) ones on its complement, its diagonal entry is \(D_x=U_x+V_x\), with
\[
U_x=a^2\,\mathbf1_{\{x\subseteq S\}}r^k(1-r)^{m-k},\qquad
V_x=b^2(pr)^k(1-pr)^{m-k}(qr)^\ell(1-qr)^{n-m-\ell}.
\]
The first term comes from the initial vacuum branch, which becomes \(|S\rangle\) after the flips. The second comes from the initially fully excited branch, which independently occupies sites of \(S\) with probability \(pr\) and sites outside \(S\) with probability \(qr\) after the two damping stages. The only off-diagonal entry is between complementary words \(S\) and \(S^c\), of modulus \(z=ab(qr)^{n/2}\). This follows directly from the two no-jump coherence multipliers.

**Step 2: complement-pair count.** The X-state concurrence theorem gives
\[
C=2\max\left\{0,z-\sum_{\{x,\bar x\}\ne\{S,S^c\}}\sqrt{D_xD_{\bar x}}\right\}.
\]
Every pair excluding the coherent pair has at most one member supported inside \(S\) because \(m<n\). Exactly \(2^m-1\) complementary pairs have such a proper-subset member; with exactly \(k\) occupied sites there are \(\binom mk\) such pairs, \(0\le k<m\). The remaining \(2^{n-1}-2^m\) pairs have \(U_x=U_{\bar x}=0\). For the latter,
\[
\sqrt{V_xV_{\bar x}}=b^2p^{m/2}q^{(n-m)/2}r^{n/2}\sqrt{A(r)}.
\]
For a proper-subset member with \(k\) ones the same product becomes
\[
\sqrt{D_xD_{\bar x}}=
 b^2p^{m/2}q^{(n-m)/2}r^{n/2}
 \sqrt{A(r)+\frac{a^2}{b^2p^k}B_k(r)}.
\]
Dividing the pair sum by \(z=ab(qr)^{n/2}\), summing multiplicities, and applying the X-state formula proves the displayed expression for \(C_{n,m}\).

**Step 3: monotonicity and the unique death boundary.** Every factor of \(A(r)\) is positive and strictly decreasing for \(0\le r\le1\), because \(0<p,q<1\). Each \(B_k(r)\), \(k<m\), is nonnegative and nonincreasing, including at the endpoints. Thus every term under the positive square roots is strictly decreasing in \(r\). All coefficients are nonnegative (since \(m\le n-1\)); hence \(R_{n,m}(p,r)\) is strictly decreasing. Evaluating at \(r=1\) gives \((2^{n-1}-1)(b/a)p^{n/2}\); evaluating at \(r=0\) and factoring each radical gives \(F_{n,m}(p)\). For \(p\in(0,1)\), all terms in the square brackets defining \(F_{n,m}\) are nonnegative and nondecreasing, and the terms indexed by \(k<m\) are strictly increasing. The prefactor \((1-p)^{-m/2}\) also increases; this proves strict monotonicity of \(F_{n,m}\). Its endpoints are zero and infinity. The intermediate value theorem proves the unique \(p_c\). Strict monotonicity in \(r\), together with the endpoint values, yields precisely the three concurrence-death alternatives above.

**Step 4: large-system budget.** Fix \(m,a,b\) and let \(p= c\,2^{-2(n-1)/m}\) with fixed \(c>0\). The \((2^{n-1}-2^m)p^{m/2}\) term of \(F_{n,m}\) tends to \((b/a)c^{m/2}\); each of the finitely many \(k<m\) terms is bounded by a constant times \(p^{(m-k)/2}\) and tends to zero; the denominator tends to one. Therefore \(F_{n,m}(p)\to(b/a)c^{m/2}\). Strict monotonicity brackets the unique crossing for any \(c\) slightly above and below \((a/b)^{2/m}\), proving the claimed asymptotic equivalence.

## Verification
The standalone `verify.py` evaluates the full \(2^n\times2^n\) density matrix using explicit tensor-product Kraus operators independently of the closed formula, computes every complementary diagonal pair, and checks the X-state concurrence expression. Its finite tests cover all \(2\le n\le6\), all \(1\le m<n\), five nonzero first-stage damping values and four second-stage survival values, with additional monotonicity and zero-pre-damping boundary checks. Run with `python verify.py` after installing `numpy` from `requirements.txt`. The supplied finite verification returns `VERIFY_OK 390`; the exact all-size assertion and asymptotic scaling are proved by the preceding algebra, not inferred from finite tests.

For the equal-amplitude five-qubit state and first-stage damping \(p=0.03\), the endpoint deficits at \(p'=1\) are approximately \(2.7107916051\) for \(m=1\), \(0.7773137356\) for \(m=2\), \(0.6909658104\) for \(m=3\), and \(0.9515118770\) for \(m=4\). These produce one finite-time death for a single intermediate flip but no finite second-stage death for any of two, three, or four intermediate flips. They are direct consequences of the stated theorem, not a separate optimization claim.

## Relationship to prior work
Abhignan, Sundararaman, Pragash, Srikanth, and Singh (2026) introduce the two-stage damping and local-NOT protocol, derive explicit concurrence dynamics for \(n=2,3,4\), discuss the initial-undamped arbitrary-\(n\) case, and show numerical strategy tables in Appendix V.1. Those protocol ideas, small-size cases, and numerical observations are prior work. The present result evaluates the general \(0<p<1\), \(1\le m<n\), arbitrary-\(n\) complementary-pair sum and proves the associated sharp monotone global phase boundary and large-\(n\) first-stage budget. Hashemi Rafsanjani et al. (2012) provide the general X-state concurrence theorem and earlier single-stage GHZ consequences; the X-state theorem itself is not new. Hashemi Rafsanjani and Eberly (2015) analyze coherent control of a distinct Jaynes–Cummings multipartite system; that mechanism is not a two-stage independent amplitude-damping channel with intermediate bit flips.

## Limitations
The exact result assumes identical local amplitude damping at each stage and a pure two-branch GHZ input with nonzero amplitudes; the proper nonempty flip masks satisfy \(1\le m<n\). It does not optimize concurrence magnitude at every intermediate time, teleportation fidelity, gate timing cost, or robustness to control imperfections and correlated environments. The second-stage completely damped endpoint always has zero concurrence; survival means positivity at every **incomplete** second-stage damping level. The earlier 2012 X-state theorem is essential and the new claims do not assert an independent general concurrence theorem. Literature priority remains subject to possible earlier unindexed equivalent specializations.

## References
1. V. Abhignan, R. Sundararaman, S. Pragash M, R. Srikanth, and A. Singh, *Decoherence Mitigation with Local NOT Gates in Multipartite Systems*, arXiv:2604.23556v1 (first posted 26 April 2026), https://arxiv.org/html/2604.23556v1. Sections III.1.2–III.1.5, V.1–V.2.
2. S. M. Hashemi Rafsanjani, M. Huber, C. J. Broadbent, and J. H. Eberly, *Genuinely Multipartite Concurrence of N-qubit X-matrices*, arXiv:1208.2706v2 (2012), https://arxiv.org/abs/1208.2706.
3. S. M. Hashemi Rafsanjani and J. H. Eberly, *Coherent control of multipartite entanglement*, arXiv:1408.2087v2 (2015), https://arxiv.org/abs/1408.2087.
